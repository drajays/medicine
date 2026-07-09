#!/usr/bin/env python3
"""Normalize PaddleOCR LaTeX/math artifacts in endo JSON text fields."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")

TEXT_KEYS = ("question", "stem", "text", "explanation", "assertion", "reason", "statement", "title")
LIST_KEYS = ("options",)


def unwrap_latex_cmds(s: str) -> str:
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"\\mathrm\{([^{}]*)\}", r"\1", s)
        s = re.sub(r"\\text\{([^{}]*)\}", r"\1", s)
        s = re.sub(r"\\textbf\{([^{}]*)\}", r"\1", s)
        s = re.sub(r"\\operatorname\{([^{}]*)\}", r"\1", s)
    return s


def collapse_spaced_letters(s: str) -> str:
    """P o t a s s i u m → Potassium; m E q → mEq."""

    def repl(m: re.Match[str]) -> str:
        return m.group(0).replace(" ", "")

    return re.sub(r"(?:[A-Za-zμ] ){2,}[A-Za-zμ]", repl, s)


def clean_latex_inner(s: str) -> str:
    s = s.strip()
    s = unwrap_latex_cmds(s)
    s = s.replace("~", " ")
    s = s.replace(r"\times", "×")
    s = s.replace(r"\mu", "μ")
    s = s.replace(r"\degree", "°")
    s = re.sub(r"\^\{([^}]+)\}", r"^\1", s)
    s = re.sub(r"\^\{?\\circ\}?", "°", s)
    s = re.sub(r"_\{([^{}]+)\}", r"\1", s)
    s = re.sub(r"_\{?(\d)\}?", r"\1", s)
    s = re.sub(r"\\[,;:!]", " ", s)
    s = re.sub(r"\\ ", " ", s)
    s = re.sub(r"\\(?=[A-Za-z])", "", s)
    s = collapse_spaced_letters(s)
    s = re.sub(r"\s*=\s*", " = ", s)
    s = re.sub(r"(\d)([a-zA-Zμ%/])", r"\1 \2", s)
    s = re.sub(r"([a-zA-Z])(\()", r"\1 \2", s)
    s = re.sub(r"\(\s*", "(", s)
    s = re.sub(r"\s*\)", ")", s)
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip()


def tighten_lab_lines(s: str) -> str:
    """Remove blank lines between consecutive lab result lines."""
    lines = s.split("\n")
    out: list[str] = []
    for ln in lines:
        stripped = ln.strip()
        is_lab = bool(stripped) and "=" in stripped and not stripped.startswith(("Which ", "What ", "How "))
        if is_lab and out and out[-1] == "":
            out.pop()
        if stripped:
            out.append(stripped)
        elif out and out[-1] != "":
            out.append("")
    return "\n".join(out)


def clean_math_blocks(s: str) -> str:
    def block_repl(m: re.Match[str]) -> str:
        return clean_latex_inner(m.group(1))

    s = re.sub(r"\$\$\s*(.*?)\s*\$\$", block_repl, s, flags=re.DOTALL)

    def inline_repl(m: re.Match[str]) -> str:
        return clean_latex_inner(m.group(1))

    s = re.sub(r"(?<!\$)\$(?!\$)\s*(.*?)\s*\$(?!\$)", inline_repl, s, flags=re.DOTALL)
    return s


def clean_aligned_envs(s: str) -> str:
    def repl(m: re.Match[str]) -> str:
        body = m.group(1)
        body = re.sub(r"\\\\", "\n", body)
        body = re.sub(r"&", " ", body)
        lines = [clean_latex_inner(ln) for ln in body.split("\n") if ln.strip()]
        return "\n".join(lines)

    return re.sub(r"\\begin\{aligned\}(.*?)\\end\{aligned\}", repl, s, flags=re.DOTALL)


def polish_units(s: str) -> str:
    s = re.sub(r"\bA\s*1\s*c\b", "A1c", s, flags=re.I)
    s = re.sub(r"\bmomol\b", "mmol", s, flags=re.I)
    s = re.sub(r"μ\s+IU", "μIU", s)
    s = re.sub(r"×10\^\{(\d+)\}", r"×10^\1", s)
    s = re.sub(r"10\^\{(\d+)\}", r"10^\1", s)
    return s


def clean_ocr_text(s: str) -> str:
    if not s:
        return s
    if "$$" in s or "$" in s or "\\mathrm" in s or "#### " in s or "\\begin{" in s:
        s = clean_aligned_envs(s)
        s = clean_math_blocks(s)
        s = re.sub(r"^#{1,6}\s+", "", s, flags=re.MULTILINE)
    s = polish_units(s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = tighten_lab_lines(s)
    return s.strip()


def clean_item(item: dict) -> bool:
    changed = False
    for key in TEXT_KEYS:
        if key in item and isinstance(item[key], str):
            cleaned = clean_ocr_text(item[key])
            if cleaned != item[key]:
                item[key] = cleaned
                changed = True
    for key in LIST_KEYS:
        if key in item and isinstance(item[key], list):
            new_opts = []
            for opt in item[key]:
                if isinstance(opt, str):
                    c = clean_ocr_text(opt)
                    new_opts.append(c)
                    if c != opt:
                        changed = True
                else:
                    new_opts.append(opt)
            item[key] = new_opts
    return changed


def clean_module(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    n = 0
    for item in data.get("items", []):
        if clean_item(item):
            n += 1
    if n:
        payload = json.dumps(data, indent=2, ensure_ascii=False)
        path.write_text(payload, encoding="utf-8")
        master = MASTER_DATA / path.name
        if master.parent.exists():
            master.write_text(payload, encoding="utf-8")
    return n


def main() -> int:
    patterns = ["endo2015_*.json", "endo2024_*.json"]
    paths: list[Path] = []
    if len(sys.argv) > 1:
        paths = [Path(p) for p in sys.argv[1:]]
    else:
        for pat in patterns:
            paths.extend(sorted(PORTAL_DATA.glob(pat)))
    total_items = 0
    total_files = 0
    for path in paths:
        if path.name == "index.json":
            continue
        n = clean_module(path)
        if n:
            print(f"{path.name}: cleaned {n} items")
            total_items += n
            total_files += 1
    print(f"Done: {total_files} files, {total_items} items updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
