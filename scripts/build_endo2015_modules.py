#!/usr/bin/env python3
"""Build ESAP 2015 (e15-*) JSON modules from split chapter MD files."""
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
CHAPTERS = MASTER / "endo2015_chapters"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = MASTER / "data"

SECTION = "Endocrine Self-Assessment Program 2015 (Endo 2015)"

MODULES = [
    ("e15-01", "FM", "Front Matter", "endo2015_chapter_01_Front_Matter.md", "reference"),
    ("e15-02", "LR", "Laboratory Reference Ranges", "endo2015_chapter_02_Laboratory_Reference_Ranges.md", "reference"),
    ("e15-03", "03", "Diabetes", "endo2015_chapter_03_Diabetes.md", "topic"),
    ("e15-04", "04", "Lipid and Obesity", "endo2015_chapter_04_Lipid_and_Obesity.md", "topic"),
    ("e15-05", "05", "Bone and Mineral Metabolism", "endo2015_chapter_05_Bone_and_Mineral_Metabolism.md", "topic"),
    ("e15-06", "06", "Thyroid", "endo2015_chapter_06_Thyroid.md", "topic"),
    ("e15-07", "07", "Adrenal", "endo2015_chapter_07_Adrenal.md", "topic"),
    ("e15-08", "08", "Pituitary", "endo2015_chapter_08_Pituitary.md", "topic"),
    ("e15-09", "09", "Reproduction Female", "endo2015_chapter_09_Reproduction_Female.md", "topic"),
    ("e15-10", "10", "Reproduction Male", "endo2015_chapter_10_Reproduction_Male.md", "topic"),
]


def ref(section: str, quote: str) -> str:
    q = quote.replace('"', "'").strip()
    if len(q) < 20:
        q = quote.strip()
    return f'{section}: "{q[:500]}"'


def letter_to_index(letter: str) -> int:
    return ord(letter.upper()) - ord("A")


def extract_quote(text: str, label: str = "Educational Objective") -> str:
    m = re.search(rf"{label}:\s*\n*(.+?)(?=\n#####|\nUpToDate|\nReference|\Z)", text, re.DOTALL | re.I)
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())[:400]
    para = re.sub(r"\s+", " ", text).strip()
    return para[:400] if para else "See ESAP 2015 discussion."


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
        discussion = adisc[am.end():].strip() if am else adisc.strip()
        quote = extract_quote(discussion)
        prefix = f"q{qnum}"
        items.append(
            {
                "id": f"{prefix}-mcq",
                "type": "mcq",
                "subtopic": f"ESAP 2015 Case {qnum}",
                "question": clean_ocr_text(stem)[:3000],
                "options": [clean_ocr_text(o) for o in options[:5]],
                "correctOption": letter_to_index(letter),
                "explanation": clean_ocr_text(discussion)[:4000] if discussion else f"Correct answer: {letter}.",
                "reference": ref(f"ESAP 2015 Question {qnum}", quote),
            }
        )
        items.append(
            {
                "id": f"{prefix}-why",
                "type": "note",
                "subtopic": f"ESAP 2015 Case {qnum}",
                "title": f"Why answer {letter} is correct",
                "text": (am.group(2) if am else quote)[:2000],
                "reference": ref(f"ESAP 2015 Answer {qnum}", quote),
            }
        )
        if len(discussion) > 120:
            items.append(
                {
                    "id": f"{prefix}-how",
                    "type": "note",
                    "subtopic": f"ESAP 2015 Case {qnum}",
                    "title": "How to apply this case clinically",
                    "text": discussion[:2500],
                    "reference": ref(f"ESAP 2015 Discussion {qnum}", extract_quote(discussion)),
                }
            )
    return items


