#!/usr/bin/env python3
"""Build Endocrine Board Review 2024 (e24-*) JSON modules from split chapter MD files."""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from clean_endo_ocr_text import clean_ocr_text  # noqa: E402
MASTER = Path("/Users/dr.ajayshukla/endo_masterapp")
CHAPTERS = MASTER / "endo2024_chapters"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = MASTER / "data"

SECTION = "Endocrine Board Review 2024 (EBR 2024)"

MODULES = [
    ("e24-01", "FM", "Front Matter", "endo2024_chapter_01_Front_Matter.md", "reference"),
    ("e24-02", "LR", "Laboratory Reference Ranges", "endo2024_chapter_02_Laboratory_Reference_Ranges.md", "reference"),
    ("e24-03", "AB", "Common Abbreviations", "endo2024_chapter_03_Common_Abbreviations.md", "reference"),
    ("e24-04", "04", "Adrenal", "endo2024_chapter_04_Adrenal.md", "topic"),
    ("e24-05", "05", "Bone", "endo2024_chapter_05_Bone.md", "topic"),
    ("e24-06", "06", "Diabetes Section 1", "endo2024_chapter_06_Diabetes_Section_1.md", "topic"),
    ("e24-07", "07", "Diabetes Section 2", "endo2024_chapter_07_Diabetes_Section_2.md", "topic"),
    ("e24-08", "08", "Female Reproduction", "endo2024_chapter_08_Female_Reproduction.md", "topic"),
    ("e24-09", "09", "Male Reproduction", "endo2024_chapter_09_Male_Reproduction.md", "topic"),
    ("e24-10", "10", "Lipids and Obesity", "endo2024_chapter_10_Lipids_and_Obesity.md", "topic"),
    ("e24-11", "11", "Pituitary", "endo2024_chapter_11_Pituitary.md", "topic"),
    ("e24-12", "12", "Thyroid Section 1", "endo2024_chapter_12_Thyroid_Section_1.md", "topic"),
    ("e24-13", "13", "Thyroid Section 2", "endo2024_chapter_13_Thyroid_Section_2.md", "topic"),
]


def ref(section: str, quote: str) -> str:
    q = quote.replace('"', "'").strip()
    if len(q) < 20:
        q = quote.strip()
    return f'{section}: "{q[:500]}"'


def letter_to_index(letter: str) -> int:
    return ord(letter.upper()) - ord("A")


def extract_quote(text: str) -> str:
    m = re.search(
        r"EDUCATIONAL OBJECTIVE:\s*\n*(.+?)(?=\n#####|\nREFERENCE|\Z)",
        text,
        re.DOTALL | re.I,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())[:400]
    para = re.sub(r"\s+", " ", text).strip()
    return para[:400] if para else "See EBR 2024 discussion."


def extract_options(block: str) -> tuple[str, list[str]]:
    opts: list[str] = []
    for letter in "ABCDE":
        m = re.search(
            rf"(?:^|\n){letter}\.\s*(.+?)(?=\n[A-E]\.\s|\nWhich of|\n## |\Z)",
            block,
            re.DOTALL,
        )
        if m:
            opts.append(re.sub(r"\s+", " ", m.group(1).strip()))
    if len(opts) < 4:
        for letter in "ABCDE":
            m = re.search(
                rf"(?:^|\n){letter}\)\s*(.+?)(?=\n[A-E]\)\s|\nWhich of|\Z)",
                block,
                re.DOTALL,
            )
            if m:
                opts.append(re.sub(r"\s+", " ", m.group(1).strip()))
    stem = block
    m0 = re.search(r"(?:^|\n)[A-E][\.)]\s", block)
    if m0:
        stem = block[: m0.start()].strip()
    stem = re.sub(r"^\d{1,3}\s+", "", stem).strip()
    return stem, opts


def parse_topic_md(text: str) -> list[dict]:
    items: list[dict] = []
    blocks = re.split(r"\n## Question (\d+)\n", text)
    if len(blocks) < 2:
        return items
    it = iter(blocks[1:])
    for qnum_s, body in zip(it, it):
        qnum = int(qnum_s)
        ans_split = re.split(r"\n### Answer \d+:", body, maxsplit=1)
        qblock = ans_split[0].strip()
        adisc = ans_split[1] if len(ans_split) > 1 else ""
        stem, options = extract_options(qblock)
        if len(options) < 4:
            continue
        letter = "A"
        am = re.match(r"\s*([A-E])\)\s*([^\n]+)", adisc)
        if am:
            letter = am.group(1)
        discussion = adisc[am.end() :].strip() if am else adisc.strip()
        quote = extract_quote(discussion)
        prefix = f"q{qnum}"
        items.append(
            {
                "id": f"{prefix}-mcq",
                "type": "mcq",
                "subtopic": f"EBR 2024 Case {qnum}",
                "question": clean_ocr_text(stem)[:3000],
                "options": [clean_ocr_text(o) for o in options[:5]],
                "correctOption": letter_to_index(letter),
                "explanation": clean_ocr_text(discussion)[:4000] if discussion else f"Correct answer: {letter}.",
                "reference": ref(f"EBR 2024 Question {qnum}", quote),
            }
        )
        items.append(
            {
                "id": f"{prefix}-why",
                "type": "note",
                "subtopic": f"EBR 2024 Case {qnum}",
                "title": f"Why answer {letter} is correct",
                "text": (am.group(2) if am else quote)[:2000],
                "reference": ref(f"EBR 2024 Answer {qnum}", quote),
            }
        )
        if len(discussion) > 120:
            items.append(
                {
                    "id": f"{prefix}-how",
                    "type": "note",
                    "subtopic": f"EBR 2024 Case {qnum}",
                    "title": "How to apply this case clinically",
                    "text": discussion[:2500],
                    "reference": ref(f"EBR 2024 Discussion {qnum}", extract_quote(discussion)),
                }
            )
    return items


