#!/usr/bin/env python3
"""Generate Williams 15e module w15-36 — Digitized Approaches to Diabetes Diagnostics and Therapeutics."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-36"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-36_Digitized_Approaches_to_Diabetes_Diagnostics_and_Therapeutics.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why CGM is transformative for diabetes management",
                "CGM improves glycemia, reduces acute complications, and improves quality of life across diabetes types, therapy modalities, and disease stages.",
                ref(
                    "KEY POINTS",
                    "The use of continuous glucose monitoring (CGM) is transformative for diabetes management, improving glycemia, reducing acute complications, and improving quality of life.",
                ),
            ),
            note(
                f"{p}-n2",
                "The Limitations of SMBG Testing",
                "How CGM differs from fingerstick SMBG",
                "SMBG gives isolated snapshots; CGM collects minute-by-minute data for a complete day-and-night glucose profile including undetected excursions.",
                ref(
                    "The Limitations of SMBG Testing",
                    "Fingerprick SMBG tests provide isolated snapshots of glucose levels at any one moment of time, whereas CGM sensors collect information to give the user and health care professionals a complete view of glucose levels throughout the day, including through the night, covering periods of high or low glucose, and peaks and troughs when glucose is variable (see Fig. 36.2).",
                ),
            ),
            note(
                f"{p}-n3",
                "The Limitations of HbA $ _{1c} $",
                "Why identical HbA1c can mask different glycemic patterns",
                "HbA1c reflects 2–3-month averages but not day-to-day variability; identical HbA1c values can hide very different hypo/hyper patterns affecting treatment.",
                ref(
                    "The Limitations of HbA $ _{1c} $",
                    "For example, people with diabetes who have identical HbA $ _{1c} $ test results can have very different patterns of hyperglycemia and hypoglycemia, which will affect their treatment needs (Fig. 36.4).",
                ),
            ),
            note(
                f"{p}-n4",
                "Sensor Calibration and Accuracy",
                "How factory calibration changes CGM workflow",
                "Factory-calibrated sensors eliminate routine fingerstick calibrations; calibration requirements influence device choice and user engagement.",
                ref(
                    "Sensor Calibration and Accuracy",
                    "Most CGM sensors are factory calibrated, $ ^{10} $ which eliminates the need for users to calibrate them using SMBG fingerprick tests, or they may require daily calibrations using SMBG fingerprick tests.",
                ),
            ),
            note(
                f"{p}-n5",
                "Sensor Calibration and Accuracy",
                "Why MARD quantifies CGM accuracy",
                "Regulatory assessment compares CGM to reference blood glucose; MARD typically 8–14%, with nonadjunctive/AID-approved devices often below 10%.",
                ref(
                    "Sensor Calibration and Accuracy",
                    "Currently available CGM devices achieve MARD values in the range of 8% to 14%,  $ ^{10,11,14} $ which compares well with the wide accuracy range of SMBG test meters.",
                ),
            ),
            note(
                f"{p}-n6",
                "Understanding and Applying Continuous Glucose Monitoring Technologies in Diabetes",
                "How isCGM differs from real-time CGM",
                "Intermittently scanned CGM transmits data only when the user actively scans the sensor with a reader or smartphone app.",
                ref(
                    "Understanding and Applying Continuous Glucose Monitoring Technologies in Diabetes",
                    "CGM devices that transmit glucose data only when the user actively scans their sensor with a reader or smartphone app are referred to as intermittently scanned CGM (isCGM).",
                ),
            ),
            note(
                f"{p}-n7",
                "Trend Arrows and Projected Glucose",
                "How CGM trend arrows guide corrective action",
                "Systems calculate direction and rate of change from prior 15 minutes of readings, displayed as trend arrows for timely insulin or carbohydrate decisions.",
                ref(
                    "Trend Arrows and Projected Glucose",
                    "CGM technology is able to collect glucose readings on a minute-by-minute basis, and each system is able to calculate both the direction and the rate of change of glucose based on the readings stored over the previous 15 minutes.",
                ),
            ),
            note(
                f"{p}-n8",
                "Time in Range in T1D and T2D",
                "Why TIR, TBR, and TAR replace averages alone",
                "International consensus defines TIR (70–180 mg/dL), TBR below 70 mg/dL, and TAR above 180 mg/dL as immediately actionable CGM metrics.",
                ref(
                    "Time in Range in T1D and T2D",
                    "Time in range (TIR) denotes the proportion of each day that a person with diabetes spends with CGM-measured glucose readings in each of three glucose ranges defined by international consensus.",
                ),
            ),
            note(
                f"{p}-n9",
                "Time in Range in T1D and T2D",
                "How consensus TIR and TBR targets apply to adults",
                "For most adults with T1D or T2D: >70% TIR (70–180 mg/dL), <4% TBR (<70 mg/dL), <1% below 54 mg/dL, and <25% TAR.",
                ref(
                    "Time in Range in T1D and T2D",
                    "Level 2 hypoglycemia, with a glucose level of below 54 mg/dL (3.0 mmol/L), with or without symptoms, is considered clinically significant in that it may trigger counterregulatory responses, cause cognitive impairment leading to severe hypoglycemia, and therefore requires immediate attention.",
                ),
            ),
            note(
                f"{p}-n10",
                "Time in Range in Elderly People With Diabetes and Those at High Risk of Hypoglycemia",
                "Why elderly/high-risk TIR targets are relaxed",
                "High-risk individuals still use 70–180 mg/dL range but aim for >50% TIR, <1% TBR, and <10% time above 250 mg/dL to prioritize hypoglycemia avoidance.",
                ref(
                    "Time in Range in Elderly People With Diabetes and Those at High Risk of Hypoglycemia",
                    "recommended target range for high-risk and elderly individuals is still 70 to 180 mg/dL (3.9–10.0 mmol/L), but the daily goal is for above 50% (>12 hours/day) TIR, rather than above 70% (16 hours, 48 min/day).",
                ),
            ),
            note(
                f"{p}-n11",
                "Time in Range During Pregnancy",
                "How pregnancy CGM targets differ from nonpregnant adults",
                "Pregnant women with pregestational diabetes should spend >70% of time between 63 and 140 mg/dL, with <4% below 63 mg/dL and <1% below 54 mg/dL.",
                ref(
                    "Time in Range During Pregnancy",
                    "International consensus guidelines propose that pregnant women with pregestational diabetes or gestational diabetes spend greater than 70% of the time with glucose between 63 and 140 mg/dL (3.5–7.8 mmol/L).",
                ),
            ),
            note(
                f"{p}-n12",
                "Ambulatory Glucose Profile—A Graphical Tool for Reviewing CGM Data",
                "How the AGP summarizes dense CGM data",
                "The AGP is the accepted standard for visualizing CGM—modal-day median, IQR, and 5th–95th percentile bands support shared therapeutic decisions.",
                ref(
                    "Ambulatory Glucose Profile—A Graphical Tool for Reviewing CGM Data",
                    "An accepted standard method for summarizing and visualizing the dense CGM data is the ambulatory glucose profile (AGP).",
                ),
            ),
            note(
                f"{p}-n13",
                "Using the Ambulatory Glucose Profile Report in a Systematic Way",
                "How to review AGP in five systematic steps",
                "Start with data capture ≥70% over 14 days, then prioritize TBR, TAR, variability (CV ≤36%), and GMI versus HbA1c before intensifying therapy.",
                ref(
                    "Using the Ambulatory Glucose Profile Report in a Systematic Way",
                    "Confirm that the patient has captured >70% of data over 14 consecutive days of sensor wear time.",
                ),
            ),
            note(
                f"{p}-n14",
                "Using CGM Improves Measures of Glycemia Compared to SMBG",
                "Why CGM improves outcomes beyond HbA1c alone",
                "RCTs show CGM lowers HbA1c, increases TIR, reduces hypo/hyperglycemia, lowers variability, improves QoL, and cuts hospital admissions for DKA and severe hypoglycemia.",
                ref(
                    "Using CGM Improves Measures of Glycemia Compared to SMBG",
                    "RCTs and prospective real-world studies confirm that use of CGM devices is associated with lowered HbA $ _{1c} $ in children and adults with T1D on either MDI or on CSII, when compared with SMBG testing alone, $ ^{[134,135]} $ and in adults with T2D, treated either with insulin or a noninsulin therapy.",
                ),
            ),
            note(
                f"{p}-n15",
                "Improvements in Glycemic Outcomes in Type 1 Diabetes",
                "How CGM benefits T1D on MDI or CSII",
                "Multiple RCTs show up to 0.6% HbA1c reduction with CGM versus SMBG; COMISAIR found CGM impact exceeds insulin delivery mode over 3 years.",
                ref(
                    "Improvements in Glycemic Outcomes in Type 1 Diabetes",
                    "A series of RCTs and prospective observational studies have given unequivocal support for the use of CGM in T1D.",
                ),
            ),
            note(
                f"{p}-n16",
                "CGM Is Effective in Daily Management of T2D on Insulin Regimens",
                "How CGM helps insulin-treated T2D",
                "DIAMOND, isCGM, and basal-insulin trials show HbA1c reductions, more TIR, and 43–64% less hypoglycemia versus SMBG alone.",
                ref(
                    "CGM Is Effective in Daily Management of T2D on Insulin Regimens",
                    "People with T2D on intensive insulin therapy benefit from using CGM devices in the same way shown for people with T1D.",
                ),
            ),
            note(
                f"{p}-n17",
                "Use of CGM in People With T2D Not on Insulin Therapy",
                "Why CGM may help T2D without insulin",
                "Randomized and real-world data show HbA1c and glycemic variability improvements in noninsulin T2D, with greater benefit when baseline control is poor.",
                ref(
                    "Use of CGM in People With T2D Not on Insulin Therapy",
                    "Evidence is accumulating that people with T2D not on insulin therapy can have clinically significant reductions in their HbA $ _{1c} $ by using CGM devices.",
                ),
            ),
            note(
                f"{p}-n18",
                "Telemonitoring and Telemedicine Are Essential Attributes of CGM Technology",
                "How CGM enables telemedicine and remote triage",
                "CGM supports remote AGP/TIR review, COVID-era glycemic stability, and stratified care prioritizing those with hypo, hyper, or high variability.",
                ref(
                    "Telemonitoring and Telemedicine Are Essential Attributes of CGM Technology",
                    "An accepted benefit of using CGM technology is the opportunity it creates for remote consultations for people with diabetes, with shared information on glycemia available for the CGM user and their health care professional to review together, while at different physical locations.",
                ),
            ),
            note(
                f"{p}-n19",
                "Connected Insulin Pens",
                "How smart pens support MDI with CGM",
                "Connected pens record doses, reduce stacking, and paired with CGM increase TIR ~2 hours/day by reducing omitted boluses.",
                ref(
                    "Connected Insulin Pens",
                    "Evidence from an observational study suggests smart pens increase TIR by approximately 2 hours per day in adults when paired with a CGM, with a reduction both in hyperglycemia (above 180 mg/dL, 10.0 mmol/L) and hypoglycemia (below 70 mg/dL, 39 mmol/L).",
                ),
            ),
            note(
                f"{p}-n20",
                "Insulin Pump Therapy Improves Measures of Glycemia and Quality of Life",
                "How CSII improves glycemia and reduces severe hypo",
                "Pump therapy lowers HbA1c and severe hypoglycemia/DKA in trials and registries; highest pre-pump HbA1c patients often gain most.",
                ref(
                    "Insulin Pump Therapy Improves Measures of Glycemia and Quality of Life",
                    "Over the years, an extensive evidence base has been developed showing use of pump therapy is associated with improvements in glycemia, decreased rates of hypoglycemia, and improvements in quality of life.",
                ),
            ),
            note(
                f"{p}-n21",
                "Sensor-Augmented Pump Therapy",
                "How SAP links sensor data to pump therapy",
                "SAP displays sensor glucose on pump/phone but requires user action; STAR-3 and JDRF data show benefit depends on consistent sensor wear (>60%).",
                ref(
                    "Sensor-Augmented Pump Therapy",
                    "With SAP therapy, sensor glucose data can be viewed either on a smartphone/dedicated reader or directly on an insulin pump; yet the onus for treatment decisions still falls to the person using the devices.",
                ),
            ),
            note(
                f"{p}-n22",
                "Automated Insulin Delivery",
                "How hybrid closed-loop AID systems work",
                "AID uses sensor, algorithm, and pump to suspend basal for hypo and increase delivery for hyperglycemia; prandial boluses remain user-initiated in hybrid systems.",
                ref(
                    "Automated Insulin Delivery",
                    "AID systems, also known as closed loop (CL) or artificial pancreas (AP) systems, not only suspend insulin delivery to mitigate hypoglycemia but also are able to ramp up insulin delivery to lessen time spent in hyperglycemia (see Fig. 36.10C).",
                ),
            ),
            note(
                f"{p}-n23",
                "Special Situations With AID Use",
                "How to manage sick days on AID",
                "Check ketones, change infusion set, exit automation during ketosis to give correction bolus and elevated temp basal, resume only after insulin duration elapses.",
                ref(
                    "Special Situations With AID Use",
                    "Sick-day management for those on AID systems should consist of regularly checking for ketones and changing the infusion set as one would for any insulin infusion pump.",
                ),
            ),
            note(
                f"{p}-n24",
                "Diabetes Technology for Noncritical Hospitalized Patients With and Without Preexisting Diabetes",
                "How inpatient CGM is used with confirmatory POC glucose",
                "RT-CGM is recommended for noncritically ill insulin-treated inpatients with confirmatory bedside POC tests; pumps/CGM may continue if patient can self-manage and staff are expert.",
                ref(
                    "Diabetes Technology for Noncritical Hospitalized Patients With and Without Preexisting Diabetes",
                    "In adults with insulin-treated diabetes hospitalized for noncritical illness, the use of real-time CGM is recommended, although with confirmatory bedside point-of-care (POC) blood glucose tests, for adjustments in insulin over POC testing alone.",
                ),
            ),
            note(
                f"{p}-n25",
                "Decision-Support Systems for Visualizing CGM Data and Beyond",
                "How AI decision-support advisers assist dosing",
                "Cloud/smart-app algorithms integrate CGM, pens, SMBG, and pump data for dose titration; one RCT showed noninferiority to physician-guided adjustments.",
                ref(
                    "Decision-Support Systems for Visualizing CGM Data and Beyond",
                    "An emerging field in diabetes care involves decision-support systems that are able to use data from connected care devices including CGM, smart insulin pens, SMBG, and insulin pumps to generate meaningful guidance and advice to people with diabetes via smart apps or cloud-based algorithms.",
                ),
            ),
            note(
                f"{p}-n26",
                "Tackling Exercise",
                "How AID helps exercise-related glycemia",
                "Exercise modes raise target glucose in advance; meta-analysis shows AID improves TIR during exercise versus conventional pump therapy.",
                ref(
                    "Tackling Exercise",
                    "A recent meta-analysis found that AID systems used during exercise improved TIR compared to conventional pump therapy.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Understanding and Applying Continuous Glucose Monitoring Technologies in Diabetes",
                "A patient asks why CGM is preferred over eight daily fingersticks. Which explanation is most accurate?",
                [
                    "CGM provides continuous profiles including nocturnal excursions missed by sparse SMBG",
                    "SMBG always captures more hypoglycemia than CGM",
                    "CGM measures capillary blood glucose directly",
                    "Fingerstick testing is more accurate than all CGM devices",
                ],
                0,
                "CGM minute-by-minute interstitial readings reveal peaks/troughs that sparse SMBG cannot fully capture.",
                ref(
                    "Understanding and Applying Continuous Glucose Monitoring Technologies in Diabetes",
                    "Even when performed multiple times daily, for example, a 7-point profile before and after meals and once at night, a full understanding of glycemic profiles can never be entirely captured by this sparse sampling approach (Fig. 36.2).",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Sensor Calibration and Accuracy",
                "When counseling on sensor types, which statement about transcutaneous versus implantable CGM is correct?",
                [
                    "Transcutaneous sensors wear 7–14 days; implantable systems may last up to 180 days",
                    "Implantable sensors require scanning every 5 minutes",
                    "Transcutaneous sensors are placed only in the upper arm permanently",
                    "All sensors require twice-daily fingerstick calibration",
                ],
                0,
                "Transcutaneous wear 7–14 days; implantable Eversense transmits up to 180 days before replacement.",
                ref(
                    "Understanding and Applying Continuous Glucose Monitoring Technologies in Diabetes",
                    "Transcutaneous CGM sensors have wear times from 7 to 14 days, during which they are active and after which a new sensor is applied. Implantable systems currently transmit glucose data for up to 180 days before replacement.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Sensor Calibration and Accuracy",
                "A clinician compares CGM systems for nonadjunctive insulin dosing. Which accuracy metric is standard?",
                [
                    "Mean absolute relative difference (MARD) versus reference blood glucose",
                    "Urine ketone concordance with sensor glucose",
                    "Fructosamine correlation only",
                    "Peak postprandial capillary glucose alone",
                ],
                0,
                "MARD compares simultaneous CGM and reference blood glucose; current devices achieve ~8–14% MARD.",
                ref(
                    "Sensor Calibration and Accuracy",
                    "Sensor accuracy is quantified by metrics that focus on the mean absolute relative difference (MARD) between a CGM measurement and the corresponding simultaneous value obtained by the reference system.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Making Daily Decisions Using CGM Technology",
                "A Dexcom user sees a rapidly falling trend arrow before a meal bolus. Best counseling principle?",
                [
                    "Adjust dosing using device-specific trend arrow rates; no universal standard exists",
                    "Ignore trend arrows; use current glucose value only",
                    "All CGM systems use identical arrow thresholds",
                    "Trend arrows replace all meal bolus calculations",
                ],
                0,
                "Trend arrow orientations and rates differ by manufacturer; insulin dosing recommendations must be device-specific.",
                ref(
                    "Making Insulin Dosing Decisions Incorporating Glucose Trend Arrows",
                    "There is no standardization between different CGM devices regarding trend arrow orientations and rate of change; thus, recommendations for insulin dosing must be adjusted to accommodate the distinctions of different CGM devices.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Time in Range in T1D and T2D",
                "Per international consensus, appropriate adult T1D/T2D targets include:",
                [
                    ">70% time 70–180 mg/dL and <4% time below 70 mg/dL",
                    ">90% time below 70 mg/dL",
                    "No TBR target when HbA1c is normal",
                    ">50% time above 250 mg/dL",
                ],
                0,
                "Consensus targets: >70% TIR, <4% TBR (<1% <54 mg/dL), <25% TAR with tighter limits for level 2 hyperglycemia.",
                ref(
                    "Time in Range in T1D and T2D",
                    "Each of these CGM-defined episodes of low glucose is considered clinically relevant if it lasts 15 minutes or more before returning above 70 mg/dL (3.9 mmol/L).",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Understanding Glycemic Variability Using CGM Data",
                "A patient has high glucose variability on AGP. Recommended CV target in T1D?",
                [
                    "Coefficient of variation ≤36%",
                    "CV must exceed 50% for safety",
                    "Variability is irrelevant if HbA1c is at goal",
                    "CV target is identical to HbA1c percentage",
                ],
                0,
                "Percent CV correlates with TBR; consensus recommends ≤36% in T1D because hypoglycemia risk rises above this.",
                ref(
                    "Understanding Glycemic Variability Using CGM Data",
                    "Percent CV is a measure of glucose variability that is strongly correlated with TBR, $ ^{80} $ and the target for the coefficient of variation in T1D is recommended as  $ \\leq $36% $ ^{65} $ based on the increased risk of hypoglycemia above this level.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Time in Range in Elderly People With Diabetes and Those at High Risk of Hypoglycemia",
                "An 82-year-old on insulin with hypoglycemia unawareness starts CGM. Most appropriate TBR goal?",
                [
                    "<1% time below 70 mg/dL (<15 min/day)",
                    "<25% time below 70 mg/dL",
                    "No hypoglycemia monitoring needed in elderly",
                    "Maintain <4% TBR identical to all adults regardless of risk",
                ],
                0,
                "High-risk/elderly: >50% TIR but stricter <1% TBR and focus on limiting time >250 mg/dL.",
                ref(
                    "Time in Range in Elderly People With Diabetes and Those at High Risk of Hypoglycemia",
                    "Because of the need to manage the risk of hypoglycemia more closely in this group, the recommendation is to keep %TBR (below 70 mg/dL, 3.9 mmol/L) below 1% or less than 15 minutes per day.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Time in Range During Pregnancy",
                "A woman with T1D at 10 weeks gestation uses CGM. Evidence-based pregnancy TIR target?",
                [
                    ">70% time 63–140 mg/dL with <4% below 63 mg/dL",
                    ">70% time 70–180 mg/dL identical to nonpregnant adults only",
                    "No CGM targets exist for pregnancy",
                    "TIR goals apply only in third trimester",
                ],
                0,
                "Pregnancy consensus: 63–140 mg/dL range, >70% TIRp, <4% below 63 mg/dL, <1% below 54 mg/dL; early optimization affects neonatal outcomes.",
                ref(
                    "Time in Range During Pregnancy",
                    "International consensus recommends a target glucose range of 63 to 140 mg/dL (3.5–7.8 mmol/L) for women with T1D during pregnancy and a %TIRp of over 70% (16 hours, 48 min/day; see Table 36.3 and Fig. 36.8).",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Ambulatory Glucose Profile—A Graphical Tool for Reviewing CGM Data",
                "Minimum CGM data needed for a representative AGP report?",
                [
                    "14 consecutive days with ≥70% data capture",
                    "Single 24-hour sensor wear",
                    "90 days mandatory before any AGP",
                    "One week of intermittent scanning only",
                ],
                0,
                "14 days at ≥70% capture satisfactorily represents patterns visible with up to 90 days of data.",
                ref(
                    "Ambulatory Glucose Profile—A Graphical Tool for Reviewing CGM Data",
                    "Fourteen consecutive days of CGM sensor use, with ≥70% data capture, is sufficient to generate an AGP report that will satisfactorily represent the patterns and trends that will be visible with up to 90 days of glucose data $ ^{124,125} $",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Using the Ambulatory Glucose Profile Report in a Systematic Way",
                "AGP shows GMI 7.2% but recent HbA1c 8.1%. Treatment intensification should be guided by:",
                [
                    "GMI only because the patient is a high glycator at hypoglycemia risk if HbA1c alone drives therapy",
                    "HbA1c only regardless of GMI",
                    "Neither metric; discontinue CGM",
                    "Average of GMI and HbA1c without clinical context",
                ],
                0,
                "When GMI is lower than HbA1c, intensifying from HbA1c alone risks hypoglycemia; use GMI for treatment decisions.",
                ref(
                    "Using the Ambulatory Glucose Profile Report in a Systematic Way",
                    "However, if GMI is noticeably lower than a recent HbA $ _{1c} $, the person is considered a “high glycator,” $ ^{130} $ and treatment intensification should be managed using the GMI value.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Improvements in Glycemic Outcomes in Type 1 Diabetes",
                "In COMISAIR, 3-year follow-up showed CGM benefit versus SMBG was:",
                [
                    "Greater than the impact of MDI versus CSII delivery mode",
                    "Absent unless on insulin pump only",
                    "Limited to children under age 10",
                    "Dependent on eliminating all meal boluses",
                ],
                0,
                "0.9% HbA1c reduction with CGM on MDI or CSII exceeded differences from insulin delivery method.",
                ref(
                    "Improvements in Glycemic Outcomes in Type 1 Diabetes",
                    "In both the MDI and CSII study groups, a 0.9% reduction in HbA $ _{1c} $ was evident compared to the SMBG group, indicating that the benefits of CGM are more impactful than the mode of insulin delivery in T1D.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "CGM Is Effective in Daily Management of T2D on Insulin Regimens",
                "In the MOBILE trial of T2D on basal insulin, CGM versus SMBG over 8 months showed:",
                [
                    "0.4% HbA1c reduction with less hypo and hyperglycemia",
                    "No change in glycemia but improved QoL only",
                    "Increased hypoglycemia admissions",
                    "CGM contraindicated on basal insulin",
                ],
                0,
                "MOBILE (n=175): CGM lowered HbA1c 0.4% and reduced time >250 mg/dL and hypoglycemia events versus SMBG.",
                ref(
                    "CGM Is Effective in Daily Management of T2D on Insulin Regimens",
                    "For people with T2D on basal insulin therapy, CGM lowered  $ HbA_{1c} $ by 0.4% and reduced both time in hyperglycemia (over 250 mg/dL, 13.9 mmol/L) and hypoglycemia event rates over an 8-month period, compared to a control group using SMBG testing alone in the Type 2 Diabetes Basal Insulin Users: The Mobile Study (MOBILE) RCT of 175 adults.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Use of CGM in People With T2D Not on Insulin Therapy",
                "A 58-year-old with T2D on metformin alone has HbA1c 7.9%. Evidence for isCGM?",
                [
                    "12-week RCT showed 0.29% HbA1c reduction versus SMBG",
                    "CGM is proven harmful in all noninsulin T2D",
                    "CGM only approved for type 1 diabetes",
                    "No published trials exist in noninsulin T2D",
                ],
                0,
                "Wada et al. RCT (n=93): isCGM reduced HbA1c 0.29% and glycemic variability versus SMBG over 12 weeks.",
                ref(
                    "Use of CGM in People With T2D Not on Insulin Therapy",
                    "An HbA $ _{1c} $ reduction of 0.29% (3.2 mmol/mol) for the isCGM group compared to the SMBG cohort was observed following 12 weeks in a randomized trial in 93 people with T2D not taking insulin.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Telemonitoring and Telemedicine Are Essential Attributes of CGM Technology",
                "During COVID-19 clinic restrictions, CGM cohort data most often showed:",
                [
                    "Stable or improved glycemia with increased TIR in most groups",
                    "Universal HbA1c deterioration in all CGM users",
                    "Complete inability to use telemedicine with CGM",
                    "Mandatory discontinuation of all diabetes technology",
                ],
                0,
                "Review of 27 cohorts (69,294 CGM users): glycemia did not worsen in 25/27 and improved in 23/27; TIR rose in 19/27.",
                ref(
                    "Telemonitoring and Telemedicine Are Essential Attributes of CGM Technology",
                    "A review of 27 separate studies on glycemic control $ ^{167} $ for a combined population of 69,294 CGM users with T1D found that despite restricted access to diabetes clinics during the COVID-19 pandemic, glycemia did not deteriorate for 25 of the 27 cohorts and improved in 23 of the 27 study groups.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Connected Insulin Pens",
                "A patient on MDI frequently forgets lunch boluses. Which smart-pen feature is most relevant?",
                [
                    "Dose memory and bolus calculators reducing omitted boluses",
                    "Automatic closed-loop basal delivery without a pump",
                    "Replacement of all CGM requirements",
                    "Elimination of carbohydrate estimation forever",
                ],
                0,
                "Smart pens record timing/dose, limit stacking, and observational data link them to fewer missed boluses and ~2 h/day more TIR with CGM.",
                ref(
                    "Connected Insulin Pens",
                    "These results are likely due to fewer omitted boluses observed following introduction of smart pens.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Additional Considerations With Insulin Pump Therapy",
                "A pump user develops ketones after a dislodged infusion set. Essential counseling?",
                [
                    "Site failure can cause hyperglycemia and DKA if undetected—follow sick-day plan",
                    "Pump therapy eliminates all DKA risk",
                    "Ketones never occur with CSII",
                    "Basal rates cannot be modified on pumps",
                ],
                0,
                "Infusion site failure, occlusion, or pump malfunction can cause DKA; proactive sick-day access to supplies and support is critical.",
                ref(
                    "Additional Considerations With Insulin Pump Therapy",
                    "Thus, paramount to successful use of pump therapy is counseling individuals with diabetes about the risk of ketoacidosis that can occur due to partial occlusion of an infusion set, dislodgement at the site, or pump malfunction.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Sensor-Augmented Pump Therapy",
                "In the 2008 SAP versus pump/SMBG RCT, HbA1c benefit required:",
                [
                    "Sensor utilization greater than 60% of the time",
                    "Complete discontinuation of meal boluses",
                    "Use of SMBG only at bedtime",
                    "Sensor wear less than 10% of the time",
                ],
                0,
                "SAP reduced HbA1c versus pump+SMBG when sensors were used >60%; hypoglycemia exposure was higher in the control arm.",
                ref(
                    "Sensor-Augmented Pump Therapy",
                    "Notably, for those in the SAP group, sensor utilization greater than 60% of the time led to a reduction in HbA $ _{1c} $ levels.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Low Glucose Suspend",
                "In ASPIRE in-home study of low glucose suspend, key finding was:",
                [
                    "Reduced hypoglycemic sensor readings without HbA1c deterioration",
                    "Mandatory HbA1c rise of 2%",
                    "Increased severe hypoglycemia seizures",
                    "Complete elimination of all basal insulin forever",
                ],
                0,
                "ASPIRE showed fewer hypoglycemic sensor readings, stable HbA1c, and stable glucose 2 hours after nocturnal insulin interruption.",
                ref(
                    "Low Glucose Suspend",
                    "Importantly, this RCT also demonstrated no deterioration in glycemia as measured by  $ \\mathrm{HbA}_{1\\mathrm{c}} $, and that with nocturnal insulin interruption glucose levels were stable 2 hours after the suspension occurred.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Automated Insulin Delivery",
                "Across AID RCTs in diverse age groups, consistent findings include:",
                [
                    "Increased %TIR with reduced hyperglycemia and stable or lower hypoglycemia",
                    "Elimination of all prandial bolus requirements in hybrid systems",
                    "Universal 30% attrition making AID unusable",
                    "No HbA1c or mean glucose change",
                ],
                0,
                "International consensus: AID increases TIR 10–15% (~2–3.5 h/day), lowers mean glucose and hyperglycemia, with stable/reduced hypo.",
                ref(
                    "The Evidence to Support the Use of Automated Insulin Delivery Systems in Diabetes Care",
                    "In assessing the data from RCTs and single-arm studies a clear picture emerged that, from toddlers to the geriatric population, AID systems have uniformly demonstrated an increase in %TIR (70–180 mg/dL, 3.9–10.0 mmol/L) that occurs concomitant with a reduction in mean glucose, time in hyperglycemia, and HbA $ _{1c} $, with either no change or a reduction in time in hypoglycemia.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Special Situations With AID Use",
                "A patient on hybrid closed-loop develops ketosis during gastroenteritis. Best advice?",
                [
                    "Exit automation, give correction bolus and elevated temp basal, resume after insulin duration",
                    "Continue automation and withhold all insulin",
                    "Remove sensor and ignore ketones",
                    "Double all meal boluses automatically",
                ],
                0,
                "During ketosis, exit AID for manual correction and higher temp basal; resume automation only after insulin action window to avoid stacking.",
                ref(
                    "Special Situations With AID Use",
                    "By doing this, the individual can administer a correction dose of insulin and leverage temporary basal rates, which can be set to deliver more insulin (e.g., 200% basal rate, which is equivalent to +100% of usual basal rates) regardless of current glucose level.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Diabetes Technology for Noncritical Hospitalized Patients With and Without Preexisting Diabetes",
                "A hospitalized adult on insulin for infection asks to keep their pump. Per ADA/AACE guidance:",
                [
                    "Continue pump/CGM if patient can self-manage, has supplies, and staff have expertise",
                    "All pumps must be removed on admission regardless of circumstance",
                    "CGM alone replaces all bedside glucose checks without confirmation",
                    "Pump use is prohibited in all noncritical wards",
                ],
                0,
                "Maintain pump/CGM when feasible with knowledgeable staff; otherwise transition to basal-bolus MDI.",
                ref(
                    "Diabetes Technology for Noncritical Hospitalized Patients With and Without Preexisting Diabetes",
                    "For individuals with diabetes using an insulin pump, the ADA and the American Association of Clinical Endocrinologists (AACE) advocate for maintaining the insulin pump and/or CGM during the hospitalization, if the individual is physically and mentally able to continue its use, has the necessary supplies, and hospital personnel with expertise in diabetes technologies can assist with management.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Tackling Exercise",
                "An adolescent with T1D on AID plans soccer practice. Pre-exercise strategy?",
                [
                    "Activate exercise/raised target mode well before activity to reduce insulin on board",
                    "Suspend all insulin for 24 hours before exercise",
                    "Exercise only when ketones are large",
                    "AID systems cannot be used during any physical activity",
                ],
                0,
                "Most AID systems raise glucose targets to restrain insulin delivery; activity modes must be set in advance to mitigate hypo.",
                ref(
                    "Tackling Exercise",
                    "Most of the commercially available AID systems have methods to restrain insulin delivery by raising the target glucose levels.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Decision-Support Systems for Visualizing CGM Data and Beyond",
                "A youth-onset T1D clinic trials an AI insulin dose adviser. Regulatory precedent includes:",
                [
                    "RCT showing algorithm dose changes noninferior to physician-guided titration",
                    "No studies comparing algorithm to clinician care",
                    "Algorithms approved only for type 2 diabetes without insulin",
                    "Decision support prohibited in pediatric diabetes",
                ],
                0,
                "Nimri et al. Nat Med 2020: automated AI decision support noninferior to physician-guided dose alterations in youths with T1D.",
                ref(
                    "Decision-Support Systems for Visualizing CGM Data and Beyond",
                    "An RCT comparing the effectiveness of physician-guided dose alterations to those recommended by a decision-support tool showed noninferiority of the algorithm, leading to regulatory approval of the device.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "CGM Data Make It Possible to Understand and Manage Multiple Risk Factors in Diabetes",
                "CGM-driven management emphasizes avoiding which risks beyond average hyperglycemia?",
                [
                    "Hypoglycemia and glucose variability as independent risk factors",
                    "Only fasting glucose elevation",
                    "Weight gain exclusively",
                    "Ketosis only in type 2 diabetes",
                ],
                0,
                "Triangle of diabetes care: manage hyperglycemia, hypoglycemia, and variability—not HbA1c average alone.",
                ref(
                    "CGM Data Make It Possible to Understand and Manage Multiple Risk Factors in Diabetes",
                    "This CGM-driven approach to diabetes management has been termed the “triangle of diabetes care” (Fig. 36.5) and builds on the understanding that the frequency of hypoglycemia and degree of glucose variability are independent risk factors in diabetes.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "AID in Pregnancy",
                "Early data on AID in pregnant women with T1D showed:",
                [
                    "Increased overnight time in 63–140 mg/dL target versus SAP",
                    "Contraindication in all pregnancy trimesters",
                    "No change in glycemia compared to MDI alone",
                    "Mandatory doubling of severe hypoglycemia",
                ],
                0,
                "4-week crossover: AID increased tight pregnancy range overnight; extension maintained benefit up to 14 weeks.",
                ref(
                    "AID in Pregnancy",
                    "A short 4-week randomized crossover study showed AID increased the percentage of time spent in tight glycemic range of 63 to 140 mg/dL (3.5–7.8 mmol/L) by about 15%, achieving more than 70% of time in target when used overnight compared to SAP therapy.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Future Directions",
                "Regulatory evolution is expected to incorporate CGM metrics into drug labeling because:",
                [
                    "CGM-derived metrics are increasingly primary/secondary outcomes in diabetes trials",
                    "HbA1c will be abandoned entirely within one year",
                    "CGM is only used in research settings",
                    "FDA prohibits any CGM endpoints in trials",
                ],
                0,
                "CGM TIR and related metrics in pivotal trials will enable FDA/EMA labeling of medications with CGM outcomes.",
                ref(
                    "Future Directions",
                    "Importantly, CGM-derived metrics will be used as primary and secondary study outcomes in diabetes medication trials.",
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
                "All individuals with diabetes, regardless of type, therapy, or disease stage, benefit from CGM.",
                True,
                "Key points state universal CGM benefit across diabetes populations.",
                ref(
                    "KEY POINTS",
                    "All individuals with diabetes, regardless of the diabetes type, therapy modality, or stage of the disease, benefit from the use of CGM.",
                ),
            ),
            tf(
                f"{p}-t2",
                "KEY POINTS",
                "Advanced hybrid closed-loop AID systems currently represent the most successful insulin treatment modality.",
                True,
                "Key points rank AID as top insulin therapy for those treated with insulin.",
                ref(
                    "KEY POINTS",
                    "Advanced hybrid closed-loop systems for automated insulin delivery (AID) currently represent the most successful treatment modality for individuals treated with insulin.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Understanding and Applying Continuous Glucose Monitoring Technologies in Diabetes",
                "Several CGM devices are approved for nonadjunctive insulin dosing without confirmatory fingerstick.",
                True,
                "Modern CGM accuracy supports therapeutic insulin adjustments without mandatory SMBG confirmation on approved devices.",
                ref(
                    "Understanding and Applying Continuous Glucose Monitoring Technologies in Diabetes",
                    "Several CGM devices are approved for making insulin-dosing and titration decisions with no need for a confirmatory SMBG test reading, so-called nonadjunctive use.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Sensor Calibration and Accuracy",
                "CGM devices approved for nonadjunctive use typically have MARD below 10%.",
                True,
                "Lower MARD devices are typical for nonadjunctive and AID use, though prospective studies have not mandated a specific threshold.",
                ref(
                    "Sensor Calibration and Accuracy",
                    "Among CGM devices, those that are approved for nonadjunctive insulin dosing and titration, or use with AID systems, typically have lower MARD values of below 10%.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Time in Range in T1D and T2D",
                "Level 2 hypoglycemia is defined as glucose below 54 mg/dL.",
                True,
                "Level 1: 54–69 mg/dL alert; level 2: <54 mg/dL clinically significant hypo requiring immediate attention.",
                ref(
                    "Time in Range in T1D and T2D",
                    "Level 2 hypoglycemia, with a glucose level of below 54 mg/dL (3.0 mmol/L), with or without symptoms, is considered clinically significant",
                ),
            ),
            tf(
                f"{p}-t6",
                "Time in Range During Pregnancy",
                "The CONCEPTT trial showed CGM improved %TIRp without increased maternal hypoglycemia.",
                True,
                "CGM increased pregnancy TIR and reduced TAR at 34–35 weeks versus SMBG without worsening hypoglycemia.",
                ref(
                    "Time in Range During Pregnancy",
                    "Importantly, the CONCEPTT trial also showed that use of CGM helps women with T1D improve their %TIRp during pregnancy compared to controls using SMBG (68% vs. 61%; 16 hours, 19 min vs. 14 hours, 38 min/day), as well as reducing %TARp (27% vs. 32%; 6 hours, 29 min vs. 7 hours, 41 min/day) at 34 to 35 weeks. This improvement in glycemia was achieved without increased maternal hypoglycemia.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Telemonitoring and Telemedicine Are Essential Attributes of CGM Technology",
                "A meta-analysis found telemedicine is at least as effective as usual care for diabetes management.",
                True,
                "Meta-analysis of >3000 participants: telemedicine ≥ usual care, especially in T2D and longer-duration interventions.",
                ref(
                    "Telemonitoring and Telemedicine Are Essential Attributes of CGM Technology",
                    "A meta-analysis of telemedicine in T1D and T2D, covering interventions in more than 3000 participants, $ ^{153} $ found that telemedicine interventions are at least as effective as usual care in managing diabetes, especially T2D.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Insulin Pump Therapy Improves Measures of Glycemia and Quality of Life",
                "Pump therapy should be limited to patients who already have excellent HbA1c before starting.",
                False,
                "Those with highest pre-pump HbA1c often derive greatest benefit; pump therapy is not restricted to well-controlled patients.",
                ref(
                    "Insulin Pump Therapy Improves Measures of Glycemia and Quality of Life",
                    "Pre-pump therapy glycemia, as measured by  $ HbA_{1c} $, does not dictate whether integration of pump therapy will be useful. Indeed, analysis has shown that those with the highest  $ HbA_{1c} $ levels before introduction of pump therapy derive the greatest benefit.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Predictive Low Glucose Suspend",
                "The PROLOG RCT showed PLGS reduced time below 70 mg/dL by 31% versus SAP.",
                True,
                "6-week PROLOG: 31% less time <70 mg/dL with predictive low glucose suspend versus sensor-augmented pump alone.",
                ref(
                    "Predictive Low Glucose Suspend",
                    "The 6-week Predictive Low Glucose Suspend for Reduction of Low Glucose (PROLOG) RCT showed that with PLGS use there was a 31% reduction in time spent below 70 mg/dL (3.9 mmol/L) when compared to the control group who used SAP.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Insights From Open-Source AID Systems",
                "Consensus guidelines recommend that clinicians support patients who choose DIY open-source AID.",
                True,
                "Providers should cautiously support DIY AID users though devices lack regulatory approval.",
                ref(
                    "Insights From Open-Source AID Systems",
                    "While health care professionals should approach recommendation of these DIY devices cautiously as they do not have regulatory approval, consensus guidelines highlight that when people with diabetes choose to use a DIY AID system providers should support them.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Diabetes Technology for Noncritical Hospitalized Patients With and Without Preexisting Diabetes",
                "Real-time CGM is recommended for noncritically ill insulin-treated inpatients with confirmatory POC glucose.",
                True,
                "Endocrine Society recommends RT-CGM plus confirmatory bedside POC testing for insulin adjustments.",
                ref(
                    "Diabetes Technology for Noncritical Hospitalized Patients With and Without Preexisting Diabetes",
                    "In adults with insulin-treated diabetes hospitalized for noncritical illness, the use of real-time CGM is recommended, although with confirmatory bedside point-of-care (POC) blood glucose tests, for adjustments in insulin over POC testing alone.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Mobile Health and the Rise of Diabetes Smartphone Apps",
                "Manufacturer diabetes device apps have undergone regulatory assessment for accuracy and data privacy.",
                True,
                "Device-company apps are regulated; many independent apps lack equivalent oversight.",
                ref(
                    "Mobile Health and the Rise of Diabetes Smartphone Apps",
                    "The apps associated with manufacturers of diabetes devices have undergone regulatory assessment to ensure compliance with system accuracy and data privacy.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Future Directions",
                "Wearable CGM should become standard of care in T2D including those not on insulin.",
                True,
                "Future goal: CGM standard in T2D broadly, including noninsulin therapy and pregnancy with pregestational T2D.",
                ref(
                    "Future Directions",
                    "A similar objective is to have wearable CGM devices as the standard of care in the treatment of T2D, as it is now in T1D. This should include people with T2D not on insulin and also be standard of care for women with pregestational T2D during pregnancy.",
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
                "Assertion: Artificial intelligence decision-support advisers can facilitate day-to-day CGM use.",
                "Reason: CGM devices cannot transmit data to smartphones or pumps.",
                2,
                "Assertion true per key points; reason false—CGM wirelessly transmits to readers, phones, watches, and AID pumps.",
                ref(
                    "Understanding and Applying Continuous Glucose Monitoring Technologies in Diabetes",
                    "Glucose readings are transmitted wirelessly at intervals from 1 to 5 minutes to a reader, to a smartphone or smartwatch app, or, in the case of automated insulin delivery (AID) systems, to an insulin pump (see Fig. 36.1).",
                ),
            ),
            ar(
                f"{p}-ar2",
                "The Limitations of HbA $ _{1c} $",
                "Assertion: HbA1c can overestimate average glucose and risk treatment overintensification.",
                "Reason: HbA1c is never influenced by nonglycemic factors affecting red cell turnover.",
                2,
                "Assertion true—CGM confirms overintensification risk; reason false—HbA1c is affected by erythrocyte turnover and other nonglycemic factors.",
                ref(
                    "The Limitations of HbA $ _{1c} $",
                    "Thus, HbA $ _{1c} $ can either overestimate or in more clinical conditions underestimate average glucose in any person with diabetes.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Sensor Calibration and Accuracy",
                "Assertion: Interstitial and blood glucose may differ because of physiologic lag.",
                "Reason: Blood and interstitial fluid are identical compartments with instantaneous equilibration.",
                2,
                "Assertion true (3–15 min average lag); reason false—different physiologic compartments with dynamic delay.",
                ref(
                    "Sensor Calibration and Accuracy",
                    "Since blood and interstitial fluid are different physiologic compartments with different glycemic dynamics, $ ^{25} $ the concordance between interstitial fluid glucose and blood glucose readings must also take into account the time it takes for blood glucose levels to",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Time in Range in T1D and T2D",
                "Assertion: Higher TIR is associated with fewer diabetes complications in T2D.",
                "Reason: No evidence links CGM metrics to clinical outcomes.",
                2,
                "Assertion true—growing TIR-outcome data in T2D; reason false—evidence supports TIR-complication associations.",
                ref(
                    "Time in Range in T1D and T2D",
                    "However, available evidence supports that for people with T2D there is a consistent association between higher TIR and fewer macrovascular and microvascular complications, $ ^{72-77} $",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Improvements in Glycemic Outcomes in Type 1 Diabetes",
                "Assertion: CGM reduces hypoglycemia in T1D compared with SMBG.",
                "Reason: IMPACT trial found isCGM increased hypoglycemia below 70 mg/dL.",
                2,
                "Assertion true across multiple trials; reason false—IMPACT showed 38% reduction in hypo <70 mg/dL with isCGM.",
                ref(
                    "Improvements in Glycemic Outcomes in Type 1 Diabetes",
                    "The Randomised Controlled Study to Evaluate the Impact of Novel Glucose Sensing Technology on Hypoglycemia in Type 1 Diabetes (IMPACT) RCT $ ^{[139]} $ using isCGM in a group of 239 adults with well-controlled T1D (baseline HbA $ _{1c} $ ≤7.5%, 58 mmol/mol) found isCGM resulted in a 38% reduction in hypoglycemia below 70 mg/dL (3.9 mmol/L)",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Telemonitoring Can Help Change the Delivery of Care",
                "Assertion: Telemonitoring with CGM allows triage of who needs urgent consultation.",
                "Reason: Telemonitoring requires every patient to attend in-person visits at the same frequency.",
                2,
                "Assertion true—stable patients need less frequent contact; reason false—telemonitoring reduces unnecessary visits.",
                ref(
                    "Telemonitoring Can Help Change the Delivery of Care",
                    "Therefore, it is possible to triage individuals for clinical attention and reduce unnecessary visits.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Connected Insulin Pens",
                "Assertion: Smart pens can reduce insulin stacking and hypoglycemia risk.",
                "Reason: Smart pens have no ability to track insulin-on-board or duration of action.",
                2,
                "Assertion true—programmed duration of action limits stacking; reason false—pens store correction factors, carb ratios, and insulin action duration.",
                ref(
                    "Connected Insulin Pens",
                    "Stacking of insulin, administration of multiple doses of insulin in a short interval of time when prior doses remain active, can be minimized by programming duration of insulin action in the device, thereby reducing the risk of hypoglycemia.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Sensor-Augmented Pump Therapy",
                "Assertion: SAP therapy provides foundation for more integrated automated systems.",
                "Reason: SAP automatically delivers correction boluses without any user input.",
                2,
                "Assertion true; reason false—SAP displays data but user must act on alerts and deliver boluses.",
                ref(
                    "Sensor-Augmented Pump Therapy",
                    "Therefore, a high-glucose alert identified by a sensor would still require the person with diabetes to act, likely by delivering a correction bolus of insulin.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Automated Insulin Delivery",
                "Assertion: Hybrid AID still requires user-initiated prandial insulin.",
                "Reason: Fully automated closed loop without meal announcement is standard commercial care.",
                2,
                "Assertion true—hybrid approach adopted after postprandial excursions with full automation; reason false—commercial systems use hybrid meal boluses.",
                ref(
                    "Automated Insulin Delivery",
                    "Early studies used a fully automated approach, leading to a full closed loop. However, this approach led to significant postprandial glycemic excursions necessitating the adoption of a “hybrid” approach whereby prandial insulin is input by the user.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Access to AID Systems: Making Systems Available for All Individuals Requiring Insulin",
                "Assertion: Patients with highest baseline HbA1c or GMI may gain most from AID.",
                "Reason: AID is reserved only for patients already at glycemic goal.",
                2,
                "Assertion true per RCT and real-world data; reason false—consensus supports broad AID access including high A1c.",
                ref(
                    "Access to AID Systems: Making Systems Available for All Individuals Requiring Insulin",
                    "More recent analyses both from RCT data and real-world observational data have shown that those with the highest baseline HbA $ _{1c} $, or GMI, have the greatest reduction in time above range and GMI, as well as increase in time in target range.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Technologies for Glycemic Control in Hospitalized Patients",
                "Assertion: Inpatient glycemic management is complicated by fluctuating insulin needs and sensor limitations.",
                "Reason: Hospitalized patients have stable insulin requirements and CGM is always perfectly accurate.",
                2,
                "Assertion true—variable insulin sensitivity, nutrition, immobility, and sensor interference; reason false.",
                ref(
                    "Technologies for Glycemic Control in Hospitalized Patients",
                    "However, hospitalization itself poses several challenges to the use of technologies to optimize glucose management due to the high variability of insulin requirements and the heterogeneous mechanisms underlying hyperglycemia",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Decision-Support Systems for Visualizing CGM Data and Beyond",
                "Assertion: Cloud decision-support portals enable remote therapy review between visits.",
                "Reason: CGM data can only be reviewed during synchronous in-person appointments.",
                2,
                "Assertion true—secure remote AGP/TIR access; reason false—portals support asynchronous review.",
                ref(
                    "Decision-Support Systems for Visualizing CGM Data and Beyond",
                    "Decision-support portals can be accessed remotely between scheduled follow-up appointments so the health care professional can review up-to-date information about the individual's response to changes in therapy or progress toward goals.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "36",
        "title": "Digitized Approaches to Diabetes Diagnostics and Therapeutics",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Tadej Battelino, Jennifer L. Sherr, Alfonso Galderisi, and Klemen Dovc",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_36_Digitized_Approaches_to_Diabetes_Diagnostics_and_Therapeutics.md",
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
