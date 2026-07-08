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


TOPIC_PRIORITY = [
    "DIABETES",
    "LIPID-OBESITY",
    "BONE",
    "THYROID",
    "ADRENAL",
    "PITUITARY",
    "REPRODUCTION, FEMALE",
    "REPRODUCTION, MALE",
]


def build_topic_map(md: str, questions: dict[int, str], answers: dict[int, str]) -> dict[str, set[int]]:
    index = parse_index_assignments(md)
    topic_map = {slug: set() for slug in TOPIC_PRIORITY}

    # Each question → single topic (priority list resolves index overlaps)
    for q in range(1, 121):
        candidates = [slug for slug in TOPIC_PRIORITY if q in index.get(slug, set())]
        if candidates:
            topic_map[candidates[0]].add(q)
        else:
            key = classify_unassigned(q, questions.get(q, ""), answers.get(q, ""))
            topic_map[key].add(q)
    return topic_map


VIGNETTE_START = re.compile(
    r"(?:^|\n)(?:"
    r"A [0-9]{1,2}-year-old|"
    r"A [0-9]{1,2} year-old|"
    r"You are asked|You are consulted|You are requested|You are seeing|"
    r"A cardiologist|A nephrologist|A urologist|A radiologist|"
    r"The patient with|The daughter of|In addition to smoking|"
    r"During an appointment|On the basis of this"
    r")",
    re.MULTILINE,
)

NUMBERED_START = re.compile(
    r"(?:^|\n)(\d{1,3}) (?:A \d|A [a-z]|The |You |During |In addition|On the|A cardiologist|A nephrologist|A urologist)",
    re.MULTILINE,
)


def split_unnumbered_block(text: str, expected_count: int) -> list[str]:
    """Split a gap block into expected_count question vignettes."""
    if expected_count <= 0:
        return []
    if expected_count == 1:
        return [text.strip()] if text.strip() else []
    starts = [m.start() for m in VIGNETTE_START.finditer(text)]
    if len(starts) >= expected_count:
        parts = []
        for i in range(expected_count):
            s = starts[i]
            e = starts[i + 1] if i + 1 < len(starts) else len(text)
            parts.append(text[s:e].strip())
        return parts
    # fallback: split on option E. followed by capital letter vignette
    fallback = [m.start() for m in re.finditer(r"\nE\.[^\n]+\n\n(?=[A-Z])", text)]
    if len(fallback) + 1 >= expected_count:
        bounds = [0] + [m + 2 for m in fallback]
        parts = []
        for i in range(expected_count):
            s = bounds[i] if i < len(bounds) else 0
            e = bounds[i + 1] if i + 1 < len(bounds) else len(text)
            if i < len(parts) or s < len(text):
                chunk = text[s:e].strip()
                if chunk:
                    parts.append(chunk)
        if len(parts) == expected_count:
            return parts
    return [text.strip()] if expected_count == 1 and text.strip() else []


def parse_questions(part_i: str) -> dict[int, str]:
    m = re.search(r"Part I\s*", part_i)
    body = part_i[m.end():] if m else part_i

    markers: list[tuple[int, int]] = []
    seen_nums: set[int] = set()
    for m in NUMBERED_START.finditer(body):
        n = int(m.group(1))
        if 1 <= n <= 120 and n not in seen_nums:
            seen_nums.add(n)
            markers.append((m.start(1), n))
    markers.sort(key=lambda x: x[0])

    chunks: dict[int, str] = {}

    # Q1 before first numbered marker (usually unnumbered)
    if not markers or markers[0][1] != 1:
        end = markers[0][0] if markers else len(body)
        chunks[1] = body[:end].strip()

    for i, (pos, num) in enumerate(markers):
        end = markers[i + 1][0] if i + 1 < len(markers) else len(body)
        raw = body[pos:end].strip()
        raw = re.sub(r"^\d{1,3}\s+", "", raw)
        next_num = markers[i + 1][1] if i + 1 < len(markers) else 121
        gap = next_num - num
        if gap == 1:
            chunks[num] = raw
        else:
            # This span covers questions num..next_num-1
            sub = split_unnumbered_block(raw, gap)
            if len(sub) == gap:
                for off, piece in enumerate(sub):
                    chunks[num + off] = re.sub(r"^\d{1,3}\s+", "", piece).strip()
            else:
                chunks[num] = raw
                # try to recover middle unnumbered from remainder
                for missing in range(num + 1, next_num):
                    if missing not in chunks and sub:
                        idx = missing - num
                        if idx < len(sub):
                            chunks[missing] = sub[idx]

    return chunks


def parse_answers(part_ii: str) -> dict[int, tuple[str, str, str]]:
    """Return qnum -> (letter, answer_line, full_discussion)."""
    body = part_ii
    m = re.search(r"Part II\s*", body)
    body = body[m.end():] if m else body

    numbered = re.compile(
        r"(?:^|\n)(?:#{1,5}\s*)?(\d{1,3})\s+ANSWER:\s*([A-E])\)\s*([^\n]+)",
        re.MULTILINE,
    )
    unnumbered_q1 = re.compile(
        r"(?:^|\n)#{1,5}\s*ANSWER:\s*([A-E])\)\s*([^\n]+)",
        re.MULTILINE,
    )

    hits: list[tuple[int, int, str, str]] = []  # start, qnum, letter, line
    for match in numbered.finditer(body):
        qnum = int(match.group(1))
        if 1 <= qnum <= 120:
            hits.append((match.start(), qnum, match.group(2), match.group(3)))
    m1 = unnumbered_q1.search(body)
    if m1 and not any(h[1] == 1 for h in hits):
        hits.append((m1.start(), 1, m1.group(1), m1.group(2)))

    hits.sort(key=lambda x: x[0])
    out: dict[int, tuple[str, str, str]] = {}
    for i, (start, qnum, letter, line) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else len(body)
        if qnum not in out:
            out[qnum] = (letter, line, body[start:end].strip())
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
