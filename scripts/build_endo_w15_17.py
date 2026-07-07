#!/usr/bin/env python3
"""Generate Williams 15e module w15-17 — Testicular Disorders."""
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
OUT_NAME = "w15-17_Testicular_Disorders.json"


def build() -> dict:
    p = "w15-17"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why testicular function matters across the lifespan",
                "Testes drive fetal genital differentiation, pubertal virilization and spermarche, and adult sexual function, muscle/bone strength, and fertility; disorders of testis function are common and often treatable with major quality-of-life gains.",
                ref(
                    "KEY POINTS",
                    "The testes are critical for normal development of internal and external genitalia in the fetus and neonate; for secondary sexual characteristics, sexual function, muscle and bone mass and strength, and initiation of spermatogenesis during puberty; and for development and maintenance of adult male phenotype, sexual function, muscle and bone mass and strength, and fertility.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How to classify male hypogonadism",
                "Measure gonadotropins in every man with confirmed low testosterone: elevated LH/FSH indicates primary testicular failure; low or inappropriately normal gonadotropins indicate secondary hypothalamic-pituitary disease—classification directs fertility options and pituitary imaging.",
                ref(
                    "KEY POINTS",
                    "In men with hypogonadism, gonadotropin concentrations should be measured to distinguish between primary and secondary hypogonadism.",
                ),
            ),
            note(
                f"{p}-n3",
                "The Testis",
                "Testicular anatomy and compartments",
                "Adult testes (15–30 mL) contain seminiferous tubules (80–90% volume; Sertoli cells + germ cells) and interstitial Leydig cells (~5% volume); small firm testes usually reflect impaired spermatogenesis.",
                ref(
                    "The Testis",
                    "The testis comprises two structurally and functionally distinct compartments: the seminiferous tubule compartment, which is composed of Sertoli cells and developing germ cells at various stages of spermatogenesis and accounts for 80% to 90% of the volume of the testis, and the interstitial compartment, which is composed of Leydig cells that secrete testosterone, the main male sex steroid hormone, as well as peritubular myoid cells, fibroblasts, neurovascular cells, and macrophages",
                ),
            ),
            note(
                f"{p}-n4",
                "Seminiferous Tubule",
                "How Sertoli cells create the blood-testis barrier",
                "Tight junctions between adjacent Sertoli cells divide tubules into basal and adluminal compartments, blocking paracellular passage of large molecules and forming the blood-testis barrier—only spermatogonia and Sertoli cells receive direct endocrine input from the circulation.",
                ref(
                    "Seminiferous Tubule",
                    "Sertoli cell tight junctions impede the passage of large molecules, steroids, and ions into the seminiferous tubule and constitute the cytologic basis of the blood-testis barrier, analogous to the blood-brain barrier.",
                ),
            ),
            note(
                f"{p}-n5",
                "Spermatogenesis",
                "Human spermatogenesis throughput",
                "Healthy young men produce ~120 million sperm daily through mitotic renewal, meiosis, and spermiogenesis; mitotic inefficiency and germ-cell loss during meiosis limit human sperm output compared with other species.",
                ref(
                    "Spermatogenesis",
                    "In male humans, the process of spermatogenesis supports a production rate of approximately 120 million mature spermatozoa per day by the testes (approximately 1000 per heartbeat!) of healthy young men.",
                ),
            ),
            note(
                f"{p}-n6",
                "Organization of Spermatogenesis",
                "Why spermatogenesis recovery lags insults by months",
                "Complete spermatogenesis takes ~64 days plus epididymal transit; gonadotropin suppression or testicular injury may not lower ejaculate counts for ≥2 months, and recovery can exceed a year.",
                ref(
                    "Organization of Spermatogenesis",
                    "Therefore, external insults to the testis (e.g., ionizing radiation) or induction of gonadotropin deficiency (e.g., by male hormonal contraceptive regimens, severe systemic illness, or drugs such as corticosteroids or opioids) that inhibit early germ cell development and reduce spermatogenesis are not reflected in reduced sperm counts in the ejaculate for 2 months or more.",
                ),
            ),
            note(
                f"{p}-n7",
                "The Testis",
                "Why scrotal temperature matters for fertility",
                "Testes operate ~2°C below core temperature via cremasteric positioning and pampiniform countercurrent exchange; cryptorchidism or prolonged hot-tub exposure elevates testicular temperature and impairs spermatogenesis.",
                ref(
                    "The Testis",
                    "A testis temperature slightly lower than core body temperature is important for normal spermatogenesis.",
                ),
            ),
            note(
                f"{p}-n8",
                "The Testis",
                "Varicocele pathophysiology and red flags",
                "Left-sided palpable varicoceles predominate (98%) from defective left testicular vein valves; new or prominent right-sided varicocele warrants evaluation for retroperitoneal venous obstruction (e.g., renal cell carcinoma, nutcracker syndrome).",
                ref(
                    "The Testis",
                    "Ninety-eight percent of palpable varicoceles occur in the left scrotum, possibly because of absent or defective valves in the left testicular vein.",
                ),
            ),
            note(
                f"{p}-n9",
                "Hypothalamic-Pituitary-Testicular Axis",
                "How the HPT axis regulates testis function",
                "Pulsatile GnRH drives LH (Leydig testosterone) and FSH (Sertoli inhibin B); testosterone and estradiol feedback suppress GnRH/LH, while inhibin B selectively suppresses FSH—essential framework for hypogonadism classification and therapy.",
                ref(
                    "Hypothalamic-Pituitary-Testicular Axis",
                    "Knowledge of the hypothalamic-pituitary-testicular axis is essential in understanding the causes, classification, differential diagnosis, clinical consequences, and treatment of testicular disorders.",
                ),
            ),
            note(
                f"{p}-n10",
                "Central Nervous System Regulation of Gonadotropin-Releasing Hormone Secretion",
                "How Kallmann syndrome links anosmia and hypogonadism",
                "GnRH neurons migrate with olfactory neurons from the olfactory placode; failed migration causes congenital hypogonadotropic hypogonadism with anosmia/hyposmia (Kallmann syndrome) from ANOS1, FGFR1, PROK2, or PROKR2 mutations.",
                ref(
                    "Central Nervous System Regulation of Gonadotropin-Releasing Hormone Secretion",
                    "Abnormalities in the development of the olfactory bulbs and migration of these neurons explain the association between CHH due to GnRH deficiency and the loss or impairment of the sense of smell (anosmia or hyposmia, respectively) that occurs in patients with Kallmann syndrome.",
                ),
            ),
            note(
                f"{p}-n11",
                "Male Hypogonadism",
                "Primary vs secondary hypogonadism",
                "Primary hypogonadism shows low testosterone with elevated LH/FSH (FSH often > LH); secondary hypogonadism shows low testosterone with low or inappropriately normal gonadotropins—secondary disease may be reversible and is the main setting where gonadotropin therapy restores fertility.",
                ref(
                    "Male Hypogonadism",
                    "Clinically, the distinction between primary and secondary hypogonadism is made based on serum gonadotropin concentrations (elevated in primary and low or normal in secondary hypogonadism).",
                ),
            ),
            note(
                f"{p}-n12",
                "Klinefelter Syndrome",
                "Klinefelter syndrome essentials",
                "47,XXY (90%) is the most common sex-chromosome abnormality and leading cause of primary hypogonadism; hallmark is very small firm testes (<4 mL), azoospermia, variable androgen deficiency, gynecomastia, and uniformly elevated gonadotropins—most men remain undiagnosed.",
                ref(
                    "Klinefelter Syndrome",
                    "In adults, the most prominent and consistent clinical feature of Klinefelter syndrome is very small testes, less than 4 mL in volume; this feature is easily detected on examination and should alert the clinician to the possibility of Klinefelter syndrome (see Fig. 17.18).",
                ),
            ),
            note(
                f"{p}-n13",
                "Male Hypogonadism",
                "Why TESE/ICSI changed Klinefelter fertility outlook",
                "Men with Klinefelter and azoospermia were once deemed untreatable; microsurgical testicular sperm extraction with ICSI now permits fatherhood in many, though genetic counseling is mandatory because of aneuploidy risk in offspring.",
                ref(
                    "Male Hypogonadism",
                    "For example, although men with Klinefelter syndrome and azoospermia (no spermatozoa in their ejaculate) were once thought to have untreatable infertility, testicular sperm extraction (TESE) using microsurgical techniques combined with intracytoplasmic sperm injection (ICSI) may permit some of these men to father children.",
                ),
            ),
            note(
                f"{p}-n14",
                "Diagnosis of Male Hypogonadism",
                "How to confirm biochemical hypogonadism",
                "Diagnose hypogonadism only with compatible symptoms/signs plus consistently low morning (7–10 AM) fasting total testosterone on ≥2 samples; exclude acute illness, opioids, and malnutrition that transiently suppress testosterone.",
                ref(
                    "Testosterone Measurements",
                    "Therefore, the biochemical diagnosis of androgen deficiency requires demonstration of consistently and unequivocally low serum testosterone concentrations in at least two blood samples obtained between 7 AM and 10 AM, preferably fasting.",
                ),
            ),
            note(
                f"{p}-n15",
                "Testosterone Measurements",
                "Why free testosterone is needed with altered SHBG",
                "Obesity, diabetes, glucocorticoids, and androgens lower SHBG and can produce misleadingly low total testosterone despite normal free testosterone; borderline totals (200–400 ng/dL) also warrant free or bioavailable testosterone by accurate methods.",
                ref(
                    "KEY POINTS",
                    "In men with low serum total testosterone concentrations and conditions that alter sex hormone–binding globulin, an accurate assessment of serum free testosterone is useful.",
                ),
            ),
            note(
                f"{p}-n16",
                "Infertility",
                "Male infertility workup overview",
                "After 1 year of unprotected intercourse, evaluate both partners; in men obtain history, focused scrotal exam (testis size, varicocele, vas deferens), and at least one WHO-standard semen analysis, then morning testosterone, LH, and FSH to separate primary from secondary hypogonadism.",
                ref(
                    "Infertility",
                    "In men, the history, physical examination, and a seminal fluid analysis are usually able to identify the potential cause of male infertility.",
                ),
            ),
            note(
                f"{p}-n17",
                "Infertility",
                "Why varicocele repair is not routine for infertility",
                "Most infertile men with varicocele have abnormal semen, yet surgical repair has not improved live-birth outcomes in trials; repair is reserved for very large or symptomatic varicoceles, not empiric correction of subclinical left varicocele.",
                ref(
                    "Infertility",
                    "Most men with a varicocele and infertility have abnormal seminal fluid analyses. However, varicocele repair has not been demonstrated to be effective in improving the outcome of live births for these men.",
                ),
            ),
            note(
                f"{p}-n18",
                "Infertility",
                "How exogenous testosterone blocks spermatogenesis",
                "Intratesticular testosterone must be ~100-fold higher than serum to support spermatogenesis; systemic testosterone replacement cannot achieve those local concentrations and therefore suppresses fertility while treating androgen deficiency.",
                ref(
                    "Infertility",
                    "Because intratesticular testosterone concentrations are normally approximately 100-fold higher than serum concentrations, exogenous testosterone treatment of men with androgen deficiency cannot deliver sufficient amounts of testosterone to support normal sperm production in the testis.",
                ),
            ),
            note(
                f"{p}-n19",
                "Cryptorchidism",
                "How to manage cryptorchidism",
                "Treat before puberty (ideally 6–24 months): trial hCG in ~10–20%, otherwise orchiopexy; even after early surgery, spermatogenesis and cancer risk remain impaired—bilateral disease carries highest infertility and malignancy risk.",
                ref(
                    "Cryptorchidism",
                    "Treatment for persistent cryptorchidism should be started before puberty, when greater germ cell degeneration occurs.",
                ),
            ),
            note(
                f"{p}-n20",
                "Seminal Fluid Analysis",
                "WHO 2021 semen reference limits",
                "Lower reference limits from fertile-partner data: concentration ≥16 million/mL, volume ≥1.4 mL, total count ≥39 million/ejaculate, total motility ≥42% (progressive ≥32%), and ≥4% normal morphology by strict criteria—repeat abnormal samples after 1–2 weeks.",
                ref(
                    "Seminal Fluid Analysis",
                    "According to recently revised WHO criteria based on approximately 1800 to 1900 men from 14 countries whose partners became pregnant in 12 months or less (Table 17.6), the lower limit of normal sperm concentration is 16 million/mL; semen volume is 1.4 mL; total sperm count is 39 million per ejaculate; total sperm motility (both progressive and nonprogressive) is 42% and",
                ),
            ),
            note(
                f"{p}-n21",
                "Testosterone Replacement Therapy",
                "Goals of testosterone replacement in adults",
                "Adult TRT targets improved libido/erections, muscle mass and strength, BMD, energy/mood, and hematocrit—gynecomastia of recent onset may improve, but long-standing gynecomastia needs surgery; TRT never restores fertility.",
                ref(
                    "Testosterone Replacement Therapy",
                    "The goals of testosterone therapy in adult hypogonadism are the following",
                ),
            ),
            note(
                f"{p}-n22",
                "Testosterone Replacement Therapy",
                "Why testosterone does not restore fertility",
                "Exogenous androgens cannot recreate intratesticular testosterone levels required for spermatogenesis and do not increase testis size; men with secondary hypogonadism who desire children need gonadotropin or pulsatile GnRH instead of TRT.",
                ref(
                    "Testosterone Replacement Therapy",
                    "Spermatogenesis requires relatively high intratesticular concentrations of testosterone that cannot be achieved by exogenous androgen administration.",
                ),
            ),
            note(
                f"{p}-n23",
                "Sex Steroids",
                "Androgenic anabolic steroid abuse",
                "High-dose synthetic androgens suppress LH/FSH and cause severe oligozoospermia or azoospermia; withdrawal usually recovers the axis, but some men—especially older users—have prolonged symptomatic secondary hypogonadism requiring workup and treatment.",
                ref(
                    "Sex Steroids",
                    "During chronic administration of high-dose androgenic anabolic steroids, serum concentrations of testosterone, LH, and FSH are very low, and sperm counts are usually suppressed to severe oligozoospermia or azoospermia.",
                ),
            ),
            note(
                f"{p}-n24",
                "Gonadotropin Therapy",
                "How gonadotropin therapy restores fertility",
                "In secondary hypogonadism with normal testes, hCG stimulates Leydig testosterone; adding FSH (or continuing hCG alone in acquired disease) can induce spermatogenesis—ineffective in primary testicular failure such as classic Klinefelter.",
                ref(
                    "KEY POINTS",
                    "Gonadotropin replacement therapy generally improves spermatogenesis and fertility in men with secondary hypogonadism.",
                ),
            ),
            note(
                f"{p}-n25",
                "Reversible Versus Organic Causes of Hypogonadism",
                "Why reversible causes must be addressed before TRT",
                "Stop or treat suppressive drugs (opioids, glucocorticoids, androgens), hyperprolactinemia, obesity, sleep apnea, and nutritional deficiency when feasible; if reversal is impractical, proceed with testosterone while monitoring efficacy and safety.",
                ref(
                    "Reversible Versus Organic Causes of Hypogonadism",
                    "Management or treatment of reversible causes of hypogonadism might improve or resolve clinical and biochemical androgen deficiency and should be considered before initiating testosterone replacement therapy.",
                ),
            ),
            note(
                f"{p}-n26",
                "Opioids",
                "Opioid-induced secondary hypogonadism",
                "Chronic potent opioids (methadone, transdermal fentanyl, heroin) suppress pulsatile GnRH, causing symptomatic hypogonadism with low testosterone, low gonadotropins, and impaired sperm motility—consider TRT when discontinuation is not possible.",
                ref(
                    "Opioids",
                    "Prolonged use of opioids causes symptomatic androgen deficiency, resulting in sexual dysfunction and long-term consequences such as loss of BMD and increased risk of osteoporosis; this is a common cause of secondary hypogonadism associated with androgen deficiency and impairment in sperm production.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Male Hypogonadism",
                "A 32-year-old has fatigue, low libido, and bilateral 3-mL firm testes. Total testosterone 180 ng/dL (repeat 175 ng/dL). LH 28 IU/L, FSH 35 IU/L. Best classification and next step?",
                [
                    "Primary hypogonadism—karyotype and genetic counseling if pursuing fertility",
                    "Secondary hypogonadism—start hCG for fertility immediately",
                    "Constitutional delay—observe without labs",
                    "Androgen resistance—start high-dose testosterone only",
                ],
                0,
                "Elevated gonadotropins with small firm testes suggest primary testicular failure (e.g., Klinefelter); karyotype confirms diagnosis and guides TESE/ICSI counseling.",
                ref(
                    "Gonadotropin Measurements",
                    "Men with primary hypogonadism caused by a disorder of the testis have low serum testosterone in association with elevated LH and FSH concentrations as a result of reduced negative feedback",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Male Hypogonadism",
                "A 28-year-old bodybuilder on weekly nandrolone has low libido. Testosterone <50 ng/dL, LH 0.5 IU/L, FSH 0.8 IU/L, azoospermia. Best initial management?",
                [
                    "Discontinue anabolic steroids; evaluate for prolonged suppression; avoid TRT if fertility desired",
                    "Start testosterone gel immediately to restore fertility",
                    "Karyotype for Klinefelter syndrome",
                    "Varicocele repair",
                ],
                0,
                "Exogenous androgens suppress the axis; stop offending agents first. TRT will not restore spermatogenesis; prolonged suppression may need gonadotropin therapy after workup.",
                ref(
                    "Sex Steroids",
                    "After discontinuation of even prolonged anabolic steroid use, recovery of the hypothalamic-pituitary-testicular axis usually occurs within weeks to months.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Congenital Hypogonadotropic Hypogonadism",
                "A 19-year-old never had puberty, cannot smell coffee, has micropenis and cryptorchidism. Testosterone 45 ng/dL, LH 1.2 IU/L, FSH 1.0 IU/L. Diagnosis?",
                [
                    "Kallmann syndrome (CHH with anosmia)",
                    "Klinefelter syndrome",
                    "Constitutional delay of puberty only",
                    "Primary testicular failure",
                ],
                0,
                "~60% of CHH cases have anosmia/hyposmia (Kallmann); low gonadotropins with eunuchoid features indicate GnRH deficiency, not primary testicular disease.",
                ref(
                    "Congenital Hypogonadotropic Hypogonadism",
                    "In approximately 60% of cases, CHH is associated with anosmia or hyposmia and is known as Kallmann syndrome.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Klinefelter Syndrome",
                "A 24-year-old with infertility has 2-mL firm testes, gynecomastia, and testosterone 310 ng/dL with LH 22 IU/L and FSH 38 IU/L. Next diagnostic test?",
                [
                    "Peripheral blood karyotype",
                    "Sellar MRI before any other testing",
                    "Seminal fructose only",
                    "Trial of clomiphene citrate",
                ],
                0,
                "Very small testes with elevated gonadotropins strongly suggest Klinefelter; karyotype confirms 47,XXY or mosaicism and guides fertility counseling.",
                ref(
                    "Klinefelter Syndrome",
                    "The diagnosis of Klinefelter syndrome is confirmed by karyotype analysis, which is usually performed on cultured peripheral blood lymphocytes.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Testosterone Measurements",
                "A 45-year-old obese man (BMI 38) has low energy and low total testosterone 210 ng/dL on two morning samples. SHBG is low. Best next laboratory step?",
                [
                    "Accurate free or calculated free testosterone measurement",
                    "Repeat testosterone at 4 PM only",
                    "Proceed directly to TRT without further labs",
                    "Serum estradiol alone to confirm hypogonadism",
                ],
                0,
                "Obesity lowers SHBG and can produce falsely low total testosterone; free testosterone confirms whether true androgen deficiency is present.",
                ref(
                    "Total Testosterone Affected by Alterations in SHBG",
                    "Common conditions that lower SHBG concentrations include moderate obesity, often associated with type 2 diabetes mellitus (T2DM); protein-losing states, such as nephrotic syndrome; administration of glucocorticoids, progestins, or androgens",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Infertility",
                "A couple is infertile 14 months. Male exam: 18-mL testes, palpable left varicocele, normal vas deferens. Semen: concentration 8 million/mL, motility 30%. Testosterone normal, FSH 12 IU/L. Best counseling?",
                [
                    "Varicocele repair is not proven to improve live births; pursue standard infertility evaluation including partner assessment",
                    "Mandatory varicocele ligation before any other therapy",
                    "Start testosterone to improve sperm count",
                    "No semen analysis needed if testosterone is normal",
                ],
                0,
                "Isolated sperm defects with selective FSH elevation suggest seminiferous tubule dysfunction; varicocele repair has not improved live-birth outcomes in trials.",
                ref(
                    "Infertility",
                    "Therefore, unless a varicocele is very large or symptomatic, surgical repair is not recommended.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Cryptorchidism",
                "An 8-month-old boy has a nonpalpable right testis after repeated exams. Left testis 1.5 mL in scrotum. Best management approach?",
                [
                    "Hormonal trial or orchiopexy before puberty; evaluate for bilateral disease and hernia",
                    "Observe until age 18 regardless of position",
                    "Immediate testosterone replacement",
                    "Bilateral orchidectomy for cancer prevention now",
                ],
                0,
                "Persistent cryptorchidism should be treated before puberty; hCG may induce descent in 10–20%, otherwise orchiopexy is indicated to preserve function and allow surveillance.",
                ref(
                    "Cryptorchidism",
                    "Hormonal treatment with hCG in infant boys is effective in stimulating descent of a cryptorchid testis in approximately 10% to 20% of cases.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Testosterone Replacement Therapy",
                "A 40-year-old with pituitary macroadenoma resection has testosterone 150 ng/dL, LH 1.0 IU/L, desires future fertility. Best androgen therapy?",
                [
                    "Defer TRT; use hCG ± FSH when attempting conception",
                    "Testosterone enanthate 200 mg IM every 2 weeks now",
                    "Oral methyltestosterone",
                    "GnRH agonist therapy",
                ],
                0,
                "In secondary hypogonadism with fertility goals, gonadotropin therapy stimulates both testosterone and spermatogenesis; exogenous testosterone suppresses sperm production.",
                ref(
                    "Testosterone Replacement Therapy",
                    "In men with gonadotropin deficiency and otherwise normal testes who are interested in fathering children, gonadotropin therapy may be used instead of testosterone replacement to stimulate sperm production, restore fertility, and correct androgen deficiency.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "The Testis",
                "A 22-year-old develops acute severe left scrotal pain. Doppler shows absent flow. Time to salvage is critical because:",
                [
                    "Testicular necrosis occurs after 6–8 hours of torsion",
                    "Varicocele always causes immediate infertility",
                    "Epididymitis requires orchidectomy within 1 hour",
                    "Cryptorchidism resolves spontaneously after torsion",
                ],
                0,
                "Testicular torsion strangulates arterial inflow; beyond ~6–8 hours irreversible infarction is likely—surgical detorsion and fixation are emergencies.",
                ref(
                    "The Testis",
                    "However, twisting of the spermatic cord, known as testicular torsion, results in strangulation of the blood supply to the testis and causes testicular necrosis and infarction after 6 to 8 hours, making this condition a surgical emergency.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Hyperprolactinemia",
                "A 35-year-old man has low libido, testosterone 220 ng/dL, LH 2 IU/L, prolactin 680 ng/mL, bitemporal hemianopia. Next step?",
                [
                    "Dopamine agonist therapy and pituitary imaging follow-up",
                    "Immediate testosterone without addressing prolactin",
                    "Varicocele repair",
                    "Empiric ketoconazole for testosterone synthesis",
                ],
                0,
                "Macroadenoma hyperprolactinemia suppresses GnRH; dopamine agonists lower prolactin, shrink tumor, and often restore testosterone—testosterone alone ignores treatable cause.",
                ref(
                    "Hyperprolactinemia",
                    "Treatment with these agents may also improve sexual dysfunction, normalize testosterone concentrations, and improve semen quality.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Infertility",
                "A man with azoospermia, normal volume, normal fructose, FSH 5 IU/L, normal exam. Most likely category?",
                [
                    "Obstructive azoospermia (e.g., CBAVD) vs nonobstructive—imaging/genetics next",
                    "Primary Leydig failure only",
                    "Kallmann syndrome",
                    "Complete androgen insensitivity",
                ],
                0,
                "Normal FSH with azoospermia suggests obstruction or ejaculatory dysfunction rather than severe tubular failure; low fructose/volume would also suggest obstruction.",
                ref(
                    "Infertility",
                    "Men with less severe seminiferous tubule dysfunction and impairment of spermatogenesis and those with azoospermia resulting from genital tract obstruction (obstructive azoospermia) have normal serum FSH concentrations.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Spermatozoa",
                "Semen analysis shows concentration 20 million/mL, 35% motility, 3% normal forms by strict criteria. Compared with WHO 2021 limits:",
                [
                    "Abnormal motility and morphology; concentration acceptable",
                    "All parameters normal—no infertility workup needed",
                    "Azoospermia—start TRT",
                    "Only volume matters for fertility assessment",
                ],
                0,
                "WHO lower limits: motility ≥42% (progressive ≥32%) and morphology ≥4%; concentration ≥16 million/mL—this sample shows isolated motility and morphology defects.",
                ref(
                    "Seminal Fluid Analysis",
                    "progressive sperm motility is 30%; and the percentage of sperm with normal morphologic forms, using strict criteria to eliminate spermatozoa with even mild abnormalities, is at least 4%.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Opioids",
                "A 42-year-old on methadone maintenance has testosterone 240 ng/dL, LH 1.5 IU/L, low libido, osteopenia. Best approach?",
                [
                    "Consider testosterone therapy if opioid cannot be stopped; treat reversible causes first",
                    "Ignore hypogonadism because opioids are short-acting",
                    "Clomiphene is FDA-approved first-line for opioid hypogonadism",
                    "Immediate bilateral orchidectomy",
                ],
                0,
                "Chronic opioids cause secondary hypogonadism; when discontinuation is not feasible, testosterone may improve symptoms and BMD after shared decision-making.",
                ref(
                    "Opioids",
                    "Therefore, testosterone treatment should be considered in cases of secondary hypogonadism resulting from chronic use of opioids.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "The Testis",
                "A 30-year-old notes new right-sided scrotal varicocele. Best next evaluation?",
                [
                    "Abdominal/pelvic imaging for retroperitoneal venous obstruction",
                    "Reassurance—right varicocele is always benign",
                    "Start testosterone for sperm improvement",
                    "No evaluation unless bilaterally symmetric",
                ],
                0,
                "New or prominent right-sided varicocele may indicate renal or retroperitoneal malignancy or venous compression—unlike typical left varicocele from valve incompetence.",
                ref(
                    "The Testis",
                    "The presence of a prominent unilateral right-sided varicocele or new-onset varicocele on either side should prompt evaluation for venous obstruction by an abdominal or pelvic malignancy (e.g., renal cell carcinoma) or lymphadenopathy",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Diagnosis of Male Hypogonadism",
                "A hospitalized septic patient has testosterone 150 ng/dL. He has no prior hypogonadal symptoms. Best action?",
                [
                    "Defer hypogonadism evaluation until recovery from acute illness",
                    "Start TRT during ICU stay",
                    "Diagnose hypogonadism and treat permanently",
                    "Measure only evening testosterone to confirm",
                ],
                0,
                "Acute and critical illness transiently suppress testosterone; diagnosis requires recovery and repeated morning fasting samples with compatible chronic symptoms.",
                ref(
                    "Transient Suppression of Testosterone",
                    "In such situations, measurement of serum testosterone should be delayed until the patient is completely recovered from the illness, the offending drugs are discontinued, the malnutrition is corrected, or the excessive exercise is stopped.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Klinefelter Syndrome",
                "A man with 47,XXY and azoospermia asks about biological children. Most accurate counseling?",
                [
                    "Micro-TESE with ICSI may retrieve sperm in 40–70%; genetic counseling mandatory",
                    "Gonadotropin therapy reliably restores ejaculate sperm",
                    "Testosterone therapy will normalize sperm counts",
                    "Fertility is impossible with any intervention",
                ],
                0,
                "Medical therapy does not reverse Klinefelter azoospermia; sperm retrieval plus ICSI offers substantial success with prenatal/preimplantation genetic counseling.",
                ref(
                    "Klinefelter Syndrome",
                    "and harvesting of sperm from 40% to 70% of men with Klinefelter syndrome for use in ICSI.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "History and Physical Examination",
                "Evaluating delayed puberty, which history finding most suggests Kallmann syndrome over constitutional delay?",
                [
                    "Inability to smell common odors since childhood",
                    "Family history of late bloomers with eventual normal puberty",
                    "Concordant bone age and height age delay only",
                    "Postpubertal onset of small testes",
                ],
                0,
                "Anosmia/hyposmia indicates failed GnRH neuron migration (Kallmann); CDGP lacks olfactory defects and often has family history of delayed but normal puberty.",
                ref(
                    "History and Physical Examination",
                    "inability or reduced ability to smell (suggesting CHH due to Kallmann syndrome)",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Glucocorticoid Excess (Cushing Syndrome)",
                "A man on prednisone 15 mg daily for 6 months has low testosterone and low-normal LH. Before TRT:",
                [
                    "Confirm free testosterone and address reversible glucocorticoid suppression when possible",
                    "Assume primary testicular failure",
                    "Start TRT without gonadotropins or free T",
                    "Varicocele ligation",
                ],
                0,
                "Glucocorticoids commonly cause secondary hypogonadism; SHBG may be low—use accurate free testosterone and treat underlying Cushing/excess glucocorticoid when feasible.",
                ref(
                    "Glucocorticoid Excess (Cushing Syndrome)",
                    "Because high doses of glucocorticoids may suppress SHBG concentrations, it is important to confirm the biochemical diagnosis of hypogonadism using an accurate measurement of free testosterone (i.e., calculated free testosterone or free testosterone by equilibrium dialysis).",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Interstitium",
                "Regarding Leydig and Sertoli cell interactions:",
                [
                    "LH-stimulated testosterone acts locally on Sertoli cells to support spermatogenesis",
                    "FSH directly stimulates Leydig testosterone synthesis",
                    "Leydig cells produce inhibin B as the main FSH feedback signal",
                    "Intratesticular testosterone equals serum concentrations",
                ],
                0,
                "Leydig-derived testosterone is both endocrine and paracrine; with FSH on Sertoli cells it maintains spermatogenesis—intratesticular levels far exceed serum.",
                ref(
                    "Interstitium",
                    "Leydig cells produce testosterone, which acts as a paracrine regulator within the seminiferous tubules of the testis on Sertoli cells in close proximity to stimulate spermatogenesis.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Testosterone Replacement Therapy",
                "A hypogonadal man on testosterone gel has improved libido but persistent erectile dysfunction. Next step?",
                [
                    "Add PDE5 inhibitor or other erectile therapy—neurovascular disease may coexist",
                    "Double testosterone gel dose only",
                    "Stop testosterone entirely",
                    "Switch to methyltestosterone orally",
                ],
                0,
                "TRT alone may not restore erections when vascular/neurologic ED contributes; combined approach per guidelines is often required.",
                ref(
                    "Testosterone Replacement Therapy",
                    "In hypogonadal men who complain primarily of sexual dysfunction, an underlying neurovascular disease or use of certain medications is usually the major cause of erectile dysfunction.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Infertility",
                "Severe oligozoospermia (<5 million/mL) before ICSI. Recommended genetic testing?",
                [
                    "Y chromosome AZF microdeletion analysis and karyotype",
                    "CFTR only in all men regardless of obstruction",
                    "No genetic testing for ICSI candidates",
                    "Prolactin level alone",
                ],
                0,
                "AZF microdeletions are the most common genetic cause of severe oligozoospermia/azoospermia; karyotype detects sex-chromosome aneuploidy—both guide counseling before ICSI.",
                ref(
                    "Infertility",
                    "In men with severe oligozoospermia (sperm concentration <5 million/mL) or azoospermia, testing for Y chromosome microdeletions in the AZF region should be performed routinely.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Meiotic Phase",
                "Klinefelter 47,XXY most commonly arises from:",
                [
                    "Meiotic nondisjunction (maternal or paternal, ~equal frequency)",
                    "Postnatal viral orchitis",
                    "Adult androgen abuse only",
                    "Isolated FSH deficiency",
                ],
                0,
                "Extra X chromosome in Klinefelter results from meiotic nondisjunction with equal maternal and paternal contribution in classic 47,XXY.",
                ref(
                    "Meiotic Phase",
                    "Klinefelter syndrome is classically associated with a 47,XXY karyotype caused by paternal meiotic nondisjunction in 50% of cases.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Risks and Adverse Effects",
                "Before starting TRT in a 55-year-old man, which finding is a relative contraindication per chapter guidance?",
                [
                    "Hematocrit 49% at sea level",
                    "PSA 1.8 ng/mL with normal DRE",
                    "Mild seasonal allergies",
                    "History of appendectomy",
                ],
                0,
                "Baseline high-normal hematocrit risks erythrocytosis on TRT; relative contraindications include hematocrit >48%, elevated PSA, untreated OSA, and severe LUTS.",
                ref(
                    "Risks and Adverse Effects",
                    "Baseline hematocrit in the high-normal range (e.g., hematocrit >48 at or near sea level or >50% at high altitudes) because further stimulation of erythropoiesis induced by testosterone therapy may result in erythrocytosis",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Pubertal Development",
                "First clinical sign of puberty in boys per Williams:",
                [
                    "Increase in testis volume to >3 mL",
                    "Appearance of pubic hair before testicular growth",
                    "Peak height velocity before any testis change",
                    "Spermarche before testicular enlargement",
                ],
                0,
                "Testicular enlargement (>3 mL) is the initial pubertal milestone, preceding penile growth and pubic hair.",
                ref(
                    "Pubertal Development",
                    "An increase in testis size is the first clinical sign of puberty.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "History and Physical Examination",
                "Best position to detect varicocele on physical exam:",
                [
                    "Standing—relaxes scrotum and distends pampiniform plexus",
                    "Supine only with legs elevated",
                    "Prone position mandatory",
                    "MRI replaces all scrotal exams",
                ],
                0,
                "Standing examination relaxes the scrotum and makes a varicocele easier to palpate; warm towel/squatting helps with retractile testes.",
                ref(
                    "History and Physical Examination",
                    "Examination of the testes and scrotum may be performed with the patient either lying on his back or standing, but the latter position is preferred because it relaxes the scrotum, making some abnormalities (e.g., varicocele) easier to detect.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Reversible Versus Organic Causes of Hypogonadism",
                "A 48-year-old with morbid obesity, testosterone 230 ng/dL (low-normal gonadotropins), fatigue. Before TRT per chapter:",
                [
                    "Initiate weight-loss lifestyle measures when obesity/metabolic syndrome is suspected contributor",
                    "Ignore weight because testosterone never relates to obesity",
                    "Start maximum-dose TRT without lifestyle counseling",
                    "Treat only if prolactin is elevated",
                ],
                0,
                "In obese men with low testosterone and normal gonadotropins, lifestyle weight loss should be emphasized before or alongside androgen therapy.",
                ref(
                    "KEY POINTS",
                    "Before initiating testosterone replacement in men with obesity or metabolic syndrome, low serum testosterone and normal serum gonadotropin concentrations, and symptoms of androgen deficiency, it is important to initiate lifestyle changes for weight loss.",
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
                "Primary hypogonadism-related infertility can sometimes be addressed with sperm extraction and assisted reproduction, but not with medical therapy alone.",
                True,
                "KEY POINTS state primary hypogonadism infertility is not treatable medically but may be treatable with sperm-extraction ART.",
                ref(
                    "KEY POINTS",
                    "Primary hypogonadism is associated with infertility that cannot be treated with medical therapy, but it might be treatable with sperm-extraction–assisted reproductive technology.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Male Hypogonadism",
                "Secondary hypogonadism is never reversible.",
                False,
                "Secondary hypogonadism may reverse when underlying causes (medications, nutrition, prolactinoma) are treated.",
                ref(
                    "Male Hypogonadism",
                    "Secondary hypogonadism may be reversible with treatment of the underlying condition (e.g., nutritional deficiency) or discontinuation of an offending medication (e.g., glucocorticoids, opioids)",
                ),
            ),
            tf(
                f"{p}-t3",
                "Spermatogenesis",
                "Klinefelter syndrome is associated with paternal meiotic nondisjunction in about half of cases.",
                True,
                "Classic 47,XXY arises from meiotic nondisjunction with roughly equal maternal and paternal contributions.",
                ref(
                    "Meiotic Phase",
                    "Klinefelter syndrome is classically associated with a 47,XXY karyotype caused by paternal meiotic nondisjunction in 50% of cases.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Infertility",
                "A single moderately low testosterone measurement is sufficient to diagnose hypogonadism.",
                False,
                "Biologic and assay variability require at least two consistent low morning samples plus compatible symptoms.",
                ref(
                    "Testosterone Measurements",
                    "There is also substantial day-to-day variation in serum testosterone concentrations, underscoring the need to repeat the measurement to confirm low concentrations",
                ),
            ),
            tf(
                f"{p}-t5",
                "Infertility",
                "Exogenous testosterone therapy restores normal sperm production in hypogonadal men.",
                False,
                "Systemic testosterone cannot achieve intratesticular concentrations needed for spermatogenesis and suppresses the axis.",
                ref(
                    "Infertility",
                    "exogenous testosterone treatment of men with androgen deficiency cannot deliver sufficient amounts of testosterone to support normal sperm production in the testis.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Cryptorchidism",
                "Orchiopexy before puberty eliminates the increased testicular cancer risk associated with cryptorchidism.",
                False,
                "Risk is reduced but remains two- to fivefold even after prepubertal orchiopexy.",
                ref(
                    "Cryptorchidism",
                    "However, the risk remains higher than normal even after the testis is surgically relocated into the scrotum",
                ),
            ),
            tf(
                f"{p}-t7",
                "Congenital Hypogonadotropic Hypogonadism",
                "Approximately 60% of congenital hypogonadotropic hypogonadism cases have associated anosmia or hyposmia.",
                True,
                "These are classified as Kallmann syndrome with failed olfactory bulb development.",
                ref(
                    "Congenital Hypogonadotropic Hypogonadism",
                    "In approximately 60% of cases, CHH is associated with anosmia or hyposmia and is known as Kallmann syndrome.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Screening and Case Finding for Androgen Deficiency",
                "Population screening for androgen deficiency in all elderly men is recommended.",
                False,
                "General population screening is not indicated; case finding applies in selected high-risk conditions.",
                ref(
                    "Screening and Case Finding for Androgen Deficiency",
                    "In the absence of evidence for long-term clinically meaningful health benefits greater than the risks for testosterone treatment of androgen deficiency, screening for androgen deficiency in the general population or in all elderly men is not indicated.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Sex Steroids",
                "Men abusing anabolic steroids often have low LH and FSH with azoospermia while taking these agents.",
                True,
                "High-dose androgens suppress gonadotropins and severely reduce sperm counts.",
                ref(
                    "Sex Steroids",
                    "During chronic administration of high-dose androgenic anabolic steroids, serum concentrations of testosterone, LH, and FSH are very low, and sperm counts are usually suppressed to severe oligozoospermia or azoospermia.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Klinefelter Syndrome",
                "Most men with Klinefelter syndrome are diagnosed in childhood.",
                False,
                "Fewer than 10% are diagnosed before puberty; 50–75% of adults are never diagnosed.",
                ref(
                    "Klinefelter Syndrome",
                    "Fewer than 10% of boys with Klinefelter syndrome (usually those with the most severe phenotype) are diagnosed before puberty.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Gonadotropin Measurements",
                "In primary hypogonadism, FSH concentrations are generally higher than LH concentrations.",
                True,
                "Loss of both sex-steroid and inhibin B feedback elevates FSH disproportionately.",
                ref(
                    "Gonadotropin Measurements",
                    "FSH concentrations are higher than LH concentrations in men with primary hypogonadism",
                ),
            ),
            tf(
                f"{p}-t12",
                "Testosterone Replacement Therapy",
                "Oral 17α-alkylated androgens such as methyltestosterone are preferred for long-term hypogonadism treatment.",
                False,
                "17α-alkylated oral androgens have hepatotoxicity risk and poor bioavailability—they should not be used for TRT.",
                ref(
                    "Testosterone Replacement Therapy",
                    "Oral 17α-alkylated testosterone derivatives, such as methyltestosterone and fluoxymesterone, should not be used for testosterone replacement therapy.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Infertility",
                "Secondary hypogonadism is one of the few treatable causes of male infertility with medical therapy.",
                True,
                "Gonadotropin or GnRH therapy can restore spermatogenesis when the testes are otherwise normal.",
                ref(
                    "Infertility",
                    "Secondary hypogonadism is one of the few treatable causes of male infertility.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Male Hypogonadism",
                "Assertion: Men with secondary hypogonadism may regain fertility with gonadotropin therapy.",
                "Reason: Secondary hypogonadism always involves irreversible testicular damage.",
                2,
                "Assertion true; reason false—secondary hypogonadism often has intact testes responsive to gonadotropins.",
                ref(
                    "Male Hypogonadism",
                    "Impaired spermatogenesis and infertility caused by gonadotropin deficiency in men with secondary hypogonadism are typically effectively treated with gonadotropin or GnRH therapy, and sperm production and fertility may be restored.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "KEY POINTS",
                "Assertion: Gonadotropin measurement is essential in hypogonadism evaluation.",
                "Reason: Gonadotropins distinguish primary from secondary hypogonadism.",
                0,
                "Both true—KEY POINTS and Male Hypogonadism sections mandate gonadotropins for classification.",
                ref(
                    "KEY POINTS",
                    "In men with hypogonadism, gonadotropin concentrations should be measured to distinguish between primary and secondary hypogonadism.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Klinefelter Syndrome",
                "Assertion: Klinefelter syndrome is the most common cause of primary hypogonadism.",
                "Reason: Klinefelter occurs in roughly 1 in 500 to 600 male births.",
                0,
                "Both true—chapter cites Klinefelter as most common sex-chromosome abnormality and leading primary hypogonadism cause with that birth prevalence.",
                ref(
                    "Male Hypogonadism",
                    "Klinefelter syndrome is the most common human sex chromosome abnormality and the most common cause of primary hypogonadism, occurring in 1 in 500 to 600 male births.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Testosterone Replacement Therapy",
                "Assertion: Testosterone replacement should not be used when a man with secondary hypogonadism desires fertility.",
                "Reason: Testosterone therapy increases intratesticular testosterone enough to support spermatogenesis.",
                2,
                "Assertion true for fertility intent; reason false—exogenous testosterone cannot achieve intratesticular levels needed for sperm production.",
                ref(
                    "Testosterone Replacement Therapy",
                    "Therefore, testosterone replacement therapy does not stimulate sperm production or increase testis size, nor does it restore fertility.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "The Testis",
                "Assertion: Varicocele is associated with testicular dysfunction.",
                "Reason: Ninety-eight percent of palpable varicoceles occur on the right side.",
                2,
                "Assertion true (altered temperature/oxidative stress); reason false—98% are left-sided.",
                ref(
                    "The Testis",
                    "Increased pressures associated with the backflow of blood, altered temperature regulation, and increased oxidative stress may contribute to testicular dysfunction associated with a varicocele.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Cryptorchidism",
                "Assertion: Cryptorchidism increases risk of testicular cancer.",
                "Reason: Orchiopexy completely normalizes cancer risk to that of descended testes.",
                2,
                "Assertion true; reason false—risk remains elevated even after orchiopexy.",
                ref(
                    "Cryptorchidism",
                    "The risk of testicular cancer in an undescended testis is 2.5- to 8-fold greater than in a scrotal testis.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Central Nervous System Regulation of Gonadotropin-Releasing Hormone Secretion",
                "Assertion: Kallmann syndrome features hypogonadotropic hypogonadism with anosmia.",
                "Reason: GnRH neurons originate in the olfactory placode and migrate with olfactory neurons.",
                0,
                "Both true—failed migration explains combined GnRH deficiency and smell loss.",
                ref(
                    "Central Nervous System Regulation of Gonadotropin-Releasing Hormone Secretion",
                    "During embryogenesis, GnRH and olfactory neurons originate outside the CNS in the olfactory placode and migrate together along olfactory axons through the cribriform plate of the ethmoid bone to the olfactory bulb",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Infertility",
                "Assertion: Varicocele repair improves live-birth rates in infertile men.",
                "Reason: Trials have not demonstrated improved live-birth outcomes with varicocele repair.",
                2,
                "Assertion false; reason true—repair not shown to improve live births except large/symptomatic cases.",
                ref(
                    "Infertility",
                    "However, varicocele repair has not been demonstrated to be effective in improving the outcome of live births for these men.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Opioids",
                "Assertion: Chronic opioid use commonly causes secondary hypogonadism.",
                "Reason: Opioids stimulate pulsatile GnRH secretion.",
                2,
                "Assertion true; reason false—opioids suppress hypothalamic GnRH and gonadotropins.",
                ref(
                    "Opioids",
                    "Therefore, exogenous administration of opioids most likely causes reduced gonadotropin secretion by suppressing hypothalamic GnRH secretion.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Seminiferous Tubule",
                "Assertion: The blood-testis barrier limits direct access of circulating hormones to adluminal germ cells.",
                "Reason: Sertoli cell tight junctions separate basal and adluminal compartments.",
                0,
                "Both true—tight junctions form the anatomic basis of the barrier.",
                ref(
                    "Seminiferous Tubule",
                    "Adjacent Sertoli cells surround spermatogonia and form specialized junctional complexes or tight junctions that divide the seminiferous tubule into the basal compartment, in which spermatogonia reside, and the adluminal compartment",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Hyperprolactinemia",
                "Assertion: Hyperprolactinemia causes secondary hypogonadism with low testosterone.",
                "Reason: Prolactin stimulates LH secretion.",
                2,
                "Assertion true; reason false—hyperprolactinemia suppresses pulsatile GnRH and gonadotropins.",
                ref(
                    "Hyperprolactinemia",
                    "Hyperprolactinemia causes gonadotropin deficiency primarily by suppressing pulsatile hypothalamic GnRH secretion",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Reversible Versus Organic Causes of Hypogonadism",
                "Assertion: Reversible causes of hypogonadism should be addressed before starting testosterone.",
                "Reason: Testosterone therapy cures medication-induced gonadotropin suppression while continuing the offending drug.",
                2,
                "Assertion true; reason false—offending drugs should be stopped when possible; TRT does not reverse suppression while drug continues.",
                ref(
                    "Reversible Versus Organic Causes of Hypogonadism",
                    "opioids, glucocorticoids, CNS-active medications, or progestins may be reversed by discontinuation of the offending drug",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "17",
        "title": "Testicular Disorders",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Alvin M. Matsumoto and Bradley D. Anawalt",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_17_Testicular_Disorders.md",
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
