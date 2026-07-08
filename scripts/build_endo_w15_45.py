#!/usr/bin/env python3
"""Generate Williams 15e module w15-45 — Endocrinology of Cancer Management and Survivorship."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-45"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-45_Endocrinology_of_Cancer_Management_and_Survivorship.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why oncofertility bridges oncology and reproductive medicine",
                "Oncofertility expands fertility options for young cancer patients at the intersection of life-preserving therapy and future reproductive health.",
                ref(
                    "KEY POINTS",
                    "Oncofertility is a relatively new interdisciplinary field at the intersection of oncology and reproductive medicine that expands fertility options for young cancer patients.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How gonadotoxicity risk guides fertility preservation",
                "When estimated gonadotoxicity risk exceeds 50% and the patient desires future children, preservation should begin before, during, and after cancer therapy.",
                ref(
                    "KEY POINTS",
                    "If the risk of gonadotoxicity and subsequent iatrogenic fertility loss is greater than 50% and the patient desires to have children in the future, a fertility preservation and restoration strategy should be initiated before, during, and after chemotherapy and radiotherapy.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why multidisciplinary oncofertility teams are essential",
                "Coordinated care among oncologists, gynecologists, endocrinologists, surgeons, reproductive biologists, scientists, and navigators ensures high-standard fertility counseling and procedures.",
                ref(
                    "KEY POINTS",
                    "A multidisciplinary oncofertility approach involving strong coordination among oncologists, gynecologists, endocrinologists, surgeons, reproductive biologists, research scientists, and patient navigators is essential to ensure a high standard of care.",
                ),
            ),
            note(
                f"{p}-n4",
                "What Is Oncofertility, and Why Is It Important?",
                "Why reproductive counseling must precede cancer therapy",
                "Guidelines mandate active discussion of therapy's reproductive effects before, during, and after treatment—yet up to half of patients never receive counseling.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "Current oncology clinical practice guidelines recommend that health care providers engage in an active discussion about the potential effects of cancer therapy on future reproductive health before, during, and after treatment.",
                ),
            ),
            note(
                f"{p}-n5",
                "What Is Oncofertility, and Why Is It Important?",
                "How adequate fertility counseling changes patient decisions",
                "Women who receive high-quality pre-treatment fertility information are five times more likely to pursue preservation and report less regret regardless of choice.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "Importantly, adult women who felt they had received adequate and high-quality information about fertility preservation before initiation of cancer therapy were five times more likely to pursue fertility preservation than women who did not receive counseling.",
                ),
            ),
            note(
                f"{p}-n6",
                "Fertility",
                "Why alkylating agents and pelvic irradiation threaten female fertility",
                "Alkylating chemotherapy and pelvic radiation are especially toxic to primordial follicles, depleting ovarian reserve and shortening the reproductive window.",
                ref(
                    "Fertility",
                    "For women with cancer, alkylating agents and pelvic irradiation are particularly toxic to primordial follicles, and these therapies deplete the ovarian reserve and shorten the reproductive window.",
                ),
            ),
            note(
                f"{p}-n7",
                "Fertility",
                "How chemotherapy and radiation impair male spermatogenesis",
                "Pelvic irradiation and chemotherapy cause azoospermia within 3 months; nearly one-quarter of male survivors have persistent azoospermia or oligospermia.",
                ref(
                    "Fertility",
                    "For men with cancer, chemotherapy and pelvic irradiation are associated with azoospermia within 3 months of the start of treatment, and almost a quarter of male cancer survivors experience persistent azoospermia or oligospermia.",
                ),
            ),
            note(
                f"{p}-n8",
                "Contraception During Cancer Therapy",
                "Why contraception remains necessary during gonadotoxic therapy",
                "Despite treatment-related gonadotoxicity, many patients remain fertile during therapy; unplanned pregnancy occurs in about 3% of women with cancer.",
                ref(
                    "Contraception During Cancer Therapy",
                    "Despite the gonadotoxic effects of cancer therapy, many cancer patients remain fertile during treatment.",
                ),
            ),
            note(
                f"{p}-n9",
                "Contraception During Cancer Therapy",
                "How to time conception after cancer treatment",
                "Wait ≥6 months after chemotherapy and ≥12 months after radiation in women; men should wait 12–24 months because of unrepaired DNA damage in spermatozoa.",
                ref(
                    "Contraception During Cancer Therapy",
                    "Conception should not be attempted sooner than 6 months after the completion of chemotherapy and 12 months after completion of radiation therapy in women with cancer, and no sooner than 12 to 24 months after completion of therapy in men given the risk of unrepaired DNA damage in ejaculated spermatozoa.",
                ),
            ),
            note(
                f"{p}-n10",
                "Gonadal Dysfunction",
                "Why POI is common yet heterogeneous in female survivors",
                "POI prevalence among young female cancer survivors ranges from 2% to 82%, driven by age, alkylating agents, radiation field/dose, and Hodgkin lymphoma diagnosis.",
                ref(
                    "Gonadal Dysfunction",
                    "The prevalence of POI among young female cancer survivors ranges widely at between 2% and 82%.",
                ),
            ),
            note(
                f"{p}-n11",
                "Gonadal Dysfunction",
                "How AMH aids ovarian reserve assessment after cancer",
                "Serum AMH, antral follicle count, and ovarian volume help predict reserve and guide contraception counseling and POI complication screening.",
                ref(
                    "Gonadal Dysfunction",
                    "Methods for better predicting ovarian reserve in female cancer survivors, including measurement of serum antimüllerian hormone (AMH), antral follicle count (AFC), and ovarian volume and surface area, are still being optimized.",
                ),
            ),
            note(
                f"{p}-n12",
                "Gonadal Dysfunction",
                "Why male cancer survivors need hypogonadism screening",
                "Testicular, pituitary, or hypothalamic injury from surgery, chemotherapy, or cranial/pelvic radiation produces subtle but consequential testosterone deficiency.",
                ref(
                    "Gonadal Dysfunction",
                    "Thus, it is important to assess for hypogonadism in men undergoing cancer treatment.",
                ),
            ),
            note(
                f"{p}-n13",
                "Gonadal Dysfunction",
                "How testosterone deficiency affects male survivor morbidity",
                "Hypogonadism links to osteoporosis, depression, metabolic dysfunction, cardiovascular disease, and mortality—though replacement is contraindicated in hormone-sensitive cancers.",
                ref(
                    "Gonadal Dysfunction",
                    "Testosterone deficiency is also associated with osteoporosis, depression, metabolic dysfunction, cardiovascular disease, and mortality.",
                ),
            ),
            note(
                f"{p}-n14",
                "What Is Oncofertility, and Why Is It Important?",
                "Why cancer therapy depletes bone mineral density",
                "Estrogen and testosterone loss from gonadotoxic treatment causes rapid BMD decline and roughly doubles fracture risk in men and women with cancer.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "Considering that these steroid hormones are essential for bone health, cancer treatments that deplete estrogen and testosterone are associated with altered bone physiology, a rapid decline in bone mineral density, and a twofold increased risk of fracture in both men and women with cancer.",
                ),
            ),
            note(
                f"{p}-n15",
                "What Is Oncofertility, and Why Is It Important?",
                "How cancer treatment increases cardiovascular late effects",
                "Anthracyclines, trastuzumab, chest irradiation, cranial radiation, and antihormone therapies contribute to cardiometabolic toxicity beyond direct cardiac injury.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "Not only are certain cancer treatments (anthracyclines, trastuzumab, chest irradiation) associated with cardiac toxicity, but specific chemotherapeutic and immunologic agents, cranial irradiation, surgical tumor removal, and antihormone therapies are also linked with adverse metabolic parameters such as obesity, glucose intolerance, insulin resistance, hypertension, atherosclerosis, and dyslipidemia that increase the risk of cardiovascular disease.",
                ),
            ),
            note(
                f"{p}-n16",
                "Importance of Fertility Preservation and Restoration",
                "Why fertility preservation must not delay urgent oncology care",
                "When gonadotoxicity risk exceeds 50%, established and experimental options should be offered before therapy while individualizing to disease urgency and patient wishes.",
                ref(
                    "Importance of Fertility Preservation and Restoration",
                    "When aggressive chemotherapy and radiotherapy are used, gonadotoxicity may occur as a side effect, leading to impairment of reproductive function, impairment of gonadal steroid hormone-dependent tissues (e.g., bone and heart), and fertility loss.",
                ),
            ),
            note(
                f"{p}-n17",
                "Fertility Preservation and Restoration Options for Young Female Patients",
                "How embryo freezing remains the female gold standard",
                "Embryo cryopreservation after ovarian stimulation and IVF was the first established method and remains preferred when partner or donor sperm is available.",
                ref(
                    "Embryo Freezing",
                    "Embryo freezing was the first established method for preserving female fertility and is still considered the gold standard.",
                ),
            ),
            note(
                f"{p}-n18",
                "Fertility Preservation and Restoration Options for Young Female Patients",
                "Why egg freezing suits single women without donor sperm",
                "ASRM-approved oocyte vitrification avoids IVF at preservation but still requires stimulation—unsuitable for prepubertal girls.",
                ref(
                    "Egg Freezing",
                    "Like embryo freezing, egg freezing requires prior ovarian stimulation for mature oocyte retrieval but does not involve IVF.",
                ),
            ),
            note(
                f"{p}-n19",
                "Fertility Preservation and Restoration Options for Young Female Patients",
                "How ovarian tissue freezing serves prepubertal girls",
                "Cortical ovarian cryopreservation avoids stimulation, does not delay cancer therapy, and may restore endocrine and reproductive function after autotransplantation.",
                ref(
                    "Ovarian Tissue Freezing and Autotransplantation",
                    "Ovarian tissue freezing followed by autotransplantation may be the only suitable fertility preservation option for prepubertal girls, although few babies have been born in women whose ovarian tissue was frozen before puberty.",
                ),
            ),
            note(
                f"{p}-n20",
                "Debatable Options for Fertility Preservation in Women and Girls",
                "Why GnRH agonist ovarian protection remains controversial",
                "Some trials suggest lower POF rates with GnRH analogues during chemotherapy, but major guidelines do not rely on them—especially ineffective against pelvic irradiation.",
                ref(
                    "GnRH Analogues and Hormonal Suppression",
                    "the role of GnRH analogue treatment before and during chemotherapy to protect the ovaries from damage is widely debated.",
                ),
            ),
            note(
                f"{p}-n21",
                "Established Options for Fertility Preservation in Men and Boys",
                "How sperm banking is the established male preservation method",
                "Sperm cryopreservation via masturbation or surgical extraction has been the gold standard since the 1950s with decades-long storage viability.",
                ref(
                    "Sperm Freezing",
                    "Sperm freezing is the first and the only established method for male fertility cryopreservation; since the 1950s, sperm freezing has been considered the gold standard option.",
                ),
            ),
            note(
                f"{p}-n22",
                "Debatable Options for Fertility Preservation in Men and Boys",
                "Why ASCO does not recommend male GnRH agonists",
                "GnRH analogues show gonadoprotection in rodents but not convincingly in humans or primates and do not protect testes from radiation.",
                ref(
                    "GnRH Analogues and Hormonal Suppression",
                    "ASCO does not recommend the use of GnRH analogues and other hormonal suppression methods for male fertility preservation.",
                ),
            ),
            note(
                f"{p}-n23",
                "Experimental Options for Fertility Preservation in Men and Boys",
                "How testicular tissue freezing addresses prepubertal boys",
                "When spermatogenesis is absent, cryopreserved testicular tissue or spermatogonial stem cells remain experimental with malignant-cell reintroduction risk.",
                ref(
                    "Testicular Tissue Freezing",
                    "Testicular tissue freezing is an experimental option that may be offered when sperm production is not possible, such as in prepubertal boys or in adults with azoospermia.",
                ),
            ),
            note(
                f"{p}-n24",
                "Decision-Making Strategies for Young Female and Male Patients With Cancer",
                "Why refer to specialized oncofertility centers",
                "Fertility preservation requires skilled oncologists, gynecologists, andrologists, reproductive biologists, and surgeons—often unavailable outside dedicated centers.",
                ref(
                    "Decision-Making Strategies for Young Female and Male Patients With Cancer",
                    "Referring patients from oncology clinics, small medical centers, or general hospitals to highly specialized oncofertility centers is strongly encouraged to guarantee a high standard of care.",
                ),
            ),
            note(
                f"{p}-n25",
                "Challenges of Fertility Preservation",
                "How provider unpreparedness limits oncofertility care",
                "Though most oncologists value reproductive health, most feel unprepared to assess it—contributing to under-counseling and under-referral.",
                ref(
                    "Challenges of Fertility Preservation",
                    "Although more than 80% of cancer health care providers believe that reproductive health is important for cancer patients, more than 70% of providers feel unprepared to formally assess and address these concerns.",
                ),
            ),
            note(
                f"{p}-n26",
                "Summary and Next Steps",
                "Why oncofertility integration defines survivor quality of life",
                "Loss of reproductive function profoundly affects endocrine health, fertility, and psychosocial well-being—requiring cross-specialty integration with emerging technologies.",
                ref(
                    "Summary and Next Steps",
                    "Oncofertility sits at the fulcrum of disciplines and requires an integration of medical specialties—oncology, urology, and reproductive endocrinology—both with each other and with the emerging technologies that will be tomorrow's breakthroughs.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "What Is Oncofertility, and Why Is It Important?",
                "A 28-year-old woman with Hodgkin lymphoma asks about fertility before ABVD. She reports no prior counseling. Best next step per guidelines?",
                [
                    "Urgent oncofertility referral and discussion of gonadotoxicity risk before therapy",
                    "Defer all fertility discussion until 5-year disease-free survival",
                    "Assume ABVD is non-gonadotoxic and omit counseling",
                    "Recommend immediate conception before any staging scans",
                ],
                0,
                "Guidelines require active reproductive-health discussion before, during, and after treatment; many patients still lack counseling.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "Current oncology clinical practice guidelines recommend that health care providers engage in an active discussion about the potential effects of cancer therapy on future reproductive health before, during, and after treatment.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "KEY POINTS",
                "A 32-year-old with breast cancer scheduled for CMF×6 cycles is estimated to have >50% gonadotoxicity risk and desires future children. Management?",
                [
                    "Initiate individualized fertility preservation before/during therapy after informed consent",
                    "Withhold all fertility options because cancer therapy must never be delayed",
                    "Offer only post-treatment adoption counseling",
                    "Start testosterone replacement to preserve ovarian follicles",
                ],
                0,
                "When gonadotoxicity risk exceeds 50% and the patient wants children, preservation should begin before, during, and after therapy.",
                ref(
                    "KEY POINTS",
                    "If the risk of gonadotoxicity and subsequent iatrogenic fertility loss is greater than 50% and the patient desires to have children in the future, a fertility preservation and restoration strategy should be initiated before, during, and after chemotherapy and radiotherapy.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Fertility",
                "A 25-year-old woman with leukemia will receive high-dose alkylating conditioning. Greatest threat to future fertility?",
                [
                    "Depletion of primordial follicles and shortened reproductive window",
                    "Isolated transient rise in inhibin B without follicle loss",
                    "Permanent activation of all dormant follicles simultaneously",
                    "GnRH-dependent suppression of uterine growth only",
                ],
                0,
                "Alkylating agents and pelvic irradiation are especially toxic to primordial follicles and deplete ovarian reserve.",
                ref(
                    "Fertility",
                    "For women with cancer, alkylating agents and pelvic irradiation are particularly toxic to primordial follicles, and these therapies deplete the ovarian reserve and shorten the reproductive window.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Fertility",
                "A 19-year-old man with testicular cancer starts BEP chemotherapy. Expected early spermatogenic effect?",
                [
                    "Azoospermia within 3 months of treatment start",
                    "Immediate irreversible Leydig cell hyperplasia",
                    "No effect on sperm until 10 years post-therapy",
                    "Guaranteed fertility preservation with normal sperm throughout treatment",
                ],
                0,
                "Chemotherapy and pelvic irradiation are associated with azoospermia within 3 months; many survivors have persistent azoospermia.",
                ref(
                    "Fertility",
                    "For men with cancer, chemotherapy and pelvic irradiation are associated with azoospermia within 3 months of the start of treatment, and almost a quarter of male cancer survivors experience persistent azoospermia or oligospermia.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Embryo Freezing",
                "A married 34-year-old with ER-positive breast cancer needs urgent fertility preservation. Established gold-standard option?",
                [
                    "Embryo cryopreservation after stimulation (often with tamoxifen/letrozole protocols)",
                    "Immediate orthotopic ovarian tissue autotransplant only",
                    "GnRH agonist monotherapy without gamete retrieval",
                    "Testicular sperm extraction",
                ],
                0,
                "Embryo freezing remains the established gold standard when stimulation, retrieval, and sperm for IVF are feasible.",
                ref(
                    "Embryo Freezing",
                    "Embryo freezing was the first established method for preserving female fertility and is still considered the gold standard.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Egg Freezing",
                "A single 29-year-old woman with lymphoma declines donor sperm. Best established female preservation option?",
                [
                    "Mature oocyte cryopreservation after ovarian stimulation",
                    "Embryo freezing requiring partner or donor sperm for IVF",
                    "Testicular tissue freezing",
                    "GnRH agonist alone per ASCO as sole preservation method",
                ],
                0,
                "Egg freezing requires stimulation but not IVF, making it suitable for single women who decline donor sperm.",
                ref(
                    "Egg Freezing",
                    "Like embryo freezing, egg freezing requires prior ovarian stimulation for mature oocyte retrieval but does not involve IVF.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Ovarian Tissue Freezing and Autotransplantation",
                "A 10-year-old girl with leukemia needs fertility preservation before alkylating therapy. Most appropriate established approach?",
                [
                    "Ovarian cortical tissue freezing without prior stimulation",
                    "Emergency embryo freezing after conventional stimulation",
                    "Sperm banking via masturbation",
                    "GnRH agonist as sole ASCO-recommended method",
                ],
                0,
                "Ovarian tissue freezing may be the only suitable option for prepubertal girls and avoids stimulation delay.",
                ref(
                    "Ovarian Tissue Freezing and Autotransplantation",
                    "Ovarian tissue freezing followed by autotransplantation may be the only suitable fertility preservation option for prepubertal girls, although few babies have been born in women whose ovarian tissue was frozen before puberty.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "GnRH Analogues and Hormonal Suppression",
                "A 36-year-old with breast cancer receives chemotherapy plus planned pelvic irradiation. GnRH agonist for ovarian protection?",
                [
                    "Not recommended for pelvic irradiation; role during chemotherapy alone is debated",
                    "Mandatory sole fertility preservation per ASCO/ESMO/ASRM",
                    "Replaces need for oocyte or embryo cryopreservation",
                    "Protects ovaries equally from chemotherapy and radiation",
                ],
                0,
                "GnRH analogues have not been shown to protect ovaries from radiotherapy; guidelines do not rely on them for preservation.",
                ref(
                    "GnRH Analogues and Hormonal Suppression",
                    "In most patients, GnRH analogues have not been shown to protect ovaries from radiotherapy-induced gonadotoxicity.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Sperm Freezing",
                "A 22-year-old man with Hodgkin lymphoma before MOPP/ABVD. Established pre-treatment fertility preservation?",
                [
                    "Sperm cryopreservation before gonadotoxic therapy",
                    "Testicular tissue freezing as first-line established method",
                    "GnRH agonist suppression per ASCO recommendation",
                    "Defer banking until azoospermia is documented post-therapy",
                ],
                0,
                "Sperm freezing is the only established male fertility cryopreservation method and gold standard since the 1950s.",
                ref(
                    "Sperm Freezing",
                    "Sperm freezing is the first and the only established method for male fertility cryopreservation; since the 1950s, sperm freezing has been considered the gold standard option.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Testicular Tissue Freezing",
                "A prepubertal 8-year-old boy with leukemia cannot produce a sperm sample. Experimental option?",
                [
                    "Testicular tissue freezing for future spermatogonial stem cell use",
                    "Established sperm banking via masturbation",
                    "GnRH agonist as ASCO-recommended male preservation",
                    "Immediate vasectomy for contraception only",
                ],
                0,
                "Testicular tissue freezing is experimental when sperm production is impossible, as in prepubertal boys.",
                ref(
                    "Testicular Tissue Freezing",
                    "Testicular tissue freezing is an experimental option that may be offered when sperm production is not possible, such as in prepubertal boys or in adults with azoospermia.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Gonadal Dysfunction",
                "A 33-year-old female leukemia survivor has amenorrhea, elevated FSH on two tests 6 weeks apart, and hot flashes. Diagnosis?",
                [
                    "Premature ovarian insufficiency (POI)",
                    "Normal post-treatment anovulation requiring no evaluation",
                    "Polycystic ovary syndrome",
                    "Functional hypothalamic amenorrhea from athletic training only",
                ],
                0,
                "POI is amenorrhea with gonadal steroid deficiency and elevated FSH on two occasions ≥1 month apart in women <40.",
                ref(
                    "Gonadal Dysfunction",
                    "POI is characterized by amenorrhea and gonadal steroid hormone deficiency with concurrent elevation in serum follicle-stimulating hormone on at least two occasions at least 1 month apart in women younger than 40 years.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Gonadal Dysfunction",
                "A 30-year-old female Hodgkin survivor with irregular menses requests fertility assessment. Best ovarian reserve marker discussed?",
                [
                    "Serum antimüllerian hormone (AMH)",
                    "Serum testosterone as primary ovarian reserve test",
                    "Single random prolactin level only",
                    "Postcoital test for cervical mucus",
                ],
                0,
                "AMH, AFC, and ovarian volume are being optimized to predict reserve in female cancer survivors.",
                ref(
                    "Gonadal Dysfunction",
                    "Methods for better predicting ovarian reserve in female cancer survivors, including measurement of serum antimüllerian hormone (AMH), antral follicle count (AFC), and ovarian volume and surface area, are still being optimized.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Gonadal Dysfunction",
                "A 48-year-old man post retroperitoneal lymph node dissection for testicular cancer reports low libido and fatigue. Next step?",
                [
                    "Assess for hypogonadism including testosterone evaluation",
                    "Assume symptoms are purely psychological without labs",
                    "Start immediate testosterone if prostate cancer history absent regardless of cancer type",
                    "Order AMH to assess testicular reserve",
                ],
                0,
                "Men after cancer therapy, especially older than 45 or with retroperitoneal radiation, need hypogonadism assessment.",
                ref(
                    "Gonadal Dysfunction",
                    "Thus, it is important to assess for hypogonadism in men undergoing cancer treatment.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Gonadal Dysfunction",
                "A 55-year-old man with advanced prostate cancer has symptomatic hypogonadism. Testosterone replacement?",
                [
                    "Generally contraindicated in advanced prostate or breast cancer",
                    "Mandatory for all cancer survivors regardless of primary tumor",
                    "Preferred over GnRH agonists in metastatic prostate cancer",
                    "Indicated solely based on gynecomastia without symptoms",
                ],
                0,
                "Testosterone replacement is readily available but not an option for men with advanced prostate or breast cancer.",
                ref(
                    "Gonadal Dysfunction",
                    "Testosterone replacement is readily available but may not be an option for men with advanced prostate cancer or breast cancer.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Contraception During Cancer Therapy",
                "A 27-year-old woman with cervical cancer on chemotherapy requests contraception. Consideration per chapter?",
                [
                    "Select method by cancer type, comorbidities, and patient preference (e.g., copper IUD vs implant)",
                    "No contraception needed because all patients are infertile during therapy",
                    "Always use high-dose estrogen-containing combined pills in all cancers",
                    "Barrier methods alone are equally effective as implants/IUDs",
                ],
                0,
                "Contraceptive choice depends on cancer type, thrombotic/liver risks, and preference—e.g., nonhormonal IUD in breast cancer.",
                ref(
                    "Contraception During Cancer Therapy",
                    "Selection of an appropriate method of female contraception is guided by the type of cancer (e.g., a nonhormonal copper intrauterine device in women with breast cancer vs. a contraceptive implant in women with cervical cancer), functional status and comorbidities (e.g., immunocompetence, thromboembolic risk, liver dysfunction), and personal preference.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Contraception During Cancer Therapy",
                "A couple asks when they may safely attempt conception after her breast cancer chemotherapy and pelvic radiation. Guidance?",
                [
                    "Wait ≥6 months after chemotherapy and ≥12 months after radiation",
                    "May conceive immediately after last chemotherapy infusion",
                    "Wait only 2 weeks after any cancer treatment",
                    "Men need no waiting period despite DNA damage risk in sperm",
                ],
                0,
                "Women should wait ≥6 months post-chemotherapy and ≥12 months post-radiation; men 12–24 months for sperm DNA repair.",
                ref(
                    "Contraception During Cancer Therapy",
                    "Conception should not be attempted sooner than 6 months after the completion of chemotherapy and 12 months after completion of radiation therapy in women with cancer, and no sooner than 12 to 24 months after completion of therapy in men given the risk of unrepaired DNA damage in ejaculated spermatozoa.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "What Is Oncofertility, and Why Is It Important?",
                "A 40-year-old breast cancer survivor on aromatase inhibitor therapy has rapid BMD decline. Mechanism?",
                [
                    "Therapy-induced estrogen deficiency impairing bone physiology",
                    "Excess testosterone stimulating osteoclast apoptosis only",
                    "Primary hyperparathyroidism from tamoxifen",
                    "Vitamin D toxicity from chemotherapy",
                ],
                0,
                "Cancer treatments depleting estrogen/testosterone cause rapid BMD loss and roughly double fracture risk.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "Considering that these steroid hormones are essential for bone health, cancer treatments that deplete estrogen and testosterone are associated with altered bone physiology, a rapid decline in bone mineral density, and a twofold increased risk of fracture in both men and women with cancer.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "What Is Oncofertility, and Why Is It Important?",
                "A childhood ALL survivor at age 25 has obesity, hypertension, and dyslipidemia. Contributing treatment exposure?",
                [
                    "Cranial irradiation and other therapies linked to adverse cardiometabolic parameters",
                    "Isolated penicillin allergy",
                    "Excess testosterone replacement in all survivors",
                    "GnRH agonist use as universal standard male preservation",
                ],
                0,
                "Beyond anthracyclines and chest radiation, cranial irradiation and antihormone therapies contribute to cardiometabolic risk.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "but specific chemotherapeutic and immunologic agents, cranial irradiation, surgical tumor removal, and antihormone therapies are also linked with adverse metabolic parameters such as obesity, glucose intolerance, insulin resistance, hypertension, atherosclerosis, and dyslipidemia that increase the risk of cardiovascular disease.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Oophoropexy",
                "A 17-year-old with pelvic Hodgkin lymphoma needs pelvic irradiation but wishes fertility preservation. Adjunct procedure?",
                [
                    "Laparoscopic oophoropexy to move ovaries from radiation field",
                    "GnRH agonist alone to protect from pelvic radiation",
                    "Routine bilateral oophorectomy before radiation",
                    "Sperm banking",
                ],
                0,
                "Oophoropexy transposes ovaries from the pelvic radiation field; it does not protect from chemotherapy.",
                ref(
                    "Oophoropexy",
                    "Oophoropexy is the surgical transposition of ovaries away from the field of pelvic irradiation, which is often used to treat pelvic malignancies such as Hodgkin lymphoma, cervical carcinoma, vaginal carcinoma, and pelvic sarcoma.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Decision-Making Strategies for Young Female and Male Patients With Cancer",
                "A rural oncology clinic lacks reproductive endocrinology. Best action for a 26-year-old newly diagnosed with leukemia?",
                [
                    "Refer to a specialized oncofertility center for counseling and preservation options",
                    "Proceed with therapy without any fertility discussion",
                    "Wait until survivorship clinic 10 years later",
                    "Limit counseling to male patients only",
                ],
                0,
                "Referral to specialized oncofertility centers is strongly encouraged when local expertise is limited.",
                ref(
                    "Decision-Making Strategies for Young Female and Male Patients With Cancer",
                    "Referring patients from oncology clinics, small medical centers, or general hospitals to highly specialized oncofertility centers is strongly encouraged to guarantee a high standard of care.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Challenges of Fertility Preservation",
                "A 31-year-old woman received brief fertility mention but no reproductive specialist referral. Likely outcome?",
                [
                    "Lower utilization of preservation despite interest; referral improves understanding",
                    "Automatic embryo banking at no cost in all centers",
                    "Fertility preservation legally prohibited during active cancer care",
                    "Male patients are always counseled more than females",
                ],
                0,
                "Options are underutilized partly due to insufficient referral after initial counseling; specialist evaluation improves understanding.",
                ref(
                    "Challenges of Fertility Preservation",
                    "Although an increasing number of cancer patients are receiving information about fertility preservation before treatment, fertility preservation options are highly underutilized, partly due to insufficient referral to reproductive specialists after initial counseling.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Ovarian Tissue Freezing and Autotransplantation",
                "A woman with ovarian carcinoma requests ovarian tissue autotransplantation after cryopreservation. Guidance?",
                [
                    "Autotransplantation absolutely contraindicated due to malignant-cell reintroduction risk",
                    "Routine recommended for all ovarian malignancies",
                    "Preferred over sperm banking in males",
                    "No contamination risk with any cancer type",
                ],
                0,
                "Autotransplantation of frozen ovarian tissue is absolutely contraindicated in ovarian carcinoma and leukemia (high risk).",
                ref(
                    "Ovarian Tissue Freezing and Autotransplantation",
                    "autotransplantation of frozen-thawed ovarian tissue should be absolutely contraindicated for women with any type of ovarian carcinoma or leukemia (high risk).",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Embryo Freezing",
                "A woman with estrogen-sensitive breast cancer needs emergency fertility preservation. Ovarian stimulation approach?",
                [
                    "Tamoxifen- or letrozole-based stimulation protocols to limit estrogen exposure",
                    "Conventional stimulation without limitation despite ER-positive tumor",
                    "No stimulation possible; only GnRH agonist",
                    "Immediate heterotopic ovarian autotransplant without retrieval",
                ],
                0,
                "Alternative stimulation with tamoxifen or letrozole minimizes elevated estrogen in ER-sensitive breast cancer.",
                ref(
                    "Embryo Freezing",
                    "Alternative ovarian stimulation protocols to minimize the effects of elevated estrogen use either tamoxifen (a selective estrogen receptor modulator) or letrozole (an aromatase inhibitor).",
                ),
            ),
            mcq(
                f"{p}-m24",
                "GnRH Analogues and Hormonal Suppression",
                "An oncologist proposes GnRH agonist alone for a 38-year-old man starting alkylating chemotherapy. Per ASCO?",
                [
                    "Do not use GnRH analogues for male fertility preservation",
                    "GnRH agonist is mandatory established male preservation",
                    "GnRH agonist replaces sperm banking",
                    "GnRH agonist protects testes from all radiation fields",
                ],
                0,
                "ASCO does not recommend GnRH analogues or other hormonal suppression for male fertility preservation.",
                ref(
                    "GnRH Analogues and Hormonal Suppression",
                    "ASCO does not recommend the use of GnRH analogues and other hormonal suppression methods for male fertility preservation.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Challenges of Fertility Preservation",
                "A 16-year-old with cancer and her parents disagree about fertility preservation urgency. Pitfall to avoid?",
                [
                    "Assuming parents' treatment priority always reflects the adolescent's fertility concerns",
                    "Involving the adolescent in age-appropriate fertility discussions",
                    "Documenting gonadotoxicity risk before therapy",
                    "Offering established and experimental options with consent",
                ],
                0,
                "Parents often prioritize immediate therapy and underestimate adolescents' fertility concerns; include patients in discussions.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "However, parents of adolescents with cancer prioritize initiation of therapy over fertility preservation and underestimate their children's concerns about future fertility.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Summary and Next Steps",
                "A fellowship program designs a survivorship curriculum. Core integrative principle of oncofertility?",
                [
                    "Bridge oncology, urology, and reproductive endocrinology across the treatment continuum",
                    "Limit fertility discussion to post-5-year survivors only",
                    "Treat oncofertility as elective infertility care excluded from cancer planning",
                    "Defer all endocrine late-effect screening until age 60",
                ],
                0,
                "Oncofertility requires integration of oncology, urology, and reproductive endocrinology with emerging technologies.",
                ref(
                    "Summary and Next Steps",
                    "Oncofertility sits at the fulcrum of disciplines and requires an integration of medical specialties—oncology, urology, and reproductive endocrinology—both with each other and with the emerging technologies that will be tomorrow's breakthroughs.",
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
                "Greater than 40% of childhood cancer survivors show endocrine system abnormalities.",
                True,
                "KEY POINTS note the endocrine system is among the most frequently affected organ systems in survivors.",
                ref(
                    "KEY POINTS",
                    "The endocrine system is one of the most frequent organ systems to be affected, with greater than 40% of childhood cancer survivors showing abnormalities.",
                ),
            ),
            tf(
                f"{p}-t2",
                "What Is Oncofertility, and Why Is It Important?",
                "Up to 80% of children, adolescents, and adults with cancer receive treatment that may affect reproductive health.",
                True,
                "Most cancer patients receive gonadotoxic or otherwise fertility-affecting therapy.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "However, up to 80% of children, adolescents, and adults with cancer receive treatment that may temporarily or permanently affect their reproductive health, including fertility, gonadal function, and psychosexual well-being.",
                ),
            ),
            tf(
                f"{p}-t3",
                "What Is Oncofertility, and Why Is It Important?",
                "Male cancer patients are more likely than females to be informed about compromised fertility before therapy.",
                False,
                "Male patients are less likely to receive fertility counseling than female counterparts.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "However, male cancer patients are less likely to be informed about potentially compromised fertility than their female counterparts.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Contraception During Cancer Therapy",
                "Barrier contraception is as effective as IUDs and implants for preventing pregnancy during cancer therapy.",
                False,
                "Barrier methods have high user failure rates compared with LARC methods.",
                ref(
                    "Contraception During Cancer Therapy",
                    "Barrier contraception provides protection against sexually transmitted infections but is not as effective as intrauterine devices and contraceptive implants in preventing pregnancy due to high user failure rates.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Gonadal Dysfunction",
                "Resumption of regular menses always indicates restored fertility in female cancer survivors.",
                False,
                "Amenorrhea is an inaccurate surrogate; regular menses does not always signal fertility.",
                ref(
                    "Providing Personalized Risk Assessment",
                    "Most studies have used amenorrhea as a surrogate marker for fertility loss in women, which is not an accurate proxy; in fact, resumption of regular menses does not always signal fertility.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Egg Freezing",
                "ASRM approved egg freezing as an established fertility preservation option in 2012.",
                True,
                "Oocyte cryopreservation became an established ASRM-approved option in 2012.",
                ref(
                    "Egg Freezing",
                    "In 2012, the ASRM approved egg freezing as an established option for female fertility preservation.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Ovarian Tissue Freezing and Autotransplantation",
                "Ovarian tissue freezing should still be considered experimental per ASRM 2019.",
                False,
                "ASRM 2019 announcement recognized ovarian tissue freezing as established, no longer experimental.",
                ref(
                    "Ovarian Tissue Freezing and Autotransplantation",
                    "Ovarian tissue freezing should be considered an established medical procedure and no longer considered experimental according to a recent announcement by the ASRM in 2019.",
                ),
            ),
            tf(
                f"{p}-t8",
                "GnRH Analogues and Hormonal Suppression",
                "ASCO, ESMO, and ASRM guidelines state GnRH analogues should not be relied on as sole female fertility preservation methods.",
                True,
                "Major guidelines do not recommend relying on GnRH analogues or OCPs alone for preservation.",
                ref(
                    "GnRH Analogues and Hormonal Suppression",
                    "According to ASCO, ESMO, and ASRM guidelines, GnRH analogues and other hormonal suppression methods (e.g., oral contraceptives) should not be relied on as female fertility preservation methods.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Oophoropexy",
                "Oophoropexy protects ovaries from chemotherapy-induced gonadotoxicity.",
                False,
                "Oophoropexy shields from irradiation but does not protect ovaries from chemotherapy.",
                ref(
                    "Oophoropexy",
                    "Oophoropexy does not protect ovaries from chemotherapy induced-gonadotoxicity.",
                ),
            ),
            tf(
                f"{p}-t10",
                "GnRH Analogues and Hormonal Suppression",
                "GnRH analogues have proven gonadoprotective effects in human males comparable to rodent models.",
                False,
                "Rodent benefit has not translated convincingly to humans or nonhuman primates.",
                ref(
                    "GnRH Analogues and Hormonal Suppression",
                    "The use of GnRH analogues before and during chemotherapy in males has been shown to have a gonadoprotective effect in mouse and rat models, but it does not appear to have the same effect in human and nonhuman primates.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Challenges of Fertility Preservation",
                "Only about one-third of adolescent and young adult cancer survivors pursue fertility preservation.",
                True,
                "Utilization remains low despite high patient interest.",
                ref(
                    "Challenges of Fertility Preservation",
                    "Only about one-third of AYA cancer survivors pursue fertility preservation.",
                ),
            ),
            tf(
                f"{p}-t12",
                "What Is Oncofertility, and Why Is It Important?",
                "More than 80% of men with prostate cancer experience BMD decline after medical or surgical castration.",
                True,
                "Androgen deprivation markedly accelerates bone loss in prostate cancer.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "In fact, more than 80% of men with prostate cancer experience a decline in bone mineral density after medical or surgical castration, and women with breast cancer experience an accelerated decline in bone density after onset of therapy-induced ovarian insufficiency.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Decision-Making Strategies for Young Female and Male Patients With Cancer",
                "Fertility preservation should be offered only to patients older than 40 years with cancer.",
                False,
                "Strategies target young patients younger than 40 years when gonadotoxicity risk is high.",
                ref(
                    "Decision-Making Strategies for Young Female and Male Patients With Cancer",
                    "If the patient is younger than 40 years and has a reasonable chance of survival, is in good health, and has satisfactory reproductive function, the cancer treatment plan should be reviewed by the oncofertility team and the risk of gonadotoxicity and subsequent fertility loss should be assessed.",
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
                "Assertion: Fertility preservation should be initiated when gonadotoxicity risk exceeds 50% in patients desiring future children.",
                "Reason: Gonadotoxicity risk depends only on patient sex and not on therapy type, dose, or age.",
                2,
                "Assertion true per KEY POINTS; reason false—risk depends on disease, therapy dose, and patient age.",
                ref(
                    "KEY POINTS",
                    "The risks of gonadotoxicity and subsequent iatrogenic fertility loss depend mainly on the type and stage of the disease, dose and dosage of anticancer therapy, and the age of the patient at the beginning of treatment.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "What Is Oncofertility, and Why Is It Important?",
                "Assertion: Adequate pre-treatment fertility counseling increases pursuit of fertility preservation.",
                "Reason: Women who receive counseling are less likely to pursue preservation than uncounseled women.",
                2,
                "Assertion true—counseled women are five times more likely to pursue preservation; reason false.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "Importantly, adult women who felt they had received adequate and high-quality information about fertility preservation before initiation of cancer therapy were five times more likely to pursue fertility preservation than women who did not receive counseling.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Fertility",
                "Assertion: Alkylating agents and pelvic irradiation deplete ovarian reserve in women with cancer.",
                "Reason: Alkylating agents selectively spare primordial follicles while destroying only corpora lutea.",
                2,
                "Assertion true—alkylators and pelvic RT are toxic to primordial follicles; reason false.",
                ref(
                    "Fertility",
                    "For women with cancer, alkylating agents and pelvic irradiation are particularly toxic to primordial follicles, and these therapies deplete the ovarian reserve and shorten the reproductive window.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Embryo Freezing",
                "Assertion: Embryo freezing remains the gold standard established female fertility preservation method.",
                "Reason: Embryo freezing requires no ovarian stimulation or sperm for IVF.",
                2,
                "Assertion true—embryo freezing is gold standard; reason false—it requires stimulation, retrieval, and sperm for IVF.",
                ref(
                    "Embryo Freezing",
                    "Embryo freezing requires prior ovarian stimulation, mature oocyte retrieval, and sperm for in vitro fertilization (IVF).",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Ovarian Tissue Freezing and Autotransplantation",
                "Assertion: Ovarian tissue freezing may be the only suitable option for prepubertal girls.",
                "Reason: Prepubertal girls have active hypothalamic-pituitary-ovarian axis suitable for conventional stimulation.",
                2,
                "Assertion true for prepubertal patients; reason false—prepubertal girls have inactive HPO axis unsuitable for stimulation.",
                ref(
                    "Embryo Freezing",
                    "Therefore, it is not suitable for prepubertal girls who have an inactive hypothalamic-pituitary-ovarian axis and for single women who do not wish to use donated sperm for personal, ethical, or religious reasons.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "GnRH Analogues and Hormonal Suppression",
                "Assertion: GnRH analogues before chemotherapy for ovarian protection are widely debated.",
                "Reason: All major guidelines endorse GnRH analogues as the sole reliable female fertility preservation method.",
                2,
                "Assertion true—role is debated; reason false—ASCO/ESMO/ASRM do not rely on GnRH analogues for preservation.",
                ref(
                    "GnRH Analogues and Hormonal Suppression",
                    "According to ASCO, ESMO, and ASRM guidelines, GnRH analogues and other hormonal suppression methods (e.g., oral contraceptives) should not be relied on as female fertility preservation methods.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Sperm Freezing",
                "Assertion: Sperm freezing is the established gold standard for male fertility cryopreservation.",
                "Reason: Sperm freezing has been considered the gold standard since the 1950s.",
                0,
                "Both true and linked—sperm cryopreservation is the only established male method since the 1950s.",
                ref(
                    "Sperm Freezing",
                    "Sperm freezing is the first and the only established method for male fertility cryopreservation; since the 1950s, sperm freezing has been considered the gold standard option.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Gonadal Dysfunction",
                "Assertion: POI in female cancer survivors is defined by elevated FSH with amenorrhea in women younger than 40.",
                "Reason: A single FSH measurement on one occasion is sufficient to diagnose POI.",
                2,
                "Assertion true per POI definition; reason false—FSH must be elevated on two occasions at least 1 month apart.",
                ref(
                    "Gonadal Dysfunction",
                    "POI is characterized by amenorrhea and gonadal steroid hormone deficiency with concurrent elevation in serum follicle-stimulating hormone on at least two occasions at least 1 month apart in women younger than 40 years.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Gonadal Dysfunction",
                "Assertion: Testosterone deficiency in male cancer survivors associates with osteoporosis and cardiovascular disease.",
                "Reason: Testosterone replacement is always safe in men with advanced prostate cancer.",
                2,
                "Assertion true—hypogonadism links to bone and CV morbidity; reason false—TRT is not an option in advanced prostate/breast cancer.",
                ref(
                    "Gonadal Dysfunction",
                    "Testosterone replacement is readily available but may not be an option for men with advanced prostate cancer or breast cancer.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Contraception During Cancer Therapy",
                "Assertion: Conception should be delayed after chemotherapy and radiation in cancer survivors.",
                "Reason: Men may attempt conception immediately after therapy without concern for sperm DNA damage.",
                2,
                "Assertion true with specified intervals; reason false—men should wait 12–24 months for DNA repair in sperm.",
                ref(
                    "Contraception During Cancer Therapy",
                    "Conception should not be attempted sooner than 6 months after the completion of chemotherapy and 12 months after completion of radiation therapy in women with cancer, and no sooner than 12 to 24 months after completion of therapy in men given the risk of unrepaired DNA damage in ejaculated spermatozoa.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "What Is Oncofertility, and Why Is It Important?",
                "Assertion: Cancer treatments that deplete estrogen and testosterone increase fracture risk.",
                "Reason: Steroid sex hormones have no meaningful role in bone physiology.",
                2,
                "Assertion true—BMD declines with hormone loss; reason false—estrogen and testosterone are essential for bone health.",
                ref(
                    "What Is Oncofertility, and Why Is It Important?",
                    "Considering that these steroid hormones are essential for bone health, cancer treatments that deplete estrogen and testosterone are associated with altered bone physiology, a rapid decline in bone mineral density, and a twofold increased risk of fracture in both men and women with cancer.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Decision-Making Strategies for Young Female and Male Patients With Cancer",
                "Assertion: Referral to specialized oncofertility centers is encouraged for fertility preservation care.",
                "Reason: All community oncology clinics are fully equipped with oncofertility teams and cryobanks.",
                2,
                "Assertion true—referral is strongly encouraged; reason false—specialized equipment and teams are often lacking locally.",
                ref(
                    "Decision-Making Strategies for Young Female and Male Patients With Cancer",
                    "To provide fertility preservation and restoration strategies to young patients with cancer, the treating center should be properly equipped, with a highly skilled team of oncologists, gynecologists, andrologists, reproductive biologists, transplantation surgeons, and research scientists.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "45",
        "title": "Endocrinology of Cancer Management and Survivorship",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Teresa K. Woodruff and Mahmoud Salama",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_45_Endocrinology_of_Cancer_Management_and_Survivorship.md",
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
