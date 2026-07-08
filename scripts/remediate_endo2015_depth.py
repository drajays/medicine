#!/usr/bin/env python3
"""Add 9 missing ESAP 2015 cases + 8 T/F + 8 A/R per topic module (e15-03–e15-10)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_endo_esap_modules import ar, ref, tf  # noqa: E402

PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")

TOPIC_MODULES = [
    "e15-03", "e15-04", "e15-05", "e15-06", "e15-07", "e15-08", "e15-09", "e15-10",
]


def case_bundle(
    eid: str,
    qnum: int,
    question: str,
    options: list[str],
    letter: str,
    why_text: str,
    how_text: str,
    quote: str,
) -> list[dict]:
    co = ord(letter.upper()) - ord("A")
    base = f"{eid}-q{qnum}"
    r = ref(f"ESAP 2015 Case {qnum}", quote)
    return [
        {
            "id": f"{base}-mcq",
            "type": "mcq",
            "subtopic": f"ESAP 2015 Case {qnum}",
            "question": question,
            "options": options[:5],
            "correctOption": co,
            "explanation": why_text,
            "reference": r,
        },
        {
            "id": f"{base}-why",
            "type": "note",
            "subtopic": f"ESAP 2015 Case {qnum}",
            "title": f"Why answer {letter} is correct",
            "text": why_text[:2000],
            "reference": r,
        },
        {
            "id": f"{base}-how",
            "type": "note",
            "subtopic": f"ESAP 2015 Case {qnum}",
            "title": "How to apply this case clinically",
            "text": how_text[:2500],
            "reference": r,
        },
    ]


MISSING_BY_MODULE: dict[str, list[dict]] = {
    "e15-03": [
        *case_bundle(
            "e15-03", 12,
            "A 72-year-old man with no history of diabetes is confused after a car crash. Fingerstick glucose is 45 mg/dL (2.50 mmol/L). CT shows multiple hepatic metastases and a complex renal mass suspicious for renal cell carcinoma; pancreas appears normal. He was asymptomatic before presentation.\n\nWhich laboratory pattern at the time of hypoglycemia is most likely?",
            [
                "High insulin, high C-peptide, positive insulin antibodies, negative sulfonylurea screen",
                "Low insulin, normal C-peptide, negative antibodies, positive sulfonylurea screen",
                "High insulin, suppressed C-peptide/proinsulin, negative antibodies, negative sulfonylurea screen",
                "Low insulin, measurable C-peptide, negative antibodies, negative sulfonylurea screen",
                "Suppressed insulin, C-peptide, and proinsulin; negative antibodies and sulfonylurea screen",
            ],
            "E",
            "Tumor-mediated hypoglycemia from a non-islet malignancy suppresses endogenous β-cell secretion; insulin, C-peptide, and proinsulin are appropriately low at hypoglycemia.",
            "In PTHrP/IGF-2–mediated or other non-insulin hypoglycemia, do not pursue insulinoma localization when β-cell peptides are suppressed and imaging shows disseminated malignancy.",
            "Guide the diagnostic workup of a patient with large hepatic lesions and hypoglycemia.",
        ),
        *case_bundle(
            "e15-03", 26,
            "A 35-year-old athletic woman has postprandial hypoglycemia symptoms relieved by eating. During a supervised fast, glucose is 49 mg/dL (2.72 mmol/L) with symptoms at 9:45 AM; glucagon is given with serial sampling.\n\nWhich laboratory set would prompt pancreatic imaging for insulinoma?",
            [
                "Insulin 3.2 µIU/mL; C-peptide 4.0 ng/mL; proinsulin 16 pg/mL; Δ glucose after glucagon 31 mg/dL; antibodies negative; sulfonylurea negative",
                "Insulin 15 µIU/mL; C-peptide 4.5 ng/mL; sulfonylurea screen positive",
                "Insulin 112 µIU/mL; suppressed C-peptide; negative sulfonylurea",
                "Markedly elevated insulin and C-peptide with positive insulin antibodies",
                "Insulin at detection limit; suppressed C-peptide; minimal glucagon response",
            ],
            "A",
            "Inappropriate persistence of β-cell polypeptides at documented hypoglycemia, with positive glucagon stimulation, indicates endogenous hyperinsulinemic hypoglycemia warranting localization.",
            "Use concurrent C-peptide, proinsulin, sulfonylurea screen, and glucagon response—not insulin alone—to distinguish insulinoma, factitious insulin, sulfonylurea, and non-insulin mediators.",
            "Evaluate a patient with recurrent hypoglycemic symptoms and interpret results from a fast.",
        ),
    ],
    "e15-04": [
        *case_bundle(
            "e15-04", 4,
            "A 19-year-old man with type 1 diabetes (BMI 40.4 kg/m²), retinopathy, smokes 1 pack/day, LDL 186 mg/dL, HDL 26 mg/dL, TG 229 mg/dL, HbA1c 7.8%. In addition to smoking cessation, which intervention most reduces lifetime cardiovascular risk?",
            ["Intensified glucose control", "Fibrate", "Statin", "Niacin", "Low-fat diet alone"],
            "C",
            "Despite young age, he has high lifetime ASCVD risk from T1DM, smoking, and marked dyslipidemia; statins provide the largest evidence-based risk reduction among listed options.",
            "In T1DM youth with LDL near 190 mg/dL and multiple risk factors, do not defer statin therapy while awaiting perfect glycemic control.",
            "Reduce cardiovascular risk in a young diabetic adult at high risk.",
        ),
        *case_bundle(
            "e15-04", 19,
            "A 40-year-old woman (BMI 23.5 kg/m²) with 37% body fat on DXA, active lifestyle, family history of T2DM. Which pattern best describes her BMI status and cardiovascular risk?",
            [
                "Elevated BMI; increased cardiovascular risk",
                "Elevated BMI; normal cardiovascular risk",
                "Normal BMI; increased cardiovascular risk",
                "Normal BMI; normal cardiovascular risk",
                "Low BMI; increased cardiovascular risk",
            ],
            "C",
            "Normal BMI with elevated body fat percentage confers metabolic risk—so-called normal-weight obesity—particularly in women.",
            "When BMI is normal but adiposity is high, assess body composition; metabolic risk may be underestimated by BMI alone.",
            "Interpret body composition data in assessing cardiometabolic risk.",
        ),
    ],
    "e15-05": [
        *case_bundle(
            "e15-05", 23,
            "A postmenopausal woman with estrogen-receptor-positive breast cancer is about to start an aromatase inhibitor after surgery. DXA shows low bone density. Which therapy best prevents AI-induced bone loss?",
            ["Tamoxifen", "GnRH agonist", "Denosumab", "Calcitonin", "Reassurance only"],
            "C",
            "Aromatase inhibitors accelerate bone loss; denosumab (anti-RANKL) is approved to prevent AI-induced bone loss when T-score ≤ −2.0 or multiple risk factors.",
            "Offer bone-directed therapy when starting aromatase inhibitors in postmenopausal women at elevated fracture risk—do not rely on calcium/vitamin D alone.",
            "Prevent bone loss in a patient starting aromatase inhibitor therapy for breast cancer.",
        ),
        *case_bundle(
            "e15-05", 66,
            "A 56-year-old woman has weight loss, confusion, hypercalcemia (14.7 mg/dL), splenomegaly with infiltrative masses on CT, and normal alkaline phosphatase. Which laboratory pattern is most characteristic?",
            [
                "High urinary calcium; low PTH; low PTHrP",
                "Low urinary calcium; high PTH; low PTHrP",
                "High urinary calcium; high PTH; low PTHrP",
                "High urinary calcium; low PTH; high PTHrP",
                "Low urinary calcium; low PTH; high PTHrP",
            ],
            "A",
            "B-cell lymphoma can produce extrarenal 1,25-(OH)₂D via macrophage 1α-hydroxylase, causing absorptive hypercalcemia with suppressed PTH and PTHrP.",
            "In lymphoma-associated hypercalcemia, measure 1,25-(OH)₂D; pattern differs from PTHrP-mediated humoral hypercalcemia of malignancy.",
            "Recognize calcitriol-mediated hypercalcemia in lymphoproliferative disease.",
        ),
    ],
    "e15-07": [
        *case_bundle(
            "e15-07", 89,
            "A 74-year-old man 4 days post total hip replacement has left flank pain; CT shows bilateral adrenal enlargement (arrows). He is on LMWH, mildly febrile, tachycardic, not frankly hypotensive yet.\n\nWhich laboratory profile is expected with bilateral adrenal hemorrhage?",
            [
                "Normal sodium/potassium; high cortisol; normal ACTH; high aldosterone",
                "Hyponatremia; hyperkalemia; low cortisol; elevated ACTH; low aldosterone",
                "Hypernatremia; normal potassium; low cortisol; suppressed ACTH; high aldosterone",
                "Normonatremia; low potassium; very high cortisol; low ACTH",
                "Hyponatremia; low potassium; low cortisol; suppressed ACTH; high aldosterone",
            ],
            "B",
            "Bilateral adrenal hemorrhage causes primary adrenal insufficiency: low cortisol with high ACTH, hyponatremia and hyperkalemia from mineralocorticoid deficiency.",
            "In anticoagulated postoperative patients with flank pain and bilateral adrenal enlargement, check cortisol and ACTH urgently—treat empirically if shock develops.",
            "Diagnose adrenal hemorrhage in a postoperative anticoagulated patient.",
        ),
    ],
    "e15-09": [
        *case_bundle(
            "e15-09", 83,
            "A young woman with classic 21-hydroxylase CAH is transitioning to adult care. On hydrocortisone and fludrocortisone with suppressed renin, she has irregular menses, hirsutism, acne, and elevated testosterone but no adrenal insufficiency symptoms.\n\nBest next step for androgen excess?",
            ["Increase fludrocortisone", "Add hormonal contraception", "Increase hydrocortisone to normalize 17-OHP", "Switch to long-acting glucocorticoid", "Spironolactone without contraception"],
            "B",
            "Overtreatment with glucocorticoids is not indicated without adrenal insufficiency; combined hormonal contraception suppresses ovarian androgens and protects the endometrium.",
            "In adult CAH with adequate glucocorticoid/mineralocorticoid replacement, treat hirsutism with hormonal contraception—not reflex glucocorticoid escalation.",
            "Select appropriate treatment for a woman with classic CAH transitioning to adult care.",
        ),
    ],
    "e15-10": [
        *case_bundle(
            "e15-10", 103,
            "A man on testosterone replacement has symptomatic improvement. PSA rose from 1.2 to 2.9 ng/mL over 12 months (increase 1.7 ng/mL). Digital exam shows benign prostatic hyperplasia without urinary symptoms.\n\nBest next step?",
            ["Refer to urologist", "Empiric antibiotics for subclinical prostatitis", "Reassure; repeat PSA in 3 months", "Reduce testosterone dose", "Start dutasteride"],
            "A",
            "Endocrine Society guidelines recommend urologic referral when PSA rises >1.4 ng/mL on testosterone therapy—this triggers evaluation, not automatic cancer diagnosis.",
            "Monitor PSA on TRT; a confirmed rise >1.4 ng/mL warrants urology referral even if absolute PSA remains 'normal'.",
            "Monitor serum prostate-specific antigen levels during testosterone therapy.",
        ),
    ],
}


def tf_ar_bank(eid: str) -> list[dict]:
    """Eight true/false + eight assertion-reason items per topic module."""
    banks: dict[str, list] = {
        "e15-03": [
            tf(f"{eid}-tf1", "DKA management", "Once glucose falls below 200 mg/dL in DKA, 5% dextrose should be added while continuing insulin until anion gap closes.", True, "Prevents hypoglycemia during insulin therapy while acidosis resolves.", ref("ESAP 2015 DKA", "add 5% dextrose to the intravenous fluids and continue intravenous insulin until the acidosis has resolved")),
            tf(f"{eid}-tf2", "Hypoglycemia driving", "A history of hypoglycemia during sleep alone should permanently prohibit driving in all patients with diabetes.", False, "Sleep-only hypoglycemia without severe events does not automatically mandate permanent driving restriction; individualized assessment is required.", ref("ESAP 2015 Case 9", "hypoglycemia that has occurred only during sleep should not automatically result in driving restrictions")),
            tf(f"{eid}-tf3", "Insulinoma imaging", "A malignant insulinoma may present with metastases despite a normal-appearing pancreas on CT.", True, "Imaging can miss primary lesions; biochemical diagnosis precedes localization.", ref("ESAP 2015 Case 12", "it would be unlikely for a malignant insulinoma to present with metastatic disease yet not be visible on CT of the pancreas")),
            tf(f"{eid}-tf4", "T1DM lipids", "Statin therapy is never appropriate in patients with type 1 diabetes under age 21 years.", False, "Young T1DM patients with marked LDL elevation and multiple risk factors may benefit from statins despite age.", ref("ESAP 2015 Case 4", "it is reasonable to recommend statin therapy")),
            tf(f"{eid}-tf5", "CGM/pumps", "Insulin pump therapy universally reduces HbA1c in all patients with type 1 diabetes.", False, "Pumps may reduce variability; HbA1c benefit is not universal and depends on engagement.", ref("ESAP 2015 Case 30", "Reduced hemoglobin A1c is one possible but not guaranteed outcome")),
            tf(f"{eid}-tf6", "Hypertriglyceridemia", "Triglycerides ≥1000 mg/dL increase acute pancreatitis risk in diabetes.", True, "Severe hypertriglyceridemia is a pancreatitis precipitant, especially with insulin deficiency.", ref("ESAP 2015 Case 7", "Triglyceride concentrations of 1000 mg/dL or higher increase the risk of acute pancreatitis")),
            tf(f"{eid}-tf7", "SGLT2 inhibitors", "SGLT2 inhibitors may be used in type 1 diabetes without special precautions.", False, "Off-label use carries DKA risk; requires specialist oversight where used.", ref("ESAP 2015", "Sodium-glucose cotransporter 2 inhibitors in type 1 diabetes")),
            tf(f"{eid}-tf8", "Celiac screening", "Microcytic anemia in type 1 diabetes should prompt celiac disease screening.", True, "Tissue transglutaminase antibodies screen for celiac disease associated with T1DM.", ref("ESAP 2015 Case 119", "Measuring tissue transglutaminase antibodies is recognized as an appropriate screening tool")),
            ar(f"{eid}-ar1", "DKA", "Continuing insulin infusion after glucose normalizes in DKA is necessary until acidosis resolves.", "Hyperglycemia correction precedes ketosis clearance; stopping insulin early risks rebound ketosis.", 0, "Both true and causally linked.", ref("ESAP 2015 Case 16", "continue intravenous insulin until the acidosis has resolved")),
            ar(f"{eid}-ar2", "Insulinoma", "Inappropriately elevated C-peptide at hypoglycemia excludes exogenous insulin administration.", "Factitious insulin use suppresses C-peptide; elevated C-peptide indicates endogenous secretion.", 2, "A is false when exogenous insulin is used; R correctly describes endogenous hyperinsulinism.", ref("ESAP 2015 Case 26", "inappropriate persistence of β-cell polypeptide secretion")),
            ar(f"{eid}-ar3", "Hypoglycemia", "Tumor-mediated hypoglycemia always elevates insulin levels.", "Non-islet tumors may cause hypoglycemia via IGF-2 or other mediators with suppressed insulin.", 2, "A false; R true—classic teaching pitfall.", ref("ESAP 2015 Case 12", "endogenous production of β-cell polypeptides should cease")),
            ar(f"{eid}-ar4", "Driving", "All patients with diabetes and neuropathy are unfit to drive.", "Neuropathy increases risk but does not automatically disqualify driving without individualized assessment.", 2, "A overstates; R is not the explanation for a blanket ban.", ref("ESAP 2015 Case 9", "should not automatically disqualify a patient from driving")),
            ar(f"{eid}-ar5", "Pumps", "Glycemic variability alone mandates insulin pump therapy.", "Pump therapy is a tool for motivated patients; variability may improve but is not an automatic indication.", 2, "A false; R not valid indication.", ref("ESAP 2015", "Continuous glucose monitoring and insulin pump therapy")),
            ar(f"{eid}-ar6", "Pancreatitis", "Hypertriglyceridemic pancreatitis presents without eruptive xanthomas.", "Severe hypertriglyceridemia often shows eruptive xanthomas on extensor surfaces.", 2, "A false; classic exam finding contradicts.", ref("ESAP 2015 Case 7", "eruptive xanthomas over the extensor surfaces")),
            ar(f"{eid}-ar7", "Neonatal diabetes", "Permanent neonatal diabetes never requires sulfonylurea instead of insulin.", "KCNJ11/ABCC8 mutations may respond to sulfonylureas.", 2, "A false; monogenic exceptions exist.", ref("ESAP 2015", "Neonatal diabetes")),
            ar(f"{eid}-ar8", "Preconception", "Normal TSH in the first trimester excludes subclinical hypothyroidism in pregnancy.", "Pregnancy-specific TSH targets are lower; 'normal' lab ranges may be inappropriate.", 2, "A false; trimester-specific ranges required.", ref("ESAP 2015", "TSH reference ranges in pregnancy")),
        ],
        "e15-04": [
            tf(f"{eid}-tf1", "Statin in youth", "A statin is the most impactful listed therapy to lower lifetime ASCVD risk in a young T1DM smoker with LDL ~186 mg/dL.", True, "Statin evidence for event reduction exceeds diet or fibrate monotherapy in this vignette.", ref("ESAP 2015 Case 4", "statin therapy is the most likely to have the greatest influence")),
            tf(f"{eid}-tf2", "Normal-weight obesity", "A normal BMI excludes increased cardiometabolic risk.", False, "Elevated body fat % with normal BMI still increases risk.", ref("ESAP 2015 Case 19", "normal BMI, increased adiposity confers an increased risk")),
            tf(f"{eid}-tf3", "Lifestyle", "Lifestyle change alone is sufficient cardiovascular therapy in high-risk dyslipidemic youth.", False, "Lifestyle is necessary but often insufficient alone when LDL is very high.", ref("ESAP 2015 Case 4", "they are not sufficient by themselves")),
            tf(f"{eid}-tf4", "Fibrate", "Fibrates reliably lower LDL cholesterol by >30%.", False, "Fibrates mainly lower TG and raise HDL; LDL effects are minimal or upward.", ref("ESAP 2015 Case 4", "minimal effects on his LDL-cholesterol level")),
            tf(f"{eid}-tf5", "Panhypopituitarism", "Low resting energy expenditure on calorimetry can indicate under-replaced hypothyroidism in panhypopituitarism.", True, "Hypothyroidism reduces metabolic rate; levothyroxine adjustment can aid weight loss.", ref("ESAP 2015 Case 25", "values less than 80% of predicted are consistent with a hypometabolic state")),
            tf(f"{eid}-tf6", "Grapefruit", "Grapefruit juice can raise statin levels and toxicity risk.", True, "CYP3A4 inhibition increases statin exposure.", ref("ESAP 2015", "Grapefruit juice")),
            tf(f"{eid}-tf7", "ApoB", "Apolipoprotein B may better capture atherogenic particle burden than LDL-C alone.", True, "ApoB reflects particle number.", ref("ESAP 2015 Case 110", "Apolipoprotein B")),
            tf(f"{eid}-tf8", "Bariatric surgery", "Bariatric surgery can increase testosterone in obese hypogonadal men.", True, "Weight loss reverses functional hypogonadism.", ref("ESAP 2015 Case 2", "Weight loss after gastric bypass surgery is associated with a significant increase in testosterone")),
            ar(f"{eid}-ar1", "Statin", "Intensified glucose control is the best next step when HbA1c is already ~7.8% in a young T1DM patient.", "Further glycemic tightening offers limited incremental CV benefit when already near intensive-trial levels.", 2, "A false; R explains limited benefit.", ref("ESAP 2015 Case 4", "improving his glycemic control now is not likely to substantially reduce his cardiovascular disease risk")),
            ar(f"{eid}-ar2", "Body fat", "DXA body fat >35% in a woman with BMI 23.5 carries no added metabolic risk.", "Normal-weight obesity increases metabolic complications and mortality.", 2, "A false.", ref("ESAP 2015 Case 19", "increased adiposity confers an increased risk")),
            ar(f"{eid}-ar3", "Niacin", "Niacin is preferred over statins in young insulin-resistant patients.", "Niacin worsens insulin resistance; statins have stronger outcome data.", 2, "A false.", ref("ESAP 2015 Case 4", "worsening of insulin resistance")),
            ar(f"{eid}-ar4", "Panhypopit", "Increasing testosterone dose promotes weight loss in panhypopituitarism.", "Testosterone improves body composition but does not drive weight loss as primary therapy.", 2, "A false.", ref("ESAP 2015 Case 25", "this intervention alone is not expected to contribute to weight loss")),
            ar(f"{eid}-ar5", "LDL", "Lifetime risk is irrelevant when 10-year ASCVD risk is low in a 19-year-old.", "Elevated LDL in youth predicts lifetime events; treatment may still be warranted.", 2, "A false.", ref("ESAP 2015 Case 4", "lifetime risk is high")),
            ar(f"{eid}-ar6", "Fibrate", "Fibrate therapy is first-line when LDL is 186 mg/dL and TG 229 mg/dL in T1DM.", "Statin is prioritized for high LDL; fibrate role is mainly for severe hypertriglyceridemia.", 2, "A false.", ref("ESAP 2015 Case 4", "statin therapy")),
            ar(f"{eid}-ar7", "Obesity", "Waist circumference adds no information when BMI is calculated.", "Waist identifies visceral adiposity risk.", 2, "A false.", ref("ESAP 2015 Case 19", "Waist circumference identifies individuals with abdominal adiposity")),
            ar(f"{eid}-ar8", "CKD", "Statins are contraindicated in all patients with chronic kidney disease.", "Statins are generally indicated in CKD for ASCVD prevention with dose adjustment.", 2, "A false.", ref("ESAP 2015", "Chronic kidney disease")),
        ],
        "e15-05": [
            tf(f"{eid}-tf1", "Denosumab", "Denosumab prevents aromatase inhibitor–induced bone loss in high-risk postmenopausal women.", True, "RANKL inhibition reduces bone resorption during estrogen deprivation.", ref("ESAP 2015 Case 23", "Denosumab increases the mineral density in women undergoing treatment with aromatase inhibitors")),
            tf(f"{eid}-tf2", "Lymphoma Ca", "1,25-(OH)₂D-mediated hypercalcemia in lymphoma suppresses PTH.", True, "Hypercalcemia feedback suppresses PTH; PTHrP is typically low.", ref("ESAP 2015 Case 66", "suppressed PTH (associated with low PTHrP levels)")),
            tf(f"{eid}-tf3", "PHPT surgery", "Distal radius BMD may improve more than spine after parathyroidectomy in PHPT.", True, "Cortical bone sites may show greater gains.", ref("ESAP 2015 Case 17", "Distal radius bone mineral density")),
            tf(f"{eid}-tf4", "Hypomagnesemia", "Hypomagnesemia must be corrected before hypocalcemia responds to calcium/PTH therapy.", True, "Magnesium depletion impairs PTH secretion and action.", ref("ESAP 2015 Case 71", "magnesium deficiency must be corrected first")),
            tf(f"{eid}-tf5", "Teriparatide", "Teriparatide is first-line for severe postmenopausal osteoporosis with multiple fractures.", False, "Antiresorptives or anabolic agents per guidelines; context-dependent—not always teriparatide first.", ref("ESAP 2015", "Osteoporosis")),
            tf(f"{eid}-tf6", "24h urine Ca", "24-hour urinary calcium helps distinguish FHH from PHPT.", True, "Low urinary calcium with hypercalcemia suggests FHH.", ref("ESAP 2015 Case 45", "Measure 24-hour urinary calcium")),
            tf(f"{eid}-tf7", "Vitamin D", "Vitamin D repletion is unnecessary when starting osteoporosis therapy.", False, "Correct deficiency before/during antiresorptive therapy.", ref("ESAP 2015", "vitamin D")),
            tf(f"{eid}-tf8", "Subtotal PTX", "Subtotal parathyroidectomy is appropriate for 4-gland hyperplasia in renal transplant hyperparathyroidism.", True, "Multigland disease in tertiary HPT often needs subtotal resection.", ref("ESAP 2015 Case 6", "Subtotal parathyroidectomy")),
            ar(f"{eid}-ar1", "Denosumab", "Tamoxifen combined with an aromatase inhibitor is standard for bone protection on AI therapy.", "Combination is not standard; denosumab or bisphosphonates are used.", 2, "A false.", ref("ESAP 2015 Case 23", "denosumab")),
            ar(f"{eid}-ar2", "Lymphoma", "PTHrP is always elevated in lymphoma-related hypercalcemia.", "Many lymphomas cause calcitriol-mediated hypercalcemia with low PTHrP.", 2, "A false.", ref("ESAP 2015 Case 66", "low PTHrP")),
            ar(f"{eid}-ar3", "Mg", "IV calcium alone corrects hypocalcemia when Mg is 1.0 mg/dL.", "PTH response is blunted until magnesium is replete.", 2, "A false.", ref("ESAP 2015 Case 71", "hypocalcemia is not responsive to calcium")),
            ar(f"{eid}-ar4", "PHPT", "Hypertension always resolves after parathyroidectomy.", "Hypertension may improve but is not guaranteed to resolve.", 2, "A false.", ref("ESAP 2015 Case 17", "Hypertension")),
            ar(f"{eid}-ar5", "FHH", "FHH presents with markedly elevated PTH and hypercalcemia.", "FHH typically has mild hypercalcemia with normal or mildly elevated PTH and low urine Ca.", 2, "A false.", ref("ESAP 2015", "Familial hypocalciuric hypercalcemia")),
            ar(f"{eid}-ar6", "AI bone", "Calcitonin is first-line for AI-induced bone loss.", "Calcitonin is weak; denosumab/bisphosphonates preferred.", 2, "A false.", ref("ESAP 2015 Case 23", "Calcitonin is a weak antiresorptive agent")),
            ar(f"{eid}-ar7", "Renal Ca", "Hypercalcemia in granulomatous disease responds to glucocorticoids.", "Steroids reduce calcitriol production in macrophage-driven hypercalcemia.", 0, "Both true and linked.", ref("ESAP 2015 Case 117", "administration of glucocorticoids")),
            ar(f"{eid}-ar8", "PTX", "Observation is preferred when all four parathyroid glands are enlarged in symptomatic PHPT.", "Surgery is indicated for symptomatic PHPT with multigland disease.", 2, "A false.", ref("ESAP 2015 Case 6", "Subtotal parathyroidectomy")),
        ],
        "e15-06": [
            tf(f"{eid}-tf1", "Pregnancy TSH", "TSH >2.5 mIU/L in the first trimester may warrant levothyroxine in pregnancy.", True, "ATA/Endocrine Society pregnancy TSH targets are lower than nonpregnant ranges.", ref("ESAP 2015", "subclinical hypothyroidism in the first trimester")),
            tf(f"{eid}-tf2", "TSH suppression", "Long-term TSH suppression after thyroid cancer always remains necessary.", False, "Low-risk survivors may relax suppression after sustained remission.", ref("ESAP 2015 Case 13", "continued TSH suppression is no longer merited")),
            tf(f"{eid}-tf3", "Amiodarone", "Amiodarone can cause both thyrotoxicosis and hypothyroidism.", True, "Iodine load and direct toxicity affect thyroid function.", ref("ESAP 2015 Case 28", "amiodarone")),
            tf(f"{eid}-tf4", "Thyroid storm", "Elevated T3 in critical illness always indicates thyroid storm.", False, "Rarely elevated T3 in ICU should prompt hyperthyroidism evaluation, not automatic storm label without context.", ref("ESAP 2015", "elevated T3 concentrations are highly unusual in critical illness")),
            tf(f"{eid}-tf5", "FNAB", "Benign FNAB cytology eliminates need for follow-up ultrasound.", False, "Benign nodules still require serial imaging.", ref("ESAP 2015", "Thyroid nodules")),
            tf(f"{eid}-tf6", "RAI Graves", "Radioiodine is contraindicated in Graves ophthalmopathy without caution.", True, "May worsen eye disease; steroids or alternative therapy considered.", ref("ESAP 2015 Case 43", "Graves ophthalmopathy")),
            tf(f"{eid}-tf7", "Subclinical hypo", "Subclinical hypothyroidism in pregnancy should never be treated.", False, "Treatment considered when TSH above trimester-specific range.", ref("ESAP 2015", "levothyroxine replacement")),
            tf(f"{eid}-tf8", "Thyroglobulin", "Undetectable thyroglobulin on suppression supports remission in differentiated thyroid cancer.", True, "Negative Tg and scan support low recurrence risk.", ref("ESAP 2015 Case 13", "undetectable serum thyroglobulin")),
            ar(f"{eid}-ar1", "Pregnancy", "Positive TPO antibodies in pregnancy always require immediate high-dose levothyroxine.", "TPO positivity alone without elevated TSH may be monitored; treatment depends on TSH.", 2, "A false.", ref("ESAP 2015", "TPO antibodies")),
            ar(f"{eid}-ar2", "Cancer", "Lowering levothyroxine in low-risk thyroid cancer survivors increases fracture and AF risk if still suppressed.", "Relaxing suppression reduces subclinical hyperthyroid complications.", 0, "Both true; suppression carries bone and AF risk.", ref("ESAP 2015 Case 13", "detrimental effects of hyperthyroidism on bone density")),
            ar(f"{eid}-ar3", "Amiodarone", "Type 1 amiodarone thyrotoxicosis is best treated with antithyroid drugs alone in all cases.", "Type 2 may need steroids; mixed types exist.", 2, "A oversimplified.", ref("ESAP 2015 Case 28", "amiodarone-induced thyrotoxicosis")),
            ar(f"{eid}-ar4", "Nodules", "All thyroid nodules >1 cm require surgery.", "FNAB and risk stratification guide management.", 2, "A false.", ref("ESAP 2015", "FNAB")),
            ar(f"{eid}-ar5", "Euthyroid sick", "Low T3 in ICU always requires levothyroxine.", "Sick euthyroid syndrome is adaptive; treatment not beneficial.", 2, "A false.", ref("Williams 15e ch48", "interventional studies have not shown benefit")),
            ar(f"{eid}-ar6", "Graves", "Methimazole is never used in pregnancy.", "Methimazole used in 2nd-3rd trimester; PTU preferred 1st trimester historically.", 2, "A false.", ref("ESAP 2015", "antithyroid drugs")),
            ar(f"{eid}-ar7", "TgAb", "Thyroglobulin antibodies invalidate all Tg monitoring.", "Tg may still be tracked with caution; antibodies interfere but do not always preclude use.", 2, "A overstated.", ref("ESAP 2015", "thyroglobulin")),
            ar(f"{eid}-ar8", "RAI", "Pregnancy is an absolute contraindication to diagnostic radioiodine scanning.", "RAI scanning contraindicated in pregnancy due to fetal thyroid destruction risk.", 0, "Both true.", ref("ESAP 2015", "pregnancy")),
        ],
        "e15-07": [
            tf(f"{eid}-tf1", "Adrenal hemorrhage", "Bilateral adrenal hemorrhage causes primary adrenal insufficiency with high ACTH.", True, "Hemorrhage destroys cortex; ACTH rises with low cortisol.", ref("ESAP 2015 Case 89", "subnormal cortisol and elevated ACTH")),
            tf(f"{eid}-tf2", "Primary aldosteronism", "Mineralocorticoid receptor blockade can initially lower GFR in primary aldosteronism.", True, "Reversal of hyperfiltration lowers GFR transiently.", ref("ESAP 2015 Case 1", "decline in glomerular filtration rate")),
            tf(f"{eid}-tf3", "Cushing", "Mild autonomous cortisol secretion may occur with adrenal incidentalomas.", True, "Subclinical hypercortisolism linked to cardiometabolic risk.", ref("ESAP 2015 Case 40", "mild adrenal-dependent hypercortisolism")),
            tf(f"{eid}-tf4", "Cosyntropin", "Cosyntropin stimulation test is unreliable in acute critical illness for adrenal insufficiency diagnosis.", True, "Altered binding proteins and free cortisol dynamics limit interpretation.", ref("Williams 15e ch48", "ACTH stimulation test is not useful in critically ill states")),
            tf(f"{eid}-tf5", "21-OH deficiency", "Classic CAH in adult women may need antiandrogen therapy beyond glucocorticoids.", True, "Ovarian androgen excess may persist; OCPs treat hirsutism.", ref("ESAP 2015 Case 83", "Hormonal contraception is the treatment of choice for hirsutism")),
            tf(f"{eid}-tf6", "Pheo", "Paradoxical hypotension after alpha blockade suggests catecholamine cardiomyopathy or volume depletion.", True, "Requires careful volume expansion and ICU care.", ref("ESAP 2015", "Pheochromocytoma")),
            tf(f"{eid}-tf7", "Adrenal crisis", "Stress-dose hydrocortisone is indicated in adrenal crisis before confirmatory labs return.", True, "Do not delay steroids in suspected crisis.", ref("ESAP 2015", "Adrenal insufficiency")),
            tf(f"{eid}-tf8", "AVS", "Adrenal venous sampling requires confirmation of successful cannulation.", True, "Selectivity index validates sampling.", ref("ESAP 2015 Case 1", "Ensure both adrenal veins have been cannulated")),
            ar(f"{eid}-ar1", "Hemorrhage", "Bilateral adrenal hemorrhage presents with hyperkalemia and hyponatremia.", "Mineralocorticoid and glucocorticoid deficiency cause electrolyte pattern.", 0, "Both true and linked.", ref("ESAP 2015 Case 89", "hyponatremia and hyperkalemia")),
            ar(f"{eid}-ar2", "PA", "Unilateral adrenalectomy is indicated when AVS shows bilateral aldosterone excess.", "Bilateral disease is treated medically with MR antagonists.", 2, "A false.", ref("ESAP 2015 Case 1", "bilateral adrenal hyperplasia")),
            ar(f"{eid}-ar3", "Cushing", "All adrenal incidentalomas require immediate surgery.", "Surgery for functioning masses or size/morphology risk; many observed.", 2, "A false.", ref("ESAP 2015", "adrenal incidentaloma")),
            ar(f"{eid}-ar4", "Steroids", "High-dose steroids always improve outcomes in septic shock.", "RCTs show faster vasopressor weaning but inconsistent mortality benefit.", 2, "A false.", ref("Williams 15e ch48", "RCTs have not shown consistent benefit")),
            ar(f"{eid}-ar5", "CAH", "17-OHP normalization is the goal of adult CAH glucocorticoid dosing.", "Overtreatment causes iatrogenic Cushing; titrate to clinical control not 17-OHP alone.", 2, "A false.", ref("ESAP 2015 Case 83", "glucocorticoid dosage should not be titrated to suppress the 17-hydroxyprogesterone")),
            ar(f"{eid}-ar6", "HyperK", "Hyperkalemia in primary adrenal insufficiency is due to aldosterone deficiency.", "Aldosterone loss impairs potassium excretion.", 0, "Both true.", ref("ESAP 2015 Case 89", "hyperkalemia")),
            ar(f"{eid}-ar7", "AVS", "CT appearance alone is sufficient to lateralize aldosterone-secreting adenoma in all patients over 40.", "AVS recommended especially over 40 due to prevalent nonfunctioning nodules.", 2, "A false.", ref("ESAP 2015", "adrenal venous sampling")),
            ar(f"{eid}-ar8", "Pheo", "Beta-blockade alone is safe first step in suspected pheochromocytoma.", "Alpha blockade must precede beta to avoid unopposed alpha crisis.", 2, "A false—classic pitfall.", ref("ESAP 2015", "Pheochromocytoma")),
        ],
        "e15-08": [
            tf(f"{eid}-tf1", "Pegvisomant", "Pegvisomant lowers IGF-1 without lowering GH secretion.", True, "GH receptor antagonist; GH levels may rise.", ref("ESAP 2015 Case 15", "Pegvisomant does not act on pituitary tumor GH secretion")),
            tf(f"{eid}-tf2", "Prolactinoma", "Bromocriptine can be used for prolactinoma when cabergoline unavailable.", True, "Dopamine agonists are first-line.", ref("ESAP 2015 Case 24", "bromocriptine")),
            tf(f"{eid}-tf3", "DI", "Diabetes insipidus is the most common endocrine presentation of pituitary metastases.", True, "Posterior pituitary involvement common.", ref("ESAP 2015 Case 120", "diabetes insipidus was documented in 70%")),
            tf(f"{eid}-tf4", "Cushing disease", "IPSS helps lateralize ACTH source in Cushing disease.", True, "Bilateral inferior petrosal sinus sampling aids localization.", ref("ESAP 2015 Case 47", "Inferior petrosal sinus sampling")),
            tf(f"{eid}-tf5", "Empty sella", "Empty sella always causes panhypopituitarism.", False, "Many are asymptomatic; hypopituitarism not universal.", ref("ESAP 2015 Case 105", "Empty sella")),
            tf(f"{eid}-tf6", "Opioids", "Opioids suppress GnRH and can cause hypogonadotropic hypogonadism.", True, "Functional hypogonadism with chronic opioids.", ref("ESAP 2015 Case 61", "Opiate use")),
            tf(f"{eid}-tf7", "TSHoma", "TSH-secreting adenomas may present with elevated free T4 and inappropriately normal/high TSH.", True, "Central hyperthyroidism pattern.", ref("ESAP 2015 Case 88", "TSH-secreting adenoma")),
            tf(f"{eid}-tf8", "GH trial", "High-dose GH in prolonged critical illness improved survival.", False, "RCTs showed increased mortality.", ref("Williams 15e ch48", "high-dose GH treatment significantly increased mortality")),
            ar(f"{eid}-ar1", "Acromegaly", "Pegvisomant causes tumor shrinkage by blocking GH secretion.", "Acts peripherally at receptor; does not shrink tumor.", 2, "A false.", ref("ESAP 2015 Case 15", "does not act on pituitary tumor")),
            ar(f"{eid}-ar2", "Prolactinoma", "Macroprolactinoma always requires transsphenoidal surgery first.", "Dopamine agonists are first-line even for macros.", 2, "A false.", ref("ESAP 2015 Case 24", "bromocriptine")),
            ar(f"{eid}-ar3", "DI", "Desmopressin is contraindicated in nephrogenic diabetes insipidus.", "DDAVP works in central DI; nephrogenic requires different management.", 0, "Both true—DDAVP for central not nephrogenic.", ref("ESAP 2015 Case 77", "Diabetes insipidus")),
            ar(f"{eid}-ar4", "Cushing", "Midnight salivary cortisol is useless in Cushing evaluation.", "Elevated late-night salivary cortisol supports hypercortisolism.", 2, "A false.", ref("ESAP 2015 Case 47", "Cushing syndrome")),
            ar(f"{eid}-ar5", "Hypopit", "Panhypopituitarism after surgery never requires hydrocortisone stress dosing education.", "All patients need steroid stress education.", 2, "A false.", ref("ESAP 2015", "Hypopituitarism")),
            ar(f"{eid}-ar6", "TSHoma", "Octreotide can treat TSH-secreting tumors.", "Somatostatin analogs may lower TSH secretion.", 0, "Both true.", ref("ESAP 2015 Case 88", "Octreotide")),
            ar(f"{eid}-ar7", "Incidentaloma", "All pituitary incidentalomas >6 mm need surgery.", "Surgery for compression or apoplexy; many observed.", 2, "A false.", ref("ESAP 2015 Case 65", "Pituitary incidentaloma")),
            ar(f"{eid}-ar8", "GH", "GH lowers IGF-1 by reducing hepatic GH receptors.", "Pegvisomant blocks receptor; GH resistance in illness lowers IGF-1.", 2, "A misstates mechanism.", ref("ESAP 2015 Case 15", "GH receptor antagonist")),
        ],
        "e15-09": [
            tf(f"{eid}-tf1", "CAH", "Hormonal contraception is first-line for hirsutism in adequately replaced adult CAH.", True, "Suppresses ovarian androgens; endometrial protection.", ref("ESAP 2015 Case 83", "Hormonal contraception is the treatment of choice for hirsutism")),
            tf(f"{eid}-tf2", "PCOS", "Rotterdam criteria require two of hyperandrogenism, oligo-anovulation, or polycystic ovaries.", True, "Standard PCOS definition.", ref("ESAP 2015 Case 27", "Rotterdam criteria")),
            tf(f"{eid}-tf3", "POI", "Karyotype is indicated in premature ovarian insufficiency.", True, "Turner and FMR1 testing part of workup.", ref("ESAP 2015 Case 5", "Karyotype analysis")),
            tf(f"{eid}-tf4", "HRT menopause", "Micronized progesterone may be better tolerated than medroxyprogesterone.", True, "Fewer mood side effects in some women.", ref("ESAP 2015 Case 101", "Micronized progesterone may be better tolerated")),
            tf(f"{eid}-tf5", "CAH pregnancy", "Women with CAH need stress steroid plans for labor and delivery.", True, "Stress dosing prevents adrenal crisis.", ref("ESAP 2015", "Congenital adrenal hyperplasia")),
            tf(f"{eid}-tf6", "PCOS fertility", "Clomiphene is first-line ovulation induction in PCOS infertility.", True, "First-line anovulation therapy.", ref("ESAP 2015 Case 44", "Clomiphene citrate")),
            tf(f"{eid}-tf7", "Spironolactone", "Spironolactone in women requires reliable contraception.", True, "Antiandrogen teratogenicity risk.", ref("ESAP 2015 Case 83", "must be paired with contraception")),
            tf(f"{eid}-tf8", "Turner", "Turner syndrome requires cardiology evaluation.", True, "Bicuspid aortic valve and coarctation risk.", ref("ESAP 2015 Case 5", "Turner syndrome")),
            ar(f"{eid}-ar1", "CAH", "Increasing glucocorticoid to normalize 17-OHP is always correct in adult CAH with hirsutism.", "Overtreatment causes Cushing; OCPs treat androgen excess.", 2, "A false.", ref("ESAP 2015 Case 83", "increasing the glucocorticoid dosage is not the best choice")),
            ar(f"{eid}-ar2", "PCOS", "Elevated testosterone alone diagnoses PCOS without other criteria.", "Need two Rotterdam criteria after excluding other causes.", 2, "A false.", ref("ESAP 2015 Case 27", "two out of three")),
            ar(f"{eid}-ar3", "POI", "Normal FSH in amenorrhea excludes ovarian failure.", "Single FSH may fluctuate; repeat and karyotype if concerned.", 2, "A false.", ref("ESAP 2015 Case 5", "primary ovarian insufficiency")),
            ar(f"{eid}-ar4", "HRT", "Estrogen alone is sufficient in women with intact uterus.", "Progesterone required for endometrial protection.", 2, "A false.", ref("ESAP 2015 Case 101", "Progesterone is necessary to protect the uterus")),
            ar(f"{eid}-ar5", "CAH", "Fludrocortisone dose should increase when renin is suppressed and BP normal.", "Suppressed renin suggests adequate mineralocorticoid replacement.", 2, "A false.", ref("ESAP 2015 Case 83", "renin activity is suppressed")),
            ar(f"{eid}-ar6", "PCOS", "Metformin is first-line for all PCOS hirsutism.", "OCPs and antiandrogens treat hirsutism; metformin role is metabolic.", 2, "A false.", ref("ESAP 2015", "Polycystic ovary syndrome")),
            ar(f"{eid}-ar7", "Fertility", "Letrozole is never used for PCOS ovulation induction.", "Letrozole is used off-label/approved in some settings for ovulation.", 2, "A false.", ref("ESAP 2015 Case 44", "fertility treatment")),
            ar(f"{eid}-ar8", "CAIS", "Complete androgen insensitivity presents with female phenotype and undescended testes.", "46,XY with AR resistance; testes present.", 0, "Both true.", ref("ESAP 2015 Case 5", "androgen insensitivity")),
        ],
        "e15-10": [
            tf(f"{eid}-tf1", "TRT PSA", "PSA rise >1.4 ng/mL on testosterone therapy warrants urology referral.", True, "Endocrine Society monitoring threshold.", ref("ESAP 2015 Case 103", "PSA increase greater than 1.4 ng/mL")),
            tf(f"{eid}-tf2", "Obesity hypogonadism", "Weight loss can reverse functional hypogonadism in obese men.", True, "Bariatric surgery and lifestyle increase testosterone.", ref("ESAP 2015 Case 2", "discontinue testosterone therapy and check levels")),
            tf(f"{eid}-tf3", "Opioids", "Buprenorphine may have less HPA suppression than traditional opioids.", True, "Partial agonist may spare gonadal axis more.", ref("ESAP 2015 Case 115", "buprenorphine")),
            tf(f"{eid}-tf4", "Infertility", "Exogenous testosterone suppresses spermatogenesis.", True, "Feedback inhibits GnRH/FSH/LH.", ref("ESAP 2015 Case 18", "Fertility treatment")),
            tf(f"{eid}-tf5", "Free T", "Free testosterone measurement is useful when SHBG is abnormal.", True, "Obesity and liver disease alter SHBG.", ref("ESAP 2015 Case 46", "Free testosterone measurement")),
            tf(f"{eid}-tf6", "Erectile dysfunction", "Normal morning total testosterone excludes organic hypogonadism in all ED patients.", False, "ED multifactorial; isolated low-normal T may still matter.", ref("ESAP 2015 Case 115", "Erectile dysfunction")),
            tf(f"{eid}-tf7", "hCG", "hCG stimulates testicular testosterone in hypogonadotropic hypogonadism desiring fertility.", True, "Preserves or restores spermatogenesis vs exogenous T.", ref("ESAP 2015 Case 18", "hCG injections")),
            tf(f"{eid}-tf8", "Dutasteride", "5-alpha reductase inhibitors are mandatory on all TRT.", False, "Only if LUTS/BPH indications; not routine.", ref("ESAP 2015 Case 103", "dutasteride is not indicated")),
            ar(f"{eid}-ar1", "PSA", "A PSA of 2.9 ng/mL on TRT always indicates prostate cancer.", "Rise triggers evaluation; does not equal cancer.", 2, "A false.", ref("ESAP 2015 Case 103", "does not indicate the presence of prostate cancer")),
            ar(f"{eid}-ar2", "Obesity", "Continued TRT is best after major weight loss with normalized testosterone.", "Exogenous T should stop to assess recovery of axis.", 2, "A false.", ref("ESAP 2015 Case 2", "Discontinue testosterone therapy")),
            ar(f"{eid}-ar3", "Fertility", "Testosterone is ideal therapy when pursuing pregnancy.", "Exogenous T inhibits spermatogenesis; use hCG/FSH.", 2, "A false.", ref("ESAP 2015 Case 18", "hCG injections")),
            ar(f"{eid}-ar4", "Opioids", "All opioids equally suppress testosterone.", "Potency and opioid type differ; buprenorphine may be less suppressive.", 2, "A false.", ref("ESAP 2015 Case 115", "buprenorphine")),
            ar(f"{eid}-ar5", "ED", "Sildenafil contraindicates testosterone therapy.", "PDE5 inhibitors and TRT can coexist when indicated.", 2, "A false.", ref("ESAP 2015 Case 115", "sildenafil")),
            ar(f"{eid}-ar6", "PSA", "Reassurance is appropriate when PSA rises 1.7 ng/mL on TRT.", "Exceeds 1.4 ng/mL threshold; refer to urology.", 2, "A false.", ref("ESAP 2015 Case 103", "referred for urologic evaluation")),
            ar(f"{eid}-ar7", "Klinefelter", "Klinefelter syndrome never produces sperm with assisted reproduction.", "Micro-TESE may retrieve sperm in some.", 2, "A false.", ref("ESAP 2015", "Klinefelter")),
            ar(f"{eid}-ar8", "SHBG", "Total testosterone is always adequate in obesity.", "Low SHBG can mask low free T; measure free/bioavailable T.", 2, "A false.", ref("ESAP 2015 Case 46", "Free testosterone measurement")),
        ],
    }
    return banks.get(eid, [])


def find_module_file(eid: str) -> Path | None:
    matches = list(PORTAL_DATA.glob(f"endo2015_{eid}_*.json"))
    return matches[0] if matches else None


def merge_items(module: dict, new_items: list[dict]) -> int:
    existing_ids = {it["id"] for it in module["items"]}
    added = 0
    for it in new_items:
        if it["id"] not in existing_ids:
            module["items"].append(it)
            existing_ids.add(it["id"])
            added += 1
    return added


def main() -> None:
    total_added = 0
    for eid in TOPIC_MODULES:
        path = find_module_file(eid)
        if not path:
            print(f"SKIP {eid}: no JSON file")
            continue
        module = json.loads(path.read_text(encoding="utf-8"))
        new_items: list[dict] = []
        new_items.extend(MISSING_BY_MODULE.get(eid, []))
        new_items.extend(tf_ar_bank(eid))
        added = merge_items(module, new_items)
        payload = json.dumps(module, indent=2, ensure_ascii=False)
        path.write_text(payload, encoding="utf-8")
        master_path = MASTER_DATA / path.name
        if master_path.parent.exists():
            master_path.write_text(payload, encoding="utf-8")
        from collections import Counter
        c = Counter(i["type"] for i in module["items"])
        wh = sum(1 for i in module["items"] if i["type"] == "note" and i.get("title", "").startswith(("Why", "How")))
        notes = c.get("note", 0)
        print(f"{eid}: +{added} items → {len(module['items'])} total {dict(c)} Why/How {wh}/{notes}")
        total_added += added
    print(f"Total items added: {total_added}")


if __name__ == "__main__":
    main()
