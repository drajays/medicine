#!/usr/bin/env python3
"""Generate remediated ESAP 2021 modules e21-05 through e21-08 (Harrison-quality schema)."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
SOURCE_DIR = Path("/Users/dr.ajayshukla/endo_masterapp/williams_2024_chapters")


def ref(section: str, quote: str) -> str:
    return f'{section}: "{quote}"'


def note(iid: str, subtopic: str, title: str, text: str, reference: str) -> dict:
    return {
        "id": iid,
        "type": "note",
        "subtopic": subtopic,
        "title": title,
        "text": text,
        "reference": reference,
    }


def mcq(
    iid: str,
    subtopic: str,
    question: str,
    options: list[str],
    correct: int,
    explanation: str,
    reference: str,
) -> dict:
    assert len(options) == 4, f"{iid}: need 4 options"
    assert 0 <= correct <= 3, f"{iid}: correctOption out of range"
    return {
        "id": iid,
        "type": "mcq",
        "subtopic": subtopic,
        "question": question,
        "options": options,
        "correctOption": correct,
        "explanation": explanation,
        "reference": reference,
    }


def tf(
    iid: str,
    subtopic: str,
    statement: str,
    correct: bool,
    explanation: str,
    reference: str,
) -> dict:
    return {
        "id": iid,
        "type": "true_false",
        "subtopic": subtopic,
        "statement": statement,
        "correctAnswer": correct,
        "explanation": explanation,
        "reference": reference,
    }


def ar(
    iid: str,
    subtopic: str,
    assertion: str,
    reason: str,
    correct: int,
    explanation: str,
    reference: str,
) -> dict:
    return {
        "id": iid,
        "type": "assertion_reason",
        "subtopic": subtopic,
        "assertion": assertion,
        "reason": reason,
        "correctOption": correct,
        "explanation": explanation,
        "reference": reference,
    }


def build_chapter_06() -> dict:
    p = "e21-06"
    items: list[dict] = []

    # --- Notes (12; 7 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Diagnostic paradigm",
                "Why biochemical assessment is paramount in Cushing syndrome",
                "Imaging supports localization but cannot establish autonomous cortisol excess or distinguish ACTH-dependent from adrenal disease. The optimal approach uses staged biochemical tests (high sensitivity first, then specificity), determines ACTH dependence, and only then pursues anatomic localization.",
                ref(
                    "Main Conclusions",
                    "The optimal approach is to (1) use a series of biochemical tests, ranging from those with high sensitivity to those with increasing specificity, (2) determine whether the disorder is ACTH-dependent, and (3) when appropriate, locate the source of ACTH. Imaging is part of this paradigm, but biochemical assessment is paramount.",
                ),
            ),
            note(
                f"{p}-n2",
                "Screening strategy",
                "How to stage the initial workup for suspected Cushing syndrome",
                "Begin with a highly sensitive test—many clinicians use the overnight 1-mg dexamethasone-suppression test. Reserve urinary free cortisol for indeterminate cases or children. Late-night salivary cortisol is excellent when the assay and normative data are validated locally.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "It is therefore essential to investigate the diagnosis in stages, beginning with a test that is simple to use and has very high sensitivity. Then, if this test indicates possible Cushing syndrome, more specific tests can be used.",
                ),
            ),
            note(
                f"{p}-n3",
                "Circadian rhythm",
                "Why loss of circadian cortisol rhythm is central to diagnosis",
                "Cushing syndrome reflects autonomous cortisol production with loss of normal feedback and loss of the nocturnal nadir. Midnight serum cortisol, late-night salivary cortisol, and failure of dexamethasone suppression all exploit this pathophysiology.",
                ref(
                    "Significance of the Clinical Problem",
                    "The diagnosis is based on the demonstration of an autonomous source of excess cortisol production, most apparent and demonstrable by loss of the normal circadian rhythmicity and failure to show adequate feedback regulation.",
                ),
            ),
            note(
                f"{p}-n4",
                "ACTH localization",
                "9-AM plasma ACTH thresholds for source localization",
                "After biochemical confirmation, collect 9-AM ACTH correctly: <10 pg/mL (<2.2 pmol/L) favors adrenal autonomy; >30 pg/mL (>6.6 pmol/L) indicates ACTH dependence. Grey-zone values (10–30 pg/mL) warrant CRH stimulation or repeat sampling.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "It is important to collect the sample correctly, and in such a situation, a concentration less than 10 pg/mL (<2.2 pmol/L) indicates an adrenal source, a concentration greater than 30 pg/mL (>6.6 pmol/L) indicates ACTH dependence.",
                ),
            ),
            note(
                f"{p}-n5",
                "BIPSS",
                "How bilateral inferior petrosal sinus sampling localizes ACTH-dependent Cushing syndrome",
                "An experienced neuroradiologist samples petrosal and peripheral veins before and after IV CRH (or desmopressin). A central-to-peripheral ACTH gradient >3 after stimulation is ~95% sensitive and nearly 100% specific for Cushing disease; absent gradient shifts probability toward ectopic ACTH.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "A central-to-peripheral ACTH gradient greater than 3 after corticotropin-releasing hormone is 95% sensitive and almost 100% specific for the diagnosis of Cushing disease.",
                ),
            ),
            note(
                f"{p}-n6",
                "Ectopic ACTH",
                "Modern spectrum of ectopic ACTH syndrome",
                "Classic small-cell lung cancer presentations are less common; small bronchial, thymic, pancreatic, and other neuroendocrine tumors occur across ages. Neck/chest CT and ⁶⁸Ga-DOTATATE PET help, but covert and occult sources still occur.",
                ref(
                    "Significance of the Clinical Problem",
                    "The classic ectopic ACTH syndrome due to small cell lung carcinoma, presenting in an older patient with severe metabolic defects and an obvious malignancy, is now being increasingly replaced in practice by small bronchial, thymic, pancreatic, or other neuroendocrine tumors occurring at almost any age.",
                ),
            ),
            note(
                f"{p}-n7",
                "Center of excellence",
                "Why Cushing syndrome should be managed at experienced centers",
                "Diagnosis and source identification remain probabilistic, not algorithmic. Severe metabolic complications, infection risk, and complex localization benefit from a dedicated multidisciplinary team.",
                ref(
                    "Main Conclusions",
                    "It cannot be overemphasized that the management of these patients requires experience and expertise of a dedicated clinical team, and the investigation and management often benefit from the input of a center of excellence.",
                ),
            ),
            note(
                f"{p}-n8",
                "Acute management",
                "How to manage overwhelming hypercortisolism before definitive therapy",
                "Address hypertension, hyperglycemia, hypokalemia, and infection risk urgently. Lower cortisol to safe concentrations with medical therapy; IV etomidate is effective when oral agents are insufficient. Many clinicians start prophylactic anticoagulation once the diagnosis is confirmed.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Patients with overwhelming metabolic complications of Cushing syndrome of any cause should be treated with intravenous etomidate, which rapidly and effectively lowers cortisol when administered with due care.",
                ),
            ),
            note(
                f"{p}-n9",
                "Pseudo-Cushing states",
                "Pitfall: obesity and depression without true Cushing syndrome",
                "Mild biochemical abnormalities occur in depression, anorexia, and obstructive sleep apnea. Catabolic stigmata—easy bruising, myopathy, osteoporosis, pediatric growth failure—raise pretest probability more than isolated metabolic syndrome features.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Thus, the clinician will see many patients with a Cushing-like presentation, and some may have mildly abnormal biochemistry, so-called pseudo-Cushing states, including patients with anorexia, depression, and obstructive sleep apnea.",
                ),
            ),
            note(
                f"{p}-n10",
                "Thrombosis risk",
                "Why anticoagulation is considered after confirming Cushing syndrome",
                "Hypercortisolism increases thrombotic risk alongside infection and metabolic derangements. Prophylactic heparin is commonly advised once the diagnosis is established while definitive therapy is planned.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Many clinicians advise anticoagulation with subcutaneous heparin as soon as the diagnosis is confirmed.",
                ),
            ),
            note(
                f"{p}-n11",
                "Cushing disease therapy",
                "How to sequence therapy for confirmed Cushing disease",
                "First-line transsphenoidal surgery by an experienced surgeon (~90% cure). Failed surgery may be followed by repeat operation, radiation/radiosurgery, or medical blockade (metyrapone, ketoconazole, mifepristone) while awaiting remission.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "For confirmed Cushing disease, transsphenoidal surgery by an experienced surgeon should have a high cure rate, approaching 90%, while a repeat surgery when initially unsuccessful can still lead to cure in around 50% of patients.",
                ),
            ),
            note(
                f"{p}-n12",
                "Bilateral macronodular hyperplasia",
                "ARMC5 and familial bilateral macronodular adrenal hyperplasia",
                "Bilateral macronodular hyperplasia may respond transiently to unilateral adrenalectomy of the dominant gland but often recurs. Bilateral adrenalectomy is definitive but mandates lifelong replacement. Germline ARMC5 variants explain some familial cases.",
                ref(
                    "Case 2 (Continued)",
                    "On further questioning, she reported that she thought her sister had a similar condition. This was confirmed, and genetic analysis identified a germline ARMC5 pathogenic variant in both the patient and her sister.",
                ),
            ),
        ]
    )

    # --- MCQs (13) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — ectopic workup",
                "A 26-year-old man has 5 years of cushingoid features. Serum cortisol is repeatedly >63 μg/dL and ACTH 300–350 pg/mL. CT chest shows left lower-lobe collapse/consolidation. What is the best next step?",
                [
                    "Corticotropin-releasing hormone stimulation test",
                    "Bilateral inferior petrosal sinus sampling",
                    "Bronchoscopy",
                    "⁶⁸Ga-DOTATATE PET scanning",
                ],
                2,
                "Cushing syndrome is already biochemically obvious. With marked ACTH elevation and a focal chest abnormality, direct bronchoscopic evaluation for a bronchial neuroendocrine tumor is more expeditious than further dynamic pituitary testing or nonspecific PET uptake in inflamed lung.",
                ref(
                    "Case 1",
                    "Bronchoscopy (Answer D) to look for a bronchial tumor is the most useful and expeditious investigation at this stage.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — after infection treated",
                "The same patient improves after treating bronchial infection; cytology is negative, pituitary MRI shows mild asymmetry, and ⁶⁸Ga-DOTATATE PET is negative. What should be done next?",
                [
                    "High-dose dexamethasone-suppression test",
                    "Thoracic surgery",
                    "Bilateral inferior petrosal sinus sampling",
                    "Combined dexamethasone–CRH test",
                ],
                2,
                "With no clear ectopic source and equivocal pituitary imaging, BIPSS is the best test to distinguish Cushing disease from occult ectopic ACTH before pituitary exploration or chest surgery.",
                ref(
                    "Case 1 (Continued)",
                    "Answer: A) Bilateral inferior petrosal sinus sampling",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — low ACTH",
                "A woman has 9-AM cortisol 20 μg/dL and fails to suppress after overnight 1-mg dexamethasone (18.5 μg/dL). Predexamethasone ACTH is 4 pg/mL. What is the most useful next test?",
                [
                    "MRI of the pituitary gland",
                    "CRH stimulation test",
                    "CT of the adrenal glands",
                    "CT of the thorax",
                ],
                2,
                "ACTH <10 pg/mL indicates primary adrenal pathology; adrenal CT is the fastest way to identify adenoma, carcinoma, or bilateral macronodular hyperplasia.",
                ref(
                    "Case 2 (Continued)",
                    "Answer: C) CT of the adrenal glands",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 2 — bilateral macronodular hyperplasia",
                "CT shows bilateral enlarged nodular adrenals (5 cm left, 3.5 cm right). CRH testing confirms persistently suppressed ACTH. After counseling, she prefers definitive therapy. What is most appropriate?",
                [
                    "Unilateral adrenalectomy of the larger adrenal",
                    "Bilateral adrenalectomy",
                    "Long-term ketoconazole monotherapy",
                    "Mifepristone as sole definitive therapy",
                ],
                1,
                "Bilateral macronodular hyperplasia often requires bilateral adrenalectomy for durable cure; unilateral surgery may transiently normalize cortisol but recurrence is common. Medical therapy is adjunctive, not definitive.",
                ref(
                    "Case 2 (Continued)",
                    "Many would advise bilateral adrenalectomy (Answer B), with the caveat that this will require lifelong adrenocortical replacement therapy.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "First-line screening",
                "Which initial screening approach is favored by many experts for suspected mild Cushing syndrome when a validated late-night salivary assay is unavailable?",
                [
                    "24-hour urinary free cortisol ×3",
                    "Overnight 1-mg dexamethasone-suppression test",
                    "Low-dose 48-hour dexamethasone test",
                    "Bilateral inferior petrosal sinus sampling",
                ],
                1,
                "The overnight 1-mg dex test is simple and highly sensitive for first-line screening; UFC is often reserved for indeterminate cases.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Many clinicians start with the overnight dexamethasone-suppression test, administering 1 mg of dexamethasone orally at midnight",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Late-night salivary cortisol",
                "A reliable late-night salivary cortisol assay is available. Which result pattern best supports Cushing syndrome?",
                [
                    "Midnight salivary cortisol within assay-specific elevated range with loss of circadian nadir",
                    "Single morning salivary cortisol at upper limit of normal",
                    "Suppressed salivary cortisol after 1-mg dexamethasone alone",
                    "Normal midnight salivary cortisol on two occasions",
                ],
                0,
                "Late-night salivary cortisol exploits loss of circadian rhythm and, with validated normative data, achieves high sensitivity and specificity.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "There is now increasing evidence that a midnight salivary cortisol measurement can also readily differentiate Cushing syndrome from noncushingoid states, and the sample can be collected at home and then brought or mailed to the laboratory.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "ACTH interpretation",
                "After biochemical confirmation of Cushing syndrome, 9-AM ACTH is 8 pg/mL on two samples. What is the most likely source?",
                [
                    "Pituitary corticotroph adenoma",
                    "Ectopic ACTH secretion",
                    "Primary adrenal tumor or hyperplasia",
                    "Exogenous glucocorticoid use",
                ],
                2,
                "ACTH persistently <10 pg/mL indicates adrenal autonomy; pituitary and ectopic sources are ACTH-dependent.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "a concentration less than 10 pg/mL (<2.2 pmol/L) indicates an adrenal source",
                ),
            ),
            mcq(
                f"{p}-q8",
                "BIPSS interpretation",
                "During BIPSS after CRH, the central:peripheral ACTH ratio is 3.5. What does this indicate?",
                [
                    "Ectopic ACTH syndrome",
                    "Primary adrenal adenoma",
                    "Cushing disease (pituitary ACTH source)",
                    "Exogenous steroid suppression",
                ],
                2,
                "A post-CRH central:peripheral gradient >3 is highly specific for pituitary ACTH secretion (Cushing disease).",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "A central-to-peripheral ACTH gradient greater than 3 after corticotropin-releasing hormone is 95% sensitive and almost 100% specific for the diagnosis of Cushing disease.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Ectopic localization",
                "In ectopic ACTH syndrome, which anatomic source is most commonly identified on detailed imaging series?",
                [
                    "Bronchial carcinoid (lung neuroendocrine tumor)",
                    "Medullary thyroid carcinoma",
                    "Pheochromocytoma",
                    "Primary adrenal carcinoma",
                ],
                0,
                "Bronchial carcinoids are the most frequent identifiable ectopic source in large series; thymic NETs and pancreatic islet tumors are also important.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "CT of the neck, chest, and abdomen often reveals a bronchial carcinoid (ie, lung neuroendocrine tumor, the most common source)",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Cyclic Cushing",
                "Biochemical hypercortisolism fluctuates >100% between visits in a patient with otherwise classic features. What is the best approach?",
                [
                    "Immediate bilateral adrenalectomy without repeat testing",
                    "Reassess during an active hypercortisol phase when clinically indicated",
                    "Exclude Cushing syndrome because of variability",
                    "Start lifelong mifepristone without further workup",
                ],
                1,
                "Marked biochemical variability occurs in ~15% of patients; prolonged true 'off' phases are rare—pragmatic reassessment during active disease is reasonable.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "In such situations, in the face of uncertainty, it may be appropriate to wait and then reassess when the disease is in an active phase.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Medical therapy bridge",
                "A patient has persistent Cushing disease after failed transsphenoidal surgery and is awaiting pituitary radiation. Which interim strategy is appropriate?",
                [
                    "Observation only despite symptomatic hypercortisolism",
                    "Metyrapone or ketoconazole to lower cortisol while awaiting radiation effect",
                    "High-dose dexamethasone chronically",
                    "Immediate thoracic exploration without localization",
                ],
                1,
                "Medical adrenal blockade can control cortisol while radiation takes months to years for biochemical remission.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Medical therapy with metyrapone, ketoconazole, or mifepristone may be used while awaiting normalization.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Etomidate",
                "A patient with severe Cushing syndrome develops refractory hyperglycemia and sepsis with cortisol >40 μg/dL despite oral blockade. What is the best acute cortisol-lowering option?",
                [
                    "Increase physiologic hydrocortisone replacement",
                    "Intravenous etomidate infusion with monitoring",
                    "Oral dexamethasone 8 mg daily",
                    "Observation until elective surgery",
                ],
                1,
                "IV etomidate rapidly lowers cortisol in life-threatening hypercortisolism when administered with appropriate intensive care monitoring.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "should be treated with intravenous etomidate, which rapidly and effectively lowers cortisol when administered with due care.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Pituitary incidentaloma trap",
                "ACTH-dependent Cushing syndrome is confirmed. Pituitary MRI shows a 4-mm incidental lesion in an older patient; chest CT is normal. What is the critical next step before transsphenoidal surgery?",
                [
                    "Proceed to surgery based on MRI alone",
                    "Bilateral inferior petrosal sinus sampling",
                    "Start pasireotide indefinitely",
                    "Unilateral adrenalectomy",
                ],
                1,
                "Incidental pituitary microadenomas are common; BIPSS confirms pituitary ACTH secretion before pituitary surgery when ectopic disease remains possible.",
                ref(
                    "Barriers to Optimal Practice",
                    "MRI may fail to detect a corticotroph tumor even with optimal imaging protocols; especially in older patients, incidental pituitary lesions may be mistaken for a corticotroph tumor.",
                ),
            ),
        ]
    )

    # --- True/False (8) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Screening tests",
                "Urinary free cortisol is the preferred first-line screening test for all adults with mild suspected Cushing syndrome.",
                False,
                "Many clinicians start with overnight 1-mg dexamethasone suppression; UFC is often reserved for indeterminate cases because assay sensitivity varies.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "it is probably best to reserve urinary free cortisol measurement for those patients whose other test results are indeterminate",
                ),
            ),
            tf(
                f"{p}-tf2",
                "ACTH thresholds",
                "A 9-AM plasma ACTH concentration persistently less than 10 pg/mL supports an adrenal source of hypercortisolism.",
                True,
                "Values <10 pg/mL indicate adrenal autonomy when sampling is correct.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "a concentration less than 10 pg/mL (<2.2 pmol/L) indicates an adrenal source",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Pituitary MRI",
                "A normal pituitary MRI excludes Cushing disease.",
                False,
                "MRI may miss microadenomas; incidentalomas are common and can be misleading.",
                ref(
                    "Barriers to Optimal Practice",
                    "MRI may fail to detect a corticotroph tumor even with optimal imaging protocols",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Ectopic imaging",
                "⁶⁸Ga-DOTATATE PET can identify all ectopic ACTH-secreting tumors.",
                False,
                "Overt, covert, and occult ectopic sources are recognized categories—advanced imaging still misses some tumors.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Radionuclide scanning with 68Ga-DOTATATE PET can be very useful, although tumors can still be missed",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Surgery outcomes",
                "Experienced transsphenoidal surgery for Cushing disease achieves cure in approximately 90% of patients.",
                True,
                "First-line pituitary surgery by an experienced surgeon has a high remission rate.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "transsphenoidal surgery by an experienced surgeon should have a high cure rate, approaching 90%",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Dexamethasone suppression",
                "A normal overnight 1-mg dexamethasone-suppression test alone definitively excludes mild Cushing syndrome.",
                False,
                "Every test has false positives and negatives; interpretation depends on pretest probability and staged testing.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Every type of investigation will have a significant false-positive and false-negative rate.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Cyclic Cushing",
                "Biochemical variability exceeding 100% has been reported in approximately 15% of patients with Cushing syndrome.",
                True,
                "Marked fluctuation is recognized and can complicate diagnosis.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "variability by more than 100% in 15% of patients with all causes of Cushing syndrome has been noted",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Medical therapy monitoring",
                "Ketoconazole for hypercortisolism requires monitoring of liver function tests.",
                True,
                "Ketoconazole is effective but hepatotoxicity risk mandates LFT surveillance.",
                ref(
                    "Case 2 (Continued)",
                    "Ketoconazole (Answer D) is probably the most suitable, but it requires frequent monitoring of liver function.",
                ),
            ),
        ]
    )

    # --- Assertion/Reason (8) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "BIPSS",
                "Assertion: A central-to-peripheral ACTH gradient greater than 3 after CRH during BIPSS supports Cushing disease.",
                "Reason: CRH stimulates pituitary corticotrophs to release ACTH into the petrosal sinuses disproportionately compared with peripheral blood.",
                0,
                "Both are true and the CRH-stimulated gradient mechanism explains the assertion.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "A central-to-peripheral ACTH gradient greater than 3 after corticotropin-releasing hormone is 95% sensitive and almost 100% specific for the diagnosis of Cushing disease.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Clinical probability",
                "Assertion: A young woman with a long history of mild Cushing features is more likely to have Cushing disease than ectopic ACTH.",
                "Reason: Ectopic ACTH syndrome more often presents with severe biochemistry and hypokalemia in older patients.",
                1,
                "Both statements are true, but demographics only shift pretest probability—they are not pathognomonic.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "A young woman with a long history of symptoms and mild Cushing syndrome is much more likely to have Cushing disease, while an older man with severe biochemistry is more likely to have an ectopic source, but there is considerable overlap",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Etomidate",
                "Assertion: Intravenous etomidate should be considered when Cushing syndrome causes overwhelming metabolic complications.",
                "Reason: Etomidate rapidly inhibits 11β-hydroxylase and lowers serum cortisol when carefully administered.",
                0,
                "Both are true; etomidate is the acute rescue option described for severe hypercortisolism.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "should be treated with intravenous etomidate, which rapidly and effectively lowers cortisol when administered with due care.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Circadian testing",
                "Assertion: Late-night salivary cortisol is useful in diagnosing Cushing syndrome.",
                "Reason: Cushing syndrome is characterized by loss of the normal nocturnal decline in cortisol secretion.",
                0,
                "Both are true and causally linked through loss of circadian rhythmicity.",
                ref(
                    "Significance of the Clinical Problem",
                    "most apparent and demonstrable by loss of the normal circadian rhythmicity and failure to show adequate feedback regulation.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Ectopic biochemistry",
                "Assertion: Marked hypokalemia with very high ACTH and cortisol suggests ectopic ACTH secretion.",
                "Reason: Ectopic ACTH secretion never occurs in Cushing disease.",
                2,
                "Assertion is true as a probabilistic clue, but the reason is false—severe Cushing disease can also cause hypokalemia.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Generally, the higher the levels of ACTH and cortisol, the more severe the metabolic upset and the presence of hypokalemia, and the more likely there is an ectopic source, but no biochemical or clinical feature is pathognomonic.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Bilateral macronodular hyperplasia",
                "Assertion: Unilateral adrenalectomy may normalize cortisol in bilateral macronodular hyperplasia.",
                "Reason: The residual adrenal gland will never enlarge and hypersecrete cortisol again.",
                1,
                "Both are true statements about initial response, but the reason is false—recurrence on the contralateral side is common.",
                ref(
                    "Case 2 (Continued)",
                    "unilateral adrenalectomy (Answer A) of the larger lesion may normalize cortisol levels in many patients, but it is likely that the residual adrenal will continue to grow and Cushing syndrome will eventually recur.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Infection mimic",
                "Assertion: Patients with Cushing syndrome are at high risk for opportunistic and mixed pulmonary infections.",
                "Reason: Profound hypercortisolism causes immunosuppression.",
                0,
                "Both are true; infection can complicate the evaluation of suspected ectopic sources in the chest.",
                ref(
                    "Case 1 (Continued)",
                    "Patients with Cushing syndrome are at considerable risk of infections with a variety of organisms, as in this case, due to profound immunosuppression.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Definitive therapy",
                "Assertion: Surgery is the most appropriate long-term management for most causes of Cushing syndrome when feasible.",
                "Reason: Medical therapy permanently cures corticotroph adenomas in most patients.",
                2,
                "Assertion is true, but medical therapy is usually temporizing—not curative for pituitary adenoma.",
                ref(
                    "Main Conclusions",
                    "The most appropriate long-term management is surgery.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "6",
        "title": "Complexities in the Diagnosis and Treatment of Cushing Syndrome",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Ashley B. Grossman, BA BSc, MD, PhD (Hon.causa), FRCP, FMedSci.",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_06_Complexities_in_the_Diagnosis_and_Treatment_of_Cushing_Syndrome.md",
        "items": items,
    }


def build_chapter_05() -> dict:
    p = "e21-05"
    items: list[dict] = []

    # --- Notes (12; 7 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Glucocorticoid choice",
                "Why dexamethasone should not be used for adrenal insufficiency replacement",
                "Its long half-life prevents physiologic circadian replacement, and the smallest available tablet potency commonly causes overtreatment and iatrogenic Cushing syndrome with limited dose-titration flexibility.",
                ref(
                    "Glucocorticoid Replacement Therapy",
                    "Dexamethasone should not be used in the treatment of adrenal insufficiency for several reasons. It has a long half-life, which does not allow for diurnal replacement.",
                ),
            ),
            note(
                f"{p}-n2",
                "Hydrocortisone dosing",
                "How to initiate hydrocortisone replacement in adrenal insufficiency",
                "Typical total daily dose is 15–25 mg in 2–3 divided doses mimicking the cortisol nadir and peaks. Prednisone/prednisolone 4–6 mg once each morning is an alternative when once-daily dosing is preferred.",
                ref(
                    "Glucocorticoid Replacement Therapy",
                    "Hydrocortisone is the most commonly used glucocorticoid, with a starting dosage of 15 to 25 mg daily in divided (2 to 3) doses.",
                ),
            ),
            note(
                f"{p}-n3",
                "Mineralocorticoid scope",
                "Why mineralocorticoid replacement is required in primary but not secondary adrenal insufficiency",
                "Primary adrenal failure destroys the zona glomerulosa; ~95% of patients need fludrocortisone. Secondary AI retains aldosterone secretion via the renin–angiotensin system.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Mineralocorticoid replacement therapy consists of fludrocortisone, 100 mcg daily (usually 50-300 mcg daily), and is required in 95% of patients with primary adrenal insufficiency.",
                ),
            ),
            note(
                f"{p}-n4",
                "Monitoring glucocorticoids",
                "Clinical monitoring of glucocorticoid replacement",
                "Assess weight, energy, sleep, sick-day steroid use, and crisis history. Routine bloodwork is not mandatory, though post-dose cortisol can confirm exposure. Overtreatment causes weight gain and cushingoid features; undertreatment causes fatigue, nausea, and crisis risk.",
                ref(
                    "Glucocorticoid Replacement Therapy",
                    "Monitoring of glucocorticoid replacement therapy includes history and physical examination (Table 2).",
                ),
            ),
            note(
                f"{p}-n5",
                "DHEA in women",
                "How to approach DHEA replacement in women with adrenal insufficiency",
                "Consider a trial of DHEA 25 mg daily in symptomatic women (especially low libido/fatigue) after stabilizing glucocorticoid and mineralocorticoid therapy; target mid-normal DHEA-S and reassess at ≥6 months.",
                ref(
                    "Glucocorticoid Replacement Therapy",
                    "Androgen replacement therapy has been described in women with either primary or secondary adrenal insufficiency with a starting dehydroepiandrosterone (DHEA) dosage of 25 mg daily.",
                ),
            ),
            note(
                f"{p}-n6",
                "Mineralocorticoid monitoring",
                "Monitoring fludrocortisone therapy",
                "Track orthostatic blood pressure, edema, potassium, sodium, and renin (or renin plasma activity) at least yearly or 3 months after dose changes. Goal: no orthostasis and renin near normal.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Monitoring includes assessment of orthostatic vitals during each visit, electrolytes, and renin plasma activity at least yearly or 3 months after each dosage adjustment (Table 2).",
                ),
            ),
            note(
                f"{p}-n7",
                "Adrenal crisis",
                "Why sick-day education prevents adrenal crisis",
                "Even educated patients have high crisis rates during intercurrent illness. Doubling oral glucocorticoid during febrile illness and switching to parenteral steroids when vomiting or severely ill are lifesaving interventions.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "As such, comprehensive education, instruction on injection, and provision of proper supplies are important interventions for adrenal crisis prevention (Table 4).",
                ),
            ),
            note(
                f"{p}-n8",
                "Pregnancy",
                "How to adjust glucocorticoids during pregnancy in adrenal insufficiency",
                "Increase hydrocortisone ~20% in the second and third trimesters (example: 15 mg → 25 mg then 30 mg daily) and monitor whether progesterone's antimineralocorticoid effect requires fludrocortisone adjustment late in pregnancy.",
                ref(
                    "Case 1",
                    "Answer: C) Increase the hydrocortisone to 25 mg daily in the second trimester and to 30 mg daily in the third trimester; monitor the need for fludrocortisone adjustment",
                ),
            ),
            note(
                f"{p}-n9",
                "Shift work",
                "Glucocorticoid timing for shift workers",
                "Align the larger hydrocortisone dose with the patient's waking period and give the second dose 6–8 hours later, adjusting mineralocorticoid timing similarly.",
                ref(
                    "Table 3. Special Circumstances in Steroid Replacement Therapy",
                    "Shift worker: Change glucocorticoid and mineralocorticoid replacement according to schedule (take the larger dose of hydrocortisone on waking, the second dose 6 to 8 hours after the first one)",
                ),
            ),
            note(
                f"{p}-n10",
                "Secondary AI testing",
                "Why cosyntropin stimulation can miss secondary adrenal insufficiency",
                "The high-dose (250 mcg) ACTH test has suboptimal sensitivity for secondary AI, yielding false negatives when the adrenal cortex is atrophied but still responds to supraphysiologic ACTH.",
                ref(
                    "Case 4",
                    "it is important to remember suboptimal sensitivity of cosyntropin-stimulation testing in diagnosing secondary adrenal insufficiency (high number of false-negative results).",
                ),
            ),
            note(
                f"{p}-n11",
                "Crisis prevention kit",
                "How to structure adrenal crisis prevention for every patient",
                "Provide steroid emergency identification, teach sick-day rules (double oral dose during illness; inject and seek emergency care if unable to take oral steroids), and ensure injectable glucocorticoid supplies at home.",
                ref(
                    "Table 4. Adrenal Crisis Prevention",
                    "Sick day rule 2: inject glucocorticoid in times of inability to take oral glucocorticoid or severe illness AND proceed to emergency care",
                ),
            ),
            note(
                f"{p}-n12",
                "Dialysis",
                "Steroid replacement adjustments in end-stage renal disease",
                "Stop fludrocortisone on dialysis and anticipate loss of morning hydrocortisone during hemodialysis—plan dosing with the nephrology team.",
                ref(
                    "Table 3. Special Circumstances in Steroid Replacement Therapy",
                    "Dialysis: Stop fludrocortisone (no longer needed) Plan glucocorticoid replacement (substantial amounts of the morning glucocorticoid dose might be lost through hemodialysis)",
                ),
            ),
        ]
    )

    # --- MCQs (13) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — pregnancy",
                "A 31-year-old woman with autoimmune primary adrenal insufficiency is 8 weeks pregnant on hydrocortisone 15 mg AM + 5 mg noon and fludrocortisone 100 mcg daily. She is well with normal electrolytes and renin at goal. What additional adjustment is recommended?",
                [
                    "No changes throughout pregnancy",
                    "Double hydrocortisone in the third trimester only",
                    "Increase hydrocortisone to 25 mg daily in the second trimester and 30 mg daily in the third; monitor fludrocortisone",
                    "Increase both hydrocortisone and fludrocortisone by 20% immediately",
                ],
                2,
                "Physiologic cortisol demand rises in later pregnancy; typical practice increases hydrocortisone in the second and third trimesters and reassesses mineralocorticoid need as progesterone antagonizes aldosterone.",
                ref(
                    "Case 1",
                    "Answer: C) Increase the hydrocortisone to 25 mg daily in the second trimester and to 30 mg daily in the third trimester; monitor the need for fludrocortisone adjustment",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — circadian dosing",
                "A 23-year-old woman with primary adrenal insufficiency has afternoon fatigue and insomnia on hydrocortisone 15 mg on waking and 5 mg at bedtime, with otherwise adequate replacement. What change is best?",
                [
                    "Refer to sleep medicine without medication changes",
                    "Add 5 mg hydrocortisone at noon only",
                    "Move bedtime hydrocortisone to early afternoon and consider DHEA 25 mg trial",
                    "Switch to dexamethasone 0.5 mg at bedtime",
                ],
                2,
                "Bedtime hydrocortisone can disrupt sleep; moving dose earlier mimics circadian physiology. DHEA may help libido/fatigue in young women after glucocorticoid timing is optimized.",
                ref(
                    "Case 2",
                    "Answer: E) Trial of DHEA supplementation AND move the bedtime hydrocortisone dose to the early afternoon",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3 — SC hydrocortisone pump",
                "A panhypopituitary man after bilateral adrenalectomy for Cushing disease asks about continuous subcutaneous hydrocortisone via insulin pump. What should you tell him?",
                [
                    "Subcutaneous hydrocortisone is clearly superior for quality of life",
                    "Hydrocortisone is not FDA approved for SC infusion and patient satisfaction data are mixed",
                    "SC and oral hydrocortisone exposure are milligram-for-milligram identical",
                    "Pumps eliminate all risk of adrenal crisis",
                ],
                1,
                "Evidence is limited and heterogeneous; hydrocortisone is not FDA approved for SC infusion, and patient preference varies.",
                ref(
                    "Case 3",
                    "Answer: E) Hydrocortisone sodium succinate is not FDA approved for subcutaneous infusion AND the data regarding patient satisfaction with subcutaneous hydrocortisone are mixed",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 4 — opioid-induced AI",
                "A 35-year-old man on tramadol 400 mg daily has morning cortisol 3 μg/dL, low DHEA-S, ACTH 9 pg/mL, but peak cortisol 18 μg/dL after 250 mcg cosyntropin. Pituitary MRI a year ago was normal. Best next step?",
                [
                    "Reassure him adrenal insufficiency is excluded",
                    "Perform 1-mcg cosyntropin test",
                    "Repeat pituitary MRI urgently",
                    "Evaluate for opioid-induced central hypogonadism and manage adrenal insufficiency",
                ],
                3,
                "Long-term opioids cause secondary AI with false-negative high-dose cosyntropin tests; central hypogonadism is the most common associated endocrinopathy and should be evaluated.",
                ref(
                    "Case 4",
                    "Answer: D) Test for central hypogonadism",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 5 — COVID-19 counseling",
                "A 40-year-old teacher with well-controlled primary adrenal insufficiency asks about COVID-19 risk and steroid adjustments. What advice is correct?",
                [
                    "She meets CDC immunosuppressed criteria on her hydrocortisone dose",
                    "Begin stress dosing now because of workplace exposure",
                    "Review sick-day rules and ensure ample hydrocortisone plus an alternative glucocorticoid prescription",
                    "Refuse dexamethasone if hospitalized for COVID-19 pneumonia",
                ],
                2,
                "She is not immunosuppressed by CDC steroid thresholds, but infection remains a crisis trigger—reinforce sick-day rules and medication supply redundancy.",
                ref(
                    "Case 5",
                    "Answer: C) She should review sick-day rules and ensure that she has access to an ample supply of hydrocortisone and an alternative glucocorticoid",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Glucocorticoid selection",
                "Which glucocorticoid is least appropriate for chronic replacement in primary adrenal insufficiency?",
                [
                    "Hydrocortisone 20 mg/day divided",
                    "Prednisone 5 mg each morning",
                    "Prednisolone 5 mg each morning",
                    "Dexamethasone 0.25 mg each morning",
                ],
                3,
                "Dexamethasone's potency and long half-life make physiologic replacement and titration difficult.",
                ref(
                    "Glucocorticoid Replacement Therapy",
                    "Dexamethasone should not be used in the treatment of adrenal insufficiency for several reasons.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Fludrocortisone dosing",
                "A patient with new primary adrenal insufficiency has orthostatic dizziness and hyperkalemia on hydrocortisone alone. Typical starting fludrocortisone dose?",
                [
                    "25 mcg daily",
                    "100 mcg daily",
                    "1 mg daily",
                    "No mineralocorticoid is ever needed",
                ],
                1,
                "Standard starting dose is 100 mcg daily, titrated by blood pressure, edema, electrolytes, and renin.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Mineralocorticoid replacement therapy consists of fludrocortisone, 100 mcg daily",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Sick-day rules",
                "A patient with adrenal insufficiency develops fever and gastroenteritis but can swallow fluids. What glucocorticoid adjustment is appropriate?",
                [
                    "Continue usual dose until recovered",
                    "Double the daily oral glucocorticoid dose until well for 24 hours",
                    "Stop hydrocortisone to avoid Cushing syndrome",
                    "Switch permanently to twice the maintenance dose",
                ],
                1,
                "Sick-day rule 1: double daily oral glucocorticoid during intercurrent illness until recovered for one day.",
                ref(
                    "Table 4. Adrenal Crisis Prevention",
                    "Sick day rule 1: double daily glucocorticoid dose in times of illness until well for 1 day",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Diabetes and glucocorticoid choice",
                "A patient with primary adrenal insufficiency and insulin-dependent diabetes has wide glucose excursions on divided hydrocortisone. What adjustment may help?",
                [
                    "Switch to once-daily prednisolone to smooth peaks",
                    "Stop all glucocorticoids",
                    "Replace fludrocortisone with dexamethasone",
                    "Use only mineralocorticoid",
                ],
                0,
                "Longer-acting morning prednisolone may reduce cortisol-driven glucose peaks compared with short-acting divided hydrocortisone.",
                ref(
                    "Table 3. Special Circumstances in Steroid Replacement Therapy",
                    "Insulin-dependent diabetes mellitus: Consider longer-acting glucocorticoids (eg, prednisolone) to avoid cortisol-driven peaks and troughs in blood glucose",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Dialysis",
                "A patient with primary adrenal insufficiency starts hemodialysis. What change to steroid therapy is indicated?",
                [
                    "Increase fludrocortisone to 200 mcg",
                    "Discontinue fludrocortisone and coordinate morning hydrocortisone with dialysis timing",
                    "Add dexamethasone nightly",
                    "No changes ever needed on dialysis",
                ],
                1,
                "Fludrocortisone is not needed on dialysis; morning hydrocortisone may be lost in the dialysate and requires planning.",
                ref(
                    "Table 3. Special Circumstances in Steroid Replacement Therapy",
                    "Dialysis: Stop fludrocortisone (no longer needed)",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Hot environment",
                "A patient with primary adrenal insufficiency plans prolonged work in a hot climate. What adjustment should be considered?",
                [
                    "Stop fludrocortisone to prevent hypertension",
                    "Additional salt intake and possible fludrocortisone increase for sweat losses",
                    "Switch to dexamethasone for heat stability",
                    "Halve hydrocortisone to reduce sweating",
                ],
                1,
                "Heat increases salt/water losses; additional salt and sometimes higher fludrocortisone compensate.",
                ref(
                    "Table 3. Special Circumstances in Steroid Replacement Therapy",
                    "Hot environment: Additional salt requirement to replace sweat losses Consider increasing fludrocortisone by 50 to 100 mg daily to compensate for salt and water loss",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Potency equivalents",
                "According to Table 1, which daily regimen approximates 20 mg hydrocortisone equivalent?",
                [
                    "Prednisone 5 mg once daily",
                    "Cortisone acetate 30–40 mg daily",
                    "Methylprednisolone 16 mg daily",
                    "Dexamethasone 1 mg daily",
                ],
                0,
                "Prednisone 5 mg ≈ 20 mg hydrocortisone equivalent per the chapter potency table.",
                ref(
                    "Table 1. Glucocorticoid Type and Potency",
                    "Prednisone 0.25 Hydrocortisone Equivalent ... Total Daily Dose 5 mg",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Adrenal crisis triggers",
                "Which scenario most commonly precipitates adrenal crisis in patients with chronic adrenal insufficiency?",
                [
                    "Mild seasonal allergies",
                    "Viral gastroenteritis or upper respiratory infection",
                    "Routine dental cleaning without stress dosing",
                    "Single missed noon hydrocortisone dose while well",
                ],
                1,
                "Intercurrent infection—especially GI illness with vomiting—is the classic crisis trigger; education and injectable supplies are critical.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Adrenal crisis usually occurs during a viral illness, such as gastroenteritis or an upper respiratory infection.",
                ),
            ),
        ]
    )

    # --- True/False (8) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Dexamethasone",
                "Dexamethasone is preferred for adrenal insufficiency because its long half-life simplifies once-daily dosing.",
                False,
                "Long half-life prevents physiologic circadian replacement and commonly causes overtreatment.",
                ref(
                    "Glucocorticoid Replacement Therapy",
                    "Dexamethasone should not be used in the treatment of adrenal insufficiency for several reasons.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Mineralocorticoid indication",
                "Fludrocortisone is required in approximately 95% of patients with primary adrenal insufficiency.",
                True,
                "Primary adrenal cortex destruction impairs aldosterone production in most patients.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "is required in 95% of patients with primary adrenal insufficiency.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Glucocorticoid monitoring",
                "Routine blood tests are mandatory to monitor stable glucocorticoid replacement in adrenal insufficiency.",
                False,
                "Clinical assessment predominates; labs are optional though post-dose cortisol can confirm exposure.",
                ref(
                    "Table 2. Monitoring Steroid Replacement Therapy",
                    "No bloodwork is needed for monitoring of therapy, but can measure post-dose cortisol to confirm exposure",
                ),
            ),
            tf(
                f"{p}-tf4",
                "DHEA evidence",
                "DHEA replacement in women with adrenal insufficiency may improve fatigue, mood, and libido.",
                True,
                "Meta-analyses show modest but statistically significant quality-of-life benefits, greater in younger women.",
                ref(
                    "Glucocorticoid Replacement Therapy",
                    "small but statistically significant improvement in quality of life, fatigue, mood, and libido in women treated with DHEA",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Cosyntropin test",
                "A normal 250-mcg cosyntropin test reliably excludes secondary adrenal insufficiency.",
                False,
                "High false-negative rate in secondary AI is a recognized pitfall, especially with opioid use.",
                ref(
                    "Case 4",
                    "suboptimal sensitivity of cosyntropin-stimulation testing in diagnosing secondary adrenal insufficiency (high number of false-negative results).",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Pregnancy renin",
                "Plasma renin is a reliable marker of mineralocorticoid adequacy throughout pregnancy.",
                False,
                "Renin is physiologically increased in pregnancy and is not useful for monitoring fludrocortisone.",
                ref(
                    "Table 3. Special Circumstances in Steroid Replacement Therapy",
                    "Monitor with sodium and potassium (plasma renin is physiologically increased in pregnancy and thus not useful)",
                ),
            ),
            tf(
                f"{p}-tf7",
                "CDC immunosuppression",
                "A patient on hydrocortisone 15 mg daily meets the CDC definition of immunosuppressed.",
                False,
                "CDC threshold is ≥20 mg prednisone equivalent (~80–100 mg hydrocortisone).",
                ref(
                    "Case 5",
                    "The Centers for Disease Control definition of immunosuppressed, however, is taking at least 20 mg daily of prednisone or equivalent (80-100 mg of hydrocortisone)",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Hypertension management",
                "In adrenal insufficiency with hypertension on adequate fludrocortisone, calcium-channel blockers are reasonable antihypertensives.",
                True,
                "Calcium-channel blockers and alpha-blockers are preferred; ACE inhibitors/ARBs are less effective.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "effective antihypertensive agents include calcium-channel blockers and α-adrenergic blockers",
                ),
            ),
        ]
    )

    # --- Assertion/Reason (8) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Hydrocortisone dosing",
                "Assertion: Hydrocortisone should be given in divided daily doses for adrenal insufficiency.",
                "Reason: Physiologic cortisol secretion follows a circadian rhythm with a morning peak.",
                0,
                "Both are true and the circadian physiology explains divided dosing.",
                ref(
                    "Main Conclusions",
                    "Glucocorticoid potency and circadian delivery need to be considered when deciding on the glucocorticoid type, dose, and frequency of administration.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Mineralocorticoid",
                "Assertion: Fludrocortisone is not routinely required in secondary adrenal insufficiency.",
                "Reason: Secondary adrenal insufficiency always abolishes aldosterone secretion.",
                2,
                "Assertion is true, but aldosterone is largely preserved in secondary AI—the reason is false.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Mineralocorticoid replacement therapy consists of fludrocortisone, 100 mcg daily (usually 50-300 mcg daily), and is required in 95% of patients with primary adrenal insufficiency.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Pregnancy",
                "Assertion: Hydrocortisone dose should increase during the second and third trimesters of pregnancy in adrenal insufficiency.",
                "Reason: Placental CRH drives adrenal cortisol hyperplasia and higher cortisol requirements.",
                0,
                "Both are true; pregnancy increases physiologic cortisol demand.",
                ref(
                    "Case 1",
                    "Cortisol production increases during pregnancy, possibly due to increased placental production of corticotropin-releasing hormone",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Opioid-induced AI",
                "Assertion: Chronic opioid therapy can cause secondary adrenal insufficiency with a false-negative cosyntropin test.",
                "Reason: Opioids stimulate adrenal cortisol production via CRH hypersecretion.",
                2,
                "Assertion is true; opioids suppress the HPA axis—the stated stimulatory reason is false.",
                ref(
                    "Case 4",
                    "Opioid-induced adrenal insufficiency should be considered in this patient due to long-term use of tramadol",
                ),
            ),
            ar(
                f"{p}-ar5",
                "DHEA timing",
                "Assertion: DHEA should be initiated only after glucocorticoid and mineralocorticoid therapy are stabilized.",
                "Reason: DHEA replaces mineralocorticoid deficiency.",
                2,
                "Assertion reflects best practice; DHEA is androgen replacement, not mineralocorticoid.",
                ref(
                    "Glucocorticoid Replacement Therapy",
                    "Another approach is to discuss DHEA with every woman who has adrenal insufficiency after stabilization of glucocorticoid and mineralocorticoid therapy.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Sick-day rules",
                "Assertion: Patients unable to take oral glucocorticoids during severe illness should receive injectable steroids and emergency care.",
                "Reason: Continued oral absorption is guaranteed during vomiting.",
                3,
                "Assertion is true; vomiting prevents reliable oral absorption—the reason is false.",
                ref(
                    "Table 4. Adrenal Crisis Prevention",
                    "Sick day rule 2: inject glucocorticoid in times of inability to take oral glucocorticoid or severe illness AND proceed to emergency care",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Subcutaneous hydrocortisone",
                "Assertion: Continuous subcutaneous hydrocortisone is not FDA approved.",
                "Reason: No study has ever administered hydrocortisone subcutaneously.",
                2,
                "Assertion is true; studies exist but FDA approval for SC infusion is lacking—the reason is false.",
                ref(
                    "Case 3",
                    "Hydrocortisone is not FDA approved for subcutaneous infusion (Answer B)",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Exercise stress dosing",
                "Assertion: Extra hydrocortisone doses may be needed during prolonged strenuous exercise.",
                "Reason: Marathon-level exertion increases cortisol requirements and salt losses.",
                0,
                "Both are true; the chapter advises small supplemental doses and salt during extreme exercise.",
                ref(
                    "Table 3. Special Circumstances in Steroid Replacement Therapy",
                    "consider 2.5 to 5 mg hydrocortisone every 3 hours during a marathon run or triathlon",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "5",
        "title": "Selection, Dosing, and Monitoring of Steroid Replacement in the Patient With Adrenal Failure",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Irina Bancos, MD; Richard Auchus, MD, PhD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_05_Selection_Dosing_and_Monitoring_of_Steroid_Replacement_in_the_Patient_With_Adrenal_Failure.md",
        "items": items,
    }


MODULES = {
    "endo2021_chapter_06_Complexities_in_the_Diagnosis_and_Treatment_of_Cushing_Syndrome.json": build_chapter_06,
    "endo2021_chapter_05_Selection_Dosing_and_Monitoring_of_Steroid_Replacement_in_the_Patient_With_Adrenal_Failure.json": build_chapter_05,
}


def write_module(filename: str, data: dict) -> tuple[Path, Path | None]:
    PORTAL_DATA.mkdir(parents=True, exist_ok=True)
    portal_path = PORTAL_DATA / filename
    portal_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    master_path: Path | None = None
    if MASTER_DATA.exists():
        MASTER_DATA.mkdir(parents=True, exist_ok=True)
        master_path = MASTER_DATA / filename
        shutil.copy2(portal_path, master_path)
    return portal_path, master_path


def main() -> None:
    for filename, builder in MODULES.items():
        data = builder()
        portal_path, master_path = write_module(filename, data)
        counts: dict[str, int] = {}
        for item in data["items"]:
            counts[item["type"]] = counts.get(item["type"], 0) + 1
        notes = counts.get("note", 0)
        wh = sum(
            1
            for i in data["items"]
            if i["type"] == "note" and i.get("title", "").startswith(("Why", "How"))
        )
        print(f"Wrote {portal_path} ({len(data['items'])} items, {counts}, Why/How {wh}/{notes})")
        if master_path:
            print(f"  Copied to {master_path}")
        else:
            print(f"  Skipped copy — {MASTER_DATA} not found")


if __name__ == "__main__":
    main()
