#!/usr/bin/env python3
"""Generate Williams 15e module w15-08 — Posterior Pituitary."""
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
OUT_NAME = "w15-08_Posterior_Pituitary.json"


def build() -> dict:
    p = "w15-08"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Anatomy",
                "Neurohypophysis structure and blood supply",
                "The posterior pituitary is neural tissue consisting only of distal axon terminals of hypothalamic magnocellular neurons. Perikarya lie in paired paraventricular and supraoptic nuclei; the posterior pituitary is supplied directly from inferior hypophyseal arteries rather than the hypothalamic–pituitary portal system.",
                ref(
                    "Anatomy",
                    "The posterior pituitary is neural tissue and consists only of the distal axons of the hypothalamic magnocellular neurons that make up the neurohypophysis.",
                ),
            ),
            note(
                f"{p}-n2",
                "Anatomy",
                "Why SON and PVN differ in organization",
                "The supraoptic nucleus is relatively simple—80% to 90% of neurons produce AVP and virtually all axons project to the posterior pituitary—whereas the human paraventricular nucleus has five subnuclei with parvocellular divisions synthesizing CRH, TRH, somatostatin, and opioids in addition to magnocellular AVP/oxytocin neurons.",
                ref(
                    "Anatomy",
                    "The supraoptic nucleus (SON) is relatively simple, with 80% to 90% of the neurons producing AVP and virtually all axons projecting to the posterior pituitary.",
                ),
            ),
            note(
                f"{p}-n3",
                "Synthesis",
                "How copeptin is co-secreted with AVP",
                "AVP and oxytocin are synthesized as part of a precursor containing the nonapeptide, a hormone-specific neurophysin, and—for AVP—a 39-amino acid peptide named copeptin. The precursor is packaged in neurosecretory granules and cleaved during transport to the posterior pituitary.",
                ref(
                    "Synthesis and Release of Neurohypophyseal Hormones",
                    "The hormones are synthesized as part of a precursor molecule consisting of the nonapeptide and a hormone-specific neurophysin and, for AVP, a 39-amino acid peptide named copeptin.",
                ),
            ),
            note(
                f"{p}-n4",
                "Synthesis",
                "Desmopressin structural modifications",
                "Desmopressin differs from AVP in that the terminal cystine is deaminated and the arginine in position 8 is a D-isomer rather than an L-isomer. These changes markedly reduce pressor activity and increase half-life, producing an agent nearly 2000 times more specific for antidiuresis.",
                ref(
                    "Synthesis and Release of Neurohypophyseal Hormones",
                    "Desmopressin differs from AVP in that the terminal cystine is deaminated, and the arginine in position 8 is a D-isomer rather than an L-isomer.",
                ),
            ),
            note(
                f"{p}-n5",
                "Physiology",
                "Why osmotic AVP release is more sensitive than volume",
                "Plasma AVP is much more sensitive to changes in osmolality, responding to as little as a 1% increase, whereas a change of 10% to 15% or greater in volume or pressure is required to stimulate AVP release.",
                ref(
                    "Physiology of Secretion of AVP and Thirst",
                    "Plasma AVP is much more sensitive to changes in osmolality, responding to as little as a 1% increase, whereas a change of 10% to 15% or greater in volume or pressure is required to stimulate the release of AVP.",
                ),
            ),
            note(
                f"{p}-n6",
                "Physiology",
                "How OVLT osmoreceptors regulate AVP",
                "Primary osmoreceptors lie outside the blood–brain barrier in the organum vasculosum of the lamina terminalis. Surgical destruction of the OVLT abolishes AVP secretion and thirst responses to hyperosmolality but not to hypovolemia.",
                ref(
                    "Osmotic Regulation",
                    "Surgical destruction of the OVLT abolishes AVP secretion and thirst responses to hyperosmolality but not their responses to hypovolemia.",
                ),
            ),
            note(
                f"{p}-n7",
                "Physiology",
                "How V2 receptors insert aquaporin-2",
                "AVP binds V2 receptors on renal collecting duct principal cells, activating adenylate cyclase and protein kinase A, which phosphorylates aquaporin 2 and moves water channels into the luminal membrane; dissociation of AVP allows reinternalization and termination of antidiuresis.",
                ref(
                    "Osmotic Regulation",
                    "Binding activates adenylate cyclase, increasing cyclic adenosine monophosphate (cAMP), which then stimulates protein kinase A. This leads to phosphorylation and activation of aquaporin 2 and movement of the water channels into the luminal membrane.",
                ),
            ),
            note(
                f"{p}-n8",
                "Physiology",
                "Baroreceptor and volume regulation of AVP",
                "High-pressure baroreceptors are in the carotid sinus and aortic arch; low-pressure volume receptors are in the atria and pulmonary venous system. Afferent signals reach the brainstem via cranial nerves 9 and 10; when hypovolemia is sufficient to decrease blood pressure, there is an exponential increase in plasma AVP.",
                ref(
                    "Volume and Pressure Regulation",
                    "High-pressure arterial baroreceptors are located in the carotid sinus and aortic arch; low-pressure volume receptors are located in the atria and pulmonary venous system.",
                ),
            ),
            note(
                f"{p}-n9",
                "Physiology",
                "Why pregnancy resets the osmostat",
                "Major fluid shifts in normal pregnancy produce a fall in plasma osmolality of about 10 mmol/kg—the best physiologic example of a true resetting of the osmostat. The shift in osmotic threshold for AVP appears at about 5 to 8 weeks of gestation and persists throughout pregnancy.",
                ref(
                    "Effects of Pregnancy on Fluid Homeostasis",
                    "Major shifts of fluid during normal pregnancy produce a fall in plasma osmolality of about 10 mmol/kg; this is the best physiologic example of a true resetting of the osmostat.",
                ),
            ),
            note(
                f"{p}-n10",
                "Physiology",
                "Oxytocinase and pregnancy-associated DI",
                "The placenta produces cysteine aminopeptidase (oxytocinase), equally potent in degrading oxytocin and AVP. Activity increases markedly around 20 weeks of gestation and further to 40 weeks, returning slowly to normal after delivery.",
                ref(
                    "Effects of Pregnancy on Fluid Homeostasis",
                    "In women, the placenta produces an enzyme, cysteine aminopeptidase, which is released into the plasma and is known as oxytocinase.",
                ),
            ),
            note(
                f"{p}-n11",
                "Aging",
                "Why elderly patients are vulnerable to dysnatremia",
                "Elderly subjects have lower nocturnal plasma AVP, prolonged desmopressin effect, decreased thirst with dehydration, and a collecting duct less responsive to AVP-stimulated aquaporin 2 insertion—predisposing to both hypernatremia and hyponatremia.",
                ref(
                    "Effects of Aging on Fluid Homeostasis",
                    "In older subjects there is a decrease in glomerular filtration rate, and the collecting duct in the aged kidney is less responsive to AVP-stimulated increases in aquaporin 2 water channels, thus limiting the ability to excrete free water.",
                ),
            ),
            note(
                f"{p}-n12",
                "Diabetes insipidus",
                "Diabetes insipidus definition and clinical features",
                "DI is characterized by excretion of large volumes of hypotonic, dilute, tasteless urine leading to polyuria and polydipsia—distinct from the hypertonic sweet urine of diabetes mellitus. CDI reflects deficient AVP secretion; NDI reflects decreased renal AVP effect.",
                ref(
                    "Diabetes Insipidus",
                    "DI is a clinical disorder that is characterized by the excretion of large volumes of urine (diabetes) that is hypotonic, dilute, and tasteless (i.e., insipid).",
                ),
            ),
            note(
                f"{p}-n13",
                "Diabetes insipidus",
                "Why sellar adenomas rarely cause CDI",
                "Pituitary adenomas almost never cause CDI to such an extent that if a patient presents with a pituitary mass and polyuria and polydipsia, it is safe to assume that he or she does not have a pituitary adenoma.",
                ref(
                    "Hypothalamic/Central Diabetes Insipidus",
                    "Pituitary adenomas almost never cause CDI to such an extent that if a patient presents with a pituitary mass and polyuria and polydipsia, it is safe to assume that he or she does not have a pituitary adenoma.",
                ),
            ),
            note(
                f"{p}-n14",
                "Diabetes insipidus",
                "How triphasic response follows pituitary stalk injury",
                "After complete stalk section: phase 1 is DI from axon shock (within 24 hours); phase 2 is antidiuretic unregulated AVP release (days 5–7) often causing hyponatremia; phase 3 is permanent CDI as damaged neurons gliose. Isolated phase 2 can occur without preceding or subsequent DI.",
                ref(
                    "Hypothalamic/Central Diabetes Insipidus",
                    "The first phase is DI, with onset within the first 24 hours of surgery, and is thought to be due to axon shock and the inability of action potentials to be propagated from the cell body to the neurons terminating in the posterior pituitary.",
                ),
            ),
            note(
                f"{p}-n15",
                "Diabetes insipidus",
                "Primary polydipsia and psychogenic causes",
                "Primary polydipsia may follow hypothalamic lesions, dry mouth from drugs, or psychiatric syndromes; in psychiatric hospitals up to 42% have some form of polydipsia. Habitual polydipsia is increasingly seen in health-conscious individuals voluntarily overdrinking.",
                ref(
                    "Diabetes Insipidus Due to Excess Fluid Intake (Primary Polydipsia)",
                    "However, most commonly there is no identifiable pathologic etiology; in this circumstance the disorder can be associated with psychiatric syndromes.",
                ),
            ),
            note(
                f"{p}-n16",
                "Diagnosis",
                "How the water deprivation test differentiates polyuria",
                "After adequate dehydration (plasma osmolality >295 mOsm/kg), urine should concentrate above 800 mOsm/kg in primary polydipsia; CDI shows little rise until desmopressin, which then concentrates urine; NDI shows minimal response to both endogenous AVP and desmopressin.",
                ref(
                    "Diabetes Insipidus",
                    "In primary polydipsia, urine should concentrate relatively normally because AVP secretion is normal, whereas in patients with either CDI or NDI the urine remains dilute until desmopressin is administered.",
                ),
            ),
            note(
                f"{p}-n17",
                "Diagnosis",
                "Why copeptin supplants direct AVP measurement",
                "Copeptin is co-secreted equimolarly with AVP, is stable ex vivo, and responds similarly to osmotic stimuli. A copeptin cutoff of 4.9 pmol/L after hypertonic saline infusion distinguished CDI from primary polydipsia with 96.5% accuracy—superior to the indirect water deprivation test.",
                ref(
                    "Diabetes Insipidus",
                    "An osmotically stimulated copeptin level of >4.9 pmol/L after infusion of 3% saline (aiming at a sodium level ≥150 mmol/L) had an overall diagnostic accuracy of 96.5% in distinguishing between patients with primary polydipsia and those with CDI.",
                ),
            ),
            note(
                f"{p}-n18",
                "Imaging",
                "Ectopic posterior pituitary bright spot",
                "T1-weighted MRI shows a bright signal in the normal posterior pituitary from stored AVP. When the bright spot is ectopic in the hypothalamic base, this indicates pituitary stalk interruption—often from traumatic delivery or pituitary embryogenesis transcription-factor defects.",
                ref(
                    "Ectopic Posterior Pituitary",
                    "With the development of magnetic resonance imaging (MRI) scans of the brain, it was discovered that T1-weighted images with MRI produced a bright signal in the posterior pituitary.",
                ),
            ),
            note(
                f"{p}-n19",
                "Treatment",
                "How desmopressin dosing balances polyuria and hyponatremia",
                "Desmopressin duration is typically 6–18 hours depending on route; maximum dose rarely exceeds 0.2 mg orally or 20 μg intranasally two to three times daily. Hyponatremia risk is reduced by omitting a weekly dose, delaying dose until polyuria returns, or delaying each dose until urination begins.",
                ref(
                    "Central Diabetes Insipidus in Ambulatory Patients",
                    "The total duration of action of desmopressin will usually be 6 to 18 hours, depending on the route of administration.",
                ),
            ),
            note(
                f"{p}-n20",
                "Treatment",
                "Why adipsic DI causes hypernatremia more than CDI",
                "Adipsic DI combines attenuated thirst with DI. Unlike CDI with intact thirst, 50% of ADI patients develop hypernatremia ambulatory and 20% develop severe hypernatremia when hospitalized; they are also vulnerable to hyponatremia when treated with desmopressin without fixed fluid intake.",
                ref(
                    "Adipsic Diabetes Insipidus",
                    "In contrast to CDI patients with intact thirst, 50% develop hypernatremia in ambulatory settings, and 20% develop severe hypernatremia when admitted to hospital.",
                ),
            ),
            note(
                f"{p}-n21",
                "Treatment",
                "How thiazides treat nephrogenic DI",
                "In congenital NDI, therapy goals are plasma volume contraction to decrease GFR, increased proximal tubular sodium and water reabsorption, and decreased fluid delivery to the collecting duct. Thiazide diuretics are the mainstay and can additionally increase aquaporin 2 independent of AVP.",
                ref(
                    "Treatment of Nephrogenic Diabetes Insipidus",
                    "Thiazide diuretics are the mainstay of treatment, and data show that these agents can additionally increase aquaporin 2 independent of AVP.",
                ),
            ),
            note(
                f"{p}-n22",
                "Treatment",
                "Lithium-induced nephrogenic DI mechanism",
                "Lithium is the commonest cause of acquired NDI. It reduces aquaporin 2 levels by as much as 95%, and even the remaining aquaporin 2 is not normally transported to the renal principal cell membrane; the defect is slow to correct and can be permanent.",
                ref(
                    "Nephrogenic Diabetes Insipidus",
                    "There is as much as a 95% decrease in aquaporin 2 content, and even the 5% of aquaporin 2 that persists is not normally transported to the renal principal cell membrane.",
                ),
            ),
            note(
                f"{p}-n23",
                "Treatment",
                "Why amiloride helps lithium-induced NDI",
                "Amiloride blocks sodium channels in the luminal membrane of collecting duct cells and inhibits lithium reabsorption—a unique advantage in treating lithium-induced NDI. Thiazide-induced volume contraction can decrease lithium excretion and predispose to toxicity.",
                ref(
                    "Treatment of Nephrogenic Diabetes Insipidus",
                    "The diuretic amiloride blocks sodium channels in the luminal membrane of the collecting duct cells and inhibits lithium reabsorption, a unique advantage in treating lithium-induced NDI.",
                ),
            ),
            note(
                f"{p}-n24",
                "SIAD",
                "SIAD definition and hallmark",
                "SIAD occurs when plasma AVP is elevated when physiologic secretion would normally be osmotically suppressed, leading to water retention and hypoosmolarity. The clinical hallmark is decreased effective osmolality of the ECF.",
                ref(
                    "KEY POINTS",
                    "The syndrome of inappropriate antidiuresis (SIAD) occurs when plasma levels of AVP are elevated at times when physiologic AVP secretion from the posterior pituitary would normally be osmotically suppressed, leading to water retention and hypoosmolarity.",
                ),
            ),
            note(
                f"{p}-n25",
                "SIAD",
                "How hyponatremia workup uses volume status and urine sodium",
                "In euvolemic hyponatremia, high urine [Na⁺] usually implies dilution-induced hypoosmolarity such as SIAD, whereas low urine [Na⁺] suggests depletion-induced hypoosmolarity from ECF losses replaced by hypotonic fluids. SIAD criteria include pOsm <275, inappropriately concentrated urine, euvolemia, and elevated urinary sodium on normal intake.",
                ref(
                    "Normal Extracellular Fluid Volume",
                    "A high urine [Na⁺] usually implies a distally mediated, dilution-induced hypoosmolarity, such as SIAD.",
                ),
            ),
            note(
                f"{p}-n26",
                "SIAD",
                "Why hypertonic saline is first-line for severe symptomatic hyponatremia",
                "In patients with severe neurologic symptoms and serum [Na⁺] below 125 mmol/L, prompt therapy with isotonic or hypertonic saline corrected sodium by ~20 mmol/L over days with neurologic recovery in almost all cases; fluid restriction alone corrected <5 mmol/L over 72 hours with much worse outcomes.",
                ref(
                    "General Principles",
                    "In a retrospective review of patients who presented with severe neurologic symptoms and serum [Na⁺] below 125 mmol/L, prompt therapy with isotonic or hypertonic saline resulted in a correction in the range of 20 mmol/L over several days and neurologic recovery in almost all cases.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Anatomy",
                "A 6-year-old boy with septal optic dysplasia has growth failure and polyuria. MRI shows the posterior pituitary bright spot at the base of the hypothalamus rather than in the sella. Which finding best explains this imaging pattern?",
                [
                    "Ectopic posterior pituitary from pituitary stalk interruption",
                    "Craniopharyngioma compressing the infundibulum",
                    "Nonfunctioning pituitary macroadenoma",
                    "Lymphocytic adenohypophysitis with stalk thickening only",
                ],
                0,
                "Ectopic bright spot in the hypothalamic base indicates pituitary stalk interruption, often with embryogenesis defects and associated anterior pituitary deficiency.",
                ref(
                    "Ectopic Posterior Pituitary",
                    "These cases are referred to as ectopic posterior pituitary or pituitary stalk interruption.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Physiology",
                "A healthy volunteer receives a hypertonic saline infusion. Plasma osmolality rises 1%. Which physiologic response occurs first?",
                [
                    "Rapid increase in AVP secretion from posterior pituitary stores",
                    "Exponential rise in plasma AVP requiring 15% blood volume loss",
                    "Primary increase in renin-angiotensin-aldosterone secretion",
                    "Suppression of thirst until plasma osmolality exceeds 300 mOsm/kg",
                ],
                0,
                "Variations as small as 1% in plasma osmolality cause rapid AVP release; volume/pressure changes require much larger stimuli.",
                ref(
                    "Osmotic Regulation",
                    "Variations as small as 1% in plasma osmolality will cause a rapid increase or decrease of AVP released from the store of hormone in the posterior pituitary.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Physiology",
                "A patient with SIAD has maximally concentrated urine despite elevated AVP. Which renal mechanism limits further urine osmolality increase?",
                [
                    "Inner medullary osmolality plateau (~800–1200 mOsm/kg)",
                    "Complete absence of aquaporin 3 in basolateral membranes",
                    "V1a receptor blockade in the collecting duct",
                    "Obligate loss of all V2 receptors during chronic AVP exposure",
                ],
                0,
                "Urine osmolality plateaus at inner medulla osmolality even when plasma AVP rises further.",
                ref(
                    "Osmotic Regulation",
                    "Although plasma AVP might increase above the normal physiologic range, the urine osmolality plateaus at approximately 800 to 1200 mOsm/kg H₂O because the maximum concentration of fluid in the renal collecting duct is the osmolality of the inner medulla of the kidney.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Physiology",
                "Experimental OVLT destruction in animals abolishes which response?",
                [
                    "AVP secretion and thirst to hyperosmolality but not to hypovolemia",
                    "AVP secretion to hypovolemia but not to hyperosmolality",
                    "Both thirst and AVP responses to hypovolemia and hyperosmolality",
                    "Renin release but not AVP secretion during dehydration",
                ],
                0,
                "OVLT lesions abolish osmotically stimulated AVP and thirst while sparing volume-mediated responses.",
                ref(
                    "Osmotic Regulation",
                    "Surgical destruction of the OVLT abolishes AVP secretion and thirst responses to hyperosmolality but not their responses to hypovolemia.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Diagnosis",
                "A man reports 8 L/day urine output. Random urine osmolality is 150 mOsm/kg and serum sodium is 142 mmol/L. What is the next best step?",
                [
                    "Proceed with water deprivation test or copeptin-based algorithm",
                    "Exclude DI—random urine osmolality confirms primary polydipsia",
                    "Start desmopressin empirically before any further testing",
                    "Order only serum glucose because polyuria always indicates diabetes mellitus",
                ],
                0,
                "Low urine osmolality with polyuria warrants differentiation among CDI, NDI, and primary polydipsia via water deprivation or copeptin testing.",
                ref(
                    "Diabetes Insipidus",
                    "The water deprivation test, which incorporates a dehydration step, followed by a desmopressin challenge, or a hypertonic saline infusion with a copeptin-based algorithm are usually the first lines of investigation.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Diagnosis",
                "During a water deprivation test, urine osmolality remains 220 mOsm/kg after plasma osmolality reaches 298 mOsm/kg. After desmopressin, urine osmolality rises to 650 mOsm/kg. What is the diagnosis?",
                [
                    "Central diabetes insipidus",
                    "Nephrogenic diabetes insipidus",
                    "Primary polydipsia",
                    "Osmotic diuresis from hyperglycemia",
                ],
                0,
                "Failure to concentrate during dehydration with good response to exogenous desmopressin indicates CDI.",
                ref(
                    "Diabetes Insipidus",
                    "In primary polydipsia, urine should concentrate relatively normally because AVP secretion is normal, whereas in patients with either CDI or NDI the urine remains dilute until desmopressin is administered.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Diagnosis",
                "A polyuric patient has copeptin 2.1 pmol/L after hypertonic saline infusion targeting Na⁺ ≥150 mmol/L. What does this support?",
                [
                    "Central diabetes insipidus rather than primary polydipsia",
                    "Nephrogenic diabetes insipidus with certainty",
                    "Primary polydipsia rather than CDI",
                    "Normal osmoregulation—no further workup needed",
                ],
                0,
                "Osmotically stimulated copeptin ≤4.9 pmol/L distinguishes CDI from primary polydipsia with high accuracy.",
                ref(
                    "Diabetes Insipidus",
                    "The same study showed that a copeptin cutoff of 4.9 pmol/L was able to differentiate between CDI and primary polydipsia with high diagnostic accuracy.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Diagnosis",
                "A patient with polyuria has copeptin 28 pmol/L without prior thirsting. Which diagnosis is most likely?",
                [
                    "Nephrogenic diabetes insipidus",
                    "Central diabetes insipidus",
                    "Primary polydipsia",
                    "Syndrome of inappropriate antidiuresis",
                ],
                0,
                "Basal copeptin >21.4 pmol/L differentiates NDI from other causes of polyuria with high sensitivity and specificity.",
                ref(
                    "Diabetes Insipidus",
                    "A single copeptin concentration of over 21.4 pmol/L without prior thirsting differentiates NDI from other causes of polyuria, with a sensitivity and specificity of 100%.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Diagnosis",
                "A 28-year-old with new CDI has normal pituitary MRI except for absent posterior bright spot and thickened stalk. Which evaluation is most important?",
                [
                    "Search for systemic causes such as germinoma, histiocytosis, or sarcoidosis",
                    "Immediate transsphenoidal adenoma resection",
                    "No further workup—idiopathic CDI is assumed in all young adults",
                    "Water loading test to confirm SIAD before any imaging follow-up",
                ],
                0,
                "CDI with stalk thickening and absent bright spot warrants systemic disease evaluation; germinoma may not appear on initial scans.",
                ref(
                    "Further Investigations of Diabetes Insipidus",
                    "When there is a diagnosis of CDI, thickening of the stalk is usually associated with absence of the posterior pituitary bright spot, and a search for systemic diseases is indicated.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Treatment",
                "A patient with complete CDI asks about desmopressin timing to avoid hyponatremia. Which strategy aligns with clinical practice?",
                [
                    "Delay each dose until urination begins",
                    "Take a double dose every morning regardless of urine output",
                    "Infuse hypotonic IV fluids routinely with each dose",
                    "Avoid all fluid intake on days desmopressin is taken",
                ],
                0,
                "Delaying desmopressin until polyuria returns allows periodic aquaresis and reduces dilutional hyponatremia risk.",
                ref(
                    "Central Diabetes Insipidus in Ambulatory Patients",
                    "Delaying each dose of desmopressin until urination begins. This is adopted by a minority of patients, particularly if they are sensitive to bloated feelings or cognitive effects with water retention.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Treatment",
                "A 19-year-old man with X-linked NDI still passes 6 L/day urine despite adequate oral intake. Which pharmacotherapy is first-line?",
                [
                    "Hydrochlorothiazide with potassium supplementation as needed",
                    "High-dose desmopressin intranasally four times daily",
                    "Fludrocortisone to increase renal AVP sensitivity",
                    "Demeclocycline to induce nephrogenic resistance",
                ],
                0,
                "Thiazides are the mainstay for NDI, reducing delivery of fluid to the collecting duct; potassium may need replacement.",
                ref(
                    "Treatment of Nephrogenic Diabetes Insipidus",
                    "Thiazide diuretics are the mainstay of treatment, and data show that these agents can additionally increase aquaporin 2 independent of AVP.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Treatment",
                "A patient on chronic lithium develops NDI. Which combination best addresses polyuria while limiting lithium toxicity risk?",
                [
                    "Amiloride with hydrochlorothiazide",
                    "Desmopressin with aggressive hypotonic fluid loading",
                    "High-dose furosemide alone without sodium replacement",
                    "Conivaptan to block V2 receptors in the collecting duct",
                ],
                0,
                "Amiloride inhibits lithium reabsorption in the collecting duct; thiazides help NDI but can raise lithium levels—amiloride mitigates that risk.",
                ref(
                    "Treatment of Nephrogenic Diabetes Insipidus",
                    "Persistent NDI can be treated with hydrochlorothiazide and amiloride.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Complications",
                "Ten days after transsphenoidal surgery for craniopharyngioma, a patient develops headache, nausea, and Na⁺ 128 mmol/L without preceding polyuria. What is the most likely mechanism?",
                [
                    "Isolated second phase of triphasic response with unregulated AVP release",
                    "New-onset primary polydipsia from hypothalamic thirst reset",
                    "Acute adrenal crisis causing hypernatremia",
                    "Nephrogenic DI from intraoperative mannitol",
                ],
                0,
                "Isolated phase 2—uncontrolled AVP release from damaged axons around days 7–10—can cause hyponatremia without preceding DI.",
                ref(
                    "Hypothalamic/Central Diabetes Insipidus",
                    "An important observation is that the second phase of the triphasic response (i.e., uncontrolled release of AVP due to axon trauma) can occur without preceding or subsequent DI.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Complications",
                "A comatose TBI patient has polyuria, serum Na⁺ 154 mmol/L, and urine osmolality 120 mOsm/kg. Which management priority is most urgent?",
                [
                    "Replace free water and treat CDI while monitoring sodium closely",
                    "Restrict all fluids to 500 mL/day to prevent cerebral edema",
                    "Give hypertonic saline to raise sodium further",
                    "Withhold desmopressin because TBI always causes SIAD only",
                ],
                0,
                "TBI commonly causes acute CDI; comatose patients cannot drink and develop hypernatremia without careful fluid and desmopressin management.",
                ref(
                    "Central Diabetes Insipidus in Neurosurgical Patients",
                    "Because a comatose patient must be given fluids parenterally, it is important to monitor serum sodium concentration regularly to check for dilutional hyponatremia.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Adipsic DI",
                "A patient after anterior communicating artery aneurysm clipping has polyuria and repeatedly normal or high serum Na⁺ despite access to water. What is the diagnosis?",
                [
                    "Adipsic diabetes insipidus",
                    "Primary polydipsia with compulsive water intake",
                    "Reset osmostat variant of SIAD",
                    "Nephrogenic DI from amiloride therapy",
                ],
                0,
                "Vascular damage to anterior hypothalamic osmoreceptors after ACom aneurysm surgery can cause permanent adipsic DI.",
                ref(
                    "Hypothalamic/Central Diabetes Insipidus",
                    "Some patients who have surgical clipping of anterior communicating artery aneurysms can develop permanent adipic CDI (adipsic diabetes insipidus [ADI]) due to vascular damage to the perforating arteries of the anterior communicating artery, which provide vascular input to the anterior hypothalamus where the osmoreceptors are situated.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Pregnancy",
                "At 28 weeks gestation, a woman with mild partial CDI develops worsening polyuria. Desmopressin is started. Which statement about therapy is correct?",
                [
                    "Desmopressin is not destroyed by placental oxytocinase and is recommended in pregnancy",
                    "Desmopressin is contraindicated because it crosses the placenta as active AVP",
                    "Oral desmopressin must be stopped because oxytocinase abolishes all effect",
                    "Only intravenous vasopressin—not desmopressin—may be used in pregnancy",
                ],
                0,
                "Desmopressin resists pregnancy oxytocinase and is the only recommended DI therapy during pregnancy.",
                ref(
                    "Treatment of Diabetes Insipidus in Pregnancy",
                    "Desmopressin is not destroyed by the cysteine aminopeptidase (oxytocinase) of pregnancy and is reported to be safe for both the mother and the child.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "SIAD",
                "A euvolemic patient has serum Na⁺ 128 mmol/L, plasma osmolality 260 mOsm/kg, and urine osmolality 450 mOsm/kg. Urine Na⁺ is 45 mmol/L. After excluding hypothyroidism and adrenal insufficiency, what is the most likely diagnosis?",
                [
                    "Syndrome of inappropriate antidiuresis",
                    "Hypovolemic hyponatremia from GI losses",
                    "Hypervolemic hyponatremia from heart failure",
                    "Primary polydipsia alone without AVP abnormality",
                ],
                0,
                "Euvolemic hypoosmolarity with inappropriately concentrated urine and elevated urine sodium fits SIAD after excluding hypothyroidism and adrenal insufficiency.",
                ref(
                    "Syndrome of Inappropriate Antidiuresis",
                    "SIAD is the most common cause of euvolemic hypoosmolarity, and it is also the single most common cause of hypoosmolarity of all etiologies encountered in clinical practice.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "SIAD",
                "An elderly man on an SSRI presents with mild hyponatremia. He appears euvolemic. Which associated finding supports SIAD?",
                [
                    "Serum uric acid <4 mg/dL",
                    "Serum uric acid >8 mg/dL with gout",
                    "Urine osmolality <50 mOsm/kg during hypoosmolarity",
                    "Low urine sodium despite euvolemia",
                ],
                0,
                "SIAD increases renal uric acid clearance causing hypouricemia; urine is inappropriately concentrated, not maximally dilute.",
                ref(
                    "Syndrome of Inappropriate Antidiuresis",
                    "Volume expansion and AVP acting on V₁ receptors in the kidney increase the clearance of uric acid, so hypouricemia is found with SIAD.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "SIAD",
                "A hospitalized patient with SIAD and urine osmolality 620 mOsm/kg is started on fluid restriction to 800 mL/day. Sum of urine [Na⁺]+[K⁺] exceeds serum [Na⁺]. What is the expected outcome?",
                [
                    "Likely failure of fluid restriction to raise serum sodium",
                    "Rapid correction of sodium by >10 mmol/L in 24 hours",
                    "Immediate conversion to hypernatremia",
                    "Spontaneous aquaresis making vaptans unnecessary in all SIAD",
                ],
                0,
                "When urine electrolytes exceed serum sodium, electrolyte-free water clearance is difficult and fluid restriction often fails.",
                ref(
                    "Fluid Restriction",
                    "If the sum of urine [Na⁺] and [K⁺] exceeds the serum [Na⁺], most patients will not respond to a fluid restriction because an electrolyte-free water clearance will be difficult to achieve.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "SIAD",
                "A euvolemic hyponatremic patient with SIAD fails fluid restriction. In the United States, which vaptan indication applies for serum Na⁺ 124 mmol/L?",
                [
                    "Tolvaptan as primary therapy because Na⁺ is below 125 mmol/L",
                    "Conivaptan is oral first-line for outpatient long-term use only",
                    "Vaptans are first-line for hypovolemic hyponatremia",
                    "Tolvaptan is contraindicated unless Na⁺ exceeds 135 mmol/L",
                ],
                0,
                "In the US, tolvaptan is primary therapy when serum Na⁺ is below 125 mmol/L; hospital initiation with frequent sodium monitoring is required.",
                ref(
                    "AVP Receptor Antagonists",
                    "In the United States, patients with a serum [Na⁺] lower than 125 mmol/L are eligible for therapy with tolvaptan as primary therapy.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "SIAD",
                "A patient with severe hyponatremic encephalopathy (seizures, Na⁺ 118 mmol/L) arrives in the ED. What is the appropriate initial treatment?",
                [
                    "100-mL bolus of 3% NaCl, repeatable if no improvement in 30 minutes",
                    "Fluid restriction to 500 mL/day as sole therapy",
                    "Oral tolvaptan 60 mg before any sodium measurement",
                    "Isotonic saline infusion alone for euvolemic SIAD",
                ],
                0,
                "Severe symptomatic hyponatremia requires prompt hypertonic saline; bolus 3% NaCl is recommended for emergent cases.",
                ref(
                    "Hypertonic Saline",
                    "An alternative option for more emergent situations is administration of a 100-mL bolus of 3% NaCl, repeated twice if there is no clinical improvement in 30 minutes.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Pitfalls",
                "A postoperative patient receives hypotonic IV fluids on day 8 after pituitary stalk surgery. She becomes obtunded with Na⁺ 121 mmol/L. What was the critical pitfall?",
                [
                    "Unrecognized phase 2 triphasic AVP release with continued hypotonic fluids",
                    "Failure to give desmopressin on day 1 for all stalk surgeries",
                    "Assuming pituitary adenoma caused her initial polyuria",
                    "Overcorrection of hypernatremia causing osmotic demyelination",
                ],
                0,
                "Phase 2 unregulated AVP release around days 5–7 plus hypotonic fluids causes dilutional hyponatremia—a common postoperative pitfall.",
                ref(
                    "Hypothalamic/Central Diabetes Insipidus",
                    "This phase, which typically occurs 5 to 7 days following surgery, is often marked by hyponatremia, particularly if there is injudicious administration of intravenous hypotonic fluids.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Pitfalls",
                "An elderly nursing-home resident on thiazide and SSRI has Na⁺ 129 mmol/L. She is alert but has had two falls this month. What is the best clinical insight?",
                [
                    "Even mild chronic hyponatremia increases fall risk and warrants treatment consideration",
                    "Asymptomatic hyponatremia in the elderly never requires correction",
                    "Thiazides always cause hypernatremia, not hyponatremia",
                    "SSRI-associated hyponatremia occurs only in young adults",
                ],
                0,
                "Chronic mild hyponatremia is linked to gait instability and falls; elderly patients on thiazides and SSRIs are high risk.",
                ref(
                    "Hypoosmolar Symptoms, Morbidity, and Mortality",
                    "Researchers found that 21% of the hyponatremic patients came to the ED because of a recent fall, compared to only 5% of the controls.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Physiology",
                "Which receptor mediates AVP-stimulated ACTH secretion from the anterior pituitary?",
                [
                    "V1b receptor",
                    "V2 receptor",
                    "V1a receptor on hepatocytes",
                    "Oxytocin receptor in the SON",
                ],
                0,
                "V1b receptors mediate the nontraditional action of AVP to stimulate ACTH secretion and are found in peripheral tissues and brain.",
                ref(
                    "Physiology of Secretion of AVP and Thirst",
                    "A third receptor, V1b, is responsible for the nontraditional biologic action of AVP to stimulate ACTH secretion from the anterior pituitary and has been found in numerous peripheral tissues and areas of the brain.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Diagnosis",
                "A psychiatric inpatient drinks 12 L/day. During hypertonic saline infusion, thirst remains high after drinking. What finding best supports primary polydipsia?",
                [
                    "Failure to suppress thirst by more than 50% after drinking",
                    "Absent posterior pituitary bright spot on MRI",
                    "Copeptin >21.4 pmol/L without thirsting",
                    "Maximal urine concentration only after desmopressin",
                ],
                0,
                "Failure to suppress stimulated thirst after drinking by >50% is a strong diagnostic indicator of primary polydipsia.",
                ref(
                    "Diabetes Insipidus",
                    "Failure to suppress thirst after drinking by more than 50% of stimulated levels is the most useful of these abnormalities because it is a strong diagnostic indicator of primary polydipsia.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Treatment",
                "A hospitalized CDI patient vomits and cannot take oral desmopressin. Serum Na⁺ rises to 152 mmol/L. What is the most likely preventable cause?",
                [
                    "Delayed or omitted desmopressin during intercurrent illness",
                    "Excessive desmopressin causing dilutional hyponatremia",
                    "Primary polydipsia from compulsive drinking",
                    "SIAD from posterior pituitary bright spot ectopia",
                ],
                0,
                "Hypernatremic dehydration during vomiting is common when desmopressin is delayed or omitted—90% of cases reflect poor clinician awareness.",
                ref(
                    "Central Diabetes Insipidus in Hospitalized Patients",
                    "This high rate of hypernatremia seems to reflect delayed administration or even omission of dDAVP doses; in 90% of cases, this appears to be due to poor awareness of clinicians of the importance of timely administration of desmopressin.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Anatomy",
                "The posterior pituitary receives its blood supply via the hypothalamic–pituitary portal system like the anterior pituitary.",
                False,
                "The posterior pituitary is supplied directly from inferior hypophyseal arteries, not the portal system.",
                ref(
                    "Anatomy",
                    "The blood supply for the anterior pituitary is via the hypothalamic/pituitary portal system, but the posterior pituitary is supplied directly from the inferior hypophyseal arteries.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Physiology",
                "Plasma AVP responds to a 1% change in osmolality but requires roughly 10–15% volume or pressure change to increase secretion.",
                True,
                "Osmoregulation is exquisitely sensitive compared with baroreceptor-mediated volume regulation.",
                ref(
                    "Physiology of Secretion of AVP and Thirst",
                    "Plasma AVP is much more sensitive to changes in osmolality, responding to as little as a 1% increase, whereas a change of 10% to 15% or greater in volume or pressure is required to stimulate the release of AVP.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Physiology",
                "V2 receptor activation inserts aquaporin-2 into the apical membrane of collecting duct principal cells.",
                True,
                "V2–cAMP–PKA signaling phosphorylates aquaporin 2 and shuttles channels to the luminal membrane.",
                ref(
                    "Osmotic Regulation",
                    "This leads to phosphorylation and activation of aquaporin 2 and movement of the water channels into the luminal membrane.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Diagnosis",
                "A random urine osmolality above 800 mOsm/kg excludes diabetes insipidus and makes primary polydipsia certain.",
                True,
                "High random urine osmolality effectively rules out DI in the polyuria evaluation.",
                ref(
                    "Diabetes Insipidus",
                    "However, a random urine osmolality above 800 mOsm/kg excludes DI and makes the diagnosis of primary polydipsia certain.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Diagnosis",
                "Copeptin is less stable ex vivo than AVP and therefore harder to measure routinely.",
                False,
                "Copeptin is much more stable ex vivo with straightforward sample handling.",
                ref(
                    "Diabetes Insipidus",
                    "It is much more stable ex vivo, so sample handling is straightforward.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Imaging",
                "Absence of the posterior pituitary bright spot on MRI alone is sufficient to diagnose CDI.",
                False,
                "The bright spot is absent in 39% of primary polydipsia patients; MRI alone cannot establish the diagnosis.",
                ref(
                    "Further Investigations of Diabetes Insipidus",
                    "Consequently, the presence or absence of the bright spot on MRI is not sufficient to establish a diagnosis in patients with DI.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Treatment",
                "Hyponatremia is the most common complication of desmopressin therapy in ambulatory CDI.",
                True,
                "Continuous antidiuresis plus social drinking causes dilutional hyponatremia in many treated patients.",
                ref(
                    "Central Diabetes Insipidus in Ambulatory Patients",
                    "Hyponatremia is the most common complication of desmopressin therapy, with mild depression of plasma sodium concentration (131–134 mmol/L) reported to occur in 27% of ambulatory blood samples in patients with intact thirst.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Treatment",
                "Patients with nephrogenic DI typically respond well to standard desmopressin doses.",
                False,
                "Pharmacologic reversal of renal AVP resistance is rarely possible; adequate water intake is the mainstay.",
                ref(
                    "Treatment of Nephrogenic Diabetes Insipidus",
                    "Pharmacologic reversal of the renal resistance to AVP is rarely possible, and patients typically do not respond to desmopressin therapy.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "SIAD",
                "Isotonic saline is effective first-line therapy for euvolemic hyponatremia due to SIAD.",
                False,
                "Isotonic saline is ineffective for dilutional hyponatremia such as SIAD and may worsen hyponatremia in euvolemic patients.",
                ref(
                    "Isotonic Saline",
                    "However, isotonic saline is ineffective for dilutional hyponatremia such as SIAD, and continued administration of isotonic saline to a euvolemic patient may worsen their hyponatremia.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "SIAD",
                "Fluid restriction of 500–1000 mL/day is often highly effective and rapidly corrects SIAD-related hyponatremia.",
                False,
                "Fluid restriction increases serum Na⁺ slowly (1–2 mmol/L/day) and randomized trials show limited efficacy in SIAD.",
                ref(
                    "Fluid Restriction",
                    "Restricting fluid intake can be effective when properly applied and managed in selected patients, but serum [Na⁺] is generally increased only slowly (1–2 mmol/L/day) even with severe fluid restriction.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "SIAD",
                "Vaptans are contraindicated in hypovolemic hyponatremia because aquaresis can worsen hypotension.",
                True,
                "Volume expansion abolishes nonosmotic AVP stimulus in hypovolemic hyponatremia; inducing diuresis can cause or worsen hypotension.",
                ref(
                    "AVP Receptor Antagonists",
                    "Vaptans are not needed in the treatment of hypovolemic hyponatremia because simple volume expansion would be expected to abolish the nonosmotic stimulus to AVP secretion and lead to a prompt aquaresis.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Pregnancy",
                "Normal pregnancy lowers plasma osmolality by resetting the osmostat threshold for AVP secretion.",
                True,
                "Pregnancy is the classic example of osmostat resetting with lower plasma osmolality maintained appropriately.",
                ref(
                    "Effects of Pregnancy on Fluid Homeostasis",
                    "Major shifts of fluid during normal pregnancy produce a fall in plasma osmolality of about 10 mmol/kg; this is the best physiologic example of a true resetting of the osmostat.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Pitfalls",
                "Overly rapid correction of chronic hyponatremia can cause osmotic demyelination syndrome.",
                True,
                "All hyponatremia therapies require attention to correction limits to reduce ODS risk, especially with rapid rises in serum Na⁺.",
                ref(
                    "Therapies for Treatment of Hyponatremia",
                    "For all therapies, careful attention should be paid to recommendations for goals and limits of correction of the serum [Na⁺] to reduce the risk of the osmotic demyelination syndrome (ODS).",
                ),
            ),
        ]
    )

    # --- Assertion–Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Anatomy",
                "Assertion: Magnocellular neurons in the SON and PVN project axons to the posterior pituitary.",
                "Reason: The posterior pituitary consists only of distal axon terminals of hypothalamic magnocellular neurons.",
                0,
                "Both are true; the reason correctly explains the neurohypophyseal anatomy.",
                ref(
                    "Anatomy",
                    "The posterior pituitary is neural tissue and consists only of the distal axons of the hypothalamic magnocellular neurons that make up the neurohypophysis.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Physiology",
                "Assertion: Small increases in plasma osmolality produce concentrated urine in healthy humans.",
                "Reason: Plasma AVP changes rapidly because its half-life in plasma is approximately 15 minutes.",
                0,
                "Both true—the short AVP half-life enables minute-to-minute antidiuretic responses to osmotic stimuli.",
                ref(
                    "Osmotic Regulation",
                    "Rapid metabolism of AVP is also characteristic of the hormone that circulates in plasma with a half-life of approximately 15 minutes, which allows rapid changes in levels of AVP in plasma.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Diagnosis",
                "Assertion: Copeptin measurement can replace the water deprivation test for evaluating polyuria.",
                "Reason: Copeptin is unrelated to AVP and is not co-secreted from the neurohypophysis.",
                2,
                "Assertion is supported by emerging data; the reason is false—copeptin is the C-terminal fragment of proAVP co-secreted equimolarly with AVP.",
                ref(
                    "Diabetes Insipidus",
                    "Copeptin is the C-terminal locus of the AVP precursor proAVP, and it is co-secreted from the neurohypophysis in equimolar amounts with AVP in response to the same stimuli.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Diagnosis",
                "Assertion: A desmopressin challenge after water deprivation helps distinguish CDI from NDI.",
                "Reason: NDI shows little or no urine concentration after desmopressin because of renal AVP resistance.",
                0,
                "Both true—CDI concentrates after exogenous desmopressin; NDI does not.",
                ref(
                    "Diabetes Insipidus",
                    "In primary polydipsia, urine should concentrate relatively normally because AVP secretion is normal, whereas in patients with either CDI or NDI the urine remains dilute until desmopressin is administered.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Treatment",
                "Assertion: Desmopressin is preferred over native AVP for chronic CDI therapy.",
                "Reason: Desmopressin has markedly reduced pressor activity and longer half-life than L-arginine AVP.",
                0,
                "Both true—D-arginine substitution and terminal deamination make desmopressin a selective antidiuretic.",
                ref(
                    "Central Diabetes Insipidus in Ambulatory Patients",
                    "Therapeutic replacement of AVP is achieved with the administration of desmopressin, a synthetic analog of AVP, in which the substitution of D-arginine markedly reduces pressor activity and removing the terminal amine increases the half-life.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Treatment",
                "Assertion: Thiazide diuretics can reduce urine volume in nephrogenic DI.",
                "Reason: Thiazides increase free water delivery to the collecting duct.",
                2,
                "Assertion is true; reason is false—thiazides decrease delivery of fluid to the collecting duct via proximal sodium and water reabsorption.",
                ref(
                    "Treatment of Nephrogenic Diabetes Insipidus",
                    "Therapy goals are plasma volume contraction in order to decrease glomerular filtration rate; proximal tubular sodium and water reabsorption; and decreased delivery of fluid to the collecting duct, resulting in a decreased volume of urine.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Adipsic DI",
                "Assertion: Adipsic DI carries higher hypernatremia risk than typical CDI.",
                "Reason: ADI patients retain normal osmoregulated thirst despite DI.",
                2,
                "Assertion is true; reason is false—ADI is defined by attenuated thirst, not preserved osmoregulated thirst.",
                ref(
                    "Adipsic Diabetes Insipidus",
                    "ADI is characterized by the combination of attenuated thirst and DI.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "SIAD",
                "Assertion: SIAD is the most common cause of euvolemic hyponatremia.",
                "Reason: SIAD occurs when AVP is suppressed during hypoosmolarity.",
                2,
                "Assertion is true; reason is false—SIAD features inappropriately elevated or nonsuppressible AVP during hypoosmolarity.",
                ref(
                    "Syndrome of Inappropriate Antidiuresis",
                    "SIAD is produced when plasma levels of AVP are elevated at times when the physiologic secretion of AVP from the posterior pituitary would normally be osmotically suppressed.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "SIAD",
                "Assertion: Tolvaptan directly antagonizes AVP at V2 receptors to increase free water excretion.",
                "Reason: Vaptans block AVP-mediated receptor activation causing aquaresis in euvolemic and hypervolemic hyponatremia.",
                0,
                "Both true—vaptans target the underlying inappropriate antidiuresis in many dilutional hyponatremias.",
                ref(
                    "AVP Receptor Antagonists",
                    "A relatively new class of pharmacologic agents (AVP receptor antagonists [vaptans]) that directly block AVP-mediated receptor activation has been approved for the treatment of euvolemic hyponatremia and hypervolemic hyponatremia in many countries.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Complications",
                "Assertion: Post-pituitary surgery hyponatremia around day 8 may reflect unregulated AVP release.",
                "Reason: Phase 2 of the triphasic response never occurs without preceding and subsequent DI phases.",
                1,
                "Assertion is true; reason is false—isolated second phase without other DI phases is well described.",
                ref(
                    "Hypothalamic/Central Diabetes Insipidus",
                    "An important observation is that the second phase of the triphasic response (i.e., uncontrolled release of AVP due to axon trauma) can occur without preceding or subsequent DI.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Pregnancy",
                "Assertion: Pregnancy-associated DI may worsen because of accelerated AVP degradation.",
                "Reason: Placental oxytocinase equally degrades oxytocin and AVP with rising activity after 20 weeks.",
                0,
                "Both true—oxytocinase can unmask borderline AVP secretory capacity in pregnancy.",
                ref(
                    "Effects of Pregnancy on Fluid Homeostasis",
                    "This enzyme is equally potent in degrading oxytocin and AVP.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Pitfalls",
                "Assertion: Hypertonic saline boluses can rapidly reduce brain swelling in acute symptomatic hyponatremia.",
                "Reason: A 100-mL 3% NaCl bolus typically raises serum Na⁺ by 10–12 mmol/L immediately.",
                1,
                "Assertion is true; reason overstates the increment—a bolus raises Na⁺ by about 2–4 mmol/L, still enough to reduce cerebral edema.",
                ref(
                    "Hypertonic Saline",
                    "Injecting this amount of hypertonic saline intravenously raises the serum [Na⁺] by an average of 2 to 4 mmol/L, which is well below the recommended maximal daily rate of change of 10 to 12 mmol/L/24 hours.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "8",
        "title": "Posterior Pituitary",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Mirjam Christ-Crain, Christopher J. Thompson, Joseph G. Verbalis",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_08_Posterior_Pituitary.md",
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
