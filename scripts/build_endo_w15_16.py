#!/usr/bin/env python3
"""Generate Williams 15e module w15-16 — Hormonal Contraception."""
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
OUT_NAME = "w15-16_Hormonal_Contraception.json"


def build() -> dict:
    p = "w15-16"
    items: list[dict] = []

    # --- Notes (26; ≥15 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "KEY POINTS",
                "Reducing barriers to contraceptive initiation and continuation lowers unintended pregnancy; LARC methods offer sterilization-level efficacy; emergency contraception should be accessible; LNG-IUD treats heavy menstrual bleeding; USMEC guides patients with comorbidities.",
                ref(
                    "KEY POINTS",
                    "Long-acting reversible contraceptive methods, which include the copper intrauterine device (IUD), the levonorgestrel IUD, and the etonogestrel subdermal implant, provide superior contraceptive effectiveness, equivalent to sterilization, and higher continuation and satisfaction rates compared with shorter-acting methods.",
                ),
            ),
            note(
                f"{p}-n2",
                "Choosing a Contraceptive Method",
                "How to tier counsel contraceptive methods",
                "Present all suitable options using tiers of effectiveness—LARC and sterilization (tier 1), combined methods/DMPA/POP (tier 2), barriers (tier 3)—while honoring patient preferences, affordability, and noncontraceptive benefits through shared decision making.",
                ref(
                    "Choosing a Contraceptive Method",
                    "When discussing contraception, clinicians should present all suitable options to their patients but can opt to outline the options in terms of tiers of effectiveness (Fig. 16.1).",
                ),
            ),
            note(
                f"{p}-n3",
                "The Combined Oral Contraceptive Pill",
                "Combined oral contraceptive counseling essentials",
                "COCs are safe, reversible, and highly effective with consistent use; counseling must cover correct daily use, missed-pill instructions, side effects in context of pregnancy risk, and noncontraceptive benefits to maximize adherence.",
                ref(
                    "The Combined Oral Contraceptive Pill",
                    "Combined oral contraceptives (COCs) offer safe, reversible, and convenient birth control that is highly effective for those who take pills correctly and consistently.",
                ),
            ),
            note(
                f"{p}-n4",
                "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                "How COCs suppress ovulation",
                "Estrogen and progestin suppress hypothalamic-pituitary-gonadal axis FSH/LH, blocking folliculogenesis and ovulation; progestin additionally thickens cervical mucus, causes endometrial atrophy, and impairs tubal cilia—failure rates rise sharply with poor adherence.",
                ref(
                    "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                    "Estrogen and progestin components of COCs contribute to inhibition of ovulation through suppression of the hypothalamic-pituitary-gonadal axis.",
                ),
            ),
            note(
                f"{p}-n5",
                "Composition and Formulations",
                "COC estrogen and progestin formulations",
                "Contraceptive COCs contain ≤35 µg ethinyl estradiol with legacy or newer progestins (norgestimate, desogestrel, drospirenone, dienogest); newer estrogens (estradiol valerate, estetrol) may carry less cardiovascular risk but data remain limited.",
                ref(
                    "Composition and Formulations",
                    "For contraceptive use, COCs contain 35 μg or less of estrogen.",
                ),
            ),
            note(
                f"{p}-n6",
                "Noncontraceptive Health Benefits",
                "Why COCs reduce gynecologic cancer risk",
                "COC use lowers epithelial ovarian and endometrial cancer risk substantially and persistently after discontinuation; benefits must be weighed against possible breast cancer signal, especially in BRCA carriers.",
                ref(
                    "Noncontraceptive Health Benefits",
                    "COC use of more than 10 years appeared to reduce the incidence of ovarian cancer by over 50%.",
                ),
            ),
            note(
                f"{p}-n7",
                "Side Effects",
                "Unscheduled bleeding on COCs",
                "Breakthrough bleeding affects 30–50% in the first 3 months, more with 20 µg EE; persistent bleeding warrants pregnancy and structural evaluation; extended regimens may improve dysmenorrhea but need anticipatory counseling.",
                ref(
                    "Side Effects",
                    "Unscheduled vaginal bleeding is a common side effect attributable to COC.",
                ),
            ),
            note(
                f"{p}-n8",
                "Health Risks",
                "USMEC eligibility categories",
                "CDC USMEC rates methods 1 (no restriction) through 4 (unacceptable risk); category 4 for estrogen methods includes prior VTE, stroke, migraine with aura, and smoking ≥15 cigarettes/day at age ≥35.",
                ref(
                    "Health Risks",
                    "Conditions that present an unacceptable health risk if the contraceptive method is used; examples for estrogen-containing methods include delivery during the past 21 days, a personal history of deep venous thrombosis or pulmonary embolism, ischemic heart disease, stroke, known thrombogenic mutations, and migraine headaches with aura or other neurologic signs.",
                ),
            ),
            note(
                f"{p}-n9",
                "Thromboembolic Disease",
                "Why VTE risk is estrogen-related",
                "COCs more than double VTE incidence (~9–10 per 10,000 woman-years vs 1–5 baseline); risk is lower with modern ≤35 µg EE but remains elevated; pregnancy and postpartum carry even higher absolute risk.",
                ref(
                    "Thromboembolic Disease",
                    "In general, COC use increases risk of VTE by more than twofold with an incidence of approximately 9 to 10 per 10,000 women per treatment year (Fig. 16.2).",
                ),
            ),
            note(
                f"{p}-n10",
                "Side Effects",
                "Why migraine with aura contraindicates COCs",
                "Migraine with aura is USMEC category 4 for estrogen-containing contraception because of increased stroke risk; new or worsening headache on COCs mandates discontinuation and evaluation.",
                ref(
                    "Side Effects",
                    "A history of migraine with aura is a contraindication for use of COC because of increased risk of stroke (described in the next section).",
                ),
            ),
            note(
                f"{p}-n11",
                "Use of Concomitant Medications With Combined Oral Contraceptive Pills",
                "How enzyme inducers reduce COC efficacy",
                "P450-inducing anticonvulsants, rifamycins, and some antiretrovirals lower hormonal contraceptive levels; use ≥30 µg EE with backup condoms or prefer DMPA/LNG-IUD when enzyme inducers are required.",
                ref(
                    "Use of Concomitant Medications With Combined Oral Contraceptive Pills",
                    "Certain anticonvulsants (phenytoin, carbamazepine, barbiturates, primidone, topiramate, and oxcarbazepine) that induce hepatic cytochrome P450 enzymes may reduce contraceptive efficacy of COCs.",
                ),
            ),
            note(
                f"{p}-n12",
                "Transdermal Contraceptive Patch",
                "Transdermal patch counseling pitfalls",
                "Patches deliver combined EE/progestin without daily pills but generate higher circulating EE than pills or rings; FDA black-box warnings restrict patch use at BMI ≥30 kg/m² because of VTE cases in approval trials.",
                ref(
                    "The Contraceptive Transdermal Patch and Vaginal Ring",
                    "Nevertheless, based on data from the approval trials for the EE/LNG patch, the U.S. Food and Drug Administration (FDA) added a black box warning to both patches to state that women with a BMI of 30 kg/m² or more should not use the patch because of the higher risk of VTE.",
                ),
            ),
            note(
                f"{p}-n13",
                "Contraceptive Vaginal Ring",
                "Contraceptive vaginal ring essentials",
                "EE/etonogestrel and EE/segesterone rings provide combined contraception with lower EE exposure than pills; rings stay in the upper vagina for 21 days with 7-day withdrawal; brief removal (<48 h) does not impair efficacy.",
                ref(
                    "Contraceptive Vaginal Ring",
                    "The ring does not require individual fitting; as long as it remains in the vagina, appropriate absorption of steroids occurs.",
                ),
            ),
            note(
                f"{p}-n14",
                "Progestin-Only Contraceptive Methods",
                "How progestin-only methods avoid estrogen risks",
                "POP, DMPA, implant, and LNG-IUD have fewer contraindications than estrogen methods and are appropriate after delivery, with VTE history, smoking age ≥35, hypertension, or long-standing diabetes.",
                ref(
                    "Progestin-Only Contraceptive Methods",
                    "Progestin-only contraceptives may be appropriate for many patients with contraindications to contraceptive doses of estrogen, including those at elevated baseline risk for VTE, those age 35 or older who smoke, and those with hypertension or who have long-standing diabetes.",
                ),
            ),
            note(
                f"{p}-n15",
                "Progestin-Only Oral Contraceptive Pill",
                "Why norethindrone POP requires strict timing",
                "Norethindrone 0.35 mg has a short half-life—levels fall within 24 hours and a dose is missed if >3 hours late; strict daily timing is essential because ovulation is not consistently suppressed.",
                ref(
                    "Progestin-Only Oral Contraceptive Pill",
                    "Because of the short half-life of POPs, serum steroid levels decline to near baseline as quickly as 24 hours after administration, and a dose is considered missed if it has been more than 3 hours beyond an expected dose.",
                ),
            ),
            note(
                f"{p}-n16",
                "Mechanism of Action",
                "Progestin-only pill mechanisms",
                "Norethindrone POP relies on cervical mucus thickening and endometrial atrophy when ovulation is not fully suppressed; drospirenone and desogestrel POPs reliably inhibit ovulation with better efficacy.",
                ref(
                    "Mechanism of Action",
                    "Unlike with COCs, ovulation is not consistently suppressed with the 0.35-mg norethindrone POP, and the progestin effects on cervical mucus and the endometrium are critical factors in preventing conception.",
                ),
            ),
            note(
                f"{p}-n17",
                "Formulations and Pharmacology",
                "DMPA mechanism and administration",
                "DMPA (150 mg IM or 104 mg SC every 13 weeks) inhibits follicular maturation and ovulation via gonadotropin suppression, with endometrial atrophy and hostile cervical mucus; obesity and enzyme inducers do not reduce efficacy.",
                ref(
                    "Formulations and Pharmacology",
                    "DMPA primarily acts by inhibiting follicular maturation and ovulation through inhibition of gonadotropin secretion.",
                ),
            ),
            note(
                f"{p}-n18",
                "Risks and Benefits of Depot Medroxyprogesterone Acetate",
                "How DMPA treats heavy menstrual bleeding",
                "DMPA-induced amenorrhea makes it ideal for heavy menstrual bleeding, dysmenorrhea, and iron deficiency anemia; 50% amenorrheic at 1 year and 75% with long-term use.",
                ref(
                    "Risks and Benefits of Depot Medroxyprogesterone Acetate",
                    "The tendency of DMPA to cause amenorrhea makes it a particularly appropriate contraceptive choice for patients with heavy menstrual bleeding, dysmenorrhea, or iron deficiency anemia.",
                ),
            ),
            note(
                f"{p}-n19",
                "Progestin-Releasing Intrauterine Devices",
                "Why LNG-IUD is tier-1 contraception",
                "LNG-IUDs provide highly effective local progestin with minimal systemic levels; 52-mg devices are approved up to 8 years, treat heavy bleeding, and suit adolescents and nulliparous patients with rapid fertility return after removal.",
                ref(
                    "Progestin-Releasing Intrauterine Devices",
                    "Levonorgestrel-releasing IUDs provide highly effective, safe, convenient, and reversible contraception.",
                ),
            ),
            note(
                f"{p}-n20",
                "Expanding the Use of Intrauterine Devices",
                "How CHOICE data support LARC uptake",
                "When cost barriers are removed and counseling standardized, 68% choose LARC with high continuation and markedly lower unintended pregnancy, abortion, and repeat abortion rates—including in adolescents.",
                ref(
                    "Expanding the Use of Intrauterine Devices",
                    "This project has shown that with standardized counseling and no financial barriers to contraceptive acquisition, the majority of participants (68%) will choose long-acting reversible contraceptive methods (45% levonorgestrel IUD, 10% copper IUD, and 13% etonogestrel implant).",
                ),
            ),
            note(
                f"{p}-n21",
                "Abnormal Bleeding, Expulsion, and Uterine Perforation",
                "How to counsel expected LNG-IUD bleeding",
                "Unpredictable bleeding is the leading discontinuation reason; by 12 months up to 50% have amenorrhea or infrequent bleeding with 52-mg devices—specific preplacement counseling improves acceptability.",
                ref(
                    "Abnormal Bleeding, Expulsion, and Uterine Perforation",
                    "As with DMPA and other progestin-only contraceptives, unpredictable uterine bleeding is the most common reason for discontinuation of LNG-IUDs.",
                ),
            ),
            note(
                f"{p}-n22",
                "Contraceptive Implants",
                "Nexplanon efficacy and extended use",
                "Etonogestrel 68-mg implant provides near-sterilization efficacy for 3 labeled years with data supporting off-label use to 5 years; most failures reflect unrecognized pregnancy or noninsertion.",
                ref(
                    "Contraceptive Implants",
                    "Although package labeling indicates Nexplanon can be used for up to 3 years, the implant appears to retain its efficacy for up to 5 years.",
                ),
            ),
            note(
                f"{p}-n23",
                "Emergency Contraception",
                "Emergency contraception access",
                "EC prevents pregnancy after unprotected intercourse or method failure up to 5 days later; advance provision improves use but regular ongoing contraception remains more effective at reducing unintended pregnancy.",
                ref(
                    "Emergency Contraception",
                    "EC can reduce the risk of unintended pregnancy up to 5 days after unprotected sex.",
                ),
            ),
            note(
                f"{p}-n24",
                "Mechanism of Action",
                "How levonorgestrel EC prevents ovulation",
                "Levonorgestrel EC prevents or delays ovulation only if taken before the LH surge; it does not impair implantation and is not an abortifacient; efficacy wanes if delayed after intercourse.",
                ref(
                    "Mechanism of Action",
                    "Levonorgestrel EC prevents or delays ovulation if administered before the commencement of the LH surge and is ineffective if taken afterward.",
                ),
            ),
            note(
                f"{p}-n25",
                "Efficacy",
                "Why copper IUD is the most effective EC",
                "Copper IUD failure rate for EC is <0.1%; LNG-IUD is non-inferior; both provide ongoing contraception and are unaffected by BMI unlike oral agents.",
                ref(
                    "Efficacy",
                    "The most effective EC is the copper IUD, with a failure rate of <0.1%.",
                ),
            ),
            note(
                f"{p}-n26",
                "Hormonal Contraception for Adolescents",
                "Why LARC suits adolescents",
                "Adolescents have high fertility and inconsistent short-acting method use; IUDs and implants should be offered with proper counseling—pelvic exam is not required to initiate hormonal contraception.",
                ref(
                    "Hormonal Contraception for Adolescents",
                    "These methods, including the DMPA injection, contraceptive implants, and IUDs, should be made available to teens.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Choosing a Contraceptive Method",
                "A 24-year-old desires the most effective reversible contraception and can return for placement. After shared decision making, best recommendation?",
                [
                    "Levonorgestrel IUD or etonogestrel implant (LARC tier 1)",
                    "Combined oral contraceptive as first-line because LARC is only for parous women",
                    "Withdrawal method with spermicide",
                    "Depot medroxyprogesterone acetate only—LARC is contraindicated under age 25",
                ],
                0,
                "LARC offers sterilization-level efficacy with high continuation; CHOICE data show most patients choose LARC when barriers are removed.",
                ref(
                    "Choosing a Contraceptive Method",
                    "Long-acting reversible contraceptives (i.e., IUDs and the implant) offer patients the advantages of high contraceptive efficacy and high rates of continuation.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                "A 19-year-old on combined OCPs misses two pills in week 3 of a 28-day pack. Best counseling per CDC Selected Practice Recommendations?",
                [
                    "Take the most recent missed pill, continue daily pills, use condoms 7 days, omit HFI and start new pack; consider EC",
                    "Stop pills for 7 days then restart—no backup needed",
                    "Take only placebo pills until next menses",
                    "Switch to POP without backup because estrogen was already absorbed",
                ],
                0,
                "Two or more missed pills require backup for 7 days; week-3 misses warrant skipping the hormone-free interval; EC may be considered.",
                ref(
                    "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                    "If two or more pills were missed in the third week of the 28-day pack, they can omit the HFI in the current pack and start a new pack.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Health Risks",
                "A 37-year-old smoker (20 cigarettes/day) requests combined OCPs. USMEC category for estrogen-containing contraception?",
                [
                    "Category 4—unacceptable risk",
                    "Category 1—no restriction",
                    "Category 2—advantages generally outweigh risks",
                    "Category 3 only if BMI <25",
                ],
                0,
                "Smoking ≥15 cigarettes/day at age ≥35 is unacceptable risk (category 4) for estrogen-containing methods.",
                ref(
                    "Thromboembolic Disease",
                    "The absolute risk of myocardial infarction and stroke increases with age.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Side Effects",
                "A 28-year-old on COCs reports new migraine with visual aura. Next step?",
                [
                    "Discontinue estrogen-containing contraception immediately",
                    "Increase ethinyl estradiol dose to stabilize migraines",
                    "Continue COC and add triptan prophylaxis",
                    "Switch to transdermal patch because nonoral route is safer with aura",
                ],
                0,
                "Migraine with aura is category 4 for all estrogen-containing methods including patch and ring; discontinue and switch to progestin-only/LARC.",
                ref(
                    "Side Effects",
                    "Similarly, any COC users who experience increased frequency or intensity of any type of migraine headache should discontinue estrogen-containing contraceptives.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Thromboembolic Disease",
                "A 26-year-old with prior pulmonary embolism (off anticoagulation 6 months) wants contraception. Safest option?",
                [
                    "Levonorgestrel IUD or etonogestrel implant",
                    "Combined OCP with 20 µg ethinyl estradiol",
                    "Contraceptive patch",
                    "Ethinyl estradiol vaginal ring",
                ],
                0,
                "Personal history of VTE is category 4 for estrogen methods; progestin-only and IUD methods are preferred per USMEC Table 16.3.",
                ref(
                    "Health Risks",
                    "Conditions that present an unacceptable health risk if the contraceptive method is used; examples for estrogen-containing methods include delivery during the past 21 days, a personal history of deep venous thrombosis or pulmonary embolism, ischemic heart disease, stroke, known thrombogenic mutations, and migraine headaches with aura or other neurologic signs.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Use of Concomitant Medications With Combined Oral Contraceptive Pills",
                "A woman with epilepsy on carbamazepine needs contraception. Best approach?",
                [
                    "LNG-IUD or DMPA; if COC used, ≥30 µg EE plus condoms",
                    "Any COC dose—carbamazepine does not affect hormones",
                    "Copper IUD is contraindicated with anticonvulsants",
                    "Etonogestrel implant without concern for enzyme induction",
                ],
                0,
                "Enzyme inducers reduce COC efficacy; high-dose progestin methods or IUDs are preferable; implants are not recommended with anticonvulsants.",
                ref(
                    "Use of Concomitant Medications With Combined Oral Contraceptive Pills",
                    "Alternatively, high-dose progestin-only methods such as DMPA or intrauterine contraceptives may be preferable because their efficacy is not reduced by medications that induce liver enzymes.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "The Contraceptive Transdermal Patch and Vaginal Ring",
                "A 32-year-old with BMI 34 kg/m² wants combined hormonal contraception without daily pills. Best counseling?",
                [
                    "Avoid contraceptive patch; consider vaginal ring or progestin-only/LARC methods",
                    "EE/LNG patch is preferred in obesity because absorption is dermal",
                    "Patch and ring have no VTE concerns at any BMI",
                    "Only copper IUD is allowed when BMI >30",
                ],
                0,
                "FDA black-box warning contraindicates patch use at BMI ≥30; rings share estrogen VTE risk but lack the same obesity restriction—individualize.",
                ref(
                    "The Contraceptive Transdermal Patch and Vaginal Ring",
                    "Nevertheless, based on data from the approval trials for the EE/LNG patch, the U.S. Food and Drug Administration (FDA) added a black box warning to both patches to state that women with a BMI of 30 kg/m² or more should not use the patch because of the higher risk of VTE.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Progestin-Only Oral Contraceptive Pill",
                "A breastfeeding 6-week postpartum patient with hypertension needs contraception. Best choice?",
                [
                    "Progestin-only pill, DMPA, implant, or IUD—estrogen deferred per USMEC early postpartum",
                    "Combined OCP started immediately—no postpartum restrictions",
                    "No hormonal method until 12 months postpartum",
                    "Combined patch because transdermal estrogen is safe postpartum",
                ],
                0,
                "Progestin-only methods can start immediately postpartum; estrogen-containing methods are category 4 until 3 weeks (4 weeks if breastfeeding).",
                ref(
                    "Progestin-Only Contraceptive Methods",
                    "In addition, they can be used immediately after delivery, whether or not the patient is breastfeeding.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Progestin-Only Oral Contraceptive Pill",
                "A 35-year-old on norethindrone POP forgets a dose by 5 hours. Management?",
                [
                    "Take pill now, continue daily, use condoms at least 2 days",
                    "No action—window is 12 hours for all POPs",
                    "Take two pills daily for a week without backup",
                    "Stop POP and start combined OCP next day",
                ],
                0,
                "Norethindrone POP doses are missed if >3 hours late; backup contraception for ≥2 days is required.",
                ref(
                    "Starting the Progestin-Only Pill",
                    "A backup contraceptive (e.g., condoms) should be used for at least 2 days if the progestin-only oral contraceptive is taken more than 3 hours late or forgotten on any day.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Risks and Benefits of Depot Medroxyprogesterone Acetate",
                "A 16-year-old with heavy menstrual bleeding and anemia desires long-acting contraception. Appropriate option?",
                [
                    "DMPA or LNG-IUD after counseling on bleeding patterns and BMD",
                    "Combined OCP contraindicated in all adolescents",
                    "DMPA permanently impairs fertility—avoid in teens",
                    "Copper IUD only—progestin methods forbidden under age 18",
                ],
                0,
                "DMPA and LNG-IUD treat heavy bleeding; adolescent medicine supports DMPA when pregnancy prevention benefits outweigh BMD concerns.",
                ref(
                    "Injectable Contraceptives in Adolescents",
                    "Although loss of bone density has been a concern in adolescents using DMPA, the position statement of the Society for Adolescent Medicine is that DMPA represents an extremely effective contraceptive and that clinical concerns about loss of BMD must be placed within the context of likely bone recovery on discontinuation, low risk of fractures, and benefits of preventing unintended pregnancy among adolescents.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Administration of Depot Medroxyprogesterone Acetate",
                "A DMPA user is 16 weeks since last injection. Next step?",
                [
                    "Urine pregnancy test before reinjection; backup contraception 7 days if restarting",
                    "Give injection without testing—grace period is 4 weeks",
                    "Switch to COC without pregnancy test",
                    "Wait until next menses regardless of timing",
                ],
                0,
                "Beyond 15 weeks (2-week grace after 13-week schedule), pregnancy testing is required before reinjection; backup needed when restarting late.",
                ref(
                    "Administration of Depot Medroxyprogesterone Acetate",
                    "In patients more than 2 weeks late for an injection, a urine pregnancy test should be performed before administering further DMPA, and backup contraception for 7 days is advised.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Contraceptive Uses",
                "A nulliparous 22-year-old requests IUD. Appropriate counseling?",
                [
                    "LNG-IUD is suitable; no parity requirement; STI risk assessment selective",
                    "IUD contraindicated until after first vaginal delivery",
                    "Only copper IUD allowed in nulliparous patients",
                    "Mandatory antibiotics before every IUD insertion",
                ],
                0,
                "Modern IUDs are safe for nulliparous and adolescent patients; prophylactic antibiotics are not recommended.",
                ref(
                    "Contraceptive Uses",
                    "There are few contraindications to IUDs, and most people are appropriate candidates including adolescents and nulliparous patients.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Mechanism of Action and Efficacy",
                "An obese patient asks whether Nexplanon efficacy is reduced at BMI 38. Best answer?",
                [
                    "Prospective data show failure rates not impacted by BMI",
                    "Implant is contraindicated when BMI >30",
                    "Implant only studied in BMI <25—cannot use",
                    "Double implant insertion required for BMI >35",
                ],
                0,
                "Although approval trials excluded obese subjects, cohort data show BMI does not affect implant contraceptive failure.",
                ref(
                    "Mechanism of Action and Efficacy",
                    "However, a prospective cohort study that examined 1168 patients (28% overweight and 35% obese) found failure rates were not impacted by BMI.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Patient Selection",
                "A woman on efavirenz-based ART needs long-acting contraception. Best option?",
                [
                    "LNG-IUD or DMPA—avoid etonogestrel implant with enzyme-inducing antiretrovirals",
                    "Etonogestrel implant—no drug interactions",
                    "Combined OCP 10 µg EE alone",
                    "No contraception needed on ART",
                ],
                0,
                "Implants are not recommended with enzyme-inducing anticonvulsants or certain antiretrovirals; IUD/DMPA are unaffected.",
                ref(
                    "Mechanism of Action and Efficacy",
                    "There are reports of implant failure in patients using anticonvulsants, particularly carbamazepine.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Emergency Contraception Regimens",
                "Unprotected intercourse occurred 4 days ago; patient wants most effective EC and ongoing contraception. Best option?",
                [
                    "Copper or LNG-IUD insertion within 5 days",
                    "Levonorgestrel 1.5 mg only—equally effective as IUD at day 4",
                    "Wait for menses then start COC",
                    "High-dose combined OCP Yuzpe regimen preferred",
                ],
                0,
                "Copper IUD is most effective EC (<0.1% failure) and provides continued contraception; LNG-IUD is non-inferior.",
                ref(
                    "Emergency Contraception Regimens",
                    "Recently, the LNG-IUD was found to be non-inferior to the copper IUD for EC.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Efficacy",
                "EC needed 60 hours after intercourse; BMI 33 kg/m². Oral agent selection?",
                [
                    "Ulipristal acetate 30 mg—more effective than levonorgestrel in overweight patients",
                    "Levonorgestrel 1.5 mg—equally effective at all weights",
                    "No oral EC works after 48 hours",
                    "Double levonorgestrel 3 mg is proven effective in obesity",
                ],
                0,
                "UPA works up to 5 days and retains efficacy in overweight patients where levonorgestrel may fail (BMI >26); do not deny EC by BMI.",
                ref(
                    "Efficacy",
                    "Patients should not be denied access to EC based upon BMI, but the potential impact of weight on EC efficacy should be discussed and considered in agent selection.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Ongoing Contraception",
                "After ulipristal acetate EC, when should regular hormonal contraception start?",
                [
                    "Delay hormonal contraception 5 days; use barriers or abstain meanwhile",
                    "Start combined OCP same day—no interaction",
                    "UPA allows immediate POP without delay",
                    "Wait one full cycle before any contraception",
                ],
                0,
                "Hormonal contraception, especially progestins, may reduce UPA efficacy; delay 5 days with barrier backup per USSPR.",
                ref(
                    "Ongoing Contraception",
                    "It has been suggested that commencement of regular hormonal contraception should be delayed for 5 days after the administration of UPA and patients should either abstain from sexual intercourse or use barrier protection for that duration.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Combined Hormonal Contraceptives in Adolescents",
                "A 17-year-old requests OCPs. Required before initiation?",
                [
                    "History excluding contraindications, BP, reasonable certainty she is not pregnant—no mandatory pelvic exam",
                    "Pelvic exam and Pap smear mandatory",
                    "Parental consent and 6-week trial of abstinence",
                    "Baseline liver biopsy",
                ],
                0,
                "USSPR: pelvic exam, cervical cancer screening, and STI screening are not required to start hormonal contraception in adolescents.",
                ref(
                    "Combined Hormonal Contraceptives in Adolescents",
                    "Initiating or continuing hormonal contraception does not require pelvic examination, cervical cancer screening, or sexually transmitted disease screening in adolescents or older reproductive-age patients.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Noncontraceptive Health Benefits",
                "A 30-year-old with PCOS and irregular bleeding desires contraception and endometrial protection. Best choice?",
                [
                    "Combined OCP to regulate cycles and prevent endometrial hyperplasia",
                    "Estrogen-only therapy without progestin",
                    "No treatment—PCOS does not affect endometrium",
                    "Copper IUD alone for endometrial protection",
                ],
                0,
                "COCs regularize bleeding and prevent endometrial hyperplasia in PCOS; copper IUD does not provide progestin-mediated endometrial protection.",
                ref(
                    "Noncontraceptive Health Benefits",
                    "Use of COC leads to more regular vaginal bleeding patterns, prevents endometrial hyperplasia, and may reduce clinical and biochemical hyperandrogenism in PCOS patients.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Progestin-Releasing Intrauterine Devices",
                "A 42-year-old with heavy menstrual bleeding declines surgery. First-line medical/device option per chapter?",
                [
                    "52-mg levonorgestrel IUD",
                    "High-dose combined OCP 50 µg EE indefinitely",
                    "Copper IUD only",
                    "Observation—LNG-IUD is not approved for bleeding",
                ],
                0,
                "52-mg LNG-IUD is first-line for heavy menstrual bleeding and alternative to ablation/hysterectomy.",
                ref(
                    "KEY POINTS",
                    "Besides offering highly effective contraception, the higher-dose levonorgestrel IUD represents a first-line treatment for heavy menstrual bleeding and an effective alternative to endometrial ablation and hysterectomy.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Upper Genital Tract Infection and Infertility",
                "Chlamydia diagnosed in a patient with LNG-IUD in place who responds to antibiotics. IUD management?",
                [
                    "Treat infection; IUD can remain if clinical improvement",
                    "Mandatory IUD removal for all STIs",
                    "Remove IUD before starting antibiotics",
                    "Replace IUD with copper device only",
                ],
                0,
                "PID/STI with IUD in place is treated per CDC guidelines; IUD may remain if patient responds to therapy.",
                ref(
                    "Upper Genital Tract Infection and Infertility",
                    "If a patient contracts gonorrhea, chlamydia, or PID with an LNG-IUD in place, treatment follows the CDC Sexually Transmitted Diseases Treatment guidelines, and if the patient responds to therapy, the IUD can remain in place.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Hormonal Contraception in Postpartum and Lactating Patients",
                "A patient is 2 weeks postpartum, breastfeeding, no VTE risk factors. When can combined hormonal contraception start per USMEC?",
                [
                    "Not before 4 weeks postpartum while breastfeeding (category 4 before then)",
                    "Immediately day 1 postpartum in all breastfeeding patients",
                    "Only after 6 months breastfeeding",
                    "Combined methods are category 1 from delivery",
                ],
                0,
                "Estrogen-containing methods are category 4 until 4 weeks in breastfeeding patients; progestin-only methods may start immediately.",
                ref(
                    "Hormonal Contraception in Postpartum and Lactating Patients",
                    "The USMEC recommends deferring use of estrogen-containing methods (category 4) until 3 weeks after delivery in everyone and until 4 weeks in breastfeeding patients.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                "A patient wants to start COCs today—last menstrual period unknown, negative pregnancy test. Approach?",
                [
                    "Quick-start COC now with backup or abstinence 7 days per USSPR",
                    "Must wait until day 1 of next menses",
                    "COCs are teratogenic if pregnancy occurs—delay until ultrasound confirms absence",
                    "Start only if serum progesterone <3 ng/mL",
                ],
                0,
                "Quick-start is safe when pregnancy excluded; inadvertent COC use in pregnancy does not increase miscarriage or fetal harm.",
                ref(
                    "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                    "Traditionally, COCs have been started on the first day of menses, but the pills can be safely started at any time if pregnancy has been excluded (quick-start method).",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Side Effects",
                "Persistent unscheduled bleeding on COCs after 4 months. Next step?",
                [
                    "Evaluate for pregnancy, cervical/endometrial pathology—not assume normal breakthrough only",
                    "Increase estrogen to 50 µg without workup",
                    "Stop COC permanently—bleeding always means failure",
                    "Ignore if patient is under 35",
                ],
                0,
                "Persistent or new bleeding requires investigation for pregnancy, infection, polyps, or neoplasia—not only dose adjustment.",
                ref(
                    "Side Effects",
                    "Persistent or new-onset bleeding should therefore be investigated.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Effect on Return of Fertility",
                "A couple plans pregnancy in 6 months. Which method may delay return of fertility longest after discontinuation?",
                [
                    "DMPA—return may take up to 18 months in some users",
                    "LNG-IUD—fertility suppressed for years after removal",
                    "COC—12-month conception rates worse than no method",
                    "POP—permanent amenorrhea common",
                ],
                0,
                "DMPA may delay ovulation return up to 18 months; IUD and COC users resume fertility rapidly.",
                ref(
                    "Effect on Return of Fertility",
                    "However, in some individuals, fertility is not reestablished until up to 18 months after the last injection.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Safety and Side Effect Profile",
                "Nexplanon user with bothersome prolonged bleeding after counseling. USSPR-endorsed short-term option?",
                [
                    "NSAIDs 5–7 days or low-dose COC/estrogen 10–20 days if no estrogen contraindication",
                    "Immediate surgical removal mandatory",
                    "High-dose medroxyprogesterone acetate injection monthly",
                    "No treatment exists—must discontinue implant",
                ],
                0,
                "USSPR recommends NSAIDs or short-course estrogen/COC for bothersome implant bleeding; long-term COC co-use may be considered.",
                ref(
                    "Safety and Side Effect Profile",
                    "If a patient using a contraceptive implant desires treatment to reduce bothersome irregular bleeding, the USSPR recommends two options: (1) NSAIDs for 5 to 7 days or (2) low-dose COCs or estrogen for 10 to 20 days.",
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
                "Copper and levonorgestrel IUDs are more effective emergency contraceptives than oral levonorgestrel or ulipristal acetate.",
                True,
                "IUDs are the most effective EC; oral UPA is next among pills, then levonorgestrel.",
                ref(
                    "KEY POINTS",
                    "The copper and levonorgestrel IUDs are the most effective emergency contraceptives, followed by oral ulipristal acetate and oral levonorgestrel.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                "Typical first-year failure rate for combined oral contraceptives with usual adherence is about 7 per 100 women.",
                True,
                "Perfect use is <1 per 100 woman-years; typical use is ~7% first-year failure.",
                ref(
                    "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                    "Typical first-year combination oral contraception failure rates are estimated at 7 per 100 women.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Side Effects",
                "Randomized placebo-controlled trials have shown COCs reliably cause clinically significant weight gain.",
                False,
                "RCTs have not shown COCs cause weight gain, nausea, breast tenderness, or mood changes—though some users report symptoms.",
                ref(
                    "Side Effects",
                    "Contrary to popular perception, randomized, placebo-controlled trials have not shown that COCs cause weight gain, nausea, breast tenderness, or mood changes.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Thromboembolic Disease",
                "Routine screening for familial thrombophilia is recommended before initiating COCs in all patients.",
                False,
                "USMEC does not recommend population screening for thrombophilia before COC initiation.",
                ref(
                    "Thromboembolic Disease",
                    "Routine screening of the general population for familial thrombophilic markers is not recommended before initiating COC use.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Use of Concomitant Medications With Combined Oral Contraceptive Pills",
                "Non-rifamycin antibiotics have been shown to reduce hormonal contraceptive efficacy.",
                False,
                "Except rifamycins, concomitant antibiotics do not reduce efficacy of hormonal contraceptives.",
                ref(
                    "Use of Concomitant Medications With Combined Oral Contraceptive Pills",
                    "With the exception of those in the rifamycin class, concomitant use of antibiotics has not been found to reduce efficacy of any hormonal contraceptives.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Progestin-Only Contraceptive Methods",
                "Progestin-only methods have no USMEC restrictions for smoking women age ≥35.",
                True,
                "Table 16.3 shows no restriction for POP, DMPA, implant, and LNG-IUD with smoking age ≥35.",
                ref(
                    "Progestin-Only Contraceptive Methods",
                    "Progestin-only contraceptives may be appropriate for many patients with contraindications to contraceptive doses of estrogen, including those at elevated baseline risk for VTE, those age 35 or older who smoke, and those with hypertension or who have long-standing diabetes.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Mechanism of Action",
                "Norethindrone 0.35-mg POP consistently suppresses ovulation like combined OCPs.",
                False,
                "Ovulation is not consistently suppressed with norethindrone POP; mucus and endometrial effects are critical.",
                ref(
                    "Mechanism of Action",
                    "Unlike with COCs, ovulation is not consistently suppressed with the 0.35-mg norethindrone POP, and the progestin effects on cervical mucus and the endometrium are critical factors in preventing conception.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Contraceptive Uses",
                "Most LNG-IUD users continue to ovulate despite amenorrhea.",
                True,
                "Local progestin suppresses endometrium while ovulation often continues.",
                ref(
                    "Contraceptive Uses",
                    "Most LNG-IUD users continue to ovulate, even when amenorrhea is present.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Upper Genital Tract Infection and Infertility",
                "Modern intrauterine contraception increases risk of subsequent infertility.",
                False,
                "Earlier flawed studies are refuted; modern IUDs do not increase infertility risk.",
                ref(
                    "Upper Genital Tract Infection and Infertility",
                    "Similarly, there is no evidence that intrauterine contraception increases the risk of subsequent infertility.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Mechanism of Action",
                "Levonorgestrel emergency contraception acts primarily by preventing implantation after fertilization.",
                False,
                "Levonorgestrel EC prevents or delays ovulation before LH surge; it does not impair implantation.",
                ref(
                    "Mechanism of Action",
                    "Neither oral agent has been shown to interfere with implantation directly.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Indications",
                "Pregnancy testing is required before administering oral hormonal emergency contraception.",
                False,
                "No clinical examination or pregnancy test is required before oral EC; EC is ineffective if pregnancy already established.",
                ref(
                    "Indications",
                    "No clinical examination or pregnancy testing is required before using oral hormonal EC.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Combined Hormonal Contraceptives in Adolescents",
                "Norethindrone POP is favored over combined OCPs for adolescents because of simpler dosing.",
                False,
                "POPs require stricter timing and are not favored for adolescents.",
                ref(
                    "Combined Hormonal Contraceptives in Adolescents",
                    "By the same token, norethindrone POPs are not favored for adolescents because they require stricter adherence for efficacy.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Hormonal Contraception in Patients Older Than 35 Years",
                "Healthy nonsmoking women over 35 may use low-dose combined hormonal contraception until menopause.",
                True,
                "Lean healthy nonsmokers can use combined methods; progestin-only preferred when additional cardiovascular risk factors present.",
                ref(
                    "Hormonal Contraception in Patients Older Than 35 Years",
                    "However, because lean, healthy, nonsmoking patients are at low risk for these rare events, they can use any method, including combined (estrogen-progestin pills, patch, and vaginal ring) methods, until menopause.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Choosing a Contraceptive Method",
                "Assertion: LARC methods should be offered to all patients including adolescents.",
                "Reason: LARC provides contraceptive effectiveness equivalent to sterilization with high continuation rates.",
                0,
                "Both true—KEY POINTS and Choosing sections endorse universal LARC offering.",
                ref(
                    "KEY POINTS",
                    "These methods can be offered to all patients, including adolescents seeking contraception.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                "Assertion: COC failure is largely attributable to poor adherence.",
                "Reason: Different progestin types in COCs cause markedly different typical failure rates.",
                2,
                "Assertion true; reason false—progestin type does not significantly alter COC efficacy.",
                ref(
                    "Mechanism of Action, Efficacy, Administration, and Effect on Pregnancy",
                    "There does not appear to be any significant difference in contraceptive efficacy of COCs formulated with different progestins.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Health Risks",
                "Assertion: Migraine with aura is a contraindication to estrogen-containing contraception.",
                "Reason: Migraine without aura is also category 4 for all estrogen methods.",
                2,
                "Assertion true; reason false—migraine without aura is category 2 (benefits outweigh risks) unless other stroke risk factors.",
                ref(
                    "Health Risks",
                    "Conditions that present an unacceptable health risk if the contraceptive method is used; examples for estrogen-containing methods include delivery during the past 21 days, a personal history of deep venous thrombosis or pulmonary embolism, ischemic heart disease, stroke, known thrombogenic mutations, and migraine headaches with aura or other neurologic signs.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Thromboembolic Disease",
                "Assertion: COC use increases venous thromboembolism risk more than twofold.",
                "Reason: VTE risk with COCs is primarily related to the progestin component.",
                2,
                "Assertion true; reason false—estrogenic component drives VTE risk.",
                ref(
                    "Thromboembolic Disease",
                    "The established increased risk of venous thromboembolism (VTE) is related to the estrogenic component and, although modern low-dose preparations (≤35 µg) carry a lower risk than the original oral contraceptives, the incidence of VTE is still increased.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Progestin-Only Contraceptive Methods",
                "Assertion: Progestin-only contraceptives are suitable for patients with prior VTE.",
                "Reason: DMPA package labeling still lists prior VTE as contraindication despite USMEC guidance.",
                0,
                "Both true—USMEC allows progestin-only methods with VTE history though legacy DMPA label disagrees.",
                ref(
                    "Risks and Benefits of Depot Medroxyprogesterone Acetate",
                    "Based on these findings, the USMEC allows DMPA and other progestin-only contraceptives for use in patients with a history of VTE and those in whom use of combination estrogen-progestin contraceptive is contraindicated.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Progestin-Only Oral Contraceptive Pill",
                "Assertion: Drospirenone POP suppresses ovulation more reliably than norethindrone POP.",
                "Reason: Drospirenone has a shorter half-life than norethindrone requiring stricter timing.",
                2,
                "Assertion true; reason false—drospirenone half-life is 24–36 hours, longer and more forgiving than norethindrone.",
                ref(
                    "Progestin-Only Oral Contraceptive Pill",
                    "The half-life of drospirenone is 24 to 36 hours, and this regimen suppresses ovulation reliably, which will likely lead to improved effectiveness.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Formulations and Pharmacology",
                "Assertion: DMPA efficacy is not reduced by obesity.",
                "Reason: High circulating progestin levels overcome enzyme-inducer effects and obesity-related metabolism.",
                0,
                "Both true—DMPA maintains efficacy with obesity and interacting medications unlike COCs.",
                ref(
                    "Formulations and Pharmacology",
                    "Because progestin levels are high, efficacy is not reduced by obesity or use of concurrent medications such as anticonvulsants.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Contraceptive Uses",
                "Assertion: LNG-IUD provides contraception primarily through local endometrial and cervical effects.",
                "Reason: Systemic levonorgestrel levels with 52-mg IUD exceed those of oral levonorgestrel pills.",
                2,
                "Assertion true; reason false—serum levonorgestrel with 52-mg IUD (150–200 pg/mL) is far lower than oral LNG pills (6.2 ng/mL).",
                ref(
                    "Progestin-Releasing Intrauterine Devices",
                    "A stable serum concentration of 150 to 200 pg/mL of levonorgestrel occurs after insertion of the 52-mg LNG-IUD, a concentration substantially lower than seen in women using a 150-μg levonorgestrel-containing oral contraceptive pill (6.2 ng/mL).",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Emergency Contraception",
                "Assertion: Ulipristal acetate is more effective than levonorgestrel EC.",
                "Reason: UPA can delay follicular rupture even after LH rise begins, unlike levonorgestrel.",
                0,
                "Both true—UPA inhibits follicular development pre-surge and delays rupture during LH rise.",
                ref(
                    "Mechanism of Action",
                    "UPA inhibits follicular development when administered before the commencement of the LH surge; in contrast, UPA delays follicular rupture when administered during the LH increase but before its peak.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Efficacy",
                "Assertion: Efficacy of oral EC decreases with increasing BMI.",
                "Reason: Copper IUD EC efficacy is also reduced in obese patients.",
                2,
                "Assertion true for oral agents; reason false—IUD EC efficacy is not affected by BMI.",
                ref(
                    "Efficacy",
                    "The efficacy of the copper and LNG-IUD is not affected by BMI.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Expanding the Use of Intrauterine Devices",
                "Assertion: Removing financial barriers increases LARC uptake.",
                "Reason: CHOICE participants had lower unintended pregnancy rates than regional/national averages.",
                0,
                "Both true—68% chose LARC when cost removed and pregnancy/abortion rates fell substantially.",
                ref(
                    "Expanding the Use of Intrauterine Devices",
                    "In addition, among subjects participating in the Contraceptive CHOICE Project, rates of unintended pregnancy, birth, and abortion were substantially lower than for other women in St. Louis and compared to women in the United States overall.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Hormonal Contraception in Postpartum and Lactating Patients",
                "Assertion: Progestin-only contraception can be started immediately postpartum.",
                "Reason: Combined OCPs are category 1 for immediate postpartum initiation in breastfeeding patients.",
                2,
                "Assertion true; reason false—estrogen methods are category 4 early postpartum, especially while breastfeeding.",
                ref(
                    "Hormonal Contraception in Postpartum and Lactating Patients",
                    "It appears reasonable to initiate progestin-only contraception, including DMPA, POPs, and implants, immediately after delivery, regardless of whether mothers are nursing their infants.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "16",
        "title": "Hormonal Contraception",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Rebecca H. Allen, Annabelle Huguenin, Martha Hickey, and Andrew M. Kaunitz",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_16_Hormonal_Contraception.md",
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
