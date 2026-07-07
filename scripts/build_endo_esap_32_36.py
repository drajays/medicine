#!/usr/bin/env python3
"""Generate remediated ESAP 2021 modules e21-32 through e21-36 (Reproductive batch)."""
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


def build_chapter_32() -> dict:
    p = "e21-32"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Diagnostic paradigm",
                "Why functional hypogonadism is a diagnosis of exclusion",
                "Functional suppression of the HPT axis from acute or chronic illness is common, but organic agonadism from structural pituitary or testicular disease must be excluded before attributing symptoms to reversible functional hypogonadism.",
                ref(
                    "Main Conclusions",
                    "Functional hypogonadism is diagnosis of exclusion and requires careful, individualized assessment to exclude organic agonadism due to anatomic pathology of the axis.",
                ),
            ),
            note(
                f"{p}-n2",
                "Organic vs functional",
                "How to distinguish organic from functional hypogonadism clinically",
                "Organic disease shows more specific signs (small testes, gynecomastia, loss of body hair) with unequivocally low testosterone and abnormal gonadotropins; functional hypogonadism has nonspecific symptoms, borderline testosterone, and usually normal gonadotropins from nondestructive hypothalamic-pituitary inhibition.",
                ref(
                    "Significance of the Clinical Problem",
                    "Most such men do not have organic hypogonadism due to classic pituitary or testicular disease, but instead have functional hypogonadism.",
                ),
            ),
            note(
                f"{p}-n3",
                "Treatment approach",
                "Why treatment differs between organic and functional hypogonadism",
                "Organic hypogonadism generally requires testosterone replacement; in functional hypogonadism, lifestyle measures—achieving healthy body weight, optimizing comorbidities, and stopping offending medications—may improve symptoms and raise serum testosterone.",
                ref(
                    "Significance of the Clinical Problem",
                    "While organic hypogonadism is generally treated with testosterone replacement, in men with functional hypogonadism, lifestyle measures—especially achieving a healthy body weight, optimizing comorbidities, and stopping offending medications—may improve symptoms and increase serum testosterone.",
                ),
            ),
            note(
                f"{p}-n4",
                "Workup staging",
                "How to work up older men with androgen deficiency features",
                "Confirm clinically significant androgen deficiency, document at least two morning fasted low total testosterone values (avoid intercurrent illness), measure SHBG/free testosterone when borderline, and individualize pituitary evaluation—prolactin and iron studies in men <65; consider imaging when testosterone <150 ng/dL with low-normal gonadotropins.",
                ref(
                    "Workup of Older Men Presenting With Features Suggestive of Androgen Deficiency",
                    "The clinical impression of androgen deficiency should be confirmed by documenting at least 2 low serum total testosterone concentrations by an accurate and reliable assay, with the sample drawn in the morning in the fasted state.",
                ),
            ),
            note(
                f"{p}-n5",
                "Pituitary imaging",
                "Pituitary imaging threshold in secondary hypogonadism",
                "In men with low to normal gonadotropins, consider pituitary imaging when total testosterone is persistently <150 ng/dL (<5.2 nmol/L), even without clinical suspicion of pituitary disease.",
                ref(
                    "Workup of Older Men Presenting With Features Suggestive of Androgen Deficiency",
                    "imaging should be considered in men with a total testosterone concentration less than 150 ng/dL (<5.2 nmol/L) and low to normal gonadotropins, even in the absence of clinical suspicion of hypothalamic pituitary disease.",
                ),
            ),
            note(
                f"{p}-n6",
                "Missed organic disease",
                "Why reevaluate for organic HPT pathology when optimization fails",
                "Features consistent with androgen deficiency may persist despite weight loss and comorbidity optimization; organic pathology can be missed on initial assessment.",
                ref(
                    "Barriers to Optimal Practice",
                    "In some men, clinical and biochemical features consistent with androgen deficiency may persist despite optimization of body weight and comorbidities. In such men, reevaluation for organic HPT axis pathology should be considered, as this can be missed.",
                ),
            ),
            note(
                f"{p}-n7",
                "T-Trials",
                "How testosterone treatment performed in the T-Trials",
                "The T-Trials enrolled men ≥65 years with baseline testosterone <275 ng/dL and hypogonadal symptoms, excluding organic hypogonadism; transdermal testosterone for 12 months modestly improved sexual function, mood, bone density, and anemia but not cognition.",
                ref(
                    "The Benefits of Testosterone Therapy",
                    "Eligible participants had a baseline testosterone concentration less than 275 ng/dL (<9.54 nmol/L) (averaged from 2 measures) and at least 1 symptom or sign consistent with hypogonadism",
                ),
            ),
            note(
                f"{p}-n8",
                "Targeted therapy",
                "How to address specific deficits without testosterone",
                "Men with functional hypogonadism can respond to targeted treatments—phosphodiesterase-5 inhibitors for erectile dysfunction or antiresorptive therapy for osteoporosis—rather than reflex testosterone prescription.",
                ref(
                    "Main Conclusions",
                    "However, such men can respond to targeted treatments addressing relevant symptoms (eg, phosphodiesterase-5 inhibitors for sexual dysfunction) or end-organ deficits (eg, antiresorptive therapy for osteoporosis).",
                ),
            ),
            note(
                f"{p}-n9",
                "RED-S",
                "Why relative energy deficit in sport causes hypogonadotropic hypogonadism",
                "Excessive exercise with dietary restriction creates relative energy deficit suppressing GnRH pulsatility; elevated SHBG, sick euthyroid pattern, and mild anemia support RED-S over pituitary adenoma in the athletic young man.",
                ref(
                    "Case 3",
                    "The International Olympic Committee has introduced the gender-neutral term relative energy deficiency in sport (RED-S) (Answer A), replacing the term \"female athlete triad\" to recognize that functional hypogonadotropic hypogonadism due to overtraining leading to a relative energy deficit may also occur in men.",
                ),
            ),
            note(
                f"{p}-n10",
                "RED-S management",
                "How to treat relative energy deficit in sport",
                "Correct the energy deficit by increasing caloric intake and reducing training intensity; gonadal axis recovery usually follows within weeks to months if successful.",
                ref(
                    "Case 3",
                    "Treatment of RED-S consists of correcting the underlying energy deficit by increasing caloric intake and reducing training intensity (Answer B).",
                ),
            ),
            note(
                f"{p}-n11",
                "Cirrhosis trap",
                "Why severe illness masks primary hypogonadism before liver transplant",
                "Decompensated cirrhosis commonly causes functional hypogonadotropic hypogonadism with low testosterone and low-normal gonadotropins; after transplant recovery, underlying primary testicular failure (e.g., prior orchitis) may unmask with elevated gonadotropins.",
                ref(
                    "Case 4",
                    "The best explanation for these findings is poor health before transplant (Answer B). This most likely led to hypothalamic-pituitary suppression causing functional central hypogonadism superimposed on, and hence masking, his underlying genuine primary hypogonadism due to previous alcohol and orchitis.",
                ),
            ),
            note(
                f"{p}-n12",
                "Off-label pitfall",
                "Pitfall: aromatase inhibitors and SERMs for functional hypogonadism",
                "Aromatase inhibitors and selective estrogen-receptor modulators are sometimes prescribed off-label to raise testosterone but lack convincing evidence of benefit; aromatase inhibitors may reduce bone density in men.",
                ref(
                    "Case 2",
                    "These agents are not approved for male hypogonadism, and there is no convincing evidence for clinical benefit. Moreover, by decreasing estradiol production, aromatase inhibitors have been reported to reduce bone density in men.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — organic pathology",
                "A 51-year-old man has repeated total testosterone 133–144 ng/dL, mild gynecomastia, 15-mL testes, mild anemia, and failed lifestyle measures. What is the best next step?",
                [
                    "Evaluate for obstructive sleep apnea",
                    "Refer to a dietician for weight loss",
                    "Evaluate for organic HPT axis pathology",
                    "Refer to a psychologist for counseling",
                ],
                2,
                "Frankly low testosterone with gynecomastia and borderline testicular size suggests organic pathology; functional hypogonadism is a diagnosis of exclusion. He was later found to have a 2-cm nonfunctioning pituitary macroadenoma.",
                ref(
                    "Case 1",
                    "Answer: C) Evaluate for organic HPT axis pathology",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — obese older man",
                "A 67-year-old obese man has total testosterone ~200 ng/dL, calculated free testosterone 5.0 ng/dL, and normal LH/FSH/prolactin without gynecomastia. Best next step?",
                [
                    "Pituitary-directed MRI",
                    "Lifestyle measures for weight loss plus phosphodiesterase-5 inhibitor",
                    "Aromatase inhibitor",
                    "Selective estrogen-receptor modulator",
                ],
                1,
                "Low clinical suspicion for organic hypogonadotropic hypogonadism; obesity is the likely driver. Weight loss may raise testosterone; PDE-5 inhibitor addresses erectile dysfunction without unnecessary pituitary imaging or unproven off-label agents.",
                ref(
                    "Case 2",
                    "Answer: B) Initiate lifestyle measures to achieve weight loss and prescribe a phosphodiesterase 5 inhibitor",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3 — cyclist",
                "A 24-year-old cyclist with 4–6 hours daily training, intentional weight loss, testosterone 75–86 ng/dL, LH 0.2, elevated SHBG, and sick euthyroid pattern. Most likely diagnosis?",
                [
                    "Relative energy deficit in sport",
                    "Pituitary adenoma",
                    "Hemochromatosis",
                    "Covert anabolic steroid use",
                ],
                0,
                "Excessive exercise with dietary restriction typifies RED-S; elevated SHBG is a sensitive marker of energy deficit. Steroid abuse would show muscular physique, small testes, low SHBG, and polycythemia.",
                ref(
                    "Case 3",
                    "Answer: A) Relative energy deficit in sport",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 3 — RED-S treatment",
                "The same cyclist with RED-S asks about management. Best next step?",
                [
                    "Initiate testosterone replacement",
                    "Reduce training intensity and restore energy deficit",
                    "Initiate clomiphene",
                    "Initiate an aromatase inhibitor",
                ],
                1,
                "RED-S treatment targets the energy deficit; gonadal recovery usually follows within weeks to months. Testosterone would not address the underlying problem.",
                ref(
                    "Case 3",
                    "Answer: B) Reduce training intensity and restore energy deficit",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 4 — post-transplant",
                "A liver transplant recipient now has very low testosterone with elevated gonadotropins, gynecomastia, and small soft testes after pretransplant functional hypogonadism. Best explanation?",
                [
                    "Covert anabolic steroid use before transplant",
                    "Primary hypogonadism masked by ill health before transplant",
                    "Testicular suppression due to immunosuppressive therapy",
                    "Laboratory error",
                ],
                1,
                "Severe illness suppresses the HPT axis functionally; recovery after transplant unmasked underlying primary testicular failure from prior alcohol and mumps orchitis.",
                ref(
                    "Case 4",
                    "Answer: B) Primary hypogonadism masked by ill health before liver transplant",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Biochemical confirmation",
                "When should morning fasting testosterone be measured in suspected hypogonadism?",
                [
                    "During acute intercurrent illness to capture nadir",
                    "At least twice in the morning fasted state, avoiding intercurrent illness",
                    "Only in the afternoon when SHBG is highest",
                    "Once at any time if symptoms are present",
                ],
                1,
                "Intercurrent illness causes temporary HPT suppression; diagnosis requires at least two reliable morning fasted low values.",
                ref(
                    "Workup of Older Men Presenting With Features Suggestive of Androgen Deficiency",
                    "Testosterone should not be measured during an intercurrent illness, as this can lead to temporary HPT axis suppression.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Gonadotropin pattern",
                "In functional hypogonadism from obesity or chronic disease, gonadotropins are typically:",
                [
                    "Markedly elevated",
                    "Low-normal from nondestructive hypothalamic-pituitary inhibition",
                    "Undetectable with high testosterone",
                    "Elevated with high inhibin B",
                ],
                1,
                "Functional hypogonadism reflects reversible central inhibition; gonadotropins are usually low-normal rather than frankly elevated as in primary testicular failure.",
                ref(
                    "Workup of Older Men Presenting With Features Suggestive of Androgen Deficiency",
                    "Most men with functional hypogonadism have low-normal gonadotropin concentrations due to nondestructive hypothalamic-pituitary inhibition from chronic disease, including being obese or underweight.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "T-Trials eligibility",
                "The T-Trials excluded which population?",
                [
                    "Men with organic hypogonadism",
                    "Men with diabetes mellitus",
                    "Men older than 65 years",
                    "Men with low libido",
                ],
                0,
                "T-Trials studied carefully selected older men with functional/late-onset hypogonadism, excluding organic pituitary or testicular disease.",
                ref(
                    "Table 2. Effects of Testosterone Treatment in Randomized Controlled Trials of Middle-Aged and Older Men: Evidence to Date",
                    "In these randomized controlled trials, men with organic hypogonadism were excluded.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "T-Trials cognition",
                "In the T-Trials, testosterone treatment for 12 months:",
                [
                    "Markedly improved cognitive function",
                    "Did not improve cognitive function",
                    "Worsened mood uniformly",
                    "Eliminated need for PDE-5 inhibitors",
                ],
                1,
                "Testosterone modestly improved sexual function and mood but did not improve cognition or memory.",
                ref(
                    "The Benefits of Testosterone Therapy",
                    "Testosterone treatment resulted in modest benefits in sexual function and slightly improved mood and depressive symptoms, but it did not improve cognitive function.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Long-term risks",
                "Regarding long-term testosterone therapy in functional hypogonadism:",
                [
                    "Definitive RCTs prove mortality benefit",
                    "Effects on fractures, disability, and mortality remain unknown",
                    "Prostate cancer risk is definitively increased",
                    "Cardiovascular benefit is established",
                ],
                1,
                "Existing trials are relatively small and short; long-term effects on major clinical endpoints are not established.",
                ref(
                    "The Benefits of Testosterone Therapy",
                    "Whether testosterone treatment reduces important clinical endpoints such as fractures, disability, or mortality in older men is not known.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Young men",
                "Functional hypogonadism in young men may occur in the context of:",
                [
                    "Only pituitary macroadenoma",
                    "Energy deficit from overtraining, eating disorders, or anabolic steroid recovery",
                    "Only primary testicular failure",
                    "Exclusively after age 40",
                ],
                1,
                "Ill health including energy deficit syndromes and recovery from anabolic steroid use can suppress the HPT axis in young men.",
                ref(
                    "Significance of the Clinical Problem",
                    "Notably, ill health can also cause functional hypogonadism in young men in the context of energy deficit (eg, the reversible energy deficit of sport syndrome, eating disorders, and body dysmorphic disorders) or during recovery from anabolic steroid use.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Prevalence",
                "Estimated community prevalence of functional hypogonadism (late-onset hypogonadism) in older men is approximately:",
                [
                    "20%–30%",
                    "2%–5%",
                    "50%",
                    "<0.1%",
                ],
                1,
                "Functional hypogonadism with symptoms and lowered testosterone without organic pathology affects roughly 2%–5% of community-dwelling men.",
                ref(
                    "The estimated prevalence of functional hypogonadism (in older men also referred late-onset hypogonadism), defined as existence of androgen deficiency-like symptoms and lowered circulating testosterone in absence of organic HPT axis pathology, is estimated to be 2% to 5% in community-dwelling men.",
                    "is estimated to be 2% to 5% in community-dwelling men.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Counseling before testosterone",
                "Before considering testosterone in functional hypogonadism, men should be counseled that:",
                [
                    "Long-term benefits and risks are fully established",
                    "High-level evidence on long-term outcomes is absent and clear goals should be set",
                    "Testosterone always restores fertility",
                    "No monitoring is required",
                ],
                1,
                "Men should understand the evidence gap, identify patient-specific goals, and stop treatment if goals are not met with guideline-conforming monitoring.",
                ref(
                    "Possible Risks of Testosterone Therapy",
                    "If treatment is considered, men with functional hypogonadism should be informed about the absence of high-level evidence regarding long-term benefits and risks.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Diagnosis",
                "Functional hypogonadism can be diagnosed without excluding organic HPT axis pathology.",
                False,
                "It is explicitly a diagnosis of exclusion requiring assessment for structural pituitary or testicular disease.",
                ref(
                    "Main Conclusions",
                    "Functional hypogonadism is diagnosis of exclusion and requires careful, individualized assessment to exclude organic agonadism due to anatomic pathology of the axis.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Lifestyle",
                "Achieving healthy body weight and optimizing comorbidities can increase circulating testosterone in functional hypogonadism.",
                True,
                "Available evidence supports health optimization improving symptoms and modestly raising testosterone.",
                ref(
                    "Main Conclusions",
                    "the available evidence suggests that measures to optimize ill health (eg, achieving a healthy body weight, optimizing comorbidities, managing offending medications) can improve androgen deficiency-like symptoms and lead to modest increase in circulating testosterone.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Intercurrent illness",
                "Testosterone should be measured during acute intercurrent illness to confirm hypogonadism.",
                False,
                "Intercurrent illness causes temporary HPT axis suppression and confounds interpretation.",
                ref(
                    "Workup of Older Men Presenting With Features Suggestive of Androgen Deficiency",
                    "Testosterone should not be measured during an intercurrent illness, as this can lead to temporary HPT axis suppression.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Imaging yield",
                "Pituitary imaging is always mandatory in every obese older man with borderline low testosterone.",
                False,
                "Evaluation for organic pathology should be individualized; probability is inversely related to BMI, age, comorbidities, and testosterone level.",
                ref(
                    "Workup of Older Men Presenting With Features Suggestive of Androgen Deficiency",
                    "Especially in older men, evaluation for underlying organic HPT axis pathology is commonly of low yield and should be individualized.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "T-Trials bone",
                "T-Trials substudies demonstrated improvements in volumetric bone mineral density with testosterone.",
                True,
                "Concomitant substudies showed BMD gains though fracture endpoints were not assessed.",
                ref(
                    "The Benefits of Testosterone Therapy",
                    "Concomitant substudies demonstrated improvements in volumetric bone mineral density and anemia.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Prostate cancer",
                "Clinical studies to date have demonstrated that testosterone treatment increases the risk of developing prostate cancer.",
                False,
                "Despite ADT efficacy in established prostate cancer, studies have not shown testosterone therapy increases incident prostate cancer risk.",
                ref(
                    "Possible Risks of Testosterone Therapy",
                    "clinical studies to date have not demonstrated that testosterone treatment increases the risk of developing prostate cancer.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "RED-S",
                "Relative energy deficit in sport can cause functional hypogonadotropic hypogonadism in men.",
                True,
                "RED-S replaces the female athlete triad concept and applies to male athletes with energy deficit.",
                ref(
                    "Case 3",
                    "functional hypogonadotropic hypogonadism due to overtraining leading to a relative energy deficit may also occur in men.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Aromatase inhibitors",
                "Aromatase inhibitors are approved and evidence-based first-line therapy for male functional hypogonadism.",
                False,
                "They are off-label without convincing benefit and may harm bone density.",
                ref(
                    "Case 2",
                    "These agents are not approved for male hypogonadism, and there is no convincing evidence for clinical benefit.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Diagnosis of exclusion",
                "Assertion: Functional hypogonadism requires exclusion of organic HPT axis pathology.",
                "Reason: Organic hypogonadism is always reversible with weight loss alone.",
                2,
                "Assertion is true; organic disease is generally irreversible—reason is false.",
                ref(
                    "Main Conclusions",
                    "Functional hypogonadism is diagnosis of exclusion and requires careful, individualized assessment to exclude organic agonadism due to anatomic pathology of the axis.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Low testosterone as marker",
                "Assertion: In most older men, low testosterone is a marker of poor health.",
                "Reason: Lowered testosterone is primarily a consequence of functional hypothalamic-pituitary suppression due to ill health.",
                0,
                "Both are true and causally linked in the functional hypogonadism paradigm.",
                ref(
                    "Conclusions",
                    "In most older men, low testosterone is a marker of poor health and should prompt a holistic approach with focus on lifestyle measures and optimization of comorbidities.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Case 1 pituitary",
                "Assertion: A man with frankly low testosterone, gynecomastia, and borderline testicular size should not be labeled functional hypogonadism without further HPT evaluation.",
                "Reason: Visual fields normal to confrontation exclude all pituitary pathology.",
                2,
                "Assertion reflects Case 1 teaching; normal confrontation visual fields do not exclude macroadenoma away from the chiasm.",
                ref(
                    "Case 1",
                    "His clinical presentation should not be attributed to functional hypogonadism, a diagnosis of exclusion. Further evaluation of his HPT axis is indicated (Answer C).",
                ),
            ),
            ar(
                f"{p}-ar4",
                "T-Trials sexual function",
                "Assertion: Testosterone treatment in the T-Trials improved sexual function modestly.",
                "Reason: Effects on libido were generally more marked than effects on erectile function.",
                0,
                "Both are true per trial outcomes and Table 2.",
                ref(
                    "Table 2. Effects of Testosterone Treatment in Randomized Controlled Trials of Middle-Aged and Older Men: Evidence to Date",
                    "In most randomized controlled trials, effect on libido more marked than on erectile function",
                ),
            ),
            ar(
                f"{p}-ar5",
                "RED-S SHBG",
                "Assertion: Elevated SHBG supports relative energy deficit in sport.",
                "Reason: Energy deficit always lowers SHBG concentrations.",
                2,
                "Assertion is true in Case 3; energy deficit raises SHBG—the reason is false.",
                ref(
                    "Case 3",
                    "In the context of hypogonadotropic hypogonadism, biochemical findings pointing to the diagnosis of RED-S in this man are the elevated serum SHBG concentration (a sensitive marker of energy deficit)",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Cirrhosis masking",
                "Assertion: Severe cirrhosis can mask underlying primary hypogonadism.",
                "Reason: Cirrhosis always causes primary testicular failure with elevated gonadotropins.",
                2,
                "Assertion is true (Case 4); cirrhosis typically causes functional central suppression—reason false.",
                ref(
                    "Case 4",
                    "In men with decompensated cirrhosis, low testosterone is common (occurring in 60%-90% of men), and gonadotropins are typically low or low-normal",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Testosterone counseling",
                "Assertion: Men considered for testosterone should be informed about absent high-level long-term outcome evidence.",
                "Reason: Definitive RCTs have proven testosterone reduces mortality in functional hypogonadism.",
                3,
                "Assertion is true; mortality benefit is not established—the reason is false.",
                ref(
                    "Possible Risks of Testosterone Therapy",
                    "men with functional hypogonadism should be informed about the absence of high-level evidence regarding long-term benefits and risks.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "PDE-5 inhibitors",
                "Assertion: Phosphodiesterase-5 inhibitors are a targeted option for erectile dysfunction in functional hypogonadism.",
                "Reason: Erectile dysfunction in obese older men never responds to PDE-5 inhibitors.",
                2,
                "Assertion is true (Case 2); PDE-5 inhibitors can improve erectile function—the blanket reason is false.",
                ref(
                    "Case 2",
                    "His erectile function should improve with the use of a phosphodiesterase 5 inhibitor.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "32",
        "title": "Diagnosis and Management of Functional Hypogonadism in the Male Patient",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Mathis Grossmann, MD, PhD, FRACP",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_32_Diagnosis_and_Management_of_Functional_Hypogonadism_in_the_Male_Patient.md",
        "items": items,
    }


def build_chapter_33() -> dict:
    p = "e21-33"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Couple evaluation",
                "Why infertility evaluation begins with the woman",
                "Women with normal fecundity usually conceive even with subnormal male reproductive function; restoring ovulation in anovulatory young women often enables conception for the couple.",
                ref(
                    "Main Conclusions",
                    "Young women who are ovulating will generally conceive with a subfertile male—restoration of ovulation in young women who are infertile will often result in conception for a couple.",
                ),
            ),
            note(
                f"{p}-n2",
                "Timing of evaluation",
                "How to time infertility evaluation by age",
                "Begin evaluation after 1 year of active attempts with regular cycles (12 ovulatory, exposed cycles); women older than 35 years should be evaluated after 6 months.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management Initial Evaluation of the Infertile Couple",
                    "Women older than 35 years should be evaluated for infertility after 6 months of unsuccessful active attempts.",
                ),
            ),
            note(
                f"{p}-n3",
                "AMH limitations",
                "Why AMH is not a fertility marker",
                "Two large studies found no correlation between AMH and fecundability; AMH predicts ovarian stimulation response (quantity) but not pregnancy (quality).",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "However, 2 large studies have not shown a correlation between AMH and fecundability. Thus, it is clear that AMH is not a \"fertility marker.\"",
                ),
            ),
            note(
                f"{p}-n4",
                "Oral contraceptives",
                "How oral contraceptives affect AMH interpretation",
                "AMH may be lowered by up to 50% with OCP use; continuous OCP use can suppress antral follicle growth—stop pills and repeat testing in 2–3 months before major decisions.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "AMH is lowered with the use of oral contraceptive pills, by as much as 50%, and thus may not be reflective of true ovarian reserve.",
                ),
            ),
            note(
                f"{p}-n5",
                "Ovulation history",
                "Menstrual clues to declining ovarian reserve",
                "Regular predictable cycles usually indicate ovulation (>98%), but shortening cycle interval or new precycle spotting may signal declining reserve or luteal-phase progesterone deficiency.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "Important questions include changes in cycle interval (a shortening of the intermenstrual interval may suggest a decline in ovarian reserve).",
                ),
            ),
            note(
                f"{p}-n6",
                "PCOS first-line",
                "How to treat anovulation in PCOS",
                "Weight reduction is first-line; if ovulation fails or the woman is older, letrozole is the most effective first-line ovulation-induction agent per randomized trials (~85% conceive with medical therapy).",
                ref(
                    "Main Conclusions",
                    "Women with polycystic ovary syndrome (PCOS) are best treated with weight reduction; if this fails to induce ovulation and/or the women is older, ovulation induction with letrozole is indicated.",
                ),
            ),
            note(
                f"{p}-n7",
                "Hypogonadotropic hypogonadism",
                "Why pulsatile GnRH is ideal for functional hypothalamic amenorrhea",
                "After treating thyroid disease or hyperprolactinemia, pulsatile GnRH most closely restores physiology with lower multiple-pregnancy risk than exogenous gonadotropins (though unavailable in the US).",
                ref(
                    "Main Conclusions",
                    "For women with functional hypothalamic amenorrhea, ovulation induction with pulsatile GnRH is the most effective and physiological.",
                ),
            ),
            note(
                f"{p}-n8",
                "Young low AMH",
                "Why low AMH in young ovulatory women does not imply infertility",
                "Decreased ovarian reserve in young women who are ovulating is not implicated in infertility or lowered fecundity; management differs from older women with diminished reserve.",
                ref(
                    "Main Conclusions",
                    "Decreased ovarian reserve in young women is not implicated in infertility and/or lowered fecundity.",
                ),
            ),
            note(
                f"{p}-n9",
                "Older women",
                "How to manage older women with diminished ovarian reserve",
                "They have a shortened timeline and often need assisted reproductive technology after a brief course of medical therapy and/or intrauterine insemination.",
                ref(
                    "Main Conclusions",
                    "Older women, especially those with diminished ovarian reserve, may have a shortened timeline for conception and should be managed more aggressively.",
                ),
            ),
            note(
                f"{p}-n10",
                "Male partner",
                "When to evaluate the male partner in infertility",
                "Both partners should be evaluated; healthy young men are >90% likely to have sperm, so focus on treating female anovulation when PCOS is obvious—but men with risk factors or hypogonadal signs need semen analysis.",
                ref(
                    "Case 3",
                    "Healthy young men are more than 90% likely to have a sperm in the ejaculate. Thus, the focus should be treatment of her chronic anovulation and not assessment of the man.",
                ),
            ),
            note(
                f"{p}-n11",
                "Unexplained infertility",
                "How to manage unexplained infertility with low AMH at age 32",
                "Low AMH may shorten the reproductive window but does not reduce current conception chance; initial treatment is clomiphene citrate with intrauterine insemination rather than immediate IVF or gonadotropins.",
                ref(
                    "Case 6",
                    "Given her young age, she should be treated as having \"unexplained infertility.\" The initial treatment of unexplained infertility is ovarian stimulation with clomiphene citrate and intrauterine insemination (Answer B).",
                ),
            ),
            note(
                f"{p}-n12",
                "Diminished reserve workup",
                "Distinguishing hypogonadotropic hypogonadism from diminished ovarian reserve",
                "Low AMH with low estradiol and low FSH suggests central amenorrhea; low AMH with elevated FSH and intact pituitary feedback indicates diminished ovarian reserve (not POI if still cycling).",
                ref(
                    "Case 5",
                    "This patient clearly has diminished ovarian reserve with low AMH and elevated (although not menopausal) FSH.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — Hashimoto",
                "A 28-year-old woman with Hashimoto disease on continuous OCPs asks about future fertility. Best course?",
                [
                    "Stop OCPs and attempt conception now",
                    "Measure serum AMH",
                    "Refer immediately for egg freezing",
                    "Reassure that young age guarantees future fertility",
                ],
                1,
                "Her autoimmune history and concern warrant ovarian reserve testing; conception should not be suggested until she is ready, and age alone is insufficient reassurance.",
                ref(
                    "Case 1",
                    "Answer: B) Measure serum AMH",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — low AMH on OCP",
                "AMH is 0.5 ng/mL on continuous OCPs. Best next step?",
                [
                    "Stop OCPs and repeat testing in 2–3 months",
                    "Refer immediately for egg freezing",
                    "Counsel regarding imminent menopause",
                    "Advise low chances for conception",
                ],
                0,
                "OCPs suppress AMH; stop and repeat before counseling on menopause risk or conception prognosis—AMH does not predict spontaneous fecundability.",
                ref(
                    "Case 1 (Continued)",
                    "Answer: A) Suggest she stop oral contraceptive pills and repeat the testing",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — subfertile male",
                "A young woman has AMH 0.5 ng/mL and AFC 5; male partner has low sperm count. Best course?",
                [
                    "Advise them to keep trying without intervention",
                    "Controlled ovarian stimulation (e.g., clomiphene) with IUI",
                    "Immediate in vitro fertilization",
                    "Egg freezing only",
                ],
                1,
                "At young age, controlled ovarian stimulation with IUI can shorten time to pregnancy; AMH does not mandate IVF and egg freezing may not be necessary.",
                ref(
                    "Case 2 (Continued)",
                    "Answer: B) Recommend controlled ovarian stimulation",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 3 — PCOS",
                "A 32-year-old woman with oligomenorrhea, hirsutism, and 9 months infertility. Best management?",
                [
                    "Increase intercourse to 4 times weekly only",
                    "Measure AMH only",
                    "Measure AMH and semen analysis",
                    "Start letrozole trial",
                ],
                3,
                "Chronic oligoanovulation with PCOS features warrants ovulation induction with letrozole rather than further delay or male testing as first priority.",
                ref(
                    "Case 3",
                    "Answer: D) Start a trial of letrozole for the woman",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 4 — amenorrhea",
                "A thin former athlete has amenorrhea 5 months after stopping OCPs: FSH 1.5, estradiol 10, AMH 0.01. Diagnosis?",
                [
                    "Primary ovarian insufficiency",
                    "PCOS",
                    "Hypogonadotropic hypogonadism",
                    "Postpill amenorrhea only",
                ],
                2,
                "Low gonadotropins with low estradiol indicate central cause; 5 months off OCPs is too long for simple postpill suppression; PCOS patients are not hypoestrogenic.",
                ref(
                    "Case 4",
                    "Answer: C) Hypogonadotropic hypogonadism",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Case 4 — treatment",
                "Best fertility treatment for functional hypogonadotropic hypogonadism?",
                [
                    "Pulsatile GnRH therapy",
                    "Letrozole",
                    "Recombinant FSH and hCG",
                    "Ovarian biopsy and IVF",
                ],
                0,
                "Pulsatile GnRH replaces the missing hypothalamic signal physiologically; aromatase inhibitors/clomiphene fail when estradiol is already very low.",
                ref(
                    "Case 4 (Continued)",
                    "Answer: A) Pulsatile GnRH therapy",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Case 5 — same-sex couple",
                "A 33-year-old with irregular cycles, FSH 15, estradiol 10, AMH 0.01. Most likely diagnosis?",
                [
                    "Primary ovarian insufficiency",
                    "PCOS",
                    "Hypogonadotropic hypogonadism",
                    "Diminished ovarian reserve",
                ],
                3,
                "Elevated FSH with low estradiol and low AMH while still cycling indicates diminished reserve, not central hypogonadism or PCOS.",
                ref(
                    "Case 5",
                    "Answer: D) Diminished ovarian reserve",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Case 5 — shared conception",
                "Best next step for severely diminished ovarian reserve in a same-sex couple?",
                [
                    "Clomiphene citrate alone",
                    "Evaluate partner's ovarian reserve for shared conception",
                    "Recombinant FSH and hCG",
                    "Ovarian biopsy followed by IVF",
                ],
                1,
                "Partner with higher reserve as gamete donor and interested partner as gestational carrier offers highest success; IVF does not fix limited oocyte pool.",
                ref(
                    "Case 5 (Continued)",
                    "Answer: B) Evaluate her partner's ovarian reserve",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Case 6 — unexplained infertility",
                "32-year-old with regular cycles, AMH 0.9, patent tubes, normal semen, 1 year infertility. Best management?",
                [
                    "Keep trying with more intercourse only",
                    "Clomiphene citrate with intrauterine insemination",
                    "Exogenous gonadotropins with IUI",
                    "Immediate in vitro fertilization",
                ],
                1,
                "Unexplained infertility with low but not prohibitive AMH: clomiphene plus IUI is appropriate first intervention at her age.",
                ref(
                    "Case 6",
                    "Answer: B) Start clomiphene citrate and proceed with intrauterine insemination",
                ),
            ),
            mcq(
                f"{p}-q10",
                "AMH and IVF",
                "AMH primarily predicts:",
                [
                    "Natural fecundability in the general population",
                    "Ovarian response to stimulation, not pregnancy per se",
                    "Embryo aneuploidy rate directly",
                    "Menopausal age with certainty",
                ],
                1,
                "AMH reflects follicle quantity and stimulation response; large studies show no fecundability correlation.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "AMH is a predictor of response to stimulation (in vitro fertilization cycle), but it does not correlate with pregnancy.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Infertility definition",
                "In the United States, infertility is typically defined as failure to conceive after:",
                [
                    "6 months of attempts",
                    "1 year of active attempts",
                    "2 years regardless of age",
                    "3 months if AMH is low",
                ],
                1,
                "Standard definition is 12 months, with earlier evaluation after 6 months if age >35.",
                ref(
                    "Significance of the Clinical Problem",
                    "In the United States, infertility is typically defined as the inability to conceive after 1 year, at which time an evaluation should begin.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Male factor prevalence",
                "In infertile couples, male factor contributes:",
                [
                    "Never—infertility is solely female",
                    "In ~35% with both partners affected plus 10%–20% male-only",
                    "Only after female workup is complete",
                    "Exclusively in men over 50",
                ],
                1,
                "Male and combined factors are common; both partners should be evaluated.",
                ref(
                    "Significance of the Clinical Problem",
                    "about 35% of couples have both a male and female etiology of their infertility with another 10% to 20% having a sole male factor as the identifiable cause.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Letrozole in PCOS",
                "First-line ovulation induction for PCOS per RCT evidence is:",
                [
                    "Metformin alone",
                    "Clomiphene citrate",
                    "Letrozole",
                    "Immediate IVF",
                ],
                2,
                "Randomized trials identify letrozole as most effective first-line for PCOS ovulation induction.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "Randomized controlled trials have identified letrozole as most effective first-line treatment.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "AMH fecundability",
                "AMH concentration correlates with natural fecundability in large prospective studies.",
                False,
                "Two large studies found no AMH–fecundability correlation.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "2 large studies have not shown a correlation between AMH and fecundability.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "OCP effect",
                "Oral contraceptive pills can lower AMH by as much as 50%.",
                True,
                "OCP suppression of antral follicles can markedly reduce measured AMH.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "AMH is lowered with the use of oral contraceptive pills, by as much as 50%",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Regular cycles",
                "Regular, cyclic, predictable menses are associated with ovulation in greater than 98% of cases.",
                True,
                "Predictable cycles strongly predict ovulation though cycle interval changes still warrant attention.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "A history of regular, cyclic, predictable periods is associated with ovulation in greater than 98% of cases.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Young low AMH",
                "Low AMH in a young ovulating woman automatically indicates current infertility.",
                False,
                "Decreased reserve in young ovulatory women is not implicated in lowered fecundity.",
                ref(
                    "Main Conclusions",
                    "Decreased ovarian reserve in young women is not implicated in infertility and/or lowered fecundity.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "PCOS conception",
                "About 85% of women with PCOS conceive with ovulation-induction drugs.",
                True,
                "Medical ovulation induction is highly effective in PCOS.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "About 85% of women with PCOS conceive with these drugs.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Gonadotropin risk",
                "Exogenous gonadotropins carry higher multiple-pregnancy and OHSS risk than pulsatile GnRH in hypothalamic amenorrhea.",
                True,
                "Direct ovarian stimulation bypasses physiological feedback.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "Gonadotropin therapy is effective, but it is much more likely than GnRH therapy to be complicated by a high risk of multiple pregnancy and ovarian hyperstimulation",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Evaluation timing",
                "Women older than 35 should begin infertility evaluation after 6 months of unsuccessful attempts.",
                True,
                "Earlier evaluation is recommended due to shortened reproductive window.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management Initial Evaluation of the Infertile Couple",
                    "Women older than 35 years should be evaluated for infertility after 6 months of unsuccessful active attempts.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Postpill amenorrhea",
                "Amenorrhea 5 months after stopping OCPs with very low FSH and estradiol is typical postpill amenorrhea alone.",
                False,
                "Prolonged suppression with hypogonadotropic pattern suggests central hypogonadism, not simple postpill recovery delay.",
                ref(
                    "Case 4",
                    "this suppression would not persist for 5 months after stopping the pills and to this extent.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "AMH role",
                "Assertion: AMH is a marker of ovarian follicle quantity.",
                "Reason: AMH directly measures oocyte genetic quality and pregnancy rate.",
                2,
                "Assertion true; AMH reflects pool size not quality—reason false.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "This suggests AMH is a marker of \"quantity\" but not \"quality\" of the oocytes.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Woman-first evaluation",
                "Assertion: Infertility evaluation should begin with the woman.",
                "Reason: Male factor never contributes to couple infertility.",
                2,
                "Assertion true per primacy of female evaluation; male factor is common—reason false.",
                ref(
                    "Main Conclusions",
                    "Primacy of the evaluation and management of the woman.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Letrozole PCOS",
                "Assertion: Letrozole is first-line ovulation induction for PCOS when weight loss fails or patient is older.",
                "Reason: Letrozole permanently destroys ovarian follicles.",
                2,
                "Assertion true; letrozole briefly blocks estrogen feedback—reason false.",
                ref(
                    "Main Conclusions",
                    "ovulation induction with letrozole is indicated.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "OCP and AMH",
                "Assertion: AMH measured on continuous OCPs may underestimate true ovarian reserve.",
                "Reason: OCPs increase AMH by stimulating antral follicle growth.",
                2,
                "Assertion true; OCPs lower AMH—reason false.",
                ref(
                    "Case 1 (Continued)",
                    "Oral contraceptive pills, especially when given in a continuous fashion, can suppress antral follicle growth and AMH levels.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Hypogonadotropic pattern",
                "Assertion: Low FSH with low estradiol suggests hypogonadotropic hypogonadism.",
                "Reason: PCOS always presents with low estradiol and low AMH.",
                2,
                "Assertion true; PCOS patients are hypoestrogenic only in rare contexts—reason false.",
                ref(
                    "Case 4",
                    "the FSH level is also low in the face of a low estradiol. This combination of findings suggests a central cause of amenorrhea",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Unexplained infertility",
                "Assertion: Low AMH at age 32 does not eliminate current conception chances in unexplained infertility.",
                "Reason: Low AMH always requires immediate IVF.",
                2,
                "Assertion true per Case 6; IVF is not mandatory—reason false.",
                ref(
                    "Case 6",
                    "her chances for pregnancy at this time are not impacted by the low reserve.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Pulsatile GnRH",
                "Assertion: Pulsatile GnRH is the most physiological treatment for functional hypothalamic amenorrhea.",
                "Reason: Pulsatile GnRH is widely available in the United States.",
                2,
                "Assertion true; agent is under FDA review and not available in US—reason false.",
                ref(
                    "Approach to the Subfertile/Infertile Woman",
                    "This agent is not available in the United States, but it is under FDA review.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Older diminished reserve",
                "Assertion: Older women with diminished ovarian reserve need more aggressive management.",
                "Reason: AMH in older women reliably predicts they cannot conceive without donor oocytes.",
                2,
                "Assertion true; AMH does not individually preclude conception—reason overstates.",
                ref(
                    "Main Conclusions",
                    "Older women, especially those with diminished ovarian reserve, may have a shortened timeline for conception and should be managed more aggressively.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "33",
        "title": "Antimullerian Hormone and Ovarian Reserve Testing",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Marcelle I. Cedars, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_33_Antimullerian_Hormone_and_Ovarian_Reserve_Testing.md",
        "items": items,
    }


def build_chapter_34() -> dict:
    p = "e21-34"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Menopause definition",
                "Why menopause is defined retrospectively after 12 months of amenorrhea",
                "Menopause reflects permanent cessation of menses from follicular depletion; the diagnosis requires 12 consecutive months without menstruation by convention.",
                ref(
                    "Main Conclusions",
                    "Menopause is defined as the permanent cessation of menses; by convention, the diagnosis of menopause is not made until the individual has had 12 months of amenorrhea.",
                ),
            ),
            note(
                f"{p}-n2",
                "Menopausal transition",
                "How the menopausal transition presents hormonally",
                "The transition is heralded by ovarian reserve depletion, cycle-length changes, reduced luteal progesterone, variable estradiol, and elevated FSH—often causing vasomotor symptoms before the final menstrual period.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The menopausal transition is heralded by ovarian follicular pool depletion (ovarian reserve), menstrual cycle length changes, reduced luteal phase progesterone synthesis, variable estradiol levels, and elevated FSH.",
                ),
            ),
            note(
                f"{p}-n3",
                "Vasomotor symptoms",
                "Why vasomotor symptoms occur in menopause",
                "Hormonal fluctuations lower the hypothalamic threshold for heat dissipation (flushing) and raise the threshold for warming; KNDy neurons adjacent to the thermoregulatory center are hypothesized drivers.",
                ref(
                    "Menopausal Symptoms",
                    "Thermoregulatory dysfunction begins in hypothalamus in response to hormonal fluctuations. The threshold in core temperature for cooling (flushes, sweats) is lowered",
                ),
            ),
            note(
                f"{p}-n4",
                "VMS duration",
                "How long vasomotor symptoms typically persist",
                "Median duration is 7.4 years with mean post-FMP persistence of 4.5 years; duration varies by race, BMI, socioeconomic status, and depression.",
                ref(
                    "Menopausal Symptoms",
                    "Vasomotor symptoms have a median duration of 7.4 years, with a mean post-final menstrual period persistence of 4.5 years.",
                ),
            ),
            note(
                f"{p}-n5",
                "GSM",
                "Why genitourinary syndrome of menopause needs long-term therapy",
                "Unlike vasomotor symptoms, genitourinary syndrome symptoms do not spontaneously resolve and may require ongoing treatment to preserve quality of life.",
                ref(
                    "Menopausal Symptoms",
                    "Unlike vasomotor symptoms, symptoms of genitourinary syndrome of menopause do not spontaneously resolve over time. Therefore, long-term treatment may be required to preserve quality of life.",
                ),
            ),
            note(
                f"{p}-n6",
                "HT efficacy",
                "How effective hormone therapy is for menopausal symptoms",
                "When used in the appropriate population, HT is highly effective for vasomotor symptoms, sleep disruption, mood, and genitourinary syndrome.",
                ref(
                    "Main Conclusions",
                    "When used in the appropriate patient population, hormone replacement therapy (HT) is highly effective and safe.",
                ),
            ),
            note(
                f"{p}-n7",
                "Progestin indication",
                "Why progestin is required with estrogen in women with a uterus",
                "Chronic unopposed estrogen increases endometrial hyperplasia and cancer risk; progestin prevents estradiol-induced endometrial neoplasia.",
                ref(
                    "Uterine Neoplasia",
                    "The incidence of uterine neoplasia is increased under conditions of chronic unopposed estrogen exposure in a woman with an intact uterus.",
                ),
            ),
            note(
                f"{p}-n8",
                "Transdermal route",
                "How route of administration affects thrombotic risk",
                "Transdermal preparations may carry lower venous thromboembolism risk than oral estrogen while providing equivalent symptomatic efficacy.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Transdermal preparations may carry lower risk of thromboembolic events while providing the same efficacy for treatment management.",
                ),
            ),
            note(
                f"{p}-n9",
                "Timing hypothesis",
                "Why timing of HT initiation affects cognitive outcomes",
                "HT in younger early-menopausal women does not impair cognition, whereas WHI Memory Study data suggest increased dementia when initiating HT after age 65.",
                ref(
                    "Cognitive Function",
                    "the Women's Health Initiative Memory Study found an increased incidence of dementia in women older than 65 years initiating HT.",
                ),
            ),
            note(
                f"{p}-n10",
                "Discontinuing HT",
                "How to assess need when stopping menopausal HT",
                "Stop HT 1 week before annual visit to assess symptom severity; most women taper slowly though 3%–15% have persistent severe symptoms requiring continued therapy or alternatives.",
                ref(
                    "Discontinuing Menopausal HT",
                    "they should stop taking HT 1 week before an annual visit to allow assessment of symptom severity.",
                ),
            ),
            note(
                f"{p}-n11",
                "Laboratory testing",
                "When laboratory tests help diagnose menopause",
                "FSH, estradiol, or AMH may be indicated after hysterectomy without oophorectomy, age <40, estrogen-containing contraceptive use, or continued menses after age 55.",
                ref(
                    "diagnosis of Menopause",
                    "Measurement of FSH and estradiol or antimullerian hormone may be indicated for women who: have had a hysterectomy without oophorectomy",
                ),
            ),
            note(
                f"{p}-n12",
                "WHI context",
                "Why fear of hormones leads to undertreatment",
                "WHI findings affected appropriate HT use; clinicians should offer evidence-based therapy and reevaluate periodically rather than defaulting to unproven compounded preparations.",
                ref(
                    "Summary",
                    "fear of hormones has led to widespread undertreatment of symptoms and a proliferation of nonrigorously tested but popular treatments such as custom compounded hormones",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — hot flash duration",
                "A 48-year-old African American woman has disruptive hot flashes. Which factor likely affects duration most among these?",
                [
                    "Race",
                    "Age alone",
                    "Depression alone",
                    "Socioeconomic status alone",
                ],
                0,
                "African American women have longer duration and persistence of hot flashes compared with other racial/ethnic groups.",
                ref(
                    "Case 1",
                    "Answer: A) Race",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — heavy bleeding",
                "A 48-year-old obese woman with PCOS has heavy bleeding after 6 months amenorrhea and wants contraception. Best treatment for bleeding?",
                [
                    "Combined oral contraception",
                    "Copper intrauterine device",
                    "Progestin intrauterine device",
                    "Barrier contraception only",
                ],
                2,
                "Progestin IUD provides contraception and reduces endometrial neoplasia risk from ovulatory dysfunction; combined estrogen methods carry higher VTE/MI/breast cancer risk after age 45.",
                ref(
                    "Case 2",
                    "Answer: C) Progestin intrauterine device",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Menopause definition",
                "Menopause is diagnosed after:",
                [
                    "6 months of amenorrhea",
                    "12 months of amenorrhea",
                    "First hot flash",
                    "FSH >40 mIU/mL on one sample",
                ],
                1,
                "By convention menopause requires 12 consecutive months without menses.",
                ref(
                    "Main Conclusions",
                    "the diagnosis of menopause is not made until the individual has had 12 months of amenorrhea.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Median menopause age",
                "Median age at natural menopause in the chapter is approximately:",
                [
                    "45 years",
                    "52.5 years",
                    "60 years",
                    "38 years",
                ],
                1,
                "Median age is 52.5 years though transition length varies widely.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Menopause typically occurs in the fifth to sixth decades of life, with a median age of 52.5 years.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "VMS prevalence",
                "Vasomotor symptoms affect up to what proportion of women?",
                [
                    "10%",
                    "40%",
                    "80%",
                    "100%",
                ],
                2,
                "Up to 80% experience vasomotor symptoms during the transition.",
                ref(
                    "Menopausal Symptoms",
                    "Vasomotor symptoms affect up to 80% of women.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "GSM persistence",
                "Genitourinary syndrome of menopause differs from vasomotor symptoms because:",
                [
                    "It always resolves within 1 year",
                    "It does not spontaneously resolve over time",
                    "It never causes dyspareunia",
                    "It requires only systemic estrogen",
                ],
                1,
                "GSM often needs long-term local or systemic therapy.",
                ref(
                    "Menopausal Symptoms",
                    "symptoms of genitourinary syndrome of menopause do not spontaneously resolve over time.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Depression risk",
                "During the menopausal transition, risk of new-onset major depression is increased:",
                [
                    "2- to 4-fold compared with premenopause",
                    "Not at all",
                    "Only when estradiol is high",
                    "Only after age 70",
                ],
                0,
                "Late transition is a vulnerability period for depression, linked to sleep disruption and night sweats.",
                ref(
                    "Menopausal Symptoms",
                    "Women are 2- to 4-fold more likely to experience new-onset major depression during the menopausal transition than premenopausal women",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Unopposed estrogen",
                "In a woman with an intact uterus, chronic unopposed estrogen increases risk of:",
                [
                    "Ovarian cancer only",
                    "Endometrial hyperplasia and cancer",
                    "Breast atrophy",
                    "Vasomotor symptom cure",
                ],
                1,
                "Progestin is indicated to oppose endometrial proliferation.",
                ref(
                    "Uterine Neoplasia",
                    "The incidence of uterine neoplasia is increased under conditions of chronic unopposed estrogen exposure in a woman with an intact uterus.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "VTE risk",
                "Venous thromboembolism risk with HT is most related to:",
                [
                    "Micronized progesterone only",
                    "Oral administration and estradiol dosage",
                    "Vaginal estrogen only",
                    "Patient age under 40 exclusively",
                ],
                1,
                "Oral route and dose drive VTE risk; transdermal may be safer.",
                ref(
                    "Enous Thromboembolism",
                    "The risk is related to oral administration and estradiol dosage.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Cognitive timing",
                "WHI Memory Study suggested increased dementia when HT was initiated:",
                [
                    "In women older than 65 years",
                    "Within 1 year of final menstrual period only",
                    "With transdermal estradiol only",
                    "Never",
                ],
                0,
                "Timing and age interact with cognitive outcomes of HT.",
                ref(
                    "Cognitive Function",
                    "found an increased incidence of dementia in women older than 65 years initiating HT.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Stopping HT",
                "When planning to discontinue HT, symptom assessment is best done:",
                [
                    "While continuing full dose",
                    "After stopping HT 1 week before the visit",
                    "Only after 12 months off hormones",
                    "Without ever stopping",
                ],
                1,
                "Brief washout before annual visit clarifies ongoing symptom need.",
                ref(
                    "Discontinuing Menopausal HT",
                    "they should stop taking HT 1 week before an annual visit to allow assessment of symptom severity.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Labs for menopause",
                "FSH/estradiol testing for menopause diagnosis is indicated in:",
                [
                    "Every perimenopausal woman routinely",
                    "A woman on estrogen-containing contraceptives with unclear status",
                    "Women with regular cycles under age 45 only",
                    "Never",
                ],
                1,
                "Labs help when history is unreliable—hysterectomy without oophorectomy, young age, OCP use, or bleeding after 55.",
                ref(
                    "diagnosis of Menopause",
                    "are using estrogen-containing contraceptives (suppress FSH and elevate estradiol)",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Evidence-based care",
                "Clinicians should prioritize:",
                [
                    "Custom compounded hormones as first-line",
                    "Evidence-based HT with periodic reevaluation",
                    "Avoiding all hormonal options permanently",
                    "Laser vaginal therapy as standard of care",
                ],
                1,
                "Assess symptoms and offer evidence-based treatment with periodic reevaluation.",
                ref(
                    "Summary",
                    "Clinicians should assess a patient's symptoms and offer evidence-based treatment, with periodic reevaluation of the necessity of treatment.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Definition",
                "Menopause reflects the loss of the finite oocyte pool produced during fetal development.",
                True,
                "Reproductive senescence is a continuous process from menarche to depletion of follicles.",
                ref(
                    "Main Conclusions",
                    "It reflects the loss of the finite numbers of oocytes produced during fetal development.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "HT efficacy",
                "Hormone therapy is the most effective treatment for life-disrupting menopausal vasomotor symptoms.",
                True,
                "HT remains the most effective option despite WHI concerns.",
                ref(
                    "Significance of the Clinical Problem",
                    "HT is currently the most effective treatment for these life-disrupting symptoms.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Transition duration",
                "The average woman takes about 4 years to transition through menopause.",
                True,
                "Wide individual variation exists around this median.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The average woman takes about 4 years to make the transition into menopause.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "KNDy neurons",
                "KNDy neurons are hypothesized to drive vasomotor symptoms.",
                True,
                "Kisspeptin/neurokinin B/dynorphin neurons sit adjacent to the thermoregulatory center.",
                ref(
                    "Menopausal Symptoms",
                    "KNDy neurons (kisspeptin/neurokinin B/dynorphin), located adjacent to the thermoregulatory center, are hypothesized to be the primary driver of vasomotor symptoms.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Routine labs",
                "Laboratory tests are always required to diagnose menopause in all women.",
                False,
                "History and exam suffice when other causes of amenorrhea are excluded.",
                ref(
                    "diagnosis of Menopause",
                    "Laboratory tests are typically not indicated if history and physical examination rule out other potential causes of amenorrhea and bothersome symptoms.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Transdermal VTE",
                "Transdermal estrogen may carry lower thromboembolic risk than oral estrogen.",
                True,
                "Route modulates VTE risk while maintaining efficacy.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Transdermal preparations may carry lower risk of thromboembolic events while providing the same efficacy for treatment management.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Persistent symptoms",
                "3% to 15% of women have persistent severe vasomotor symptoms when attempting to stop HT.",
                True,
                "A minority require continued hormones or nonhormonal alternatives.",
                ref(
                    "Discontinuing Menopausal HT",
                    "a small proportion of women (3% to 15%) have persistence of severe symptoms and will require continued hormones or nonhormonal alternatives.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Compounded hormones",
                "Custom compounded hormones are rigorously tested replacements for FDA-approved HT.",
                False,
                "Fear of hormones has driven proliferation of nonrigorously tested alternatives.",
                ref(
                    "Summary",
                    "a proliferation of nonrigorously tested but popular treatments such as custom compounded hormones",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Menopause definition",
                "Assertion: Menopause requires 12 months of amenorrhea by convention.",
                "Reason: Hormonal changes never cause symptoms before cessation of menses.",
                2,
                "Assertion true; symptoms often precede final menstrual period—reason false.",
                ref(
                    "Main Conclusions",
                    "Menopause is defined as the permanent cessation of menses; by convention, the diagnosis of menopause is not made until the individual has had 12 months of amenorrhea.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Progestin",
                "Assertion: Women with a uterus need progestogen with systemic estrogen therapy.",
                "Reason: Progestogen is only for cosmetic skin benefits.",
                2,
                "Assertion true for endometrial protection—reason false.",
                ref(
                    "Uterine Neoplasia",
                    "the primary indication of progestin therapy during menopause is to prevent estradiol-induced endometrial hyperplasia and cancer.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "VMS duration",
                "Assertion: Vasomotor symptoms have a median duration of 7.4 years.",
                "Reason: All women resolve hot flashes within 1 year of the final menstrual period.",
                2,
                "Assertion true; mean post-FMP persistence is 4.5 years—reason false.",
                ref(
                    "Menopausal Symptoms",
                    "Vasomotor symptoms have a median duration of 7.4 years, with a mean post-final menstrual period persistence of 4.5 years.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Race and VMS",
                "Assertion: African American women tend to have longer hot flash duration.",
                "Reason: Race is the only modifier of vasomotor symptom duration.",
                1,
                "Both race and other factors (BMI, SES, depression) modify duration—reason overstates.",
                ref(
                    "Case 1",
                    "African American women are more likely to have a longer duration and persistence of hot flashes.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "GSM",
                "Assertion: Genitourinary syndrome of menopause may require long-term treatment.",
                "Reason: GSM symptoms always resolve spontaneously like vasomotor symptoms.",
                2,
                "Assertion true; GSM does not spontaneously resolve—reason false.",
                ref(
                    "Menopausal Symptoms",
                    "symptoms of genitourinary syndrome of menopause do not spontaneously resolve over time.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Cognitive timing",
                "Assertion: Initiating HT after age 65 may increase dementia risk.",
                "Reason: HT always improves cognition regardless of age.",
                2,
                "Assertion supported by WHI Memory Study—reason false.",
                ref(
                    "Cognitive Function",
                    "found an increased incidence of dementia in women older than 65 years initiating HT.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "VTE timing",
                "Assertion: VTE events are more likely in the first year of HT.",
                "Reason: VTE risk is unrelated to obesity or thrombophilia.",
                2,
                "Assertion true; risk is magnified by cofactors—reason false.",
                ref(
                    "Enous Thromboembolism",
                    "Venous thromboembolism events are more likely to occur within the first year of HT, and the risk is magnified with coexisting risk factors such as obesity or thrombophilia.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Early HT window",
                "Assertion: HT within the first 5 years after final menstrual period may attenuate some hypogonadism-related morbidity.",
                "Reason: HT benefits and risks are identical for all organ systems regardless of timing.",
                2,
                "Assertion from summary; risks/benefits vary by organ system and timing—reason false.",
                ref(
                    "Summary",
                    "HT, when administered within the first 5 years of the final menopause attenuates some but not all adverse effects of menopause that are related to hypogonadism.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "34",
        "title": "Management of Hormone Replacement Therapy in Post-Reproductive-Aged Women",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Genevieve Neal-Perry, MD, PhD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_34_Management_of_Hormone_Replacement_Therapy_in_PostReproductiveAged_Women.md",
        "items": items,
    }


def build_chapter_35() -> dict:
    p = "e21-35"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "PED scope",
                "Why androgenic PEDs dominate performance-enhancing drug abuse",
                "Androgens at pharmacologic doses are the only drug class with definitive evidence of enhancing strength and athletic performance; they are the most commonly abused PEDs in clinical practice.",
                ref(
                    "Significance of the Clinical Problem",
                    "Androgens administered at pharmacological dosages are the most commonly used PEDs, and they are the only class of drugs with definitive evidence that they enhance strength and athletic performance.",
                ),
            ),
            note(
                f"{p}-n2",
                "Clinical presentation",
                "How androgenic PED abusers typically present",
                "Chronic abusers present with infertility or requests for testosterone therapy; semen analyses show azoospermia or very low sperm counts with suppressed gonadotropins.",
                ref(
                    "Main Conclusions",
                    "The common clinical presentations of androgenic PED abuse are male infertility and requests for testosterone prescriptions to treat low serum testosterone.",
                ),
            ),
            note(
                f"{p}-n3",
                "Hormone patterns",
                "How serum hormones differ by androgenic PED type",
                "Exogenous testosterone, precursors, and hCG raise testosterone and suppress gonadotropins; nontestosterone anabolic steroids lower testosterone and gonadotropins; aromatase inhibitors and clomiphene raise testosterone and gonadotropins.",
                ref(
                    "Diagnosis of Androgenic PED Abuse",
                    "The use of nontestosterone androgenic anabolic steroids (eg, nadrolone, oxandrolone, danazol, stanozolol, or tetrahydrogestrinone) is associated with low testosterone and gonadotropin concentrations.",
                ),
            ),
            note(
                f"{p}-n4",
                "Diagnostic clues",
                "Why muscular physique with very low testosterone suggests PED abuse",
                "Discordance between muscularity and suppressed gonadotropins/low testosterone, elevated hematocrit, and low SHBG/HDL support abuse; re-ask respectfully about use before expensive pituitary workup.",
                ref(
                    "Case 1",
                    "This man has a discordance between his physical appearance (muscularity) and his serum testosterone concentration (very low), and he is a member of a social group at higher risk for use of androgenic PEDs (weightlifter at a gym).",
                ),
            ),
            note(
                f"{p}-n5",
                "Supportive labs",
                "How to support clinical suspicion of androgenic PED abuse",
                "Measure hematocrit plus HDL cholesterol, SHBG, and/or thyroxine-binding globulin—androgens suppress HDL, SHBG, and TBG; cortisol-binding globulin is unaffected.",
                ref(
                    "Diagnosis of Androgenic PED Abuse",
                    "Androgens raise serum hematocrit and decrease serum HDL cholesterol, SHBG, and thyroxine-binding globulin.",
                ),
            ),
            note(
                f"{p}-n6",
                "Urine testing",
                "Why urine anti-doping panels are not used clinically",
                "WADA methods require observed random sampling; outpatients can dilute, substitute, or time samples—commercial labs lack widespread access.",
                ref(
                    "Diagnosis of Androgenic PED Abuse",
                    "methods to accurately measure androgenic PEDs and their metabolites in urine are not relevant diagnostic studies in clinical practice.",
                ),
            ),
            note(
                f"{p}-n7",
                "Trust-based care",
                "How to approach patients who abuse androgenic PEDs",
                "Establish trust through respectful nonjudgmental counseling; screen for anxiety, depression, and substance use; query readiness to cease before selecting therapy.",
                ref(
                    "Treatment of Androgenic PED Abuse and Withdrawal Syndrome",
                    "A key principle for the care of androgenic PED users is the establishment a relationship of trust based on respectful and nonjudgmental behavior.",
                ),
            ),
            note(
                f"{p}-n8",
                "Short-term abuse cessation",
                "Why men with ≤1 year PED use need no adjunctive hormones to quit",
                "Gonadotropins normalize within 3–6 months and testosterone within 6 months in most short-term users; spermatogenesis recovers 3–6 months after testosterone normalizes.",
                ref(
                    "Treatment of Androgenic PED Abuse and Withdrawal Syndrome",
                    "Immediate discontinuation of androgenic PEDs without additional medical therapy is the best choice for men who have used these drugs for 1 year or less.",
                ),
            ),
            note(
                f"{p}-n9",
                "Chronic abuse fertility",
                "How to restore fertility after chronic androgenic PED abuse",
                "For men using PEDs >1 year who want conception within 2 years, hCG or clomiphene may hasten recovery; exogenous testosterone continues to suppress spermatogenesis.",
                ref(
                    "Treatment of Androgenic PED Abuse and Withdrawal Syndrome",
                    "For men who are infertile because of androgenic PED use for more than 1 year and who want to have a child within the next 2 years, the best options may be hCG therapy or clomiphene therapy.",
                ),
            ),
            note(
                f"{p}-n10",
                "Withdrawal syndrome",
                "Why androgenic PED withdrawal causes mood symptoms",
                "An androgenic PED withdrawal syndrome of depressed mood, anxiety, and low self-esteem may follow acute cessation, especially after chronic high-dose stacking.",
                ref(
                    "Significance of the Clinical Problem",
                    "there is increasing evidence that there is an androgenic PED withdrawal syndrome of depressed mood, anxiety, and low self-esteem after acute cessation.",
                ),
            ),
            note(
                f"{p}-n11",
                "Conversion strategy",
                "How 'conversion' to prescription testosterone may help reluctant quitters",
                "IM testosterone at 2–3× replacement dose with gradual taper can be safer than unregulated high-dose stacking and builds clinician trust over time.",
                ref(
                    "Treatment of Androgenic PED Abuse and Withdrawal Syndrome",
                    "Conversion to intramuscular testosterone formulations at up to 2 to 3 times the usual replacement dosage with a tapering of the dosage over several months is likely to be safer than very high dosages of androgenic PEDs of unknown safety and purity purchased from unregulated sources.",
                ),
            ),
            note(
                f"{p}-n12",
                "Proven adverse effects",
                "Documented health consequences of androgenic PED abuse in men",
                "Proven consequences include infertility, acne, and erythrocytosis; oral alkylated androgens cause hepatopathy; tendon ruptures and cardiovascular/psychiatric risks remain concerning though confounded.",
                ref(
                    "Main Conclusions",
                    "The proven health consequences include infertility, acne, and erythrocytosis in men.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — evaluation",
                "A muscular weightlifter has undetectable LH/FSH, low testosterone, and hematocrit 46%. Best additional testing?",
                [
                    "Lipid panel and cortisol-binding globulin",
                    "Lipid panel and SHBG",
                    "TBG and cortisol-binding globulin",
                    "Urinary steroid metabolite mass spectrometry panel",
                ],
                1,
                "Low SHBG and HDL support androgen exposure; urine anti-doping panels are not clinically available and are easily gamed.",
                ref(
                    "Case 1",
                    "Answer: B) Serum lipid panel and SHBG measurement",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — 1 year use",
                "A man used stacked PEDs for 1 year and wants to stop. Best recommendation besides cessation?",
                [
                    "No additional therapy",
                    "Testosterone gel taper 6 months",
                    "Clomiphene taper 12 months",
                    "hCG taper 6 months",
                ],
                0,
                "Short-term users recover spontaneously within 6–12 months; exogenous testosterone or hCG may delay axis recovery.",
                ref(
                    "Case 1 (Continued)",
                    "Answer: A) No additional therapy",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 1 — chronic use infertility",
                "After years of PED abuse, 2 months off, testosterone 80 ng/dL, azoospermia, couple trying to conceive. Best therapy?",
                [
                    "Reassurance only",
                    "Intramuscular testosterone taper",
                    "hCG therapy",
                    "Anastrozole",
                ],
                2,
                "Chronic abuse with persistent hypogonadism and infertility warrants hCG to restore testosterone and spermatogenesis; testosterone would suppress fertility further.",
                ref(
                    "Case 1 (Continued)",
                    "Answer: C) hCG therapy",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 3 — masters athlete",
                "A 55-year-old runner has new gynecomastia, testosterone 770 ng/dL, LH 13, FSH 10. Most likely cause?",
                [
                    "LH-secreting pituitary macroadenoma",
                    "Clomiphene abuse",
                    "hCG-producing tumor",
                    "Androstenedione abuse",
                ],
                1,
                "High testosterone with elevated gonadotropins suggests SERMs like clomiphene; hCG and androstenedione would suppress gonadotropins.",
                ref(
                    "Case 3",
                    "Answer: B) Clomiphene abuse",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Nontestosterone steroids",
                "Nontestosterone anabolic androgenic steroid use typically shows:",
                [
                    "High testosterone, low gonadotropins",
                    "Low testosterone, low gonadotropins",
                    "High testosterone, high gonadotropins",
                    "Normal testosterone, high gonadotropins",
                ],
                1,
                "Exogenous non-testosterone androgens suppress the axis and lower measured testosterone.",
                ref(
                    "Table. Serum Hormone Concentrations During Androgenic PED Use",
                    "Nontestosterone anabolic androgenic steroid",
                ),
            ),
            mcq(
                f"{p}-q6",
                "hCG pattern",
                "During hCG abuse as a PED, expected hormones are:",
                [
                    "Low testosterone, high LH",
                    "High testosterone, low LH and FSH",
                    "Low testosterone, high LH and FSH",
                    "Normal testosterone, normal gonadotropins",
                ],
                1,
                "hCG mimics LH, raising testosterone while suppressing pituitary gonadotropins.",
                ref(
                    "Table. Serum Hormone Concentrations During Androgenic PED Use",
                    "hCG",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Prevalence",
                "Lifetime prevalence of ever using androgenic PEDs in men worldwide is approximately:",
                [
                    "0.01%",
                    "1%–5%",
                    "25%",
                    "50%",
                ],
                1,
                "Lifetime prevalence is probably 1%–5% though chronic abuse is lower.",
                ref(
                    "Significance of the Clinical Problem",
                    "the lifetime prevalence of ever using these PEDs is probably 1% to 5% in men worldwide.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Semen findings",
                "Semen analysis in chronic androgenic PED abusers typically shows:",
                [
                    "Normal sperm concentration",
                    "Azoospermia or very low sperm concentration",
                    "Only decreased motility with normal count",
                    "High sperm concentration",
                ],
                1,
                "Suppressed intratesticular testosterone shuts down spermatogenesis.",
                ref(
                    "Diagnosis of Androgenic PED Abuse",
                    "Seminal fluid analyses generally show azoospermia or very low sperm concentrations.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Recovery timeline",
                "After discontinuing short-term PED use, gonadotropins typically normalize within:",
                [
                    "1 week",
                    "3–6 months",
                    "5 years",
                    "Never",
                ],
                1,
                "Most men with ≤1 year use recover axis function within months.",
                ref(
                    "Treatment of Androgenic PED Abuse and Withdrawal Syndrome",
                    "serum gonadotropin concentrations spontaneously normalize within 3 to 6 months",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Physical exam",
                "Which finding is sensitive and specific for PED abuse?",
                [
                    "No single physical finding is sensitive and specific",
                    "Gynecomastia alone",
                    "Small testes alone",
                    "Muscularity alone",
                ],
                0,
                "Gynecomastia and small testes may be present but are not sensitive or specific; testicular size may remain normal if baseline volume was large.",
                ref(
                    "Diagnosis of Androgenic PED Abuse",
                    "gynecomastia and small testes, but these findings are not sensitive or specific.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Oral androgens",
                "Hepatopathy with androgenic PEDs occurs with:",
                [
                    "Injectable testosterone only",
                    "Oral alkylated androgens only",
                    "Clomiphene only",
                    "Aromatase inhibitors only",
                ],
                1,
                "Oral 17-alkylated androgens carry hepatotoxicity risk.",
                ref(
                    "Significance of the Clinical Problem",
                    "Hepatopathy occurs with use of oral alkylated androgens only",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Not prepared to quit",
                "For a patient unwilling to stop PEDs, a harm-reduction option includes:",
                [
                    "Ignore all counseling",
                    "Conversion to prescription testosterone with gradual taper",
                    "Immediate bilateral orchiectomy",
                    "High-dose finasteride monotherapy",
                ],
                1,
                "Conversion may be safer than unregulated products and builds therapeutic alliance.",
                ref(
                    "Treatment of Androgenic PED Abuse and Withdrawal Syndrome",
                    "Some men who are not willing to discontinue androgenic PEDs are willing to \"convert\" to prescription testosterone.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Definitive diagnosis",
                "Definitive diagnosis of PED abuse in the general public requires:",
                [
                    "Low SHBG alone",
                    "Patient disclosure—no definitive test except in elite sport settings",
                    "MRI of the pituitary",
                    "Bone density scan",
                ],
                1,
                "Except for disclosure, no definitive outpatient diagnostic method exists.",
                ref(
                    "Barriers to Optimal Practice",
                    "Except for disclosure of androgenic abuse by the patient, there are no methods of making a definitive diagnosis of androgenic PED abuse in members of the general public.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Definition",
                "Eugonadal men taking pharmacologic androgens for performance are abusing PEDs.",
                True,
                "Replacement in hypogonadal patients is not abuse; use in eugonadal men is.",
                ref(
                    "Significance of the Clinical Problem",
                    "Individuals who are eugonadal and take androgenic PEDs are abusing them; prescription of androgen and gonadotropin replacement to hypogonadal patients is not PED abuse.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Recovery",
                "Gonadal axis function can recover spontaneously after discontinuation of androgenic PEDs.",
                True,
                "Recovery timeline depends on duration and intensity of abuse.",
                ref(
                    "Main Conclusions",
                    "Recovery of gonadal axis function occurs spontaneously after discontinuation of androgenic PEDs.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Female abusers",
                "Chronic female androgenic PED abusers are commonly seen in general endocrinology practice.",
                False,
                "Long-term abusers are almost exclusively male elite athletes—rare in most practices.",
                ref(
                    "Clinical Presentation of Androgenic PED Abuse",
                    "Women who are chronic androgenic abusers are almost exclusively elite athletes and are rarely seen by most endocrinologists",
                ),
            ),
            tf(
                f"{p}-tf4",
                "SHBG",
                "Androgens decrease serum SHBG concentrations.",
                True,
                "Low SHBG supports clinical suspicion alongside low HDL.",
                ref(
                    "Diagnosis of Androgenic PED Abuse",
                    "Androgens raise serum hematocrit and decrease serum HDL cholesterol, SHBG, and thyroxine-binding globulin.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Testosterone taper fertility",
                "Intramuscular testosterone taper preserves fertility during recovery from PED abuse.",
                False,
                "Exogenous testosterone continues to suppress spermatogenesis.",
                ref(
                    "Treatment of Androgenic PED Abuse and Withdrawal Syndrome",
                    "Exogenous testosterone therapy will continue to suppress spermatogenesis and fertility.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Clomiphene pattern",
                "Clomiphene abuse can raise testosterone and gonadotropins.",
                True,
                "SERMs block estrogen negative feedback, increasing LH/FSH and testosterone.",
                ref(
                    "Table. Serum Hormone Concentrations During Androgenic PED Use",
                    "Clomiphene",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Tendon rupture",
                "Anabolic-androgenic steroid users have increased risk of tendon rupture.",
                True,
                "Upper-extremity tendon ruptures are reported especially in steroid users.",
                ref(
                    "Significance of the Clinical Problem",
                    "there appears to be increased risk of tendinous ruptures, particularly in muscles of the arms and chest.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Stigma",
                "Social stigma is a barrier to disclosure of androgenic PED abuse.",
                True,
                "Stigma and anti-doping laws limit honest reporting.",
                ref(
                    "Barriers to Optimal Practice",
                    "Social stigma and laws against androgenic PED abuse are barriers to disclosure of abuse.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Presentation",
                "Assertion: Chronic androgenic PED abusers often present with infertility.",
                "Reason: Androgens stimulate spermatogenesis at pharmacologic doses.",
                2,
                "Assertion true; exogenous androgens suppress the HPG axis and impair sperm production—reason false.",
                ref(
                    "Main Conclusions",
                    "Serum gonadotropins are suppressed, and seminal fluid analyses show azoospermia or very low sperm concentrations.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Short-term cessation",
                "Assertion: Men with ≤1 year PED use should stop without adjunctive hormone therapy.",
                "Reason: All men require hCG after any PED exposure.",
                2,
                "Assertion true for short-term users—reason false.",
                ref(
                    "Treatment of Androgenic PED Abuse and Withdrawal Syndrome",
                    "Immediate discontinuation of androgenic PEDs without additional medical therapy is the best choice for men who have used these drugs for 1 year or less.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "hCG fertility",
                "Assertion: hCG therapy may restore spermatogenesis in chronic PED abusers seeking conception.",
                "Reason: hCG has no LH activity on Leydig cells.",
                2,
                "Assertion true (Case 1 continued)—reason false; hCG mimics LH.",
                ref(
                    "Case 1 (Continued)",
                    "Treatment with hCG therapy (Answer C) (that has LH) is likely to be effective in restoring his normal endogenous testosterone concentrations and may restore spermatogenesis within 6 to 12 months.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Clomiphene abuse",
                "Assertion: Clomiphene abuse can cause gynecomastia with high-normal testosterone and elevated gonadotropins.",
                "Reason: Clomiphene always suppresses gonadotropins.",
                2,
                "Assertion true (Case 3)—clomiphene raises gonadotropins; reason false.",
                ref(
                    "Case 3",
                    "high-normal serum testosterone and serum gonadotropins suggests the use of a selective estrogen receptor modulator such as clomiphene",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Urine testing",
                "Assertion: Urine steroid panels are not useful for routine clinical diagnosis of PED abuse.",
                "Reason: Elite sport testing methods are easily applied to unobserved outpatient samples.",
                2,
                "Assertion true; outpatient samples are easily falsified—reason false.",
                ref(
                    "Diagnosis of Androgenic PED Abuse",
                    "methods to accurately measure androgenic PEDs and their metabolites in urine are not relevant diagnostic studies in clinical practice.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Trust",
                "Assertion: Respectful nonjudgmental care improves engagement of PED users.",
                "Reason: PED users universally trust scientists about adverse effects without question.",
                2,
                "Assertion true; users may distrust clinicians who denied benefits for decades—reason false.",
                ref(
                    "Treatment of Androgenic PED Abuse and Withdrawal Syndrome",
                    "They are often distrustful of traditional health care providers and scientists.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Erythrocytosis",
                "Assertion: Erythrocytosis is a proven adverse effect of androgenic PED abuse in men.",
                "Reason: Androgens always lower hematocrit.",
                2,
                "Assertion true—reason false; androgens raise hematocrit.",
                ref(
                    "Main Conclusions",
                    "The proven health consequences include infertility, acne, and erythrocytosis in men.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Anastrozole",
                "Assertion: Anastrozole has weaker evidence than gonadotropin therapy for PED-related infertility.",
                "Reason: Aromatase inhibitors are first-line with robust RCT data in this setting.",
                2,
                "Assertion true per Case 1—anastrozole is anecdotal; hCG has stronger evidence.",
                ref(
                    "Case 1 (Continued)",
                    "there is much stronger evidence for effectiveness with gonadotropin replacement therapy.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "35",
        "title": "detection and Management of Abuse of Androgenic performanceEnhancing Drugs",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Bradley D. Anawalt, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_35_detection_and_Management_of_Abuse_of_Androgenic_performanceEnhancing_Drugs.md",
        "items": items,
    }


def build_chapter_36() -> dict:
    p = "e21-36"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Classification",
                "Why male infertility is classified into three buckets",
                "Secondary hypogonadism, testicular failure, and obstruction have distinct hormonal patterns and treatments—endocrinologists must recognize each for appropriate multidisciplinary referral.",
                ref(
                    "Main Conclusions",
                    "Male infertility may be classified into secondary hypogonadism, testicular failure, and obstruction.",
                ),
            ),
            note(
                f"{p}-n2",
                "Secondary hypogonadism",
                "How gonadotropin therapy induces spermatogenesis in hypogonadotropic hypogonadism",
                "Start hCG to mimic LH and produce intratesticular testosterone; add FSH-containing preparations after 6 months if still azoospermic; pulsatile GnRH is physiological but rarely available.",
                ref(
                    "Induction of Spermatogenesis With Gonadotropin Injections",
                    "A typical gonadotropin therapy protocol includes the initiation of hCG to mimic the biological activity of LH and induce the testes to produce testosterone.",
                ),
            ),
            note(
                f"{p}-n3",
                "NOA and mTESE",
                "How microdissection TESE changed management of nonobstructive azoospermia",
                "mTESE retrieves sperm in 20%–40% of men with NOA—including Klinefelter syndrome—by identifying engorged seminiferous tubules under microscopy.",
                ref(
                    "Main Conclusions",
                    "Microsurgical testicular sperm extraction (mTESE) is used to successfully retrieve sperm in 20% to 40% of men with NOA, including men with Klinefelter syndrome.",
                ),
            ),
            note(
                f"{p}-n4",
                "Obstructive azoospermia",
                "Why obstructive azoospermia is often underrecognized",
                "OA shows normal testicular volume, normal FSH, and normal testosterone—genitourinary infections (e.g., chlamydia) are the most common worldwide cause; CFTR variants cause congenital bilateral absence of vas deferens.",
                ref(
                    "Obstructive Azoospermia",
                    "OA can be caused by genitourinary tract infections such as chlamydia, ureaplasma, and mycoplasma, which lead to scarring and blockage of the epididymis.",
                ),
            ),
            note(
                f"{p}-n5",
                "OA management",
                "How obstructive azoospermia is treated surgically",
                "Percutaneous or microsurgical epididymal sperm aspiration collects sperm when spermatogenesis is intact; there is no role for endocrine therapy in OA.",
                ref(
                    "Surgical Management of Male Infertility",
                    "Percutaneous epididymal sperm aspiration or microsurgical epididymal sperm aspiration are highly effective techniques for collecting sperm in men with OA",
                ),
            ),
            note(
                f"{p}-n6",
                "Y chromosome",
                "Why AZF microdeletion subtype matters before mTESE",
                "AZFa and AZFb deletions are largely incompatible with spermatogenesis; AZFc deletions may still yield sperm with mTESE and ICSI.",
                ref(
                    "Y-Chromosome Microdeletions",
                    "Deletions of the AZFa and AZFb regions are largely incompatible with spermatogenesis, and mTESE is not advised.",
                ),
            ),
            note(
                f"{p}-n7",
                "SERMs and aromatase inhibitors",
                "How clomiphene and aromatase inhibitors differ from testosterone in infertile hypogonadal men",
                "They reduce estrogenic pituitary feedback, raising endogenous testosterone while preserving spermatogenesis—unlike exogenous testosterone, which suppresses the axis.",
                ref(
                    "Selective Estrogen Receptor Modulators and Aromatase Inhibitors",
                    "elevate levels of serum testosterone in men with hypogonadism while preserving spermatogenesis.",
                ),
            ),
            note(
                f"{p}-n8",
                "Semen analysis",
                "How to obtain a valid semen analysis",
                "Perform after 2–7 days abstinence; assess volume, concentration (≥15×10⁶/mL), motility, and morphology per WHO thresholds.",
                ref(
                    "Assessment",
                    "Semen analysis should be performed in all patients following abstinence of a minimum of 2 days and maximum of 7 days",
                ),
            ),
            note(
                f"{p}-n9",
                "Prior testosterone",
                "Why prior testosterone therapy does not preclude sperm induction",
                "Meta-analyses suggest prior testosterone does not significantly reduce gonadotropin-induced spermatogenesis success in hypogonadotropic hypogonadism.",
                ref(
                    "Case 1",
                    "Recent meta-analyses suggest that testosterone therapy does not significantly reduce the effectiveness of sperm induction for hypogonadotropic hypogonadism",
                ),
            ),
            note(
                f"{p}-n10",
                "Klinefelter mTESE",
                "How to counsel men with Klinefelter syndrome before mTESE",
                "Sperm retrieval is reported in nonmosaic Klinefelter; counsel about thromboembolic risk; avoid starting testosterone before retrieval if pursuing fertility.",
                ref(
                    "Case 2",
                    "Sperm retrieval following mTESE is reported widely in men with nonmosaic Klinefelter syndrome",
                ),
            ),
            note(
                f"{p}-n11",
                "Multifactorial oligoasthenoteratospermia",
                "Why male subfertility is often multifactorial",
                "Cryptorchidism, genitourinary infection, obesity, and female-factor infertility may coexist—pituitary incidentalomas may be unrelated.",
                ref(
                    "Case 4",
                    "The principle learning point is that multiple factors may contribute to the etiology.",
                ),
            ),
            note(
                f"{p}-n12",
                "Hormonal stimulation before mTESE",
                "Pitfall: empiric gonadotropins/SERMs before mTESE in NOA",
                "Urologists sometimes use hormonal stimulation before mTESE, but insufficient evidence supports widespread safety or efficacy in nonobstructive azoospermia.",
                ref(
                    "Main Conclusions",
                    "Hormonal stimulation with gonadotropins or selective estrogen receptor modulators are used routinely before mTESE in men with NOA, but there are insufficient data to support their widespread use.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — hCG counseling",
                "A man with hypogonadotropic hypogonadism after childhood delayed puberty seeks fertility after stopping testosterone. Correct statement?",
                [
                    "Prior testosterone always prevents sperm induction",
                    "WHO reference sperm count is required for spontaneous pregnancy",
                    "FSH pretreatment is proven superior to starting hCG",
                    "Counsel about gynecomastia risk when starting hCG",
                ],
                3,
                "hCG may cause gynecomastia; prior testosterone does not block induction; pregnancy can occur with counts below WHO reference.",
                ref(
                    "Case 1",
                    "Answer: D) He should be counseled about the risk of gynecomastia when starting hCG therapy",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — Klinefelter",
                "A 32-year-old with 47,XXY azoospermia asks about mTESE. Correct statement?",
                [
                    "Start testosterone immediately before surgery",
                    "mTESE never succeeds in nonmosaic Klinefelter",
                    "Counsel about increased thromboembolic surgical risk",
                    "New hypogonadism after mTESE occurs in exactly 5% of NOA men",
                ],
                2,
                "Klinefelter men have thrombophilia risk; testosterone before retrieval suppresses sperm; mTESE can succeed; post-mTESE hypogonadism in NOA is ~20%.",
                ref(
                    "Case 2",
                    "Answer: C) Men with Klinefelter syndrome have increased surgical risk due to thrombophilia",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3 — obstructive pattern",
                "36-year-old with azoospermia, normal testes (22 mL), normal FSH and testosterone. Most likely diagnosis?",
                [
                    "Genitourinary infection",
                    "AZFb microdeletion",
                    "Mumps orchitis",
                    "Klinefelter syndrome",
                ],
                0,
                "Normal volume and FSH with azoospermia indicates obstruction; GU infections are the most common worldwide cause.",
                ref(
                    "Case 3",
                    "Answer: A) Genitourinary infection",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 4 — multifactorial",
                "Man with oligoasthenoteratospermia, 8-mL left testis after orchidopexy, elevated round cells, obesity, partner age 39. Contributing factors include:",
                [
                    "Pituitary microadenoma alone",
                    "Cryptorchidism, infection, obesity, and female-factor infertility",
                    "Only CFTR-related obstruction",
                    "Only prolactinoma",
                ],
                1,
                "Multiple concurrent male and female factors explain subfertility; incidental pituitary lesion is likely unrelated.",
                ref(
                    "Case 4",
                    "Answer: B, C, D, and E) Testicular failure secondary to cryptorchidism, genitourinary infection, obesity, and female-factor infertility",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Secondary hypogonadism hormones",
                "Hypogonadotropic hypogonadism typically shows:",
                [
                    "High FSH, high LH, low testosterone",
                    "Low FSH, low LH, low testosterone",
                    "Normal FSH, azoospermia, normal testosterone",
                    "High testosterone, low LH only",
                ],
                1,
                "Central failure lowers both gonadotropins and testosterone with azoospermia.",
                ref(
                    "Table 1. Causes of Male Infertility",
                    "FSH: low LH: low Testosterone: low",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Testicular failure hormones",
                "Primary testicular failure typically shows:",
                [
                    "Low FSH and low LH",
                    "High or normal FSH/LH with low or normal testosterone",
                    "Normal FSH with normal testosterone and azoospermia",
                    "Undetectable testosterone with normal gonadotropins",
                ],
                1,
                "Loss of inhibin feedback raises FSH; Leydig failure may lower testosterone.",
                ref(
                    "Table 1. Causes of Male Infertility",
                    "FSH: high LH: high or normal Testosterone: low or normal",
                ),
            ),
            mcq(
                f"{p}-q7",
                "OA hormones",
                "Obstructive azoospermia typically shows:",
                [
                    "High FSH, small testes",
                    "Normal FSH and normal testosterone with normal testicular volume",
                    "Low LH and low testosterone",
                    "High prolactin",
                ],
                1,
                "Spermatogenesis is often intact; obstruction blocks delivery.",
                ref(
                    "Table 1. Causes of Male Infertility",
                    "FSH: normal Testosterone: normal Testicular volume: normal",
                ),
            ),
            mcq(
                f"{p}-q8",
                "hCG protocol",
                "In gonadotropin induction, FSH is added when:",
                [
                    "Immediately with first hCG dose always",
                    "Patient remains azoospermic after 6 months of hCG",
                    "Only if prolactin is elevated",
                    "Never—hCG alone is always sufficient",
                ],
                1,
                "Semen analysis at 6 months guides addition of FSH-containing injections.",
                ref(
                    "Induction of Spermatogenesis With Gonadotropin Injections",
                    "FSH-containing injections (such as menotropin) should be added to hCG therapy in patients who remaining azoospermic following 6 months of hCG treatment.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "AZFc deletion",
                "AZFc Y-chromosome microdeletion:",
                [
                    "Always precludes any spermatogenesis",
                    "May still allow mTESE with possible sperm retrieval",
                    "Causes obstructive azoospermia only",
                    "Requires testosterone before mTESE",
                ],
                1,
                "AZFc may retain some spermatogenic potential unlike AZFa/AZFb.",
                ref(
                    "Y-Chromosome Microdeletions",
                    "deletions of the AZFc region may be compatible with a degree of spermatogenesis in some patients, so mTESE may be considered",
                ),
            ),
            mcq(
                f"{p}-q10",
                "CFTR and OA",
                "CFTR pathogenic variants are associated with:",
                [
                    "Congenital bilateral absence of vas deferens",
                    "Klinefelter syndrome",
                    "Isolated high FSH",
                    "Retrograde ejaculation only",
                ],
                0,
                "CFTR carrier status links to CBAVD as a form of OA.",
                ref(
                    "Obstructive Azoospermia",
                    "OA may also be associated with CFTR gene carrier status.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Testosterone in infertility",
                "Exogenous testosterone in a man desiring fertility:",
                [
                    "Improves sperm count",
                    "Suppresses spermatogenesis and should be avoided",
                    "Is first-line for NOA",
                    "Replaces hCG therapy",
                ],
                1,
                "Exogenous androgens suppress the HPG axis and sperm production.",
                ref(
                    "Case 2",
                    "Testosterone therapy should not be started, otherwise any residual spermatogenesis is likely to be suppressed",
                ),
            ),
            mcq(
                f"{p}-q12",
                "WHO sperm concentration",
                "WHO lower reference limit for sperm concentration is:",
                [
                    "1 × 10⁶ per mL",
                    "15 × 10⁶ per mL",
                    "50 × 10⁶ per mL",
                    "100 × 10⁶ per mL",
                ],
                1,
                "WHO 5th edition reference threshold is 15 million/mL.",
                ref(
                    "Table 2. World Health Organization Minimum Thresholds of Semen Parameters in Men Fathering Children Without Fertility Problems",
                    "Sperm concentration 15 × 10⁶ per mL",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Male factor burden",
                "Approximately what fraction of infertility cases involve a male factor?",
                [
                    "None",
                    "Up to about half",
                    "90%",
                    "Only when female workup is normal",
                ],
                1,
                "Up to half of infertility is attributed to male-partner problems.",
                ref(
                    "Significance of the Clinical Problem",
                    "Up to half of cases of infertility are attributed to a problem in the male partner",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Classification",
                "Gonadotropin injections are highly effective for inducing spermatogenesis in secondary hypogonadism.",
                True,
                "hCG ± FSH is standard fertility induction for hypogonadotropic hypogonadism.",
                ref(
                    "Main Conclusions",
                    "Gonadotropin injections are highly effective at inducing spermatogenesis in men with secondary hypogonadism.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "GnRH pulsatile",
                "Pulsatile GnRH for male infertility is widely available outside research settings.",
                False,
                "Pulsatile GnRH is usually restricted to research when unavailable commercially.",
                ref(
                    "Main Conclusions",
                    "GnRH pulsatile therapy is usually restricted to research settings when inducing spermatogenesis in men with secondary hypogonadism.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "NOA prevalence",
                "Most cases of male infertility are due to testicular failure.",
                True,
                "Testicular failure/NOA is the most common category.",
                ref(
                    "Main Conclusions",
                    "Most cases of male infertility are due to testicular failure (ie, hypergonadotropic hypogonadism).",
                ),
            ),
            tf(
                f"{p}-tf4",
                "OA endocrine therapy",
                "There is a major role for endocrine therapy in obstructive azoospermia.",
                False,
                "Surgical sperm retrieval is appropriate; endocrine therapy does not treat obstruction.",
                ref(
                    "Main Conclusions",
                    "There is no role for endocrine therapy in the management of OA",
                ),
            ),
            tf(
                f"{p}-tf5",
                "mTESE yield",
                "mTESE retrieves sperm in 20%–40% of men with NOA.",
                True,
                "Including some men with Klinefelter syndrome.",
                ref(
                    "Main Conclusions",
                    "mTESE is used to successfully retrieve sperm in 20% to 40% of men with NOA",
                ),
            ),
            tf(
                f"{p}-tf6",
                "SERMs licensed",
                "Clomiphene is FDA-licensed for male hypogonadism and infertility.",
                False,
                "Neither SERMs nor aromatase inhibitors are licensed for male hypogonadism/infertility.",
                ref(
                    "Selective Estrogen Receptor Modulators and Aromatase Inhibitors",
                    "neither drug class is licensed for the treatment of male hypogonadism or male infertility.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Genetic testing",
                "Men with azoospermia should have karyotype, Y-microdeletion, and CFTR testing.",
                True,
                "Genetic evaluation is part of standard azoospermia workup.",
                ref(
                    "Assessment",
                    "Genetic testing should be performed for all patients with azoospermia; these tests should include karyotype analysis and assessment for Y-chromosome microdeletions and CFTR pathogenic variants.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Sperm count for pregnancy",
                "Spontaneous pregnancy requires sperm concentration at or above the WHO reference range.",
                False,
                "Couples can conceive with sperm counts much lower than 15 million/mL.",
                ref(
                    "Case 1",
                    "Couples can become pregnant with sperm counts much lower than the World Health Organization reference range",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "hCG mechanism",
                "Assertion: hCG therapy mimics LH to stimulate testicular testosterone production.",
                "Reason: hCG directly stimulates FSH receptors on Sertoli cells.",
                2,
                "Assertion true; hCG acts on Leydig cells—reason false.",
                ref(
                    "Induction of Spermatogenesis With Gonadotropin Injections",
                    "initiation of hCG to mimic the biological activity of LH and induce the testes to produce testosterone.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "OA pattern",
                "Assertion: Obstructive azoospermia may have normal FSH and normal testicular volume.",
                "Reason: Obstructive azoospermia always presents with high FSH.",
                2,
                "Assertion true; FSH is normal when spermatogenesis is intact—reason false.",
                ref(
                    "Assessment",
                    "OA should be suspected if men have azoospermia despite having normal testicular volume and no features of hypogonadism.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Testosterone fertility",
                "Assertion: Exogenous testosterone suppresses spermatogenesis in men seeking fertility.",
                "Reason: Testosterone stimulates intratesticular sperm production at replacement doses.",
                2,
                "Assertion true; exogenous testosterone inhibits the axis—reason false.",
                ref(
                    "Case 2",
                    "Testosterone therapy should not be started, otherwise any residual spermatogenesis is likely to be suppressed",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Klinefelter mTESE",
                "Assertion: mTESE can retrieve sperm in some men with nonmosaic Klinefelter syndrome.",
                "Reason: Klinefelter syndrome always has absent spermatogenesis making mTESE futile.",
                2,
                "Assertion true—reason false per contemporary surgical series.",
                ref(
                    "Case 2",
                    "Sperm retrieval following mTESE is reported widely in men with nonmosaic Klinefelter syndrome",
                ),
            ),
            ar(
                f"{p}-ar5",
                "AZFa/AZFb",
                "Assertion: AZFa and AZFb microdeletions generally preclude successful mTESE.",
                "Reason: All Y-chromosome microdeletions have identical prognosis for sperm retrieval.",
                2,
                "Assertion true; AZFc may differ—reason false.",
                ref(
                    "Y-Chromosome Microdeletions",
                    "Deletions of the AZFa and AZFb regions are largely incompatible with spermatogenesis, and mTESE is not advised.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Prior testosterone",
                "Assertion: Prior testosterone therapy does not significantly reduce sperm induction success in hypogonadotropic hypogonadism.",
                "Reason: Any prior testosterone permanently destroys seminiferous tubules.",
                2,
                "Assertion supported by meta-analyses—reason false.",
                ref(
                    "Case 1",
                    "testosterone therapy does not significantly reduce the effectiveness of sperm induction for hypogonadotropic hypogonadism",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Round cells",
                "Assertion: Elevated semen round cells may indicate genitourinary infection.",
                "Reason: Round cells in semen always represent immature sperm only.",
                2,
                "Assertion true (Case 4)—many round cells are leukocytes suggesting infection.",
                ref(
                    "Case 4",
                    "Most round cells in the seminal plasma are leukocytes, so an elevated count may indicate genitourinary infection",
                ),
            ),
            ar(
                f"{p}-ar8",
                "NOA hormonal pretreatment",
                "Assertion: Routine hormonal stimulation before mTESE in NOA lacks sufficient supporting evidence.",
                "Reason: Large RCTs prove gonadotropin pretreatment doubles mTESE success in all NOA men.",
                2,
                "Assertion true per chapter—widespread use is not evidence-supported.",
                ref(
                    "Main Conclusions",
                    "there are insufficient data to support their widespread use.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "36",
        "title": "Evaluation of Male Infertility",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Channa Jayasena, MD, PhD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_36_Evaluation_of_Male_Infertility.md",
        "items": items,
    }


MODULES = {
    "endo2021_chapter_32_Diagnosis_and_Management_of_Functional_Hypogonadism_in_the_Male_Patient.json": build_chapter_32,
    "endo2021_chapter_33_Antimullerian_Hormone_and_Ovarian_Reserve_Testing.json": build_chapter_33,
    "endo2021_chapter_34_Management_of_Hormone_Replacement_Therapy_in_PostReproductiveAged_Women.json": build_chapter_34,
    "endo2021_chapter_35_detection_and_Management_of_Abuse_of_Androgenic_performanceEnhancing_Drugs.json": build_chapter_35,
    "endo2021_chapter_36_Evaluation_of_Male_Infertility.json": build_chapter_36,
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
