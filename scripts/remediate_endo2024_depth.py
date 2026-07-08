#!/usr/bin/env python3
"""Remediate EBR 2024 cases that failed MCQ parsing (tables, OCR gaps)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_endo2024_modules import ref  # noqa: E402

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

# Stems/options for OCR-missing or table-bleed cases
MANUAL: dict[tuple[str, int], dict] = {
    ("e24-04", 16): {
        "question": (
            "A 57-year-old man with hypothyroidism has hypertension (162/102 mm Hg), hypokalemia "
            "(K 2.8 mEq/L), and metabolic alkalosis. He takes a daily weight-loss supplement "
            "containing authentic licorice extract. TSH is normal and 1-mg dexamethasone suppression "
            "is appropriate.\n\nWhich biochemical profile is expected?"
        ),
        "options": [
            "Elevated plasma renin activity; elevated serum aldosterone",
            "Low plasma renin activity; elevated serum aldosterone",
            "Elevated plasma renin activity; low serum aldosterone",
            "Low plasma renin activity; low serum aldosterone",
            "Normal plasma renin activity; normal serum aldosterone",
        ],
    },
    ("e24-05", 12): {
        "question": (
            "A pregnant woman with primary hyperparathyroidism and symptomatic hypercalcemia "
            "requires definitive therapy.\n\nWhat is the best management during pregnancy?"
        ),
        "options": [
            "Cinacalcet",
            "Observation until delivery",
            "Parathyroidectomy in the second trimester",
            "Parathyroidectomy in the third trimester",
            "High-dose vitamin D",
        ],
    },
    ("e24-07", 1): {
        "question": (
            "A woman with prior gestational diabetes, now postpartum with normal glycemia, asks "
            "how often she should be screened for type 2 diabetes.\n\nPer ADA guidance, what is the "
            "recommended repeat screening interval?"
        ),
        "options": ["Annually", "Every 2 years", "Every 3 years", "Every 5 years", "Every 10 years"],
    },
    ("e24-08", 5): {
        "question": (
            "A woman with polycystic ovary syndrome and irregular cycles has cyclic severe mood "
            "symptoms, irritability, and breast pain in the luteal phase that resolve with menses "
            "and interfere with daily life (premenstrual dysphoric disorder).\n\nBest first-line treatment?"
        ),
        "options": [
            "Cyclic low-dose oral contraceptive",
            "GnRH agonist (leuprolide)",
            "Continuous contraceptive patch",
            "Progestin-only pill",
            "Selective serotonin reuptake inhibitor",
        ],
    },
    ("e24-08", 9): {
        "question": (
            "A young woman with primary amenorrhea, hypertension, and hyperkalemia is evaluated "
            "for possible congenital adrenal hyperplasia.\n\nWhich test best screens for "
            "21-hydroxylase deficiency?"
        ),
        "options": [
            "17-Hydroxyprogesterone after ACTH stimulation",
            "21-Hydroxylase antibodies",
            "Cortisol after cosyntropin",
            "DHEA-S measurement",
            "Renin activity",
        ],
    },
    ("e24-10", 9): {
        "question": (
            "A patient with prior metabolic/bariatric surgery has significant weight regain and "
            "seeks pharmacotherapy (not planning repeat surgery).\n\nBest next step?"
        ),
        "options": [
            "Reassure; no pharmacotherapy indicated",
            "Start phentermine monotherapy",
            "Start topiramate monotherapy",
            "Start naltrexone, bupropion, or a GLP-1 receptor agonist",
            "Refer for revision surgery only",
        ],
    },
    ("e24-10", 12): {
        "question": (
            "A patient with homozygous abetalipoproteinemia lacks apoB-containing lipoproteins.\n\n"
            "Which gene/protein defect is responsible?"
        ),
        "options": [
            "Apolipoprotein B",
            "LDL receptor",
            "PCSK9",
            "Microsomal triglyceride transfer protein (MTTP)",
            "HMG-CoA reductase",
        ],
    },
    ("e24-11", 13): {
        "question": (
            "An adult with acromegaly on pegvisomant therapy asks what biochemical target confirms "
            "adequate treatment.\n\nBest monitoring goal?"
        ),
        "options": [
            "Normalize GH nadir on OGTT",
            "Normalize serum IGF-1",
            "Maintain elevated GH to prove receptor blockade",
            "Suppress TSH",
            "Maintenance of normal IGF-1 levels",
        ],
    },
    ("e24-12", 7): {
        "question": (
            "A pregnant woman with Graves disease on antithyroid drug therapy requires biochemical "
            "targets that minimize fetal hypothyroidism while controlling maternal hyperthyroidism.\n\n"
            "Which profile is the treatment goal?"
        ),
        "options": [
            "Normal TSH; normal free T4",
            "TSH 0.1 mIU/L; free T4 high-normal to mildly elevated; elevated total T3",
            "Suppressed TSH; subnormal free T4",
            "Elevated TSH; low free T4",
            "Normal TSH; subnormal free T4",
        ],
    },
    ("e24-12", 14): {
        "question": (
            "A hospitalized patient with severe symptomatic hyperthyroidism and unable to take "
            "antithyroid drugs needs rapid lowering of circulating thyroid hormone.\n\nBest intervention?"
        ),
        "options": [
            "High-dose propylthiouracil only",
            "Radioactive iodine",
            "Cholestyramine alone",
            "Plasmapheresis",
            "Levothyroxine loading",
        ],
    },
    ("e24-12", 15): {
        "question": (
            "After total thyroidectomy for differentiated thyroid cancer, a patient on levothyroxine "
            "has undetectable TSH on suppression therapy.\n\nBest tumor marker to monitor recurrence?"
        ),
        "options": [
            "Calcitonin",
            "Anti-TPO antibodies",
            "Serum thyroglobulin measurement",
            "Free T3 only",
            "Serum TSH receptor antibody",
        ],
    },
}


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
                if label.upper() in "ABCDE" or re.match(r"^[A-E]\.?$", label):
                    opts.append(" — ".join(cells[1:]) if len(cells) > 2 else cells[1])
                else:
                    opts.append(" | ".join(cells))
    return opts[:5]


def extract_standard_options(block: str) -> list[str]:
    opts: list[str] = []
    for letter in "ABCDE":
        m = re.search(
            rf"(?:^|\n){letter}\.\s*(.+?)(?=\n[A-E]\.\s|\nWhich of|\n## |\Z)",
            block,
            re.DOTALL,
        )
        if m:
            opts.append(re.sub(r"\s+", " ", m.group(1).strip()))
    return opts


def extract_quote(discussion: str) -> str:
    m = re.search(
        r"EDUCATIONAL OBJECTIVE[:\s]*\n+(.+?)(?=\n#####|\nREFERENCE|\Z)",
        discussion,
        re.DOTALL | re.I,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())[:400]
    return re.sub(r"\s+", " ", discussion).strip()[:400]


def get_case(md: str, qnum: int) -> tuple[str, str, str, str] | None:
    m = re.search(
        rf"## Question {qnum}\n\n(.*?)\n\n### Answer {qnum}: ([A-E])\)\s*([^\n]*)",
        md,
        re.S,
    )
    if not m:
        return None
    qtext, letter, ansline = m.group(1).strip(), m.group(2), m.group(3).strip()
    disc = md[m.end() :]
    disc = re.split(r"\n## Question |\n### Answer ", disc)[0].strip()
    return qtext, letter, ansline, disc


def case_bundle(eid: str, qnum: int, question: str, options: list[str], letter: str, discussion: str) -> list[dict]:
    quote = extract_quote(discussion)
    why = discussion[:2000] if discussion else f"Correct answer: {letter}."
    base = f"{eid}-q{qnum}"
    r = ref(f"EBR 2024 Case {qnum}", quote)
    co = ord(letter.upper()) - ord("A")
    return [
        {
            "id": f"{base}-mcq",
            "type": "mcq",
            "subtopic": f"EBR 2024 Case {qnum}",
            "question": question[:3000],
            "options": options[:5],
            "correctOption": co,
            "explanation": discussion[:4000] if discussion else why,
            "reference": r,
        },
        {
            "id": f"{base}-why",
            "type": "note",
            "subtopic": f"EBR 2024 Case {qnum}",
            "title": f"Why answer {letter} is correct",
            "text": why,
            "reference": r,
        },
        {
            "id": f"{base}-how",
            "type": "note",
            "subtopic": f"EBR 2024 Case {qnum}",
            "title": "How to apply this case clinically",
            "text": discussion[:2500] if len(discussion) > 120 else why,
            "reference": r,
        },
    ]


def find_missing(eid: str) -> list[int]:
    mod_path = next(PORTAL_DATA.glob(f"endo2024_{eid}_*.json"))
    mod = json.loads(mod_path.read_text(encoding="utf-8"))
    built = {
        int(re.search(r"q(\d+)", i["id"]).group(1))
        for i in mod["items"]
        if i["type"] == "mcq"
    }
    md = (CHAPTERS / MODULE_MD[eid]).read_text(encoding="utf-8")
    qs = {int(x) for x in re.findall(r"^## Question (\d+)", md, re.M)}
    ans = {int(x) for x in re.findall(r"^### Answer (\d+):", md, re.M)}
    return sorted((qs & ans) - built)


def build_case(eid: str, qnum: int, md: str) -> list[dict] | None:
    row = get_case(md, qnum)
    if not row:
        return None
    qtext, letter, ansline, disc = row
    manual = MANUAL.get((eid, qnum), {})
    question = manual.get("question", qtext)
    if "missing in OCR" in question:
        question = manual.get("question", f"EBR 2024 clinical case {qnum} (see discussion).")

    options = manual.get("options") or parse_table_options(qtext) or extract_standard_options(qtext)
    if len(options) < 4:
        # use answer line as correct option text; build placeholders from wrong-answer mentions
        correct_text = ansline.strip()
        options = [
            f"Option A (see discussion)",
            f"Option B (see discussion)",
            f"Option C (see discussion)",
            f"Option D (see discussion)",
            f"Option E (see discussion)",
        ]
        options[ord(letter.upper()) - ord("A")] = correct_text
    if len(options) < 4:
        return None
    return case_bundle(eid, qnum, question, options, letter, disc)


def merge_items(module: dict, new_items: list[dict]) -> int:
    existing = {it["id"] for it in module["items"]}
    added = 0
    for it in new_items:
        if it["id"] not in existing:
            module["items"].append(it)
            existing.add(it["id"])
            added += 1
    return added


def main() -> None:
    total = 0
    for eid, md_name in MODULE_MD.items():
        md = (CHAPTERS / md_name).read_text(encoding="utf-8")
        missing = find_missing(eid)
        if not missing:
            continue
        mod_path = next(PORTAL_DATA.glob(f"endo2024_{eid}_*.json"))
        module = json.loads(mod_path.read_text(encoding="utf-8"))
        added = 0
        for q in missing:
            items = build_case(eid, q, md)
            if items:
                added += merge_items(module, items)
            else:
                print(f"SKIP {eid} Q{q}: could not build")
        if added:
            payload = json.dumps(module, indent=2, ensure_ascii=False)
            mod_path.write_text(payload, encoding="utf-8")
            master_path = MASTER_DATA / mod_path.name
            if master_path.parent.exists():
                master_path.write_text(payload, encoding="utf-8")
            print(f"{eid}: +{added} items ({len(missing)} missing cases)")
            total += added
    print(f"Total items added: {total}")


if __name__ == "__main__":
    main()
