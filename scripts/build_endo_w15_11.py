#!/usr/bin/env python3
"""Generate Williams 15e module w15-11 — Hypothyroidism and Thyroiditis."""
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
OUT_NAME = "w15-11_Hypothyroidism_and_Thyroiditis.json"


def build() -> dict:
    p = "w15-11"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Epidemiology",
                "Why autoimmunity dominates hypothyroidism in iodine-sufficient regions",
                "Over 90% of noniatrogenic hypothyroidism in iodine-sufficient areas is autoimmune; environmental factors likely contribute to the rising prevalence alongside genetic susceptibility.",
                ref(
                    "KEY POINTS",
                    "Autoimmunity is responsible for over 90% of noniatrogenic hypothyroidism in iodine-sufficient areas.",
                ),
            ),
            note(
                f"{p}-n2",
                "Hashimoto thyroiditis",
                "Hashimoto and atrophic autoimmune hypothyroidism",
                "Hashimoto thyroiditis causes goiter in iodine-sufficient regions; atrophic thyroiditis (primary myxedema) presents as hypothyroidism without goiter. TPO and thyroglobulin antibodies are present in almost all patients.",
                ref(
                    "Autoimmune Hypothyroidism",
                    "Hashimoto thyroiditis is the common cause of goiter in iodine-sufficient regions; atrophic thyroiditis (primary myxedema) presents as hypothyroidism without a goiter.",
                ),
            ),
            note(
                f"{p}-n3",
                "Subclinical hypothyroidism",
                "Why TSH magnitude and TPOAb predict progression to overt disease",
                "Progression from subclinical to overt hypothyroidism is most closely tied to how high TSH is and whether anti-TPO antibodies are present—rates of 3–8% per year, higher when TSH exceeds 10 mU/L.",
                ref(
                    "KEY POINTS",
                    "The risk of progression from subclinical to overt hypothyroidism is most closely related to the magnitude of serum thyrotropin (thyroid-stimulating hormone [TSH]) elevation and the presence of antithyroid peroxidase (TPO) antibodies.",
                ),
            ),
            note(
                f"{p}-n4",
                "Subclinical hypothyroidism",
                "Subclinical hypothyroidism definition and prevalence",
                "Subclinical hypothyroidism is elevated TSH with normal free T4; in the United States about 4.3% of adults have this mild phase, which may progress and sometimes benefit from treatment.",
                ref(
                    "Hypothyroidism",
                    "Subclinical hypothyroidism is defined as an elevated serum TSH level with a normal serum FT $ _{4} $ concentration.",
                ),
            ),
            note(
                f"{p}-n5",
                "Laboratory evaluation",
                "How to screen for hypothyroidism in primary care",
                "Start with TSH; add free T4 when suspicion is strong, a goiter is present, or central hypothyroidism is possible. As disease progresses TSH rises first, then free T4 falls, while T3 may remain normal late.",
                ref(
                    "Primary and Central Hypothyroidism",
                    "A strategy for evaluating the patient suspected of hypothyroidism involves a TSH determination (Table 11.1). If the suspicion of hypothyroidism is strong, if a goiter is present, or if central hypothyroidism is part of the differential diagnosis, an  $ FT_{4} $ measurement should be included.",
                ),
            ),
            note(
                f"{p}-n6",
                "Laboratory evaluation",
                "Why distinguishing primary from central hypothyroidism is critical",
                "Low free T4 with normal or low TSH signals central hypothyroidism and should prompt evaluation for other pituitary hormone deficiencies; immunoreactive but biologically weak TSH can occur.",
                ref(
                    "Primary and Central Hypothyroidism",
                    "The differentiation of hypothyroidism due to intrinsic thyroid failure from hypothyroidism due to diminished TSH secretion from hypothalamic or pituitary disease (central or secondary hypothyroidism) is the most critical decision point in this pathway (see Fig. 11.5).",
                ),
            ),
            note(
                f"{p}-n7",
                "Congenital hypothyroidism",
                "Congenital hypothyroidism and neurologic stakes",
                "Neonatal screening identifies primary hypothyroidism in about 1:3000 newborns; deficiency in fetal or early postnatal life causes irreversible neurologic damage if not corrected promptly.",
                ref(
                    "Central and Peripheral Nervous Systems",
                    "If the deficiency is not corrected in early postnatal life, the damage is irreversible.",
                ),
            ),
            note(
                f"{p}-n8",
                "Congenital hypothyroidism",
                "Why early high-dose levothyroxine is mandatory in infants",
                "Infants need 10–15 µg/kg/day levothyroxine to normalize TSH quickly; intellectual outcome depends on how soon adequate treatment begins.",
                ref(
                    "Infants and Children",
                    "In infants with congenital hypothyroidism, the determining factor for eventual intellectual attainment is the age at which adequate treatment with thyroid hormone is begun.",
                ),
            ),
            note(
                f"{p}-n9",
                "Central hypothyroidism",
                "Central hypothyroidism pathophysiology",
                "Central hypothyroidism reflects hypothalamic or pituitary TSH deficiency; because ~10–15% of thyroid function is TSH-independent, it is usually milder than primary hypothyroidism and often accompanies other pituitary failures.",
                ref(
                    "Central Hypothyroidism",
                    "Because a small but significant fraction of thyroid gland function is independent of TSH (~10%–15%), hypothyroidism due to central causes tends to be less severe than primary hypothyroidism.",
                ),
            ),
            note(
                f"{p}-n10",
                "Central hypothyroidism",
                "How to replace thyroid hormone in central hypothyroidism",
                "TSH cannot guide adequacy—target free T4 in the upper half of the reference range and treat coexisting glucocorticoid deficiency before starting thyroid hormone.",
                ref(
                    "Institution of Replacement Therapy",
                    "In patients with central hypothyroidism, serum TSH is not a reliable index of adequate replacement, and the serum  $ FT_{4} $ should be restored to a concentration in the upper half of the reference range.",
                ),
            ),
            note(
                f"{p}-n11",
                "Resistance to thyroid hormone",
                "RTHβ clinical and biochemical pattern",
                "RTHβ from THRB mutations causes elevated peripheral hormones with inappropriately normal or high TSH; tissues with predominant TRβ are hypothyroid while TRα-rich organs (heart) show hyperthyroid signs.",
                ref(
                    "Resistance to Thyroid Hormone",
                    "Biochemically, these patients have elevated peripheral hormones and a high normal or elevated TSH.",
                ),
            ),
            note(
                f"{p}-n12",
                "Resistance to thyroid hormone",
                "Why RTHβ must be distinguished from TSHoma",
                "Tachycardia, goiter, and elevated T4/T3 with nonsuppressed TSH overlap with TSH-secreting adenoma—family history, α-subunit, and THRB sequencing differentiate them.",
                ref(
                    "Resistance to Thyroid Hormone",
                    "The principal differential diagnosis with such a constellation is between a TSH-secreting pituitary tumor causing hyperthyroidism and RTHb.",
                ),
            ),
            note(
                f"{p}-n13",
                "Consumptive hypothyroidism",
                "Consumptive hypothyroidism from D3-expressing tumors",
                "Large hemangiomas or certain epithelial tumors overexpress type 3 deiodinase, destroying thyroid hormone so rapidly that massive replacement doses are required to normalize TSH.",
                ref(
                    "Consumptive Hypothyroidism",
                    "Consumptive hypothyroidism is the term given to a rare cause of hypothyroidism that was first identified in infants with visceral hemangiomas or related tumors,",
                ),
            ),
            note(
                f"{p}-n14",
                "Levothyroxine therapy",
                "How to dose levothyroxine in uncomplicated adults",
                "Typical replacement is ~1.6–1.8 µg/kg ideal body weight daily; allow 6 weeks for equilibration before adjusting dose based on TSH in primary hypothyroidism.",
                ref(
                    "Pharmacologic and Physiologic Considerations",
                    "The typical dose of levothyroxine, approximately 1.6 to 1.8 µg/kg ideal body weight per day (0.7–0.8 µg/lb), generally results in the prescription of between 75 and 125 µg/day for women and 125 to 200 µg/day for men.",
                ),
            ),
            note(
                f"{p}-n15",
                "Levothyroxine therapy",
                "Why levothyroxine should be taken on an empty stomach",
                "Although T4 can be absorbed with food, consistent empty-stomach ingestion minimizes day-to-day TSH variability on replacement therapy.",
                ref(
                    "Pharmacologic and Physiologic Considerations",
                    "Although  $ \\mathrm{T}_{4} $ is well absorbed and can be taken in a nonfasting state, regular ingestion of levothyroxine on an empty stomach results in the least variation in serum TSH concentration.",
                ),
            ),
            note(
                f"{p}-n16",
                "Levothyroxine therapy",
                "Why T4+T3 combination therapy remains controversial",
                "Levothyroxine alone yields a lower serum T3:T4 ratio than endogenous euthyroidism; aggregate trials show no consistent advantage of combination therapy, though symptomatic subsets may benefit.",
                ref(
                    "KEY POINTS",
                    "There continues to be interest in combination therapy with both levothyroxine and liothyronine, with the goals of better symptom resolution and restoration of more normal thyroid physiology.",
                ),
            ),
            note(
                f"{p}-n17",
                "Pregnancy",
                "Why pregnancy increases levothyroxine requirements ~30%",
                "Athyrotic women planning pregnancy should increase levothyroxine by about 30% early in the first trimester; requirements stay elevated until delivery, then revert within weeks.",
                ref(
                    "KEY POINTS",
                    "Athyreotic patients who are planning a pregnancy will need an increase in the dose of levothyroxine of around 30% magnitude, typically early in the first trimester.",
                ),
            ),
            note(
                f"{p}-n18",
                "Drug interactions",
                "How malabsorption and coadministered drugs raise levothyroxine needs",
                "Bowel disease, impaired gastric acid, sucralfate, calcium, iron, cholestyramine, and CYP3A4 inducers (rifampin, phenytoin) increase levothyroxine requirements in treated hypothyroid patients.",
                ref(
                    "KEY POINTS",
                    "Levothyroxine requirements are increased in malabsorption due to bowel diseases and impaired gastric acid secretion, adsorption of levothyroxine to coadministered medications, or situations in which levothyroxine metabolism is accelerated.",
                ),
            ),
            note(
                f"{p}-n19",
                "Subclinical hypothyroidism",
                "Why subclinical hypothyroidism treatment is individualized",
                "Trials in older adults with mild TSH elevations often show no symptom benefit; treat when progression risk, cardiovascular factors, or patient preference favor therapy—avoid driving TSH below normal.",
                ref(
                    "Subclinical Hypothyroidism",
                    "The decision to treat a patient with subclinical hypothyroidism should involve a joint decision between the patient and physician that considers potential risks and benefits.",
                ),
            ),
            note(
                f"{p}-n20",
                "Myxedema coma",
                "Myxedema coma presentation and triggers",
                "Myxedema coma is the terminal stage of severe long-standing hypothyroidism with hypothermia, bradycardia, hypotension, and high mortality—precipitated by cold, infection, trauma, or sedatives.",
                ref(
                    "Myxedema Coma",
                    "Myxedema coma is the ultimate stage of severe long-standing hypothyroidism.",
                ),
            ),
            note(
                f"{p}-n21",
                "Myxedema coma",
                "How to treat myxedema coma emergently",
                "Treat on clinical grounds without awaiting labs: IV levothyroxine 200–500 µg load then 100 µg daily, hydrocortisone for relative adrenal insufficiency, avoid hypotonic fluids, and support ventilation.",
                ref(
                    "Myxedema Coma",
                    "Administration of levothyroxine as a single intravenous dose of 200-500 µg repletes the peripheral hormone pool and may cause improvement within hours.",
                ),
            ),
            note(
                f"{p}-n22",
                "Postpartum thyroiditis",
                "Postpartum painless thyroiditis and permanent hypothyroidism risk",
                "Immune rebound after pregnancy causes painless postpartum thyroiditis; 10–50% develop permanent hypothyroidism over the next decade, especially with TPOAb during the hypothyroid phase.",
                ref(
                    "Sex and Pregnancy",
                    "This phenomenon results in transient postpartum thyroiditis, a form of painless subacute thyroiditis, and in 10% to 50% of these cases, permanent hypothyroidism may appear over the next decade.",
                ),
            ),
            note(
                f"{p}-n23",
                "Drug-induced thyroiditis",
                "Checkpoint inhibitors and TKIs causing autoimmune thyroid destruction",
                "Tyrosine kinase inhibitors and immune checkpoint blockers (CTLA4, PD1) can trigger destructive autoimmune thyroiditis leading to hypothyroidism—monitor thyroid function during oncologic therapy.",
                ref(
                    "KEY POINTS",
                    "Hypothyroidism due to direct thyroidal inflammation or activation of autoimmune destruction has been associated with a number of drugs, including tyrosine kinase inhibitors (TKIs) and checkpoint inhibitors.",
                ),
            ),
            note(
                f"{p}-n24",
                "Thyroiditis",
                "Painless versus painful subacute thyroiditis",
                "Painless subacute thyroiditis causes sudden thyrotoxicosis without severe pain and may follow pregnancy; painful subacute (de Quervain) thyroiditis features extreme tenderness radiating to ear and pharynx.",
                ref(
                    "Thyroiditis",
                    "The classic presentation of postviral thyroiditis, a condition referred to as painful subacute thyroiditis, is characterized by extreme thyroid tenderness, with pain radiating to the oropharynx and ears, and must be differentiated from acute infectious thyroiditis caused by bacterial or fungal infection.",
                ),
            ),
            note(
                f"{p}-n25",
                "Riedel thyroiditis",
                "Riedel (IgG4-related) sclerosing thyroiditis",
                "Riedel thyroiditis is a rare stony-hard asymmetric goiter in middle-aged women that invades adjacent structures mimicking carcinoma; tamoxifen may suppress TGFβ and reduce need for surgery.",
                ref(
                    "Riedel Thyroiditis",
                    "The thyroid gland is moderately enlarged, stony hard, and usually asymmetric.",
                ),
            ),
            note(
                f"{p}-n26",
                "Clinical presentation",
                "Why severe hypothyroidism is still missed clinically",
                "Fully developed myxedema is characteristic when considered, but mild hypothyroidism in older adults overlaps with other chronic disorders—maintain a high index of suspicion and measure TSH.",
                ref(
                    "Differential Diagnosis",
                    "Despite the availability of inexpensive and specific tests, it is still surprising how often obvious, severe, primary hypothyroidism is not recognized.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Hashimoto thyroiditis",
                "A 48-year-old woman has fatigue, constipation, and a firm painless goiter. TSH is 18 mU/L, free T4 low-normal, and TPOAb strongly positive. What is the leading diagnosis?",
                [
                    "Autoimmune Hashimoto thyroiditis",
                    "Subacute painful thyroiditis",
                    "TSH-secreting pituitary adenoma",
                    "Resistance to thyroid hormone β",
                ],
                0,
                "Elevated TSH with positive TPOAb in a goitrous patient indicates autoimmune primary hypothyroidism.",
                ref(
                    "Primary and Central Hypothyroidism",
                    "In patients with an elevated TSH level and a reduced  $ FT_{4} $, the presence of TPOAb generally points to autoimmune thyroid disease (Hashimoto disease) as the cause of the hypothyroidism (see Fig. 11.5).",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Subclinical hypothyroidism",
                "A 55-year-old woman has TSH 8.2 mU/L, normal free T4, and positive TPOAb but minimal symptoms. What best guides the decision to start levothyroxine?",
                [
                    "Joint assessment of progression risk, comorbidities, and patient preference",
                    "Mandatory immediate full replacement in all TPOAb-positive patients",
                    "Observation only until free T4 falls regardless of TSH",
                    "Start liothyronine monotherapy instead of levothyroxine",
                ],
                0,
                "Mild subclinical hypothyroidism therapy is individualized; TSH magnitude and TPOAb inform progression risk.",
                ref(
                    "Subclinical Hypothyroidism",
                    "The decision to treat a patient with subclinical hypothyroidism should involve a joint decision between the patient and physician that considers potential risks and benefits.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Laboratory evaluation",
                "A patient has low free T4 and TSH 2.1 mU/L (inappropriately normal). Which next step is most appropriate?",
                [
                    "Evaluate for central hypothyroidism and other pituitary hormone deficiencies",
                    "Diagnose primary Hashimoto disease and start high-dose levothyroxine",
                    "Reassure—normal TSH excludes hypothyroidism",
                    "Order radioactive iodine uptake as the first test",
                ],
                0,
                "Low thyroid hormones with nonsuppressed TSH indicates central hypothyroidism until proven otherwise.",
                ref(
                    "Primary and Central Hypothyroidism",
                    "A low thyroid hormone level with a normal or low TSH level should lead to an evaluation for the possibility of failure of other endocrine systems that require trophic pituitary hormones for normal function (see Box 11.1) (see Chapters 6 and 7).",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Congenital hypothyroidism",
                "A 3-week-old infant has confirmed congenital hypothyroidism and no heart disease. What initial levothyroxine strategy is recommended?",
                [
                    "10–15 µg/kg/day to rapidly normalize TSH",
                    "Adult dose 1.6 µg/kg once weekly",
                    "Liothyronine alone 5 µg daily",
                    "Defer treatment until 6 months to avoid craniosynostosis",
                ],
                0,
                "Neonates require weight-based high-dose levothyroxine promptly to protect neurodevelopment.",
                ref(
                    "Infants and Children",
                    "This is usually accomplished by administering an initial levothyroxine dose of 10 to 15 µg/kg/day for severe hypothyroidism and about 10 µg/kg/day for mild hypothyroidism.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Central hypothyroidism",
                "A patient with panhypopituitarism starts levothyroxine before glucocorticoid replacement. What complication is being risked?",
                [
                    "Adrenal crisis from unmasked cortisol deficiency as metabolism rises",
                    "Immediate thyroid storm from TSH surge",
                    "Permanent pituitary destruction from levothyroxine",
                    "Wolff-Chaikoff blockade of thyroid hormone synthesis",
                ],
                0,
                "Treat adrenal insufficiency before thyroid replacement in central hypothyroidism with ACTH deficiency.",
                ref(
                    "Institution of Replacement Therapy",
                    "Patients with central hypothyroidism should also be evaluated and treated for glucocorticoid deficiency, if necessary, before institution of thyroid replacement.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Resistance to thyroid hormone",
                "A teenager has goiter, palpitations, elevated free T4/T3, and TSH 6 mU/L. Family members have similar labs. Most likely diagnosis?",
                [
                    "Generalized resistance to thyroid hormone β (RTHβ)",
                    "Primary Hashimoto hypothyroidism",
                    "Factitious levothyroxine ingestion",
                    "Euthyroid sick syndrome",
                ],
                0,
                "Elevated hormones with nonsuppressed TSH and familial pattern suggests RTHβ rather than primary thyroid failure.",
                ref(
                    "Resistance to Thyroid Hormone",
                    "Both RTHb and RTHa are typically inherited in an autosomal-dominant manner, or they are caused by monoallelic de novo mutations.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Resistance to thyroid hormone",
                "Before labeling elevated TSH with high T4 as RTHβ, which finding would favor TSHoma instead?",
                [
                    "Elevated glycoprotein α-subunit with pituitary macroadenoma",
                    "Normal thyroid hormones in first-degree relatives",
                    "Negative pituitary imaging with THRB mutation",
                    "Low free T4 with suppressed TSH",
                ],
                0,
                "TSHomas lack familial thyroid hormone pattern and may show elevated α-subunit unlike RTH.",
                ref(
                    "Resistance to Thyroid Hormone",
                    "Factors that may assist in the differential diagnosis are as follows: absence of a family history in patients with TSH-producing tumors, normal thyroid hormone levels in family members of individuals with TSH-induced hyperthyroidism due to pituitary tumor, and the presence of an elevated glycoprotein  $ \\alpha $-subunit in patients with a pituitary tumor but not in those with RTH.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Consumptive hypothyroidism",
                "An infant with a large hepatic hemangioma has TSH >100 mU/L despite very high-dose oral levothyroxine. Best explanation?",
                [
                    "Tumor D3-mediated consumptive hypothyroidism requiring massive hormone replacement",
                    "Pituitary TSH resistance from THRB mutation",
                    "Inadequate dietary iodine alone",
                    "Transient postpartum thyroiditis",
                ],
                0,
                "Vascular tumors expressing D3 destroy thyroid hormone rapidly, requiring unusually high replacement doses.",
                ref(
                    "Consumptive Hypothyroidism",
                    "Consumptive hypothyroidism is the term given to a rare cause of hypothyroidism that was first identified in infants with visceral hemangiomas or related tumors,",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Levothyroxine therapy",
                "A stable hypothyroid patient on levothyroxine asks whether missing one pill matters. What is accurate counseling?",
                [
                    "A single missed dose has little effect; it can be taken the next day",
                    "Missing one dose requires doubling the next three doses",
                    "Weekly dosing is never acceptable under any circumstance",
                    "Food improves absorption so missed doses should be taken with high-fat meals only",
                ],
                0,
                "Levothyroxine's 7-day half-life allows flexibility for occasional missed doses.",
                ref(
                    "Pharmacologic and Physiologic Considerations",
                    "With its long half-life, omission of a single day's tablet has no significant effect, and the patient may safely take an omitted tablet the following day.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Levothyroxine therapy",
                "A 70-year-old with angina and new overt hypothyroidism (TSH 45 mU/L) needs levothyroxine. What starting approach is safest?",
                [
                    "25 µg daily with 12.5 µg increments every 2–3 months",
                    "Full replacement 1.7 µg/kg immediately",
                    "Liothyronine 25 µg every 6 hours intravenously as outpatient",
                    "Defer all thyroid hormone until after coronary bypass regardless of symptoms",
                ],
                0,
                "Elderly cardiac patients require low initial levothyroxine with slow titration.",
                ref(
                    "Institution of Replacement Therapy",
                    "At the other extreme, the elderly patient with heart disease, particularly angina pectoris, without reversible coronary lesions, should be given a small initial dose of levothyroxine (25  $ \\mu $g/day), and the dosage should be increased in 12.5- $ \\mu $g increments at intervals of 2 to 3 months with careful clinical and laboratory evaluation.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Pregnancy",
                "A athyreotic woman on levothyroxine discovers pregnancy at 5 weeks. TSH is 4.8 mU/L. Best immediate adjustment?",
                [
                    "Increase levothyroxine by ~30% and recheck TSH in 4–6 weeks",
                    "Stop levothyroxine until second trimester",
                    "Switch to desiccated thyroid extract only",
                    "Add antithyroid drug to normalize TSH",
                ],
                0,
                "Pregnancy raises levothyroxine need early—athyrotic women should empirically increase dose ~30% at confirmation.",
                ref(
                    "Institution of Replacement Therapy",
                    "Athyrotic patients who are planning a pregnancy can be advised to increase the dose by around 30% as soon as the diagnosis is confirmed because the change in requirement appears soon after implantation.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Drug interactions",
                "A hypothyroid patient started cholestyramine and calcium for hyperlipidemia now has rising TSH on unchanged levothyroxine. Mechanism?",
                [
                    "Binding/interference with levothyroxine absorption in the gut",
                    "Direct pituitary TSH suppression by resin",
                    "Increased thyroid hormone production from goitrogens",
                    "Consumptive inactivation by type 3 deiodinase in resin",
                ],
                0,
                "Resins and calcium carbonate adsorb levothyroxine and increase replacement requirements.",
                ref(
                    "Institution of Replacement Therapy",
                    "Other conditions in which levothyroxine requirements are increased (see Box 11.2) $ ^{208,209,265} $ include malabsorption due to bowel diseases, impaired gastric acid secretion, $ ^{226} $ and adsorption of levothyroxine to coadministered medications such as sucralfate, aluminum hydroxide, calcium carbonate, ferrous sulfate, lovastatin, or various resins.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Drug interactions",
                "A patient on stable levothyroxine starts omeprazole and TSH rises. What management is supported?",
                [
                    "Increase levothyroxine or use liquid formulation; impaired acid reduces tablet absorption",
                    "Stop levothyroxine because PPIs cause hyperthyroidism",
                    "Add potassium iodide to enhance absorption",
                    "Switch to weekly liothyronine monotherapy",
                ],
                0,
                "Reduced gastric acid increases levothyroxine dose needs; liquid T4 may absorb better with PPIs.",
                ref(
                    "Pharmacologic and Physiologic Considerations",
                    "Patients with impaired acid secretion on levothyroxine therapy require a 22% to 34% higher dose of levothyroxine to maintain the desired serum TSH.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Subclinical hypothyroidism",
                "A 42-year-old with TSH 12 mU/L, normal free T4, and strong TPOAb asks about treatment to prevent progression. What is most accurate?",
                [
                    "Progression risk is higher with TSH >10 and positive TPOAb; treatment may be offered",
                    "Progression never occurs if free T4 is normal",
                    "Levothyroxine is contraindicated until free T4 falls",
                    "TPOAb positivity excludes autoimmune thyroid disease",
                ],
                0,
                "Higher baseline TSH and TPOAb predict faster progression to overt hypothyroidism.",
                ref(
                    "Subclinical Hypothyroidism",
                    "Prospective studies of women with subclinical hypothyroidism have shown rates of progression from approximately 3% to 8% per year, with the higher rates seen in individuals with initial TSH concentrations greater than 10 and those with positive anti-TPOAb.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Coronary disease",
                "A hypothyroid patient with angina needs levothyroxine. What does evidence support before full replacement?",
                [
                    "Evaluate/treat correctable coronary lesions first when angina is present",
                    "Always achieve full euthyroidism before any cardiac evaluation",
                    "Use liothyronine alone to avoid angina",
                    "Withhold all thyroid hormone permanently if any CAD exists",
                ],
                0,
                "Revascularize remediable coronary disease before levothyroxine when angina is present.",
                ref(
                    "Coexisting Coronary Artery Disease and Hypothyroidism",
                    "However, patients with preexisting angina pectoris should be evaluated for correctable lesions of the coronary arteries and treated appropriately before levothyroxine is administered.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Myxedema coma",
                "An elderly woman is obtunded with temperature 32°C, hypotension, and bradycardia. What is the priority after sending labs?",
                [
                    "Start IV levothyroxine and hydrocortisone without waiting for results",
                    "Await TSH before any treatment",
                    "Give large volumes of hypotonic D5W",
                    "Apply external heating pads as primary therapy",
                ],
                0,
                "Myxedema coma requires immediate IV thyroid hormone and glucocorticoid support on clinical grounds.",
                ref(
                    "Myxedema Coma",
                    "Otherwise, the diagnosis should be made on clinical grounds; after serum has been sent for thyroid function tests, therapy should be initiated without awaiting the results of delayed confirmatory tests because the mortality rate may be 20% or higher.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Myxedema coma",
                "During myxedema coma treatment, which fluid strategy avoids a common pitfall?",
                [
                    "Avoid hypotonic fluids because of reduced free water clearance",
                    "Infuse hypotonic saline rapidly to correct hyponatremia only with D5W",
                    "Withhold all IV fluids to prevent overload",
                    "Use external warming as the sole resuscitative measure",
                ],
                0,
                "Hypothyroid patients clear free water poorly—hypotonic fluids risk water intoxication.",
                ref(
                    "Myxedema Coma",
                    "Hypotonic fluids should not be given because of the danger of water intoxication owing to the reduced free water clearance of the hypothyroid patient.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Postpartum thyroiditis",
                "Four months postpartum a woman had painless thyrotoxicosis; she now has TSH 9 mU/L and mild symptoms. TPOAb is positive. Next step?",
                [
                    "Start levothyroxine and plan reassessment—permanent hypothyroidism is common",
                    "High-dose methimazole for 18 months",
                    "Therapeutic radioiodine ablation",
                    "Ignore TSH because postpartum changes always resolve within 2 weeks",
                ],
                0,
                "Postpartum thyroiditis often progresses to permanent hypothyroidism, especially with TPOAb.",
                ref(
                    "Sex and Pregnancy",
                    "Those women with hypothyroidism and positive TPO antibodies during the phase of postpartum thyroiditis are most at risk of such an outcome.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Drug-induced thyroiditis",
                "A melanoma patient on pembrolizumab develops TSH 25 mU/L and low free T4. Management?",
                [
                    "Levothyroxine replacement and continued oncology coordination",
                    "High-dose glucocorticoids alone without thyroid hormone",
                    "Stop checkpoint inhibitor permanently in all cases before treating hypothyroidism",
                    "Radioiodine ablation of the thyroid",
                ],
                0,
                "Checkpoint inhibitors commonly cause autoimmune thyroiditis leading to hypothyroidism requiring replacement.",
                ref(
                    "Drug-Induced Thyroid Destruction",
                    "Therapy of solid tumors with monoclonal antibodies against CTLA4 and checkpoint inhibitors is a new and very frequent cause of autoimmune thyroiditis, ultimately resulting in hypothyroidism.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Subacute thyroiditis",
                "A patient has painful thyroid, fever, ESR 90 mm/h, and transient thyrotoxicosis. Which therapy is appropriate for thyrotoxic symptoms?",
                [
                    "Beta-blockers; antithyroid drugs do not reduce hormone release",
                    "Methimazole for 12–18 months",
                    "Radioiodine ablation immediately",
                    "Levothyroxine suppression of TSH during thyrotoxic phase",
                ],
                0,
                "Destructive thyroiditis releases stored hormone—symptoms are treated with beta-blockers, not thionamides.",
                ref(
                    "Transient Hypothyroidism",
                    "Transient hypothyroidism is defined as a period of reduced  $ FT_{4} $ with suppressed, normal, or elevated TSH levels that are eventually followed by a euthyroid state.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Subacute thyroiditis",
                "After painful subacute thyroiditis, a patient has TSH 11 mU/L and negative TPOAb. What distinguishes this from Hashimoto hypothyroidism?",
                [
                    "Negative/low TPOAb favors transient post-thyroiditis hypothyroidism—trial dose reduction later",
                    "Positive TRAb confirms subacute thyroiditis",
                    "Elevated RAIU confirms Hashimoto disease",
                    "Painful thyroiditis never causes hypothyroidism",
                ],
                0,
                "Absent TPOAb after thyroiditis suggests possible recovery—consider temporary rather than lifelong replacement.",
                ref(
                    "Transient Hypothyroidism",
                    "Negative or low antibodies argue strongly for a nonautoimmune cause. This is significant, in that it may be possible for the patient to be treated only temporarily for hypothyroidism.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Infectious thyroiditis",
                "A febrile child has focal left thyroid pain, leukocytosis, and purulent FNA. Most likely diagnosis?",
                [
                    "Acute infectious thyroiditis—often left lobe with piriform sinus fistula",
                    "Painless postpartum thyroiditis",
                    "Riedel sclerosing thyroiditis",
                    "Subclinical Hashimoto disease only",
                ],
                0,
                "Bacterial thyroiditis presents with severe localized tenderness; left lobe disease often links to piriform sinus fistula.",
                ref(
                    "Acute Infectious Thyroiditis",
                    "The most common cause of repeated childhood infectious thyroiditis, particularly in the left lobe, is a consequence of an internal fistula extending from the piriform sinus to the thyroid.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Riedel thyroiditis",
                "A 52-year-old woman has a hard asymmetric goiter fixed to surrounding tissues without lymphadenopathy. Biopsy shows dense fibrosis. Initial medical therapy?",
                [
                    "Tamoxifen 10–20 mg/day, with or without corticosteroids",
                    "High-dose methimazole",
                    "Therapeutic radioiodine",
                    "Observation only—Riedel never causes compressive symptoms",
                ],
                0,
                "Tamoxifen may suppress TGFβ and relieve Riedel thyroiditis, sometimes avoiding surgery.",
                ref(
                    "Riedel Thyroiditis",
                    "Tamoxifen, 10 to 20 mg/day (with or without corticosteroids), has been successful in many of these patients and is thought to suppress transforming growth factor beta (TGF $ \\beta $).",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Levothyroxine monitoring",
                "A patient on levothyroxine has normal free T4 but TSH remains elevated. Adherence is confirmed. Next consideration?",
                [
                    "Malabsorption or interfering medications/supplements",
                    "Switch to PTU to raise TSH",
                    "Diagnose RTH and stop levothyroxine",
                    "Increase dose daily without retesting for 6 months",
                ],
                0,
                "Elevated TSH despite adequate prescribed dose suggests malabsorption, interference, or nonadherence patterns.",
                ref(
                    "Adverse Effects of Levothyroxine Therapy",
                    "In some patients, TSH levels remain elevated despite the prescription of adequate replacement doses.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Combination therapy",
                "A hypothyroid patient with normal TSH on levothyroxine still feels fatigued. What does current evidence support?",
                [
                    "Explore non-thyroid causes; routine switch to T4+T3 is not consistently beneficial",
                    "Mandatory conversion to desiccated thyroid for all symptomatic patients",
                    "Add high-dose liothyronine until TSH is suppressed below normal",
                    "Stop levothyroxine because normal TSH proves symptoms are unrelated to thyroid",
                ],
                0,
                "Persistent nonspecific symptoms on adequate levothyroxine are common—combination therapy has not shown consistent benefit.",
                ref(
                    "Patients With Hypothyroid Symptoms Despite Restitution of Normal Thyroid Function",
                    "The addition of thyroid replacement containing triiodothyronine has been investigated for these patients but has not been shown to consistently provide relief of symptoms.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Screening",
                "A 58-year-old asymptomatic woman asks about routine thyroid screening. What aligns with US guidance?",
                [
                    "Population screening is not recommended; case-finding in higher-risk groups is reasonable",
                    "Universal annual TSH for all adults is mandatory",
                    "Screening is required only in men over 65",
                    "TSH screening should replace all other preventive labs",
                ],
                0,
                "USPSTF finds insufficient evidence for universal screening; targeted testing in at-risk groups is advocated.",
                ref(
                    "Screening for Primary Hypothyroidism",
                    "An updated report from the U.S. Preventive Services Task Force concluded that there is still insufficient evidence to recommend population screening for hypothyroidism in nonpregnant adults.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Epidemiology",
                "Overt hypothyroidism affects about 0.3% and subclinical hypothyroidism about 4.3% of U.S. adults.",
                True,
                "NHANES-era estimates cited in Williams for overt and subclinical disease prevalence.",
                ref(
                    "Hypothyroidism",
                    "In the United States, 0.3% have overt hypothyroidism, defined as an elevated serum TSH concentration and reduced free thyroxine concentration (FT $ _4 $), and 4.3% have what is designated as subclinical or mild hypothyroidism.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Epidemiology",
                "Primary hypothyroidism accounts for approximately 99% of hypothyroidism cases.",
                True,
                "Central TSH deficiency and other causes are rare compared with primary thyroid failure.",
                ref(
                    "Hypothyroidism",
                    "Primary hypothyroidism is the cause in approximately 99% of cases of hypothyroidism, with less than 1% of cases being due to TSH deficiency or other causes.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Hashimoto thyroiditis",
                "Up to 20% of autoimmune hypothyroid patients may have TSH receptor-blocking antibodies.",
                True,
                "Blocking TSHRAbs can cause hypothyroidism and rarely alternate with stimulating antibodies.",
                ref(
                    "Autoimmune Hypothyroidism",
                    "Up to 20% of patients with autoimmune hypothyroidism have TSH receptor antibodies that block the receptor, rather than stimulating it, as in Graves disease;",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Subclinical hypothyroidism",
                "Overt hypothyroidism should be treated with levothyroxine, whereas mild subclinical disease may not require treatment.",
                True,
                "KEY POINTS distinguish mandatory treatment of overt disease from individualized subclinical management.",
                ref(
                    "KEY POINTS",
                    "Mild or subclinical hypothyroidism may not require treatment, depending on the clinical situation. However, overt hypothyroidism should be treated with levothyroxine.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Levothyroxine therapy",
                "Levothyroxine replacement in athyrotic patients typically produces slightly higher serum free T4 than endogenous euthyroidism at normalized TSH.",
                True,
                "T4 feedback at the pituitary allows higher FT4 for equivalent T3 on replacement.",
                ref(
                    "KEY POINTS",
                    "The quantity of levothyroxine required to normalize TSH in an athyrotic patient results in a slightly higher serum-free thyroxine ( $ T_{4} $) concentration than is present in endogenous euthyroidism.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Levothyroxine therapy",
                "Approximately six weeks are required for full equilibration after a levothyroxine dose change.",
                True,
                "The 7-day half-life means dose adjustments should be judged after ~6 weeks except in pregnancy.",
                ref(
                    "Pharmacologic and Physiologic Considerations",
                    "Because of the 7-day half-life, approximately 6 weeks are required before there is complete equilibration of the  $ FT_{4} $ and the biologic effects of levothyroxine.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Central hypothyroidism",
                "Serum TSH is a reliable marker of adequate replacement in central hypothyroidism.",
                False,
                "TSH is unreliable in central hypothyroidism—use free T4 in the upper reference range.",
                ref(
                    "Institution of Replacement Therapy",
                    "In patients with central hypothyroidism, serum TSH is not a reliable index of adequate replacement, and the serum  $ FT_{4} $ should be restored to a concentration in the upper half of the reference range.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Myxedema coma",
                "Myxedema coma patients may remain afebrile despite serious infection.",
                True,
                "Hypometabolism masks fever; infection is a common precipitant.",
                ref(
                    "Myxedema Coma",
                    "The myxedematous patient may be afebrile despite a significant infection.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Postpartum thyroiditis",
                "Permanent hypothyroidism develops in 10% to 50% of women after postpartum thyroiditis.",
                True,
                "Long-term follow-up shows substantial risk of permanent thyroid failure.",
                ref(
                    "Sex and Pregnancy",
                    "in 10% to 50% of these cases, permanent hypothyroidism may appear over the next decade.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Drug-induced thyroiditis",
                "Sunitinib and other TKIs can cause hypothyroidism through thyroid destruction.",
                True,
                "TKI-associated hypothyroidism may follow destructive thyroiditis with long-term replacement need.",
                ref(
                    "Hypothyroidism Due to Drug-Induced Thyroid Destruction",
                    "TKIs, such as sunitinib, have been associated with a high incidence of hypothyroidism due to thyroid destruction.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Subacute thyroiditis",
                "Painful subacute thyroiditis is usually preceded by an upper respiratory infection.",
                True,
                "Table 11.2 shows preceding URI in 88% of subacute thyroiditis cases.",
                ref(
                    "TABLE 11.2 Features Useful in Differentiating Between Acute Infectious Thyroiditis and Subacute Thyroiditis",
                    "Preceding upper respiratory infection",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Riedel thyroiditis",
                "Riedel thyroiditis is closely related to IgG4-related sclerosing disease.",
                True,
                "Morphologic overlap links Riedel thyroiditis with IgG4-related fibrosis.",
                ref(
                    "Riedel Thyroiditis",
                    "The morphologic similarities between the fibrosis of Riedel thyroiditis and IgG4-related sclerosing disease suggest that these entities are closely related, with thyroiditis representing an initial manifestation of a more generalized process.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Symptoms",
                "Levothyroxine therapy improves symptoms in euthyroid patients with nonspecific complaints.",
                False,
                "A randomized trial showed no benefit treating biochemically euthyroid patients with nonspecific symptoms.",
                ref(
                    "Symptoms Overlapping With Hypothyroid Symptoms",
                    "A randomized controlled trial of treatment for such patients did not show any benefit.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Hashimoto thyroiditis",
                "Assertion: TPO antibodies strongly support autoimmune Hashimoto hypothyroidism.",
                "Reason: TPOAb are absent in virtually all patients with Hashimoto disease.",
                2,
                "Assertion is true; reason is false—TPOAb are present in almost all autoimmune hypothyroid patients.",
                ref(
                    "Autoimmune Hypothyroidism",
                    "Circulating autoantibodies against thyroglobulin and TPO are present in almost all patients with autoimmune hypothyroidism.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Subclinical hypothyroidism",
                "Assertion: Subclinical hypothyroidism is defined by elevated TSH with normal free T4.",
                "Reason: Subclinical hypothyroidism always requires immediate levothyroxine in every patient.",
                2,
                "Assertion is true; reason is false—treatment depends on clinical context and shared decision-making.",
                ref(
                    "KEY POINTS",
                    "Mild or subclinical hypothyroidism may not require treatment, depending on the clinical situation.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Laboratory evaluation",
                "Assertion: Low free T4 with normal or low TSH suggests central hypothyroidism.",
                "Reason: Central hypothyroidism always presents with markedly elevated TSH.",
                2,
                "Assertion is true; reason is false—central disease shows low/inappropriately normal TSH with low T4.",
                ref(
                    "Primary and Central Hypothyroidism",
                    "A low thyroid hormone level with a normal or low TSH level should lead to an evaluation for the possibility of failure of other endocrine systems that require trophic pituitary hormones for normal function",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Congenital hypothyroidism",
                "Assertion: Delayed treatment of congenital hypothyroidism causes irreversible neurologic damage.",
                "Reason: Adult-onset hypothyroidism produces equally irreversible brain injury.",
                2,
                "Assertion is true for untreated neonatal disease; reason is false—adult deficiency is usually reversible with treatment.",
                ref(
                    "Central and Peripheral Nervous Systems",
                    "Deficiency of thyroid hormone beginning in adult life causes less severe manifestations that usually respond to treatment with the hormone.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Resistance to thyroid hormone",
                "Assertion: RTHβ patients may have tachycardia despite tissue-level hypothyroidism in some organs.",
                "Reason: TRα is the predominant receptor in the heart.",
                0,
                "Both true—cardiac TRα expression explains tachycardia with mixed clinical picture in RTHβ.",
                ref(
                    "Resistance to Thyroid Hormone",
                    "With respect to the heart, palpitations and tachycardia are common. This is explained by the fact that TRa is the predominant receptor in the heart.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Consumptive hypothyroidism",
                "Assertion: Consumptive hypothyroidism requires unusually high thyroid hormone doses.",
                "Reason: D3-expressing tumors accelerate thyroid hormone inactivation.",
                0,
                "Both true—massive replacement is needed when D3 degrades hormone rapidly.",
                ref(
                    "Hypothyroidism",
                    "Consumptive hypothyroidism, identified in an increasing number of clinical settings, is the result of accelerated inactivation of thyroid hormone by type 3 iodothyronine deiodinase (D3).",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Levothyroxine therapy",
                "Assertion: TSH normalization is the goal of levothyroxine in primary hypothyroidism.",
                "Reason: TSH is equally reliable for dosing in central hypothyroidism.",
                2,
                "Assertion is true for primary disease; reason is false—central hypothyroidism requires free T4 targeting.",
                ref(
                    "Pharmacologic and Physiologic Considerations",
                    "Return of the serum TSH level to normal is therefore the goal of levothyroxine therapy in the patient with primary hypothyroidism.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Pregnancy",
                "Assertion: Hypothyroid pregnant women need increased levothyroxine early in gestation.",
                "Reason: Thyroid hormone requirements fall throughout pregnancy and stay elevated postpartum.",
                2,
                "Assertion is true; reason is false—requirements rise in pregnancy and return to prepregnancy levels after delivery.",
                ref(
                    "Institution of Replacement Therapy",
                    "The increased requirement persists throughout pregnancy but returns to normal rapidly after delivery.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Myxedema coma",
                "Assertion: Myxedema coma therapy should begin before confirmatory lab results return.",
                "Reason: Delaying treatment improves survival because hormone levels correlate with severity.",
                2,
                "Assertion is true; reason is false—delay worsens prognosis; treat on clinical suspicion.",
                ref(
                    "Myxedema Coma",
                    "therapy should be initiated without awaiting the results of delayed confirmatory tests because the mortality rate may be 20% or higher.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Postpartum thyroiditis",
                "Assertion: Postpartum thyroiditis can present with painless thyrotoxicosis followed by hypothyroidism.",
                "Reason: Postpartum thyroiditis never leads to permanent hypothyroidism.",
                2,
                "Assertion is true; reason is false—10–50% develop permanent hypothyroidism over years.",
                ref(
                    "Sex and Pregnancy",
                    "in 10% to 50% of these cases, permanent hypothyroidism may appear over the next decade.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Drug-induced thyroiditis",
                "Assertion: Checkpoint inhibitors can cause autoimmune thyroiditis with eventual hypothyroidism.",
                "Reason: Checkpoint inhibitors only cause thyrotoxicosis and never hypothyroidism.",
                2,
                "Assertion is true; reason is false—checkpoint blockade commonly ends in hypothyroidism.",
                ref(
                    "Hypothyroidism Due to Drug-Induced Thyroid Destruction",
                    "Therapy of solid tumors with monoclonal antibodies against CTLA4 and checkpoint inhibitors is a new and very frequent cause of autoimmune thyroiditis, ultimately resulting in hypothyroidism.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Riedel thyroiditis",
                "Assertion: Riedel thyroiditis can mimic thyroid carcinoma clinically.",
                "Reason: Riedel goiter is soft, mobile, and associated with marked lymphadenopathy.",
                2,
                "Assertion is true; reason is false—Riedel gland is stony hard, invasive, without nodal enlargement.",
                ref(
                    "Riedel Thyroiditis",
                    "The consistency of the gland and the invasion of adjacent structures suggest carcinoma, but there is no enlargement of regional lymph nodes.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "11",
        "title": "Hypothyroidism and Thyroiditis",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Takashi Akamizu, Jacqueline Jonklaas",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_11_Hypothyroidism_and_Thyroiditis.md",
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
