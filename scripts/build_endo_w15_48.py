#!/usr/bin/env python3
"""Generate Williams 15e module w15-48 — Endocrine Disorders of Critical Illness."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-48"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-48_Endocrine_Disorders_of_Critical_Illness.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why endocrine alterations differ in acute versus prolonged critical illness",
                "Characteristic endocrine changes in critical illness differ between the acute and prolonged phases and complicate diagnosis of preexisting endocrine disease.",
                ref(
                    "KEY POINTS",
                    "In critical illness, characteristic endocrine alterations develop; these alterations differ in the acute versus prolonged phase of illness and complicate the diagnosis of preexisting endocrine disease.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How the acute critical illness endocrine phenotype looks",
                "Acute critical illness features low thyroid hormone and IGF-1 with high cortisol—presumably adaptive changes driven mainly by peripheral hormone metabolism.",
                ref(
                    "KEY POINTS",
                    "Acute critical illness is characterized by low levels of thyroid hormone and insulin-like growth factor 1, and high levels of cortisol, which is presumably adaptive and mainly brought about by peripheral alterations in hormone metabolism.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why prolonged ICU stay causes central neuroendocrine suppression",
                "In prolonged critical illness, central suppression of somatotropic, thyrotropic, and adrenocorticotropic axes may impair rehabilitation; optimal treatment awaits adequately powered trials.",
                ref(
                    "KEY POINTS",
                    "In patients with prolonged critical illness, a central suppression of the somatotropic, thyrotropic, and adrenocorticotropic axes progressively develops, which may impair rehabilitation, although treatment indications and regimens remain to be studied in adequately powered trials.",
                ),
            ),
            note(
                f"{p}-n4",
                "KEY POINTS",
                "How to achieve safe blood glucose control in the ICU",
                "Safe glycemic control requires a validated protocol with accurate frequent glucose measurements and avoidance of insulin boluses.",
                ref(
                    "KEY POINTS",
                    "Safe blood glucose control in critically ill patients requires a validated protocol, with accurate and frequent blood glucose measurements and avoidance of insulin boluses.",
                ),
            ),
            note(
                f"{p}-n5",
                "KEY POINTS",
                "Why the ideal ICU glucose target remains unclear",
                "Without early parenteral nutrition, the optimal blood glucose target in critically ill patients has not been definitively established.",
                ref(
                    "KEY POINTS",
                    "The ideal blood glucose target in critically ill patients not receiving early parenteral nutrition remains unclear.",
                ),
            ),
            note(
                f"{p}-n6",
                "KEY POINTS",
                "How to interpret low vitamin D in acute critical illness",
                "Low vitamin D concentrations in critically ill patients are probably adaptive during the acute phase of illness.",
                ref(
                    "KEY POINTS",
                    "Critically ill patients have low vitamin D concentrations, which is probably adaptive in the acute phase of illness.",
                ),
            ),
            note(
                f"{p}-n7",
                "Introduction",
                "Why critical illness triggers profound endocrine alterations",
                "Severe illness, major surgery, or trauma provoke neuroendocrine changes, insulin resistance, stress hyperglycemia, and vitamin D alterations assumed adaptive but complicating preexisting endocrine diagnosis.",
                ref(
                    "Introduction",
                    "As part of the stress response, profound endocrine alterations occur, including neuroendocrine changes, insulin resistance and stress hyperglycemia, and alterations in vitamin D, which have been assumed to be adaptive.",
                ),
            ),
            note(
                f"{p}-n8",
                "Alterations in the Somatotropic Axis",
                "How the GH axis changes in acute critical illness",
                "GH secretion increases with higher pulse frequency and amplitude, but peripheral GH resistance lowers hepatic receptors and IGF-1, IGFBP3, and ALS.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "In the acute phase of critical illness, growth hormone (GH) secretion increases, with increased pulse frequency and amplitude and elevated trough concentrations.",
                ),
            ),
            note(
                f"{p}-n9",
                "Alterations in the Somatotropic Axis",
                "Why high-dose GH increases mortality in prolonged critical illness",
                "RCTs showed high-dose GH after 5–7 days in expected long-stay ICU patients significantly increased mortality, likely from GH overdosing when peripheral responsiveness recovers.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "two randomized controlled trials (RCTs) revealed that high-dose GH treatment, initiated after 5 to 7 days in expected long-stay critically ill patients, significantly increased mortality, which may be explained by GH overdosing in a state of recovered GH responsiveness.",
                ),
            ),
            note(
                f"{p}-n10",
                "Alterations in the Somatotropic Axis",
                "How dopamine suppresses the somatotropic axis in ICU",
                "Dopamine, historically used as a vasoactive agent, centrally suppresses the somatotropic axis in critically ill patients.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "The administration of dopamine treatment, commonly used as vasoactive strategy in the past, centrally suppresses the somatotropic axis.",
                ),
            ),
            note(
                f"{p}-n11",
                "Alterations in the Thyroid Axis",
                "Why T3 falls rapidly in acute critical illness",
                "Type 1 deiodinase activity falls while type 3 deiodinase rises, increasing T4 conversion to inactive rT3 and T3 degradation, lowering T3 and the T3:rT3 ratio.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "Mechanistically, the activity of type 1 deiodinase is attenuated while type 3 deiodinase activity increases, leading to increased peripheral conversion of thyroxine ( $ T_{4} $) secreted by the thyroid gland to the biologically inactive reverse  $ T_{3} $ ( $ rT_{3} $).",
                ),
            ),
            note(
                f"{p}-n12",
                "Alterations in the Thyroid Axis",
                "How euthyroid sick syndrome presents biochemically",
                "Low T3 with brief TSH and T4 rise then normalization defines euthyroid sick syndrome, nonthyroid illness, or acute low T3 syndrome triggered by inflammation and fasting.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "These alterations have been designated as euthyroid sick syndrome, nonthyroid illness, or acute low  $ T_{3} $ syndrome.",
                ),
            ),
            note(
                f"{p}-n13",
                "Alterations in the Thyroid Axis",
                "Why low or normal TSH does not exclude hypothyroidism in ICU",
                "In overt primary hypothyroidism during critical illness, TSH may be lower than expected; history, exam, autoantibodies, and repeat testing after recovery aid diagnosis.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "In critically ill patients who do have overt primary hypothyroidism, the TSH concentrations may be lower than expected. Hence, a low or normal TSH does not exclude primary hypothyroidism.",
                ),
            ),
            note(
                f"{p}-n14",
                "Alterations in the Thyroid Axis",
                "How ICU drugs suppress the thyroid axis",
                "Iatrogenic suppression arises from iodine dressings, contrast, glucocorticoids, somatostatin, dopamine, and amiodarone.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "Apart from the critical illness-induced alterations, TSH secretion and/or thyroid hormone production may be suppressed by iatrogenic factors, including iodine-containing wound dressings and contrast agents, and drugs such as glucocorticoids, somatostatin, dopamine, and amiodarone.",
                ),
            ),
            note(
                f"{p}-n15",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "Why ACTH-cortisol dissociation occurs after acute stress",
                "After brief ACTH rise, ACTH falls while cortisol stays high because cortisol breakdown is suppressed and binding protein changes increase free cortisol.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "The persistent hypercortisolemia in the presence of suppressed ACTH (ACTH-cortisol dissociation) after the hyperacute phase is explained by suppressed breakdown of cortisol.",
                ),
            ),
            note(
                f"{p}-n16",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "How CRH and vasopressin relate to ACTH suppression",
                "Negative feedback from hypercortisolemia suppresses pituitary ACTH while ongoing CRH and arginine-vasopressin drive POMC expression without ACTH processing.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "Recent evidence indicates that the rapid suppression of ACTH following acute stress is explained by negative feedback inhibition through stress-induced hypercortisolemia on the pituitary gland, while ongoing stress-induced hypothalamic stimulation through corticotropin-releasing hormone (CRH) and arginine-vasopressin (AVP) leads to ongoing expression of the ACTH precursor pro-opiomelanocortin (POMC), which is no longer processed into ACTH.",
                ),
            ),
            note(
                f"{p}-n17",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "Why adrenal insufficiency is hard to diagnose in critical illness",
                "Elevated cortisol largely reflects peripheral adaptations, not increased production, so random cortisol and cosyntropin testing are difficult to interpret.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "the diagnosis of adrenal insufficiency in critical illness is very difficult, because high cortisol concentrations are largely mediated by peripheral adaptations and not by increased cortisol production.",
                ),
            ),
            note(
                f"{p}-n18",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "How septic shock steroid trials inform CIRCI controversy",
                "Large RCTs showed no mortality benefit from hydrocortisone in low cosyntropin responders; recent evidence questions CIRCI and generalized glucocorticoid resistance concepts.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "Altogether, recent evidence questions the traditional concept of critical illness-related corticosteroid insufficiency (CIRCI), which has been assumed to be present in septic shock, and has been related to a decreased incremental cortisol response to ACTH, as well as to generalized glucocorticoid resistance.",
                ),
            ),
            note(
                f"{p}-n19",
                "Insulin Resistance and Stress Hyperglycemia",
                "Why stress hyperglycemia develops in critical illness",
                "Severe inflammation and counter-regulatory hormone elevations usually cause hyperglycemia associated with poor ICU outcomes.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "In response to severe inflammation and elevations in counter-regulatory hormones, critically ill patients usually develop hyperglycemia, which has been associated with poor outcomes.",
                ),
            ),
            note(
                f"{p}-n20",
                "Insulin Resistance and Stress Hyperglycemia",
                "How Leuven and NICE-SUGAR trials differ in glucose control",
                "Discordant RCT results reflect different control-group targets, monitoring accuracy, insulin protocols, and feeding strategies—notably early parenteral nutrition in Leuven.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "The outcome differences between these landmark RCTs have been attributed to differences in glucose targets in the control group, differences in accuracy of the glucose monitoring and the insulin protocol, and differences in feeding strategies (Table 48.1).",
                ),
            ),
            note(
                f"{p}-n21",
                "Insulin Resistance and Stress Hyperglycemia",
                "Why insulin boluses should be avoided in ICU glucose control",
                "Continuous IV insulin infusion without boluses slowly reaches target and minimizes hypoglycemia and glucose variability, both linked to poor outcomes.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "Insulin is preferably administered through continuous intravenous insulin infusion while avoiding boluses, to slowly progress toward blood glucose target and to avoid hypoglycemia and large glucose fluctuations, because both have been associated with poor outcomes.",
                ),
            ),
            note(
                f"{p}-n22",
                "Insulin Resistance and Stress Hyperglycemia",
                "How HbA1c distinguishes stress hyperglycemia from diabetes",
                "Routine admission HbA1c helps separate pure stress hyperglycemia from hyperglycemia superimposed on previously unknown diabetes, guiding post-ICU follow-up.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "Therefore, routine HbA $ _{1c} $ measurements may aid in discriminating pure stress hyperglycemia versus stress hyperglycemia superimposed on diabetes mellitus, which could be important for post-ICU follow-up.",
                ),
            ),
            note(
                f"{p}-n23",
                "Alterations in Vitamin D",
                "Why prolonged critical illness increases bone resorption risk",
                "Prolonged ICU patients show increased bone resorption and fracture risk, potentially mediated partly by vitamin D deficiency.",
                ref(
                    "Alterations in Vitamin D",
                    "Prolonged critically ill patients have signs of increased bone resorption and increased fracture risk.",
                ),
            ),
            note(
                f"{p}-n24",
                "Alterations in Vitamin D",
                "How vitamin D supplementation RCTs inform ICU practice",
                "High-dose vitamin D RCTs raised 25OHD or active hormone without clinical benefit; acute low vitamin D is likely adaptive and needs no pharmacologic correction beyond maintenance dose.",
                ref(
                    "Alterations in Vitamin D",
                    "Altogether, current evidence suggests that low vitamin D concentrations are adaptive during acute critical illness and do not require pharmacologic correction on top of a normal maintenance dose.",
                ),
            ),
            note(
                f"{p}-n25",
                "Conclusion",
                "Why prolonged critical illness endocrine profile may be maladaptive",
                "Patients remaining ICU-dependent for weeks develop a different endocrine profile that may contribute to hypercatabolism and immune suppression.",
                ref(
                    "Conclusion",
                    "In patients who do not recover swiftly and remain dependent on intensive care for a prolonged period of time, a different endocrine profile develops, which may be maladaptive by contributing to the hypercatabolic phenotype and immune suppression associated with this condition.",
                ),
            ),
            note(
                f"{p}-n26",
                "Conclusion",
                "How illness-induced endocrine changes impede diagnosis",
                "Neuroendocrine abnormalities, stress hyperglycemia, and low vitamin D proportional to illness severity often obscure preexisting endocrine disease in the ICU.",
                ref(
                    "Conclusion",
                    "The illness-induced alterations often impede the diagnosis of preexisting endocrine disease.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Alterations in the Thyroid Axis",
                "A septic ICU patient has low T3, normal-low TSH, and no hypothyroid symptoms. Most appropriate interpretation?",
                [
                    "Euthyroid sick (nonthyroidal illness) syndrome",
                    "Primary hypothyroidism requiring immediate levothyroxine",
                    "TSH-secreting pituitary adenoma",
                    "Factitious thyrotoxicosis from exogenous T3",
                ],
                0,
                "Low T3 with normalized TSH/T4 defines euthyroid sick syndrome triggered by inflammation and fasting in acute critical illness.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "These alterations have been designated as euthyroid sick syndrome, nonthyroid illness, or acute low  $ T_{3} $ syndrome.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Alterations in the Thyroid Axis",
                "A mechanically ventilated patient on amiodarone and dopamine has low TSH and low T4. Besides critical illness, what should be considered?",
                [
                    "Iatrogenic suppression from ICU medications",
                    "Isolated primary hyperthyroidism",
                    "Thyroid storm requiring emergent thyroidectomy",
                    "Pituitary macroadenoma is the only explanation",
                ],
                0,
                "Glucocorticoids, somatostatin, dopamine, amiodarone, and iodine sources can suppress TSH and thyroid hormone production in ICU patients.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "Apart from the critical illness-induced alterations, TSH secretion and/or thyroid hormone production may be suppressed by iatrogenic factors, including iodine-containing wound dressings and contrast agents, and drugs such as glucocorticoids, somatostatin, dopamine, and amiodarone.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Alterations in the Thyroid Axis",
                "An ICU patient with known hypothyroidism has low-normal TSH. Can primary hypothyroidism still be present?",
                [
                    "Yes—a low or normal TSH does not exclude primary hypothyroidism",
                    "No—normal TSH always rules out hypothyroidism in ICU",
                    "Only if TSH is above 20 mIU/L",
                    "Only in hyperthyroid patients on methimazole",
                ],
                0,
                "Critical illness lowers expected TSH in overt primary hypothyroidism; diagnosis requires clinical context and repeat testing after recovery.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "In critically ill patients who do have overt primary hypothyroidism, the TSH concentrations may be lower than expected. Hence, a low or normal TSH does not exclude primary hypothyroidism.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Alterations in the Thyroid Axis",
                "A critically ill patient has unexpectedly elevated T3. Best next step in interpretation?",
                [
                    "Suspect hyperthyroidism or thyroid storm",
                    "Dismiss as adaptive euthyroid sick syndrome",
                    "Start high-dose levothyroxine immediately",
                    "Attribute solely to fasting without further workup",
                ],
                0,
                "Elevated T3 is highly unusual in critical illness and should prompt suspicion of hyperthyroidism or thyroid storm.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "Conversely, elevated  $ T_{3} $ concentrations are highly unusual in critical illness and should always lead to suspicion of hyperthyroidism or even thyroid storm.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Alterations in the Thyroid Axis",
                "A medical ICU team considers levothyroxine for low T3 in acute sepsis without hypothyroidism. Evidence-based approach?",
                [
                    "Do not supplement—acute alterations are adaptive without outcome benefit",
                    "Always give T4 plus T3 to all septic patients",
                    "Supplement only when TSH exceeds 20 mIU/L in acute sepsis",
                    "Thyroid hormone always improves mortality in acute critical illness",
                ],
                0,
                "Acute-phase thyroid alterations are assumed adaptive; interventional thyroid hormone supplementation has not shown outcome benefit.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "In the acute phase of critical illness, these alterations are assumed to be adaptive. $ ^{2} $ Interventional studies supplementing thyroid hormone in the acute phase of critical illness have not shown benefit on outcomes.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "A patient with septic shock has total cortisol 28 µg/dL and low ACTH. Does this exclude adrenal insufficiency?",
                [
                    "No—elevated cortisol does not exclude adrenal insufficiency in critical illness",
                    "Yes—any cortisol above 15 µg/dL rules out insufficiency",
                    "Only if ACTH is simultaneously elevated",
                    "Cortisol is uninterpretable only in hypothyroidism",
                ],
                0,
                "High cortisol in critical illness largely reflects peripheral adaptations; random cortisol is difficult to interpret for adrenal insufficiency.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "Hence, random cortisol measurements can be difficult to interpret because elevated cortisol concentrations do not exclude adrenal insufficiency.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "An ICU fellow plans cosyntropin stimulation to decide hydrocortisone therapy in septic shock. Best evidence-based advice?",
                [
                    "Cosyntropin test does not identify patients who benefit from glucocorticoids",
                    "Low cosyntropin response mandates high-dose dexamethasone for mortality benefit",
                    "Cosyntropin response perfectly predicts steroid-responsive shock",
                    "Only free T4 guides steroid decisions in sepsis",
                ],
                0,
                "Although low incremental cortisol response correlated with mortality observationally, large RCTs showed no mortality impact from steroids in low responders.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "The cosyntropin stimulation test does not identify patients who would benefit from treatment with glucocorticoids.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "A long-stay ICU patient weaned from vasopressors develops hypotension and hyponatremia one week after ICU discharge with rising ACTH and cortisol. Likely mechanism?",
                [
                    "Reversible central HPA suppression unmasked after ICU discharge",
                    "Primary hyperaldosteronism from exogenous fludrocortisone only",
                    "Isolated SIADH unrelated to HPA axis",
                    "Thyroid storm causing secondary adrenal failure",
                ],
                0,
                "Central HPA suppression in prolonged illness may manifest after discharge; ACTH and cortisol rise to supranormal levels corroborating reversible central suppression.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "On the other hand, the central suppression of the HPA axis observed in long-stay ICU patients, and the rise of ACTH and cortisol 1 week after ICU discharge, suggest that central adrenal insufficiency may exist in a subset of long-stay ICU patients, which could clinically manifest as a persistent need for vasopressors, impaired consciousness, and electrolyte abnormalities.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "Regarding hydrocortisone in septic shock, which statement matches recent RCT evidence?",
                [
                    "Most trials show faster vasopressor weaning but inconsistent mortality benefit",
                    "All RCTs show uniform 50% mortality reduction",
                    "Steroids never shorten vasopressor duration",
                    "Hydrocortisone is contraindicated in all septic shock",
                ],
                0,
                "Hydrocortisone RCTs often shortened vasopressor support but showed inconsistent benefit on hard endpoints; only one RCT found significant mortality benefit.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "Although most RCTs demonstrated faster weaning of vasopressor support, which could be expected based on the well-known blood pressure-augmenting effects of steroids, only one RCT found significant mortality benefit.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Alterations in the Somatotropic Axis",
                "A prolonged ICU patient has low IGF-1 with declining GH pulses. Consultant considers GH therapy day 6. Best recommendation?",
                [
                    "Avoid high-dose GH—RCTs increased mortality in long-stay critically ill patients",
                    "Start high-dose GH to reverse catabolism immediately",
                    "GH is first-line anabolic therapy after day 3 in all ICU patients",
                    "GH only contraindicated in children not adults",
                ],
                0,
                "High-dose GH initiated after 5–7 days in expected long-stay patients significantly increased mortality in RCTs.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "two randomized controlled trials (RCTs) revealed that high-dose GH treatment, initiated after 5 to 7 days in expected long-stay critically ill patients, significantly increased mortality, which may be explained by GH overdosing in a state of recovered GH responsiveness.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Alterations in the Somatotropic Axis",
                "An ICU patient on dopamine infusion has low IGF-1. Besides critical illness itself, what drug effect should be considered?",
                [
                    "Dopamine centrally suppresses the somatotropic axis",
                    "Dopamine exclusively stimulates GH secretion",
                    "Dopamine has no pituitary effects",
                    "Dopamine only affects thyroid hormone binding globulin",
                ],
                0,
                "Dopamine treatment centrally suppresses the somatotropic axis among ICU therapeutic effects on endocrine axes.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "The administration of dopamine treatment, commonly used as vasoactive strategy in the past, centrally suppresses the somatotropic axis.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Alterations in the Somatotropic Axis",
                "In acute critical illness, GH is high but IGF-1 is low. Primary mechanism?",
                [
                    "Peripheral GH resistance with low hepatic GH receptors",
                    "Primary pituitary GH deficiency",
                    "Excess IGF-1 feedback suppressing GH",
                    "Isolated renal failure clearing all GH",
                ],
                0,
                "Acute illness combines increased GH secretion with peripheral GH resistance lowering hepatic receptors and IGF-1, IGFBP3, and ALS.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "Similarly, peripheral growth hormone resistance occurs, with lowered expression of hepatic GH receptors, leading to low concentrations of insulin-like growth factor 1 (IGF1), IGF-binding protein 3 (IGFBP3), and acid-labile subunit (ALS) (Fig. 48.1).",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Insulin Resistance and Stress Hyperglycemia",
                "A surgical ICU uses tight glucose control 80–110 mg/dL with insulin boluses and capillary glucometers, no early PN. Compared with Leuven protocols, concern?",
                [
                    "NICE-SUGAR showed harm with tight control; boluses and capillary monitoring increase risk",
                    "Identical safety to Leuven arterial monitoring without boluses",
                    "Tight control is always beneficial regardless of feeding or monitoring",
                    "Insulin boluses are preferred to continuous infusion in ICU",
                ],
                0,
                "NICE-SUGAR showed harm from tight control vs <180 mg/dL; differences include bolus insulin, less accurate monitoring, and no early PN context of Leuven benefit.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "the NICE-SUGAR RCT subsequently showed harm by tight glucose control compared with maintaining blood glucose below 180 mg/dL.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Insulin Resistance and Stress Hyperglycemia",
                "An ICU nurse asks preferred site for glucose monitoring during IV glucose infusion. Best answer?",
                [
                    "Arterial blood glucose measurements are preferred",
                    "Capillary glucometer always preferred in shock",
                    "Venous samples are never falsely elevated",
                    "Urinary glucose replaces blood testing in ICU",
                ],
                0,
                "Arterial glucose is preferred; venous values may be falsely high with concurrent IV glucose, and capillary values are unreliable with poor perfusion.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "Arterial blood glucose measurements are preferred, because venous measurements can be falsely elevated in cases of concurrent intravenous glucose infusion, and capillary measurements are potentially unreliable in",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Insulin Resistance and Stress Hyperglycemia",
                "A diabetic ICU patient with admission HbA1c 10.2% develops glucose 95 mg/dL on insulin infusion. Special vulnerability?",
                [
                    "Poorly controlled diabetics are more vulnerable to severe and relative hypoglycemia",
                    "Diabetics are immune to hypoglycemia in critical illness",
                    "HbA1c has no bearing on hypoglycemia risk in ICU",
                    "Only nondiabetic patients suffer hypoglycemia-related harm",
                ],
                0,
                "Observational data show poorly controlled diabetes increases vulnerability to severe and relative hypoglycemia during critical illness.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "Patients with poorly controlled diabetes may be more vulnerable to severe and relative hypoglycemia, $ ^{67,68} $",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Insulin Resistance and Stress Hyperglycemia",
                "A patient without known diabetes has ICU glucose 240 mg/dL and HbA1c 7.8% on admission. Clinical implication?",
                [
                    "Likely stress hyperglycemia superimposed on previously unknown diabetes",
                    "Pure stress hyperglycemia—HbA1c is never useful in ICU",
                    "HbA1c only reflects the last 24 hours of glucose",
                    "Admission hyperglycemia never warrants post-ICU endocrine follow-up",
                ],
                0,
                "Routine HbA1c helps discriminate pure stress hyperglycemia from hyperglycemia on underlying diabetes, informing post-ICU follow-up.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "Therefore, routine HbA $ _{1c} $ measurements may aid in discriminating pure stress hyperglycemia versus stress hyperglycemia superimposed on diabetes mellitus, which could be important for post-ICU follow-up.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Insulin Resistance and Stress Hyperglycemia",
                "When is tight glucose control benefit most clearly demonstrated per chapter evidence?",
                [
                    "With early parenteral nutrition supplementing insufficient enteral feeds",
                    "Only when insulin boluses are used liberally",
                    "Exclusively in patients not receiving any nutrition",
                    "Never in any ICU population under any protocol",
                ],
                0,
                "Tight glucose control benefit was demonstrated in the context of early parenteral nutrition, a strategy later abandoned because of harm.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "In this context, a benefit of tight glucose control was only demonstrated in a context of early parenteral nutrition supplementing insufficient enteral nutrition, $ ^{10-12,61} $",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Alterations in Vitamin D",
                "An ICU patient has low 25OHD on admission day 1. Acute management per current evidence?",
                [
                    "Low vitamin D is likely adaptive—no pharmacologic correction beyond maintenance dose",
                    "Immediate megadose vitamin D3 to normalize all metabolites acutely",
                    "Stop all calcium and vitamin D in every ICU patient",
                    "IV 25OHD always normalizes active 1,25(OH)2D in acute illness",
                ],
                0,
                "Current evidence suggests acute low vitamin D is adaptive and does not require pharmacologic correction on top of normal maintenance dosing.",
                ref(
                    "Alterations in Vitamin D",
                    "Altogether, current evidence suggests that low vitamin D concentrations are adaptive during acute critical illness and do not require pharmacologic correction on top of a normal maintenance dose.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Alterations in Vitamin D",
                "A 6-week ICU survivor is evaluated for bone health. Finding associated with prolonged critical illness?",
                [
                    "Increased bone resorption and increased fracture risk",
                    "Osteoporosis is impossible during critical illness",
                    "Vitamin D always normalizes active hormone with oral D3 in ICU",
                    "Fracture risk decreases during prolonged ICU stay",
                ],
                0,
                "Prolonged critically ill patients demonstrate increased bone resorption and fracture risk, potentially linked to vitamin D alterations.",
                ref(
                    "Alterations in Vitamin D",
                    "Prolonged critically ill patients have signs of increased bone resorption and increased fracture risk.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Alterations in the Thyroid Axis",
                "A patient with preexisting hypothyroidism on oral levothyroxine is NPO and needs IV replacement. Dose adjustment?",
                [
                    "Reduce substitution dose by approximately 25% for IV therapy",
                    "Double the oral dose when switching to IV",
                    "Stop all thyroid hormone during any ICU admission",
                    "IV levothyroxine requires no dose change from oral",
                ],
                0,
                "IV substitution is usually reduced ~25% to account for roughly 75% oral levothyroxine bioavailability.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "When the patient is in need of intravenous substitution, the substitution dose is usually reduced by approximately 25%, to account for an oral bioavailability of roughly 75%.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "Stress-dose hydrocortisone in septic shock without adrenal insufficiency compared with endogenous cortisol production?",
                [
                    "Stress doses far exceed estimated ~60 mg/day cortisol production rate",
                    "Stress doses are always below physiologic cortisol production",
                    "Endogenous production exceeds 500 mg/day in all septic patients",
                    "Hydrocortisone has no hemodynamic effects in shock",
                ],
                0,
                "Stress hydrocortisone doses for septic shock exceed the estimated ~60 mg/day cortisol production in hyperinflammatory patients without adrenal insufficiency.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "Indeed, stress doses of hydrocortisone to prevent adrenal crisis and as adjunctive treatment of septic shock far exceed the cortisol production rate in hyperinflammatory patients without adrenal insufficiency, which has been estimated to be approximately 60 mg per day.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Alterations in the Somatotropic Axis",
                "Tight insulin therapy in fed critically ill adults affects the GH axis how?",
                [
                    "Increases GH resistance with lower IGF-1, IGFBP3, and ALS and higher GH",
                    "Normalizes IGF-1 by suppressing all GH secretion permanently",
                    "Has no effect on somatotropic hormones",
                    "Eliminates need for glucose monitoring",
                ],
                0,
                "Tight glucose control with insulin in a fed state increases GH resistance, suppressing IGF-1 and binding proteins while raising GH.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "by intensive insulin therapy in a fed state further increases GH resistance in both critically ill children and adults, with suppression of IGF1 and the ternary complex proteins IGFBP3 and ALS, and results in a concomitant increase in GH.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Alterations in the Thyroid Axis",
                "Prolonged ICU patient has very low T3, low TSH, and low T4. Central mechanism?",
                [
                    "Hyposecretion of TRH with absent pulsatile TSH secretion",
                    "Isolated primary thyroid gland destruction only",
                    "Excess dietary iodine is the sole cause",
                    "Pituitary TSH hypersecretion from thyroid resistance",
                ],
                0,
                "Prolonged illness further lowers T3 via virtually absent pulsatile TSH from hypothalamic TRH hyposecretion.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "In prolonged critical illness, alterations in peripheral metabolism often persist:  $ T_3 $ concentrations further decline due to the virtually absent pulsatile TSH secretion, and this results in low TSH and  $ T_4 $ concentrations.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "KEY POINTS",
                "An ICU director implements a glucose protocol. Minimum safety elements per chapter?",
                [
                    "Validated protocol, accurate frequent measurements, no insulin boluses",
                    "Capillary checks once daily with prn boluses",
                    "Target <70 mg/dL in all adults regardless of diabetes",
                    "Oral hypoglycemics as first-line in ventilated patients",
                ],
                0,
                "KEY POINTS mandate validated protocol, accurate frequent glucose measurement, and avoidance of insulin boluses for safe ICU glycemic control.",
                ref(
                    "KEY POINTS",
                    "Safe blood glucose control in critically ill patients requires a validated protocol, with accurate and frequent blood glucose measurements and avoidance of insulin boluses.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Conclusion",
                "A patient remains ventilated 4 weeks with wasting and immune dysfunction. Endocrine context?",
                [
                    "Prolonged illness endocrine profile may be maladaptive and contribute to catabolism",
                    "All endocrine changes normalize by day 7 in every ICU patient",
                    "Acute adaptive changes persist unchanged indefinitely without consequence",
                    "Neuroendocrine axes are unaffected by ICU length of stay",
                ],
                0,
                "Prolonged ICU dependence brings a maladaptive endocrine profile contributing to hypercatabolism and immune suppression.",
                ref(
                    "Conclusion",
                    "In patients who do not recover swiftly and remain dependent on intensive care for a prolonged period of time, a different endocrine profile develops, which may be maladaptive by contributing to the hypercatabolic phenotype and immune suppression associated with this condition.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "Acute critical illness: cortisol remains high while ACTH is low. Primary explanation?",
                [
                    "Suppressed cortisol breakdown plus altered binding proteins increasing free cortisol",
                    "Unlimited ACTH hypersecretion from pituitary adenoma",
                    "Complete adrenal cortex atrophy within hours",
                    "Isolated decrease in CRH with absent cortisol production",
                ],
                0,
                "ACTH-cortisol dissociation after the hyperacute phase reflects suppressed cortisol metabolism and altered CBG/albumin binding increasing free cortisol.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "Thereafter, ACTH concentrations rapidly decline to low levels, while cortisol concentrations remain persistently elevated.",
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
                "Acute critical illness is characterized by low thyroid hormone and IGF-1 and high cortisol.",
                True,
                "KEY POINTS explicitly describe this acute-phase endocrine pattern as presumably adaptive.",
                ref(
                    "KEY POINTS",
                    "Acute critical illness is characterized by low levels of thyroid hormone and insulin-like growth factor 1, and high levels of cortisol, which is presumably adaptive and mainly brought about by peripheral alterations in hormone metabolism.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Alterations in the Thyroid Axis",
                "Interventional studies supplementing thyroid hormone in the acute phase of critical illness have shown mortality benefit.",
                False,
                "Interventional thyroid hormone supplementation in acute critical illness has not shown outcome benefit.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "Interventional studies supplementing thyroid hormone in the acute phase of critical illness have not shown benefit on outcomes.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "The cosyntropin stimulation test identifies patients with septic shock who benefit from glucocorticoid treatment.",
                False,
                "Cosyntropin stimulation does not identify glucocorticoid-responsive patients; large RCTs showed no mortality benefit in low responders.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "The cosyntropin stimulation test does not identify patients who would benefit from treatment with glucocorticoids.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Alterations in the Somatotropic Axis",
                "High-dose GH treatment initiated after 5 to 7 days in expected long-stay critically ill patients increased mortality in RCTs.",
                True,
                "Two RCTs showed significantly increased mortality with high-dose GH in prolonged critically ill patients.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "two randomized controlled trials (RCTs) revealed that high-dose GH treatment, initiated after 5 to 7 days in expected long-stay critically ill patients, significantly increased mortality, which may be explained by GH overdosing in a state of recovered GH responsiveness.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Insulin Resistance and Stress Hyperglycemia",
                "The NICE-SUGAR RCT showed harm from tight glucose control compared with maintaining blood glucose below 180 mg/dL.",
                True,
                "NICE-SUGAR demonstrated harm with intensive versus conventional glucose control targeting <180 mg/dL.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "the NICE-SUGAR RCT subsequently showed harm by tight glucose control compared with maintaining blood glucose below 180 mg/dL.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Insulin Resistance and Stress Hyperglycemia",
                "Insulin boluses are preferred over continuous infusion to rapidly reach glucose targets in critically ill patients.",
                False,
                "Continuous IV insulin without boluses is preferred to avoid hypoglycemia and glucose fluctuations linked to poor outcomes.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "Insulin is preferably administered through continuous intravenous insulin infusion while avoiding boluses, to slowly progress toward blood glucose target and to avoid hypoglycemia and large glucose fluctuations, because both have been associated with poor outcomes.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Alterations in Vitamin D",
                "Large vitamin D supplementation RCTs in critically ill patients showed no clinical endpoint benefit despite raising 25OHD or active hormone.",
                True,
                "High-dose vitamin D RCTs increased metabolite levels without clinical benefit in deficient critically ill patients.",
                ref(
                    "Alterations in Vitamin D",
                    "Administration of much higher doses of vitamin  $ D_3 $ in large RCTs powered for clinical endpoints did significantly increase 25OHD or 1,25(OH) $ _2 $D in critically ill patients with baseline vitamin D deficiency, although there was no benefit on clinical endpoints.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "Recent evidence supports generalized glucocorticoid resistance as the uniform explanation for steroid response in all tissues during septic shock.",
                False,
                "Tissue-specific glucocorticoid availability and action argue against generalized glucocorticoid resistance in sepsis.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "Observations documenting tissue-specific alterations in local glucocorticoid availability and action, as well as differential responses associated with increased glucocorticoid availability in human critically ill patients and in a septic mouse model, argue against generalized glucocorticoid resistance in sepsis.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Alterations in the Thyroid Axis",
                "Fasting during critical illness evokes thyroid hormone metabolic changes thought to reflect an adaptive response preventing hypercatabolism.",
                True,
                "Fasting produces similar thyroid metabolic alterations considered adaptive against hypercatabolism.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "Of note, fasting evokes similar alterations in thyroid hormone metabolism and is thought to reflect an adaptive response preventing hypercatabolism.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Alterations in the Somatotropic Axis",
                "Dopamine administration centrally suppresses the somatotropic axis in critically ill patients.",
                True,
                "Dopamine used as vasoactive therapy centrally suppresses the somatotropic axis.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "The administration of dopamine treatment, commonly used as vasoactive strategy in the past, centrally suppresses the somatotropic axis.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Insulin Resistance and Stress Hyperglycemia",
                "A considerable proportion of critically ill patients may have previously unknown diabetes detectable by elevated admission HbA1c.",
                True,
                "Recent studies show many ICU patients have antecedent diabetes by elevated admission HbA1c.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "Moreover, recent studies have shown that a considerable amount of critically ill patients may have previously unknown antecedent diabetes mellitus, as derived from elevated HbA $ _{1c} $ levels on ICU admission.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Conclusion",
                "Illness-induced endocrine alterations often impede diagnosis of preexisting endocrine disease in the ICU.",
                True,
                "The conclusion states illness-induced alterations often impede diagnosis of preexisting endocrine disease.",
                ref(
                    "Conclusion",
                    "The illness-induced alterations often impede the diagnosis of preexisting endocrine disease.",
                ),
            ),
            tf(
                f"{p}-t13",
                "KEY POINTS",
                "The ideal blood glucose target in critically ill patients not receiving early parenteral nutrition has been definitively established.",
                False,
                "KEY POINTS state the ideal glucose target without early parenteral nutrition remains unclear.",
                ref(
                    "KEY POINTS",
                    "The ideal blood glucose target in critically ill patients not receiving early parenteral nutrition remains unclear.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Alterations in the Thyroid Axis",
                "Assertion: Low T3 in acute critical illness reflects euthyroid sick syndrome.",
                "Reason: Systemic inflammation and fasting accompanying severe illness trigger altered peripheral thyroid hormone metabolism.",
                0,
                "Both true and linked—inflammation and fasting drive the low T3 biochemical constellation of nonthyroidal illness.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "Triggers of this biochemical constellation are systemic inflammation and fasting accompanying",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "Assertion: Elevated cortisol in critical illness does not exclude adrenal insufficiency.",
                "Reason: High cortisol in critical illness always proves intact adrenal reserve.",
                2,
                "Assertion true; reason false—elevated cortisol reflects peripheral adaptations and random cortisol is hard to interpret.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "Hence, random cortisol measurements can be difficult to interpret because elevated cortisol concentrations do not exclude adrenal insufficiency.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Alterations in the Somatotropic Axis",
                "Assertion: High-dose GH increased mortality in long-stay critically ill patients.",
                "Reason: Peripheral GH responsiveness may recover, making GH overdosing hazardous.",
                0,
                "Both true and linked—recovered responsiveness may explain mortality from high-dose GH in prolonged illness.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "significantly increased mortality, which may be explained by GH overdosing in a state of recovered GH responsiveness.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Insulin Resistance and Stress Hyperglycemia",
                "Assertion: Tight glucose control showed benefit in Leuven RCTs.",
                "Reason: Leuven trials used early parenteral nutrition, a context in which tight control benefit was demonstrated.",
                0,
                "Both true and linked—benefit of tight control was tied to early parenteral nutrition feeding strategy.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "In this context, a benefit of tight glucose control was only demonstrated in a context of early parenteral nutrition supplementing insufficient enteral nutrition, $ ^{10-12,61} $",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Insulin Resistance and Stress Hyperglycemia",
                "Assertion: Hypoglycemia and large glucose fluctuations are associated with poor outcomes in critical illness.",
                "Reason: Insulin boluses are the preferred method to minimize glucose variability in ICU.",
                2,
                "Assertion true; reason false—boluses should be avoided; continuous infusion is preferred.",
                ref(
                    "Insulin Resistance and Stress Hyperglycemia",
                    "Insulin is preferably administered through continuous intravenous insulin infusion while avoiding boluses, to slowly progress toward blood glucose target and to avoid hypoglycemia and large glucose fluctuations, because both have been associated with poor outcomes.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Alterations in Vitamin D",
                "Assertion: Low vitamin D in acute critical illness is probably adaptive.",
                "Reason: All critically ill patients require high-dose vitamin D3 supplementation on ICU admission.",
                2,
                "Assertion true; reason false—acute low vitamin D does not require pharmacologic correction beyond maintenance dose.",
                ref(
                    "Alterations in Vitamin D",
                    "Altogether, current evidence suggests that low vitamin D concentrations are adaptive during acute critical illness and do not require pharmacologic correction on top of a normal maintenance dose.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "Assertion: ACTH declines while cortisol stays elevated after acute critical stress.",
                "Reason: Cortisol breakdown is suppressed after the hyperacute phase.",
                0,
                "Both true and linked—suppressed cortisol metabolism helps explain persistent hypercortisolemia with low ACTH.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "The persistent hypercortisolemia in the presence of suppressed ACTH (ACTH-cortisol dissociation) after the hyperacute phase is explained by suppressed breakdown of cortisol.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Alterations in the Thyroid Axis",
                "Assertion: Thyroid hormone should be supplemented in all acute critically ill patients with low T3.",
                "Reason: Acute thyroid alterations are assumed adaptive and supplementation trials showed no outcome benefit.",
                2,
                "Assertion false; reason true—acute low T3 is adaptive and supplementation has not helped outcomes.",
                ref(
                    "Alterations in the Thyroid Axis",
                    "In the acute phase of critical illness, these alterations are assumed to be adaptive. $ ^{2} $ Interventional studies supplementing thyroid hormone in the acute phase of critical illness have not shown benefit on outcomes.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "KEY POINTS",
                "Assertion: Prolonged critical illness causes central suppression of multiple pituitary axes.",
                "Reason: Central suppression improves rehabilitation without need for further study.",
                2,
                "Assertion true; reason false—central suppression may impair rehabilitation and treatment needs adequately powered trials.",
                ref(
                    "KEY POINTS",
                    "In patients with prolonged critical illness, a central suppression of the somatotropic, thyrotropic, and adrenocorticotropic axes progressively develops, which may impair rehabilitation, although treatment indications and regimens remain to be studied in adequately powered trials.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Alterations in the Somatotropic Axis",
                "Assertion: Acute critical illness features high GH with low IGF-1.",
                "Reason: GH secretion decreases to undetectable levels in the acute phase.",
                2,
                "Assertion true; reason false—acute illness increases GH secretion with peripheral resistance lowering IGF-1.",
                ref(
                    "Alterations in the Somatotropic Axis",
                    "In the acute phase of critical illness, growth hormone (GH) secretion increases, with increased pulse frequency and amplitude and elevated trough concentrations.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                "Assertion: Hydrocortisone RCTs in septic shock often shortened vasopressor duration.",
                "Reason: All hydrocortisone RCTs uniformly reduced mortality by 50%.",
                1,
                "Both true but not causally linked—vasopressor weaning is common but mortality benefit is inconsistent.",
                ref(
                    "Alterations in the Hypothalamic-Pituitary-Adrenal Axis",
                    "Although most RCTs demonstrated faster weaning of vasopressor support, which could be expected based on the well-known blood pressure-augmenting effects of steroids, only one RCT found significant mortality benefit.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Conclusion",
                "Assertion: Selected endocrine abnormalities may persist for years after critical illness.",
                "Reason: All neuroendocrine axes fully normalize within 48 hours of ICU discharge in every survivor.",
                2,
                "Assertion true per conclusion; reason false—some abnormalities may persist years after critical illness.",
                ref(
                    "Conclusion",
                    "In patients surviving critical illness, selected endocrine abnormalities may persist for years after randomization.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "48",
        "title": "Endocrine Disorders of Critical Illness",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Jan Gunst and Greet Van den Berghe",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_48_Endocrine_Disorders_of_Critical_Illness.md",
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
