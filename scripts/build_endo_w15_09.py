#!/usr/bin/env python3
"""Generate Williams 15e module w15-09 — Thyroid Pathophysiology and Diagnostic Evaluation."""
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
OUT_NAME = "w15-09_Thyroid_Pathophysiology_and_Diagnostic_Evaluation.json"


def build() -> dict:
    p = "w15-09"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Embryology",
                "Thyroid anlage migration and thyroglossal duct",
                "The thyroid anlage buds from foregut endoderm at embryonic day 16–17, migrates caudally along the thyroglossal duct, and normally fragments by the second month leaving the foramen caecum. Remnants can form lingual thyroid, thyroglossal duct cysts, or ectopic mediastinal tissue.",
                ref(
                    "Structural Embryology",
                    "Normally the thyroglossal duct undergoes dissolution and fragmentation by about the second month after conception, leaving at its point of origin a small dimple at the junction of the middle and posterior thirds of the tongue, the foramen caecum.",
                ),
            ),
            note(
                f"{p}-n2",
                "Embryology",
                "Why early thyroid growth is TSH independent",
                "Follicular cells acquire thyroglobulin synthesis by day 29, but iodide trapping and T4 synthesis await NIS expression around week 11, whereas pituitary TSH capacity does not appear until week 14—so early thyroid development proceeds without TSH drive.",
                ref(
                    "Functional Ontogeny",
                    "Early growth and development of the thyroid do not seem to be TSH dependent because the capacity of the pituitary to synthesize and secrete TSH is not apparent until the 14th week.",
                ),
            ),
            note(
                f"{p}-n3",
                "Anatomy",
                "Normal thyroid size and vascularity",
                "The euthyroid gland weighs 15–20 g with lobes ~4 cm long; blood flow is 4–6 mL/min/g. In Graves disease flow may exceed 1 L/min with an audible bruit or palpable thrill.",
                ref(
                    "Anatomy and Histology",
                    "Estimates of thyroid blood flow range from 4 to 6 mL/minute/g, well in excess of the blood flow to the kidney (3 mL/minute/g).",
                ),
            ),
            note(
                f"{p}-n4",
                "Iodine economy",
                "Dietary iodine requirements and deficiency burden",
                "At least 100 µg iodine daily eliminates deficiency signs; ~1 billion people live in iodine-deficient areas, causing endemic goiter and preventable cretinism—the most common preventable cause of mental impairment worldwide.",
                ref(
                    "Dietary Iodine",
                    "An estimated 1 billion individuals live in iodine-deficient areas of the world, and these people often develop TSH-induced compensatory enlargement of the thyroid (endemic goiter).",
                ),
            ),
            note(
                f"{p}-n5",
                "Iodine transport",
                "How NIS concentrates iodide in thyrocytes",
                "NIS (SLC5A5) uses the sodium gradient to co-transport two Na⁺ with one I⁻, generating a 20- to 40-fold iodide gradient; it also transports pertechnetate and perchlorate competitively.",
                ref(
                    "Iodide Metabolism by the Thyroid Cell",
                    "The iodide transport system generates an iodide gradient of 20 to 40 across the cell membrane, and NIS also transports pertechnetate ( $ TcO_4^- $), perchlorate ( $ ClO_4^- $), and thiocyanate (SCN $ ^- $), accounting for the utility of radioactive  $ TcO_4^- $ as a thyroid scanning tool and the capacity of  $ KClO_4^- $ to block iodide uptake as a competitive inhibitor.",
                ),
            ),
            note(
                f"{p}-n6",
                "Iodine transport",
                "Why pendrin matters at the apical membrane",
                "After basolateral NIS uptake, iodide must enter the follicular lumen via pendrin (SLC26A4); biallelic mutations cause Pendred syndrome with deafness, goiter, and partial organification defect.",
                ref(
                    "Iodide Metabolism by the Thyroid Cell",
                    "At the apical membrane, iodide must enter the follicular lumen. This process is thought to involve pendrin, a highly hydrophobic membrane glycoprotein and multianion exchanger located at the apical membrane of thyrocytes.",
                ),
            ),
            note(
                f"{p}-n7",
                "Hormone synthesis",
                "How TPO and DUOX organize iodide on thyroglobulin",
                "DUOX1/2 generate H₂O₂ at the apical membrane; TPO oxidizes iodide and iodinates Tg tyrosines to MIT/DIT, then couples residues to form stored T4 and T3 within colloid.",
                ref(
                    "Iodide Oxidation and Organization",
                    "Oxidation of thyroidal iodide is mediated by the heme-containing protein TPO and requires the  $ H_{2}O_{2} $ generated by the calcium-dependent DUOX1 and DUOX2 enzymes, with DUOX2 being the major contributor as a result of its higher expression levels in the thyroid.",
                ),
            ),
            note(
                f"{p}-n8",
                "Thyroglobulin",
                "Thyroglobulin structure and hormonogenic sites",
                "Human Tg is a ~660-kDa homodimer with only a few acceptor tyrosines (Y24, Y1310, Y2766, Y2573) forming T4/T3; Graves stimulation doubles T3 residues per molecule independent of iodination state.",
                ref(
                    "Iodothyronine Synthesis",
                    "Although 25 to 33 of the tyrosyl residues are iodinated, only residues Y24, Y1310, Y2766, and Y2573 form  $ T_4 $ or  $ T_3 $.",
                ),
            ),
            note(
                f"{p}-n9",
                "Hormone release",
                "How colloid is endocytosed and hormone secreted",
                "TSH stimulates macropinocytosis and micropinocytosis of colloid; lysosomal proteolysis releases T4/T3 while DEHAL1 recycles MIT/DIT iodide; basolateral exit involves MCT8.",
                ref(
                    "Storage and Release of Thyroid Hormone",
                    "The first step in thyroid hormone release is the endocytosis of colloid from the follicular lumen by two processes: macropinocytosis by pseudopods formed at the apical membrane and micropincocytosis by small coated vesicles that form at the apical surface.",
                ),
            ),
            note(
                f"{p}-n10",
                "TSH signaling",
                "Why TSHR couples to both cAMP and PLC pathways",
                "TSHR mainly signals via Gs/cAMP (growth, NIS, Tg, TPO transcription) but at high TSH also couples Gq/11, activating PLC/Ca²⁺ pathways regulating iodide efflux, H₂O₂, and iodination.",
                ref(
                    "Role and Mechanism of Thyrotropin Effects",
                    "When activated by high concentrations of TSH (100 times physiologic levels), it also couples to G $ _{q} $/G $ _{11} $, activating the inositol-phosphate diacylglycerol cascade.",
                ),
            ),
            note(
                f"{p}-n11",
                "Deiodinases",
                "How D1, D2, and D3 shape circulating T3",
                "D1 and D2 outer-ring deiodinate T4 to active T3 (D1 PTU-sensitive, plasma-oriented); D3 inner-ring deiodinates to inactivate T3 and rT3; ~80% of circulating T3 derives from peripheral T4 conversion.",
                ref(
                    "lodothyronine Deiodination",
                    "This reaction is catalyzed by the type 1 and 2 deiodinases (D1 and D2) and is the source of more than 80% of the circulating  $ T_3 $ in humans (see Fig. 9.2).",
                ),
            ),
            note(
                f"{p}-n12",
                "Deiodinases",
                "Why D2 protects brain T3 during iodine deficiency",
                "D2 in CNS, pituitary, and BAT increases when serum T4 falls—ubiquitination slows—maintaining intracellular T3 before plasma T3 drops, explaining early TSH rise in iodine deficiency.",
                ref(
                    "Enzymology and Regulation of the Selenodeiodinases",
                    "For this reason, D2 has principally been thought of as an enzyme that provides intracellular  $ T_3 $, but there is increasing evidence that D2 could also contribute to plasma  $ T_3 $.",
                ),
            ),
            note(
                f"{p}-n13",
                "Transport proteins",
                "TBG, TTR, and albumin binding of thyroid hormones",
                "TBG binds ~68% of T4; TTR ~11%; albumin ~20% despite low affinity. TBG changes (estrogen, illness) alter total T4/T3 while free hormone is defended by feedback.",
                ref(
                    "Thyroxine-Binding Globulin",
                    "Because TBG is the principal  $ T_{4} $- and  $ T_{3} $-binding protein, changes in TBG or its binding are paralleled by changes in total plasma  $ T_{4} $ and  $ T_{3} $ even though  $ T_{4} $ and  $ T_{3} $ production is little changed.",
                ),
            ),
            note(
                f"{p}-n14",
                "Transport",
                "How MCT8 deficiency causes Allan-Herndon-Dudley syndrome",
                "MCT8 mutations cause severe neurologic disability with high serum T3: tissues using other transporters are hyperthyroid while MCT8-dependent brain is hypothyroid—a coexistence of excess and deprivation.",
                ref(
                    " $ T_{4} $ and  $ T_{3} $ Transport Across Cell Membranes and Intracellular  $ T_{3} $ Binding",
                    "Coexistence of thyroid hormone excess and deprivation in different tissues is a distinct characteristic of this syndrome.",
                ),
            ),
            note(
                f"{p}-n15",
                "Receptors",
                "TR alpha/beta and resistance to thyroid hormone",
                "TRβ2 in pituitary mediates feedback; THRB mutations cause RTHβ with elevated T4/T3 and inappropriately normal/elevated TSH plus tissue-selective hypo- and hyperthyroid features.",
                ref(
                    "Mechanism of Thyroid Hormone Action",
                    "RTH is usually dominantly inherited and characterized by resistance to thyroid hormone in tissues predominantly expressing TR $ \\beta $ (e.g., the liver and the pituitary) but is associated with signs of thyrotoxicosis in tissues with predominant expression of TR $ \\alpha $ (e.g., the heart).",
                ),
            ),
            note(
                f"{p}-n16",
                "HPT axis",
                "Log-linear TSH–free T4 relationship",
                "Serum TSH is an exquisitely sensitive inverse log-linear function of free T4, making TSH the preferred screening test when the hypothalamic-pituitary axis is intact.",
                ref(
                    "Thyrotropin Synthesis and Secretion",
                    "There is a linear inverse relationship between the serum free  $ T_4 $ concentration and the log of the TSH (Fig. 9.11), making the serum TSH concentration an exquisitely sensitive indicator of the thyroid state of patients with an intact hypothalamic-pituitary axis.",
                ),
            ),
            note(
                f"{p}-n17",
                "HPT axis",
                "How TRH regulates thyrotroph TSH secretion",
                "Parvocellular PVN TRH travels via portal vessels to thyrotrophs; T3 suppresses prepro-TRH mRNA and blocks TRH-stimulated TSH release—feedback requires both circulating T3 and local T4→T3 conversion in tanycytes.",
                ref(
                    "Thyrotropin-Releasing Hormone Synthesis and Secretion",
                    "In addition to inhibiting the synthesis of prepro-TRH mRNA, thyroid hormone also blocks the capacity of TRH to stimulate TSH release from the thyrotroph.",
                ),
            ),
            note(
                f"{p}-n18",
                "Iodine excess",
                "Wolff-Chaikoff effect and escape",
                "High intrathyroidal iodide transiently blocks organification; normal glands escape by downregulating NIS, but fetal thyroid, Hashimoto disease, or prior irradiation may develop iodide myxedema without escape.",
                ref(
                    "Effects of Increased Iodine Intake on Thyroid Hormone Synthesis",
                    "This decreasing yield of organic iodine from increasing doses of iodide, termed the Wolff-Chaikoff effect, results from a high concentration of inorganic iodide within the thyroid cell.",
                ),
            ),
            note(
                f"{p}-n19",
                "Iodine deficiency",
                "Compensatory responses to iodine deficiency",
                "Falling T4 raises TSH, increases NIS/TPO/Tg, shifts Tg T4:T3 ratio toward T3, and upregulates CNS D2—maintaining serum T3 until severe deficiency causes hypothyroidism.",
                ref(
                    "Iodine Deficiency",
                    "Because of the decrease in iodide supply and the ratio of DIT to MIT, the ratio of  $ T_4 $ to  $ T_3 $ in Tg decreases, and the rate of thyroidal  $ T_3 $ secretion may increase despite a fall in  $ T_4 $ secretion.",
                ),
            ),
            note(
                f"{p}-n20",
                "Pregnancy",
                "Why pregnancy alters thyroid test interpretation",
                "Estrogen raises TBG so total T4/T3 rise ~1.5-fold; first-trimester hCG mildly stimulates TSHR causing transient low TSH and higher free T4; iodine needs and T4 production increase 20–40%.",
                ref(
                    "Thyroid Function in Pregnancy and in the Fetus and Newborn",
                    "The total serum  $ T_{4} $ and  $ T_{3} $ concentrations rise to levels about 1.5-fold those of nonpregnant women owing to the increase in TBG concentration in the first trimester (Fig. 9.13).",
                ),
            ),
            note(
                f"{p}-n21",
                "Fetal thyroid",
                "Fetal and neonatal thyroid physiology",
                "Fetal TSH exceeds maternal levels; cord T3 is low with high rT3 due to D3; a neonatal TSH surge at 2–4 hours drives T4/T3 into the hyperthyroid range by 24 hours.",
                ref(
                    "Thyroid Function in the Newborn",
                    "After delivery, the serum TSH level in the neonate increases rapidly to a peak at about 2 to 4 hours after birth, returning to its initial value within 48 hours.",
                ),
            ),
            note(
                f"{p}-n22",
                "Euthyroid sick syndrome",
                "Why illness lowers T3 without primary thyroid disease",
                "Fasting and critical illness reduce D1/D2 activity, increase D3 and rT3, and suppress TRH-TSH—an adaptive energy-sparing low-T3 state termed euthyroid sick syndrome.",
                ref(
                    "Thyroid Function During Fasting or Illness",
                    "This constellation of findings is termed low- $ T_{3} $ syndrome, euthyroid sick syndrome, or nonthyroidal illness.",
                ),
            ),
            note(
                f"{p}-n23",
                "Physical exam",
                "Thyroid examination technique and findings",
                "Inspect during swallowing for movement (distinguishes goiter from other neck masses); palpate lobes against trachea; note consistency, nodules, pyramidal lobe, bruit (Graves), and Pemberton sign for retrosternal goiter.",
                ref(
                    "Physical Examination",
                    "Any masses should be assessed for movement on swallowing, which is a characteristic of the thyroid gland because of its ensheathment in the pretracheal fascia and distinguishes a goiter from most other neck masses.",
                ),
            ),
            note(
                f"{p}-n24",
                "Laboratory testing",
                "Why biotin interferes with thyroid immunoassays",
                "High-dose biotin (common OTC supplement) disrupts streptavidin-biotin assays, causing falsely low TSH and falsely high free T4 and anti-TSHR antibodies—must be suspected in discordant results.",
                ref(
                    "Tests of the Hypothalamic-Pituitary-Thyroid Axis Thyroid-Stimulating Hormone",
                    "This is especially worrisome because high levels of serum biotin can both result in very low TSH levels and artifactually raise the free  $ T_{4} $ measured in robotic assays based on biotin/streptavidin chemistry, as well as causing false-positive measurements of anti-TSHR antibodies (see Chapter 4).",
                ),
            ),
            note(
                f"{p}-n25",
                "RAIU",
                "How RAIU and perchlorate discharge test work",
                "24-hour RAIU (reference ~5–25% in North America) distinguishes hyperthyroidism (high uptake) from thyroiditis/factitia (low). Perchlorate blocks NIS; >10% discharge in 2 hours indicates organification defect.",
                ref(
                    "The Perchlorate Discharge Test",
                    "In patients with Pendred syndrome or with other disorders that inhibit the iodination of tyrosine, such as Hashimoto thyroiditis, or those receiving thiourea drugs, this process is delayed, as shown by the exit (discharge) of more than 10% of the thyroidal radioiodine within 2 hours of administration of 500 mg of  $ KClO_{4} $.",
                ),
            ),
            note(
                f"{p}-n26",
                "Thyroglobulin",
                "Serum thyroglobulin clinical applications",
                "Tg is normally up to ~50 ng/mL; undetectable after total thyroidectomy for cancer signals recurrence when it reappears. Low Tg with low RAIU thyrotoxicosis suggests factitia; anti-Tg antibodies artifactually alter assays.",
                ref(
                    "Serum Thyroglobulin",
                    "Subnormal or undetectable concentrations are found in patients with thyrotoxicosis factitia and aid in differentiating this disorder from other causes of thyrotoxicosis with a low thyroid radioiodine uptake (RAIU).",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Embryology",
                "A newborn has no palpable thyroid but a midline base-of-tongue mass. TSH is markedly elevated. What is the most likely diagnosis?",
                [
                    "Lingual thyroid as the sole functioning thyroid tissue",
                    "Thyroglossal duct cyst without thyroid tissue",
                    "Ectopic mediastinal thyroid with normal neck gland",
                    "Transient neonatal thyrotoxicosis from maternal TRAb",
                ],
                0,
                "Lingual thyroid from thyroglossal duct remnants may be the only functioning thyroid present.",
                ref(
                    "Functional Ontogeny",
                    "Rarely, thyroid tissue may develop from remnants of the thyroglossal duct near the base of the tongue. Such lingual thyroid tissue may be the sole functioning thyroid present.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Iodine transport",
                "A child with congenital hypothyroidism and goiter has a negative perchlorate discharge test at 1 hour but parents report no iodide supplementation. Which defect is most likely?",
                [
                    "Biallelic NIS (SLC5A5) mutation with iodide trapping defect",
                    "Isolated TPO antibody positivity without hypothyroidism",
                    "Activating TSHR mutation causing neonatal thyrotoxicosis",
                    "MCT8 mutation causing elevated serum T3",
                ],
                0,
                "Absent iodide trapping from NIS mutations causes CH with goiter unless large iodide loads are given.",
                ref(
                    "Iodide Metabolism by the Thyroid Cell",
                    "That the iodide-concentrating mechanism is required for normal thyroid function has been known for decades in that its absence is associated with congenital hypothyroidism and goiter unless large quantities of inorganic iodide are provided.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Hormone synthesis",
                "A neonate with goiter, elevated TSH, and partial organification on perchlorate testing also has sensorineural deafness. Which gene is most likely mutated?",
                [
                    "SLC26A4 (pendrin)",
                    "THRB",
                    "MCT8 (SLC16A2)",
                    "SECISBP2",
                ],
                0,
                "Pendred syndrome combines deafness, goiter, and partial iodide organification from SLC26A4 mutations.",
                ref(
                    "Iodide Metabolism by the Thyroid Cell",
                    "Mutations in the SLC26A4 gene lead to Pendred syndrome, an autosomal-recessive disorder characterized by sensorineural deafness, goiter, and a partial defect in iodide organization.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Hormone synthesis",
                "A patient with permanent congenital hypothyroidism and goiter is found to have biallelic DUOX2 mutations. Which mechanism is impaired?",
                [
                    "Apical H₂O₂ generation required for TPO-catalyzed iodination",
                    "Basolateral iodide trapping by NIS",
                    "MCT8-mediated hormone export",
                    "Pituitary TRH synthesis",
                ],
                0,
                "DUOX2 provides thyroidal H₂O₂ for TPO; DUOX2 mutations cause goitrous CH.",
                ref(
                    "Iodide Oxidation and Organization",
                    "They are  $ Ca^{2+} $, NADPH-dependent oxidases that catalyze the formation of the  $ H_{2}O_{2} $ required for TPO-catalyzed Tg iodination.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Deiodinases",
                "A patient with Graves disease starts propylthiouracil rather than methimazole. Which effect explains the more rapid fall in serum T3?",
                [
                    "PTU inhibits D1-catalyzed peripheral T4-to-T3 conversion",
                    "PTU blocks TSH secretion from the pituitary",
                    "PTU stimulates thyroidal D3 activity",
                    "PTU increases TBG synthesis",
                ],
                0,
                "PTU inhibits D1 (not D2/D3), reducing extrathyroidal T3 production especially when thyroidal D1 is upregulated in thyrotoxicosis.",
                ref(
                    "Storage and Release of Thyroid Hormone",
                    "An inhibition of the D1-catalyzed  $ T_4 $-to- $ T_3 $ conversion may contribute to the rapid effect of PTU to reduce circulating  $ T_3 $ in patients with Graves disease (see Chapter 10).",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Transport",
                "A boy with developmental delay, elevated serum T3, low-normal T4, and normal TSH is evaluated. Which treatment targets peripheral thyrotoxicosis while brain remains T3-deprived?",
                [
                    "PTU with levothyroxine or TRIAC/DITPA trials",
                    "High-dose methimazole alone without levothyroxine",
                    "Radioactive iodine ablation of the thyroid",
                    "Levothyroxine suppression of TSH to undetectable levels",
                ],
                0,
                "MCT8 deficiency causes peripheral hyperthyroidism and CNS hypothyroidism; combined PTU plus T4 analogues that bypass MCT8 have been used.",
                ref(
                    " $ T_{4} $ and  $ T_{3} $ Transport Across Cell Membranes and Intracellular  $ T_{3} $ Binding",
                    "PTU combined with  $ L-T_{4} $ $ ^{84} $ and a thymimetic compound, diiodothyropropionic acid (DITPA), which is not dependent on MCT8 for cellular entry, have been used to treat several patients harboring MCT8 gene mutations, and recent data show promising results for TRIAC treatment in ameliorating anthropomorphic parameters and peripheral thyrotoxicity across all age categories.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Receptors",
                "A patient has goiter, tachycardia, elevated free T4 and T3, and TSH 6 mU/L (inappropriately normal). Pituitary MRI is normal. What is the leading diagnosis?",
                [
                    "Resistance to thyroid hormone β (THRB mutation)",
                    "TSH-secreting pituitary adenoma",
                    "Primary hypothyroidism with assay artifact",
                    "Central hypothyroidism from TRH deficiency",
                ],
                0,
                "Elevated thyroid hormones with non-suppressed TSH suggests RTHβ or TSHoma; normal MRI favors RTHβ.",
                ref(
                    "TSH in Patients With Thyroid Dysfunction",
                    "An elevation in both serum TSH and free  $ T_{4} $ is unusual and indicates either autonomous TSH production due to a TSH-secreting pituitary tumor, resistance to thyroid hormone  $ \\beta $ (RTH $ \\beta $), or hyperthyroidism with an artifactual elevation in TSH.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Iodine",
                "A euthyroid patient with multinodular goiter receives IV iodinated contrast for CT. Two weeks later TSH is 28 mU/L and free T4 is low. What mechanism is most likely?",
                [
                    "Wolff-Chaikoff effect with failure to escape in a nodular gland",
                    "Acute subacute thyroiditis with hormone leak",
                    "Factitious thyrotoxicosis from levothyroxine",
                    "Gestational hCG-mediated TSH suppression",
                ],
                0,
                "Excess iodine can cause transient organification block; susceptible glands may develop iodide myxedema without escape.",
                ref(
                    "Effects of Increased Iodine Intake on Thyroid Hormone Synthesis",
                    "The susceptibility to the Wolff-Chaikoff effect can be increased either by stimulation of iodide trapping, as occurs in patients with Graves disease, or during persistent TSH stimulation by impairment of iodine organization in the human fetus, in patients with Hashimoto disease, or in thyroids previously irradiated by either  $ ^{131} $I or external beam therapy.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Pregnancy",
                "At 9 weeks gestation a woman has suppressed TSH (0.05 mU/L) and high-normal free T4 without symptoms. TRAb is negative. What is the most likely explanation?",
                [
                    "Physiologic hCG-mediated TSHR stimulation",
                    "Graves disease requiring methimazole",
                    "Primary hypothyroidism with assay error",
                    "Iodine-induced thyrotoxicosis from contrast dye",
                ],
                0,
                "First-trimester hCG can partially stimulate TSHR causing transient gestational thyrotoxicosis with low TSH.",
                ref(
                    "Thyroid Function in Pregnancy and in the Fetus and Newborn",
                    "hCG cross-reacts with the TSHR, which results in a small and transient increase in free  $ T_{4} $ levels near the end of the first trimester (peak circulating hCG), resulting in a partial TSH suppression.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Illness",
                "An ICU patient with sepsis has TSH 0.2 mU/L, low total T4, low T3, and elevated rT3. Which statement is most accurate?",
                [
                    "This pattern reflects euthyroid sick syndrome, not primary hyperthyroidism",
                    "The patient requires immediate high-dose levothyroxine",
                    "TSH suppression proves autonomous thyroid hormone excess",
                    "Free T4 must be elevated confirming thyrotoxicosis",
                ],
                0,
                "Critical illness commonly suppresses TSH and lowers T3 with elevated rT3—the nonthyroidal illness pattern.",
                ref(
                    "Causes of a Subnormal or Suppressed TSH",
                    "In severe illnesses, with or without dopamine infusion or excess glucocorticoid, TSH is suppressed, making assessment of thyroid functional status difficult (see earlier discussion).",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Physical exam",
                "A patient with diffuse goiter has a systolic bruit over the thyroid and tachycardia. Cardiac exam is otherwise normal. What diagnosis is most suggested?",
                [
                    "Graves disease with markedly increased thyroid blood flow",
                    "Hashimoto thyroiditis in hypothyroid phase",
                    "Thyroglossal duct cyst",
                    "Medullary thyroid carcinoma",
                ],
                0,
                "Thyroid bruit in the absence of cardiac disease suggests hypervascular Graves goiter.",
                ref(
                    "Physical Examination",
                    "Auscultation of the neck may confirm the increased vascularity of an enlarged, hyperactive gland, suggesting Graves disease.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Laboratory",
                "A woman on high-dose biotin for hair growth has TSH <0.01 mU/L and elevated free T4 by immunoassay but is clinically euthyroid. What is the best next step?",
                [
                    "Stop biotin and repeat thyroid tests after washout",
                    "Start methimazole for presumed Graves disease",
                    "Order RAIU immediately without stopping biotin",
                    "Treat as central hypothyroidism with levothyroxine",
                ],
                0,
                "Biotin interferes with streptavidin-based assays causing spurious thyrotoxic biochemistry.",
                ref(
                    "Causes of a Subnormal or Suppressed TSH",
                    "As mentioned, patients with few or no symptoms of thyrotoxicosis and subnormal TSH and high free  $ T_{4} $ values should be questioned regarding biotin ingestion.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Laboratory",
                "A hypothyroid patient on levothyroxine has elevated TSH and elevated free T4 on the same sample. What explanation should be considered first?",
                [
                    "Intermittent noncompliance with levothyroxine (lab caught a post-dose spike)",
                    "RTHβ requiring no change in therapy",
                    "TSH-secreting adenoma requiring surgery",
                    "MCT8 deficiency requiring PTU",
                ],
                0,
                "Poor compliance with intermittent large levothyroxine doses can produce elevated TSH and free T4 together.",
                ref(
                    "Causes of an Elevated TSH",
                    "In patients on substitution therapy with levothyroxine, an elevated TSH with a concomitant increase in the free  $ T_4 $ may reflect poor compliance with levothyroxine treatment.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Autoantibodies",
                "A patient with hyperthyroidism has positive TPO-Ab. Which statement about these antibodies is correct?",
                [
                    "They are common in Graves disease reflecting associated thyroiditis but do not alone confirm Graves",
                    "TPO-Ab always cause hyperthyroidism directly",
                    "TPO-Ab are absent in Hashimoto thyroiditis",
                    "Low-level TPO-Ab never occur in euthyroid individuals",
                ],
                0,
                "TPO-Ab occur in 50–80% of Graves patients from associated lymphocytic infiltration; TSHR-Ab testing is needed for etiology.",
                ref(
                    "Thyroid Autoantibodies in Hashimoto Thyroiditis and Graves Disease",
                    "Tg-Ab and TPO-Ab are also detectable in 50% to 90% of patients with Graves disease, indicative of the associated thyroiditis that is evident histologically as a heterogeneous lymphocytic infiltration.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Thyroglobulin",
                "After total thyroidectomy and RAI for papillary cancer, stimulated Tg rises from undetectable to 8 ng/mL. What does this most likely indicate?",
                [
                    "Persistent or recurrent differentiated thyroid carcinoma",
                    "Successful ablation with no residual tissue",
                    "Factitious thyrotoxicosis",
                    "Physiologic neonatal Tg elevation",
                ],
                0,
                "After total ablation, reappearance of measurable Tg typically signifies persistent/recurrent disease.",
                ref(
                    "Serum Thyroglobulin",
                    "After total thyroid ablation for papillary or follicular thyroid carcinoma, Tg should not be detectable, and its subsequent appearance typically signifies the presence of persistent or recurrent disease.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "RAIU",
                "A thyrotoxic patient has RAIU 2% at 24 hours. Tg is undetectable. Which diagnosis is most likely?",
                [
                    "Thyrotoxicosis factitia from exogenous hormone",
                    "Graves disease",
                    "Toxic multinodular goiter",
                    "Iodine-deficient hyperthyroidism",
                ],
                0,
                "Low RAIU with low Tg in thyrotoxicosis points to exogenous hormone rather than thyroiditis (Tg elevated) or hyperthyroidism (high RAIU).",
                ref(
                    "Exogenous Thyroid Hormone: Thyrotoxicosis Factitia",
                    "The low level of Tg in serum differentiates thyrotoxicosis (factitia) from other causes of thyrotoxicosis with decreased RAIU.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "RAIU",
                "A patient with thyrotoxicosis has RAIU 35% and diffuse uptake. TSH is suppressed. Which etiology is most likely?",
                [
                    "Endogenous hyperthyroidism such as Graves disease",
                    "Subacute thyroiditis in the hyperthyroid phase",
                    "Exogenous levothyroxine ingestion",
                    "Amiodarone-induced destructive thyroiditis only",
                ],
                0,
                "Elevated RAIU indicates endogenous hormone synthesis as in hyperthyroidism; thyroiditis and factitia show low uptake.",
                ref(
                    "States Associated With Decreased RAIU",
                    "Therefore, the major indication for measuring the RAIU is to establish whether thyrotoxicosis is due to hyperthyroidism (high RAIU) or thyroiditis (low RAIU).",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Dynamic tests",
                "A patient has elevated T4/T3 and non-suppressed TSH. TRH stimulation shows blunted TSH rise; T3 suppression fails to lower TSH. MRI shows a pituitary lesion. What is the diagnosis?",
                [
                    "TSH-secreting pituitary adenoma (TSHoma)",
                    "RTHβ with exuberant TRH response",
                    "Primary hypothyroidism",
                    "Gestational thyrotoxicosis",
                ],
                0,
                "TSHoma shows blunted TRH response and no TSH suppression after T3; RTHβ shows preserved/exuberant TRH response.",
                ref(
                    "T $ _{3} $ Suppression Test and Response to Somatostatin Analogues",
                    "A partial inhibition of basal TSH secretion after T₃ suppression (80–100 µg/day divided into 3 administrations for 10 days, sampling at 0, 5, and 10 days) is seen in most patients with RTHβ, whereas basal TSH usually remains unsuppressed in TSHomas.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Binding proteins",
                "A euthyroid man has total T4 180 nmol/L (high) and normal free T4 by equilibrium dialysis. Family members have similar pattern. What is the diagnosis?",
                [
                    "Familial dysalbuminemic hyperthyroxinemia",
                    "TBG deficiency",
                    "Primary hyperthyroidism",
                    "MCT8 deficiency",
                ],
                0,
                "FDH causes high total T4 (or T3) with normal free hormone and euthyroidism—risk of erroneous treatment if unrecognised.",
                ref(
                    "Albumin",
                    "Both are dominantly inherited and characterized by a high concentration of total  $ T_{4} $ or  $ T_{3} $ (FDH). However, the free hormone concentrations remain normal, and the patients are euthyroid.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Screening",
                "An asymptomatic adult has TSH 8 mU/L and normal free T4. Which management approach aligns with guideline principles in this chapter?",
                [
                    "Confirm abnormality, assess clinical context, and document hormones before treating",
                    "Start levothyroxine immediately based on TSH alone",
                    "Assume euthyroidism because free T4 is normal—no follow-up",
                    "Order TRH test as mandatory first step",
                ],
                0,
                "TSH is indirect; abnormal screening requires confirmation and hormone documentation before therapy.",
                ref(
                    "Causes of an Elevated TSH",
                    "Despite the utility and general efficacy of the serum TSH measurement alone as a screening tool for identifying patients with thyroid dysfunction, a patient should not receive treatment solely on the basis of an abnormal TSH.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Central hypothyroidism",
                "A patient post pituitary surgery has low free T4 and TSH 4.2 mU/L (reference 0.4–4.2). What explains the pattern?",
                [
                    "Central hypothyroidism with poorly bioactive glycosylated TSH",
                    "Subclinical primary hyperthyroidism",
                    "RTHβ with elevated thyroid hormones",
                    "Acute illness euthyroid sick syndrome only",
                ],
                0,
                "Hypothalamic-pituitary hypothyroidism may show low/normal TSH that is immunoreactive but biologically inactive.",
                ref(
                    "TSH in Patients With Thyroid Dysfunction",
                    "In contrast, patients with hypothalamic or pituitary hypothyroidism can have low, normal, or even slightly elevated serum TSH levels. The circulating TSH in this situation generally has reduced biologic activity as a result of abnormal glycosylation, reflecting the impaired action of TRH at the level of the thyrotroph.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Iodine deficiency",
                "In an iodine-deficient region, a woman has TSH 15 mU/L, low T4, but normal T3. Which compensatory mechanism best explains preserved T3?",
                [
                    "Increased thyroidal and peripheral D2-mediated T4-to-T3 conversion",
                    "Complete shutdown of all deiodinases",
                    "MCT8 overexpression in liver only",
                    "Wolff-Chaikoff block of all hormone release",
                ],
                0,
                "Iodine deficiency upregulates D2 and shifts Tg production toward T3 to conserve iodine.",
                ref(
                    "Iodine Deficiency",
                    "In the rat model, the fall in plasma  $ T_4 $ increases D2 from 5- to 20-fold in the CNS, hypothalamus, and pituitary, increasing the efficiency of  $ T_4 $ conversion to  $ T_3 $.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Drugs",
                "A patient on amiodarone has high T4, normal T3, and mildly elevated TSH that later normalizes. What is the mechanism?",
                [
                    "Amiodarone inhibits D1/D2 deiodination and hepatic T4 transport",
                    "Amiodarone stimulates thyroid autoimmunity only",
                    "Amiodarone increases TBG to cause true hyperthyroidism",
                    "Amiodarone blocks TSHR permanently",
                ],
                0,
                "Amiodarone structurally resembles T4, inhibits deiodination and hepatocyte transport, raising T4 while T3 is maintained.",
                ref(
                    "Pharmacologic Agents Inhibiting Thyroid Hormone Deiodination",
                    "The antiarrhythmic drug amiodarone shares sufficient structural similarity with  $ T_4 $ that it can inhibit deiodination of  $ T_4 $ and  $ rT_3 $ by D1 and by D2 (Fig. 9.8).",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Neonatal",
                "A premature infant has low T4, low T3, and blunted TSH surge at 24 hours. Which factor contributes?",
                [
                    "Immature HPT axis and illness-related changes resembling euthyroid sick syndrome",
                    "Maternal hCG causing thyrotoxicosis",
                    "Excess iodine from contrast only",
                    "RTHβ from THRB mutation",
                ],
                0,
                "Preterm infants have immature thyroid/HPT function and illness can mimic low-T3 sick syndrome.",
                ref(
                    "Thyroid Function in the Newborn",
                    "Premature infants have an immature HPT axis with low  $ T_4 $,  $ T_3 $, and TSH.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Autoimmunity",
                "When monitoring TPO-Ab titers longitudinally in a patient, what practice is recommended?",
                [
                    "Use the same commercial assay consistently because standardization varies between kits",
                    "Switch assays each visit to average results",
                    "TPO-Ab need not be standardized—any method is equivalent",
                    "Only measure Tg-Ab because TPO-Ab are never clinically useful",
                ],
                0,
                "Despite standardization efforts, commercial TPO/Tg antibody assays vary—consistency is required for serial comparison.",
                ref(
                    "Autoantibodies to Thyroid Peroxidase and Thyroglobulin",
                    "Hence, when monitoring antibody titers (e.g., measuring Tg-Ab after the treatment of thyroid cancer), it is always best to use the same autoantibody assay consistently.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Perchlorate",
                "A patient on methimazole has 15% thyroidal radioiodine discharge 2 hours after potassium perchlorate. What does this indicate?",
                [
                    "Delayed organification consistent with thionamide effect or organification defect",
                    "Normal trapping with complete organification",
                    "Excess iodine intake only—no organification problem",
                    "MCT8 transport defect",
                ],
                0,
                "Discharge >10% after perchlorate indicates trapped iodide was not promptly organified.",
                ref(
                    "The Perchlorate Discharge Test",
                    "In patients with Pendred syndrome or with other disorders that inhibit the iodination of tyrosine, such as Hashimoto thyroiditis, or those receiving thiourea drugs, this process is delayed, as shown by the exit (discharge) of more than 10% of the thyroidal radioiodine within 2 hours of administration of 500 mg of  $ KClO_{4} $.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Phylogeny",
                "Recognizable thyroid tissue is present in all vertebrates but not in invertebrates.",
                True,
                "Thyroid tissue is confined to vertebrates; invertebrates may have MIT/DIT without thyroid glands.",
                ref(
                    "Phylogeny",
                    "Thyroid tissue is confined to, and is present in, all vertebrates.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Iodine",
                "The thyroid contains the largest pool of body iodine under normal circumstances.",
                True,
                "The thyroid holds ~8000 µg iodine, mostly as DIT/MIT, far exceeding the extracellular pool.",
                ref(
                    "Dietary Iodine",
                    "The thyroid contains the largest pool of body iodine, under normal circumstances approximately 8000 µg, most of which is in the form of DIT and MIT.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "TSHR",
                "The unliganded TSH receptor displays constitutive activity unlike LH/CG receptors.",
                True,
                "Wild-type TSHR has basal signaling not shared by closely related gonadotropin receptors.",
                ref(
                    "Role and Mechanism of Thyrotropin Effects",
                    "Remarkably, the wild-type TSHR itself displays constitutive activity, a phenomenon that is not shared by the closely related receptors for luteinizing hormone/chorionic gonadotropin (LH/CG) and follicle-stimulating hormone (FSH).",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Deiodinases",
                "Type 2 deiodinase is inhibited by propylthiouracil.",
                False,
                "PTU inhibits D1; D2 and D3 are PTU-insensitive.",
                ref(
                    "Enzymology and Regulation of the Selenodeiodinases",
                    "D1 is inhibited by PTU, unlike D2 or D3.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Transport",
                "Congenital TBG deficiency in males causes complete absence of TBG protein.",
                True,
                "TBG deficiency occurs in 1/5000 newborns with absent protein in affected males.",
                ref(
                    "Thyroxine-Binding Globulin",
                    "Congenital deficiency of TBG is common, occurring in 1/5000 newborns, and is associated with the complete absence of the protein in males.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Receptors",
                "TRβ2 is predominantly expressed in pituitary thyrotrophs and is essential for HPT feedback.",
                True,
                "TRβ2 in pituitary and hypothalamus mediates negative feedback on the thyroid axis.",
                ref(
                    "Mechanism of Thyroid Hormone Action",
                    "TR $ \\beta_2 $ is predominantly expressed in the hypothalamus and the pituitary thyrotrophs and thus is essential for negative feedback regulation and control of the thyroid axis.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Pregnancy",
                "Chronic high iodine intake during the third trimester is safe because the fetal thyroid can escape the Wolff-Chaikoff effect.",
                False,
                "Escape does not occur in third-trimester fetus—excess iodine can cause fetal hypothyroidism and goiter.",
                ref(
                    "Effects of Increased Iodine Intake on Thyroid Hormone Synthesis",
                    "Importantly, it does not occur in the third-trimester fetus; hence, chronic high iodine intake during pregnancy must be avoided because it will cause fetal hypothyroidism and a compensatory, potentially obstructive goiter in the newborn (Fig. 9.12).",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Illness",
                "Most controlled studies show clear mortality benefit from T4 or T3 supplementation in euthyroid sick syndrome.",
                False,
                "Routine thyroid hormone supplementation in low-T3 syndrome has not shown benefit except limited cardiac surgery data.",
                ref(
                    "Thyroid Function During Fasting or Illness",
                    "Even with such alterations in thyroid hormone status, most controlled studies have not shown beneficial effects of  $ T_4 $ or  $ T_3 $ supplementation.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Laboratory",
                "A minimally suitable TSH assay should quantify 0.1 mU/L with CV <20%.",
                True,
                "Sensitive TSH assays need functional sensitivity to 0.1 mU/L for subclinical disease detection.",
                ref(
                    "Tests of the Hypothalamic-Pituitary-Thyroid Axis Thyroid-Stimulating Hormone",
                    "A minimally suitable TSH assay should be able to quantitate concentrations of TSH of 0.1 mU/L with a coefficient of variation of less than 20%.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Autoantibodies",
                "TPO antibodies are thought to be the primary cause of Hashimoto thyroiditis rather than a secondary response to injury.",
                False,
                "Tg-Ab and TPO-Ab appear secondary to thyroid injury though they may contribute to chronicity.",
                ref(
                    "Do Thyroglobulin and Thyroid Peroxidase Antibodies Have a Pathogenic Role?",
                    "Tg-Abs and TPO-Abs appear to be a secondary response to thyroid injury and are not thought to cause disease themselves.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "RAIU",
                "RAIU testing should not be performed in pregnant or breastfeeding women.",
                True,
                "Radioiodine exposure is contraindicated in pregnancy and lactation.",
                ref(
                    "Radioiodine Uptake",
                    "However, it should not be performed in pregnant and breastfeeding women.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Hormone release",
                "Pharmacologic iodide can rapidly inhibit thyroid hormone release, useful in thyroid storm preparation.",
                True,
                "Iodide inhibits hormone release distinct from organification block, improving severe hyperthyroidism quickly.",
                ref(
                    "Effects on Thyroid Hormone Release",
                    "An important practical effect of pharmacologic doses of iodide is the prompt inhibition of thyroid hormone release.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Dynamic tests",
                "Intravenous TRH testing is widely available for TSHoma diagnosis in the United States.",
                False,
                "TRH is not available in countries including the United States, limiting this dynamic test.",
                ref(
                    "TRH Test (Not Available in All Countries)",
                    "A limitation consists of the fact that TRH is not available in countries such as the United States.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Iodine transport",
                "Assertion: Perchlorate can block thyroid radioiodine uptake on scanning.",
                "Reason: NIS transports perchlorate as well as iodide and pertechnetate.",
                0,
                "Both true—perchlorate competes at NIS, explaining its use as uptake inhibitor and in discharge testing.",
                ref(
                    "Iodide Metabolism by the Thyroid Cell",
                    "NIS also transports pertechnetate ( $ TcO_4^- $), perchlorate ( $ ClO_4^- $), and thiocyanate (SCN $ ^- $), accounting for the utility of radioactive  $ TcO_4^- $ as a thyroid scanning tool and the capacity of  $ KClO_4^- $ to block iodide uptake as a competitive inhibitor.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Hormone storage",
                "Assertion: Antithyroid drugs can be given for weeks before serum T4 falls significantly.",
                "Reason: The thyroid stores weeks of hormone with ~1% daily turnover.",
                0,
                "Both true—the large colloid reservoir buffers circulating T4 during synthesis blockade.",
                ref(
                    "Storage and Release of Thyroid Hormone",
                    "In normal humans, the administration of antithyroid agents for as long as 2 weeks has little effect on serum  $ T_4 $ concentrations.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Deiodinases",
                "Assertion: PTU lowers serum T3 faster than methimazole in Graves disease.",
                "Reason: PTU inhibits thyroidal D2 deiodination of T4.",
                2,
                "Assertion is true; reason is false—PTU inhibits D1, not D2; D3 is also PTU-resistant.",
                ref(
                    "Enzymology and Regulation of the Selenodeiodinases",
                    "D1 is inhibited by PTU, unlike D2 or D3.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Free hormone",
                "Assertion: Free T4 concentration determines the metabolic thyroid state.",
                "Reason: Bound hormone in plasma is the primary mediator of tissue effects.",
                2,
                "Assertion reflects the free hormone hypothesis; reason is false—bound hormone acts as a reservoir; free hormone enters tissues.",
                ref(
                    "Free Thyroid Hormones",
                    "It is the free hormone that is available to the tissues for cellular uptake, deiodination to form active  $ T_3 $ or inactive  $ rT_3 $, and hormone action, including feedback to the hypothalamus and pituitary.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "MCT8",
                "Assertion: MCT8-null mice reproduce the severe neurologic phenotype of human AHDS.",
                "Reason: Mice compensate at the blood-brain barrier with Oatp1c1 when MCT8 is absent.",
                1,
                "Assertion is false in mice; reason is true—Oatp1c1 explains the species discrepancy.",
                ref(
                    " $ T_{4} $ and  $ T_{3} $ Transport Across Cell Membranes and Intracellular  $ T_{3} $ Binding",
                    "The discrepancy with the human phenotype is now explained by the fact that mice express Oatp1c1 at the blood-brain barrier, which compensates for the lack of transport by MCT8.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "RTH",
                "Assertion: Patients with RTHβ may have tachycardia despite elevated TSH.",
                "Reason: RTHβ causes uniform resistance to thyroid hormone in all tissues including heart.",
                2,
                "Assertion is true (cardiac TRα effects); reason is false—RTHβ affects TRβ-predominant tissues; heart expresses TRα causing thyrotoxic signs.",
                ref(
                    "Mechanism of Thyroid Hormone Action",
                    "RTH is usually dominantly inherited and characterized by resistance to thyroid hormone in tissues predominantly expressing TR $ \\beta $ (e.g., the liver and the pituitary) but is associated with signs of thyrotoxicosis in tissues with predominant expression of TR $ \\alpha $ (e.g., the heart).",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Iodine excess",
                "Assertion: Jod-Basedow phenomenon can occur when iodine is given to iodine-deficient patients with nodular goiter.",
                "Reason: Excess iodine always causes permanent Wolff-Chaikoff hypothyroidism in all adults.",
                2,
                "Assertion is plausible in susceptible glands; reason overstates—Wolff-Chaikoff is transient with escape in normal thyroids, while excess iodine can also trigger hyperthyroidism in nodular glands.",
                ref(
                    "Effects of Increased Iodine Intake on Thyroid Hormone Synthesis",
                    "In normal subjects given iodide, the inhibition of iodothyronine formation is reversible over time.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Pregnancy",
                "Assertion: Pregnant women with hypothyroidism often need increased levothyroxine dose.",
                "Reason: Estrogen increases TBG requiring higher T4 production to maintain free hormone.",
                0,
                "Both true—TBG expansion and increased T4 turnover raise requirements 20–40% in pregnancy.",
                ref(
                    "Gonadal Steroids",
                    "Estrogen also increases the levothyroxine requirement in patients with primary hypothyroidism.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Illness",
                "Assertion: Recovery from critical illness may show transient TSH elevation above normal.",
                "Reason: TSH elevation during recovery always indicates permanent primary hypothyroidism.",
                2,
                "Assertion is true during recovery phase; reason is false—transient TSH rise can mimic hypothyroidism before normalization.",
                ref(
                    "Thyroid Function During Fasting or Illness",
                    "Although serum TSH concentrations in severely ill patients are reduced, an increase in TSH above the normal range may appear during recovery, with the elevation in TSH concentration persisting until circulating free  $ T_4 $ and  $ T_3 $ levels return to normal.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Screening",
                "Assertion: Normal TSH alone cannot exclude all thyroid disorders.",
                "Reason: Central hypothyroidism and some hormone action defects may present with normal TSH.",
                0,
                "Both true—the chapter mandates full hormone profiling when clinical suspicion remains despite normal TSH.",
                ref(
                    "Causes of an Elevated TSH",
                    "Additionally, euthyroidism should not be assumed in cases where TSH alone is normal because thyroid dysfunction may exist with normal TSH (e.g., central hypothyroidism, disorders of thyroid hormone action such as  $ RTH\\alpha $,  $ RTH\\beta $, SECISBP2, or MCT8 deficiency).",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Thyroglobulin",
                "Assertion: Serum Tg is useful for detecting recurrence after total thyroidectomy for differentiated cancer.",
                "Reason: Tg elevation reliably distinguishes benign from malignant thyroid nodules at initial diagnosis.",
                1,
                "Assertion is true for surveillance post-ablation; reason is false—Tg does not distinguish benign from malignant nodules at diagnosis.",
                ref(
                    "Serum Thyroglobulin",
                    "Serum Tg concentrations are increased in patients with both benign and differentiated malignant follicular cell-derived tumors of the thyroid and do not serve to distinguish between the two.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Dynamic tests",
                "Assertion: T3 suppression test can help distinguish TSHoma from RTHβ.",
                "Reason: Long-acting somatostatin analogues lower free T4 in RTHβ but not in TSHoma.",
                2,
                "Assertion is true; reason reverses the pattern—somatostatin analogues lower hormones in TSHoma, not RTHβ.",
                ref(
                    "T $ _{3} $ Suppression Test and Response to Somatostatin Analogues",
                    "Chronic administration of long-acting somatostatin analogues (20–30 mg intramuscular [IM] every 28 days for 2–4 months, with preinjection sampling at 0 and every 28 days) usually causes a decrease of free T₄ and free T₃ levels in TSHomas, whereas patients with RTHβ do not respond.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "9",
        "title": "Thyroid Pathophysiology and Diagnostic Evaluation",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Domenico Salvatore, Nadia Schoenmakers, Ronald Cohen, Peter A. Kopp",
        "sourceFile": "williams_2024_chapters/williams_2024_chapter_09_Thyroid_Pathophysiology_and_Diagnostic_Evaluation.md",
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
