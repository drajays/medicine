# Endocrinology Master — Content Upload Plan

Structured pipeline to bring **`endo_masterapp`** to Harrison-quality production inside the Medicine portal (`/medicine/endo/` sub-app).

## Current inventory

| Tree | Entries | Source | On portal | Quality |
|------|---------|--------|-----------|---------|
| ESAP 2021 | 43 (`e21-01`–`e21-43`) | ✅ MD split | ✅ `endo/data/` | ✅ 43/43 remediated |
| Williams 15e | 49 (`w15-00`–`w15-48`) | ✅ MD split | ✅ `endo/data/` | ✅ 34/48 authored · ⏳ w15-00 skip |
| ESAP 2015 | 4 placeholders | ⚠️ OCR only | ❌ | ❌ Wrong TOC |
| Hot Topics / Cases / Trials | 0 | — | — | Empty |

**Authoring workspace:** `/Users/dr.ajayshukla/endo_masterapp`  
**Published copy:** `/Users/dr.ajayshukla/harrison_app/endo/data/`  
**Push:** content-only (no React rebuild)

## Architecture

```
williams_2024_chapters/*.md  →  validate  →  endo_masterapp/data/*.json
                                              ↓ sync_endo_to_medicine.sh
                                    harrison_app/endo/data/*.json  →  git push
```

## Quality target (Harrison / mcq_skill)

| Type | ESAP module | Williams chapter |
|------|-------------|------------------|
| notes | 10–18 | 26–30 |
| mcq | 12–18 (4 options) | 26–30 |
| true_false | 8–10 | 12–14 |
| assertion_reason | 8–10 | 12 |

- ≥50% of **notes** titled Why/How
- Every item: verbatim `reference` with section heading
- MCQ: `question` field, 4 options, `correctOption` 0–3
- AI scripts: preserve `distillation_trace` when used

## Phase 0 — Foundation

- [x] `CONTENT_UPLOAD_PLAN.md` (this file)
- [x] `.claude/skills/endo_mcq_skill/SKILL.md`
- [x] `scripts/validate_endo_json.py`
- [x] `scripts/sync_endo_to_medicine.sh`
- [x] Catalog title fixes in `data/index.json`

## Phase 1 — ESAP 2021 remediation (43 modules)

**Order:**

1. e21-05–08 (Adrenal)
2. e21-09–15 (Bone)
3. e21-17–20 (Diabetes)
4. e21-21–27 (Pituitary/NET)
5. e21-28–31 (Pediatric)
6. e21-32–36 (Reproductive) ✅
7. e21-38–43 (Thyroid/interfaces) ✅
8. e21-01–04 (Obesity/lipids) ✅

**Per module:** read MD → write JSON → validate → sync → commit (one module per commit).

| Module | Status | Items | Why/How |
|--------|--------|-------|---------|
| e21-06 Cushing | ✅ remediated | 41 | 67% |
| e21-05 Adrenal replacement | ✅ remediated | 41 | 67% |
| e21-07 Genetic screening | ✅ remediated | 41 | 83% |
| e21-08 Critical illness AI | ✅ remediated | 41 | 92% |
| e21-09 Bone & mineral metabolism | ✅ remediated | 41 | 75% |
| e21-10 Hypophosphatemia | ✅ remediated | 41 | 100% |
| e21-11 Challenging mineral disease | ✅ remediated | 41 | 92% |
| e21-12 Bone turnover markers | ✅ remediated | 41 | 83% |
| e21-13 Personalize osteoporosis | ✅ remediated | 41 | 92% |
| e21-14 Vitamin D level/dosage | ✅ remediated | 41 | 92% |
| e21-15 Stopping bone meds | ✅ remediated | 41 | 100% |
| e21-17 CGM/pump clinic visit | ✅ remediated | 41 | 67% |
| e21-18 Genetic diabetes | ✅ remediated | 41 | 50% |
| e21-19 GLP-1 RA / SGLT2i CV outcomes | ✅ remediated | 41 | 50% |
| e21-20 NAFLD/NASH pharmacology | ✅ remediated | 41 | 50% |
| e21-16 Paget disease of bone | ✅ remediated | 41 | 58% |
| e21-21 Pseudoacromegaly syndromes | ✅ remediated | 41 | 58% |
| e21-22 Carcinoid crisis | ✅ remediated | 41 | 67% |
| e21-23 Acromegaly complications | ✅ remediated | 41 | 58% |
| e21-24 Dopamine agonist risks | ✅ remediated | 41 | 58% |
| e21-25 Functioning gonadotroph adenomas | ✅ remediated | 41 | 50% |
| e21-26 Pituitary hormone transition | ✅ remediated | 41 | 67% |
| e21-27 Pediatric bone fragility | ✅ remediated | 41 | 67% |
| e21-28 DI in children | ✅ remediated | 41 | 67% |
| e21-29 ALD newborn screening | ✅ remediated | 41 | 58% |
| e21-30 Youth-onset T2DM | ✅ remediated | 41 | 75% |
| e21-31 Pediatric dyslipidemia | ✅ remediated | 41 | 58% |
| e21-32 Functional hypogonadism (male) | ✅ remediated | 41 | 83% |
| e21-33 AMH & ovarian reserve | ✅ remediated | 41 | 75% |
| e21-34 HRT in post-reproductive women | ✅ remediated | 41 | 91% |
| e21-35 Androgenic PED abuse | ✅ remediated | 41 | 91% |
| e21-36 Male infertility | ✅ remediated | 41 | 91% |
| e21-38 Discordant TFTs | ✅ remediated | 41 | 83% |
| e21-39 Hemithyroidectomy surveillance | ✅ remediated | 41 | 75% |
| e21-40 Thyroid in pregnancy | ✅ remediated | 41 | 83% |
| e21-41 Endo–oncology interface | ✅ remediated | 41 | 100% |
| e21-42 ICI endocrine effects | ✅ remediated | 41 | 67% |
| e21-43 Endo–psychiatry interface | ✅ remediated | 41 | 92% |
| e21-01 Advanced lipoprotein testing | ✅ remediated | 41 | 67% |
| e21-02 Nutritional/medical obesity | ✅ remediated | 41 | 75% |
| e21-03 Medication weight effects | ✅ remediated | 41 | 67% |
| e21-04 Bariatric surgery | ✅ remediated | 41 | 67% |
| e21-37 Thyroid cancer (MTC) | ✅ remediated | 41 | 83% |

