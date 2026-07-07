#!/usr/bin/env python3
"""Generate Williams 15e module w15-10 — Hyperthyroid Disorders."""
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
OUT_NAME = "w15-10_Hyperthyroid_Disorders.json"


def build() -> dict:
    p = "w15-10"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Clinical manifestations",
                "Why symptom chronology distinguishes thyroiditis from Graves",
                "Graves hyperthyroidism evolves over months with gradual hormone rises, whereas thyroiditis releases 30–60 days of stored hormone over days to weeks—patients often date thyroiditis onset precisely.",
                ref(
                    "Clinical Manifestations of Thyrotoxicosis",
                    "On the other hand, patients with thyrotoxicosis resulting from thyroiditis can often date the onset of their symptoms precisely, usually to within a month or so of their seeking medical attention, as might be expected from the effects of the release of the equivalent of 30 to 60 days' supply of thyroid hormone into the circulation over a few days to weeks.",
                ),
            ),
            note(
                f"{p}-n2",
                "Clinical manifestations",
                "Why masked thyrotoxicosis is easily missed",
                "Older patients may lack classic hypermetabolic signs and present with heart failure, arrhythmia, or unexplained weight loss without increased appetite—the syndrome termed masked or apathetic thyrotoxicosis.",
                ref(
                    "Clinical Manifestations of Thyrotoxicosis",
                    "The term masked or apathetic thyrotoxicosis is used to describe the syndrome sometimes seen in the elderly, which may present as congestive heart failure with arrhythmia or as unexplained weight loss without the increased appetite and other typical symptoms and signs of the younger patient.",
                ),
            ),
            note(
                f"{p}-n3",
                "Cardiovascular",
                "Cardiovascular manifestations of thyrotoxicosis",
                "Thyrotoxicosis lowers peripheral resistance, raises cardiac output via tachycardia and later stroke volume, widens pulse pressure, and causes supraventricular arrhythmias—atrial fibrillation occurs in 2–20% and explains ~15% of unexplained AF.",
                ref(
                    "Cardiovascular System",
                    "Between 2% and 20% of patients with thyrotoxicosis have atrial fibrillation, and about 15% of patients with otherwise unexplained atrial fibrillation are thyrotoxic, which may be caused directly by the thyroid hormone excess or by activating autoantibodies to the  $ \\beta_{1} $-adrenergic receptors.",
                ),
            ),
            note(
                f"{p}-n4",
                "Cardiovascular",
                "Why cardioversion is deferred during active thyrotoxicosis",
                "Attempts to convert atrial fibrillation while thyrotoxicosis persists are not indicated; ~60% revert spontaneously to sinus rhythm after treatment, most within 4 months.",
                ref(
                    "Cardiovascular System",
                    "Attempts to convert or abate atrial fibrillation to sinus rhythm are not indicated while thyrotoxicosis is present, and about 60% of patients revert spontaneously to sinus rhythm after treatment, most within 4 months.",
                ),
            ),
            note(
                f"{p}-n5",
                "Nervous system",
                "Neuropsychiatric and hyperkinetic features",
                "Thyrotoxic patients show nervousness, emotional lability, insomnia, and characteristic hyperkinesia with frequent position shifts and quick jerky movements; children may mimic ADHD with school decline.",
                ref(
                    "Nervous System",
                    "During the interview the patient shifts positions frequently, and movements are quick, jerky, exaggerated, and often purposeless.",
                ),
            ),
            note(
                f"{p}-n6",
                "Muscle",
                "Thyrotoxic myopathy and periodic paralysis",
                "Proximal weakness without primary myopathy is typical; periodic hypokalemic paralysis is accentuated by thyrotoxicosis, especially in Asian and Latino males.",
                ref(
                    "Muscle",
                    "The coincidence of the two disorders is particularly common in Asian and Latino males.",
                ),
            ),
            note(
                f"{p}-n7",
                "Eyes",
                "How lid lag differs from Graves orbitopathy",
                "Lid retraction, lid lag, and globe lag from increased adrenergic tone occur in all thyrotoxicosis causes and must be distinguished from infiltrative autoimmune orbitopathy specific to Graves disease.",
                ref(
                    "Eyes",
                    "It is important to differentiate these signs, which may occur in all forms of thyrotoxicosis, from those of infiltrative autoimmune orbitopathy, which are associated with Graves disease and are described later.",
                ),
            ),
            note(
                f"{p}-n8",
                "Laboratory diagnosis",
                "How RAIU separates hyperthyroidism from thyroiditis",
                "With suppressed TSH, elevated or inappropriately normal RAIU indicates excess production (Graves, toxic nodules); very low uptake (<5%) favors thyroiditis, factitia, or recent iodine load.",
                ref(
                    "Laboratory Diagnosis",
                    "Laboratory tests, including an increased sedimentation rate and a high serum thyroglobulin (Tg), may favor thyroiditis, but the most critical differentiating test is the radioactive iodine uptake (RAIU), which is elevated or inappropriately high-normal given the suppressed serum TSH level with excess thyroid hormone production and very low (<5%) in patients with thyroiditis (Fig. 10.1).",
                ),
            ),
            note(
                f"{p}-n9",
                "Graves disease",
                "Graves disease immunopathogenesis and TRAb",
                "Graves is a multisystem autoimmune disorder from loss of tolerance to TSHR; stimulating TSHRAbs (LATS) drive hyperthyroidism and can cross the placenta causing fetal/neonatal thyrotoxicosis.",
                ref(
                    "GRAVES DISEASE",
                    "Graves disease is a multisystem autoimmune disorder due to the loss of tolerance to the TSHR and in which hyperthyroidism is ultimately caused by TSHRAbs.",
                ),
            ),
            note(
                f"{p}-n10",
                "Graves disease",
                "Why TSHRAbs guide diagnosis and remission prediction",
                "TBII/TSI/TBAb assays support Graves diagnosis, orbitopathy, fetal risk, and remission likelihood; disappearance of TSHRAbs before stopping antithyroid drugs predicts high remission chance.",
                ref(
                    "Natural History and Prognosis",
                    "If TSHRAbs have disappeared, chances of remission are high.",
                ),
            ),
            note(
                f"{p}-n11",
                "Treatment",
                "How methimazole is first-line antithyroid therapy",
                "Methimazole (or carbimazole) is preferred for virtually all nonpregnant patients choosing antithyroid drugs; PTU is reserved for first-trimester pregnancy, thyroid storm, and methimazole intolerance.",
                ref(
                    "Practical Use",
                    "Guidelines agree that MMI (CBZ) should be used in virtually every nonpregnant patient who chooses ATD therapy.",
                ),
            ),
            note(
                f"{p}-n12",
                "Treatment",
                "Why PTU is not first-line outside special settings",
                "PTU can cause fulminant hepatic necrosis and accounts for 10% of drug-related liver transplants; the FDA advised in 2009 that PTU should not be first-line for hyperthyroidism.",
                ref(
                    "Adverse Effects (Table 10.3)",
                    "Because of this well-known rare but serious PTU side effect of hepatic failure, sometimes requiring liver transplantation, in June 2009 the U.S. Food and Drug Administration (FDA) issued an advisory that PTU should not be used as a first-line agent in hyperthyroidism.",
                ),
            ),
            note(
                f"{p}-n13",
                "Treatment",
                "How RAI therapy goals differ from euthyroid restoration",
                "ATA recommends sufficient single-dose RAI (typically 10–15 mCi) to render Graves patients hypothyroid—cure of hyperthyroidism is exchanged for lifelong levothyroxine replacement.",
                ref(
                    "Radioactive lodine",
                    "Sufficient activity of RAI should be administered in a single application, typically a mean dose of 10–15 mCi (370–555 MBq), to render the patient with Graves' disease hypothyroid.",
                ),
            ),
            note(
                f"{p}-n14",
                "Graves orbitopathy",
                "Graves orbitopathy clinical spectrum",
                "GO presents with eyelid swelling, retraction, proptosis in ~60%, diplopia in ~50%, and dysthyroid optic neuropathy in <5%; it may precede, accompany, or follow hyperthyroidism resolution.",
                ref(
                    "KEY POINTS",
                    "Graves orbitopathy (GO) remains one of the most difficult endocrine-related diseases to treat and requires a multidisciplinary approach. It may occur before, during, or even long after resolution of the hyperthyroidism.",
                ),
            ),
            note(
                f"{p}-n15",
                "Graves orbitopathy",
                "Why RAI can worsen orbitopathy without prophylaxis",
                "RAI worsens or induces GO in ~15% versus antithyroid drugs or surgery, likely from post-RAI TSHRAb rise; low-dose oral prednisone prophylaxis usually prevents this.",
                ref(
                    "Complications of RAI Therapy",
                    "RAI therapy is associated with development or worsening of GO in about 15% of cases compared to ATDs or thyroidectomy, as evident from three randomized clinical trials.",
                ),
            ),
            note(
                f"{p}-n16",
                "Graves dermopathy",
                "Graves dermopathy (pretibial myxedema)",
                "Rare pretibial peau d'orange plaques/nodules almost always occur with GO and high TSHRAbs; topical triamcinolone under occlusion and treating GO may improve lesions.",
                ref(
                    "Graves Dermopathy",
                    "Graves dermopathy is also known as pretibial myxedema or local myxedema. It is a rather rare phenotype of Graves disease that almost always occurs in the presence of GO and is associated with very high levels of TSHRAbs.",
                ),
            ),
            note(
                f"{p}-n17",
                "Pregnancy",
                "Gestational thyrotoxicosis from hCG",
                "Late first-trimester physiologic hCG can mildly stimulate TSHR causing transient low TSH; severe cases with very high hCG (twins, hyperemesis) must be distinguished from Graves by TRAb.",
                ref(
                    "Transient Gestational Thyrotoxicosis",
                    "In the late first trimester of normal pregnancy in humans, there is often a physiologic mild transient gestational thyrotoxicosis or hyperthyroidism.",
                ),
            ),
            note(
                f"{p}-n18",
                "Pregnancy",
                "Why PTU is used in the first trimester",
                "Methimazole embryopathy risk peaks weeks 6–10; PTU is reserved for first-trimester organogenesis though both drugs carry small teratogenic risk—lowest effective dose is mandatory.",
                ref(
                    "KEY POINTS",
                    "Methimazole embryopathy is rare. It may be avoided by the use of PTU in the first trimester as well as for women planning a pregnancy while under treatment for hyperthyroidism.",
                ),
            ),
            note(
                f"{p}-n19",
                "Pregnancy",
                "How to titrate antithyroid drugs in pregnancy",
                "Overtreatment causes fetal goiter and hypothyroidism; aim for maternal free T4 at or just above the nonpregnant upper limit with suppressed TSH—block-and-replace is inappropriate because only antithyroid drugs cross the placenta freely.",
                ref(
                    "Caring for the Pregnant Patient",
                    "However, the drugs may overtreat the fetus compared with the mother, and accordingly, the aim of therapy is to keep the mother in a state of subclinical hyperthyroidism analogous to the normal gestational physiology of the first trimester.",
                ),
            ),
            note(
                f"{p}-n20",
                "Toxic multinodular goiter",
                "Toxic multinodular goiter pathogenesis and presentation",
                "Toxic MNG evolves from long-standing nodular goiter via somatic TSHR mutations in autonomous nodules; presentation is milder than Graves, often after age 50, and iodine loads can precipitate thyrotoxicosis.",
                ref(
                    "Clinical Presentation",
                    "Sometimes hyperthyroidism develops abruptly, often after exposure to increased quantities of iodine, such as the contrast media for CT scanning, treatment with amiodarone, or excessive intake of kelp or similar products, which permits autonomous foci to increase hormone secretion to excessive levels and may simply exacerbate already established mild hyperthyroidism (see \"Iodide-Induced Hyperthyroidism\").",
                ),
            ),
            note(
                f"{p}-n21",
                "Toxic adenoma",
                "Toxic adenoma genetics and treatment",
                "Solitary toxic adenomas harbor constitutive activating TSHR or Gα mutations; treatment is radioiodine, hemithyroidectomy (preferred <18 years), or thermal ablation for suitable nodules.",
                ref(
                    "KEY POINTS",
                    "Toxic thyroid nodules are caused by a constitutive activating mutation in the TSHR.",
                ),
            ),
            note(
                f"{p}-n22",
                "Subclinical hyperthyroidism",
                "Why subclinical hyperthyroidism matters in older adults",
                "Suppressed TSH with normal free hormones increases atrial fibrillation risk—28% over 10 years when TSH ≤0.1 mU/L in Framingham patients >60—and may worsen bone density in postmenopausal women.",
                ref(
                    "Definition",
                    "On the other hand, in the classic studies in the Framingham population over 60 years of age, the cumulative incidence of atrial fibrillation over 10 years was 28% in patients with a serum TSH concentration of 0.1 mU/L or less, whereas it was only 11% in those with serum TSH concentrations falling between 0.1 and 0.4 mU/L.",
                ),
            ),
            note(
                f"{p}-n23",
                "Iodide-induced hyperthyroidism",
                "Jod-Basedow and iodinated contrast risk",
                "Iodide-induced thyrotoxicosis (Jod-Basedow) affects elderly patients with nodular disease or latent Graves; contrast-associated overt hyperthyroidism is rare (~0.1%) but high-risk patients may need prophylactic methimazole/perchlorate.",
                ref(
                    "Iodide-Induced Hyperthyroidism",
                    "The prevalence of iodine-induced overt hyperthyroidism after administration of iodinated contrast agents for radiographic procedures was found to be extremely low (around 0.1%) in a systematic review and meta-analysis of the literature.",
                ),
            ),
            note(
                f"{p}-n24",
                "Amiodarone",
                "How amiodarone causes types 1 and 2 thyrotoxicosis",
                "Amiodarone releases 6 mg iodide daily from a 200-mg tablet; AIT type 1 reflects iodine excess on autonomous thyroid tissue, whereas type 2 is destructive thyroiditis—mixed forms are common and color-flow Doppler helps distinguish them.",
                ref(
                    "Amiodarone-Induced Thyrotoxicosis",
                    "AIT type 1 is caused by iodine excess superimposed on preexistent thyroid autonomy, such as latent Graves disease or nodular goiter. AIT type 2 is due to the cytotoxic effect of amiodarone on thyrocytes resulting in transient destructive thyroiditis.",
                ),
            ),
            note(
                f"{p}-n25",
                "TSHoma",
                "TSH-secreting pituitary adenoma (TSHoma)",
                "Inappropriately normal or elevated TSH with high free T4/T3 suggests TSHoma or RTHβ; only ~1% of pituitary adenomas secrete TSH and 25% may co-secrete GH or prolactin.",
                ref(
                    "Pituitary Tumor",
                    "Only 1% of pituitary adenomas are TSH producing, and 25% may co-secrete growth hormone or prolactin.",
                ),
            ),
            note(
                f"{p}-n26",
                "Thyroid storm",
                "Why thyroid storm is a clinical diagnosis",
                "Thyroid storm is a clinical emergency—serum hormone levels do not correlate with severity or predict storm; mortality remains 10–25% despite ICU care.",
                ref(
                    "KEY POINTS",
                    "Thyroid storm is a rare endocrine emergency with a high mortality rate (10%–25%) even with immediate supportive treatment in intensive care facilities. The diagnosis is primarily based on clinical presentation and overall organ manifestations because thyroid hormone concentrations in serum are not correlated with the severity of hyperthyroidism, and they cannot predict development of thyroid storm.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Clinical manifestations",
                "A 72-year-old man has new atrial fibrillation and 8-kg weight loss without increased appetite. TSH is 0.02 mU/L. Which presentation pattern is most likely?",
                [
                    "Masked thyrotoxicosis without classic hypermetabolic signs",
                    "Subacute thyroiditis with painful goiter",
                    "Factitious thyrotoxicosis from levothyroxine",
                    "Primary hypothyroidism with assay interference",
                ],
                0,
                "Elderly patients may present with AF or heart failure without typical thyrotoxic symptoms—apathetic thyrotoxicosis.",
                ref(
                    "Clinical Manifestations of Thyrotoxicosis",
                    "The term masked or apathetic thyrotoxicosis is used to describe the syndrome sometimes seen in the elderly, which may present as congestive heart failure with arrhythmia or as unexplained weight loss without the increased appetite and other typical symptoms and signs of the younger patient.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Clinical manifestations",
                "A thyrotoxic patient asks why cardioversion for new atrial fibrillation was deferred. What is the best explanation?",
                [
                    "Rhythm control should wait until euthyroidism is restored; most revert spontaneously",
                    "Atrial fibrillation in thyrotoxicosis always requires lifelong anticoagulation first",
                    "Thyrotoxic AF is always ventricular and cannot be cardioverted",
                    "Amiodarone must be started before any rhythm strategy",
                ],
                0,
                "Cardioversion is not indicated during active thyrotoxicosis; ~60% revert after treating hyperthyroidism.",
                ref(
                    "Cardiovascular System",
                    "Attempts to convert or abate atrial fibrillation to sinus rhythm are not indicated while thyrotoxicosis is present, and about 60% of patients revert spontaneously to sinus rhythm after treatment, most within 4 months.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Laboratory diagnosis",
                "A woman has TSH 0.03 mU/L and elevated free T4. She recalls exact symptom onset 3 weeks ago after a viral illness. RAIU is 2%. What is the leading diagnosis?",
                [
                    "Destructive thyroiditis with hormone leak",
                    "Graves disease with diffuse uptake",
                    "Toxic multinodular goiter",
                    "TSH-secreting pituitary adenoma",
                ],
                0,
                "Abrupt onset and very low RAIU point to thyroiditis; Graves and toxic nodular disease show elevated uptake.",
                ref(
                    "Laboratory Diagnosis",
                    "the most critical differentiating test is the radioactive iodine uptake (RAIU), which is elevated or inappropriately high-normal given the suppressed serum TSH level with excess thyroid hormone production and very low (<5%) in patients with thyroiditis (Fig. 10.1).",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Laboratory diagnosis",
                "A thyrotoxic patient had CT with iodinated contrast 10 days ago. RAIU is low despite hyperthyroid biochemistry. What additional test helps confirm recent iodine load?",
                [
                    "24-hour urine iodine measurement",
                    "Serum calcitonin",
                    "TRH stimulation test",
                    "Serum reverse T3 only",
                ],
                0,
                "Recent iodine (e.g., contrast) suppresses RAIU and can be confirmed with urine iodine.",
                ref(
                    "Laboratory Diagnosis",
                    "However, the RAIU may also be low in a hyperthyroid patient who has recently received an iodine load, usually iodinated contrast for a computed tomography (CT) scan or for angiography. A 24-hour urine iodine measurement can confirm this.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Graves disease",
                "A diffuse goiter patient has suppressed TSH, elevated free T4, and positive TSHRAb. Which mechanism drives the hyperthyroidism?",
                [
                    "Stimulating autoantibodies acting as TSHR agonists",
                    "Blocking TSHR antibodies causing pituitary TSH excess",
                    "Exogenous levothyroxine ingestion",
                    "Ectopic hCG from ovarian teratoma only",
                ],
                0,
                "Graves hyperthyroidism is caused by stimulating TSHRAbs that activate the TSH receptor.",
                ref(
                    "KEY POINTS",
                    "Graves disease is caused by the development of unique human autoantibodies to the thyroid-stimulating hormone (thyrotropin; TSH) receptor (TSHR); these autoantibodies act as TSHR agonists.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Treatment",
                "A newly diagnosed Graves patient without pregnancy plans asks about first-line medical therapy. What does current guidance recommend?",
                [
                    "Methimazole as the default antithyroid drug",
                    "Propylthiouracil as first-line for all adults",
                    "Potassium iodide monotherapy until euthyroid",
                    "Immediate radioiodine without discussion of alternatives",
                ],
                0,
                "Methimazole is first-line for virtually all nonpregnant patients choosing antithyroid drugs.",
                ref(
                    "KEY POINTS",
                    "The treatment of hyperthyroidism is best initiated with the antithyroid drug methimazole; propylthiouracil (PTU) is no longer recommended as first-line therapy because of its rare, but occasionally severe, hepatic toxicity.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Treatment",
                "A patient with severe thyrotoxicosis needs rapid T3 reduction and cannot take methimazole. Which PTU property is clinically relevant?",
                [
                    "PTU inhibits D1-mediated peripheral T4-to-T3 conversion",
                    "PTU blocks TSH secretion from the pituitary directly",
                    "PTU stimulates thyroidal hormone release",
                    "PTU irreversibly ablates thyroid tissue",
                ],
                0,
                "Large-dose PTU blocks D1 conversion of T4 to T3 in liver, kidney, and Graves thyroid—useful in severe thyrotoxicosis.",
                ref(
                    "KEY POINTS",
                    "PTU may be useful in treating severe hyperthyroidism because of its capacity to block conversion of thyroxine ( $ T_{4} $) to triiodothyronine ( $ T_{3} $) by the type 1 deiodinase (D1) in liver, kidney, and Graves thyroid.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Treatment",
                "A Graves patient with mild inactive orbitopathy is scheduled for radioiodine. What prophylactic measure reduces orbitopathy risk?",
                [
                    "Low-dose oral prednisone tapered over weeks after RAI",
                    "High-dose methimazole continued through RAI day only",
                    "Potassium iodide alone before RAI",
                    "Immediate orbital decompression before RAI",
                ],
                0,
                "Steroid prophylaxis after RAI prevents GO worsening in at-risk patients.",
                ref(
                    "Complications of RAI Therapy",
                    "The untoward effect of RAI on GO can, however, almost always be prevented by the so-called steroid prophylaxis with low-dose oral prednisone given for few weeks after RAI treatment (0.3–0.5 mg/kg body weight gradually tapered and withdrawn after 3 months).",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Graves orbitopathy",
                "A thyrotoxic patient has lid retraction and stare but no proptosis or diplopia. What is the most accurate interpretation?",
                [
                    "Adrenergic thyrotoxic eye signs that can occur in any cause of thyrotoxicosis",
                    "Definite moderate Graves orbitopathy requiring IV steroids",
                    "Myasthenia gravis until proven otherwise",
                    "Isolated dysthyroid optic neuropathy",
                ],
                0,
                "Lid lag/retraction from adrenergic tone occurs in all thyrotoxicosis and differs from infiltrative GO.",
                ref(
                    "Eyes",
                    "Some retraction of the upper or lower eyelids, or both, evident as the presence of a rim of sclera between either lid and the limbus, may be seen in all forms of thyrotoxicosis regardless of the underlying cause and is responsible for the typical stare of the patient.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Pregnancy",
                "At 8 weeks gestation a woman has suppressed TSH and high-normal free T4 without goiter; TRAb is negative. What is the most likely diagnosis?",
                [
                    "Physiologic gestational thyrotoxicosis from hCG",
                    "Graves disease requiring high-dose methimazole",
                    "Toxic multinodular goiter",
                    "Amiodarone-induced thyrotoxicosis type 1",
                ],
                0,
                "First-trimester hCG can cause mild transient gestational thyrotoxicosis; TRAb helps distinguish Graves.",
                ref(
                    "Transient Gestational Thyrotoxicosis",
                    "It may be difficult to separate this syndrome from early Graves disease, and measurement of TSHRAbs may be helpful, whereas 99mTc thyroid scintigraphy is contraindicated in pregnancy.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Pregnancy",
                "A pregnant Graves patient on antithyroid drug has TSH 0.8 mU/L and free T4 mid-normal for pregnancy. What adjustment is indicated?",
                [
                    "Reduce antithyroid dose—normal TSH suggests overtreatment risk to the fetus",
                    "Increase dose to normalize TSH",
                    "Add levothyroxine in a block-and-replace regimen",
                    "Start therapeutic radioiodine immediately",
                ],
                0,
                "Therapeutic target is mild maternal undertreatment; normal or unsuppressed TSH on therapy warrants dose reduction.",
                ref(
                    "Caring for the Pregnant Patient",
                    "Indeed, a normal or even a suppressed TSH during drug therapy is an indication that the dose of the drug should be reduced.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Pregnancy",
                "A woman with Graves disease in remission on methimazole discovers pregnancy at 5 weeks. What antithyroid strategy aligns with guidance?",
                [
                    "Switch to PTU for first-trimester organogenesis, then consider methimazole",
                    "Continue high-dose methimazole throughout pregnancy",
                    "Stop all therapy and use iodide monotherapy",
                    "Proceed with radioiodine in the first trimester",
                ],
                0,
                "PTU is reserved for first trimester because of methimazole embryopathy risk during organogenesis.",
                ref(
                    "Antithyroid Drugs in Pregnancy",
                    "Previously, the antithyroid drug of choice throughout pregnancy in the United States was PTU, but because of the rare yet serious side effect of PTU-induced hepatic failure, in June 2009 the FDA issued an advisory that PTU should be reserved for the first trimester of pregnancy while organogenesis is occurring.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Toxic multinodular goiter",
                "A 68-year-old woman with long-standing nodular goiter develops thyrotoxicosis after IV contrast for angiography. What mechanism is most likely?",
                [
                    "Iodine-triggered hormone release from autonomous nodules (Jod-Basedow)",
                    "New-onset Graves disease with TRAb",
                    "Painless postpartum thyroiditis",
                    "TSHoma with diffuse uptake",
                ],
                0,
                "Toxic MNG can worsen abruptly after iodine exposure when autonomous foci secrete excess hormone.",
                ref(
                    "Clinical Presentation",
                    "Sometimes hyperthyroidism develops abruptly, often after exposure to increased quantities of iodine, such as the contrast media for CT scanning, treatment with amiodarone, or excessive intake of kelp or similar products, which permits autonomous foci to increase hormone secretion to excessive levels and may simply exacerbate already established mild hyperthyroidosis (see \"Iodide-Induced Hyperthyroidism\").",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Toxic adenoma",
                "A 35-year-old man has a single hot nodule on scan and suppressed TSH. He prefers definitive therapy and is 16 years old in a similar case—what would guidelines favor?",
                [
                    "Surgical excision over radioiodine in patients younger than 18",
                    "Observation only until age 65",
                    "High-dose potassium iodide monotherapy",
                    "Thyroid hormone suppression to shrink the nodule",
                ],
                0,
                "Surgery is preferred under 18 to avoid long-term irradiation effects on perinodular tissue.",
                ref(
                    "Surgery",
                    "Surgical excision is always preferable in patients younger than 18 years of age to avoid the long-term consequences of irradiation, including effects on perinodular tissue.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Subclinical hyperthyroidism",
                "A 70-year-old woman has persistent TSH 0.05 mU/L with normal free T4/T3 and osteoporosis. What does evidence support?",
                [
                    "Consider treatment because suppressed TSH increases AF risk and may worsen bone density",
                    "Ignore TSH because free hormones are normal in all tissues",
                    "Mandate immediate total thyroidectomy for all subclinical disease",
                    "Start levothyroxine to raise TSH",
                ],
                0,
                "Older patients with TSH ≤0.1 and cardiac disease or osteoporosis are treatment candidates.",
                ref(
                    "Treatment",
                    "However, treatment should be considered in those over age 65 with cardiac disease or osteoporosis. There is increasing support for treatment of individuals with persistently subnormal TSH concentrations less than 0.1 mU/L (with normal free thyroid hormones) who are over age 65 and for those younger than age 65 with cardiac disease or risk factors for cardiac disease or significant risk for osteoporosis.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Amiodarone",
                "A patient on amiodarone for 2 months develops thyrotoxicosis with a vascular goiter on color Doppler. What is the preferred initial treatment?",
                [
                    "High-dose methimazole (AIT type 1)",
                    "Oral prednisone alone (AIT type 2)",
                    "Immediate total thyroidectomy without antithyroid drugs",
                    "Therapeutic radioiodine while continuing amiodarone",
                ],
                0,
                "Type 1 AIT (early onset, underlying autonomy, high vascularity) is treated with antithyroid drugs.",
                ref(
                    "Management",
                    "Specific guidelines recommend treatment with antithyroid drugs in AIT type 1 (Fig. 10.22).",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Amiodarone",
                "After 30 months on amiodarone a patient develops thyrotoxicosis without goiter; Doppler shows absent thyroid vascularity. Best initial therapy?",
                [
                    "Oral prednisone with possible continuation of amiodarone if cardiology agrees",
                    "Methimazole 60 mg daily without steroids",
                    "Potassium iodide three times daily",
                    "Levothyroxine suppression of TSH",
                ],
                0,
                "Type 2 AIT is destructive thyroiditis treated with glucocorticoids; amiodarone may be continued in selected patients.",
                ref(
                    "Management",
                    "Management is completely different in AIT type 2. Here the preferred drug is oral prednisone, in a daily dose of 30 mg.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "TSHoma",
                "A patient has elevated free T4 and T3 with TSH 4.8 mU/L (inappropriately normal). Pituitary MRI shows a macroadenoma. What is the leading diagnosis?",
                [
                    "TSH-secreting pituitary adenoma",
                    "Primary Graves disease",
                    "Subclinical hypothyroidism",
                    "Gestational thyrotoxicosis",
                ],
                0,
                "Detectable/elevated TSH with high thyroid hormones suggests TSHoma or RTH; adenoma confirms TSHoma.",
                ref(
                    "Pituitary Tumor",
                    "Laboratory studies demonstrating an inappropriately detectable or somewhat elevated TSH in the presence of elevated thyroid hormone levels must first be confirmed by eliminating assay artifacts.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Gestational hCG",
                "A young woman has hyperthyroidism, amenorrhea, and very high hCG. Ultrasound shows no intrauterine pregnancy. Next step?",
                [
                    "Evaluate for hydatidiform mole and evacuate if confirmed",
                    "Start methimazole and observe for 12 months",
                    "Schedule elective radioiodine ablation",
                    "Treat as painless postpartum thyroiditis",
                ],
                0,
                "Trophoblastic disease secretes hCG that cross-stimulates TSHR; evacuation is definitive for molar pregnancy.",
                ref(
                    "Tumor Chorionic Gonadotropin-Induced Hyperthyroidism",
                    "The possibility of a molar pregnancy should be considered in a young woman with hyperthyroidism and amenorrhea because the appropriate therapy is evacuation of the uterus.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Transient thyroiditis",
                "Four months postpartum a woman has mild thyrotoxicosis, elevated TPOAb, and RAIU 1%. TRAb is negative. Most likely diagnosis?",
                [
                    "Postpartum thyroiditis (destructive)",
                    "Graves disease requiring methimazole for 18 months",
                    "Toxic adenoma",
                    "TSHoma",
                ],
                0,
                "Postpartum thyroiditis causes transient thyrotoxicosis with low RAIU; TRAb distinguishes Graves relapse.",
                ref(
                    "Transient Postpartum Thyroiditis",
                    "Transient postpartum thyroiditis remains the most common form of hyperthyroidism in the postpartum period and usually precedes a period of hypothyroidism.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Subacute thyroiditis",
                "A patient has painful thyroid, ESR 110 mm/h, suppressed TSH, and RAIU 2%. What treatment is appropriate for thyrotoxic symptoms?",
                [
                    "Beta-blockers; antithyroid drugs are not indicated",
                    "High-dose methimazole for 18 months",
                    "Therapeutic radioiodine immediately",
                    "Levothyroxine to suppress TSH",
                ],
                0,
                "Destructive thyroiditis releases stored hormone—beta-blockers treat symptoms; thionamides do not reduce release.",
                ref(
                    "Treatment",
                    "The thyrotoxic phase may require alleviation of the peripheral manifestations through the use of  $ \\beta $-blockers.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Thyroid storm",
                "A febrile, agitated thyrotoxic patient is started on iodide before antithyroid drug. What complication is being avoided?",
                [
                    "Flare of thyrotoxicosis from increased hormone synthesis before blockade",
                    "Permanent hypothyroidism from iodide alone",
                    "Methimazole-induced agranulocytosis",
                    "Wolff-Chaikoff hypothyroidism in the pituitary",
                ],
                0,
                "Give antithyroid drug first, then iodide 1 hour later to avoid transient worsening from iodine-organified hormone production.",
                ref(
                    "First-Line Specific Antithyroid Therapy",
                    "One hour after the first antithyroid drug dose, potassium iodide should be given as 250 mg orally every 6 hours. The sequence is important to avoid a flare-up of thyrotoxicosis resulting from increased thyroid hormone production.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Thyroid storm",
                "In thyroid storm, which agent is preferred as the antithyroid drug and why?",
                [
                    "Propylthiouracil for higher doses and D1 inhibition",
                    "Methimazole only because PTU is contraindicated in storm",
                    "Carbimazole topical cream",
                    "Potassium perchlorate as monotherapy",
                ],
                0,
                "Storm protocols use PTU loading (500–1000 mg) then 250 mg q4h for rapid effect and T3 reduction.",
                ref(
                    "First-Line Specific Antithyroid Therapy",
                    "Antithyroid drugs should be given, and propylthiouracil is the first choice (500- to 1000-mg load, if possible, intravenously, followed by 250 mg every 4 hours).",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Graves dermopathy",
                "A patient has pretibial peau d'orange plaques and severe proptosis. What laboratory finding is expected?",
                [
                    "Very high TSH receptor antibody levels",
                    "Undetectable TSHRAbs",
                    "Isolated low TPOAb with negative TRAb",
                    "Elevated serum TSH with low free T4",
                ],
                0,
                "Graves dermopathy almost always accompanies GO and very high TSHRAbs.",
                ref(
                    "Graves Dermopathy",
                    "It is a rather rare phenotype of Graves disease that almost always occurs in the presence of GO and is associated with very high levels of TSHRAbs.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Treatment",
                "Before stopping 18 months of methimazole in Graves disease, which test best predicts remission?",
                [
                    "TSHRAb assay—undetectable antibodies favor remission",
                    "Routine WBC count weekly",
                    "Serum reverse T3 alone",
                    "TRH stimulation test mandatory in all patients",
                ],
                0,
                "TSHRAb disappearance before stopping ATD indicates high remission probability.",
                ref(
                    "Natural History and Prognosis",
                    "It has been recommended to measure TSHRAbs just before stopping ATD. If TSHRAbs have disappeared, chances of remission are high.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Iodide-induced hyperthyroidism",
                "An elderly man with nodular goiter receives iodinated contrast and develops thyrotoxicosis. RAIU may be normal or high. Expected course?",
                [
                    "Often spontaneous resolution within about 6 months",
                    "Permanent Graves disease requiring lifelong methimazole",
                    "Immediate progression to thyroid storm in all cases",
                    "Irreversible hypothyroidism within 48 hours",
                ],
                0,
                "Iodide-induced thyrotoxicosis in patients with underlying autonomy often resolves spontaneously.",
                ref(
                    "Iodide-Induced Hyperthyroidism",
                    "IIT usually resolves spontaneously in 6 months.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Epidemiology",
                "Hyperthyroidism prevalence is about 1% to 2% in women and 0.1% to 0.2% in men.",
                True,
                "Williams key points cite this sex-different prevalence.",
                ref(
                    "KEY POINTS",
                    "Hyperthyroidism has a prevalence of 1% to 2% in women and 0.1% to 0.2% in men.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Causes",
                "Graves disease and toxic multinodular goiter are the most common causes of overactive thyroid.",
                True,
                "These are the leading causes in iodine-sufficient regions.",
                ref(
                    "KEY POINTS",
                    "The most common causes of an overactive thyroid are Graves disease and toxic multinodular goiter.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Clinical manifestations",
                "Tachycardia is virtually always present in thyrotoxicosis.",
                True,
                "Tachycardia from increased sympathetic and decreased vagal tone is a hallmark.",
                ref(
                    "Cardiovascular System",
                    "Tachycardia is virtually always present and is due to a combination of increased sympathetic and decreased vagal tone.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Muscle",
                "Thyrotoxic periodic paralysis is especially common in Asian and Latino males.",
                True,
                "Hypokalemic periodic paralysis coincides with thyrotoxicosis more in these groups.",
                ref(
                    "Muscle",
                    "The coincidence of the two disorders is particularly common in Asian and Latino males.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Laboratory diagnosis",
                "In thyrotoxicosis, free T3 is usually more elevated than free T4 except in thyroiditis or levothyroxine intake.",
                True,
                "Thyroiditis and exogenous T4 cause relatively higher free T4 than T3.",
                ref(
                    "Laboratory Diagnosis",
                    "In general, serum free  $ T_{3} $ is more elevated than is the free  $ T_{4} $, but free  $ T_{4} $ is relatively high if thyrotoxicosis is caused by thyroiditis or intake of levothyroxine.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Treatment",
                "Neither ATA nor ETA recommends routine WBC monitoring during antithyroid drug therapy.",
                True,
                "Patients are warned about fever/sore throat; routine CBC monitoring is not recommended.",
                ref(
                    "Adverse Effects (Table 10.3)",
                    "Neither the American Thyroid Association (ATA) nor the ETA recommends routine monitoring of white blood cells during ATD therapy.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Treatment",
                "After agranulocytosis on PTU, switching to methimazole is generally safe because cross-reactivity is low.",
                False,
                "Cross-reactivity is high—thionamides should not be given again after agranulocytosis.",
                ref(
                    "Adverse Effects (Table 10.3)",
                    "consequently, thionamides should not be given again.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Graves orbitopathy",
                "Graves orbitopathy occurs only while the patient is hyperthyroid.",
                False,
                "GO may occur before, during, or long after hyperthyroidism resolves.",
                ref(
                    "KEY POINTS",
                    "It may occur before, during, or even long after resolution of the hyperthyroidism.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Pregnancy",
                "Overtreatment of hyperthyroidism in pregnancy can impair fetal cognitive development.",
                True,
                "Both ATDs cross the placenta and can cause fetal hypothyroidism if overdosed.",
                ref(
                    "KEY POINTS",
                    "Overtreatment of the pregnant hyperthyroid patient must be avoided because of the transplacental passage of both PTU and methimazole. Fetal hypothyroidism can impair cognitive development.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Subclinical hyperthyroidism",
                "Most NHANES participants with subnormal TSH on levothyroxine were intentionally treated for thyroid cancer rather than inadvertent overtreatment.",
                False,
                "In a Colorado screening study, 58% of TSH-suppressed individuals were on thyroid hormone—often not intentional overtreatment for cancer.",
                ref(
                    "Diagnosis",
                    "In a study of over 25,000 individuals attending health fairs in Colorado, 58% of those with a TSH of less than 0.3 mU/L were receiving thyroid hormones.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Amiodarone",
                "Amiodarone-induced thyrotoxicosis type 2 typically has low or absent thyroid vascularity on color Doppler.",
                True,
                "Type 2 is destructive thyroiditis with low vascularity; type 1 shows high flow.",
                ref(
                    "Diagnosis",
                    "Most useful is color flow Doppler sonography, which provides a noninvasive, real-time assessment of thyroid vascularity.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Transient thyroiditis",
                "Subacute (de Quervain) thyroiditis is usually painful, unlike painless postpartum thyroiditis.",
                True,
                "Key points contrast painful subacute thyroiditis with painless postpartum autoimmune thyroiditis.",
                ref(
                    "KEY POINTS",
                    "Subacute thyroiditis secondary to infectious agents is usually painful, in marked contrast to the transient autoimmune thyroiditis seen in the postpartum period.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Thyroid storm",
                "Serum thyroid hormone concentrations reliably predict the severity of thyroid storm.",
                False,
                "Storm is a clinical diagnosis—hormone levels do not correlate with severity.",
                ref(
                    "Clinical Presentation",
                    "the concentrations of peripheral thyroid hormones in serum are not correlated with the severity of hyperthyroidism, and they cannot predict a development into thyroid storm.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Clinical manifestations",
                "Assertion: Patients with thyroiditis can often pinpoint symptom onset to within a month.",
                "Reason: Thyroiditis releases weeks of stored hormone into circulation over days to weeks.",
                0,
                "Both true—the abrupt hormone leak explains precise dating of onset.",
                ref(
                    "Clinical Manifestations of Thyrotoxicosis",
                    "patients with thyrotoxicosis resulting from thyroiditis can often date the onset of their symptoms precisely, usually to within a month or so of their seeking medical attention, as might be expected from the effects of the release of the equivalent of 30 to 60 days' supply of thyroid hormone into the circulation over a few days to weeks.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Cardiovascular",
                "Assertion: Thyrotoxic atrial fibrillation should not be cardioverted while thyrotoxicosis persists.",
                "Reason: Atrial fibrillation in thyrotoxicosis never reverts after treating hyperthyroidism.",
                2,
                "Assertion is true; reason is false—about 60% revert spontaneously after treatment.",
                ref(
                    "Cardiovascular System",
                    "about 60% of patients revert spontaneously to sinus rhythm after treatment, most within 4 months.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Laboratory diagnosis",
                "Assertion: Elevated RAIU with suppressed TSH suggests endogenous hyperthyroidism.",
                "Reason: Low RAIU always indicates Graves disease.",
                2,
                "Assertion is true; reason is false—low RAIU indicates thyroiditis, iodine load, or factitia, not Graves.",
                ref(
                    "Laboratory Diagnosis",
                    "the radioactive iodine uptake (RAIU), which is elevated or inappropriately high-normal given the suppressed serum TSH level with excess thyroid hormone production and very low (<5%) in patients with thyroiditis (Fig. 10.1).",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Graves disease",
                "Assertion: Stimulating TSHRAbs can cause fetal thyrotoxicosis.",
                "Reason: Maternal TSHRAbs do not cross the placenta.",
                2,
                "Assertion is true; reason is false—transplacental TRAb stimulation causes fetal/neonatal thyrotoxicosis.",
                ref(
                    "GRAVES DISEASE",
                    "Another example of the in vivo effects of TSHRAbs is the transplacental passage of maternal TSHRAbs, which may stimulate the fetal thyroid gland and cause fetal/neonatal thyrotoxicosis.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Treatment",
                "Assertion: Methimazole is preferred first-line antithyroid therapy in nonpregnant adults.",
                "Reason: PTU is preferred because it never causes hepatotoxicity.",
                2,
                "Assertion is true; reason is false—PTU carries rare but severe hepatic failure risk.",
                ref(
                    "KEY POINTS",
                    "propylthiouracil (PTU) is no longer recommended as first-line therapy because of its rare, but occasionally severe, hepatic toxicity.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Treatment",
                "Assertion: Radioiodine therapy for Graves often aims to induce lifelong hypothyroidism.",
                "Reason: Meticulous dosimetry reliably maintains long-term euthyroidism after RAI.",
                2,
                "Assertion reflects ATA practice; reason is false—fixed ablative doses accept hypothyroidism.",
                ref(
                    "Radioactive lodine",
                    "no dose calculation can secure long-term euthyroidism and it is fully acceptable to offer a fixed dose of RAI.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Graves orbitopathy",
                "Assertion: Radioiodine can worsen Graves orbitopathy in some patients.",
                "Reason: TSHRAbs decrease after radioiodine compared with antithyroid drugs.",
                2,
                "Assertion is true (~15%); reason is false—TSHRAbs rise after RAI versus fall with ATD/surgery.",
                ref(
                    "Complications of RAI Therapy",
                    "whereas in contrast, TSHRAbs decrease after thyroidectomy or upon treatment with ATD.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Pregnancy",
                "Assertion: Pregnant Graves patients should avoid antithyroid drug overtreatment.",
                "Reason: Fetal hypothyroidism from excess transplacental ATD can harm neurodevelopment.",
                0,
                "Both true—target mild maternal undertreatment with free T4 at upper normal and suppressed TSH acceptable.",
                ref(
                    "KEY POINTS",
                    "Fetal hypothyroidism can impair cognitive development.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Amiodarone",
                "Assertion: AIT type 2 is treated with glucocorticoids rather than antithyroid drugs alone.",
                "Reason: Type 2 AIT results from destructive thyroiditis without underlying autonomy.",
                0,
                "Both true—type 2 is cytotoxic thyroiditis; prednisone is preferred.",
                ref(
                    "Amiodarone-Induced Thyrotoxicosis",
                    "AIT type 2 is due to the cytotoxic effect of amiodarone on thyrocytes resulting in transient destructive thyroiditis.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Subclinical hyperthyroidism",
                "Assertion: TSH ≤0.1 mU/L in older adults increases atrial fibrillation risk.",
                "Reason: Subclinical hyperthyroidism never affects cardiovascular outcomes.",
                2,
                "Assertion is supported by Framingham data; reason is false—cardiac and bone endpoints are affected.",
                ref(
                    "Definition",
                    "Furthermore, heart failure is the leading cause of increased cardiovascular mortality rate in both overt and mild hyperthyroidism.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Thyroid storm",
                "Assertion: Thyroid storm requires PTU as the preferred antithyroid drug.",
                "Reason: PTU is first-line for all outpatient Graves patients including mild disease.",
                1,
                "Assertion is true in storm; reason is false—outpatient first-line is methimazole, not PTU.",
                ref(
                    "First-Line Specific Antithyroid Therapy",
                    "propylthiouracil is the first choice (500- to 1000-mg load, if possible, intravenously, followed by 250 mg every 4 hours).",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Transient thyroiditis",
                "Assertion: Beta-blockers are the main treatment for thyrotoxic symptoms in painless autoimmune thyroiditis.",
                "Reason: Antithyroid drugs accelerate hormone release from inflamed follicles.",
                2,
                "Assertion is true; reason is false—destructive thyroiditis releases stored hormone; thionamides do not treat release.",
                ref(
                    "Treatment",
                    "The thyrotoxic phase may require alleviation of the peripheral manifestations through the use of  $ \\beta $-blockers.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "10",
        "title": "Hyperthyroid Disorders",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Anthony Hollenberg, Wilmar Wiersinga, Luigi Bartalena, Ulla Feldt-Rasmussen",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_10_Hyperthyroid_Disorders.md",
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
