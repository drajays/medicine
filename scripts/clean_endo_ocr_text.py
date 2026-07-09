#!/usr/bin/env python3
"""Normalize PaddleOCR LaTeX/math artifacts in endo JSON text fields."""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PORTAL_DATA = ROOT / "endo" / "data"
PORTAL_IMGS = ROOT / "endo" / "imgs"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
IMG_SOURCES = [
    Path("/Users/dr.ajayshukla/endo_masterapp/williams_2024_chapters/imgs"),
    Path("/Users/dr.ajayshukla/endo_masterapp/endo2015_chapters/imgs"),
    Path("/Users/dr.ajayshukla/endo_masterapp/endo2024_chapters/imgs"),
]

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
    s = re.sub(r"kg/m\s*\^\{2\}", "kg/m²", s)
    s = re.sub(r"kg/m\s*\^2", "kg/m²", s)
    s = re.sub(r"(?<![A-Za-z])m\s*\^\{2\}", "m²", s)
    s = re.sub(r"(?<![A-Za-z])m\s*\^2", "m²", s)
    s = re.sub(r"\\%", "%", s)
    return s


def fix_ocr_glitches(s: str) -> str:
    s = re.sub(r"\bF=+ucose\b", "Glucose", s, flags=re.I)
    s = re.sub(r"\bupmuI\s*U/m\s*L\b", "μIU/mL", s, flags=re.I)
    s = re.sub(r"\bSpenlic\b", "Splenic", s)
    s = re.sub(r"\bPrefunch\b", "Prelunch", s)
    s = re.sub(r"\bhemoglobin\s{2,}A(?:1c|lc|tc)\b", "Hemoglobin A1c", s, flags=re.I)
    s = re.sub(r"\bhemoglobin\s+A(?:lc|tc)\b", "Hemoglobin A1c", s, flags=re.I)
    s = re.sub(r"\bHemoglobin\s{2,}A1c\b", "Hemoglobin A1c", s)
    s = re.sub(r"\bhemoglobin\s{2,}A1c\b", "Hemoglobin A1c", s, flags=re.I)
    s = re.sub(r"\^\{([^}]+)\}", r"^\1", s)
    return s


SOURCE_CHAPTERS = [
    Path("/Users/dr.ajayshukla/endo_masterapp/endo2015_chapters"),
    Path("/Users/dr.ajayshukla/endo_masterapp/endo2024_chapters"),
]
_MD_TABLES: list[str] | None = None


def _md_tables() -> list[str]:
    global _MD_TABLES
    if _MD_TABLES is not None:
        return _MD_TABLES
    tables: list[str] = []
    for base in SOURCE_CHAPTERS:
        if not base.is_dir():
            continue
        for md in base.glob("*.md"):
            text = md.read_text(encoding="utf-8", errors="ignore")
            tables.extend(re.findall(r"<table[^>]*>.*?</table>", text, flags=re.DOTALL | re.I))
    _MD_TABLES = tables
    return tables