**Phase 1 ESAP 2021: 43/43 modules complete** (~1,763 items)

## Phase 2 — Williams 15e (49 chapters)

Batches A–J (w15-01 → w15-48). Skip or minimal w15-00 Front Matter.

| Module | Status | Items | Why/How |
|--------|--------|-------|---------|
| w15-01 Principles of Endocrinology | ✅ authored | 77 | 54% |
| w15-02 Principles of Hormone Action | ✅ authored | 77 | 54% |
| w15-03 Genetics of Endocrinology | ✅ authored | 77 | 54% |
| w15-04 Laboratory Techniques | ✅ authored | 77 | 58% |
| w15-05 Neuroendocrinology | ✅ authored | 77 | 54% |
| w15-06 Pituitary physiology & diagnostics | ✅ authored | 77 | 54% |
| w15-07 Pituitary adenomas & masses | ✅ authored | 77 | 58% |
| w15-08 Posterior pituitary | ✅ authored | 77 | 65% |
| w15-09 Thyroid pathophysiology & diagnostics | ✅ authored | 77 | 54% |
| w15-10 Hyperthyroid disorders | ✅ authored | 77 | 58% |
| w15-11 Hypothyroidism & thyroiditis | ✅ authored | 77 | 58% |
| w15-12 Goiter, nodules & thyroid cancer | ✅ authored | 77 | 54% |
| w15-13 The adrenal cortex | ✅ authored | 77 | 54% |
| w15-14 Endocrine hypertension | ✅ authored | 77 | 73% |
| w15-15 Female reproductive axis | ✅ authored | 77 | 62% |
| w15-16 Hormonal contraception | ✅ authored | 77 | 58% |
| w15-17 Testicular disorders | ✅ authored | 77 | 62% |
| w15-18 Sexual function & dysfunction | ✅ authored | 77 | 62% |
| w15-19 Endocrine changes in pregnancy | ✅ authored | 77 | 65% |
| w15-20 Fetal endocrine development | ✅ authored | 77 | 58% |
| w15-21 Differences of sex development | ✅ authored | 77 | 62% |
| w15-22 Normal & aberrant growth in children | ✅ authored | 77 | 85% |
| w15-23 Physiology & disorders of puberty | ✅ authored | 77 | 73% |
| w15-24 Transgender endocrinology | ✅ authored | 77 | 77% |
| w15-25 Hormones & athletic performance | ✅ authored | 77 | 73% |
| w15-26 Endocrine function & aging | ✅ authored | 77 | 88% |
| w15-27 Hormones & disorders of mineral metabolism | ✅ authored | 77 | 100% |
| w15-28 Endocrine functions of bone | ✅ authored | 77 | 85% |
| w15-29 Osteoporosis: basic & clinical aspects | ✅ authored | 77 | 62% |
| w15-30 Rickets & osteomalacia | ✅ authored | 77 | 62% |
| w15-31 Kidney stones | ✅ authored | 77 | 100% |
| w15-32 Physiology of insulin secretion | ✅ authored | 77 | 100% |
| w15-33 Pathophysiology of T2DM | ✅ authored | 77 | 100% |
| w15-34 Therapeutics of T2DM | ✅ authored | 77 | 100% |

**Phase 2 Williams 15e: 34/48 chapters complete** (~2,618 items)

## Phase 3 — ESAP 2015

Re-split `noupload/endo2015/` → proper module TOC → author.

## Phase 4 — Optional

Hot topics, case reports, trials; React migration to main `data/` catalog.