def extract_options(block: str) -> tuple[str, list[str]]:
    opts: list[str] = []
    for letter in "ABCDE":
        m = re.search(
            rf"(?:^|\n){letter}\.\s*(.+?)(?=\n[A-E]\.\s|\nWhich of|\nYou are|\nOn physical|\nLaboratory|\n## |\Z)",
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


def build_reference_module(eid: str, ch_no: str, title: str, md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    items: list[dict] = []
    if eid == "e15-01":
        overview = re.search(r"##### OVERVIEW\s*\n+(.+?)(?=\n#####|\Z)", text, re.DOTALL)
        objectives = re.search(r"##### LEARNING OBJECTIVES\s*\n+(.+?)(?=\n#####|\Z)", text, re.DOTALL)
        if overview:
            items.append(
                {
                    "id": "e15-01-n1",
                    "type": "note",
                    "subtopic": "ESAP 2015 overview",
                    "title": "What ESAP 2015 covers",
                    "text": re.sub(r"\s+", " ", overview.group(1).strip())[:2000],
                    "reference": ref("OVERVIEW", overview.group(1).strip()[:300]),
                }
            )
        if objectives:
            items.append(
                {
                    "id": "e15-01-n2",
                    "type": "note",
                    "subtopic": "Learning objectives",
                    "title": "How to use ESAP 2015 for board prep",
                    "text": re.sub(r"\s+", " ", objectives.group(1).strip())[:2000],
                    "reference": ref("LEARNING OBJECTIVES", objectives.group(1).strip()[:300]),
                }
            )
    elif eid == "e15-02":
        chunks = re.split(r"\n##### ", text)
        n = 0
        for chunk in chunks[1:]:
            n += 1
            head, _, body = chunk.partition("\n")
            body = body.strip()
            if not body:
                continue
            items.append(
                {
                    "id": f"e15-02-n{n}",
                    "type": "note",
                    "subtopic": head.strip(),
                    "title": ("How to interpret " if n % 2 else "Why reference ranges matter: ") + head.strip()[:50],
                    "text": re.sub(r"\s+", " ", body)[:2500],
                    "reference": ref(head.strip(), body[:300].replace("\n", " ")),
                }
            )
    return {
        "id": eid,
        "volume": 2015,
        "chapterNo": ch_no,
        "title": title,
        "section": SECTION,
        "authors": "Endocrine Society ESAP 2015 Program Faculty",
        "sourceFile": f"endo2015_chapters/{md_path.name}",
        "items": items,
    }


def build_topic_module(eid: str, ch_no: str, title: str, md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    items = parse_topic_md(text)
    # re-id with module prefix
    out_items = []
    for it in items:
        it = dict(it)
        old = it["id"]
        it["id"] = f"{eid}-{old}"
        out_items.append(it)
    return {
        "id": eid,
        "volume": 2015,
        "chapterNo": ch_no,
        "title": title,
        "section": SECTION,
        "authors": "Endocrine Society ESAP 2015 Program Faculty",
        "sourceFile": f"endo2015_chapters/{md_path.name}",
        "items": out_items,
    }


def slug_title(title: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", title).strip("_")
    return s


def main() -> None:
    if not CHAPTERS.exists():
        raise SystemExit("Run scripts/split_endo2015.py first.")

    PORTAL_DATA.mkdir(parents=True, exist_ok=True)
    MASTER_DATA.mkdir(parents=True, exist_ok=True)

    for eid, ch_no, title, md_name, kind in MODULES:
        md_path = CHAPTERS / md_name
        if not md_path.exists():
            print(f"SKIP missing {md_name}")
            continue
        if kind == "reference":
            mod = build_reference_module(eid, ch_no, title, md_path)
        else:
            mod = build_topic_module(eid, ch_no, title, md_path)
        fname = f"endo2015_{eid}_{slug_title(title)}.json"
        out_portal = PORTAL_DATA / fname
        out_master = MASTER_DATA / fname
        payload = json.dumps(mod, indent=2, ensure_ascii=False)
        out_portal.write_text(payload, encoding="utf-8")
        out_master.write_text(payload, encoding="utf-8")
        notes = sum(1 for i in mod["items"] if i["type"] == "note")
        mcqs = sum(1 for i in mod["items"] if i["type"] == "mcq")
        wh = sum(1 for i in mod["items"] if i["type"] == "note" and i.get("title", "").startswith(("Why", "How")))
        print(f"{eid}: {len(mod['items'])} items ({notes} notes, {mcqs} MCQs, Why/How {wh}/{notes}) → {fname}")

    # Copy chapter MD sources for traceability
    dest_md = PORTAL_DATA / "endo2015_chapters"
    if dest_md.exists():
        shutil.rmtree(dest_md)
    shutil.copytree(CHAPTERS, dest_md, ignore=shutil.ignore_patterns("*.json", "imgs"))
    print("Copied endo2015_chapters MD sources to portal.")


if __name__ == "__main__":
    main()
