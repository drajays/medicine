#!/usr/bin/env python3
"""Generate Williams 15e module w15-46 — Endocrinology of HIV/AIDS."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-46"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-46_Endocrinology_of_HIVAIDS.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why adrenal dysfunction risk differs by HIV control status",
                "Adrenal dysfunction is relatively common with untreated or advanced HIV but appears less common when virologic control is achieved on ART.",
                ref(
                    "KEY POINTS",
                    "Adrenal dysfunction is relatively common in those with untreated or advanced human immunodeficiency virus (HIV) but appears less common in those with virologic control.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How boosted ART precipitates iatrogenic adrenal insufficiency",
                "Ritonavir and cobicistat inhibit CYP3A4 metabolism of inhaled or injected corticosteroids, causing glucocorticoid excess, adrenal suppression, and severe adrenal insufficiency when steroids are stopped.",
                ref(
                    "KEY POINTS",
                    "Specific antiretrovirals, including ritonavir and cobicistat, may reduce metabolism of inhaled and injected steroids and increase systemic glucocorticoid exposure, causing iatrogenic adrenal insufficiency with steroid discontinuation.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why free testosterone is required to diagnose hypogonadism in HIV",
                "SHBG is increased in 30% to 55% of patients with HIV; total testosterone assays may underestimate true hypogonadism.",
                ref(
                    "KEY POINTS",
                    "Hypogonadism is often seen among individuals with HIV, is frequently associated with low or normal gonadotropins, and should be assessed using a specific free testosterone assay, given increases in sex hormone-binding globulin in this population.",
                ),
            ),
            note(
                f"{p}-n4",
                "KEY POINTS",
                "How AIDS wasting differs from HIV lipodystrophy",
                "AIDS wasting is sarcopenia with lean mass loss, whereas lipodystrophy features subcutaneous fat loss and visceral fat redistribution.",
                ref(
                    "KEY POINTS",
                    "Acquired immunodeficiency syndrome (AIDS) wasting, characterized by sarcopenia, should be distinguished from HIV lipodystrophy, which is characterized by subcutaneous fat loss.",
                ),
            ),
            note(
                f"{p}-n5",
                "Adrenal Insufficiency",
                "Why CMV adrenalitis dominates advanced HIV adrenal failure",
                "CMV adrenalitis is the most common opportunistic cause of adrenal destruction at autopsy, though destruction is usually insufficient alone to cause insufficiency.",
                ref(
                    "Adrenal Insufficiency",
                    "CMV adrenalitis is the most common cause, seen in approximately 40% to 90% of patients with CMV infection at autopsy.",
                ),
            ),
            note(
                f"{p}-n6",
                "Medication Effects",
                "How ritonavir-boosted ART interacts with inhaled corticosteroids",
                "CYP3A4 inhibition by ritonavir or cobicistat reduces inhaled corticosteroid metabolism, producing Cushing features, suppressed ACTH/cortisol, and withdrawal adrenal crisis.",
                ref(
                    "Medication Effects",
                    "The resulting reduction in metabolism of the inhaled corticosteroid, via inhibition of CYP3A4 by ritonavir or cobicistat, can result in glucocorticoid excess, adrenal suppression, symptoms of Cushing syndrome, and potentially severe adrenal insufficiency with discontinuation of the inhaled corticosteroid.",
                ),
            ),
            note(
                f"{p}-n7",
                "Clinical Assessment",
                "How to evaluate suspected adrenal insufficiency in HIV",
                "Cosyntropin testing is usually adequate first-line; morning cortisol, metyrapone, or insulin tolerance testing may be needed when recent hypothalamic-pituitary disease is suspected.",
                ref(
                    "Clinical Assessment",
                    "Cosyntropin testing is usually an adequate first step, except in those patients in whom hypothalamic or pituitary insufficiency of recent onset is suspected.",
                ),
            ),
            note(
                f"{p}-n8",
                "Male Gonadal Dysfunction",
                "Why hypogonadism in HIV is usually secondary",
                "Most men with reduced free testosterone have low or inappropriately normal gonadotropins, especially during ART initiation.",
                ref(
                    "Male Gonadal Dysfunction",
                    "Most often, hypogonadism is secondary in nature, with low or inappropriately normal gonadotropin levels, as seen in 91% of patients with reduced free testosterone levels during initiation of ART in the Swiss HIV cohort.",
                ),
            ),
            note(
                f"{p}-n9",
                "Male Gonadal Dysfunction",
                "How to measure testosterone accurately in men with HIV",
                "Free testosterone by equilibrium dialysis or accepted calculation is preferred; analogue free-testosterone assays are not independent of SHBG.",
                ref(
                    "Male Gonadal Dysfunction",
                    "In contrast, determination of free testosterone by equilibrium dialysis or calculation by an accepted equation are more useful strategies to detect hypogonadism among those with HIV.",
                ),
            ),
            note(
                f"{p}-n10",
                "Female Gonadal Dysfunction",
                "Why amenorrhea risk is higher in women with HIV",
                "Meta-analysis shows 2% to 7% amenorrhea prevalence and 62% higher odds versus HIV-uninfected women.",
                ref(
                    "Female Gonadal Dysfunction",
                    "In a more recent meta-analysis, amenorrhea was seen in 2% to 7% of premenopausal women with HIV, and the odds of amenorrhea were 62% higher in women with HIV compared to those without.",
                ),
            ),
            note(
                f"{p}-n11",
                "Thyroid Function",
                "How immune reconstitution causes Graves disease after ART",
                "Graves disease develops in about 3% of women and 0.2% of men after ART, often years after initiation.",
                ref(
                    "Thyroid Function",
                    "This most commonly manifests as Graves disease, estimated to occur in 3% of women and 0.2% of men following treatment with ART, or less commonly results in autoimmune hypothyroidism.",
                ),
            ),
            note(
                f"{p}-n12",
                "Thyroid Function",
                "Why routine thyroid screening is not recommended on ART",
                "In virologically controlled adults, overt thyroid disease prevalence is not increased versus the general population.",
                ref(
                    "Thyroid Function",
                    "In ART-treated individuals with virologic control, studies do not support an increased prevalence of overt thyroid disease compared with the general population.",
                ),
            ),
            note(
                f"{p}-n13",
                "Sodium",
                "How SIADH contributes to hyponatremia in AIDS",
                "SIADH accounts for 23% to 47% of hyponatremia in hospitalized patients with AIDS.",
                ref(
                    "Sodium",
                    "SIADH (volume-replete patients with low levels of serum sodium, and inappropriately elevated levels of urine osmolarity) is seen in 23% to 47% of hyponatremic patients.",
                ),
            ),
            note(
                f"{p}-n14",
                "Potassium",
                "Why trimethoprim causes hyperkalemia in HIV",
                "Structural similarity to amiloride inhibits tubular potassium secretion in 20% to 53% of AIDS patients on trimethoprim.",
                ref(
                    "Potassium",
                    "Hyperkalemia occurs in 20% to 53% of AIDS patients on trimethoprim because of structural similarities to amiloride and inhibition of tubular potassium excretion.",
                ),
            ),
            note(
                f"{p}-n15",
                "Calcium Homeostasis",
                "How efavirenz lowers vitamin D in HIV",
                "Efavirenz increases catabolism of 25-hydroxyvitamin D through CYP24A induction.",
                ref(
                    "Calcium Homeostasis",
                    "Vitamin D deficiency may be caused by malabsorption from AIDS enteropathy or by specific effects of antiretroviral drugs (e.g., inhibition of 1α-hydroxylation of 25-hydroxyvitamin D by PIs or increased conversion of 25-hydroxyvitamin D to 24,25-dihydroxyvitamin D3 by efavirenz).",
                ),
            ),
            note(
                f"{p}-n16",
                "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                "Why TDF and PIs accelerate bone loss in HIV",
                "TDF causes phosphate wasting and tubulopathy; PIs may inhibit vitamin D activation—both are linked to osteopenia and osteoporosis progression.",
                ref(
                    "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                    "In this large cohort, factors associated with progression of bone loss were age, male sex, lower body mass index (BMI), PI use, and TDF use.",
                ),
            ),
            note(
                f"{p}-n17",
                "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                "How to mitigate ART-initiation bone loss",
                "High-dose vitamin D3 and calcium can attenuate loss by 50%; single-dose zoledronic acid before ART can prevent loss over 96 weeks.",
                ref(
                    "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                    "In a randomized controlled trial, high-dose vitamin D3 (4000 IU/d) and calcium (1000 mg/d) at the time of ART initiation with TDF/FTC/EFV was shown to attenuate ART-initiation associated bone loss by 50%.",
                ),
            ),
            note(
                f"{p}-n18",
                "The Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "Why GH patterns differ in wasting versus lipodystrophy",
                "AIDS wasting shows GH resistance (high GH, low IGF1), whereas central fat accumulation shows relative GH deficiency.",
                ref(
                    "The Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "Among patients with AIDS wasting and significant weight loss, GH levels are increased in association with reduced IGF1 levels, a pattern typical of GH resistance seen with malnutrition.",
                ),
            ),
            note(
                f"{p}-n19",
                "The Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "How VAT predicts relative GH deficiency in HIV",
                "Increased visceral adipose tissue strongly predicts reduced overnight GH and pulse amplitude via FFAs, somatostatin, and reduced ghrelin.",
                ref(
                    "The Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "Relative GH deficiency is strongly predicted by increased VAT, with a multifactorial etiology likely including GH suppression from increased free fatty acids (FFAs) due to increased lipolytic rate, increased somatostatin tone, and reduced ghrelin.",
                ),
            ),
            note(
                f"{p}-n20",
                "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                "Why HbA1c alone is unreliable for diabetes in HIV",
                "ART-related macrocytosis lowers A1c sensitivity; a 5.8% cutoff improves detection versus 6.5%.",
                ref(
                    "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                    "Hemoglobin A1c (A1c) has been shown to underestimate levels of blood glucose in patients with HIV, particularly those with increased mean corpuscular volume resulting from specific ART agents.",
                ),
            ),
            note(
                f"{p}-n21",
                "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                "How protease inhibitors impair glucose uptake",
                "PIs decrease insulin sensitivity by inhibiting GLUT4-mediated glucose transport in vitro and in vivo.",
                ref(
                    "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                    "PIs have been shown to decrease glucose uptake by inhibiting the transport function of GLUT4 (glucose transporter type 4) in vitro and have been shown to reduce insulin sensitivity in vivo.",
                ),
            ),
            note(
                f"{p}-n22",
                "Treatment of AIDS Wasting and Loss of Lean Body Mass",
                "How testosterone treats AIDS wasting in hypogonadal men",
                "Intramuscular testosterone increases lean body mass about 2 kg over 6 months and improves quality of life.",
                ref(
                    "Treatment of AIDS Wasting and Loss of Lean Body Mass",
                    "Randomized studies of intramuscular testosterone for hypogonadal men with AIDS wasting suggest a beneficial effect of testosterone administration on lean body mass (2.0 kg over 6 months) and improved quality of life.",
                ),
            ),
            note(
                f"{p}-n23",
                "Treatments for Visceral Fat Accumulation",
                "How tesamorelin reduces HIV-associated visceral adiposity",
                "GHRH(1–44) reduced VAT 15.4% versus placebo without worsening glucose, and was FDA-approved for central fat accumulation in 2010.",
                ref(
                    "Treatments for Visceral Fat Accumulation",
                    "In the combined analysis of two large, randomized, placebo-controlled phase 3 trials of over 800 patients, GHRH(1–44) (tesamorelin) reduced VAT by 15.4% relative to placebo in PWH with central fat accumulation.",
                ),
            ),
            note(
                f"{p}-n24",
                "Weight Gain in the Modern ART Era: Potential Effects of Tenofovir Alafenamide and Integrase Strand Transfer Inhibitors",
                "Why integrase inhibitors promote weight gain on modern ART",
                "Dolutegravir-containing regimens produced greater weight gain than efavirenz in ADVANCE, with obesity incidence up to 28% in women.",
                ref(
                    "Weight Gain in the Modern ART Era: Potential Effects of Tenofovir Alafenamide and Integrase Strand Transfer Inhibitors",
                    "In the ADVANCE study, for example, ART-naive individuals with HIV in South Africa were randomized to one of three arms: DTG with TDF/FTC, DTG with TAF/FTC, or EFV plus TDF/FTC.",
                ),
            ),
            note(
                f"{p}-n25",
                "Lipids and Cardiovascular Disease in People With HIV",
                "Why cardiovascular risk is elevated beyond traditional factors",
                "PWH face roughly twofold CVD risk; inflammation and immune activation contribute beyond dyslipidemia and smoking.",
                ref(
                    "Lipids and Cardiovascular Disease in People With HIV",
                    "PWH face roughly twofold risk of CVD compared to the general population.",
                ),
            ),
            note(
                f"{p}-n26",
                "KEY POINTS",
                "How endocrine management reduces long-term HIV morbidity",
                "Treating insulin resistance, diabetes, and dyslipidemia may lower CVD risk; testosterone and GH address wasting, while GHRH reduces visceral fat in lipodystrophy.",
                ref(
                    "KEY POINTS",
                    "Endocrine management of insulin resistance, diabetes mellitus, and dyslipidemia, common among PWH, may reduce CVD risk in this population.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Medication Effects",
                "A 52-year-old man with well-controlled HIV on darunavir/ritonavir develops Cushingoid features on fluticasone for asthma, then adrenal crisis after stopping the inhaler. Mechanism?",
                [
                    "CYP3A4 inhibition increases systemic glucocorticoid exposure and adrenal suppression",
                    "Fluticasone directly destroys adrenal cortex like CMV",
                    "Ritonavir induces cortisol metabolism causing deficiency during use",
                    "HIV itself always causes primary adrenal hyperplasia",
                ],
                0,
                "Boosted PIs inhibit CYP3A4, raising inhaled steroid levels, suppressing the HPA axis, and precipitating crisis on withdrawal.",
                ref(
                    "Medication Effects",
                    "The resulting reduction in metabolism of the inhaled corticosteroid, via inhibition of CYP3A4 by ritonavir or cobicistat, can result in glucocorticoid excess, adrenal suppression, symptoms of Cushing syndrome, and potentially severe adrenal insufficiency with discontinuation of the inhaled corticosteroid.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Adrenal Insufficiency",
                "A 38-year-old man with advanced untreated HIV, disseminated CMV, hyponatremia, and fatigue is evaluated for adrenal insufficiency. Most likely primary adrenal cause historically?",
                [
                    "CMV adrenalitis with adrenal tissue destruction",
                    "Autoimmune Addison disease as in the general population",
                    "Pituitary prolactinoma causing secondary insufficiency",
                    "Excess endogenous cortisol from lipodystrophy alone",
                ],
                0,
                "CMV adrenalitis is the most common opportunistic cause of adrenal destruction in advanced HIV, though destruction is often subtotal.",
                ref(
                    "Adrenal Insufficiency",
                    "Adrenal insufficiency occurring in the context of advanced HIV disease is most often caused by tissue destruction of the adrenal glands from opportunistic infections.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Clinical Assessment",
                "A woman with HIV on ART for 5 years has fatigue and hyponatremia after stopping megestrol acetate for cachexia. Best initial adrenal evaluation?",
                [
                    "Cosyntropin stimulation test unless recent pituitary disease suspected",
                    "Immediate insulin tolerance test in all patients",
                    "Defer testing because adrenal disease is impossible on ART",
                    "Salivary cortisol only without further workup",
                ],
                0,
                "Cosyntropin is usually adequate first-line; special tests are reserved for suspected recent hypothalamic-pituitary insufficiency.",
                ref(
                    "Clinical Assessment",
                    "Cosyntropin testing is usually an adequate first step, except in those patients in whom hypothalamic or pituitary insufficiency of recent onset is suspected.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Male Gonadal Dysfunction",
                "A 45-year-old man with HIV on ART has low libido. Total testosterone is normal but calculated free testosterone is low with inappropriately normal LH/FSH. Interpretation?",
                [
                    "Secondary hypogonadism; SHBG elevation may mask low free testosterone",
                    "Primary testicular failure requiring immediate high-dose anabolic steroids",
                    "Normal androgen status; no further testing needed",
                    "Efavirenz-induced primary hypergonadism",
                ],
                0,
                "Hypogonadism is usually secondary with low/normal gonadotropins; SHBG is increased in many patients, so free testosterone is essential.",
                ref(
                    "Male Gonadal Dysfunction",
                    "Sex hormone-binding globulin (SHBG) levels are increased in 30% to 55% of patients with HIV.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Male Gonadal Dysfunction",
                "A clinician orders an analogue free-testosterone radioimmunoassay in a man with HIV and elevated SHBG. Pitfall?",
                [
                    "Analogue assays are not independent of SHBG and have poor sensitivity",
                    "Analogue assays are the gold standard preferred over dialysis",
                    "SHBG is always low in HIV, making free testosterone unnecessary",
                    "Total testosterone is more sensitive than any free testosterone method",
                ],
                0,
                "Analogue free-testosterone assays are not SHBG-independent; equilibrium dialysis or calculation is preferred.",
                ref(
                    "Male Gonadal Dysfunction",
                    "As a caveat, analogue assays of free testosterone may not be independent of SHBG and should not be used.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Male Gonadal Dysfunction",
                "A 40-year-old man with HIV develops gynecomastia on efavirenz-containing ART. Mechanism?",
                [
                    "Direct estrogen receptor activation by efavirenz",
                    "Excess testosterone aromatization from PI-induced CYP inhibition only",
                    "Primary prolactin deficiency",
                    "GH excess from integrase inhibitor therapy",
                ],
                0,
                "Efavirenz is most closely associated with gynecomastia through direct estrogen receptor activation.",
                ref(
                    "Male Gonadal Dysfunction",
                    "Of ART medications, efavirenz (EFV) is most closely associated with gynecomastia, which is due to direct activation of the estrogen receptor.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Female Gonadal Dysfunction",
                "A 34-year-old woman with HIV and low CD4 reports amenorrhea. Compared with HIV-uninfected women, her odds of amenorrhea are?",
                [
                    "Approximately 62% higher per meta-analysis",
                    "Identical because ART normalizes all gonadal function",
                    "Lower because HIV protects ovarian reserve",
                    "Only increased if she uses protease inhibitors",
                ],
                0,
                "Meta-analysis shows amenorrhea in 2% to 7% of premenopausal women with HIV with 62% higher odds than controls.",
                ref(
                    "Female Gonadal Dysfunction",
                    "the odds of amenorrhea were 62% higher in women with HIV compared to those without.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Thyroid Function",
                "A 29-year-old woman starts ART and develops Graves disease 2 years later with suppressed TSH and elevated T4. Management consideration?",
                [
                    "Radioactive iodine has been used successfully in HIV-associated immune reconstitution Graves",
                    "Immediate total thyroidectomy is always contraindicated in HIV",
                    "ART must be stopped permanently to treat Graves",
                    "Routine thyroid surveillance is mandatory for all new ART patients per guidelines",
                ],
                0,
                "Immune reconstitution Graves may occur years after ART; RAI has been used successfully; routine screening is not recommended.",
                ref(
                    "Thyroid Function",
                    "Patients with HIV and Graves disease due to immune reconstitution have been successfully treated with radioactive iodine.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Thyroid Function",
                "A man with virologically suppressed HIV on modern ART asks about routine annual thyroid labs. Best guidance?",
                [
                    "No routine screening; test when clinically indicated",
                    "Mandatory TSH every 3 months for all PWH on ART",
                    "Thyroid disease is universally more prevalent on suppressed ART",
                    "Only children require any thyroid assessment in HIV",
                ],
                0,
                "In virologically controlled adults, overt thyroid disease prevalence is not increased; clinical suspicion should guide testing.",
                ref(
                    "Thyroid Function",
                    "At present, evidence does not report routine screening of thyroid studies in adults living with HIV.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Sodium",
                "A hospitalized patient with AIDS has sodium 125 mmol/L, euvolemia, and concentrated urine. Likely diagnosis?",
                [
                    "Syndrome of inappropriate antidiuretic hormone secretion (SIADH)",
                    "Primary hyperaldosteronism with hypertension",
                    "Diabetes insipidus from integrase inhibitor",
                    "Factitious hyponatremia from water restriction alone",
                ],
                0,
                "SIADH is common among hyponatremic AIDS patients (23% to 47%) and is treated with fluid restriction and hypertonic saline if severe.",
                ref(
                    "Sodium",
                    "SIADH (volume-replete patients with low levels of serum sodium, and inappropriately elevated levels of urine osmolarity) is seen in 23% to 47% of hyponatremic patients.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Potassium",
                "A patient with HIV on TMP-SMX for Pneumocystis prophylaxis develops potassium 6.2 mmol/L without renal failure. Mechanism?",
                [
                    "Trimethoprim inhibits tubular potassium secretion like amiloride",
                    "Tenofovir-induced Fanconi syndrome with potassium retention",
                    "Excess mineralocorticoid from efavirenz",
                    "GH deficiency causing pseudohyperkalemia",
                ],
                0,
                "Trimethoprim structurally resembles amiloride and inhibits tubular K+ secretion, causing hyperkalemia in 20% to 53% of AIDS patients.",
                ref(
                    "Potassium",
                    "Hyperkalemia occurs in 20% to 53% of AIDS patients on trimethoprim because of structural similarities to amiloride and inhibition of tubular potassium excretion.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Calcium Homeostasis",
                "A man with HIV on efavirenz has low 25-hydroxyvitamin D. Primary ART-related mechanism?",
                [
                    "Increased CYP24A-mediated catabolism of 25-hydroxyvitamin D",
                    "Direct PTH suppression by integrase inhibitors",
                    "Excess dietary calcium from ART formulations",
                    "PI stimulation of 1α-hydroxylase only",
                ],
                0,
                "Efavirenz increases conversion of 25-hydroxyvitamin D to 24,25-dihydroxyvitamin D3 via CYP24A induction.",
                ref(
                    "Calcium Homeostasis",
                    "increased conversion of 25-hydroxyvitamin D to 24,25-dihydroxyvitamin D3 by efavirenz",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                "A 55-year-old man with HIV, low BMI, and long-term TDF/PI therapy needs ART optimization for fracture prevention. Best recommendation?",
                [
                    "Avoid TDF and PIs when at fracture risk; consider switch to TAF or integrase-based regimens",
                    "Continue TDF and PI because they improve BMD",
                    "Withhold ART entirely to preserve bone",
                    "Routine teriparatide for all patients regardless of BMD",
                ],
                0,
                "Current recommendations advise avoiding TDF and PIs in PWH at fracture risk; switching may improve BMD.",
                ref(
                    "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                    "Current recommendations suggest that TDF should be avoided for the initial or continued treatment of PWH at risk for fracture.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                "A treatment-naive patient with HIV and osteoporosis risk starts TDF-based ART. Evidence-based strategy to limit bone loss?",
                [
                    "Vitamin D 4000 IU/day plus calcium 1000 mg/day or pre-ART zoledronic acid",
                    "No intervention because ART never affects bone",
                    "High-dose megestrol acetate for bone anabolism",
                    "Stop ART after 6 months to recover BMD",
                ],
                0,
                "High-dose vitamin D/calcium attenuates ART-initiation bone loss by 50%; single-dose zoledronic acid prevented loss over 96 weeks.",
                ref(
                    "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                    "In another randomized trial, a single dose of zoledronic acid (5 mg) before ART initiation prevented bone loss over 96 weeks;",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                "FRAX without BMD underestimates 10-year fracture risk in a 60-year-old woman with HIV. Improvement?",
                [
                    "Include HIV as a secondary cause of osteoporosis in FRAX",
                    "FRAX cannot be used in any patient with HIV",
                    "Subtract 10 years from age when entering FRAX",
                    "Ignore fracture risk because HIV protects bone",
                ],
                0,
                "FRAX tends to underestimate fracture risk in PWH; accuracy improves by including HIV as a secondary osteoporosis cause.",
                ref(
                    "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                    "When using FRAX without a BMD measurement, accuracy can be improved by including HIV as a secondary cause of osteoporosis.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "The Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "A man with AIDS wasting has high GH and low IGF1. Pattern?",
                [
                    "GH resistance typical of malnutrition-related wasting",
                    "Primary GH deficiency requiring immediate GHRH",
                    "Acromegaly from excess GHRH-secreting tumor",
                    "Normal axis; no endocrine abnormality",
                ],
                0,
                "AIDS wasting shows elevated GH with reduced IGF1, consistent with nutrition-mediated GH resistance.",
                ref(
                    "The Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "Among patients with AIDS wasting and significant weight loss, GH levels are increased in association with reduced IGF1 levels, a pattern typical of GH resistance seen with malnutrition.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                "A man with HIV on an older PI regimen has fasting glucose 142 mg/dL. HbA1c is 5.9% despite hyperglycemia. Explanation?",
                [
                    "HbA1c underestimates glycemia in HIV, especially with ART-related macrocytosis",
                    "HbA1c always overestimates glucose in HIV",
                    "PIs lower red cell lifespan causing falsely high A1c",
                    "Diabetes cannot occur in patients on ART",
                ],
                0,
                "A1c underestimates blood glucose in HIV; lower cutoffs (e.g., 5.8%) improve sensitivity.",
                ref(
                    "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                    "Hemoglobin A1c (A1c) has been shown to underestimate levels of blood glucose in patients with HIV, particularly those with increased mean corpuscular volume resulting from specific ART agents.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                "A patient switches from an integrase inhibitor to a first-generation PI and develops worsening insulin resistance. Proposed direct drug mechanism?",
                [
                    "Inhibition of GLUT4-mediated glucose transport",
                    "Excess insulin secretion from beta-cell hyperplasia only",
                    "GH deficiency from PI therapy",
                    "Increased adiponectin from PI-induced fat gain",
                ],
                0,
                "PIs reduce insulin sensitivity partly by inhibiting GLUT4 glucose transport.",
                ref(
                    "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                    "PIs have been shown to decrease glucose uptake by inhibiting the transport function of GLUT4 (glucose transporter type 4) in vitro",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Treatment of AIDS Wasting and Loss of Lean Body Mass",
                "A hypogonadal man with AIDS wasting seeks therapy to increase muscle mass. Evidence-based option?",
                [
                    "Physiologic testosterone replacement after diagnostic workup",
                    "Megestrol acetate as first-line lean-mass anabolic therapy",
                    "High-dose GH for all eugonadal patients without caution",
                    "GnRH agonist to stimulate endogenous testosterone",
                ],
                0,
                "Testosterone increases lean mass ~2 kg over 6 months in hypogonadal men with AIDS wasting; megestrol adds fat not lean mass.",
                ref(
                    "Treatment of AIDS Wasting and Loss of Lean Body Mass",
                    "Randomized studies of intramuscular testosterone for hypogonadal men with AIDS wasting suggest a beneficial effect of testosterone administration on lean body mass (2.0 kg over 6 months) and improved quality of life.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Treatments for Visceral Fat Accumulation",
                "A man with HIV lipodystrophy and excess visceral fat asks about FDA-approved therapy that avoids worsening glucose. Best option?",
                [
                    "Tesamorelin (GHRH 1–44)",
                    "High-dose recombinant GH as first-line long-term therapy",
                    "Megestrol acetate for visceral fat reduction",
                    "Leptin replacement FDA-approved specifically for HIV lipodystrophy",
                ],
                0,
                "Tesamorelin reduced VAT 15.4% without raising glucose and was FDA-approved in 2010; GH worsens glucose.",
                ref(
                    "Treatments for Visceral Fat Accumulation",
                    "GHRH(1–44) was approved by the FDA for the treatment of central fat accumulation in PWH in 2010.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Changes in Fat Mass and Distribution",
                "A patient on stavudine and a PI develops facial lipoatrophy and central fat gain. Primary peripheral fat-loss mechanism?",
                [
                    "NRTI mitochondrial toxicity and PI effects on adipogenesis (SREBP1/PPARγ)",
                    "Excess testosterone aromatization only",
                    "Primary Cushing disease from HIV viremia",
                    "Integrase inhibitor-induced subcutaneous fat gain",
                ],
                0,
                "NRTIs inhibit mitochondrial DNA polymerase gamma; PIs inhibit SREBP1 nuclear localization and PPARγ, causing lipoatrophy.",
                ref(
                    "Changes in Fat Mass and Distribution",
                    "NRTIs variably inhibit mitochondrial DNA polymerase gamma and contribute to mitochondrial dysfunction.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Weight Gain in the Modern ART Era: Potential Effects of Tenofovir Alafenamide and Integrase Strand Transfer Inhibitors",
                "An ART-naive woman starts dolutegravir/TAF/FTC and gains 7 kg over 96 weeks versus 2.3 kg on EFV/TDF/FTC. Interpretation?",
                [
                    "Integrase inhibitors, especially with TAF, are associated with greater weight gain than EFV in trials",
                    "EFV always causes more weight gain than integrase inhibitors",
                    "Weight change is unrelated to ART class",
                    "TDF is the primary driver of obesity in ADVANCE",
                ],
                0,
                "ADVANCE showed greater weight gain with DTG-containing arms than EFV, with higher obesity incidence in women.",
                ref(
                    "Weight Gain in the Modern ART Era: Potential Effects of Tenofovir Alafenamide and Integrase Strand Transfer Inhibitors",
                    "Over 96 weeks, those persons randomized to DTG gained more weight (mean 7.1 kg with a TAF-containing regimen and 4.3 kg with a TDF-containing regimen) compared to those randomized to EFV (mean 2.3 kg).",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Lipid Abnormalities",
                "A patient with HIV not on ART has low HDL, low LDL, and hypertriglyceridemia with advanced disease. Explanation?",
                [
                    "Viral infection and inflammation alter lipids before ART-related changes",
                    "All untreated HIV patients have high HDL",
                    "Integrase inhibitors cause this pattern before any ART",
                    "Statin therapy is mandatory before starting ART",
                ],
                0,
                "Untreated HIV lowers TC, HDL, and LDL while hypertriglyceridemia increases with advanced disease.",
                ref(
                    "Lipid Abnormalities",
                    "Those with HIV not receiving ART generally demonstrate reductions in TC, HDL-C, and low-density lipoprotein cholesterol (LDL-C).",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Treatment of Hyperlipidemia Among PWH",
                "A man with HIV on ritonavir-boosted ART needs statin therapy for high LDL. Safest statin choice per interactions?",
                [
                    "Pitavastatin, which does not interact with current antiretrovirals",
                    "Simvastatin at high dose with ritonavir",
                    "Lovastatin combined with cobicistat",
                    "No statin is ever safe with any ART",
                ],
                0,
                "Simvastatin and lovastatin should be avoided with CYP450-inhibiting ART; pitavastatin has no interactions with current antiretrovirals.",
                ref(
                    "Treatment of Hyperlipidemia Among PWH",
                    "Pitavastatin does not interact with any current antiretrovirals.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Lipids and Cardiovascular Disease in People With HIV",
                "A 48-year-old man with suppressed HIV has MI risk above that predicted by Framingham score alone. Contributing nontraditional factor?",
                [
                    "Chronic inflammation and immune activation",
                    "Lower smoking rates than the general population",
                    "Protective effect of low CD4 count",
                    "Absence of dyslipidemia in all treated patients",
                ],
                0,
                "Traditional risk factors explain only part of excess MI risk; inflammation and immune activation are central.",
                ref(
                    "Lipids and Cardiovascular Disease in People With HIV",
                    "Although traditional cardiovascular (CV) risk factors like dyslipidemia and cigarette smoking account for some of the increased risk, other mechanisms including chronic inflammation and immune activation also appear central to CVD in PWH.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Treatment of AIDS Wasting and Loss of Lean Body Mass",
                "A cachectic patient with AIDS wasting is offered megestrol acetate for weight gain. Counseling point?",
                [
                    "Weight gain is mostly fat; abrupt withdrawal may precipitate adrenal crisis",
                    "Megestrol reliably increases lean body mass like testosterone",
                    "Megestrol has no glucocorticoid activity or metabolic side effects",
                    "Megestrol is preferred over ART optimization for muscle mass",
                ],
                0,
                "Megestrol increases weight mainly as fat, causes hypogonadism/hyperglycemia, and abrupt stop can cause adrenal crisis.",
                ref(
                    "Treatment of AIDS Wasting and Loss of Lean Body Mass",
                    "However, the change in weight is almost entirely fat mass without an increase in lean body mass.",
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
                "Fracture incidence is increased among people with HIV and has multiple contributing factors including ART and vitamin D deficiency.",
                True,
                "KEY POINTS list increased fractures with multifactorial etiology including bone turnover, ART, immune activation, vitamin D, and hypogonadism.",
                ref(
                    "KEY POINTS",
                    "Fracture incidence is increased among people with HIV (PWH) and is multifactorial in nature, potentially related to increases in bone turnover, certain antiretroviral medications, immune activation, vitamin D deficiency, and gonadal dysfunction.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Adrenal Function",
                "Clinically relevant adrenal insufficiency is common among patients with virologically controlled HIV on ART.",
                False,
                "Adrenal dysfunction is less common with virologic control; insufficient evidence supports increased clinically relevant insufficiency in this group.",
                ref(
                    "Adrenal Insufficiency",
                    "In the current era, data on adrenal function in individuals with virologically controlled HIV are sparse, and there is insufficient evidence to support an increased prevalence of clinically relevant adrenal insufficiency in this population.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Male Gonadal Dysfunction",
                "Reliance on total testosterone alone would have missed 33% of hypogonadal men with HIV in the MACS study.",
                True,
                "Free testosterone calculated by the Vermeulen equation was lower in men with HIV despite similar total testosterone.",
                ref(
                    "Male Gonadal Dysfunction",
                    "Reliance on total testosterone alone would have missed 33% of patients with hypogonadism.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Thyroid Function",
                "Graves disease after ART may develop several years after treatment initiation.",
                True,
                "Immune reconstitution Graves has median onset 29.5 to 63 months after ART in cohort studies.",
                ref(
                    "Thyroid Function",
                    "Graves disease may develop several years after initiation of ART, with a median time between ART initiation and Graves of 29.5 months in one cohort",
                ),
            ),
            tf(
                f"{p}-t5",
                "Sodium",
                "Adrenal insufficiency is documented in 30% of volume-depleted, hyponatremic patients with HIV.",
                True,
                "Volume depletion and SIADH are common causes; adrenal insufficiency contributes substantially among hyponatremic hospitalized patients.",
                ref(
                    "Sodium",
                    "Adrenal insufficiency is documented in 30% of volume-depleted, hyponatremic patients with HIV.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                "The first 2 years after ART initiation are associated with a 2% to 6% decrease in BMD, greater with TDF or PIs.",
                True,
                "ART initiation causes early BMD loss, amplified by TDF and PI exposure.",
                ref(
                    "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                    "The first 2 years after the initiation of ART is associated with a 2% to 6% decrease in BMD with the larger decreases in this range observed in those receiving TDF or PIs.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                "Integrase strand transfer inhibitors have been associated with diabetes risk in recent studies.",
                True,
                "InSTIs, widely used in modern regimens, are linked to diabetes risk though mechanisms need further study.",
                ref(
                    "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                    "Most recently, integrase strand transfer inhibitors (InSTIs), which are used widely, have been associated with diabetes risk.",
                ),
            ),
            tf(
                f"{p}-t8",
                "The AIDS Wasting Syndrome and Loss of Lean Body Mass",
                "AIDS wasting is characterized by disproportionate loss of lean body mass with relative sparing of fat in men.",
                True,
                "Wasting features sarcopenia; women may lose fat disproportionately with progression.",
                ref(
                    "The AIDS Wasting Syndrome and Loss of Lean Body Mass",
                    "It is characterized by a disproportionate loss of lean body mass, with a relative sparing of body fat, particularly in men.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Treatments for Visceral Fat Accumulation",
                "Low-dose GH was approved by the FDA for HIV lipodystrophy because it improves glucose tolerance.",
                False,
                "GH reduced VAT but increased 2-hour glucose and was not FDA-approved; tesamorelin was approved instead.",
                ref(
                    "Treatments for Visceral Fat Accumulation",
                    "Largely because of its ability to aggravate glucose, GH was not approved by the FDA for HIV lipodystrophy.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Treatment of Lipoatrophy",
                "Switching off stavudine is an established treatment for lipoatrophy, though changes may be incomplete.",
                True,
                "No other established lipoatrophy therapy exists beyond switching contributing ART.",
                ref(
                    "Treatment of Lipoatrophy",
                    "There are no established treatments for lipoatrophy except for switching off contributing ART, such as stavudine.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Lipids and Cardiovascular Disease in People With HIV",
                "People with HIV have roughly twofold increased cardiovascular disease risk compared with the general population.",
                True,
                "CVD risk is approximately doubled in PWH from multiple mechanisms.",
                ref(
                    "Lipids and Cardiovascular Disease in People With HIV",
                    "PWH face roughly twofold risk of CVD compared to the general population.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Treatment of Hyperlipidemia Among PWH",
                "Simvastatin and lovastatin should generally be avoided in people with HIV on interacting antiretrovirals.",
                True,
                "CYP450 inhibitors like ritonavir and cobicistat raise levels of these statins severalfold.",
                ref(
                    "Treatment of Hyperlipidemia Among PWH",
                    "Simvastatin and lovastatin are highly metabolized by CYP450 and should generally be avoided in PWH.",
                ),
            ),
            tf(
                f"{p}-t13",
                "KEY POINTS",
                "Medications used to treat HIV have no endocrine or metabolic effects.",
                False,
                "KEY POINTS note numerous ART effects on steroid metabolism, gonadal function, vitamin D, phosphate, glucose, and lipids.",
                ref(
                    "KEY POINTS",
                    "Medications used in the treatment of HIV disease have numerous endocrine and metabolic effects, including effects on steroid metabolism, gonadal function, vitamin D synthesis, renal phosphate excretion, glucose uptake, and very low-density lipoprotein metabolism.",
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
                "Assertion: Ritonavir or cobicistat combined with inhaled corticosteroids can cause iatrogenic adrenal insufficiency on steroid withdrawal.",
                "Reason: Boosted antiretrovirals induce CYP3A4 and accelerate corticosteroid clearance.",
                2,
                "Assertion true—CYP3A4 inhibition increases steroid exposure; reason false—inhibition slows metabolism, not induces clearance.",
                ref(
                    "Medication Effects",
                    "via inhibition of CYP3A4 by ritonavir or cobicistat",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Male Gonadal Dysfunction",
                "Assertion: Hypogonadism in men with HIV should be assessed with free testosterone measurement.",
                "Reason: SHBG is decreased in most patients with HIV, making total testosterone falsely low.",
                2,
                "Assertion true; reason false—SHBG is increased in 30% to 55%, making total testosterone falsely normal/high.",
                ref(
                    "Male Gonadal Dysfunction",
                    "Sex hormone-binding globulin (SHBG) levels are increased in 30% to 55% of patients with HIV.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Adrenal Insufficiency",
                "Assertion: CMV adrenalitis is the most common cause of adrenal destruction in advanced HIV.",
                "Reason: CMV always destroys more than 50% of adrenal cortex, invariably causing clinical insufficiency.",
                2,
                "Assertion true; reason false—CMV destruction is usually less than 50% and unlikely alone to cause insufficiency.",
                ref(
                    "Adrenal Insufficiency",
                    "However, adrenocortical destruction caused by CMV is usually less than 50% and therefore unlikely to cause adrenal insufficiency,",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Thyroid Function",
                "Assertion: Immune reconstitution after ART can cause Graves disease.",
                "Reason: Graves occurs exclusively within the first week of ART initiation.",
                2,
                "Assertion true; reason false—Graves may develop years after ART (median 29.5–63 months).",
                ref(
                    "Thyroid Function",
                    "Graves disease may develop several years after initiation of ART, with a median time between ART initiation and Graves of 29.5 months in one cohort",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                "Assertion: TDF use is associated with bone loss in people with HIV.",
                "Reason: TDF improves proximal tubule phosphate reabsorption and increases BMD.",
                2,
                "Assertion true; reason false—TDF causes phosphate wasting/tubulopathy and bone loss.",
                ref(
                    "Bone Loss: Prevalence, Etiologic Factors, and Treatment Strategies",
                    "Studies demonstrate that switching to a TDF-based regimen is associated with bone loss and increased bone turnover",
                ),
            ),
            ar(
                f"{p}-ar6",
                "The Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "Assertion: Patients with HIV and central fat accumulation may have relative GH deficiency.",
                "Reason: Relative GH deficiency is predicted by increased visceral adipose tissue.",
                0,
                "Both true and linked—increased VAT predicts reduced GH secretion via multiple mechanisms.",
                ref(
                    "The Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "Relative GH deficiency is strongly predicted by increased VAT, with a multifactorial etiology likely including GH suppression from increased free fatty acids (FFAs) due to increased lipolytic rate, increased somatostatin tone, and reduced ghrelin.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                "Assertion: Protease inhibitors can reduce insulin sensitivity in people with HIV.",
                "Reason: PIs inhibit GLUT4-mediated glucose transport.",
                0,
                "Both true and causally linked—PIs impair GLUT4 function in vitro and reduce insulin sensitivity in vivo.",
                ref(
                    "Epidemiology of Diabetes Mellitus and Insulin Resistance",
                    "PIs have been shown to decrease glucose uptake by inhibiting the transport function of GLUT4 (glucose transporter type 4) in vitro and have been shown to reduce insulin sensitivity in vivo.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Treatment of AIDS Wasting and Loss of Lean Body Mass",
                "Assertion: Megestrol acetate increases weight in patients with AIDS wasting.",
                "Reason: Megestrol increases lean body mass comparably to testosterone.",
                2,
                "Assertion true—megestrol increases weight 3–4 kg; reason false—gain is almost entirely fat mass.",
                ref(
                    "Treatment of AIDS Wasting and Loss of Lean Body Mass",
                    "Randomized studies in the literature show that megestrol acetate increases weight 3 to 4 kg over 12 weeks with an increase in caloric intake.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Treatments for Visceral Fat Accumulation",
                "Assertion: Tesamorelin reduces visceral adipose tissue in HIV lipodystrophy.",
                "Reason: Tesamorelin significantly reduces subcutaneous adipose tissue as its primary effect.",
                2,
                "Assertion true—VAT reduced 15.4%; reason false—no clinically significant SAT reduction; selective for VAT.",
                ref(
                    "Treatments for Visceral Fat Accumulation",
                    "Interestingly, no clinically significant effect to reduce SAT was seen, and thus GHRH(1–44) was selective for VAT.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Changes in Fat Mass and Distribution",
                "Assertion: NRTIs contribute to HIV-associated lipoatrophy.",
                "Reason: NRTIs stimulate mitochondrial DNA polymerase gamma in adipocytes.",
                2,
                "Assertion true; reason false—NRTIs inhibit mitochondrial DNA polymerase gamma, causing mitochondrial dysfunction.",
                ref(
                    "Changes in Fat Mass and Distribution",
                    "NRTIs variably inhibit mitochondrial DNA polymerase gamma and contribute to mitochondrial dysfunction.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Lipids and Cardiovascular Disease in People With HIV",
                "Assertion: Traditional risk factors do not fully explain excess myocardial infarction risk in HIV.",
                "Reason: HIV serostatus confers no independent MI risk after adjusting for age, gender, and race.",
                2,
                "Assertion true—DM/HTN/dyslipidemia explain only ~25% of excess risk; reason false—HIV remains associated with increased MI (RR 1.75).",
                ref(
                    "Lipids and Cardiovascular Disease in People With HIV",
                    "Triant and colleagues demonstrated an RR of 1.75 (95% CI, 1.51–2.02; p <0.0001) for increased MI in individuals with and without HIV in a model accounting for age, gender, and race",
                ),
            ),
            ar(
                f"{p}-ar12",
                "KEY POINTS",
                "Assertion: Endocrine strategies may treat sarcopenia in AIDS wasting or reduce visceral fat in HIV lipodystrophy.",
                "Reason: AIDS wasting and HIV lipodystrophy are identical syndromes with the same treatment approach.",
                2,
                "Assertion true—testosterone/GH for wasting, GHRH for visceral fat; reason false—they must be distinguished.",
                ref(
                    "KEY POINTS",
                    "Acquired immunodeficiency syndrome (AIDS) wasting, characterized by sarcopenia, should be distinguished from HIV lipodystrophy, which is characterized by subcutaneous fat loss.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "46",
        "title": "Endocrinology of HIV/AIDS",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Takara Stanley and Todd T. Brown",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_46_Endocrinology_of_HIVAIDS.md",
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