def _normalize_table_marker(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\$+", "", s)
    s = re.sub(r"\^\{([^}]+)\}", r"^\1", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def recover_truncated_tables(s: str) -> str:
    if "<table" not in s:
        return s
    if "</table>" in s:
        return s
    start = s.find("<table")
    partial = s[start:]
    markers = [
        re.sub(r"\s+", " ", m).strip()
        for m in re.findall(r">([^<>]{4,}?)</t[dh]>", partial, flags=re.I)
    ]
    header_markers = [m for m in markers[:8] if m.lower() in {"time", "glucose", "insulin", "c-peptide", "symptoms"}]
    if len(header_markers) >= 3:
        for table in _md_tables():
            norm = _normalize_table_marker(table)
            if all(_normalize_table_marker(m) in norm for m in header_markers):
                return s[:start] + table
    for marker in markers:
        norm_marker = _normalize_table_marker(marker)
        if len(norm_marker) < 8:
            continue
        for table in _md_tables():
            if norm_marker in _normalize_table_marker(table):
                return s[:start] + table
    if partial.count("</td>") < 2:
        return s[:start].rstrip()
    return s


def clean_table_cell(chunk: str) -> str:
    chunk = clean_math_blocks(chunk)
    chunk = re.sub(r"<br\s*/?>", " ", chunk, flags=re.I)
    chunk = re.sub(r"<[^>]+>", "", chunk)
    chunk = polish_units(chunk)
    chunk = fix_ocr_glitches(chunk)
    chunk = re.sub(r"\s+", " ", chunk)
    return chunk.strip()


def clean_html_tables(s: str) -> str:
    if "<table" not in s:
        return s

    def table_repl(m: re.Match[str]) -> str:
        table = m.group(0)
        table = re.sub(r"\sstyle='[^']*'", "", table)
        table = re.sub(r'\sstyle="[^"]*"', "", table)
        table = re.sub(r"\sborder=\d+", "", table)

        def cell_repl(cm: re.Match[str]) -> str:
            return cm.group(1) + clean_table_cell(cm.group(2)) + cm.group(3)

        return re.sub(
            r"(<t[dh][^>]*>)(.*?)(</t[dh]>)",
            cell_repl,
            table,
            flags=re.DOTALL | re.I,
        )

    s = recover_truncated_tables(s)
    s = re.sub(r"<table[^>]*>[\s\S]*?</table>", table_repl, s, flags=re.I)
    if "<table" in s:
        s = re.sub(r"<table[^>]*>[\s\S]*$", table_repl, s, flags=re.I)
    return s


def pipe_tables_to_html(s: str) -> str:
    """Convert flattened pipe-separated table rows back to simple HTML tables."""
    if "<table" in s:
        return s
    lines = s.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        pipe_count = ln.count("|")
        if pipe_count >= 2:
            col_count = pipe_count + 1
            block: list[str] = []
            while i < len(lines) and lines[i].count("|") + 1 == col_count:
                block.append(lines[i])
                i += 1
            if len(block) >= 2:
                rows = []
                for row in block:
                    cells = [clean_table_cell(part.strip()) for part in row.split("|")]
                    rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
                out.append("<table>" + "".join(rows) + "</table>")
                continue
            out.extend(block)
            continue
        out.append(ln)
        i += 1
    return "\n".join(out)


def resolve_image_src(src: str) -> str:
    src = src.strip()
    if src.startswith("imgs/"):
        return src
    name = unquote(src.split("?")[0].split("/")[-1])
    for base in IMG_SOURCES:
        candidate = base / name
        if candidate.is_file():
            return f"imgs/{name}"
    return src


def normalize_embedded_images(s: str) -> str:
    if "<img" not in s:
        return s

    def img_repl(m: re.Match[str]) -> str:
        tag = m.group(0)
        src_m = re.search(r'\bsrc="([^"]+)"', tag)
        if not src_m:
            return tag
        return tag.replace(src_m.group(1), resolve_image_src(src_m.group(1)))

    return re.sub(r"<img[^>]+/?>", img_repl, s)


def clean_ocr_text(s: str) -> str:
    if not s:
        return s
    if "$$" in s or "$" in s or "\\mathrm" in s or "#### " in s or "\\begin{" in s:
        s = clean_aligned_envs(s)
        s = clean_math_blocks(s)
        s = re.sub(r"^#{1,6}\s+", "", s, flags=re.MULTILINE)
    s = polish_units(s)
    s = fix_ocr_glitches(s)
    s = clean_html_tables(s)
    s = pipe_tables_to_html(s)
    s = normalize_embedded_images(s)
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


def collect_image_names(data: dict) -> set[str]:
    names: set[str] = set()

    def scan(value: object) -> None:
        if not isinstance(value, str) or "<img" not in value:
            return
        for m in re.finditer(r'<img[^>]+src="([^"]+)"', value):
            src = m.group(1)
            if src.startswith("imgs/"):
                names.add(src.split("/", 1)[1])
            elif src.startswith("http"):
                names.add(unquote(src.split("?")[0].split("/")[-1]))

    for item in data.get("items", []):
        for key in TEXT_KEYS:
            if key in item:
                scan(item[key])
        for opt in item.get("options") or []:
            scan(opt)
    return names


def sync_portal_images(paths: list[Path]) -> int:
    needed: set[str] = set()
    for path in paths:
        if not path.is_file() or path.name == "index.json":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        needed.update(collect_image_names(data))

    PORTAL_IMGS.mkdir(parents=True, exist_ok=True)
    copied = 0
    for name in sorted(needed):
        dest = PORTAL_IMGS / name
        if dest.is_file():
            continue
        for base in IMG_SOURCES:
            src = base / name
            if src.is_file():
                shutil.copy2(src, dest)
                copied += 1
                break
    return copied


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
    copied = sync_portal_images(paths)
    print(f"Done: {total_files} files, {total_items} items updated, {copied} images copied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