## Commit discipline

Stage only changed JSON + `index.json`. Never `git add -A`. One module per commit.

## Progress log

| Date | Module | Items | Why/How % | Commit |
|------|--------|-------|-----------|--------|
| 2026-07-07 | e21-06 | 41 | 67% | pending |
| 2026-07-07 | e21-05 | 41 | 67% | pending |
| 2026-07-07 | e21-07 | 41 | 83% | pending |
| 2026-07-07 | e21-08 | 41 | 92% | pending |
| 2026-07-07 | e21-09 | 41 | 75% | pending |
| 2026-07-07 | e21-10 | 41 | 100% | pending |
| 2026-07-07 | e21-11 | 41 | 92% | pending |
| 2026-07-07 | e21-12 | 41 | 83% | pending |
| 2026-07-07 | e21-13 | 41 | 92% | pending |
| 2026-07-07 | e21-14 | 41 | 92% | pending |
| 2026-07-07 | e21-15 | 41 | 100% | pending |
| 2026-07-07 | e21-17 | 41 | 67% | pending |
| 2026-07-07 | e21-18 | 41 | 50% | pending |
| 2026-07-07 | e21-19 | 41 | 50% | pending |
| 2026-07-07 | e21-20 | 41 | 50% | pending |
| 2026-07-07 | e21-16 | 41 | 58% | pending |
| 2026-07-07 | e21-21 | 41 | 58% | pending |
| 2026-07-07 | e21-22 | 41 | 67% | pending |
| 2026-07-07 | e21-23 | 41 | 58% | pending |
| 2026-07-07 | e21-24 | 41 | 58% | pending |
| 2026-07-07 | e21-25 | 41 | 50% | pending |
| 2026-07-07 | e21-26 | 41 | 67% | pending |
| 2026-07-07 | e21-27 | 41 | 67% | pending |
| 2026-07-07 | e21-28 | 41 | 67% | pending |
| 2026-07-07 | e21-29 | 41 | 58% | pending |
| 2026-07-07 | e21-30 | 41 | 75% | pending |
| 2026-07-07 | e21-31 | 41 | 58% | pending |
| 2026-07-07 | e21-38 | 41 | 83% | pending |
| 2026-07-07 | e21-39 | 41 | 75% | pending |
| 2026-07-07 | e21-40 | 41 | 83% | pending |
| 2026-07-07 | e21-41 | 41 | 100% | pending |
| 2026-07-07 | e21-42 | 41 | 67% | pending |
| 2026-07-07 | e21-43 | 41 | 92% | pending |
| 2026-07-07 | e21-01 | 41 | 67% | pending |
| 2026-07-07 | e21-02 | 41 | 75% | pending |
| 2026-07-07 | e21-03 | 41 | 67% | pending |
| 2026-07-07 | e21-04 | 41 | 67% | pending |
| 2026-07-07 | e21-37 | 41 | 83% | 8ba74f9 |
| 2026-07-07 | w15-01 | 77 | 54% | db0e87d |
| 2026-07-08 | w15-02 | 77 | 54% | a30b90f |
| 2026-07-08 | w15-03 | 77 | 54% | ee6f9c6 |
| 2026-07-08 | w15-04 | 77 | 58% | de85f14 |
| 2026-07-08 | w15-05 | 77 | 54% | 1e24265 |
| 2026-07-08 | w15-06 | 77 | 54% | 52f14f7 |
| 2026-07-08 | w15-07 | 77 | 58% | e5c3521 |
| 2026-07-08 | w15-08 | 77 | 65% | aa965c3 |
| 2026-07-08 | w15-09 | 77 | 54% | d0ad44b |
| 2026-07-08 | w15-10 | 77 | 58% | cb9cde7 |
| 2026-07-08 | w15-11 | 77 | 58% | 80890f7 |
| 2026-07-08 | w15-12 | 77 | 54% | dad764a |
| 2026-07-08 | w15-13 | 77 | 54% | 367a60d |
| 2026-07-08 | w15-14 | 77 | 73% | 40efcae |
| 2026-07-08 | w15-15 | 77 | 62% | 55782d1 |
| 2026-07-08 | w15-16 | 77 | 58% | 2cb50d9 |
| 2026-07-08 | w15-17 | 77 | 62% | bfb4add |
| 2026-07-08 | w15-18 | 77 | 62% | 7d280bb |
| 2026-07-08 | w15-19 | 77 | 65% | d27785d |
| 2026-07-08 | w15-20 | 77 | 58% | c5b0937 |
| 2026-07-08 | w15-21 | 77 | 62% | b0666db |
| 2026-07-08 | w15-22 | 77 | 85% | a6e4f7f |
| 2026-07-08 | w15-23 | 77 | 73% | 5c7a757 |
| 2026-07-08 | w15-24 | 77 | 77% | 073a9c4 |
| 2026-07-08 | w15-25 | 77 | 73% | 4b6ef51 |
| 2026-07-08 | w15-26 | 77 | 88% | pending |
