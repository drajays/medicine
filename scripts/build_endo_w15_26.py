#!/usr/bin/env python3
"""Generate Williams 15e module w15-26 — Endocrine Function and Aging."""
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
OUT_NAME = "w15-26_Endocrine_Function_and_Aging.json"


def build() -> dict:
    p = "w15-26"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why endocrine–aging interactions need clearer physiologic meaning",
                "Bidirectional hormone–aging relationships require understanding whether age-related endocrine changes are biomarkers, mechanisms, or protective adaptations before hormone manipulation is justified.",
                ref(
                    "KEY POINTS",
                    "Interactions between the endocrine system and aging include age-related changes in the secretion and actions of hormones, as well as the evolutionarily conserved influence of hormonal signaling on the biologic process of aging. A clearer understanding of the physiologic meaning of the age-related endocrine changes is needed to establish the role of hormone manipulations to delay or reverse aging.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How menopause defines the most dramatic endocrine aging event",
                "Menopause is permanent cessation of menstruation from loss of ovarian follicular function—the cardinal age-related endocrine change in women.",
                ref(
                    "KEY POINTS",
                    "The most dramatic age-related endocrine change is represented in menopause, defined as the permanent cessation of menstruation resulting from the loss of ovarian follicular function.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why isolated TSH rise in elders is often misclassified",
                "TSH rises with normal aging; many older adults labeled subclinically hypothyroid actually have age-appropriate TSH—overtreatment carries substantial risk.",
                ref(
                    "KEY POINTS",
                    "Thyroid-stimulating hormone (TSH) rises during normal aging, and many older adults with isolated TSH elevations are misclassified as subclinically hypothyroid, despite having age-appropriate TSH levels.",
                ),
            ),
            note(
                f"{p}-n4",
                "KEY POINTS",
                "How to threshold levothyroxine in older isolated TSH elevation",
                "Reserve thyroid hormone replacement for persistently elevated TSH >7 mIU/L (>10 mIU/L in oldest-old)—restoring youthful TSH lacks benefit and risks overtreatment.",
                ref(
                    "KEY POINTS",
                    "Thyroid hormone replacement in older adults with isolated TSH elevation should be reserved for those with TSH levels persistently above 7 mIU/L, and in the oldest-old, above 10 mIU/L, due to lack of benefits of restoring TSH to youthful levels and substantial risks of overtreatment.",
                ),
            ),
            note(
                f"{p}-n5",
                "KEY POINTS",
                "Why greater cortisol diurnal decline may protect older adults",
                "Phase-advanced circadian cortisol and possible HPA hyperactivity accompany aging, but a steeper diurnal cortisol decline and lower 24-hour average associate with less functional decline and mortality.",
                ref(
                    "KEY POINTS",
                    "A greater diurnal decline in cortisol and lower 24-hour average cortisol secretion have been associated with reduced risks for functional decline, morbidity, and mortality in older individuals.",
                ),
            ),
            note(
                f"{p}-n6",
                "KEY POINTS",
                "How DHEA declines and what replacement actually achieves",
                "DHEA falls with adrenal zona reticularis atrophy; oral DHEA modestly improves postmenopausal BMD and intravaginal DHEA treats genitourinary syndrome of menopause, but systemic antiaging benefits are unproven and sex-steroid safety is unknown.",
                ref(
                    "KEY POINTS",
                    "Dehydroepiandrosterone (DHEA), a precursor for androgen and estrogen production in target tissues, declines with aging.",
                ),
            ),
            note(
                f"{p}-n7",
                "KEY POINTS",
                "Why obesity accelerates andropause and weight loss helps",
                "Testosterone declines with aging, accelerated by obesity and metabolic dysfunction; weight loss can normalize testosterone in overweight older men.",
                ref(
                    "KEY POINTS",
                    "Aging men experience a decline in testosterone, which is accelerated by obesity and metabolic dysfunction. In such men, weight loss may normalize testosterone levels.",
                ),
            ),
            note(
                f"{p}-n8",
                "KEY POINTS",
                "How somatopause (GH-IGF1 decline) should inform therapy decisions",
                "Physiologic GH-IGF1 decline improves body composition with GH replacement but not functional capacity, with adverse effects and uncertain long-term safety—antiaging GH is not recommended.",
                ref(
                    "KEY POINTS",
                    "During the aging process, growth hormone–insulin-like growth factor 1 (GH-IGF1) activity declines, but it is unclear if this attenuation is causal for age-related changes in body composition and functional capacity. GH replacement in older adults with physiologic decline in GH-IGF1 activity improves body composition but does not benefit overall functional capacity, and it is associated with adverse effects and uncertain long-term safety.",
                ),
            ),
            note(
                f"{p}-n9",
                "The Endocrinology of Aging",
                "WHI paradigm shift in postmenopausal hormone therapy",
                "Combined estrogen-progestin increased breast cancer, CHD, stroke, VTE, and probable dementia; estrogen alone raised stroke/VTE risk—HRT now reserved for short-term vasomotor symptoms, not disease prevention.",
                ref(
                    "The Endocrinology of Aging",
                    "Although estrogen replacement was a widely recommended treatment for postmenopausal women until the early 2000s, findings from the landmark Women's Health Initiative (WHI) study led to a paradigm shift after it demonstrated that, compared to placebo, combined estrogen and progesterone replacement increased the risk for invasive breast cancer, coronary heart disease, stroke, venous thromboembolism, $ ^{29} $ and probable dementia.",
                ),
            ),
            note(
                f"{p}-n10",
                "Thyroid Axis in Aging",
                "How NHANES data redefine 'normal' TSH with age",
                "In iodine-replete adults without thyroid disease, median TSH shifts from 1.26 mIU/L (ages 20–29) to 1.90 mIU/L (≥80 years); 97.5th percentile rises from 3.56 to 7.49 mIU/L—non-age-specific ranges overdiagnose subclinical hypothyroidism.",
                ref(
                    "Thyroid Axis in Aging",
                    "Median and the 97.5th percentile TSH values, respectively, shift from 1.26 and 3.56 mIU/L between the ages of 20 and 29 years to 1.90 and 7.49 mIU/L in those 80 years of age and above.",
                ),
            ),
            note(
                f"{p}-n11",
                "Thyroid Axis in Aging",
                "Why mildly elevated TSH may support healthy longevity",
                "Higher TSH with stable free T4 associates with longer survival; centenarians and offspring of long-lived parents show higher TSH with similar free T4—mild TSH elevation may be adaptive, not pathologic.",
                ref(
                    "Thyroid Axis in Aging",
                    "However, higher levels of TSH and lower levels of  $ T_{4} $ may be advantageous for healthy aging and longevity, because in longitudinal studies, age-associated rise in TSH was found to be neutral $ ^{42} $ or associated with longer survival, $ ^{45} $ whereas rise in free  $ T_{4} $ was associated with higher mortality.",
                ),
            ),
            note(
                f"{p}-n12",
                "Adrenal Axis in Aging",
                "How aging shifts the cortisol circadian rhythm",
                "Older adults show 1–2 hour phase advance of morning cortisol peak and evening nadir, with relative flattening of the diurnal curve—overlap with sleep disruption remains unresolved.",
                ref(
                    "Adrenal Axis in Aging",
                    "Most reports agree that aged individuals display alterations in cortisol circadian rhythm, such that early morning maximum and evening nadir occur 1 to 2 hours earlier (phase advance) than in younger subjects.",
                ),
            ),
            note(
                f"{p}-n13",
                "Adrenal Axis in Aging",
                "Why sleep quality links to HPA dynamics in aging",
                "Greater diurnal cortisol decline associates with better physical performance and longer, less disturbed sleep—circadian/sleep disruption may interact with adrenal aging.",
                ref(
                    "Adrenal Axis in Aging",
                    "In cross-sectional studies conducted later in life, a more dynamic activity of the HPA axis, characterized by a greater diurnal decline, has been associated with better physical performance, $ ^{87-89} $ longer sleep duration and less sleep disturbance, $ ^{79} $ and lower prevalence of osteoporotic fractures $ ^{90} $ and type 2 diabetes (T2D).",
                ),
            ),
            note(
                f"{p}-n14",
                "Dehydroepiandrosterone in Aging",
                "DHEAS decline and intracrinology after menopause",
                "DHEAS peaks in the third decade then falls to ~20–30% of peak by age 70–80; in postmenopausal women nearly 100% of active sex steroids arise from adrenal precursors via intracrine synthesis in target tissues.",
                ref(
                    "Dehydroepiandrosterone in Aging",
                    "In postmenopausal women, nearly 100% of sex steroids are synthesized in peripheral tissues from precursors of adrenal origin, except for a small contribution from ovarian or adrenal testosterone and androstenedione.",
                ),
            ),
            note(
                f"{p}-n15",
                "DHEA Replacement Therapy",
                "How intravaginal DHEA treats genitourinary syndrome of menopause",
                "Daily intravaginal DHEA improves vaginal dryness and dyspareunia with minimal systemic hormone elevation—FDA-approved for moderate-to-severe menopausal dyspareunia.",
                ref(
                    "DHEA Replacement Therapy",
                    "Daily intravaginal administration of DHEA was shown to improve signs and symptoms of genitourinary syndrome of menopause, including vaginal dryness and pain with sexual activity, $ ^{130} $ and has been approved by the U.S. Food and Drug Administration for treatment of moderate to severe dyspareunia due to menopause.",
                ),
            ),
            note(
                f"{p}-n16",
                "DHEA Replacement Therapy",
                "Why oral DHEA is a weak osteoporosis strategy",
                "Oral DHEA consistently raises postmenopausal BMD modestly (~half the benefit of bisphosphonates) but RCTs lack fracture-power; in men pooled analyses show no BMD benefit.",
                ref(
                    "DHEA Replacement Therapy",
                    "A beneficial effect of oral DHEA administration has been constantly reported for increase in bone mineral density (BMD) in postmenopausal women, $ ^{114,116,123,129} $ possibly mediated by increases in serum estrogens. $ ^{116} $ These positive effects, however, were modest, equating to approximately half of the benefit observed with use of approved osteoporosis therapies, such as bisphosphonates.",
                ),
            ),
            note(
                f"{p}-n17",
                "Male Gonadal Axis in Aging",
                "How EMAS defines late-onset hypogonadism (andropause)",
                "LOH requires three sexual symptoms plus total testosterone <11 nmol/L and free testosterone <0.22 nmol/L; severe LOH uses total testosterone <8 nmol/L—prevalence 2.1% (5.1% in men 70–79).",
                ref(
                    "Male Gonadal Axis in Aging",
                    "The EMAS investigators proposed minimal diagnostic criteria for LOH, consisting of the \"syndromic\" simultaneous presence of three sexual symptoms (i.e., poor morning erections, decreased sexual interest, and erectile dysfunction), together with a serum total testosterone level less than 11 nmol/L (320 ng/dL), and free testosterone levels less than 0.22 nmol/L (6.4 ng/dL) (Fig. 26.5).",
                ),
            ),
            note(
                f"{p}-n18",
                "Male Gonadal Axis in Aging",
                "Why low testosterone without sexual symptoms matters less",
                "EMAS showed LOH associates with lower hemoglobin, muscle and bone mass, and poorer performance; biochemical low testosterone alone carries weaker health associations—symptoms define clinical relevance.",
                ref(
                    "Male Gonadal Axis in Aging",
                    "Men with LOH had lower hemoglobin, muscle, and bone mass and poorer physical performance and general health compared to their peers. Men with low testosterone only, irrespective of sexual symptoms, showed considerably lesser magnitude of associations with the same endpoints.",
                ),
            ),
            note(
                f"{p}-n19",
                "Somatotropic Axis in Aging",
                "How somatopause manifests physiologically",
                "GH pulse amplitude and duration fall with age, lowering 24-hour GH secretion despite preserved pulse frequency; IGF1 declines in parallel—hypothalamic signaling (reduced GHRH, increased somatostatin) drives somatopause.",
                ref(
                    "Somatotropic Axis in Aging",
                    "The activity of the somatotropic axis, clinically characterized by GH and insulin-like growth factor 1 (IGF1) levels, progressively declines with age. Mean GH pulses are lower in amplitude and shorter in duration in healthy older men and women compared with younger people $ ^{1,2,23} $ (Fig. 26.9).",
                ),
            ),
            note(
                f"{p}-n20",
                "Somatotropic Axis in Aging",
                "Why low IGF1 hazard differs by age (antagonistic pleiotropy)",
                "UK Biobank data show low IGF1 predicts greater disease/mortality hazard in younger adults but reduced hazard in older adults—age-appropriate somatotroph decline may be adaptive.",
                ref(
                    "Somatotropic Axis in Aging",
                    "Notably, over an average follow-up time of 11 years, the risk conferred by low IGF1 for the above diseases and mortality was much lower for older adults (baseline age 63–74 years) than for younger individuals (baseline age 37–50 years) $ ^{235} $ (Fig. 26.13).",
                ),
            ),
            note(
                f"{p}-n21",
                "Growth Hormone Replacement Therapy in Aging",
                "Rudman landmark trial: body composition without function",
                "Six months of biosynthetic GH in older men raised lean mass 8.8% and lowered fat 14.4% but also raised systolic BP and fasting glucose—composition changed without functional benefit.",
                ref(
                    "Growth Hormone Replacement Therapy in Aging",
                    "In the treatment group, lean body mass rose by 8.8%, skin thickness increased by 7.1%, lumbar vertebral density increased by 1.6%, and adipose mass decreased by 14.4%.",
                ),
            ),
            note(
                f"{p}-n22",
                "Growth Hormone Replacement Therapy in Aging",
                "How GH therapy fails sarcopenia and strength endpoints",
                "GH increases lean mass in elders but systematic reviews find no conclusive benefit on muscle strength or physical performance; GH plus exercise does not outperform exercise alone.",
                ref(
                    "Growth Hormone Replacement Therapy in Aging",
                    "A systematic review of pharmacologic interventions that increased GH or IGF1 levels did not find conclusive evidence for benefit for muscle strength or physical performance in individuals over age 65 years.",
                ),
            ),
            note(
                f"{p}-n23",
                "Parathyroid Hormone in Aging",
                "Why PTH rises with age independent of vitamin D",
                "Each decade above age 20 associates with 5–6% higher PTH even after excluding renal disease, low vitamin D, and hypercalcemia—age-specific PTH references prevent misclassification.",
                ref(
                    "Parathyroid Hormone in Aging",
                    "In one study of over 15,000 patients, after careful exclusion of individuals with a history of osteoporosis or known parathyroid disease, abnormal ionized calcium or phosphate levels, estimated glomerular filtration rate (eGFR) <60 mL/min/1.73m $ ^{2} $, or 25-hydroxyvitamin D of <50 nmol/L, it was found that each 10-year increase in age above age 20 was associated with a 5% to 6% increase in PTH concentrations.",
                ),
            ),
            note(
                f"{p}-n24",
                "Parathyroid Hormone in Aging",
                "How parathyroid VDR loss may drive age-related PTH elevation",
                "Parathyroid tissue shows inverse correlation of VDR and 1α-hydroxylase with age and positive correlation with PTH expression—reduced local vitamin D signaling may disinhibit PTH.",
                ref(
                    "Parathyroid Hormone in Aging",
                    "Age was inversely correlated with expression levels of vitamin D receptor (VDR), vitamin D  $ 1\\alpha $-hydroxylase enzyme, and 24-hydroxylase enzyme in the parathyroid glands. On the other hand, there was a positive correlation between age and PTH expression in the parathyroid tissue (Fig. 26.18).",
                ),
            ),
            note(
                f"{p}-n25",
                "The Endocrinology of Aging",
                "How menopause drives bone loss",
                "Hypoestrogenemia after ovarian failure causes vasomotor and genitourinary symptoms; prolonged estrogen deficiency reduces bone mass—WHI confirmed estrogen/progestin fracture protection but shifted risk-benefit calculus.",
                ref(
                    "The Endocrinology of Aging",
                    "Hypoestrogenemia causes many women to experience vasomotor and genitourinary symptoms, whereas prolonged estrogen loss leads to a decline in bone mass.",
                ),
            ),
            note(
                f"{p}-n26",
                "The Concept of Successful Aging",
                "Why antiaging hormone marketing outpaces evidence",
                "Sex steroids, thyroid hormone, DHEA, and GH have limited effects on elderly physical capacity with considerable adverse effects—consumer antiaging hormone claims are poorly supported, exaggerated, and often unsafe.",
                ref(
                    "The Concept of Successful Aging",
                    "However, evidence available to date indicates that hormonal interventions with sex steroids, thyroid hormone, DHEA, and/or GH have very limited effects on physical capacity in elderly individuals, whereas adverse effects are often considerable. Antiaging or rejuvenating effects of hormonal or hormone-related products advertised directly to consumers are generally poorly or not at all supported by data, are grossly exaggerated, are often unsafe, and sometimes are preposterous.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Thyroid Axis in Aging",
                "A healthy 82-year-old woman has TSH 6.2 mIU/L on two morning samples, normal free T4, no thyroid antibodies, and mild fatigue only. Best management?",
                [
                    "Observe without levothyroxine—TSH is within age-appropriate range",
                    "Start levothyroxine to normalize TSH below 2.5 mIU/L",
                    "Treat because any TSH >4.5 mIU/L is subclinical hypothyroidism",
                    "Radioactive iodine ablation for TSH suppression",
                ],
                0,
                "TSH 4.5–6.9 mIU/L falls within age-specific reference for older adults; observational data and RCTs show no benefit of treatment in this range with overtreatment risk.",
                ref(
                    "Thyroid Axis in Aging",
                    "With regard to older adults with TSH levels that are persistently above the upper limit of the reference range for the general population, most experts agree that levothyroxine replacement should not be prescribed to individuals with TSH levels in the range of 4.5 to 6.9 mIU/L, whereas it should be considered in most of those with TSH ≥10.0 mIU/L.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Thyroid Axis in Aging",
                "A geriatrician counsels that 70% of elders labeled subclinically hypothyroid using standard ranges would be reclassified normal with age-specific TSH references. Primary reason?",
                [
                    "TSH distribution shifts higher with healthy aging in iodine-replete populations",
                    "All older adults develop thyroid autoimmunity by age 80",
                    "Free T4 always falls below reference in aging",
                    "Centenarians uniformly require levothyroxine",
                ],
                0,
                "NHANES and longitudinal data show TSH rises with age independent of antibodies; non-age-specific ranges misclassify many euthyroid elders.",
                ref(
                    "Thyroid Axis in Aging",
                    "Seventy percent of older adults classified as having subclinical hypothyroidism based on non-age-specific TSH ranges (i.e., with TSH levels above 4.5 mIU/L, or the 97.5th percentile in the NHANES III $ ^{54} $) would be reclassified to \"normal\" if age-specific reference ranges were used.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Thyroid Axis in Aging",
                "An 88-year-old man has persistent TSH 8.5 mIU/L, normal free T4, no goiter or heart failure. Most appropriate next step?",
                [
                    "Observation—intermediate TSH often appropriate especially after age 85",
                    "Immediate high-dose levothyroxine (1.6 mcg/kg)",
                    "Thyroidectomy for TSH >7 mIU/L",
                    "Liothyronine monotherapy to lower TSH rapidly",
                ],
                0,
                "In absence of heart failure, goiter, or dyslipidemia, observation is likely appropriate for TSH 7.0–9.9 mIU/L, especially age ≥85.",
                ref(
                    "Thyroid Axis in Aging",
                    "In the absence of history of hemithyroidectomy, goiter, or dyslipidemia, observation without treatment is likely appropriate in most older adults with intermediate TSH levels (i.e., 7.0–9.9 mIU/L), especially in those age 85 years and older.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Adrenal Axis in Aging",
                "A 74-year-old with insomnia and early-morning fatigue has salivary cortisol with peak and nadir both shifted ~90 minutes earlier than young-adult norms. Best characterization?",
                [
                    "Phase advance of circadian cortisol secretion with aging",
                    "Complete loss of diurnal cortisol variation",
                    "Primary adrenal insufficiency requiring hydrocortisone",
                    "Cushing syndrome from ectopic ACTH",
                ],
                0,
                "Aged individuals commonly show 1–2 hour phase advance of morning cortisol maximum and evening nadir with relative curve flattening.",
                ref(
                    "Adrenal Axis in Aging",
                    "Most reports agree that aged individuals display alterations in cortisol circadian rhythm, such that early morning maximum and evening nadir occur 1 to 2 hours earlier (phase advance) than in younger subjects.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Adrenal Axis in Aging",
                "Among community-dwelling older adults, which cortisol pattern associates with better outcomes?",
                [
                    "Greater diurnal cortisol decline and lower 24-hour average secretion",
                    "Flat cortisol curve with high evening nadir",
                    "Highest possible 24-hour urinary free cortisol",
                    "Absent morning cortisol peak",
                ],
                0,
                "More dynamic HPA activity with steeper diurnal decline and lower average 24-hour cortisol links to better function and lower morbidity/mortality.",
                ref(
                    "Adrenal Axis in Aging",
                    "A more dynamic activity of the HPA axis, characterized by a greater diurnal decline in cortisol, and lower average 24-hour cortisol secretion have been associated with enhanced functional performance and protection from morbidity and mortality in older individuals.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Dehydroepiandrosterone in Aging",
                "A 68-year-old postmenopausal woman asks about oral DHEA 50 mg/day for 'antiaging.' Evidence-based counseling?",
                [
                    "No convincing benefit for delaying aging consequences; cancer safety of induced sex steroids unknown",
                    "Oral DHEA is FDA-approved to reverse menopause and prevent all fractures",
                    "DHEA reliably improves cognition in all older women per large RCTs",
                    "DHEA replaces need for bisphosphonates in osteoporosis",
                ],
                0,
                "Despite supplement popularity, compelling systemic antiaging benefits are lacking and safety of sex-steroid increases from oral DHEA is unknown.",
                ref(
                    "Dehydroepiandrosterone in Aging",
                    "There is no convincing evidence at present to recommend the use of DHEA for delaying or preventing the physiologic consequences of aging, and its safety is unknown.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "DHEA Replacement Therapy",
                "A 62-year-old with genitourinary syndrome of menopause and moderate dyspareunia prefers local therapy. FDA-approved option?",
                [
                    "Intravaginal DHEA for moderate-to-severe dyspareunia due to menopause",
                    "High-dose oral DHEA 100 mg daily",
                    "Testosterone gel for vulvovaginal atrophy",
                    "Growth hormone injections",
                ],
                0,
                "Intravaginal DHEA improves vaginal dryness and dyspareunia with intracrine action and is FDA-approved for moderate-to-severe menopausal dyspareunia.",
                ref(
                    "DHEA Replacement Therapy",
                    "Daily intravaginal administration of DHEA was shown to improve signs and symptoms of genitourinary syndrome of menopause, including vaginal dryness and pain with sexual activity, $ ^{130} $ and has been approved by the U.S. Food and Drug Administration for treatment of moderate to severe dyspareunia due to menopause.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Male Gonadal Axis in Aging",
                "A 72-year-old obese man (BMI 34) has total testosterone 9 nmol/L, low-normal LH, and erectile dysfunction. First-line endocrine strategy?",
                [
                    "Weight loss to address obesity-driven hypogonadotropic hypogonadism",
                    "Immediate testosterone gel without lifestyle intervention",
                    "GnRH pump for fertility preservation",
                    "No evaluation—testosterone always falls normally with age",
                ],
                0,
                "Obesity causally lowers testosterone via hypothalamic-pituitary dysfunction; weight loss increases testosterone in overweight men.",
                ref(
                    "Male Gonadal Axis in Aging",
                    "The association of obesity with hypogonadism is almost certainly causal, because in overweight or obese men with low testosterone levels, weight loss leads to increase of testosterone, $ ^{151} $ although the mechanistic underpinnings of this relationship remain unclear.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Male Gonadal Axis in Aging",
                "A 68-year-old has total testosterone 10 nmol/L and free testosterone 0.18 nmol/L but denies decreased libido, poor morning erections, and erectile dysfunction. Per EMAS, does he have LOH?",
                [
                    "No—LOH requires syndromic sexual symptoms plus biochemical thresholds",
                    "Yes—any low free testosterone defines LOH regardless of symptoms",
                    "Yes—LOH is diagnosed by age alone over 65",
                    "No—testosterone must be measured only in the afternoon",
                ],
                0,
                "EMAS LOH criteria require three sexual symptoms simultaneously with low total and free testosterone—biochemistry alone is insufficient.",
                ref(
                    "Male Gonadal Axis in Aging",
                    "The EMAS investigators proposed minimal diagnostic criteria for LOH, consisting of the \"syndromic\" simultaneous presence of three sexual symptoms (i.e., poor morning erections, decreased sexual interest, and erectile dysfunction), together with a serum total testosterone level less than 11 nmol/L (320 ng/dL), and free testosterone levels less than 0.22 nmol/L (6.4 ng/dL) (Fig. 26.5).",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Male Gonadal Axis in Aging",
                "A 66-year-old with LOH starts transdermal testosterone. Mandatory safety monitoring per guidelines includes:",
                [
                    "PSA, hematocrit, and prostate assessment",
                    "Weekly GH isoform testing",
                    "Monthly TSH suppression to <0.1 mIU/L",
                    "No monitoring required for gel formulations",
                ],
                0,
                "Guidelines mandate monitoring prostate size, PSA, and hematocrit during testosterone therapy in older men.",
                ref(
                    "Male Gonadal Axis in Aging",
                    "Monitoring of prostate size, PSA levels, and hematocrit is mandatory.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                "In TTrials, 12-month testosterone in men >65 with testosterone <275 ng/dL most clearly improved:",
                [
                    "Self-reported sexual function",
                    "Memory and other cognitive functions",
                    "Vitality (FACIT-Fatigue ≥4-point gain vs placebo)",
                    "6-minute walk distance in Physical Function Trial alone (significant)",
                ],
                0,
                "TTrials showed greater sexual-function improvement with testosterone; cognitive and vitality endpoints did not significantly benefit.",
                ref(
                    "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                    "These trials reported that in men age >65 years with testosterone levels below 9.5 nmol/L (275 ng/dL), a 12-month treatment with a transdermal testosterone gel, with dose adjustments to maintain testosterone levels in the midnormal range of young men, led to greater improvement in self-reported sexual function compared with placebo treatment.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                "A 70-year-old with LOH and unexplained anemia (hemoglobin 10.8 g/dL) is enrolled in TTrials Bone/Anemia substudies. Expected testosterone effect on anemia?",
                [
                    "Significant improvement in anemia of unknown cause",
                    "Worsening anemia requiring transfusion",
                    "No effect—testosterone only affects lipids",
                    "Megaloblastic anemia correction",
                ],
                0,
                "TTrials demonstrated testosterone significantly improved anemia due to unknown cause in older hypogonadal men.",
                ref(
                    "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                    "Testosterone treatment also significantly improved anemia due to unknown cause.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Somatotropic Axis in Aging",
                "A 75-year-old asks whether declining IGF1 causes his sarcopenia and whether GH will restore strength. Best evidence-based answer?",
                [
                    "GH may increase lean mass but does not improve muscle strength or functional capacity in older adults",
                    "GH reliably doubles grip strength within 3 months in all elders",
                    "IGF1 decline has no relationship to body composition",
                    "GH is FDA-approved antiaging therapy for healthy seniors",
                ],
                0,
                "GH replacement improves body composition but not strength/function; antiaging GH use in healthy elders is forbidden.",
                ref(
                    "Somatotropic Axis in Aging",
                    "Administration of GH in older adults causes an increase in lean body mass and an appreciable loss of fat mass. However, GH treatment does not improve muscle strength and functional capacity in older people, despite restoration of circulating IGF1 concentrations to young adult levels.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Growth Hormone Replacement Therapy in Aging",
                "A 'longevity clinic' offers rhGH to a healthy 70-year-old with low-normal IGF1. Major adverse-effect pitfall from RCTs?",
                [
                    "High rates of carpal tunnel syndrome, edema, arthralgias, and glucose intolerance",
                    "Universal improvement in cognition without side effects",
                    "GH is prohibited only in athletes—not in clinical antiaging use",
                    "No adverse effects occur below 0.03 mg/kg dosing",
                ],
                0,
                "GH trials in elders report frequent carpal tunnel syndrome, edema, arthralgias, and new glucose intolerance/diabetes.",
                ref(
                    "Growth Hormone Replacement Therapy in Aging",
                    "Carpal tunnel syndrome in 38% of women and 24% of men treated with GH compared to 7% of women and 0% of men on placebo.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Growth Hormone Replacement Therapy in Aging",
                "An older man completes 6 months of GH plus structured resistance training expecting additive strength gains. Trial evidence shows:",
                [
                    "GH does not add to exercise benefits for muscle mass or strength vs placebo",
                    "GH triples strength gains beyond exercise alone in all RCTs",
                    "Exercise is contraindicated during GH therapy",
                    "Only women benefit from GH plus exercise",
                ],
                0,
                "When GH was combined with resistance training, muscle mass and strength outcomes did not differ from placebo plus exercise.",
                ref(
                    "Growth Hormone Replacement Therapy in Aging",
                    "with resistance exercise training, effect on muscle mass and muscle strength did not differ from those seen with placebo treatment, which suggests that GH does not add to the beneficial effects of exercise.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "The Endocrinology of Aging",
                "A 58-year-old postmenopausal woman with only vasomotor symptoms asks about systemic HRT for osteoporosis prevention. Current recommendation after WHI?",
                [
                    "HRT for short-term vasomotor symptoms—not for disease prevention; use specific osteoporosis drugs",
                    "Combined estrogen-progestin for lifelong fracture and CHD prevention",
                    "Estrogen alone prevents dementia and stroke",
                    "No fracture benefit was ever shown with estrogen",
                ],
                0,
                "WHI shifted practice: HRT for vasomotor symptoms short-term; potent osteoporosis therapies replace estrogen for bone disease prevention.",
                ref(
                    "The Endocrinology of Aging",
                    "Based on these findings, hormone replacement is currently recommended for short-term treatment of vasomotor symptoms, but not for the prevention of age-related diseases. The availability of potent pharmacologic therapies specific for osteoporosis obviates the need to use estrogen for osteoporosis treatment.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "The Endocrinology of Aging",
                "A resident confuses female menopause with male andropause. Key distinction per Williams?",
                [
                    "Unlike menopause, male sex hormone deficiency syndrome has not been clearly defined",
                    "All men experience abrupt testosterone cessation at age 50 identical to menopause",
                    "Andropause affects 50% of men age 40–49 per EMAS LOH criteria",
                    "Testosterone never declines with chronologic age",
                ],
                0,
                "Female menopause is a defined event; male androgen deficiency syndrome lacks a clear universal definition unlike menopause.",
                ref(
                    "The Endocrinology of Aging",
                    "Nonetheless, the syndrome of male sex hormone deficiency, unlike female menopause, has not been clearly defined.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Parathyroid Hormone in Aging",
                "A 76-year-old with normal calcium and eGFR has PTH at the 95th percentile for young adults but within age-adjusted range. Misclassification risk if using single PTH reference?",
                [
                    "Approximately 11% of adults ≥70 would be labeled abnormally elevated",
                    "No older adults ever have elevated PTH",
                    "PTH never rises with age when vitamin D is normal",
                    "All elevated PTH in elders requires parathyroidectomy",
                ],
                0,
                "Using one PTH reference range misclassifies ~11% of adults ≥70 as abnormally high when age-specific ranges account for physiologic rise.",
                ref(
                    "Parathyroid Hormone in Aging",
                    "In addition, using a single PTH reference range for all age groups, rather than age-specific references ranges, resulted in misclassification of approximately 11% of adults age 70 and older as having abnormally elevated PTH.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Parathyroid Hormone in Aging",
                "Older men maintain normal ionized calcium yet have ~2-fold higher PTH than younger men. Dynamic testing suggests:",
                [
                    "Right-shifted calcium–PTH set-point with blunted calcium suppression of PTH",
                    "Complete PTH unresponsiveness requiring calcimimetic in all elders",
                    "Primary hyperparathyroidism in every man over 70",
                    "Lower PTH secretion at any calcium level in aging",
                ],
                0,
                "Aging shifts the PTH–calcium curve rightward: PTH higher at any ionized calcium and less suppressible by calcium infusion.",
                ref(
                    "Parathyroid Hormone in Aging",
                    "These results suggested that aging alters the steady-state relationship between calcium and PTH, such that at any concentration of ionized calcium the PTH level is increased, with the PTH curve shifted to the right (Fig. 26.17).",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Which Older Men Should Be Treated With Testosterone?",
                "A 67-year-old with fatigue and low mood but normal morning total testosterone on two fasting LC-MS/MS measurements. Next step?",
                [
                    "Do not start testosterone—symptoms are nonspecific; biochemistry not unequivocally low",
                    "Start testosterone immediately for age-related decline",
                    "Treat because chronologic age is an approved indication",
                    "Measure testosterone only in the evening to confirm deficiency",
                ],
                0,
                "Guidelines advise against treating asymptomatic men or those without unequivocally low morning testosterone on two occasions; many symptoms are nonspecific.",
                ref(
                    "Which Older Men Should Be Treated With Testosterone?",
                    "The current recommendation $ ^{191} $ is not to treat asymptomatic older men with age-related decline in testosterone levels.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Which Older Men Should Be Treated With Testosterone?",
                "Establishing biochemical hypogonadism in an older man requires:",
                [
                    "Morning fasting total testosterone unequivocally low on two separate days (preferably LC-MS/MS)",
                    "Single afternoon saliva testosterone below reference",
                    "Total testosterone below age-90 reference regardless of symptoms",
                    "LH elevation alone without testosterone measurement",
                ],
                0,
                "Morning fasting testosterone measured twice with verified LC-MS/MS assay establishes the biochemical diagnosis.",
                ref(
                    "Which Older Men Should Be Treated With Testosterone?",
                    "Testosterone should be measured in the morning, under fasting conditions (to avoid reduction in testosterone levels due to circadian fluctuation and prandial suppression), and should be unequivocally low on two separate days to establish the biochemical part of the diagnosis of androgen deficiency.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Somatotropic Axis in Aging",
                "Octogenarians retain pituitary responsiveness to GHRH/peptides but often fail to reach youthful GH levels. Contributing mechanism?",
                [
                    "Increased somatostatin tone partially reversible with arginine",
                    "Complete somatotroph apoptosis by age 60",
                    "GH receptor resistance abolishing all IGF1 response",
                    "Irreversible pituitary fibrosis preventing any GH release",
                ],
                0,
                "Attenuated GH response to GHRH reverses with arginine (somatostatin inhibition), implicating increased somatostatin tone with aging.",
                ref(
                    "Somatotropic Axis in Aging",
                    "The attenuated response of GH to GHRH was reversed with coadministration of arginine, a somatostatin inhibitor, suggesting that increased somatostatin tone with age may also contribute to a reduction in GH production.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "DHEA Replacement Therapy",
                "A 65-year-old man with low DHEAS asks if oral DHEA will improve his lumbar spine BMD. Evidence in older men?",
                [
                    "Pooled RCTs and meta-analyses show no improvement in lumbar or femoral BMD",
                    "DHEA doubles BMD equivalently to zoledronate in all men",
                    "Only intravaginal DHEA affects male bone density",
                    "DHEA is first-line male osteoporosis therapy",
                ],
                0,
                "Unlike postmenopausal women, older men show no BMD improvement after DHEA in pooled RCT/meta-analysis data.",
                ref(
                    "DHEA Replacement Therapy",
                    "In older men, a pooled analysis of four RCTs involving 290 men and a meta-analysis of eight RCTs involving 640 men found no improvement in lumbar or femoral BMD or markers of bone turnover after DHEA administration for 1 year.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                "In Snyder's 36-month RCT of testosterone patches in men >65, lean mass increased but:",
                [
                    "Muscle strength and physical function did not differ significantly from placebo",
                    "Grip strength doubled in the testosterone group",
                    "Placebo group lost 5 kg lean mass uniformly",
                    "Walking speed improved more than with phosphodiesterase inhibitors",
                ],
                0,
                "Testosterone increased lean mass and decreased fat mass vs placebo, but strength and physical function endpoints were not significantly different.",
                ref(
                    "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                    "However, changes in parameters of muscle strength and physical function were not significantly different between the groups.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Adrenal Axis in Aging",
                "A meta-analysis of 45 cross-sectional HPA studies (>1200 subjects) found age associated with:",
                [
                    "Higher cortisol response to stimulation and/or reduced suppression—greater in women",
                    "Lower cortisol responses in all elders regardless of sex",
                    "No change in HPA axis activity with aging",
                    "Complete ACTH unresponsiveness after age 60",
                ],
                0,
                "Meta-analysis supports age-related HPA hyperactivity (enhanced stimulation response/reduced suppression), with stronger association in women.",
                ref(
                    "Adrenal Axis in Aging",
                    "A meta-analysis of 45 cross-sectional studies, which included more than 1200 young and older nonhospitalized subjects, reported that age was associated with higher cortisol levels in response to challenges, defined as either stronger response to physiologic or pharmacologic stimulation (including psychosocial stress, insulin-induced hypoglycemia, CRH, ACTH, or opioid antagonists, among others) or reduced inhibition after a suppression test with agents such as dexamethasone or prednisolone.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "KEY POINTS",
                "A clinic advertises melatonin and GH as proven antiaging hormones. Williams KEY POINTS teaching point?",
                [
                    "Manipulating endocrine function to reverse aging has no current clinical role",
                    "All elders should receive GH and melatonin nightly",
                    "Hormone antiaging products are FDA-approved and fully evidence-based",
                    "Endocrine aging changes are fully understood and uniformly pathologic",
                ],
                0,
                "KEY POINTS conclude that hormone manipulation to delay/reverse aging remains unexplored for practice—antiaging hormonal intervention is not established.",
                ref(
                    "KEY POINTS",
                    "The possibility of slowing down or reversing aging by manipulating endocrine function remains to be explored, but currently appears to have no place in clinical practice.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "KEY POINTS",
                "Menopause is defined as permanent cessation of menstruation from loss of ovarian follicular function.",
                True,
                "KEY POINTS and Endocrinology of Aging sections define menopause identically.",
                ref(
                    "KEY POINTS",
                    "The most dramatic age-related endocrine change is represented in menopause, defined as the permanent cessation of menstruation resulting from the loss of ovarian follicular function.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Thyroid Axis in Aging",
                "In iodine-sufficient adults without thyroid disease, TSH levels increase with age.",
                True,
                "Large epidemiologic cross-sectional and longitudinal studies in iodine-replete populations demonstrate rising TSH with age.",
                ref(
                    "Thyroid Axis in Aging",
                    "In iodine-sufficient individuals, free of thyroid disease and thyroid antibodies, TSH levels increase with age.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Thyroid Axis in Aging",
                "More than 60% of individuals with subclinical hypothyroidism and TSH <10 mIU/L revert to euthyroid range on repeat testing.",
                True,
                "Single elevated TSH should not trigger treatment because most mild elevations spontaneously normalize.",
                ref(
                    "Thyroid Axis in Aging",
                    "In general, treatment should not be commenced based on a single elevated TSH level, because more than 60% of individuals with subclinical hypothyroidism and TSH values <10 mIU/L will revert to euthyroid range with repeat testing.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Adrenal Axis in Aging",
                "Aging is associated with a phase advance in circadian cortisol secretion.",
                True,
                "Morning cortisol peak and evening nadir occur 1–2 hours earlier in older vs younger individuals.",
                ref(
                    "Adrenal Axis in Aging",
                    "Aging is associated with phase advance in the circadian cortisol secretion such that morning maximum and evening nadir occur 1 to 2 hours earlier in older vs. young individuals.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Dehydroepiandrosterone in Aging",
                "By age 70–80, serum DHEAS concentrations are about 20% of peak in men and 30% in women.",
                True,
                "Adrenal zona reticularis atrophy drives progressive DHEAS decline from third-decade peak.",
                ref(
                    "Dehydroepiandrosterone in Aging",
                    "In healthy individuals, serum concentrations of DHEA and its sulfate are highest in the third decade of life, after which the concentrations of both gradually decrease as a result of atrophy of zona reticularis of the adrenal cortex, $ ^{98} $ so that by age 70 to 80 years, the values are about 20% of peak values in men and 30% of peak values in women $ ^{99} $ (Fig. 26.3).",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Male Gonadal Axis in Aging",
                "Chronologic age alone is an approved indication for testosterone therapy in the United States.",
                False,
                "Chronologic age is explicitly not an approved indication; therapy requires symptoms plus documented hypogonadism.",
                ref(
                    "Male Gonadal Axis in Aging",
                    "Chronologic age is not an approved indication for testosterone therapy.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Somatotropic Axis in Aging",
                "Despite restoring youthful IGF1, GH treatment improves muscle strength and functional capacity in older people.",
                False,
                "GH increases lean mass and decreases fat but does not improve strength or functional capacity in elders.",
                ref(
                    "Somatotropic Axis in Aging",
                    "However, GH treatment does not improve muscle strength and functional capacity in older people, despite restoration of circulating IGF1 concentrations to young adult levels.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Growth Hormone Replacement Therapy in Aging",
                "Use of GH in healthy older individuals as antiaging therapy is expressly forbidden in the United States.",
                True,
                "Chronologic age is not an approved GH indication; antiaging GH in healthy elders is prohibited.",
                ref(
                    "Growth Hormone Replacement Therapy in Aging",
                    "In the United States, chronologic age is not included among approved indications for GH therapy, and use of GH in healthy older individuals as antiaging therapy is expressly forbidden.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                "In TTrials, testosterone therapy significantly improved memory and other cognitive functions in older men.",
                False,
                "Cognitive evaluation at 6 and 12 months showed no testosterone benefit over placebo.",
                ref(
                    "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                    "Cognitive function was longitudinally evaluated at baseline, 6 months, and 12 months in all of the TTrials participants; however, testosterone therapy did not improve memory or other cognitive functions.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Parathyroid Hormone in Aging",
                "PTH levels rise with age independently of ionized calcium, vitamin D, and other common confounders.",
                True,
                "Large cross-sectional studies after exclusions show progressive age-related PTH rise.",
                ref(
                    "Parathyroid Hormone in Aging",
                    "PTH levels rise with age, independently of ionized calcium concentrations, vitamin D levels, or other potential confounders.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "The Endocrinology of Aging",
                "Combined estrogen and progesterone from the WHI was protective against osteoporotic fractures.",
                True,
                "WHI confirmed fracture protection even as systemic HRT risks shifted recommendations away from prevention use.",
                ref(
                    "The Endocrinology of Aging",
                    "However, estrogen and a combination of estrogen-progesterone were found to be protective against osteoporotic fractures.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "DHEA Replacement Therapy",
                "Oral DHEA administration in most RCTs significantly improved insulin sensitivity and glucose tolerance in unselected older adults.",
                False,
                "Most studies in older men and women with low DHEAS did not improve metabolic parameters including insulin sensitivity and glucose tolerance.",
                ref(
                    "DHEA Replacement Therapy",
                    "In most studies, administration of DHEA in older men and women with low serum DHEAS levels did not significantly improve metabolic parameters, including insulin secretion and sensitivity, glucose tolerance, lipid metabolism, $ ^{[112,114,117-119]} $ or body composition.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Somatotropic Axis in Aging",
                "GH-releasing peptides can restore pituitary GH production even in octogenarians.",
                True,
                "Decline is attributed partly to hypothalamic signaling; GH-releasing peptides restore somatotroph GH production in advanced age.",
                ref(
                    "Somatotropic Axis in Aging",
                    "The decline in somatotropic hormones is attributed to alterations in hypothalamic signaling because treatment with GH-releasing peptides restores production of GH by pituitary somatotrophs, even in octogenarians $ ^{237,238} $ (Fig. 26.11).",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Thyroid Axis in Aging",
                "Assertion: Many older adults labeled subclinically hypothyroid have age-appropriate TSH elevations.",
                "Reason: TSH levels decrease with advancing age in iodine-replete populations.",
                2,
                "Assertion true; reason false—TSH increases, not decreases, with age in iodine-sufficient adults without thyroid disease.",
                ref(
                    "Thyroid Axis in Aging",
                    "larger epidemiologic cross-sectional and longitudinal studies in iodine-replete populations have demonstrated that levels of TSH increase with age, $ ^{39-42} $ especially in women.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Thyroid Axis in Aging",
                "Assertion: Levothyroxine should not be started based on a single elevated TSH in older adults.",
                "Reason: More than 60% of individuals with TSH <10 mIU/L will revert to euthyroid on repeat testing.",
                0,
                "Both true and causally linked—spontaneous normalization of mild TSH elevation supports confirmatory testing before treatment.",
                ref(
                    "Thyroid Axis in Aging",
                    "In general, treatment should not be commenced based on a single elevated TSH level, because more than 60% of individuals with subclinical hypothyroidism and TSH values <10 mIU/L will revert to euthyroid range with repeat testing.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Male Gonadal Axis in Aging",
                "Assertion: Obesity can cause secondary hypogonadism in older men.",
                "Reason: Weight loss in overweight men with low testosterone can increase testosterone levels.",
                0,
                "Both true—the causal obesity–hypogonadism link is supported by testosterone rise after weight loss.",
                ref(
                    "Male Gonadal Axis in Aging",
                    "The association of obesity with hypogonadism is almost certainly causal, because in overweight or obese men with low testosterone levels, weight loss leads to increase of testosterone, $ ^{151} $ although the mechanistic underpinnings of this relationship remain unclear.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Male Gonadal Axis in Aging",
                "Assertion: EMAS defines late-onset hypogonadism using sexual symptoms plus low testosterone.",
                "Reason: Low testosterone alone without sexual symptoms carries the same health associations as syndromic LOH.",
                2,
                "Assertion true; reason false—low testosterone without sexual symptoms shows considerably weaker endpoint associations than LOH.",
                ref(
                    "Male Gonadal Axis in Aging",
                    "Men with low testosterone only, irrespective of sexual symptoms, showed considerably lesser magnitude of associations with the same endpoints.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Growth Hormone Replacement Therapy in Aging",
                "Assertion: GH administration in older adults increases lean body mass.",
                "Reason: GH administration in older adults reliably increases muscle strength and functional capacity.",
                2,
                "Assertion true; reason false—lean mass rises but strength and functional capacity do not improve consistently.",
                ref(
                    "Growth Hormone Replacement Therapy in Aging",
                    "Administration of GH in older adults causes an increase in lean body mass and an appreciable loss of fat mass. However, GH treatment does not improve muscle strength and functional capacity in older people, despite restoration of circulating IGF1 concentrations to young adult levels.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Growth Hormone Replacement Therapy in Aging",
                "Assertion: Rudman's landmark GH trial reported favorable body-composition changes in older men.",
                "Reason: The trial demonstrated no rise in blood pressure or fasting glucose during GH treatment.",
                2,
                "Assertion true; reason false—systolic BP rose 8 mm Hg and fasting glucose increased 7.2 mg/dL during treatment.",
                ref(
                    "Growth Hormone Replacement Therapy in Aging",
                    "However, during the treatment period, systolic blood pressure also rose by an average of 8 mm Hg and fasting glucose increased by an average of 7.2 mg/dL, causing some participants to cross into the prediabetes range.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Dehydroepiandrosterone in Aging",
                "Assertion: DHEA is widely marketed as an antiaging dietary supplement in the United States.",
                "Reason: RCTs consistently demonstrate compelling systemic antiaging benefits of oral DHEA in older adults.",
                2,
                "Assertion true; reason false—no convincing evidence supports DHEA for preventing aging consequences and safety is unknown.",
                ref(
                    "Dehydroepiandrosterone in Aging",
                    "DHEA, which is currently available as a dietary supplement, is widely used within the United States as an unapproved preventive treatment against aging. There is no convincing evidence at present to recommend the use of DHEA for delaying or preventing the physiologic consequences of aging, and its safety is unknown.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "The Endocrinology of Aging",
                "Assertion: WHI combined estrogen-progestin increased invasive breast cancer risk.",
                "Reason: WHI found no increase in coronary heart disease or stroke with combined therapy.",
                2,
                "Assertion true; reason false—WHI combined therapy increased CHD, stroke, VTE, and breast cancer vs placebo.",
                ref(
                    "The Endocrinology of Aging",
                    "findings from the landmark Women's Health Initiative (WHI) study led to a paradigm shift after it demonstrated that, compared to placebo, combined estrogen and progesterone replacement increased the risk for invasive breast cancer, coronary heart disease, stroke, venous thromboembolism, $ ^{29} $ and probable dementia.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Adrenal Axis in Aging",
                "Assertion: Greater diurnal decline in cortisol associates with better outcomes in older individuals.",
                "Reason: Flattened diurnal cortisol curves are associated with longer survival in all studies.",
                2,
                "Assertion true; reason false—greater diurnal decline is protective; flattening/high average cortisol links to worse outcomes.",
                ref(
                    "Adrenal Axis in Aging",
                    "In cross-sectional studies conducted later in life, a more dynamic activity of the HPA axis, characterized by a greater diurnal decline, has been associated with better physical performance, $ ^{87-89} $ longer sleep duration and less sleep disturbance, $ ^{79} $ and lower prevalence of osteoporotic fractures $ ^{90} $ and type 2 diabetes (T2D).",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Parathyroid Hormone in Aging",
                "Assertion: PTH rises with age even after excluding renal disease and low vitamin D.",
                "Reason: Age-related PTH elevation has been proven pathologic and requires treatment in all elders.",
                2,
                "Assertion true; reason false—it remains unknown whether age-related PTH rise is pathologic or benign.",
                ref(
                    "Parathyroid Hormone in Aging",
                    "Although the age-related increase in PTH is well documented, it remains unknown whether this rise is a normal manifestation of aging or is pathologic.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Somatotropic Axis in Aging",
                "Assertion: Age-related decline in GH-IGF1 may reflect reduced hypothalamic GHRH drive.",
                "Reason: Pituitary somatotrophs lose all responsiveness to GHRH and GH-stimulating peptides in octogenarians.",
                2,
                "Assertion true; reason false—GH-releasing peptides restore pituitary GH production even in octogenarians.",
                ref(
                    "Somatotropic Axis in Aging",
                    "The decline in somatotropic hormones is attributed to alterations in hypothalamic signaling because treatment with GH-releasing peptides restores production of GH by pituitary somatotrophs, even in octogenarians $ ^{237,238} $ (Fig. 26.11).",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                "Assertion: Testosterone therapy in TTrials improved sexual function in older hypogonadal men.",
                "Reason: Testosterone therapy in TTrials produced greater vitality improvement than placebo on FACIT-Fatigue.",
                2,
                "Assertion true; reason false—vitality (FACIT-Fatigue) did not significantly benefit vs placebo.",
                ref(
                    "Randomized Controlled Trials of Testosterone Replacement Therapy in Older Men",
                    "Further, testosterone treatment showed no significant benefit over placebo with respect to vitality, as determined by an increase of at least 4 points in the FACIT–Fatigue score $ ^{220} $ (Fig. 26.8).",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "26",
        "title": "Endocrine Function and Aging",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Sandra Aleksic, Andrzej Bartke, Steven W. J. Lamberts, and Sofiya Milman",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_26_Endocrine_Function_and_Aging.md",
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
