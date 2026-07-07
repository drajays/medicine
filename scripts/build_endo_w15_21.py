#!/usr/bin/env python3
"""Generate Williams 15e module w15-21 — Differences of Sex Development."""
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
OUT_NAME = "w15-21_Differences_of_Sex_Development.json"


def build() -> dict:
    p = "w15-21"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why achieving a DSD diagnosis matters",
                "Diagnosis informs natural history, associated features, endocrine monitoring, tumor risk, fertility counseling, inheritance, and sometimes gender-assignment decisions.",
                ref(
                    "KEY POINTS",
                    "Achieving a diagnosis is important for understanding the natural history of specific conditions, identifying associated features, monitoring endocrine function and tumor risk, advising about fertility potential, and counseling families about inheritance patterns.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How multidisciplinary care should span the lifespan",
                "DSD are chronic, multisystem conditions with broad psychosocial impact; coordinated MDT care from diagnosis through adulthood is essential.",
                ref(
                    "KEY POINTS",
                    "A multidisciplinary team approach is key in providing coordinated management from diagnosis through later life.",
                ),
            ),
            note(
                f"{p}-n3",
                "Sex Determination and Sex Differentiation",
                "Why sex determination differs from sex differentiation",
                "Sex determination commits the bipotential gonad to testis or ovary; sex differentiation shapes internal and external genitalia under gonadal peptide hormones and steroids.",
                ref(
                    "Sex Determination and Sex Differentiation",
                    "Sex determination is the process whereby the bipotential gonad develops into a testis or an ovary. Sex differentiation refers to the development of the internal and external genitalia, as directed by the production of peptide hormones and sex steroids by the developing gonad.",
                ),
            ),
            note(
                f"{p}-n4",
                "Male Sex Differentiation",
                "How testosterone and AMH drive male development",
                "Testicular testosterone stabilizes wolffian structures; AMH causes müllerian regression; DHT masculinizes external genitalia and urogenital sinus.",
                ref(
                    "Sex Determination and Sex Differentiation",
                    "Testicular production of testosterone and anti-müllerian hormone (AMH; also called müllerian-inhibiting factor/substance [MIF/MIS]) is required for typical male sex development.",
                ),
            ),
            note(
                f"{p}-n5",
                "Classification of Differences of Sex Development",
                "How karyotype guides initial DSD workup",
                "Consensus classification groups DSD into sex-chromosome, XY, and XX categories—karyotype does not define gender but focuses investigations and counseling.",
                ref(
                    "Classification of Differences of Sex Development",
                    "The consensus statement that introduced the term DSD further suggested a classification of DSD by karyotype (Table 21.2): sex-chromosome DSD (variations in sex-chromosome complement), XY DSD (conditions affecting testis development, androgen synthesis, and androgen action), and XX DSD (androgen excess and conditions affecting ovarian development).",
                ),
            ),
            note(
                f"{p}-n6",
                "21-Hydroxylase Deficiency",
                "Why 46,XX CAH is the classic newborn DSD emergency",
                "21-hydroxylase deficiency is among the most common causes of atypical newborn genitalia; salt-wasting adrenal crisis can be life-threatening if missed.",
                ref(
                    "21-Hydroxylase Deficiency",
                    "Deficiency of 21-hydroxylase (CYP21A2) (see Fig. 21.11) is one of the most common causes of atypical genital appearance in newborns, affecting around 1 in 15,000 children, with most XX patients presenting at birth due to virilization of the genitalia (see Chapter 13).",
                ),
            ),
            note(
                f"{p}-n7",
                "Conditions Affecting Testicular Development",
                "How complete gonadal dysgenesis (Swyer) presents",
                "Swyer syndrome: 46,XY with no external virilization and persistent müllerian structures from absent AMH; partial dysgenesis spans clitoromegaly to hypospadias.",
                ref(
                    "Conditions Affecting Testicular Development",
                    "Complete testicular dysgenesis, a condition sometimes called Swyer syndrome, is associated with a complete lack of virilization of the external genitalia and persistent müllerian structures due to low AMH production.",
                ),
            ),
            note(
                f"{p}-n8",
                "Conditions Affecting Androgen Action",
                "Why CAIS differs from Swyer on exam and labs",
                "CAIS: female external genitalia, breast development, primary amenorrhea, absent uterus (AMH intact), elevated testosterone/LH; Swyer lacks gonadal steroids and retains müllerian structures.",
                ref(
                    "Conditions Affecting Androgen Action",
                    "The main differential diagnosis in an adolescent with an XY karyotype is complete gonadal dysgenesis (Swyer syndrome), which is distinguished from CAIS by (1) absence of gonadal sex-steroid production, resulting in little to no breast development, and (2) absence of AMH production, resulting in retention of müllerian structures, in Swyer syndrome.",
                ),
            ),
            note(
                f"{p}-n9",
                "Ovotesticular Differences of Sex Development",
                "How ovotesticular DSD is defined histologically",
                "Ovotesticular DSD requires ovarian tissue with follicles plus testicular tissue in the same or opposite gonad—whorled stroma without oocytes is insufficient.",
                ref(
                    "Ovotesticular Differences of Sex Development",
                    "The diagnosis of ovotesticular DSD requires the presence of ovarian tissue (containing follicles) and testicular tissue in the same or the opposite gonad (Fig. 21.19; see Table 21.3).",
                ),
            ),
            note(
                f"{p}-n10",
                "45,X/46,XY Mosaicism and Variants",
                "Why genital asymmetry suggests mixed gonadal dysgenesis",
                "Asymmetric external genitalia strongly suggests asymmetric gonadal development (mixed gonadal dysgenesis); müllerian structures may be hemiuterine on the dysgenetic side.",
                ref(
                    "45,X/46,XY Mosaicism and Variants",
                    "Asymmetry of the external genitalia strongly suggests asymmetric gonadal development (i.e., mixed gonadal dysgenesis).",
                ),
            ),
            note(
                f"{p}-n11",
                "The Initial Approach to the Baby With Atypical Genitalia",
                "How to use the BASIC newborn DSD mnemonic",
                "BASIC: Bonding, Adrenal insufficiency screening, Sex/gender designation, Imaging, Cytogenetics—addresses psychosocial needs, salt-wasting risk, assignment, anatomy, and karyotype.",
                ref(
                    "The Initial Approach to the Baby With Atypical Genitalia",
                    "A useful mnemonic for the initial approach is BASIC: bonding, adrenal insufficiency, sex/gender designation, imaging, and cytogenetics.",
                ),
            ),
            note(
                f"{p}-n12",
                "Sex/Gender Designation",
                "Why gender assignment should not be rushed",
                "Premature sex designation can be traumatic to reverse; use neutral language while gathering karyotype, diagnosis, anatomy, endocrine function, fertility, and tumor-risk data.",
                ref(
                    "Sex/Gender Designation",
                    "Sex/gender designation should be undertaken as soon as possible but should not be rushed.",
                ),
            ),
            note(
                f"{p}-n13",
                "Investigations for DSD",
                "How AMH helps distinguish XY DSD mechanisms",
                "AMH is detectable throughout childhood; low AMH suggests testicular dysgenesis or streak gonads, while elevated AMH with female genitalia suggests AIS or androgen-synthesis defects.",
                ref(
                    "Investigations for DSD",
                    "AMH is detectable throughout childhood and is reduced in testicular dysgenesis or absent in cases of streak gonads or anorchia; AMH may be high in AIS or reduced androgen production due to steroidogenic defects.",
                ),
            ),
            note(
                f"{p}-n14",
                "Tumor Risk and DSD",
                "Why gonadal tumor risk varies by DSD category",
                "Gonadal dysgenesis with Y-chromosomal GBY carries high early GCT risk; differentiated testes with androgen synthesis/action defects have lower prepubertal risk.",
                ref(
                    "Tumor Risk and DSD",
                    "In general, forms of DSD with impaired or arrested gonadal development (gonadal dysgenesis) have a high risk of GCTs that can be present early in life—as early as 3 months of age—whereas forms of DSD with normal testis development but reduced androgen synthesis or action have a lower risk, and gonadal tumors rarely arise before puberty.",
                ),
            ),
            note(
                f"{p}-n15",
                "Surgery and DSD",
                "How timing of DSD surgery has evolved",
                "Surgery is no longer automatic; indications, timing, and cosmetic vs functional goals require individualized MDT discussion with option to defer until the child can participate.",
                ref(
                    "Surgery and DSD",
                    "Surgery was once felt to be a standard part of the management of DSD, but there is now much more cautious consideration of the need for surgery and its timing.",
                ),
            ),
            note(
                f"{p}-n16",
                "Terminology",
                "Why to use condition-specific names with families",
                "Use the specific diagnosis when speaking with families; 'differences of sex development' replaced 'disorders' but remains debated—engage about preferred terms.",
                ref(
                    "Terminology",
                    "When speaking with a patient or family, it is generally best to use the name of the patient's specific condition, if known, instead of DSD.",
                ),
            ),
            note(
                f"{p}-n17",
                "Chromosomal Sex",
                "SRY as the primary testis-determining gene",
                "SRY loss-of-function causes 46,XY complete gonadal dysgenesis; transgenic Sry expression can induce testis development in XX mice.",
                ref(
                    "Chromosomal Sex",
                    "A series of elegant studies in mice and humans established Sry/SRY as the primary Y-chromosomal testis-determining gene.",
                ),
            ),
            note(
                f"{p}-n18",
                "Conditions Affecting Androgen Synthesis",
                "5α-reductase deficiency and pubertal virilization",
                "46,XY individuals with 5α-reductase deficiency may be raised female but virilize at puberty when testosterone rises—genetic confirmation guides gender counseling.",
                ref(
                    "Presentation During Adolescence",
                    "The conditions that are typically associated with virilization at puberty are 5α-reductase deficiency and 17β-hydroxysteroid dehydrogenase deficiency.",
                ),
            ),
            note(
                f"{p}-n19",
                "Management of Androgen Insensitivity Syndromes",
                "CAIS gonadectomy timing and counseling",
                "Female rearing is recommended for CAIS; delaying gonadectomy allows spontaneous puberty and shared decision-making; prepubertal tumor risk is low (~0.8–2%).",
                ref(
                    "Management of Androgen Insensitivity Syndromes",
                    "Female sex designation and gender of rearing are recommended for individuals with CAIS, although recent studies have suggested that around 2% of individuals with CAIS may not identify as female later in life.",
                ),
            ),
            note(
                f"{p}-n20",
                "Steroidogenic Factor 1: NR5A1",
                "NR5A1 mutations across the XY DSD spectrum",
                "Heterozygous NR5A1 variants cause ~15% of mild XY gonadal dysgenesis with normal adrenal function; homozygous mutations cause adrenal failure and severe under-virilization.",
                ref(
                    "Steroidogenic Factor 1: NR5A1",
                    "A range of phenotypes is seen, most commonly mild gonadal dysgenesis and significantly impaired virilization, where alterations in SF1 are found in approximately 15% of cases.",
                ),
            ),
            note(
                f"{p}-n21",
                "The Newborn With Atypical Genital Appearance",
                "Prevalence and red-flag newborn genital findings",
                "~1 in 2000 newborns need specialist evaluation; bilateral nonpalpable gonads may signal life-threatening salt-wasting CAH in an XX infant.",
                ref(
                    "The Newborn With Atypical Genital Appearance",
                    "It is estimated that around 1 in 2000 babies has a genital appearance that warrants specialist evaluation.",
                ),
            ),
            note(
                f"{p}-n22",
                "Presentation During Adolescence",
                "Three adolescent DSD presentations",
                "Adolescent DSD: (1) virilization at puberty, (2) absent puberty, (3) primary amenorrhea after breast development—each needs sensitive MDT evaluation.",
                ref(
                    "Presentation During Adolescence",
                    "Another common time for DSD to present is during adolescence in one of three well-recognized ways: (1) a girl who experiences spontaneous virilization at puberty, (2) a girl with absence of pubertal development, and (3) a girl who has primary amenorrhea after having normal breast development.",
                ),
            ),
            note(
                f"{p}-n23",
                "Other Conditions Affecting XY Sex Development",
                "Persistent müllerian duct syndrome (PMDS)",
                "XY males with normal external genitalia and testes but müllerian derivatives—often discovered at hernia repair; AMH or AMHR2 mutations in ~88% of proven cases.",
                ref(
                    "Other Conditions Affecting XY Sex Development",
                    "Persistent müllerian duct syndrome (PMDS) is a condition in which XY males have well-developed testes and normal male external genitalia but also have müllerian duct derivatives.",
                ),
            ),
            note(
                f"{p}-n24",
                "Klinefelter Syndrome and Variants",
                "Klinefelter and the Y chromosome in sex determination",
                "47,XXY males develop testes and male genitalia—evidence that Y-chromosome presence (not X number) drives testis determination; postnatal hypogonadism emerges in adolescence.",
                ref(
                    "Klinefelter Syndrome and Variants",
                    "The development of testes and a male genital phenotype in individuals with Klinefelter syndrome provides important evidence for the key role of the presence of the Y chromosome (rather than X-chromosome number) in testis determination and subsequent prenatal androgen production.",
                ),
            ),
            note(
                f"{p}-n25",
                "Genetic Testing and DSD",
                "Next-generation sequencing in DSD diagnosis",
                "Molecular diagnosis is reached in ~25–40% of gonadal dysgenesis and most classic steroidogenesis disorders; panel/exome sequencing is increasingly central but needs careful counseling.",
                ref(
                    "Differences of Sex Development",
                    "The percentage of patients with conditions affecting gonadal development who can be diagnosed at the molecular level is increasing with the use of next generation sequencing of gene panels or exomes (currently around 25%–40%),",
                ),
            ),
            note(
                f"{p}-n26",
                "Fertility/Family Building",
                "Fertility options across DSD conditions",
                "Many DSD forms cause infertility, but TESE-ICSI (PAIS, 5α-reductase), donor gametes, adoption, and uterus transplantation expand family-building options when counseling is individualized.",
                ref(
                    "Fertility/Family Building",
                    "Many forms of DSD are associated with reduced fertility or infertility.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "The Newborn With Atypical Genital Appearance",
                "A 3-day-old with Prader stage 3 genitalia and bilateral impalpable gonads is hemodynamically stable. Most urgent next step?",
                [
                    "Serial electrolytes and CAH biochemical workup while avoiding premature sex assignment",
                    "Immediate clitoroplasty before karyotype returns",
                    "Empiric testosterone for micropenis",
                    "Discharge home; reassess at 6 months",
                ],
                0,
                "Nonpalpable gonads in virilized-appearing neonates may be salt-wasting 46,XX CAH; BASIC workup and adrenal monitoring take priority over surgery or assignment.",
                ref(
                    "The Initial Approach to the Baby With Atypical Genitalia",
                    "Adrenal insufficiency is associated with some causes of DSD and is potentially life threatening if not promptly recognized and treated.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "21-Hydroxylase Deficiency",
                "A newborn with 46,XX karyotype, marked clitoromegaly, and rising 17-OHP has normal blood pressure. Best initial glucocorticoid strategy?",
                [
                    "Hydrocortisone (or equivalent) at stress-replacement doses with mineralocorticoid if salt-wasting",
                    "Fludrocortisone alone without glucocorticoid",
                    "High-dose dexamethasone to maximize growth suppression",
                    "Withhold steroids until adrenarche",
                ],
                0,
                "Classic CAH requires glucocorticoid replacement and mineralocorticoid/salt when salt-wasting; virilization is addressed after adrenal stabilization.",
                ref(
                    "21-Hydroxylase Deficiency",
                    "High fetal concentrations of 17-OHP, androstenedione, and testosterone are the hallmark of CAH due to 21-hydroxylase deficiency.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Conditions Affecting Androgen Action",
                "A 16-year-old with primary amenorrhea, Tanner IV breasts, scant pubic hair, and 46,XY karyotype most likely has:",
                [
                    "Complete androgen insensitivity syndrome",
                    "Turner syndrome",
                    "5α-reductase deficiency",
                    "Classic 21-hydroxylase deficiency",
                ],
                0,
                "CAIS presents with female phenotype, breast development from aromatized androgens, absent uterus, and androgen resistance with elevated testosterone/LH.",
                ref(
                    "Conditions Affecting Androgen Action",
                    "CAIS is an X-linked condition that typically presents in an adolescent female who had breast development and a pubertal growth spurt but who has not had menarche (Box 21.10).",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Conditions Affecting Testicular Development",
                "A 14-year-old with 46,XY karyotype, no breast development, primary amenorrhea, and a uterus on ultrasound most likely has:",
                [
                    "Complete gonadal dysgenesis (Swyer syndrome)",
                    "Complete androgen insensitivity syndrome",
                    "17α-hydroxylase deficiency",
                    "Klinefelter syndrome",
                ],
                0,
                "Swyer syndrome: dysgenetic streak gonads with absent AMH (uterus present) and no estrogen-driven breast development.",
                ref(
                    "Presentation During Adolescence",
                    "In complete testicular dysgenesis (Swyer syndrome), both Leydig cell production of testosterone and Sertoli cell production of AMH are impaired. As a result, müllerian structures are typically present.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Other Conditions Affecting XY Sex Development",
                "A boy undergoing inguinal hernia repair is found to have a uterus and fallopian tubes alongside testes. Serum AMH is undetectable. Diagnosis?",
                [
                    "Persistent müllerian duct syndrome due to AMH or AMHR2 defect",
                    "Partial androgen insensitivity syndrome",
                    "Ovotesticular DSD",
                    "Complete gonadal dysgenesis",
                ],
                0,
                "PMDS: normal male external genitalia with müllerian persistence; low AMH suggests AMH gene mutation (normal AMH with müllerian structures suggests AMHR2 defect).",
                ref(
                    "Other Conditions Affecting XY Sex Development",
                    "Measurement of serum AMH can provide a useful means for guiding genetic analysis; patients with PMDS caused by mutations of the AMH gene typically have low or undetectable levels of serum AMH (except for the p.Gln496His mutation, which is thought to affect receptor binding), whereas AMH concentrations are normal for age or elevated in patients with mutations in AMHR2.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "45,X/46,XY Mosaicism and Variants",
                "A newborn with asymmetric labioscrotal development and a palpable gonad only on the right has 45,X/46,XY mosaicism. Most likely gonadal pattern?",
                [
                    "Mixed gonadal dysgenesis with dysgenetic gonad on one side and more differentiated gonad on the other",
                    "Bilateral normal testes",
                    "Bilateral ovaries with normal müllerian structures",
                    "Ovotesticular DSD requiring immediate gender-neutral rearing only",
                ],
                0,
                "45,X/46,XY mosaicism with genital asymmetry suggests mixed gonadal dysgenesis; tumor risk and sex assignment require individualized MDT assessment.",
                ref(
                    "45,X/46,XY Mosaicism and Variants",
                    "Marked differences in gonadal development and histologic appearance can sometimes be seen between the right and the left sides (referred to as mixed gonadal dysgenesis) or even within a single gonad.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Ovotesticular Differences of Sex Development",
                "A child with 46,XX/46,XY chimerism and inguinal gonads plus hemiuterus. Biopsy shows follicles and seminiferous tubules. Management priority?",
                [
                    "MDT counseling on gender, tumor risk, and timed gonadal surgery vs puberty blockade",
                    "Immediate bilateral gonadectomy in infancy without discussion",
                    "No evaluation needed—chimerism is benign",
                    "Start high-dose androgen in infancy for all cases",
                ],
                0,
                "Ovotesticular DSD management depends on age, anatomy, hormone production, fertility potential, and patient/family goals; gonadectomy timing is individualized.",
                ref(
                    "Ovotesticular Differences of Sex Development",
                    "The management of ovotesticular DSD depends on the age at diagnosis, genital development, internal structures, and reproductive capacity.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Conditions Affecting Androgen Synthesis",
                "A 46,XY infant with female external genitalia has low testosterone that does not rise after prolonged hCG; LH is elevated. Müllerian structures are absent. Next test?",
                [
                    "LHCGR gene sequencing for Leydig cell hypoplasia",
                    "CYP21A2 sequencing first",
                    "Karyotype repeat expecting 47,XXY",
                    "AMH level only—no further testing",
                ],
                0,
                "Leydig cell hypoplasia (LHCGR mutations) causes undervirilization with intact Sertoli/AMH function; hCG fails to stimulate testosterone.",
                ref(
                    "Conditions Affecting Androgen Synthesis",
                    "The typical biochemical profile of patients with Leydig cell hypoplasia includes elevated basal and GnRH-stimulated LH (and FSH) levels in early infancy or at puberty due to loss of sex-steroided negative feedback.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Conditions Affecting Androgen Synthesis",
                "A 13-year-old raised female virilizes at puberty with rising testosterone; testosterone:DHT ratio >20. Most likely diagnosis?",
                [
                    "5α-reductase 2 deficiency",
                    "Complete androgen insensitivity syndrome",
                    "Turner syndrome",
                    "Aromatase deficiency",
                ],
                0,
                "5α-reductase deficiency impairs DHT formation; pubertal testosterone surge causes virilization; elevated T:DHT ratio supports the diagnosis.",
                ref(
                    "Presentation During Adolescence",
                    "The conditions that are typically associated with virilization at puberty are 5α-reductase deficiency and 17β-hydroxysteroid dehydrogenase deficiency.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Conditions Affecting Androgen Action",
                "A girl with bilateral inguinal hernias at age 2 is found to have testes in the hernia sac. Best screening step?",
                [
                    "Karyotype or Y-chromosome FISH because ~1–2% of girls with bilateral inguinal hernias have CAIS",
                    "No workup—hernia repair only",
                    "Immediate gonadectomy before cytogenetics",
                    "ACTH stimulation test",
                ],
                0,
                "Bilateral inguinal hernias are rare in girls; CAIS may present this way—evaluate for Y-chromosomal material before assignment assumptions.",
                ref(
                    "Conditions Affecting Androgen Action",
                    "Bilateral inguinal hernias are rare in girls, and an estimated 1% to 2% of girls with bilateral inguinal hernias have CAIS.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Sex/Gender Designation",
                "Parents of a newborn with 46,XY PAIS and minimal virilization ask for immediate female assignment. Best counseling point?",
                [
                    "Gather karyotype, diagnosis, anatomy, and psychosocial data before rushing assignment—reversal is traumatic",
                    "Assign male because XY karyotype always dictates male rearing",
                    "Defer all discussion until age 18",
                    "Perform gonadectomy before any conversation",
                ],
                0,
                "Sex/gender designation should be thoughtful; premature assignment that later conflicts with identity or anatomy carries major psychosocial harm.",
                ref(
                    "Sex/Gender Designation",
                    "However, if an inappropriate gender designation is made initially, it can be very traumatic to change the designation later, so keeping an open mind from the start and avoiding premature recommendations is critical.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Investigations for DSD",
                "An XY newborn with impalpable gonads has detectable AMH. This finding most strongly suggests:",
                [
                    "Functional testicular tissue rather than anorchia or streak gonads",
                    "Ovarian tissue only",
                    "Adrenal crisis from CAH",
                    "Complete androgen insensitivity with absent testes",
                ],
                0,
                "AMH is a marker of Sertoli cell/testicular integrity; undetectable AMH with high gonadotropins predicts anorchia.",
                ref(
                    "Investigations for DSD",
                    "AMH is detectable throughout childhood and is reduced in testicular dysgenesis or absent in cases of streak gonads or anorchia",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Tumor Risk and DSD",
                "A 46,XY patient with Frasier syndrome (WT1 splice mutation) has intra-abdominal dysgenetic gonads. Recommended gonadal management?",
                [
                    "Prophylactic gonadectomy when gonads are nonfunctional and not monitorable—tumor risk up to ~60%",
                    "Observation only until age 40",
                    "Annual AFP screening replaces gonadectomy",
                    "Testosterone stimulation to prevent tumors",
                ],
                0,
                "Frasier syndrome carries the highest early gonadoblastoma risk; prophylactic gonadectomy is recommended for nonfunctional undescended gonads.",
                ref(
                    "Tumor Risk and DSD",
                    "The highest risk for early gonadoblastoma occurs for patients with Frasier syndrome (caused by mutations in WT1), for whom the risk may be as high as 60%.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Management of Androgen Insensitivity Syndromes",
                "A woman with CAIS asks whether to keep intra-abdominal testes after spontaneous puberty. Most accurate counseling?",
                [
                    "Prepubertal malignancy risk is low; adolescent/adult GCNIS risk ~10–14%—shared decision on gonadectomy vs surveillance",
                    "Gonadectomy is mandatory in infancy for all CAIS",
                    "Tumor risk is zero if testosterone is elevated",
                    "MRI reliably detects GCNIS annually",
                ],
                0,
                "CAIS gonadal tumors rarely arise before puberty; delaying gonadectomy enables spontaneous puberty but requires counseling on surveillance limitations.",
                ref(
                    "Management of Androgen Insensitivity Syndromes",
                    "In CAIS, the risk of developing GCNIS or a germ cell tumor before puberty is low (on the order of 0.8%–2%).",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Surgery and DSD",
                "Parents of a girl with salt-wasting CAH request clitoroplasty in the first month of life. Best recommendation per current practice?",
                [
                    "Observe with medical CAH treatment first—clitoral size often decreases; defer elective genital surgery",
                    "Mandatory early clitoroplasty for all CAH girls",
                    "Gonadectomy before adrenal stabilization",
                    "No glucocorticoids until after surgery",
                ],
                0,
                "Feminizing genital surgery in CAH is increasingly deferred; adrenal suppression often reduces clitoromegaly and outcome data show surgical harms.",
                ref(
                    "Surgery and DSD",
                    "For babies with CAH, treatment to achieve adrenal suppression often results in considerable reduction in the size of the clitorophallus, and the clitorophallus may also become less prominent as the child grows, so a period of observation is appropriate before decisions about surgery are made.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Steroidogenic Factor 1: NR5A1",
                "A 46,XY newborn with female genitalia, müllerian structures, and primary adrenal insufficiency. Highest-yield gene test?",
                [
                    "NR5A1 (SF1) homozygous or severe compound heterozygous mutations",
                    "AR gene sequencing",
                    "CYP19A1",
                    "SRY deletion only",
                ],
                0,
                "Homozygous NR5A1 mutations cause combined adrenal failure and 46,XY gonadal dysgenesis with müllerian persistence.",
                ref(
                    "Steroidogenic Factor 1: NR5A1",
                    "NR5A1 mutations were first reported in two XY individuals with female external genitalia, persistent müllerian structures, and primary adrenal insufficiency.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Conditions Affecting Androgen Synthesis",
                "A 46,XY infant presents at 6 weeks with adrenal crisis, female genitalia, and absent müllerian structures. STAR mutation is found. Diagnosis?",
                [
                    "Lipoid congenital adrenal hyperplasia",
                    "Isolated 17α-hydroxylase deficiency",
                    "Partial androgen insensitivity syndrome",
                    "Ovotesticular DSD",
                ],
                0,
                "Lipoid CAH from StAR defects causes severe adrenal insufficiency; XY infants have female external genitalia with regressed müllerian ducts.",
                ref(
                    "Steroidogenic Acute Regulatory Protein Defects",
                    "In XY individuals, mutations in STAR typically cause a marked deficiency in testosterone synthesis by fetal Leydig cells so that there is also typical female genital appearance.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Presentation During Adolescence",
                "A girl with primary amenorrhea, normal breasts, 46,XY karyotype, and male-range testosterone. Pelvic ultrasound shows no uterus. Next step?",
                [
                    "AR gene sequencing and CAIS counseling including gonadal management",
                    "Immediate hysterectomy",
                    "Start GnRH agonist for precocious puberty",
                    "Diagnose MRKH syndrome",
                ],
                0,
                "Breast development with absent uterus and XY karyotype is classic CAIS; MRKH is XX with uterine agenesis.",
                ref(
                    "Presentation During Adolescence",
                    "In the absence of a uterus, the diagnosis is most likely to be CAIS if the karyotype is XY and testosterone is in the male range or a form of uterine agenesis, such as MRKH syndrome, if the karyotype is XX.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Klinefelter Syndrome and Variants",
                "A 17-year-old 47,XXY boy has small firm testes, gynecomastia, and testosterone in the lower male range with elevated FSH. Best management?",
                [
                    "Counsel on learning/support needs; consider testosterone replacement and fertility preservation discussion",
                    "Immediate bilateral gonadectomy",
                    "Estrogen replacement to induce breasts",
                    "No follow-up—phenotype is benign",
                ],
                0,
                "Klinefelter syndrome needs education support, monitoring of testosterone during puberty, and discussion of fertility options including TESE-ICSI.",
                ref(
                    "Klinefelter Syndrome and Variants",
                    "A significant proportion of individuals with Klinefelter syndrome receive testosterone supplementation to fully induce puberty and to support sex characteristics, sexual desire, and bone mineralization in adult life.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Genetic Testing and DSD",
                "Rapid newborn DSD workup at a center without karyotyping capacity. Best interim chromosomal assessment?",
                [
                    "FISH or qfPCR for X and Y signals while expediting full karyotype",
                    "Defer all genetics for 1 year",
                    "AMH alone replaces chromosomal testing",
                    "Parental karyotype only",
                ],
                0,
                "Rapid sex-chromosome complement assessment (FISH or qfPCR) guides urgent CAH vs XY DSD pathways while formal karyotype is pending.",
                ref(
                    "The Initial Approach to the Baby With Atypical Genitalia",
                    "For centers that cannot conduct rapid karyotyping, rapid determination of sex-chromosome complement can be performed by FISH for X-chromosome and Y-chromosome markers (see Fig. 21.3), and in some centers, it is now being performed by quantitative fluorescent polymerase chain reaction (qPCR) on DNA.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Conditions Affecting Androgen Action",
                "A boy with PAIS (confirmed AR mutation) and EMS 3 at birth reaches puberty. Most likely pubertal course?",
                [
                    "Variable spontaneous virilization—may need supraphysiologic androgens; gynecomastia is common",
                    "Complete absence of any testosterone rise",
                    "Automatic female gender identity",
                    "No risk of germ cell tumors ever",
                ],
                0,
                "PAIS pubertal development is unpredictable; functional AR assays do not reliably predict androgen needs; gynecomastia is nearly universal.",
                ref(
                    "Management of Androgen Insensitivity Syndromes",
                    "Gynecomastia is an almost universal finding as boys with PAIS reach puberty.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Wilms Tumor 1 Gene: WT1",
                "A 46,XY infant with penoscrotal hypospadias, cryptorchidism, and early proteinuria. Gene to prioritize?",
                [
                    "WT1 (Denys-Drash or Frasier syndrome)",
                    "CYP21A2",
                    "INSL3",
                    "KCNJ11",
                ],
                0,
                "WT1 mutations cause DSD with nephropathy and tumor predisposition—urinalysis for proteinuria is essential in 46,XY DSD.",
                ref(
                    "Wilms Tumor 1 Gene: WT1",
                    "Taken together, these cases highlight the importance of considering this diagnosis in 46,XY DSD and of performing urinalysis for proteinuria in children with 46,XY DSD.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "The Initial Approach to the Baby With Atypical Genitalia",
                "Pelvic ultrasound in a newborn DSD shows a structure interpreted as uterus. Before confirming, you should:",
                [
                    "Correlate with AMH and examination—utricular remnants and bowel loops can be mistaken for uterus",
                    "Accept ultrasound as definitive for sex assignment",
                    "Skip karyotype if uterus seen",
                    "Start estrogen immediately",
                ],
                0,
                "Imaging in DSD is operator-dependent; utricular remnants and bowel may mimic müllerian structures—biochemistry and cytogenetics are essential.",
                ref(
                    "The Initial Approach to the Baby With Atypical Genitalia",
                    "Also, a utricular remnant (commonly found in boys with hypospadias) or a loop of bowel can be mistaken as a uterus, and lymph nodes can be mistaken as testes.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Sex-Determining Region of the Y Chromosome: SRY and SRY-Related Homeobox Genes 8 and 9 (SOX8 and SOX9)",
                "A 46,XY adolescent with female genitalia and no puberty is found to have SRY HMG-box mutation. Gonadal management?",
                [
                    "Gonadectomy recommended—high gonadal tumor risk in SRY-related complete dysgenesis",
                    "No tumor risk—observe gonads lifelong",
                    "Testosterone to induce müllerian regression",
                    "Oocyte harvest for fertility",
                ],
                0,
                "SRY mutations cause Swyer syndrome with high gonadal malignancy risk; dysgenetic gonads should be removed.",
                ref(
                    "Sex-Determining Region of the Y Chromosome: SRY and SRY-Related Homeobox Genes 8 and 9 (SOX8 and SOX9)",
                    "Most individuals with SRY mutations present as girls who have no pubertal development (Swyer syndrome). Gonadal tumor risk in this group is high.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Presentation During Adolescence",
                "A 15-year-old 46,XY patient with 17α-hydroxylase deficiency has hypertension and delayed puberty. Internal genitalia finding?",
                [
                    "Absent uterus because AMH production is intact",
                    "Normal uterus and fallopian tubes",
                    "Bilateral ovaries",
                    "Persistent müllerian duct syndrome",
                ],
                0,
                "17α-hydroxylase deficiency blocks adrenal/gonadal steroids but Sertoli AMH secretion persists, so müllerian structures regress.",
                ref(
                    "Presentation During Adolescence",
                    "In contrast, an XY individual with 17α-hydroxylase/17,20-lyase deficiency has intact Sertoli cell function and AMH production and, as a result, does not have a uterus.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Support for the Parents",
                "Parents of a newborn with DSD are overwhelmed by family asking 'boy or girl?' Best initial support strategy?",
                [
                    "Help them plan communication—some delay announcement; offer written materials and MDT contact",
                    "Insist they announce sex immediately",
                    "Avoid all psychosocial support until adolescence",
                    "Refer only to surgery without counseling",
                ],
                0,
                "Parental stress from social questioning is common; individualized communication strategies and information leaflets reduce isolation.",
                ref(
                    "Support for the Parents",
                    "A potentially significant source of stress for parents can be repeated questions from family and friends regarding whether the child is a girl or a boy.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Classification of Differences of Sex Development",
                "DSD is defined as congenital conditions in which chromosomal, gonadal, or anatomic sex is atypical.",
                True,
                "This is the consensus umbrella definition introduced in 2006.",
                ref(
                    "Classification of Differences of Sex Development",
                    "DSD has been defined as “congenital conditions in which development of chromosomal, gonadal, or anatomic sex is atypical.”",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Gonadal Sex",
                "Ovarian hormonal secretion in fetal life has little, if any, effect on sex development.",
                True,
                "Fetal ovarian steroids minimally affect genital differentiation; ovarian effects manifest mainly at puberty.",
                ref(
                    "Gonadal Sex",
                    "In contrast, ovarian hormonal secretion in fetal life has little, if any, effect on sex development.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "21-Hydroxylase Deficiency",
                "21-hydroxylase deficiency affects only 46,XY individuals.",
                False,
                "It is a leading cause of XX DSD from fetal androgen excess; XY infants are usually not virilized.",
                ref(
                    "21-Hydroxylase Deficiency",
                    "Deficiency of 21-hydroxylase (CYP21A2) (see Fig. 21.11) is one of the most common causes of atypical genital appearance in newborns, affecting around 1 in 15,000 children, with most XX patients presenting at birth due to virilization of the genitalia (see Chapter 13).",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Conditions Affecting Androgen Action",
                "In complete AIS, müllerian structures are typically absent because AMH action is preserved.",
                True,
                "CAIS patients have functional Sertoli cells producing AMH despite androgen resistance.",
                ref(
                    "Conditions Affecting Androgen Action",
                    "The uterus is absent as a result of normal AMH action, although there may be müllerian remnants.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Ovotesticular Differences of Sex Development",
                "Spermatogenesis is expected in 46,XX ovotesticular DSD because SRY is present.",
                False,
                "Spermatogenesis requires Y-chromosomal genes beyond SRY; XX ovotesticular patients do not produce sperm.",
                ref(
                    "Ovotesticular Differences of Sex Development",
                    "Spermatogenesis requires Y-chromosomal genes other than SRY, so boys with XX ovotesticular DSD will not produce sperm.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Klinefelter Syndrome and Variants",
                "Classic Klinefelter syndrome (47,XXY) typically causes ambiguous genitalia at birth.",
                False,
                "47,XXY usually yields male genital development; diagnosis is often made in adolescence or adulthood.",
                ref(
                    "Klinefelter Syndrome and Variants",
                    "In many cases of classic sex-chromosome aneuploidy, the diagnosis is made in childhood or later during evaluation of characteristic features, impaired pubertal development, or infertility.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Conditions Affecting Testicular Development",
                "A genetic diagnosis is currently reached in most patients with XY testicular dysgenesis.",
                False,
                "Despite expanding gene panels, only about 20–40% receive a molecular diagnosis.",
                ref(
                    "Conditions Affecting Testicular Development",
                    "Although associated features can sometimes help to direct genetic analysis, often there are no other findings, and a genetic diagnosis is currently reached in only about 20% to 40% of individuals with XY testicular dysgenesis.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "The Initial Approach to the Baby With Atypical Genitalia",
                "Any child with nonpalpable gonads should be evaluated for possible life-threatening CAH.",
                True,
                "Severe XX CAH can present with virilization and impalpable gonads—adrenal crisis risk mandates urgent evaluation.",
                ref(
                    "The Initial Approach to the Baby With Atypical Genitalia",
                    "In particular, any child with nonpalpable gonads needs careful review because this child could be an XX baby with severe, potentially life-threatening CAH.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Management of Androgen Insensitivity Syndromes",
                "Gonadectomy in infancy is universally recommended for all CAIS patients.",
                False,
                "Current practice favors delaying gonadectomy to allow spontaneous puberty and shared decision-making.",
                ref(
                    "Management of Androgen Insensitivity Syndromes",
                    "Rather than performing gonadectomy at this early stage, delaying a decision about gonadectomy is favored, because this approach enables spontaneous puberty to occur, allows the patient to be involved in the decision-making process and does not substantially increase the risk for malignancy (discussed later in chapter).",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Surgery and DSD",
                "Few DSD surgeries require urgent performance in the newborn period.",
                True,
                "Most procedures can be deferred for informed MDT and family decision-making.",
                ref(
                    "Surgery and DSD",
                    "Few surgeries need to be performed urgently, and the family should be advised that there is ample time for decision making.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Tumor Risk and DSD",
                "Germ cell tumors in CAIS commonly arise before puberty.",
                False,
                "CAIS prepubertal GCT/GCNIS risk is low; higher risks emerge in adolescence/adulthood.",
                ref(
                    "Tumor Risk and DSD",
                    "The risk of GCT is lower in AIS than in gonadal dysgenesis (see “Conditions Affecting Androgen Action”), and again the germ cell tumors associated with AIS rarely arise before puberty.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Sex/Gender Designation",
                "Karyotype alone should determine gender of rearing in all DSD cases.",
                False,
                "Karyotype guides diagnosis but does not define gender identity; phenotype, endocrine function, and psychosocial factors matter.",
                ref(
                    "Sex/Gender Designation",
                    "The karyotype per se does not determine gender identity, but it is a useful starting point for focusing investigations and reaching a diagnosis (see Table 21.2 for classification of DSD).",
                ),
            ),
            tf(
                f"{p}-tf13",
                "KEY POINTS",
                "Psychosocial support is optional in DSD care.",
                False,
                "Experienced psychology/allied support and peer groups are integral across the lifespan.",
                ref(
                    "KEY POINTS",
                    "An experienced psychologist or allied professional can help support patients and families in the early years, throughout childhood and adolescence, and following transition to adult services.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Sex Determination and Sex Differentiation",
                "Assertion: SRY is the primary Y-chromosomal testis-determining gene in humans.",
                "Reason: SRY is expressed only in ovarian granulosa cells during fetal life.",
                2,
                "Assertion true; reason false—SRY is expressed in developing Sertoli cells of the testis, not ovaries.",
                ref(
                    "Chromosomal Sex",
                    "A series of elegant studies in mice and humans established Sry/SRY as the primary Y-chromosomal testis-determining gene.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Conditions Affecting Androgen Synthesis",
                "Assertion: Defects in androgen synthesis in 46,XY individuals usually leave müllerian structures absent.",
                "Reason: Sertoli cell AMH secretion remains intact in most androgen-synthesis disorders.",
                0,
                "Both true—AMH from Sertoli cells causes müllerian regression even when testosterone synthesis is impaired.",
                ref(
                    "Conditions Affecting Androgen Synthesis",
                    "In all of these conditions, because Sertoli cell secretion of AMH is intact, müllerian structures are absent.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Conditions Affecting Androgen Action",
                "Assertion: CAIS may present in infancy with bilateral inguinal/labial swellings from testes.",
                "Reason: CAIS always presents only after menarche fails in adolescence.",
                2,
                "Assertion true; reason false—infantile inguinal hernia with testes is a recognized early presentation.",
                ref(
                    "Conditions Affecting Androgen Action",
                    "CAIS may present in early infancy with bilateral inguinal or labial swellings that, on evaluation, are found to be partially descended testes.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "21-Hydroxylase Deficiency",
                "Assertion: 46,XX infants with 21-hydroxylase deficiency can have marked genital virilization at birth.",
                "Reason: Elevated fetal adrenal androgens virilize external genitalia when 21-hydroxylase is deficient.",
                0,
                "Both true—classic CAH causes fetal androgen excess and ambiguous genitalia in affected females.",
                ref(
                    "21-Hydroxylase Deficiency",
                    "An XX fetus with 21-hydroxylase deficiency can become androgenized to various degrees, as illustrated by the Prader classification (Fig. 21.33).",
                ),
            ),
            ar(
                f"{p}-ar5",
                "45,X/46,XY Mosaicism and Variants",
                "Assertion: 45,X/46,XY mosaicism carries increased gonadal tumor risk.",
                "Reason: Tumor risk is zero whenever any Y material is present.",
                2,
                "Assertion true; reason false—Y-containing dysgenetic gonads have estimated 15–40% gonadoblastoma risk.",
                ref(
                    "45,X/46,XY Mosaicism and Variants",
                    "The risk of germ cell tumors (most commonly gonadoblastoma) in individuals with 45,X/46,XY DSD is estimated to be 15% to 40%.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Ovotesticular Differences of Sex Development",
                "Assertion: A 46,XX/46,XY karyotype strongly suggests ovotesticular DSD.",
                "Reason: An XX or XY karyotype alone excludes ovotesticular DSD.",
                2,
                "Assertion true; reason false—ovotestes can occur with XX or XY karyotypes, especially with asymmetry.",
                ref(
                    "Ovotesticular Differences of Sex Development",
                    "A 46,XX/46,XY karyotype strongly suggests the diagnosis, but the detection of an XX or XY karyotype does not exclude the diagnosis, especially if there is genital asymmetry.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Management of Androgen Insensitivity Syndromes",
                "Assertion: Serum AMH is usually in or above the male range in CAIS.",
                "Reason: AMH is low in CAIS because Sertoli cells are absent.",
                2,
                "Assertion true; reason false—CAIS has functional testes/Sertoli cells; low AMH suggests gonadal dysgenesis instead.",
                ref(
                    "Hormone Profiles in Androgen Insensitivity Syndromes",
                    "Serum AMH concentration is usually in or above the typical male range in CAIS, a finding that further distinguishes CAIS from gonadal dysgenesis, in which AMH levels are low.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Steroidogenic Factor 1: NR5A1",
                "Assertion: Heterozygous NR5A1 mutations can cause XY DSD with normal adrenal function.",
                "Reason: All NR5A1 mutations inevitably cause primary adrenal insufficiency at birth.",
                2,
                "Assertion true; reason false—many heterozygous NR5A1 variants cause isolated gonadal phenotypes.",
                ref(
                    "Steroidogenic Factor 1: NR5A1",
                    "However, the past decade has seen a different picture emerging as an ever-increasing number of monoallelic (heterozygous) nonsense, frameshift, and missense mutations in NR5A1 have been associated with a spectrum of XY DSD conditions in individuals with normal adrenal function (see Fig. 21.21).",
                ),
            ),
            ar(
                f"{p}-ar9",
                "The Initial Approach to the Baby With Atypical Genitalia",
                "Assertion: Rapid karyotype or FISH aids early DSD management.",
                "Reason: Cytogenetics is unnecessary if genital appearance is mildly atypical.",
                2,
                "Assertion true; reason false—sex-chromosome complement is essential in all significant DSD evaluations.",
                ref(
                    "The Initial Approach to the Baby With Atypical Genitalia",
                    "Cytogenetics or some other rapid assessment of sex-chromosome complement is essential.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Surgery and DSD",
                "Assertion: Early feminizing genital surgery in CAH may impair genital sensation and sexual function.",
                "Reason: Outcome studies show no differences between operated and unoperated women with CAH.",
                2,
                "Assertion true; reason false—studies demonstrate impaired sensitivity/function though comparisons are limited.",
                ref(
                    "Surgery and DSD",
                    "Outcome studies in women with CAH who had undergone feminizing genital surgery have demonstrated impaired genital sensitivity and sexual function, but comparisons to women who had not undergone surgery are difficult because the practice of feminizing genitoplasty has been so widespread.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Presentation During Adolescence",
                "Assertion: 17β-HSD deficiency can present with virilization at puberty in individuals raised female.",
                "Reason: 17β-HSD deficiency blocks all androgen production permanently with no pubertal change.",
                2,
                "Assertion true; reason false—pubertal testosterone rise can virilize when the enzymatic block is partial.",
                ref(
                    "Presentation During Adolescence",
                    "The conditions that are typically associated with virilization at puberty are 5α-reductase deficiency and 17β-hydroxysteroid dehydrogenase deficiency.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "KEY POINTS",
                "Assertion: Adult endocrinologists have an important role in lifelong DSD care.",
                "Reason: DSD are resolved after childhood and require no adult follow-up.",
                2,
                "Assertion true; reason false—DSD need transition to adult services for hormones, bone health, fertility, and psychosocial support.",
                ref(
                    "KEY POINTS",
                    "Adult endocrinologists therefore have a crucial role to play in managing young people who present in adulthood as well as in providing long-term follow-up of individuals with DSD diagnosed in childhood.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "21",
        "title": "Differences of Sex Development",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Yee-Ming Chan and Sabine E. Hannema",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_21_Differences_of_Sex_Development.md",
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
