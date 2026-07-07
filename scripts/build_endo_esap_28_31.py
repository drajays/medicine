#!/usr/bin/env python3
"""Generate remediated ESAP 2021 modules e21-28 through e21-31 (Pediatric batch)."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")


def build_chapter_28() -> dict:
    p = "e21-28"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Diagnostic threshold",
                "Why use a urine osmolality threshold of at least 750 mOsm/kg",
                "Thresholds of 600–750 mOsm/kg can miss partial DI; clinical practice shows patients subsequently diagnosed with partial DI whose initial urine osmolality fell between these values.",
                ref(
                    "Main Conclusions",
                    "Thus, it is advised to use a urine osmolality threshold of at least 750 mOsm/kg to assess the possibility of DI when there is clinical suspicion for disease.",
                ),
            ),
            note(
                f"{p}-n2",
                "Established hyperosmolality",
                "How to confirm DI without water deprivation when plasma is already hyperosmolar",
                "When simultaneous plasma osmolality exceeds 300 mOsm/kg and urine osmolality is below 300 mOsm/kg after excluding other causes of polyuria, DI is confirmed—formal water deprivation is unnecessary and desmopressin trial plus MRI can proceed.",
                ref(
                    "Central DI",
                    "In children with polyuria and polydipsia, a plasma osmolality exceeding 300 mOsm/kg, reflecting hyperosmolality, with a simultaneous urine osmolality less than 300 mOsm/kg confirms the diagnosis of DI.",
                ),
            ),
            note(
                f"{p}-n3",
                "Polyuria differential",
                "Non-DI causes of polyuria in children",
                "Before pursuing central DI, exclude hyperglycemia, thyrotoxicosis, hypercalcemia, hypokalemia, protein malnutrition, lithium, and psychogenic polydipsia—the most common mimic of central DI.",
                ref(
                    "Main Conclusions",
                    "In addition to hyperglycemia, other conditions such as thyrotoxicosis, hypercalcemia, and hypokalemia can lead to polyuria.",
                ),
            ),
            note(
                f"{p}-n4",
                "Etiology workup",
                "Why MRI is mandatory after central DI is established",
                "Once central DI is confirmed and the etiology is unknown, pituitary MRI is mandatory; the pediatric endocrinologist must decide when to repeat imaging and whether CNS biopsy is required.",
                ref(
                    "Significance of the Clinical Problem",
                    "After establishing a diagnosis of central DI, MRI of the pituitary is mandatory if the etiology is not known.",
                ),
            ),
            note(
                f"{p}-n5",
                "Thickened stalk",
                "How to surveil central DI with pituitary stalk thickening",
                "Measure tumor markers and anterior pituitary hormones at presentation; repeat pituitary MRI and markers every 3 months for 1–2 years, then yearly for 2 years. CSF tumor markers (hCG, α-fetoprotein) are more sensitive than serum when germ-cell tumor is suspected.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Pituitary MRI and measurement of serum tumor markers and anterior pituitary hormones should be performed every 3 months for 1 to 2 years, then yearly for 2 years.",
                ),
            ),
            note(
                f"{p}-n6",
                "Ectopic neurohypophysis",
                "Ectopic posterior pituitary bright spot on MRI",
                "An ectopic posterior pituitary bright spot on T1-weighted images usually indicates the child does not have central DI but is at risk for anterior pituitary hormone deficiencies.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "A child who has an ectopic posterior pituitary gland recognized on T1-weighted images as an ectopic posterior pituitary bright spot does not typically have central DI but is at risk for anterior pituitary hormone deficiencies.",
                ),
            ),
            note(
                f"{p}-n7",
                "Psychogenic polydipsia",
                "Why psychogenic polydipsia is the key mimic",
                "Psychogenic polydipsia is the most common state that must be distinguished from central DI; severe cases can cause hyponatremic seizures, while persistently low or low-normal serum sodium without hypernatremia raises suspicion for psychiatric polydipsia.",
                ref(
                    "Main Conclusions",
                    "Psychogenic polydipsia is the most common state that must be distinguished from central DI.",
                ),
            ),
            note(
                f"{p}-n8",
                "Desmopressin therapy",
                "How to choose desmopressin formulation in children",
                "Desmopressin remains mainstay therapy since the 1970s; oral, intranasal, and subcutaneous formulations require individualized dose and schedule titration. Adverse effects include fluid retention and hyponatremia.",
                ref(
                    "Treatment of the Child With Central DI",
                    "Desmopressin is available for outpatient therapy as a pill, nasal spray, or subcutaneous injection. The adverse effects of desmopressin include fluid retention and hyponatremia.",
                ),
            ),
            note(
                f"{p}-n9",
                "Post-neurosurgery",
                "Triphasic DI/SIADH/DI response after pituitary surgery",
                "Following complete stalk resection—common after craniopharyngioma surgery—children may show a well-described triphasic pattern of DI, then SIADH, then DI again in the immediate postoperative period.",
                ref(
                    "Central DI Following Neurosurgery: The Triphasic Response",
                    "A well-described triphasic response of DI/SIADH/DI is seen in the immediate postoperative period following complete stalk resection, as observed in many children following surgery for craniopharyngioma.",
                ),
            ),
            note(
                f"{p}-n10",
                "Neonatal DI",
                "How to manage central DI in infants",
                "Infants cannot communicate thirst; fluids alone or thiazide diuretics with low solute intake may suffice. If desmopressin is used, choose a low dose and monitor closely for hyponatremia.",
                ref(
                    "The Infant With Central DI",
                    "Often, fluids alone are used to treat DI, although adding a thiazide class of diuretics with a low solute intake can be effective.",
                ),
            ),
            note(
                f"{p}-n11",
                "Genetic DI",
                "Autosomal dominant central DI and AVP gene variants",
                "Genetic central DI typically shows absent posterior bright spot with normal stalk size; more than 55 pathogenic AVP-peptide variants are described, most autosomal dominant, reducing AVP biological activity.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "More than 55 pathogenic variants that cause central DI have been described; most are associated with autosomal dominant inheritance.",
                ),
            ),
            note(
                f"{p}-n12",
                "Partial DI pitfall",
                "Why partial or evolving DI requires prolonged testing",
                "Patients with partial or evolving central DI may have reassuringly normal initial labs and require prolonged water deprivation to prove DI—premature reassurance can delay diagnosis.",
                ref(
                    "Summary",
                    "those with partial or evolving central DI can have reassuringly normal laboratory results and may require prolonged water deprivation to prove there is DI.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case — established DI",
                "A child has serum sodium 152 mEq/L, glucose 80 mg/dL, BUN 8 mg/dL, and urine osmolality 193 mOsm/kg. Other causes of polyuria are excluded. What is the best next step?",
                [
                    "Order copeptin to establish DI of any cause",
                    "Perform inpatient water-deprivation testing",
                    "Initiate desmopressin therapy",
                    "Defer all therapy until formal osmolality is measured",
                ],
                2,
                "Calculated serum osmolality already exceeds 300 mOsm/kg with dilute urine—DI is established. A desmopressin trial (with MRI if central) is appropriate without water deprivation.",
                ref(
                    "Case 2",
                    "Answer: C) Therapy with desmopressin can be initiated",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 3 — thickened stalk",
                "A 14-year-old boy has water-deprivation–confirmed central DI. MRI shows absent posterior bright spot and infundibular thickening without mass; serum hCG and α-fetoprotein are negative. He is Tanner 4 with 16-mL testes, no headaches or vision changes. What is true?",
                [
                    "Absent bright spot confirms CNS malignancy risk",
                    "Pubertal findings indicate stalled puberty",
                    "Cerebrospinal fluid should be sampled for tumor markers",
                    "Annual MRI for 5 years is sufficient surveillance",
                ],
                2,
                "Thickened stalk raises risk for infiltrative disease; CSF tumor markers are more sensitive than serum for occult germ-cell tumors. MRI should be every 3 months initially, not yearly.",
                ref(
                    "Case 3",
                    "Answer: C) Cerebrospinal fluid sample should be obtained",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 4 — borderline sodium",
                "A 4-year-old drinks from puddles and bathroom faucets with new enuresis and mild dehydration. Sodium 144 mEq/L, glucose 72 mg/dL, urine osmolality 184 mOsm/kg. What is true?",
                [
                    "High copeptin would establish central DI",
                    "Inpatient water-deprivation study is indicated",
                    "MRI should precede all other testing",
                    "Desmopressin should be started immediately",
                ],
                1,
                "Hyperosmolality is not yet established; inpatient water deprivation is needed before MRI or desmopressin when CNS symptoms are absent.",
                ref(
                    "Case 4",
                    "Answer: B) A water-deprivation study is indicated and should be done on an inpatient basis",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Excluding DI",
                "Which paired laboratory findings best excludes diabetes insipidus?",
                [
                    "Serum osmolality <270 mOsm/kg with maximally concentrated urine",
                    "Serum osmolality >300 mOsm/kg with urine osmolality <300 mOsm/kg",
                    "Serum sodium >145 mEq/L with urine output >4 mL/kg/h",
                    "Normal glucose with urine osmolality 400 mOsm/kg",
                ],
                0,
                "Low serum osmolality with maximally concentrated urine excludes DI; hyperosmolality with dilute urine confirms it.",
                ref(
                    "Central DI",
                    "if a simultaneous serum osmolality is less than 270 mOsm/kg and the urine osmolality is maximally concentrated, the diagnosis of DI is excluded.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Stalk thickness",
                "In children with central DI and stalk thickening, an infundibular diameter greater than 4.5 mm correlates with what outcome?",
                [
                    "Resolution of hypophysitis within 6 months",
                    "Greater likelihood of multiple anterior pituitary hormone deficiencies",
                    "Definitive diagnosis of germ-cell tumor",
                    "No need for repeat MRI",
                ],
                1,
                "Stalk thickness >4.5 mm correlates with higher risk of evolving panhypopituitarism.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "an infundibular stalk greater than 4.5 mm in thickness was correlated with a greater likelihood of developing multiple anterior pituitary hormone deficiencies.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Germ-cell tumor workup",
                "A child with central DI and thickened stalk has no bone lesions of Langerhans cell histiocytosis. What should be obtained at initial presentation?",
                [
                    "Immediate pituitary biopsy",
                    "Serum and CSF quantitative hCG and α-fetoprotein",
                    "Empiric chemotherapy",
                    "PET scan before any biochemical testing",
                ],
                1,
                "Tumor markers in serum and CSF assess for CNS germ-cell tumor when LCH is not evident.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "serum and cerebrospinal fluid tumor markers for quantitative hCG and α-fetoprotein should be obtained at initial presentation to assess for the possibility of a central nervous system germ-cell tumor.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Normal stalk surveillance",
                "A child has new central DI, normal pituitary stalk on MRI, and no CNS red-flag symptoms. What MRI schedule is recommended?",
                [
                    "No repeat imaging ever needed",
                    "Repeat MRI in 3–6 months, then every 6–12 months for 2 years",
                    "Monthly MRI for 5 years",
                    "MRI only if desmopressin dose increases",
                ],
                1,
                "Even a normal stalk does not exclude occult pathology; structured repeat imaging is advised.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "it is recommended to perform a repeated MRI in 3 to 6 months, then every 6 to 12 months for the next 2 years.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Craniopharyngioma",
                "Which imaging feature most strongly suggests craniopharyngioma in a sellar/suprasellar mass causing central DI?",
                [
                    "Absent posterior bright spot alone",
                    "Calcifications on CT",
                    "Thickened infundibulum without mass",
                    "Ectopic posterior pituitary",
                ],
                1,
                "Calcifications strongly suggest craniopharyngioma; CT detects them more reliably than MRI.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Calcifications strongly suggest craniopharyngioma. CT is more reliable than MRI in detecting calcifications.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Lithium effect",
                "A child on lithium presents with polyuria. What is the mechanism?",
                [
                    "Central AVP deficiency from hypothalamic injury",
                    "Reduced renal responsiveness to AVP (nephrogenic pattern)",
                    "Osmotic diuresis from hyperglycemia",
                    "Primary polydipsia from psychiatric disease",
                ],
                1,
                "Lithium reduces renal responsiveness to AVP, causing nephrogenic concentrating defects.",
                ref(
                    "Polyuria: Differential Diagnosis",
                    "Lithium is unique because it reduces the renal responsiveness to AVP, leading to defects in urinary concentrating capacity.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Copeptin testing",
                "Regarding copeptin measurement in pediatric DI workup, which statement is most accurate?",
                [
                    "Low copeptin after hypertonic saline confirms nephrogenic DI",
                    "Copeptin has been fully validated as a water-deprivation substitute in children",
                    "Copeptin may help identify central DI but has not been studied in pediatric patients",
                    "High copeptin in hyperosmolality confirms central DI",
                ],
                2,
                "Copeptin after hypertonic saline is promising but not yet studied in children; low copeptin in hyperosmolality would suggest central, not nephrogenic, DI.",
                ref(
                    "The Child With Polydipsia and Polyuria",
                    "Copeptin measurement after infusion of hypertonic saline may be an alternative approach to water-deprivation testing in diagnosing DI, but this has not been studied in pediatric patients.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "DI diagnostic criteria",
                "Which combination supports formal DI diagnosis after excluding other polyuria causes?",
                [
                    "Serum sodium >145 mEq/L, urine osmolality <300 mOsm/kg, urine output >4 mL/kg/h",
                    "Serum sodium <136 mEq/L with dilute urine",
                    "Urine osmolality >750 mOsm/kg with polydipsia",
                    "Normal serum osmolality with concentrated urine",
                ],
                0,
                "Hypernatremia/hyperosmolality with dilute urine and high urine output defines DI once mimics are excluded.",
                ref(
                    "Central DI",
                    "DI is diagnosed when the serum sodium concentration exceeds 145 mEq/L (>145 mmol/L), urine osmolality is less than 300 mOsm/kg, urine output is persistently greater than 4 mL/kg per h, and other causes of polyuria have been excluded.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Stalk thickening epidemiology",
                "Approximately what proportion of children with central DI show thickened pituitary stalk on MRI, and what fraction of those may have germ-cell tumor?",
                [
                    "One-third thickened; ~17% germ-cell tumor",
                    "Two-thirds thickened; ~50% germ-cell tumor",
                    "10% thickened; nearly all Langerhans cell histiocytosis",
                    "All have thickened stalk; biopsy is always required",
                ],
                0,
                "About one-third have stalk thickening; among those, ~17% germ-cell tumor and ~17% LCH in one cited series.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "MRI in children with central DI shows a thickened stalk in approximately one-third of cases. Of the children with a thickened stalk, one study showed that 17% were eventually diagnosed with a germ-cell tumor and 17% were diagnosed with Langerhans cell histiocytosis.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Clinical clues",
                "Which history finding most strongly suggests pathologic thirst rather than benign increased fluid intake?",
                [
                    "Drinking extra water during sports",
                    "Drinking from toilet bowls, puddles, or others' bottles",
                    "Using a school water fountain at lunch",
                    "Parent-reported normal urine frequency",
                ],
                1,
                "Drinking from unusual sources signals abnormal thirst warranting DI evaluation.",
                ref(
                    "The Child With Polydipsia and Polyuria",
                    "Drinking from unusual sources such as puddles, bathtub faucets, the toilet, or other people's drinks suggests abnormal thirst.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Water deprivation",
                "A formal water-deprivation study is always required before diagnosing diabetes insipidus in children.",
                False,
                "When plasma osmolality already exceeds 300 mOsm/kg with urine osmolality below 300 mOsm/kg, DI is confirmed without water deprivation.",
                ref(
                    "Case 2",
                    "The main point of this vignette is to show that sometimes water-deprivation study (Answer B) is not needed, as the diagnosis is already established.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Posterior bright spot",
                "An absent posterior pituitary bright spot is specific for central nervous system malignancy.",
                False,
                "The absent bright spot is seen in all causes of central DI, not specific to tumor.",
                ref(
                    "Case 3",
                    "The absent bright spot is seen in all causes of central DI, so it is not a specific finding for a tumor etiology",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Psychogenic polydipsia",
                "Psychogenic polydipsia is the most common condition that must be distinguished from central DI.",
                True,
                "Explicitly stated in main conclusions.",
                ref(
                    "Main Conclusions",
                    "Psychogenic polydipsia is the most common state that must be distinguished from central DI.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Stalk surveillance",
                "Children with central DI and stalk thickening should have pituitary MRI every 3 months for the first 1–2 years.",
                True,
                "Recommended surveillance interval for thickened stalk.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Pituitary MRI and measurement of serum tumor markers and anterior pituitary hormones should be performed every 3 months for 1 to 2 years, then yearly for 2 years.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Ectopic neurohypophysis",
                "An ectopic posterior pituitary bright spot typically indicates central DI.",
                False,
                "Ectopic bright spot usually means no central DI but risk of anterior pituitary deficiency.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "does not typically have central DI but is at risk for anterior pituitary hormone deficiencies.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Hypercalcemia",
                "Hypercalcemia can impair renal concentrating capacity and cause polyuria.",
                True,
                "Listed among endocrine polyuria mimics.",
                ref(
                    "Polyuria: Differential Diagnosis",
                    "Hypercalcemia, regardless of etiology, can produce deficits in renal concentrating capacity.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Desmopressin safety",
                "Desmopressin therapy carries risk of hyponatremia from fluid retention.",
                True,
                "Fluid retention and hyponatremia are recognized adverse effects.",
                ref(
                    "Treatment of the Child With Central DI",
                    "The adverse effects of desmopressin include fluid retention and hyponatremia.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Common causes",
                "Idiopathic (likely hypophysitis), tumor, histiocytosis, germ-cell tumors, structural defects, and congenital genetic defects are the most common causes of central DI.",
                True,
                "Listed as most common etiologies after diagnosis.",
                ref(
                    "Main Conclusions",
                    "The most common causes are idiopathic (likely hypophysitis), tumor, histiocytosis, germ-cell tumors, structural defects, and congenital (genetic) defects.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Diagnostic threshold",
                "Assertion: A urine osmolality threshold of at least 750 mOsm/kg should be used when clinical suspicion for DI is high.",
                "Reason: Some patients initially between 600 and 750 mOsm/kg are later diagnosed with partial DI.",
                0,
                "Both true and causally linked.",
                ref(
                    "Main Conclusions",
                    "we have cared for patients who were subsequently diagnosed with partial DI whose initial urine osmolality was between these values.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "MRI mandate",
                "Assertion: Pituitary MRI is mandatory after central DI is established when etiology is unknown.",
                "Reason: MRI always reveals the diagnosis on first scan.",
                2,
                "Assertion true; initial MRI often does not reveal etiology—reason false.",
                ref(
                    "Barriers to Optimal Practice",
                    "One of the challenges in establishing the etiology of central DI is that the diagnosis is usually not known after the initial MRI.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "CSF markers",
                "Assertion: CSF tumor markers may be more sensitive than serum for occult germ-cell tumors in central DI.",
                "Reason: Germ-cell tumors never secrete hCG or α-fetoprotein into CSF.",
                2,
                "Assertion true per case discussion; reason false.",
                ref(
                    "Case 3",
                    "cerebrospinal fluid is more sensitive than serum samples.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "AVP physiology",
                "Assertion: AVP acts on V2 receptors in renal collecting ducts to insert aquaporin-2 channels.",
                "Reason: AVP binding increases collecting duct water permeability via cAMP signaling.",
                0,
                "Both true and mechanistically linked.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "AVP binds to the AVP V2 receptors in the collecting ducts of the renal tubules. Through a cyclic AMP signal transduction mechanism, this results in activation, transport, and insertion of aquaporin-2 water channels",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Triphasic response",
                "Assertion: Children after complete stalk resection may show DI, then SIADH, then DI again.",
                "Reason: This triphasic pattern never occurs after craniopharyngioma surgery.",
                2,
                "Assertion describes classic postoperative course; reason false.",
                ref(
                    "Central DI Following Neurosurgery: The Triphasic Response",
                    "A well-described triphasic response of DI/SIADH/DI is seen in the immediate postoperative period following complete stalk resection",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Infant management",
                "Assertion: Neonatal central DI is particularly difficult because infants cannot communicate thirst.",
                "Reason: Infants reliably self-regulate free water intake without caregiver input.",
                2,
                "Assertion true; infants depend on caregivers—reason false.",
                ref(
                    "The Infant With Central DI",
                    "Management of neonatal DI is particularly difficult, as infants cannot communicate thirst and are dependent on caretakers for providing fluids.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Hypernatremia without polyuria",
                "Assertion: Hypernatremia without polyuria often reflects hypernatremic dehydration rather than DI.",
                "Reason: All hypernatremia in children is due to central DI.",
                2,
                "Assertion true for dehydration settings; reason overgeneralizes.",
                ref(
                    "Hypernatremia (Hyperosmolality)",
                    "Hypernatremia in the absence of polyuria most often reflects hypernatremic dehydration",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Stalk resolution",
                "Assertion: Resolution of pituitary stalk thickening is more often associated with lymphocytic hypophysitis.",
                "Reason: Stalk thickening never resolves in any condition.",
                2,
                "Assertion true; LCH lesions can also change size—reason false.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Resolution of pituitary stalk thickening is more often associated with lymphocytic hypophysitis and confers a positive prognosis.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "28",
        "title": "Diabetes Insipidus in Children",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Craig A. Alter, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_28_diabetes_Insipidus_in_Children.md",
        "items": items,
    }


def build_chapter_29() -> dict:
    p = "e21-29"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Newborn screening",
                "Why ALD was added to newborn screening panels",
                "ALD has a presymptomatic phase and life-saving interventions exist for adrenal insufficiency and cerebral ALD; initial screening data suggest higher prevalence than previously estimated, with some boys developing adrenal insufficiency in early infancy.",
                ref(
                    "Main Conclusions",
                    "Recently, ALD was added to state newborn screening panels. Initial newborn screening data suggest that ALD may be more prevalent than previously described and adrenal insufficiency may develop in some affected boys during early infancy.",
                ),
            ),
            note(
                f"{p}-n2",
                "Pathophysiology",
                "How ABCD1 variants cause adrenal and neurologic disease",
                "ABCD1 encodes a peroxisomal VLCFA transporter; pathogenic variants raise VLCFA that accumulate in adrenal cortex, nervous system, and Leydig cells. There is no genotype-phenotype or VLCFA-degree correlation with adrenal or neurologic onset.",
                ref(
                    "Pathophysiology and Epidemiology",
                    "There is no genotype-phenotype correlation, and the degree of VLCFA elevation is not predictive of onset of adrenal insufficiency or neurologic symptoms.",
                ),
            ),
            note(
                f"{p}-n3",
                "Surveillance schedule",
                "How to monitor adrenal function in screen-positive boys",
                "Start screening shortly after ALD diagnosis: every 3–4 months under age 2 years and every 4–6 months thereafter, recognizing unpredictable infant cortisol/ACTH rhythms and ambiguous baseline results.",
                ref(
                    "Surveillance for Adrenal Insufficiency",
                    "Follow-up surveillance for adrenal insufficiency was recommended every 3 to 4 months for children younger than 2 years and every 4 to 6 months for children older than age 2 years",
                ),
            ),
            note(
                f"{p}-n4",
                "Infant testing pitfall",
                "Why 8-AM cortisol alone is inadequate in young infants with ALD",
                "Infants lack predictable diurnal ACTH/cortisol patterns; borderline ACTH requires paired cortisol, and ACTH may rise before cortisol falls—draw both when travel burden is not prohibitive.",
                ref(
                    "Case 1",
                    "The baby is unlikely to have predictable diurnal secretion of ACTH and cortisol, as he is not sleeping through the night and is younger than 6 months.",
                ),
            ),
            note(
                f"{p}-n5",
                "Stress-dose hydrocortisone",
                "When to start stress-dose hydrocortisone per the PES algorithm",
                "Stress doses begin when stimulated peak cortisol is below threshold (e.g., 17.1 μg/dL at 6 weeks in Case 2); cutoff of 18 μg/dL derives from older polyclonal assays and may differ with monoclonal assays.",
                ref(
                    "Case 2",
                    "stress doses of hydrocortisone should have been started at 6 weeks of age (Answer A), when the peak cortisol concentration was 17.1 μg/dL (471.8 nmol/L).",
                ),
            ),
            note(
                f"{p}-n6",
                "Daily hydrocortisone",
                "How to time daily hydrocortisone replacement in ALD",
                "Daily therapy is initiated when ACTH reaches ≥300 pg/mL (≥66 pmol/L) per algorithm, but clinical judgment matters—weight loss and hyperpigmentation may warrant earlier treatment despite lower ACTH.",
                ref(
                    "Case 2",
                    "Based on the algorithm, daily hydrocortisone doses should have been started at age 13 months (Answer D). The ACTH cutoff of 300 pg/mL or higher (≥66 pmol/L) was chosen",
                ),
            ),
            note(
                f"{p}-n7",
                "Replacement therapy",
                "Hydrocortisone dosing and sick-day rules in ALD adrenal insufficiency",
                "Preferred glucocorticoid is hydrocortisone 8–12 mg/m² daily in three divided doses with stress-dose escalation and injectable hydrocortisone when oral intake fails; medical identification is mandatory.",
                ref(
                    "Management of Adrenal Insufficiency",
                    "Hydrocortisone is the preferred glucocorticoid and, for ALD, the starting dosage is 8 to 12 mg/m² daily divided into 3 doses.",
                ),
            ),
            note(
                f"{p}-n8",
                "Cerebral ALD MRI",
                "Neurologic surveillance MRI schedule after positive newborn screen",
                "Brain MRI begins around 12 months, annually to age 3, then every 6 months until age 10, then annually; more frequent imaging when concerning lesions appear. Early cerebral ALD may be treated with hematopoietic stem-cell therapy.",
                ref(
                    "Neurologic Disease: Cerebral ALD and Adrenomyeloneuropathy",
                    "MRI of the brain is initiated around 12 months of age and performed annually until age 3 years, when the risk for cerebral ALD increases. Surveillance MRI of the brain is then repeated every 6 months until age 10 years.",
                ),
            ),
            note(
                f"{p}-n9",
                "Female newborn screen",
                "How to evaluate a girl with positive ALD newborn screen",
                "Obtain ABCD1 sequencing; test both parents when feasible. Symptomatic male relatives (e.g., brother with poor weight gain and hyperpigmentation) need urgent VLCFA and endocrine evaluation before molecular results return.",
                ref(
                    "Case 3",
                    "it would be most practical to have metabolic center order VLCFA measurement of the patient's brother. Thus, the patient's father, father, and brother (Answer D) should all be evaluated by the metabolic center.",
                ),
            ),
            note(
                f"{p}-n10",
                "Lifetime adrenal risk",
                "Burden of adrenal insufficiency in males with ALD",
                "Before newborn screening, ~80% lifetime prevalence of adrenal insufficiency with median diagnosis age 14 years and average 3.5-year delay after symptoms; most had endocrine symptoms at ALD diagnosis.",
                ref(
                    "Pathophysiology and Epidemiology",
                    "there was an estimated 80% lifetime prevalence of adrenal insufficiency, with most developing adrenal insufficiency during childhood and adolescence (median age of diagnosis, 14 years).",
                ),
            ),
            note(
                f"{p}-n11",
                "Screening test performance",
                "VLCFA newborn screening sensitivity and female carriers",
                "Filter-paper VLCFA testing is excellent for hemizygous males; 20% of heterozygous females lack VLCFA elevation and are not detected. Elevated VLCFA may also reflect rarer peroxisomal disorders.",
                ref(
                    "Newborn Screening",
                    "The sensitivity and specificity of the filter paper VLCFA measurements are reported to be excellent for males hemizygous for pathogenic ABCD1 variants. As 20% of females heterozygous for ABCD1 pathogenic variants do not have VLCFA elevations, they are not expected to be identified by newborn screening.",
                ),
            ),
            note(
                f"{p}-n12",
                "Behavioral changes",
                "Why subtle behavioral changes warrant reassessment in screen-positive boys",
                "Inattention or irritability may herald evolving adrenal insufficiency or cerebral ALD; normal labs 3 months ago do not preclude urgent repeat ACTH/cortisol and clinical reassessment.",
                ref(
                    "Case 4",
                    "Answer B) Make arrangements now for a repeated 8-AM measurement of ACTH and cortisol and reassess for clinical adrenal insufficiency",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — 3-month-old screen-positive boy",
                "A 3-month-old breastfed boy with ALD on newborn screen (VUS in ABCD1) presents at 1 PM with possible scrotal hyperpigmentation and normal growth. Initial screen cortisol/ACTH were 'normal.' Best next step?",
                [
                    "ACTH measurement only today",
                    "Cortisol measurement only today",
                    "Both ACTH and cortisol today",
                    "Return for 8-AM ACTH and cortisol only",
                ],
                2,
                "Infants lack predictable diurnal rhythms; paired ACTH and cortisol can be drawn in clinic. ACTH alone may be borderline without cortisol context.",
                ref(
                    "Case 1",
                    "Answer: C) Draw sample for both ACTH and cortisol measurement today",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — stress dosing",
                "A screen-positive boy had peak stimulated cortisol 17.1 μg/dL at 6 weeks. At what age should stress-dose hydrocortisone have started?",
                [
                    "6 weeks",
                    "4 months",
                    "7 months",
                    "13 months",
                ],
                0,
                "Per algorithm, stress doses begin at 6 weeks when stimulated peak cortisol is below threshold.",
                ref(
                    "Case 2",
                    "Answer: A) 6 weeks",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — daily hydrocortisone",
                "Same patient: ACTH rose to 314 pg/mL at 13 months with cortisol 12.1 μg/dL while on stress doses. When should daily hydrocortisone have started?",
                [
                    "6 weeks",
                    "4 months",
                    "7 months",
                    "13 months",
                ],
                3,
                "ACTH ≥300 pg/mL triggers daily replacement per PES algorithm, though clinical context may modify timing.",
                ref(
                    "Case 2",
                    "Answer: D) 13 months",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 3 — family evaluation",
                "A 2-week-old girl has positive ALD screen; brother has poor weight gain and tanned skin. Which family member needs urgent pediatric endocrinology evaluation before confirmatory testing returns?",
                [
                    "Mother",
                    "Father",
                    "Brother",
                    "All three equally",
                ],
                2,
                "Symptomatic brother may have life-threatening unrecognized adrenal insufficiency and needs urgent evaluation.",
                ref(
                    "Case 3",
                    "Answer: C) Patient's brother",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 4 — school behavior",
                "A 4-year-old screen-positive boy has new inattention and irritability; ACTH 34 pg/mL and cortisol 10.2 μg/dL were normal 3 months ago. Best next step?",
                [
                    "Reassure; routine screening in 2 months",
                    "Repeat 8-AM ACTH and cortisol now and reassess clinically",
                    "Emergency department brain MRI immediately",
                    "Refer to psychologist only",
                ],
                1,
                "Subtle behavioral change warrants prompt biochemical reassessment for evolving adrenal insufficiency.",
                ref(
                    "Case 4",
                    "Answer B) Make arrangements now for a repeated 8-AM measurement of ACTH and cortisol and reassess for clinical adrenal insufficiency",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Hydrocortisone dosing",
                "Preferred starting daily hydrocortisone dose for adrenal insufficiency in a boy with ALD is:",
                [
                    "2–4 mg/m² once daily",
                    "8–12 mg/m² divided into 3 doses",
                    "20–25 mg flat dose regardless of size",
                    "Fludrocortisone 100 mcg without glucocorticoid",
                ],
                1,
                "ALD adrenal replacement follows primary AI principles with weight-based hydrocortisone.",
                ref(
                    "Management of Adrenal Insufficiency",
                    "the starting dosage is 8 to 12 mg/m² daily divided into 3 doses.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Newborn screening rationale",
                "Which feature makes ALD well suited for newborn screening?",
                [
                    "Presymptomatic phase with available life-saving interventions",
                    "All females are detected by VLCFA testing",
                    "Genotype reliably predicts cerebral ALD onset",
                    "Mineralocorticoid deficiency is universal at birth",
                ],
                0,
                "Presymptomatic detection with treatable adrenal and neurologic disease underpins screening.",
                ref(
                    "Newborn Screening",
                    "ALD is considered an ideal condition for screening, as there is a presymptomatic phase and life-saving interventions are available to treat both the primary adrenal insufficiency and cerebral ALD.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "VLCFA in women",
                "Regarding VLCFA testing in ALD, which statement is correct?",
                [
                    "All heterozygous females have elevated VLCFA",
                    "20% of heterozygous females lack VLCFA elevation",
                    "VLCFA elevation predicts neurologic onset age",
                    "VLCFA are normal in all hemizygous males",
                ],
                1,
                "Most but not all carrier females have elevated VLCFA; all hemizygous males do.",
                ref(
                    "Newborn Screening",
                    "As 20% of females heterozygous for ABCD1 pathogenic variants do not have VLCFA elevations, they are not expected to be identified by newborn screening.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Cerebral ALD treatment",
                "Early cerebral ALD detected on surveillance MRI may be treated with:",
                [
                    "Hematopoietic stem-cell therapy",
                    "High-dose dexamethasone alone",
                    "Testosterone replacement",
                    "Observation without intervention until symptoms",
                ],
                0,
                "Hematopoietic stem-cell therapy can halt early cerebral ALD; gene therapy remains investigational.",
                ref(
                    "Neurologic Disease: Cerebral ALD and Adrenomyeloneuropathy",
                    "Cerebral ALD, when detected in its earliest stages, can be treated with hematopoietic stem-cell therapy.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Infant ACTH interpretation",
                "In a screen-positive infant, ACTH may rise before cortisol becomes frankly low. Therefore:",
                [
                    "Cortisol alone is sufficient for surveillance",
                    "Measuring cortisol without ACTH may miss evolving primary adrenal insufficiency",
                    "Cosyntropin testing is never useful in infancy",
                    "8-AM sampling is mandatory under 6 months",
                ],
                1,
                "Paired testing captures early adrenal axis dysfunction.",
                ref(
                    "Case 1",
                    "You may miss evolving primary adrenal insufficiency by measuring cortisol without ACTH (Answer B), as ACTH will rise before the cortisol is frankly low.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "AMN presentation",
                "Adrenomyeloneuropathy (AMN) most commonly presents in which age range?",
                [
                    "First decade",
                    "Second decade",
                    "Third to fourth decade",
                    "Neonatal period",
                ],
                2,
                "AMN is the most common adult phenotype with spastic paraparesis and high adrenal insufficiency prevalence.",
                ref(
                    "Table. Clinical Presentations of Adrenoleukodystrophy",
                    "Adrenomyeloneuropathy (AMN) ~40%-46% of affected males)",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Screening expansion",
                "As of late 2019, approximately how many U.S. states screened newborns for ALD?",
                [
                    "1 state only",
                    "13 states and the District of Columbia",
                    "All 50 states",
                    "No states; only research protocols",
                ],
                1,
                "New York was first (2013); expansion continued through 2019.",
                ref(
                    "Significance of the Clinical Problem",
                    "As of October 2019, newborn screening for ALD has been expanded to 13 states and the District of Columbia",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Cosyntropin in infancy",
                "When travel to clinic is a major burden for an ALD screen-positive family, what test may be discussed?",
                [
                    "Overnight dexamethasone suppression test",
                    "High-dose cosyntropin-stimulation test",
                    "Water-deprivation test",
                    "Oral glucose tolerance test",
                ],
                1,
                "Cosyntropin stimulation can be discussed when baseline labs are ambiguous and access is limited.",
                ref(
                    "Case 1",
                    "If travel to the clinic is a significant burden for a family, a cosyntropin-stimulation test (Answer E) can be discussed.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Infant diurnal rhythm",
                "Infants with ALD have established predictable diurnal variation in ACTH and cortisol secretion.",
                False,
                "Listed as a barrier to optimal practice.",
                ref(
                    "Barriers to Optimal Practice",
                    "Infants do not have established predictable diurnal variation in ACTH and cortisol secretion.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Genotype prediction",
                "The ABCD1 genotype reliably predicts age of adrenal insufficiency onset.",
                False,
                "No genotype-phenotype correlation exists.",
                ref(
                    "Pathophysiology and Epidemiology",
                    "There is no genotype-phenotype correlation",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Adrenal prevalence",
                "Approximately 80% of males with ALD develop adrenal insufficiency over their lifetime.",
                True,
                "Supported by large clinic series.",
                ref(
                    "Pathophysiology and Epidemiology",
                    "there was an estimated 80% lifetime prevalence of adrenal insufficiency",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Female adrenal insufficiency",
                "Routine adrenal testing without symptoms is recommended for all female heterozygotes.",
                False,
                "Adrenal insufficiency is rare in female heterozygotes; symptomatic brother needed urgent evaluation in Case 3.",
                ref(
                    "Case 3",
                    "As adrenal insufficiency is reported to be rare in female heterozygotes, routine testing, without symptoms of adrenal insufficiency, is not recommended.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Mineralocorticoid deficiency",
                "Mineralocorticoid deficiency is common at ALD diagnosis in young males.",
                False,
                "None of 18 tested patients in one prospective series had mineralocorticoid deficiency.",
                ref(
                    "Pathophysiology and Epidemiology",
                    "None of the 18 patients tested had mineralocorticoid deficiency.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Stress dosing",
                "The PES ALD algorithm recommends stress-dose hydrocortisone when stimulated cortisol is below threshold even before daily replacement.",
                True,
                "Case 2 illustrates stress dosing at 6 weeks.",
                ref(
                    "Case 2",
                    "stress doses of hydrocortisone should have been started at 6 weeks of age",
                ),
            ),
            tf(
                f"{p}-tf7",
                "RUSP inclusion",
                "ALD was added to the Recommended Uniform Screening Panel in 2016.",
                True,
                "Stated in significance section.",
                ref(
                    "Significance of the Clinical Problem",
                    "ALD was added to the Recommended Uniform Screening Panel in 2016.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Other peroxisomal disorders",
                "Elevated VLCFA on newborn screening may reflect disorders other than ALD.",
                True,
                "Zellweger syndrome and other peroxisomal disorders can elevate VLCFA.",
                ref(
                    "Newborn Screening",
                    "VLCFA are also elevated in other, rarer peroxisomal disorders, including but not limited to Zellweger syndrome",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Early adrenal insufficiency",
                "Assertion: Adrenal insufficiency may develop in some ALD boys during early infancy after a positive newborn screen.",
                "Reason: Newborn screening prevents all adrenal crises in ALD.",
                2,
                "Assertion true per main conclusions; screening reduces but does not eliminate risk—reason overstates benefit.",
                ref(
                    "Main Conclusions",
                    "adrenal insufficiency may develop in some affected boys during early infancy.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "ACTH before cortisol",
                "Assertion: Measuring cortisol without ACTH may miss evolving adrenal insufficiency in ALD infants.",
                "Reason: ACTH always falls before cortisol rises in primary adrenal insufficiency.",
                2,
                "Assertion true; ACTH rises before cortisol falls—the reason reverses physiology.",
                ref(
                    "Case 1",
                    "ACTH will rise before the cortisol is frankly low.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Hydrocortisone choice",
                "Assertion: Hydrocortisone is the preferred glucocorticoid for ALD-associated adrenal insufficiency.",
                "Reason: Treatment is the same as for most other causes of primary adrenal insufficiency.",
                0,
                "Both true and aligned.",
                ref(
                    "Management of Adrenal Insufficiency",
                    "Treatment of adrenal insufficiency associated with ALD is the same as treatment for most other causes of primary adrenal insufficiency.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "VLCFA cytotoxicity",
                "Assertion: VLCFA accumulation damages adrenocortical cells in ALD.",
                "Reason: VLCFA only affect the nervous system, not the adrenal cortex.",
                2,
                "Assertion true; VLCFA affect adrenal cortex, brain, and testes—reason false.",
                ref(
                    "Pathophysiology and Epidemiology",
                    "In males, the excess VLCFA accumulate in the adrenal cortex, nervous system, and testicular Leydig cells.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Cerebral ALD MRI",
                "Assertion: Brain MRI surveillance intensifies after age 3 because cerebral ALD risk increases.",
                "Reason: Cerebral ALD never occurs after the first decade.",
                2,
                "Assertion reflects surveillance protocol; childhood cerebral ALD peaks in first decade—reason false.",
                ref(
                    "Neurologic Disease: Cerebral ALD and Adrenomyeloneuropathy",
                    "performed annually until age 3 years, when the risk for cerebral ALD increases.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Brother evaluation",
                "Assertion: A symptomatic older brother of a screen-positive infant should be evaluated urgently for adrenal insufficiency.",
                "Reason: Adrenal insufficiency is never life-threatening in children.",
                2,
                "Assertion true; unrecognized AI carries mortality risk—reason false.",
                ref(
                    "Case 3",
                    "The patient's brother should be evaluated by a pediatric endocrinologist (Answer C) as soon as possible for primary adrenal insufficiency, as he is described to be symptomatic and adrenal insufficiency is a potentially life-threatening condition.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Algorithm limits",
                "Assertion: The PES adrenal surveillance algorithm is a guide and does not replace clinical judgment.",
                "Reason: ACTH and cortisol never fluctuate in ALD.",
                2,
                "Assertion true per Case 2 discussion; levels fluctuate—reason false.",
                ref(
                    "Case 2",
                    "the algorithm is intended to be a guide and is not meant to replace good clinical judgment.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Newborn screening females",
                "Assertion: Most females with pathogenic ABCD1 variants are not detected by VLCFA newborn screening.",
                "Reason: 20% of heterozygous females lack VLCFA elevation.",
                0,
                "Both true; explains female false negatives.",
                ref(
                    "Newborn Screening",
                    "As 20% of females heterozygous for ABCD1 pathogenic variants do not have VLCFA elevations, they are not expected to be identified by newborn screening.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "29",
        "title": "Screening of the Newborn for Adrenoleukodystrophy",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Molly O. Regelmann, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_29_Screening_of_the_Newborn_for_Adrenoleukodystrophy.md",
        "items": items,
    }


def build_chapter_30() -> dict:
    p = "e21-30"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Epidemiology",
                "Why youth-onset T2DM demands distinct management",
                "Incidence has risen dramatically though prevalence remains <50,000 in the U.S.; youth-onset disease shows faster β-cell failure, earlier complications, and disproportionate impact on minorities with complex psychosocial barriers to lifestyle change.",
                ref(
                    "Significance of the Clinical Problem",
                    "β-cell failure appears to be more rapid in youth than in adults, leading to loss of glycemic control on oral therapy that is more rapid.",
                ),
            ),
            note(
                f"{p}-n2",
                "Puberty link",
                "How puberty contributes to youth T2DM onset",
                "Median diagnosis ~14 years aligns with pubertal insulin resistance; transient pubertal insulin resistance may allow reversibility in some youth, but limited β-cell reserve leads to hyperglycemia.",
                ref(
                    "Significance of the Clinical Problem",
                    "there is an important association of T2DM with pubertal development—the median age of onset of T2DM in youth is approximately 14 years.",
                ),
            ),
            note(
                f"{p}-n3",
                "Diagnosis",
                "How to diagnose diabetes mellitus in youth",
                "Confirm diabetes by ADA/ISPAD criteria; asymptomatic hyperglycemia during stress requires repeat testing on a different day. HbA1c must be DCCT-aligned lab assay—not point-of-care—and is less validated in youth.",
                ref(
                    "Diagnosis",
                    "in the absence of symptoms, hyperglycemia detected incidentally or under conditions of acute physiologic stress may be transitory and should not be regarded as diagnostic of diabetes. Accordingly, a second test on a different day is required.",
                ),
            ),
            note(
                f"{p}-n4",
                "Autoantibody testing",
                "Why pancreatic autoantibodies are mandatory in presumed T2DM",
                "10–15% of obese adolescents have T1DM; autoantibody positivity predicts rapid insulin requirement and other autoimmune disorders—test all youth with clinical T2DM and consider in obese pubertal T1DM phenotypes who may wean from insulin.",
                ref(
                    "Diagnosis",
                    "diabetes autoantibody testing (glutamic acid decarboxylase antibodies [GAD], microinsulin autoantibodies [mIAA], zinc transporter 8 antibodies [ZnT8], tyrosine phosphatase-based islet antigen 2 antibody [IA2]) should be done in all youth with the clinical diagnosis of T2DM",
                ),
            ),
            note(
                f"{p}-n5",
                "Initial therapy",
                "How to start treatment when diabetes type is uncertain",
                "Acidosis requires IV insulin; once resolved, T2DM-leaning patients get basal insulin 0.2–0.4 units/kg daily plus metformin titrated to 2000 mg, with insulin stopped after antibody negativity. HbA1c >9–10% may need basal insulin even if asymptomatic.",
                ref(
                    "Management",
                    "When the clinical impression is T2DM, basal insulin at a dosage of 0.2 to 0.4 units/kg once daily is started and titrated based on fingerstick glucose measurements. At the same time, metformin is initiated at 500 mg once daily and titrated weekly to a maximally tolerated dosage, with a target of 2000 mg daily.",
                ),
            ),
            note(
                f"{p}-n6",
                "Glycemic target",
                "Glycemic target and monitoring frequency in youth T2DM",
                "Target HbA1c below 6.5% (<48 mmol/mol); non-insulin patients check fingersticks twice daily a few days per week—enough safety without excessive burden on poorly adherent adolescents.",
                ref(
                    "Management",
                    "The target of therapy is to attain and maintain hemoglobin A1c below 6.5% (<48 mmol/mol).",
                ),
            ),
            note(
                f"{p}-n7",
                "TODAY study",
                "Why suboptimal early metformin response predicts failure",
                "TODAY showed HbA1c >6.3% after short metformin monotherapy carries 4- to 10-fold increased loss-of-control risk with median ~11 months to failure—discuss intensification early.",
                ref(
                    "Case 2",
                    "a hemoglobin A1c level greater than 6.3% (>45 mmol/mol) after a few months of metformin monotherapy is associated with a 4- to 10-fold increased risk for loss of glycemic control",
                ),
            ),
            note(
                f"{p}-n8",
                "FDA-approved agents",
                "Approved pharmacotherapy for youth T2DM as of 2019",
                "Only metformin and insulin were FDA-approved through mid-2019; liraglutide was subsequently approved for youth based on the ELLIPSE trial—RISE data show youth may respond differently than adults.",
                ref(
                    "Management",
                    "the only FDA-approved medications as of June 2019 for youth with T2DM were metformin and insulin, although liraglutide, a GLP-1 receptor agonist, has recently been approved for youth based on data from the ELLIPSE trial.",
                ),
            ),
            note(
                f"{p}-n9",
                "Comorbidity screening",
                "How to screen complications at T2DM diagnosis",
                "Evaluate lipids, blood pressure (sex/height/age norms), urine albumin, liver enzymes, PCOS, depression, eating disorders, and sleep disturbance once metabolically stable.",
                ref(
                    "Case 3",
                    "evaluation should occur either at the time of initial diagnosis or upon reestablishment of metabolic stability.",
                ),
            ),
            note(
                f"{p}-n10",
                "Triglycerides and pancreatitis",
                "When to treat hypertriglyceridemia in youth T2DM",
                "Fasting triglycerides >500 mg/dL warrant fibrate therapy to prevent pancreatitis—not for CVD prevention alone. LDL goals <100 mg/dL; statins after 6 months of lifestyle if LDL >130 mg/dL.",
                ref(
                    "Case 3",
                    "if fasting triglycerides are greater than 500 mg/dL (>5.65 mmol/L), a fabric acid is started (Answer B) due to significantly increased risk for acute pancreatitis",
                ),
            ),
            note(
                f"{p}-n11",
                "Diabetic kidney disease",
                "Why youth T2DM kidney screening differs from T1DM",
                "Albuminuria is often present at T2DM diagnosis and progresses faster than T1DM (4-fold higher CKD risk); screen T2DM at diagnosis and annually vs T1DM after 2–5 years.",
                ref(
                    "Case 4",
                    "Youth-onset T2DM is also associated with a 4-fold higher risk of progression to chronic kidney disease compared with that in T1DM (hazard ratio, 4.03; 95% CI, 1.64-9.95).",
                ),
            ),
            note(
                f"{p}-n12",
                "Nephroprotection",
                "How to intensify nephroprotection in youth with macroalbuminuria",
                "SGLT-2 inhibitors have RCT evidence for preventing macroalbuminuria and ESKD progression (CREDENCE); an 18-year-old may use adult agents despite lack of pediatric approval.",
                ref(
                    "Case 5",
                    "SGLT-2 inhibitors (Answer E) have demonstrated beneficial effects in preventing the development of macroalbuminuria and progression to end-stage kidney disease.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — re-evaluation after 3 years",
                "A 16-year-old obese Latina girl had 'T2DM' diagnosed 3 years ago, took metformin briefly, then none. After suicide attempt admission: glucose 550 mg/dL, HbA1c 12.5%, small ketonuria, normal pH. Most important next investigation?",
                [
                    "Fasting lipid panel",
                    "Fasting and stimulated C-peptide",
                    "Home glucose monitoring",
                    "Pancreatic autoantibody measurements",
                ],
                3,
                "No clinical feature excludes T1DM with 100% sensitivity; rigorous type determination with autoantibodies is paramount even after years off therapy.",
                ref(
                    "Case 1",
                    "Answer: E) Pancreatic autoantibody measurements",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — metformin response",
                "A 15-year-old Latino boy with antibody-negative T2DM reaches HbA1c 7.1% on metformin 2000 mg after 3 months. Best next step?",
                [
                    "Fasting C-peptide",
                    "Stimulated C-peptide",
                    "Start liraglutide 1.8 mg daily",
                    "Start basal insulin once daily",
                ],
                3,
                "HbA1c remains above nondiabetes range; TODAY data support discussing early basal insulin as standard add-on when metformin response is insufficient.",
                ref(
                    "Case 2",
                    "Answer: D) Start basal insulin once daily",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3 — comorbidity priority",
                "Newly diagnosed obese adolescent with T2DM (HbA1c 7.8%): LDL 160, triglycerides 745, BP 145/82, urine ACR 48, ALT 87. Most important immediate prescription?",
                [
                    "Atorvastatin 10 mg for LDL 160",
                    "Fenofibrate 67 mg for triglycerides 745",
                    "Lisinopril 10 mg for BP 145/82",
                    "Lisinopril 20 mg for ACR 48",
                ],
                1,
                "Triglycerides >500 mg/dL warrant fibrate to prevent pancreatitis; BP and microalbuminuria need confirmatory steps before ACE inhibitor.",
                ref(
                    "Case 3",
                    "Answer: B) Fenofibrate, 67 mg daily, for a triglyceride level of 745 mg/dL (8.42 mmol/L)",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 4 — DKD comparison",
                "Compared with youth-onset T1DM, youth-onset T2DM diabetic kidney disease:",
                [
                    "Is more prevalent at onset and progresses more slowly",
                    "Is more prevalent at onset and progresses more rapidly",
                    "Has similar CKD risk after 10 years",
                    "Is rare at diagnosis in both types",
                ],
                1,
                "SEARCH data show higher prevalent albuminuria and ~4-fold faster CKD progression in T2DM youth.",
                ref(
                    "Case 4",
                    "Answer: B) Diabetic kidney disease is more prevalent at onset in T2DM and progresses more rapidly",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 5 — macroalbuminuria",
                "An 18-year-old man with T2DM, ACR 312–418 mg/g on lisinopril 20 mg, HbA1c 7.6%, BP 125/78. Best next nephroprotective step?",
                [
                    "Add angiotensin-receptor blocker",
                    "Add GLP-1 receptor agonist",
                    "Add long-acting insulin",
                    "Add SGLT-2 inhibitor",
                ],
                3,
                "SGLT-2 inhibitors have RCT evidence for reducing ESKD progression; patient is adult-aged though pediatric approval lacking.",
                ref(
                    "Case 5",
                    "Answer: E) SGLT-2 inhibitor",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Sex prevalence",
                "In U.S. adolescents, type 2 diabetes prevalence is:",
                [
                    "Equal in boys and girls",
                    "~60% higher in girls than boys",
                    "Higher only in prepubertal children",
                    "Confined to non-obese youth",
                ],
                1,
                "Adolescent girls have 60% higher prevalence than boys.",
                ref(
                    "Significance of the Clinical Problem",
                    "adolescent girls have a 60% higher prevalence rate than that of adolescent boys.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Ketoacidosis in T2DM",
                "Obese adolescents with clinical T2DM:",
                [
                    "Never present with ketoacidosis",
                    "May present with clinically significant ketoacidosis",
                    "Always have positive autoantibodies if ketotic",
                    "Should never receive insulin initially",
                ],
                1,
                "Substantial fraction present with ketoacidosis; initial therapy follows clinical presentation.",
                ref(
                    "Management",
                    "a substantial percentage of adolescents with T2DM present with clinically significant ketoacidosis.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Liraglutide dosing",
                "When starting liraglutide in an adolescent with T2DM, appropriate dosing is:",
                [
                    "1.8 mg daily immediately",
                    "0.6 mg daily for 1 week, then uptitrate",
                    "Once-weekly 2 mg without titration",
                    "Only with concurrent basal-bolus insulin",
                ],
                1,
                "Starting at maximum 1.8 mg increases GI adverse effects; titrate from 0.6 mg.",
                ref(
                    "Case 2",
                    "the starting dosage of liraglutide is 0.6 mg daily for 1 week, increasing to 1.2 mg injections thereafter.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Microalbuminuria confirmation",
                "Persistent microalbuminuria in an adolescent requires:",
                [
                    "Single elevated spot urine ACR",
                    "Two of three consecutive abnormal values on different days",
                    "Exercise immediately before collection",
                    "Renal biopsy before any ACE inhibitor",
                ],
                1,
                "Orthostatic and other benign causes require confirmatory testing.",
                ref(
                    "Case 3",
                    "the diagnosis of persistent abnormal microalbuminuria requires documentation of 2 of 3 consecutive abnormal values obtained on different days",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Blood pressure treatment",
                "Initial treatment of elevated blood pressure in youth T2DM consists of:",
                [
                    "Immediate ACE inhibitor monotherapy",
                    "Weight loss, dietary salt restriction, and increased physical activity",
                    "Calcium-channel blocker before lifestyle",
                    "Combination ACE inhibitor and ARB",
                ],
                1,
                "Lifestyle first for BP above 95th percentile; ACE inhibitor after 6 months if still elevated.",
                ref(
                    "Case 3",
                    "Initial treatment of blood pressure above the 95th percentile consists of weight loss, limitation of dietary salt, and increased physical activity.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Fatty liver",
                "Regarding hepatic steatosis in youth T2DM, which is correct?",
                [
                    "Vitamin E is first-line for adolescents",
                    "25–50% have steatosis; monitor enzymes and refer if persistently elevated",
                    "Fatty liver is rare in obese youth",
                    "Statin therapy worsens steatosis mandating discontinuation",
                ],
                1,
                "Vitamin E is not recommended in adolescents; ongoing ALT monitoring with biopsy referral when markedly elevated.",
                ref(
                    "Case 3",
                    "Hepatic steatosis is present in 25% to 50% of adolescents with T2DM",
                ),
            ),
            mcq(
                f"{p}-q12",
                "C-peptide during decompensation",
                "Fasting C-peptide measurement during acute metabolic decompensation:",
                [
                    "Definitively distinguishes T1DM from T2DM",
                    "May be transiently low and misleading",
                    "Is superior to autoantibody testing",
                    "Should replace HbA1c for diagnosis",
                ],
                1,
                "Insulin and C-peptide secretion fall transiently during decompensation.",
                ref(
                    "Case 1",
                    "During acute decompensation, insulin and C-peptide secretion are transiently decreased.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "MODY consideration",
                "Monogenic diabetes (MODY) should be considered when:",
                [
                    "Every obese adolescent has ketosis",
                    "Presentation and course are not characteristic of T1DM or T2DM",
                    "Autoantibodies are positive",
                    "HbA1c is below 5.7%",
                ],
                1,
                "Atypical course prompts MODY evaluation.",
                ref(
                    "Diagnosis",
                    "single-gene forms of diabetes, such as maturity-onset diabetes of the young should be considered in individuals who have a presentation and course that is not characteristic of either T1DM or T2DM.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Autoantibodies",
                "Pancreatic autoantibody testing should be performed in all youth with a clinical diagnosis of T2DM.",
                True,
                "Explicit recommendation due to overlap with T1DM.",
                ref(
                    "Diagnosis",
                    "should be done in all youth with the clinical diagnosis of T2DM",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Prepubertal T2DM",
                "Youth with T2DM are almost always pubertal at diagnosis.",
                True,
                "T2DM youth are rarely prepubertal; mean age 13–14 years.",
                ref(
                    "Diagnosis",
                    "youth with T2DM are almost always in puberty, with a mean age of diagnosis of 13 to 14 years and Tanner stage 4 to 5 and are rarely prepubertal.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "HbA1c diagnosis",
                "Point-of-care HbA1c is adequate for diagnosing diabetes in youth.",
                False,
                "ADA HbA1c criterion assumes DCCT-aligned laboratory assay, not POC.",
                ref(
                    "Diagnosis",
                    "this assumes measurement in a laboratory with a DCCT-aligned assay, not point-of-care testing, and it has not been specifically validated in youth.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "TODAY failure risk",
                "HbA1c >6.3% after short metformin monotherapy predicts higher loss-of-control risk in TODAY.",
                True,
                "4- to 10-fold increased risk cited in Case 2.",
                ref(
                    "Case 2",
                    "a hemoglobin A1c level greater than 6.3% (>45 mmol/mol) after a few months of metformin monotherapy is associated with a 4- to 10-fold increased risk for loss of glycemic control",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Lisinopril for BP",
                "Lisinopril should be started immediately for blood pressure at the 95th percentile without lifestyle trial.",
                False,
                "Initial BP management is lifestyle; ACE inhibitor after 6 months if still elevated.",
                ref(
                    "Case 3",
                    "Thus, prescribing lisinopril now (Answer C) is incorrect.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Statin threshold",
                "Statin therapy is started when LDL remains >130 mg/dL after 6 months of lifestyle in youth T2DM.",
                True,
                "Described lipid management pathway.",
                ref(
                    "Case 3",
                    "If LDL cholesterol remains greater than 130 mg/dL (>1.04 mmol/L) after 6 months, statin therapy should be started",
                ),
            ),
            tf(
                f"{p}-tf7",
                "DKD screening T2DM",
                "Youth with T2DM should be screened for diabetic kidney disease at diagnosis and annually.",
                True,
                "Contrasts with T1DM delayed screening.",
                ref(
                    "Case 4",
                    "young persons with T2DM should be screened at diagnosis and annually thereafter.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Lifestyle challenges",
                "Lifestyle modification is often harder to sustain in adolescents with T2DM than in adults.",
                True,
                "Family norms and adherence barriers cited.",
                ref(
                    "Management",
                    "the challenges in implementing lifestyle modifications in adolescents are greater than in adult patients",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Autoantibody mandate",
                "Assertion: Autoantibody testing is essential even in obese adolescents with typical T2DM phenotype.",
                "Reason: Obesity protects against islet autoimmunity.",
                2,
                "Assertion true; obesity does not protect—reason false.",
                ref(
                    "Case 1",
                    "obesity does not protect from autoimmunity.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Metformin plus insulin",
                "Assertion: Basal insulin plus metformin is a standard intensification strategy when metformin alone fails in youth T2DM.",
                "Reason: Multiple daily injections should always be first add-on in adolescents.",
                2,
                "Assertion true; simplest effective regimen preferred—reason false.",
                ref(
                    "Case 2",
                    "Initiation of basal insulin (Answer D) is the standard approach to add-on therapy",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Triglyceride treatment",
                "Assertion: Fibrate therapy is indicated for fasting triglycerides >500 mg/dL in youth T2DM.",
                "Reason: Elevated triglycerides are treated solely for cardiovascular prevention at this level.",
                2,
                "Assertion true for pancreatitis prevention—reason false about sole indication.",
                ref(
                    "Case 3",
                    "if fasting triglycerides are greater than 500 mg/dL (>5.65 mmol/L), a fabric acid is started (Answer B) due to significantly increased risk for acute pancreatitis",
                ),
            ),
            ar(
                f"{p}-ar4",
                "DKD prevalence",
                "Assertion: Diabetic kidney disease is more prevalent at diagnosis in youth T2DM than T1DM.",
                "Reason: Albuminuria never appears until 10 years of diabetes in T2DM youth.",
                2,
                "Assertion true; often present at T2DM diagnosis—reason false.",
                ref(
                    "Case 4",
                    "Diabetic kidney disease (ie, elevated albumin excretion (≥30 mg/g) is often present at diagnosis in patients with youth-onset T2DM",
                ),
            ),
            ar(
                f"{p}-ar5",
                "SGLT2 inhibitors",
                "Assertion: SGLT-2 inhibitors reduce progression to end-stage kidney disease in diabetic nephropathy.",
                "Reason: CREDENCE showed 32% lower ESKD risk with canagliflozin vs placebo.",
                0,
                "Both true with trial evidence cited in Case 5.",
                ref(
                    "Case 5",
                    "the risk of progression to end-stage kidney disease was 32% lower in those treated with canagliflozin vs placebo.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Puberty and insulin resistance",
                "Assertion: Pubertal development is associated with increased T2DM risk in youth.",
                "Reason: Puberty causes transient reduction in insulin sensitivity requiring compensatory insulin secretion.",
                0,
                "Both true and mechanistically linked.",
                ref(
                    "Significance of the Clinical Problem",
                    "This observation is most likely related to the transient reduction in insulin sensitivity that occurs in children as they enter puberty",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Vitamin E",
                "Assertion: Vitamin E may improve fatty liver in adolescents with T2DM.",
                "Reason: Vitamin E is currently recommended to treat hepatic steatosis in adolescents.",
                2,
                "Some evidence for improvement but not recommended in adolescents—reason false.",
                ref(
                    "Case 3",
                    "Vitamin E is currently not recommended to treat hepatic steatosis in adolescents.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Complications at diagnosis",
                "Assertion: Microvascular complications and macrovascular risk markers may be present at T2DM diagnosis in youth.",
                "Reason: Youth T2DM never has complications at diagnosis.",
                2,
                "Assertion true per significance section; reason false.",
                ref(
                    "Significance of the Clinical Problem",
                    "there is evidence of microvascular complications and risk markers for macrovascular complications at the time of diagnosis",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "30",
        "title": "Youth-Onset Type 2 Diabetes Mellitus",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Philip Zeitler, MD, PhD; Petter Bjornstad, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_30_YouthOnset_Type_2_Diabetes_Mellitus.md",
        "items": items,
    }


def build_chapter_31() -> dict:
    p = "e21-31"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Atherosclerosis origins",
                "Why dyslipidemia screening in childhood matters",
                "CVD is the leading U.S. cause of death; atherosclerosis begins in youth. Universal screening and early treatment—especially for familial hypercholesterolemia—can reduce future events.",
                ref(
                    "Main Conclusions",
                    "Universal screening and early treatment have the potential to significantly reduce future CVD-related events in youth with familial hypercholesterolemia.",
                ),
            ),
            note(
                f"{p}-n2",
                "Universal screening age",
                "How U.S. guidelines define who to screen for dyslipidemia",
                "Selective screening from age ≥2 with family risk; universal lipid screening for all children ages 9–11, repeated between 17–21 if initial result normal.",
                ref(
                    "Who to screen",
                    "Universal screening of all children 9 to 11 years of age regardless of general health or the presence/absence of CVD risk factors.",
                ),
            ),
            note(
                f"{p}-n3",
                "Screening method",
                "Preferred cholesterol screening method in pediatrics",
                "Fasting or nonfasting lipid panels are acceptable; nonfasting is often more practical. Direct LDL assay needed when triglycerides >400 mg/dL preclude Friedewald calculation.",
                ref(
                    "Question 2: What is the preferred method of cholesterol screening?",
                    "Screening can be performed using a fasting or nonfasting lipid profile. A nonfasting blood sample is often more practical and efficient.",
                ),
            ),
            note(
                f"{p}-n4",
                "FH diagnosis",
                "Familial hypercholesterolemia clinical pattern",
                "In absence of secondary causes, marked LDL elevation (~1:200–1:500 prevalence) with premature family CVD; youth are often asymptomatic yet highest CVD risk.",
                ref(
                    "Question 2: Based on this patient's findings, which of the following is the most likely cause of her lipid abnormality?",
                    "In the absence of secondary causes of hypercholesterolemia, the most likely diagnosis is familial hypercholesterolemia (~1:200-1:500).",
                ),
            ),
            note(
                f"{p}-n5",
                "Statin indications",
                "Why LDL thresholds trigger statin therapy in pediatric FH",
                "FDA-approved for age ≥10 when LDL >190 mg/dL or >160 mg/dL with ≥1 additional risk factor; goal LDL ≤100 mg/dL or ≥50% reduction from baseline.",
                ref(
                    "Main Conclusions",
                    "All statins have been approved by the US FDA for use in children with familial hypercholesterolemia and should be recommended to patients aged 10 years and older when the LDL-cholesterol concentration is greater than 190 mg/dL (>4.92 mmol/L) or greater than 160 mg/dL (>4.14 mmol/L) in patients with 1 or more additional risk factors.",
                ),
            ),
            note(
                f"{p}-n6",
                "Statin safety",
                "How long-term pravastatin data support childhood FH treatment",
                "Clinical trials show statins are safe and improve carotid intima-media thickness; 20-year pravastatin follow-up showed remarkable absence of MACE vs affected parent.",
                ref(
                    "Question 3: Is there evidence that lipid-lowering medications, such as statins, are safe when prescribed at a young age? If so, are they effective?",
                    "demonstrated a remarkable absence of major adverse cardiovascular events at age 40 years and older in contrast to the affected parent.",
                ),
            ),
            note(
                f"{p}-n7",
                "Genetic testing",
                "How to approach genetic testing in suspected FH",
                "Test LDLR, APOB, PCSK9 with appropriate sequencing/deletion analysis; cascade testing of relatives when pathogenic variant found. Negative testing does not exclude FH or need for therapy.",
                ref(
                    "Question 4: Is there a role for genetic testing?",
                    "Genetic testing is recommended for all individuals clinically suspected to have familial hypercholesterolemia.",
                ),
            ),
            note(
                f"{p}-n8",
                "Cascade screening",
                "Why cascade screening of relatives is recommended",
                "Systematic first-degree relative cholesterol or genotype testing enhances detection; adults in the family often have greater short-term risk than affected children.",
                ref(
                    "Question 5: Now that you have initiated treatment, is there a role for cascade screening?",
                    "Screening the family of a patient with familial hypercholesterolemia by systematically identifying first-degree relatives (ie, cascade screening), is recommended",
                ),
            ),
            note(
                f"{p}-n9",
                "Pregnancy and statins",
                "How pregnancy affects statin therapy in FH",
                "Statins, ezetimibe, and niacin are category X—stop at least 4 weeks before conception; discontinue immediately if unintended pregnancy; withhold lipid drugs during breastfeeding.",
                ref(
                    "Case 1 (Continued)",
                    "These treatments SHOULD NOT BE USED during pregnancy. In the case of an unintended pregnancy, a woman with familial hypercholesterolemia should discontinue statins, ezetimibe, and niacin immediately.",
                ),
            ),
            note(
                f"{p}-n10",
                "Lipoprotein(a)",
                "Role of lipoprotein(a) in selected pediatric cases",
                "Adult Lp(a) levels are set by age 2–5 years; >50 mg/dL (>100 nmol/L) affects ~1 in 5 individuals and is an independent causative CVD risk factor counted within LDL fraction.",
                ref(
                    "Advanced Lipid Testing",
                    "Elevated lipoprotein (a), defined as greater than 50 mg/dL (>100 nmol/L), is the most common genetic dyslipidemia, affecting nearly 1 in 5 individuals in the United States.",
                ),
            ),
            note(
                f"{p}-n11",
                "Hypertriglyceridemia goals",
                "Treatment goals differ by triglyceride severity",
                "TG <150 mg/dL for health maintenance/CVD prevention; TG ≥500–999 mg/dL focus on pancreatitis prevention with fibrates/omega-3; extreme elevations need strict fat restriction.",
                ref(
                    "Table 4. Treatment of Hypertriglyceridemia",
                    "Goal ... CVD Risk Prevention ... Avoid Pancreatitis",
                ),
            ),
            note(
                f"{p}-n12",
                "Secondary causes",
                "Secondary causes to exclude before diagnosing FH",
                "Screen hypothyroidism, liver/kidney disease, diabetes/obesity, and medications (steroids, isotretinoin, OCPs) when evaluating pediatric dyslipidemia.",
                ref(
                    "Table 3. Secondary Causes of Dyslipidemia",
                    "Hypothyroidism ... Liver diseases ... Kidney diseases ... Diabetes mellitus ... Obesity, insulin resistance ... Medications",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — screening at age 10",
                "A healthy 10-year-old girl had cholesterol screening at a well-child visit showing elevated LDL. Was this appropriate?",
                [
                    "No—only screen if symptomatic",
                    "Yes—universal screening includes ages 9–11",
                    "No—wait until age 18 only",
                    "Only if BMI >95th percentile",
                ],
                1,
                "AAP/AHA recommend universal lipid screening at 9–11 years regardless of risk factors.",
                ref(
                    "Who to screen",
                    "Universal screening of all children 9 to 11 years of age regardless of general health or the presence/absence of CVD risk factors.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — diagnosis at 16",
                "A 16-year-old girl with LDL 172 mg/dL, BMI >95th percentile, acanthosis, HbA1c 6.2%, maternal statin use, and grandfather MI at 44. Most likely lipid diagnosis?",
                [
                    "Isolated dietary hypercholesterolemia",
                    "Familial hypercholesterolemia",
                    "Type III dysbetalipoproteinemia",
                    "Cholesteryl ester storage disease",
                ],
                1,
                "After excluding secondary causes, FH is most likely (~1:200–1:500) despite obesity-related metabolic findings.",
                ref(
                    "Question 2: Based on this patient's findings, which of the following is the most likely cause of her lipid abnormality?",
                    "the most likely diagnosis is familial hypercholesterolemia (~1:200-1:500).",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Statin initiation",
                "A 16-year-old with FH has LDL 172 mg/dL and multiple risk factors (obesity, prediabetes, family history). Appropriate therapy?",
                [
                    "Observation only until age 21",
                    "Start statin after LDL >190 mg/dL only",
                    "Start statin (e.g., atorvastatin) with LDL goal ≤100 mg/dL",
                    "Niacin as first-line in adolescents",
                ],
                2,
                "LDL >160 with risk factors meets FDA-approved pediatric statin indication; goal ≤100 or 50% reduction.",
                ref(
                    "Question 3: What treatment would you recommend? What are your treatment goals?",
                    "greater than 160 mg/dL (>4.14 mmol/L) with 1 or more additional risk factor.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Sexually active adolescent",
                "When starting atorvastatin in a sexually active 16-year-old girl with FH, what else is essential?",
                [
                    "Discontinue statin permanently",
                    "Recommend effective contraception and counsel on pregnancy statin risks",
                    "Switch to fenofibrate monotherapy",
                    "Defer statin until menopause",
                ],
                1,
                "Statins are contraindicated in pregnancy; contraception counseling is mandatory in sexually active females.",
                ref(
                    "Case 1 (Continued)",
                    "Because she is sexually active, an oral contraceptive pill is also recommended.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Pregnancy discovery",
                "A 17-year-old on atorvastatin for FH is found 8 weeks pregnant. Best management?",
                [
                    "Continue atorvastatin for fetal LDL benefit",
                    "Stop statin, ezetimibe, and niacin immediately; counsel on pregnancy FH risks",
                    "Double statin dose for placental transfer blockade",
                    "Add ezetimibe for enhanced LDL lowering",
                ],
                1,
                "Category X lipid drugs must stop immediately in pregnancy; prepregnancy counseling advised for all women on therapy.",
                ref(
                    "Case 1 (Continued)",
                    "a woman with familial hypercholesterolemia should discontinue statins, ezetimibe, and niacin immediately.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Triglycerides in FH",
                "A patient with FH has triglycerides 165 mg/dL and BMI >95th percentile with HbA1c 6.2%. This suggests:",
                [
                    "FH cannot coexist with elevated triglycerides",
                    "Possible insulin resistance/prediabetes as secondary contributor",
                    "Mandatory fibrate therapy for pancreatitis prevention",
                    "Exclusion of cascade screening",
                ],
                1,
                "Elevated TG does not exclude FH; insulin resistance may contribute additional CVD risk.",
                ref(
                    "Question 2: Is this patient's elevated triglycerides of concern?",
                    "the presence of an elevated value does not exclude familial hypercholesterolemia.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Nonfasting screening",
                "Preferred practical approach to pediatric lipid screening in clinic is often:",
                [
                    "Mandatory 12-hour fast only",
                    "Nonfasting lipid panel",
                    "Random glucose instead of lipids",
                    "POC total cholesterol alone without HDL",
                ],
                1,
                "Nonfasting samples are practical and acceptable per guidelines.",
                ref(
                    "Question 2: What is the preferred method of cholesterol screening?",
                    "A nonfasting blood sample is often more practical and efficient.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Direct LDL",
                "When triglycerides exceed 400 mg/dL, LDL cholesterol should be:",
                [
                    "Calculated with Friedewald formula only",
                    "Measured with direct assay",
                    "Assumed zero",
                    "Replaced by hemoglobin A1c",
                ],
                1,
                "High TG precludes reliable Friedewald LDL calculation.",
                ref(
                    "Question 2: What is the preferred method of cholesterol screening?",
                    "Significant triglyceride elevation (eg, >400 mg/dL [>4.52 mmol/L]) precludes calculation of LDL cholesterol using the Friedewald formula, in which case LDL cholesterol can be measured with a direct assay.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Genetic panel",
                "Genetic testing for suspected FH should include:",
                [
                    "LDLR, APOB, and PCSK9 analysis",
                    "ABCD1 sequencing only",
                    "KCNJ11 alone",
                    "HLA typing",
                ],
                0,
                "Standard FH gene panel includes LDLR, APOB, PCSK9 with appropriate structural variant analysis.",
                ref(
                    "Question 4: Is there a role for genetic testing?",
                    "genetic testing for suspected familial hypercholesterolemia should include analysis of LDLR, APOB, and PCSK9",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Cascade screening",
                "After identifying FH in an index child, recommended family approach is:",
                [
                    "No family testing needed",
                    "Cascade screening of first-degree relatives",
                    "MRI coronary angiography for all siblings under 5",
                    "Statin for all relatives regardless of LDL",
                ],
                1,
                "Cascade cholesterol or genotype testing of relatives is recommended.",
                ref(
                    "Question 5: Now that you have initiated treatment, is there a role for cascade screening?",
                    "cascade screening), is recommended to enhance detection of individuals at-risk for familial hypercholesterolemia.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Female undertreatment",
                "Data suggest women and children with FH are often:",
                [
                    "Overtreated with combination lipid therapy",
                    "Undertreated compared with men",
                    "Diagnosed earlier than men on average",
                    "Never candidates for statins",
                ],
                1,
                "European registry data show women less likely on lipid-lowering therapy and goal LDL.",
                ref(
                    "Question 1: Should treatment be delayed because the patient is female?",
                    "Recent data from the European Atherosclerosis Society 2020 Virtual Congress suggest that female patients and children are generally undertreated.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Pediatric LDL thresholds",
                "Per Table 1, LDL ≥130 mg/dL in children is classified as:",
                [
                    "Acceptable",
                    "Borderline",
                    "High",
                    "Low",
                ],
                2,
                "Pediatric norms use population percentiles; ≥130 mg/dL is high.",
                ref(
                    "Table 1. Acceptable, Borderline, and High Plasma Lipid and Lipoprotein Concentrations for Children and Adolescents",
                    "LDL cholesterol ... ≥130 mg/dL (SI): ≥3.37 mmol/L)",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Negative genetic test",
                "A child with clinical FH has negative LDLR/APOB/PCSK9 testing. Next step?",
                [
                    "Stop all lipid-lowering therapy permanently",
                    "Consider other genetic causes and continue therapy based on clinical risk",
                    "Assume normal lipids lifelong",
                    "Defer cascade screening",
                ],
                1,
                "Negative testing does not exclude FH or obviate treatment; other genes and polygenic inheritance exist.",
                ref(
                    "Question 4: Is there a role for genetic testing?",
                    "For individuals with negative genetic test results, other pathogenic variants ... and as-yet unidentified genes or polygenic inheritance should be considered.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Universal screening",
                "All U.S. children ages 9–11 should undergo universal cholesterol screening.",
                True,
                "Current AAP/AHA recommendation.",
                ref(
                    "Who to screen",
                    "Universal screening of all children 9 to 11 years of age regardless of general health or the presence/absence of CVD risk factors.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Repeat screening",
                "If initial childhood cholesterol screening is normal, repeat testing is recommended between ages 17 and 21.",
                True,
                "Stated in screening guidelines.",
                ref(
                    "Who to screen",
                    "If the initial cholesterol value is normal, screening should be repeated between 17 and 21 years of age.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Statin pregnancy",
                "Statins may be continued throughout pregnancy in women with familial hypercholesterolemia.",
                False,
                "Category X—must discontinue in pregnancy and breastfeeding.",
                ref(
                    "Case 1 (Continued)",
                    "These treatments SHOULD NOT BE USED during pregnancy.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "FH prevalence",
                "Familial hypercholesterolemia affects approximately 1 in 200–500 individuals.",
                True,
                "Cited prevalence range.",
                ref(
                    "Question 2: Based on this patient's findings, which of the following is the most likely cause of her lipid abnormality?",
                    "familial hypercholesterolemia (~1:200-1:500).",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Advanced lipid testing",
                "Routine advanced lipoprotein subclass analysis is recommended for all children.",
                False,
                "Not routinely recommended; may help selected cases.",
                ref(
                    "Advanced Lipid Testing",
                    "routine measurement of lipoprotein (a), apolipoprotein B, apolipoprotein A1, and lipoprotein subclasses and their sizes by advanced lipoprotein analysis is not currently recommended",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Statin pediatric approval",
                "All statins are FDA-approved for use in children with familial hypercholesterolemia meeting LDL thresholds.",
                True,
                "Main conclusions statement.",
                ref(
                    "Main Conclusions",
                    "All statins have been approved by the US FDA for use in children with familial hypercholesterolemia",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Lifestyle alone in FH",
                "A heart-healthy lifestyle alone is unlikely to prevent atherosclerosis in familial hypercholesterolemia.",
                True,
                "Listed as barrier—lifestyle alone insufficient for FH.",
                ref(
                    "Significance of the Clinical Problem",
                    "A heart-healthy lifestyle alone is unlikely to prevent atherosclerosis in individuals with familial hypercholesterolemia.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Lp(a) stability",
                "Lipoprotein(a) levels are generally stable throughout an individual's lifespan after early childhood.",
                True,
                "Adult levels achieved by 2–5 years and remain constant.",
                ref(
                    "Advanced Lipid Testing",
                    "in general the level is stable and remains constant throughout the lifespan of an individual.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Universal screening",
                "Assertion: Universal lipid screening at ages 9–11 can identify asymptomatic familial hypercholesterolemia.",
                "Reason: Cascade screening alone is more effective than universal testing.",
                2,
                "Assertion true; cascade depends on index case—reason misstates comparative strategy.",
                ref(
                    "Significance of the Clinical Problem",
                    "Universal testing has the advantage of identifying familial hypercholesterolemia in asymptomatic youth and young adults",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Statin efficacy",
                "Assertion: Pediatric statin therapy improves noninvasive measures of atherosclerosis.",
                "Reason: No pediatric statin trial has ever measured carotid intima-media thickness.",
                2,
                "Assertion true per trials; reason false.",
                ref(
                    "Question 3: Is there evidence that lipid-lowering medications, such as statins, are safe when prescribed at a young age? If so, are they effective?",
                    "pharmacologic treatment is safe and effective and improves noninvasive measures of atherosclerosis, such as carotid intima-media thickness.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Nonfasting lipids",
                "Assertion: Nonfasting lipid screening is acceptable in children.",
                "Reason: Food intake always invalidates LDL measurement in pediatrics.",
                2,
                "Assertion true; direct LDL and Lp(a) minimally affected—reason false.",
                ref(
                    "Question 2: What is the preferred method of cholesterol screening?",
                    "Screening can be performed using a fasting or nonfasting lipid profile.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "FH and obesity",
                "Assertion: Elevated triglycerides do not exclude familial hypercholesterolemia.",
                "Reason: FH always presents with normal triglycerides.",
                2,
                "Assertion true; most FH have normal TG but obesity can coexist—reason false.",
                ref(
                    "Question 2: Is this patient's elevated triglycerides of concern?",
                    "the presence of an elevated value does not exclude familial hypercholesterolemia.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Genetic testing",
                "Assertion: Genetic testing is recommended for clinically suspected FH.",
                "Reason: A negative genetic test always means statins are unnecessary.",
                2,
                "Assertion true; negative test does not exclude need for therapy—reason false.",
                ref(
                    "Question 4: Is there a role for genetic testing?",
                    "some parents might assume that a lipid-lowering medication is unnecessary for children in whom no common genetic pathogenic variant is found.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Pregnancy statins",
                "Assertion: Statins should be stopped immediately if FH patient has unintended pregnancy.",
                "Reason: Statins are safe category A drugs in pregnancy.",
                2,
                "Assertion true; category X—reason false.",
                ref(
                    "Case 1 (Continued)",
                    "instructions to stop statins, ezetimibe, and niacin at least 4 weeks before discontinuing contraception. These treatments SHOULD NOT BE USED during pregnancy.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Treatment goal",
                "Assertion: LDL goal in pediatric FH is ≤100 mg/dL or ≥50% reduction from baseline.",
                "Reason: Pediatric LDL goals are always <70 mg/dL regardless of age.",
                2,
                "Assertion states guideline goal; <70 not specified here—reason false.",
                ref(
                    "Question 3: What treatment would you recommend? What are your treatment goals?",
                    "The treatment goal is an LDL-cholesterol concentration of 100 mg/dL or less (≤2.59 mmol/L), or a minimum of 50% reduction from baseline.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Cascade screening",
                "Assertion: Cascade screening of first-degree relatives is recommended after FH diagnosis.",
                "Reason: Only children, never adults, need family screening.",
                2,
                "Assertion true; adults often at greater short-term risk—reason false.",
                ref(
                    "Question 5: Now that you have initiated treatment, is there a role for cascade screening?",
                    "adults in the family, many of whom may be unaware of their hypercholesterolemia, are at greater short-term risk than affected children.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "31",
        "title": "What Pediatric Endocrinologists Need to Know About Dyslipidemia",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Don P. Wilson, MD, FNLA",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_31_What_Pediatric_Endocrinologists_Need_to_Know_About_Dyslipidemia.md",
        "items": items,
    }


MODULES = {
    "endo2021_chapter_28_diabetes_Insipidus_in_Children.json": build_chapter_28,
    "endo2021_chapter_29_Screening_of_the_Newborn_for_Adrenoleukodystrophy.json": build_chapter_29,
    "endo2021_chapter_30_YouthOnset_Type_2_Diabetes_Mellitus.json": build_chapter_30,
    "endo2021_chapter_31_What_Pediatric_Endocrinologists_Need_to_Know_About_Dyslipidemia.json": build_chapter_31,
}


def write_module(filename: str, data: dict) -> tuple[Path, Path]:
    PORTAL_DATA.mkdir(parents=True, exist_ok=True)
    portal_path = PORTAL_DATA / filename
    portal_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
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
        pct = 100 * wh // notes if notes else 0
        print(
            f"Wrote {portal_path.name} ({len(data['items'])} items, {counts}, Why/How {wh}/{notes} = {pct}%)"
        )
        print(f"  Copied to {master_path}")


if __name__ == "__main__":
    main()
