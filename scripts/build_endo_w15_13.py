#!/usr/bin/env python3
"""Generate Williams 15e module w15-13 — The Adrenal Cortex."""
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
OUT_NAME = "w15-13_The_Adrenal_Cortex.json"


def build() -> dict:
    p = "w15-13"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Adrenal cortex chapter scope",
                "Williams 15e covers adrenal steroidogenesis, HPA-axis regulation, glucocorticoid receptor action, Cushing syndrome, adrenal insufficiency, CAH, replacement therapy, and adrenal tumors.",
                ref(
                    "KEY POINTS",
                    "Glucocorticoid excess and Cushing syndrome, adrenal insufficiency and Addison disease, and inherited disorders of the adrenal gland are also discussed.",
                ),
            ),
            note(
                f"{p}-n2",
                "Anatomy and Development",
                "Adrenal cortical zonation and development",
                "The adult cortex comprises zona glomerulosa (~15%), fasciculata (~75%), and reticularis; fetal zone involutes postnatally while definitive zone differentiates into adult zones with distinct steroidogenic enzyme expression.",
                ref(
                    "Anatomy and Development",
                    "The ZF makes up 75% of the cortex; cells are large and lipid laden and form radial cords within the fibrovascular radial network.",
                ),
            ),
            note(
                f"{p}-n3",
                "Adrenal Steroids and Steroidogenesis",
                "Why zona glomerulosa cannot synthesize cortisol",
                "Zona glomerulosa lacks 17α-hydroxylase (CYP17A1), so it cannot convert progesterone through 17OHP to cortisol; aldosterone synthesis is confined there via zone-restricted CYP11B2 expression.",
                ref(
                    "Adrenal Steroids and Steroidogenesis",
                    "17α-Hydroxylation is an essential prerequisite for cortisol synthesis, and the ZG does not express 17α-hydroxylase.",
                ),
            ),
            note(
                f"{p}-n4",
                "Adrenal Steroids and Steroidogenesis",
                "How StAR gates adrenal steroidogenesis",
                "ACTH raises intracellular cAMP, inducing StAR to shuttle cholesterol across the mitochondrial membrane—the rate-limiting step before CYP11A1 converts cholesterol to pregnenolone.",
                ref(
                    "Adrenal Steroids and Steroidogenesis",
                    "StAR is induced by an increase in intracellular cyclic adenosine monophosphate (cAMP) after binding of ACTH to its cognate receptor, providing the first important rate-limiting step in adrenal steroidogenesis.",
                ),
            ),
            note(
                f"{p}-n5",
                "Regulation of Adrenal Steroidogenesis",
                "Functional zonation of glucocorticoid and mineralocorticoid secretion",
                "Glucocorticoids (~10–20 mg/day cortisol) are secreted from zona fasciculata under ACTH; aldosterone (~100–150 µg/day) from zona glomerulosa under angiotensin II, with zone-specific enzyme expression enforcing separation.",
                ref(
                    "Regulation of Adrenal Steroidogenesis: Functional Zonation of the Adrenal Cortex",
                    "Glucocorticoids are secreted in relatively high amounts (cortisol, 10–20 mg/day) from the ZF under the control of ACTH; mineralocorticoids are secreted in low amounts (aldosterone, 100–150 µg/day) from the ZG under the principal control of angiotensin II.",
                ),
            ),
            note(
                f"{p}-n6",
                "Corticosteroid Hormone Action",
                "Why 11βHSD2 confers mineralocorticoid receptor specificity",
                "Because MR binds cortisol with affinity similar to aldosterone, renal 11βHSD2 inactivates cortisol to cortisone so aldosterone can occupy the receptor without cortisol acting as a mineralocorticoid.",
                ref(
                    "Corticosteroid Hormone Action",
                    "Specificity on the MR is conferred through the \"prereceptor\" metabolism of cortisol via the enzyme 11βHSD2, which converts cortisol and corticosterone to inactive 11-keto metabolites, enabling aldosterone to bind to the MR.",
                ),
            ),
            note(
                f"{p}-n7",
                "Negative Feedback",
                "HPA-axis glucocorticoid negative feedback",
                "Glucocorticoids inhibit POMC transcription in the pituitary and CRH/AVP synthesis in the hypothalamus; prolonged exogenous steroids can suppress the axis for months after withdrawal.",
                ref(
                    "Negative Feedback",
                    "Suppression of the HPA axis by pharmacologic corticosteroids may persist for many months after cessation of therapy, and adrenocortical insufficiency should be anticipated.",
                ),
            ),
            note(
                f"{p}-n8",
                "Glucocorticoid Secretion",
                "How CRH and AVP coordinate ACTH release",
                "Hypothalamic CRH is the principal ACTH secretagogue via type I CRH receptors and cAMP; AVP potentiates CRH through V1b receptors and protein kinase C.",
                ref(
                    "Corticotropin-Releasing Hormone and Arginine Vasopressin",
                    "CRH is the principal stimulus for ACTH secretion, but AVP is able to potentiate CRH-mediated secretion.",
                ),
            ),
            note(
                f"{p}-n9",
                "Circadian Rhythm",
                "Circadian and pulsatile cortisol secretion",
                "ACTH and cortisol peak on awakening and fall to a nadir by evening; circadian rhythm depends on sleep-wake and day-night cycles and is lost in Cushing disease.",
                ref(
                    "Circadian Rhythm",
                    "ACTH, and hence cortisol, is secreted in a pulsatile fashion with a circadian rhythm; levels are highest on awakening and decline throughout the day, reaching nadir values in the evening (Fig. 13.8).",
                ),
            ),
            note(
                f"{p}-n10",
                "Cushing Syndrome",
                "Why ectopic ACTH syndrome causes hypokalemic alkalosis",
                "Very high cortisol secretion saturates renal 11βHSD2, allowing cortisol to act as a mineralocorticoid; elevated DOC from ACTH drive also contributes—hypokalemia occurs in >95% of ectopic cases versus <10% in Cushing disease.",
                ref(
                    "Question 2: What Is the Cause of Cushing Syndrome in This Patient?",
                    "Hypokalemic alkalosis is present in more than 95% of patients with the ectopic ACTH syndrome but in fewer than 10% of those with Cushing disease.",
                ),
            ),
            note(
                f"{p}-n11",
                "Corticosteroid Hormone Action",
                "Glucocorticoid transrepression and anti-inflammatory action",
                "GR-ligand complexes antagonize AP-1 and NF-κB, repressing pro-inflammatory cytokines and explaining rapid anti-inflammatory effects beyond classic GRE-mediated transactivation.",
                ref(
                    "Receptors and Gene Transcription",
                    "The GR-ligand complex can bind to c-Jun and prevent interaction with the AP1 site, thereby mediating the so-called transrepressive effects of glucocorticoids.",
                ),
            ),
            note(
                f"{p}-n12",
                "Therapeutic Corticosteroids",
                "How oral glucocorticoid potencies compare",
                "Relative GR potency guides replacement and suppression risk: ~20 mg hydrocortisone, ~5 mg prednisolone, and ~0.75 mg dexamethasone are bioequivalent; dexamethasone has longer half-life and stronger HPA suppression.",
                ref(
                    "ACTH Suppression by Exogenous Glucocorticoids",
                    "these suggest that oral doses of 20 mg of hydrocortisone, 5 mg of prednisolone, and 0.75 mg of dexamethasone are bioequivalent.",
                ),
            ),
            note(
                f"{p}-n13",
                "Cushing Syndrome",
                "Cushing syndrome versus Cushing disease",
                "Cushing syndrome denotes any pathologic hypercortisolism (endogenous or exogenous); Cushing disease is pituitary ACTH-dependent Cushing syndrome, most often from a corticotrope adenoma.",
                ref(
                    "Cushing Syndrome",
                    "The term Cushing syndrome is used to describe all causes, whereas Cushing disease is reserved for pituitary-dependent Cushing syndrome.",
                ),
            ),
            note(
                f"{p}-n14",
                "Question 1: Does This Patient Have Cushing Syndrome?",
                "Why late-night salivary cortisol screens for Cushing",
                "Loss of circadian rhythm means elevated nocturnal free cortisol; salivary cortisol avoids hospitalization and, in validated assays, discriminates Cushing with high sensitivity and specificity.",
                ref(
                    "Salivary Cortisol",
                    "In one study, a cortisol value of greater than 2.0 ng/mL (>5.5 nmol/L) had a 100% sensitivity and a 96% specificity for diagnosis of Cushing syndrome.",
                ),
            ),
            note(
                f"{p}-n15",
                "Inferior Petrosal Sinus Sampling and Selective Venous Catheterization",
                "How IPSS distinguishes pituitary from ectopic ACTH",
                "Simultaneous petrosal and peripheral ACTH sampling after CRH stimulation: petrosal/peripheral ratio >3 after CRH has ~95% sensitivity and nearly 100% specificity for Cushing disease.",
                ref(
                    "Inferior Petrosal Sinus Sampling and Selective Venous Catheterization",
                    "Using this approach, an ACTH petrosal sinus/peripheral ratio of >3 after CRH administration has a sensitivity of 95% and specificity of nearly 100% for diagnosing Cushing disease.",
                ),
            ),
            note(
                f"{p}-n16",
                "Addison Disease",
                "Addison disease epidemiology and prognosis",
                "Primary adrenal failure is rare (~0.8/100,000 incidence) but carries twofold excess mortality if missed; autoimmune adrenalitis accounts for >70% of acquired cases in Western countries.",
                ref(
                    "Addison Disease",
                    "Addison disease is a rare condition with an estimated incidence in the developed world of 0.8 cases per 100,000 and a prevalence of 4 to 11 cases per 100,000 population.",
                ),
            ),
            note(
                f"{p}-n17",
                "Clinical Features of Adrenal Insufficiency",
                "Why hyperpigmentation signals primary adrenal failure",
                "ACTH (not α-MSH) overstimulates melanocortin-1 receptors in skin; pigmentation is nearly universal in primary insufficiency and absent in secondary ACTH deficiency.",
                ref(
                    "Clinical Features of Adrenal Insufficiency",
                    "The most obvious feature that differentiates primary from secondary hypoadrenalism is skin pigmentation (Table 13.10), which is almost always present in cases of primary adrenal insufficiency (unless of short duration) and absent in secondary insufficiency.",
                ),
            ),
            note(
                f"{p}-n18",
                "Assessing Adequacy of Function of the HPA Axis",
                "How the short synacthen test assesses adrenal reserve",
                "250 µg synthetic ACTH(1–24) is given IV/IM; peak cortisol >550 nmol/L (assay-dependent, often >430–450 with LC-MS/MS) indicates adequate zona fasciculata responsiveness.",
                ref(
                    "Assessing Adequacy of Function of the HPA Axis",
                    "a normal response has previously been defined by a peak plasma cortisol level greater than 550 nmol/L (>20 µg/dL).",
                ),
            ),
            note(
                f"{p}-n19",
                "Treatment of Acute Adrenal Insufficiency",
                "Acute adrenal crisis management",
                "Do not delay treatment: IV hydrocortisone 100 mg q6–8h, aggressive saline/dextrose resuscitation, and treat precipitating illness; draw ACTH/cortisol before steroids when possible.",
                ref(
                    "Treatment of Acute Adrenal Insufficiency",
                    "In adults, intravenous hydrocortisone should be given in a dose of 100 mg every 6 to 8 hours.",
                ),
            ),
            note(
                f"{p}-n20",
                "Long-Term Replacement Therapy",
                "Chronic glucocorticoid and mineralocorticoid replacement",
                "Hydrocortisone 15–20 mg on waking plus 5–10 mg afternoon mimics physiologic secretion (~8–15 mg/day production); primary failure also needs fludrocortisone 0.05–0.2 mg with renin and electrolyte monitoring.",
                ref(
                    "Long-Term Replacement Therapy",
                    "Most patients are adequately treated with less than 30 mg/day (usually 15–25 mg/day in divided doses).",
                ),
            ),
            note(
                f"{p}-n21",
                "Maintenance Therapy",
                "Why stress-dose glucocorticoids are mandatory",
                "Patients on replacement cannot mount a cortisol surge during illness or surgery; doubling oral dose for febrile illness or giving parenteral hydrocortisone for vomiting, trauma, or major surgery prevents adrenal crisis.",
                ref(
                    "Treatment of Minor Febrile Illness or Stress",
                    "Increase glucocorticoid dose twofold to threefold for the few days of illness; do not change mineralocorticoid dose.",
                ),
            ),
            note(
                f"{p}-n22",
                "Congenital Adrenal Hyperplasia",
                "How 21-hydroxylase deficiency causes virilization",
                "Blocked 21-hydroxylation impairs cortisol synthesis, removing negative feedback and driving ACTH-mediated accumulation of adrenal androgen precursors proximal to the enzymatic block.",
                ref(
                    "21-Hydroxylase Deficiency",
                    "Reduced cortisol biosynthesis results in a reduced negative feedback drive and increased ACTH secretion; as a consequence, adrenal androgens are produced in excess (Fig. 13.35).",
                ),
            ),
            note(
                f"{p}-n23",
                "Classic 21-Hydroxylase Deficiency",
                "Classic versus nonclassic 21-hydroxylase deficiency",
                "Classic disease causes cortisol deficiency with virilization of 46,XX infants and salt wasting in ~75%; nonclassic disease presents later with hyperandrogenism mimicking PCOS, with normal basal cortisol.",
                ref(
                    "Classic 21-Hydroxylase Deficiency",
                    "About 75% of patients with classic 21-hydroxylase deficiency have concomitant, clinically manifested aldosterone deficiency and a strong propensity for salt wasting.",
                ),
            ),
            note(
                f"{p}-n24",
                "Classic 21-Hydroxylase Deficiency",
                "Why males with classic CAH are often diagnosed late",
                "46,XY infants appear phenotypically normal at birth, so diagnosis may be delayed until precocious pubarche or growth acceleration—contributing to skewed female-to-male detection before newborn screening.",
                ref(
                    "Classic 21-Hydroxylase Deficiency",
                    "Males are phenotypically normal at birth and are at risk of not being diagnosed; this explains the skewed female-to-male ratio of simple virilizing CAH diagnosed in the preneonatal screening era.",
                ),
            ),
            note(
                f"{p}-n25",
                "Incidentalomas",
                "Adrenal incidentaloma biochemical screening",
                "All incidentally discovered adrenal masses need endocrine testing: plasma or urinary metanephrines, overnight 1-mg dexamethasone suppression, and renin/aldosterone if hypertensive; DHEAS when androgen excess is suspected.",
                ref(
                    "Incidentalomas",
                    "This testing should comprise 24-hour urinary metanephrine collection or measurement of plasma metanephrines; an overnight dexamethasone suppression test; and for those with hypertension, measurement of plasma renin and aldosterone.",
                ),
            ),
            note(
                f"{p}-n26",
                "Incidentalomas",
                "How incidentaloma size predicts malignancy",
                "In true incidentalomas, malignancy is rare <4 cm but ~25% when >6 cm; smooth homogeneous lesions <10 HU on CT or signal dropout on chemical-shift MRI are invariably benign.",
                ref(
                    "Incidentalomas",
                    "Fewer than 2% of incidentalomas smaller than 4 cm but 25% of those larger than 6 cm in diameter are malignant (Fig. 13.41).",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Question 1: Does This Patient Have Cushing Syndrome?",
                "A 48-year-old woman with central obesity, purple striae, and proximal weakness has normal 9 AM serum cortisol. Best next screening test?",
                [
                    "Late-night salivary cortisol or 1-mg overnight dexamethasone suppression test",
                    "Random morning cortisol alone because it is already normal",
                    "Serum DHEAS to exclude adrenal source",
                    "Immediate bilateral adrenalectomy without biochemical confirmation",
                ],
                0,
                "Random morning cortisol is unhelpful; Endocrine Society guidelines recommend UFC, late-night salivary cortisol, or low-dose dexamethasone suppression when Cushing is suspected.",
                ref(
                    "Diagnostic Guidelines",
                    "Recommendations are to proceed initially with one of four highly sensitive screening tests: urinary free cortisol, late-night salivary cortisol, overnight dexamethasone, or the 2-mg/48-hour dexamethasone suppression test.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Question 1: Does This Patient Have Cushing Syndrome?",
                "After 1 mg dexamethasone at 11 PM, 8 AM plasma cortisol is 62 nmol/L (2.2 µg/dL). Interpretation?",
                [
                    "Failure to suppress—supports Cushing syndrome; confirm with a second test",
                    "Normal suppression—Cushing excluded permanently",
                    "Result proves pituitary Cushing disease",
                    "Result indicates primary adrenal insufficiency",
                ],
                0,
                "Post-dexamethasone cortisol <50 nmol/L is normal suppression; values above cutoff indicate lack of feedback suppression seen in Cushing syndrome.",
                ref(
                    "Low-Dose Overnight Dexamethasone Suppression Tests",
                    "A normal response is a plasma cortisol level of less than 50 nmol/L (<1.8 μg/dL) between 8 and 9 AM the following morning.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Question 2: What Is the Cause of Cushing Syndrome in This Patient?",
                "Confirmed Cushing syndrome: ACTH 35 pmol/L, hypokalemia, very high UFC. Most likely source?",
                [
                    "Ectopic ACTH secretion rather than pituitary Cushing disease",
                    "Nonfunctioning adrenal adenoma",
                    "Primary adrenal insufficiency",
                    "Iatrogenic glucocorticoid withdrawal",
                ],
                0,
                "Markedly elevated ACTH with hypokalemic alkalosis strongly favors ectopic ACTH; pituitary disease rarely causes hypokalemia.",
                ref(
                    "Question 2: What Is the Cause of Cushing Syndrome in This Patient?",
                    "ACTH levels in the ectopic ACTH syndrome are high (usually >20 pmol/L [>90 pg/mL]); nevertheless, overlap values are seen in Cushing disease in 30% of cases.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Inferior Petrosal Sinus Sampling and Selective Venous Catheterization",
                "ACTH-dependent Cushing: MRI shows no pituitary adenoma; high-dose dexamethasone and CRH results are equivocal. Definitive next test?",
                [
                    "Inferior petrosal sinus sampling with CRH stimulation",
                    "Repeat random morning cortisol in 6 months",
                    "Serum aldosterone to lateralize the lesion",
                    "Thyroid scintigraphy",
                ],
                0,
                "IPSS with CRH is the most robust test to distinguish pituitary Cushing disease from ectopic ACTH when imaging and dynamic tests are inconclusive.",
                ref(
                    "Inferior Petrosal Sinus Sampling and Selective Venous Catheterization",
                    "The most robust test to distinguish Cushing disease from the ectopic ACTH syndrome is IPSS.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Imaging",
                "Biochemically confirmed ACTH-independent Cushing with undetectable ACTH. Pitfall to avoid on adrenal CT?",
                [
                    "Mistaking asymmetric macronodular hyperplasia for a unilateral adenoma and operating on the wrong premise",
                    "Assuming bilateral adrenal enlargement always means metastases",
                    "Ordering IPSS before adrenal imaging",
                    "Treating with fludrocortisone before surgery",
                ],
                0,
                "Asymmetric nodular hyperplasia can mimic a unilateral adenoma; ignoring low-normal ACTH risks inappropriate unilateral adrenalectomy.",
                ref(
                    "Morning Plasma ACTH",
                    "The danger is that in some patients, the asymmetry of the nodular hyperplasia may lead to a diagnosis of adrenal adenoma, the plasma ACTH is ignored, and an inappropriate adrenalectomy is performed.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Treatment of Cushing Syndrome",
                "A patient undergoes laparoscopic adrenalectomy for a cortisol-secreting adenoma. Postoperative 9 AM cortisol is 30 nmol/L. Management?",
                [
                    "Continue glucocorticoid replacement until contralateral adrenal recovery; carry steroid alert card",
                    "No replacement needed because tumor is removed",
                    "Start mitotane immediately",
                    "Begin high-dose dexamethasone suppression testing daily",
                ],
                0,
                "After unilateral adrenalectomy the contralateral gland is suppressed; physiologic hydrocortisone is continued until morning cortisol recovers.",
                ref(
                    "Adrenal Causes",
                    "After surgery, it may take many months or even years for the contralateral suppressed adrenal to recover.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Clinical Features of Adrenal Insufficiency",
                "A 34-year-old has fatigue, weight loss, postural dizziness, and buccal pigmentation. Electrolytes: Na 128, K 5.8 mmol/L. Diagnosis?",
                [
                    "Primary adrenal insufficiency (Addison disease)",
                    "Secondary adrenal insufficiency from pituitary disease",
                    "Primary hyperaldosteronism",
                    "Subclinical hyperthyroidism",
                ],
                0,
                "Hyperpigmentation with hyponatremia and hyperkalemia indicates primary adrenal failure with mineralocorticoid and glucocorticoid deficiency.",
                ref(
                    "Routine Biochemical Profile",
                    "Among patients with established primary adrenal insufficiency, hyponatremia is present in about 90% and hyperkalemia in 65%.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Treatment of Acute Adrenal Insufficiency",
                "A known Addison patient presents hypotensive after vomiting and cannot take oral steroids. Immediate management?",
                [
                    "IV hydrocortisone 100 mg plus saline resuscitation",
                    "Oral fludrocortisone alone",
                    "Wait for SST results before any treatment",
                    "IV dexamethasone 4 mg weekly only",
                ],
                0,
                "Adrenal crisis is an emergency: parenteral hydrocortisone and volume resuscitation must not wait for confirmatory testing.",
                ref(
                    "Emergency Measures",
                    "Inject intravenous hydrocortisone (100 mg immediately and every 6 hours).",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Assessing Adequacy of Function of the HPA Axis",
                "A patient on chronic prednisolone 7.5 mg daily for 2 years plans elective surgery. Best preoperative assessment?",
                [
                    "Evaluate HPA-axis recovery (morning cortisol ± SST after brief steroid omission) and provide perioperative stress coverage",
                    "Stop all steroids abruptly 1 week before surgery",
                    "Assume axis is intact because dose is low",
                    "Measure serum aldosterone before surgery",
                ],
                0,
                "Long-term glucocorticoids suppress the HPA axis unpredictably; patients need assessment and supplemental steroid cover for surgery.",
                ref(
                    "ACTH Suppression by Exogenous Glucocorticoids",
                    "All patients receiving long-term therapy with corticosteroids should be treated in a similar fashion to patients with chronic ACTH deficiency; they should carry steroid cards and be offered steroid alert bracelets or necklaces.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "ACTH Suppression by Exogenous Glucocorticoids",
                "An asthmatic on high-dose inhaled fluticasone develops fatigue and hypotension. Likely mechanism?",
                [
                    "Iatrogenic secondary adrenal insufficiency from inhaled glucocorticoid HPA suppression",
                    "Primary hyperaldosteronism from fluticasone",
                    "Pheochromocytoma crisis",
                    "Excess endogenous cortisol production",
                ],
                0,
                "Inhaled fluticasone at >1000 µg/day for >1 year can suppress the HPA axis, especially with CYP3A4 inhibitors.",
                ref(
                    "ACTH Suppression by Exogenous Glucocorticoids",
                    "adults using over 1000 μg of inhaled fluticasone for over a year were at risk of adrenal suppression.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Congenital Adrenal Hyperplasia",
                "A newborn 46,XX infant has ambiguous genitalia and salt wasting at 3 weeks. Most likely enzymatic defect?",
                [
                    "21-Hydroxylase deficiency (CYP21A2)",
                    "17α-Hydroxylase deficiency",
                    "Aldosterone synthase deficiency only",
                    "11β-Hydroxylase deficiency with hypertension",
                ],
                0,
                "21-Hydroxylase deficiency accounts for 90–95% of CAH and causes cortisol deficiency with androgen excess and salt wasting in most classic cases.",
                ref(
                    "21-Hydroxylase Deficiency",
                    "Between 90% and 95% of cases of CAH are caused by 21-hydroxylase deficiency.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Nonclassic 21-Hydroxylase Deficiency",
                "A 22-year-old woman has hirsutism and oligomenorrhea. Total testosterone modestly elevated; 17OHP after ACTH stimulation is 85 nmol/L. Next step?",
                [
                    "Treat as nonclassic 21-hydroxylase deficiency—glucocorticoid ± antiandrogen therapy",
                    "Diagnose polycystic ovary syndrome and ignore 17OHP",
                    "Emergency bilateral adrenalectomy",
                    "Start fludrocortisone for mineralocorticoid excess",
                ],
                0,
                "Stimulated 17OHP >30 nmol/L supports nonclassic 21-hydroxylase deficiency, a recognized PCOS mimic.",
                ref(
                    "Diagnostic Criteria",
                    "Stimulated values are invariably grossly elevated in patients with classic (>300 nmol/L [>1,000 ng/dL]) and less so in nonclassic (>30 nmol/L [>1,000 ng/dL]) forms of the disorder (see Table 13.12).",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Treatment",
                "A child with classic salt-wasting CAH is started on replacement. Which monitoring best guides glucocorticoid dose?",
                [
                    "Growth velocity and bone age, with 17OHP/androgens as adjuncts",
                    "Serum sodium alone",
                    "Urinary cortisol only in adults",
                    "TSH suppression to <0.1 mU/L",
                ],
                0,
                "Pediatric CAH dosing balances preventing salt-wasting crises against suppressing androgen-driven growth acceleration and premature epiphyseal closure.",
                ref(
                    "Treatment",
                    "Response is best monitored through growth velocity and bone age, with biochemical markers from blood (17OHP, androstenedione, testosterone), urine, and saliva (17OHP, androstenedione, testosterone) being useful adjuncts.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "11β-Hydroxylase Deficiency",
                "An infant with ambiguous genitalia has hypertension and elevated DOC. Likely CAH variant?",
                [
                    "11β-Hydroxylase deficiency",
                    "21-Hydroxylase salt-wasting form",
                    "17α-Hydroxylase deficiency",
                    "Cortisone reductase deficiency",
                ],
                0,
                "11β-Hydroxylase deficiency blocks cortisol synthesis and causes DOC excess with hypertension, distinguishing it from classic 21-hydroxylase deficiency.",
                ref(
                    "11β-Hydroxylase Deficiency",
                    "The principal difference from 21-hydroxylase deficiency is hypertension, which is thought to be secondary to the mineralocorticoid effect of DOC excess.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Incidentalomas",
                "A 2.5-cm homogeneous adrenal mass (8 HU) is found on CT for renal colic. Patient is normotensive. Essential workup?",
                [
                    "Plasma metanephrines and overnight 1-mg dexamethasone suppression test",
                    "Immediate open adrenalectomy without biochemistry",
                    "Fine-needle biopsy of the adrenal mass first",
                    "No testing—all incidentalomas are malignant",
                ],
                0,
                "ENSAT/ESE guidelines mandate biochemical screening for pheochromocytoma, cortisol autonomy, and hyperaldosteronism when hypertensive.",
                ref(
                    "Incidentalomas",
                    "This testing should comprise 24-hour urinary metanephrine collection or measurement of plasma metanephrines; an overnight dexamethasone suppression test; and for those with hypertension, measurement of plasma renin and aldosterone.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Incidentalomas",
                "A 5.5-cm heterogeneous adrenal incidentaloma with 35 HU and history of weight loss. Best management?",
                [
                    "Surgical resection after pheochromocytoma exclusion—high suspicion for carcinoma",
                    "Observation only because most incidentalomas are benign",
                    "131I adrenal scintigraphy as sole therapy",
                    "Empiric dexamethasone suppression for 6 months",
                ],
                0,
                "Lesions >4–6 cm with malignant imaging features warrant surgery; carcinoma risk rises sharply above 6 cm.",
                ref(
                    "Incidentalomas",
                    "adrenalectomy is considered for functional tumors and for tumors larger than 4 cm in diameter",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Carcinomas",
                "A 44-year-old woman has rapid onset Cushingoid features, abdominal pain, and a 9-cm adrenal mass with liver metastases. First-line systemic therapy?",
                [
                    "Mitotane with cytotoxic chemotherapy (e.g., etoposide/doxorubicin/cisplatin) after maximal surgical debulking when feasible",
                    "Levothyroxine suppression",
                    "Radioiodine ablation",
                    "Observation only",
                ],
                0,
                "Adrenocortical carcinoma has poor prognosis; mitotane with combination chemotherapy is standard when metastatic disease is present.",
                ref(
                    "Carcinomas",
                    "The combination of etoposide, doxorubicin, and cisplatin is the first-line cytotoxic chemotherapy with or without mitotane",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Adrenal Steroids and Steroidogenesis",
                "A patient with autoimmune Addison disease starts rifampicin for TB. Risk to monitor?",
                [
                    "Adrenal crisis from increased cortisol metabolism reducing effective replacement",
                    "Hyperkalemia from rifampicin mineralocorticoid effect",
                    "Cushing syndrome from rifampicin",
                    "No interaction—rifampicin does not affect steroids",
                ],
                0,
                "Rifampicin induces CYP3A4 and accelerates cortisol clearance; hydrocortisone doses may need upward adjustment in replaced patients.",
                ref(
                    "Corticosteroid-Binding Globulin and Corticosteroid Hormone Metabolism",
                    "Adrenal crisis has been reported in steroid-replaced addisonian patients given rifampicin",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Pro-Opiomelanocortin and ACTH",
                "Hyperpigmentation in untreated Addison disease is primarily driven by:",
                [
                    "Elevated ACTH binding melanocortin-1 receptors rather than α-MSH secretion",
                    "Excess α-MSH from pituitary secretion",
                    "High aldosterone stimulating melanocytes",
                    "Estrogen-induced melanogenesis",
                ],
                0,
                "ACTH itself stimulates MC1R; α-MSH is not the principal pigmentary mediator in Addison disease.",
                ref(
                    "Pro-Opiomelanocortin and ACTH",
                    "the increased pigmentation characteristic of Addison disease is thought to arise directly from increased ACTH concentrations binding to the melanocortin-1 receptor (MC1R) rather than from αMSH secretion.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Primary and Central Hypoadrenalism",
                "Which feature reliably distinguishes primary from secondary adrenal insufficiency?",
                [
                    "Hyperpigmentation and hyperkalemia occur in primary but not secondary disease",
                    "Secondary disease always causes more severe hypotension",
                    "Primary disease has suppressed plasma renin",
                    "Secondary disease requires fludrocortisone in all patients",
                ],
                0,
                "Mineralocorticoid deficiency accompanies primary adrenal failure; secondary ACTH deficiency leaves the renin-angiotensin-aldosterone axis intact.",
                ref(
                    "Primary and Central Hypoadrenalism",
                    "A major distinction between these forms of hypoadrenalism is that mineralocorticoid deficiency invariably accompanies primary hypoadrenalism, but this does not occur in central hypoadrenalism",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Corticotropin-Releasing Hormone Test",
                "After IV CRH, ACTH rises >100% and cortisol >50% over baseline in ACTH-dependent Cushing. Interpretation?",
                [
                    "Response favors pituitary Cushing disease over ectopic ACTH",
                    "Proves adrenal adenoma",
                    "Excludes any form of Cushing syndrome",
                    "Indicates primary adrenal insufficiency",
                ],
                0,
                "Marked ACTH and cortisol responses to CRH are typical of Cushing disease and help exclude most ectopic ACTH syndromes.",
                ref(
                    "Corticotropin-Releasing Hormone Test",
                    "a positive response, defined as an ACTH increase of 100% or a cortisol rise of 50% over baseline values, effectively eliminates a diagnosis of ectopic ACTH syndrome, which is the real benefit of this test.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Clinical Features of Cushing Syndrome",
                "Which finding best discriminates Cushing syndrome from simple obesity?",
                [
                    "Proximal myopathy and wide purple striae",
                    "Generalized obesity alone",
                    "Mild facial fullness only",
                    "Isolated weight gain without other features",
                ],
                0,
                "Proximal myopathy, bruising, wide livid striae, and facial plethora are among the most discriminatory features in Table 13.6.",
                ref(
                    "Clinical Features of Cushing Syndrome",
                    "Myopathy and bruising are two of the most discriminatory features of the syndrome.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Pituitary-Dependent Cushing Syndrome",
                "After transsphenoidal surgery for Cushing disease, day 3 cortisol is 25 nmol/L off hydrocortisone. Meaning?",
                [
                    "Likely remission with suppressed corticotrophs—continue glucocorticoid replacement",
                    "Surgical failure requiring immediate bilateral adrenalectomy",
                    "Normal outcome—stop all steroids immediately",
                    "Indicates ectopic ACTH recurrence",
                ],
                0,
                "Low postoperative cortisol after selective microadenoma removal reflects suppressed normal corticotrophs and expected remission requiring temporary replacement.",
                ref(
                    "Pituitary-Dependent Cushing Syndrome",
                    "After selective removal of a microadenoma, the surrounding corticotrophs are usually suppressed (Fig. 13.29). As a result, plasma cortisol levels are less than 30 nmol/L (<1 µg/dL) postoperatively, and ongoing glucocorticoid replacement therapy is required.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Autoimmune Adrenalitis",
                "A patient with new-onset Addison disease should also be screened for:",
                [
                    "Autoimmune thyroid disease and other polyglandular autoimmune conditions",
                    "Pheochromocytoma before any steroids",
                    "Medullary thyroid carcinoma with calcitonin",
                    "Growth hormone deficiency only",
                ],
                0,
                "About half of autoimmune Addison patients have associated autoimmune endocrinopathies, especially thyroid disease.",
                ref(
                    "Autoimmune Adrenalitis",
                    "Fifty percent of patients with this form of Addison disease have an associated autoimmune disease (Table 13.9), with thyroid disease being the most common.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Incidentalomas",
                "Mild autonomous cortisol excess (MACE) on dexamethasone testing in an incidentaloma patient is associated with:",
                [
                    "Higher rates of hypertension, diabetes, osteoporosis, and cardiovascular events",
                    "No metabolic consequences whatsoever",
                    "Mandatory immediate mitotane therapy",
                    "Diagnostic certainty of pheochromocytoma",
                ],
                0,
                "Low-grade biochemical hypercortisolism in incidentalomas correlates with cardiometabolic morbidity, though causality remains debated.",
                ref(
                    "Incidentalomas",
                    "When there is evidence of low-grade excess biochemical hypercortisolism, there is an associated increase in the prevalence of diabetes, obesity, hypertension, new cardiovascular events, osteoporosis, and fatality.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Long-Term Replacement Therapy",
                "A stable Addison patient on hydrocortisone 20 mg AM / 10 mg PM develops intercurrent gastroenteritis with vomiting. Advice?",
                [
                    "IM/IV hydrocortisone immediately and seek urgent care—do not rely on oral dosing",
                    "Skip steroids until vomiting resolves",
                    "Double fludrocortisone only",
                    "Switch to once-weekly dexamethasone",
                ],
                0,
                "Vomiting prevents oral replacement; parenteral hydrocortisone is mandatory during intercurrent illness.",
                ref(
                    "Treatment of Minor Febrile Illness or Stress",
                    "If the patient is vomiting and cannot take medication by mouth, parenteral hydrocortisone must be given urgently.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-t1",
                "Anatomy and Development",
                "The adult adrenal cortex zona fasciculata constitutes approximately 75% of cortical volume.",
                True,
                "Zona fasciculata is the largest cortical zone and produces glucocorticoids under ACTH.",
                ref(
                    "Anatomy and Development",
                    "The ZF makes up 75% of the cortex; cells are large and lipid laden and form radial cords within the fibrovascular radial network.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Adrenal Steroids and Steroidogenesis",
                "Mutations in adrenal steroidogenic enzymes can cause human disease.",
                True,
                "Enzyme defects underlie CAH and other inherited adrenal disorders.",
                ref(
                    "Adrenal Steroids and Steroidogenesis",
                    "Mutations in the genes encoding these enzymes result in human disease, so some understanding of the underlying pathways and steroid precursors is required.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Circadian Rhythm",
                "Random morning plasma cortisol alone is sufficient to diagnose Cushing syndrome.",
                False,
                "Morning cortisol may be normal in Cushing; circadian loss requires late-night or dynamic testing.",
                ref(
                    "Circadian Rhythm of Plasma Cortisol",
                    "Random morning plasma cortisol levels are therefore of little value in making the diagnosis, whereas a midnight cortisol level of greater than 200 nmol/L (>7.5 µg/dL) indicates Cushing syndrome.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Question 1: Does This Patient Have Cushing Syndrome?",
                "Urinary free cortisol can be normal in up to 8–15% of patients with Cushing syndrome.",
                True,
                "UFC is useful but not fully sensitive; abnormal screening should be confirmed with another test.",
                ref(
                    "Urinary Free Cortisol Excretion",
                    "although it is accepted that the value can be normal in up to 8% to 15% of patients with Cushing syndrome.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Imaging",
                "Adrenal imaging should be performed even when ACTH is suppressed and biochemistry suggests an adrenal source only after confirming undetectable ACTH.",
                True,
                "Incidental adrenal nodules are common; imaging must follow biochemical localization to avoid misclassification.",
                ref(
                    "CT/MRI Scanning of Pituitary and Adrenal Glands",
                    "adrenal imaging should not be performed unless biochemical investigation has suggested a primary adrenal cause (i.e., undetectable ACTH concentrations).",
                ),
            ),
            tf(
                f"{p}-t6",
                "Addison Disease",
                "Autoimmune adrenalitis accounts for more than 70% of acquired primary hypoadrenalism in Western countries.",
                True,
                "Anti-21-hydroxylase antibodies are detectable in most autoimmune cases.",
                ref(
                    "Autoimmune Adrenalitis",
                    "In the Western world, autoimmune adrenalis accounts for more than 70% of all cases of acquired primary hypoadrenalism.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Clinical Features of Adrenal Insufficiency",
                "Hyperkalemia is typical in secondary adrenal insufficiency.",
                False,
                "Hyperkalemia reflects aldosterone deficiency in primary disease; the RAA axis is intact in secondary insufficiency.",
                ref(
                    "Routine Biochemical Profile",
                    "Hyperkalemia occurs because of aldosterone deficiency, so it is usually absent in patients with secondary adrenal failure.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Assessing Adequacy of Function of the HPA Axis",
                "The short synacthen test should be used to diagnose central hypoadrenalism within 6 weeks of pituitary surgery.",
                False,
                "Residual adrenal responsiveness after pituitary insult can yield false-normal SST for 6 weeks.",
                ref(
                    "Assessing Adequacy of Function of the HPA Axis",
                    "the ACTH test should not be used to diagnose central hypoadrenalism in patients with a recent pituitary insult (e.g., surgery, apoplexy).",
                ),
            ),
            tf(
                f"{p}-t9",
                "21-Hydroxylase Deficiency",
                "Nonclassic 21-hydroxylase deficiency is more common than classic disease in population incidence.",
                True,
                "Nonclassic incidence is nearly 1 in 200 live births versus ~1 in 10,000–15,000 for classic disease.",
                ref(
                    "21-Hydroxylase Deficiency",
                    "Nonclassic 21-hydroxylase deficiency is more common, with an incidence of nearly 1 in 200 live births.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Classic 21-Hydroxylase Deficiency",
                "About 75% of patients with classic 21-hydroxylase deficiency have clinically significant mineralocorticoid deficiency.",
                True,
                "Salt-wasting crises commonly present after the second week of life if untreated.",
                ref(
                    "Classic 21-Hydroxylase Deficiency",
                    "About 75% of patients with classic 21-hydroxylase deficiency have concomitant, clinically manifested aldosterone deficiency and a strong propensity for salt wasting.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Incidentalomas",
                "Up to 10% of patients undergoing abdominal imaging may harbor an adrenal incidentaloma.",
                True,
                "Incidentalomas rise in frequency with age and are uncommon before age 30.",
                ref(
                    "Incidentalomas",
                    "An adrenal mass is uncovered in up to 10% of patients imaged for nonadrenal disease.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Carcinomas",
                "Primary adrenocortical carcinoma has an annual incidence of about 1 per 1 million population.",
                True,
                "Carcinoma is rare among incidentalomas but aggressive when present.",
                ref(
                    "Carcinomas",
                    "Primary adrenal carcinoma is very rare, with an annual incidence of 1 per 1 million population.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Cushing Syndrome",
                "Iatrogenic Cushing syndrome from prescribed glucocorticoids is common.",
                True,
                "Exogenous steroids are the most frequent cause of Cushing syndrome in clinical practice.",
                ref(
                    "Cushing Syndrome",
                    "Iatrogenic Cushing syndrome is common, occurring to some degree in most patients taking long-term corticosteroid therapy.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Anatomy and Development",
                "Assertion: The zona glomerulosa cannot synthesize cortisol.",
                "Reason: The zona glomerulosa does not express 17α-hydroxylase required for cortisol biosynthesis.",
                0,
                "Both statements are true and causally linked—lack of CYP17A1 confines ZG to mineralocorticoid pathways.",
                ref(
                    "Adrenal Steroids and Steroidogenesis",
                    "17α-Hydroxylation is an essential prerequisite for cortisol synthesis, and the ZG does not express 17α-hydroxylase.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Adrenal Steroids and Steroidogenesis",
                "Assertion: StAR mediates the rate-limiting step of adrenal steroidogenesis.",
                "Reason: StAR transports cholesterol into mitochondria before CYP11A1 action.",
                0,
                "Both true—StAR is ACTH-inducible and essential for mitochondrial cholesterol delivery.",
                ref(
                    "Adrenal Steroids and Steroidogenesis",
                    "Naturally occurring human mutations have confirmed the importance of a 30-kDa protein, steroidogenic acute regulatory protein (StAR), in mediating this effect.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Negative Feedback",
                "Assertion: Exogenous glucocorticoids can cause adrenal insufficiency after withdrawal.",
                "Reason: Glucocorticoids stimulate CRH and ACTH secretion.",
                2,
                "Assertion true; reason false—glucocorticoids inhibit, not stimulate, CRH and ACTH.",
                ref(
                    "Negative Feedback",
                    "Glucocorticoids inhibit POMC transcription in the anterior pituitary and CRH and AVP mRNA synthesis and secretion in the hypothalamus.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Question 1: Does This Patient Have Cushing Syndrome?",
                "Assertion: Late-night salivary cortisol is useful for screening Cushing syndrome.",
                "Reason: CBG is absent from saliva, reflecting free cortisol.",
                0,
                "Both true—salivary cortisol measures biologically active free hormone without hospitalization.",
                ref(
                    "Salivary Cortisol",
                    "CBG is absent from saliva, and the use of salivary cortisol measurements offers a sensible alternative in that the test does not require hospitalization.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Question 2: What Is the Cause of Cushing Syndrome in This Patient?",
                "Assertion: Ectopic ACTH syndrome often causes hypokalemic alkalosis.",
                "Reason: Ectopic ACTH secretion is usually associated with very high cortisol production rates that overwhelm renal 11βHSD2.",
                0,
                "Both true—mineralocorticoid excess from cortisol and DOC explains hypokalemia in ectopic disease.",
                ref(
                    "Metabolic and Endocrine Features",
                    "Hypokalemic alkalosis is found in 10% to 15% of patients with Cushing disease but in more than 95% of patients with ectopic ACTH syndrome.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Inferior Petrosal Sinus Sampling and Selective Venous Catheterization",
                "Assertion: IPSS can distinguish pituitary from ectopic ACTH sources.",
                "Reason: In ectopic ACTH syndrome the petrosal-to-peripheral ACTH ratio is usually less than 1.4:1.",
                0,
                "Both true—central-to-peripheral gradient rises in Cushing disease especially after CRH.",
                ref(
                    "Inferior Petrosal Sinus Sampling and Selective Venous Catheterization",
                    "In virtually all patients with the ectopic ACTH syndrome, the ratio of the ACTH concentration in the inferior petrosal sinus and that in simultaneously drawn peripheral venous blood is less than 1.4:1.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Primary and Central Hypoadrenalism",
                "Assertion: Mineralocorticoid replacement is required in primary but not secondary adrenal insufficiency.",
                "Reason: Secondary hypoadrenalism spares aldosterone secretion because the renin-angiotensin system remains intact.",
                0,
                "Both true—only ACTH-driven glucocorticoid production is lost centrally.",
                ref(
                    "Primary and Central Hypoadrenalism",
                    "A major distinction between these forms of hypoadrenalism is that mineralocorticoid deficiency invariably accompanies primary hypoadrenalism, but this does not occur in central hypoadrenalism: here, only ACTH is deficient, and the renin-angiotensin-aldosterone (RAA) axis is intact.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Clinical Features of Adrenal Insufficiency",
                "Assertion: Hyperpigmentation helps distinguish primary from secondary adrenal insufficiency.",
                "Reason: Hyperpigmentation in Addison disease results from elevated ACTH stimulating MC1R.",
                0,
                "Both true—pigmentation is absent in secondary ACTH deficiency.",
                ref(
                    "Clinical Features of Adrenal Insufficiency",
                    "The cause of the pigmentation has long been debated but is thought to reflect increased stimulation of the MC1R by ACTH itself.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Congenital Adrenal Hyperplasia",
                "Assertion: Classic 21-hydroxylase deficiency causes virilization of female infants.",
                "Reason: Androgen excess occurs because impaired cortisol synthesis removes negative feedback and increases ACTH-driven adrenal androgen production.",
                0,
                "Both true—enzyme block shunts precursors to androgens in utero.",
                ref(
                    "21-Hydroxylase Deficiency",
                    "Reduced cortisol biosynthesis results in a reduced negative feedback drive and increased ACTH secretion; as a consequence, adrenal androgens are produced in excess (Fig. 13.35).",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Classic 21-Hydroxylase Deficiency",
                "Assertion: Male infants with classic 21-hydroxylase deficiency may escape early diagnosis.",
                "Reason: Male external genitalia are phenotypically normal at birth in classic 21-hydroxylase deficiency.",
                0,
                "Both true—males present later with precocious pubarche unless newborn screening intervenes.",
                ref(
                    "Classic 21-Hydroxylase Deficiency",
                    "Males are phenotypically normal at birth and are at risk of not being diagnosed",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Incidentalomas",
                "Assertion: Large adrenal incidentalomas have higher malignancy risk.",
                "Reason: All adrenal masses smaller than 4 cm are malignant.",
                2,
                "Assertion true; reason false—malignancy is rare under 4 cm; risk rises above 6 cm.",
                ref(
                    "Incidentalomas",
                    "Fewer than 2% of incidentalomas smaller than 4 cm but 25% of those larger than 6 cm in diameter are malignant (Fig. 13.41).",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Corticosteroid Hormone Action",
                "Assertion: Cortisol can exert mineralocorticoid effects when 11βHSD2 is overwhelmed.",
                "Reason: 11βHSD2 converts cortisol to inactive cortisone in mineralocorticoid target tissues.",
                0,
                "Both true—ectopic ACTH and APPARENT mineralocorticoid excess illustrate this physiology.",
                ref(
                    "Corticosteroid-Binding Globulin and Corticosteroid Hormone Metabolism",
                    "If this enzyme-protective mechanism is impaired, cortisol is able to act as a mineralocorticoid; this explains some forms of endocrine hypertension (apparent mineralocorticoid excess, licorice ingestion) and the mineralocorticoid excess state that characterizes the ectopic ACTH syndrome.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "13",
        "title": "The Adrenal Cortex",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Richard J. Auchus, Christa E. Flück Pandey",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_13_The_Adrenal_Cortex.md",
        "items": items,
    }


MODULES = {OUT_NAME: build}


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
