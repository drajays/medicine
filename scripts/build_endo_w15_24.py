#!/usr/bin/env python3
"""Generate Williams 15e module w15-24 — Transgender Endocrinology."""
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
OUT_NAME = "w15-24_Transgender_Endocrinology.json"


def build() -> dict:
    p = "w15-24"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why gender-affirming care aligns body with identity",
                "Transgender and gender-diverse people have gender identities differing from sex designated at birth; GAH reduces endogenous sex hormones and replaces them to achieve phenotypic transition.",
                ref(
                    "KEY POINTS",
                    "Transgender and gender-diverse people have gender identities that differ from the gender implied by their sex designated (assigned) at birth.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How pubertal suppression precedes gender-affirming hormones in youth",
                "Eligible adolescents start GnRH agonists at Tanner stage 2 to halt undesired puberty, then transition to affirmed-gender hormone therapy when appropriate.",
                ref(
                    "KEY POINTS",
                    "Youth deemed eligible to initiate hormone therapy generally start with gonadotropin-releasing hormone agonists at Tanner stage 2 to halt further pubertal progression, and at the appropriate time, they start gender-affirming hormone therapy that is aligned with the affirmed gender.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Transfeminine adult estrogen regimens",
                "Transfeminine adults start estrogen combined with androgen-lowering agents; transmasculine adults start testosterone—both titrated to physiologic targets with monitoring.",
                ref(
                    "KEY POINTS",
                    "Transfeminine adults with a gender identity that is not aligned with their sex designated at birth will start on a regimen of estrogen in combination with androgen-lowering medications.",
                ),
            ),
            note(
                f"{p}-n4",
                "KEY POINTS",
                "Why physiologic hormone levels limit long-term risk",
                "GAH risks are relatively few when levels remain physiologic, but adverse-event monitoring continues until longer-term safety data mature.",
                ref(
                    "KEY POINTS",
                    "The long-term risks of gender-affirming hormone therapy are relatively few when hormone levels remain in the physiologic range; however, monitoring of potential adverse events is still recommended until long-term risks can be better ascertained.",
                ),
            ),
            note(
                f"{p}-n5",
                "Mental Health Considerations and Care of Transgender Youth",
                "Why earlier access to gender-affirming care improves mental health",
                "Early-pubertal TGD youth presenting for care have better baseline mental health than those presenting later—supporting timely multidisciplinary evaluation.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "Notably, early-pubertal TGD youth presenting for gender-affirming medical care had better baseline mental health compared to those presenting at later stages of puberty, pointing to the potential benefits of accessing gender-affirming care earlier in life.",
                ),
            ),
            note(
                f"{p}-n6",
                "Mental Health Considerations and Care of Transgender Youth",
                "How family support buffers psychiatric risk in TGD youth",
                "Parental support correlates with higher self-esteem, life satisfaction, and fewer suicide attempts—many mental health burdens reflect societal rejection rather than intrinsic transgender identity.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "With respect to the impact of family support, TGD youth had greater positive self-esteem and life satisfaction, as well as lesser anxiety and fewer suicide attempts, in comparison to those individuals whose parents were not supportive.",
                ),
            ),
            note(
                f"{p}-n7",
                "Mental Health Considerations and Care of Transgender Youth",
                "Why GD worsening at puberty predicts persistent transgender identity",
                "Gender dysphoria that emerges or intensifies with physical puberty strongly suggests adult transgender identity—mandating qualified mental health/gender specialist evaluation.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "GD that either worsens or emerges with onset of physical puberty implies a high likelihood of a transgender identity during adulthood.",
                ),
            ),
            note(
                f"{p}-n8",
                "Mental Health Considerations and Care of Transgender Youth",
                "How WPATH and Endocrine Society guide adolescent care",
                "Dutch pioneering work informs ES clinical practice guidelines and WPATH standards of care—both endorse pubertal suppression at Tanner 2 when criteria are met.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "Based on pioneering work from the Netherlands, gender-affirming medical care of TGD youth has been primarily informed by a clinical practice guideline (CPG) from the Endocrine Society (ES) and cosponsoring organizations and by standards of care (SOCs) from the World Professional Association for Transgender Health (WPATH).",
                ),
            ),
            note(
                f"{p}-n9",
                "Mental Health Considerations and Care of Transgender Youth",
                "How GnRH agonists provide reversible pubertal pause",
                "GnRH agonists at Tanner 2 pause irreversible secondary sex characteristic development, allowing gender exploration without ongoing pubertal pressure; Tanner 2 breast/testicular tissue typically regresses.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "Considered fully reversible treatments, GnRH agonists, by pausing puberty in this clinical setting, provide additional time for gender identity exploration without the pressure of continued pubertal progression and prevent irreversible development of secondary sex characteristics associated with a puberty that is not aligned with the person's gender identity.",
                ),
            ),
            note(
                f"{p}-n10",
                "Mental Health Considerations and Care of Transgender Youth",
                "Why delaying GAH until age 16 may harm bone and psychosocial health",
                "Blocking puberty at Tanner 2 then withholding sex hormones until 16 risks bone health and prolonged social isolation from age-matched peers.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "Delaying sex hormone treatment until age 16 years in an adolescent whose puberty was blocked at Tanner stage 2 could not only be detrimental to bone health, but also keeping someone suspended in an early pubertal state until this age could isolate the individual further from age-matched peers, with potentially negative consequences for emotional well-being.",
                ),
            ),
            note(
                f"{p}-n11",
                "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                "Fertility counseling before pubertal suppression",
                "Informed consent and fertility implications discussion must precede pubertal suppression or GAH—early suppression may compromise later fertility if physical transition proceeds.",
                ref(
                    "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                    "It is essential that an informed consent process and a discussion about implications for fertility precede any treatment of TGD youth with pubertal suppression and/or GAH.",
                ),
            ),
            note(
                f"{p}-n12",
                "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                "How GnRH agonists affect bone mineral density in youth",
                "GnRH agonist monotherapy lowers BMD Z-scores; adding GAH may partially recover density—adequate calcium, vitamin D (≥30 ng/mL), and weight-bearing exercise are essential.",
                ref(
                    "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                    "Treatment with GnRH agonist therapy in TGD adolescents is associated with significant decreases in BMD Z-scores.",
                ),
            ),
            note(
                f"{p}-n13",
                "Outcomes of Current Treatment Models for TGD Youth and Potential Adverse Effects",
                "Netherlands three-stage outcome data",
                "After pubertal suppression, cross-sex hormones, and surgery, GD resolved, psychological functioning improved, and well-being matched or exceeded population controls without treatment regret.",
                ref(
                    "Outcomes of Current Treatment Models for TGD Youth and Potential Adverse Effects",
                    "After the completion of this three-stage approach to care, GD was resolved, general psychological functioning steadily improved, and a sense of well-being based on standardized survey results was noted to be equal to or greater than that seen in age-matched controls from the general population; none of the study participants regretted treatment.",
                ),
            ),
            note(
                f"{p}-n14",
                "Care of Transgender Adults",
                "Why mental health referral is not mandatory for adult GAH",
                "Adults with fixed gender identity may receive GAH from knowledgeable prescribers without mandatory mental health referral per ES CPG—though referral helps when GD severity or comorbidity is unclear.",
                ref(
                    "Care of Transgender Adults",
                    "It is not a requirement to have a mental health referral in adults as stated in the ES CPG",
                ),
            ),
            note(
                f"{p}-n15",
                "Transfeminine Hormone Therapy",
                "Why 17β-estradiol is preferred over ethinyl estradiol",
                "Conjugated and synthetic estrogens cannot be monitored in serum; ethinyl estradiol carries elevated VTE and cardiovascular mortality risk—17β-estradiol is preferred.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "With respect to estrogen treatment,  $ 17\\beta $-estradiol (transdermal, oral, or parenteral) is preferred to conjugated (e.g., Premarin) or synthetic estrogens (e.g., ethinyl estradiol) because conjugated and synthetic estrogen levels cannot be monitored in the serum, and ethinyl estradiol is associated with an increased risk for venous thromboembolic disease and death from cardiovascular causes in adult studies (see later discussion on hormone therapy in TGD adults).",
                ),
            ),
            note(
                f"{p}-n16",
                "Transfeminine Hormone Therapy",
                "How to titrate oral estradiol in transfeminine adults",
                "Oral estradiol is titrated to serum estradiol 100–200 pg/mL; typical daily doses of 2–6 mg achieve target range in combination with antiandrogens.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "The dose of oral estradiol is titrated to a serum estradiol range of 100 to 200 pg/mL.",
                ),
            ),
            note(
                f"{p}-n17",
                "Transfeminine Hormone Therapy",
                "Why transdermal estrogen is favored after age 40",
                "Transdermal estradiol is presumed less prothrombotic; Dutch practice switches all transgender women to transdermal estrogen after age 40 because of thromboembolic risk.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "Transdermal estrogen, presumed to be less stimulatory of prothrombotic proteins, is preferred in transgender women over the age of 40 due to the increased risk of thromboembolic disease.",
                ),
            ),
            note(
                f"{p}-n18",
                "Testosterone-Lowering Agents",
                "How cyproterone compares with spironolactone",
                "Cyproterone acetate lowers testosterone more effectively than spironolactone in RCTs but carries hyperprolactinemia and meningioma concerns—lowest effective dose (10 mg) may suffice.",
                ref(
                    "Testosterone-Lowering Agents",
                    "A randomized controlled trial of cyproterone acetate 25 mg daily versus spironolactone 100 mg daily, both in combination with estradiol 4 mg daily, found that cyproterone was more effective in lowering serum testosterone concentrations.",
                ),
            ),
            note(
                f"{p}-n19",
                "5α-Reductase Inhibitors",
                "Why finasteride is not first-line in transfeminine care",
                "5α-reductase inhibitors do not lower serum testosterone and may worsen depression/sexual dysfunction—problematic in a population already at elevated suicide risk.",
                ref(
                    "5α-Reductase Inhibitors",
                    "Because there is already an increased rate of depression and suicide in the transgender population, these medications should not be used as first-line therapies.",
                ),
            ),
            note(
                f"{p}-n20",
                "Transmasculine Hormone Therapy",
                "How testosterone achieves virilization goals",
                "Testosterone targets cisgender male concentrations to induce facial/body hair, voice deepening, muscle mass, and amenorrhea while reducing dysphoria and improving mood.",
                ref(
                    "Transmasculine Hormone Therapy",
                    "The goal of the testosterone therapy is to reach serum testosterone concentrations in the range expected for cisgender men and to induce male secondary sex characteristics, including increased body and facial hair, deeper voice, increased muscle mass, and cessation of menses (see Box 24.4).",
                ),
            ),
            note(
                f"{p}-n21",
                "Potential Risks Associated With Transmasculine Hormone Therapy",
                "Why hematocrit monitoring is essential on testosterone",
                "Testosterone stimulates erythropoietin and raises hematocrit; ES CPG recommends keeping hematocrit below 55% to prevent complications of polycythemia.",
                ref(
                    "Potential Risks Associated With Transmasculine Hormone Therapy",
                    "The ES CPG recommends maintaining hematocrit below 55% to avoid adverse events arising from increased red cell mass.",
                ),
            ),
            note(
                f"{p}-n22",
                "Potential Risks Associated With Transfeminine Hormone Therapy",
                "Venous thromboembolism as the major transfeminine risk",
                "VTE is the best-studied serious complication of transfeminine therapy—driven primarily by estrogen formulation, route, age, and perioperative factors.",
                ref(
                    "Potential Risks Associated With Transfeminine Hormone Therapy",
                    "Thromboembolism is the most well-studied and most serious complication resulting from transfeminine hormone therapy, primarily from estrogen.",
                ),
            ),
            note(
                f"{p}-n23",
                "Potential Risks Associated With Transfeminine Hormone Therapy",
                "How adequate estrogen protects bone in transfeminine adults",
                "Adequate estrogen suppresses gonadotropins and increases lumbar/hip BMD over 12–24 months; baseline BMD may be low before therapy.",
                ref(
                    "Potential Risks Associated With Transfeminine Hormone Therapy",
                    "Adequate estrogen therapy is protective against bone loss in transgender women.",
                ),
            ),
            note(
                f"{p}-n24",
                "Effects of Pubertal Suppression on Need for GAS and Effects on GAS",
                "How early pubertal blockade affects future genital surgery",
                "Early GnRH suppression prevents masculine facial changes but underdevelops penoscrotal tissue—vaginoplasty may require peritoneal or graft lining alternatives.",
                ref(
                    "Effects of Pubertal Suppression on Need for GAS and Effects on GAS",
                    "However, pubertal suppression at an early stage of puberty also leads to underdevelopment of the penoscrotal tissue, which can have an impact on gender-affirming genital surgery.",
                ),
            ),
            note(
                f"{p}-n25",
                "Progestins",
                "Progesterone lacks evidence in transfeminine regimens",
                "ES CPG does not recommend progesterone; insufficient evidence supports breast enhancement claims, and WHI data raise stroke concerns with medroxyprogesterone plus conjugated estrogens.",
                ref(
                    "Progestins",
                    "There currently is insufficient evidence to support the use of progesterone for transgender women.",
                ),
            ),
            note(
                f"{p}-n26",
                "Barriers to Care and Priorities for Research for Transgender Youth and Adults",
                "Barriers to transgender endocrine care",
                "GnRH agonists and GAH are off-label, often expensive, and frequently denied by insurers; long-term cardiovascular/cancer data and provider training remain limited.",
                ref(
                    "Barriers to Care and Priorities for Research for Transgender Youth and Adults",
                    "Furthermore, GnRH agonists and gender-affirming sex hormones are off-label for TGD youth and adults, can be expensive (GnRH agonists and transdermal preparations of hormones, in particular), and are often denied by insurance companies.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Mental Health Considerations and Care of Transgender Youth",
                "A 14-year-old assigned female at birth with worsening gender dysphoria since menarche is evaluated. Before initiating medical therapy, what is the essential first step?",
                [
                    "Comprehensive biopsychosocial assessment by a qualified mental health/gender specialist",
                    "Immediate bilateral oophorectomy",
                    "Start testosterone without evaluation",
                    "Karyotype to rule out Turner syndrome",
                ],
                0,
                "Youth seeking transition-related care require thorough mental health/gender specialist evaluation for GD, comorbidities, and readiness before hormone therapy.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "Given the complexity of GD—and of adolescence itself—it is essential that youth with GD undergo a thorough evaluation by a qualified mental health/gender specialist.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Mental Health Considerations and Care of Transgender Youth",
                "A 12-year-old assigned male at birth (Tanner 2, TV 5 mL) with persistent GD requests pubertal blockade. Per WPATH/ES guidance, appropriate initial medical therapy?",
                [
                    "GnRH agonist to pause pubertal progression",
                    "High-dose oral ethinyl estradiol",
                    "Testosterone 200 mg IM every 2 weeks",
                    "Observation until age 18 regardless of distress",
                ],
                0,
                "Eligible youth start GnRH agonists at Tanner 2 to halt undesired pubertal changes before later GAH when criteria persist.",
                ref(
                    "KEY POINTS",
                    "Youth deemed eligible to initiate hormone therapy generally start with gonadotropin-releasing hormone agonists at Tanner stage 2 to halt further pubertal progression, and at the appropriate time, they start gender-affirming hormone therapy that is aligned with the affirmed gender.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Mental Health Considerations and Care of Transgender Youth",
                "A 15-year-old transmasculine adolescent on GnRH agonist since Tanner 2 develops uterine bleeding when testosterone is started at low dose. Best add-on?",
                [
                    "Progestin per Table 24.2 to achieve amenorrhea",
                    "Discontinue all hormone therapy permanently",
                    "GnRH agonist must never be stopped on testosterone",
                    "High-dose glucocorticoids",
                ],
                0,
                "Once adult testosterone levels are reached GnRH can usually stop; breakthrough bleeding warrants progestin as outlined in progestogen regimens.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "If uterine bleeding occurs, a progestin can be added, as outlined in Table 24.2.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Mental Health Considerations and Care of Transgender Youth",
                "A 16-year-old trans feminine teen blocked at Tanner 2 since age 13 has persistent GD and multidisciplinary clearance. When initiating estrogen, what must continue?",
                [
                    "GnRH agonist or alternative antiandrogen until gonadectomy if pursued",
                    "GnRH agonist is never needed with estrogen",
                    "Ethinyl estradiol 50 mcg daily as first choice",
                    "No laboratory monitoring is required",
                ],
                0,
                "Initial estrogen doses do not suppress endogenous testosterone—GnRH analog or antiandrogen continues until gonadectomy if surgery is planned.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "In individuals designated male at birth and treated with estrogen therapy, it is therefore recommended that GnRH analog treatment (or an alternative antiandrogen) be continued until gonadectomy, if such surgery is pursued.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                "Parents of a 13-year-old starting GnRH agonist ask about fertility. Most appropriate counseling?",
                [
                    "Discuss fertility implications and preservation options before treatment",
                    "Fertility is never affected by pubertal suppression",
                    "Sperm banking is impossible after any blockade",
                    "Fertility counseling can wait until age 25",
                ],
                0,
                "Informed consent must include fertility discussion before pubertal suppression or GAH—early blockade may compromise fertility if transition proceeds.",
                ref(
                    "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                    "It is essential that an informed consent process and a discussion about implications for fertility precede any treatment of TGD youth with pubertal suppression and/or GAH.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                "A 14-year-old on GnRH agonist alone for 18 months has declining lumbar spine BMD Z-scores. Best management emphasis?",
                [
                    "Ensure calcium/vitamin D (goal ≥30 ng/mL), weight-bearing exercise, and timely GAH initiation",
                    "Stop blockade and observe—bone loss is irreversible",
                    "High-dose prednisone",
                    "Bisphosphonates as mandatory first-line in all adolescents",
                ],
                0,
                "GnRH monotherapy lowers BMD; adequate nutrition, vitamin D, exercise, and transition to GAH address skeletal risk.",
                ref(
                    "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                    "Given previous study results, particularly during GnRH agonist treatment, it would seem important to ensure adequate intake of calcium and vitamin D, to encourage weight-bearing exercise, and to routinely monitor 25(OH)D levels, with a goal of maintaining levels of  $ \\geq $30 ng/mL.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Care of Transgender Adults",
                "A 28-year-old trans woman requests estrogen from her PCP; she has clear longstanding GD, stable support, and no acute psychiatric crisis. Per ES CPG, mental health letter requirement?",
                [
                    "Not required for adults—though referral may help if concerns exist",
                    "Two letters from psychiatrists are always mandatory",
                    "Mental health clearance required only for surgery, never hormones",
                    "Hormones are contraindicated without 2 years of psychotherapy",
                ],
                0,
                "ES CPG does not mandate mental health referral for adult hormone initiation when GD is clear, though referral helps with ambiguous cases.",
                ref(
                    "Care of Transgender Adults",
                    "It is not a requirement to have a mental health referral in adults as stated in the ES CPG",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Transfeminine Hormone Therapy",
                "A 35-year-old trans woman starts feminizing therapy. Which estrogen formulation should be avoided per current guidelines?",
                [
                    "Ethinyl estradiol",
                    "Oral 17β-estradiol",
                    "Transdermal estradiol patch",
                    "Parenteral estradiol valerate",
                ],
                0,
                "Ethinyl estradiol and conjugated estrogens are no longer recommended—unmonitorable levels and higher VTE/cardiovascular mortality risk.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "Studies have demonstrated that conjugated estrogens and synthetic estrogens are associated with increased risks of thromboembolism and thus are no longer recommended for use by the ES CPG.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Transfeminine Hormone Therapy",
                "A trans woman on estradiol 4 mg and spironolactone has estradiol 280 pg/mL and testosterone 80 ng/dL. Best adjustment?",
                [
                    "Reduce estradiol dose—target estradiol 100–200 pg/mL and testosterone <50 ng/dL",
                    "Increase estradiol to 8 mg daily",
                    "Stop spironolactone immediately",
                    "No change—supraphysiologic estradiol is preferred",
                ],
                0,
                "Box 24.4 targets estradiol 100–200 pg/mL and testosterone <50 ng/dL—supraphysiologic levels increase adverse-event risk.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "b. Serum estradiol should not exceed the peak physiologic range: 100–200 pg/mL.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Transfeminine Hormone Therapy",
                "A 45-year-old trans woman with obesity and smoking history starts feminizing hormones. Preferred estrogen route?",
                [
                    "Transdermal estradiol",
                    "Oral ethinyl estradiol",
                    "Conjugated equine estrogen",
                    "No estrogen—spironolactone alone",
                ],
                0,
                "Transdermal estrogen is preferred over age 40 and presumed less prothrombotic—especially relevant with additional VTE risk factors.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "Transdermal estrogen, presumed to be less stimulatory of prothrombotic proteins, is preferred in transgender women over the age of 40 due to the increased risk of thromboembolic disease.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Testosterone-Lowering Agents",
                "A trans woman in Europe is offered cyproterone 25 mg vs spironolactone 100 mg with estradiol 4 mg. Expected testosterone suppression?",
                [
                    "Cyproterone will lower testosterone more effectively",
                    "Spironolactone always achieves lower testosterone",
                    "Neither agent affects testosterone",
                    "GnRH agonists are contraindicated in all trans women",
                ],
                0,
                "RCT data show cyproterone acetate more effective than spironolactone for testosterone lowering when combined with estradiol.",
                ref(
                    "Testosterone-Lowering Agents",
                    "A randomized controlled trial of cyproterone acetate 25 mg daily versus spironolactone 100 mg daily, both in combination with estradiol 4 mg daily, found that cyproterone was more effective in lowering serum testosterone concentrations.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Testosterone-Lowering Agents",
                "A trans woman on spironolactone 200 mg daily develops mild hyperkalemia. Monitoring per ES Box 24.4?",
                [
                    "Serum electrolytes especially potassium every 3 months in year 1, then annually",
                    "No electrolyte monitoring needed with spironolactone",
                    "Daily ECG only—no labs",
                    "Discontinue estrogen instead of adjusting spironolactone",
                ],
                0,
                "Spironolactone requires potassium and electrolyte monitoring per transfeminine monitoring protocol.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "3. For individuals on spironolactone, serum electrolytes, particularly potassium, should be monitored every 3 months in the first year and annually thereafter.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Transmasculine Hormone Therapy",
                "A trans man prefers less frequent injections. Which regimen matches ES Table 24.3?",
                [
                    "Testosterone undecanoate 1000 mg IM every 12 weeks after loading doses",
                    "Testosterone propionate daily sublingual",
                    "Oral methyltestosterone twice daily",
                    "Estrogen patch 0.1 mg daily",
                ],
                0,
                "Testosterone undecanoate permits 12-week IM dosing after initial loading—listed in ES hormone therapy recommendations.",
                ref(
                    "Transmasculine Hormone Therapy",
                    "Testosterone undecanoate is a longer-acting testosterone that can be given by intramuscular injection every 12 weeks and is also well tolerated among transgender men, as reported by a prospective study of 17 transgender men in Europe.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Transmasculine Hormone Therapy",
                "A trans man on testosterone cypionate 100 mg weekly has trough testosterone 950 ng/dL and hematocrit 54%. Next step?",
                [
                    "Reduce dose or lengthen interval—maintain testosterone in range and hematocrit <55%",
                    "Add erythropoietin",
                    "Switch to estrogen therapy",
                    "No action—hematocrit is irrelevant on testosterone",
                ],
                0,
                "Target testosterone 400–700 ng/dL (mid-interval for injections) and keep hematocrit below 55%.",
                ref(
                    "Transmasculine Hormone Therapy",
                    "The ES CPG recommends maintaining hematocrit below 55% to avoid adverse events arising from increased red cell mass.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Potential Risks Associated With Transfeminine Hormone Therapy",
                "A trans woman planning vaginoplasty asks whether to stop estrogen 3 weeks pre-op. Per recent evidence, best advice?",
                [
                    "Continuing estrogen with adequate VTE prophylaxis may be safe—coordinate with surgeon",
                    "Must always stop estrogen 8 weeks before any surgery",
                    "No VTE prophylaxis is needed if estrogen is stopped",
                    "Switch to ethinyl estradiol perioperatively",
                ],
                0,
                "Kozato et al found no VTE increase when estrogen continued with standard prophylaxis—individualize with surgical team.",
                ref(
                    "Potential Risks Associated With Transfeminine Hormone Therapy",
                    "Therefore, transgender women who receive adequate VTE prophylaxis peri- and postoperatively using conventional therapies such as subcutaneous heparin and lower extremity compression devices may not need to discontinue estrogen therapy.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Potential Risks Associated With Transfeminine Hormone Therapy",
                "A trans woman on cyproterone and estradiol has prolactin 85 ng/mL. Most likely contributor?",
                [
                    "Cyproterone acetate rather than estradiol alone",
                    "Spironolactone is the usual prolactin stimulant",
                    "Testosterone excess",
                    "Prolactin elevation never occurs on feminizing therapy",
                ],
                0,
                "Hyperprolactinemia is largely cyproterone-driven; prolactin falls after cyproterone discontinuation post-orchiectomy.",
                ref(
                    "Potential Risks Associated With Transfeminine Hormone Therapy",
                    "However, in the majority of these cases, the transgender women were also taking the antiandrogen cyproterone acetate.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Potential Risks Associated With Transmasculine Hormone Therapy",
                "A trans man on testosterone has cervical tissue present. Cancer screening per ES CPG?",
                [
                    "Follow ACOG cervical screening guidelines for retained tissue",
                    "No screening ever if identifying as male",
                    "Annual orchiectomy is required",
                    "Mammography every 6 months",
                ],
                0,
                "Screen remaining reproductive tissues per standard guidelines—cervical screening per ACOG when cervix is present.",
                ref(
                    "Potential Risks Associated With Transmasculine Hormone Therapy",
                    "5. If cervical tissue is present, monitor as recommended by the American College of Obstetricians and Gynecologists.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "5α-Reductase Inhibitors",
                "A trans woman with androgenic alopecia requests finasteride as first-line antiandrogen. Best recommendation?",
                [
                    "Not first-line—spironolactone/cyproterone/GnRH preferred; finasteride only if insufficient response",
                    "Finasteride is mandatory for all trans women",
                    "Finasteride lowers serum testosterone substantially",
                    "Finasteride has no psychiatric risks",
                ],
                0,
                "5α-reductase inhibitors don't lower testosterone and may worsen depression—reserve for selected alopecia cases.",
                ref(
                    "5α-Reductase Inhibitors",
                    "5α-Reductase inhibitors, such as finasteride or dutasteride, have not been routinely recommended for use in transgender women because they do not lower serum concentrations of testosterone, and they have a higher cost.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Progestins",
                "A trans woman requests progesterone for breast development. Evidence-based response?",
                [
                    "Insufficient evidence to support routine progesterone—shared decision if trial desired",
                    "Progesterone is ES guideline-mandated",
                    "Progesterone is safer than estradiol for VTE",
                    "All trans women require medroxyprogesterone",
                ],
                0,
                "ES CPG does not recommend progesterone; high-quality data supporting breast enhancement are lacking.",
                ref(
                    "Progestins",
                    "The ES CPG does not make a recommendation for the use of progesterone as part of a gender-affirming hormone regimen.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Effects of Pubertal Suppression on Need for GAS and Effects on GAS",
                "A trans woman who started GnRH at Tanner 2 plans penile-inversion vaginoplasty. Surgical planning consideration?",
                [
                    "May need peritoneal or graft lining due to inadequate penoscrotal skin",
                    "Pubertal suppression guarantees abundant penile skin",
                    "Vaginoplasty is contraindicated after any blockade",
                    "No hair removal is needed before surgery",
                ],
                0,
                "Early pubertal suppression limits penoscrotal tissue—alternative lining techniques may be required.",
                ref(
                    "Effects of Pubertal Suppression on Need for GAS and Effects on GAS",
                    "Peritoneal lining and/or distant skin grafts can be used for individuals who have inadequate penoscrotal skin (e.g., treatment with pubertal suppression at an early stage of puberty, as discussed subsequently).",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Gender-Affirming Chest Surgery",
                "A trans feminine patient requests breast augmentation after 6 months of estrogen. Surgeon consultation advice?",
                [
                    "Minimum 1 year of hormonal supplementation typically required before augmentation",
                    "Breast augmentation should precede any hormone therapy",
                    "Estrogen is contraindicated before chest surgery",
                    "Implant dimensions are identical to cisgender women",
                ],
                0,
                "Without adequate estrogen exposure, augmentation is unlikely to yield aesthetic results—≥1 year of hormones is required.",
                ref(
                    "Gender-Affirming Chest Surgery",
                    "Without exogenous hormone supplementation, breast augmentation is unlikely to yield an aesthetic result, and a minimum of 1 year of hormonal supplementation is required before surgery.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Mental Health Considerations and Care of Transgender Youth",
                "A 17-year-old assigned female at birth presents post-pubertally with GD. Initial endocrine approach?",
                [
                    "Adult-style feminizing protocol; GnRH alone possible if deferring GAH",
                    "Must restart Tanner 2 blockade only",
                    "No medical options exist after puberty",
                    "Immediate surgical gonadectomy before any assessment",
                ],
                0,
                "Late-pubertal/postpubertal adolescents use adult protocols; GnRH without GAH is an option if uncertain about hormones.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "Some TGD adolescents first come to medical attention when they are already in the later stages of puberty or are postpubertal. These adolescents are treated using protocols like those used in TGD adults (see later discussion on hormone therapy in TGD adults).",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Outcomes of Current Treatment Models for TGD Youth and Potential Adverse Effects",
                "A clinic reviews mental health outcomes after adolescent GAH access. Best evidence summary?",
                [
                    "Improved depression, anxiety, appearance congruence, and life satisfaction",
                    "Universal treatment regret in longitudinal studies",
                    "No change in suicidal ideation with blockade or GAH",
                    "Only surgical patients benefit—hormones worsen mood",
                ],
                0,
                "Large observational data show psychosocial gains with gender-affirming medical care including blockade and GAH.",
                ref(
                    "Outcomes of Current Treatment Models for TGD Youth and Potential Adverse Effects",
                    "The largest observational study of TGD adolescents and young adults in the United States (n = 315, age 12–20 years) assessing the mental health impact of gender-affirming medical care demonstrated significant improvements in psychosocial functioning, with decreases in depression and anxiety and increases in appearance congruence (the degree to which physical characteristics align with gender identity), positive affect, and life satisfaction.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Care of Transgender Adults",
                "A trans man on testosterone cypionate asks about injection technique. Evidence-based preference?",
                [
                    "Subcutaneous weekly dosing is effective and often preferred",
                    "Subcutaneous testosterone is contraindicated",
                    "Only intramuscular gluteal injections are valid",
                    "Oral testosterone undecanoate once weekly is standard",
                ],
                0,
                "Retrospective data show trans men often prefer subcutaneous testosterone administration.",
                ref(
                    "Transmasculine Hormone Therapy",
                    "In a small retrospective study of 22 transgender men who received both intramuscular and subcutaneous testosterone at some point during their gender transition, all preferred testosterone administration subcutaneously.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Potential Risks Associated With Transfeminine Hormone Therapy",
                "A 50-year-old trans woman on estradiol asks about breast cancer screening. Appropriate guidance?",
                [
                    "Routine cancer screening of all present tissues as in nontransgender individuals",
                    "No screening ever because breast cancer does not occur",
                    "Bilateral mastectomy obviates all screening in every patient",
                    "Screen only if on cyproterone",
                ],
                0,
                "Box 24.4 recommends routine cancer screening for all present tissues per standard nontransgender protocols.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "4. Routine cancer screening is recommended, as in nontransgender individuals (all tissues present).",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Mental Health Considerations and Care of Transgender Youth",
                "An adolescent with GD and autism spectrum disorder seeks hormones. Best practice?",
                [
                    "Ongoing mental health/gender specialist support; ASD co-occurrence is common",
                    "Autism is an absolute contraindication to all GAH",
                    "No mental health input is ever needed if ASD is present",
                    "Start surgery before any hormone discussion",
                ],
                0,
                "Gender incongruence associates with ASD—ongoing mental health/gender specialist support is recommended throughout care.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "There is an association between gender incongruence and autism spectrum disorder.",
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
                "Youth eligible for hormone therapy should undergo comprehensive biopsychosocial assessment by a qualified mental health/gender specialist before medical transition.",
                True,
                "KEY POINTS mandate specialist assessment before medical/surgical transition-related care.",
                ref(
                    "KEY POINTS",
                    "Youth with a gender identity that is not aligned with their sex designated at birth seeking medical/surgical transition-related care should undergo a comprehensive biopsychosocial assessment by a qualified mental health/gender specialist.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Prevalence",
                "U.S. population surveys estimate approximately 1.4% of youth ages 13–17 identify as transgender.",
                True,
                "Williams Institute 2022 data cite 1.4% transgender youth prevalence.",
                ref(
                    "Prevalence",
                    "Based on state-level population-based surveys, a 2022 report from the Williams Institute of the University of California-Los Angeles School of Law indicated that 0.5% of U.S. adults and 1.4% of youth age 13 to 17 years identify as transgender.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Mental Health Considerations and Care of Transgender Youth",
                "GnRH agonist pubertal suppression is considered a fully reversible treatment in appropriate TGD adolescents.",
                True,
                "GnRH agonists pause puberty reversibly, allowing exploration and preventing undesired irreversible changes.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "Considered fully reversible treatments, GnRH agonists, by pausing puberty in this clinical setting, provide additional time for gender identity exploration without the pressure of continued pubertal progression and prevent irreversible development of secondary sex characteristics associated with a puberty that is not aligned with the person's gender identity.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Mental Health Considerations and Care of Transgender Youth",
                "Lack of availability of certain multidisciplinary team members should always preclude timely initiation of medically necessary gender-affirming care.",
                False,
                "ES/WPATH recommend multidisciplinary care but state discipline unavailability should not block timely necessary treatment.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "Although the involvement of relevant disciplines throughout this entire process is recommended, a lack of availability to certain disciplines should not preclude timely initiation of medically necessary care.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                "There are robust data confirming GnRH agonist monotherapy past age 14 without risk to skeletal health.",
                False,
                "No data currently inform safe GnRH monotherapy past age 14 without significant skeletal health risks.",
                ref(
                    "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                    "It is important to note that there currently are no data to inform whether GnRH agonist use can be administered as monotherapy past age 14 years without posing significant risks to skeletal health.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Transfeminine Hormone Therapy",
                "Conjugated and synthetic estrogens remain first-line for transfeminine hormone therapy per the Endocrine Society.",
                False,
                "ES CPG no longer recommends conjugated or synthetic estrogens because of thromboembolism risk and unmonitorable levels.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "Studies have demonstrated that conjugated estrogens and synthetic estrogens are associated with increased risks of thromboembolism and thus are no longer recommended for use by the ES CPG.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Potential Risks Associated With Transfeminine Hormone Therapy",
                "UK case-control data suggest transdermal estrogen carries lower VTE risk than oral estrogen preparations.",
                True,
                "Vinogradova et al found lower thromboembolism risk with transdermal vs oral estrogen in women.",
                ref(
                    "Potential Risks Associated With Transfeminine Hormone Therapy",
                    "However, a recent case-control study conducted in the UK of women with a diagnosis of venous thromboembolism matched to women without a thromboembolism found that transdermal estrogen preparations are associated with a lower risk of thromboembolism compared to oral estrogen preparations.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Potential Risks Associated With Transfeminine Hormone Therapy",
                "Adequate estrogen therapy is protective against bone loss in transgender women.",
                True,
                "Multiple studies show GAH increases BMD at spine and hip when estrogen is adequate.",
                ref(
                    "Potential Risks Associated With Transfeminine Hormone Therapy",
                    "Adequate estrogen therapy is protective against bone loss in transgender women.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Potential Risks Associated With Transmasculine Hormone Therapy",
                "The Endocrine Society recommends maintaining hematocrit below 55% in transmasculine patients on testosterone.",
                True,
                "Hematocrit threshold of 55% is the ES recommendation to limit polycythemia complications.",
                ref(
                    "Potential Risks Associated With Transmasculine Hormone Therapy",
                    "The ES CPG recommends maintaining hematocrit below 55% to avoid adverse events arising from increased red cell mass.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Potential Risks Associated With Transfeminine Hormone Therapy",
                "Routine liver enzyme monitoring remains mandatory for all transgender women on estrogen per the 2017 ES update.",
                False,
                "Routine ALT/AST monitoring was removed after studies showed mostly transient, non-clinically meaningful changes.",
                ref(
                    "Potential Risks Associated With Transfeminine Hormone Therapy",
                    "Thus, the recommendation for routine monitoring of liver enzymes was removed in the 2017 guidelines update.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Outcomes of Current Treatment Models for TGD Youth and Potential Adverse Effects",
                "Dutch longitudinal data report treatment regret among adolescents completing pubertal suppression, GAH, and surgery.",
                False,
                "de Vries et al reported none of the participants regretted treatment after the three-stage approach.",
                ref(
                    "Outcomes of Current Treatment Models for TGD Youth and Potential Adverse Effects",
                    "none of the study participants regretted treatment.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Effects of Pubertal Suppression on Need for GAS and Effects on GAS",
                "Early pubertal suppression in assigned females at birth can prevent breast development and reduce need for later mastectomy.",
                True,
                "GnRH blockade before glandular breast development may obviate future chest masculinization surgery.",
                ref(
                    "Effects of Pubertal Suppression on Need for GAS and Effects on GAS",
                    "In individuals assigned female at birth, pubertal suppression can prevent development of glandular breast tissue and thus the need for gender-affirming mastectomy later in life.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Care of Transgender Adults",
                "Gender-affirming hormone therapy under medical supervision carries low adverse-event risk when hormone levels remain physiologic.",
                True,
                "Supervised titration to physiologic ranges keeps risks low though monitoring continues.",
                ref(
                    "Care of Transgender Adults",
                    "In general, when hormone therapy is taken under medical supervision, the risks of adverse events are low, likely due to the careful attention not to exceed supraphysiologic concentrations.",
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
                "Assertion: Youth eligible for hormones should start GnRH agonists at Tanner stage 2.",
                "Reason: GnRH agonists permanently destroy pituitary gonadotropes within 48 hours.",
                2,
                "Assertion true; reason false—GnRH agonists reversibly pause puberty and are considered fully reversible in this setting.",
                ref(
                    "KEY POINTS",
                    "Youth deemed eligible to initiate hormone therapy generally start with gonadotropin-releasing hormone agonists at Tanner stage 2 to halt further pubertal progression, and at the appropriate time, they start gender-affirming hormone therapy that is aligned with the affirmed gender.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Mental Health Considerations and Care of Transgender Youth",
                "Assertion: TGD youth have increased rates of anxiety, depression, and suicidal ideation.",
                "Reason: These mental health burdens are intrinsic biological consequences of being transgender.",
                2,
                "Assertion true; reason false—studies support that lack of societal acceptance drives much of the psychiatric morbidity.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "Such studies support the concept that many of the mental health challenges faced by TGD youth are not intrinsic to being transgender but rather are largely a consequence of lack of societal acceptance.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Mental Health Considerations and Care of Transgender Youth",
                "Assertion: WPATH standards of care inform gender-affirming medical treatment of TGD youth.",
                "Reason: WPATH SOCs prohibit any use of pubertal suppression in adolescents.",
                2,
                "Assertion true; reason false—WPATH and ES endorse pubertal suppression at Tanner 2 when criteria are met.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "The ES CPG and WPATH SOCs endorse the use of pubertal suppression in TGD adolescents who meet the criteria for GD using gonadotropin-releasing hormone (GnRH) agonists at Tanner stage 2 of pubertal development (testicular volume  $ \\geq $4 mL for assigned males at birth; initial stage of breast budding for assigned females at birth).",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Mental Health Considerations and Care of Transgender Youth",
                "Assertion: Transmasculine adolescents on testosterone can typically discontinue GnRH agonist once adult testosterone levels are reached.",
                "Reason: Testosterone at physiologic doses always suppresses endogenous gonadotropins from the first injection.",
                2,
                "Assertion true; reason false—initial testosterone doses may be insufficient to suppress endogenous hormones; GnRH stop is appropriate once adult levels achieved.",
                ref(
                    "Mental Health Considerations and Care of Transgender Youth",
                    "In individuals designated female at birth and treated with testosterone, GnRH analog treatment can typically be discontinued once adult testosterone levels have been reached.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Transfeminine Hormone Therapy",
                "Assertion: 17β-estradiol is preferred over ethinyl estradiol for transfeminine therapy.",
                "Reason: Ethinyl estradiol serum levels can be reliably monitored to avoid supraphysiologic exposure.",
                2,
                "Assertion true; reason false—synthetic/conjugated estrogens cannot be monitored in blood and ethinyl estradiol increases VTE risk.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "Another issue with conjugated estrogens and synthetic estrogens is the inability of physicians to measure these drugs in blood and/or estimate equivalent estradiol levels, which impairs efforts to avoid supraphysiologic exposure to estrogen.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Transfeminine Hormone Therapy",
                "Assertion: Serum estradiol should be maintained at 100–200 pg/mL in transfeminine patients.",
                "Reason: Supraphysiologic estradiol levels are recommended to accelerate feminization.",
                2,
                "Assertion true; reason false—exceeding peak physiologic estradiol increases adverse events; careful titration avoids supraphysiologic concentrations.",
                ref(
                    "Transfeminine Hormone Therapy",
                    "b. Serum estradiol should not exceed the peak physiologic range: 100–200 pg/mL.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Potential Risks Associated With Transfeminine Hormone Therapy",
                "Assertion: Thromboembolism is the most serious well-studied complication of transfeminine hormone therapy.",
                "Reason: Estrogen therapy has no effect on prothrombotic factors.",
                2,
                "Assertion true; reason false—estrogen promotes prothrombotic factors contributing to VTE risk.",
                ref(
                    "Potential Risks Associated With Transfeminine Hormone Therapy",
                    "Estrogen is likely the cause for the increased incidence of thromboembolism, given its known mechanism for promoting prothrombotic factors and evidence from clinical trials of cisgender women on estrogen therapy.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Potential Risks Associated With Transmasculine Hormone Therapy",
                "Assertion: Testosterone therapy in trans men commonly raises hemoglobin and hematocrit.",
                "Reason: Testosterone suppresses erythropoietin production.",
                2,
                "Assertion true; reason false—testosterone stimulates erythropoietin and increases red cell mass.",
                ref(
                    "Potential Risks Associated With Transmasculine Hormone Therapy",
                    "GAH therapy with testosterone in transgender men is commonly associated with increases in red blood cell mass and hematocrit due to stimulation of erythropoietin.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                "Assertion: GnRH agonist therapy in TGD adolescents decreases BMD Z-scores.",
                "Reason: GnRH agonists directly stimulate osteoblast activity and increase bone formation.",
                2,
                "Assertion true; reason false—pubertal suppression without sex steroids compromises bone mineral accrual.",
                ref(
                    "Potential Adverse Effects of Gender-Affirming Medical Care in Transgender Youth",
                    "Treatment with GnRH agonist therapy in TGD adolescents is associated with significant decreases in BMD Z-scores.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Effects of Pubertal Suppression on Need for GAS and Effects on GAS",
                "Assertion: Early pubertal suppression in assigned males at birth may reduce need for facial feminization surgery.",
                "Reason: Testosterone exposure during puberty has no effect on facial bone structure.",
                2,
                "Assertion true; reason false—pubertal testosterone drives masculine facial features that early blockade can prevent.",
                ref(
                    "Effects of Pubertal Suppression on Need for GAS and Effects on GAS",
                    "This can be particularly valuable for individuals assigned male at birth who, with pubertal suppression, forgo the effects that testosterone has on facial features, minimizing or preventing the desire for gender-affirming facial surgery in the future.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Testosterone-Lowering Agents",
                "Assertion: Cyproterone acetate lowers testosterone more effectively than spironolactone when combined with estradiol.",
                "Reason: Spironolactone is a pure GnRH agonist that abolishes all adrenal androgen production.",
                2,
                "Assertion true; reason false—spironolactone acts via androgen receptor antagonism and altered testosterone metabolism, not as a GnRH agonist.",
                ref(
                    "Testosterone-Lowering Agents",
                    "A randomized controlled trial of cyproterone acetate 25 mg daily versus spironolactone 100 mg daily, both in combination with estradiol 4 mg daily, found that cyproterone was more effective in lowering serum testosterone concentrations.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Care of Transgender Adults",
                "Assertion: Adults with TGD identity can receive hormone therapy without mandatory mental health referral per ES CPG.",
                "Reason: The ES CPG requires two psychiatric evaluations before any adult can start hormones.",
                2,
                "Assertion true; reason false—mental health referral is not required in adults though it may be helpful when GD severity is unclear.",
                ref(
                    "Care of Transgender Adults",
                    "It is not a requirement to have a mental health referral in adults as stated in the ES CPG",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "24",
        "title": "Transgender Endocrinology",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Abby Walch, Stephen M. Rosenthal, Jens U. Berli, and Vin Tangpricha",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_24_Transgender_Endocrinology.md",
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