def build_reference_module(eid: str, ch_no: str, title: str, md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    items: list[dict] = []
    if eid == "e24-01":
        overview = re.search(r"##### OVERVIEW\s*\n+(.+?)(?=\n#####|\Z)", text, re.DOTALL)
        objectives = re.search(r"##### LEARNING OBJECTIVES\s*\n+(.+?)(?=\n#####|\Z)", text, re.DOTALL)
        if overview:
            items.append(
                {
                    "id": "e24-01-n1",
                    "type": "note",
                    "subtopic": "EBR 2024 overview",
                    "title": "What Endocrine Board Review 2024 covers",
                    "text": re.sub(r"\s+", " ", overview.group(1).strip())[:2000],
                    "reference": ref("OVERVIEW", overview.group(1).strip()[:300]),
                }
            )
        if objectives:
            items.append(
                {
                    "id": "e24-01-n2",
                    "type": "note",
                    "subtopic": "Learning objectives",
                    "title": "How to use EBR 2024 for board prep",
                    "text": re.sub(r"\s+", " ", objectives.group(1).strip())[:2000],
                    "reference": ref("LEARNING OBJECTIVES", objectives.group(1).strip()[:300]),
                }
            )
    elif eid == "e24-02":
        major = re.split(
            r"\n##### (Lipid Values|Hematologic Values|Thyroid Values|Endocrine Values|Urine|Saliva|Semen)\s*\n",
            text,
        )
        if len(major) > 1:
            for i in range(1, len(major), 2):
                head = major[i].strip()
                body = major[i + 1].strip() if i + 1 < len(major) else ""
                if not body:
                    continue
                n = len(items) + 1
                items.append(
                    {
                        "id": f"e24-02-n{n}",
                        "type": "note",
                        "subtopic": head,
                        "title": ("How to interpret " if n % 2 else "Why reference ranges matter: ") + head,
                        "text": re.sub(r"\s+", " ", body)[:2500],
                        "reference": ref(head, body[:300].replace("\n", " ")),
                    }
                )
        else:
            items.append(
                {
                    "id": "e24-02-n1",
                    "type": "note",
                    "subtopic": "Laboratory reference ranges",
                    "title": "Why laboratory reference ranges matter on boards",
                    "text": re.sub(r"\s+", " ", text)[:3000],
                    "reference": ref("LABORATORY REFERENCE RANGES", text[:300]),
                }
            )
    elif eid == "e24-03":
        body = re.sub(r"^#.+?\n", "", text, count=1).strip()
        items.append(
            {
                "id": "e24-03-n1",
                "type": "note",
                "subtopic": "Abbreviations",
                "title": "Why common endocrine abbreviations matter on boards",
                "text": re.sub(r"\s+", " ", body)[:3000],
                "reference": ref("COMMON ABBREVIATIONS", body[:300]),
            }
        )
    return {
        "id": eid,
        "volume": 2024,
        "chapterNo": ch_no,
        "title": title,
        "section": SECTION,
        "authors": "Endocrine Society EBR 2024 Program Faculty",
        "sourceFile": f"endo2024_chapters/{md_path.name}",
        "items": items,
    }


def build_topic_module(eid: str, ch_no: str, title: str, md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    items = parse_topic_md(text)
    out_items = []
    for it in items:
        it = dict(it)
        it["id"] = f"{eid}-{it['id']}"
        out_items.append(it)
    return {
        "id": eid,
        "volume": 2024,
        "chapterNo": ch_no,
        "title": title,
        "section": SECTION,
        "authors": "Endocrine Society EBR 2024 Program Faculty",
        "sourceFile": f"endo2024_chapters/{md_path.name}",
        "items": out_items,
    }


def slug_title(title: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", title).strip("_")


def main() -> None:
    if not CHAPTERS.exists():
        raise SystemExit("Run scripts/split_endo2024.py first.")

    PORTAL_DATA.mkdir(parents=True, exist_ok=True)
    MASTER_DATA.mkdir(parents=True, exist_ok=True)

    summary: list[str] = []
    for eid, ch_no, title, md_name, kind in MODULES:
        md_path = CHAPTERS / md_name
        if not md_path.exists():
            print(f"SKIP {eid}: missing {md_name}")
            continue
        module = (
            build_reference_module(eid, ch_no, title, md_path)
            if kind == "reference"
            else build_topic_module(eid, ch_no, title, md_path)
        )
        fname = f"endo2024_{eid}_{slug_title(title)}.json"
        payload = json.dumps(module, indent=2, ensure_ascii=False)
        (PORTAL_DATA / fname).write_text(payload, encoding="utf-8")
        (MASTER_DATA / fname).write_text(payload, encoding="utf-8")
        mcq = sum(1 for i in module["items"] if i["type"] == "mcq")
        notes = sum(1 for i in module["items"] if i["type"] == "note")
        wh = sum(
            1
            for i in module["items"]
            if i["type"] == "note" and i.get("title", "").startswith(("Why", "How"))
        )
        summary.append(f"{eid}: {len(module['items'])} items ({mcq} MCQ, {notes} notes, Why/How {wh}/{notes})")
        print(summary[-1])

    print(f"Wrote {len(summary)} modules to {PORTAL_DATA} and {MASTER_DATA}")


if __name__ == "__main__":
    main()
