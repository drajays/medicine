#!/usr/bin/env python3
"""Generate Williams 15e module w15-15 — Female Reproductive Axis."""
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
OUT_NAME = "w15-15_Physiology_and_Pathology_of_the_Female_Reproductive_Axis.json"


def build() -> dict:
    p = "w15-15"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Female reproductive axis overview",
                "Ovulation and uterine preparation for pregnancy are tightly regulated by hypothalamic, pituitary, and ovarian hormones; common disorders disrupting this axis include hypothalamic anovulation, hyperprolactinemia, PCOS, ovarian insufficiency, endometriosis, and uterine fibroids.",
                ref(
                    "KEY POINTS",
                    "A premenopausal woman often seeks medical help because of disorders that disrupt or complicate ovulation, normal menses, or fertility; the most common disorders include hypothalamic anovulation, hyperprolactinemia, polycystic ovary syndrome (POCS), ovarian insufficiency, endometriosis, and uterine fibroids.",
                ),
            ),
            note(
                f"{p}-n2",
                "Reproductive Physiology",
                "Why pulsatile GnRH is essential",
                "Normal menses every 21–35 days requires coordinated hypothalamic GnRH pulses, pituitary FSH/LH, ovarian steroidogenesis, and endometrial response; disorders at any level cause anovulation and irregular bleeding.",
                ref(
                    "Reproductive Physiology",
                    "In summary, the female reproductive function from puberty to menopause can be viewed as an extremely delicate ticking clock.",
                ),
            ),
            note(
                f"{p}-n3",
                "Gonadotropin-Releasing Hormone",
                "GnRH neuronal anatomy and Kallmann syndrome",
                "GnRH is synthesized in arcuate and preoptic neurons, secreted at the median eminence into portal vessels, and delivered to anterior pituitary gonadotrophs; failed embryologic migration of GnRH neurons causes Kallmann syndrome with hypogonadotropic hypogonadism and anosmia.",
                ref(
                    "Gonadotropin-Releasing Hormone",
                    "GnRH and olfactory neurons migrate together along cranial nerves connecting the nose and forebrain to the hypothalamus during embryologic development, and disruption of this process causes hypogonadotropic hypogonadism with anosmia, or Kallmann syndrome.",
                ),
            ),
            note(
                f"{p}-n4",
                "Gonadotropin-Releasing Hormone",
                "How GnRH pulse frequency governs the axis",
                "Knobil showed pulsatile GnRH within 60–90 minutes restores gonadotropins; slower pulses cause anovulation from inadequate stimulation, while continuous GnRH downregulates receptors and also abolishes gonadotropin responses.",
                ref(
                    "Gonadotropin-Releasing Hormone",
                    "Slower frequency causes anovulation and amenorrhea because of inadequate stimulation. Higher frequency or constant exposure to GnRH also gives rise to anovulation by downregulating expression of GnRH receptors, thereby abolishing gonadotropin responses.",
                ),
            ),
            note(
                f"{p}-n5",
                "Regulation of Gonadotropin-Releasing Hormone Secretion",
                "How kisspeptin drives GnRH pulsatility",
                "Kisspeptin binding to KISS1R on GnRH neurons stimulates GnRH release; KISS1R mutations cause isolated hypogonadotropic hypogonadism, and kisspeptin neurons are critical targets of estrogen and progesterone feedback.",
                ref(
                    "Regulation of Gonadotropin-Releasing Hormone Secretion",
                    "Mutations or knockout of KISS1R produces isolated hypogonadotropic hypogonadism in humans and mice, indicating that signaling through this receptor is essential for sexual development and function.",
                ),
            ),
            note(
                f"{p}-n6",
                "Regulation of Circulating Levels of Follicle-Stimulating Hormone and Luteinizing Hormone",
                "How inhibin, activin, and follistatin modulate FSH",
                "Inhibin B from granulosa cells (follicular phase) and inhibin A from corpus luteum suppress FSH; activin stimulates FSH biosynthesis, while follistatin binds activin and limits its action.",
                ref(
                    "Regulation of Circulating Levels of Follicle-Stimulating Hormone and Luteinizing Hormone",
                    "Inhibin B is secreted by ovarian granulosa cells during the follicular phase (under the control of FSH) and inhibin A by the corpus luteum in the luteal phase (under the control of LH).",
                ),
            ),
            note(
                f"{p}-n7",
                "Ovary",
                "Ovarian anatomy and functional units",
                "The adult ovary has cortex (follicles, germinal epithelium), medulla, and hilum; the follicle—oocyte plus granulosa and theca cells—is the fundamental functional unit integrating oocyte release and estradiol/progesterone production.",
                ref(
                    "Ovary",
                    "The ovarian follicle comprising the oocyte and surrounding granulosa and theca cells constitutes the fundamental functional unit of the ovary.",
                ),
            ),
            note(
                f"{p}-n8",
                "Follicles",
                "How folliculogenesis proceeds to ovulation",
                "Primordial follicle recruitment takes ~85 days, mostly FSH-independent; late-luteal FSH rise rescues a 2–5 mm cohort, and the dominant follicle ovulates 10–14 days after selection following the mid-cycle LH surge.",
                ref(
                    "Follicles",
                    "The total time to achieve preovulatory status is approximately 85 days.",
                ),
            ),
            note(
                f"{p}-n9",
                "Ovarian Follicle-Stimulating Hormone and Luteinizing Hormone Receptors",
                "Why FSH is essential for follicular maturation",
                "FSH receptor is exclusive to granulosa cells and promotes follicular growth, aromatase induction, and LH receptor acquisition; FSH β-subunit or receptor mutations arrest follicles at the preantral stage.",
                ref(
                    "Ovarian Follicle-Stimulating Hormone and Luteinizing Hormone Receptors",
                    "FSH is the main promoter of follicular maturation.",
                ),
            ),
            note(
                f"{p}-n10",
                "Two-Cell Theory for Ovarian Steroidogenesis",
                "How the two-cell model produces estradiol",
                "LH on theca cells drives StAR and androstenedione synthesis; androstenedione diffuses to granulosa cells where FSH-induced aromatase converts it to estrone and estradiol—the classic two-cell, two-gonadotropin mechanism.",
                ref(
                    "Two-Cell Theory for Ovarian Steroidogenesis",
                    "The StAR protein is the primary regulator of production of androstenedione, which subsequently diffuses into granulosa cells to serve as the estrogen precursor.",
                ),
            ),
            note(
                f"{p}-n11",
                "Overview of the Hormonal Changes During the Ovarian Cycle",
                "How the menstrual cycle resets FSH",
                "Corpus luteum regression removes estradiol/progesterone/inhibin feedback, permitting pre-menstrual FSH rise; mid-cycle estradiol positive feedback triggers LH surge, ovulation, and 14-day luteal progesterone secretion.",
                ref(
                    "Overview of the Hormonal Changes During the Ovarian Cycle",
                    "Ovulation is triggered by the rapid rise in circulating levels of estradiol.",
                ),
            ),
            note(
                f"{p}-n12",
                "Effects of Ovarian Steroids on Endometrium",
                "How estrogen and progesterone shape endometrium",
                "Estradiol proliferates endometrium; progesterone limits estrogenic growth and promotes differentiation; withdrawal of either hormone causes functional layer shedding while the basalis regenerates with the next cycle.",
                ref(
                    "Reproductive Physiology",
                    "The biologically active estrogen, estradiol, induces the growth of endometrium; progesterone limits this estrogenic effect and enhances differentiation.",
                ),
            ),
            note(
                f"{p}-n13",
                "Mechanism of Menstruation",
                "Mechanism of menstruation",
                "Menstruation depends on spiral artery vasoconstriction and sloughing of the stratum functionalis after progesterone or estrogen withdrawal; only primates with spiral arteries experience true menstruation.",
                ref(
                    "Endometrium",
                    "Menstruation is shedding of endometrial tissue with hemorrhage that depends on sex steroid hormone-directed changes in blood flow in the spiral arteries.",
                ),
            ),
            note(
                f"{p}-n14",
                "Approach to the Woman With Reproductive Dysfunction",
                "How to approach amenorrhea workup",
                "After excluding pregnancy, categorize secondary amenorrhea by history and estrogen status: hypothalamic dysfunction, hyperprolactinemia, ovarian insufficiency, androgen excess, chronic illness, or uterine disease; FSH and prolactin orient the differential.",
                ref(
                    "Approach to the Woman With Reproductive Dysfunction",
                    "After pregnancy is ruled out, secondary amenorrhea is most often caused by chronic anovulation, which can be broadly categorized as hypothalamic dysfunction, hyperprolactinemia-associated anovulation, ovarian insufficiency, androgen excess, chronic illness related, or primary uterine disease (e.g., intrauterine adhesion formation after a postpartum curettage).",
                ),
            ),
            note(
                f"{p}-n15",
                "Chronic Anovulation",
                "Five categories of chronic anovulation",
                "Reproductive-age chronic anovulation falls into hypothalamic anovulation, hyperprolactinemia, androgen excess (chiefly PCOS), POI, or chronic illness; estrogen-deficient vs androgen-excess phenotypes guide urgency of therapy and endometrial protection.",
                ref(
                    "Chronic Anovulation",
                    "For practical purposes, most of the etiologic factors giving rise to chronic anovulation in a woman of reproductive age fall into five broad categories: hypothalamic anovulation, hyperprolactinemia, androgen excess, POI, and chronic illness (e.g., hepatic or renal insufficiency, acquired immunodeficiency syndrome [AIDS]).",
                ),
            ),
            note(
                f"{p}-n16",
                "Chronic Anovulation",
                "How FSH and prolactin categorize anovulation",
                "Low or normal FSH suggests hypothalamic amenorrhea, PCOS, or hyperprolactinemia; elevated FSH indicates ovarian insufficiency; elevated prolactin warrants evaluation for prolactinoma, pituitary disease, or hypothyroidism.",
                ref(
                    "Chronic Anovulation",
                    "An undetectable or low-normal FSH level is consistent with hypothalamic amenorrhea, PCOS, or hyperprolactinemia, whereas high FSH levels suggest ovarian insufficiency.",
                ),
            ),
            note(
                f"{p}-n17",
                "Hypothalamic Anovulation",
                "Why reduced GnRH pulse causes amenorrhea",
                "Reduced GnRH pulse frequency below 60–120 minutes to >180 minutes lowers LH/FSH, arrests follicular maturation, and produces estrogen-deficient amenorrhea without hot flashes—distinguishing it from ovarian failure.",
                ref(
                    "Hypothalamic Anovulation",
                    "A reduction in GnRH pulse frequency from the characteristic 60 to 120 minutes to intervals longer than 180 minutes leads to lower levels of LH.",
                ),
            ),
            note(
                f"{p}-n18",
                "Functional Hypothalamic Amenorrhea",
                "Functional hypothalamic amenorrhea",
                "FHA is a diagnosis of exclusion after 6+ months amenorrhea without anatomic lesion, preceded by stress, caloric restriction, excessive exercise, or psychiatric illness; LH pulses are reduced and endogenous opioid tone is often increased.",
                ref(
                    "Functional Hypothalamic Amenorrhea",
                    "This condition typically manifests as amenorrhea of at least a 6-month duration and has also been called functional hypothalamic amenorrhea.",
                ),
            ),
            note(
                f"{p}-n19",
                "Functional Hypothalamic Amenorrhea",
                "Why opioids mediate FHA",
                "Naloxone increases LH pulse frequency and amplitude in many women with hypothalamic amenorrhea, suggesting heightened endogenous opioid inhibition of pulsatile GnRH—linking stress, exercise, and eating disorders to reproductive suppression.",
                ref(
                    "Functional Hypothalamic Amenorrhea",
                    "Blockade of endogenous opiate receptors by the administration of naloxone, an opiate antagonist, causes an increase in the frequency and amplitude of pulsatile LH release in the majority of women with hypothalamic amenorrhea.",
                ),
            ),
            note(
                f"{p}-n20",
                "Chronic Anovulation Associated With Pituitary Disorders",
                "Why hyperprolactinemia causes anovulation",
                "The most common pituitary cause of anovulation is hyperprolactinemia from prolactinomas or other pituitary disorders, frequently presenting with galactorrhea and suppressed gonadotropin secretion.",
                ref(
                    "Chronic Anovulation Associated With Pituitary Disorders",
                    "The most common pituitary-related causes of anovulation are associated with hyperprolactinemia caused by prolactinomas or other functional or anatomic disorders of the pituitary.",
                ),
            ),
            note(
                f"{p}-n21",
                "Polycystic Ovary Syndrome",
                "PCOS clinical scope",
                "PCOS affects 5–10% of reproductive-age women with chronic anovulation and androgen excess after excluding other hyperandrogenic disorders; long-term risks include infertility, endometrial neoplasia, insulin resistance, diabetes, and cardiovascular disease.",
                ref(
                    "Polycystic Ovary Syndrome",
                    "PCOS is the most common form of chronic anovulation associated with androgen excess; it occurs in perhaps 5% to 10% of reproductive-age women.",
                ),
            ),
            note(
                f"{p}-n22",
                "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                "How PCOS is diagnosed",
                "Diagnosis requires hyperandrogenism plus ovarian dysfunction (oligo-anovulation and/or polycystic ovaries) after excluding thyroid dysfunction, hyperprolactinemia, nonclassic CAH, and androgen-secreting tumors; Rotterdam criteria expanded NIH definitions.",
                ref(
                    "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                    "The diagnosis of PCOS is made by excluding other hyperandrogenic disorders (e.g., nonclassic congenital adrenal hyperplasia, androgen-secreting tumors, hyperprolactinemia) in women with chronic anovulation and androgen excess.",
                ),
            ),
            note(
                f"{p}-n23",
                "Gonadotropin Production in Polycystic Ovary Syndrome",
                "Gonadotropin abnormalities in PCOS",
                "PCOS features elevated mean LH with low or normal FSH from accelerated GnRH-LH pulsatility, often without progesterone-mediated opioid suppression; obesity may normalize LH amplitude despite persistent pulse-frequency abnormalities.",
                ref(
                    "Gonadotropin Production in Polycystic Ovary Syndrome",
                    "Women with PCOS have higher mean concentrations of LH but low or low-normal levels of FSH compared with levels found in normal women in the early follicular phase.",
                ),
            ),
            note(
                f"{p}-n24",
                "Insulin Resistance and Polycystic Ovary Syndrome",
                "Insulin resistance in PCOS pathogenesis",
                "Insulin resistance in lean and obese PCOS drives hyperinsulinemia, ovarian androgen production, low SHBG, and metabolic syndrome overlap; acanthosis nigricans marks severe hyperinsulinemia.",
                ref(
                    "Insulin Resistance and Polycystic Ovary Syndrome",
                    "Insulin resistance is frequently observed in lean and obese women with PCOS.",
                ),
            ),
            note(
                f"{p}-n25",
                "Premature Ovarian Insufficiency",
                "Premature ovarian insufficiency",
                "POI is hypergonadotropic hypogonadism with follicle depletion before age 40, presenting after normal puberty with oligomenorrhea, amenorrhea, hot flashes, and elevated FSH; causes include genetics (FMR1 premutation, Turner variants), autoimmunity, and gonadotoxic therapy.",
                ref(
                    "Premature Ovarian Insufficiency",
                    "POI, which is defined as early depletion of ovarian follicles (before the age of 40 years), is a state of hypergonadotropic hypogonadism.",
                ),
            ),
            note(
                f"{p}-n26",
                "Diagnosis and Management of Premature Ovarian Insufficiency",
                "How to diagnose and manage POI",
                "Menopausal FSH ≥40 IU/L on two occasions confirms POI in women <40; karyotype if <30, FMR1 testing, TSH screening, hormone therapy for deficiency, and donor-oocyte IVF for fertility when autologous pregnancy is unlikely.",
                ref(
                    "Diagnosis and Management of Premature Ovarian Insufficiency",
                    "Menopausal serum FSH levels (40 IU/L) on at least two occasions are sufficient for the diagnosis of POI.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Approach to the Woman With Reproductive Dysfunction",
                "A 22-year-old college runner has 8 months of amenorrhea, low BMI, and no hot flashes. Pregnancy test negative. Best next laboratory tests?",
                [
                    "FSH, prolactin, and TSH",
                    "24-hour urine cortisol only",
                    "Serum testosterone and DHEAS alone without FSH",
                    "Immediate laparoscopy before any labs",
                ],
                0,
                "FHA is a diagnosis of exclusion; FSH categorizes hypogonadotropic vs hypergonadotropic causes, and prolactin/TSH rule out prolactinoma and hypothyroidism.",
                ref(
                    "Functional Hypothalamic Amenorrhea",
                    "LH and FSH levels are usually lower than the normal values ordinarily found in the early follicular phase. TSH and prolactin levels are obtained to rule out hypothyroidism and hyperprolactinemia.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Functional Hypothalamic Amenorrhea",
                "A thin 19-year-old with FHA has scant withdrawal bleeding after medroxyprogesterone 10 days but bleeds after combined estrogen-progestin. This pattern indicates:",
                [
                    "Uterus is intact but chronic hypoestrogenism—consistent with hypothalamic anovulation",
                    "Intact pituitary prolactinoma requiring immediate surgery",
                    "Primary müllerian agenesis with absent uterus",
                    "Confirmed POI requiring donor oocytes immediately",
                ],
                0,
                "Positive estrogen-progestin withdrawal with weak progestin-only response reflects low endogenous estradiol with a normal uterine compartment.",
                ref(
                    "Functional Hypothalamic Amenorrhea",
                    "The administration of combined estrogen (2 mg/day of oral micronized estradiol) with progestin (5 mg/day of MPA for 10 days) will result in endometrial growth followed by vaginal bleeding after one or more cycles of therapy because the uterine compartment remains functionally normal.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Gonadotropin-Releasing Hormone",
                "Continuous GnRH agonist infusion in ovariectomized monkeys abolishes LH/FSH. Clinical parallel?",
                [
                    "Downregulation of pituitary GnRH receptors used therapeutically after initial flare",
                    "Immediate ovulation induction from constant GnRH",
                    "Permanent restoration of fertility without desensitization",
                    "Increased FSH preferentially over LH with continuous exposure",
                ],
                0,
                "Constant GnRH suppresses gonadotropins by receptor downregulation—the basis of depot agonist therapy after the initial flare.",
                ref(
                    "Gonadotropin-Releasing Hormone",
                    "Higher frequency or constant exposure to GnRH also gives rise to anovulation by downregulating expression of GnRH receptors, thereby abolishing gonadotropin responses.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Overview of the Hormonal Changes During the Ovarian Cycle",
                "A woman mid-cycle has sharply rising estradiol and an LH surge. What event follows in ~34–36 hours?",
                [
                    "Follicular rupture and ovulation",
                    "Corpus luteum regression",
                    "Menstrual shedding of functionalis",
                    "FSH peak from corpus luteum withdrawal",
                ],
                0,
                "The LH surge triggers ovulation predictably 34–36 hours after its onset.",
                ref(
                    "Ovulation",
                    "Follicular rupture or ovulation occurs predictably 34 to 36 hours after the start of the LH surge.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Two-Cell Theory for Ovarian Steroidogenesis",
                "A patient has intact theca androgen production but granulosa aromatase deficiency. Expected hormonal pattern?",
                [
                    "Elevated androstenedione with low estradiol despite normal LH/FSH",
                    "Isolated progesterone excess from corpus luteum only",
                    "Suppressed LH with high inhibin A only",
                    "Low androstenedione with high estradiol",
                ],
                0,
                "The two-cell model requires theca androstenedione diffusion to granulosa aromatase for estradiol synthesis.",
                ref(
                    "Two-Cell Theory for Ovarian Steroidogenesis",
                    "Because granulosa cells do not have a direct connection to the circulation, CYP19A1 (aromatase) in granulosa cells depends for substrate on androstenedione that diffuses from theca cells.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Polycystic Ovary Syndrome",
                "A 24-year-old with irregular menses since menarche, hirsutism, acanthosis nigricans, and well-estrogenized cervix. Most likely diagnosis after pregnancy excluded?",
                [
                    "Polycystic ovary syndrome",
                    "Functional hypothalamic amenorrhea with estrogen deficiency",
                    "Premature ovarian insufficiency",
                    "Sheehan syndrome",
                ],
                0,
                "Pubertal-onset irregular bleeding with androgen excess and insulin-resistance stigmata fits PCOS; FHA is estrogen-deficient.",
                ref(
                    "Approach to the Woman With Reproductive Dysfunction",
                    "For example, PCOS is unlikely without a long-standing history of irregular periods since the menarche.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                "An anovulatory woman has elevated testosterone and polycystic ovaries on ultrasound. Essential exclusion before confirming PCOS?",
                [
                    "Measure prolactin and TSH to rule out hyperprolactinemia and hypothyroidism",
                    "No further testing—ultrasound alone confirms PCOS",
                    "Inferior petrosal sinus sampling for Cushing disease in all cases",
                    "Immediate bilateral oophorectomy for histology",
                ],
                0,
                "PCOS is a diagnosis of exclusion; prolactin and TSH are routine screens for mimics of androgen excess and anovulation.",
                ref(
                    "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                    "Prolactin and TSH concentrations should be measured routinely to rule out mild androgen excess and anovulation that may be associated with hyperprolactinemia.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                "A PCOS patient has predictable withdrawal bleeding on cyclic progestin. Endometrial surveillance strategy?",
                [
                    "Periodic biopsy not needed during effective progestin or OCP therapy with predictable bleeds",
                    "Never perform biopsy in women under 40 regardless of anovulation duration",
                    "Biopsy only if amenorrheic—oligomenorrhea excludes hyperplasia risk",
                    "Hysterectomy for all PCOS patients at diagnosis",
                ],
                0,
                "Unopposed estrogen exposure duration drives endometrial risk; predictable progestin/OCP withdrawal bleeding is reassuring.",
                ref(
                    "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                    "Response to oral contraceptives or periodic progestin treatment with predictable withdrawal bleeding episodes is reassuring, and patients with predictable bleeding patterns do not need endometrial sampling during these treatments.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Ovulation Induction in Polycystic Ovary Syndrome",
                "An infertile woman with PCOS failed clomiphene 150 mg. Evidence-based next step for ovulation induction?",
                [
                    "Letrozole (first-line aromatase inhibitor) before conventional high-dose FSH",
                    "Conventional FSH 150 IU daily as first-line",
                    "Bilateral wedge resection of ovaries",
                    "Observation for 2 years without treatment",
                ],
                0,
                "Letrozole achieves higher live-birth rates than clomiphene; conventional high-dose gonadotropins risk multiples and OHSS.",
                ref(
                    "Ovulation Induction in Polycystic Ovary Syndrome",
                    "Therefore, letrozole is the first-line (yet off-label) treatment for ovulation induction in these patients.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Management of Long-Term Deleterious Effects of Polycystic Ovary Syndrome",
                "A nonsmoking 28-year-old with PCOS does not desire pregnancy and has irregular bleeding. Best long-term endometrial protection?",
                [
                    "Low-dose combined oral contraceptive or cyclic progestin",
                    "Estrogen-only therapy without progestin",
                    "No treatment because amenorrhea excludes hyperplasia risk",
                    "GnRH agonist monotherapy indefinitely without add-back",
                ],
                0,
                "Chronic unopposed estradiol in PCOS increases endometrial cancer risk even in young women; progestin exposure is mandatory.",
                ref(
                    "Management of Long-Term Deleterious Effects of Polycystic Ovary Syndrome",
                    "Anovulatory women with PCOS may have endometrial cancer even in their early 20s.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Premature Ovarian Insufficiency",
                "A 32-year-old has 6 months amenorrhea, hot flashes, and FSH 62 IU/L on two occasions. Next essential evaluation?",
                [
                    "FMR1 premutation testing and TSH; consider karyotype if younger",
                    "Repeat FSH in 5 years before any action",
                    "Serum AMH only—FSH is unnecessary",
                    "Immediate bilateral salpingo-oophorectomy without workup",
                ],
                0,
                "POI workup includes confirming elevated FSH, fragile X premutation carrier testing, and thyroid evaluation per Box 15.6.",
                ref(
                    "Diagnosis and Management of Premature Ovarian Insufficiency",
                    "Women with POI are at increased risk for an FMR1 premutation and should be informed of the availability of fragile X testing.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Premature Ovarian Insufficiency",
                "A 28-year-old with POI desires pregnancy. Most effective fertility option?",
                [
                    "Donor oocyte IVF after endometrial priming with estrogen and progesterone",
                    "Expectant management—autologous pregnancy rate exceeds 50% per cycle",
                    "High-dose clomiphene alone without monitoring",
                    "Pulsatile GnRH only—restores normal fertility in most POI",
                ],
                0,
                "Autologous pregnancy in POI is uncommon; donor oocyte IVF offers >50% live-birth rate per cycle.",
                ref(
                    "Diagnosis and Management of Premature Ovarian Insufficiency",
                    "This approach offers an excellent chance of achieving live birth (>50% per donor oocyte IVF cycle).",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Chronic Anovulation Associated With Pituitary Disorders",
                "A 30-year-old with amenorrhea and galactorrhea on risperidone has prolactin 85 ng/mL. Best initial step?",
                [
                    "Evaluate for medication effect and hypothyroidism; consider pituitary imaging if persistent",
                    "Start estrogen replacement without evaluating prolactin",
                    "Assume PCOS and prescribe metformin only",
                    "Schedule bilateral adrenalectomy",
                ],
                0,
                "Galactorrhea-amenorrhea warrants prolactin evaluation; antipsychotics and hypothyroidism are common reversible causes before assuming prolactinoma.",
                ref(
                    "Approach to the Woman With Reproductive Dysfunction",
                    "Galactorrhea in the absence of a recent history of pregnancy suggests a host of diagnostic possibilities and is frequently a manifestation of excessive prolactin secretion, although it may result from increased sensitivity of breast tissue to the hormones necessary for milk production.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Functional Hypothalamic Amenorrhea",
                "A ballet dancer with FHA refuses to reduce training but has low bone density. Reasonable management?",
                [
                    "Low-dose combined oral contraceptive if no contraindications, plus lifestyle counseling",
                    "Withhold all hormones until menopause",
                    "High-dose testosterone to improve bone density",
                    "Immediate bilateral oophorectomy",
                ],
                0,
                "Hypoestrogenism in FHA risks osteoporosis; OCP is reasonable when lifestyle modification alone fails.",
                ref(
                    "Treatment and Management of Functional Hypothalamic Anovulation",
                    "If the patient is not at risk for thromboembolism, does not smoke cigarettes, and does not have another contraindication for an oral contraceptive, a low-dose combination oral contraceptive is a reasonable replacement option.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Functional Hypothalamic Amenorrhea",
                "A woman with FHA wishes to conceive. Most physiologic ovulation induction?",
                [
                    "Pulsatile intravenous GnRH (~5 µg every 90 minutes)",
                    "Continuous depot GnRH agonist",
                    "High-dose oral estrogen suppression of FSH",
                    "Observation only for 24 months",
                ],
                0,
                "The defect is reduced endogenous GnRH; pulsatile GnRH restores physiologic gonadotropins with high ovulation rates and low OHSS risk.",
                ref(
                    "Treatment and Management of Functional Hypothalamic Anovulation",
                    "Pulsatile intravenous GnRH (5 μg every 90 minutes) was shown to be effective.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Gonadotropin Production in Polycystic Ovary Syndrome",
                "An obese anovulatory woman has normal LH level but clinical hyperandrogenism. Interpretation?",
                [
                    "Low LH does not exclude PCOS—diagnosis rests on androgen excess and oligo-anovulation after exclusions",
                    "Normal LH rules out PCOS definitively",
                    "Elevated LH is mandatory for PCOS diagnosis per NIH criteria",
                    "Obesity always normalizes androgens in PCOS",
                ],
                0,
                "NIH criteria do not require elevated LH; obesity may lower LH despite PCOS.",
                ref(
                    "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                    "A significant number of patients with PCOS do not manifest elevated LH levels or increased LH/FSH ratios.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Insulin Resistance and Polycystic Ovary Syndrome",
                "A PCOS patient has fasting glucose 102 mg/dL and acanthosis nigricans. Best metabolic intervention alongside cycle management?",
                [
                    "Lifestyle modification with weight loss target ≥5% and screen glucose periodically",
                    "Ignore insulin resistance if menses are irregular only",
                    "Start insulin infusion chronically",
                    "Discontinue all hormonal therapy to improve glucose",
                ],
                0,
                "All PCOS patients are at metabolic risk; weight reduction of at least 5% can reduce insulin resistance and androgen excess.",
                ref(
                    "Management of Long-Term Deleterious Effects of Polycystic Ovary Syndrome",
                    "Insulin resistance and androgen excess can be reduced with a weight reduction of at least 5%.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Approach to the Woman With Reproductive Dysfunction",
                "A 26-year-old presents with 2 months amenorrhea. First step in every reproductive-age woman?",
                [
                    "Exclude pregnancy (urine or serum hCG)",
                    "MRI of the pituitary before pregnancy test",
                    "Endometrial biopsy immediately",
                    "Start combined OCP without evaluation",
                ],
                0,
                "Pregnancy is the most common cause of amenorrhea and must be excluded first.",
                ref(
                    "Approach to the Woman With Reproductive Dysfunction",
                    "Pregnancy is the most common cause of amenorrhea (and other menstrual irregularities) in a woman of reproductive age.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Chronic Anovulation",
                "A 35-year-old has amenorrhea, vaginal atrophy, and FSH 68 IU/L. She reports night sweats. Most likely category?",
                [
                    "Premature ovarian insufficiency (hypergonadotropic hypogonadism)",
                    "Functional hypothalamic amenorrhea",
                    "PCOS with androgen excess",
                    "Nonclassic 21-hydroxylase deficiency only",
                ],
                0,
                "High FSH with estrogen deficiency and vasomotor symptoms indicates ovarian insufficiency, not hypothalamic or PCOS phenotypes.",
                ref(
                    "Chronic Anovulation",
                    "Patients with hypothalamic anovulation or galactorrhea-hyperprolactinemia usually do not complain of hot flashes, whereas women with POI present with vasomotor symptoms.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Ovarian Follicle-Stimulating Hormone and Luteinizing Hormone Receptors",
                "A woman with inactivating LH receptor mutation would be expected to have:",
                [
                    "Antral follicles with theca layer but no ovulation or corpora lutea",
                    "Absent primordial follicles identical to Turner syndrome streaks",
                    "Normal ovulatory cycles with isolated low FSH",
                    "Isolated progesterone excess throughout the cycle",
                ],
                0,
                "LH is essential for ovulation and adequate estrogen; LH receptor loss permits antral development but blocks preovulatory maturation.",
                ref(
                    "Ovarian Follicle-Stimulating Hormone and Luteinizing Hormone Receptors",
                    "The ovary contained follicles that developed up to the antral stage with a well-developed theca layer but no preovulatory follicles or corpora lutea.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Regulation of Gonadotropin-Releasing Hormone Secretion",
                "Slower GnRH pulse frequency in the late luteal phase favors:",
                [
                    "Relative FSH secretion over LH",
                    "Massive LH surge for ovulation",
                    "Complete abolition of all gonadotropins permanently",
                    "Progesterone withdrawal bleeding within hours",
                ],
                0,
                "Progesterone slows GnRH pulsatility, biasing gonadotroph output toward FSH—observed in late luteal physiology.",
                ref(
                    "Regulation of Gonadotropin-Releasing Hormone Secretion",
                    "Increased progesterone levels may decrease GnRH pulse frequency and thereby lead to preferential biosynthesis and secretion of FSH, as observed in the late luteal phase.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Ovulation Induction in Polycystic Ovary Syndrome",
                "During clomiphene/letrozole cycles, a PCOS patient develops multiple large follicles and estradiol >2000 pg/mL before hCG. Best OHSS prevention?",
                [
                    "Withhold hCG trigger and cancel or convert cycle",
                    "Administer higher hCG dose to force ovulation",
                    "Start conventional 150 IU daily FSH immediately",
                    "Ignore because OHSS never occurs in PCOS",
                ],
                0,
                "High follicle number and estradiol predict severe OHSS; withholding hCG is key prevention.",
                ref(
                    "Ovulation Induction in Polycystic Ovary Syndrome",
                    "Prevention includes withholding of the hCG injection and intrauterine insemination.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Steroid Production in Polycystic Ovary Syndrome",
                "Why PCOS patients face endometrial cancer risk despite often normal serum estradiol?",
                [
                    "Continuous peripheral conversion of elevated androstenedione to estradiol without cyclic progesterone",
                    "Isolated progesterone excess causing hyperplasia",
                    "Complete estrogen deficiency with atrophic endometrium",
                    "Daily LH suppression eliminating all estrogen",
                ],
                0,
                "Steady-state androgen and androstenedione production fuels ongoing estradiol formation without luteal progesterone opposition.",
                ref(
                    "Steroid Production in Polycystic Ovary Syndrome",
                    "In patients with persistent anovulation, the average daily production of estrogen and androgens is increased and depends on LH stimulation.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Diagnosis and Management of Premature Ovarian Insufficiency",
                "POI patient age 26 with 45,X/46,XX mosaicism and virilization. Critical management concern?",
                [
                    "Risk of gonadal tumor—consider gonadectomy when Y chromosomal material or virilization present",
                    "No imaging or surgery ever indicated after age 20",
                    "Start testosterone for virilization without evaluation",
                    "Defer karyotype—it never changes management",
                ],
                0,
                "Y chromosomal mosaicism and virilization carry significant gonadal tumor risk; karyotype guides surgical decisions in young POI.",
                ref(
                    "Diagnosis and Management of Premature Ovarian Insufficiency",
                    "Secondary virilization in patients with karyotypic abnormalities and POI is associated with a significantly increased risk of a gonadal tumor.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Functional Hypothalamic Amenorrhea",
                "Sudden-onset amenorrhea with new bitemporal hemianopia. Next step?",
                [
                    "MRI of the head to exclude suprasellar mass before labeling FHA",
                    "Reassure as functional hypothalamic amenorrhea without imaging",
                    "Start metformin for presumed PCOS",
                    "Progestin challenge only",
                ],
                0,
                "Neurologic signs or sudden amenorrhea mandate imaging to exclude pituitary/hypothalamic tumor.",
                ref(
                    "Functional Hypothalamic Amenorrhea",
                    "Imaging of the head is especially important if amenorrhea develops suddenly or is associated with a neurologic sign, both of which make the presence of a tumor more likely.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Peptide Gonadotropin-Releasing Hormone Agonists",
                "Clinician starts depot GnRH agonist day 3 of follicular phase for leiomyoma preop. Expected initial effect?",
                [
                    "Transient LH/FSH flare with possible bleeding worsening before downregulation",
                    "Immediate amenorrhea without any gonadotropin rise",
                    "Permanent fertility restoration",
                    "Isolated FSH suppression with LH elevation only",
                ],
                0,
                "Agonists cause an initial flare especially in early follicular phase; luteal-phase or OCP pretreatment avoids this.",
                ref(
                    "Peptide Gonadotropin-Releasing Hormone Agonists",
                    "An initial agonistic action (i.e., flare effect) is associated with an increase in the circulating levels of LH and FSH.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-t1",
                "Gonadotropin-Releasing Hormone",
                "Continuous GnRH exposure can cause anovulation by downregulating pituitary GnRH receptors.",
                True,
                "Both too-slow and continuous GnRH disrupt normal gonadotropin secretion.",
                ref(
                    "Gonadotropin-Releasing Hormone",
                    "Higher frequency or constant exposure to GnRH also gives rise to anovulation by downregulating expression of GnRH receptors, thereby abolishing gonadotropin responses.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Regulation of Gonadotropin-Releasing Hormone Secretion",
                "KISS1R mutations can cause isolated hypogonadotropic hypogonadism.",
                True,
                "Kisspeptin-KISS1R signaling is essential for puberty and reproductive function.",
                ref(
                    "Regulation of Gonadotropin-Releasing Hormone Secretion",
                    "Mutations or knockout of KISS1R produces isolated hypogonadotropic hypogonadism in humans and mice, indicating that signaling through this receptor is essential for sexual development and function.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Ovarian Follicle-Stimulating Hormone and Luteinizing Hormone Receptors",
                "FSH receptors are expressed on ovarian theca cells.",
                False,
                "FSH receptor is exclusive to granulosa cells; LH receptor predominates on theca-interstitial cells.",
                ref(
                    "Ovarian Follicle-Stimulating Hormone and Luteinizing Hormone Receptors",
                    "The FSH receptor is expressed exclusively by granulosa cells.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Corpus Luteum",
                "The corpus luteum is the most active steroidogenic tissue in humans relative to its size.",
                True,
                "It secretes up to ~40 mg progesterone daily in midluteal phase.",
                ref(
                    "Corpus Luteum",
                    "In view of the small size of the corpus luteum, it is the most active steroidogenic tissue in humans.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Functional Hypothalamic Amenorrhea",
                "Women with functional hypothalamic amenorrhea typically report hot flashes similar to menopause.",
                False,
                "FHA patients are hypoestrogenic but usually lack hot flashes, unlike POI.",
                ref(
                    "Functional Hypothalamic Amenorrhea",
                    "These women do not complain of hot flashes, in contrast to women with ovarian insufficiency.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Polycystic Ovary Syndrome",
                "PCOS affects approximately 5% to 10% of reproductive-age women.",
                True,
                "It is the most common androgen-excess anovulation syndrome.",
                ref(
                    "Polycystic Ovary Syndrome",
                    "PCOS is the most common form of chronic anovulation associated with androgen excess; it occurs in perhaps 5% to 10% of reproductive-age women.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                "An elevated LH:FSH ratio is required to diagnose PCOS.",
                False,
                "NIH consensus concluded LH and LH/FSH ratio are not required; many PCOS patients have normal LH.",
                ref(
                    "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                    "The NIH-sponsored consensus conference on diagnostic criteria for PCOS in 1990 recommended that LH and the LH/FSH ratio are not required for the diagnosis of PCOS.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Insulin Resistance and Polycystic Ovary Syndrome",
                "Acanthosis nigricans in hyperandrogenic women is associated with insulin resistance and hyperinsulinemia.",
                True,
                "Skin changes reflect severe insulin resistance in many PCOS patients.",
                ref(
                    "Insulin Resistance and Polycystic Ovary Syndrome",
                    "Acanthosis nigricans in hyperandrogenic women depends on the presence and severity of hyperinsulinemia and insulin resistance.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Premature Ovarian Insufficiency",
                "POI is defined as follicle depletion before age 40 with hypergonadotropic hypogonadism.",
                True,
                "Menopause before 40 with elevated gonadotropins defines POI.",
                ref(
                    "Premature Ovarian Insufficiency",
                    "POI, which is defined as early depletion of ovarian follicles (before the age of 40 years), is a state of hypergonadotropic hypogonadism.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Diagnosis and Management of Premature Ovarian Insufficiency",
                "A single mildly elevated FSH measurement is sufficient to diagnose POI.",
                False,
                "Menopausal FSH (40 IU/L) on at least two occasions is required.",
                ref(
                    "Diagnosis and Management of Premature Ovarian Insufficiency",
                    "Menopausal serum FSH levels (40 IU/L) on at least two occasions are sufficient for the diagnosis of POI.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Chronic Anovulation Associated With Pituitary Disorders",
                "Hyperprolactinemia is a common pituitary cause of anovulation.",
                True,
                "Prolactinomas and other pituitary disorders frequently disrupt gonadotropin secretion.",
                ref(
                    "Chronic Anovulation Associated With Pituitary Disorders",
                    "The most common pituitary-related causes of anovulation are associated with hyperprolactinemia caused by prolactinomas or other functional or anatomic disorders of the pituitary.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Ovulation",
                "In women, LH or hCG is essential to stimulate rupture of the mature follicle.",
                True,
                "Ovulation requires the mid-cycle gonadotropin surge.",
                ref(
                    "Ovulation",
                    "In women, LH or its surrogate, hCG, is essential to stimulate rupture of the mature follicle.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                "Polycystic-appearing ovaries on ultrasound are specific to PCOS and not seen in other causes of anovulation.",
                False,
                "Any persistent anovulation may produce polycystic ovarian morphology—it is not pathognomonic.",
                ref(
                    "Diagnosis of Polycystic Ovary Syndrome and Laboratory Testing",
                    "The typical polycystic-appearing ovary may emerge in a nonspecific fashion when a state of anovulation of any cause persists for any length of time.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Gonadotropin-Releasing Hormone",
                "Assertion: Pulsatile GnRH is required for normal gonadotropin secretion.",
                "Reason: Continuous GnRH infusion downregulates pituitary GnRH receptors and abolishes LH/FSH responses.",
                0,
                "Both true and causally linked—Knobil's experiments established frequency-dependent GnRH action.",
                ref(
                    "Gonadotropin-Releasing Hormone",
                    "Knobil demonstrated in a pioneering series of experiments that normal gonadotropin secretion requires pulsatile GnRH discharge within a critical frequency and amplitude.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Two-Cell Theory for Ovarian Steroidogenesis",
                "Assertion: Ovarian estradiol production in the preovulatory follicle requires both LH and FSH.",
                "Reason: LH stimulates androstenedione in theca cells that granulosa aromatase converts to estrogen.",
                0,
                "Both true—the two-cell, two-gonadotropin model explains follicular estradiol synthesis.",
                ref(
                    "Two-Cell Theory for Ovarian Steroidogenesis",
                    "Ovarian steroidogenesis in the preovulatory follicle takes place through LH receptors on theca cells and FSH (possibly also LH) receptors on granulosa cells.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Overview of the Hormonal Changes During the Ovarian Cycle",
                "Assertion: The mid-cycle LH surge is triggered by rising estradiol.",
                "Reason: Progesterone from the corpus luteum causes the LH surge in the follicular phase.",
                2,
                "Assertion true; reason false—estradiol positive feedback drives the preovulatory LH surge; progesterone rises after ovulation.",
                ref(
                    "Overview of the Hormonal Changes During the Ovarian Cycle",
                    "A positive feedback response at the level of the anterior pituitary and possibly at the hypothalamus results in the mid-cycle surge of LH that is necessary for expulsion of the egg and formation of the corpus luteum.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Chronic Anovulation",
                "Assertion: Low FSH helps distinguish hypothalamic amenorrhea from ovarian insufficiency.",
                "Reason: Ovarian insufficiency presents with low FSH and hot flashes.",
                2,
                "Assertion true; reason false—POI has high FSH and vasomotor symptoms; low FSH suggests hypothalamic/PCOS/hyperprolactinemia.",
                ref(
                    "Chronic Anovulation",
                    "An undetectable or low-normal FSH level is consistent with hypothalamic amenorrhea, PCOS, or hyperprolactinemia, whereas high FSH levels suggest ovarian insufficiency.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Functional Hypothalamic Amenorrhea",
                "Assertion: Functional hypothalamic amenorrhea is a diagnosis of exclusion.",
                "Reason: Neuroanatomic and genetic disorders can mimic FHA and must be ruled out.",
                0,
                "Both true—Box 15.1 lists structural and genetic mimics requiring evaluation.",
                ref(
                    "Functional Hypothalamic Amenorrhea",
                    "The diagnosis is one of exclusion.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Polycystic Ovary Syndrome",
                "Assertion: PCOS increases endometrial cancer risk.",
                "Reason: Chronic anovulation causes unopposed estradiol exposure of the endometrium.",
                0,
                "Both true—continuous peripheral estrogen formation without progesterone drives hyperplasia risk.",
                ref(
                    "Polycystic Ovary Syndrome",
                    "The endometrium of the patient with PCOS must be evaluated by biopsy because long-term unopposed estrogen stimulation leaves these patients at increased risk for endometrial cancer.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Gonadotropin Production in Polycystic Ovary Syndrome",
                "Assertion: Women with PCOS often have elevated LH.",
                "Reason: Chronic progesterone excess increases hypothalamic opioid tone and suppresses GnRH-LH pulsatility.",
                2,
                "Assertion true; reason false—absence of progesterone from anovulation reduces opioid inhibition and accelerates GnRH-LH pulses in PCOS.",
                ref(
                    "Gonadotropin Production in Polycystic Ovary Syndrome",
                    "The enhanced pulsatile secretion of GnRH has been attributed to a reduction in hypothalamic opioid inhibition caused by the chronic absence of progesterone.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Insulin Resistance and Polycystic Ovary Syndrome",
                "Assertion: Insulin resistance contributes to hyperandrogenism in PCOS.",
                "Reason: Hyperinsulinemia augments ovarian androgen production and lowers SHBG.",
                0,
                "Both true—insulin acts on theca cells and liver to worsen androgen bioavailability.",
                ref(
                    "Insulin Resistance and Polycystic Ovary Syndrome",
                    "Insulin increases free testosterone levels in PCOS by two mechanisms: increasing ovarian secretion of testosterone precursors (e.g., androstenedione) and suppressing SHBG.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Premature Ovarian Insufficiency",
                "Assertion: POI should be suspected in women under 40 with amenorrhea and hot flashes.",
                "Reason: POI is a hypogonadotropic hypogonadal state.",
                2,
                "Assertion true; reason false—POI is hypergonadotropic hypogonadism with elevated FSH.",
                ref(
                    "Premature Ovarian Insufficiency",
                    "POI, which is defined as early depletion of ovarian follicles (before the age of 40 years), is a state of hypergonadotropic hypogonadism.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Ovulation Induction in Polycystic Ovary Syndrome",
                "Assertion: Letrozole is preferred over clomiphene for ovulation induction in PCOS.",
                "Reason: Randomized data show higher live-birth rates with letrozole than clomiphene.",
                0,
                "Both true—letrozole is first-line despite off-label status.",
                ref(
                    "Ovulation Induction in Polycystic Ovary Syndrome",
                    "In a randomized study, as compared with clomiphene (50 mg/day), letrozole (2.5 mg/day) was associated with higher rates of live birth and ovulation among infertile women with PCOS.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Regulation of Gonadotropin-Releasing Hormone Secretion",
                "Assertion: Endogenous opioids can suppress GnRH secretion in hypothalamic amenorrhea.",
                "Reason: Naloxone decreases LH pulse frequency in women with hypothalamic amenorrhea.",
                2,
                "Assertion true; reason false—naloxone increases LH pulse frequency, indicating increased opioid tone was inhibiting GnRH.",
                ref(
                    "Functional Hypothalamic Amenorrhea",
                    "Blockade of endogenous opiate receptors by the administration of naloxone, an opiate antagonist, causes an increase in the frequency and amplitude of pulsatile LH release in the majority of women with hypothalamic amenorrhea.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Chronic Anovulation Associated With Pituitary Disorders",
                "Assertion: Hyperprolactinemia can cause anovulation.",
                "Reason: Elevated prolactin suppresses GnRH pulsatility and gonadotropin secretion.",
                0,
                "Both true—prolactinomas and other causes of hyperprolactinemia commonly disrupt the reproductive axis.",
                ref(
                    "Chronic Anovulation Associated With Pituitary Disorders",
                    "These disorders are frequently associated with dysregulation of gonadotropin secretion.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "15",
        "title": "Physiology and Pathology of the Female Reproductive Axis",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Serdar E. Bulun and Elnur Babayev",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_15_Physiology_and_Pathology_of_the_Female_Reproductive_Axis.md",
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
