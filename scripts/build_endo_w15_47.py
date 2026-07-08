#!/usr/bin/env python3
"""Generate Williams 15e module w15-47 — Acute and Chronic COVID-19 and the Endocrine System."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-47"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-47_Acute_and_Chronic_COVID19_and_the_Endocrine_System.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why SARS-CoV-2 can affect every endocrine tissue",
                "SARS-CoV-2 can target all endocrine tissues either directly or indirectly, with pituitary and thyroid damage underrecognized after infection or vaccination.",
                ref(
                    "KEY POINTS",
                    "SARS-CoV-2 can target all endocrine tissues either directly or indirectly.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "Why obesity and diabetes worsen COVID-19 severity",
                "Obesity and diabetes mellitus are major risk factors for disease severity and interact bidirectionally with viral infection.",
                ref(
                    "KEY POINTS",
                    "Obesity and diabetes mellitus are major risk factors for disease severity.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "How islet cells may be targeted causing new-onset diabetes",
                "Viral infection of islet cells expressing ACE2 may cause de novo diabetes mellitus beyond worsening of known diabetes.",
                ref(
                    "KEY POINTS",
                    "Islet cells may also be targeted by viral infection and this may cause de novo occurrence of diabetes mellitus.",
                ),
            ),
            note(
                f"{p}-n4",
                "Introduction and Overview of COVID-19 and Endocrine Disorders",
                "Why the endocrine system is involved in acute COVID-19",
                "The pituitary, thyroid, and pancreas can be targeted directly by SARS-CoV-2 and by the immune response; acute treatments can worsen metabolic derangements.",
                ref(
                    "Introduction and Overview of COVID-19 and Endocrine Disorders",
                    "Treatments for acute COVID-19 can worsen the metabolic response, but it is clear that the pituitary, thyroid, and pancreas can be targeted directly by the virus, as well as being involved in the immune response.",
                ),
            ),
            note(
                f"{p}-n5",
                "Post-Acute Sequelae of SARS-CoV-2",
                "How PASC endocrine manifestations complicate recovery",
                "PASC includes metabolic, thyroid, adrenal, and pituitary manifestations beyond glucose intolerance and T2DM, with variable presentation and duration.",
                ref(
                    "Introduction and Overview of COVID-19 and Endocrine Disorders",
                    "Other endocrine manifestations are just emerging, beyond the metabolic syndrome and T2DM, including autoimmune thyroid disease, adrenal insufficiency, and pituitary disease.",
                ),
            ),
            note(
                f"{p}-n6",
                "Prevalence of Diabetes Mellitus in COVID-19",
                "Why diabetes is a frequent COVID-19 comorbidity",
                "Diabetes prevalence in hospitalized COVID-19 patients ranges from 7.3% to 43.3% across cohorts; the typical hospitalized phenotype is an aged male with metabolic comorbidities.",
                ref(
                    "Prevalence of Diabetes Mellitus in COVID-19",
                    "Diabetes mellitus is one of the most frequent comorbidities in hospitalized COVID-19 patients ranging from 7.3% in China to 18% in South Korea and 43.3% in U.S. veterans.",
                ),
            ),
            note(
                f"{p}-n7",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "How hyperglycemia worsens pulmonary COVID-19 outcomes",
                "Hyperglycemia induces respiratory dysfunction and worsens pulmonary radiologic scores; poor glycemic control linearly relates to mortality when HbA1c exceeds 10%.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Hyperglycemia may also induce respiratory dysfunction that is worsened in patients with diabetes affected by COVID-19, who may show deteriorated pulmonary radiologic scores.",
                ),
            ),
            note(
                f"{p}-n8",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "Why insulin is preferred in hospitalized COVID-19 with dexamethasone",
                "Insulin is the most effective antihyperglycemic agent in seriously ill hospitalized COVID-19 patients, especially those on high-dose dexamethasone.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Insulin is the most effective antihyperglycemic agent in hospitalized seriously ill patients such as those with COVID-19, particularly when under high-dose dexamethasone treatment",
                ),
            ),
            note(
                f"{p}-n9",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "How metformin and statins may protect in COVID-19",
                "Continuing metformin and statins during hospitalization for COVID-19, when not contraindicated, may be associated with decreased disease severity and mortality.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Use of metformin and statins was reported to be associated with decreased disease severity and mortality, suggesting the opportunity to continue these treatments during hospitalization for COVID-19, if there are no specific contraindications.",
                ),
            ),
            note(
                f"{p}-n10",
                "COVID-19 and New-Onset Diabetes",
                "Why ACE2 on beta-cells enables direct pancreatic damage",
                "SARS-CoV-2 can directly damage pancreatic beta-cells that abundantly express ACE2 and/or increase insulin resistance, causing new-onset diabetes in previously nondiabetic patients.",
                ref(
                    "COVID-19 and New-Onset Diabetes",
                    "SARS-CoV-2 can directly damage pancreatic β-cells, which abundantly express the ACE2 receptor and/or increase insulin resistance.",
                ),
            ),
            note(
                f"{p}-n11",
                "COVID-19 and New-Onset Diabetes",
                "How cytokines and glucocorticoids drive acute hyperglycemia",
                "Overwhelming cytokine release and glucocorticoid therapy for moderate to severe COVID-19 can cause glucose intolerance and transient beta-cell dysfunction, especially in obesity.",
                ref(
                    "COVID-19 and New-Onset Diabetes",
                    "Overwhelming cytokine release can lead to glucose intolerance, as well as glucocorticoids that are used to treat moderate to severe infections.",
                ),
            ),
            note(
                f"{p}-n12",
                "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                "Why obese patients have worse COVID-19 outcomes",
                "Obesity alters pulmonary function, drives chronic inflammation, cytokine activation, and hypercoagulability, increasing ICU admission and mechanical ventilation risk.",
                ref(
                    "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                    "Obesity is also known to be a state of low-grade chronic inflammation, cytokine activation, with altered adiponectin versus leptin ratio, innate and adaptive immunity dysfunction, and hypercoagulability with increased risk of thrombosis, may all be relevant contributing factors to poor prognosis in obese COVID-19 patients.",
                ),
            ),
            note(
                f"{p}-n13",
                "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                "How elevated ACE2 in adipose tissue increases susceptibility",
                "Elevated ACE2 expression in adipose tissue may prolong SARS-CoV-2 exposure, making obese patients more susceptible and vulnerable to infection.",
                ref(
                    "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                    "Additionally, elevated expression of ACE2 in adipose tissue may lead to prolonged exposure to SARS-CoV-2 making obese patients more susceptible and vulnerable to the infection.",
                ),
            ),
            note(
                f"{p}-n14",
                "Hypocalcemia",
                "Why hypocalcemia predicts poor COVID-19 prognosis",
                "Hypocalcemia is highly prevalent in hospitalized COVID-19 patients, is associated with inflammatory markers, and independently predicts hospitalization, ICU admission, and mortality.",
                ref(
                    "Hypocalcemia",
                    "Hypocalcemia was also found to be an independent predictor of hospitalization.",
                ),
            ),
            note(
                f"{p}-n15",
                "Vitamin D and COVID-19",
                "How vitamin D modulates COVID-19 immune response",
                "Vitamin D regulates innate and adaptive immunity, may downregulate ACE2, and modulate proinflammatory cytokines that drive the cytokine storm.",
                ref(
                    "Vitamin D and COVID-19",
                    "Moreover, vitamin D may also play a further specific role in COVID-19 downregulating ACE2 and modulating proinflammatory cytokines, which may result in counteracting the cytokine storm.",
                ),
            ),
            note(
                f"{p}-n16",
                "Vertebral Fractures",
                "Why vertebral fractures predict COVID-19 mortality",
                "Opportunistic vertebral fractures on admission chest imaging were prevalent in 36% of hospitalized patients and predicted higher mortality and need for mechanical ventilation.",
                ref(
                    "Vertebral Fractures",
                    "Vertebral fractures detected opportunistically on cross-sectional chest x-rays performed at admission and submitted to morphometric analysis were reported to be highly prevalent (36%) in a single-center cohort of hospitalized COVID-19 patients",
                ),
            ),
            note(
                f"{p}-n17",
                "The Pituitary and COVID-19",
                "How SARS-CoV-2 targets the pituitary gland",
                "Autopsy studies detected SARS-CoV-2 in two-thirds of pituitary glands; ACE2 and TMPRSS2 expression in pituitary tissue enables direct involvement causing apoplexy, hyponatremia, and hypophysitis.",
                ref(
                    "The Pituitary and COVID-19",
                    "Recent autopsy studies detected SARS-CoV-2 antigens and its genome in two-thirds of pituitary glands from patients who died from COVID-19, but not in controls",
                ),
            ),
            note(
                f"{p}-n18",
                "The Pituitary and COVID-19",
                "Why hyponatremia occurs in hospitalized COVID-19",
                "Mild to moderate hyponatremia occurs in up to 50% of hospitalized COVID-19 patients, often from SIADH mediated by IL-6 and nonosmotic vasopressin secretion.",
                ref(
                    "The Pituitary and COVID-19",
                    "Hyponatremia was related to syndrome of inappropriate antidiuretic hormone (SIADH) possibly mediated by increased interleukin-6 (IL6) and consequent nonosmotic secretion of vasopressin.",
                ),
            ),
            note(
                f"{p}-n19",
                "Thyroid and COVID-19",
                "How subacute thyroiditis presents atypically in COVID-19",
                "COVID-19-related subacute thyroiditis is often painless, may show thyrotoxicosis without elevated thyroid autoantibodies, and can be followed by hypothyroidism.",
                ref(
                    "Thyroid and COVID-19",
                    "Subacute thyroiditis reported in several patients with COVID-19 was defined as atypical because it is painless and may be characterized by thyrotoxicosis followed in some instances by hypothyroidism without elevated thyroid autoantibodies.",
                ),
            ),
            note(
                f"{p}-n20",
                "Thyroid and COVID-19",
                "Why Graves disease can follow SARS-CoV-2 infection",
                "SARS-CoV-2 cytokine storm may trigger thyroid autoimmunity complicated by thyrotoxicosis, Graves ophthalmopathy, and primary hypothyroidism.",
                ref(
                    "Thyroid and COVID-19",
                    "Nevertheless, SARS-CoV-2 cytokine storm may be associated also with thyroid autoimmunity that may be complicated by thyrotoxicosis, Graves ophthalmopathy, and primary hypothyroidism.",
                ),
            ),
            note(
                f"{p}-n21",
                "Sex Hormones and COVID-19",
                "Why men have higher COVID-19 morbidity and mortality",
                "Men have higher odds of ICU admission (2.8–3.0) and death (1.4–1.7) versus women, partly from androgen-driven ACE2/TMPRSS2 transcription and weaker T-cell responses in men.",
                ref(
                    "Sex Hormones and COVID-19",
                    "However, there is evidence that men are at higher risk of COVID-19 morbidity and mortality, with an odds ratio of 2.8 to 3 and 1.4 to 1.7 for ICU admission and death in males versus females.",
                ),
            ),
            note(
                f"{p}-n22",
                "COVID-19 Vaccination and Endocrine Diseases",
                "How Graves disease can occur after COVID-19 vaccination",
                "Sporadic cases of subacute thyroiditis and Graves disease after vaccination are likely linked to autoimmune syndrome induced by adjuvants (ASIA), with distinctive PoVEO GD features in some series.",
                ref(
                    "COVID-19 Vaccination and Endocrine Diseases",
                    "In particular, in the former, several sporadic cases of subacute thyroiditis and of Graves disease occurring after COVID-19 vaccination were recently reported, likely linked to ASIA, that is, the autoimmune syndrome induced by adjuvants.",
                ),
            ),
            note(
                f"{p}-n23",
                "Definition and Prevalence",
                "Why PASC includes a metabolic endocrine cluster",
                "The N3C consortium algorithmically clustered PASC into cardiopulmonary, neurologic, and metabolic categories using ICD-10 code U09.9.",
                ref(
                    "Introduction and Overview of COVID-19 and Endocrine Disorders",
                    "The N3C consortium has algorithmically clustered three major categories of PASC using machine learning and the U09.9: cardiopulmonary, neurologic, and metabolic.",
                ),
            ),
            note(
                f"{p}-n24",
                "Metabolic Dysfunction",
                "How glucose intolerance persists after SARS-CoV-2 infection",
                "Retrospective cohort data show increased burden of glucose intolerance and antihyperglycemic medication use after infection, supporting metabolic dysfunction as a PASC manifestation.",
                ref(
                    "Metabolic Dysfunction",
                    "In respect to PASC, there is evidence from retrospective cohort studies that there is a higher frequency of glucose intolerance.",
                ),
            ),
            note(
                f"{p}-n25",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "How to manage T1DM during COVID-19 with fever",
                "T1DM patients with fever and hyperglycemia need close glucose and ketone monitoring with proactive insulin dose adjustment to maintain euglycemia.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Therefore, close monitoring of blood glucose and urinary ketones measurement is recommended in T1DM patients with fever and hyperglycemia who should also proactively adapt insulin (basal and/or bolus) dose to maintain euglycemia.",
                ),
            ),
            note(
                f"{p}-n26",
                "Summary",
                "Why the endocrine-COVID relationship is bidirectional",
                "Coexisting endocrine morbidity enhances acute infection severity and may predispose to long COVID; obesity and T2DM chronic inflammation coupled to viral persistence drive greater morbidity.",
                ref(
                    "Endocrine Determinants of PASC",
                    "As noted earlier in this chapter, the relationship between the body's endocrine systems and the virus is bidirectional, such that coexisting morbidity enhances further the likelihood of acute infection severity and may predispose to long COVID.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Prevalence of Diabetes Mellitus in COVID-19",
                "A 68-year-old man with type 2 diabetes is hospitalized with COVID-19 pneumonia. His wife asks whether diabetes increased his chance of catching SARS-CoV-2. Best answer?",
                [
                    "Diabetes does not increase infection risk but worsens clinical course",
                    "Diabetes doubles the risk of contracting SARS-CoV-2",
                    "Only type 1 diabetes increases infection susceptibility",
                    "Diabetes protects against severe COVID-19",
                ],
                0,
                "There is no evidence diabetic patients are at greater risk of contracting SARS-CoV-2; however, clinical course is worse.",
                ref(
                    "Prevalence of Diabetes Mellitus in COVID-19",
                    "There is no evidence, however, that diabetic patients are at greater risk of contracting SARS-CoV-2. Rather, the clinical course is worse (see following discussion).",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "A hospitalized COVID-19 patient with T2DM on high-dose dexamethasone has persistent hyperglycemia. Most appropriate inpatient glucose management?",
                [
                    "Insulin as the most effective antihyperglycemic agent",
                    "Oral metformin monotherapy despite NPO status",
                    "Withhold all glucose-lowering therapy during steroids",
                    "Sulfonylureas as first-line in critically ill patients",
                ],
                0,
                "Insulin is most effective in seriously ill hospitalized COVID-19 patients, especially on high-dose dexamethasone.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Insulin is the most effective antihyperglycemic agent in hospitalized seriously ill patients such as those with COVID-19, particularly when under high-dose dexamethasone treatment",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "A man with T2DM admitted for COVID-19 is on home metformin and atorvastatin without contraindications. Hospitalist asks about continuing them. Best advice?",
                [
                    "Continue metformin and statin if no contraindications",
                    "Stop both because they worsen COVID-19 outcomes",
                    "Continue statin only; metformin is always harmful in hospital",
                    "Stop statin because it increases ACE inhibitor mortality",
                ],
                0,
                "Metformin and statin use were associated with decreased disease severity and mortality; continue if not contraindicated.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Use of metformin and statins was reported to be associated with decreased disease severity and mortality, suggesting the opportunity to continue these treatments during hospitalization for COVID-19, if there are no specific contraindications.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "COVID-19 and New-Onset Diabetes",
                "A previously nondiabetic 45-year-old obese man develops hyperglycemia and DKA during acute COVID-19. Most likely mechanism?",
                [
                    "Direct beta-cell ACE2-mediated damage plus insulin resistance",
                    "Isolated autoimmune destruction unrelated to infection",
                    "Dexamethasone is the only possible cause of hyperglycemia",
                    "COVID-19 never causes new-onset diabetes",
                ],
                0,
                "SARS-CoV-2 can damage ACE2-expressing beta-cells and increase insulin resistance, causing new-onset diabetes.",
                ref(
                    "COVID-19 and New-Onset Diabetes",
                    "New-onset diabetes in COVID-19 patients who were previously nondiabetic has been widely reported, leading to the hypothesis of a potential diabetogenic action of SARS-CoV-2.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                "A 42-year-old woman with BMI 38 kg/m² tests positive for SARS-CoV-2 in outpatient clinic. Compared with normal-weight peers, her risk profile includes?",
                [
                    "Higher risk of hospitalization, ICU care, and mechanical ventilation",
                    "Lower risk of any respiratory complication",
                    "Identical outcomes because obesity is protective",
                    "Only increased infection risk with no severity effect",
                ],
                0,
                "Meta-analyses show obese patients at increased risk of hospitalization, ICU admission, and mechanical ventilation (OR 1.39–2.4).",
                ref(
                    "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                    "Furthermore, several meta-analyses pointed to obese people as being at increased risk of poor outcomes, including hospitalization, admission in ICU, and need for mechanical ventilation (odds ratio 1.39–2.4).",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Hypocalcemia",
                "A hospitalized COVID-19 patient has low ionized calcium and poor prognosis markers. Clinical significance?",
                [
                    "Hypocalcemia independently predicts ICU admission and mortality",
                    "Hypocalcemia is benign and never requires monitoring",
                    "Only total calcium matters; ionized calcium is irrelevant",
                    "Hypercalcemia is the typical COVID-19 mineral disturbance",
                ],
                0,
                "Hypocalcemia is highly prevalent, associated with inflammation, and predicts ICU admission and mortality; ionized calcium is important.",
                ref(
                    "Hypocalcemia",
                    "Hypocalcemia was also found to be an independent predictor of hospitalization.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Vitamin D and COVID-19",
                "An elderly patient with diabetes and obesity in a vitamin D–deficient region asks about supplementation before potential COVID-19 exposure. Evidence-based counseling?",
                [
                    "Reinstating adequate vitamin D may have preventive role in high-risk individuals",
                    "Vitamin D has no immune relevance in respiratory infections",
                    "High-dose vitamin D always cures hospitalized COVID-19",
                    "Supplementation is contraindicated in all diabetic patients",
                ],
                0,
                "In high-risk individuals with diabetes and obesity in vitamin D–deficient areas, supplementation to adequate status may have preventive role.",
                ref(
                    "Vitamin D and COVID-19",
                    "However, in individuals at high concomitant risk of COVID-19 and hypovitaminosis D (elderly with diabetes and obesity), particularly if living in areas characterized by widespread vitamin D deficiency, reinstating through supplementation adequate vitamin D status may have a preventive role in the context of COVID-19",
                ),
            ),
            mcq(
                f"{p}-m8",
                "The Pituitary and COVID-19",
                "A man with COVID-19 develops sudden headache, vision loss, and hypotension. MRI shows pituitary hemorrhage. Association with COVID-19?",
                [
                    "Pituitary apoplexy reported with or without preexisting adenoma",
                    "Pituitary apoplexy never occurs with SARS-CoV-2 infection",
                    "Only patients with acromegaly can develop apoplexy in COVID-19",
                    "Apoplexy is exclusively a postvaccination phenomenon",
                ],
                0,
                "Several case series report pituitary apoplexy with COVID-19, with or without preexisting pituitary adenoma.",
                ref(
                    "The Pituitary and COVID-19",
                    "Recently, several series of cases of pituitary apoplexy in association with COVID-19 were reported in the context of the neurovascular manifestations of COVID-19, either in the presence of or without a preexisting pituitary adenoma.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "The Pituitary and COVID-19",
                "A COVID-19 patient has sodium 132 mmol/L, euvolemia, and concentrated urine. Most likely mechanism?",
                [
                    "SIADH mediated by IL-6 and nonosmotic vasopressin secretion",
                    "Primary adrenal hyperplasia with hypernatremia",
                    "Diabetes insipidus from SARS-CoV-2 in the kidney only",
                    "Excessive salt supplementation in all ICU patients",
                ],
                0,
                "Hyponatremia in up to 50% of hospitalized COVID-19 patients is often SIADH related to IL-6 and nonosmotic vasopressin release.",
                ref(
                    "The Pituitary and COVID-19",
                    "Hyponatremia was related to syndrome of inappropriate antidiuretic hormone (SIADH) possibly mediated by increased interleukin-6 (IL6) and consequent nonosmotic secretion of vasopressin.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Thyroid and COVID-19",
                "A woman recovers from COVID-19 and presents with painless thyrotoxicosis, low radioiodine uptake, and normal thyroid antibodies. Diagnosis?",
                [
                    "Atypical subacute (postviral) thyroiditis",
                    "Graves disease with high radioiodine uptake",
                    "Factitious thyrotoxicosis from levothyroxine",
                    "Primary hypothyroidism with low TSH",
                ],
                0,
                "COVID-19 subacute thyroiditis is often painless, thyrotoxic, with low uptake and without elevated autoantibodies.",
                ref(
                    "Thyroid and COVID-19",
                    "Subacute thyroiditis reported in several patients with COVID-19 was defined as atypical because it is painless and may be characterized by thyrotoxicosis followed in some instances by hypothyroidism without elevated thyroid autoantibodies.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Thyroid and COVID-19",
                "A critically ill ICU patient with COVID-19 has low T3, normal-low TSH, and no clinical hypothyroidism. Interpretation?",
                [
                    "Euthyroid sick (nonthyroidal illness) syndrome",
                    "Primary autoimmune hypothyroidism requiring levothyroxine",
                    "TSH-secreting pituitary adenoma",
                    "Graves disease with suppressed TSH",
                ],
                0,
                "Euthyroid sick syndrome is frequent in hospitalized and ICU COVID-19 patients with low-normal thyroid function and TSH without clinical hypothyroidism.",
                ref(
                    "Thyroid and COVID-19",
                    "Euthyroid sick syndrome was frequently observed in hospitalized COVID-19 patients, particularly when admitted in ICUs, who show low to normal thyroid function and thyroid-stimulating hormone (TSH) without clinical manifestations of hypothyroidism.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "COVID-19 Vaccination and Endocrine Diseases",
                "A 52-year-old man develops Graves disease 3 weeks after mRNA COVID-19 vaccination. Compared with unvaccinated-onset Graves, PoVEO GD features may include?",
                [
                    "Older age, male sex, and rapid response to methimazole",
                    "Exclusive occurrence only in adolescent females",
                    "Permanent resistance to all antithyroid drugs",
                    "Mandatory discontinuation of all future vaccines",
                ],
                0,
                "PoVEO GD patients were older, more frequently male, and showed rapid hormonal/immune response to methimazole with lower TRAb titers.",
                ref(
                    "Graves Disease",
                    "These included greater age at onset, male sex, and rapid hormonal and immune response to methimazole.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Sex Hormones and COVID-19",
                "Researchers study why men fare worse with COVID-19. Mechanistic contributor in lung epithelium?",
                [
                    "Androgen-influenced transcription of ACE2 and TMPRSS2",
                    "Estrogen suppression of all immune responses in women only",
                    "Progesterone blocks all viral entry universally",
                    "Sex hormones have no role in viral entry receptors",
                ],
                0,
                "SARS-CoV-2 enters via ACE2 and TMPRSS2; androgens influence their transcription in lung epithelial cells.",
                ref(
                    "Sex Hormones and COVID-19",
                    "SARS-CoV-2 enters the cells through ACE2 and TMPRSS2, the transcription of which is influenced by androgens in epithelial cells of the lung.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "A T1DM teenager with COVID-19 fever has glucose 380 mg/dL. Immediate priorities beyond insulin?",
                [
                    "Urinary ketone monitoring and proactive insulin adjustment",
                    "Withhold insulin until fever resolves",
                    "High-dose sulfonylurea to replace insulin",
                    "No ketone testing needed in type 1 diabetes",
                ],
                0,
                "T1DM patients with fever and hyperglycemia need glucose and ketone monitoring with proactive insulin dose adaptation.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Therefore, close monitoring of blood glucose and urinary ketones measurement is recommended in T1DM patients with fever and hyperglycemia who should also proactively adapt insulin (basal and/or bolus) dose to maintain euglycemia.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Vertebral Fractures",
                "Admission chest radiograph in a COVID-19 patient shows morphometric vertebral fractures. Clinical implication?",
                [
                    "Higher mortality risk and increased mechanical ventilation need",
                    "Fractures exclude any need for respiratory support",
                    "Vertebral fractures are absent in COVID-19 cohorts",
                    "Antiosteoporotic therapy must be stopped during COVID-19",
                ],
                0,
                "Vertebral fractures were prevalent on admission imaging and predicted higher mortality and mechanical ventilation requirement.",
                ref(
                    "Vertebral Fractures",
                    "Moreover, COVID-19 patients with vertebral fractures, particularly if severe, at hospital referral showed a higher mortality risk compared with subjects without vertebral fractures.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "The Pituitary and COVID-19",
                "A patient with active Cushing disease contracts COVID-19. Why might severity be increased?",
                [
                    "Glucocorticoid excess causes immunosuppression plus metabolic comorbidities",
                    "Cushing disease is protective against all infections",
                    "Excess cortisol enhances viral clearance exclusively",
                    "Cushing has no overlap with obesity or diabetes risk",
                ],
                0,
                "Cushing disease increases infection risk via glucocorticoid-mediated immunosuppression and comorbidities including hypertension, obesity, and diabetes.",
                ref(
                    "The Pituitary and COVID-19",
                    "Patients with Cushing disease were reported to be at higher risk of SARS-CoV-2 infection and COVID-19 due to the excess glucocorticoid-mediated immunosuppressive effect.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "The Pituitary and COVID-19",
                "A patient with primary adrenal insufficiency on hydrocortisone develops COVID-19. Key management principle from Italian cohort data?",
                [
                    "Optimal hormonal management and sick-day rules are crucial",
                    "Stop all glucocorticoids immediately to fight infection",
                    "Adrenal insufficiency always causes worse COVID-19 outcomes",
                    "No monitoring differs from the general population",
                ],
                0,
                "With strict follow-up and sick-day rules, adrenal insufficiency patients had similar COVID-19 outcomes to controls.",
                ref(
                    "The Pituitary and COVID-19",
                    "These data, which were obtained in patients submitted to strict follow-up, monitoring, and adequate training for infection prevention, suggested that optimal hormonal management of this condition, including correct and early application of sick-day rules, can be crucial in prevention of COVID-19 in these patients.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Definition and Prevalence",
                "A patient has fatigue and brain fog 6 weeks after mild COVID-19. How is PASC/long COVID currently defined for coding?",
                [
                    "Ongoing symptoms ≥4 weeks after acute infection (ICD-10 U09.9)",
                    "Only symptoms within 48 hours of PCR positivity",
                    "PASC requires prior ICU admission exclusively",
                    "No ICD code exists for post-COVID conditions",
                ],
                0,
                "PASC/long COVID is defined as ongoing, relapsing, or new symptoms ≥4 weeks after acute infection; ICD-10 U09.9 was recognized October 2021.",
                ref(
                    "Definition and Prevalence",
                    "As such, PASC or long COVID is now defined by ongoing, relapsing, or new symptoms or other health effects occurring after the acute phase of SARS-CoV-2 infection (i.e., present 4 or more weeks after the acute infection).",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Metabolic Dysfunction",
                "A COVID-19 survivor without prior diabetes develops persistent hyperglycemia months later. Supporting epidemiologic evidence?",
                [
                    "Increased incident diabetes burden in long COVID cohort studies",
                    "Diabetes never occurs after acute COVID-19 resolves",
                    "Only children develop post-COVID glucose abnormalities",
                    "Glucose intolerance always resolves within 48 hours",
                ],
                0,
                "Retrospective cohort studies show higher frequency of glucose intolerance and antihyperglycemic medication use after infection.",
                ref(
                    "Metabolic Dysfunction",
                    "Xie and Al-Aly demonstrated an increased burden of disease related to glucose intolerance and antihyperglycemic medications from electronic health records at the Veterans Administration Hospital.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Pathophysiology of Metabolic Dysfunction in PASC",
                "Researchers study adipose tissue in PASC. Finding supporting chronic metabolic inflammation?",
                [
                    "Reduced adiponectin-to-leptin ratio in PASC patients",
                    "Elevated adiponectin with suppressed leptin universally",
                    "No viral or inflammatory signals in adipose tissue",
                    "Adipose tissue is spared in all SARS-CoV-2 infections",
                ],
                0,
                "Several studies suggest reduced adiponectin-to-leptin ratio in PASC, reflecting inflammatory adipose dysfunction.",
                ref(
                    "Pathophysiology of Metabolic Dysfunction in PASC",
                    "Several studies have suggested that the ratio of adiponectin to leptin is reduced in patients with PASC.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "COVID-19 Vaccination and Endocrine Diseases",
                "A teenager develops new-onset T1DM with ketoacidosis shortly after COVID-19 vaccination. Reported features include?",
                [
                    "Loss of insulin secretion, autoantibody positivity, and at-risk haplotypes",
                    "Isolated type 2 diabetes without any autoimmune markers",
                    "Vaccination universally prevents all diabetes",
                    "Hyperglycemia only occurs before vaccination never after",
                ],
                0,
                "Case reports describe new-onset T1DM after vaccination with loss of endogenous insulin, autoantibodies, and at-risk haplotypes.",
                ref(
                    "COVID-19 Vaccination and Endocrine Diseases",
                    "Loss of endogenous insulin secretion, positivity for autoantibodies, and specific at-risk haplotypes were reported in those cases.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "A diabetic COVID-19 inpatient has severe retinopathy. Independent risk associated with retinopathy?",
                [
                    "Higher risk of intubation, possibly reflecting microvascular/endothelial damage",
                    "Lower risk of any respiratory intervention",
                    "Retinopathy is unrelated to COVID-19 severity",
                    "Retinopathy mandates stopping all antihypertensives",
                ],
                0,
                "In hospitalized COVID-19 patients with poorly controlled diabetes, retinopathy was independently associated with higher intubation risk.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "In fact, in hospitalized COVID-19 patients with poorly controlled diabetes, retinopathy was independently associated with a higher risk of intubation.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                "An outpatient with obesity tests positive for SARS-CoV-2. Spanish cohort data on infection risk?",
                [
                    "Obesity-associated increased infection hazard ratio ~1.23",
                    "Obesity eliminates any risk of infection",
                    "Only underweight patients are susceptible",
                    "BMI has no epidemiologic association with infection",
                ],
                0,
                "A large Spanish outpatient cohort reported obesity-associated increased SARS-CoV-2 infection risk (HR 1.23).",
                ref(
                    "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                    "A study of a large Spanish cohort of persons diagnosed in an outpatient setting with COVID-19 reported an obesity-associated increased risk of SARS-CoV-2 infection (hazard ratio 1.23 [1.21–1.25]).",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Hypocalcemia",
                "A post-thyroidectomy patient with mild hypoparathyroidism is admitted with COVID-19. Calcium management priority?",
                [
                    "Strict calcium monitoring; do not discontinue calcium supplements",
                    "Stop all calcium to avoid hypercalcemia regardless of levels",
                    "Hypoparathyroidism is irrelevant during COVID-19 hospitalization",
                    "Only intravenous phosphate is needed for all hypocalcemia",
                ],
                0,
                "Postsurgical hypoparathyroidism patients with COVID-19 need strict calcium monitoring; calcium should not be discontinued or downtitrated.",
                ref(
                    "Hypocalcemia",
                    "Therefore, people with postsurgical hypoparathyroidism, also if mild and untreated, and particularly if obese/overweight, who are infected with SARS-CoV-2 should undergo strict calcium monitoring on hospital admission and during hospitalization.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Thyroid and COVID-19",
                "A hyperthyroid patient starts methimazole during the COVID-19 pandemic. Monitoring concern?",
                [
                    "Agranulocytosis symptoms may overlap with COVID-19 infection",
                    "Methimazole cannot cause any hematologic side effects",
                    "COVID-19 prevents all antithyroid drug toxicity",
                    "No monitoring is needed for new methimazole starts",
                ],
                0,
                "Agranulocytosis from antithyroid drugs may overlap with COVID-19 symptoms; close monitoring is suggested.",
                ref(
                    "Thyroid and COVID-19",
                    "Symptoms of agranulocytosis (a rare side effect of antithyroid drugs used in the treatment of Graves disease) may overlap with those of COVID-19, and therefore close monitoring is suggested in hyperthyroid patients starting medical treatment during the COVID-19 pandemic.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "KEY POINTS",
                "A clinician summarizes endocrine priorities in long COVID. Which statement is best supported?",
                [
                    "Low vitamin D is linked to acute outcomes, long COVID, and weaker vaccine immune persistence",
                    "Vitamin D excess is the main driver of PASC thyroid disease",
                    "Endocrine tissues are spared in chronic COVID-19",
                    "Vaccination has no reported endocrine adverse effects",
                ],
                0,
                "KEY POINTS note low vitamin D associations with acute outcomes, long COVID, and reduced vaccine immune persistence.",
                ref(
                    "KEY POINTS",
                    "Low vitamin D levels have been associated with acute COVID-19 outcomes, long COVID occurrence, and decreased persistence of immune response to COVID-19 vaccination.",
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
                "Thyroid and pituitary damage after SARS-CoV-2 infection or vaccination is underrecognized.",
                True,
                "KEY POINTS explicitly state thyroid and pituitary damage is underrecognized after infection/vaccination.",
                ref(
                    "KEY POINTS",
                    "Thyroid and pituitary damage is underrecognized after SARS-CoV-2 infection/vaccination.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Prevalence of Diabetes Mellitus in COVID-19",
                "Diabetic patients are at greater risk of contracting SARS-CoV-2 than nondiabetic individuals.",
                False,
                "There is no evidence diabetic patients have greater infection risk; clinical course is worse once infected.",
                ref(
                    "Prevalence of Diabetes Mellitus in COVID-19",
                    "There is no evidence, however, that diabetic patients are at greater risk of contracting SARS-CoV-2. Rather, the clinical course is worse (see following discussion).",
                ),
            ),
            tf(
                f"{p}-t3",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "Treatment of diabetes with ACE inhibitors was associated with increased COVID-19 mortality.",
                False,
                "Antihypertensive therapy including ACE inhibitors was not associated with increased mortality.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Treatment of patients with diabetes with antihypertensive drugs, including ACE inhibitors, was not associated with increased mortality.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                "Obesity prevalence in hospitalized COVID-19 patients admitted to ICU may reach approximately 41% to 43%.",
                True,
                "Meta-analysis reported 32% obesity in hospitalized patients, rising to 41%–43% in ICU/mechanical ventilation subsets.",
                ref(
                    "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                    "In a recent meta-analysis of 19 studies 32% prevalence of obesity in hospitalized COVID-19 patients increasing to 41% and 43% when COVID-19 patients admitted to intensive care or needing invasive mechanical ventilation were considered, respectively.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Hypocalcemia",
                "Hypocalcemia may be more frequent in hospitalized COVID-19 patients than in non-COVID-19 hospitalized patients.",
                True,
                "Studies suggested hypocalcemia as a distinctive feature of COVID-19 hospitalization.",
                ref(
                    "Hypocalcemia",
                    "Finally, it was suggested that hypocalcemia may represent a peculiar feature of COVID-19 being more frequent than in non-COVID-19-hospitalized patients.",
                ),
            ),
            tf(
                f"{p}-t6",
                "The Pituitary and COVID-19",
                "Pituitary hormone mRNA and regulatory genes were suppressed in COVID-19 autopsy cases independently of virus detection in the gland.",
                True,
                "Autopsy studies found suppressed pituitary hormone genes in all COVID-19 cases regardless of viral positivity.",
                ref(
                    "The Pituitary and COVID-19",
                    "whereas pituitary hormone mRNA and their regulatory genes were found to be suppressed in all COVID-19 cases independently from virus positivity.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Thyroid and COVID-19",
                "COVID-19-related subacute thyroiditis is typically painful with classic elevated sedimentation rate presentation.",
                False,
                "COVID-19 subacute thyroiditis is defined as atypical because it is often painless.",
                ref(
                    "Thyroid and COVID-19",
                    "Subacute thyroiditis reported in several patients with COVID-19 was defined as atypical because it is painless",
                ),
            ),
            tf(
                f"{p}-t8",
                "Sex Hormones and COVID-19",
                "Women with COVID-19 appeared to have more effective T-cell responses than men.",
                True,
                "Sex-differential immune responses include more effective T-cell response in women with COVID-19.",
                ref(
                    "Sex Hormones and COVID-19",
                    "Women with COVID-19 appeared to have more effective T-cell response than men.",
                ),
            ),
            tf(
                f"{p}-t9",
                "COVID-19 Vaccination and Endocrine Diseases",
                "There is no evidence that osteoporosis treatments such as denosumab predispose to severe COVID-19.",
                True,
                "Chapter notes no evidence that denosumab or antiosteoporotic therapy increases severe COVID-19 risk.",
                ref(
                    "Vertebral Fractures",
                    "In regard to this drug there is no evidence that osteoporosis treatments predispose to severe COVID-19.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Definition and Prevalence",
                "Estimated PASC prevalence in cross-sectional studies ranges from approximately 10% to 30% of acute SARS-CoV-2 infections.",
                True,
                "Several studies estimate 10%–30% of acute infections develop PASC symptoms.",
                ref(
                    "Definition and Prevalence",
                    "Several cross-sectional and longitudinal studies have estimated that 10% to 30% of patients with acute SARS-CoV-2 will develop symptoms that could be considered as PASC.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Pathophysiology of Metabolic Dysfunction in PASC",
                "There is increased incidence of type 1 diabetes after SARS-CoV-2 infection in children.",
                True,
                "Pediatric data show increased T1DM incidence after SARS-CoV-2 infection.",
                ref(
                    "Pathophysiology of Metabolic Dysfunction in PASC",
                    "In regard to the pancreas, it is notable that there is an increased incidence of T1DM after SARS-CoV-2 infections in children.",
                ),
            ),
            tf(
                f"{p}-t12",
                "COVID-19 Vaccination and Endocrine Diseases",
                "Patients with hypovitaminosis D may have reduced persistency of immune response to COVID-19 vaccination.",
                True,
                "Recent data link low vitamin D to impaired long-term vaccine immune response.",
                ref(
                    "COVID-19 Vaccination and Endocrine Diseases",
                    "Finally, it was recently reported that patients with hypovitaminosis D may have reduced persistency of immune response to COVID-19 vaccination.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Summary",
                "Obesity complicates acute COVID-19 and likely contributes to postacute sequelae of SARS-CoV-2.",
                True,
                "Summary states obesity complicates acute course and likely contributes to PASC.",
                ref(
                    "Summary",
                    "Obesity complicates the clinical course of acute COVID-19 and likely contributes to postacute sequelae of SARS-CoV-2.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "KEY POINTS",
                "Assertion: Islet cells may be targeted by SARS-CoV-2 causing new-onset diabetes.",
                "Reason: Beta-cells abundantly express ACE2 receptor enabling direct viral injury.",
                0,
                "Both true and linked—ACE2-expressing beta-cells can be directly damaged, supporting new-onset diabetes.",
                ref(
                    "COVID-19 and New-Onset Diabetes",
                    "SARS-CoV-2 can directly damage pancreatic β-cells, which abundantly express the ACE2 receptor and/or increase insulin resistance.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "Assertion: Insulin is the most effective antihyperglycemic agent in hospitalized COVID-19 patients on dexamethasone.",
                "Reason: Dexamethasone eliminates all need for glucose monitoring in diabetes.",
                2,
                "Assertion true; reason false—dexamethasone worsens hyperglycemia and increases insulin requirements.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Current glycometabolic control and fluctuations of blood glucose during the first days of hospitalization were reported to be determinants of length of stay, ICU requirement, and mortality, particularly in patients treated with high-dose glucocorticoids and consequent need of concomitant intensive insulin treatment.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                "Assertion: Obese patients are at increased risk of ICU admission with COVID-19.",
                "Reason: Obesity improves pulmonary reserve and reduces pneumonia risk.",
                2,
                "Assertion true; reason false—obesity impairs pulmonary function and worsens outcomes.",
                ref(
                    "Impact of Obesity on Susceptibility to SARS-CoV-2 and on Clinical Outcome of Patients With Acute COVID-19",
                    "It is well known that obesity, particularly when severe, is commonly associated with altered pulmonary function, pneumonia, and respiratory failure.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Vitamin D and COVID-19",
                "Assertion: Low vitamin D status predicts severity of COVID-19.",
                "Reason: Low vitamin D is only a consequence of illness and can never influence outcomes.",
                2,
                "Assertion true; reason false—whether marker or causal remains debated, but low vitamin D consistently predicts severity.",
                ref(
                    "Vitamin D and COVID-19",
                    "Low vitamin D status was consistently reported to predict severity of COVID-19 in terms of clinical outcomes and lung involvement (as defined by chest computed tomography stages) and even mortality.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "The Pituitary and COVID-19",
                "Assertion: SARS-CoV-2 can involve the pituitary gland directly.",
                "Reason: Pituitary tissue expresses ACE2 and TMPRSS2 receptors.",
                0,
                "Both true and linked—receptor expression enables direct pituitary involvement.",
                ref(
                    "The Pituitary and COVID-19",
                    "This direct involvement of the gland in COVID-19 is likely due to the expression of ACE2 and TMPRSS2 receptors in pituitary tissue.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Thyroid and COVID-19",
                "Assertion: Graves disease can occur after SARS-CoV-2 infection.",
                "Reason: SARS-CoV-2 cytokine storm can be associated with thyroid autoimmunity and thyrotoxicosis.",
                0,
                "Both true and causally linked—immune mechanisms after infection can trigger Graves/hyperthyroidism.",
                ref(
                    "Thyroid and COVID-19",
                    "Nevertheless, SARS-CoV-2 cytokine storm may be associated also with thyroid autoimmunity that may be complicated by thyrotoxicosis, Graves ophthalmopathy, and primary hypothyroidism.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "COVID-19 Vaccination and Endocrine Diseases",
                "Assertion: Graves disease has been reported after COVID-19 vaccination.",
                "Reason: Vaccination only causes hypothyroidism and never hyperthyroidism.",
                2,
                "Assertion true; reason false—both subacute thyroiditis and Graves disease reported postvaccination.",
                ref(
                    "COVID-19 Vaccination and Endocrine Diseases",
                    "several sporadic cases of subacute thyroiditis and of Graves disease occurring after COVID-19 vaccination were recently reported",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Sex Hormones and COVID-19",
                "Assertion: Men have higher COVID-19 mortality than women.",
                "Reason: Women have less effective T-cell responses to SARS-CoV-2 than men.",
                2,
                "Assertion true; reason false—women showed more effective T-cell responses than men.",
                ref(
                    "Sex Hormones and COVID-19",
                    "Women with COVID-19 appeared to have more effective T-cell response than men.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                "Assertion: Metformin use may be associated with decreased COVID-19 mortality in diabetes.",
                "Reason: Metformin must always be stopped in all hospitalized COVID-19 patients.",
                2,
                "Assertion true; reason false—metformin may be continued when no contraindications exist.",
                ref(
                    "Increased Risk of Morbidity and Mortality in Patients With Diabetes and COVID-19",
                    "Use of metformin and statins was reported to be associated with decreased disease severity and mortality, suggesting the opportunity to continue these treatments during hospitalization for COVID-19, if there are no specific contraindications.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Hypocalcemia",
                "Assertion: Hypocalcemia is highly prevalent in hospitalized COVID-19 patients.",
                "Reason: Hypocalcemia in COVID-19 is exclusively caused by hyperparathyroidism.",
                2,
                "Assertion true; reason false—mechanisms include vitamin D deficiency, impaired PTH response, inflammation, and malnutrition.",
                ref(
                    "Hypocalcemia",
                    "Mechanistically, widespread vitamin D deficiency associated with an impaired PTH compensatory response may predispose to the occurrence of hypocalcemia",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Endocrine Determinants of PASC",
                "Assertion: Obesity and T2DM predispose to greater COVID-19 morbidity and may contribute to long COVID.",
                "Reason: Chronic inflammation and viral persistence in metabolic tissues may drive sustained immune dysregulation.",
                0,
                "Both true and linked—preexisting inflammatory metabolic state plus viral persistence contributes to acute and chronic morbidity.",
                ref(
                    "Endocrine Determinants of PASC",
                    "Particularly for obese and T2DM patients, the preexistence of a chronic inflammatory state, with high cytokine and adipokine levels, coupled to viral persistence and hyperglycemia, almost certainly contributes to the greater morbidity and mortality from COVID-19.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Definition and Prevalence",
                "Assertion: PASC symptoms may persist 4 or more weeks after acute SARS-CoV-2 infection.",
                "Reason: PASC can only be diagnosed when PCR remains positive for at least 6 months.",
                2,
                "Assertion true per U09.9 definition; reason false—PASC is defined by persistent symptoms after acute phase, not ongoing PCR positivity.",
                ref(
                    "Definition and Prevalence",
                    "As such, PASC or long COVID is now defined by ongoing, relapsing, or new symptoms or other health effects occurring after the acute phase of SARS-CoV-2 infection (i.e., present 4 or more weeks after the acute infection).",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "47",
        "title": "Acute and Chronic COVID-19 and the Endocrine System",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Andrea Giustina and Clifford J. Rosen",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_47_Acute_and_Chronic_COVID19_and_the_Endocrine_System.md",
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
