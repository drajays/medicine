"""ESAP 2021 modules e21-25 (gonadotroph adenomas), e21-26 (transition), e21-27 (pediatric bone)."""
from __future__ import annotations

from build_endo_esap_modules import ar, mcq, note, ref, tf


def build_chapter_25() -> dict:
    p = "e21-25"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Epidemiology",
                "Why functioning gonadotroph adenomas are easily missed",
                "More than 80% of clinically nonfunctioning adenomas are gonadotroph tumors, but only 3–13% function with gonadal hyperstimulation—lack of familiarity causes diagnostic delay.",
                ref(
                    "Main Conclusions",
                    "More than 80% of clinically nonfunctioning pituitary adenomas are gonadotroph adenomas.",
                ),
            ),
            note(
                f"{p}-n2",
                "OHSS pattern",
                "How FSH-secreting adenomas mimic PCOS—and how they differ",
                "Spontaneous OHSS shows increased or normal FSH with invariably low LH and very high estradiol—opposite of PCOS where LH is elevated with smaller follicles.",
                ref(
                    "Biochemical Evaluation",
                    "LH levels are invariably low. This is the opposite gonadotropin pattern of that observed in polycystic ovary syndrome.",
                ),
            ),
            note(
                f"{p}-n3",
                "Treatment",
                "Why surgery is first-line for functioning gonadotroph adenomas",
                "Transsphenoidal removal rapidly lowers FSH, estradiol, and ovarian cysts within days—cabergoline effects are transient and must not delay surgery.",
                ref(
                    "Main Conclusions",
                    "Surgical removal of the pituitary adenoma is the treatment of choice, as it leads to a rapid fall in FSH levels and thus, in case of OHSS, reversal of ovarian hyperstimulation",
                ),
            ),
            note(
                f"{p}-n4",
                "GnRH agonist danger",
                "Pitfall: GnRH agonists in undiagnosed gonadotroph adenomas",
                "GnRH agonists can trigger pituitary apoplexy and are not recommended—they may persistently stimulate FSH secretion from FSH-secreting tumors.",
                ref(
                    "Main Conclusions",
                    "GnRH agonists are not recommended, as they may be responsible for pituitary apoplexy.",
                ),
            ),
            note(
                f"{p}-n5",
                "Spontaneous OHSS",
                "Spontaneous ovarian hyperstimulation as presenting feature",
                "Premenopausal women present with amenorrhea, pelvic pain, and large multicystic ovaries on ultrasound—always consider pituitary MRI even without chiasmal compression.",
                ref(
                    "Hyperstimulation Syndromes",
                    "Spontaneous OHSS is the most typical picture in premenopausal women.",
                ),
            ),
            note(
                f"{p}-n6",
                "Stalk effect",
                "Mild hyperprolactinemia from pituitary stalk compression",
                "Stalk compression disinhibits dopamine tone—prolactin rises but stays below 150–200 ng/mL, distinguishing from macroprolactinomas where levels correlate with tumor size.",
                ref(
                    "Mass Effects",
                    "prolactin serum levels are always below 150 to 200 ng/mL (<6.5-8.7 nmol/L). This distinguishes them from macroprolactinomas",
                ),
            ),
            note(
                f"{p}-n7",
                "Pathology",
                "Gonadotroph adenoma immunocytochemistry patterns",
                "Cells are chromophobic with low gonadotropin-positive fraction (<20–30%); some express β-FSH, β-LH, or α-subunit; SF-1 marks null-cell gonadotroph lineage.",
                ref(
                    "Pathology",
                    "The percentage of cells positive for gonadotropin antibodies ranges from 100% to a few islands, but it is usually low (<20%-30%).",
                ),
            ),
            note(
                f"{p}-n8",
                "Apoplexy",
                "Pituitary apoplexy presentation in gonadotroph adenomas",
                "Sudden headache, meningismus, visual changes, and ophthalmoplegia may be spontaneous or triggered by stimulation tests or GnRH analogues.",
                ref(
                    "Pituitary Apoplexy",
                    "Apoplexy may be triggered by stimulation tests or injection of GnRH analogues.",
                ),
            ),
            note(
                f"{p}-n9",
                "Case 1 outcome",
                "How surgery reverses OHSS biochemically within days",
                "Case illustrates FSH fall from 11.6 to 1.4 mIU/mL and estradiol from 3242 to 98 pg/mL by day 3 postoperatively with cyst regression and subsequent spontaneous pregnancy.",
                ref(
                    "Case 1",
                    "Correction of the FSH excess allows for rapid resolution of ovarian cysts and pituitary mass effect if present.",
                ),
            ),
            note(
                f"{p}-n10",
                "Medical therapy",
                "Limited role of cabergoline in functioning gonadotroph adenomas",
                "Cabergoline may transiently lower FSH and estradiol and allow pregnancy in some reports, but surgery must not be delayed.",
                ref(
                    "Medical Management",
                    "the effect is generally transient and surgery must not be delayed.",
                ),
            ),
            note(
                f"{p}-n11",
                "Stimulation tests",
                "Why TRH/GnRH stimulation tests are no longer recommended",
                "Tests are neither sensitive nor specific for gonadotroph adenomas and can precipitate apoplexy.",
                ref(
                    "Biochemical Evaluation",
                    "these tests are neither sensitive nor specific for indicating the gonadotroph nature of nonfunctioning pituitary adenomas.",
                ),
            ),
            note(
                f"{p}-n12",
                "Differential",
                "How to distinguish FSH adenoma OHSS from McCune-Albright and granulosa-cell tumor",
                "McCune-Albright has low gonadotropins with autonomous ovarian estrogen; granulosa-cell tumors suppress gonadotropins; FSH adenoma shows low LH with high estradiol.",
                ref(
                    "Case 1",
                    "their gonadotropins are low, suppressed by the very high levels of estrogens autonomously produced by the ovarian cysts",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "A woman with macroadenoma, estradiol 3241 pg/mL, LH <0.1, FSH 11.6, and large ovarian cysts with torsion has:",
                [
                    "Polycystic ovary syndrome",
                    "OHSS related to FSH-secreting adenoma",
                    "McCune-Albright syndrome",
                    "Ovarian granulosa-cell tumor",
                ],
                1,
                "Spontaneous OHSS with pituitary mass and low LH/high estradiol indicates FSH-secreting gonadotroph adenoma.",
                ref(
                    "Case 1",
                    "Answer: B) OHSS related to FSH-secreting adenoma",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "After GnRH agonist injection, a man develops headache, third-nerve palsy, and FSH 9.2 with low LH and testosterone. Correct statements include:",
                [
                    "No relationship between GnRH and pituitary events",
                    "GnRH agonist triggered pituitary apoplexy",
                    "Hormonal pattern typical of gonadotroph adenoma",
                    "Pattern is typical GnRH flare-up in normal pituitary only",
                ],
                1,
                "Answers B and C—apoplexy triggered by GnRH agonist with gonadotroph hormonal pattern.",
                ref(
                    "Case 2",
                    "Answer: B and C) The injection of GnRH analogue triggered pituitary apoplexy and the hormonal pattern in this patient is typical of a gonadotroph adenoma.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Biochemistry",
                "In functioning gonadotroph adenoma OHSS, typical gonadotropin pattern is:",
                [
                    "High LH, low FSH",
                    "High FSH or normal FSH with low LH",
                    "Low FSH and high LH",
                    "Suppressed FSH and LH",
                ],
                1,
                "FSH may be elevated or normal; LH is invariably low.",
                ref(
                    "Biochemical Evaluation",
                    "FSH levels are increased in more than half of OHSS cases due to gonadotroph adenomas, but they can be also in the normal range (in the other half). However, LH levels are invariably low.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Treatment",
                "First-line treatment for functioning FSH-secreting pituitary adenoma with OHSS is:",
                [
                    "GnRH agonist therapy",
                    "Transsphenoidal adenomectomy",
                    "Cabergoline monotherapy without surgery",
                    "Bilateral oophorectomy",
                ],
                1,
                "Surgery is treatment of choice; GnRH agonists are contraindicated.",
                ref(
                    "Surgical Treatment",
                    "Surgical removal of the culprit pituitary adenoma is the treatment of choice",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Prevalence",
                "Functioning gonadotroph adenomas represent what fraction of nonfunctioning/gonadotroph adenomas?",
                [
                    "50–60%",
                    "3–13%",
                    "80–90%",
                    "<1%",
                ],
                1,
                "Majority of NFPA are gonadotroph; only minority function clinically.",
                ref(
                    "Epidemiology",
                    "They represent a minority (3%-13%) of nonfunctioning pituitary adenomas/gonadotroph adenomas.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "PCOS distinction",
                "Compared with PCOS, FSH adenoma OHSS typically has:",
                [
                    "Smaller follicles <10 mm and elevated LH",
                    "Large cysts, very high estradiol, and low LH",
                    "High testosterone and normal estradiol",
                    "Low estradiol with high LH:FSH ratio",
                ],
                1,
                "PCOS has small follicles and elevated LH; FSH adenoma causes massive cysts and estradiol.",
                ref(
                    "Case 1",
                    "multiple follicles in women with polycystic ovary syndrome are much smaller (<10 mm) and the hormonal pattern is quite different in terms of LH and FSH levels",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Prolactin",
                "Stalk compression hyperprolactinemia in macroadenoma typically shows prolactin:",
                [
                    ">1000 ng/mL proportional to size",
                    "Below 150–200 ng/mL",
                    "Undetectable always",
                    "Only elevated postpartum",
                ],
                1,
                "Stalk effect causes mild elevation, not macroprolactinoma levels.",
                ref(
                    "Mass Effects",
                    "prolactin serum levels are always below 150 to 200 ng/mL",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Complications",
                "OHSS from FSH adenoma may be complicated by:",
                [
                    "Adnexal torsion requiring detorsion",
                    "Isolated hypokalemia only",
                    "Primary adrenal insufficiency",
                    "Diabetes insipidus only",
                ],
                0,
                "Case 1 had ovarian torsion requiring laparoscopic detorsion.",
                ref(
                    "Case 1",
                    "OHSS can be complicated by ovarian torsion, as seen in this case, justifying surgical detorsion.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Men",
                "In men, functioning FSH-secreting adenomas may present with:",
                [
                    "Macroorchidism",
                    "Primary testicular failure with high LH",
                    "Isolated hyperprolactinemia only",
                    "Cushing syndrome",
                ],
                0,
                "Macroorchidism is described in very few male cases.",
                ref(
                    "Hyperstimulation Syndromes",
                    "In men, macroorchidism has been described in very few cases.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Postmenopausal",
                "In postmenopausal women, increased FSH with low LH and low other pituitary hormones suggests:",
                [
                    "Primary ovarian failure",
                    "Gonadotroph adenoma preoperatively",
                    "Normal menopause only",
                    "Prolactinoma",
                ],
                1,
                "Paradoxical FSH elevation with low LH aids preoperative diagnosis.",
                ref(
                    "Biochemical Evaluation",
                    "The hormonal pattern of increased FSH contrasting with low LH levels and generally low levels of all pituitary hormones in postmenopausal women can help with the preoperative diagnosis of a gonadotroph adenoma.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Cabergoline",
                "Cabergoline in functioning gonadotroph adenoma:",
                [
                    "Replaces surgery as definitive therapy",
                    "May transiently lower FSH but must not delay surgery",
                    "Is contraindicated in all cases",
                    "Causes permanent cure in all patients",
                ],
                1,
                "Medical effect is generally transient.",
                ref(
                    "Medical Management",
                    "However, the effect is generally transient and surgery must not be delayed.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Children",
                "Functioning gonadotroph adenomas in children may rarely cause:",
                [
                    "Precocious puberty",
                    "Permanent hypothyroidism only",
                    "Neonatal DI only",
                    "Growth hormone deficiency only",
                ],
                0,
                "Isosexual precocious puberty has been rarely described.",
                ref(
                    "Hyperstimulation Syndromes",
                    "Isosexual precocious puberty has also very rarely been described in both sexes.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Imaging",
                "In spontaneous OHSS, pituitary MRI should be performed because:",
                [
                    "All patients have optic chiasm compression",
                    "Adenoma size is variable and microadenomas may lack mass effects",
                    "MRI is only needed after oophorectomy",
                    "Ultrasound alone confirms FSH adenoma",
                ],
                1,
                "MRI detects adenoma even when mass effects absent; size varies widely.",
                ref(
                    "Case 1",
                    "With microadenomas, mass effects may not be present at time of diagnosis.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Surgery",
                "Postoperative FSH decline can normalize estradiol and resolve ovarian cysts within days.",
                True,
                "Case 1 table shows rapid biochemical and clinical improvement.",
                ref(
                    "Surgical Treatment",
                    "this is achieved in a few days postoperatively.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "GnRH agonist",
                "GnRH agonists are recommended to lower FSH before surgery in OHSS.",
                False,
                "GnRH agonists may cause apoplexy and are not recommended.",
                ref(
                    "Medical Management",
                    "GnRH agonists are not recommended, as they may be responsible for pituitary apoplexy.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "NFPA",
                "Most clinically nonfunctioning pituitary adenomas are gonadotroph adenomas on immunocytochemistry.",
                True,
                "Greater than 80% are gonadotroph lineage.",
                ref(
                    "Background",
                    "greater than 80% of them are gonadotroph.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Stimulation tests",
                "TRH and GnRH stimulation tests are sensitive and specific for gonadotroph adenomas.",
                False,
                "Neither sensitive nor specific; can trigger apoplexy.",
                ref(
                    "Biochemical Evaluation",
                    "these tests are neither sensitive nor specific",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Pregnancy",
                "Spontaneous pregnancy has been achieved after surgery for functioning gonadotroph adenoma.",
                True,
                "Case 1 achieved pregnancy 5 months postoperatively.",
                ref(
                    "Surgical Treatment",
                    "Pregnancy has been achieved shortly after the operation in a few cases",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Estradiol",
                "In most OHSS cases from FSH adenomas, estradiol levels are high or very high.",
                True,
                "Biochemical evaluation section states this.",
                ref(
                    "Biochemical Evaluation",
                    "In most cases of OHSS, estradiol levels are high or very high.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Demographics",
                "Functioning gonadotroph adenomas are more often described in women of reproductive age.",
                True,
                "Very rarely in men; reproductive-age women predominate.",
                ref(
                    "Epidemiology",
                    "functioning gonadotroph adenomas are more often described in women of reproductive age (very rarely in men).",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Basic FSH isoforms",
                "Gonadotroph adenomas may produce more basic FSH isoforms considered more biologically active.",
                True,
                "Chromatofocusing studies support this paradox.",
                ref(
                    "Gonadal Hyperstimulation",
                    "gonadotroph adenomas produce more basic FSH isoforms, which, paradoxically, are considered to be more biologically active.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "OHSS",
                "Assertion: Spontaneous OHSS in a premenopausal woman should prompt pituitary MRI.",
                "Reason: FSH-secreting adenomas may present without optic chiasm compression or visual field defects.",
                0,
                "Both true—case 1 emphasizes MRI even without mass effects.",
                ref(
                    "Case 1",
                    "The finding of OHSS should lead to pituitary MRI, even in the absence of pituitary mass effects.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "GnRH danger",
                "Assertion: GnRH agonists can trigger pituitary apoplexy in gonadotroph adenomas.",
                "Reason: GnRH agonists always suppress FSH permanently in gonadotroph adenomas like normal pituitary.",
                2,
                "Assertion true; they may have persistent stimulatory effect on FSH-secreting tumors.",
                ref(
                    "Case 2",
                    "they may have a persistent stimulatory effect on tumor secretion in patients with FSH-secreting pituitary adenomas.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Surgery",
                "Assertion: Transsphenoidal surgery rapidly reverses ovarian hyperstimulation in FSH adenoma OHSS.",
                "Reason: Surgery lowers FSH and estradiol within days with cyst regression.",
                0,
                "Both true—mechanism and timeline from case 1.",
                ref(
                    "Surgical Treatment",
                    "rapidly produces a fall in FSH levels and thus, in the case of OHSS, decreases ovarian stimulation, which is associated with rapid diminution of estradiol levels and regression of ovarian cysts",
                ),
            ),
            ar(
                f"{p}-ar4",
                "PCOS",
                "Assertion: PCOS can be distinguished from FSH adenoma OHSS by follicle size and LH level.",
                "Reason: PCOS typically has large ovarian cysts and very high estradiol.",
                2,
                "Assertion true; reason describes FSH adenoma, not PCOS.",
                ref(
                    "Case 1",
                    "multiple follicles in women with polycystic ovary syndrome are much smaller (<10 mm)",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Cabergoline",
                "Assertion: Cabergoline may be used as sole definitive therapy for functioning gonadotroph adenoma.",
                "Reason: Cabergoline effects are generally transient and surgery must not be delayed.",
                2,
                "Assertion false; reason correctly limits medical therapy.",
                ref(
                    "Medical Management",
                    "the effect is generally transient and surgery must not be delayed.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Prolactin",
                "Assertion: Stalk compression can cause mild hyperprolactinemia below 150–200 ng/mL.",
                "Reason: This prolactin level pattern is identical to macroprolactinoma proportional to tumor size.",
                2,
                "Assertion true; macroprolactinomas cause much higher levels.",
                ref(
                    "Mass Effects",
                    "This distinguishes them from macroprolactinomas, which are associated with much higher prolactin levels, proportional to tumor size.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Apoplexy",
                "Assertion: Pituitary apoplexy may be the presenting feature of gonadotroph adenomas.",
                "Reason: Apoplexy only occurs after radiation therapy.",
                2,
                "Assertion true; apoplexy may be spontaneous or triggered.",
                ref(
                    "Pituitary Apoplexy",
                    "Pituitary apoplexy can be the presenting feature of gonadotroph adenomas",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Hypogonadism paradox",
                "Assertion: Gonadotroph adenomas often cause hypogonadism despite producing gonadotropins.",
                "Reason: Abnormal glycosylation may reduce biological activity of adenoma-secreted gonadotropins.",
                0,
                "Both true—explains nonfunctioning majority vs rare functioning cases.",
                ref(
                    "Gonadal Hyperstimulation",
                    "hypogonadism may thus be related to decreased biological activity of gonadotropins related to abnormal glycosylation of the isoforms produced by the adenoma.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "25",
        "title": "Treatment of Functioning Gonadotroph Pituitary Adenomas",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Philippe Chanson, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_25_Treatment_of_Functioning_Gonadotroph_Pituitary_Adenomas.md",
        "items": items,
    }


def build_chapter_26() -> dict:
    p = "e21-26"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Variable course",
                "Why hypopituitarism requires lifelong vigilance",
                "Deficits may evolve from isolated GH deficiency to combined pituitary hormone deficiency—regular testing is needed across childhood, adolescence, and adulthood.",
                ref(
                    "Main Conclusions",
                    "The condition may evolve throughout adolescence and childhood, and hence there is a need for vigilance and regular testing of pituitary function on a lifelong basis.",
                ),
            ),
            note(
                f"{p}-n2",
                "Transition",
                "How to manage hypopituitarism at adolescent transition",
                "Transition clinics with pediatric and adult endocrinologists plus nurse specialists address adherence, puberty/fertility concerns, high-risk behaviors, and re-evaluation of hormone needs.",
                ref(
                    "Management at Transition",
                    "Transition clinics with input from pediatric/adolescent endocrinologists, adult endocrinologists, and the endocrinology clinical nurse specialist are critical to the successful transition of patients.",
                ),
            ),
            note(
                f"{p}-n3",
                "GH retesting",
                "When childhood-onset GH deficiency does not need retesting",
                "Retesting is not required with ≥2 pituitary hormone deficiencies, confirmed genetic cause, or structural defect (except isolated ectopic posterior pituitary)—25–88% may reverse isolated idiopathic GHD.",
                ref(
                    "Treatment",
                    "retesting is not required for those with more than 2 pituitary hormone deficiencies, a confirmed genetic pathogenic variant accounting for the hypopituitarism, and/or a specific hypothalamic-pituitary structural defect on MRI with the exception of an ectopic posterior pituitary.",
                ),
            ),
            note(
                f"{p}-n4",
                "Central hypothyroidism",
                "How to diagnose secondary hypothyroidism without TRH test",
                "Low free T4 with inappropriately normal or low TSH is sufficient—TRH stimulation does not change management.",
                ref(
                    "Diagnosis",
                    "a low concentration of free T₄ in the presence of an inappropriately low or normal concentration of TSH is sufficient for the diagnosis of secondary or tertiary hypothyroidism",
                ),
            ),
            note(
                f"{p}-n5",
                "ACTH masking DI",
                "Why central diabetes insipidus may appear only after starting glucocorticoids",
                "Cortisol sufficiency is required for renal free water clearance via inhibition of ADH—ACTH deficiency masks coexistent DI until hydrocortisone is started.",
                ref(
                    "Diagnosis",
                    "ACTH deficiency may mask coexistent central diabetes insipidus until glucocorticoid replacement is initiated.",
                ),
            ),
            note(
                f"{p}-n6",
                "Hydrocortisone transition",
                "How to counsel adolescents on hydrocortisone timing and sick-day rules",
                "Dose at least 3× daily; double/triple during illness; emergency IM hydrocortisone (25 mg <1 yr, 25–50 mg 1–5 yr, 100 mg >5 yr); discuss alcohol and late sleep schedules.",
                ref(
                    "Treatment",
                    "Doses should be doubled or even tripled in the face of illness, with patient education on how and when to administer emergency intramuscular hydrocortisone",
                ),
            ),
            note(
                f"{p}-n7",
                "Puberty timing",
                "Puberty in hypopituitarism: septo-optic dysplasia versus combined deficiency",
                "Septo-optic dysplasia may have normal or precocious puberty; isolated combined pituitary hormone deficiency more often has delayed or absent puberty.",
                ref(
                    "Treatment",
                    "Puberty may be precocious or occur at the normal time in those with hypopituitarism associated with septo-optic dysplasia, but it may be delayed or absent in those with isolated combined pituitary hormone deficiency.",
                ),
            ),
            note(
                f"{p}-n8",
                "MRI predictors",
                "MRI predictors of combined pituitary hormone deficiency in congenital hypopituitarism",
                "Ectopic posterior pituitary carries 27-fold higher hypopituitarism risk; stalk agenesis and corpus callosum abnormalities predict combined deficiency over isolated GHD.",
                ref(
                    "Diagnosis",
                    "the risk of hypopituitarism was 27 times greater in patients with an ectopic posterior pituitary.",
                ),
            ),
            note(
                f"{p}-n9",
                "PROP1",
                "Why PROP1 testing matters for suprasellar masses",
                "PROP1 pathogenic variants can cause suprasellar masses that spontaneously resolve—genetic diagnosis may avoid unnecessary surgery.",
                ref(
                    "Diagnosis",
                    "PROP1 pathogenic variants are associated with suprasellar masses that undergo spontaneous resolution, and the presence of a PROP1 pathogenic variant may help to reassure families of the absence of a brain tumor and circumvent the need for surgery.",
                ),
            ),
            note(
                f"{p}-n10",
                "DDAVP caution",
                "How to start desmopressin safely in central DI",
                "Titrate using paired plasma and urine osmolalities inpatient; err on underdosing—overdose causes hyponatremia and dangerous fluid shifts; warn about MDMA and overdrinking.",
                ref(
                    "Treatment",
                    "Treatment should generally err on the side of underdosing, since overdosing DDAVP can result in water intoxication, hyponatremia, and rapid fluid shifts",
                ),
            ),
            note(
                f"{p}-n11",
                "Case 1 genetics",
                "POU1F1 mutations cause GH, TSH, and prolactin deficiencies",
                "Dominant-negative POU1F1 (e.g., p.R271W) affects somatotroph, thyrotroph, and lactotroph development—not ACTH or gonadotropins; MRI shows small anterior pituitary with normal posterior pituitary.",
                ref(
                    "Case 1",
                    "Pathogenic variants are associated with GH, TSH, and prolactin deficiencies, but not ACTH or gonadotropin deficiencies.",
                ),
            ),
            note(
                f"{p}-n12",
                "Case 2 ectopic PP",
                "Why fatigue in a teen with ectopic posterior pituitary needs full axis reassessment",
                "Ectopic posterior pituitary strongly predicts evolving combined deficiency—reassess GH dose, cortisol, and thyroid when new symptoms appear at puberty.",
                ref(
                    "Case 2",
                    "With an ectopic posterior pituitary, this patient would most likely have developed other hormone deficiencies.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "A patient with GH, TSH, and prolactin deficiencies and small anterior pituitary most likely has a variant in:",
                [
                    "KAL1",
                    "LHX4",
                    "PROP1",
                    "POU1F1",
                ],
                3,
                "POU1F1 (PIT1) affects GH, TSH, PRL—not ACTH or gonadotropins.",
                ref(
                    "Case 1",
                    "Answer: D)POU1F1",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "A 15-year-old girl with ectopic posterior pituitary and fatigue on GH therapy. Best next steps include:",
                [
                    "Restart ethinyl estradiol only",
                    "Assess GH dose, cortisol, and thyroid function and evaluate comorbidities",
                    "Stop all hormones permanently",
                    "Immediate brain biopsy",
                ],
                1,
                "Answer E (B, C, D)—optimize GH, test axes, evaluate associated conditions.",
                ref(
                    "Case 2",
                    "Answer: E) B, C, and D",
                ),
            ),
            mcq(
                f"{p}-q3",
                "GH retesting",
                "GH retesting at transition is NOT required if the patient has:",
                [
                    "Idiopathic isolated GHD only",
                    "Ectopic posterior pituitary only as structural defect",
                    "Confirmed PROP1 pathogenic variant",
                    "Single hormone deficiency and normal MRI",
                ],
                2,
                "Genetic confirmation or ≥2 deficiencies or structural defect (except ectopic PP alone) exempts retesting.",
                ref(
                    "Treatment",
                    "retesting is not required for those with more than 2 pituitary hormone deficiencies, a confirmed genetic pathogenic variant",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Hypothyroidism",
                "Levothyroxine dosing in central hypothyroidism should be guided by:",
                [
                    "TSH target in lower normal range",
                    "Free T4 maintained in upper half of normal range",
                    "Total T3 only",
                    "Thyrotropin-releasing hormone stimulation results",
                ],
                1,
                "TSH is unreliable; free T4 guides therapy, especially with hypothalamic obesity risk.",
                ref(
                    "Treatment",
                    "Free T₄ concentrations should be maintained in the upper half of the normal range",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Emergency steroid",
                "Emergency IM hydrocortisone dose for a child older than 5 years is:",
                [
                    "25 mg",
                    "50 mg",
                    "100 mg",
                    "250 mg",
                ],
                2,
                "Age-stratified emergency dosing: 100 mg for >5 years.",
                ref(
                    "Treatment",
                    "emergency intramuscular hydrocortisone (doses <1 year, 25 mg; 1-5 years, 25-50 mg; >5 years, 100 mg)",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Gonadotropin testing",
                "Testing for hypogonadotropic hypogonadism is most informative:",
                [
                    "At age 3 years routinely",
                    "During mini-puberty or pubertal ages (>8 girls, >9 boys)",
                    "Only after age 25",
                    "Never—always empiric steroids",
                ],
                1,
                "HP-gonadal axis is quiescent outside mini-puberty and puberty.",
                ref(
                    "Diagnosis",
                    "Testing for hypogonadotropic hypogonadism is not useful outside of the mini-puberty (up to age 6 months) and pubertal phases (boys aged >9 years, girls aged >8 years)",
                ),
            ),
            mcq(
                f"{p}-q7",
                "CPHD evolution",
                "In idiopathic childhood isolated GHD followed ≥3.5 years, additional pituitary deficiencies developed in:",
                [
                    "0.5%",
                    "5.5%",
                    "25%",
                    "50%",
                ],
                1,
                "GeNeSIS data: 5.5% developed additional deficiencies in long follow-up.",
                ref(
                    "Evolution of Endocrinopathies",
                    "Combined pituitary hormone deficiency developed in 2.0% of the overall cohort and in 5.5% among children followed for a minimum of 3.5 years.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Estrogen route",
                "In female hypogonadotropic hypogonadism, preferred estrogen replacement emphasizes:",
                [
                    "High-dose oral ethinyl estradiol first",
                    "17β-estradiol with transdermal route favored for bone accrual",
                    "No estrogen until age 21",
                    "Testosterone instead of estrogen",
                ],
                1,
                "Transdermal 17β-estradiol may be superior for bone and uterine growth with lower genotoxic metabolites.",
                ref(
                    "Treatment",
                    "It has been suggested that the transdermal route is superior to the oral route in terms of bone accrual and uterine growth.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Transition risks",
                "Loss to follow-up after transition most risks:",
                [
                    "Isolated acne",
                    "Adrenal crisis and untreated hypothyroidism",
                    "Excess height gain",
                    "Precocious puberty only",
                ],
                1,
                "Nonadherence risks adrenal crisis, hypothyroidism, low BMD, fatigue, low libido.",
                ref(
                    "Management at Transition",
                    "Loss to follow-up by a physician may be associated with the risk of adrenal crisis, a hypothyroid state, reduced bone mineral density, and fatigue with reduced libido.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Congenital incidence",
                "Reported incidence of congenital hypopituitarism is approximately:",
                [
                    "1 in 4000 to 1 in 10,000 live births",
                    "1 in 100 live births",
                    "1 in 100,000 only",
                    "Unknown—never reported",
                ],
                0,
                "Congenital hypopituitarism is rare but not ultra-rare.",
                ref(
                    "Significance of the Clinical Problem",
                    "Congenital hypopituitarism is a rare disorder and may be congenital (1 in 4000 to 1 in 10,000 live births)",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Craniopharyngioma",
                "In craniopharyngioma, early weight gain may:",
                [
                    "Be unrelated to hypothalamic injury",
                    "Precede diagnosis of suprasellar mass by months and predict hypothalamic obesity",
                    "Indicate excess GH secretion",
                    "Rule out pituitary disease",
                ],
                1,
                "Weight/BMI changes may precede mass diagnosis and predict hypothalamic obesity.",
                ref(
                    "Diagnosis",
                    "in patients with craniopharyngiomas, early changes in weight and BMI have been shown to precede the diagnosis of a suprasellar mass by several months and may be predictive of future hypothalamic obesity.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "GH and tumors",
                "GH replacement in childhood tumor survivors:",
                [
                    "Is absolutely contraindicated",
                    "At replacement doses is not associated with increased recurrence; second neoplasm risk unclear",
                    "Always causes tumor recurrence within 1 year",
                    "Requires doses higher than childhood growth doses lifelong",
                ],
                1,
                "Replacement GH does not increase recurrence; second primary neoplasm signal is uncertain—use minimum effective dose.",
                ref(
                    "Treatment",
                    "GH therapy in replacement dosages is not associated with an increased risk of recurrence or progression, although some evidence suggests that there may be a small increased risk of second primary neoplasms, but this is not completely clear.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Multidisciplinary",
                "Holistic hypopituitarism care at transition should include:",
                [
                    "Endocrinologist only",
                    "Ophthalmology, psychology, dietitian, and nurse specialist among others",
                    "Surgery alone without nursing input",
                    "No psychology until adulthood",
                ],
                1,
                "Main conclusions list multidisciplinary team including ophthalmology, neurodevelopment, nursing, psychology, dietitian, social work.",
                ref(
                    "Main Conclusions",
                    "A holistic approach involves a pediatric and adult (at transition and thereafter) endocrinologist, ophthalmologist, neurodevelopmental pediatrician, clinical nurse specialist, psychologist, dietitian, and social worker.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Reversibility",
                "Pituitary hormone deficits may reverse even with structurally abnormal pituitary glands.",
                True,
                "Main conclusions emphasize reversibility.",
                ref(
                    "Main Conclusions",
                    "Reversibility of pituitary hormone deficits may occur, even in the presence of a structurally abnormal pituitary gland.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Septo-optic",
                "Septo-optic dysplasia may paradoxically have early or normally timed puberty.",
                True,
                "Pubertal timing is highly variable in hypopituitarism.",
                ref(
                    "Main Conclusions",
                    "Paradoxically, in patients with septo-optic dysplasia, it may occur early.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "TRH test",
                "TRH stimulation is required to distinguish secondary from tertiary hypothyroidism in children.",
                False,
                "Low free T4 with low/normal TSH suffices; TRH does not change management.",
                ref(
                    "Diagnosis",
                    "an additional thyrotropin-releasing hormone stimulation test neither distinguishes the 2 nor changes clinical management.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Organic GHD",
                "Organic isolated childhood GHD has higher risk of evolving to CPHD than idiopathic GHD.",
                True,
                "20.7% vs 5.5% in long follow-up subgroups.",
                ref(
                    "Evolution of Endocrinopathies",
                    "there was a higher frequency of combined pituitary hormone deficiency (9.9% in the overall cohort, and 20.7% in the subgroup followed up for a minimum of 3.5 years).",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Levothyroxine",
                "Starting levothyroxine before ruling out ACTH deficiency can unmask central DI.",
                True,
                "Glucocorticoid replacement unmasks ADH axis when cortisol was masking DI.",
                ref(
                    "Treatment",
                    "Before commencing replacement, preexisting ACTH deficiency should be detected to avoid the risk of precipitating a hypocortisolemic crisis.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "GH reversal",
                "Between 25% and 88% of patients may reverse GH secretion at transition retesting.",
                True,
                "Stated in treatment section on retesting.",
                ref(
                    "Treatment",
                    "Between 25% and 88% of patients reverse their GH secretion at the time of transition.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "MDMA risk",
                "MDMA use can be extremely dangerous in patients on desmopressin due to overdrinking risk.",
                True,
                "Recreational overdrinking risk highlighted.",
                ref(
                    "Treatment",
                    "certain \"recreational\" drugs such as MDMA (\"Ecstasy\") may lead to overdrinking, which could be extremely dangerous in patients on desmopressin.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Adherence",
                "Adolescent adherence challenges are a major barrier to optimal hypopituitarism care.",
                True,
                "Listed under barriers to optimal practice.",
                ref(
                    "Barriers to Optimal Practice",
                    "Lack of engagement from the young person.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Lifelong follow-up",
                "Assertion: Hypopituitarism requires lifelong pituitary function monitoring.",
                "Reason: Deficits may evolve from single to multiple hormone deficiencies over time.",
                0,
                "Both true—evolution documented in GeNeSIS and congenital cohorts.",
                ref(
                    "Evolution of Endocrinopathies",
                    "Children with isolated GH deficiency have a significant risk of developing additional pituitary deficiencies.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Ectopic PP",
                "Assertion: Ectopic posterior pituitary on MRI increases risk of hypopituitarism 27-fold.",
                "Reason: Ectopic posterior pituitary is associated with isolated GHD only without other deficits.",
                2,
                "Assertion true; ectopic PP predicts broader hypopituitarism risk.",
                ref(
                    "Diagnosis",
                    "the risk of hypopituitarism was 27 times greater in patients with an ectopic posterior pituitary.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Transition clinic",
                "Assertion: Transition clinics improve outcomes in adolescent hypopituitarism.",
                "Reason: Transition clinics are critical for successful transfer to adult care.",
                0,
                "Both true per management at transition section.",
                ref(
                    "Management at Transition",
                    "Transition clinics with input from pediatric/adolescent endocrinologists, adult endocrinologists, and the endocrinology clinical nurse specialist are critical to the successful transition of patients.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "POU1F1",
                "Assertion: POU1F1 mutations cause GH, TSH, and prolactin deficiencies.",
                "Reason: POU1F1 mutations also cause ACTH and gonadotropin deficiencies.",
                2,
                "Assertion true; ACTH and gonadotropins spared.",
                ref(
                    "Case 1",
                    "Pathogenic variants are associated with GH, TSH, and prolactin deficiencies, but not ACTH or gonadotropin deficiencies.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Central hypothyroidism",
                "Assertion: Low free T4 with low or normal TSH confirms central hypothyroidism.",
                "Reason: TRH stimulation is required before starting levothyroxine.",
                2,
                "Assertion true; TRH not required.",
                ref(
                    "Diagnosis",
                    "a low concentration of free T₄ in the presence of an inappropriately low or normal concentration of TSH is sufficient for the diagnosis",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Puberty induction",
                "Assertion: Delaying sex steroid replacement far beyond usual pubertal age is not generally recommended.",
                "Reason: Long-term bone mineral accrual benefits favor timely pubertal induction.",
                0,
                "Both true—individualized but not excessively delayed.",
                ref(
                    "Treatment",
                    "Delaying commencement of the latter beyond the usual pubertal age (~12 years in girls and 14-15 years in boys) is not generally recommended, given the long-term benefits on bone mineral accretion.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "DDAVP",
                "Assertion: DDAVP dosing should err on the side of underdosing.",
                "Reason: Overdosing causes water intoxication and dangerous rapid fluid shifts.",
                0,
                "Both true—inpatient titration recommended.",
                ref(
                    "Treatment",
                    "overdosing DDAVP can result in water intoxication, hyponatremia, and rapid fluid shifts that are difficult to correct safely",
                ),
            ),
            ar(
                f"{p}-ar8",
                "PROP1",
                "Assertion: PROP1 variants may produce resolving suprasellar masses mimicking tumors.",
                "Reason: All PROP1 patients require immediate craniotomy regardless of genetics.",
                2,
                "Assertion true; genetics may avoid unnecessary surgery—reason false.",
                ref(
                    "Diagnosis",
                    "the presence of a PROP1 pathogenic variant may help to reassure families of the absence of a brain tumor and circumvent the need for surgery.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "26",
        "title": "Management of Pituitary Hormone Replacement Through Transition From Adolescence to Young Adulthood",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Mehul T. Dattani, MBBS, DCH, FRCPCH, FRCP, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_26_Management_of_Pituitary_Hormone_Replacement_Through_Transition_From_Adolescence_to_Young_Adulthood.md",
        "items": items,
    }


def build_chapter_27() -> dict:
    p = "e21-27"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Peak bone mass",
                "Why pediatric bone fragility affects lifetime fracture risk",
                "Foundation for lifetime bone strength is set in the first two decades—each 10% (1 SD) gain in peak bone strength may halve lifetime fracture risk.",
                ref(
                    "Main Conclusions",
                    "Each 10% (1 SD) gain in peak bone strength has been estimated to reduce an individual's lifetime fracture risk by 50%",
                ),
            ),
            note(
                f"{p}-n2",
                "ISCD criteria",
                "How ISCD defines pediatric osteoporosis",
                "Diagnose with vertebral compression fracture without major trauma OR low BMD Z-score <−2 plus ≥2 long-bone fractures by age 10 or ≥3 by age 19—finger/toe fractures do not count.",
                ref(
                    "Defining Pediatric Osteoporosis",
                    "Low bone mineral content or density for age (a standard deviation for age or Z-score less than -2) plus 2 or more long bone fractures by age 10 years or 3 or more by age 19 years",
                ),
            ),
            note(
                f"{p}-n3",
                "DXA limitations",
                "Why DXA alone is an imperfect pediatric fracture predictor",
                "DXA, pQCT, and HR-pQCT are imperfect surrogates—expert panel restricted osteoporosis diagnosis to significant fracture history because no pediatric FRAX equivalent exists.",
                ref(
                    "Main Conclusions",
                    "these have proven to be imperfect surrogate predictors of fracture risk.",
                ),
            ),
            note(
                f"{p}-n4",
                "Bisphosphonates",
                "How bisphosphonates perform in pediatric osteoporosis",
                "Bisphosphonates reduce fractures in most primary and secondary osteoporosis causes except anorexia nervosa—none are FDA-approved in children due to limited RCTs using fracture endpoints.",
                ref(
                    "Drug Therapy",
                    "Bisphosphonates appear to be effective in most causes of primary and secondary osteoporosis with the exception of anorexia nervosa.",
                ),
            ),
            note(
                f"{p}-n5",
                "Athletic triad",
                "How to evaluate a dancer with stress fracture and amenorrhea",
                "Athletic triad combines energy deficit, hypogonadism, and bone stress—exclude hyperprolactinemia, POI, celiac disease, and vitamin D deficiency; DXA may not change management.",
                ref(
                    "Case 1",
                    "The diagnosis is one of exclusion, and it is important to exclude other causes of amenorrhea, including primary ovarian insufficiency or hyperprolactinemia (Answer C).",
                ),
            ),
            note(
                f"{p}-n6",
                "Recurrent fractures",
                "When recurrent childhood fractures warrant genetic testing",
                "Femur fracture before age 5, low-trauma fractures, and family history justify OI genetic testing—even normal DXA Z-scores do not exclude OI.",
                ref(
                    "Case 2",
                    "Genetic testing (Answer E) was performed in this patient, which confirmed a pathogenic variant in the COL1A1 gene.",
                ),
            ),
            note(
                f"{p}-n7",
                "DMD glucocorticoids",
                "Why lateral spine x-ray precedes bisphosphonates in DMD on deflazacort",
                "Declining BMD Z-score alone is insufficient for therapy—vertebral fracture establishes osteoporosis diagnosis and indication for IV bisphosphonates; oral alendronate is less effective for vertebral fractures.",
                ref(
                    "Case 3",
                    "Finding a vertebral fracture would establish the diagnosis of osteoporosis and would be an indication to offer bisphosphonates.",
                ),
            ),
            note(
                f"{p}-n8",
                "Immobilization",
                "Bone health evaluation in nonambulatory children with cerebral palsy",
                "DXA will be low due to narrow bones from absent loading—lateral spine x-ray by age 6–8 guides treatment; bisphosphonates reserved for fragility fractures.",
                ref(
                    "Case 5",
                    "A lateral spine x-ray (Answer E) would influence treatment.",
                ),
            ),
            note(
                f"{p}-n9",
                "Vertebral cascade",
                "STOPP consortium: vertebral fracture cascade in glucocorticoid-treated children",
                "Even one mild grade 1 vertebral fracture predicts future fractures in ALL and other GC-treated cohorts—71% of incident fractures occur in first 2 years.",
                ref(
                    "Case 3",
                    "The presence of even 1 mild grade 1 vertebral fracture predicted future fractures, a phenomenon called the \"vertebral fracture cascade.\"",
                ),
            ),
            note(
                f"{p}-n10",
                "Vitamin D before BP",
                "How to prepare vitamin D-deficient rickets before bisphosphonates",
                "Replete 25-hydroxyvitamin D to >20 ng/mL before bisphosphonate infusion to reduce hypocalcemia and osteomalacia exacerbation—lateral spine x-ray still indicated.",
                ref(
                    "Case 4",
                    "initiate bisphosphonate therapy, but only after vitamin D stores have been repleted (25-hydroxyvitamin D >20 ng/mL [>50 nmol/L]) to reduce the risk of postinfusion hypocalcemia",
                ),
            ),
            note(
                f"{p}-n11",
                "Bone turnover markers",
                "Pediatric bone turnover markers in clinical practice",
                "PINP and CTx have high variability in children—not recommended for diagnosis but may monitor oversuppression during drug therapy.",
                ref(
                    "Evaluation",
                    "These tests are not recommended for diagnosis or decision making for treatment, but they may be useful to monitor for over-suppression of bone turnover during pharmacologic therapy.",
                ),
            ),
            note(
                f"{p}-n12",
                "Anabolic agents",
                "Why teriparatide is not used in growing children",
                "Synthetic parathyroid hormone (teriparatide) carries a black box warning against use in growing patients—bisphosphonates remain main pharmacologic option.",
                ref(
                    "Drug Therapy",
                    "The most commonly prescribed of these, synthetic parathyroid hormone, carries a black box warning against its use in growing patients.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "A 14-year-old ballet dancer with stress fracture, amenorrhea, and low BMI. Best initial evaluation?",
                [
                    "DXA spine and hip only",
                    "DXA whole body and spine only",
                    "Prolactin, LH, FSH, estradiol, 25-OH vitamin D, and celiac screen",
                    "Lateral spine x-ray first",
                ],
                2,
                "Athletic triad workup excludes other amenorrhea causes and checks vitamin D/celiac before imaging decisions.",
                ref(
                    "Case 1",
                    "Answer: C) Prolactin, LH, FSH, estradiol, and 25-hydroxyvitamin D measurements and celiac screen",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "A 14-year-old boy with 7 long-bone fractures including femur at age 3. Best evaluation now?",
                [
                    "Reassurance only",
                    "DXA only",
                    "Bone biopsy first",
                    "Genetic studies for osteogenesis imperfecta",
                ],
                3,
                "Concerning fracture pattern warrants COL1A1/COL1A2 testing—confirmed OI in case.",
                ref(
                    "Case 2",
                    "Answer: E) Genetic studies for osteogenesis imperfecta",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3",
                "A 9-year-old with DMD on deflazacort has spine BMD Z-score declining to −2.1 without fractures. Best advice?",
                [
                    "Start weekly oral alendronate",
                    "Start IV zoledronic acid now",
                    "Obtain lateral spine x-ray",
                    "Repeat DXA in 6 months and treat if Z < −2.5",
                ],
                2,
                "Vertebral imaging determines osteoporosis diagnosis—BMD change alone is insufficient.",
                ref(
                    "Case 3",
                    "Answer: D) Obtain lateral spine x-ray",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 5",
                "A nonambulatory 7-year-old with epilepsy on ketogenic diet requests bone density testing. Best study?",
                [
                    "No imaging",
                    "DXA distal femur, spine, and total body",
                    "Lateral spine x-ray",
                    "DXA hip",
                ],
                2,
                "Immobilization lowers DXA predictively; spine x-ray detects vertebral fractures that change management.",
                ref(
                    "Case 5",
                    "Answer: E) Lateral spine x ray",
                ),
            ),
            mcq(
                f"{p}-q5",
                "ISCD definition",
                "Pediatric osteoporosis by ISCD can be diagnosed with:",
                [
                    "DXA Z-score −1.5 and one wrist fracture",
                    "Vertebral compression fracture without major trauma",
                    "Three finger fractures by age 12",
                    "Low BMI alone",
                ],
                1,
                "Vertebral compression fracture alone suffices; long-bone criteria exclude digits.",
                ref(
                    "Defining Pediatric Osteoporosis",
                    "One or more vertebral compression fractures occurring without local disease or major trauma",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Fracture epidemiology",
                "By age 16, approximate fraction of healthy boys with at least one fracture is:",
                [
                    "10%",
                    "25%",
                    "40%",
                    "64%",
                ],
                3,
                "Up to 64% of boys and 40% of girls have fractured by 16—context for interpreting recurrence.",
                ref(
                    "Case 2",
                    "By 16 years of age, up to 40% of otherwise healthy girls and 64% of boys will have experienced at least 1 broken bone",
                ),
            ),
            mcq(
                f"{p}-q7",
                "DXA regions",
                "If DXA is performed in athletic triad evaluation, preferred regions are:",
                [
                    "Spine and hip",
                    "Whole body and spine",
                    "Forearm only",
                    "Heel ultrasound only",
                ],
                1,
                "Case 1 specifies whole body and spine, not hip.",
                ref(
                    "Case 1",
                    "the preferred regions of interest would be whole body and spine (Answer B) and not spine and hip (Answer A).",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Anorexia",
                "Bisphosphonates in pediatric osteoporosis are LEAST effective in:",
                [
                    "Osteogenesis imperfecta",
                    "Glucocorticoid-induced osteoporosis",
                    "Anorexia nervosa",
                    "Juvenile idiopathic arthritis",
                ],
                2,
                "Explicit exception in drug therapy section.",
                ref(
                    "Drug Therapy",
                    "with the exception of anorexia nervosa.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Baseline labs",
                "Initial laboratory evaluation for pediatric bone fragility should include:",
                [
                    "25-hydroxyvitamin D, calcium, phosphate, creatinine, PTH, and celiac antibodies",
                    "IGF-1 and GH stimulation only",
                    "Serum cortisol only",
                    "No labs—imaging only",
                ],
                0,
                "Baseline panel listed in evaluation section.",
                ref(
                    "Evaluation",
                    "Baseline laboratory studies include measurement of serum 25-hydroxyvitamin D, calcium, phosphate, creatinine, PTH, antibodies for celiac disease, and urinary calcium excretion.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "DMD bisphosphonate",
                "In glucocorticoid-treated DMD, oral alendronate compared with IV agents:",
                [
                    "Is preferred for vertebral fracture prevention",
                    "Has not been shown as effective as IV agents for vertebral fractures in children",
                    "Is FDA-approved for DMD osteoporosis",
                    "Should start at BMD Z −1.5",
                ],
                1,
                "Oral alendronate less effective than IV for vertebral fractures in children on GCs.",
                ref(
                    "Case 3",
                    "oral bisphosphonates such as alendronate have not been shown to be effective as intravenous agents in preventing vertebral fractures in children.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "OI management",
                "A infant with COL1A1 variant and hypotonia. Before starting bisphosphonates:",
                [
                    "Start immediately without labs",
                    "Replete vitamin D and obtain lateral spine x-ray",
                    "Bone biopsy required first",
                    "Avoid all imaging",
                ],
                1,
                "Rule out rickets and vertebral fractures; replete vitamin D before infusion.",
                ref(
                    "Case 4",
                    "order a chemistry panel and 25-hydroxyvitamin D measurement and obtain lateral spine x-ray (Answer D).",
                ),
            ),
            mcq(
                f"{p}-q12",
                "High-risk fractures",
                "Concerning fracture history features in children include:",
                [
                    "Distal radius fracture from fall off bicycle only",
                    "Femur fracture from standing-height trauma",
                    "Finger fracture playing sports",
                    "Toe fracture",
                ],
                1,
                "Low-trauma femur, hip, spine fractures suggest fragility; digits excluded from ISCD counts.",
                ref(
                    "Evaluation",
                    "Features of a concerning fracture history include low-trauma injuries (from standing height or less) or vertebral or femur fractures",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Hypothalamic amenorrhea",
                "First-line treatment for bone health in hypothalamic amenorrhea emphasizes:",
                [
                    "Immediate bisphosphonates before nutrition",
                    "Nutritional rehabilitation and reducing excessive exercise",
                    "High-dose testosterone",
                    "Parathyroid hormone analog",
                ],
                1,
                "Energy deficit drives bone fragility—nutrition first; sex steroids/IGF-1 if rehabilitation fails.",
                ref(
                    "Drug Therapy",
                    "Nutritional therapy is recommended as first-line treatment with reduction in excessive activity if present.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Lifetime risk",
                "A 1 SD increase in peak bone strength may reduce lifetime fracture risk by about 50%.",
                True,
                "Main conclusions cite this estimate.",
                ref(
                    "Main Conclusions",
                    "Each 10% (1 SD) gain in peak bone strength has been estimated to reduce an individual's lifetime fracture risk by 50%",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Finger fractures",
                "Finger and toe fractures count toward ISCD long-bone fracture criteria.",
                False,
                "Guidelines emphasize long bone—not finger/toe—fractures.",
                ref(
                    "Defining Pediatric Osteoporosis",
                    "Fractures of long bones but not fingers and toes are important in decision making about treatment.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "DXA threshold",
                "There is an established pediatric DXA fracture threshold equivalent to adult FRAX.",
                False,
                "No pediatric FRAX-like tool exists.",
                ref(
                    "Significance of the Clinical Problem",
                    "there is no tool comparable to FRAX used in adults to weight the clinical factors that aid in calculating fracture risk.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Second fracture risk",
                "A child with one prior fracture has approximately double the risk of a second fracture.",
                True,
                "Epidemiologic data cited in case 2.",
                ref(
                    "Case 2",
                    "The risk of a second fracture has been estimated to double for a child who has already had 1 fracture.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "DMD BMD",
                "Declining BMD Z-score alone in DMD on glucocorticoids is sufficient to start bisphosphonates.",
                False,
                "Need vertebral fracture or ISCD fracture criteria—not BMD alone.",
                ref(
                    "Case 3",
                    "the change in BMD Z-score alone is not a sufficient indication for drug therapy (thus, Answer E is incorrect).",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Teriparatide",
                "Teriparatide is approved for routine use in growing children with osteoporosis.",
                False,
                "Black box warning against use in growing patients.",
                ref(
                    "Drug Therapy",
                    "carries a black box warning against its use in growing patients.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Immobilization DXA",
                "DXA BMD is often low in immobilized children primarily because of smaller, narrower bones.",
                True,
                "Absent skeletal loading reduces bone geometry seen on DXA.",
                ref(
                    "Case 5",
                    "Two-dimensional assessments of BMD by DXA will be low for age as a result of the smaller, narrower bones.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "ALL fractures",
                "In STOPP ALL cohort, majority of incident fractures occurred after the first 2 years of therapy.",
                False,
                "71% occurred in first 2 years.",
                ref(
                    "Case 3",
                    "71% occurred in the first 2 years of treatment.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Pediatric osteoporosis",
                "Assertion: ISCD restricts pediatric osteoporosis diagnosis to significant fracture history criteria.",
                "Reason: DXA and CT surrogates are imperfect predictors of fracture risk in children.",
                0,
                "Both true—explains restrictive criteria.",
                ref(
                    "Main Conclusions",
                    "the diagnosis of pediatric osteoporosis be restricted to those with a significant fracture history.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Athletic triad",
                "Assertion: Athletic triad evaluation should exclude hyperprolactinemia and celiac disease.",
                "Reason: Athletic triad is a diagnosis of exclusion.",
                0,
                "Both true—case 1 workup.",
                ref(
                    "Case 1",
                    "The diagnosis is one of exclusion, and it is important to exclude other causes of amenorrhea",
                ),
            ),
            ar(
                f"{p}-ar3",
                "OI testing",
                "Assertion: Multiple low-trauma fractures including femur in childhood warrant OI genetic testing.",
                "Reason: Most childhood fractures are evenly distributed and never recur.",
                2,
                "Assertion true; some children fracture repeatedly—reason false.",
                ref(
                    "Case 2",
                    "some children fracture more than once, while others escape injury.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "DMD imaging",
                "Assertion: Lateral spine x-ray is indicated before starting bisphosphonates in glucocorticoid-treated DMD with falling BMD Z-score.",
                "Reason: BMD Z-score decline alone establishes osteoporosis diagnosis.",
                2,
                "Assertion true; BMD alone insufficient—reason false.",
                ref(
                    "Case 3",
                    "the change in BMD Z-score alone is not a sufficient indication for drug therapy",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Bisphosphonates",
                "Assertion: Bisphosphonates reduce fractures in most pediatric primary and secondary osteoporosis.",
                "Reason: Bisphosphonates are equally effective in anorexia nervosa.",
                2,
                "Assertion true; anorexia is the exception—reason false.",
                ref(
                    "Drug Therapy",
                    "Bisphosphonates appear to be effective in most causes of primary and secondary osteoporosis with the exception of anorexia nervosa.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Vitamin D",
                "Assertion: Vitamin D should be repleted before bisphosphonate infusion in rickets.",
                "Reason: Post-infusion hypocalcemia risk rises if vitamin D is deficient.",
                0,
                "Both true—case 4 protocol.",
                ref(
                    "Case 4",
                    "only after vitamin D stores have been repleted (25-hydroxyvitamin D >20 ng/mL [>50 nmol/L]) to reduce the risk of postinfusion hypocalcemia",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Immobilization",
                "Assertion: Lateral spine x-ray influences treatment in nonambulatory children more than DXA alone.",
                "Reason: DXA low values in immobilization always mandate bisphosphonates.",
                2,
                "Assertion true; DXA alone does not guide treatment—reason false.",
                ref(
                    "Case 5",
                    "finding \"low bone density for age\" will most likely add to parental concern but not necessarily guide treatment.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Vertebral cascade",
                "Assertion: A single mild vertebral fracture predicts future fractures in glucocorticoid-treated children.",
                "Reason: Vertebral fractures never occur in the first 2 years of ALL therapy.",
                2,
                "Assertion true (vertebral fracture cascade); most fractures occur early—reason false.",
                ref(
                    "Case 3",
                    "The presence of even 1 mild grade 1 vertebral fracture predicted future fractures, a phenomenon called the \"vertebral fracture cascade.\"",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "27",
        "title": "Pediatric Bone Fragility: When to Worry and What to Do?",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Laura K. Bachrach, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_27_When_to_Worry_and_What_to_Do.md",
        "items": items,
    }
