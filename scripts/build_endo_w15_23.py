#!/usr/bin/env python3
"""Generate Williams 15e module w15-23 — Physiology and Disorders of Puberty."""
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
OUT_NAME = "w15-23_Physiology_and_Disorders_of_Puberty.json"


def build() -> dict:
    p = "w15-23"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why puberty depends on GnRH pulse reactivation",
                "Puberty reflects reawakening of the HPG axis driven by pulsatile GnRH, which stimulates LH/FSH and gonadal steroidogenesis.",
                ref(
                    "KEY POINTS",
                    "Puberty involves the reawakening of the hypothalamopituitary-gonadal (HPG) axis, driven by pulsatile gonadotropin-releasing hormone (GnRH) secretion.",
                ),
            ),
            note(
                f"{p}-n2",
                "Introduction",
                "How GnRH acts as the pubertal biological alarm clock",
                "Pulsatile hypothalamic GnRH stimulates pituitary gonadotropes to secrete LH and FSH, triggering gonadal steroidogenesis and gametogenesis.",
                ref(
                    "Introduction",
                    "The pulsatile secretion of gonadotropin-releasing hormone (GnRH) by a specialized network of neurons serves as the biological alarm clock that initiates puberty by stimulating the pituitary gonadotropes to secrete hormones (luteinizing hormone [LH] and follicle-stimulating hormone [FSH]), which in turn trigger steroidogenesis and gametogenesis in the gonads.",
                ),
            ),
            note(
                f"{p}-n3",
                "Adrenarche",
                "DHEAS as the biochemical hallmark of adrenarche",
                "Rising circulating DHEAS from zona reticularis differentiation precedes gonadarche by ~2 years and marks adrenal androgen secretion.",
                ref(
                    "Adrenarche",
                    "The rise in circulating dehydroepiandrosterone sulfate (DHEAS) levels is the biochemical hallmark of adrenarche.",
                ),
            ),
            note(
                f"{p}-n4",
                "Pulsatile Secretion",
                "How kisspeptin reactivates the GnRH pulse generator",
                "At puberty onset the pulse generator reactivates through stimulatory arcuate kisspeptin output alongside glial and neurotransmitter signaling.",
                ref(
                    "Pulsatile Secretion",
                    "At puberty onset, the pulse generator reactivates as a result of progressive stimulatory influences on GnRH neurons from glial and neurotransmitter signaling and the recurrence of stimulatory arcuate kisspeptin output.",
                ),
            ),
            note(
                f"{p}-n5",
                "Kisspeptins and KISS1R",
                "Why KISS1R loss causes hypogonadotropic hypogonadism",
                "Mutant KISS1R mice show HH with normal hypothalamic GnRH content and responsiveness to GnRH or gonadotropins—implicating kisspeptin signaling upstream of GnRH release.",
                ref(
                    "Kisspeptins and KISS1R",
                    "Mice transfected with mutant KISS1R genes exhibited hypogonadotropic hypogonadism (HH), although they had normal content of GnRH in the hypothalamus and were responsive to GnRH or gonadotropin administration, suggesting normal function of the gonadotroph GnRH receptors and the gonadal LH and FSH receptors despite the mutation.",
                ),
            ),
            note(
                f"{p}-n6",
                "Timing and Onset of Puberty",
                "How MKRN3 acts as a pubertal brake",
                "Puberty onset reflects balance of stimulatory factors (glutamate, kisspeptin) against inhibitory GABAergic tone, opioids, and MKRN3 expression.",
                ref(
                    "Timing and Onset of Puberty",
                    "Although the increased pulsatile release of GnRH is most frequently considered, this change is caused by a balance in the inhibitory and excitatory factors through coordinated changes in transsynaptic and glial-neuronal communication, increased stimulatory factors (most prominently glutamate and kisspeptin), and decreased inhibitory tone, mostly through GABAergic neurons (i.e., those secreting  $ \\gamma $-aminobutyric acid), opioidergic neurons, and MKRN3 expression, all controlled by gene expression.",
                ),
            ),
            note(
                f"{p}-n7",
                "Timing and Onset of Puberty",
                "Why MKRN3 loss-of-function causes central precocious puberty",
                "MKRN3 is imprinted and expressed from the paternal allele; loss-of-function mutations remove the CNS brake on GnRH, advancing puberty.",
                ref(
                    "Timing and Onset of Puberty",
                    "MKRN3 is imprinted as the maternal allele is methylated and suppressed in normal individuals and only the paternal gene functions; with the mutation in the paternal MKRN3, there is no longer function.",
                ),
            ),
            note(
                f"{p}-n8",
                "Pro-Permissive Evidence",
                "Why leptin is permissive—not a trigger—for human puberty",
                "Leptin signals adequate energy stores but a sharp rise at puberty onset is not required; CDGP boys can enter puberty without rising leptin.",
                ref(
                    "Pro-Permissive Evidence",
                    "In constitutional delay in growth and adolescence, an increase in prepubertal leptin levels is not essential for the onset of puberty.",
                ),
            ),
            note(
                f"{p}-n9",
                "The Secular Trend in Puberty and Menarche",
                "Secular trend in age of menarche",
                "In industrialized countries menarche age fell ~2–3 months per decade over the past 150 years, with slowing after ~1940–1970 as health improved.",
                ref(
                    "The Secular Trend in Puberty and Menarche",
                    "The average age of menarche in industrialized European countries has decreased by 2 to 3 months per decade over the past 150 years; in the United States, the decrease has been approximately 2 to 3 months per decade during the past century",
                ),
            ),
            note(
                f"{p}-n10",
                "Normal Pubertal Development",
                "Normal chronologic windows for pubertal onset",
                "Pubertal onset ranges roughly 8–13 years in girls and 9–14 years in boys, with sex-dependent progression patterns.",
                ref(
                    "Normal Pubertal Development",
                    "The timing of pubertal onset varies greatly in the general population, even among individuals of the same ethnicity, ranging roughly from 8 to 13 years in girls and 9 to 14 years in boys.",
                ),
            ),
            note(
                f"{p}-n11",
                "Secondary Sexual Characteristics in Males",
                "How testicular volume defines pubertal onset in boys",
                "Testicular enlargement to ≥3–4 mL is the first detectable pubertal sign in boys, preceding penile growth and pubarche by 6–12 months.",
                ref(
                    "Secondary Sexual Characteristics in Males",
                    "In boys, several prospective cohorts have confirmed that testicular enlargement (volume  $ \\geq $3–4 mL) is the first detectable sign of puberty, occurring at a mean age of 11.5 years.",
                ),
            ),
            note(
                f"{p}-n12",
                "Delayed Puberty",
                "How delayed puberty is defined clinically",
                "Delayed puberty is >2 SD later than population mean—classically no testicular enlargement by age 14 in boys or no breast development by 13 / no menarche by 15 in girls.",
                ref(
                    "Delayed Puberty",
                    "Classically, this corresponds to an absence of testicular enlargement and virilization in boys (TV <4 mL) by age 14 or the absence of breast development by age 13 or primary amenorrhea by age 15 in girls (Box 23.5).",
                ),
            ),
            note(
                f"{p}-n13",
                "Delayed Puberty",
                "Why obese boys are misreferred for micropenis",
                "Suprapubic adipose tissue buries the phallus; retracting fat reveals true penile size—among the most common causes of inappropriate hypogonadism referral.",
                ref(
                    "Delayed Puberty",
                    "Obese boys often appear to have a small penis because of excessive adipose tissue surrounding the phallus; only when the fat is retracted can the full extent of phallic development be assessed.",
                ),
            ),
            note(
                f"{p}-n14",
                "Constitutional Delay in Growth and Puberty",
                "How CDGP differs from permanent hypogonadotropic hypogonadism",
                "CDGP is transient GnRH deficiency with eventual spontaneous puberty; CHH is permanent GnRH deficiency with absent/incomplete puberty and infertility.",
                ref(
                    "Constitutional Delay in Growth and Puberty",
                    "CDGP is the most common cause of delayed puberty in both sexes and results from a transient state of GnRH deficiency where puberty eventually occurs, although with marked delay.",
                ),
            ),
            note(
                f"{p}-n15",
                "Constitutional Delay in Growth and Puberty",
                "Why morning testosterone heralds imminent puberty in CDGP boys",
                "A morning serum T >0.7 nmol/L predicts phenotypic puberty within 12–15 months as the hypothalamic-pituitary axis matures.",
                ref(
                    "Constitutional Delay in Growth and Puberty",
                    "A morning serum T value of >0.7 nmol/L heralds an imminent onset of phenotypic puberty in boys within 12 to 15 months.",
                ),
            ),
            note(
                f"{p}-n16",
                "Congenital Hypogonadotropic Hypogonadism",
                "CHH diagnostic criteria",
                "CHH presents with low sex steroids and low/normal gonadotropins, normal pituitary function otherwise, and no hypothalamic-pituitary lesion on MRI; anosmia defines Kallmann syndrome.",
                ref(
                    "Congenital Hypogonadotropic Hypogonadism",
                    "Because GnRH cannot be reliably measured in the serum because of a very short half-life, the diagnosis relies on low serum sex steroids in the setting of low/normal serum gonadotropin levels, otherwise normal pituitary function, and the absence of a hypothalamic-pituitary lesion on MRI.",
                ),
            ),
            note(
                f"{p}-n17",
                "Clinical Presentation",
                "How CHH males present at adolescence",
                "Most males seek care for lack of virilization; complete CHH shows prepubertal testes <4 mL, while ~25% have partial CHH with some testicular growth but T <1 nmol/L.",
                ref(
                    "Clinical Presentation",
                    "Although the majority of males with CHH exhibit absent puberty (complete CHH, i.e., no virilization and prepubertal testis <4 mL), approximately 25% exhibit some degree of pubertal development (partial CHH, TV greater than 4 mL).",
                ),
            ),
            note(
                f"{p}-n18",
                "Delayed Puberty",
                "Why smell testing is essential in delayed puberty",
                "History of anosmia or hyposmia in the patient or relatives points to isolated gonadotropin deficiency (Kallmann syndrome) rather than CDGP.",
                ref(
                    "Delayed Puberty",
                    "Questions about the patient's sense of smell are essential.",
                ),
            ),
            note(
                f"{p}-n19",
                "Precocious Puberty",
                "Central versus peripheral precocious puberty",
                "GnRH-dependent CPP shows pubertal LH pulsatility and LH rise after GnRH/agonist; PPP features gonadal steroids or hCG independent of hypothalamic GnRH activation.",
                ref(
                    "Precocious Puberty",
                    "If iso sexual precocity results from premature reactivation of the hypothalamic GnRH pulse generator/pituitary gonadotropingonadal axis, the condition is GnRH dependent and is termed CPP.",
                ),
            ),
            note(
                f"{p}-n20",
                "Precocious Puberty",
                "Why untreated CPP paradoxically shortens adult height",
                "Accelerated gonadal steroids advance bone age and epiphyseal fusion—tall in childhood but mean adult heights ~152 cm in girls and ~155 cm in untreated boys.",
                ref(
                    "Precocious Puberty",
                    "In all forms of sexual precocity, increased gonadal steroid secretion increases height velocity, somatic development, and the rate of skeletal maturation; because of premature epiphyseal fusion, sexual precocity can lead to the paradox of tall stature in childhood but short adult height (Table 23.7).",
                ),
            ),
            note(
                f"{p}-n21",
                "Central Precocious Puberty",
                "How to diagnose CPP biochemically",
                "Third-generation LH assays on basal samples diagnose most girls; LH 60–240 min after GnRH or GnRH agonist challenge confirms CPP with high sensitivity.",
                ref(
                    "Central Precocious Puberty",
                    "Gonadotropin determination 60 or 240 minutes after a single subcutaneous dose of GnRH or GnRH agonist can diagnose CPP with high specificity and sensitivity.",
                ),
            ),
            note(
                f"{p}-n22",
                "Central Precocious Puberty",
                "Why CPP in boys mandates CNS evaluation",
                "In boys, neurologic lesions account for at least half of CPP cases—sexual precocity may be the sole manifestation of a hypothalamic tumor.",
                ref(
                    "Central Precocious Puberty",
                    "Therefore, it is essential to search for a CNS cause for CPP, especially in boys, because sexual precocity may be the only manifestation of a CNS tumor (Table 23.9 and Box 23.8).",
                ),
            ),
            note(
                f"{p}-n23",
                "Hamartomas of the Tuber Cinereum",
                "Hypothalamic hamartoma as ectopic GnRH pulse generator",
                "Hamartomas contain GnRH neurons that escape CNS inhibitory restraint; pulsatile—not continuous—GnRH release causes CPP, controllable with GnRH agonist.",
                ref(
                    "Hamartomas of the Tuber Cinereum",
                    "The precocious sexual development can be controlled by treatment with GnRH agonist therapy.",
                ),
            ),
            note(
                f"{p}-n24",
                "Genetics of Central Precocious Puberty",
                "MKRN3 as the most common monogenic familial CPP cause",
                "Loss-of-function MKRN3 mutations (paternally expressed) are the most common monogenic cause of familial CPP, often presenting before age 7 in girls.",
                ref(
                    "Genetics of Central Precocious Puberty",
                    "The loss-of-function MKRN3 mutations, causing premature activation of the reproductive axis, are the most common monogenic cause of familial CPP.",
                ),
            ),
            note(
                f"{p}-n25",
                "Miscellaneous Causes",
                "How GnRH agonists suppress central precocious puberty",
                "Potent GnRH agonists cause an initial LH/FSH flare, then within 1–2 weeks suppress pulsatile gonadotropins and gonadal steroids to prepubertal levels.",
                ref(
                    "Miscellaneous Causes",
                    "Treatment of CPP with a potent GnRH agonist results in 1 to 3 days of increased FSH and LH release and a rise in circulating gonadal steroid levels, followed after 7 to 14 days of treatment by suppression of pulsatile secretion of LH and FSH and of the pubertal LH response to the administration of native GnRH (Figs. 23.51 and 23.52).",
                ),
            ),
            note(
                f"{p}-n26",
                "Miscellaneous Causes",
                "Why early GnRH agonist therapy preserves adult height in CPP",
                "Best height outcomes occur when treatment starts soon after onset with only modest bone-age advancement; ~90% reach target adult height with therapy.",
                ref(
                    "Miscellaneous Causes",
                    "Adult height in children treated with GnRH agonists is improved, especially when therapy starts before 6 years of age rather than after 8 years of age (Table 23.11).",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Delayed Puberty",
                "A 15-year-old boy has TV 3 mL, height −2.5 SD, delayed bone age, and a father who was a 'late bloomer.' LH and FSH are prepubertal; exam otherwise normal. Best initial approach?",
                [
                    "Presumptive constitutional delay with observation and serial assessment",
                    "Immediate cranial irradiation",
                    "Karyotype for Turner syndrome",
                    "Start GnRH agonist therapy",
                ],
                0,
                "Classic CDGP: normal exam aside from delay, short for age but appropriate for bone age, positive family history—presumptive diagnosis after excluding pathology.",
                ref(
                    "Delayed Puberty",
                    "A presumptive diagnosis of constitutional delay in growth and adolescence is made if there are no clinical signs of a systemic or hypothalamic-pituitary disease, if the physical examination is strictly normal (besides the pubertal delay), if the height is short for chronologic age but normal for bone age, and if a similar history of spontaneous resolving delayed puberty is found in parents or siblings.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Delayed Puberty",
                "A 14-year-old obese boy is referred for 'micropenis.' Stretched penile length is normal after retraction of suprapubic fat; testes 8 mL. Most likely pitfall?",
                [
                    "Misattributing buried penis to hypogonadism",
                    "Missed Klinefelter syndrome",
                    "Undiagnosed congenital adrenal hyperplasia",
                    "Central precocious puberty",
                ],
                0,
                "Excessive adipose tissue around the phallus is among the most common causes of inappropriate referral for hypogonadism in obese boys.",
                ref(
                    "Delayed Puberty",
                    "Obese boys often appear to have a small penis because of excessive adipose tissue surrounding the phallus; only when the fat is retracted can the full extent of phallic development be assessed.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Constitutional Delay in Growth and Puberty",
                "A 16-year-old boy with CDGP has morning testosterone 0.8 nmol/L. What should you counsel regarding timing of spontaneous virilization?",
                [
                    "Phenotypic puberty likely within 12–15 months",
                    "Permanent infertility is certain",
                    "Immediate pituitary surgery is indicated",
                    "GnRH agonist is required to induce puberty",
                ],
                0,
                "Morning T >0.7 nmol/L in CDGP boys heralds imminent clinical puberty as gonadotropins rise with advancing bone age.",
                ref(
                    "Constitutional Delay in Growth and Puberty",
                    "A morning serum T value of >0.7 nmol/L heralds an imminent onset of phenotypic puberty in boys within 12 to 15 months.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Congenital Hypogonadotropic Hypogonadism",
                "A 17-year-old male has no virilization, TV 2 mL, low LH/FSH, low testosterone, normal prolactin/TSH, and normal pituitary MRI. He cannot smell coffee. Diagnosis?",
                [
                    "Kallmann syndrome (CHH with anosmia)",
                    "Klinefelter syndrome",
                    "Constitutional delay",
                    "McCune-Albright syndrome",
                ],
                0,
                "CHH with anosmia is Kallmann syndrome—failed GnRH neuron migration; low gonadotropins with low testosterone and no pituitary mass.",
                ref(
                    "Congenital Hypogonadotropic Hypogonadism",
                    "When CHH is associated with anosmia, it is classified as KS.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Constitutional Delay in Growth and Puberty",
                "Differentiating CDGP from CHH in adolescence is difficult. Which finding favors CDGP over CHH?",
                [
                    "Positive family history of delayed puberty and rare anosmia",
                    "Undescended testes more common than in general population",
                    "Absent spontaneous gonadotropin rise with bone age advancement",
                    "Micropenis and cryptorchidism at birth",
                ],
                0,
                "Unlike KS, impaired olfaction is very rare in CDGP; family history of delayed puberty is common (50–75%).",
                ref(
                    "Constitutional Delay in Growth and Puberty",
                    "Unlike in KS, impaired olfaction is very rare in CDGP, and undescended testes occur at the rate found in the general population.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Precocious Puberty",
                "A 7-year-old girl has progressive breast development, accelerated growth, and bone age 10 years. Basal LH is pubertal and rises further after leuprolide stimulation. Diagnosis?",
                [
                    "Central (GnRH-dependent) precocious puberty",
                    "Peripheral precocious puberty from ovarian tumor",
                    "Premature thelarche only—no therapy needed",
                    "Isolated premature adrenarche",
                ],
                0,
                "Pubertal basal LH and pubertal LH response to GnRH agonist indicate GnRH-dependent CPP with activation of the hypothalamic pulse generator.",
                ref(
                    "Precocious Puberty",
                    "Pulsatile LH release has a pubertal pattern, and the rise in the concentration of LH after GnRH or GnRH agonist administration is indistinguishable from the normal pubertal pattern of serum LH.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Central Precocious Puberty",
                "A 5-year-old boy develops testicular enlargement and rapid growth. MRI is normal. Compared with girls with CPP, what is true?",
                [
                    "CNS pathology is far more likely in boys—repeat imaging and close follow-up",
                    "Idiopathic CPP is eight times more common in boys than girls",
                    "GnRH agonist is contraindicated in all boys",
                    "Peripheral precocity is ruled out by normal growth velocity",
                ],
                0,
                "CPP is idiopathic far more often in girls; in boys neurologic lesions are at least as common as idiopathic CPP—mandatory CNS evaluation.",
                ref(
                    "Central Precocious Puberty",
                    "CNS abnormalities occurred at least as often as idiopathic CPP in boys, whereas in girls, neurologic lesions were one-fifth as common as idiopathic disorders.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Hamartomas of the Tuber Cinereum",
                "A 2-year-old boy has CPP and gelastic seizures. MRI shows a hypothalamic hamartoma attached to the tuber cinereum. Best endocrine management?",
                [
                    "GnRH agonist therapy; surgery reserved for refractory seizures or mass growth",
                    "Immediate surgical extirpation of hamartoma for all CPP cases",
                    "Medroxyprogesterone as first-line therapy",
                    "Observation only—hamartomas always regress",
                ],
                0,
                "Medical GnRH agonist is optimal for precocious puberty with hamartoma when seizures are absent or controlled; surgery is not recommended for CPP alone.",
                ref(
                    "Hamartomas of the Tuber Cinereum",
                    "Medical therapy with GnRH agonist in lieu of surgery is the optimal treatment of precocious puberty associated with these hamartomas if seizures are absent or under control.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Miscellaneous Causes",
                "A 5-year-old girl with idiopathic CPP starts deslorelin. What occurs during the first 2 weeks?",
                [
                    "Initial LH/FSH flare with rising estradiol, then suppression to prepubertal levels",
                    "Immediate permanent suppression without flare",
                    "Adrenal androgen suppression and loss of pubic hair within 48 hours",
                    "Irreversible pituitary destruction",
                ],
                0,
                "GnRH agonists cause a 1–3 day gonadotropin flare, then within 7–14 days suppress pulsatile LH/FSH and gonadal steroids.",
                ref(
                    "Miscellaneous Causes",
                    "Treatment of CPP with a potent GnRH agonist results in 1 to 3 days of increased FSH and LH release and a rise in circulating gonadal steroid levels, followed after 7 to 14 days of treatment by suppression of pulsatile secretion of LH and FSH and of the pubertal LH response to the administration of native GnRH (Figs. 23.51 and 23.52).",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Idiopathic True or Central Precocious Puberty",
                "A healthy 7-year-old girl has slowly progressive breast Tanner 2 for 6 months, prepubertal LH after GnRH agonist, uterine length 30 mm, and normal growth velocity. Management?",
                [
                    "Observation with serial follow-up—may be benign early thelarche variant",
                    "Urgent GnRH agonist to maximize adult height",
                    "Bilateral oophorectomy",
                    "High-dose glucocorticoids",
                ],
                0,
                "Therapy may not be needed if sleep LH pulsatility, basal/stimulated LH, and uterine size remain prepubertal—regular follow-up is essential.",
                ref(
                    "Idiopathic True or Central Precocious Puberty",
                    "Therapy may not be indicated if a pubertal pattern of pulsatile LH secretion during sleep is not present, if the basal LH as measured by ultrasensitive assay or the LH response to exogenous GnRH or GnRH agonist is prepubertal, or if the uterus on sensitive ultrasound is less than 34 mm.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Precocious Puberty",
                "A 4-year-old girl has isosexual precocity with pubic hair, clitoromegaly, and markedly elevated testosterone; LH is suppressed and does not rise after GnRH. Diagnosis?",
                [
                    "Peripheral (GnRH-independent) precocious puberty",
                    "Central precocious puberty",
                    "Constitutional delay",
                    "Premature adrenarche only",
                ],
                0,
                "PPP features gonadal steroids or gonadotropins independent of hypothalamic GnRH—suppressed prepubertal LH pattern despite virilization/feminization.",
                ref(
                    "Precocious Puberty",
                    "If extrapituitary secretion of gonadotropins or secretion of gonadal steroids independent of pulsatile GnRH stimulation leads to virilization in boys or feminization in girls, the condition is termed peripheral precocious puberty (PPP).",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Kisspeptins and KISS1R",
                "A teenager with delayed puberty and anosmia has normal MRI sella. Genetic testing shows inactivating KISS1R mutation. Expected hormonal pattern?",
                [
                    "Low LH/FSH with low sex steroids—hypogonadotropic hypogonadism",
                    "High LH/FSH with low sex steroids",
                    "High testosterone with suppressed LH",
                    "Normal gonadotropins with precocious puberty",
                ],
                0,
                "Inactivating KISS1R mutations cause isolated HH with low gonadotropins despite normal hypothalamic GnRH content.",
                ref(
                    "Kisspeptins and KISS1R",
                    "Mice transfected with mutant KISS1R genes exhibited hypogonadotropic hypogonadism (HH), although they had normal content of GnRH in the hypothalamus and were responsive to GnRH or gonadotropin administration, suggesting normal function of the gonadotroph GnRH receptors and the gonadal LH and FSH receptors despite the mutation.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Genetics of Central Precocious Puberty",
                "A 6-year-old girl with familial CPP has a paternally inherited MKRN3 frameshift mutation. Mechanism?",
                [
                    "Loss of pubertal brake on KISS1/TAC3 transcription in arcuate neurons",
                    "Excess adrenal androgen secretion",
                    "Activating GnRH receptor mutation",
                    "Primary ovarian failure with high gonadotropins",
                ],
                0,
                "MKRN3 is paternally expressed; loss-of-function removes inhibition of KISS1/TAC3, prematurely activating the GnRH pulse generator.",
                ref(
                    "Genetics of Central Precocious Puberty",
                    "MKRN3 acts to prevent puberty onset, at least in part, by repressing KISS1 and TAC3 transcription and that this action may involve an MKRN3-directed ubiquitination mechanism.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Delayed Puberty",
                "A short 13-year-old girl has no breast development. Karyotype 45,X. Expected gonadotropin pattern?",
                [
                    "Elevated LH and FSH—hypergonadotropic hypogonadism",
                    "Low LH/FSH with low estradiol",
                    "Normal prepubertal gonadotropins",
                    "Suppressed LH with high estradiol",
                ],
                0,
                "Turner syndrome causes primary gonadal failure with elevated gonadotropins—hypergonadotropic hypogonadism, not HH.",
                ref(
                    "Females",
                    "Syndrome of gonadal dysgenesis (Turner syndrome) and its variants XX and XY gonadal dysgenesis",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Functional Hypogonadotropic Hypogonadism",
                "A 16-year-old female cross-country runner has primary amenorrhea, low BMI, low LH/FSH, and normal MRI. Most likely diagnosis?",
                [
                    "Functional hypothalamic amenorrhea from energy deficit/exercise",
                    "Turner syndrome",
                    "Central precocious puberty",
                    "Congenital adrenal hyperplasia",
                ],
                0,
                "Functional HH (FHA) is prevalent in females with weight loss, eating disorders, or excessive exercise—exercise amenorrhea in athletes.",
                ref(
                    "Delayed Puberty",
                    "Functional HH (or functional hypothalamic amenorrhea [FHA]) is more prevalent in females and could be suggested by the presence of weight loss, eating disorders, excessive physical activity, and/or chronic underlying conditions.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Pulsatile Secretion",
                "Arcuate kisspeptin neurons are critical for puberty because they:",
                [
                    "Innervate GnRH neuron projections and are essential pulse-generator components",
                    "Secrete ACTH to drive adrenal androgens",
                    "Directly aromatize testosterone to estradiol",
                    "Replace GnRH at the pituitary receptor",
                ],
                0,
                "Arcuate kisspeptin neurons innervate GnRH neurosecretory zones and are critical components of the GnRH pulse generator in all mammals.",
                ref(
                    "Pulsatile Secretion",
                    "The arcuate nucleus kisspeptin neurons that innervate the projections of GnRH neurons in and around their neurosecretory zone are also critical components of the pulse generator in all mammals.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Adrenarche",
                "A 7-year-old has pubic hair without breast development or testicular enlargement. DHEAS is elevated; LH/FSH prepubertal. Diagnosis?",
                [
                    "Premature adrenarche with dissociation from gonadarche",
                    "Central precocious puberty",
                    "Congenital adrenal hyperplasia until proven otherwise—always",
                    "Kallmann syndrome",
                ],
                0,
                "Premature adrenarche (pubic/axillary hair before age 8) reflects adrenal androgens with absent gonadarche—dissociation is common.",
                ref(
                    "Adrenarche",
                    "Dissociation of adrenarche and gonadarche occurs in a variety of disorders of sexual maturation (see Fig. 23.4), including premature adrenarche (i.e., onset of pubic or axillary hair before 8 years of age), chronic adrenal insufficiency, central precocious puberty (CPP), primary hypogonadism, isolated gonadotropin deficiency, and anorexia nervosa.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Central Precocious Puberty",
                "A girl with NF1 develops CPP. Most common CNS lesion?",
                [
                    "Optic pathway glioma",
                    "Craniopharyngioma",
                    "Rathke cleft cyst",
                    "Empty sella",
                ],
                0,
                "In neurofibromatosis type 1, optic chiasm gliomas are the most common cause of CPP among CNS tumors in affected children.",
                ref(
                    "Neurofibromatosis Type 1",
                    "Neurofibromatosis type 1 (NF1; or von Recklinghausen disease) is associated with a propensity to develop the optic chiasm tumors that are the most common cause (but not the only cause) of the development of CPP in a child with neurofibromatosis.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Constitutional Delay in Growth and Puberty",
                "Parents of a 14-year-old CDGP boy request GH for height. Best evidence-based counseling?",
                [
                    "GH has limited height benefit in CDGP—brief sex-steroid induction addresses distress",
                    "GH reliably adds 10 cm to final height in CDGP",
                    "GnRH agonist combined with GH is standard for all CDGP",
                    "No treatment ever indicated in CDGP",
                ],
                0,
                "There is little place for GH in CDGP-associated short stature; low-dose sex-steroid replacement addresses psychosocial distress without impairing final height.",
                ref(
                    "Constitutional Delay in Growth and Puberty",
                    "There is little place for GH treatment in children with CDGP-associated short stature, as illustrated by limited height gain in the few available clinical studies.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Miscellaneous Causes",
                "When should GnRH agonist therapy for CPP be strongly recommended to protect adult height?",
                [
                    "Onset of puberty before age 6 years with rapidly advancing bone age",
                    "Any breast Tanner 2 after age 10 regardless of bone age",
                    "Premature adrenarche alone",
                    "Adolescent gynecomastia in boys",
                ],
                0,
                "Treatment is recommended for all children with puberty onset before 6 years to optimize adult height; efficacy after 8 years is inconsistent.",
                ref(
                    "Miscellaneous Causes",
                    "We recommend treatment of all affected children with onset of puberty before 6 years of age to ensure an optimal prognosis for adult height.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Delayed Puberty",
                "Initial laboratory evaluation of delayed puberty should include:",
                [
                    "LH, FSH, testosterone or estradiol, thyroid studies, and bone age",
                    "IGF-1 alone",
                    "24-hour urinary cortisol only",
                    "Synacthen test before any gonadal hormones",
                ],
                0,
                "Box 23.6 lists gonadotropins, sex steroids, thyroxine (± prolactin), bone age, and targeted imaging based on clinical findings.",
                ref(
                    "Delayed Puberty",
                    "Laboratory studies (Box 23.6) include determination of plasma LH and FSH concentrations by sensitive third-generation assays in pediatric endocrine laboratories and determination of T concentrations in boys and  $ E_{2} $ levels in girls, ideally in laboratories using HPLC-MS/MS and disposing reference values for adolescent populations.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Precocious Puberty",
                "A boy with McCune-Albright syndrome has peripheral precocity. Which treatment approach applies?",
                [
                    "Aromatase or androgen inhibitors—not GnRH agonist alone",
                    "GnRH agonist as sole therapy",
                    "Thyroid hormone suppression",
                    "No therapy possible",
                ],
                0,
                "McCune-Albright causes GnRH-independent PPP; GnRH agonists do not suppress gonadal steroid excess from autonomous ovarian/testicular activation.",
                ref(
                    "Precocious Puberty",
                    "If extrapituitary secretion of gonadotropins or secretion of gonadal steroids independent of pulsatile GnRH stimulation leads to virilization in boys or feminization in girls, the condition is termed peripheral precocious puberty (PPP).",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Timing and Onset of Puberty",
                "A child with congenital leptin deficiency loses weight on recombinant leptin and develops early pubertal LH pattern after GnRH. This supports leptin as:",
                [
                    "A permissive factor required at threshold levels, not the puberty trigger",
                    "The sole trigger of puberty in all children",
                    "Irrelevant to reproduction",
                    "A direct GnRH neuron stimulant in humans",
                ],
                0,
                "Leptin deficiency causes severe HH; replacement permits puberty but leptin alone does not trigger puberty in normal prepubertal children.",
                ref(
                    "Timing and Onset of Puberty",
                    "In summary, leptin is a permissive factor (tonic mediator) and not a trigger (phasic mediator) in the onset of human puberty (Box 23.2).",
                ),
            ),
            mcq(
                f"{p}-q24",
                "CHH Reversal",
                "A man with CHH regained fertility after prior testosterone therapy. What is essential next?",
                [
                    "Long-term monitoring—relapse to GnRH deficiency can occur",
                    "Discharge from all follow-up",
                    "Bilateral orchiectomy",
                    "Permanent GnRH agonist suppression",
                ],
                0,
                "CHH reversal occurs in ~10–20% but may not be permanent—relapse has been documented, requiring ongoing surveillance.",
                ref(
                    "CHH Reversal",
                    "Importantly, recovery of reproductive axis function may not be permanent because some patients experience a relapse to a state of GnRH deficiency; therefore, long-term monitoring is imperative.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Central Precocious Puberty",
                "After cranial irradiation, a child develops combined GH deficiency and CPP. Optimal growth strategy?",
                [
                    "Combined GH and GnRH agonist therapy",
                    "GnRH agonist alone",
                    "GH alone without addressing puberty",
                    "High-dose estrogen to fuse epiphyses rapidly",
                ],
                0,
                "GH deficiency plus CPP after CNS radiation requires combined GH and GnRH agonist for better growth and height prognosis than agonist alone.",
                ref(
                    "Central Nervous System Tumors Causing True Precocious Puberty",
                    "Treatment with a combination of GH and a GnRH agonist is indicated in these patients and results in better growth and improved height prognosis when compared with the use of a GnRH agonist alone.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Idiopathic True or Central Precocious Puberty",
                "A 7-year-old girl began breast development at 6.5 years; bone age is chronologic; predicted adult height is midparental. Management?",
                [
                    "Observation—GnRH agonist not needed for midparental height in this age range",
                    "Mandatory GnRH agonist for all CPP",
                    "Bilateral adrenalectomy",
                    "Cyproterone acetate as preferred agent",
                ],
                0,
                "Girls with puberty onset at 6–8 years often represent normal variation; meta-analysis shows GnRH agonist not needed to achieve midparental height.",
                ref(
                    "Idiopathic True or Central Precocious Puberty",
                    "In otherwise healthy girls, those with onset of puberty at 6 to 8 years of age often represent one end of the normal range of age at puberty onset; those with constitutional delay in growth and adolescence fall at the opposite end of the normal range of variation.",
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
                "The age of onset of puberty has decreased over past decades while the timing for complete pubertal development did not change.",
                True,
                "Williams KEY POINTS state earlier pubertal onset without prolongation of total pubertal duration.",
                ref(
                    "KEY POINTS",
                    "The age of onset of puberty has decreased over the past decades, although the timing for complete pubertal development did not change.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Pulsatile Secretion",
                "Puberty represents the first initiation of GnRH secretion rather than reactivation after childhood quiescence.",
                False,
                "Puberty is disinhibition/reactivation of the GnRH pulse generator after the juvenile pause, not de novo initiation.",
                ref(
                    "Central Processes of Puberty Onset",
                    "In this light, puberty does not represent the initiation or first occurrence of pulsatile secretion of GnRH or pituitary gonadotropins but the reactivation or disinhibition of GnRH neurosecretory neurons",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Kisspeptins and KISS1R",
                "Inactivating KISS1R mutations cause central precocious puberty.",
                False,
                "Inactivating KISS1R causes hypogonadotropic hypogonadism; activating KISS1/KISS1R mutations are linked to CPP.",
                ref(
                    "Kisspeptins and KISS1R",
                    "Mice transfected with mutant KISS1R genes exhibited hypogonadotropic hypogonadism (HH), although they had normal content of GnRH in the hypothalamus and were responsive to GnRH or gonadotropin administration, suggesting normal function of the gonadotroph GnRH receptors and the gonadal LH and FSH receptors despite the mutation.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Pro-Permissive Evidence",
                "A sharp rise in circulating leptin is required at the onset of human puberty.",
                False,
                "Pro-permissive evidence shows no obligatory leptin surge at puberty onset; leptin acts as permissive factor.",
                ref(
                    "Pro-Permissive Evidence",
                    "A sharp rise in circulating leptin does not occur at the onset of puberty.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Delayed Puberty",
                "Delayed puberty affects approximately 2% of the population with a male predominance.",
                True,
                "Williams cites ~2% prevalence with more males affected than females.",
                ref(
                    "Delayed Puberty",
                    "Delayed puberty is a common condition, occurring in approximately 2% of the general population, with more males affected than females.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Constitutional Delay in Growth and Puberty",
                "CDGP is the most common cause of delayed puberty and eventually resolves with full sexual maturity.",
                True,
                "CDGP is transient GnRH deficiency with eventual puberty—often termed a normal variant.",
                ref(
                    "Constitutional Delay in Growth and Puberty",
                    "CDGP is the most common cause of delayed puberty in both sexes and results from a transient state of GnRH deficiency where puberty eventually occurs, although with marked delay.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Congenital Hypogonadotropic Hypogonadism",
                "CHH is always a permanent condition with no possibility of spontaneous HPG axis recovery.",
                False,
                "A subset (~10–20%) experience CHH reversal with recovery of GnRH function, though relapse can occur.",
                ref(
                    "CHH Reversal",
                    "Although CHH was previously considered a permanent condition, it is now known that a subset of patients with CHH will spontaneously recover HPG function after treatment with T or gonadotropins.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Precocious Puberty",
                "Untreated idiopathic CPP in girls is associated with mean adult heights around 151–155 cm.",
                True,
                "Historical controls show substantially reduced final heights without treatment.",
                ref(
                    "Precocious Puberty",
                    "Untreated females with idiopathic CPP demonstrated a mean adult height of 151 to 155 cm.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Central Precocious Puberty",
                "GnRH agonist therapy suppresses adrenal androgen secretion and eliminates pubic hair in treated CPP.",
                False,
                "GnRH agonists suppress gonadotropins and gonadal steroids but do not affect adrenal androgens or sexual hair growth.",
                ref(
                    "Miscellaneous Causes",
                    "GnRH agonist therapy does not affect the secretion of adrenal androgens or sexual hair growth.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Central Precocious Puberty",
                "CPP in females leads to premature menopause.",
                False,
                "CPP does not cause premature menopause, though breast cancer risk in adulthood may be increased.",
                ref(
                    "Central Precocious Puberty",
                    "CPP in females does not lead to premature menopause.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Genetics of Central Precocious Puberty",
                "MKRN3 loss-of-function mutations are the most common monogenic cause of familial CPP.",
                True,
                "Paternally expressed MKRN3 mutations are the leading monogenic familial CPP cause in recent cohorts.",
                ref(
                    "Genetics of Central Precocious Puberty",
                    "The loss-of-function MKRN3 mutations, causing premature activation of the reproductive axis, are the most common monogenic cause of familial CPP.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Adrenarche",
                "Children with Addison disease and absent adrenal androgens usually fail to undergo normal puberty.",
                False,
                "Adrenal insufficiency patients typically have normal pubertal onset and progression despite lacking adrenarchal androgens.",
                ref(
                    "Relation to Puberty",
                    "Further, prepubertal children who have adrenal insufficiency (i.e., Addison disease) and lack adequate adrenal androgen secretion usually have a normal onset and progression of puberty.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Miscellaneous Causes",
                "GnRH agonist treatment of CPP causes an immediate sustained suppression of LH without an initial flare.",
                False,
                "An initial 1–3 day gonadotropin flare occurs before desensitization and suppression after 7–14 days.",
                ref(
                    "Miscellaneous Causes",
                    "Treatment of CPP with a potent GnRH agonist results in 1 to 3 days of increased FSH and LH release and a rise in circulating gonadal steroid levels, followed after 7 to 14 days of treatment by suppression of pulsatile secretion of LH and FSH and of the pubertal LH response to the administration of native GnRH (Figs. 23.51 and 23.52).",
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
                "Assertion: Puberty involves reawakening of the HPG axis driven by pulsatile GnRH.",
                "Reason: GnRH is secreted continuously at high levels throughout childhood without pulsatility.",
                2,
                "Assertion true; reason false—childhood features low-amplitude pulsatile GnRH during the juvenile pause, then augmented pulsatility at puberty.",
                ref(
                    "KEY POINTS",
                    "Puberty involves the reawakening of the hypothalamopituitary-gonadal (HPG) axis, driven by pulsatile gonadotropin-releasing hormone (GnRH) secretion.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Kisspeptins and KISS1R",
                "Assertion: Kisspeptin neurons in the arcuate nucleus are critical components of the GnRH pulse generator.",
                "Reason: Kisspeptin acts only on adrenal zona reticularis to cause adrenarche.",
                2,
                "Assertion true; reason false—arcuate kisspeptin innervates GnRH neurons and drives pulsatile GnRH/LH release.",
                ref(
                    "Pulsatile Secretion",
                    "The arcuate nucleus kisspeptin neurons that innervate the projections of GnRH neurons in and around their neurosecretory zone are also critical components of the pulse generator in all mammals.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Timing and Onset of Puberty",
                "Assertion: MKRN3 mutations predicted to cause loss of function can cause central precocious puberty.",
                "Reason: MKRN3 stimulates kisspeptin release to advance puberty.",
                2,
                "Assertion true; reason false—MKRN3 inhibits puberty; loss-of-function removes the brake.",
                ref(
                    "Timing and Onset of Puberty",
                    "In contrast with kisspeptin and neurokinin B, which stimulate the commencement of puberty, MKRN3 seems to inhibit puberty: Abreu and associates show that mutations in MKRN3 predicted to cause loss of function of the protein cause central precocious puberty.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Delayed Puberty",
                "Assertion: CDGP is the most frequent cause of delayed puberty.",
                "Reason: CDGP is caused by permanent destruction of GnRH neurons.",
                2,
                "Assertion true; reason false—CDGP is transient/reversible GnRH deficiency with eventual puberty.",
                ref(
                    "Delayed Puberty",
                    "The first group is CDGP, the most frequent cause, which is a transient form of GnRH deficiency causing HH.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Constitutional Delay in Growth and Puberty",
                "Assertion: CDGP is a diagnosis of exclusion.",
                "Reason: CDGP can be confirmed by a single elevated LH level at initial presentation.",
                2,
                "Assertion true; reason false—gonadotropins are low initially and rise as bone age advances; other causes must be excluded.",
                ref(
                    "Constitutional Delay in Growth and Puberty",
                    "CDGP is a diagnosis of exclusion, and other underlying causes of delayed puberty should be actively investigated and ruled out, including HH (e.g., Klinefelter syndrome or TS), permanent HH (e.g., CHH, tumors, infiltrative diseases), and functional HH (e.g., systemic illness, anorexia nervosa, excessive exercise).",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Congenital Hypogonadotropic Hypogonadism",
                "Assertion: CHH presents with low sex steroids and low or normal gonadotropins.",
                "Reason: CHH is defined by primary gonadal failure with elevated LH and FSH.",
                2,
                "Assertion true; reason false—CHH is hypogonadotropic, not hypergonadotropic.",
                ref(
                    "Congenital Hypogonadotropic Hypogonadism",
                    "the diagnosis relies on low serum sex steroids in the setting of low/normal serum gonadotropin levels, otherwise normal pituitary function, and the absence of a hypothalamic-pituitary lesion on MRI.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Precocious Puberty",
                "Assertion: CPP is GnRH-dependent with pubertal LH response to GnRH agonist.",
                "Reason: All forms of sexual precocity, including CPP, are independent of GnRH stimulation.",
                2,
                "Assertion true; reason false—only CPP is GnRH-dependent; PPP is GnRH-independent.",
                ref(
                    "Precocious Puberty",
                    "Pulsatile LH release has a pubertal pattern, and the rise in the concentration of LH after GnRH or GnRH agonist administration is indistinguishable from the normal pubertal pattern of serum LH.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Precocious Puberty",
                "Assertion: Sexual precocity can cause tall stature in childhood but short adult height.",
                "Reason: Precocious puberty delays bone age advancement and epiphyseal fusion.",
                2,
                "Assertion true; reason false—precocity accelerates skeletal maturation and premature epiphyseal fusion.",
                ref(
                    "Precocious Puberty",
                    "because of premature epiphyseal fusion, sexual precocity can lead to the paradox of tall stature in childhood but short adult height (Table 23.7).",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Central Precocious Puberty",
                "Assertion: CNS tumors must be considered in any patient with CPP.",
                "Reason: CNS tumors causing CPP are more common in girls than boys.",
                2,
                "Assertion true; reason false—CNS lesions are proportionally far more common in boys with CPP.",
                ref(
                    "Central Precocious Puberty",
                    "A CNS neoplasm must be considered in the differential diagnosis of any patient with CPP.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Miscellaneous Causes",
                "Assertion: GnRH agonist therapy improves adult height in CPP when started early.",
                "Reason: GnRH agonists accelerate bone age maturation during treatment.",
                2,
                "Assertion true; reason false—agonists slow skeletal maturation dramatically, preserving height potential.",
                ref(
                    "Miscellaneous Causes",
                    "Skeletal maturation slows dramatically during the first 3 years, to a rate that often is less than the progression in chronologic age.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Pro-Permissive Evidence",
                "Assertion: Leptin is a permissive factor for human puberty onset.",
                "Reason: All children require a doubling of leptin levels to enter puberty.",
                2,
                "Assertion true; reason false—threshold permissive leptin is needed but a surge is not required.",
                ref(
                    "Pro-Permissive Evidence",
                    "In constitutional delay in growth and adolescence, an increase in prepubertal leptin levels is not essential for the onset of puberty.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Hamartomas of the Tuber Cinereum",
                "Assertion: Hypothalamic hamartomas can cause CPP through ectopic GnRH secretion.",
                "Reason: Continuous non-pulsatile GnRH release from hamartomas causes CPP by receptor desensitization.",
                2,
                "Assertion true; reason false—pulsatile, not continuous, GnRH release from hamartomas causes CPP.",
                ref(
                    "Hamartomas of the Tuber Cinereum",
                    "If the hamartoma were to secrete GnRH in a continuous fashion, CPP would not occur because the GnRH receptors would be desensitized.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "23",
        "title": "Physiology and Disorders of Puberty",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Nelly Pitteloud, Georgios E. Papadakis, and An Jacobs",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_23_Physiology_and_Disorders_of_Puberty.md",
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
