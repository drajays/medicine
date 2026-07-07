#!/usr/bin/env python3
"""Generate Williams 15e module w15-04 — Laboratory Techniques for Recognition of Endocrine Disorders."""
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
OUT_NAME = "w15-04_Laboratory_Techniques_for_Recognition_of_Endocrine_Disorders.json"


def build() -> dict:
    p = "w15-04"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Endocrine lab dependence",
                "Why endocrinology relies on accurate laboratory measurements",
                "Small changes in hormone levels, biomarkers, or molecular markers may be more specific and sensitive for early disease detection than classic physical signs. Most endocrinologists no longer develop assays locally and must interpret results from centralized laboratories.",
                ref(
                    "KEY POINTS",
                    "The practice of endocrinology relies heavily on accurate laboratory measurements. Small changes in hormone levels, biomarkers, or molecular markers are often more specific and earlier indicators of disease than the appearance of physical symptoms.",
                ),
            ),
            note(
                f"{p}-n2",
                "Picomolar range",
                "Six-logarithm hormone concentration range",
                "Peripheral hormone levels range from 10⁻⁶ to 10⁻¹² mol/L—micromolar to picomolar—requiring exquisite analytic sensitivity and wide dynamic range. Antibody-based methods historically met these demands and remain widely used despite mass spectrometry advances.",
                ref(
                    "Laboratory Methods",
                    "Expressed in molar units to allow direct comparisons, peripheral hormone levels range from  $ 10^{-6} $ to  $ 10^{-12} $ mol/L (i.e., micromolar to picomolar concentrations). Thus, clinically useful analytic methods must have exquisite sensitivity.",
                ),
            ),
            note(
                f"{p}-n3",
                "Method-specific results",
                "Why immunoassay results are method-specific",
                "Even well-validated antibody assays with known reference intervals produce measurements that cannot be compared across laboratories or reagent platforms because cross-reactivity with hormone isoforms, fragments, and metabolites differs between methods.",
                ref(
                    "Laboratory Methods",
                    "this limitation is manifest as producing measurements that are method-specific, vitiating the ability of clinicians to compare measurements reported using different assays (e.g., assays from different laboratories) for the same hormone or biomarker.",
                ),
            ),
            note(
                f"{p}-n4",
                "Competitive immunoassays",
                "How competitive binding assays quantify analytes",
                "Labeled and unlabeled analyte compete for limited antibody binding sites; bound labeled analyte is inversely proportional to specimen analyte concentration. Competitive designs suit small molecules with a single epitope, such as steroid hormones.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "If the concentrations of antibody and labeled analyte are held constant, the amount of labeled analyte bound is inversely proportional to the concentration of the competing unlabeled analyte, as illustrated in Fig. 4.3.",
                ),
            ),
            note(
                f"{p}-n5",
                "Immunometric assays",
                "How sandwich immunometric assays work",
                "Capture antibody immunoextracts antigen; labeled detection antibody binds a second epitope forming a tertiary complex. Excess antibody yields fast first-order kinetics without steady-state competition, enabling 5–20 minute assays with broad measuring ranges.",
                ref(
                    "Epitope-Specific Immunometric Assays",
                    "The capture antibody immunoextracts the antigen from the sample, and the signal antibody binds to the capture antibody-antigen complex to form a tertiary complex.",
                ),
            ),
            note(
                f"{p}-n6",
                "LOD and heteroscedastic CV",
                "Why measurement variance is heteroscedastic",
                "Immunometric LOD occurs at low signal; competitive LOD at high signal. Percent CV rises at extremes where dose-response is lost. Mid-range QC variance underestimates imprecision near LOD or maximum response—critical for interpreting borderline values.",
                ref(
                    "Epitope-Specific Immunometric Assays",
                    "The highest percent CV (e.g., CV × 100) will occur at the extremes of the measurement where the analyte dose response is lost. This point is critical when interpreting assay results or monitoring quality control performance.",
                ),
            ),
            note(
                f"{p}-n7",
                "Monoclonal vs polyclonal",
                "Why monoclonal antibodies alter hormone measurements",
                "Monoclonal epitope specificity can cause marked patient-to-patient variation when hormones circulate as heterogeneous genetic variants, precursors, and degradation products, whereas polyclonal antisera cross-react more uniformly across isoforms.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "These genetic differences can cause marked variations in measurements made using assays with specific monoclonal antibodies, compared with more uniform measurements made using assays with polyclonal antisera that tend to cross-react with the multiple forms.",
                ),
            ),
            note(
                f"{p}-n8",
                "PTH and hCG cross-reactivity",
                "Method-specific PTH and hCG immunoassays",
                "Cross-reactivity among hCG molecular forms and among circulating PTH fragments causes method-specific differences. Three hCG assays calibrated identically diverge when free β-hCG fraction rises because cross-reactivity with fragments differs.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "Similarly, cross-reactivity among various circulating metabolic fragments causes method-specific differences in parathyroid hormone (PTH) assays.",
                ),
            ),
            note(
                f"{p}-n9",
                "Cortisol interference",
                "Cortisol immunoassay cross-reactivity and matrix effects",
                "Cortisol assays cross-react with corticosterone, 11-deoxycortisol, cortisone, and synthetic steroids. Albumin matrix effects also alter cortisol immunoassay results—mass spectrometry provides more robust steroid measurement.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "Cortisol is an example of an analyte for which major cross-reactivity with other steroids, such as corticosterone, 11-deoxycortisol, cortisone, and numerous synthetic steroids, causes significant immunoassay interferences.",
                ),
            ),
            note(
                f"{p}-n10",
                "Macroprolactin",
                "Why macroprolactin causes false hyperprolactinemia",
                "Endogenous antibodies bound to prolactin form macroprolactin, which is biologically inactive but detected by many immunometric assays, producing elevated prolactin discordant with absent clinical hyperprolactinemia.",
                ref(
                    "Analytic Specificity",
                    "endogenous antibodies bound to prolactin create what is referred to as macroprolactin. Macroprolactin is not biologically active but is measured in many immunometric assays.",
                ),
            ),
            note(
                f"{p}-n11",
                "Lateral flow assays",
                "Lateral flow point-of-care immunoassay design",
                "Specimen flows across capture and control antibody bands with gold-particle detection antibody; COVID-era lateral flow advances now extend toward home hormone testing, though most remain qualitative or semiquantitative.",
                ref(
                    "Lateral Flow Assays (Home-Based Tests)",
                    "A drop of specimen (e.g., blood, serum, plasma, urine) is placed on one end of the strip and carried across the analytic strip by lateral flow, passing first through the detection antibody reservoir and then over the capture antibodies in sequence.",
                ),
            ),
            note(
                f"{p}-n12",
                "Black box precision",
                "Why decimal precision can mislead clinicians",
                "User-friendly home and point-of-care devices conceal system details; numeric values reported to several decimal places can falsely suggest accuracy and reproducibility beyond the technology's technical limits.",
                ref(
                    "KEY POINTS",
                    "Numeric values, especially when reported to several decimal places, can falsely suggest levels of accuracy and reproducibility beyond the technical limits of the technology used.",
                ),
            ),
            note(
                f"{p}-n13",
                "LC-MS/MS adoption",
                "Why mass spectrometry is replacing immunoassays",
                "Since the early 2000s, LC-MS/MS systems measure hormones by molecular composition rather than antibody binding, improving specificity for steroids and increasingly replacing competitive immunoassays in reference laboratories.",
                ref(
                    "Laboratory Methods",
                    "Since the early 2000s, technologic advances in mass spectrometry-based assay systems have led to the rapid and ongoing replacement of antibody-based methods for the clinical measurement of hormones and biomarkers relevant to the endocrine practice.",
                ),
            ),
            note(
                f"{p}-n14",
                "Electrospray ionization",
                "How ESI links chromatography to mass spectrometry",
                "ESI pushes chromatography effluent through a charged capillary creating an aerosol; analytes ionize at low temperature with minimal fragmentation, enabling direct LC coupling and tandem MS specificity for endocrine analytes.",
                ref(
                    "Mass Spectrometry",
                    "This technology allows connection of liquid chromatography systems directly to mass spectrometry and is currently the method of choice for measuring analytes relevant to endocrinology, such as steroid hormones, in biologic fluids.",
                ),
            ),
            note(
                f"{p}-n15",
                "Triple quadrupole MRM",
                "Multiple reaction monitoring in steroid profiling",
                "Triple quadrupole instruments filter parent ions in Q1, fragment in Q2, and monitor product ions in Q3. MRM mode with fixed m/z transitions—e.g., testosterone 289/97—enables simultaneous steroid profiling with high specificity.",
                ref(
                    "Mass Spectrometry",
                    "Multiple reaction monitoring mode allows both analytic analyzers (quadrupoles 1 and 3) to be fixed, selecting for a specific m/z. This adjustment increases specificity and sensitivity.",
                ),
            ),
            note(
                f"{p}-n16",
                "Free hormone hypothesis",
                "Free versus total steroid hormone measurement",
                "Less than 5–10% of most steroid hormones circulate unbound; physiologic effects often depend on free concentration. Assay design must release or exclude protein-bound hormone depending on whether total or free hormone is intended.",
                ref(
                    "Free Hormone Methods",
                    "Less than 5% to 10% of most steroid hormones circulate as free (unbound) analytes, and assay design requires that the protein-bound analyte be released or does not interfere in the assay in order to have an accurate measure of the total hormone present.",
                ),
            ),
            note(
                f"{p}-n17",
                "Equilibrium dialysis",
                "Equilibrium dialysis for free hormone separation",
                "Dialysis membranes allow free steroid diffusion while retaining binding proteins. Free hormone in dialysate can be measured directly or calculated from labeled tracer distribution—but no established reference method exists for free steroids.",
                ref(
                    "Free Hormone Methods",
                    "One might easily get the misimpression, especially now that LC/MS-MS systems with sufficiently high sensitivity have been combined with it, that equilibrium dialysis is the method of choice or a gold standard method for measuring free hormones.",
                ),
            ),
            note(
                f"{p}-n18",
                "One-step free hormone pitfalls",
                "Why one-step free testosterone assays fail",
                "Labeled steroid analogues that do not bind carrier proteins compete for antibody in one-step formats; this assumption is invalid for free testosterone and only limited for free thyroxine across binding protein concentrations.",
                ref(
                    "Free Hormone Methods",
                    "This has been shown not to be true for free testosterone assays and is likely valid only over a limited range for binding protein concentrations for free thyroxine assays.",
                ),
            ),
            note(
                f"{p}-n19",
                "Carrier proteins",
                "CBG, SHBG, and TBG steroid carriers",
                "Corticosteroid-binding globulin carries glucocorticoids; sex hormone-binding globulin binds testosterone and estradiol; thyroxine-binding globulin carries T4 and T3. Carrier concentrations profoundly affect free hormone measurements and immunoassay interpretation.",
                ref(
                    "Free Hormone Methods",
                    "Corticosteroid-binding globulin (CBG) Glucocorticoids, mineralocorticoids",
                ),
            ),
            note(
                f"{p}-n20",
                "Hook effect",
                "How the hook effect falsifies very high values",
                "When antigen vastly exceeds capture antibody capacity, detection antibody is blocked and signal paradoxically decreases into the reportable range—potentially reporting zero analyte in extreme prolactinoma, hCG, or thyroglobulin specimens.",
                ref(
                    "Analytic Specificity",
                    "Extending the principle to the extreme, it is theoretically possible to have so much analyte present that all the binding sites on both the capture and detection antibodies are occupied; in this case, no detection antibody can be bound to the solid phase and the signal is baseline, which would be interpreted as no analyte present!",
                ),
            ),
            note(
                f"{p}-n21",
                "Biotin interference",
                "Why biotin supplements distort immunoassay results",
                "High-dose oral biotin competes with biotinylated reagents: falsely elevated competitive assays and falsely low immunometric assays. Concurrent high FT4 and low TSH from biotin can mimic thyrotoxicosis.",
                ref(
                    "Analytic Specificity",
                    "This can result in falsely elevated sample values in competitive binding immunoassays and falsely low sample values in immunometric assays.",
                ),
            ),
            note(
                f"{p}-n22",
                "PCR amplification",
                "How polymerase chain reaction amplifies DNA targets",
                "Denaturation, primer annealing, and polymerase extension double DNA copies each cycle; 20 cycles at 85–90% efficiency yields ~250,000-fold amplification, demanding rigorous contamination precautions.",
                ref(
                    "Amplification",
                    "At 85% to 90% efficiency, this process can amplify the DNA by about 250,000-fold in 20 cycles. This huge amplification is subject to major problems with contamination if special precautions are not taken.",
                ),
            ),
            note(
                f"{p}-n23",
                "Hybridization and NGS",
                "Nucleic acid hybridization and next-generation sequencing",
                "Complementary probe hybridization enables genotyping; NGS performs parallel sequencing of DNA/RNA fragments orders of magnitude faster and cheaper than Sanger sequencing, increasingly applied to endocrine tumors and inherited disease.",
                ref(
                    "Sequencing Methods",
                    "NGS approaches hold tremendous clinical diagnostic potential because parallel sequencing is faster and orders of magnitude cheaper than serial sequencing.",
                ),
            ),
            note(
                f"{p}-n24",
                "Analytic validation",
                "How analytic validation parameters interrelate",
                "Method validation requires demonstrating fitness for use through specificity, sensitivity, precision, accuracy, utility (robustness), and interpretation parameters including reportable range and reference intervals—an iterative development process.",
                ref(
                    "Analytic Validation",
                    "These characteristics include sensitivity, specificity, precision, and accuracy. Validation must also include specification of the assay's utility and provide data to support the clinical interpretation of results generated by the assay",
                ),
            ),
            note(
                f"{p}-n25",
                "Quality control",
                "Quality control versus quality assurance",
                "QC monitors control materials within validated limits detecting random and systematic analytic errors. QA extends beyond analytic phase—most laboratory errors occur preanalytically; clinicians must flag discordant results for laboratory investigation.",
                ref(
                    "Quality Assurance",
                    "As illustrated in Fig. 4.27, errors that occur during the analytic process represent less than a third of all errors associated with laboratory testing.",
                ),
            ),
            note(
                f"{p}-n26",
                "CLIA and FDA classes",
                "CLIA certification versus FDA assay regulation",
                "CLIA governs laboratory certification and reimbursement; FDA regulates instrument and reagent manufacture under cGMP. FDA-cleared kits require limited laboratory verification; laboratory-developed tests require full validation.",
                ref(
                    "Classes of Assays",
                    "Requirements for laboratory-developed methods, which include any modifications of FDA-approved/cleared commercial procedures, are more extensive, and validation per se is expected.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Lab dependence",
                "A resident evaluates a patient with subtle biochemical abnormalities but minimal symptoms. According to Williams, why is early endocrine diagnosis increasingly laboratory-driven?",
                [
                    "Physical examination remains more sensitive than any biomarker",
                    "Small hormone or molecular marker changes may precede and outspecific classic signs",
                    "All endocrine disorders present with pathognomonic stigmata",
                    "Centralized laboratories eliminate the need for clinical correlation",
                ],
                1,
                "Endocrinology depends on detecting small, specific laboratory changes before overt clinical disease.",
                ref(
                    "KEY POINTS",
                    "Small changes in hormone levels, biomarkers, or molecular markers are often more specific and earlier indicators of disease than the appearance of physical symptoms.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Picomolar sensitivity",
                "TSH must be measured alongside analytes spanning six orders of magnitude in molar concentration. What analytic property is therefore essential?",
                [
                    "Narrow dynamic range with high upper limit only",
                    "Exquisite sensitivity and very wide dynamic range",
                    "Measurement only in mass units without molar conversion",
                    "Elimination of all antibody-based methods",
                ],
                1,
                "Endocrine hormones range from micromolar to picomolar requiring both sensitivity and wide dynamic range.",
                ref(
                    "Laboratory Methods",
                    "Thus, clinically useful analytic methods must have exquisite sensitivity.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Method comparison",
                "A patient's TSH is 2.1 mIU/L at hospital A and 4.8 mIU/L at hospital B on the same day, both within each lab's reference interval. Best explanation?",
                [
                    "One laboratory must have a random error only correctable by repeat",
                    "Immunoassay measurements for the same hormone are often method-specific and not directly comparable",
                    "TSH cannot be measured by immunoassay",
                    "Reference intervals are identical across all platforms by regulation",
                ],
                1,
                "Well-validated assays still produce method-specific results that cannot be extrapolated across reagent systems.",
                ref(
                    "Laboratory Methods",
                    "this limitation is manifest as producing measurements that are method-specific, vitiating the ability of clinicians to compare measurements reported using different assays",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Competitive vs immunometric",
                "Which analyte class is most appropriately measured by a competitive (not sandwich) immunoassay?",
                [
                    "Intact TSH dimer",
                    "Cortisol",
                    "Macroprolactin complex",
                    "Intact hCG with α-β bridge antibody pair",
                ],
                1,
                "Competitive assays are used primarily for small molecules with a single epitope such as steroid hormones.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "In clinical practice today, competitive assays are used primarily for the measurement of small molecules, such as steroid hormones or bioactive peptides, which present only one antigenic epitope.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Immunometric kinetics",
                "Compared with competitive immunoassays, immunometric sandwich assays are faster primarily because:",
                [
                    "They require establishment of binding steady state before quantitation",
                    "Excess antibody yields first-order kinetics without steady-state competition",
                    "They use only polyclonal antisera",
                    "They cannot be automated",
                ],
                1,
                "Immunometric assays use antibody excess and do not require time-consuming steady-state competition.",
                ref(
                    "Epitope-Specific Immunometric Assays",
                    "these assays are referred to as immunometric because the binding reaction is very fast (first-order kinetics due to excess antibody) and because it is not necessary to establish a binding steady state",
                ),
            ),
            mcq(
                f"{p}-q6",
                "LOD interpretation",
                "An immunometric assay reports a value just above the limit of detection with percent CV >20%. What pitfall applies?",
                [
                    "Mid-range precision always reflects extreme-range imprecision",
                    "Heteroscedastic variance is highest at LOD and maximum response extremes",
                    "LOD is identical for competitive and immunometric designs",
                    "CV is constant across the entire measuring range",
                ],
                1,
                "Variance increases at assay extremes where dose-response is lost; borderline LOD values have poor precision.",
                ref(
                    "Epitope-Specific Immunometric Assays",
                    "The highest percent CV (e.g., CV × 100) will occur at the extremes of the measurement where the analyte dose response is lost.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Monoclonal isoforms",
                "Two LH assays—one polyclonal, one monoclonal—give discordant results in a patient with a genetic LH variant. Why?",
                [
                    "Monoclonal antibodies cross-react uniformly with all isoforms",
                    "Monoclonal epitope specificity detects variant forms differently than polyclonal antisera",
                    "LH cannot be measured immunometrically",
                    "Genetic variants never affect immunoassays",
                ],
                1,
                "Monoclonal epitope specificity can cause marked variation versus polyclonal cross-reactivity across hormone isoforms.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "These genetic differences can cause marked variations in measurements made using assays with specific monoclonal antibodies, compared with more uniform measurements made using assays with polyclonal antisera",
                ),
            ),
            mcq(
                f"{p}-q8",
                "PTH fragments",
                "Serial PTH values trend differently when the hospital switches reagent lots despite unchanged clinical status. Most likely explanation?",
                [
                    "Preanalytic hemolysis alone",
                    "Cross-reactivity differences among circulating PTH fragments between assays",
                    "PTH is measured only by mass spectrometry clinically",
                    "Hook effect always lowers values on new reagents",
                ],
                1,
                "PTH assays differ in recognition of circulating metabolic fragments causing method-specific trends.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "cross-reactivity among various circulating metabolic fragments causes method-specific differences in parathyroid hormone (PTH) assays.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Cortisol cross-reactivity",
                "A patient on prednisone has serum cortisol measured by immunoassay. Which pitfall is most relevant?",
                [
                    "Prednisone never cross-reacts in any cortisol assay",
                    "Structural similarity among steroids and synthetic glucocorticoids causes immunoassay interference",
                    "Cortisol must be measured only in urine",
                    "Albumin never affects cortisol immunoassays",
                ],
                1,
                "Cortisol immunoassays cross-react with corticosterone, 11-deoxycortisol, cortisone, and numerous synthetic steroids.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "Cortisol is an example of an analyte for which major cross-reactivity with other steroids, such as corticosterone, 11-deoxycortisol, cortisone, and numerous synthetic steroids, causes significant immunoassay interferences.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Macroprolactin",
                "A woman has prolactin 180 ng/mL, normal menses, and no galactorrhea. MRI shows no adenoma. Next best step?",
                [
                    "Immediate transsphenoidal surgery",
                    "Evaluate for macroprolactin with polyethylene glycol precipitation or equivalent",
                    "Assume assay is always biologically accurate",
                    "Start dopamine agonist without further testing",
                ],
                1,
                "Macroprolactin is inactive but immunoreactive; precipitation distinguishes true hyperprolactinemia.",
                ref(
                    "Analytic Specificity",
                    "Macroprolactin is not biologically active but is measured in many immunometric assays. This results in prolactin levels being reported as elevated, a result that is discordant with the absent clinical manifestations of hyperprolactinemia.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Home lateral flow",
                "A patient uses a home lateral flow hormone test with smartphone readout. What limitation should the clinician emphasize?",
                [
                    "Lateral flow assays exceed reference-lab precision for all hormones",
                    "Most remain qualitative or semiquantitative despite user-friendly formats",
                    "Lateral flow cannot detect any protein hormones",
                    "Home tests eliminate all preanalytic variables",
                ],
                1,
                "Lateral flow home tests are advancing but remain primarily qualitative or semiquantitative for hormones.",
                ref(
                    "Lateral Flow Assays (Home-Based Tests)",
                    "However, currently they remain primarily qualitative of semiquantitative methods.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Decimal precision trap",
                "A point-of-care device reports free T4 as 1.247 ng/dL. What conceptual error should the clinician avoid?",
                [
                    "Assuming reported decimal places reflect true analytic reproducibility",
                    "Ignoring that all POCT devices are FDA-cleared for free T4",
                    "Treating any numeric output as a reference-method value",
                    "Both A and C",
                ],
                3,
                "Black-box systems may report excessive decimal precision beyond technical limits—numeric output is not necessarily reference-quality.",
                ref(
                    "KEY POINTS",
                    "Numeric values, especially when reported to several decimal places, can falsely suggest levels of accuracy and reproducibility beyond the technical limits of the technology used.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "LC-MS/MS advantage",
                "A reference laboratory replaces serum testosterone immunoassay with LC-MS/MS. Primary analytic advantage?",
                [
                    "Indirect competition for antibody binding sites",
                    "Quantitation based on molecular composition and unique m/z transitions rather than antibody cross-reactivity",
                    "Elimination of all preanalytic specimen requirements",
                    "Lower specificity than immunoassay for steroids",
                ],
                1,
                "MS measures analytes by molecular composition via chromatographic separation and specific ion transitions.",
                ref(
                    "Mass Spectrometry",
                    "The technical advantages of the mass spectrometer (measurements based directly on the molecular composition of the analyte rather than indirect competition of the analyte for antibody binding)",
                ),
            ),
            mcq(
                f"{p}-q14",
                "ESI principle",
                "In LC-MS/MS endocrine testing, electrospray ionization primarily enables:",
                [
                    "Heat volatilization of steroids without derivatization only",
                    "Direct coupling of liquid chromatography effluent to the mass spectrometer with low-fragmentation ionization",
                    "Elimination of internal standards",
                    "Replacement of all nucleic acid testing",
                ],
                1,
                "ESI creates charged aerosol from LC effluent, enabling automated high-throughput LC-MS/MS.",
                ref(
                    "Mass Spectrometry",
                    "This technology allows connection of liquid chromatography systems directly to mass spectrometry and is currently the method of choice for measuring analytes relevant to endocrinology",
                ),
            ),
            mcq(
                f"{p}-q15",
                "MRM mode",
                "A laboratory profiles nine serum steroids simultaneously using fixed parent/product ion pairs. Which MS mode is used?",
                [
                    "Electron impact scanning only",
                    "Multiple reaction monitoring on a triple quadrupole instrument",
                    "Southern blot hybridization",
                    "Equilibrium dialysis alone",
                ],
                1,
                "MRM with fixed quadrupole m/z filters enables specific multi-steroid quantitation after LC separation.",
                ref(
                    "Mass Spectrometry",
                    "Multiple reaction monitoring mode allows both analytic analyzers (quadrupoles 1 and 3) to be fixed, selecting for a specific m/z.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Free hormone carriers",
                "A man has low SHBG and symptoms of androgen excess. Total testosterone is mid-normal. Which measurement best reflects tissue androgen exposure per the free hormone framework?",
                [
                    "Total testosterone alone always suffices",
                    "Free testosterone accounting for SHBG binding",
                    "TBG concentration",
                    "Urinary cortisol only",
                ],
                1,
                "Physiologic steroid effects often depend on free hormone; SHBG markedly influences free testosterone.",
                ref(
                    "Free Hormone Methods",
                    "in many cases the physiologic effects of steroid hormones depend on the free hormone concentration rather than the total hormone concentration.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Equilibrium dialysis limits",
                "A colleague calls equilibrium dialysis the gold standard for free T4. Most accurate response?",
                [
                    "Equilibrium dialysis is the established reference method for all free hormones",
                    "No established reference method exists; dialysis may not replicate in vivo conditions",
                    "One-step analogue immunoassays are always superior",
                    "Free hormones cannot be measured in clinical practice",
                ],
                1,
                "Williams cautions that no established reference method exists for free steroid hormones.",
                ref(
                    "Free Hormone Methods",
                    "it must be emphasized that currently there is no established reference method for the measurement of free steroid hormones",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Free testosterone assay",
                "Direct free testosterone immunoassay correlates with total testosterone but not with equilibrium dialysis free testosterone. Explanation?",
                [
                    "Analogue one-step assays are invalidated by binding protein complexity",
                    "Free testosterone does not exist in serum",
                    "SHBG has no effect on any assay",
                    "Mass spectrometry cannot measure testosterone",
                ],
                1,
                "One-step analogue competitive free testosterone assays have been shown not to measure true free testosterone.",
                ref(
                    "Free Hormone Methods",
                    "This has been shown not to be true for free testosterone assays and is likely valid only over a limited range for binding protein concentrations for free thyroxine assays.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Hook effect",
                "A giant prolactinoma patient has prolactin reported as 45 ng/mL (mildly elevated) despite massive tumor on MRI. First laboratory action?",
                [
                    "Accept result; hook effect is theoretical only",
                    "Request serial dilution and retesting to exclude hook effect",
                    "Switch to urine prolactin only",
                    "Disregard prolactin entirely in prolactinomas",
                ],
                1,
                "Extreme antigen excess can paradoxically lower immunometric signal; dilution reveals true concentration.",
                ref(
                    "Analytic Specificity",
                    "Hook effects occur and are extremely important to recognize in the context of measuring hormones in patients with tumors that secrete large quantities of the hormone.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Biotin interference",
                "A patient on high-dose biotin supplements has FT4 elevated and TSH suppressed on the same platform. Before diagnosing thyrotoxicosis, you should:",
                [
                    "Ignore supplements; biotin never affects immunoassays",
                    "Suspect biotin interference with streptavidin-based assays and confirm after biotin hold or alternate method",
                    "Order only total T4",
                    "Assume Graves disease without further evaluation",
                ],
                1,
                "Biotin causes falsely high competitive and falsely low immunometric results on biotin-streptavidin systems.",
                ref(
                    "Analytic Specificity",
                    "If, for example, free thyroxine and TSH assays both use biotin, the reported free thyroxine can be falsely high and the reported TSH can be falsely low, a situation that could be mistakenly interpreted as indicative of thyrotoxicosis.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "PCR contamination",
                "A molecular lab reports a pathogenic RET variant on repeat testing after initial negative result in a low-prevalence context. Most likely technical explanation?",
                [
                    "PCR cannot amplify endocrine gene targets",
                    "Amplicon contamination given extreme PCR amplification efficiency",
                    "Hybridization never produces false positives",
                    "NGS eliminates all contamination risk",
                ],
                1,
                "PCR's ~250,000-fold amplification in 20 cycles demands strict contamination control.",
                ref(
                    "Amplification",
                    "This huge amplification is subject to major problems with contamination if special precautions are not taken.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "NGS in endocrinology",
                "Which application best reflects current clinical NGS use in endocrine practice per Williams?",
                [
                    "Routine replacement of all serum hormone immunoassays",
                    "Characterization of advanced malignancies and inherited endocrine syndromes",
                    "Elimination of analytic validation requirements",
                    "Exclusive use in research without clinical laboratories",
                ],
                1,
                "NGS is increasingly used for endocrine tumors, inherited disease, and targeted therapeutics.",
                ref(
                    "Sequencing Methods",
                    "Until recently, NGS was primarily a research tool providing unique information concerning the mechanisms of disease, but it is playing a rapidly increasing role in clinical medicine—for example, for the characterization of advanced malignancies, among others.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Analytic specificity",
                "An assay generates signal from a structurally similar steroid metabolite. Which validation parameter is directly violated?",
                [
                    "Precision only",
                    "Analytic specificity (and thereby accuracy)",
                    "Specimen transport time",
                    "CLIA inspection interval",
                ],
                1,
                "Specificity is the ability to measure only the intended analyte; cross-reactivity undermines accuracy.",
                ref(
                    "Analytic Specificity",
                    "Analytic specificity can be simply defined as the ability of the assay to measure only the intended analyte.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Reference intervals",
                "A laboratory adopts a new TSH reagent lot. What must be reassessed?",
                [
                    "Only instrument serial number",
                    "Reference intervals and clinical decision points may shift with reagent changes",
                    "Reference intervals are universal across all methods by FDA mandate",
                    "Nothing if QC materials are within range",
                ],
                1,
                "Reagent lot changes can alter immunoassay performance requiring reference interval revision.",
                ref(
                    "Robustness (Assay Stability)",
                    "changes in antisera can cause significant changes in immunoassay performance, which in turn require revising reference interval and clinical decision points.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Discordant results workup",
                "Clinical picture conflicts with a markedly elevated immunometric tumor marker. Best initial laboratory troubleshooting sequence?",
                [
                    "Repeat on same specimen; consider dilution for hook effect; test heterophile blockers",
                    "Accept numeric value without question",
                    "Change diagnosis to match the laboratory",
                    "Discontinue all tumor marker monitoring",
                ],
                0,
                "QA emphasizes repeat testing, dilution linearity, recovery studies, and interference evaluation including heterophile antibodies.",
                ref(
                    "Quality Assurance",
                    "Repeated testing of the same specimen is a valuable first step.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "LDT vs FDA kit",
                "A hospital lab modifies an FDA-cleared immunoassay extraction step before reporting patient results. Regulatory implication in the US?",
                [
                    "No additional validation beyond manufacturer insert",
                    "Modified procedure is a laboratory-developed test requiring more extensive validation",
                    "CLIA exempts all endocrine assays",
                    "FDA premarket approval is never required for any assay component",
                ],
                1,
                "Modifications of cleared commercial procedures are LDTs requiring full laboratory validation.",
                ref(
                    "Classes of Assays",
                    "Requirements for laboratory-developed methods, which include any modifications of FDA-approved/cleared commercial procedures, are more extensive, and validation per se is expected.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Lab reliance",
                "Most practicing endocrinologists today develop and validate their own hormone assays in clinic laboratories.",
                False,
                "Most endocrinologists rely on centralized hospital or commercial reference laboratories rather than local assay development.",
                ref(
                    "KEY POINTS",
                    "Most endocrinologists no longer have facilities to develop and validate laboratory assays. They must rely on centralized hospital or commercial reference laboratories.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Method harmonization",
                "Well-validated immunoassays with established reference intervals always yield directly comparable numeric results across different manufacturers for the same hormone.",
                False,
                "Method-specific measurements cannot be extrapolated across assays using different reagents.",
                ref(
                    "Laboratory Methods",
                    "assay results cannot be extrapolated across assays using different reagents.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Immunometric speed",
                "Immunometric assays typically require longer incubation than competitive assays because steady-state competition must be established.",
                False,
                "Immunometric assays are faster (5–20 minutes) because they do not require steady-state competition.",
                ref(
                    "Epitope-Specific Immunometric Assays",
                    "Immunometric assays can be performed very quickly (5–20 minutes compared to 30 minutes to days for competitive assays)",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Sandwich cross-reactivity",
                "A pair of antibodies in an immunometric assay generally has lower cross-reactivity than either antibody alone because both epitopes must be present.",
                True,
                "Cross-reacting substances must bind both epitopes simultaneously; paired cross-reactivity is less than the product of individual cross-reactivities.",
                ref(
                    "Epitope-Specific Immunometric Assays",
                    "The cross-reactivity of a pair of antibodies is less than the cross-reactivity of each of the individual antibodies because any cross-reacting substance must contain both binding epitopes to simultaneously bind to both antibodies.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Antigen vs bioactivity",
                "Immunoassays always measure biologic activity of hormones because antibody epitopes coincide with receptor activation sites.",
                False,
                "Antigenic epitopes recognized by antibodies are not necessarily identical to structural elements involved in receptor activation.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "the structural elements of the hormone involved in receptor activation and biologic signaling, are not necessarily identical to antigenic epitopes recognized in the assay.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "LC-MS/MS adoption",
                "Mass spectrometry-based methods are rapidly replacing many antibody-based hormone assays, especially competitive immunoassays, in clinical laboratories.",
                True,
                "Technologic advances since the early 2000s have driven ongoing replacement of antibody methods, particularly in reference and academic laboratories.",
                ref(
                    "Laboratory Methods",
                    "technologic advances in mass spectrometry-based assay systems have led to the rapid and ongoing replacement of antibody-based methods",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Free hormone gold standard",
                "Equilibrium dialysis combined with LC-MS/MS is the universally accepted reference method for free steroid hormones.",
                False,
                "Williams states there is no established reference method for free steroid hormone measurement.",
                ref(
                    "Free Hormone Methods",
                    "currently there is no established reference method for the measurement of free steroid hormones",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Hook effect",
                "The hook effect can cause falsely low or undetectable immunometric results when analyte concentration vastly exceeds assay capacity.",
                True,
                "Extreme antigen excess can block detection antibody binding and return signal toward baseline.",
                ref(
                    "Analytic Specificity",
                    "no detection antibody can be bound to the solid phase and the signal is baseline, which would be interpreted as no analyte present!",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Heterophile antibodies",
                "Heterophile antibodies can cause falsely elevated immunometric results by bridging capture and detection antibodies without analyte present.",
                True,
                "Bivalent endogenous anti-animal IgG antibodies can link assay antibodies independent of analyte.",
                ref(
                    "Analytic Specificity",
                    "endogenous antibodies (called heterophile antibodies) to animal immunoglobulins can, because antibodies are bivalent, link the detection antibody to the solid-phase capture antibody in the absence of analyte, resulting in a falsely high value reported.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "PCR efficiency",
                "Twenty PCR cycles at 85–90% efficiency can amplify target DNA approximately 250,000-fold.",
                True,
                "Exponential amplification makes contamination control essential.",
                ref(
                    "Amplification",
                    "At 85% to 90% efficiency, this process can amplify the DNA by about 250,000-fold in 20 cycles.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "QC error distribution",
                "Analytic-phase errors account for the majority of all laboratory testing errors.",
                False,
                "Analytic errors represent less than a third of total laboratory testing errors.",
                ref(
                    "Quality Assurance",
                    "errors that occur during the analytic process represent less than a third of all errors associated with laboratory testing.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "LDT validation",
                "Laboratory-developed tests and modified FDA-cleared methods require more extensive validation than verification alone for unmodified cleared kits.",
                True,
                "LDTs require full validation; cleared kits require limited verification studies.",
                ref(
                    "Classes of Assays",
                    "Requirements for laboratory-developed methods, which include any modifications of FDA-approved/cleared commercial procedures, are more extensive, and validation per se is expected.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Specimen dilution",
                "When an immunometric result exceeds the reportable range, serial dilution and retesting is an important step to obtain accurate quantitation and detect hook effect.",
                True,
                "Laboratories dilute high specimens; dilution also unmasks hook effect artifacts.",
                ref(
                    "Analytic Specificity",
                    "the laboratory can control variance associated with high analyte concentrations by determining at what level of analyte to dilute and retest the specimen",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Picomolar measurement",
                "Assertion: Endocrine hormone immunoassays require antisera with very high affinity constants.",
                "Reason: Peripheral hormone concentrations can be in the picomolar range requiring sensitive binding assays.",
                0,
                "Both are true; high-affinity antisera (often >10¹² L/M) enable picomolar measurement because hormone concentrations are extremely low.",
                ref(
                    "Classic Competitive Binding Immunoassays",
                    "Antisera used in immunoassays typically have affinity constants above the  $ 10^{12} $ L/M range and can easily measure picomolar concentrations of analytes in biologic fluids.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Method-specific calibration",
                "Assertion: Two immunoassays calibrated with the same WHO reference preparation can report different patient results.",
                "Reason: Assays differ in cross-reactivity with circulating hormone isoforms and fragments.",
                0,
                "Both true and linked: identical calibrator recovery does not ensure identical patient measurements when isoform cross-reactivity differs.",
                ref(
                    "Epitope-Specific Immunometric Assays",
                    "Two immunoassays calibrated with the same reference preparation can give widely varying measurements on patient specimens.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Immunometric LOD",
                "Assertion: In an immunometric assay the limit of detection is associated with a small signal.",
                "Reason: In a competitive assay the limit of detection is associated with a large signal.",
                1,
                "Both statements are true but describe different assay designs; the assertion's reason should explain immunometric LOD (low signal at zero analyte), not competitive assay behavior.",
                ref(
                    "Epitope-Specific Immunometric Assays",
                    "for an immunometric assay the LOD is associated with a small signal, but in a competitive assay the LOD is associated with a large signal",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Gonadotropin cross-reactivity",
                "Assertion: Modern two-antibody LH assays have cross-reactivity with hCG less than 0.01%.",
                "Reason: A cross-reactant must possess both epitopes recognized by capture and detection antibodies.",
                0,
                "Both true; dual-epitope requirement multiplies individual cross-reactivities, minimizing gonadotropin cross-reactivity.",
                ref(
                    "Epitope-Specific Immunometric Assays",
                    "The cross-reactivity of the pair is less than the product of the two cross-reactivities or, in this case, less than 0.01%.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "ESI and LC-MS/MS",
                "Assertion: Electrospray ionization enabled routine clinical LC-MS/MS for endocrine steroids.",
                "Reason: ESI allows direct coupling of liquid chromatography effluent to the mass spectrometer.",
                0,
                "Both true and causally linked: ESI's LC coupling was the key advance enabling clinical steroid MS.",
                ref(
                    "Mass Spectrometry",
                    "ESI has directly resulted in the development of systems that are rapidly replacing the antibody-based assays in the clinical laboratory.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "MRM specificity",
                "Assertion: Multiple reaction monitoring improves specificity for testosterone measurement.",
                "Reason: Two quadrupoles select fixed parent and product m/z transitions unique to testosterone.",
                0,
                "Both true; fixed MRM transitions confirm analyte identity after chromatographic separation.",
                ref(
                    "Mass Spectrometry",
                    "For example, two unique ions (first/second analyzer) for testosterone are 289.221/97.140 and 289.222/109.130.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Free testosterone immunoassay",
                "Assertion: One-step analogue free testosterone immunoassays do not accurately measure free testosterone.",
                "Reason: Competition kinetics among multiple binding proteins and the antibody are too complex for the analogue assumption.",
                0,
                "Both true; binding protein complexity invalidates the one-step analogue competitive design.",
                ref(
                    "Free Hormone Methods",
                    "for free steroid assay designs, the kinetics of competition and binding are very complex given the variety of proteins interacting with steroid hormones over a wide range of affinities.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Hook effect prolactin",
                "Assertion: A patient with giant prolactinoma can have falsely low serum prolactin by immunometric assay.",
                "Reason: Extreme antigen excess can saturate capture and detection antibodies reducing signal.",
                0,
                "Both true; hook effect is the mechanism for paradoxically low prolactin in macroprolactinomas.",
                ref(
                    "Analytic Specificity",
                    "analyte concentrations vastly exceeding the binding capacity of the capture antibody result in also blocking the detection antibody, resulting in a decrease in signal back into the reportable range.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Biotin thyrotoxicosis mimic",
                "Assertion: High-dose biotin ingestion can produce a pattern mimicking thyrotoxicosis on some platforms.",
                "Reason: Biotin competes with biotinylated reagents causing falsely high FT4 and falsely low TSH on the same analyzer.",
                0,
                "Both true; opposing directional interference on competitive and immunometric biotin-based assays creates misleading combined pattern.",
                ref(
                    "Analytic Specificity",
                    "the reported free thyroxine can be falsely high and the reported TSH can be falsely low, a situation that could be mistakenly interpreted as indicative of thyrotoxicosis.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Specificity and accuracy",
                "Assertion: An immunoassay cannot be accurate if it lacks analytic specificity.",
                "Reason: Specificity is defined as measuring only the intended analyte, which accuracy requires.",
                0,
                "Both true; nonspecific signal prevents accurate concentration estimation though specificity alone does not guarantee accuracy.",
                ref(
                    "Analytic Specificity",
                    "an assay cannot be accurate if it is not specific.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Heterophile false elevation",
                "Assertion: Heterophile antibody interference can cause falsely elevated tumor marker immunoassay results.",
                "Reason: Heterophile antibodies are bivalent and can cross-link assay antibodies without analyte.",
                0,
                "Both true; bivalent heterophile bridging of capture and detection antibodies elevates signal independent of analyte.",
                ref(
                    "Analytic Specificity",
                    "endogenous antibodies (called heterophile antibodies) to animal immunoglobulins can, because antibodies are bivalent, link the detection antibody to the solid-phase capture antibody in the absence of analyte",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Pulsatile specimen timing",
                "Assertion: Single random serum cortisol measurements can mislead when interpreting pulsatile secretion.",
                "Reason: Reproductive hormone reference intervals require high-resolution sampling across the menstrual cycle.",
                0,
                "Both true; pulsatile and cyclic secretion demands timed sampling and nuanced reference intervals—specimen timing is a preanalytic pitfall.",
                ref(
                    "Interpretation Parameters",
                    "The reference intervals for many endocrine tests depend on sex, age, developmental status, and other test values.",
                ),
            ),
        ]
    )

    return {
        "id": "w15-04",
        "volume": 15,
        "chapterNo": "4",
        "title": "Laboratory Techniques for Recognition of Endocrine Disorders",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Patrick M. Sluss, Martin Bidlingmaier, Frances J. Hayes",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_04_Laboratory_Techniques_for_Recognition_of_Endocrine_Disorders.md",
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
