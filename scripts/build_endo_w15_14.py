#!/usr/bin/env python3
"""Generate Williams 15e module w15-14 — Endocrine Hypertension."""
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
OUT_NAME = "w15-14_Endocrine_Hypertension.json"


def build() -> dict:
    p = "w15-14"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Endocrine hypertension scope",
                "Williams 15e ch14 covers at least 14 endocrine causes of hypertension—from catecholamine-secreting tumors and primary aldosteronism to Cushing syndrome, thyroid disease, and acromegaly—each offering a potential surgical cure or dramatic pharmacologic response.",
                ref(
                    "KEY POINTS",
                    "There are at least 14 endocrine disorders for which hypertension may be the initial clinical presentation.",
                ),
            ),
            note(
                f"{p}-n2",
                "Adrenal Medulla and Catecholamines",
                "How adrenergic receptor subtypes raise blood pressure",
                "Catecholamines increase heart rate, blood pressure, myocardial contractility, and cardiac conduction velocity through α, β, and dopaminergic G protein-coupled receptors with distinct subtypes mediating vascular, cardiac, and metabolic effects.",
                ref(
                    "Adrenal Medulla and Catecholamines",
                    "Catecholamines affect many cardiovascular and metabolic processes—they increase heart rate, blood pressure, myocardial contractility, and cardiac conduction velocity.",
                ),
            ),
            note(
                f"{p}-n3",
                "Catecholamine Synthesis",
                "Why epinephrine-secreting tumors localize to the adrenal medulla",
                "PNMT converts norepinephrine to epinephrine in the adrenal medulla; PNMT expression requires high local glucocorticoid concentrations from the corticomedullary portal system, so epinephrine-predominant neoplasms are almost exclusively adrenal.",
                ref(
                    "Catecholamine Synthesis",
                    "Therefore, catecholamine-secreting tumors that secrete primarily epinephrine are localized to the adrenal medulla.",
                ),
            ),
            note(
                f"{p}-n4",
                "Catecholamine Metabolism and Inactivation",
                "How COMT metabolism enables biochemical pheochromocytoma detection",
                "Intratumoral COMT O-methylates epinephrine to metanephrine and norepinephrine to normetanephrine continuously, so fractionated metanephrines in urine or plasma are more sensitive case-detection markers than episodic plasma catecholamines.",
                ref(
                    "Catecholamine Metabolism and Inactivation",
                    "Although COMT is found primarily outside neural tissue, O-methylation in the adrenal medulla is the predominant source of metanephrine (COMT converts epinephrine to metanephrine) and a major source of normetanephrine (COMT converts norepinephrine to normetanephrine) through methylation of the 3-hydroxy group.",
                ),
            ),
            note(
                f"{p}-n5",
                "Pheochromocytoma and Paraganglioma",
                "Why pheochromocytoma must be suspected despite rarity",
                "Annual incidence is 2–8 per million, yet detection matters because hypertension may be cured surgically, lethal paroxysms occur, ≥10% are malignant, and ~40% are familial with implications for relatives.",
                ref(
                    "Pheochromocytoma and Paraganglioma",
                    "Catecholamine-secreting tumors are rare, with an annual incidence of 2 to 8 cases per 1 million people.",
                ),
            ),
            note(
                f"{p}-n6",
                "Other Genetic Forms of Pheochromocytoma and Paraganglioma",
                "Pheochromocytoma genetic clusters",
                "Germline variants in ~20 genes account for ~40% of tumors; cluster 1 (hypoxia pathway, noradrenergic, often extra-adrenal), cluster 2 (kinase signaling, adrenergic, usually adrenal), and cluster 3 (Wnt signaling) guide genetic testing strategy.",
                ref(
                    "Other Genetic Forms of Pheochromocytoma and Paraganglioma",
                    "Mutations contributing to pheochromocytoma and paraganglioma have three general transcription signatures: cluster 1—genes encoding proteins that function in the cellular response to hypoxia; cluster 2—genes encoding proteins that activate kinase signaling; and cluster 3—genes in the Wnt-signaling group.",
                ),
            ),
            note(
                f"{p}-n7",
                "von Hippel-Lindau Disease",
                "Why MEN2 and VHL pheochromocytomas have distinct biochemical phenotypes",
                "MEN2-associated tumors overexpress PNMT and tyrosine hydroxylase, producing predominantly epinephrine and metanephrine; VHL tumors underexpress PNMT, yielding a noradrenergic (norepinephrine/normetanephrine) profile that directs genetic testing.",
                ref(
                    "von Hippel-Lindau Disease",
                    "Pheochromocytomas occurring in patients with MEN2 produce predominantly epinephrine and its major metabolite, metanephrine, whereas those occurring in patients with VHL syndrome produce predominantly norepinephrine and its major metabolite, normetanephrine.",
                ),
            ),
            note(
                f"{p}-n8",
                "Succinate Dehydrogenase Gene Mutations",
                "How SDHx mutations drive familial paraganglioma",
                "SDHB, SDHC, SDHD, SDHA, and SDHAF2 encode mitochondrial complex II; loss-of-function variants cause succinate accumulation, HIF stabilization, and predominantly extra-adrenal noradrenergic paragangliomas with high malignancy risk in SDHB.",
                ref(
                    "Succinate Dehydrogenase Gene Mutations",
                    "Most cases of familial paraganglioma are caused by pathogenic variants in the SDH (succinate:ubiquinone oxidoreductase) subunit genes (SDHB, SDHC, SDHD, SDHA, and SDHAF2), which make up portions of mitochondrial complex II.",
                ),
            ),
            note(
                f"{p}-n9",
                "Case Detection",
                "How to biochemically detect pheochromocytoma",
                "Diagnosis requires increased fractionated metanephrines and catecholamines in urine or plasma; 24-hour urine testing at Mayo has 98% sensitivity and specificity, while plasma metanephrines are reserved for high clinical suspicion because of higher false-positive rates.",
                ref(
                    "Measurement of Fractionated Metanephrines and Catecholamines in Urine and Plasma",
                    "The diagnosis must be confirmed biochemically by the presence of increased concentrations of fractionated metanephrines and catecholamines in urine or plasma (Fig. 14.4).",
                ),
            ),
            note(
                f"{p}-n10",
                "Localization",
                "Pheochromocytoma imaging localization",
                "After biochemical confirmation, CT or MRI of abdomen and pelvis is first-line (>95% sensitivity); ~85% of tumors are adrenal and 95% are in the abdomen/pelvis. Localization must not precede biochemistry.",
                ref(
                    "Localization",
                    "Localization studies should not be initiated until biochemical studies have confirmed the diagnosis of a catecholamine-secreting tumor (see Fig. 14.4).",
                ),
            ),
            note(
                f"{p}-n11",
                "Preoperative Management",
                "How to sequence alpha- and beta-blockade before pheochromocytoma surgery",
                "All patients need preoperative preparation—even if normotensive. Start α-blockade 7–10 days before surgery with sodium loading; only after adequate α-blockade add β-blockade to control tachycardia—never β-blockade alone, which risks unopposed α-mediated hypertensive crisis.",
                ref(
                    "Preoperative Management",
                    "The β-adrenergic antagonist should be administered only after α-adrenergic blockade is effective because with β-adrenergic blockade alone, severe hypertension or cardiopulmonary decompensation may occur as a result of the unopposed α-adrenergic stimulation.",
                ),
            ),
            note(
                f"{p}-n12",
                "Anesthesia and Surgery",
                "Pheochromocytoma surgical principles",
                "Resection is high-risk and requires an experienced team; laparoscopic adrenalectomy is preferred for solitary adrenal tumors <8 cm. Avoid fentanyl, ketamine, morphine, and metoclopramide perioperatively because they may stimulate catecholamine release.",
                ref(
                    "Anesthesia and Surgery",
                    "Surgical resection of a catecholamine-secreting tumor is a high-risk surgical procedure, and an experienced surgeon-anesthesiologist team is required.",
                ),
            ),
            note(
                f"{p}-n13",
                "Renin-Angiotensin-Aldosterone System",
                "Why 11βHSD2 confers mineralocorticoid receptor specificity",
                "Aldosterone is secreted from zona glomerulosa under angiotensin II, potassium, and ACTH; renal 11βHSD2 inactivates cortisol to cortisone so aldosterone can occupy mineralocorticoid receptors without cortisol acting as a mineralocorticoid.",
                ref(
                    "Aldosterone",
                    "Specificity of action is provided in many tissues by the presence of a glucocorticoid-inactivating enzyme, 11β-hydroxysteroid dehydrogenase 2 (11βHSD2), which prevents cortisol and corticosterone from interacting with the receptor (see Chapter 13).",
                ),
            ),
            note(
                f"{p}-n14",
                "Primary Aldosteronism",
                "How primary aldosteronism subtypes differ",
                "Hypertension with suppressed renin and increased aldosterone defines primary aldosteronism; aldosterone-producing adenoma (~30%) and bilateral idiopathic hyperaldosteronism (~60%) are most common, with somatic driver mutations in nearly all APAs.",
                ref(
                    "Primary Aldosteronism",
                    "Hypertension, suppressed plasma renin activity or plasma renin concentration, and increased aldosterone excretion characterize the syndrome of primary aldosteronism, which was first fully described in 1955.",
                ),
            ),
            note(
                f"{p}-n15",
                "Prevalence",
                "Why primary aldosteronism is underdiagnosed",
                "Older approaches requiring hypokalemia and drug washout found <0.5% prevalence; paired morning PAC and renin screening while on most antihypertensives now shows 5–10% of all hypertensives and ≥20% with resistant hypertension.",
                ref(
                    "Prevalence",
                    "Measurement of plasma aldosterone concentration (PAC) and renin (with PRA or PRC) as a case-detection test, followed by aldosterone suppression for confirmatory testing, has resulted in much higher prevalence estimates for primary aldosteronism—5% to 10% of all patients with hypertension.",
                ),
            ),
            note(
                f"{p}-n16",
                "Diagnosis",
                "How to stage primary aldosteronism diagnosis",
                "Workup proceeds in three phases: case-detection (morning PAC and renin/PRA), confirmatory aldosterone suppression testing, then subtype evaluation to distinguish unilateral from bilateral disease—72% of patients are normokalemic at presentation.",
                ref(
                    "Diagnosis",
                    "There is no typical clinical phenotype to guide the clinician for when to suspect primary aldosteronism—72% of patients with primary aldosteronism are normokalemic.",
                ),
            ),
            note(
                f"{p}-n17",
                "Case-Detection Tests",
                "How the aldosterone-renin ratio screens for primary aldosteronism",
                "Morning ambulatory PAC and PRA (or PRC) can be drawn on most antihypertensives; suppressed PRA (<1 ng/mL/h) with elevated PAC (>10 ng/dL) raises suspicion, but confirmatory suppression testing is usually required before treatment.",
                ref(
                    "Case-Detection Tests",
                    "The PAC:PRA ratio, first proposed as a case-detection test for primary aldosteronism in 1981, is based on the concept of paired hormone measurements.",
                ),
            ),
            note(
                f"{p}-n18",
                "Confirmatory Tests",
                "How confirmatory aldosterone suppression works",
                "Positive ARR requires demonstration of inappropriate aldosterone secretion—oral sodium loading (urinary aldosterone >12 µg/24 h on high-sodium diet), IV saline infusion (PAC not suppressed <10 ng/dL), or alternatives when renin is suppressed and PAC >10 ng/dL.",
                ref(
                    "Confirmatory Tests",
                    "A positive case-detection test with PAC above 10 ng/dL and PRA below 1 ng/mL per hour is not diagnostic by itself, and (in the absence of spontaneous hypokalemia—see earlier discussion) primary aldosteronism should be confirmed by demonstration of inappropriate aldosterone secretion.",
                ),
            ),
            note(
                f"{p}-n19",
                "Adrenal Venous Sampling",
                "How AVS lateralizes primary aldosteronism",
                "AVS is the criterion standard when CT is equivocal: continuous cosyntropin infusion, cortisol-corrected aldosterone lateralization ratio >4:1 indicates unilateral disease (95% sensitivity, 98.6% specificity); CT alone misclassifies many patients.",
                ref(
                    "Adrenal Venous Sampling",
                    "AVS is the criterion standard test to distinguish between unilateral and bilateral disease in patients with primary aldosteronism.",
                ),
            ),
            note(
                f"{p}-n20",
                "Somatic Mutations in KCNJ5, ATP1A1, ATP2B3, CACNA1D, and CTNNB1 Genes",
                "KCNJ5 and other APA driver mutations",
                "Somatic KCNJ5 mutations occur in ~43–47% of APAs, causing channel depolarization and aldosterone hypersecretion; ATP1A1, ATP2B3, CACNA1D, and CTNNB1 account for additional sporadic APAs with distinct histology and imaging features.",
                ref(
                    "Somatic Mutations in KCNJ5, ATP1A1, ATP2B3, CACNA1D, and CTNNB1 Genes",
                    "In a meta-analysis including 13 studies with 1636 patients, the overall prevalence of somatic KCNJ5 mutations in patients with APAs was 43%.",
                ),
            ),
            note(
                f"{p}-n21",
                "Principles of Treatment",
                "Why aldosterone blockade matters beyond blood pressure",
                "Treatment targets hypertension, hypokalemia, cardiovascular damage, and nephrotoxicity; normalize circulating aldosterone or provide mineralocorticoid receptor blockade—not blood pressure alone—because aldosterone excess drives cardiorenal morbidity.",
                ref(
                    "Principles of Treatment",
                    "Normalization of blood pressure should not be the only goal. In addition to the kidney and colon, mineralocorticoid receptors are present in the heart, brain, and blood vessels.",
                ),
            ),
            note(
                f"{p}-n22",
                "Apparent Mineralocorticoid Excess Syndrome",
                "Why AME causes hypertension with low aldosterone",
                "11βHSD2 normally converts cortisol to inactive cortisone in renal mineralocorticoid target tissues; genetic deficiency or licorice inhibition lets cortisol activate the mineralocorticoid receptor, producing hypertension, hypokalemia, and suppressed renin and aldosterone.",
                ref(
                    "Apparent Mineralocorticoid Excess Syndrome",
                    "Apparent mineralocorticoid excess is the result of impaired activity of the microsomal enzyme 11βHSD2, which normally inactivates cortisol in the kidney by converting it to the inactive 11-keto compound, cortisone.",
                ),
            ),
            note(
                f"{p}-n23",
                "Cushing Syndrome",
                "How Cushing syndrome causes hypertension",
                "Hypertension occurs in 75–80% of Cushing syndrome from increased DOC (ACTH-dependent), enhanced pressor sensitivity, increased cardiac output, elevated angiotensinogen, and cortisol overwhelming 11βHSD2 at the mineralocorticoid receptor.",
                ref(
                    "Cushing Syndrome",
                    "Hypertension occurs in 75% to 80% of patients with Cushing syndrome (see Chapter 13).",
                ),
            ),
            note(
                f"{p}-n24",
                "Hyperthyroidism",
                "How hyperthyroidism raises blood pressure",
                "Excess thyroid hormone increases metabolic activity and catecholamine sensitivity, producing tachycardia, high cardiac output, decreased peripheral resistance, and elevated systolic pressure—initial management includes β-blockade while treating the underlying thyrotoxicosis.",
                ref(
                    "Hyperthyroidism",
                    "The initial management in patients with hypertension and hyperthyroidism includes use of a β-adrenergic blocker to treat hypertension, tachycardia, and tremor.",
                ),
            ),
            note(
                f"{p}-n25",
                "Hypothyroidism",
                "Hypothyroid hypertension",
                "Diastolic hypertension is threefold more common in hypothyroidism, driven by increased systemic vascular resistance and extracellular volume expansion; levothyroxine normalizes blood pressure in about one-third and improves it in most others.",
                ref(
                    "Hypothyroidism",
                    "The frequency of hypertension (usually diastolic) is increased threefold in hypothyroid patients and may account for as many as 1% of cases of diastolic hypertension in the general population.",
                ),
            ),
            note(
                f"{p}-n26",
                "Acromegaly",
                "Acromegaly-associated hypertension",
                "Hypertension occurs in 20–40% of acromegaly from sodium retention and volume expansion; curing excess GH is most effective, with somatostatin analogs or pegvisomant when surgery fails, and diuretics for residual hypertension.",
                ref(
                    "Acromegaly",
                    "Hypertension occurs in 20% to 40% of the patients with acromegaly and is associated with sodium retention and extracellular volume expansion (see Chapter 7).",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Clinical Presentation",
                "A 42-year-old man has episodic palpitations, headache, pallor, and diaphoresis lasting 15–20 minutes. Between spells he is normotensive. Best initial biochemical test?",
                [
                    "24-hour urine fractionated metanephrines and catecholamines (or plasma metanephrines if high suspicion)",
                    "Random plasma cortisol at 9 AM only",
                    "Serum aldosterone without renin",
                    "Abdominal CT before any biochemistry",
                ],
                0,
                "Pheochromocytoma must be confirmed biochemically before imaging; fractionated metanephrines are the preferred case-detection markers.",
                ref(
                    "Measurement of Fractionated Metanephrines and Catecholamines in Urine and Plasma",
                    "The diagnosis must be confirmed biochemically by the presence of increased concentrations of fractionated metanephrines and catecholamines in urine or plasma (Fig. 14.4).",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Clinical Presentation",
                "A patient with suspected pheochromocytoma is started on propranolol for tachycardia before alpha-blockade. What complication is most feared?",
                [
                    "Severe hypertension or cardiopulmonary decompensation from unopposed alpha stimulation",
                    "Immediate adrenal crisis from glucocorticoid suppression",
                    "Spuriously low metanephrines from beta-blockade",
                    "Hyperkalemia from mineralocorticoid antagonism",
                ],
                0,
                "Beta-blockade without prior alpha-blockade is dangerous in catecholamine excess.",
                ref(
                    "Preoperative Management",
                    "The β-adrenergic antagonist should be administered only after α-adrenergic blockade is effective because with β-adrenergic blockade alone, severe hypertension or cardiopulmonary decompensation may occur as a result of the unopposed α-adrenergic stimulation.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Genetic Testing",
                "Biochemical testing shows predominantly elevated normetanephrine with norepinephrine excess and bilateral adrenal masses in a 28-year-old. Which genetic syndrome should be prioritized?",
                [
                    "von Hippel-Lindau disease",
                    "MEN2A with RET mutation",
                    "21-hydroxylase deficiency",
                    "Glucocorticoid-remediable aldosteronism",
                ],
                0,
                "VHL-associated pheochromocytomas have a noradrenergic biochemical phenotype; MEN2 tumors are adrenergic (epinephrine/metanephrine predominant).",
                ref(
                    "von Hippel-Lindau Disease",
                    "Genetic testing for VHL syndrome should be considered for patients with bilateral noradrenergic (norepinephrine and normetanephrine predominant) pheochromocytoma, diagnosis of unilateral noradrenergic pheochromocytoma at a young age (e.g., ≤45 years), or pheochromocytoma/paraganglioma patients with co-phenotype disorders (e.g., retinal angioma).",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Succinate Dehydrogenase Gene Mutations",
                "A 35-year-old has a large extra-adrenal paraganglioma. SDHB germline mutation is found. What additional risk must be discussed?",
                [
                    "High risk of metastatic malignant disease compared with many other hereditary forms",
                    "Mandatory bilateral adrenalectomy for cure",
                    "No need for family screening because penetrance is low",
                    "Expected adrenergic (metanephrine-predominant) biochemistry",
                ],
                0,
                "Malignancy is common with SDHB-related disease; cluster 1 tumors are usually noradrenergic extra-adrenal paragangliomas.",
                ref(
                    "Long-Term Postoperative Follow-Up",
                    "Malignancy is rare in patients with MEN2 or VHL syndrome, but it is common in those with familial paraganglioma caused by pathogenic variants in SDHB.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Localization",
                "Biochemically confirmed pheochromocytoma: CT shows a 2.5-cm right adrenal mass with unenhanced attenuation 35 HU. Next step?",
                [
                    "Proceed with preoperative alpha- and beta-blockade and surgical resection—imaging phenotype is consistent with pheochromocytoma",
                    "Defer surgery because HU <40 always indicates benign adenoma",
                    "Start spironolactone and repeat CT in 1 year",
                    "Perform adrenal venous sampling for aldosterone lateralization",
                ],
                0,
                "Pheochromocytomas typically have attenuation >10 HU and marked enhancement; biochemical confirmation precedes resection.",
                ref(
                    "Imaging Phenotype",
                    "If an adrenal mass has an unenhanced CT attenuation of <10 HU, it cannot be a pheochromocytoma.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Preoperative Management",
                "A normotensive patient with biochemically proven adrenal pheochromocytoma is scheduled for laparoscopic adrenalectomy. Preoperative management?",
                [
                    "Alpha-blockade for 7–10 days with sodium loading, then beta-blockade if needed—preparation is indicated even if asymptomatic",
                    "No pharmacologic preparation because blood pressure is normal",
                    "Beta-blockade alone starting the morning of surgery",
                    "Immediate surgery without blockade to avoid orthostasis",
                ],
                0,
                "All patients with catecholamine-secreting tumors require preoperative pharmacologic preparation regardless of symptoms or blood pressure.",
                ref(
                    "Preoperative Management",
                    "Some form of preoperative pharmacologic preparation is indicated for all patients with catecholamine-secreting neoplasms, including those who are asymptomatic and normotensive.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Anesthesia and Surgery",
                "During pheochromocytoma resection the surgeon must avoid tumor capsule rupture because:",
                [
                    "Rupture can seed diffuse peritoneal implants even from apparently benign tumors",
                    "Rupture always causes permanent hypertension",
                    "Rupture invalidates postoperative metanephrine testing",
                    "Rupture mandates immediate bilateral adrenalectomy in all cases",
                ],
                0,
                "Capsule violation can convert a curable benign-appearing tumor into incurable peritoneal disease.",
                ref(
                    "Anesthesia and Surgery",
                    "Great care should be taken to avoid tumor capsule rupture—this can create incurable diffuse peritoneal disease implants from an apparent benign pheochromocytoma.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Case-Detection Tests",
                "A 55-year-old with resistant hypertension on four drugs has normal serum potassium. Screening for primary aldosteronism?",
                [
                    "Measure morning PAC and renin (PRA or PRC)—hypokalemia is not required for suspicion",
                    "Defer testing because potassium is normal—primary aldosteronism always causes hypokalemia",
                    "Order 24-hour urine cortisol as first-line screen",
                    "Start empiric amiloride without any biochemical testing",
                ],
                0,
                "Most patients with primary aldosteronism are normokalemic; resistant hypertension is a guideline-indicated screening scenario.",
                ref(
                    "Diagnosis",
                    "There is no typical clinical phenotype to guide the clinician for when to suspect primary aldosteronism—72% of patients with primary aldosteronism are normokalemic.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Case-Detection Tests",
                "Morning labs: PAC 18 ng/dL, PRA 0.3 ng/mL/h. Patient takes lisinopril. Best interpretation?",
                [
                    "Findings suggest primary aldosteronism; proceed to confirmatory aldosterone suppression testing",
                    "ACE inhibitor makes the diagnosis impossible—stop all workup",
                    "Elevated renin excludes primary aldosteronism",
                    "Diagnosis is confirmed—start unilateral adrenalectomy without further testing",
                ],
                0,
                "ARR is a case-detection tool; suppressed renin with elevated PAC warrants confirmatory testing. ACE inhibitors may elevate renin but low PRA on therapy still supports PA.",
                ref(
                    "Case-Detection Tests",
                    "It is critical for the clinician to recognize that the measurement of PAC and renin is only a case-detection tool, and most positive results should be followed by a confirmatory aldosterone suppression test to verify autonomous aldosterone production before treatment is initiated.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Confirmatory Tests",
                "After ARR positivity, oral sodium loading shows 24-hour urinary aldosterone 18 µg with urinary sodium 220 mEq. Interpretation?",
                [
                    "Confirms autonomous aldosterone secretion (cutoff >12 µg/24 h)",
                    "Excludes primary aldosteronism because sodium intake was adequate",
                    "Proves bilateral idiopathic hyperaldosteronism without further testing",
                    "Indicates secondary hyperaldosteronism from renovascular disease",
                ],
                0,
                "On high-sodium diet, urinary aldosterone >12 µg/24 h supports primary aldosteronism with 96% sensitivity and 93% specificity.",
                ref(
                    "Oral Sodium Loading Test",
                    "Urinary aldosterone excretion of more than 12 μg/24 hours in this setting is consistent with autonomous aldosterone secretion.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Subtype Studies",
                "Confirmed PA: CT shows bilateral nodularity and a 1.2-cm left adrenal nodule. Young patient wants curative surgery. Essential next test?",
                [
                    "Adrenal venous sampling to distinguish unilateral from bilateral aldosterone secretion",
                    "Immediate left adrenalectomy based on CT alone",
                    "Inferior petrosal sinus sampling",
                    "Plasma metanephrines only",
                ],
                0,
                "CT misclassifies many patients; AVS is essential when surgical cure is pursued and imaging is equivocal.",
                ref(
                    "Computed Tomography of the Adrenal Glands",
                    "Adrenal CT is not accurate in distinguishing between APA and IHA.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Adrenal Venous Sampling",
                "During AVS with cosyntropin, right adrenal vein PAC/cortisol is 45, left is 1.2, IVC is 3.0. Lateralization ratio (high:low)?",
                [
                    "37.5—consistent with unilateral right aldosterone excess (ratio >4)",
                    "0.03—consistent with bilateral hyperaldosteronism",
                    "15—indeterminate; repeat CT only",
                    "1.0—failed cannulation in both veins",
                ],
                0,
                "Cortisol-corrected aldosterone lateralization ratio >4 indicates unilateral disease with high sensitivity and specificity.",
                ref(
                    "Adrenal Venous Sampling",
                    "A cutoff point of more than 4:1 for this ratio is used to indicate unilateral aldosterone excess (see Fig. 14.12).",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Somatic Mutations in KCNJ5, ATP1A1, ATP2B3, CACNA1D, and CTNNB1 Genes",
                "A woman with PA has a 2.8-cm APA. Histology shows zona fasciculata-like cells. Most likely somatic driver?",
                [
                    "KCNJ5 mutation—associated with larger APAs and more common in women",
                    "CYP21A2 mutation causing salt wasting",
                    "RET proto-oncogene activating variant",
                    "VHL loss-of-function mutation",
                ],
                0,
                "KCNJ5 mutations are overrepresented in women and produce larger APAs with fasciculata-like histology.",
                ref(
                    "Somatic Mutations in KCNJ5, ATP1A1, ATP2B3, CACNA1D, and CTNNB1 Genes",
                    "KCNJ5 mutations were overrepresented in APAs from women compared with men (63% vs. 24%), and APAs with KCNJ5 mutations had larger lesional diameters than those without the mutation (2.7 cm vs. 1.7 cm, respectively).",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Surgical Treatment of Unilateral Primary Aldosteronism",
                "One week after laparoscopic adrenalectomy for APA, potassium is 5.8 mmol/L off supplements. Likely mechanism?",
                [
                    "Postoperative hypoaldosteronism from chronic suppression of the contralateral RAA axis",
                    "Spironolactone continuation despite instruction to stop",
                    "Undiagnosed pheochromocytoma recurrence",
                    "Expected permanent hyperaldosteronism requiring higher MRA dose",
                ],
                0,
                "Transient hypoaldosteronism and hyperkalemia occur after curative unilateral surgery; monitor potassium and use generous dietary sodium early postoperatively.",
                ref(
                    "Surgical Treatment of Unilateral Primary Aldosteronism",
                    "Because of the risk of temporary hypoaldosteronism due to chronic suppression of the RAA axis, serum potassium levels should be monitored weekly for 4 weeks after surgery, and a generous-sodium diet should be followed.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Pharmacologic Treatment",
                "A man with bilateral IHA refuses surgery. Best long-term therapy to address aldosterone-mediated cardiorenal risk?",
                [
                    "Mineralocorticoid receptor antagonist (spironolactone or eplerenone) titrated to normalize potassium and raise renin",
                    "Calcium channel blocker alone without MRA",
                    "High-dose thiazide without MRA to avoid gynecomastia",
                    "Physiologic glucocorticoid replacement only",
                ],
                0,
                "IHA requires lifelong MRA; target high-normal potassium and PRA >1 ng/mL/h to ensure adequate receptor blockade.",
                ref(
                    "Pharmacologic Treatment",
                    "IHA and GRA should be treated medically. In addition, although not optimal, APA may be treated medically if therapy includes mineralocorticoid receptor blockade.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Familial Hyperaldosteronism Type III—Germline KCNJ5 Mutations",
                "A 9-year-old presents with severe hypertension, hypokalemia, and marked PA. Family history negative. Consider:",
                [
                    "Germline KCNJ5 mutation (familial hyperaldosteronism type III) with possible need for bilateral adrenalectomy",
                    "Factitious licorice ingestion only",
                    "Renin-secreting juxtaglomerular cell tumor",
                    "Subclinical hyperthyroidism as sole explanation",
                ],
                0,
                "Germline KCNJ5 variants cause severe childhood PA; many require bilateral adrenalectomy.",
                ref(
                    "Familial Hyperaldosteronism Type III—Germline KCNJ5 Mutations",
                    "Most patients with germline KCNJ5 pathogenic variants present with polyuria, polydipsia, and refractory hypertension in childhood—investigations show marked hypokalemia and marked primary aldosteronism.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Apparent Mineralocorticoid Excess Syndrome",
                "A child has hypertension, hypokalemia, low renin and aldosterone, and normal serum cortisol. Parents use herbal teas daily. Next step?",
                [
                    "Detailed history for glycyrrhizic acid (licorice) ingestion and urinary cortisol/cortisone metabolite ratio",
                    "Immediate bilateral adrenalectomy",
                    "High-dose dexamethasone suppression to diagnose Cushing disease",
                    "Measure plasma metanephrines first",
                ],
                0,
                "Acquired AME from licorice blocks 11βHSD2; congenital AME shows elevated urinary cortisol/cortisone ratio.",
                ref(
                    "Apparent Mineralocorticoid Excess Syndrome",
                    "Decreased 11βHSD2 activity may be hereditary, or it may be secondary to pharmacologic inhibition of enzyme activity by metabolites of glycyrrhizic acid, the active principle of licorice root (Glycyrrhiza glabra).",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Cushing Syndrome",
                "A patient with ectopic ACTH syndrome has severe hypertension and hypokalemic alkalosis. Major contributor to mineralocorticoid effect?",
                [
                    "Cortisol overwhelming renal 11βHSD2 plus elevated DOC from ACTH drive",
                    "Primary aldosteronism from adrenal adenoma",
                    "Excess TSH stimulating thyroid hormone receptors",
                    "Isolated 17α-hydroxylase deficiency",
                ],
                0,
                "Massive cortisol secretion can activate mineralocorticoid receptors when 11βHSD2 is saturated; DOC excess also contributes in ACTH-dependent disease.",
                ref(
                    "Apparent Mineralocorticoid Excess Syndrome",
                    "In addition, when 11βHSD2 is overwhelmed by massive cortisol hypersecretion associated with Cushing syndrome due to ectopic ACTH syndrome, hypokalemic hypertension may be one of the outcomes.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Hyperthyroidism",
                "A 38-year-old with Graves disease has systolic hypertension and resting heart rate 115/min while awaiting definitive therapy. Initial antihypertensive approach?",
                [
                    "Beta-adrenergic blocker for blood pressure, tachycardia, and tremor",
                    "Spironolactone as first-line for systolic hypertension",
                    "Alpha-blockade before any beta-blocker regardless of indication",
                    "Avoid all antihypertensives until euthyroid for 6 months",
                ],
                0,
                "Thyrotoxicosis increases catecholamine sensitivity; beta-blockers provide symptomatic cardiovascular control pending cause-specific treatment.",
                ref(
                    "Hyperthyroidism",
                    "The initial management in patients with hypertension and hyperthyroidism includes use of a β-adrenergic blocker to treat hypertension, tachycardia, and tremor.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Hypothyroidism",
                "A 50-year-old with new diastolic hypertension has TSH 28 mU/L. After levothyroxine replacement, blood pressure improves. Mechanism of initial hypertension?",
                [
                    "Increased systemic vascular resistance and extracellular volume expansion",
                    "Catecholamine-secreting thyroid medullary tumor",
                    "Primary hyperaldosteronism unmasked by hypothyroidism",
                    "Renin-secreting renal carcinoma",
                ],
                0,
                "Hypothyroidism commonly causes diastolic hypertension through hemodynamic and volume mechanisms reversible with thyroid replacement.",
                ref(
                    "Hypothyroidism",
                    "The mechanisms for the elevation in blood pressure include increased systemic vascular resistance and extracellular volume expansion.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Acromegaly",
                "A patient with active acromegaly has hypertension despite low-dose ACE inhibitor. Most effective long-term blood pressure strategy?",
                [
                    "Treat the growth hormone excess (surgery or medical GH suppression) rather than adding agents alone",
                    "Bilateral adrenalectomy for presumed occult APA",
                    "Licorice-containing supplements to raise blood pressure further",
                    "Immediate renal denervation before any pituitary evaluation",
                ],
                0,
                "Acromegaly hypertension links to sodium retention and volume expansion; curing or suppressing GH excess is most effective.",
                ref(
                    "Acromegaly",
                    "The hypertension of acromegaly is treated most effectively by curing the excess of growth hormone.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Differential Diagnosis",
                "Most patients tested for pheochromocytoma because of spells do not have the tumor. Critical pitfall when metanephrines are mildly elevated on tricyclic antidepressants?",
                [
                    "Medication interference—taper TCAs ≥2 weeks before hormonal assessment when feasible",
                    "Proceed directly to adrenalectomy without imaging",
                    "Assume panic disorder and never retest",
                    "Use plasma cortisol suppression as sole confirmatory test",
                ],
                0,
                "Many drugs elevate catecholamines/metanephrines; tricyclic antidepressants are the most frequent interferers with urinary testing.",
                ref(
                    "Differential Diagnosis",
                    "To effectively screen for catecholamine-secreting tumors, treatment with tricyclic antidepressants and other psychoactive agents listed in Box 14.4 should be tapered and discontinued at least 2 weeks before any hormonal assessments.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Long-Term Postoperative Follow-Up",
                "Benign pheochromocytoma resected 2 weeks ago: 24-hour urine metanephrines remain elevated. Management?",
                [
                    "Evaluate for residual tumor, second primary, or metastatic disease—levels should normalize after complete resection",
                    "Discharge with no follow-up because hypertension resolved intraoperatively",
                    "Start fludrocortisone for mineralocorticoid deficiency",
                    "Repeat surgery immediately without biochemical localization",
                ],
                0,
                "Persistent postoperative elevation indicates incomplete resection or additional tumor; lifelong biochemical surveillance is recommended.",
                ref(
                    "Long-Term Postoperative Follow-Up",
                    "Increased levels of fractionated catecholamines and metanephrines detected postoperatively are consistent with residual tumor (i.e., a second primary lesion or occult metastases).",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Case-Detection Tests",
                "A patient on spironolactone for heart failure has PAC 14 ng/dL and suppressed PRA. How should this affect PA workup?",
                [
                    "If renin remains suppressed on MRA, PA evaluation (including confirmatory testing and AVS) can proceed",
                    "Spironolactone always makes testing impossible—stop forever",
                    "Elevated PAC on spironolactone always indicates adequate MRA dosing—no PA",
                    "Switch to licorice tea to stimulate renin before testing",
                ],
                0,
                "If hypokalemic despite MRA, receptors are not fully blocked; suppressed renin still supports PA and permits continued evaluation.",
                ref(
                    "Case-Detection Tests",
                    "For example, if the patient is hypokalemic despite treatment with spironolactone or eplerenone, then the mineralocorticoid receptors are not fully blocked, and PRA or PRC should be suppressed in such a patient with primary aldosteronism.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "11β-Hydroxylase Deficiency",
                "An adolescent girl has hypertension, hypokalemia, low renin and aldosterone, acne, and virilization. Most likely diagnosis?",
                [
                    "11β-hydroxylase deficiency CAH with DOC excess",
                    "Classic 21-hydroxylase salt-wasting CAH without hypertension",
                    "Pheochromocytoma with MEN2A",
                    "Primary hyperparathyroidism",
                ],
                0,
                "11β-hydroxylase deficiency impairs cortisol synthesis and causes DOC-mediated hypertension with low renin and aldosterone.",
                ref(
                    "11β-Hydroxylase Deficiency",
                    "The impaired conversion of DOC to corticosterone results in high levels of DOC and 11-deoxycortisol; the substrate mass effect results in increased levels of adrenal androgens.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Pheochromocytoma in Pregnancy",
                "Pregnant woman with biochemically confirmed pheochromocytoma diagnosed in the second trimester after alpha-blockade. Preferred imaging and timing of surgery?",
                [
                    "MRI without gadolinium; adrenalectomy in second trimester or after elective Cesarean if later",
                    "CT with contrast and immediate surgery in first trimester",
                    "68Ga-DOTATATE PET/CT before any medical therapy",
                    "Defer all treatment until after delivery regardless of severity",
                ],
                0,
                "MRI without gadolinium is preferred in pregnancy; alpha-blockade improves outcomes; antepartum surgery in the second trimester is an option.",
                ref(
                    "Pheochromocytoma in Pregnancy",
                    "MRI (without gadolinium enhancement) is the preferred imaging modality, and 123I-MIBG scintigraphy and 68Ga-DOTATATE PET/CT are contraindicated.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-t1",
                "KEY POINTS",
                "Approximately 40% of catecholamine-secreting tumors are familial.",
                True,
                "Germline pathogenic variants explain a large minority of pheochromocytoma/paraganglioma and mandate genetic counseling.",
                ref(
                    "KEY POINTS",
                    "40% of these tumors are familial, and their detection in the proband may result in early diagnosis in other family members.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Catecholamine Synthesis",
                "Metyrosine inhibits tyrosine hydroxylase and may reduce tumoral catecholamine synthesis.",
                True,
                "Alpha-methyl-paratyrosine blocks the rate-limiting step in catecholamine synthesis.",
                ref(
                    "Catecholamine Synthesis",
                    "α-Methyl-paratyrosine (metyrosine) is a tyrosine hydroxylase inhibitor that may be used therapeutically in patients with catecholamine-secreting neoplasms to decrease tumoral synthesis of catecholamines.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Clinical Presentation",
                "Flushing is a typical hallmark symptom of pheochromocytoma spells.",
                False,
                "Flushing is listed among findings not typical of pheochromocytoma; pallor and diaphoresis are more characteristic spell features.",
                ref(
                    "Clinical Presentation",
                    "However, the clinician must recognize that most patients with spells do not have a pheochromocytoma (Box 14.3).",
                ),
            ),
            tf(
                f"{p}-t4",
                "Genetic Testing",
                "Genetic testing should be discussed with all patients who have pathology-confirmed pheochromocytoma or paraganglioma.",
                True,
                "Hereditary syndromes are common enough that universal discussion of genetic testing is recommended.",
                ref(
                    "Genetic Testing",
                    "Genetic testing should be considered and discussed with all patients who have pathology-confirmed pheochromocytoma or paraganglioma.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Localization",
                "An adrenal mass with unenhanced CT attenuation <10 HU can still be a pheochromocytoma.",
                False,
                "Very low attenuation indicates lipid-rich benign cortical adenoma; pheochromocytomas have higher HU values.",
                ref(
                    "Imaging Phenotype",
                    "If an adrenal mass has an unenhanced CT attenuation of <10 HU, it cannot be a pheochromocytoma.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Preoperative Management",
                "Preoperative alpha-adrenergic blockade should be started 7 to 10 days before surgery.",
                True,
                "Adequate alpha-blockade normalizes blood pressure and expands contracted volume before beta-blockade and surgery.",
                ref(
                    "Preoperative Management",
                    "α-Adrenergic blockade should be started 7 to 10 days preoperatively to normalize blood pressure and expand the contracted blood volume.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Primary Aldosteronism",
                "Somatic mutations account for nearly all aldosterone-producing adenomas.",
                True,
                "Driver mutations in KCNJ5, ATPases, CACNA1D, and CTNNB1 explain the majority of APAs.",
                ref(
                    "Primary Aldosteronism",
                    "Somatic mutations account for nearly all aldosterone-producing adenomas and include pathogenic variants in genes encoding components of the potassium channel (KCNJ5), the sodium/potassium and calcium adenosine triphosphatases (ATPases) (ATP1A1 and ATP2B3), a voltage-dependent C-type calcium channel (CACNA1D), and β-catenin-activating CTNNB1.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Prevalence",
                "Primary aldosteronism affects at least 20% of patients with resistant hypertension in modern screening studies.",
                True,
                "Case-detection with PAC and renin followed by confirmatory testing reveals much higher prevalence than historic hypokalemia-based approaches.",
                ref(
                    "KEY POINTS",
                    "Use of morning blood levels of aldosterone and renin as a case-detection test, followed by aldosterone suppression for confirmatory testing, has resulted in prevalence estimates for primary aldosteronism of 5% to 10% of all patients with hypertension and at least 20% in those with resistant hypertension.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Subtype Studies",
                "Adrenal CT alone is sufficient to direct surgery in most patients with primary aldosteronism.",
                False,
                "CT accuracy is only ~53% in some series; AVS is essential when surgical cure is pursued and imaging is equivocal.",
                ref(
                    "Computed Tomography of the Adrenal Glands",
                    "In a study of 203 patients with primary aldosteronism who were evaluated with both CT and AVS, CT was accurate in only 53% of patients",
                ),
            ),
            tf(
                f"{p}-t10",
                "Apparent Mineralocorticoid Excess Syndrome",
                "Patients with apparent mineralocorticoid excess typically have elevated plasma aldosterone.",
                False,
                "AME presents with low renin and low aldosterone because cortisol activates the mineralocorticoid receptor.",
                ref(
                    "Apparent Mineralocorticoid Excess Syndrome",
                    "The clinical phenotype of patients with apparent mineralocorticoid excess due to congenital deficiency of or inhibition of 11βHSD2 includes hypertension, hypokalemia, metabolic alkalosis, low renin, low aldosterone, and normal plasma cortisol levels.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Cushing Syndrome",
                "Endogenous Cushing disease is common, affecting more than 1% of the population.",
                False,
                "Endogenous Cushing is rare (<1 per million per year); iatrogenic glucocorticoid excess is relatively common.",
                ref(
                    "Cushing Syndrome",
                    "However, endogenous Cushing disease is rare, with an incidence of less than 1 case per 1 million people per year.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Renin-Secreting Tumor",
                "Renin-secreting tumors typically present with hypertension, hypokalemia, high aldosterone, and elevated renin.",
                True,
                "Juxtaglomerular cell tumors cause secondary hyperaldosteronism with renin-driven aldosterone excess.",
                ref(
                    "Renin-Secreting Tumor",
                    "These juxtaglomerular cell tumors typically present with secondary hyperaldosteronism (hypertension, hypokalemia, high PAC, and elevated renin) in young adults.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Multiple Endocrine Neoplasia Type 2A",
                "Pheochromocytoma occurs in approximately 50% of patients with MEN2A.",
                True,
                "MEN2A features MTC in all patients and adrenergic pheochromocytoma in about half, often bilateral.",
                ref(
                    "Multiple Endocrine Neoplasia Type 2A",
                    "MEN2A is characterized by medullary thyroid cancer (MTC) in all patients, adrenergic (epinephrine and metanephrines are predominant) pheochromocytoma in 50% (usually bilateral and frequently asynchronous), primary hyperparathyroidism in 20%",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Catecholamine Synthesis",
                "Assertion: Epinephrine-secreting catecholamine tumors are almost always adrenal.",
                "Reason: PNMT expression in chromaffin cells depends on high local glucocorticoid concentrations from the corticomedullary portal system.",
                0,
                "Both true and causally linked—PNMT converts norepinephrine to epinephrine only where cortisol exposure is high.",
                ref(
                    "Catecholamine Synthesis",
                    "PNMT expression is regulated by the presence of glucocorticoids, which are in high concentration in the adrenal medulla through the corticomedullary portal system.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Catecholamine Metabolism and Inactivation",
                "Assertion: Fractionated metanephrines are preferred biochemical markers for pheochromocytoma case detection.",
                "Reason: Metanephrines are formed continuously by intratumoral COMT O-methylation of catecholamines.",
                0,
                "Both true—continuous intratumoral metabolism improves sensitivity over episodic catecholamine measurement.",
                ref(
                    "Case Detection",
                    "The metabolism of catecholamines is primarily intratumoral, with formation of metanephrine from epinephrine and normetanephrine from norepinephrine.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Preoperative Management",
                "Assertion: Beta-adrenergic blockers should not be started before effective alpha-blockade in pheochromocytoma.",
                "Reason: Alpha-adrenergic blockade causes severe bradycardia if started after beta-blockade.",
                2,
                "Assertion true; reason false—the danger of beta-first therapy is unopposed alpha-mediated vasoconstriction and hypertensive crisis, not bradycardia from alpha-blockade.",
                ref(
                    "Preoperative Management",
                    "The β-adrenergic antagonist should be administered only after α-adrenergic blockade is effective because with β-adrenergic blockade alone, severe hypertension or cardiopulmonary decompensation may occur as a result of the unopposed α-adrenergic stimulation.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "von Hippel-Lindau Disease",
                "Assertion: Biochemical phenotype can guide genetic testing in hereditary pheochromocytoma.",
                "Reason: MEN2 tumors are noradrenergic whereas VHL tumors are adrenergic.",
                2,
                "Assertion true; reason false—the phenotypes are reversed—MEN2 is adrenergic (epinephrine/metanephrine) and VHL is noradrenergic.",
                ref(
                    "von Hippel-Lindau Disease",
                    "Pheochromocytomas occurring in patients with MEN2 produce predominantly epinephrine and its major metabolite, metanephrine, whereas those occurring in patients with VHL syndrome produce predominantly norepinephrine and its major metabolite, normetanephrine.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Prevalence",
                "Assertion: Primary aldosteronism is more common than historically recognized.",
                "Reason: Most patients with primary aldosteronism are not hypokalemic, and screening can be done on antihypertensive therapy.",
                0,
                "Both true—normokalemia and modern ARR screening explain higher detected prevalence.",
                ref(
                    "Prevalence",
                    "However, it is now recognized that most patients with primary aldosteronism are not hypokalemic and that screening can be completed while the patient is taking antihypertensive drugs.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Case-Detection Tests",
                "Assertion: The PAC:PRA ratio is useful for case detection of primary aldosteronism.",
                "Reason: A suppressed PRA with elevated PAC suggests autonomous aldosterone secretion.",
                0,
                "Both true—paired hormone measurement forms the basis of ARR screening before confirmatory testing.",
                ref(
                    "Case-Detection Tests",
                    "Primary aldosteronism should be suspected if PRA is suppressed (e.g., <1.0 ng/mL per hour) and PAC is increased (e.g., >10 ng/dL) (see Fig. 14.9).",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Adrenal Venous Sampling",
                "Assertion: AVS is superior to adrenal CT for lateralizing aldosterone secretion.",
                "Reason: CT accurately lateralizes disease in more than 90% of patients with primary aldosteronism.",
                2,
                "Assertion true; reason false—CT misclassifies many patients; AVS lateralization ratio >4 has ~95% sensitivity.",
                ref(
                    "Computed Tomography of the Adrenal Glands",
                    "In a study of 203 patients with primary aldosteronism who were evaluated with both CT and AVS, CT was accurate in only 53% of patients",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Somatic Mutations in KCNJ5, ATP1A1, ATP2B3, CACNA1D, and CTNNB1 Genes",
                "Assertion: KCNJ5 mutations are a common somatic cause of aldosterone-producing adenomas.",
                "Reason: KCNJ5 variants depolarize glomerulosa cells and trigger aldosterone production and proliferation.",
                0,
                "Both true—channel mutations are the most frequent APA drivers in meta-analyses.",
                ref(
                    "Familial Hyperaldosteronism Type III—Germline KCNJ5 Mutations",
                    "This KCNJ5 pathogenic variant produces increased sodium conductance and cell depolarization, triggering calcium entry into glomerulosa cells, the signal for aldosterone production and cell proliferation.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Apparent Mineralocorticoid Excess Syndrome",
                "Assertion: Apparent mineralocorticoid excess can cause hypertension with low aldosterone.",
                "Reason: 11βHSD2 normally inactivates cortisol to cortisone in the kidney.",
                0,
                "Both true—when 11βHSD2 is deficient, cortisol acts as a mineralocorticoid despite normal aldosterone levels.",
                ref(
                    "Apparent Mineralocorticoid Excess Syndrome",
                    "Cortisol can be a potent mineralocorticoid, and when 11βHSD2 is genetically deficient or its activity blocked, high levels of cortisol accumulate in the kidney.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Cushing Syndrome",
                "Assertion: Hypertension is common in Cushing syndrome.",
                "Reason: Hypertension in Cushing syndrome never involves mineralocorticoid receptor activation.",
                2,
                "Assertion true; reason false—cortisol can activate mineralocorticoid receptors when 11βHSD2 is overwhelmed, especially in ectopic ACTH syndrome.",
                ref(
                    "Cushing Syndrome",
                    "The mechanisms of hypertension include increased production of DOC (in ACTH-dependent Cushing syndrome), enhanced pressor sensitivity to endogenous vasoconstrictors (e.g., epinephrine, angiotensin II), increased cardiac output, activation of the RAA system by increased hepatic production of angiotensinogen, and cortisol activation of the mineralocorticoid receptor.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Hyperthyroidism",
                "Assertion: Beta-blockers are useful in hypertensive hyperthyroid patients.",
                "Reason: Excess thyroid hormone increases sensitivity to circulating catecholamines.",
                0,
                "Both true—beta-blockade treats adrenergic symptoms while definitive thyroid therapy is undertaken.",
                ref(
                    "Hyperthyroidism",
                    "When excessive amounts of circulating thyroid hormones interact with thyroid hormone receptors on peripheral tissues, both metabolic activity and sensitivity to circulating catecholamines increase.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Acromegaly",
                "Assertion: Treating growth hormone excess improves hypertension in acromegaly.",
                "Reason: Acromegaly-associated hypertension is linked to sodium retention and extracellular volume expansion.",
                0,
                "Both true—volume-mediated hypertension responds best to curing or suppressing GH excess.",
                ref(
                    "Acromegaly",
                    "Hypertension occurs in 20% to 40% of the patients with acromegaly and is associated with sodium retention and extracellular volume expansion (see Chapter 7).",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "14",
        "title": "Endocrine Hypertension",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "William F. Young Jr.",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_14_Endocrine_Hypertension.md",
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
