#!/usr/bin/env python3
"""Generate Williams 15e module w15-19 — Endocrine Changes in Pregnancy."""
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
OUT_NAME = "w15-19_Endocrine_Changes_in_Pregnancy.json"


def build() -> dict:
    p = "w15-19"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why pregnancy begins with endocrine change at implantation",
                "The endocrine impact of pregnancy is profound and starts with trophoblastic hCG at implantation—this sets the stage for corpus-luteum rescue, placental hormone production, and all subsequent maternal-fetal metabolic adaptation.",
                ref(
                    "KEY POINTS",
                    "The impact of pregnancy on the endocrine system is profound and begins with very early production of human chorionic gonadotropin from the trophoblast occurring at implantation.",
                ),
            ),
            note(
                f"{p}-n2",
                "Placental Development",
                "How hCG rescues the corpus luteum",
                "hCG appears in maternal serum 6–9 days after conception and maintains corpus-luteum progesterone until the luteal-placental shift at ~9–10 weeks—luteectomy before then causes progesterone collapse and pregnancy loss.",
                ref(
                    "Placental Development",
                    "The hCG is first detected in the maternal serum 6 to 9 days after conception and is essential for rescue and maintenance of the corpus luteum until the placenta takes over complete hormone production (the luteal-placental shift) at about 9 to 10 weeks of gestation.",
                ),
            ),
            note(
                f"{p}-n3",
                "Metabolic Adaptations",
                "How pregnancy reallocates maternal fuel to the fetus",
                "Pregnancy drives hyperinsulinemia, insulin resistance, higher lipids, relative fasting hypoglycemia, and efficient amino-acid transport—maternal tissues shift to lipolysis ('accelerated starvation') so glucose and amino acids preferentially supply the fetus.",
                ref(
                    "KEY POINTS",
                    "Changes in maternal metabolism during pregnancy prioritize fetal growth, including hyperinsulinemia, insulin resistance, increased plasma lipids, and more efficient plasma amino acid transport.",
                ),
            ),
            note(
                f"{p}-n4",
                "Metabolic Adaptations",
                "Why gestational diabetes resolves after delivery",
                "Placental hPL and placental growth hormone reduce insulin receptors and glucose transport; insulin resistance peaks in late pregnancy and reverses when the placenta is delivered—explaining transient GDM and postpartum normoglycemia in most women.",
                ref(
                    "Metabolic Adaptations",
                    "It is evident that the placenta and pregnancy hormones are key to metabolic changes observed to support the fetus—a phenomenon largely reversed with delivery of the placenta and resolution of gestational diabetes shortly after birth.",
                ),
            ),
            note(
                f"{p}-n5",
                "Human Chorionic Gonadotropin",
                "Why early pregnancy TSH falls",
                "hCG shares receptor homology with TSH; rising first-trimester hCG weakly stimulates the thyroid and suppresses maternal TSH—clinically important in hyperemesis, twin pregnancy, and trophoblastic disease where hCG can cause thyrotoxicosis.",
                ref(
                    "Human Chorionic Gonadotropin",
                    "Because of the close structural homology of the hLH-hCG receptor with the other glycoprotein hormone receptors, hCG may interact with the hTSH and hFSH receptors and thus has weak intrinsic hTSH and hFSH biologic activity.",
                ),
            ),
            note(
                f"{p}-n6",
                "Thyroid Gland",
                "How to adjust levothyroxine in pregnant hypothyroidism",
                "The mother is the fetal thyroid source through the first trimester; levothyroxine needs rise as early as week 5, with 50–85% of women requiring dose increases up to ~50%. Check TSH at the first prenatal visit and every 4–8 weeks—or empirically increase dose when pregnancy is confirmed.",
                ref(
                    "Thyroid Gland",
                    "Increased doses of thyroid hormone are needed in 50% to 85% of pregnant patients, and the total dose may increase as much as 50%.",
                ),
            ),
            note(
                f"{p}-n7",
                "Thyroid Gland",
                "Why subclinical hypothyroidism screening remains debated",
                "Subclinical hypothyroidism affects 2–3% of reproductive-age individuals; large RCTs (treatment after ~13 weeks) showed no neurocognitive benefit, but early gestation and TPO-antibody status may matter—guidelines diverge on universal screening.",
                ref(
                    "Thyroid Gland",
                    "Subclinical maternal hypothyroidism is a commonly encountered disorder of pregnancy and affects 2% to 3% of all people of reproductive age, with maternal thyroid peroxidase antibodies (TPO-ab) identified in up to 15%.",
                ),
            ),
            note(
                f"{p}-n8",
                "Pancreas",
                "How late-pregnancy insulin resistance develops",
                "Early pregnancy favors insulin hypersecretion and glycogen storage; later rising hPL and glucocorticoids drive insulin resistance—oral glucose loads produce higher, more sustained glucose and insulin with greater glucagon suppression than outside pregnancy.",
                ref(
                    "Pancreas",
                    "As pregnancy progresses, the levels of hPL rise, as do the levels of glucocorticoids, leading to the insulin resistance found during the last half of pregnancy.",
                ),
            ),
            note(
                f"{p}-n9",
                "Parathyroid Glands",
                "How calcium homeostasis adapts in pregnancy",
                "~30 g calcium transfers to the fetus (mostly third trimester); albumin-adjusted and ionized calcium rise slightly despite lower total calcium; intestinal absorption doubles and 1,25(OH)₂D increases from renal and placental 1α-hydroxylase.",
                ref(
                    "Parathyroid Glands",
                    "During pregnancy, approximately 30 g of calcium is transferred from the maternal compartment to the fetus, with most of the transfer occurring during the last trimester.",
                ),
            ),
            note(
                f"{p}-n10",
                "Parathyroid Glands",
                "How to manage hypoparathyroidism in pregnancy",
                "Fetal calcium demand often requires escalating oral elemental calcium (1.0–1.5 g/day) and calcitriol (0.5–1.0 µg/day) through gestation to prevent maternal and fetal hypocalcemia and fractures.",
                ref(
                    "Parathyroid Glands",
                    "This often requires a steady increase in calcium (1.0 or 1.5 g of elemental calcium per day) and calcitriol, the active form of vitamin D (1,25[OH]2D3; dosage is 0.5 to 1.0  $ \\mu $g/d) throughout pregnancy to maintain normal maternal serum calcium homeostasis.",
                ),
            ),
            note(
                f"{p}-n11",
                "Pituitary Gland",
                "Pituitary enlargement in pregnancy",
                "The anterior pituitary enlarges ~36% from lactotroph hyperplasia; prolactin rises to a mean ~207 ng/mL at term versus ~10 ng/mL premenopausally—distinguish physiologic enlargement from prolactinoma when evaluating headache or visual loss.",
                ref(
                    "Pituitary Gland",
                    "The anterior pituitary gland enlarges by an average of 36% during pregnancy, primarily because of a 10-fold increase in lactotroph size and number.",
                ),
            ),
            note(
                f"{p}-n12",
                "Pituitary Gland",
                "How to manage symptomatic prolactinoma in pregnancy",
                "Pregnancy-related pituitary enlargement can worsen micro- or macroadenomas; bromocriptine is effective and considered safe for symptomatic expansion, with transsphenoidal surgery reserved for refractory cases—cabergoline has less pregnancy experience.",
                ref(
                    "Pituitary Gland",
                    "In cases of symptomatic tumor expansion in pregnancy, the dopamine agonist bromocriptine can be safely used and is successful in reducing tumor size and symptoms in the majority of cases.",
                ),
            ),
            note(
                f"{p}-n13",
                "Adrenal Glands",
                "Maternal hypercortisolism without Cushing stigmata",
                "Estrogen doubles cortisol-binding globulin; total and free cortisol rise threefold by mid-pregnancy with maintained diurnal rhythm—elevated progesterone may block glucocorticoid stigmata despite high free cortisol.",
                ref(
                    "Adrenal Glands",
                    "Despite the elevated free cortisol levels, pregnant individuals do not develop the stigma of glucocorticoid excess, possibly because of the antiglucocorticoid activities of the elevated concentrations of progesterone.",
                ),
            ),
            note(
                f"{p}-n14",
                "Adrenal Glands",
                "Why Cushing syndrome in pregnancy favors adrenal etiology",
                "Hypercortisolism is rare in pregnancy because it usually causes infertility; when it occurs in pregnancy, primary adrenal hyperplasia is more common than pituitary Cushing disease—associated with hypertension, diabetes, preeclampsia, preterm delivery, and stillbirth.",
                ref(
                    "Adrenal Glands",
                    "Whereas outside of pregnancy hypercortisolism is most commonly caused by an ACTH-producing pituitary adenoma (Cushing disease), when encountered in pregnancy it is more likely due to primary adrenal hyperplasia (Cushing syndrome).",
                ),
            ),
            note(
                f"{p}-n15",
                "Human Placental Lactogen",
                "How hPL shapes maternal-fetal metabolism",
                "hPL correlates with placental mass, stimulates IGF-1, promotes insulin secretion yet induces insulin resistance and lipolysis—shunting glucose and amino acids to the fetus while the mother metabolizes free fatty acids.",
                ref(
                    "Human Placental Lactogen",
                    "It stimulates pancreatic islet insulin secretion, both directly and after carbohydrate administration, and is a diabetogenic factor during pregnancy through its promotion of insulin resistance.",
                ),
            ),
            note(
                f"{p}-n16",
                "Placental Growth Hormone",
                "Placental GH and pituitary GH suppression",
                "Placental GH-V rises from ~10 weeks, peaks third trimester, and at term accounts for ~85% of maternal GH bioactivity—high IGF-1 suppresses pituitary GH; pituitary GH normalizes within 48 hours postpartum.",
                ref(
                    "Placental Growth Hormone",
                    "It has been estimated that at term, 85% of the GH biologic activity in maternal serum is due to hGH-V, 12% to hPL, and only 3% to pituitary hGH.",
                ),
            ),
            note(
                f"{p}-n17",
                "Renin-Angiotensin System",
                "ACE inhibitors and ARBs in pregnancy",
                "ACE inhibitors cause oligohydramnios, fetal renal dysplasia, and calvarial hypoplasia; ARBs are also avoided—switch hypertensive patients to pregnancy-safe agents (e.g., methyldopa, nifedipine) before or in the first trimester.",
                ref(
                    "Renin-Angiotensin System",
                    "ACE inhibitors have been linked to oligohydramnios, fetal renal dysplasia, and fetal calvarial hypoplasia.",
                ),
            ),
            note(
                f"{p}-n18",
                "Noninvasive Prenatal Testing and Microchimerism",
                "Why positive NIPT requires confirmatory testing",
                "NIPT is highly accurate for common aneuploidies but false positives/negatives occur (e.g., confined placental mosaicism)—a positive screen mandates invasive fetal karyotype confirmation before irreversible decisions.",
                ref(
                    "Noninvasive Prenatal Testing and Microchimerism",
                    "Although NIPT is an improvement over older methods, false-positive and false-negative results are encountered, and therefore a positive NIPT screen result requires invasive fetal testing for confirmation.",
                ),
            ),
            note(
                f"{p}-n19",
                "Noninvasive Prenatal Testing and Microchimerism",
                "How microchimerism links pregnancy to autoimmune thyroid disease",
                "Bidirectional fetal-maternal cell trafficking persists indefinitely postpartum; microchimerism has been implicated in autoimmune thyroid disorders and type 1 diabetes—relevant when evaluating postpartum thyroid dysfunction and long-term maternal endocrine risk.",
                ref(
                    "KEY POINTS",
                    "Persistent postpartum microchimerism has been linked to autoimmune endocrinopathies in later life in both mother and offspring.",
                ),
            ),
            note(
                f"{p}-n20",
                "Human Chorionic Gonadotropin",
                "hCG kinetics in normal pregnancy",
                "hCG rises logarithmically, peaks 8–10 weeks after LMP, declines to a nadir at ~18 weeks, then plateaus until delivery—discordant curves (e.g., moles, ectopic pregnancy) prompt evaluation for GTD or nonviable pregnancy.",
                ref(
                    "Human Chorionic Gonadotropin",
                    "hCG is first detected in maternal serum 6 to 9 days after conception. The levels rise in a logarithmic fashion, peaking 8 to 10 weeks after the last menstrual period, followed by a decline to a nadir at 18 weeks, with subsequent levels remaining constant until delivery",
                ),
            ),
            note(
                f"{p}-n21",
                "Placental Hormone Production",
                "Maternal-fetal-placental steroid unit",
                "Placental progesterone depends on maternal LDL cholesterol; fetal adrenal DHEAS is sulfated, 16α-hydroxylated, and aromatized in placenta to estriol—the dominant maternal estrogen and a historical marker of fetal well-being.",
                ref(
                    "Placental Hormone Production",
                    "Further metabolism in the trophoblast by  $ 3\\beta $HSD1,  $ 17\\beta $HSD, and CYP19 leads to the generation of estriol, which is quantitatively the major estrogen in the maternal circulation during pregnancy.",
                ),
            ),
            note(
                f"{p}-n22",
                "Physiologic Adaptations",
                "How pregnancy alters drug dosing",
                "GFR and plasma volume rise ~50% in pregnancy—increase or monitor doses of renally cleared drugs (antiepileptics, β-lactams, low-molecular-weight heparin) to maintain therapeutic levels.",
                ref(
                    "Physiologic Adaptations",
                    "Some of these medications require dose adjustments because of the increased GFR of pregnancy.",
                ),
            ),
            note(
                f"{p}-n23",
                "The \"Fourth Trimester\" and the Parental Brain",
                "Why postpartum endocrine withdrawal matters clinically",
                "Placental hormones fall abruptly after delivery; vulnerable patients may develop postpartum psychiatric and metabolic maladaptation—gestational diabetes and hypertensive disorders herald later diabetes and cardiovascular disease and warrant continued surveillance.",
                ref(
                    "The \"Fourth Trimester\" and the Parental Brain",
                    "Particularly, we know now that gestational diabetes predisposes to maternal diabetes after gestation and that gestational hypertension is a harbinger of later maternal cardiovascular disease.",
                ),
            ),
            note(
                f"{p}-n24",
                "Thyroid Gland",
                "Pregnancy thyroid binding globulin changes",
                "Estrogen doubles TBG via increased synthesis and reduced clearance—total T₄/T₃ rise throughout pregnancy while free T₄ and free T₃ remain normal for most of gestation; do not mislabel euthyroid pregnant patients as hyperthyroid on total hormone assays alone.",
                ref(
                    "Thyroid Gland",
                    "The results are a twofold increase in TBG and increased total thyroxine ( $ T_4 $) and triiodothyronine ( $ T_3 $) levels in maternal serum throughout pregnancy, whereas for most of the gestation, the free  $ T_4 $ and free  $ T_3 $ concentrations remain normal.",
                ),
            ),
            note(
                f"{p}-n25",
                "Parathyroid Glands",
                "Hyperparathyroidism in pregnancy",
                "Pregnancy is somewhat protective because fetal calcium uptake lowers maternal calcium, but hypercalcemia can still cause nephrolithiasis, pancreatitis, hypertension, or crisis—bisphosphonates and plicamycin are avoided; calcitonin may be considered.",
                ref(
                    "Parathyroid Glands",
                    "Pregnancy is somewhat protective for patients with hyperparathyroidism because calcium uptake by the fetus helps lower maternal calcium levels.",
                ),
            ),
            note(
                f"{p}-n26",
                "Human Chorionic Corticotropin",
                "Placental ACTH and maternal cortisol",
                "Placental hCC and pituitary ACTH both rise in pregnancy; placental CRH is stimulated (not suppressed) by glucocorticoids—contributing to ACTH resistance to dexamethasone suppression and elevated maternal free cortisol.",
                ref(
                    "Human Chorionic Corticotropin",
                    "Indeed, the resistance of maternal plasma ACTH concentrations to suppression after glucocorticoid administration may reflect the placental hCC contribution to the total pool of circulating immunoreactive ACTH.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Thyroid Gland",
                "A 28-year-old at 8 weeks' gestation has TSH 0.1 mIU/L (low), free T₄ normal, no thyrotoxic symptoms, and hCG 95,000 IU/L. Best next step?",
                [
                    "Reassurance and repeat thyroid tests—likely physiologic hCG-mediated TSH suppression",
                    "Start methimazole immediately for Graves disease",
                    "Order radioactive iodine uptake scan",
                    "Withhold all thyroid testing until postpartum",
                ],
                0,
                "First-trimester hCG has weak TSH activity; isolated low TSH with normal free T₄ and very high hCG is usually physiologic unless thyrotoxic symptoms or Graves markers are present.",
                ref(
                    "Human Chorionic Gonadotropin",
                    "It is especially important in patients with hydatidiform moles and other forms of trophoblastic disease, in which hCG levels may exceed 100,000 IU/L and result in clinical thyrotoxicosis",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Thyroid Gland",
                "A woman with hypothyroidism on levothyroxine 100 µg daily has a positive pregnancy test at 5 weeks. TSH is pending. Best management now?",
                [
                    "Increase levothyroxine empirically (~25–30%) and check TSH within 4 weeks",
                    "Stop levothyroxine until TSH returns",
                    "Switch to liothyronine monotherapy",
                    "Defer any dose change until the third trimester",
                ],
                0,
                "Requirements rise as early as week 5; most patients need 50–85% dose increases—empiric uptitration at pregnancy confirmation is acceptable per THERAPY trial data cited in the chapter.",
                ref(
                    "Thyroid Gland",
                    "Thus, in those with preexisting hypothyroidism, it is necessary to check thyroid function at the first prenatal visit to determine if additional thyroid hormone replacement is necessary. Alternatively, the dose can be empirically increased when pregnancy is confirmed before any laboratory assessment of thyroid function.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Pancreas",
                "A 32-year-old G2P1 at 26 weeks has a 1-hour 50-g glucose screen of 165 mg/dL. She is obese. Most likely underlying physiology?",
                [
                    "Late-gestation hPL- and cortisol-mediated insulin resistance",
                    "Autoimmune destruction of β-cells identical to type 1 diabetes",
                    "Excess pituitary GH causing hypoglycemia",
                    "Placental sulfatase deficiency",
                ],
                0,
                "GDM reflects progressive placental hormone-driven insulin resistance in the second half of pregnancy, not autoimmune β-cell loss.",
                ref(
                    "Pancreas",
                    "As pregnancy progresses, the levels of hPL rise, as do the levels of glucocorticoids, leading to the insulin resistance found during the last half of pregnancy.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Metabolic Adaptations",
                "A woman with diet-controlled GDM delivers at term. When should you expect glucose tolerance to normalize in most patients?",
                [
                    "Shortly after placental delivery",
                    "Only after 12 months of lactation",
                    "Never—GDM always becomes permanent type 2 diabetes immediately",
                    "After menopause",
                ],
                0,
                "Insulin resistance is placental-driven; delivery of the placenta typically resolves GDM, though long-term diabetes risk remains elevated.",
                ref(
                    "Metabolic Adaptations",
                    "a phenomenon largely reversed with delivery of the placenta and resolution of gestational diabetes shortly after birth.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Pituitary Gland",
                "A 30-year-old with known prolactinoma on cabergoline becomes pregnant and develops bitemporal field loss at 14 weeks. Best initial therapy?",
                [
                    "Bromocriptine for symptomatic tumor expansion",
                    "Immediate bilateral adrenalectomy",
                    "High-dose estrogen to shrink the tumor",
                    "Observation only—pituitary tumors never grow in pregnancy",
                ],
                0,
                "Symptomatic prolactinoma expansion in pregnancy is treated with dopamine agonists; bromocriptine has the most pregnancy safety data.",
                ref(
                    "Pituitary Gland",
                    "In cases of symptomatic tumor expansion in pregnancy, the dopamine agonist bromocriptine can be safely used and is successful in reducing tumor size and symptoms in the majority of cases.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Parathyroid Glands",
                "A woman with surgical hypoparathyroidism is planning pregnancy. Preconception counseling should emphasize:",
                [
                    "Anticipate increasing calcium and calcitriol doses during gestation",
                    "Discontinue all calcium supplements once pregnant",
                    "Fetal hyperparathyroidism will protect maternal calcium",
                    "IV bisphosphonates are first-line in pregnancy",
                ],
                0,
                "Substantial fetal calcium transfer in the third trimester often requires escalating oral calcium and active vitamin D to prevent hypocalcemia and fractures.",
                ref(
                    "Parathyroid Glands",
                    "This often requires a steady increase in calcium (1.0 or 1.5 g of elemental calcium per day) and calcitriol, the active form of vitamin D (1,25[OH]2D3; dosage is 0.5 to 1.0  $ \\mu $g/d) throughout pregnancy to maintain normal maternal serum calcium homeostasis.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Parathyroid Glands",
                "A 34-year-old at 30 weeks has total calcium 8.0 mg/dL (low) but albumin-adjusted and ionized calcium normal. Interpretation?",
                [
                    "Physiologic dilutional hypocalcemia from expanded vascular volume",
                    "Severe maternal hypoparathyroidism requiring emergency calcitriol",
                    "Primary hyperparathyroidism crisis",
                    "Vitamin D intoxication",
                ],
                0,
                "Total calcium falls with hypoalbuminemia in pregnancy, but adjusted and ionized calcium are typically normal or slightly elevated.",
                ref(
                    "Parathyroid Glands",
                    "Maternal total serum calcium levels decrease during pregnancy, with a nadir at 28 to 32 weeks related to the decrease in albumin levels that accompanies the increase in vascular volume. However, the albumin-adjusted total calcium and the ionized calcium concentrations actually rise slightly above this level in the nonpregnant state.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Renin-Angiotensin System",
                "A woman with type 2 diabetes and microalbuminuria on lisinopril discovers she is 6 weeks pregnant. Best antihypertensive change?",
                [
                    "Stop ACE inhibitor and switch to a pregnancy-safe agent such as methyldopa or nifedipine",
                    "Continue lisinopril because renal protection outweighs fetal risk",
                    "Add an ARB for synergistic fetal renal protection",
                    "Stop all antihypertensives regardless of blood pressure",
                ],
                0,
                "ACE inhibitors are teratogenic in pregnancy (oligohydramnios, fetal renal dysplasia, calvarial hypoplasia) and must be discontinued.",
                ref(
                    "Renin-Angiotensin System",
                    "As a result, this group of medications is avoided in pregnancy.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Adrenal Glands",
                "A 26-year-old at 20 weeks has new hypertension, glucose intolerance, and purple striae; 24-hour urine cortisol is markedly elevated. In pregnancy, the most likely etiology is:",
                [
                    "Primary adrenal Cushing syndrome rather than pituitary Cushing disease",
                    "Physiologic pregnancy hypercortisolism only—no workup needed",
                    "Addison disease",
                    "Pheochromocytoma exclusively",
                ],
                0,
                "When hypercortisolism occurs in pregnancy, adrenal Cushing syndrome is more likely than pituitary Cushing disease because pituitary disease more often causes infertility.",
                ref(
                    "Adrenal Glands",
                    "when encountered in pregnancy it is more likely due to primary adrenal hyperplasia (Cushing syndrome).",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Human Chorionic Gonadotropin",
                "A 22-year-old at 10 weeks has severe nausea, tachycardia, suppressed TSH, and hCG >200,000 IU/L after twin pregnancy diagnosis. Thyrotoxicosis mechanism?",
                [
                    "hCG cross-stimulation of the TSH receptor",
                    "Graves TSH-receptor stimulating antibodies only",
                    "Destructive thyroiditis from iodine excess",
                    "Pituitary TSH hypersecretion",
                ],
                0,
                "Very high hCG (twins, GTD) can cause clinical thyrotoxicosis via weak intrinsic TSH activity of hCG.",
                ref(
                    "Human Chorionic Gonadotropin",
                    "the hTSH-like activity of hCG is clinically manifested during normal pregnancy by the reciprocal decrease in maternal hTSH at the time of the hCG peak between 8 and 12 weeks after the last menstrual period.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Placental Development",
                "A patient undergoes therapeutic abortion at 7 weeks' gestation. Progesterone falls rapidly afterward because:",
                [
                    "The corpus luteum depends on trophoblastic hCG until the luteal-placental shift",
                    "Placental progesterone already supplies 90% of hormone by 7 weeks",
                    "hCG stimulates progesterone only after 20 weeks",
                    "Progesterone is never required for early pregnancy",
                ],
                0,
                "Before ~9–10 weeks the corpus luteum requires hCG; abortion removes the trophoblastic signal and progesterone collapses.",
                ref(
                    "Human Chorionic Gonadotropin",
                    "After a therapeutic abortion, progesterone levels also drop rapidly.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Noninvasive Prenatal Testing and Microchimerism",
                "Cell-free DNA screening reports trisomy 21; ultrasound is normal. Next step?",
                [
                    "Offer invasive diagnostic testing (e.g., amniocentesis) for confirmation",
                    "Terminate pregnancy based on NIPT alone",
                    "No further testing—NIPT is definitive",
                    "Repeat NIPT in the third trimester only",
                ],
                0,
                "Positive NIPT requires invasive fetal testing for confirmation because false-positive and false-negative results occur.",
                ref(
                    "Noninvasive Prenatal Testing and Microchimerism",
                    "a positive NIPT screen result requires invasive fetal testing for confirmation.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Physiologic Adaptations",
                "A pregnant woman on enoxaparin for prior PE has subtherapeutic anti-Xa levels at 20 weeks despite adequate pre-pregnancy dosing. Most likely explanation?",
                [
                    "Increased GFR and volume of distribution in pregnancy",
                    "Placental degradation of heparin",
                    "Complete cessation of renal LMWH clearance",
                    "hCG directly antagonizes anticoagulation",
                ],
                0,
                "Pregnancy increases GFR and distribution volume, often necessitating higher LMWH doses to maintain therapeutic anti-Xa levels.",
                ref(
                    "Physiologic Adaptations",
                    "Although only a small portion of the drug is cleared in the kidney, the increased GFR of pregnancy is thought to contribute to the much larger doses required in pregnant individuals to maintain effectiveness.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Human Placental Lactogen",
                "A lean woman fasts overnight at 34 weeks and develops ketonemia with normal glucose. This reflects:",
                [
                    "Accelerated starvation physiology with maternal lipolysis sparing glucose for the fetus",
                    "Diabetic ketoacidosis requiring insulin infusion",
                    "Growth hormone deficiency",
                    "Adrenal insufficiency crisis",
                ],
                0,
                "Pregnancy shifts maternal fuel use to lipids/ketones while conserving glucose for fetal transfer—an 'accelerated starvation' state.",
                ref(
                    "Metabolic Adaptations",
                    "To compensate, maternal cells turn toward lipid metabolism for energy-producing levels of ketones similar to that seen after prolonged fasting.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Thyroid Gland",
                "A euthyroid woman at 16 weeks has total T₄ above the nonpregnant reference range and normal free T₄. Management?",
                [
                    "No treatment—expected rise in total T₄ from increased TBG",
                    "Start antithyroid drugs",
                    "Reduce dietary iodine to zero",
                    "Subtotal thyroidectomy",
                ],
                0,
                "Estrogen doubles TBG, raising total T₄/T₃ while free hormones remain normal in most of gestation.",
                ref(
                    "Thyroid Gland",
                    "whereas for most of the gestation, the free  $ T_4 $ and free  $ T_3 $ concentrations remain normal.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Pituitary Gland",
                "MRI at 28 weeks shows pituitary height 12 mm with homogeneous enlargement, no adenoma, normal visual fields. Best interpretation?",
                [
                    "Physiologic lactotroph hyperplasia of pregnancy",
                    "Craniopharyngioma requiring urgent resection",
                    "Sheehan syndrome",
                    "Empty sella syndrome",
                ],
                0,
                "Anterior pituitary enlarges ~36% in pregnancy from lactotroph proliferation—distinguish from adenoma by clinical context and imaging morphology.",
                ref(
                    "Pituitary Gland",
                    "This enlargement increases the height and convexity of the pituitary that is observed on magnetic resonance imaging.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Human Chorionic Gonadotropin",
                "Serum hCG is elevated but urine pregnancy test is negative. Suspected diagnosis?",
                [
                    "Phantom hCG from heterophilic antibodies—not true gestational hCG",
                    "Complete hydatidiform mole",
                    "Normal intrauterine twin pregnancy",
                    "Placental sulfatase deficiency",
                ],
                0,
                "Heterophilic antibody interference causes serum false positives not excreted in urine—urine test negative despite 'positive' serum.",
                ref(
                    "Human Chorionic Gonadotropin",
                    "Because these substances are not excreted in the urine, a urine pregnancy test will be negative in the presence of such \"phantom hCG.\"",
                ),
            ),
            mcq(
                f"{p}-q18",
                "The \"Fourth Trimester\" and the Parental Brain",
                "A woman had GDM treated with insulin during pregnancy. Postpartum glucose is normal. Long-term counseling should include:",
                [
                    "Screen for type 2 diabetes because GDM predicts later maternal diabetes",
                    "No further metabolic follow-up is ever needed",
                    "Permanent insulin therapy is mandatory lifelong",
                    "Breastfeeding contraindicated after GDM",
                ],
                0,
                "GDM resolves postpartum in most but strongly predicts future diabetes and cardiovascular disease—ongoing surveillance is warranted.",
                ref(
                    "The \"Fourth Trimester\" and the Parental Brain",
                    "gestational diabetes predisposes to maternal diabetes after gestation",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Parathyroid Glands",
                "A pregnant woman with primary hyperparathyroidism develops worsening nausea and abdominal pain. Concerning complication to evaluate?",
                [
                    "Hypercalcemic pancreatitis or nephrolithiasis",
                    "Hypocalcemic tetany from fetal protection",
                    "Adrenal crisis",
                    "Sheehan syndrome",
                ],
                0,
                "Hyperparathyroidism in pregnancy can cause nausea, vomiting, pain, renal colic, pancreatitis, hypertension, and hypercalcemic crisis.",
                ref(
                    "Parathyroid Glands",
                    "Although patients with hypercalcemia in pregnancy often have mild to moderate symptoms of nausea, vomiting, pain, and renal colic, some experience more serious complications such as nephrolithiasis, pancreatitis, hypertension, bone disease, and hypercalcemic crisis.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Placental Growth Hormone",
                "At 32 weeks, maternal IGF-1 is high and pituitary GH response to hypoglycemia is blunted. Explanation?",
                [
                    "Placental GH-V drives IGF-1 and suppresses pituitary GH",
                    "Growth hormone deficiency from pituitary infarction",
                    "hPL blocks all GH receptors",
                    "Estrogen abolishes IGF-1 production",
                ],
                0,
                "Placental GH stimulates IGF-1, which feeds back to suppress pituitary GH—provocative GH responses differ between first and second halves of pregnancy.",
                ref(
                    "Pituitary Gland",
                    "The observed rise in placental GH- stimulated IGF1 likely suppresses pituitary GH during the second half of pregnancy.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Thyroid Gland",
                "A 29-year-old at 10 weeks has TPO antibodies positive, normal TSH, and no symptoms. Per current evidence in this chapter, screening debate centers on:",
                [
                    "Whether early treatment of subclinical hypothyroidism improves offspring neurodevelopment",
                    "Whether TPO antibodies cause acromegaly",
                    "Whether levothyroxine is contraindicated in all pregnancy",
                    "Whether hCG never affects thyroid tests",
                ],
                0,
                "Large RCTs after ~13 weeks showed no cognitive benefit from treating subclinical hypothyroidism, but early gestation and antibody status remain areas of uncertainty.",
                ref(
                    "Thyroid Gland",
                    "Subsequently, two large randomized trials were unable to demonstrate a benefit in neurocognitive development for the offspring of patients screened and treated for subclinical hypothyroidism.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Noninvasive Prenatal Testing and Microchimerism",
                "A woman develops new thyroid autoimmunity years after delivery. Plausible contributing mechanism discussed in this chapter?",
                [
                    "Persistent fetal microchimerism triggering autoimmune endocrinopathy",
                    "Complete clearance of all fetal cells by 6 weeks postpartum",
                    "hPL permanently destroying the thyroid",
                    "Placental CRH curing autoimmune disease",
                ],
                0,
                "Microchimerism persists indefinitely and has been linked to autoimmune thyroid disorders in mother and offspring.",
                ref(
                    "Noninvasive Prenatal Testing and Microchimerism",
                    "Although both maternal and fetal microchimerism have been implicated as causes of autoimmune diseases, including autoimmune thyroid disorders and type 1 diabetes,",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Adrenal Glands",
                "A pregnant woman at 30 weeks has elevated total cortisol but no striae, glucose 92 mg/dL fasting, and normal blood pressure. Best conclusion?",
                [
                    "Likely physiologic pregnancy hypercortisolism with progesterone blocking cushingoid features",
                    "Definite Cushing syndrome requiring adrenalectomy",
                    "Addison disease",
                    "Pheochromocytoma",
                ],
                0,
                "Elevated free cortisol is expected in pregnancy; progesterone's antiglucocorticoid effect prevents typical Cushing stigmata in uncomplicated pregnancies.",
                ref(
                    "Adrenal Glands",
                    "Despite the elevated free cortisol levels, pregnant individuals do not develop the stigma of glucocorticoid excess, possibly because of the antiglucocorticoid activities of the elevated concentrations of progesterone.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Human Chorionic Gonadotropin",
                "A complete hydatidiform mole is suspected. Besides ultrasound, the most useful tumor marker is:",
                [
                    "Serial serum hCG reflecting trophoblast burden",
                    "Serum prolactin only",
                    "Urine estriol as sole marker",
                    "Plasma renin activity",
                ],
                0,
                "GTD secretes hCG proportional to tumor burden—serial hCG guides diagnosis and treatment response.",
                ref(
                    "Human Chorionic Gonadotropin",
                    "the serum and urine concentrations of hCG roughly parallel the tumor burden and also provide prognostic information.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Metabolic Adaptations",
                "A resident asks why pregnant women become hypertriglyceridemic. Best explanation?",
                [
                    "Pregnancy increases LDL/VLDL, supplying placental cholesterol for steroidogenesis",
                    "Placental HMG-CoA reductase overactivity",
                    "Complete cessation of lipolysis",
                    "Insulin hypersensitivity lowering all lipids",
                ],
                0,
                "Elevated LDL/VLDL support placental steroid hormone production because the placenta has limited de novo cholesterol synthesis.",
                ref(
                    "Metabolic Adaptations",
                    "The increased maternal low-density lipoprotein (LDL) and very low-density lipoprotein (VLDL) that occur in pregnancy are also thought to be the main cholesterol supply for steroid hormone production in the placenta, as the placenta has very low hydroxymethylglutaryl-coenzyme A (HMG-CoA) reductase activity and thus limited ability to produce cholesterol from acetate in situ.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Renin-Angiotensin System",
                "A pregnant patient needs antihypertensive therapy. Which agent has the strongest pregnancy safety evidence in this chapter?",
                [
                    "Methyldopa",
                    "Lisinopril",
                    "Losartan",
                    "Spironolactone at high dose for all patients",
                ],
                0,
                "Methyldopa is the best-studied antihypertensive in pregnancy; ACE inhibitors and ARBs are avoided.",
                ref(
                    "Renin-Angiotensin System",
                    "Methyldopa is the best studied antihypertensive medication in pregnancy and is safe for use at any point in gestation.",
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
                "Human chorionic gonadotropin production begins at implantation.",
                True,
                "KEY POINTS state pregnancy's endocrine impact begins with early trophoblastic hCG at implantation.",
                ref(
                    "KEY POINTS",
                    "The impact of pregnancy on the endocrine system is profound and begins with very early production of human chorionic gonadotropin from the trophoblast occurring at implantation.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Placental Development",
                "hCG is essential for corpus luteum maintenance until the luteal-placental shift at about 9 to 10 weeks.",
                True,
                "Trophoblastic hCG rescues the corpus luteum until placental hormone production assumes full support.",
                ref(
                    "Placental Development",
                    "essential for rescue and maintenance of the corpus luteum until the placenta takes over complete hormone production (the luteal-placental shift) at about 9 to 10 weeks of gestation.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Thyroid Gland",
                "Free thyroxine concentrations remain normal for most of gestation despite increased total T₄ from elevated TBG.",
                True,
                "Estrogen doubles TBG raising total hormones while free T₄/T₃ stay normal for most of pregnancy.",
                ref(
                    "Thyroid Gland",
                    "whereas for most of the gestation, the free  $ T_4 $ and free  $ T_3 $ concentrations remain normal.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Metabolic Adaptations",
                "Gestational diabetes typically resolves shortly after delivery of the placenta.",
                True,
                "Placental hormones drive insulin resistance; removal of placenta reverses GDM in most cases.",
                ref(
                    "Metabolic Adaptations",
                    "resolution of gestational diabetes shortly after birth.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Pituitary Gland",
                "The anterior pituitary enlarges during pregnancy primarily from lactotroph hyperplasia.",
                True,
                "A 36% average enlargement reflects 10-fold lactotroph increase.",
                ref(
                    "Pituitary Gland",
                    "primarily because of a 10-fold increase in lactotroph size and number.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Renin-Angiotensin System",
                "ACE inhibitors are safe throughout pregnancy for diabetic nephropathy.",
                False,
                "ACE inhibitors are linked to fetal renal dysplasia, oligohydramnios, and calvarial hypoplasia and are avoided.",
                ref(
                    "Renin-Angiotensin System",
                    "As a result, this group of medications is avoided in pregnancy.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Parathyroid Glands",
                "Approximately 30 g of calcium is transferred from mother to fetus during pregnancy.",
                True,
                "Most calcium transfer occurs in the third trimester.",
                ref(
                    "Parathyroid Glands",
                    "During pregnancy, approximately 30 g of calcium is transferred from the maternal compartment to the fetus, with most of the transfer occurring during the last trimester.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Human Chorionic Gonadotropin",
                "hCG has weak intrinsic thyrotropin activity that can suppress maternal TSH in early pregnancy.",
                True,
                "hCG can interact with TSH receptors, producing reciprocal hCG peak and TSH nadir at 8–12 weeks.",
                ref(
                    "Human Chorionic Gonadotropin",
                    "the hTSH-like activity of hCG is clinically manifested during normal pregnancy by the reciprocal decrease in maternal hTSH at the time of the hCG peak between 8 and 12 weeks after the last menstrual period.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Adrenal Glands",
                "When hypercortisolism occurs in pregnancy, pituitary Cushing disease is more common than adrenal Cushing syndrome.",
                False,
                "In pregnancy, primary adrenal hyperplasia is more likely than pituitary ACTH adenoma.",
                ref(
                    "Adrenal Glands",
                    "when encountered in pregnancy it is more likely due to primary adrenal hyperplasia (Cushing syndrome).",
                ),
            ),
            tf(
                f"{p}-t10",
                "Noninvasive Prenatal Testing and Microchimerism",
                "A positive NIPT result requires invasive fetal testing for confirmation.",
                True,
                "False-positive and false-negative NIPT results mandate confirmatory invasive testing.",
                ref(
                    "Noninvasive Prenatal Testing and Microchimerism",
                    "a positive NIPT screen result requires invasive fetal testing for confirmation.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Human Placental Lactogen",
                "Human placental lactogen promotes insulin resistance during pregnancy.",
                True,
                "hPL is described as a diabetogenic factor through insulin resistance despite stimulating insulin secretion.",
                ref(
                    "Human Placental Lactogen",
                    "is a diabetogenic factor during pregnancy through its promotion of insulin resistance.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Thyroid Gland",
                "Large randomized trials demonstrated clear neurocognitive benefit from treating subclinical hypothyroidism identified after 13 weeks' gestation.",
                False,
                "RCTs cited in the chapter did not show offspring neurocognitive benefit with treatment initiated after ~13 weeks.",
                ref(
                    "Thyroid Gland",
                    "two large randomized trials were unable to demonstrate a benefit in neurocognitive development for the offspring of patients screened and treated for subclinical hypothyroidism.",
                ),
            ),
            tf(
                f"{p}-t13",
                "KEY POINTS",
                "Persistent postpartum microchimerism has been linked to autoimmune endocrinopathies.",
                True,
                "KEY POINTS and microchimerism section link persistent fetal cells to autoimmune thyroid and other endocrine disorders.",
                ref(
                    "KEY POINTS",
                    "Persistent postpartum microchimerism has been linked to autoimmune endocrinopathies in later life in both mother and offspring.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Placental Development",
                "Assertion: hCG maintains early pregnancy by rescuing the corpus luteum.",
                "Reason: hCG is first detected 6 to 9 days after conception and supports the corpus luteum until the luteal-placental shift.",
                0,
                "Both true—early trophoblastic hCG is the physiologic corpus-luteum rescue signal.",
                ref(
                    "Placental Development",
                    "The hCG is first detected in the maternal serum 6 to 9 days after conception and is essential for rescue and maintenance of the corpus luteum until the placenta takes over complete hormone production (the luteal-placental shift) at about 9 to 10 weeks of gestation.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Human Chorionic Gonadotropin",
                "Assertion: Very high hCG levels can cause clinical thyrotoxicosis.",
                "Reason: hCG has no interaction with TSH receptors.",
                2,
                "Assertion true in moles/GTD; reason false—hCG has weak intrinsic TSH activity via receptor homology.",
                ref(
                    "Human Chorionic Gonadotropin",
                    "hCG may interact with the hTSH and hFSH receptors and thus has weak intrinsic hTSH and hFSH biologic activity.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Thyroid Gland",
                "Assertion: Most pregnant hypothyroid patients need increased levothyroxine dosing.",
                "Reason: The fetus produces its own thyroid hormone throughout the first trimester.",
                2,
                "Assertion true (50–85% need increases); reason false—the mother supplies fetal thyroid hormone in the first trimester.",
                ref(
                    "Thyroid Gland",
                    "the pregnant woman is the source of  $ T_4 $ and  $ T_3 $ for the fetus throughout the first trimester.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Pancreas",
                "Assertion: Insulin resistance increases in the last half of pregnancy.",
                "Reason: Rising hPL and glucocorticoids contribute to late-gestation insulin resistance.",
                0,
                "Both true—placental and adrenal hormones drive progressive insulin resistance.",
                ref(
                    "Pancreas",
                    "As pregnancy progresses, the levels of hPL rise, as do the levels of glucocorticoids, leading to the insulin resistance found during the last half of pregnancy.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Metabolic Adaptations",
                "Assertion: Gestational diabetes usually resolves after delivery.",
                "Reason: Insulin resistance is largely placental-hormone mediated.",
                0,
                "Both true—delivery of placenta reverses the diabetogenic hormonal milieu.",
                ref(
                    "Metabolic Adaptations",
                    "largely reversed with delivery of the placenta and resolution of gestational diabetes shortly after birth.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Parathyroid Glands",
                "Assertion: Pregnancy increases intestinal calcium absorption.",
                "Reason: 1,25-dihydroxyvitamin D levels fall throughout pregnancy.",
                2,
                "Assertion true; reason false—1,25(OH)₂D and its free fraction rise, enhancing absorption.",
                ref(
                    "Parathyroid Glands",
                    "intestinal calcium absorption undergoes a twofold increase.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Pituitary Gland",
                "Assertion: Bromocriptine can be used for symptomatic prolactinoma expansion in pregnancy.",
                "Reason: Dopamine agonists are absolutely contraindicated in all pregnancies.",
                2,
                "Assertion true; reason false—bromocriptine is used safely for symptomatic expansion in pregnancy.",
                ref(
                    "Pituitary Gland",
                    "the dopamine agonist bromocriptine can be safely used and is successful in reducing tumor size and symptoms in the majority of cases.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Adrenal Glands",
                "Assertion: Pregnant women may have elevated free cortisol without Cushing stigmata.",
                "Reason: High progesterone may exert antiglucocorticoid activity.",
                0,
                "Both true—physiologic hypercortisolism differs from Cushing syndrome clinically.",
                ref(
                    "Adrenal Glands",
                    "possibly because of the antiglucocorticoid activities of the elevated concentrations of progesterone.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Renin-Angiotensin System",
                "Assertion: ACE inhibitors should be avoided in pregnancy.",
                "Reason: ACE inhibitors are linked to fetal renal dysplasia and oligohydramnios.",
                0,
                "Both true—teratogenic renal and amniotic fluid effects mandate avoidance.",
                ref(
                    "Renin-Angiotensin System",
                    "ACE inhibitors have been linked to oligohydramnios, fetal renal dysplasia, and fetal calvarial hypoplasia.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Human Placental Lactogen",
                "Assertion: hPL contributes to gestational insulin resistance.",
                "Reason: hPL only enhances insulin sensitivity.",
                2,
                "Assertion true; reason false—hPL is diabetogenic via insulin resistance despite stimulating insulin secretion.",
                ref(
                    "Human Placental Lactogen",
                    "is a diabetogenic factor during pregnancy through its promotion of insulin resistance.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Noninvasive Prenatal Testing and Microchimerism",
                "Assertion: Microchimerism may contribute to autoimmune thyroid disease after pregnancy.",
                "Reason: All fetal cells are cleared from maternal circulation within days of delivery.",
                2,
                "Assertion true per chapter; reason false—fetal cells persist indefinitely postpartum.",
                ref(
                    "Noninvasive Prenatal Testing and Microchimerism",
                    "microchimerism apparently persists indefinitely, as fetal cells have been found in maternal circulation decades after birth",
                ),
            ),
            ar(
                f"{p}-ar12",
                "The \"Fourth Trimester\" and the Parental Brain",
                "Assertion: Gestational diabetes predicts later maternal diabetes.",
                "Reason: GDM has no relationship to future maternal metabolic disease.",
                2,
                "Assertion true; reason false—the chapter links GDM to post-gestational diabetes and cardiovascular risk.",
                ref(
                    "The \"Fourth Trimester\" and the Parental Brain",
                    "gestational diabetes predisposes to maternal diabetes after gestation",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "19",
        "title": "Endocrine Changes in Pregnancy",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Sarah L. Berga and Thaddeus P. Waters",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_19_Endocrine_Changes_in_Pregnancy.md",
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
