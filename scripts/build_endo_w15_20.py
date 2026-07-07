#!/usr/bin/env python3
"""Generate Williams 15e module w15-20 — Endocrinology of Fetal Development."""
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
OUT_NAME = "w15-20_Endocrinology_of_Fetal_Development.json"


def build() -> dict:
    p = "w15-20"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why the fetal endocrine milieu is unique",
                "The placental-fetal endocrine environment combines placental hormones, fetal adaptations, and neutralization of maternal hormones—disordered thyroid, pituitary, pancreas, or gonadal development can produce recognizable neonatal phenotypes.",
                ref(
                    "KEY POINTS",
                    "The placental-fetal endocrine environment is created by a spectrum of placental hormones and growth factors and a variety of fetal endocrine adaptations to the intrauterine environment.",
                ),
            ),
            note(
                f"{p}-n2",
                "Human Hypothalamo-Pituitary Development",
                "How to time functional fetal HPT axis maturity",
                "Hypothalamic neuropeptide neurons appear by 10–14 weeks, portal vasculature matures through 30–35 weeks, and all pituitary hormones are detectable by 10–17 weeks—anatomy and biosynthesis appear functional by 12–17 weeks gestation.",
                ref(
                    "Human Hypothalamo-Pituitary Development",
                    "Thus, the anatomy and biosynthetic mechanisms that make up the hypothalamo-pituitary neuroendocrine transducer appear functional by 12 to 17 weeks of gestation.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why fetal adrenal steroids are mostly inactive precursors",
                "Fetal ACTH drives adrenal steroidogenesis, yet the fetal zone produces pregnenolone and DHEA rather than mature cortisol/aldosterone for much of gestation—substrates for placental estrogen synthesis.",
                ref(
                    "KEY POINTS",
                    "Fetal adrenocorticotropic hormone (ACTH) is required for adrenal cortex steroidogenesis. Paradoxically, adrenal steroidogenesis leads to production of mostly inactive steroids such as pregnenolone and dehydroepiandrosterone (DHEA).",
                ),
            ),
            note(
                f"{p}-n4",
                "Placental Transfer of Hormones",
                "How placental 11βHSD2 protects the fetus from maternal cortisol",
                "Maternal cortisol is ~10-fold higher than fetal levels; placental 11βHSD2 converts cortisol to inactive cortisone. Synthetic glucocorticoids bypass this barrier—acute antenatal betamethasone aids lung maturation, but chronic exposure risks growth and metabolic programming.",
                ref(
                    "Placental Transfer of Hormones",
                    "Placental cells contain an active  $ 11\\beta $-hydroxysteroid dehydrogenase type 2 ( $ 11\\beta HSD2 $) that catalyzes conversion of maternal cortisol to inactive cortisone.",
                ),
            ),
            note(
                f"{p}-n5",
                "KEY POINTS",
                "Why SRY timing matters for male sexual differentiation",
                "With SRY present, male gonadal differentiation begins at 7 weeks; Leydig-cell testosterone from ~10 weeks drives wolffian structures, while DHT masculinizes the urogenital sinus and external genitalia.",
                ref(
                    "KEY POINTS",
                    "In the presence of SRY, the sex-determining region of the Y chromosome, male gonadal differentiation starts at 7 weeks of gestation.",
                ),
            ),
            note(
                f"{p}-n6",
                "Fetal Adrenal Steroidogenesis",
                "How 21-hydroxylase deficiency virilizes 46,XX fetuses",
                "A midgestation cortisol peak (8–9 wpc) depends on transient HSD3B2; absent cortisol in CYP21/CYP11 defects elevates ACTH and androgen drive when external genitalia are androgen-sensitive—virilizing ambiguous genitalia in affected females.",
                ref(
                    "Fetal Adrenal Steroidogenesis",
                    "46,XX fetuses with steroidogenic defects (e.g., in CYP21 or CYP11) lack cortisol and have an elevated ACTH drive that results in excess production of fetal androgens at a time when the genital and scrotal folds are sensitive to androgen exposure, resulting in virilization of female genitalia.",
                ),
            ),
            note(
                f"{p}-n7",
                "Placental Transfer of Hormones",
                "Why maternal thyroid hormone matters before fetal synthesis",
                "During the first trimester, transplacental T₄ supports neurodevelopment while placental deiodinases inactivate most maternal thyroid hormone—mild untreated maternal hypothyroidism associates with impaired offspring cognition.",
                ref(
                    "Placental Transfer of Hormones",
                    "During the first trimester, transplacental passage of thyroid hormones from the maternal circulation to the fetus is important for neurodevelopment.",
                ),
            ),
            note(
                f"{p}-n8",
                "Congenital Hypothyroidism",
                "How newborn screening changes congenital hypothyroidism outcomes",
                "CH affects ~1:3000–4000 births; classic signs emerge after maternal T₄ wanes. Most countries screen rigorously so levothyroxine starts before irreversible neurologic injury—international treatment guidelines exist.",
                ref(
                    "Congenital Hypothyroidism",
                    "Most countries have a rigorous screening program to ensure early diagnosis and treatment, and international guidelines for treatment of CH are available.",
                ),
            ),
            note(
                f"{p}-n9",
                "Limitation of Hormone Secretion",
                "Why fetal insulin secretion stays blunted despite hyperglycemia",
                "The fetal pancreas is functional in the second trimester, but glucose-stimulated insulin release is minimal until after birth—chronic maternal hyperglycemia can still provoke islet hyperplasia and fetal hyperinsulinemia.",
                ref(
                    "Limitation of Hormone Secretion",
                    "The human fetal pancreas is functional during the second trimester, but secretion of insulin in response to glucose or pyruvate is minimal until the neonatal period.",
                ),
            ),
            note(
                f"{p}-n10",
                "Glucose Homeostasis",
                "How to manage neonatal hypoglycemia after diabetic pregnancy",
                "Cord clamping ends continuous placental glucose; counter-regulatory hormones surge but infants of diabetic mothers have relative hyperinsulinism and more severe, prolonged hypoglycemia—early feeding and glucose monitoring are essential.",
                ref(
                    "Glucose Homeostasis",
                    "Infants born to diabetic mothers have more severe neonatal hypoglycemia because of relative hyperinsulinism.",
                ),
            ),
            note(
                f"{p}-n11",
                "Programming of Fetal Endocrine Systems",
                "Why IUGR predicts adult cardiometabolic disease",
                "The Barker hypothesis links low birth weight to later hypertension, insulin resistance, diabetes, and cardiovascular disease—programming involves epigenetic, neuroendocrine, and placental adaptations.",
                ref(
                    "Programming of Fetal Endocrine Systems",
                    "There is now extensive documentation of the association of IUGR with an increased risk of later hypertension, insulin resistance, diabetes, and cardiovascular and coronary heart disease.",
                ),
            ),
            note(
                f"{p}-n12",
                "Programming of Fetal Endocrine Systems",
                "How imprinted genes control fetal growth",
                "Paternally expressed imprinted genes (IGF2, insulin) enhance growth; maternally expressed genes (H19, IGF2R) restrain it—loss of methylation at H19/IGF2 causes Silver-Russell syndrome, whereas gain contributes to Beckwith-Wiedemann overgrowth.",
                ref(
                    "Programming of Fetal Endocrine Systems",
                    "Paternally expressed imprinted genes tend to enhance and maternally expressed genes tend to suppress fetal growth.",
                ),
            ),
            note(
                f"{p}-n13",
                "Fetal Adrenal Steroidogenesis",
                "Why prenatal dexamethasone for CAH remains experimental",
                "Maternal dexamethasone at 8–12 wpc can reduce fetal androgen virilization but crosses the placenta unimpeded, achieving ~60-fold supraphysiologic fetal exposure with neurologic and metabolic concerns—treatment should occur only in audited research settings.",
                ref(
                    "Fetal Adrenal Steroidogenesis",
                    "due to paucity of high-quality evidence in terms of efficacy and safety, this should be regarded as a highly controversial experimental treatment.",
                ),
            ),
            note(
                f"{p}-n14",
                "Glucose Homeostasis",
                "How the neonate adapts glucose after placental separation",
                "Blood glucose falls in the first 2–4 hours after delivery; glucagon, catecholamines, GH, and cortisol rise while insulin falls—hepatic gluconeogenesis matures over 12–72 hours to stabilize glucose near adult levels.",
                ref(
                    "Glucose Homeostasis",
                    "Counterregulatory hormones rapidly become active, with high catecholamine, glucagon, GH, and glucocorticoid concentrations and a fall in insulin.",
                ),
            ),
            note(
                f"{p}-n15",
                "Congenital Hyperinsulinism",
                "How to diagnose congenital hyperinsulinism at hypoglycemia",
                "During hypoglycemia, CHI shows glucose infusion rate >8 mg/kg/min with detectable insulin/C-peptide, low ketones, and low free fatty acids—first-line therapy is diazoxide with chlorothiazide; focal lesions may be cured surgically after ¹⁸F-DOPA PET.",
                ref(
                    "Congenital Hyperinsulinism",
                    "Diagnostic criteria are a glucose infusion rate more than 8 mg/kg/min, a laboratory blood glucose less than 3 mmol/L with detectable serum insulin or C-peptide, low serum ketone bodies, and low serum fatty acids.",
                ),
            ),
            note(
                f"{p}-n16",
                "Adrenal",
                "Fetal zone of the human adrenal",
                "The transient fetal zone accounts for 80–90% of adrenal mass by midgestation, expresses CYP17α, and produces DHEA/DHEAS for placental aromatization—it involutes rapidly after birth with a 50% adrenal weight loss within 2 weeks.",
                ref(
                    "Embryology",
                    "The fetal adrenal undergoes tremendous growth as pregnancy progresses, largely due to an increase in size of the FZ, which accounts for 80% to 90% of the mass of the gland by midgestation.",
                ),
            ),
            note(
                f"{p}-n17",
                "Intermediate Lobe of the Pituitary",
                "Fetal intermediate pituitary lobe",
                "The prominent fetal intermediate lobe secretes α-MSH and β-endorphin from POMC; α-MSH levels fall with gestational age and may participate in fetal adrenal activation and growth.",
                ref(
                    "Intermediate Lobe of the Pituitary",
                    "The intermediate lobe of the pituitary gland is prominent in both the human and the sheep fetus.",
                ),
            ),
            note(
                f"{p}-n18",
                "Transcriptional Regulation of Adrenal Development",
                "DAX1 and X-linked adrenal hypoplasia",
                "DAX1 (NR0B1) is a negative regulator of SF1; inactivating mutations cause X-linked adrenal hypoplasia congenita with early salt-losing adrenal failure and hypogonadotropic hypogonadism in males.",
                ref(
                    "Transcriptional Regulation of Adrenal Development",
                    "Pathogenic variants or deletions of  $ DAX1 $ in humans are well established as the cause of X-linked AHC.",
                ),
            ),
            note(
                f"{p}-n19",
                "Genes Involved in Pituitary Disease",
                "HESX1 and septo-optic dysplasia",
                "HESX1 mutations cause septo-optic dysplasia and combined pituitary hormone deficiency with variable anterior pituitary hypoplasia and ectopic or eutopic posterior pituitary—illustrating how early transcription factors pattern the HPT axis.",
                ref(
                    "Genes Involved in Pituitary Disease",
                    "Mutations in  $ HESX1 $ have been identified in patients with SOD (a combination of pituitary, eye, and midline forebrain defects), combined pituitary hormone deficiencies ( $ CPHDs $), and isolated growth hormone deficiency (IGHD).",
                ),
            ),
            note(
                f"{p}-n20",
                "Fetal Sex Steroid Production",
                "AMH and müllerian regression",
                "Sertoli-cell AMH peaks during müllerian duct regression (6–12 wpc); AMH gene mutations cause persistent müllerian duct syndrome in XY infants despite normal testosterone.",
                ref(
                    "Fetal Sex Steroid Production",
                    "Mutation of the AMH gene results in a persistent müllerian duct syndrome in the XY fetus.",
                ),
            ),
            note(
                f"{p}-n21",
                "Production of Inactive Hormone Metabolites",
                "Fetal thyroid hormone inactivation",
                "Placental and fetal D3 convert T₄ to rT₃; sulfated iodothyronines accumulate, keeping circulating T₃ low until late gestation while D2 supplies local T₃ to brain and brown fat.",
                ref(
                    "Production of Inactive Hormone Metabolites",
                    "Fetal thyroid hormone metabolism is characterized by conversion of active thyroid hormones to inactive rT₃ and inactive sulfated iodothyronines and by limited receptor and postreceptor responsiveness to thyroid hormone in selected tissues.",
                ),
            ),
            note(
                f"{p}-n22",
                "Cortisol Surge",
                "Prenatal cortisol surge near term",
                "Late-gestation cortisol rises as 11βHSD2 activity falls, promoting lung surfactant, hepatic T₄→T₃ conversion, intestinal enzyme maturation, and ductus arteriosus closure—basis for antenatal corticosteroids in threatened preterm delivery.",
                ref(
                    "Cortisol Surge",
                    "Augments surfactant synthesis in lung tissue",
                ),
            ),
            note(
                f"{p}-n23",
                "Thyroid Function in Preterm Infants",
                "Transient hypothyroxinemia of prematurity",
                "Low free T₄ with normal TSH affects ~50% of infants <28 weeks and reflects HPT immaturity—it does not require levothyroxine treatment; distinguish from primary hypothyroidism needing therapy until ~3 years.",
                ref(
                    "Thyroid Function in Preterm Infants",
                    "Transient hypothyroxinemia of prematurity—identified by a low free  $ T_{4} $ and normal TSH and seen in 50% of preterm infants born less than 28 weeks—does not require treatment.",
                ),
            ),
            note(
                f"{p}-n24",
                "Insulin-Like Growth Factors",
                "Beckwith-Wiedemann and IGF2 overgrowth",
                "Loss of imprinting with biallelic IGF2 expression or CDKN1C loss-of-function causes Beckwith-Wiedemann overgrowth, macrosomia, and increased embryonal tumor risk—contrast with IMAGe from CDKN1C gain-of-function.",
                ref(
                    "Insulin-Like Growth Factors",
                    "overexpression of IGF2 as a result of loss of imprinting associated with uniparental disomy, CDKN1C gene loss of function, alteration in the KvLQT1 differentially methylated region (DMR), or microdeletions in the human H19 DMR are associated with overgrowth in the form of Beckwith-Wiedemann syndrome.",
                ),
            ),
            note(
                f"{p}-n25",
                "Catecholamine Surge",
                "Neonatal catecholamine surge at birth",
                "Spontaneous term delivery produces cord NE ~15 nmol/L and epinephrine ~2 nmol/L—driving blood pressure, glucagon release, thermogenesis, and pulmonary fluid mobilization critical for extrauterine adaptation.",
                ref(
                    "Catecholamine Surge",
                    "Cord blood NE concentrations of 15 nmol/L (2500 pg/mL) and epinephrine concentrations of 2 nmol/L (370 pg/mL) are common after spontaneous delivery of term infants.",
                ),
            ),
            note(
                f"{p}-n26",
                "Maternal and Fetal Medicine",
                "Fetal endocrine diagnostics and therapy",
                "Maternal plasma cell-free fetal DNA, fetal blood sampling, and intrauterine thyroid/adrenal diagnosis are now standard; in utero therapy (e.g., intra-amniotic levothyroxine for fetal goiter) remains high-risk and often controversial.",
                ref(
                    "Maternal and Fetal Medicine",
                    "Intrauterine diagnosis of fetal adrenal and thyroid disorders has become the standard of care, followed by the prospect of in utero treatment, although this is often controversial.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Fetal Adrenal Steroidogenesis",
                "A 20-week ultrasound shows clitoromegaly in a fetus with normal female karyotype. Maternal dexamethasone was started at 9 weeks after prior CAH-affected child. Best interpretation of antenatal steroid use?",
                [
                    "Experimental therapy with limited safety evidence—requires research oversight",
                    "Standard of care with proven long-term neurologic benefit",
                    "Contraindicated because dexamethasone cannot cross the placenta",
                    "Use only after 30 weeks when fetal zone involutes",
                ],
                0,
                "Prenatal dexamethasone to reduce CAH virilization lacks robust efficacy/safety data and exposes the fetus to very high glucocorticoid levels.",
                ref(
                    "Fetal Adrenal Steroidogenesis",
                    "Clinical use of single or multiple courses of glucocorticoid treatment in the obstetric management of threatened preterm delivery continues but treatment for other proposed indications lacking robust evidence—for example, use in pregnancy to reduce virilization of a fetus with congenital adrenal hyperplasia—should take place only in a research setting with careful auditing.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Congenital Hypothyroidism",
                "A term newborn passes CH newborn screen with elevated TSH; examination is normal. Next step?",
                [
                    "Confirm diagnosis and start levothyroxine promptly—do not wait for clinical signs",
                    "Repeat screen at 6 months because signs are absent",
                    "Withhold treatment until macroglossia appears",
                    "Start propylthiouracil for suppressed TSH",
                ],
                0,
                "Classic CH signs appear weeks after birth once maternal T₄ is gone; screening enables treatment before neurologic injury.",
                ref(
                    "Congenital Hypothyroidism",
                    "Classic signs of CH (jaundice, lethargy, feeding difficulties, macroglossia, myxedema, hypothermia, growth retardation and progressive developmental delay, and intelligence quotient [IQ] deterioration) appear during the initial critical weeks and months of extrauterine life as maternal  $ T_{4} $ becomes unavailable",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Congenital Hyperinsulinism",
                "A 2-day-old infant of a poorly controlled diabetic mother has glucose 1.8 mmol/L with detectable insulin and no ketones. Most likely mechanism?",
                [
                    "Fetal β-cell hyperplasia with persistent hyperinsulinism",
                    "Growth hormone deficiency",
                    "Primary adrenal insufficiency",
                    "Congenital hypothyroidism",
                ],
                0,
                "Maternal hyperglycemia drives fetal hyperinsulinemia and β-cell hyperplasia, causing severe neonatal hypoglycemia after placental glucose supply ends.",
                ref(
                    "Congenital Hyperinsulinism",
                    "Maternal hyperglycemia also leads to hyperinsulinism and  $ \\beta $-cell hyperplasia in the infant.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Gonadal Development",
                "A 46,XY newborn has palpable testes, normal male external genitalia, and a uterus on pelvic ultrasound. Most likely diagnosis?",
                [
                    "Persistent müllerian duct syndrome (AMH pathway defect)",
                    "Complete androgen insensitivity syndrome",
                    "5α-reductase deficiency",
                    "Congenital adrenal hyperplasia with salt wasting",
                ],
                0,
                "AMH failure allows müllerian structures to persist despite normal testicular testosterone production.",
                ref(
                    "Fetal Sex Steroid Production",
                    "Mutation of the AMH gene results in a persistent müllerian duct syndrome in the XY fetus.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Human Hypothalamo-Pituitary Development",
                "An infant has optic nerve hypoplasia, midline defects, and low GH, ACTH, and TSH. Gene testing should prioritize:",
                [
                    "HESX1",
                    "CYP21A2",
                    "KCNJ11",
                    "TPO",
                ],
                0,
                "HESX1 mutations cause septo-optic dysplasia with combined pituitary hormone deficiency.",
                ref(
                    "Genes Involved in Pituitary Disease",
                    "Mutations in  $ HESX1 $ have been identified in patients with SOD (a combination of pituitary, eye, and midline forebrain defects), combined pituitary hormone deficiencies ( $ CPHDs $), and isolated growth hormone deficiency (IGHD).",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Thyroid Embryology",
                "A newborn has a lingual thyroid mass and no palpable cervical thyroid. Embryologic explanation?",
                [
                    "Failed caudal migration of the median thyroid anlage",
                    "Excess maternal TSH blocking descent",
                    "Autoimmune destruction of a normally located gland only",
                    "Iodine excess preventing bud formation",
                ],
                0,
                "Thyroid precursor cells migrate caudally from the pharyngeal floor; abnormal descent causes ectopic thyroid and thyroglossal remnants.",
                ref(
                    "Thyroid Embryology",
                    "An ectopic thyroid and a persistent thyroglossal duct or cyst may occur because of abnormal thyroid descent.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Fetal Growth",
                "A fetus with severe IUGR has low umbilical cord IGF1. Maternal smoking history is present. Best mechanistic link?",
                [
                    "Reduced substrate and IGF1 signaling impairing fetal growth",
                    "Excess fetal GH receptor activation",
                    "Maternal hyperthyroidism alone",
                    "Fetal hyperinsulinemic macrosomia",
                ],
                0,
                "IGFs are regulated by transplacental nutrition; umbilical IGF1 correlates with birth weight and is reduced by maternal smoking.",
                ref(
                    "KEY POINTS",
                    "Insulin-like growth factors (IGFs) are important for fetal growth and are regulated mainly by transplacentally derived nutritional substrate.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Placental Transfer of Hormones",
                "A woman with autoimmune thyroiditis and normal TSH receives no levothyroxine in early pregnancy. Fetal risk in first trimester?",
                [
                    "Impaired neurodevelopment from inadequate transplacental T₄",
                    "No risk because the placenta blocks all maternal thyroid hormone",
                    "Fetal thyrotoxicosis from TSH receptor antibodies only",
                    "Immediate fetal thyroid autonomy from week 5",
                ],
                0,
                "Early pregnancy depends on maternal T₄ crossing the placenta for fetal brain development before fetal thyroid function matures.",
                ref(
                    "Placental Transfer of Hormones",
                    "During the first trimester, transplacental passage of thyroid hormones from the maternal circulation to the fetus is important for neurodevelopment.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Adrenal Insufficiency",
                "A male neonate presents with salt wasting, hyperpigmentation, and low cortisol with very high ACTH. DAX1 sequencing is negative. Next gene to consider for primary adrenal failure?",
                [
                    "NR5A1 (SF1)",
                    "KAL1",
                    "INSR",
                    "MCT8",
                ],
                0,
                "SF1 (NR5A1) mutations can cause primary adrenal failure and 46,XY DSD; DAX1 causes X-linked AHC without hyperpigmentation pattern of ACTH excess in some forms.",
                ref(
                    "Adrenal Insufficiency",
                    "Heterozygous and homozygous mutations in SF1 have been associated with adrenal failure in 46,XY phenotypic females, as well as in at least one 46,XX girl, although the latter phenotype is rare.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Neonatal Diabetes",
                "Permanent neonatal diabetes at 8 weeks fails insulin therapy but responds to glibenclamide. Most likely genotype?",
                [
                    "Activating KCNJ11 or ABCC8 mutation",
                    "HNF1A MODY",
                    "Autoimmune T1D with positive GAD antibodies",
                    "Complete pancreatic agenesis (PDX1 null)",
                ],
                0,
                "K-ATP channel activating mutations impair insulin secretion but often respond to sulfonylureas that close the channel.",
                ref(
                    "Neonatal Diabetes",
                    "Permanent neonatal diabetes mellitus (PNDM) is most often due to activating mutations in KCNJ11 or ABCC8, resulting in overactivation of potassium channels and thus impaired insulin secretion. These patients are responsive to sulfonylurea therapy and do not require insulin treatment.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Thyroid Function in Preterm Infants",
                "A 26-week preterm infant has low free T₄ and normal TSH on day 3. Management?",
                [
                    "Observe—likely transient hypothyroxinemia of prematurity",
                    "Emergency thyroidectomy",
                    "High-dose propylthiouracil",
                    "Lifelong levothyroxine without reassessment",
                ],
                0,
                "Low free T₄ with normal TSH in extreme prematurity is common and does not require treatment.",
                ref(
                    "Thyroid Function in Preterm Infants",
                    "Transient hypothyroxinemia of prematurity—identified by a low free  $ T_{4} $ and normal TSH and seen in 50% of preterm infants born less than 28 weeks—does not require treatment.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Fetal Sex Steroid Production",
                "At 11 weeks, a male fetus needs masculinization of external genitalia. Which hormone is most critical?",
                [
                    "Dihydrotestosterone from 5α-reductase",
                    "AMH",
                    "Estradiol from placenta",
                    "Maternal progesterone",
                ],
                0,
                "Testosterone differentiates wolffian ducts; DHT mediates urogenital sinus and external genital masculinization.",
                ref(
                    "Fetal Sex Steroid Production",
                    "DHT stimulates male differentiation of the urogenital sinus and external genitalia, including differentiation of the prostate, growth of the genital tubercle to form a phallus, and fusion of the urogenital folds to form the penile urethra.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Programming of Fetal Endocrine Systems",
                "An adult with hypertension and insulin resistance was born SGA. Best unifying fetal mechanism?",
                [
                    "Epigenetic/metabolic programming after IUGR",
                    "Isolated adult-onset GH excess",
                    "Congenital thyrotoxicosis",
                    "Neonatal hyperparathyroidism",
                ],
                0,
                "IUGR is linked to later cardiometabolic disease through developmental programming of endocrine and metabolic systems.",
                ref(
                    "Programming of Fetal Endocrine Systems",
                    "There is now extensive documentation of the association of IUGR with an increased risk of later hypertension, insulin resistance, diabetes, and cardiovascular and coronary heart disease.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Congenital Hyperinsulinism",
                "A hypoglycemic neonate requires glucose infusion 10 mg/kg/min with detectable insulin and low β-hydroxybutyrate. First-line medical therapy?",
                [
                    "Diazoxide with chlorothiazide",
                    "Immediate near-total pancreatectomy",
                    "High-dose levothyroxine",
                    "Growth hormone replacement",
                ],
                0,
                "CHI first-line treatment is diazoxide and chlorothiazide; surgery follows imaging if diazoxide-unresponsive.",
                ref(
                    "Congenital Hyperinsulinism",
                    "First-line treatment is diazoxide and chlorothiazide, and second-line treatments include octreotide, glucagon, and nifedipine.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Fetal Adrenal Steroidogenesis",
                "Why does the human fetal adrenal produce little cortisol until late gestation?",
                [
                    "Relative lack of HSD3B2 in fetal zone directing steroidogenesis to DHEA",
                    "Absence of ACTH receptors until birth",
                    "Placental destruction of all fetal ACTH",
                    "Complete absence of CYP11A1",
                ],
                0,
                "During most of gestation the fetal adrenal lacks HSD3B2, preventing cortisol/aldosterone synthesis and favoring DHEA production.",
                ref(
                    "Fetal Adrenal Steroidogenesis",
                    "During most of gestation, the fetal adrenal lacks type 2 3β-hydroxysteroid dehydrogenase (HSD3B2), preventing cortisol and aldosterone synthesis and directing steroid production toward DHEA production.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Ontogeny of Thyroid Hormone Secretion",
                "A fetus at 16 weeks has low serum T₃ but brain T₃ 60–80% of adult levels. Explanation?",
                [
                    "Local D2 converts T₄ to T₃ in brain despite low circulating T₃",
                    "Maternal T₃ is the sole source after 12 weeks",
                    "Placental D3 is absent until term",
                    "Fetal thyroid produces excess T₃ from week 8",
                ],
                0,
                "D2 activity in fetal brain maintains local T₃ even when circulating T₃ is low until late gestation.",
                ref(
                    "Fetal Thyroid Hormone Biosynthesis",
                    "On the other hand, fetal brain  $ T_{3} $ concentrations are 60% to 80% of those in the adult by fetal age 20 to 26 weeks owing to D2 activity.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Insulin",
                "A fetus with pancreatic agenesis on ultrasound is predicted to be born with:",
                [
                    "IUGR with low muscle mass and little adipose tissue",
                    "Macrosomia with organomegaly",
                    "Normal birth weight with isolated hyperglycemia",
                    "Isolated hypercalcemia",
                ],
                0,
                "Pancreatic agenesis causes a small fetus with decreased muscle and absent fat despite insulin's role as a fetal growth factor.",
                ref(
                    "Insulin",
                    "Conversely, the human fetus with pancreatic agenesis is small and has decreased muscle bulk and little or no adipose tissue.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Gonadal Development",
                "A 46,XX infant has testicular tissue and ambiguous genitalia. SOX9 duplication is found. Mechanism?",
                [
                    "Ectopic SOX9 expression drives testicular differentiation without SRY",
                    "AMH deficiency",
                    "Androgen receptor loss",
                    "Maternal virilizing tumor only",
                ],
                0,
                "SOX3/SOX9 regulatory rearrangements can cause 46,XX testicular differentiation when SOX9 reaches threshold without SRY.",
                ref(
                    "Embryology",
                    "SOX3 duplication or rearrangements of the SOX3 regulatory region have been found in 46,XX individuals with dysgenetic testes.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Maternal and Fetal Medicine",
                "Fetal goiter and suspected hypothyroidism are found at 24 weeks. Counseling about intra-amniotic levothyroxine should emphasize:",
                [
                    "Procedure risks including miscarriage—evidence limited",
                    "It is mandatory and risk-free standard care",
                    "No prenatal diagnosis is possible",
                    "Treatment always prevents all neurologic injury without risk",
                ],
                0,
                "Intrauterine thyroid therapy carries significant procedural risks and lacks large trials for optimal management.",
                ref(
                    "Maternal and Fetal Medicine",
                    "Management of hypothyroid fetal goiter, for example, poses significant risks (including miscarriage) associated with both diagnostic amniocentesis/cordocentesis and intra-amniotic thyroid hormone therapy.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Ectopic Fetal Hormone Production",
                "Fetal testicular Leydig cells at 12–20 weeks are stimulated primarily by:",
                [
                    "hCG",
                    "Maternal FSH",
                    "Placental prolactin",
                    "Fetal TSH",
                ],
                0,
                "hCG is the predominant gonadotropin stimulating fetal Leydig testosterone before the fetal pituitary-gonadal axis matures.",
                ref(
                    "Ectopic Fetal Hormone Production",
                    "hCG is also found in fetal ovary, kidney, lung, adrenal, thymus, spleen, and muscle, and hCG/LH receptors have been demonstrated in fetal kidney, liver, pancreas, lung, small and large intestines, and adrenals.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Adrenal Insufficiency",
                "A newborn with TBX19 mutation presents with:",
                [
                    "Severe isolated ACTH deficiency and hypoglycemia",
                    "Primary adrenal Cushing syndrome",
                    "Hyperthyroidism from TSH excess",
                    "Isolated mineralocorticoid excess",
                ],
                0,
                "TBX19/TPIT mutations cause early-onset isolated ACTH deficiency with profound neonatal hypoglycemia.",
                ref(
                    "Adrenal Insufficiency",
                    "Recessive mutations in the T-box factor TPIT (TBX19) have been identified in patients with severe, early-onset isolated ACTH deficiency with profound hypoglycemia, prolonged jaundice, and sudden neonatal death.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Glucose Homeostasis",
                "A healthy term newborn has glucose 2.6 mmol/L at 3 hours without symptoms. Best management?",
                [
                    "Encourage feeding and observe—often physiologic transitional hypoglycemia",
                    "Immediate subtotal pancreatectomy",
                    "Start chronic hydrocortisone replacement",
                    "Withhold feeds until glucose >10 mmol/L",
                ],
                0,
                "Early postnatal glucose nadirs are common and usually asymptomatic during adaptation to extrauterine life.",
                ref(
                    "Glucose Homeostasis",
                    "Low concentrations are usually transient, asymptomatic, and part of the normal adaptation to extrauterine life.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Insulin-Like Growth Factors",
                "A child with Silver-Russell syndrome and growth restriction is found to have:",
                [
                    "Loss of methylation at the H19/IGF2 domain",
                    "Biallelic IGF2 overexpression",
                    "Activating FGFR3 mutation",
                    "TSH receptor activating mutation",
                ],
                0,
                "Loss of methylation at H19/IGF2 is identified in over half of Russell-Silver patients.",
                ref(
                    "Programming of Fetal Endocrine Systems",
                    "A loss of DNA methylation (LOM) at the H19/IGF2 domain has been identified in over 50% of patients with Russell-Silver syndrome.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Posterior Pituitary",
                "Cord blood AVP is elevated with fetal bradycardia. Clinical significance?",
                [
                    "Fetal stress response—AVP rises more with hypoxia than osmolar stimuli",
                    "Primary diabetes insipidus",
                    "Maternal SIADH only",
                    "Normal finding unrelated to stress",
                ],
                0,
                "Fetal AVP responds vigorously to hypoxia and supports circulatory homeostasis during stress.",
                ref(
                    "Posterior Pituitary",
                    "Plasma AVP concentrations in human cord blood are elevated in association with intrauterine bradycardia and meconium passage.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Congenital Hypothyroidism",
                "A screened newborn has elevated TSH; thyroid ultrasound shows athyreosis. Most likely category?",
                [
                    "Thyroid dysgenesis (~85% of permanent primary CH)",
                    "TSH resistance from TSHR mutation only",
                    "Central hypothyroidism from TRHR defect",
                    "Transient maternal antibody block only",
                ],
                0,
                "Most permanent primary CH results from thyroid dysgenesis.",
                ref(
                    "Congenital Hypothyroidism",
                    "Most cases of permanent primary CH are due to thyroid dysgenesis (85%).",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Fetal Adrenal Steroidogenesis",
                "Long-term follow-up of antenatal betamethasone for threatened preterm birth shows:",
                [
                    "Increased insulin resistance decades later, especially in women",
                    "No metabolic sequelae",
                    "Permanent adrenal suppression requiring lifelong steroids in all",
                    "Guaranteed prevention of all neurologic injury",
                ],
                0,
                "Antenatal synthetic glucocorticoids may program adult insulin resistance years after exposure.",
                ref(
                    "Fetal Adrenal Steroidogenesis",
                    "Longitudinal follow-up of the offspring of women treated with betamethasone for threatened preterm birth has shown that individuals exhibit insulin resistance 30 years after treatment, particularly women.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Human Hypothalamo-Pituitary Development",
                "All anterior pituitary hormone cell types are present between 7 and 16 weeks of gestation.",
                True,
                "Corticotropes, somatotropes, lactotropes, thyrotropes, and gonadotropes differentiate during this window.",
                ref(
                    "Human Hypothalamo-Pituitary Development",
                    "Specialized anterior pituitary cell types, lactotropes, somatotropes, corticotropes, thyrotropes, and gonadotropes are present between 7 and 16 weeks.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Placental Transfer of Hormones",
                "Maternal hormones larger than ~1 kDa generally have little access to the fetal compartment.",
                True,
                "Placental transfer decreases with molecular weight; hormones >0.7–1.2 kDa cross poorly.",
                ref(
                    "Placental Transfer of Hormones",
                    "Placental transfer of hormones decreases with increasing molecular weight, and those larger than 0.7 to 1.2 kDa have little or no access to the fetal compartment.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Fetal Adrenal Steroidogenesis",
                "The fetal adrenal fetal zone involutes rapidly after birth.",
                True,
                "FZ involution begins immediately after birth with ~50% adrenal weight loss within 2 weeks.",
                ref(
                    "Embryology",
                    "Immediately after birth the FZ rapidly involutes and remodels by a process involving apoptosis of cells in its inner region,",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Fetal Sex Steroid Production",
                "Fetal pituitary gonadotropins are required for normal gonadal differentiation and external genital development.",
                False,
                "LH/FSH receptor knockouts are phenotypically normal at birth—hCG and testis hormones drive differentiation.",
                ref(
                    "Fetal Sex Steroid Production",
                    "Fetal pituitary gonadotropins are not required for gonadal development or sexual differentiation; LH or FSH receptor knockout mice are born phenotypically normal.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Thyroid Embryology",
                "Thyroid hormone synthesis begins at approximately 11 weeks of gestation.",
                True,
                "NIS upregulation at ~10 weeks coincides with onset of synthesis at 11 weeks.",
                ref(
                    "KEY POINTS",
                    "Thyroid hormone synthesis starts at 11 weeks of gestation.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Limitation of Hormone Secretion",
                "Fetal glucagon secretion increases promptly in response to acute hypoglycemia throughout gestation.",
                False,
                "Fetal glucagon secretory capacity is blunted; acute hypoglycemia does not evoke glucagon in the rat fetus.",
                ref(
                    "Functional Development of the Endocrine Pancreas",
                    "acute hypoglycemia does not evoke glucagon secretion in the rat fetus.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Insulin-Like Growth Factors",
                "Mutations in IGF1 or IGF1R in humans are associated with IUGR.",
                True,
                "Human IGF1 signaling contributes significantly to fetal growth; mutations cause growth restriction and hypoglycemia.",
                ref(
                    "Insulin-Like Growth Factors",
                    "In humans, mutations in IGF1 or IGF1R are associated with IUGR, suggesting that IGF1 signaling contributes significantly to fetal growth.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Programming of Fetal Endocrine Systems",
                "Imprinted genes are expressed from both parental alleles equally.",
                False,
                "Imprinted genes are expressed from only the paternal or maternal copy.",
                ref(
                    "Programming of Fetal Endocrine Systems",
                    "Imprinted genes are a class of genes in placental mammals and marsupials whose expression depends on the parental origin; they are expressed only from the paternal or the maternal gene copy but not biparentally.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Congenital Hypothyroidism",
                "Congenital hypothyroidism affects approximately 1 in 3000 to 4000 live births.",
                True,
                "CH is among the most common neonatal endocrine disorders.",
                ref(
                    "Congenital Hypothyroidism",
                    "Congenital hypothyroidism (CH) is a common endocrine disorder with an incidence of 1:3000 to 4000 at birth.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Insulin",
                "Infants of diabetic mothers may have macrosomia primarily from increased body fat.",
                True,
                "Fetal hyperinsulinemia increases lipogenesis; length increases little but fat and some organs enlarge.",
                ref(
                    "Insulin",
                    "Most of this increased weight is accounted for by body fat; there is little increase in body length, but some organomegaly may occur.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Cortisol Surge",
                "Homozygous CRH or glucocorticoid receptor deficiency in mice causes neonatal death with lung dysplasia.",
                True,
                "Prenatal cortisol/CRH signaling is essential for surfactant and lung maturation.",
                ref(
                    "Cortisol Surge",
                    "the progeny of homozygous CRH-deficient or glucocorticoid receptor-deficient animals die in the first 12 hours with lung dysplasia and surfactant deficiency.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Fetal Growth",
                "Postnatal GH is the primary driver of fetal somatic growth.",
                False,
                "T₄, GH, and gonadal steroids have limited fetal growth roles; IGFs and substrate supply dominate.",
                ref(
                    "Fetal Growth",
                    "The hormones most important for postnatal growth,  $ T_4 $, GH, and gonadal steroids, have a limited role in fetal growth",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Maternal and Fetal Medicine",
                "Noninvasive prenatal diagnosis can use cell-free fetal DNA from maternal blood.",
                True,
                "Maternal plasma DNA analysis enables lower-risk fetal evaluation.",
                ref(
                    "Maternal and Fetal Medicine",
                    "examples include sampling and analysis of free fetal DNA from maternal blood and analysis of fetal products accessible at maternal sites.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Fetal Adrenal Steroidogenesis",
                "Assertion: 46,XX fetuses with classic 21-hydroxylase deficiency may be virilized in utero.",
                "Reason: Cortisol deficiency elevates ACTH and excess adrenal androgen production during genital sensitivity.",
                0,
                "Both true and causally linked—loss of cortisol feedback drives androgen excess when external genitalia are forming.",
                ref(
                    "Fetal Adrenal Steroidogenesis",
                    "46,XX fetuses with steroidogenic defects (e.g., in CYP21 or CYP11) lack cortisol and have an elevated ACTH drive that results in excess production of fetal androgens at a time when the genital and scrotal folds are sensitive to androgen exposure, resulting in virilization of female genitalia.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Placental Transfer of Hormones",
                "Assertion: Antenatal betamethasone can mature fetal lungs in threatened preterm delivery.",
                "Reason: Synthetic glucocorticoids are inactivated by placental 11βHSD2 like endogenous cortisol.",
                2,
                "Assertion true; reason false—synthetic glucocorticoids bypass 11βHSD2 protection.",
                ref(
                    "Placental Transfer of Hormones",
                    "Synthetic glucocorticoids, such as dexamethasone or betamethasone, can bypass this protective mechanism resulting in exposure of the fetus to steroid hormones.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Ontogeny of Thyroid Hormone Secretion",
                "Assertion: Maternal T₄ is essential for early fetal brain development.",
                "Reason: Placental D3 completely blocks all maternal thyroid hormone transfer.",
                2,
                "Assertion true; reason false—limited but critical T₄ crosses early in gestation.",
                ref(
                    "Ontogeny of Thyroid Hormone Secretion",
                    "Early in gestation, placental transfer is the only source of  $ T_4 $ in fetal fluids and is essential for normal fetal neurodevelopment.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Fetal Sex Steroid Production",
                "Assertion: AMH causes regression of müllerian ducts in the male fetus.",
                "Reason: AMH is produced by fetal Leydig cells.",
                2,
                "Assertion true; reason false—AMH is secreted by Sertoli cells, not Leydig cells.",
                ref(
                    "Fetal Sex Steroid Production",
                    "It is produced by testicular Sertoli cells and reaches the müllerian ducts largely by diffusion; duct regression in vitro requires 24- to 36-hour exposure to AMH.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Insulin",
                "Assertion: Fetal hyperinsulinemia can cause macrosomia.",
                "Reason: Insulin stimulates fetal lipogenesis and growth.",
                0,
                "Both true—maternal diabetes and CHI/Beckwith states illustrate insulin-driven in utero growth.",
                ref(
                    "Insulin",
                    "Infants born to women with diabetes mellitus may have hyperinsulinemia associated with increased birth weight.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Programming of Fetal Endocrine Systems",
                "Assertion: IUGR is associated with adult cardiovascular disease.",
                "Reason: IUGR has no relationship to later metabolic disease.",
                2,
                "Assertion true; reason false—the chapter documents strong IUGR–cardiometabolic links.",
                ref(
                    "Programming of Fetal Endocrine Systems",
                    "There is now extensive documentation of the association of IUGR with an increased risk of later hypertension, insulin resistance, diabetes, and cardiovascular and coronary heart disease.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Human Hypothalamo-Pituitary Development",
                "Assertion: Rathke's pouch derives from oral ectoderm.",
                "Reason: The posterior pituitary also originates from oral ectoderm.",
                2,
                "Assertion true; reason false—posterior pituitary arises from ventral diencephalon infundibulum.",
                ref(
                    "Anterior Pituitary and Target Organs",
                    "the anterior and intermediate lobes are derived from oral ectoderm, and the posterior pituitary originates from the infundibulum, a specific region of the developing central nervous system (CNS) that forms in the midline of the ventral diencephalon.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Congenital Hyperinsulinism",
                "Assertion: CHI is the most common cause of persistent neonatal hypoglycemia.",
                "Reason: CHI features inappropriately high insulin at low glucose with suppressed ketogenesis.",
                0,
                "Both true—hyperinsulinism suppresses ketones/FFAs and requires high glucose infusion rates.",
                ref(
                    "Congenital Hyperinsulinism",
                    "Congenital hyperinsulinism (CHI) represents a group of clinically, genetically, and morphologically heterogeneous disorders and is the most frequent cause of persistent and recurrent hypoglycemia in neonates and infants.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Fetal Thyroid Hormone Biosynthesis",
                "Assertion: Fetal hypothalamo-pituitary-thyroid axis maturation completes by ~2 months after birth.",
                "Reason: The fetus has fully mature TSH feedback from midgestation.",
                2,
                "Assertion true; reason false—fetus progresses from primary/tertiary hypothyroid states to mature axis after birth.",
                ref(
                    "Fetal Thyroid Hormone Biosynthesis",
                    "Functionally, the fetus progresses from a state of both primary (thyroidal) and tertiary (hypothalamic) hypothyroidism at midgestation, through a state of mild tertiary hypothyroidism during the final weeks in utero, to a fully mature hypothalamic-pituitary-thyroid axis by 2 months after birth.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "The Fetal-Placental Unit",
                "Assertion: Placental estrogen synthesis requires fetal adrenal DHEA substrate.",
                "Reason: The placenta expresses CYP17 and synthesizes androgens de novo.",
                2,
                "Assertion true; reason false—placenta lacks CYP17 and depends on fetal/maternal C19 androgens.",
                ref(
                    "Placental Transfer of Hormones",
                    "the placenta lacks the cytochrome P450 enzyme CYP17 and accordingly is unable to synthesize estrogens de novo.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Glucose Homeostasis",
                "Assertion: Premature infants have more prolonged neonatal hypoglycemia than term infants.",
                "Reason: Preterm infants have reduced glycogen stores and immature gluconeogenesis.",
                0,
                "Both true—IUGR/preterm adaptation to intermittent feeding is incomplete.",
                ref(
                    "Glucose Homeostasis",
                    "Premature infants have more severe and more prolonged hypoglycemia because of reduced glycogen stores and impaired hepatic gluconeogenesis.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Neonatal Diabetes",
                "Assertion: KCNJ11 mutations can cause permanent neonatal diabetes responsive to sulfonylureas.",
                "Reason: KCNJ11 mutations always require lifelong insulin regardless of genotype.",
                2,
                "Assertion true; reason false—many KCNJ11/ABCC8 patients switch from insulin to sulfonylureas.",
                ref(
                    "Neonatal Diabetes",
                    "These patients are responsive to sulfonylurea therapy and do not require insulin treatment.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "20",
        "title": "Endocrinology of Fetal Development",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Harshini Katugampola, Ranna El-Khairi, and Mehul T. Dattani",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_20_Endocrinology_of_Fetal_Development.md",
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
