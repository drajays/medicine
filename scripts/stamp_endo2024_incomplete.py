#!/usr/bin/env python3
"""Stamp EBR 2024 question stems that lack OCR answer keys as INCOMPLETE notes."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = Path("/Users/dr.ajayshukla/endo_masterapp/endo2024_chapters")
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")

MODULE_MD = {
    "e24-04": "endo2024_chapter_04_Adrenal.md",
    "e24-05": "endo2024_chapter_05_Bone.md",
    "e24-06": "endo2024_chapter_06_Diabetes_Section_1.md",
    "e24-07": "endo2024_chapter_07_Diabetes_Section_2.md",
    "e24-08": "endo2024_chapter_08_Female_Reproduction.md",
    "e24-09": "endo2024_chapter_09_Male_Reproduction.md",
    "e24-10": "endo2024_chapter_10_Lipids_and_Obesity.md",
    "e24-11": "endo2024_chapter_11_Pituitary.md",
    "e24-12": "endo2024_chapter_12_Thyroid_Section_1.md",
    "e24-13": "endo2024_chapter_13_Thyroid_Section_2.md",
}

INCOMPLETE_BANNER = (
    "⚠️ INCOMPLETE — no verified answer key in OCR for this case number. "
    "Review/replace before using for graded study."
)


def ref(section: str, quote: str) -> str:
    q = quote.replace('"', "'").strip()
    return f'{section}: "{q[:500]}"'


def clean_stem(text: str) -> str:
    text = re.sub(r"^#+\s+.*Board Review.*\n", "", text, flags=re.I | re.M)
    text = re.sub(r"^#+\s+[A-Z][^\n]+\n", "", text, flags=re.M)
    text = re.sub(r"^\d{1,2}\s+", "", text.strip())
    return text.strip()


def extract_options(block: str) -> list[str]:
    opts: list[str] = []
    for letter in "ABCDE":
        m = re.search(
            rf"(?:^|\n){letter}\.\s*(.+?)(?=\n[A-E]\.\s|\nWhich of|\n## |\Z)",
            block,
            re.DOTALL,
        )
        if m:
            opts.append(re.sub(r"\s+", " ", m.group(1).strip()))
    if not opts:
        opts = parse_table_options(block)
    return opts[:5]


def parse_table_options(block: str) -> list[str]:
    tables = re.findall(r"<table.*?</table>", block, re.S | re.I)
    opts: list[str] = []
    for table in tables:
        rows = re.findall(r"<tr>(.*?)</tr>", table, re.S | re.I)
        for row in rows[1:]:
            cells = [
                re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", c)).strip()
                for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S | re.I)
            ]
            cells = [c for c in cells if c]
            if len(cells) >= 2:
                label = cells[0].rstrip(".")
                if re.match(r"^[A-E]\.?$", label):
                    opts.append(" — ".join(cells[1:]) if len(cells) > 2 else cells[1])
                else:
                    opts.append(" | ".join(cells))
    return opts[:5]


def get_question_block(md: str, qnum: int) -> str | None:
    m = re.search(rf"## Question {qnum}\n\n(.*?)(?=\n## Question |\Z)", md, re.S)
    return m.group(1).strip() if m else None


def gaps_without_answer(md: str) -> set[int]:
    qs = {int(x) for x in re.findall(r"^## Question (\d+)", md, re.M)}
    ans = {int(x) for x in re.findall(r"^### Answer (\d+):", md, re.M)}
    return qs - ans


def build_incomplete_item(eid: str, qnum: int, block: str) -> dict:
    stem = clean_stem(block)
    opts = extract_options(block)
    parts = [
        "⚠️ **Authoring status: INCOMPLETE** — answer key missing from OCR for this case number. "
        "Replace this stub with verified MCQ + Why/How when the source answer is available.",
        "",
        "**Stem (from OCR):**",
        stem[:2800],
    ]
    if opts:
        parts.extend(["", "**Options parsed from stem:**"])
        for i, o in enumerate(opts):
            parts.append(f"{chr(ord('A') + i)}. {o}")
    else:
        parts.extend(["", "**Options:** not parsed — add A–E when completing."])
    text = "\n".join(parts)
    quote = re.sub(r"\s+", " ", stem)[:300] or f"EBR 2024 case {qnum}"
    return {
        "id": f"{eid}-q{qnum}-incomplete",
        "type": "note",
        "subtopic": f"EBR 2024 Case {qnum}",
        "title": f"INCOMPLETE — EBR 2024 Case {qnum} (answer key pending)",
        "text": text[:3500],
        "authoringStatus": "incomplete",
        "reference": ref(f"EBR 2024 Question {qnum} [INCOMPLETE]", quote),
    }


def tag_unverified_mcqs(module: dict, gaps: set[int]) -> int:
    tagged = 0
    for it in module["items"]:
        if it.get("type") != "mcq":
            continue
        m = re.search(r"-q(\d+)-mcq$", it.get("id", ""))
        if not m:
            continue
        qnum = int(m.group(1))
        if qnum not in gaps:
            continue
        if it.get("authoringStatus") == "incomplete":
            continue
        it["authoringStatus"] = "incomplete"
        expl = it.get("explanation", "")
        if INCOMPLETE_BANNER not in expl:
            it["explanation"] = f"{INCOMPLETE_BANNER}\n\n{expl}"[:4000]
        tagged += 1
    return tagged


def main() -> None:
    total_notes = 0
    total_tagged = 0
    for eid, md_name in MODULE_MD.items():
        md = (CHAPTERS / md_name).read_text(encoding="utf-8")
        gaps = gaps_without_answer(md)
        if not gaps:
            continue
        mod_path = next(PORTAL_DATA.glob(f"endo2024_{eid}_*.json"))
        module = json.loads(mod_path.read_text(encoding="utf-8"))
        existing_ids = {i["id"] for i in module["items"]}
        notes_added = 0
        for q in sorted(gaps):
            block = get_question_block(md, q)
            if not block:
                continue
            item = build_incomplete_item(eid, q, block)
            if item["id"] not in existing_ids:
                module["items"].append(item)
                existing_ids.add(item["id"])
                notes_added += 1
        mcq_tagged = tag_unverified_mcqs(module, gaps)
        if notes_added or mcq_tagged:
            payload = json.dumps(module, indent=2, ensure_ascii=False)
            mod_path.write_text(payload, encoding="utf-8")
            master_path = MASTER_DATA / mod_path.name
            if master_path.parent.exists():
                master_path.write_text(payload, encoding="utf-8")
            print(
                f"{eid}: +{notes_added} incomplete notes, "
                f"tagged {mcq_tagged} unverified MCQs (Q {sorted(gaps)})"
            )
            total_notes += notes_added
            total_tagged += mcq_tagged
    print(f"Total: {total_notes} incomplete notes, {total_tagged} MCQs tagged unverified")


if __name__ == "__main__":
    main()
