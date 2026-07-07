#!/usr/bin/env python3
"""Generate remediated ESAP 2021 modules e21-17 through e21-20 (Diabetes batch)."""
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


def build_chapter_17() -> dict:
    p = "e21-17"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Hybrid closed-loop",
                "Why postmeal glucose remains difficult on hybrid closed-loop pumps",
                "Despite improved overall glycemic control, regulating postmeal glucose is still challenging because carbohydrate counting is imperfect for mixed meals and the patient—not the algorithm—still determines meal boluses.",
                ref(
                    "Main Conclusions",
                    "With the use of hybrid closed-loop pumps, despite the improvement in glycemic control, regulating postmeal glucose concentrations is still a challenge.",
                ),
            ),
            note(
                f"{p}-n2",
                "CGM metrics",
                "How to use time in range when interpreting pump downloads",
                "Target time in range >70%, time below range <4%, and time above range <25% for most adults; fourteen days of CGM data correlate well with hemoglobin A1c and respond faster to regimen changes than A1c alone.",
                ref(
                    "Usual Target Recommendations",
                    "Time in range >70%",
                ),
            ),
            note(
                f"{p}-n3",
                "GMI discordance",
                "Why glucose management indicator may differ from hemoglobin A1c",
                "When GMI is lower than A1c, consider avoiding hypoglycemia or raising the A1c target; when GMI is higher, address hyperglycemia. Discordance may reflect A1c interference, recent glycemic change, or calibration issues.",
                ref(
                    "Using GMI",
                    "If GMI is lower than hemoglobin A1c considers Avoiding hypoglycemia",
                ),
            ),
            note(
                f"{p}-n4",
                "Sensor selection",
                "How to choose a CGM when hypoglycemia unawareness is present",
                "Avoid the original Libre without alerts; DexCom, Guardian 3, and Eversense all work, with DexCom favored when calibration error is a concern. For pump/closed-loop goals, match sensor to pump partner (Guardian 3 for Medtronic, DexCom for Tandem).",
                ref(
                    "Choosing a Sensor",
                    "Not Libre (no alerts), but consider Libre 2, which does have alarms",
                ),
            ),
            note(
                f"{p}-n5",
                "DexCom G6",
                "DexCom G6: factory calibration and alert capabilities",
                "G6 is factory calibrated with MARD <10%, 10-day wear, high/low and predictive alerts, and no routine need for fingerstick confirmation—though compression artifact and site rotation remain practical limits.",
                ref(
                    "DexCom",
                    "No need for fingerstick confirmation",
                ),
            ),
            note(
                f"{p}-n6",
                "Closed-loop evolution",
                "How closed-loop systems have progressed over two decades",
                "Systems evolved from threshold suspend (pump off at low glucose), to predictive low-glucose suspend, to hybrid closed-loop where the algorithm corrects toward target while the patient still delivers meal boluses.",
                ref(
                    "Sensor-Pump Interactions: Toward \"Closing the Loop\"",
                    "Hybrid closed-loop systems: the algorithm corrects the glucose toward a target/target range; the patient still determines meal boluses",
                ),
            ),
            note(
                f"{p}-n7",
                "Meal bolus timing",
                "How late meal boluses cause postprandial variability on downloads",
                "When glucose rises before the bolus is delivered, early postprandial insulin is inadequate and later periods have relative insulin excess—producing late hypoglycemia even on hybrid closed-loop systems.",
                ref(
                    "Case 2",
                    "the blood glucose levels start to rise BEFORE the meal bolus delivery.",
                ),
            ),
            note(
                f"{p}-n8",
                "Correction stacking",
                "Why manual correction boluses on closed-loop cause hypoglycemia",
                "When the closed-loop system is already lowering glucose, patient-initiated correction boluses stack insulin and provoke hypoglycemia at variable times—exercise-induced lows are less likely when lows follow glucose spikes.",
                ref(
                    "Case 3",
                    "she is in effect inadvertently \"stacking\" insulin and overcorrecting (Answer A).",
                ),
            ),
            note(
                f"{p}-n9",
                "Pregnancy targets",
                "Pregnancy CGM glucose targets on pump/sensor downloads",
                "Pregnancy targets for time in range are 63 to 140 mg/dL (3.5–7.8 mmol/L)—looser than nonpregnant targets in older patients but tighter overnight control may still require insulin timing adjustments.",
                ref(
                    "Usual Target Recommendations",
                    "Pregnancy targets for time in range are 63 to 140 mg/dL (3.5-7.8 mmol/L).",
                ),
            ),
            note(
                f"{p}-n10",
                "Compression lows",
                "Pitfall: nocturnal false lows from compression artifact",
                "DexCom and other sensors can report \"compression lows\" when the sensor is compressed during sleep; unconfirmed lows with discordant fingersticks should prompt site/position counseling—not forced recalibration of factory-calibrated systems.",
                ref(
                    "DexCom",
                    "\"Compression lows\"",
                ),
            ),
            note(
                f"{p}-n11",
                "Eversense indications",
                "When to consider implantable Eversense CGM",
                "Eversense suits body-image or athletic concerns, adherence problems, needle phobia, or running out of infusion/sensor sites—but it lacks a current US pump partner for threshold suspend or hybrid closed loop.",
                ref(
                    "So When Eversense?",
                    "Body image issues/athletics",
                ),
            ),
            note(
                f"{p}-n12",
                "Clinic workflow",
                "How to handle pump/CGM downloads during a busy visit",
                "Efficient interpretation requires pre-visit upload, focus on time in range, GMI, auto-mode utilization, bolus timing relative to meals, and correction-bolus patterns—technology choice must align with insurance, alerts, and pump integration needs.",
                ref(
                    "Barriers to Optimal Practice",
                    "Logistics of office download and interpretation of data from pump/CGM and closed-loop systems.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — pregnancy",
                "A 35-year-old pregnant woman with type 2 diabetes on bedtime NPH has elevated postlunch glucose on Libre download; overnight values are low-normal. Time in range is 88%. What is the best next step?",
                [
                    "Continue the regimen; time in range is 88%",
                    "Reduce NPH because time below range is 9%",
                    "Move NPH insulin to the morning",
                    "Re-introduce metformin",
                ],
                2,
                "Pregnancy target is 63–140 mg/dL; postlunch hyperglycemia with acceptable overnight values favors morning NPH to cover daytime meals rather than reducing bedtime NPH or adding metformin.",
                ref(
                    "Case 1",
                    "Answer: C) Move her NPH insulin to the morning",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — late boluses",
                "A 46-year-old man on a 670G hybrid closed-loop has A1c 8.1% with wide variability. Pump download shows glucose rising before meal bolus delivery. Most likely explanation?",
                [
                    "Inaccurate carbohydrate counting",
                    "High-fat meals",
                    "Inappropriate insulin-to-carbohydrate ratio",
                    "Late meal boluses",
                ],
                3,
                "Rising glucose before bolus delivery causes early under-insulinization and later relative excess—classic late bolus pattern on CGM/pump overlay.",
                ref(
                    "Case 2",
                    "Answer: D) Late meal boluses",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3 — correction stacking",
                "A 51-year-old woman on 670G auto-mode has postprandial spikes followed by hypoglycemia at variable times. She takes manual correction boluses when high. Most likely cause of lows?",
                [
                    "Overcorrecting her blood glucose",
                    "Sensor error",
                    "Premeal exercise",
                    "Incorrect insulin-to-carbohydrate ratio",
                ],
                0,
                "Hypoglycemia follows spikes and coincides with manual corrections while auto-mode is already delivering insulin—stacking effect.",
                ref(
                    "Case 3",
                    "Answer: A) Overcorrecting her blood glucose",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 4 — nocturnal false lows",
                "A 60-year-old man with LADA on DexCom G6 has recurrent ~3 AM sensor lows unconfirmed by fingerstick; recalibrating with fingersticks worsened accuracy. Best management?",
                [
                    "Increase overnight basal insulin",
                    "Counsel on compression artifact and avoid unnecessary G6 recalibration",
                    "Switch to Guardian 3 requiring daily calibration",
                    "Disable all low alerts permanently",
                ],
                1,
                "Factory-calibrated G6 lows discordant with fingersticks during sleep suggest compression lows; forced recalibration can worsen accuracy.",
                ref(
                    "Case 4",
                    "He used fingerstick blood glucose to recalibrate his sensor, with even worsening accuracy.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Sensor choice — type 2 without hypo unawareness",
                "Which CGM is often favored for a patient with type 2 diabetes and no hypoglycemia unawareness when cost and ease matter?",
                [
                    "Freestyle Libre",
                    "Eversense implantable sensor",
                    "Guardian 3 only",
                    "No CGM is appropriate in type 2 diabetes",
                ],
                0,
                "All four sensors can work; Libre may be easier, less costly, and at least as accurate as fingersticks with factory calibration.",
                ref(
                    "Choosing a Sensor",
                    "Libre may be easier, less costly, and at least as accurate as fingerstick measurements and is factory calibrated",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Pump-sensor pairing",
                "A patient desires Tandem Control-IQ hybrid closed-loop. Which sensor partner is appropriate?",
                [
                    "Guardian 3",
                    "DexCom",
                    "Eversense",
                    "Original Freestyle Libre without alerts",
                ],
                1,
                "Tandem pairs with DexCom; Medtronic systems use Guardian 3.",
                ref(
                    "Choosing a Sensor",
                    "If desire Tandem System (vide infra) is desired, then DexCom",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Time in range duration",
                "How many days of CGM data generally suffice to correlate with hemoglobin A1c?",
                [
                    "3 days",
                    "7 days",
                    "14 days",
                    "90 days",
                ],
                2,
                "Fourteen days of CGM correlate well with A1c for clinic interpretation.",
                ref(
                    "Regarding Time in Range",
                    "Fourteen days suffice to correlate well with hemoglobin A1c.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "GMI calculation",
                "Per the chapter GMI formula, a 25 mg/dL increase in mean CGM glucose changes GMI by approximately:",
                [
                    "0.1%",
                    "0.3%",
                    "0.6%",
                    "1.5%",
                ],
                2,
                "GMI (%) = 3.31 + 0.02392 × mean CGM glucose; each 25 mg/dL raises GMI ~0.6%.",
                ref(
                    "Glucose Management Indicator",
                    "Each change of 25 mg/dL results in a GMI increase of ~0.6%.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Threshold suspend",
                "What does a low-glucose threshold suspend system do?",
                [
                    "Automatically delivers meal boluses",
                    "Shuts off insulin delivery when glucose falls below a preset threshold",
                    "Replaces all basal insulin with glucagon",
                    "Eliminates need for patient meal boluses",
                ],
                1,
                "Threshold suspend stops the pump at a low glucose value—earliest step toward closed loop.",
                ref(
                    "Sensor-Pump Interactions: Toward \"Closing the Loop\"",
                    "Low-glucose (threshold) suspend systems: the pump shuts off if a low glucose value is used",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Hypoglycemia unawareness sensor",
                "A patient with severe hypoglycemia unawareness needs alerts. Which option is inappropriate as sole CGM?",
                [
                    "DexCom G6",
                    "Guardian 3",
                    "Original US Freestyle Libre without alarms",
                    "Libre 2 with optional alarms",
                ],
                2,
                "Original Libre lacks alerts; Libre 2 adds alarms. DexCom, Guardian, and Eversense provide alerts.",
                ref(
                    "Choosing a Sensor",
                    "Not Libre (no alerts), but consider Libre 2, which does have alarms",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Eversense and pumps",
                "Why is Eversense generally avoided when threshold suspend or hybrid closed loop is desired?",
                [
                    "It requires calibration every 24 hours",
                    "It has no current US pump partner",
                    "MARD exceeds 20%",
                    "It cannot provide vibratory alerts",
                ],
                1,
                "Eversense lacks a pump partner for automated insulin delivery systems in the US at the time of the chapter.",
                ref(
                    "Choosing a Sensor",
                    "Eversense does not have a \"pump partner\" at present, so would not use if threshold suspend or hybrid closed loop are desired",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Successful meal bolus prerequisites",
                "Before optimizing bolus type or timing, what must first be verified on pump download review?",
                [
                    "Basal rate(s) are correct",
                    "Patient uses only rapid-acting analog at all meals",
                    "Sensor is changed daily",
                    "A1c is below 6.0%",
                ],
                0,
                "Correct basal rates are foundational before adjusting bolus mode (regular, square-wave, combo).",
                ref(
                    "Successful Meal Bolus",
                    "Ensure the basal rate(s) is/are correct",
                ),
            ),
            mcq(
                f"{p}-q13",
                "DCCT legacy",
                "Intensive glycemic control in the DCCT reduced microvascular complications but also caused what important adverse effect?",
                [
                    "Tripling of severe hypoglycemia",
                    "Doubling of DKA admissions",
                    "Increased retinopathy incidence",
                    "Loss of counterregulatory hormone response only in type 2 diabetes",
                ],
                0,
                "DCCT intensive therapy tripled severe hypoglycemia—motivating safer intensification with pumps and RT-CGM.",
                ref(
                    "Significance of the Clinical Problem",
                    "intensive diabetes control resulted in a tripling of the occurrence of severe hypoglycemia.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Hybrid closed-loop",
                "On hybrid closed-loop systems the algorithm fully automates all meal boluses without patient input.",
                False,
                "Hybrid closed-loop corrects toward target but the patient still determines meal boluses.",
                ref(
                    "Sensor-Pump Interactions: Toward \"Closing the Loop\"",
                    "the patient still determines meal boluses",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Time in range",
                "A typical adult CGM target is time in range greater than 70%.",
                True,
                "Usual recommendation is TIR >70% with TBR <4% and TAR <25%.",
                ref(
                    "Usual Target Recommendations",
                    "Time in range >70%",
                ),
            ),
            tf(
                f"{p}-tf3",
                "DexCom G6 calibration",
                "DexCom G6 generally requires routine fingerstick calibration every 12 hours.",
                False,
                "G6 is factory calibrated and does not require routine fingerstick confirmation.",
                ref(
                    "DexCom",
                    "No need for fingerstick confirmation",
                ),
            ),
            tf(
                f"{p}-tf4",
                "GMI",
                "Glucose management indicator (GMI) estimates hemoglobin A1c from mean CGM glucose.",
                True,
                "GMI replaces the older eA1c terminology to estimate A1c from CGM mean glucose.",
                ref(
                    "Glucose Management Indicator",
                    "GMI is a new term for estimating hemoglobin A1c from CGM readings",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Libre alerts",
                "The older US Freestyle Libre version lacked alerts, unlike Libre 2.",
                True,
                "Original Libre required active scanning and lacked alerts; Libre 2 adds optional alarms.",
                ref(
                    "Freestyle Libre: Flash Technology",
                    "Older US version does not have alerts; Libre 2 has optional alarms",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Eversense wear",
                "Eversense sensor life is approximately 3 months in the United States.",
                True,
                "Implanted sensor lasts 3 months in the US and 6 months in the EU per chapter.",
                ref(
                    "Eversense (Senseonics)",
                    "Sensor life = 3 months United States; 6 months European Union",
                ),
            ),
            tf(
                f"{p}-tf7",
                "TIR vs A1c",
                "Time in range responds faster to therapeutic interventions than hemoglobin A1c.",
                True,
                "TIR reflects recent glycemia and variability more rapidly than A1c.",
                ref(
                    "Advantages of Time in Range",
                    "It responds faster to interventions than does hemoglobin A1c",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Medicare coverage",
                "At the time of writing, Medicare covered only Freestyle Libre and Dexcom among CGM systems.",
                True,
                "Insurance coverage strongly influences sensor choice; Medicare coverage was limited to Libre and Dexcom.",
                ref(
                    "Selecting a Pump",
                    "Medicare is only \"covering\" Freestyle Libre and Dexcom.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Late boluses",
                "Assertion: Late meal boluses can cause late postprandial hypoglycemia on hybrid closed-loop therapy.",
                "Reason: Glucose begins rising before insulin is delivered, leaving early hyperglycemia and later relative insulin excess.",
                0,
                "Both are true and mechanistically linked on pump/CGM downloads.",
                ref(
                    "Case 2",
                    "there is inadequate insulin early after meals and excess insulin in the later postprandial period, resulting in late hypoglycemia.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Correction stacking",
                "Assertion: Manual correction boluses during auto-mode can provoke hypoglycemia.",
                "Reason: The closed-loop algorithm never delivers insulin when glucose is elevated.",
                2,
                "Assertion is true; the algorithm does deliver insulin—stacking with patient corrections causes lows.",
                ref(
                    "Case 3",
                    "she is taking \"correction boluses\" at a time that the closed-loop system is already correcting her blood glucose.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "TIR and A1c",
                "Assertion: Fourteen days of CGM data correlate well with hemoglobin A1c.",
                "Reason: Time in range is unaffected by red-cell turnover that alters A1c.",
                0,
                "Both are true; TIR avoids some A1c confounders while correlating over ~14 days.",
                ref(
                    "Regarding Time in Range",
                    "Fourteen days suffice to correlate well with hemoglobin A1c.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Sensor-pump matching",
                "Assertion: Sensor choice may dictate pump choice for closed-loop systems.",
                "Reason: All sensors interoperate with all pumps without restriction.",
                2,
                "Assertion is true; pump-sensor partnerships are proprietary—the reason is false.",
                ref(
                    "Selecting a Pump",
                    "If a sensor-augmented system or closed-loop system will be used, the sensor may dictate choice of pump",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Pregnancy insulin timing",
                "Assertion: Moving NPH from bedtime to morning may improve postlunch glucose in pregnancy.",
                "Reason: Bedtime NPH peaks during overnight hours when fasting targets are already acceptable.",
                0,
                "Both are true for the case vignette physiology.",
                ref(
                    "Case 1",
                    "Moving her NPH insulin to the morning (Answer C) is therefore the best next step.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Libre in hypo unawareness",
                "Assertion: Original Freestyle Libre without alerts is unsuitable for severe hypoglycemia unawareness.",
                "Reason: Libre sensors are inherently inaccurate compared with fingersticks.",
                1,
                "Both statements have support, but the lack of alerts—not accuracy—is the primary contraindication cited.",
                ref(
                    "Choosing a Sensor",
                    "Not Libre (no alerts), but consider Libre 2, which does have alarms",
                ),
            ),
            ar(
                f"{p}-ar7",
                "GMI discordance",
                "Assertion: When GMI exceeds hemoglobin A1c, intensifying hyperglycemia treatment should be considered.",
                "Reason: A higher GMI always proves laboratory A1c error.",
                2,
                "Assertion reflects chapter guidance; GMI above A1c suggests hyperglycemia but does not prove lab error alone.",
                ref(
                    "Using GMI",
                    "If GMI is higher than hemoglobin A1c consider: Addressing hyperglycemia",
                ),
            ),
            ar(
                f"{p}-ar8",
                "DCCT and technology",
                "Assertion: RT-CGM and pump advances aim to intensify control while reducing hypoglycemia.",
                "Reason: Intensive control in the DCCT carried no hypoglycemia penalty.",
                2,
                "Assertion is true; DCCT intensive therapy tripled severe hypoglycemia—the reason is false.",
                ref(
                    "Significance of the Clinical Problem",
                    "intensive diabetes control resulted in a tripling of the occurrence of severe hypoglycemia.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "17",
        "title": "How to Digest Data and Develop Treatment Recommendations During a Clinic Visit",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Steven D. Wittlin, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_17_How_to_Digest_Data_and_Develop_Treatment_Recommendations_During_a_Clinic_Visit.md",
        "items": items,
    }


def build_chapter_18() -> dict:
    p = "e21-18"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Diagnostic impact",
                "Why monogenic diabetes diagnosis changes management",
                "Accurate genetic diagnosis directs gene-specific therapy, identifies at-risk relatives, and prevents years of unnecessary insulin or inappropriate agents in misclassified type 1 or type 2 diabetes.",
                ref(
                    "Main Conclusions",
                    "accurate diagnosis through genetic testing directs treatment and management and identifies affected and at-risk family members.",
                ),
            ),
            note(
                f"{p}-n2",
                "Screening triggers",
                "How to identify patients who need monogenic diabetes testing",
                "Refer when pancreatic autoantibodies are negative and endogenous insulin persists >3 years after diagnosis; biomarkers and the MODY probability calculator refine pretest probability in young-onset diabetes.",
                ref(
                    "Main Conclusions",
                    "These include negative pancreatic autoantibodies and continued endogenous insulin production more than 3 years after diabetes diagnosis.",
                ),
            ),
            note(
                f"{p}-n3",
                "Misdiagnosis burden",
                "Burden of misdiagnosed MODY",
                "More than 80% of monogenic diabetes may be missed or mislabeled for years, driving unnecessary intensive insulin, adverse drug effects, and excess cost.",
                ref(
                    "Significance of the Clinical Problem",
                    "more than 80% of cases go undiagnosed or are misdiagnosed for many years.",
                ),
            ),
            note(
                f"{p}-n4",
                "K-ATP neonatal diabetes",
                "Sulfonylurea therapy for K-ATP channel neonatal diabetes",
                "Permanent neonatal diabetes from KCNJ11 or ABCC8 variants often responds to high-dose sulfonylureas with excellent glycemic control and improved neurologic outcomes versus insulin alone.",
                ref(
                    "Barriers to Optimal Practice",
                    "Permanent neonatal diabetes owing to pathogenic variants in KCNJ11 or ABCC8, the genes encoding the ATP-sensitive potassium channel in the β cell, respond to high-dosage sulfonylureas",
                ),
            ),
            note(
                f"{p}-n5",
                "GCK-MODY",
                "Why GCK-MODY usually needs no treatment outside pregnancy",
                "Glucokinase defects cause stable, regulated mild hyperglycemia from birth; discontinuing therapy does not alter A1c and long-term complication risk at this glycemic level is low.",
                ref(
                    "Barriers to Optimal Practice",
                    "GCK-MODY is characterized by stable mildly elevated blood glucose due to a glucose-sensing defect.",
                ),
            ),
            note(
                f"{p}-n6",
                "GCK-MODY pregnancy",
                "How to manage GCK-MODY during pregnancy without amniocentesis",
                "Fetal macrosomia risk depends on whether the fetus inherits the GCK variant; insulin is recommended only when fetal abdominal circumference rises disproportionately above the 75th percentile—amniocentesis solely for GCK genotyping is not advised.",
                ref(
                    "Case 1",
                    "Answer: C) Initiation of insulin therapy should be based on second-trimester fetal growth",
                ),
            ),
            note(
                f"{p}-n7",
                "HNF1A/HNF4A MODY",
                "Sulfonylurea sensitivity in HNF1A- and HNF4A-MODY",
                "These MODY subtypes show marked sulfonylurea sensitivity that bypasses the primary β-cell defect, often matching or beating insulin with lower treatment burden.",
                ref(
                    "Barriers to Optimal Practice",
                    "HNF1A-MODY and HNF4A-MODY exhibit a marked sensitivity to sulfonylureas, which bypass the major β-cell defect.",
                ),
            ),
            note(
                f"{p}-n8",
                "HNF1B-MODY",
                "Extra-pancreatic features of HNF1B-MODY",
                "HNF1B variants cause developmental renal disease, pancreatic hypoplasia, genital tract anomalies, hypomagnesemia, and hyperuricemia—accurate diagnosis enables surveillance beyond glycemia.",
                ref(
                    "Barriers to Optimal Practice",
                    "Heterozygous HNF1B pathogenic variants are the most common cause of developmental renal disease",
                ),
            ),
            note(
                f"{p}-n9",
                "Sulfonylurea transition",
                "How to transition insulin-treated MODY to low-dose sulfonylurea",
                "Confirm C-peptide/endogenous insulin; young normal-weight patients on subreplacement insulin can often stop insulin and start half the lowest glyburide tablet, titrating carefully—long duration or full replacement doses require gradual basal reduction.",
                ref(
                    "Case 2",
                    "Answer: D) Stop all insulin and start glyburide 1/2 of the 1.25 mg tablet daily",
                ),
            ),
            note(
                f"{p}-n10",
                "6q24 transient neonatal diabetes",
                "Relapsed transient neonatal diabetes and sulfonylureas",
                "Transient neonatal diabetes from 6q24 abnormalities often relapses in adolescence or early adulthood and can be treated with low-dose sulfonylureas.",
                ref(
                    "Barriers to Optimal Practice",
                    "Relapse of transient neonatal diabetes due to 6q24 abnormalities can be treated with low doses of sulfonylureas.",
                ),
            ),
            note(
                f"{p}-n11",
                "VUS pitfall",
                "Pitfall: variants of uncertain significance on genetic panels",
                "A VUS must not be treated as diagnostic MODY—expert consultation is advised when report interpretation is unclear.",
                ref(
                    "Barriers to Optimal Practice",
                    "Interpretation of genetic testing reports can be confusing and lead to erroneous diagnosis of monogenic diabetes when a variant of uncertain significance is detected.",
                ),
            ),
            note(
                f"{p}-n12",
                "Cost-effectiveness",
                "Why targeted genetic testing is cost-effective",
                "Cost-effectiveness analyses support testing in appropriate young-onset cohorts, especially with biomarker pre-screening and family cascade testing.",
                ref(
                    "Significance of the Clinical Problem",
                    "Cost-effectiveness analyses suggest that genetic testing for monogenic diabetes in appropriate populations can be cost-saving.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — GCK-MODY pregnancy",
                "A 32-year-old woman with GCK-MODY plans pregnancy. Regarding insulin therapy, what should you advise?",
                [
                    "Start insulin early to prevent all macrosomia",
                    "Base insulin on second-trimester maternal glycemia only",
                    "Base insulin on second-trimester fetal growth on ultrasound",
                    "Obtain amniocentesis solely to determine fetal GCK genotype",
                ],
                2,
                "Insulin is guided by fetal growth pattern reflecting inherited GCK status; invasive testing solely for GCK genotype is not recommended.",
                ref(
                    "Case 1",
                    "Answer: C) Initiation of insulin therapy should be based on second-trimester fetal growth",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — HNF1A transition",
                "A 26-year-old man with genetically confirmed HNF1A-MODY has C-peptide, BMI 22.6, diabetes duration 6 years, and subreplacement insulin (glargine 8 U + 1–2 U aspart with meals). Best sulfonylurea transition plan?",
                [
                    "Continue all insulin and add glyburide 0.625 mg daily",
                    "Stop meal insulin only; start glyburide 0.625 mg daily",
                    "Stop basal only; start glyburide 0.625 mg daily",
                    "Stop all insulin; start glyburide 0.625 mg daily with close glucose monitoring",
                ],
                3,
                "Young, lean, short-duration MODY with documented endogenous insulin on subreplacement doses is ideal for direct transition to low-dose sulfonylurea.",
                ref(
                    "Case 2",
                    "Answer: D) Stop all insulin and start glyburide 1/2 of the 1.25 mg tablet daily",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Testing indications",
                "Which feature most strongly supports monogenic diabetes genetic testing?",
                [
                    "Positive GAD autoantibody at diagnosis",
                    "Negative autoantibodies with measurable C-peptide 5 years after diagnosis",
                    "Obesity with A1c 10% at age 55",
                    "Ketosis at presentation only",
                ],
                1,
                "Negative antibodies plus persistent endogenous insulin years after diagnosis are hallmark referral criteria.",
                ref(
                    "Main Conclusions",
                    "negative pancreatic autoantibodies and continued endogenous insulin production more than 3 years after diabetes diagnosis.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "GCK-MODY treatment",
                "Outside pregnancy, what is appropriate management of GCK-MODY?",
                [
                    "Start basal insulin for A1c >6.5%",
                    "No glucose-lowering therapy; monitor complications",
                    "Metformin 2000 mg daily mandatory",
                    "SGLT2 inhibitor for renal protection",
                ],
                1,
                "Stable mild hyperglycemia rarely warrants treatment outside pregnancy; complications are uncommon at this glycemic level.",
                ref(
                    "Barriers to Optimal Practice",
                    "treatment is not needed outside of pregnancy.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "HNF1B management",
                "A patient with HNF1B-MODY is most likely to require which non-glycemic surveillance?",
                [
                    "Annual thyroid ultrasound only",
                    "Renal imaging and monitoring of renal function",
                    "Quarterly cosyntropin stimulation tests",
                    "Routine muscle biopsy",
                ],
                1,
                "HNF1B causes developmental renal disease and extra-renal manifestations needing structured surveillance.",
                ref(
                    "Barriers to Optimal Practice",
                    "Heterozygous HNF1B pathogenic variants cause a spectrum of abnormalities that can be assessed for and managed once an accurate diagnosis is made.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Neonatal diabetes therapy",
                "Permanent neonatal diabetes due to KCNJ11 mutations is best treated with:",
                [
                    "High-dose sulfonylureas",
                    "Metformin monotherapy",
                    "GLP-1 receptor agonist",
                    "Immunosuppression",
                ],
                0,
                "K-ATP channel mutations respond to high-dose sulfonylureas with improved glycemia and neurologic outcomes.",
                ref(
                    "Barriers to Optimal Practice",
                    "respond to high-dosage sulfonylureas with excellent glycemic control and improvement in neurologic outcomes.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "MODY prevalence",
                "Approximately what fraction of young-onset diabetes is monogenic?",
                [
                    "0.2%",
                    "2%",
                    "20%",
                    "50%",
                ],
                1,
                "Monogenic diabetes accounts for roughly 2% of young-onset diabetes but is frequently misclassified.",
                ref(
                    "Significance of the Clinical Problem",
                    "accounts for approximately 2% of young-onset diabetes.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Sulfonylurea dosing in MODY",
                "When starting sulfonylurea in HNF1A-MODY, what dosing approach is advised?",
                [
                    "Full standard type 2 diabetes dose immediately",
                    "Half of the lowest available tablet with gradual titration",
                    "Only long-acting glipizide once weekly",
                    "Combine with DPP-4 inhibitor first line",
                ],
                1,
                "Marked sensitivity warrants starting at half the lowest dose (e.g., half of 1.25 mg glyburide) and titrating.",
                ref(
                    "Case 2",
                    "starting with one-half tablet of the lowest dose and titrating up to achieve adequate glycemic control is advised.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "GCK pregnancy insulin risk",
                "Why is insulin during GCK-MODY pregnancy potentially harmful?",
                [
                    "It always causes DKA",
                    "Mothers may experience hypoglycemia including severe hypoglycemia",
                    "It permanently suppresses fetal insulin secretion",
                    "It is contraindicated in all pregnancies regardless of fetal genotype",
                ],
                1,
                "Insulin when the fetus inherits GCK may cause maternal hypoglycemia and theoretical growth restriction in affected fetuses.",
                ref(
                    "Case 1",
                    "Women with GCK-MODY may experience hypoglycemia, including severe hypoglycemia, when treated with insulin during pregnancy.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "6q24 relapse",
                "Transient neonatal diabetes due to 6q24 abnormalities that relapses in adolescence is often treated with:",
                [
                    "High-dose insulin only",
                    "Low-dose sulfonylureas",
                    "Thiazolidinediones",
                    "Immunotherapy",
                ],
                1,
                "Relapsed 6q24-related diabetes responds to low-dose sulfonylureas.",
                ref(
                    "Barriers to Optimal Practice",
                    "Relapse of transient neonatal diabetes due to 6q24 abnormalities can be treated with low doses of sulfonylureas.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Population screening",
                "Universal genetic screening of all diabetes patients for MODY is:",
                [
                    "Recommended by all guidelines",
                    "Not economically feasible; testing should be targeted",
                    "Required before starting metformin",
                    "Only useful in neonates",
                ],
                1,
                "Testing must target high-risk phenotypes using biomarkers and clinical calculators.",
                ref(
                    "Barriers to Optimal Practice",
                    "population for MODY is not economically feasible. Thus, it is important to target genetic testing to high-risk populations",
                ),
            ),
            mcq(
                f"{p}-q12",
                "HNF1A misdiagnosis",
                "A lean young adult misdiagnosed with type 1 diabetes for 6 years but with persistent C-peptide most likely has:",
                [
                    "Latent autoimmune diabetes requiring more insulin",
                    "HNF1A-MODY or another monogenic form",
                    "Type 2 diabetes requiring metformin only",
                    "Steroid-induced diabetes",
                ],
                1,
                "Persistent endogenous insulin years after supposed type 1 diagnosis should prompt monogenic testing.",
                ref(
                    "Case 2",
                    "Monogenic diabetes was suspected due to his ability to miss basal insulin and continued C-peptide production.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Family cascade",
                "Proband diagnosis of MODY primarily helps relatives by:",
                [
                    "Eliminating need for any glucose monitoring",
                    "Enabling earlier correct classification and gene-directed therapy",
                    "Mandating prophylactic pancreatectomy",
                    "Proving they cannot develop type 2 diabetes",
                ],
                1,
                "Cascade testing allows timely correct treatment in affected relatives.",
                ref(
                    "Significance of the Clinical Problem",
                    "Proband diagnosis also aids in earlier diagnosis and correct classification of diabetes in family members.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "GCK-MODY pregnancy",
                "In GCK-MODY pregnancy, insulin is always required regardless of fetal genotype.",
                False,
                "Insulin is indicated only when the fetus is known or suspected not to carry the GCK variant based on growth.",
                ref(
                    "Barriers to Optimal Practice",
                    "Insulin therapy is recommended only when the fetus is known or suspected to not carry a GCK pathogenic variant",
                ),
            ),
            tf(
                f"{p}-tf2",
                "HNF1A sulfonylureas",
                "HNF1A-MODY often achieves equal or better control with sulfonylureas than with insulin.",
                True,
                "Multiple studies show sulfonylurea sensitivity in HNF1A-MODY.",
                ref(
                    "Barriers to Optimal Practice",
                    "A number of studies have demonstrated equal or improved control as compared with insulin therapy.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Misdiagnosis rate",
                "More than 80% of monogenic diabetes cases may be undiagnosed or misdiagnosed.",
                True,
                "Misclassification as type 1 or type 2 is common.",
                ref(
                    "Significance of the Clinical Problem",
                    "more than 80% of cases go undiagnosed or are misdiagnosed for many years.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "HNF1B therapy",
                "Most patients with HNF1B-MODY require insulin therapy.",
                True,
                "Unlike HNF1A/HNF4A, HNF1B usually needs insulin but benefits from extra-renal surveillance.",
                ref(
                    "Barriers to Optimal Practice",
                    "The majority of people with HNF1B-MODY require insulin therapy.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Amniocentesis for GCK",
                "Amniocentesis solely to determine fetal GCK genotype is routinely recommended.",
                False,
                "Invasive testing only for GCK genotype is not recommended due to pregnancy loss risk.",
                ref(
                    "Case 1",
                    "Amniocentesis or chorionic villus sampling for the sole purpose of assessing fetal genotype for a heterozygous GCK pathogenic variant (Answer D) is not recommended",
                ),
            ),
            tf(
                f"{p}-tf6",
                "GCK discontinuation",
                "Discontinuing therapy in GCK-MODY does not alter hemoglobin A1c.",
                True,
                "Stable regulated hyperglycemia persists without treatment effect on A1c.",
                ref(
                    "Barriers to Optimal Practice",
                    "discontinuation of therapy in GCK-MODY does not alter hemoglobin A1c.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "VUS diagnosis",
                "A variant of uncertain significance on a MODY panel confirms monogenic diabetes.",
                False,
                "VUS must not be overcalled; expert input is needed.",
                ref(
                    "Barriers to Optimal Practice",
                    "lead to erroneous diagnosis of monogenic diabetes when a variant of uncertain significance is detected.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "KCNJ11 therapy",
                "High-dose sulfonylureas can improve neurologic outcomes in K-ATP neonatal diabetes.",
                True,
                "Sulfonylureas treat both glycemia and neurologic features in KCNJ11/ABCC8 disease.",
                ref(
                    "Barriers to Optimal Practice",
                    "respond to high-dosage sulfonylureas with excellent glycemic control and improvement in neurologic outcomes.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "GCK pregnancy",
                "Assertion: Insulin in GCK-MODY pregnancy should be guided by fetal abdominal growth pattern.",
                "Reason: Fetal genotype determines whether maternal mild hyperglycemia is perceived as normal.",
                0,
                "Both are true and causally linked.",
                ref(
                    "Case 1",
                    "the risk of fetal macrosomia is based on whether the fetus inherits the heterozygous GCK pathogenic variant from the mother.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "HNF1A insulin transition",
                "Assertion: A young lean HNF1A-MODY patient on subreplacement insulin can often stop insulin when starting low-dose sulfonylurea.",
                "Reason: HNF1A-MODY patients never produce endogenous insulin.",
                2,
                "Assertion is true when C-peptide is present; the reason is false.",
                ref(
                    "Case 2",
                    "positive C-peptide indicates that the patient continues to make insulin.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Genetic testing",
                "Assertion: Targeted genetic testing in high-risk young-onset diabetes can be cost-saving.",
                "Reason: Universal screening of all people with diabetes is economically feasible.",
                2,
                "Assertion is supported; universal screening is not feasible—the reason is false.",
                ref(
                    "Significance of the Clinical Problem",
                    "Cost-effectiveness analyses suggest that genetic testing for monogenic diabetes in appropriate populations can be cost-saving.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "HNF1B surveillance",
                "Assertion: HNF1B-MODY diagnosis enables renal and extra-pancreatic surveillance.",
                "Reason: HNF1B variants affect only pancreatic beta cells.",
                2,
                "Assertion is true; HNF1B has multisystem effects—the reason is false.",
                ref(
                    "Barriers to Optimal Practice",
                    "Heterozygous HNF1B pathogenic variants cause a spectrum of abnormalities that can be assessed for and managed",
                ),
            ),
            ar(
                f"{p}-ar5",
                "6q24 relapse",
                "Assertion: Relapsed transient neonatal diabetes from 6q24 abnormalities may respond to low-dose sulfonylureas.",
                "Reason: All neonatal diabetes requires lifelong insulin regardless of genotype.",
                2,
                "Assertion is true; genotype-directed therapy contradicts the reason.",
                ref(
                    "Barriers to Optimal Practice",
                    "Relapse of transient neonatal diabetes due to 6q24 abnormalities can be treated with low doses of sulfonylureas.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Autoantibodies",
                "Assertion: Negative pancreatic autoantibodies support considering monogenic diabetes.",
                "Reason: All MODY patients have positive GAD antibodies.",
                2,
                "Assertion is a referral criterion; MODY is typically antibody negative—the reason is false.",
                ref(
                    "Main Conclusions",
                    "negative pancreatic autoantibodies and continued endogenous insulin production more than 3 years after diabetes diagnosis.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Sulfonylurea mechanism",
                "Assertion: Sulfonylureas are effective in HNF1A-MODY because they bypass the major β-cell defect.",
                "Reason: Sulfonylureas work only by increasing insulin sensitivity in muscle.",
                2,
                "Assertion is true; sulfonylureas stimulate insulin secretion—the reason is false.",
                ref(
                    "Barriers to Optimal Practice",
                    "HNF1A-MODY and HNF4A-MODY exhibit a marked sensitivity to sulfonylureas, which bypass the major β-cell defect.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "GCK complications",
                "Assertion: Long-term complications are rare at the glycemic levels seen in GCK-MODY.",
                "Reason: GCK-MODY causes rapidly progressive beta-cell failure requiring insulin within 2 years.",
                2,
                "Assertion is true; GCK-MODY is stable—the reason is false.",
                ref(
                    "Barriers to Optimal Practice",
                    "At this level of glycemic control, diabetes-related complications are rare.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "18",
        "title": "Practical Approaches to the Genetic Diagnosis and Management of Patients With Diabetes Mellitus",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Rochelle N. Naylor, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_18_Practical_Approaches_to_the_Genetic_Diagnosis_and_Management_of_Patients_With_Diabetes_Mellitus.md",
        "items": items,
    }


from build_endo_esap_17_20_ch19_20 import build_chapter_19, build_chapter_20  # noqa: E402

MODULES = {
    "endo2021_chapter_17_How_to_Digest_Data_and_Develop_Treatment_Recommendations_During_a_Clinic_Visit.json": build_chapter_17,
    "endo2021_chapter_18_Practical_Approaches_to_the_Genetic_Diagnosis_and_Management_of_Patients_With_Diabetes_Mellitus.json": build_chapter_18,
    "endo2021_chapter_19_Cardiovascular_Outcomes_in_Patients_With_Type_2_Diabetes_Mellitus_Treated_With_GLP1_Receptor_Agonists_and_SGLT2_Inhibitors.json": build_chapter_19,
    "endo2021_chapter_20_Pharmacologic_Approaches_to_the_Patient_With_Nonalcoholic_Fatty_Liver_Disease.json": build_chapter_20,
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
        print(f"Wrote {portal_path} ({len(data['items'])} items, {counts}, Why/How {wh}/{notes})")
        print(f"  Copied to {master_path}")


if __name__ == "__main__":
    main()

