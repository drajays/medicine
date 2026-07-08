#!/usr/bin/env python3
"""Split Endocrine Board Review 2024 OCR into chapter MD + JSON under endo2024_chapters/."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = Path("/Users/dr.ajayshukla/endo_masterapp")
SRC_MD = MASTER / "endo2024" / "endo2024.pdf_by_PaddleOCR-VL-1.6.md"
SRC_JSON = MASTER / "endo2024" / "endo2024.pdf_by_PaddleOCR-VL-1.6.json"
DEST = MASTER / "endo2024_chapters"

STRUCTURAL = [
    (1, "Front_Matter", None, "# LABORATORY REFERENCE RANGES"),
    (2, "Laboratory_Reference_Ranges", "# LABORATORY REFERENCE RANGES", "# COMMON ABBREVIATIONS"),
    (3, "Common_Abbreviations", "# COMMON ABBREVIATIONS", "## ENDOCRINE BOARD REVIEW"),
]

TOPIC_SECTIONS = [
    (4, "Adrenal", "Adrenal Board Review"),
    (5, "Bone", "Bone Board Review"),
    (6, "Diabetes_Section_1", "Diabetes Mellitus, Section 1 Board Review"),
    (7, "Diabetes_Section_2", "Diabetes Mellitus, Section 2 Board Review"),
    (8, "Female_Reproduction", "Female Reproduction Board Review"),
    (9, "Male_Reproduction", "Male Reproduction Board Review"),
    (10, "Lipids_and_Obesity", "Lipids & Obesity Board Review"),
    (11, "Pituitary", "Pituitary Board Review"),
    (12, "Thyroid_Section_1", "Thyroid, Section 1 Board Review"),
    (13, "Thyroid_Section_2", "Thyroid, Section 2 Board Review"),
]

Q_START = "## ENDOCRINE BOARD REVIEW"
A_START = "## ENDOCRINE BOARD REVIEW"

VIGNETTE_START = re.compile(
    r"(?:^|\n)(?:"
    r"\d{1,2} (?:A [0-9]{1,2}-year|A [0-9]{1,2} year|Which |You |The |During |In |On |A cardiologist|"
    r"A nephrologist|A urologist|A radiologist|A woman|A man|An |"
    r"Following |After |Before |Despite |Because )"
    r")",
    re.MULTILINE,
)

ANSWER_RE = re.compile(
    r"(?:^|\n)(?:#{1,4}\s*)?(\d{1,2})\s+ANSWER:\s*([A-E])\)\s*([^\n]+)",
    re.MULTILINE | re.IGNORECASE,
)
ANSWER_Q1_RE = re.compile(
    r"(?:^|\n)#{1,4}\s*ANSWER:\s*([A-E])\)\s*([^\n]+)",
    re.MULTILINE | re.IGNORECASE,
)


def localize_images(text: str) -> str:
    pattern = r'https://[a-zA-Z0-9.-]+\.bcebos\.com/[^"\s>]+?/imgs/([^"\s>?]+)(?:\?[^"\s>]*)?'
    return re.sub(pattern, r"imgs/\1", text)


def heading_match(line: str, heading: str | None) -> bool:
    if not heading:
        return False
    stripped = line.strip()
    if stripped == heading:
        return True
    if heading.startswith("#") and stripped.startswith("#"):
        return heading.lower() in stripped.lower()
    return heading.lower() in stripped.lower()


def slice_md(lines: list[str], start_heading: str | None, end_heading: str | None) -> str:
    start = 0
    if start_heading:
        for i, line in enumerate(lines):
            if heading_match(line, start_heading):
                start = i
                break
    end = len(lines)
    if end_heading:
        for i in range(start + 1, len(lines)):
            stripped = lines[i].strip()
            if heading_match(lines[i], end_heading):
                end = i
                break
            if end_heading.startswith("##") and stripped.startswith("## ENDOCRINE BOARD REVIEW"):
                if i > start + 50:
                    end = i
                    break
    return localize_images("".join(lines[start:end]))


def find_section_bounds(md: str) -> tuple[int, int, int]:
    """Return (questions_start, answers_start, end) char offsets."""
    q_pos = md.find(Q_START)
    if q_pos < 0:
        raise ValueError("Questions block not found")
    a_pos = md.find(A_START, q_pos + len(Q_START))
    if a_pos < 0:
        raise ValueError("Answers block not found")
    return q_pos, a_pos, len(md)


def classify_topic_header(line: str) -> str | None:
    """Map a # ... Board Review heading to chapter slug."""
    h = line.strip().lstrip("#").strip().lower()
    if "adrenal board review" in h and "diabetes" not in h:
        return "Adrenal"
    if h.startswith("bone board review"):
        return "Bone"
    if "diabetes mellitus" in h and "section 1" in h:
        return "Diabetes_Section_1"
    if "diabetes mellitus" in h and "section 2" in h:
        return "Diabetes_Section_2"
    if "female reproduction" in h:
        return "Female_Reproduction"
    if "male reproduction" in h:
        return "Male_Reproduction"
    if "lipids" in h and "obesity" in h:
        return "Lipids_and_Obesity"
    if h.startswith("pituitary board review"):
        return "Pituitary"
    if "thyroid" in h and "section 1" in h:
        return "Thyroid_Section_1"
    if "thyroid" in h and "section 2" in h:
        return "Thyroid_Section_2"
    return None


