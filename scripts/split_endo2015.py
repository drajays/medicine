#!/usr/bin/env python3
"""Split ESAP 2015 OCR into chapter MD files under endo_masterapp/endo2015_chapters/."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = Path("/Users/dr.ajayshukla/endo_masterapp")
SRC_MD = MASTER / "noupload/endo2015/endo2015.pdf_by_PaddleOCR-VL-1.6.md"
SRC_JSON = MASTER / "noupload/endo2015/endo2015.pdf_by_PaddleOCR-VL-1.6.json"
DEST = MASTER / "endo2015_chapters"
IMGS = DEST / "imgs"

STRUCTURAL = [
    (1, "Front_Matter", None, "# Laboratory Reference Ranges"),
    (2, "Laboratory_Reference_Ranges", "# Laboratory Reference Ranges", "## ENDOCRINE SELF-ASSESSMENT PROGRAM 2015"),
    (3, "Questions_Part_I", "## ENDOCRINE SELF-ASSESSMENT PROGRAM 2015", "# ANSWERS"),
    (4, "Answers_Part_II", "# ANSWERS", "## ENDOCRINE SELF-ASSESSMENT PROGRAM 2015\n\nPart III"),
    (5, "Index_Part_III", "## ENDOCRINE SELF-ASSESSMENT PROGRAM 2015\n\nPart III", None),
]

TOPIC_SECTIONS = [
    ("03", "Diabetes", "DIABETES"),
    ("04", "Lipid_and_Obesity", "LIPID-OBESITY"),
    ("05", "Bone_and_Mineral_Metabolism", "BONE"),
    ("06", "Thyroid", "THYROID"),
    ("07", "Adrenal", "ADRENAL"),
    ("08", "Pituitary", "PITUITARY"),
    ("09", "Reproduction_Female", "REPRODUCTION, FEMALE"),
    ("10", "Reproduction_Male", "REPRODUCTION, MALE"),
]

KEYWORD_RULES: list[tuple[str, list[str]]] = [
    ("BONE", ["parathyroid", "calcium", "phosphate", "vitamin d", "osteoporosis", "bone mineral", "pth", "denosumab", "risedronate", "zoledronic", "hypercalcemia", "hypocalcemia", "nephrolithiasis"]),
    ("THYROID", ["thyroid", "tsh", " thyroglobulin", "graves", "amiodarone", "levothyroxine", "methimazole", "propylthiouracil", "radioiodine", "fnab", "nodular", "goiter", "thyrotoxic"]),
    ("ADRENAL", ["aldosterone", "cortisol", "cushing", "adrenal", "pheochromocytoma", "hyperaldosteronism", "cosyntropin", "dexamethasone", "21-hydroxy", "conn", "adrenalectomy"]),
]


def localize_images(text: str) -> str:
    pattern = r'https://[a-zA-Z0-9.-]+\.bcebos\.com/[^"\s>]+?/imgs/([^"\s>?]+)(?:\?[^"\s>]*)?'
    return re.sub(pattern, r"imgs/\1", text)


def slice_md(lines: list[str], start_heading: str | None, end_heading: str | None) -> str:
    start = 0
    if start_heading:
        for i, line in enumerate(lines):
            if line.strip() == start_heading or (start_heading in line and line.strip().startswith("#")):
                start = i
                break
    end = len(lines)
    if end_heading:
        for i in range(start + 1, len(lines)):
            if lines[i].strip() == end_heading or (end_heading in lines[i] and lines[i].strip().startswith("#")):
                end = i
                break
    return localize_images("".join(lines[start:end]))


def parse_index_assignments(md: str) -> dict[str, set[int]]:
    start = md.find("Part III")
    block = md[start:] if start >= 0 else ""
    sections: dict[str, set[int]] = {}
    current: str | None = None
    for line in block.split("\n"):
        s = line.strip().replace("##### ", "")
        if s in {"DIABETES", "LIPID-OBESITY", "PITUITARY", "REPRODUCTION, FEMALE", "REPRODUCTION, MALE"}:
            current = s
            sections.setdefault(current, set())
            continue
        if current and ":" in s:
            nums = re.findall(r"\b(\d{1,3})\b", s.split(":", 1)[1])
            for n in nums:
                q = int(n)
                if 1 <= q <= 120:
                    sections[current].add(q)
    return sections


def classify_unassigned(qnum: int, qtext: str, atext: str) -> str:
    blob = (qtext + " " + atext).lower()
    scores = {k: 0 for k, _ in KEYWORD_RULES}
    for key, words in KEYWORD_RULES:
        for w in words:
            if w in blob:
                scores[key] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "BONE"


def build_topic_map(md: str, questions: dict[int, str], answers: dict[int, str]) -> dict[str, set[int]]:
    index = parse_index_assignments(md)
    topic_map = {
        "DIABETES": set(index.get("DIABETES", set())),
        "LIPID-OBESITY": set(index.get("LIPID-OBESITY", set())),
        "PITUITARY": set(index.get("PITUITARY", set())),
        "REPRODUCTION, FEMALE": set(index.get("REPRODUCTION, FEMALE", set())),
        "REPRODUCTION, MALE": set(index.get("REPRODUCTION, MALE", set())),
        "BONE": set(),
        "THYROID": set(),
        "ADRENAL": set(),
    }
    assigned = set().union(*topic_map.values())
    for q in range(1, 121):
        if q in assigned:
            continue
        key = classify_unassigned(q, questions.get(q, ""), answers.get(q, ""))
        topic_map[key].add(q)
    return topic_map


def parse_questions(part_i: str) -> dict[int, str]:
    m = re.search(r"Part I\s*", part_i)
    body = part_i[m.end():] if m else part_i
    # Find question starts: line begins with optional number + age vignette
    markers: list[tuple[int, int]] = []
    for m in re.finditer(r"(?:^|\n)(\d{1,3}) ([A-Z][^\n]{10,80}?(?:year|yr|yo|old))", body):
        markers.append((m.start(1), int(m.group(1))))
    if not markers:
        return {}
    chunks: dict[int, str] = {}
    # Q1 is text before first numbered marker (if marker isn't 1)
    if markers[0][1] != 1:
        chunks[1] = body[: markers[0][0]].strip()
    for i, (pos, num) in enumerate(markers):
        end = markers[i + 1][0] if i + 1 < len(markers) else len(body)
        chunk = body[pos:end].strip()
        chunk = re.sub(r"^\d{1,3}\s+", "", chunk)
        chunks[num] = chunk
    return chunks


def parse_answers(part_ii: str) -> dict[int, tuple[str, str, str]]:
    """Return qnum -> (letter, answer_line, full_discussion)."""
    body = part_ii
    m = re.search(r"Part II\s*", body)
    body = body[m.end():] if m else body
    pat = re.compile(
        r"(?:^|\n)(?:#{1,5}\s*)?(\d{1,3})\s+ANSWER:\s*([A-E])\)\s*([^\n]+)",
        re.MULTILINE,
    )
    matches = list(pat.finditer(body))
  # Q1 without number prefix
    m1 = re.search(r"(?:^|\n)#{1,5}\s*ANSWER:\s*([A-E])\)\s*([^\n]+)", body)
    out: dict[int, tuple[str, str, str]] = {}
    if m1 and (not matches or matches[0].start() > 0):
        pre = body[: m1.start()]
        if "spironolactone" in pre.lower() or matches and matches[0].group(1) != "1":
            end = matches[0].start() if matches else len(body)
            out[1] = (m1.group(1), m1.group(2), body[m1.start():end].strip())
    for i, match in enumerate(matches):
        qnum = int(match.group(1))
        letter = match.group(2)
        line = match.group(3)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        out[qnum] = (letter, line, body[match.start():end].strip())
    return out


def extract_options(block: str) -> tuple[str, list[str]]:
    opts: list[str] = []
    for letter in "ABCDE":
        m = re.search(rf"(?:^|\n){letter}\.\s*(.+?)(?=\n[A-E]\.|\nWhich of|\Z)", block, re.DOTALL)
        if m:
            opts.append(re.sub(r"\s+", " ", m.group(1).strip()))
    stem = block
    m0 = re.search(r"(?:^|\n)A\.\s", block)
    if m0:
        stem = block[: m0.start()].strip()
    stem = re.sub(r"^\d{1,3}\s+", "", stem).strip()
    return stem, opts


def write_topic_mds(
    topic_map: dict[str, set[int]],
    questions: dict[int, str],
    answers: dict[int, tuple[str, str, str]],
) -> None:
    key_to_slug = {slug: name for num, name, slug in TOPIC_SECTIONS}
    for _num, name, slug in TOPIC_SECTIONS:
        nums = sorted(topic_map.get(slug, set()))
        parts = [f"# ESAP 2015 — {name.replace('_', ' ')}\n", f"Questions: {', '.join(map(str, nums))}\n\n"]
        for q in nums:
            parts.append(f"## Question {q}\n\n")
            parts.append(questions.get(q, "*[question text missing in OCR]*\n"))
            parts.append("\n\n")
            ans = answers.get(q)
            if ans:
                letter, line, discussion = ans
                parts.append(f"### Answer {q}: {letter}) {line}\n\n")
                parts.append(discussion)
                parts.append("\n\n")
        out = DEST / f"endo2015_chapter_{_num}_{name}.md"
        out.write_text(localize_images("".join(parts)), encoding="utf-8")
        print(f"  topic MD: {out.name} ({len(nums)} questions)")


def main() -> None:
    if not SRC_MD.exists():
        raise SystemExit(f"Missing source MD: {SRC_MD}")
    md_text = SRC_MD.read_text(encoding="utf-8")
    lines = md_text.splitlines(keepends=True)

    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)
    IMGS.mkdir(parents=True)

    # Structural splits
    for num, label, start_h, end_h in STRUCTURAL:
        text = slice_md(lines, start_h, end_h)
        if num == 1 and not text.strip().startswith("#"):
            text = "# ESAP 2015 — Front Matter\n\n" + text
        (DEST / f"endo2015_chapter_{num:02d}_{label}.md").write_text(text, encoding="utf-8")
        print(f"structural: endo2015_chapter_{num:02d}_{label}.md")

    # Optional JSON page slices (no image download)
    if SRC_JSON.exists():
        pages = json.loads(SRC_JSON.read_text(encoding="utf-8"))
        page_cuts = [0, 6, 10, 81, 205, len(pages)]
        for i, (num, label, *_rest) in enumerate(STRUCTURAL):
            chunk = pages[page_cuts[i] : page_cuts[i + 1]]
            (DEST / f"endo2015_chapter_{num:02d}_{label}.json").write_text(
                json.dumps(chunk, indent=2, ensure_ascii=False), encoding="utf-8"
            )

    q_md = (DEST / "endo2015_chapter_03_Questions_Part_I.md").read_text(encoding="utf-8")
    a_md = (DEST / "endo2015_chapter_04_Answers_Part_II.md").read_text(encoding="utf-8")
    questions = parse_questions(q_md)
    answers = parse_answers(a_md)
    print(f"parsed {len(questions)} questions, {len(answers)} answers")
    topic_map = build_topic_map(md_text, questions, {k: v[2] for k, v in answers.items()})
    write_topic_mds(topic_map, questions, answers)

    meta = {
        "questions": len(questions),
        "answers": len(answers),
        "topics": {slug: sorted(nums) for slug, nums in topic_map.items()},
    }
    (DEST / "endo2015_split_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print("Wrote endo2015_split_meta.json")


if __name__ == "__main__":
    main()
