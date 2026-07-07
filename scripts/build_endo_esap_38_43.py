#!/usr/bin/env python3
"""Generate remediated ESAP 2021 modules e21-38 through e21-43 (Thyroid/interfaces batch)."""
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


def build_chapter_38() -> dict:
    p = "e21-38"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Discordant TFTs",
                "Why discordant thyroid function tests demand a systematic approach",
                "Discordant results may reflect intercurrent illness, medications, assay interference, poor levothyroxine adherence, or rare HPT-axis disorders; successful resolution requires understanding physiology, assay methodology, and TFT patterns before advanced testing.",
                ref(
                    "Main Conclusions",
                    "Discordant or anomalous TFT results may arise in the context of: Confounding intercurrent illness and/or medication use. Erratic or poor adherence to levothyroxine therapy. Interference in commonly used laboratory assays for thyroid hormone or TSH measurement. Rare genetic or acquired disorders of the hypothalamic-pituitary-thyroid (HPT) axis.",
                ),
            ),
            note(
                f"{p}-n2",
                "Clinical significance",
                "Raised thyroid hormones with nonsuppressed TSH",
                "Elevated T4/T3 with nonsuppressed TSH is a common discordant pattern; many cases reflect illness, drugs, or analytic interference, but resistance to thyroid hormone and TSH-secreting pituitary tumors must be distinguished to avoid wasteful investigation and incorrect treatment.",
                ref(
                    "Significance of the Clinical Problem",
                    "Raised thyroid hormones (T4, T3) with nonsuppressed TSH levels are an important, and relatively commonly encountered, pattern of discordant TFTs; many cases can be explained by confounding intercurrent illness, concomitant medication use, or analytic interference in thyroid hormone or TSH assays, but differentiating between these and other rarer causes (eg, resistance to thyroid hormone, TSH-secreting pituitary tumor) can be difficult.",
                ),
            ),
            note(
                f"{p}-n3",
                "TSH assays",
                "How TSH sandwich assays are susceptible to interference",
                "Sandwich TSH assays use capture and detection antibodies; human anti-animal or heterophile antibodies can cause falsely low or high TSH via blocking or cross-linking. Confirm with alternate assays, dilution nonlinearity, or immunosuptraction.",
                ref(
                    "TSH Measurement",
                    "Thus, a human anti-animal antibody that blocks TSH binding to either capture or detection antibodies will result in \"negative interference,\" causing a falsely low TSH value. Conversely, a human anti-animal antibody that is capable of cross-linking the capture and detection antibodies may cause \"positive interference,\" leading to a falsely high TSH value.",
                ),
            ),
            note(
                f"{p}-n4",
                "Free hormone assays",
                "How heparin causes artifactual free T4 elevation",
                "Heparin activates endothelial lipoprotein lipase, raising free fatty acids that displace T4 from binding proteins—raising measured free but not total T4 in vitro, especially with delayed sample processing.",
                ref(
                    "Case 2",
                    "Heparin (both conventional and low-molecular-weight in prophylactic and treatment dosages) is able to activate endothelial lipoprotein lipase. In some patients, the accompanying rise in serum free fatty acid levels is sufficient to cause displacement of T4 from its binding sites (eg, on thyroxine-binding globulin), thereby raising free, but not total, thyroid hormone levels.",
                ),
            ),
            note(
                f"{p}-n5",
                "Biotin",
                "Why biotin supplements confound immunoassays",
                "Biotin as medication or supplement interferes with streptavidin-biotin assay platforms and can affect many laboratory tests—not only thyroid hormone and TSH measurements.",
                ref(
                    "Biotin (Vitamin B₇)",
                    "Biotin used either as a medication or dietary supplement presents a specific challenge for laboratory platforms that use biotin as part of the core assay configuration (eg, streptavidin-biotin complex). This issue can affect a multitude of assays, not simply thyroid hormone or TSH measurements.",
                ),
            ),
            note(
                f"{p}-n6",
                "FDH",
                "How familial dysalbuminemic hyperthyroxinemia confounds free T4",
                "Dominantly inherited albumin or transthyretin variants alter iodothyronine binding and can overestimate free T4 on one-step analogue assays; two-step assays, equilibrium dialysis, or mass spectrometry help confirm.",
                ref(
                    "Free T4 and Free T3 Measurement",
                    "Variant thyroid hormone-binding proteins: dominantly-inherited genetic variants of albumin (familial dysalbuminemic hyperthyroxinemia [FDH] or transthyretin [transthyretin-associated hyperthyroxinemia (TTR-AH)]), may alter affinity for iodothyronines, and can cause free T4 (and less frequently free T3) to be overestimated, particularly in \"1-step\" analogue hormone assays.",
                ),
            ),
            note(
                f"{p}-n7",
                "RTH vs thyrotropinoma",
                "Why distinguishing resistance to thyroid hormone from thyrotropinoma is difficult",
                "Both occur in similar age ranges and either gender; central/pituitary resistance may show thyrotoxic symptoms, so clinical features are not discriminatory—pitfalls include α-subunit in nonfunctioning tumors, falsely low SHBG in mixed GH/TSH tumors, and thyrotroph hyperplasia on imaging after thyroid ablation in RTH.",
                ref(
                    "Resistance to Thyroid Hormone vs TSH-Secreting Pituitary Tumor",
                    "Resistance to thyroid hormone (estimated incidence 1 in 40,000 to 50,000 live births) and TSH-secreting pituitary tumors (estimated prevalence 1 to 3 per million) occur in patients of a similar age range and either gender.",
                ),
            ),
            note(
                f"{p}-n8",
                "Case 1 pitfall",
                "Why assay interference must be excluded before thyrotropinoma workup",
                "In elevated T4/T3 with nonsuppressed TSH, the TSH may be artifactually high while true primary thyrotoxicosis exists with suppressed TSH—most endocrine laboratories can screen for TSH assay interference before MRI or dynamic testing.",
                ref(
                    "Case 1",
                    "Before embarking on further investigations to distinguish a TSH-secreting pituitary adenoma (thyrotropinoma) from resistance to thyroid hormone, it is first necessary to exclude laboratory assay interference as a cause for the unusual TFT pattern.",
                ),
            ),
            note(
                f"{p}-n9",
                "Levothyroxine adherence",
                "How erratic levothyroxine adherence produces discordant TFTs",
                "Intermittent ingestion can yield normal or elevated thyroid hormone levels on the day of testing while failing to normalize a chronically elevated TSH—especially if a larger dose is taken immediately before the blood draw.",
                ref(
                    "Case 3",
                    "Erratic adherence to levothyroxine therapy (Answer A) could produce this pattern of results, especially if the patient takes a larger dosage of levothyroxine on the day(s) immediately before the blood test, which can be sufficient to produce serum T4 levels within the laboratory reference range, but is inadequate to normalize a chronically raised TSH.",
                ),
            ),
            note(
                f"{p}-n10",
                "Confounding factors",
                "How clinical context alters TFT interpretation",
                "Age, pregnancy trimester-specific ranges, levothyroxine dosing, medications (amiodarone, heparin, biotin), and nonthyroidal illness all influence TFT patterns and must be reviewed before labeling results as inexplicable.",
                ref(
                    "Consider Potential Confounding Factors",
                    "It is important to pay attention to the clinical context, as several factors may have particular relevance for the interpretation of TFTs, including: Age: Many laboratories do not report age-specific reference ranges, with potential implications for interpreting TFT results at the extremes of age.",
                ),
            ),
            note(
                f"{p}-n11",
                "Barriers",
                "Pitfall: reflex advanced imaging without excluding interference",
                "Limited awareness of assay susceptibility and rare HPT disorders leads to misdirected investigation, resource wastage, and inappropriate therapeutic intervention.",
                ref(
                    "Significance of the Clinical Problem",
                    "Misdirected investigation of these entities results in wastage of resources and/or incorrect therapeutic intervention.",
                ),
            ),
            note(
                f"{p}-n12",
                "Case 2 synthesis",
                "How normal total T4 excludes genuine thyrotoxicosis in heparin artifact",
                "Raised free T4 with normal TSH and normal total T4 argues against true thyrotoxicosis and against FDH; postoperative thromboprophylaxis with low-molecular-weight heparin is the likely explanation.",
                ref(
                    "Case 2",
                    "Although the patient has an apparently raised free T₄ level, the TSH is not suppressed and subsequent investigations on the same serum sample show an entirely normal total T₄ level. Taken together, the normal TSH and total T₄ levels argue against genuine thyrotoxicosis and also exclude familial dysalbuminemic hyperthyroxinemia",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "A 43-year-old woman has palpitations, weight loss, heat intolerance, fine tremor, small goiter, free T4 3.5 ng/dL, free T3 11.7 pg/mL, and TSH 4.8 mIU/L. Most appropriate next step?",
                [
                                        "Contrast-enhanced pituitary MRI",
                    "Measure serum α-subunit",
                    "Measure serum SHBG",
                    "Seek advice on further laboratory analyses",
],
                3,
                "Exclude TSH assay interference before pursuing thyrotropinoma vs resistance to thyroid hormone; the clinical picture suggests true thyrotoxicosis with a potentially erroneous TSH.",
                ref("Case 1", "Answer: E) Seek advice on further laboratory analyses"),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "A 73-year-old post hip-replacement patient on thromboprophylaxis has fast AF, small goiter, free T4 2.2 ng/dL, TSH 1.8 mIU/L, and total T4 9.2 μg/dL. Most likely explanation?",
                [
                                        "Familial dysalbuminemic hyperthyroxinemia",
                    "Iodinated contrast-induced thyrotoxicosis",
                    "Medication-induced artifactual elevation of free T4",
                    "Resistance to thyroid hormone due to THRB pathogenic variant",
],
                2,
                "Normal TSH and total T4 with elevated free T4 point to in vitro heparin displacement of T4 from binding proteins, not genuine thyrotoxicosis.",
                ref("Case 2", "Answer: C) Medication-induced artifactual elevation of free T_{4}"),
            ),
            mcq(
                f"{p}-q3",
                "Case 3",
                "A 33-year-old post-total thyroidectomy woman on up to 300 mcg levothyroxine daily has persistently elevated TSH with free T4 in the upper reference range and is clinically euthyroid. Most likely explanation?",
                [
                                        "Erratic adherence to levothyroxine therapy",
                    "Malabsorption syndrome (e.g., celiac disease)",
                    "Nonthyroidal illness",
                    "Resistance to thyroid hormone",
],
                0,
                "Taking a larger dose immediately before testing can normalize T4 transiently while TSH remains chronically elevated; malabsorption is less likely with upper-range free T4.",
                ref("Case 3", "Answer: A) Erratic adherence to levothyroxine therapy"),
            ),
            mcq(
                f"{p}-q4",
                "Assay interference",
                "Which finding most strongly supports TSH assay interference?",
                [
                                        "Uniformly concordant TSH across all platforms",
                    "Linear TSH results on serial dilution",
                    "Discordant TSH between assays using different antibody pairs",
                    "Suppressed TSH with elevated free T4",
],
                2,
                "Discordant results between methodologies using different antibody pairs is a standard laboratory strategy to confirm interference.",
                ref(
                    "TSH Measurement",
                    "Discordant TSH results in different assays that use different antibody pairs/methodology.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Biotin",
                "A patient taking high-dose biotin has discordant TFTs across platforms. Best initial step?",
                [
                                        "Immediate thyroidectomy",
                    "Stop biotin and repeat testing after appropriate washout; alert the laboratory",
                    "Start methimazole",
                    "Pituitary MRI",
],
                1,
                "Biotin interferes with streptavidin-biotin assay configurations; hold biotin and involve the laboratory before invasive workup.",
                ref(
                    "Biotin (Vitamin B₇)",
                    "Biotin used either as a medication or dietary supplement presents a specific challenge for laboratory platforms that use biotin as part of the core assay configuration",
                ),
            ),
            mcq(
                f"{p}-q6",
                "FDH workup",
                "Suspected familial dysalbuminemic hyperthyroxinemia with elevated free T4 on one-step assay. Best confirmatory approach?",
                [
                                        "Two-step back-titration assay, equilibrium dialysis, or mass spectrometry",
                    "Immediate radioiodine uptake scan",
                    "TRH stimulation test only",
                    "Empiric antithyroid drugs",
],
                0,
                "Two-step methods and equilibrium dialysis or mass spectrometry are less susceptible to binding-protein interference than one-step analogue assays.",
                ref(
                    "Free T4 and Free T3 Measurement",
                    "The use of a 2-step (\"back titration\") assay method (which is less susceptible to such interference), equilibrium dialysis, or mass spectrometry can be useful in confirming or excluding this possibility.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "RTH pitfalls",
                "In resistance to thyroid hormone, which pitfall can mislead thyrotropinoma evaluation?",
                [
                                        "Normal α-subunit always excludes pituitary tumor",
                    "Pituitary enlargement never occurs in RTH",
                    "Persistently elevated TSH after thyroid ablation can cause thyrotroph hyperplasia and pituitary enlargement",
                    "SHBG is always elevated in RTH",
],
                2,
                "Thyrotroph hyperplasia from chronic TSH elevation in RTH can mimic adenoma on imaging; ~15% of RTH lacks THRB variants.",
                ref(
                    "Resistance to Thyroid Hormone vs TSH-Secreting Pituitary Tumor",
                    "persistently elevated TSH levels following thyroid ablation in resistance to thyroid hormone results in thyrotroph hyperplasia and pituitary enlargement.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Levothyroxine physiology",
                "Physiological levothyroxine replacement may be associated with which laboratory pattern?",
                [
                                        "Suppressed TSH and low free T4",
                    "Mildly elevated free T4 with normal free T3",
                    "High TSH and low total T4",
                    "Isolated low free T3 only",
],
                1,
                "Differing hormone half-lives mean optimized TSH replacement can show mildly elevated free T4 while free T3 remains normal.",
                ref(
                    "Consider Potential Confounding Factors",
                    "Levothyroxine replacement in a physiological dosage to optimize TSH may be associated with mildly elevated free T4 (but normal free T3) levels in some patients.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "NTI",
                "During nonthyroidal illness, TFT interpretation requires:",
                [
                                        "Ignoring illness stage entirely",
                    "Recognition that multiple TFT patterns may occur depending on illness stage and assay",
                    "Mandatory thyroidectomy",
                    "Always starting levothyroxine",
],
                1,
                "NTI produces stage-dependent TFT patterns that must be distinguished from primary thyroid disease and assay artifacts.",
                ref(
                    "Consider Potential Confounding Factors",
                    "Nonthyroidal illness: Several different TFT patterns may be seen during nonthyroidal illness depending on the stage of the illness and laboratory assays used",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Pregnancy",
                "In pregnancy, TFT interpretation should ideally use:",
                [
                                        "Nonpregnant adult reference ranges only",
                    "Trimester-specific reference ranges wherever possible",
                    "Only total T3 measurements",
                    "TSH alone without free T4",
],
                1,
                "Thyroid hormone and TSH vary during normal pregnancy; trimester-specific ranges improve accuracy.",
                ref(
                    "Consider Potential Confounding Factors",
                    "Pregnancy: Thyroid hormone and TSH levels vary during normal pregnancy, and trimester-specific reference ranges should be used wherever possible.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Anti-animal antibodies",
                "Human anti-animal antibodies in TSH sandwich assays can cause:",
                [
                                        "Only falsely low TSH",
                    "Only falsely high TSH",
                    "Falsely low or falsely high TSH depending on mechanism",
                    "No interference whatsoever",
],
                2,
                "Blocking antibodies cause negative interference (low TSH); cross-linking antibodies cause positive interference (high TSH).",
                ref(
                    "TSH Measurement",
                    "a human anti-animal antibody that blocks TSH binding to either capture or detection antibodies will result in \"negative interference,\" causing a falsely low TSH value. Conversely, a human anti-animal antibody that is capable of cross-linking the capture and detection antibodies may cause \"positive interference,\" leading to a falsely high TSH value.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "TRH test",
                "Regarding the TRH test in thyrotropinoma evaluation:",
                [
                                        "All thyrotropinomas show absent TSH response",
                    "10% to 20% of TSH-secreting pituitary tumors may show apparent preserved TSH response",
                    "TRH always distinguishes RTH from thyrotropinoma definitively",
                    "TRH is first-line before excluding interference",
],
                1,
                "A subset of TSH-secreting tumors show preserved TRH response—another reason to integrate multiple tests after excluding interference.",
                ref(
                    "Resistance to Thyroid Hormone vs TSH-Secreting Pituitary Tumor",
                    "Thyrotropin-releasing hormone test: 10% to 20% of patients with TSH-secreting pituitary tumors show an apparent preserved TSH response.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Competition assays",
                "Free T4 immunoassays commonly use competition format because:",
                [
                                        "T4 is too large for sandwich assays",
                    "T4 is too small for sandwich assays",
                    "TSH blocks sandwich formation",
                    "Only total T4 can be measured",
],
                1,
                "The relatively small size of T4 and T3 precludes sandwich assay format; competition assays with conserved free hormone equilibrium are used instead.",
                ref(
                    "Free T4 and Free T3 Measurement",
                    "The relatively small size of T4 (and T3) precludes use of a \"sandwich\" assay format, so competition assays are commonly used.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Heparin artifact",
                "Postoperative low-molecular-weight heparin thromboprophylaxis can raise measured free T4 without raising total T4.",
                True,
                "Heparin displaces T4 from binding proteins in vitro, elevating free but not total hormone levels.",
                ref("Case 2", "thereby raising free, but not total, thyroid hormone levels."),
            ),
            tf(
                f"{p}-tf2",
                "Biotin scope",
                "Biotin interference is limited to thyroid hormone and TSH assays.",
                False,
                "Streptavidin-biotin platforms are used broadly; biotin can affect many assays beyond thyroid tests.",
                ref(
                    "Biotin (Vitamin B₇)",
                    "This issue can affect a multitude of assays, not simply thyroid hormone or TSH measurements.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "RTH incidence",
                "Resistance to thyroid hormone has an estimated incidence of approximately 1 in 40,000 to 50,000 live births.",
                True,
                "RTH is rare but must be considered after excluding more common causes of discordant TFTs.",
                ref(
                    "Resistance to Thyroid Hormone vs TSH-Secreting Pituitary Tumor",
                    "Resistance to thyroid hormone (estimated incidence 1 in 40,000 to 50,000 live births)",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Adherence pattern",
                "Erratic levothyroxine adherence can produce elevated T4 on the day of testing with persistently elevated TSH.",
                True,
                "A pre-test bolus dose can transiently normalize T4 while failing to correct chronic TSH elevation.",
                ref("Case 3", "especially if the patient takes a larger dosage of levothyroxine on the day(s) immediately before the blood test"),
            ),
            tf(
                f"{p}-tf5",
                "Thyrotropinoma prevalence",
                "TSH-secreting pituitary tumors have an estimated prevalence of 1 to 3 per million.",
                True,
                "Thyrotropinomas are far rarer than assay interference or adherence issues.",
                ref(
                    "Resistance to Thyroid Hormone vs TSH-Secreting Pituitary Tumor",
                    "TSH-secreting pituitary tumors (estimated prevalence 1 to 3 per million)",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Dilution testing",
                "Nonlinear TSH measurement following sample dilution suggests assay interference.",
                True,
                "Nonlinear dilution behavior is a standard laboratory clue to antibody interference.",
                ref(
                    "TSH Measurement",
                    "Nonlinear TSH measurement following sample dilution.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "SHBG in mixed tumors",
                "Serum SHBG may be falsely low in mixed GH/TSH-secreting pituitary tumors.",
                True,
                "GH inhibits SHBG synthesis, complicating use of SHBG to distinguish RTH from thyrotropinoma.",
                ref(
                    "Resistance to Thyroid Hormone vs TSH-Secreting Pituitary Tumor",
                    "SHBG: falsely low levels can occur in mixed GH/TSH-secreting tumors due to inhibition of SHBG synthesis by GH",
                ),
            ),
            tf(
                f"{p}-tf8",
                "THRB testing",
                "Approximately 15% of resistance to thyroid hormone cases lack pathogenic THRB variants.",
                True,
                "Negative THRB testing does not fully exclude RTH.",
                ref(
                    "Resistance to Thyroid Hormone vs TSH-Secreting Pituitary Tumor",
                    "THRB gene analysis: Approximately 15% of cases of resistance to thyroid hormone are not associated with THRB pathogenic variants.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Case 1 priority",
                "Assertion: In suspected thyrotoxicosis with nonsuppressed TSH, laboratory advice should precede pituitary MRI.",
                "Reason: Because TSH may be artifactually elevated while true primary thyrotoxicosis exists with suppressed TSH.",
                0,
                "Both true and causally linked—interference must be excluded before costly pituitary investigation.",
                ref("Case 1", "Thus, seeking advice on further laboratory analyses (Answer E) is correct."),
            ),
            ar(
                f"{p}-ar2",
                "Heparin artifact",
                "Assertion: Normal total T4 with elevated free T4 and normal TSH argues against genuine thyrotoxicosis.",
                "Reason: Because heparin raises total T4 more than free T4 via lipoprotein lipase activation.",
                2,
                "Assertion true; reason false—heparin raises free but not total T4.",
                ref("Case 2", "subsequent investigations on the same serum sample show an entirely normal total T₄ level."),
            ),
            ar(
                f"{p}-ar3",
                "Sandwich interference",
                "Assertion: Human anti-animal antibodies can cause falsely high TSH in sandwich assays.",
                "Reason: Because such antibodies may cross-link capture and detection antibodies.",
                0,
                "Both true—cross-linking produces positive interference.",
                ref(
                    "TSH Measurement",
                    "a human anti-animal antibody that is capable of cross-linking the capture and detection antibodies may cause \"positive interference,\" leading to a falsely high TSH value.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Levothyroxine adherence",
                "Assertion: Poor levothyroxine adherence can yield upper-range free T4 with elevated TSH.",
                "Reason: Because intermittent large doses before blood draw can transiently elevate serum T4 without normalizing TSH.",
                0,
                "Both true and causally linked per Case 3 explanation.",
                ref("Case 3", "could produce this pattern of results, especially if the patient takes a larger dosage of levothyroxine on the day(s) immediately before the blood test"),
            ),
            ar(
                f"{p}-ar5",
                "FDH assays",
                "Assertion: FDH can cause overestimated free T4 on one-step analogue assays.",
                "Reason: Because variant albumin has increased affinity for iodothyronines, elevating measured free hormone.",
                0,
                "Both true—altered binding protein affinity confounds one-step free hormone assays.",
                ref(
                    "Free T4 and Free T3 Measurement",
                    "may alter affinity for iodothyronines, and can cause free T4 (and less frequently free T3) to be overestimated, particularly in \"1-step\" analogue hormone assays.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Misdirected workup",
                "Assertion: Failure to recognize assay interference leads to wasteful investigation.",
                "Reason: Because all discordant TFTs ultimately require thyroidectomy.",
                2,
                "Assertion true; reason false—interference causes misdirected testing, not universal surgery.",
                ref(
                    "Significance of the Clinical Problem",
                    "Misdirected investigation of these entities results in wastage of resources and/or incorrect therapeutic intervention.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "RTH imaging",
                "Assertion: Pituitary imaging abnormalities may occur in resistance to thyroid hormone.",
                "Reason: Because chronic TSH elevation after thyroid ablation can cause thyrotroph hyperplasia.",
                0,
                "Both true—RTH can mimic tumor on imaging.",
                ref(
                    "Resistance to Thyroid Hormone vs TSH-Secreting Pituitary Tumor",
                    "persistently elevated TSH levels following thyroid ablation in resistance to thyroid hormone results in thyrotroph hyperplasia and pituitary enlargement.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Amiodarone",
                "Assertion: Medications such as amiodarone can alter thyroid physiology or cause artifactual results.",
                "Reason: Because amiodarone only affects TSH sandwich assays via biotin.",
                2,
                "Assertion true; reason false—amiodarone alters physiology (iodine) and is listed among confounding medications.",
                ref(
                    "Consider Potential Confounding Factors",
                    "Medications and supplements have the potential to alter thyroid physiology (eg, amiodarone) or cause artifactual laboratory results (eg, heparin or biotin—see below).",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "38",
        "title": "When Thyroid Function Test Results Dont Make Sense",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Mark Gurnell, MD, PhD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_38_When_Thyroid_Function_Test_Results_Dont_Make_Sense.md",
        "items": items,
    }


def build_chapter_39() -> dict:
    p = "e21-39"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Surveillance imaging",
                "Why neck ultrasonography is primary after hemithyroidectomy",
                "After hemithyroidectomy for low-risk differentiated thyroid cancer, surveillance is primarily with neck ultrasonography; optimal long-term imaging frequency remains unknown.",
                ref(
                    "Main Conclusions",
                    "Imaging surveillance after hemithyroidectomy is primarily with neck ultrasonography. Optimal frequency of follow-up is unknown.",
                ),
            ),
            note(
                f"{p}-n2",
                "Thyroglobulin thresholds",
                "How dynamic risk stratification differs after hemithyroidectomy",
                "Modified dynamic risk stratification uses nonstimulated thyroglobulin less than 30 ng/mL to define excellent response—different from total thyroidectomy thresholds; trend over time matters more than a single value.",
                ref(
                    "Significance of the Clinical Problem",
                    "modified dynamic risk stratification has been developed, which has a thyroglobulin threshold of less than 30 ng/mL (<30 μg/L) to define an excellent response to therapy",
                ),
            ),
            note(
                f"{p}-n3",
                "Thyroglobulin pitfalls",
                "Why detectable thyroglobulin does not always mean recurrence",
                "Thyroglobulin is produced by normal and malignant thyroid tissue; detectable levels after lobectomy may reflect remnant normal tissue, and levels can rise ~10% per year without recurrence.",
                ref(
                    "Significance of the Clinical Problem",
                    "Detectable thyroglobulin does not always indicate recurrence of thyroid cancer, and it may indicate the presence of normal thyroid tissue.",
                ),
            ),
            note(
                f"{p}-n4",
                "Levothyroxine need",
                "How often patients require thyroid hormone after lobectomy",
                "Many patients choose hemithyroidectomy to avoid lifelong levothyroxine, but 50% to 71% require thyroid hormone to achieve goal TSH less than 2.0 mIU/L for most response categories.",
                ref(
                    "Significance of the Clinical Problem",
                    "studies have shown that in order for patients to attain goal TSH (<2.0 mIU/L for most patients based on response to therapy), 50% to 71% of patients require some amount of thyroid hormone therapy.",
                ),
            ),
            note(
                f"{p}-n5",
                "Preoperative imaging",
                "Why preoperative neck ultrasonography is essential",
                "Thorough preoperative imaging of thyroid and central/lateral neck guides initial surgery extent and establishes baseline for postoperative surveillance; missing preoperative imaging should be completed postoperatively.",
                ref(
                    "Significance of the Clinical Problem",
                    "Thorough preoperative imaging of both the thyroid and central and lateral neck compartments is essential when evaluating persons with suspicious thyroid nodules",
                ),
            ),
            note(
                f"{p}-n6",
                "False-positive US",
                "Pitfall: over-monitoring from false-positive surveillance ultrasound",
                "False-positive findings on surveillance ultrasonography occur in 57% to 67% of low- and intermediate-risk patients, risking unnecessary procedures.",
                ref(
                    "Significance of the Clinical Problem",
                    "studies have shown that false-positive findings on surveillance ultrasonography can occur in 57% to 67% of patients at low and intermediate risk.",
                ),
            ),
            note(
                f"{p}-n7",
                "Tg antibodies",
                "How thyroglobulin antibodies interfere with tumor marker use",
                "Thyroglobulin antibodies interfere with the immunoassay and confound interpretation of serum thyroglobulin as a tumor marker—use the same assay serially when monitoring.",
                ref(
                    "Barriers to Optimal Practice",
                    "The presence of thyroglobulin antibodies interferes with the thyroglobulin immunoassay and interferes with the interpretation of serum thyroglobulin as a tumor marker.",
                ),
            ),
            note(
                f"{p}-n8",
                "Case 1 management",
                "How to manage rising thyroglobulin with negative neck imaging after lobectomy",
                "With negative neck imaging and TSH above goal 0.5–2.0 mIU/L off levothyroxine, start low-dose levothyroxine; if opposed to hormone, short-interval surveillance with consistent Tg assay is reasonable.",
                ref(
                    "Case 1",
                    "Therefore, starting low-dosage levothyroxine (Answer C) is recommended, with follow-up measurement of TSH, thyroglobulin, and thyroglobulin antibodies.",
                ),
            ),
            note(
                f"{p}-n9",
                "Case 3 low risk",
                "What surveillance is appropriate after low-risk FVPTC hemithyroidectomy",
                "For low-risk follicular variant papillary carcinoma with negative contralateral lobe and nodes: neck US at 6 months, TSH measurement with levothyroxine if TSH above goal, and selective thyroglobulin monitoring.",
                ref(
                    "Case 3",
                    "Answer: A, B, and possibly C) TSH measurement and thyroid hormone therapy if TSH is >2.0 mIU/L, neck ultrasonography, and possibly measurement of thyroglobulin and thyroglobulin antibodies",
                ),
            ),
            note(
                f"{p}-n10",
                "Hobnail variant",
                "Why hobnail papillary carcinoma requires completion thyroidectomy",
                "Hobnail variants are ATA intermediate-risk aggressive histology associated with extrathyroidal extension and nodal metastases—completion thyroidectomy and possible radioactive iodine are recommended.",
                ref(
                    "Case 4",
                    "Hobnail variants are in the American Thyroid Association intermediate risk of recurrence category and are considered to be aggressive histologic types.",
                ),
            ),
            note(
                f"{p}-n11",
                "Extranodal extension",
                "How extranodal extension changes management after lobectomy",
                "Extranodal extension is a risk factor for structural recurrence; with central neck nodal metastasis and extranodal extension, completion thyroidectomy with central neck dissection is preferred.",
                ref(
                    "Case 5",
                    "Extranodal extension is considered a risk factor for structural disease recurrence",
                ),
            ),
            note(
                f"{p}-n12",
                "Angioinvasive follicular",
                "When angioinvasive follicular carcinoma requires completion therapy",
                "High-risk angioinvasive follicular thyroid carcinoma is an indication for adjuvant radioactive iodine at diagnosis; continued surveillance alone is inadequate—many clinicians choose completion thyroidectomy with adjuvant RAI.",
                ref(
                    "Case 2",
                    "High-risk angioinvasive follicular thyroid carcinoma is an indication for adjuvant radioactive iodine therapy at the time of diagnosis.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "One year after left lobectomy for 1.2-cm papillary carcinoma, TSH 2.7 mIU/L off levothyroxine, stable 4-mm right spongiform nodule, Tg 75 ng/mL on different assay. Best next step?",
                [
                                        "Chest CT for metastatic disease",
                    "FNA of right thyroid nodule",
                    "Initiate levothyroxine 50 mcg daily",
                    "Observation with US, Tg, TgAb, and TFT in 6 months",
],
                2,
                "Negative neck imaging with TSH above goal favors starting low-dose levothyroxine; if hormone-averse, Answer D with same Tg assay is acceptable.",
                ref("Case 1", "Answer: C or D) Initiation of levothyroxine, 50 mcg daily or continued observation"),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "After hemithyroidectomy, pathology reveals high-risk angioinvasive follicular thyroid carcinoma. Best management?",
                [
                                        "Continued surveillance alone",
                    "Completion thyroidectomy with adjuvant radioactive iodine",
                    "Levothyroxine only with TSH 0.5–2.0 mIU/L",
                    "131I whole-body scan before any surgery",
],
                1,
                "Angioinvasive follicular carcinoma warrants completion thyroidectomy and adjuvant RAI; surveillance alone is inadequate.",
                ref(
                    "Case 2",
                    "many clinicians would choose completion thyroidectomy with adjuvant radioactive iodine (Answer B)",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3",
                "Six months after hemithyroidectomy for 1.8-cm encapsulated FVPTC without vascular invasion, appropriate actions include:",
                [
                                        "TSH measurement and levothyroxine if TSH >2.0 mIU/L",
                    "Neck ultrasonography",
                    "Routine chest CT",
                    "Completion thyroidectomy and RAI",
],
                0,
                "Answers A, B, and possibly E—low-risk disease does not need completion therapy or chest CT.",
                ref("Case 3", "Answer: A, B, and possibly C)"),
            ),
            mcq(
                f"{p}-q4",
                "Case 4",
                "Post-lobectomy hobnail variant papillary carcinoma. Recommended now?",
                [
                                        "Molecular testing to guide therapy",
                    "Measure Tg and TgAb only",
                    "Observation for 6 months",
                    "Completion thyroidectomy and consideration of RAI",
],
                3,
                "Aggressive hobnail histology warrants completion thyroidectomy and possible RAI; observation is not preferred.",
                ref("Case 4", "Answer: E) Completion thyroidectomy and consideration of radioactive iodine"),
            ),
            mcq(
                f"{p}-q5",
                "Case 5",
                "After right lobectomy for toxic nodule, pathology shows papillary carcinoma with 9-mm nodal metastasis and extranodal extension without formal central neck dissection. Best next step?",
                [
                                        "Observation with US and Tg in 6–12 weeks",
                    "Completion thyroidectomy alone",
                    "Completion thyroidectomy with central neck dissection",
                    "TSH suppression with levothyroxine alone",
],
                2,
                "T2N1a with extranodal extension and incomplete nodal staging requires completion thyroidectomy with central neck dissection and consideration of RAI.",
                ref("Case 5", "Answer: C) Completion thyroidectomy with central neck dissection"),
            ),
            mcq(
                f"{p}-q6",
                "Excellent response TSH",
                "After hemithyroidectomy with excellent response (Tg <30 ng/mL), TSH goal is:",
                [
                                        "<0.1 mIU/L",
                    "0.1–0.5 mIU/L",
                    "0.5–2.0 mIU/L",
                    "2.5–4.0 mIU/L",
],
                2,
                "Modified dynamic risk stratification sets TSH 0.5–2.0 mIU/L for excellent response after hemithyroidectomy.",
                ref(
                    "Significance of the Clinical Problem",
                    "Nonstimulated thyroglobulin <30 ng/mL (SI: <30 μg/L) ... TSH Goals ... 0.5-2.0 mIU/L",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Indeterminate response",
                "Indeterminate response after lobectomy (stable/declining TgAb, Tg not defining) targets TSH:",
                [
                                        "<0.1 mIU/L",
                    "0.1–0.5 mIU/L",
                    "0.5–2.0 mIU/L",
                    "2.0–4.0 mIU/L",
],
                1,
                "Indeterminate response category uses TSH 0.1–0.5 mIU/L per modified hemithyroidectomy table.",
                ref(
                    "Significance of the Clinical Problem",
                    "Stable or declining thyroglobulin antibody levels ... 0.1-0.5 mIU/L",
                ),
            ),
            mcq(
                f"{p}-q8",
                "NIFT-P",
                "If hemithyroidectomy pathology were NIFT-P with normal contralateral lobe and nodes:",
                [
                                        "Mandatory completion thyroidectomy",
                    "Routine chest CT",
                    "Mandatory Tg every 3 months",
                    "No routine Tg; maintain normal TSH without levothyroxine goal <2.0",
],
                3,
                "NIFT-P has very low malignant potential; many clinicians omit routine Tg and do not treat to TSH <2.0.",
                ref(
                    "Case 3 (Continued)",
                    "treating with levothyroxine for a goal TSH less than 2.0 IU/L is not necessary.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Vascular invasion",
                "Microscopic vascular invasion on lobectomy pathology implies:",
                [
                                        "Excellent response category only",
                    "Intermediate ATA recurrence risk; consider completion thyroidectomy ± RAI",
                    "No further therapy ever",
                    "Immediate external beam radiation only",
],
                1,
                "Vascular invasion classifies intermediate risk (~15%–30% structural recurrence); completion thyroidectomy should be considered.",
                ref(
                    "Case 3 (Continued)",
                    "If the tumor had vascular invasion, then it would be classified at intermediate risk of structural recurrence according to the American Thyroid Association classification (approximately 15%-30%).",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Preoperative counseling",
                "Before hemithyroidectomy, clinicians should discuss:",
                [
                                        "Only surgical scar cosmesis",
                    "Postoperative surveillance, Tg monitoring, and possibility of needing levothyroxine",
                    "That levothyroxine is never needed after lobectomy",
                    "That RAI is always required",
],
                1,
                "Preoperative discussion must cover surveillance plan, bilateral nodularity implications, and realistic levothyroxine expectations.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "There should also be discussion regarding preference for thyroid hormone therapy. Many patients assume they will not need thyroid hormone if they have a hemithyroidectomy.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Rising Tg",
                "If thyroglobulin rises after lobectomy, next step includes:",
                [
                                        "Ignore if patient feels well",
                    "Neck ultrasonography and consider TSH suppression to 0.1–0.5 mIU/L",
                    "Immediate total body PET only",
                    "Stop all surveillance",
],
                1,
                "Rising Tg prompts neck imaging and may warrant levothyroxine adjustment toward indeterminate-response TSH goals.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "If thyroglobulin is rising, the neck should be imaged with ultrasonography.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Completion indications",
                "Completion thyroidectomy is recommended when initial hemithyroidectomy patient:",
                [
                                        "Has low-risk microcarcinoma only",
                    "Meets criteria for radioactive iodine therapy",
                    "Has negative Tg always",
                    "Refuses all imaging",
],
                1,
                "If criteria for RAI are met, completion thyroidectomy ± central neck dissection is recommended.",
                ref(
                    "Main Conclusions",
                    "If a patient meets criteria for radioactive iodine, then completion thyroidectomy ± central neck dissection is recommended.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Assay consistency",
                "When serially monitoring thyroglobulin after lobectomy:",
                [
                                        "Any laboratory assay is interchangeable",
                    "The same assay should be used each time",
                    "Only stimulated Tg is valid",
                    "Tg is never useful after lobectomy",
],
                1,
                "Tg values vary between assays and must be evaluated using the same assay every time.",
                ref(
                    "Barriers to Optimal Practice",
                    "Thyroglobulin values can vary between assays, so they must be evaluated using the same assay every time.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "US primary",
                "Imaging surveillance after hemithyroidectomy is primarily performed with neck ultrasonography.",
                True,
                "ATA approach emphasizes neck US as the main surveillance modality after lobectomy.",
                ref("Main Conclusions", "Imaging surveillance after hemithyroidectomy is primarily with neck ultrasonography."),
            ),
            tf(
                f"{p}-tf2",
                "Tg excellent",
                "Nonstimulated thyroglobulin less than 30 ng/mL defines excellent response after hemithyroidectomy.",
                True,
                "Modified dynamic risk stratification uses this threshold distinct from total thyroidectomy criteria.",
                ref(
                    "Significance of the Clinical Problem",
                    "a thyroglobulin threshold of less than 30 ng/mL (<30 μg/L) to define an excellent response to therapy",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Levothyroxine rates",
                "More than half of patients may need levothyroxine after lobectomy to reach goal TSH.",
                True,
                "50%–71% require thyroid hormone to achieve TSH goals in studies cited.",
                ref(
                    "Significance of the Clinical Problem",
                    "50% to 71% of patients require some amount of thyroid hormone therapy.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Tg trend",
                "A rising thyroglobulin over time is more predictive of recurrence than a single stable value.",
                True,
                "Trend analysis outweighs isolated measurements; gradual rise without recurrence can still occur.",
                ref(
                    "Significance of the Clinical Problem",
                    "A rising thyroglobulin level over time is more predictive of recurrence than one that is stable or dropping.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "No levothyroxine Tg rise",
                "If a patient does not take thyroid hormone after lobectomy, TSH elevation may raise thyroglobulin without cancer recurrence.",
                True,
                "Lack of levothyroxine can increase Tg from remnant tissue stimulation.",
                ref(
                    "Barriers to Optimal Practice",
                    "If a patient does not take thyroid hormone, this may cause a rise in thyroglobulin without recurrence.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Subcentimeter nodule FNA",
                "In Case 1, FNA of a stable subcentimeter very-low-risk spongiform nodule is recommended.",
                False,
                "Stable low-risk subcentimeter nodule does not meet FNA criteria; neck imaging is negative.",
                ref("Case 1", "This is a low-risk nodule sonographically and it is subcentimeter in size. Hence, FNA (Answer B) would not be recommended."),
            ),
            tf(
                f"{p}-tf7",
                "Hobnail observation",
                "Observation alone is preferred for hobnail variant papillary carcinoma after initial lobectomy.",
                False,
                "Higher recurrence risk mandates completion thyroidectomy and possible RAI.",
                ref("Case 4", "Observation (Answer D) is not preferred because the potential higher risk of recurrence."),
            ),
            tf(
                f"{p}-tf8",
                "131I before completion",
                "131I whole-body scan is recommended before completion thyroidectomy with remaining thyroid lobe.",
                False,
                "Whole-body scan is not recommended before completion when a thyroid lobe remains.",
                ref("Case 2", "131 I whole-body scan (Answer D) would not be recommended before completion thyroidectomy."),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Tg threshold",
                "Assertion: Excellent response after hemithyroidectomy includes nonstimulated Tg <30 ng/mL.",
                "Reason: Because this threshold is identical to total thyroidectomy plus RAI criteria.",
                2,
                "Assertion true; reason false—hemithyroidectomy uses modified thresholds.",
                ref(
                    "Main Conclusions",
                    "Dynamic risk stratification after hemithyroidectomy has different thyroglobulin thresholds that define response to therapy as compared with thresholds of persons who have undergone total thyroidectomy.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Levothyroxine expectation",
                "Assertion: Many hemithyroidectomy patients ultimately need levothyroxine.",
                "Reason: Because 50% to 71% require hormone to achieve goal TSH.",
                0,
                "Both true and directly linked in cited studies.",
                ref(
                    "Significance of the Clinical Problem",
                    "50% to 71% of patients require some amount of thyroid hormone therapy.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Case 1 Tg assay",
                "Assertion: Different thyroglobulin assay limits direct comparison to prior values.",
                "Reason: Because thyroglobulin assays are standardized internationally with no variation.",
                2,
                "Assertion true per Case 1; reason false—assay variation is a known barrier.",
                ref("Case 1", "Thyroglobulin was measured using a different assay, making it difficult to directly compare"),
            ),
            ar(
                f"{p}-ar4",
                "False-positive US",
                "Assertion: Serial neck ultrasound may identify false-positive findings in low-risk patients.",
                "Reason: Because ultrasound has no role after hemithyroidectomy.",
                2,
                "Assertion true; reason false—US is primary surveillance but can overcall disease.",
                ref(
                    "Significance of the Clinical Problem",
                    "false-positive findings on surveillance ultrasonography can occur in 57% to 67% of patients at low and intermediate risk.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Extranodal extension",
                "Assertion: Extranodal extension increases structural recurrence risk.",
                "Reason: Because it mandates levothyroxine alone without surgery.",
                2,
                "Assertion true; reason false—completion surgery with nodal dissection is preferred.",
                ref("Case 5", "Extranodal extension is considered a risk factor for structural disease recurrence"),
            ),
            ar(
                f"{p}-ar6",
                "Low-risk FVPTC",
                "Assertion: Low-risk FVPTC after lobectomy does not require completion thyroidectomy.",
                "Reason: Because contralateral lobe and nodes were normal without high-risk histology.",
                0,
                "Both true for Case 3—completion and RAI not recommended.",
                ref("Case 3", "completion thyroidectomy or radioactive iodine therapy (Answer E) would not be recommended."),
            ),
            ar(
                f"{p}-ar7",
                "TgAb interference",
                "Assertion: Thyroglobulin antibodies interfere with Tg immunoassay interpretation.",
                "Reason: Because TgAb always indicates active recurrence.",
                2,
                "Assertion true; reason false—TgAb interferes with assay but does not always mean recurrence.",
                ref(
                    "Barriers to Optimal Practice",
                    "The presence of thyroglobulin antibodies interferes with the thyroglobulin immunoassay and interferes with the interpretation of serum thyroglobulin as a tumor marker.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "RAI criteria",
                "Assertion: Patients meeting RAI criteria after initial lobectomy should undergo completion thyroidectomy.",
                "Reason: Because RAI can be given effectively with a full thyroid lobe remaining without surgery.",
                2,
                "Assertion true per guidelines; reason false—completion is needed for RAI in most protocols.",
                ref(
                    "Main Conclusions",
                    "If a patient meets criteria for radioactive iodine, then completion thyroidectomy ± central neck dissection is recommended.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "39",
        "title": "Surveillance of the Patient Who Has Had Therapeutic Hemithyroidectomy for Thyroid Cancer",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Whitney Goldner, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_39_Surveillance_of_the_Patient_Who_Has_Had_Therapeutic_Hemithyroidectomy_for_Thyroid_Cancer.md",
        "items": items,
    }
def build_chapter_40() -> dict:
    p = "e21-40"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Pregnancy TSH cutoff",
                "Why the pregnancy TSH upper limit was revised to 4 mIU/L",
                "Accumulating evidence shows levothyroxine for TSH below 4 mIU/L does not necessarily improve obstetric or neurocognitive outcomes and may cause harm; when trimester-specific ranges are unavailable, 4 mIU/L is the suggested cutoff.",
                ref(
                    "Definition of Thyroid Dysfunction Before and During Pregnancy",
                    "If no suitable generalizable ranges can be found, then current guidance suggests the use of 4 mIU/L as the cutoff for TSH concentrations during pregnancy. The previous pragmatic upper limit of normal of 2.5 mIU/L is now deemed too low.",
                ),
            ),
            note(
                f"{p}-n2",
                "TABLET trial",
                "Why levothyroxine does not help euthyroid TPO-positive women",
                "The TABLET trial found no benefit of 50 mcg levothyroxine vs placebo on live birth or other pregnancy outcomes in euthyroid women with raised TPO antibodies—TPO effects may reflect generalized autoimmunity rather than thyroid dysfunction.",
                ref(
                    "Levothyroxine Replacement in Euthyroid TPO-Positive Women Before and During Pregnancy",
                    "The live birth rate at 34 weeks' gestation was 37.4% in the levothyroxine group and 37.9% in the placebo group (relative risk, 0.97 [95% CI, 0.83-1.14]; P = .74).",
                ),
            ),
            note(
                f"{p}-n3",
                "Subclinical hypothyroidism",
                "How to treat subclinical hypothyroidism in pregnancy",
                "Insufficient evidence to treat all women with TSH 2.5–4 mIU/L; consider levothyroxine when TPO positive with TSH >4, TPO negative with TSH >10, infertility/recurrent loss, or other risk factors.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "there is insufficient evidence to universally treat pregnant women with serum TSH values between 2.5 and 4 mIU/L regardless of TPO antibody status. Levothyroxine should be considered in women who are TPO positive and have serum TSH values greater than 4.0 mIU/L",
                ),
            ),
            note(
                f"{p}-n4",
                "Overtreatment risk",
                "Pitfall: overzealous levothyroxine in mild subclinical hypothyroidism",
                "Observational data show levothyroxine benefit mainly when TSH >4 mIU/L, but treatment of lower values may increase premature delivery, gestational diabetes, and preeclampsia risks.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "Importantly, the beneficial effects of levothyroxine replacement were predominantly present in the subgroup of women with TSH values greater than 4.0 mIU/L.",
                ),
            ),
            note(
                f"{p}-n5",
                "CATS trial",
                "Why antenatal screening trials showed no IQ benefit",
                "CATS and the US multicenter trial initiated levothyroxine at median 13–18 weeks and found no child IQ differences at 3–9 years; late initiation and possible overtreatment may explain negative results.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "At 3 years, IQ scores were not different in offspring from treated vs nontreated women.",
                ),
            ),
            note(
                f"{p}-n6",
                "Hyperthyroidism pregnancy",
                "How to manage Graves disease before pregnancy",
                "Counsel on fetal harm from uncontrolled hyperthyroidism; achieve euthyroid state before conception; switch methimazole to PTU in early pregnancy due to teratogenicity window weeks 6–10.",
                ref(
                    "Management of Hyperthyroidism Before and During Pregnancy",
                    "since this is associated with a higher risk of teratogenicity than propylthiouracil, the latter is usually preferred before and during the first 16 weeks of pregnancy.",
                ),
            ),
            note(
                f"{p}-n7",
                "Gestational thyrotoxicosis",
                "How to distinguish Graves disease from gestational thyrotoxicosis",
                "New early-pregnancy thyrotoxicosis requires TRAb and free T3—elevated in Graves but not in hCG-mediated gestational thyrotoxicosis, which is usually supportive care.",
                ref(
                    "Management of Hyperthyroidism Before and During Pregnancy",
                    "Measurement of TSH-receptor antibodies (TRAb) and free T3 concentrations are informative, as they will be raised in the former but not in the latter.",
                ),
            ),
            note(
                f"{p}-n8",
                "Case 1",
                "How to manage TPO-positive subclinical hypothyroidism with recurrent miscarriage",
                "TSH 4.2 mIU/L with TPO 350 IU/mL after recurrent loss: repeat TFT in 4 weeks or start low-dose levothyroxine 25–50 mcg daily is reasonable.",
                ref(
                    "Case 1",
                    "Answer: B or E) Repeat thyroid function tests after 4 weeks or start levothyroxine, 25 to 50 mcg daily",
                ),
            ),
            note(
                f"{p}-n9",
                "Isolated hypothyroxinemia",
                "Why isolated hypothyroxinemia treatment is controversial",
                "RCTs show no obstetric or neurocognitive benefit; ATA does not recommend treatment whereas European guidance may consider first-trimester therapy—repeating TFTs is reasonable.",
                ref(
                    "Case 2",
                    "Current American Thyroid Association guidelines do not recommend treatment of this condition, whereas European guidance suggests that treatment may be considered in the first trimester of pregnancy.",
                ),
            ),
            note(
                f"{p}-n10",
                "Preconception Graves",
                "What to advise women with Graves wishing to conceive on methimazole",
                "Switch to PTU, or consider definitive radioiodine or thyroidectomy; continuing methimazole or stopping antithyroid drugs abruptly is inappropriate.",
                ref(
                    "Case 3",
                    "Answer: B, C, or D) Change to propylthiouracil, 300 mg twice daily or advise radioiodine therapy or advise total thyroidectomy",
                ),
            ),
            note(
                f"{p}-n11",
                "Alemtuzumab Graves",
                "How to manage refractory Graves in second-trimester pregnancy",
                "After failed high-dose PTU, switch to methimazole in second trimester or pursue urgent thyroidectomy around 18–20 weeks; do not terminate pregnancy or rely on glucocorticoids alone.",
                ref(
                    "Case 4",
                    "Answer: B or C) Change propylthiouracil to methimazole, 80 mg daily, OR recommend urgent thyroidectomy at 18 to 20 weeks' gestation",
                ),
            ),
            note(
                f"{p}-n12",
                "Case 5 prepregnancy",
                "How to counsel TPO-positive euthyroid woman before conception",
                "TPO 320 IU/mL with TSH 2.4 mIU/L and recurrent miscarriage: repeat TSH monitoring before/during early pregnancy or consider low-dose levothyroxine given autoimmunity and loss history.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "Levothyroxine should be considered in women who are TPO positive and have serum TSH values greater than 4.0 mIU/L",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "8 weeks pregnant with 3 prior miscarriages, TSH 4.2 mIU/L, normal free T4, TPO 350 IU/mL. Best advice?",
                [
                                        "Reassure and routine antenatal care only",
                    "Repeat TFT at 20 weeks only",
                    "Start levothyroxine 1.6 mcg/kg daily",
                    "Start levothyroxine 25–50 mcg daily",
],
                3,
                "TPO positive with TSH >4 and recurrent loss supports low-dose levothyroxine; repeating TFT in 4 weeks (Answer B) is also appropriate.",
                ref("Case 1", "Answer: B or E) Repeat thyroid function tests after 4 weeks or start levothyroxine, 25 to 50 mcg daily"),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 alternative",
                "Same patient prefers to defer medication initially. Also acceptable:",
                [
                                        "Discharge without any thyroid follow-up",
                    "Repeat thyroid function tests after 4 weeks",
                    "Start methimazole",
                    "Radioiodine ablation",
],
                1,
                "Repeat TFT in 4 weeks is appropriate regardless of whether levothyroxine is started.",
                ref("Case 1", "Repeating thyroid function testing after 4 weeks (Answer B) is appropriate regardless of whether levothyroxine is started."),
            ),
            mcq(
                f"{p}-q3",
                "Case 2",
                "13 weeks pregnant, TSH 1.4, free T4 0.6 ng/dL, TPO negative—isolated hypothyroxinemia. Reasonable approach?",
                [
                                        "Urgent 9-AM cortisol",
                    "Repeat TFT after 4 weeks or start levothyroxine 25–50 mcg",
                    "Start 1.6 mcg/kg levothyroxine immediately",
                    "Measure free T3 and treat only if low",
],
                1,
                "Isolated hypothyroxinemia: repeat testing or optional low-dose levothyroxine per regional guidance; cortisol not indicated.",
                ref("Case 2", "Answer: C or E) Repeat thyroid function tests after 4 weeks or start levothyroxine, 25 to 50 mcg daily"),
            ),
            mcq(
                f"{p}-q4",
                "Case 3",
                "Woman with controlled Graves on methimazole wishes to conceive. Appropriate options include:",
                [
                                        "Continue methimazole unchanged",
                    "Switch to propylthiouracil",
                    "Radioiodine therapy with 6-month pregnancy deferral",
                    "Total thyroidectomy",
],
                1,
                "PTU preferred before/early pregnancy; definitive therapy also appropriate; stopping ATDs or continuing methimazole alone is less preferred.",
                ref("Case 3", "Answer: B, C, or D)"),
            ),
            mcq(
                f"{p}-q5",
                "Case 4",
                "14 weeks pregnant, alemtuzumab-associated refractory Graves on high-dose PTU with persistent thyrotoxicosis. Best advice?",
                [
                                        "Increase PTU to 400 mg three times daily",
                    "Switch to methimazole or urgent thyroidectomy at 18–20 weeks",
                    "Terminate pregnancy",
                    "Glucocorticoids alone",
],
                1,
                "Second-trimester teratogenicity risk for methimazole is lower; thyroidectomy around 18–20 weeks if drugs fail.",
                ref("Case 4", "Answer: B or C)"),
            ),
            mcq(
                f"{p}-q6",
                "Case 5",
                "Prepregnancy counseling: TSH 2.4 mIU/L, TPO 320 IU/mL, 2 prior first-trimester losses. Best approach?",
                [
                                        "No thyroid follow-up needed",
                    "Repeat TSH before/during early pregnancy or consider levothyroxine",
                    "Immediate radioiodine",
                    "Methimazole 30 mg daily",
],
                1,
                "Below 4 mIU/L but TPO positive with miscarriage history warrants monitoring or individualized levothyroxine consideration.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "those with infertility or recurrent pregnancy loss.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "TSH cutoff",
                "When pregnancy-specific TSH ranges are unavailable, upper limit for TSH is:",
                [
                                        "2.5 mIU/L",
                    "3.0 mIU/L",
                    "4.0 mIU/L",
                    "10.0 mIU/L only",
],
                2,
                "Current guidance uses 4 mIU/L; prior 2.5 mIU/L cutoff is now deemed too low.",
                ref(
                    "Definition of Thyroid Dysfunction Before and During Pregnancy",
                    "current guidance suggests the use of 4 mIU/L as the cutoff for TSH concentrations during pregnancy.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "TABLET",
                "TABLET trial primary outcome in euthyroid TPO-positive women showed:",
                [
                                        "Large increase in live births with levothyroxine",
                    "No significant difference in live births vs placebo",
                    "Reduced preterm birth only",
                    "Improved child IQ at 3 years",
],
                1,
                "Live birth rates were nearly identical between levothyroxine and placebo groups.",
                ref(
                    "Levothyroxine Replacement in Euthyroid TPO-Positive Women Before and During Pregnancy",
                    "The live birth rate at 34 weeks' gestation was 37.4% in the levothyroxine group and 37.9% in the placebo group",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Overt hypothyroidism",
                "Overt hypothyroidism in pregnancy (high TSH, low free T4) requires:",
                [
                                        "No treatment until postpartum",
                    "Timely levothyroxine with preconception/first-trimester TSH target up to 2.5 mIU/L",
                    "Propylthiouracil",
                    "Observation only if TPO negative",
],
                1,
                "Overt disease associates with miscarriage, preeclampsia, and neurodevelopmental harm—treat promptly with trimester monitoring.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "The preconception and first trimester of pregnancy TSH target is between the lower reference limit and 2.5 mIU/L.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Levothyroxine dose",
                "On positive pregnancy test, levothyroxine-treated women are often advised to:",
                [
                                        "Halve their dose immediately",
                    "Empirically increase dose (e.g., double dose 2 days per week)",
                    "Stop levothyroxine until 20 weeks",
                    "Switch to liothyronine only",
],
                1,
                "Pregnancy increases thyroid hormone requirements; empirical dose increase and TFT every 4 weeks in first half are recommended.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "An empirical increase in the dosage of levothyroxine upon finding of a positive pregnancy test is appropriate, and often women are advised to double the dose on 2 days of the week.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Hypothyroxinemia RCTs",
                "RCTs of levothyroxine for gestational isolated hypothyroxinemia showed:",
                [
                                        "Clear IQ benefit at 9 years",
                    "No demonstrated child neurocognitive benefit",
                    "Mandatory treatment per all guidelines",
                    "Increased live birth only",
],
                1,
                "CATS and US trial found no IQ benefit; treatment generally not recommended.",
                ref(
                    "Isolated Hypothyroxinemia During Pregnancy",
                    "The randomized controlled trials investigating potential benefits of levothyroxine in women with hypothyroxinemia have not shown beneficial effects on child neurocognition.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "PTU vs MMI",
                "In early pregnancy, antithyroid drug preference is:",
                [
                                        "Methimazole due to once-daily dosing",
                    "Propylthiouracil due to lower teratogenicity risk weeks 6–10",
                    "No antithyroid drugs ever",
                    "Block-and-replace regimen",
],
                1,
                "PTU preferred in first 16 weeks; highest teratogenicity risk for methimazole is gestational weeks 6–10.",
                ref(
                    "Management of Hyperthyroidism Before and During Pregnancy",
                    "The highest risk window for birth defects is from gestation weeks 6 to 10",
                ),
            ),
            mcq(
                f"{p}-q13",
                "TRAb monitoring",
                "Pregnant women with preexisting Graves after ablation/surgery should have:",
                [
                                        "No TRAb testing ever",
                    "TRAb measured in early pregnancy and often around 20 weeks",
                    "Weekly TRAb only",
                    "TRAb replaces all fetal ultrasound",
],
                1,
                "Persisting TRAbs cross placenta and risk fetal thyroid dysfunction—monitor TRAb and fetal growth/heart rate.",
                ref(
                    "Management of Hyperthyroidism Before and During Pregnancy",
                    "Measurement of TRAbs in early pregnancy is indicated in those with preexisting Graves disease and is often repeated around 20 weeks' gestation.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "TSH 2.5 cutoff",
                "A universal pregnancy TSH upper limit of 2.5 mIU/L remains current standard.",
                False,
                "2.5 mIU/L is now deemed too low; 4 mIU/L used when trimester-specific ranges unavailable.",
                ref(
                    "Definition of Thyroid Dysfunction Before and During Pregnancy",
                    "The previous pragmatic upper limit of normal of 2.5 mIU/L is now deemed too low.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "TABLET negative",
                "TABLET showed levothyroxine did not improve live birth rates in euthyroid TPO-positive women.",
                True,
                "Live birth rates were 37.4% vs 37.9% (levothyroxine vs placebo).",
                ref(
                    "Levothyroxine Replacement in Euthyroid TPO-Positive Women Before and During Pregnancy",
                    "relative risk, 0.97 [95% CI, 0.83-1.14]; P = .74",
                ),
            ),
            tf(
                f"{p}-tf3",
                "TPO treatment threshold",
                "TPO-positive pregnant women with TSH >4 mIU/L should be considered for levothyroxine.",
                True,
                "Explicit recommendation in synthesis paragraph.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "Levothyroxine should be considered in women who are TPO positive and have serum TSH values greater than 4.0 mIU/L",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Block and replace",
                "Block-and-replace antithyroid regimens are advisable in pregnancy.",
                False,
                "ATDs cross placenta preferentially—block-and-replace increases fetal hypothyroidism risk.",
                ref(
                    "Management of Hyperthyroidism Before and During Pregnancy",
                    "Block-and-replace regimens are not advisable during pregnancy since antithyroid drugs preferentially cross the placenta",
                ),
            ),
            tf(
                f"{p}-tf5",
                "hCG effect",
                "High hCG in early pregnancy can lower maternal TSH via TSH receptor stimulation.",
                True,
                "Physiologic gestational TSH nadir occurs around 10–12 weeks.",
                ref(
                    "Definition of Thyroid Dysfunction Before and During Pregnancy",
                    "High concentrations of hCG stimulate the pituitary TSH receptor resulting in increased thyroid hormone production, which is usually associated with reduced serum TSH concentrations reaching a trough at 10 to 12 weeks of pregnancy.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "CATS IQ",
                "CATS trial showed improved child IQ with antenatal levothyroxine treatment.",
                False,
                "No IQ difference at 3 years; 9-year follow-up also negative.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "At 3 years, IQ scores were not different in offspring from treated vs nontreated women.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Uncontrolled hyperthyroidism",
                "Uncontrolled overt hyperthyroidism in pregnancy increases miscarriage and stillbirth risk.",
                True,
                "Active management required to avoid maternal and fetal complications.",
                ref(
                    "Management of Hyperthyroidism Before and During Pregnancy",
                    "Uncontrolled overt hyperthyroidism before and during pregnancy is associated with increased risks of miscarriage, stillbirth, intrauterine growth retardation, maternal hypertension, and heart failure",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Hypothyroxinemia harm",
                "Treating gestational hypothyroxinemia is generally not recommended given lack of benefit and potential harm signals.",
                True,
                "Overtreatment in CATS linked to higher ADHD rates in offspring.",
                ref(
                    "Isolated Hypothyroxinemia During Pregnancy",
                    "this approach is generally not recommended",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "4 mIU/L cutoff",
                "Assertion: 4 mIU/L is the suggested pregnancy TSH cutoff when trimester-specific ranges are unavailable.",
                "Reason: Because levothyroxine for TSH below 4 mIU/L always improves obstetric outcomes.",
                2,
                "Assertion true; reason overstates benefit—evidence does not support universal treatment below 4.",
                ref(
                    "Definition of Thyroid Dysfunction Before and During Pregnancy",
                    "current guidance suggests the use of 4 mIU/L as the cutoff for TSH concentrations during pregnancy.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "TABLET",
                "Assertion: TABLET found no live-birth benefit from levothyroxine in euthyroid TPO-positive women.",
                "Reason: Because TPO antibodies may reflect generalized autoimmunity rather than thyroid-mediated harm.",
                0,
                "Both true—trial negative and autoimmune hypothesis consistent.",
                ref(
                    "Levothyroxine Replacement in Euthyroid TPO-Positive Women Before and During Pregnancy",
                    "indicating that the effects of TPO antibodies may not be related through thyroid dysfunction but rather reflect a generalized adverse autoimmune state.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "PTU early pregnancy",
                "Assertion: PTU is preferred over methimazole in early pregnancy.",
                "Reason: Because methimazole has higher teratogenicity risk especially weeks 6–10.",
                0,
                "Both true and causally linked.",
                ref(
                    "Management of Hyperthyroidism Before and During Pregnancy",
                    "since this is associated with a higher risk of teratogenicity than propylthiouracil",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Case 1",
                "Assertion: TSH 4.2 mIU/L with TPO positivity after recurrent miscarriage supports low-dose levothyroxine.",
                "Reason: Because TABLET proved levothyroxine doubles live births in all TPO-positive women.",
                2,
                "Assertion reasonable per case; reason false—TABLET was negative.",
                ref("Case 1", "represents a reasonable indication to start low-dosage levothyroxine (Answer E)"),
            ),
            ar(
                f"{p}-ar5",
                "Overt hypothyroidism",
                "Assertion: Untreated overt maternal hypothyroidism harms pregnancy and child neurodevelopment.",
                "Reason: Because maternal hypothyroidism has no obstetric consequences.",
                2,
                "Assertion true; reason false.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "When uncorrected during pregnancy, it is associated with adverse outcomes, including miscarriage, preeclampsia, low birth weight, and preterm birth.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Gestational thyrotoxicosis",
                "Assertion: Gestational thyrotoxicosis from hCG is usually managed conservatively.",
                "Reason: Because TRAb and free T3 are elevated identically to Graves disease.",
                2,
                "Assertion true; reason false—TRAb/T3 distinguish Graves.",
                ref(
                    "Management of Hyperthyroidism Before and During Pregnancy",
                    "Transient rises in circulating thyroid hormones are usually treated in a supportive manner",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Levothyroxine dose pregnancy",
                "Assertion: Empirical levothyroxine dose increase is appropriate on positive pregnancy test.",
                "Reason: Because pregnancy decreases thyroid hormone requirements.",
                2,
                "Assertion true; reason false—requirements increase in pregnancy.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "An empirical increase in the dosage of levothyroxine upon finding of a positive pregnancy test is appropriate",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Case 5",
                "Assertion: Prepregnancy TPO-positive woman with TSH 2.4 mIU/L warrants individualized monitoring or levothyroxine consideration.",
                "Reason: Because all women with TSH <4 mIU/L must receive levothyroxine per TABLET.",
                2,
                "Assertion aligns with nuanced care; reason false—universal treatment not supported.",
                ref(
                    "Management of Hypothyroidism Before and During Pregnancy",
                    "there is insufficient evidence to universally treat pregnant women with serum TSH values between 2.5 and 4 mIU/L regardless of TPO antibody status.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "40",
        "title": "Management of Thyroid Dysfunction Before and During Pregnancy",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Kristien Boelaert, MD, PhD, FRCP",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_40_Management_of_Thyroid_Dysfunction_Before_and_During_Pregnancy.md",
        "items": items,
    }


def build_chapter_41() -> dict:
    p = "e21-41"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Oncology interface",
                "Why endocrinologists are vital in cancer care",
                "Improved survival and novel therapies increase endocrine complications; endocrinologists partner with oncologists so endocrinopathies do not delay or prohibit anticancer therapy.",
                ref(
                    "Main Conclusions",
                    "endocrinologists are vital partners to oncologists in ensuring that the endocrinopathies do not delay or prohibit anticancer therapy.",
                ),
            ),
            note(
                f"{p}-n2",
                "SIADH",
                "How to diagnose SIADH in a euvolemic cancer patient",
                "SIADH requires euvolemia, serum osmolality <275 mOsm/kg, urine osmolality ≥100 mOsm/kg, urinary sodium ≥20 mEq/L, normal thyroid and adrenal function, and exclusion of drug-induced hyponatremia.",
                ref(
                    "Clinical Case Vignette 1",
                    "A diagnosis of SIADH requires 7 conditions to be met (in the untreated state): Clinical euvolemia • Serum osmolality <275 mOsm/kg • Urine osmolality ≥100 mOsm/kg • Urinary sodium ≥20 mEq/L",
                ),
            ),
            note(
                f"{p}-n3",
                "Hyponatremia treatment",
                "How hyponatremia treatment depends on severity and onset",
                "Treatment of hyponatremia depends on severity, speed of onset, and underlying diagnosis—acute life-threatening hyponatremia presents with seizures and coma.",
                ref(
                    "Clinical Case Vignette 1",
                    "Answer: Depends on the severity, speed of onset, and underlying diagnosis",
                ),
            ),
            note(
                f"{p}-n4",
                "ICI thyroiditis",
                "How to manage checkpoint inhibitor thyroiditis",
                "Thyroiditis is often transient asymptomatic hyperthyroidism; thionamides are of no value; it usually progresses to irreversible hypothyroidism—exclude cortisol deficiency before levothyroxine.",
                ref(
                    "Thyroiditis",
                    "Thionamide treatment (carbamazole/propylthiouracil) is of no value. Thyroiditis usually progresses to irreversible hypothyroidism. Cortisol deficiency must be excluded before levothyroxine is initiated.",
                ),
            ),
            note(
                f"{p}-n5",
                "ICI hypophysitis",
                "Why hypophysitis requires urgent hydrocortisone when sick",
                "Hypophysitis causes ACTH deficiency; methylprednisolone may help mass effect but is not appropriate for acute cortisol deficiency alone—physiological glucocorticoid replacement is needed.",
                ref(
                    "Hypophysitis",
                    "Methylprednisolone is not an appropriate treatment for acute cortisol deficiency secondary to ACTH deficiency alone.",
                ),
            ),
            note(
                f"{p}-n6",
                "ICI continuation",
                "Why endocrine adverse effects should not stop checkpoint inhibitors",
                "Early recognition and management are essential; endocrine complications are not a reason to discontinue immune checkpoint inhibitor therapy.",
                ref(
                    "Thyroiditis",
                    "endocrine complications are not a reason to discontinue immune checkpoint inhibitor therapy.",
                ),
            ),
            note(
                f"{p}-n7",
                "Cancer therapy bone loss",
                "How cancer therapy accelerates bone loss",
                "Cancer therapy-related bone loss from GnRH agonists, aromatase inhibitors, antiandrogens, chemotherapy-induced ovarian failure, and glucocorticoids can be up to 7-fold faster than normal aging.",
                ref(
                    "Cancer Therapy-Related Bone Loss",
                    "Cancer therapy-related bone loss is more rapid than postmenopausal bone loss in women or normal age-related osteoporosis in men, with rates being up to 7-fold higher than that seen with normal aging.",
                ),
            ),
            note(
                f"{p}-n8",
                "Breast cancer bone",
                "How to manage bone loss in young breast cancer survivor on AI",
                "Counsel calcium 700–1000 mg and vitamin D 800 IU daily, lifestyle measures, and discuss antiresorptive risks/benefits; FRAX may not apply under age 40.",
                ref(
                    "Case Vignette 3",
                    "Answer: Calcium, 700-1000 mg daily, and vitamin D, 800 IU daily",
                ),
            ),
            note(
                f"{p}-n9",
                "Hodgkin breast risk",
                "Why Hodgkin survivors with chest RT have high breast cancer risk",
                "Women treated with chest radiotherapy for childhood malignancy have very high breast cancer risk; Hodgkin survivors have ~35% breast cancer risk by age 50.",
                ref(
                    "Cancer-Related New Content Hormone Replacement Therapy",
                    "This risk is highest in survivors of Hodgkin lymphoma, who have a 35% chance of developing breast cancer by age 50 years.",
                ),
            ),
            note(
                f"{p}-n10",
                "Case vignette 4",
                "How mediastinal RT affects 10-year breast cancer risk on POP",
                "Prior mediastinal RT gives ~15% 10-year and ~30% 20-year breast cancer risk; progesterone-only pill adds ~20% relative hazard, yielding ~18% 10-year risk.",
                ref(
                    "Clinical Case Vignette 4",
                    "Answer: D) 18%",
                ),
            ),
            note(
                f"{p}-n11",
                "Pelvic RT fractures",
                "How pelvic radiotherapy causes insufficiency fractures",
                "Radiotherapy-related insufficiency fractures occur in 10%–20% after pelvic RT; may occur with normal DXA BMD; ~83% managed conservatively with analgesia.",
                ref(
                    "Clinical Case Vignette 5",
                    "Radiotherapy-related insufficiency fractures occur in approximately 10% to 20% of patients who undergo pelvic radiotherapy.",
                ),
            ),
            note(
                f"{p}-n12",
                "Pelvic RT management",
                "How to treat radiotherapy-related sacral insufficiency fractures",
                "Conservative management with analgesia, physiotherapy, and calcium/vitamin D repletion; bisphosphonates lack evidence; teriparatide is contraindicated after skeletal irradiation.",
                ref(
                    "Clinical Case Vignette 5",
                    "Answer: A, B, and C) Analgesia; physiotherapy; and calcium, 1000 mg once daily, and vitamin D, 800 IU once daily",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "SIADH vignette",
                "Euvolemic small cell lung cancer patient: Na 110, serum osm 226, urine osm 611, urine Na 42. Diagnosis?",
                [
                                        "Cerebral salt wasting",
                    "SIADH",
                    "Primary polydipsia",
                    "Adrenal insufficiency only",
],
                1,
                "Low serum osmolality with inappropriately concentrated urine and urinary sodium ≥20 in euvolemic patient meets SIADH criteria.",
                ref("Clinical Case Vignette 1", "Answer: SIADH"),
            ),
            mcq(
                f"{p}-q2",
                "Adrenalitis case",
                "Nivolumab patient initially thought to have isolated ACTH deficiency later has high ACTH and renin with low aldosterone. Diagnosis?",
                [
                                        "Continued central adrenal insufficiency",
                    "Nivolumab-induced primary adrenal failure",
                    "SIADH alone",
                    "Factitious disorder",
],
                1,
                "Rising ACTH and renin with low aldosterone and bilateral adrenal PET uptake indicate primary adrenal failure.",
                ref(
                    "Clinical Case Vignette 2",
                    "Answer: Nivolumab-induced primary adrenal failure, as evidenced by raised ACTH and renin",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Breast cancer bone",
                "Premenopausal breast cancer survivor on goserelin and exemestane with significant BMD decline age 33→35. Initial management?",
                [
                                        "Immediate teriparatide",
                    "Calcium 700–1000 mg and vitamin D 800 IU daily with lifestyle counseling",
                    "Stop all cancer therapy immediately",
                    "No intervention until fracture occurs",
],
                1,
                "Young patient without fracture: optimize calcium/vitamin D and lifestyle; discuss antiresorptives with limited young-patient data.",
                ref("Case Vignette 3", "Answer: Calcium, 700-1000 mg daily, and vitamin D, 800 IU daily"),
            ),
            mcq(
                f"{p}-q4",
                "Hodgkin survivor",
                "39-year-old Hodgkin survivor with mediastinal RT at 19 on progesterone-only pill: approximate 10-year breast cancer risk?",
                [
                                        "0.1%",
                    "1%",
                    "5%",
                    "18%",
],
                3,
                "Chest RT baseline ~15% at 10 years plus POP hazard ratio ~1.2 yields ~18%.",
                ref("Clinical Case Vignette 4", "Answer: D) 18%"),
            ),
            mcq(
                f"{p}-q5",
                "Pelvic RT fracture",
                "Post pelvic RT patient with sacral insufficiency fractures and normal DXA. Best treatment options?",
                [
                                        "Analgesia only",
                    "Analgesia, physiotherapy, and calcium/vitamin D",
                    "Teriparatide first-line",
                    "Immediate bisphosphonate mandatory",
],
                1,
                "Conservative analgesia, PT, and calcium/vitamin D are standard; teriparatide contraindicated after skeletal RT.",
                ref("Clinical Case Vignette 5", "Answer: A, B, and C)"),
            ),
            mcq(
                f"{p}-q6",
                "ICI monitoring",
                "Thyroid function during checkpoint inhibitor therapy should be checked:",
                [
                                        "Only at completion of all cycles",
                    "With every cycle",
                    "Never",
                    "Only if symptomatic after 2 years",
],
                1,
                "Guidance recommends TFT with every cycle; complications often arise within first 4 cycles.",
                ref(
                    "Thyroiditis",
                    "Thyroid function should be checked with every cycle of immune checkpoint inhibitor therapy.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Hypophysitis steroids",
                "For checkpoint inhibitor hypophysitis with acute ACTH deficiency without mass effect:",
                [
                                        "High-dose methylprednisolone instead of hydrocortisone",
                    "Physiological glucocorticoid replacement",
                    "No glucocorticoids ever",
                    "Stop checkpoint inhibitor permanently",
],
                1,
                "Methylprednisolone is for mass effect; ACTH deficiency requires physiological replacement.",
                ref(
                    "Hypophysitis",
                    "Methylprednisolone is not an appropriate treatment for acute cortisol deficiency secondary to ACTH deficiency alone.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Thionamides in ICI thyroiditis",
                "Asymptomatic checkpoint inhibitor-mediated thyrotoxicosis should:",
                [
                                        "Receive carbimazole immediately",
                    "Avoid thionamides; monitor for progression to hypothyroidism",
                    "Receive radioactive iodine",
                    "Stop immunotherapy permanently",
],
                1,
                "Thyroiditis hyperthyroid phase is self-limited; thionamides do not help and may worsen subsequent hypothyroidism.",
                ref("Thyroiditis", "Thionamide treatment (carbamazole/propylthiouracil) is of no value."),
            ),
            mcq(
                f"{p}-q9",
                "DXA in cancer survivors",
                "When should DXA be performed in nonmetastatic cancer patients on endocrine therapy?",
                [
                                        "Never",
                    "When osteoporotic fracture risk factors exist and bone-modifying therapy is considered",
                    "Only after pathologic fracture",
                    "Daily",
],
                1,
                "DXA of spine, hip, and femoral neck quantifies fracture risk when bone-modifying therapy is being considered.",
                ref(
                    "Bone Loss",
                    "When 1 or more risk factor for osteoporotic fracture is present, and there is consideration for use of a bone-modifying agent, then evaluate bone mineral density",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Hyponatremia workup",
                "Initial hyponatremia evaluation in cancer patients should include:",
                [
                                        "Serum osmolality, cortisol, thyroid function, glucose, and urine studies",
                    "Head CT only",
                    "Immediate hypertonic saline without assessment",
                    "Serum sodium repeat in 1 year",
],
                0,
                "Structured evaluation includes osmolality, adrenal and thyroid status, glucose, and urine osmolality/electrolytes.",
                ref(
                    "Clinical Case Vignette 1",
                    "Measurement of serum osmolality, cortisol (document exogenous glucocorticoids), thyroid function, and glucose",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Primary adrenalitis ICI",
                "Primary adrenalitis from checkpoint inhibitors may require:",
                [
                                        "Fludrocortisone in addition to glucocorticoids",
                    "Thionamides",
                    "Growth hormone",
                    "Levothyroxine before cortisol",
],
                0,
                "Primary adrenal failure with low aldosterone may need fludrocortisone plus glucocorticoid replacement.",
                ref("Clinical Case Vignette 2", "Fludrocortisone is started."),
            ),
            mcq(
                f"{p}-q12",
                "Bisphosphonates pelvic RT",
                "For radiotherapy-related insufficiency fractures, bisphosphonates:",
                [
                                        "Are proven first-line in meta-analyses",
                    "Lack evidence of efficacy; low-turnover state may limit benefit",
                    "Are mandatory in all patients",
                    "Replace analgesia entirely",
],
                1,
                "~6% receive bisphosphonates but evidence is lacking; anabolic agents contraindicated after skeletal RT.",
                ref(
                    "Clinical Case Vignette 5",
                    "there is no current evidence that this is effective, particularly as there is the likelihood that this is a low bone-turnover state.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Immunotherapy timing",
                "Endocrine complications of checkpoint inhibitors most commonly develop:",
                [
                                        "Only after completing all treatment",
                    "Within the first 4 cycles",
                    "After 5 years",
                    "Only with CTLA4 monotherapy never PD-1",
],
                1,
                "Most endocrine immune adverse events appear early, though they can occur later.",
                ref(
                    "Thyroiditis",
                    "Endocrine complications most commonly develop within 4 cycles of commencing treatment.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "SIADH euvolemia",
                "SIADH requires clinical euvolemia.",
                True,
                "Volume status assessment is central to hyponatremia differential diagnosis.",
                ref("Clinical Case Vignette 1", "Clinical euvolemia"),
            ),
            tf(
                f"{p}-tf2",
                "ICI stop",
                "Endocrine complications are an automatic reason to permanently discontinue checkpoint inhibitor therapy.",
                False,
                "Endocrine AEs should generally not lead to cessation; temporary pause if very unwell.",
                ref("Thyroiditis", "endocrine complications are not a reason to discontinue immune checkpoint inhibitor therapy."),
            ),
            tf(
                f"{p}-tf3",
                "Thionamides ICI",
                "Thionamides are effective for checkpoint inhibitor-mediated thyroiditis.",
                False,
                "Thionamides are of no value in this transient destructive thyroiditis.",
                ref("Thyroiditis", "Thionamide treatment (carbamazole/propylthiouracil) is of no value."),
            ),
            tf(
                f"{p}-tf4",
                "Bone loss rate",
                "Cancer therapy-related bone loss can exceed normal aging bone loss by up to 7-fold.",
                True,
                "Endocrine and glucocorticoid cancer therapies accelerate bone loss markedly.",
                ref(
                    "Cancer Therapy-Related Bone Loss",
                    "rates being up to 7-fold higher than that seen with normal aging.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Hodgkin risk",
                "Hodgkin lymphoma survivors treated with chest RT have up to 35% breast cancer risk by age 50.",
                True,
                "Highest risk among childhood chest irradiation survivors.",
                ref(
                    "Cancer-Related New Content Hormone Replacement Therapy",
                    "survivors of Hodgkin lymphoma, who have a 35% chance of developing breast cancer by age 50 years.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Pelvic RT fractures normal BMD",
                "Pelvic radiotherapy insufficiency fractures can occur despite normal DXA BMD.",
                True,
                "Case vignette 5 demonstrates fractures with normal hip/spine density.",
                ref(
                    "Clinical Case Vignette 5",
                    "they can occur in younger women with normal total hip and spine bone mineral density by DXA.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Cortisol before T4",
                "Cortisol deficiency must be excluded before starting levothyroxine after checkpoint inhibitor thyroiditis.",
                True,
                "Risk of adrenal crisis if cortisol deficiency is missed.",
                ref("Thyroiditis", "Cortisol deficiency must be excluded before levothyroxine is initiated."),
            ),
            tf(
                f"{p}-tf8",
                "Teriparatide RT",
                "Teriparatide is contraindicated after prior radiation to the skeleton.",
                True,
                "Anabolic agents contraindicated in humans with prior skeletal irradiation.",
                ref(
                    "Clinical Case Vignette 5",
                    "they are contraindicated in humans who have received previous radiation therapy to the skeleton.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "SIADH",
                "Assertion: SIADH diagnosis requires inappropriately concentrated urine despite low serum osmolality.",
                "Reason: Because urine osmolality must be <100 mOsm/kg in SIADH.",
                2,
                "Assertion true; reason false—urine osmolality is ≥100 mOsm/kg.",
                ref("Clinical Case Vignette 1", "Urine osmolality ≥100 mOsm/kg"),
            ),
            ar(
                f"{p}-ar2",
                "ICI thyroiditis",
                "Assertion: Checkpoint inhibitor thyroiditis often progresses to permanent hypothyroidism.",
                "Reason: Because thionamides prevent progression to hypothyroidism.",
                2,
                "Assertion true; reason false—thionamides are of no value.",
                ref("Thyroiditis", "Thyroiditis usually progresses to irreversible hypothyroidism."),
            ),
            ar(
                f"{p}-ar3",
                "Hypophysitis",
                "Assertion: High-dose methylprednisolone is inappropriate for isolated ACTH deficiency without mass effect.",
                "Reason: Because methylprednisolone is inferior to physiological replacement for acute cortisol deficiency alone.",
                0,
                "Both true per chapter guidance.",
                ref(
                    "Hypophysitis",
                    "Methylprednisolone is not an appropriate treatment for acute cortisol deficiency secondary to ACTH deficiency alone.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Bone monitoring",
                "Assertion: Cancer survivors on aromatase inhibitors are at risk for accelerated bone loss.",
                "Reason: Because endocrine therapy never affects bone mineral density.",
                2,
                "Assertion true; reason false—AI/GnRH/antiandrogen therapy accelerates loss.",
                ref(
                    "Cancer Therapy-Related Bone Loss",
                    "added risks of treatment-related bone loss due to hypogonadism from endocrine therapy",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Hodgkin POP",
                "Assertion: Progesterone-only contraception may further increase breast cancer risk after chest RT.",
                "Reason: Because POP increases breast cancer hazard while on therapy with HR ~1.2.",
                0,
                "Both true—combined risk yields ~18% at 10 years in vignette.",
                ref(
                    "Clinical Case Vignette 4",
                    "progesterone-only contraception increases breast cancer risk while on therapy with a hazard ratio of approximately 1.2.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Pelvic RT fractures",
                "Assertion: Most radiotherapy-related pelvic insufficiency fractures are managed conservatively.",
                "Reason: Because approximately 83% are managed conservatively with analgesia.",
                0,
                "Both true per meta-analysis cited.",
                ref(
                    "Clinical Case Vignette 5",
                    "83% are generally managed conservatively with analgesia (Answer A)",
                ),
            ),
            ar(
                f"{p}-ar7",
                "ICI monitoring",
                "Assertion: Thyroid function should be checked with each checkpoint inhibitor cycle.",
                "Reason: Because endocrine complications never occur after cycle 4.",
                2,
                "Assertion true; reason false—most common within 4 cycles but monitoring continues.",
                ref("Thyroiditis", "Thyroid function should be checked with every cycle of immune checkpoint inhibitor therapy."),
            ),
            ar(
                f"{p}-ar8",
                "Adrenalitis",
                "Assertion: Nivolumab can cause primary adrenal failure with elevated ACTH and renin.",
                "Reason: Because isolated ACTH deficiency always presents with low ACTH.",
                2,
                "Assertion true for revised diagnosis; reason false—primary failure raises ACTH.",
                ref(
                    "Clinical Case Vignette 2",
                    "Answer: Nivolumab-induced primary adrenal failure, as evidenced by raised ACTH and renin",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "41",
        "title": "The EndocrinologyOncology InterfaceHow Do We Help Each Other",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Claire Higham, DPhil, FRCP; Sacha Howell, PhD, FRCP; Peter Trainer, MD, FRCPE",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_41_The_EndocrinologyOncology_InterfaceHow_Do_We_Help_Each_Other.md",
        "items": items,
    }


def build_chapter_42() -> dict:
    p = "e21-42"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "ICI overview",
                "Why immune checkpoint inhibitors cause endocrine adverse effects",
                "Checkpoint inhibitors block CTLA4, PD-1, or PD-L1 immune brakes, augmenting antitumor immunity but causing immune-mediated endocrinopathies in ~15% with single agents and 20%–30% with combination therapy.",
                ref(
                    "Significance of the Clinical Problem",
                    "immune-mediated endocrine dysfunction is observed in approximately 15% of patients treated with a single agent and in 20% to 30% of those treated with a combination of 2 checkpoint inhibitors.",
                ),
            ),
            note(
                f"{p}-n2",
                "Thyroiditis prevalence",
                "How thyroid dysfunction prevalence varies by agent",
                "Destructive thyroiditis is most common with PD-1/PD-L1 blockers (hypothyroidism up to ~8%–8.5%); hypophysitis is most frequent with CTLA4 blockade (~5% with ipilimumab).",
                ref(
                    "Table. Prevalence of Endocrinopathies During Immune Checkpoint Inhibitor Therapy",
                    "Ipilimumab ... Hypothyroidism 3.8% ... Pituitary Dysfunction 5.6% ... Nivolumab ... Hypothyroidism 8% ... Pituitary Dysfunction 0.5%",
                ),
            ),
            note(
                f"{p}-n3",
                "Hypophysitis urgency",
                "Why hypophysitis with adrenal crisis requires immediate hydrocortisone",
                "Sick hypotensive patient on combination ipilimumab/nivolumab needs serum cortisol and IV hydrocortisone 100 mg stat before MRI or cosyntropin testing.",
                ref("Case 1", "Answer: B) Measure serum cortisol and give intravenous hydrocortisone, 100 mg stat"),
            ),
            note(
                f"{p}-n4",
                "Thyroiditis monitoring",
                "How to manage asymptomatic checkpoint inhibitor thyrotoxicosis",
                "Mild asymptomatic thyrotoxicosis: repeat TFT in 2 weeks with TRAb; do not cancel immunotherapy or start thionamides; ~50% develop permanent hypothyroidism.",
                ref("Case 2", "Answer: E) Order repeated thyroid function tests in 2 weeks with TSH-receptor antibodies"),
            ),
            note(
                f"{p}-n5",
                "Thionamide pitfall",
                "Why thionamides should not be used in ICI thyroiditis",
                "Methimazole does not improve immune-mediated thyrotoxicosis and may prolong or worsen rebound hypothyroidism.",
                ref(
                    "Case 2",
                    "Starting methimazole (Answer C) is incorrect, as it will not improve thyrotoxicosis in thyroiditis; it will just make any rebound hypothyroidism more prolonged or severe.",
                ),
            ),
            note(
                f"{p}-n6",
                "Central hypothyroidism",
                "How to recognize checkpoint inhibitor central hypothyroidism",
                "Declining free T4 with normal or low TSH during CTLA4 therapy suggests hypophysitis—mandatory screening for adrenal insufficiency before levothyroxine.",
                ref(
                    "Hypothyroidism",
                    "It is mandatory to screen for and treat hypoadrenalism before starting levothyroxine replacement.",
                ),
            ),
            note(
                f"{p}-n7",
                "Hypophysitis demographics",
                "Who is at highest risk for ipilimumab hypophysitis",
                "Hypophysitis is more common in older men (3:1) after 3–5 cycles, especially at 10 mg/kg ipilimumab doses.",
                ref(
                    "Pituitary Dysfunction",
                    "It is more common in older men (male:female, 3:1) and with higher dosages of ipilimumab (10 mg/kg).",
                ),
            ),
            note(
                f"{p}-n8",
                "Do not stop ICI",
                "Why treatable endocrinopathy should not end checkpoint therapy",
                "Transformative cancer benefit means endocrine adverse effects should not routinely lead to discontinuation—temporary pause if significantly unwell.",
                ref(
                    "Barriers to Optimal Practice",
                    "development of a treatable endocrine adverse effect should not routinely lead to discontinuation of the checkpoint inhibitor therapy.",
                ),
            ),
            note(
                f"{p}-n9",
                "Type 1 diabetes",
                "How fulminant type 1 diabetes presents on checkpoint inhibitors",
                "Fulminant type 1 diabetes with ketoacidosis can occur, more often with combination CTLA4/PD-1 blockade (~2% type 1 diabetes).",
                ref(
                    "Main Conclusions",
                    "Fulminant type 1 diabetes, often with ketoacidosis, and primary adrenal insufficiency can also be observed but are more rare.",
                ),
            ),
            note(
                f"{p}-n10",
                "Misattribution trap",
                "Pitfall: attributing ICI endocrinopathy symptoms to progressive cancer",
                "Nonspecific weight loss, lethargy, and hypotension from adrenal insufficiency may be misread as tumor progression.",
                ref(
                    "Barriers to Optimal Practice",
                    "nonspecific deterioration, including weight loss, poor appetite, lethargy, and hypotension may be misattributed to advancing cancer rather than to a readily treatable endocrinopathy",
                ),
            ),
            note(
                f"{p}-n11",
                "Hypothyroid treatment threshold",
                "When to treat checkpoint inhibitor hypothyroidism",
                "Asymptomatic subclinical hypothyroidism with TSH 4–10 may be observed; treat when TSH ≥10 or symptomatic; assume primary hypothyroidism is permanent.",
                ref(
                    "Hypothyroidism",
                    "it is not necessary to treat patients with asymptomatic mild/subclinical primary hypothyroidism with serum TSH concentrations in the range of 4 to 10 mIU/L and normal serum free T₄ levels, but treatment is indicated once the TSH concentration rises to 10 mIU/L or higher.",
                ),
            ),
            note(
                f"{p}-n12",
                "Recovery expectations",
                "What endocrine recovery to expect after checkpoint inhibitors",
                "Recovery is not expected in most instances; secondary adrenal insufficiency is usually permanent though hypothyroidism/hypogonadism may recover in ~50%.",
                ref(
                    "Main Conclusions",
                    "Recovery from endocrine dysfunction is not expected in most instances.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "Melanoma patient on ipilimumab/nivolumab cycle 3 with hypotension, hyponatremia, confusion. Immediate priority?",
                [
                                        "Measure cortisol, aldosterone, and ACTH only",
                    "Measure cortisol and give IV hydrocortisone 100 mg stat",
                    "Urine sodium and osmolality first",
                    "Pituitary MRI before steroids",
],
                1,
                "Acutely ill patient needs empiric IV hydrocortisone while drawing cortisol; detailed testing waits until stable.",
                ref("Case 1", "Answer: B) Measure serum cortisol and give intravenous hydrocortisone, 100 mg stat"),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "Asymptomatic mild thyrotoxicosis before pembrolizumab cycle 4. Best action?",
                [
                                        "Cancel pembrolizumab cycle",
                    "Start methimazole 15 mg daily",
                    "Start propranolol 80 mg daily",
                    "Repeat TFT in 2 weeks with TRAb",
],
                3,
                "Mild asymptomatic thyroiditis: monitor; TRAb helps exclude Graves; thionamides and cycle cancellation inappropriate.",
                ref("Case 2", "Answer: E) Order repeated thyroid function tests in 2 weeks with TSH-receptor antibodies"),
            ),
            mcq(
                f"{p}-q3",
                "ICI prevalence",
                "Which agent has the highest pituitary dysfunction rate in the ICI table?",
                [
                                        "Nivolumab (~0.5%)",
                    "Pembrolizumab (~1.1%)",
                    "Ipilimumab (~5.6%)",
                    "Atezolizumab (not listed)",
],
                2,
                "CTLA4 blockade with ipilimumab carries highest hypophysitis rate in the summary table.",
                ref(
                    "Table. Prevalence of Endocrinopathies During Immune Checkpoint Inhibitor Therapy",
                    "Ipilimumab ... Pituitary Dysfunction ... 5.6%",
                ),
            ),
            mcq(
                f"{p}-q4",
                "PD-1 thyroid",
                "Destructive thyroiditis causing hypothyroidism is most common with:",
                [
                                        "PD-1/PD-L1 blockers",
                    "CTLA4 blockade only",
                    "Chemotherapy alone",
                    "Radiation only",
],
                0,
                "Chapter states destructive thyroiditis is typically seen after PD-1/PD-L1 blockers.",
                ref(
                    "Main Conclusions",
                    "Destructive thyroiditis, manifest as either transient hyperthyroidism or permanent hypothyroidism, is the most common endocrine adverse effect, typically seen after use of PD1/PD-L1 blockers.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Hypophysitis imaging",
                "Pituitary MRI in checkpoint inhibitor hypophysitis is indicated to:",
                [
                                        "Avoid glucocorticoid replacement",
                    "Exclude metastasis and assess hypophysitis",
                    "Replace hormonal testing",
                    "Prove diabetes insipidus always present",
],
                1,
                "MRI excludes metastatic pituitary disease; moderately enlarged bright pituitary may be seen.",
                ref(
                    "Pituitary Dysfunction",
                    "Affected patients need pituitary MRI whether they present with mass effects or hormonal dysfunction, as other causes of pituitary failure (particularly metastasis) must be excluded.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Sick euthyroid vs central",
                "In high tumor burden, central hypothyroidism from hypophysitis differs from sick euthyroid syndrome because:",
                [
                                        "Free T4 is usually lower in central hypothyroidism",
                    "TSH is always high in central hypothyroidism",
                    "Sick euthyroid always needs levothyroxine urgently",
                    "No difference exists",
],
                0,
                "Sick euthyroid tends to preserve free T4 relative to central hypothyroidism with low free T4.",
                ref(
                    "Hypothyroidism",
                    "serum free T₄ tends to be relatively preserved in sick euthyroid syndrome and is likely to be lower in central hypothyroidism.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "High-dose steroids",
                "High-dose methylprednisolone in hypophysitis is appropriate for:",
                [
                                        "Isolated ACTH deficiency without mass effect",
                    "Optic nerve compression with visual loss",
                    "Mild subclinical hypothyroidism",
                    "Asymptomatic thyrotoxicosis",
],
                1,
                "High-dose glucocorticoids for vision-threatening mass effect until vision restored.",
                ref(
                    "Pituitary Dysfunction",
                    "Rarely, patients present with optic nerve compression causing visual disturbance, and they should be treated with high-dosage glucocorticoids such as methylprednisolone or dexamethasone until vision is restored.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Methimazole harm",
                "Starting methimazole for pembrolizumab-related thyrotoxicosis may:",
                [
                                        "Improve long-term euthyroidism",
                    "Prolong or worsen subsequent hypothyroidism",
                    "Prevent all thyroid disease",
                    "Replace need for levothyroxine",
],
                1,
                "Thionamides are ineffective in thyroiditis and may worsen hypothyroid phase.",
                ref("Case 2", "it will just make any rebound hypothyroidism more prolonged or severe."),
            ),
            mcq(
                f"{p}-q9",
                "Combination therapy",
                "Combination CTLA4 + PD-1 checkpoint inhibition endocrine toxicity rate is approximately:",
                [
                                        "1%–2%",
                    "5%",
                    "15%–30%",
                    "60%–80%",
],
                2,
                "Combination therapy doubles or more the endocrine AE rate vs single agent.",
                ref(
                    "Significance of the Clinical Problem",
                    "in 20% to 30% of those treated with a combination of 2 checkpoint inhibitors.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Hypoadrenalism before T4",
                "Before levothyroxine for checkpoint inhibitor hypothyroidism, you must:",
                [
                                        "Start levothyroxine first always",
                    "Screen for and treat adrenal insufficiency",
                    "Give methimazole",
                    "Stop all immunotherapy permanently",
],
                1,
                "Treating hypothyroidism before cortisol replacement risks adrenal crisis.",
                ref(
                    "Hypothyroidism",
                    "It is mandatory to screen for and treat hypoadrenalism before starting levothyroxine replacement.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Case 2 natural history",
                "In Case 2, repeated labs showed progression to TSH 39 with low free T4 requiring:",
                [
                                        "Methimazole increase",
                    "Levothyroxine 75 mcg daily",
                    "Radioactive iodine",
                    "Thyroidectomy",
],
                1,
                "Destructive thyroiditis progressed to permanent hypothyroidism treated with levothyroxine.",
                ref("Case 2", "Levothyroxine, 75 mcg daily, was started."),
            ),
            mcq(
                f"{p}-q12",
                "Hypophysitis timing",
                "Hypophysitis from ipilimumab typically presents after:",
                [
                                        "1 day",
                    "3–5 cycles (9–16 weeks)",
                    "5 years",
                    "Only post-treatment",
],
                1,
                "Headache and fatigue emerge after several cycles.",
                ref(
                    "Pituitary Dysfunction",
                    "Headache and fatigue are the earliest symptoms and are typically found after 3 to 5 cycles (9-16 weeks).",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Primary adrenal ICI",
                "Primary adrenal insufficiency with checkpoint inhibitors is:",
                [
                                        "Most common with single PD-1 agents",
                    "Rare with single agents; higher with combination CTLA4/PD-1",
                    "Never seen",
                    "Always self-limited",
],
                1,
                "Primary adrenal insufficiency is rare on monotherapy but more frequent with combination blockade.",
                ref(
                    "Primary Adrenal Insufficiency",
                    "Primary adrenal insufficiency seems to be rare with single-agent checkpoint inhibition, but combination CTLA4/PD-1 blockade therapy",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Thyroid most common",
                "Thyroid dysfunction is the most common endocrine adverse effect of checkpoint inhibitors.",
                True,
                "Destructive thyroiditis predominates, especially with PD-1/PD-L1 agents.",
                ref(
                    "Main Conclusions",
                    "Destructive thyroiditis ... is the most common endocrine adverse effect",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Stop ICI routine",
                "Endocrine adverse effects should routinely lead to permanent checkpoint inhibitor discontinuation.",
                False,
                "Treat endocrinopathy and continue therapy when possible; pause if very unwell.",
                ref(
                    "Barriers to Optimal Practice",
                    "should not routinely lead to discontinuation of the checkpoint inhibitor therapy.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "IV hydrocortisone sick",
                "Acutely ill suspected hypophysitis patient should receive IV hydrocortisone 100 mg immediately.",
                True,
                "Empiric steroids while measuring cortisol in sick patient per Case 1.",
                ref("Case 1", "give intravenous hydrocortisone, 100 mg stat (Answer B) is correct because he is sick"),
            ),
            tf(
                f"{p}-tf4",
                "Thionamides thyroiditis",
                "Methimazole improves immune checkpoint inhibitor-mediated thyrotoxicosis.",
                False,
                "Thyroiditis thyrotoxicosis is self-limited; thionamides are ineffective.",
                ref("Case 2", "Starting methimazole (Answer C) is incorrect"),
            ),
            tf(
                f"{p}-tf5",
                "Ipilimumab hypophysitis",
                "Ipilimumab causes hypophysitis in approximately 5% of patients.",
                True,
                "Table lists pituitary dysfunction 5.6% for ipilimumab.",
                ref(
                    "Table. Prevalence of Endocrinopathies During Immune Checkpoint Inhibitor Therapy",
                    "Ipilimumab ... Pituitary Dysfunction ... 5.6%",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Permanent hypothyroid",
                "Primary hypothyroidism after checkpoint inhibitor thyroiditis should be assumed permanent.",
                True,
                "Long-term levothyroxine usually required.",
                ref("Hypothyroidism", "Primary hypothyroidism should be assumed to be permanent."),
            ),
            tf(
                f"{p}-tf7",
                "Cancel cycle mild",
                "Mild asymptomatic thyrotoxicosis warrants cancelling the next checkpoint inhibitor cycle.",
                False,
                "Case 2: not ill enough to interrupt life-prolonging therapy.",
                ref("Case 2", "Cancelling this cycle of pembrolizumab (Answer A) is wrong because she is not ill enough"),
            ),
            tf(
                f"{p}-tf8",
                "Recovery common",
                "Most checkpoint inhibitor endocrinopathies fully recover without replacement therapy.",
                False,
                "Recovery not expected in most instances.",
                ref("Main Conclusions", "Recovery from endocrine dysfunction is not expected in most instances."),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Case 1 steroids",
                "Assertion: IV hydrocortisone 100 mg is priority in sick suspected ICI adrenal crisis patient.",
                "Reason: Because cosyntropin testing must always precede any glucocorticoid.",
                2,
                "Assertion true when ill; reason false—treat first, test when stable.",
                ref("Case 1", "he is sick and should be treated immediately with parenteral hydrocortisone"),
            ),
            ar(
                f"{p}-ar2",
                "Case 2 monitor",
                "Assertion: Asymptomatic mild ICI thyrotoxicosis can be monitored with repeat TFT in 2 weeks.",
                "Reason: Because thionamides are first-line for immune-mediated thyroiditis.",
                2,
                "Assertion true; reason false—thionamides contraindicated.",
                ref("Case 2", "Answer: E) Order repeated thyroid function tests in 2 weeks with TSH-receptor antibodies"),
            ),
            ar(
                f"{p}-ar3",
                "CTLA4 hypophysitis",
                "Assertion: CTLA4 blockade carries higher hypophysitis risk than PD-1 monotherapy.",
                "Reason: Because ipilimumab pituitary dysfunction rate exceeds nivolumab in prevalence table.",
                0,
                "Both true—5.6% vs 0.5% in table.",
                ref(
                    "Table. Prevalence of Endocrinopathies During Immune Checkpoint Inhibitor Therapy",
                    "Ipilimumab ... Pituitary Dysfunction ... 5.6% ... Nivolumab ... 0.5%",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Cortisol before T4",
                "Assertion: Adrenal insufficiency must be treated before levothyroxine in ICI hypophysitis.",
                "Reason: Because levothyroxine can precipitate adrenal crisis if cortisol is deficient.",
                0,
                "Both true—standard hypophysitis management.",
                ref(
                    "Hypothyroidism",
                    "It is mandatory to screen for and treat hypoadrenalism before starting levothyroxine replacement.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Combination toxicity",
                "Assertion: Combination checkpoint inhibition increases endocrine adverse events.",
                "Reason: Because combination therapy reduces immune activation.",
                2,
                "Assertion true; reason false—combination increases immune toxicity.",
                ref(
                    "Significance of the Clinical Problem",
                    "in 20% to 30% of those treated with a combination of 2 checkpoint inhibitors.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Misattribution",
                "Assertion: ICI adrenal insufficiency may mimic progressive malignancy.",
                "Reason: Because lethargy and weight loss never occur in cancer patients.",
                2,
                "Assertion true; reason absurd—symptoms overlap with cancer progression.",
                ref(
                    "Barriers to Optimal Practice",
                    "may be misattributed to advancing cancer rather than to a readily treatable endocrinopathy",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Permanent adrenal",
                "Assertion: Secondary adrenal insufficiency from ICI hypophysitis is usually permanent.",
                "Reason: Because all pituitary axes always recover within 2 weeks.",
                2,
                "Assertion true; reason false—recovery rare for ACTH deficiency.",
                ref(
                    "Pituitary Dysfunction",
                    "Secondary adrenal insufficiency should be assumed to be permanent, although rare cases of recovery have been documented.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Thyrotoxicosis half",
                "Assertion: Approximately 50% of ICI thyrotoxicosis patients develop permanent hypothyroidism.",
                "Reason: Because thionamides prevent hypothyroid progression.",
                2,
                "Assertion true per Case 2; reason false—thionamides worsen hypothyroid phase.",
                ref("Case 2", "permanent hypothyroidism occurs in approximately 50% of cases."),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "42",
        "title": "How to Screen and Treat",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Simon H. S. Pearce, MD, FRCP",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_42_How_to_Screen_and_Treat.md",
        "items": items,
    }


def build_chapter_43() -> dict:
    p = "e21-43"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Antipsychotic prolactin",
                "Why hyperprolactinemia is common on antipsychotics",
                "Most antipsychotics act as D2 receptor antagonists; first-generation agents and risperidone/paliperidone elevate prolactin in most patients without underlying prolactinoma.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "Most antipsychotic agents work in part as dopamine D_{2} receptor antagonists. Thus, it is not surprising that hyperprolactinemia is a common adverse effect.",
                ),
            ),
            note(
                f"{p}-n2",
                "Dopamine agonist pitfall",
                "Why dopamine agonists may worsen psychiatric disease",
                "Treating drug-induced hyperprolactinemia with cabergoline while on dopamine antagonists is like 'stepping on gas and brake' and may exacerbate psychiatric symptoms.",
                ref(
                    "Case 1",
                    "starting one of these medications while being treated with an agent that is acting as a dopamine antagonist is a little like stepping on the gas and the brake at the same time",
                ),
            ),
            note(
                f"{p}-n3",
                "Case 1 management",
                "How to manage amenorrhea from paliperidone-induced hyperprolactinemia",
                "With depot paliperidone and well-controlled schizophrenia, estrogen replacement for bone health is preferred over dopamine agonists or risky antipsychotic switches.",
                ref("Case 1", "Answer: C) Start an oral contraceptive pill or other estrogen replacement"),
            ),
            note(
                f"{p}-n4",
                "Prolactin MRI thresholds",
                "When to defer MRI in medication-induced hyperprolactinemia",
                "On known prolactin-raising agents, prolactin <100 ng/mL often does not need MRI; risperidone/phenothiazines can exceed 200 ng/mL without tumor.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "In patients on an antipsychotic agent known to increase prolactin who have a prolactin concentration less than 100 ng/mL (<4.3 nmol/L), many clinicians would not routinely recommend MRI.",
                ),
            ),
            note(
                f"{p}-n5",
                "Metabolic monitoring",
                "How to monitor antipsychotic metabolic adverse effects",
                "Screen glucose and lipids per consensus guidance; consider BMI and diabetes checks as early as 4–6 weeks after initiation given rapid weight and glycemic changes.",
                ref(
                    "Management of Metabolic Changes",
                    "Given the significant patient variability and what can be very rapid-onset changes, earlier initial evaluation (eg, 4-6 weeks after start of treatment) may be most appropriate",
                ),
            ),
            note(
                f"{p}-n6",
                "Olanzapine diabetes",
                "Why olanzapine can cause rapid severe hyperglycemia",
                "Olanzapine causes rapid weight gain and direct effects on insulin signaling and pancreatic beta cells—DKA can occur even without major weight gain.",
                ref(
                    "Case 3",
                    "Answer: C) Olanzapine",
                ),
            ),
            note(
                f"{p}-n7",
                "Case 3 acute care",
                "How to manage acute antipsychotic-induced hyperglycemia",
                "Symptomatic glucose 420 mg/dL with rapid HbA1c rise requires insulin acutely; SGLT2 inhibitors or nutrition alone are insufficient.",
                ref("Case 3", "Answer: D) Start insulin"),
            ),
            note(
                f"{p}-n8",
                "Liothyronine depression",
                "Why liothyronine is used for refractory depression",
                "Despite limited blinded data, liothyronine augmentation remains an option for life-threatening treatment-resistant depression after failed antidepressant trials.",
                ref(
                    "Liothyronine as Augmentation Therapy for Depression",
                    "Strategies for treatment-refractory depression include augmentation therapy with nonantidepressant medications such as liothyronine (T₃).",
                ),
            ),
            note(
                f"{p}-n9",
                "T3 thyrotoxicosis",
                "How liothyronine causes low T4 with suppressed TSH",
                "Exogenous T3 suppresses TSH and lowers T4 via pituitary-thyroid axis—Case 2 patient on 75 mcg liothyronine had T3 thyrotoxicosis pattern.",
                ref(
                    "Case 2",
                    "further testing in the outpatient setting showed he had T_{3} thyrotoxicosis. This results in suppression of TSH and a subsequently low T_{4} level.",
                ),
            ),
            note(
                f"{p}-n10",
                "Liothyronine monitoring",
                "How to monitor liothyronine augmentation safely",
                "Target TSH at lower limit of normal; assess bone mineral density by DXA every 2 years to limit hyperthyroid complications.",
                ref(
                    "Liothyronine as Augmentation Therapy for Depression",
                    "It is also recommended to assess bone mineral density by DXA every 2 years while on therapy.",
                ),
            ),
            note(
                f"{p}-n11",
                "Communication",
                "Why endocrine-psychiatry communication is essential",
                "Never stop or change antipsychotics without psychiatric consultation; collaborative decisions balance psychiatric stability against endocrine harm.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "stopping an antipsychotic medication can be difficult and should never be done without consultation with the patient's mental health care provider.",
                ),
            ),
            note(
                f"{p}-n12",
                "Case 2 differential",
                "Why discordant TFTs in hospitalized psychiatric patients have broad differential",
                "Low TSH with low free T4 may reflect central hypothyroidism, euthyroid sick syndrome, assay interference, or T3 thyrotoxicosis—Answer E any of the above.",
                ref("Case 2", "Answer: E) Any of the above"),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "38-year-old on paliperidone depot, prolactin 125 ng/mL, 2-mm pituitary lesion, amenorrhea 2 years, stable psychosis. Best step?",
                [
                                        "Cabergoline",
                    "Ignore prolactin",
                    "Oral contraceptive or estrogen replacement",
                    "Switch antipsychotic immediately without psychiatry input",
],
                2,
                "Estrogen for hypogonadism/bone protection preferred over dopamine agonist or high-risk medication switch.",
                ref("Case 1", "Answer: C) Start an oral contraceptive pill or other estrogen replacement"),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 TFT",
                "Hospitalized patient: TSH 0.02, free T4 0.52. Possible explanations include:",
                [
                                        "Central hypothyroidism only",
                    "Laboratory error only",
                    "T3 thyrotoxicosis only",
                    "Any of the above",
],
                3,
                "Broad differential until outpatient clarification—ultimately liothyronine-induced T3 thyrotoxicosis.",
                ref("Case 2", "Answer: E) Any of the above"),
            ),
            mcq(
                f"{p}-q3",
                "Case 3 glycemia",
                "5 weeks after olanzapine for schizophrenia relapse, weight up 11 kg, glucose 420 mg/dL, HbA1c 9.1%. Most likely cause?",
                [
                                        "Poor diet alone",
                    "Poor diabetes medication adherence",
                    "Olanzapine adverse effect",
                    "New LADA",
],
                2,
                "Rapid profound weight gain and hyperglycemia classic for olanzapine metabolic toxicity.",
                ref("Case 3", "Answer: C) Olanzapine"),
            ),
            mcq(
                f"{p}-q4",
                "Case 3 treatment",
                "Same patient at visit with polyuria/polydipsia and glucose 420 mg/dL. Most appropriate intervention now?",
                [
                                        "Switch to aripiprazole only",
                    "Start SGLT2 inhibitor only",
                    "Nutrition referral only",
                    "Start insulin",
],
                3,
                "Acute symptomatic severe hyperglycemia requires insulin; psychiatry collaboration for antipsychotic change later.",
                ref("Case 3", "Answer: D) Start insulin"),
            ),
            mcq(
                f"{p}-q5",
                "Prolactin agents",
                "Which antipsychotic has minimal prolactin effect?",
                [
                                        "Risperidone",
                    "Paliperidone",
                    "Haloperidol",
                    "Aripiprazole",
],
                3,
                "Aripiprazole has partial agonist activity and minimal prolactin elevation per table.",
                ref(
                    "Table. Effect of Common Antipsychotic Medications on Increasing Prolactin",
                    "Aripiprazole ... -",
                ),
            ),
            mcq(
                f"{p}-q6",
                "High prolactin agents",
                "Highest prolactin elevation (+++) is seen with:",
                [
                                        "Clozapine",
                    "Quetiapine",
                    "Risperidone",
                    "Aripiprazole",
],
                2,
                "Risperidone, paliperidone, and amisulpride are +++ in the table.",
                ref(
                    "Table. Effect of Common Antipsychotic Medications on Increasing Prolactin",
                    "Risperidone ... +++",
                ),
            ),
            mcq(
                f"{p}-q7",
                "MRI deferral",
                "Prolactin 80 ng/mL on risperidone with temporal link to drug start. MRI:",
                [
                                        "Always mandatory immediately",
                    "May be deferred by many clinicians if medication clearly causal and prolactin modest",
                    "Never indicated in psychiatry patients",
                    "Replaces need for TFT",
],
                1,
                "Medication-induced hyperprolactinemia with clear temporal relationship may not need urgent MRI if <100 ng/mL on known agent.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "prolactin concentration less than 100 ng/mL (<4.3 nmol/L), many clinicians would not routinely recommend MRI.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Metabolic agents",
                "Most weight-neutral antipsychotics with less diabetes risk include:",
                [
                                        "Olanzapine and clozapine",
                    "Ziprasidone and aripiprazole",
                    "Risperidone and paliperidone",
                    "Chlorpromazine only",
],
                1,
                "Ziprasidone and aripiprazole are considered more weight-neutral with fewer diabetes-related events.",
                ref(
                    "Management of Metabolic Changes",
                    "Ziprasidone and aripiprazole are thought to be the most weight-neutral options with less diabetes-related adverse events",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Liothyronine dosing",
                "Typical starting liothyronine augmentation dose for depression is:",
                [
                                        "5 mcg once monthly",
                    "25 mcg daily increasing to 50 mcg after a week",
                    "200 mcg levothyroxine",
                    "No dosing exists",
],
                1,
                "Psychiatric literature commonly starts 25 mcg daily, titrating to 50 mcg.",
                ref(
                    "Liothyronine as Augmentation Therapy for Depression",
                    "The dosing recommendation is typically 25 mcg daily increased to 50 mcg daily after a week",
                ),
            ),
            mcq(
                f"{p}-q10",
                "STAR*D liothyronine",
                "STAR*D trial suggested liothyronine augmentation vs lithium had:",
                [
                                        "Marked inferior tolerability vs lithium",
                    "Slight advantages in effectiveness and tolerability vs lithium",
                    "No role in depression",
                    "Mandatory TSH suppression monitoring",
],
                1,
                "STAR*D authors noted slight advantages for T3 over lithium though study had limitations.",
                ref(
                    "Liothyronine as Augmentation Therapy for Depression",
                    "T_{3} has slight advantages over lithium in effectiveness and tolerability.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Hypogonadism from prolactin",
                "Primary clinical harm of antipsychotic hyperprolactinemia is:",
                [
                                        "Galactorrhea only in men",
                    "Hypogonadism leading to amenorrhea/low testosterone and bone loss",
                    "Hyperthyroidism",
                    "Adrenal crisis",
],
                1,
                "Hypogonadism from prolactin suppression of GnRH is the main clinically important consequence.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "the primary adverse effect of hyperprolactinemia is due to subsequent hypogonadism.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Routine prolactin screening",
                "Routine prolactin monitoring on antipsychotics is:",
                [
                                        "Recommended for all patients monthly",
                    "Not recommended unless symptomatic",
                    "Illegal",
                    "Replaces psychiatric follow-up",
],
                1,
                "Monitor for galactorrhea, amenorrhea, decreased libido rather than routine prolactin levels.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "we do not recommend routinely checking prolactin levels in patients on these medications.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Liothyronine safety",
                "Safety monitoring during liothyronine augmentation should include:",
                [
                                        "TSH at lower limit of normal and DXA every 2 years",
                    "No thyroid testing ever",
                    "Weekly CT chest",
                    "Only prolactin levels",
],
                0,
                "Updated guidance recommends TFT and periodic DXA during T3 augmentation.",
                ref(
                    "Liothyronine as Augmentation Therapy for Depression",
                    "assess bone mineral density by DXA every 2 years while on therapy.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "D2 mechanism",
                "Antipsychotic hyperprolactinemia results primarily from D2 receptor antagonism.",
                True,
                "D2 blockade disinhibits prolactin secretion.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "Most antipsychotic agents work in part as dopamine D_{2} receptor antagonists.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Routine prolactin",
                "Routine prolactin measurement is recommended for all patients on antipsychotics.",
                False,
                "Monitor symptoms; routine labs not recommended.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "we do not recommend routinely checking prolactin levels in patients on these medications.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Cabergoline case 1",
                "Cabergoline is the best first step for paliperidone-induced hyperprolactinemia with amenorrhea.",
                False,
                "Dopamine agonist risks psychiatric destabilization; estrogen replacement preferred.",
                ref("Case 1", "treating with a dopamine agonist (Answer A) ... carries with it the potential for exacerbating her psychiatric condition."),
            ),
            tf(
                f"{p}-tf4",
                "Olanzapine weight",
                "Olanzapine can cause >7% body weight gain rapidly.",
                True,
                "Olanzapine among agents with largest weight gains, sometimes >7% baseline.",
                ref(
                    "Antipsychotic Agents and Metabolic Alterations",
                    "olanzapine, clozapine, zotepine, and chlorpromazine result in some of the largest weight gains, which can be rapid and significant (gain of >7% of baseline weight).",
                ),
            ),
            tf(
                f"{p}-tf5",
                "DKA without weight gain",
                "Antipsychotic-associated DKA can occur without significant weight gain.",
                True,
                "Direct beta-cell and insulin signaling effects independent of weight.",
                ref(
                    "Antipsychotic Agents and Metabolic Alterations",
                    "acute decompensation with diabetic ketoacidosis ... in patients without weight gain.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Liothyronine monitoring",
                "Liothyronine augmentation requires thyroid function and bone density monitoring.",
                True,
                "Safety monitoring now recommended despite limited efficacy data.",
                ref(
                    "Liothyronine as Augmentation Therapy for Depression",
                    "Subsequent guidelines now recommend safety monitoring.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "T3 pattern",
                "T3 thyrotoxicosis from liothyronine can show suppressed TSH with low free T4.",
                True,
                "Exogenous T3 suppresses TSH and lowers T4.",
                ref(
                    "Case 2",
                    "T_{3} thyrotoxicosis. This results in suppression of TSH and a subsequently low T_{4} level.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Psychiatry consult",
                "Antipsychotic changes for endocrine adverse effects require psychiatric collaboration.",
                True,
                "Never stop or switch antipsychotics without mental health provider input.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "should never be done without consultation with the patient's mental health care provider.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Case 1 estrogen",
                "Assertion: Estrogen replacement is preferred over dopamine agonist in Case 1.",
                "Reason: Because cabergoline always improves psychosis on concurrent antipsychotics.",
                2,
                "Assertion true; reason false—agonist may worsen psychosis.",
                ref("Case 1", "providing estrogen for bone health (Answer C) would be the best option"),
            ),
            ar(
                f"{p}-ar2",
                "Prolactin MRI",
                "Assertion: Prolactin <100 ng/mL on known prolactin-raising antipsychotic may not require MRI.",
                "Reason: Because all prolactin elevation mandates immediate surgery.",
                2,
                "Assertion true per guidelines nuance; reason false.",
                ref(
                    "Antipsychotic Agents and Hyperprolactinemia",
                    "many clinicians would not routinely recommend MRI.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Olanzapine diabetes",
                "Assertion: Olanzapine likely caused rapid worsening glycemic control in Case 3.",
                "Reason: Because the rapid 11-kg weight gain pattern fits olanzapine toxicity.",
                0,
                "Both true—rapid weight gain and direct metabolic effects.",
                ref("Case 3", "The rapidity with which he has gained such a significant amount of weight is very suggestive of an olanzapine adverse effect"),
            ),
            ar(
                f"{p}-ar4",
                "Insulin acute",
                "Assertion: Insulin is required acutely for glucose 420 mg/dL with symptoms in Case 3.",
                "Reason: Because SGLT2 inhibitors alone correct DKA-level hyperglycemia immediately.",
                2,
                "Assertion true; reason false—insulin needed for acute severe hyperglycemia.",
                ref("Case 3", "he needs insulin (Answer D) acutely."),
            ),
            ar(
                f"{p}-ar5",
                "Liothyronine use",
                "Assertion: Liothyronine remains an option for refractory severe depression.",
                "Reason: Because large blinded RCTs proved definitive IQ-level efficacy.",
                2,
                "Assertion true per practice; reason overstates evidence quality.",
                ref(
                    "Liothyronine as Augmentation Therapy for Depression",
                    "Despite limited data on its clinical efficacy, liothyronine (T₃) remains a consideration",
                ),
            ),
            ar(
                f"{p}-ar6",
                "T3 thyrotoxicosis",
                "Assertion: Liothyronine therapy can produce T3 thyrotoxicosis with low T4.",
                "Reason: Because T3 suppresses TSH and lowers T4 concentrations.",
                0,
                "Both true per Case 2 mechanism.",
                ref(
                    "Case 2",
                    "T_{3} thyrotoxicosis. This results in suppression of TSH and a subsequently low T_{4} level.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Aripiprazole prolactin",
                "Assertion: Aripiprazole has minimal prolactin elevation.",
                "Reason: Because it acts as a pure D2 antagonist without agonist activity.",
                2,
                "Assertion true; reason false—it has partial agonist properties.",
                ref(
                    "Table. Effect of Common Antipsychotic Medications on Increasing Prolactin",
                    "Aripiprazole ... -",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Metabolic monitoring",
                "Assertion: Early metabolic monitoring (4–6 weeks) may catch rapid antipsychotic adverse effects.",
                "Reason: Because metabolic changes only occur after 5 years of therapy.",
                2,
                "Assertion true; reason false—changes can be rapid within weeks.",
                ref(
                    "Management of Metabolic Changes",
                    "earlier initial evaluation (eg, 4-6 weeks after start of treatment) may be most appropriate",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "43",
        "title": "The EndocrinologyPsychiatry InterfaceHow Do We Help Each Other",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Elizabeth J. Murphy, MD, DPhil; Kewchang Lee, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_43_The_EndocrinologyPsychiatry_InterfaceHow_Do_We_Help_Each_Other.md",
        "items": items,
    }


MODULES = {
    "endo2021_chapter_38_When_Thyroid_Function_Test_Results_Dont_Make_Sense.json": build_chapter_38,
    "endo2021_chapter_39_Surveillance_of_the_Patient_Who_Has_Had_Therapeutic_Hemithyroidectomy_for_Thyroid_Cancer.json": build_chapter_39,
    "endo2021_chapter_40_Management_of_Thyroid_Dysfunction_Before_and_During_Pregnancy.json": build_chapter_40,
    "endo2021_chapter_41_The_EndocrinologyOncology_InterfaceHow_Do_We_Help_Each_Other.json": build_chapter_41,
    "endo2021_chapter_42_How_to_Screen_and_Treat.json": build_chapter_42,
    "endo2021_chapter_43_The_EndocrinologyPsychiatry_InterfaceHow_Do_We_Help_Each_Other.json": build_chapter_43,
}


def write_module(filename: str, data: dict) -> tuple[Path, Path]:
    PORTAL_DATA.mkdir(parents=True, exist_ok=True)
    portal_path = PORTAL_DATA / filename
    portal_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
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
        pct = 100 * wh // notes if notes else 0
        print(
            f"Wrote {portal_path.name} ({len(data['items'])} items, {counts}, Why/How {wh}/{notes} = {pct}%)"
        )
        print(f"  Copied to {master_path}")


if __name__ == "__main__":
    main()