def split_topic_blocks(text: str) -> dict[str, str]:
    """Split questions or answers region into per-topic text blocks."""
    header_re = re.compile(r"^#\s+.+Board\s+Review.*$", re.MULTILINE | re.IGNORECASE)
    hits: list[tuple[int, str]] = []
    for m in header_re.finditer(text):
        line = m.group(0)
        slug = classify_topic_header(line)
        if slug:
            hits.append((m.start(), slug))
    hits.sort(key=lambda x: x[0])
    out: dict[str, str] = {}
    for i, (start, slug) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else len(text)
        out[slug] = text[start:end].strip()
    return out


def parse_questions_in_block(block: str) -> dict[int, str]:
    """Parse numbered questions within one topic block."""
    block = re.sub(r"^## (\d{1,2}) ", r"\n\1 ", block, flags=re.MULTILINE)

    numbered = list(re.finditer(r"(?:^|\n)(\d{1,2}) ", block))
    chunks: dict[int, str] = {}
    for i, m in enumerate(numbered):
        qnum = int(m.group(1))
        if not (1 <= qnum <= 60):
            continue
        end = numbered[i + 1].start() if i + 1 < len(numbered) else len(block)
        body = block[m.start() : end].strip()
        body = re.sub(r"^\d{1,2}\s+", "", body, count=1).strip()
        if len(body) > 40:
            chunks[qnum] = body

    # Thyroid section 1 Q1 is sometimes unnumbered in OCR
    if not chunks and block.strip():
        m0 = re.search(
            r"(?:^|\n)(A \d{1,2}-year-old|A \d{1,2} year-old|You are|Which of the following)",
            block,
        )
        if m0:
            chunks[1] = block[m0.start() :].strip()
    elif 1 not in chunks:
        pre = block[: numbered[0].start()].strip() if numbered else ""
        if re.search(r"A \d{1,2}-year-old|Which of the following", pre):
            chunks[1] = pre
    return chunks


def parse_answers_in_block(block: str) -> dict[int, tuple[str, str, str]]:
    """Return qnum -> (letter, answer_line, full_discussion)."""
    hits: list[tuple[int, int, str, str]] = []
    for m in ANSWER_RE.finditer(block):
        qnum = int(m.group(1))
        if 1 <= qnum <= 60:
            hits.append((m.start(), qnum, m.group(2).upper(), m.group(3).strip()))

    m1 = ANSWER_Q1_RE.search(block)
    if m1 and not any(h[1] == 1 for h in hits):
        hits.append((m1.start(), 1, m1.group(1).upper(), m1.group(2).strip()))

    hits.sort(key=lambda x: x[0])
    out: dict[int, tuple[str, str, str]] = {}
    for i, (start, qnum, letter, line) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else len(block)
        if qnum not in out:
            out[qnum] = (letter, line, block[start:end].strip())
    return out


def write_topic_md(num: int, slug: str, title: str, questions: dict[int, str], answers: dict[int, tuple[str, str, str]]) -> None:
    nums = sorted(set(questions) | set(answers))
    parts = [
        f"# Endocrine Board Review 2024 — {title.replace('_', ' ')}\n",
        f"Questions: {', '.join(map(str, nums))}\n\n",
    ]
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
    out = DEST / f"endo2024_chapter_{num:02d}_{slug}.md"
    out.write_text("".join(parts), encoding="utf-8")
    print(f"  topic MD: {out.name} ({len(nums)} Q, {len(answers)} A)")


def page_markdown(page: dict) -> str:
    md = page.get("markdown", "")
    if isinstance(md, dict):
        return md.get("text", "") or json.dumps(md)
    return str(md) if md else ""


def assign_json_pages(pages: list[dict], md_text: str, chapter_files: list[tuple[str, str]]) -> dict[str, list[int]]:
    """Map chapter slug -> page indices using proportional char offsets in source MD."""
    n = len(pages)
    total = max(len(md_text), 1)
    markers: list[tuple[int, str]] = []
    for slug, needle in chapter_files:
        pos = md_text.lower().find(needle.lower())
        if pos >= 0:
            markers.append((pos, slug))
    markers.sort(key=lambda x: x[0])
    assignment: dict[str, list[int]] = {slug: [] for slug, _ in chapter_files}
    for i, (start_pos, slug) in enumerate(markers):
        end_pos = markers[i + 1][0] if i + 1 < len(markers) else len(md_text)
        p0 = int(start_pos / total * n)
        p1 = int(end_pos / total * n)
        assignment[slug] = list(range(p0, max(p0 + 1, p1)))
    return assignment


def main() -> None:
    if not SRC_MD.exists():
        raise SystemExit(f"Missing source MD: {SRC_MD}")
    md_text = SRC_MD.read_text(encoding="utf-8")
    lines = md_text.splitlines(keepends=True)

    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)
    (DEST / "imgs").mkdir(parents=True)

    for num, label, start_h, end_h in STRUCTURAL:
        text = slice_md(lines, start_h, end_h)
        if num == 1 and "OVERVIEW" not in text:
            text = "# Endocrine Board Review 2024 — Front Matter\n\n" + text
        (DEST / f"endo2024_chapter_{num:02d}_{label}.md").write_text(text, encoding="utf-8")
        print(f"structural: endo2024_chapter_{num:02d}_{label}.md")

    q_pos, a_pos, end = find_section_bounds(md_text)
    q_region = md_text[q_pos:a_pos]
    a_region = md_text[a_pos:end]

    q_blocks = split_topic_blocks(q_region)
    a_blocks = split_topic_blocks(a_region)

    # Female answers use lowercase header variant
    if "Female_Reproduction" not in a_blocks:
        m = re.search(r"#\s*female\s+Reproduction\s+Board\s+Review", a_region, re.I)
        if m:
            rest = a_region[m.start() :]
            nxt = re.search(r"#\s*Male\s+Reproduction\s+Board\s+Review", rest, re.I)
            a_blocks["Female_Reproduction"] = rest[: nxt.start() if nxt else len(rest)].strip()

    # Thyroid section 2 answers lowercase header
    if "Thyroid_Section_2" not in a_blocks:
        m = re.search(r"#\s*thyroid,\s*Section\s*2\s+Board\s+Review", a_region, re.I)
        if m:
            a_blocks["Thyroid_Section_2"] = a_region[m.start() :].strip()

    all_meta: dict = {"topics": {}}
    for num, slug, title in TOPIC_SECTIONS:
        qs = parse_questions_in_block(q_blocks.get(slug, ""))
        ans = parse_answers_in_block(a_blocks.get(slug, ""))
        write_topic_md(num, slug, title, qs, ans)
        all_meta["topics"][slug] = {
            "questions": sorted(qs),
            "answers": sorted(ans),
            "mcq_parsed": len([q for q in qs if q in ans]),
        }

    if SRC_JSON.exists():
        pages = json.loads(SRC_JSON.read_text(encoding="utf-8"))
        markers_for_pages: list[tuple[str, str]] = [
            ("Front_Matter", "ENDOCRINE BOARD 16TH EDITION REVIEW 2024"),
            ("Laboratory_Reference_Ranges", "# LABORATORY REFERENCE RANGES"),
            ("Common_Abbreviations", "# COMMON ABBREVIATIONS USED IN ENDOCRINE BOARD REVIEW"),
            ("Adrenal", "# Adrenal Board Review Tobias"),
            ("Bone", "# Bone Board Review\n\n# Natalie"),
            ("Diabetes_Section_1", "# Diabetes Mellitus, Section 1 Board Review"),
            ("Diabetes_Section_2", "# Diabetes Mellitus, Section 2 Board Review"),
            ("Female_Reproduction", "# Female Reproduction Board Review"),
            ("Male_Reproduction", "# Male Reproduction Board Review"),
            ("Lipids_and_Obesity", "# Lipids & Obesity Board Review"),
            ("Pituitary", "# Pituitary Board Review\n\n# John David"),
            ("Thyroid_Section_1", "# Thyroid, Section 1 Board Review"),
            ("Thyroid_Section_2", "# Thyroid, Section 2 Board Review Kaniksha"),
        ]
        assignment = assign_json_pages(pages, md_text, markers_for_pages)
        for num, label, *_ in STRUCTURAL:
            idxs = assignment.get(label, [])
            chunk = [pages[i] for i in idxs if i < len(pages)]
            (DEST / f"endo2024_chapter_{num:02d}_{label}.json").write_text(
                json.dumps(chunk, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            print(f"  JSON slice: endo2024_chapter_{num:02d}_{label}.json ({len(chunk)} pages)")
        for num, slug, title in TOPIC_SECTIONS:
            idxs = assignment.get(slug, [])
            chunk = [pages[i] for i in idxs if i < len(pages)]
            (DEST / f"endo2024_chapter_{num:02d}_{slug}.json").write_text(
                json.dumps(chunk, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            print(f"  JSON slice: endo2024_chapter_{num:02d}_{slug}.json ({len(chunk)} pages)")

    total_q = sum(len(v["questions"]) for v in all_meta["topics"].values())
    total_a = sum(len(v["answers"]) for v in all_meta["topics"].values())
    all_meta["total_questions"] = total_q
    all_meta["total_answers"] = total_a
    (DEST / "endo2024_split_meta.json").write_text(json.dumps(all_meta, indent=2), encoding="utf-8")
    print(f"Parsed {total_q} questions, {total_a} answers → endo2024_split_meta.json")


if __name__ == "__main__":
    main()
