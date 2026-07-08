#!/usr/bin/env python3
"""Generate Williams 15e module w15-34 — Therapeutics of Type 2 Diabetes Mellitus."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-34"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-34_Therapeutics_of_Type_2_Diabetes_Mellitus.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why T2D remains a global public health crisis",
                "IDF 2021 data estimate 535.6 million adults with diabetes worldwide, projected to 783 million by 2045—T2D accounts for ~90% of cases and drives enormous health expenditures.",
                ref(
                    "KEY POINTS",
                    "The International Diabetes Federation (IDF) estimated a global diabetes prevalence of 535.6 million people worldwide in 2021, with a projected increase in prevalence to 783 million by 2045.",
                ),
            ),
            note(
                f"{p}-n2",
                "Epidemiology",
                "How diabetes complications shorten life expectancy",
                "In the United States, diabetes is the leading cause of blindness, accounts for ≥40% of ESRD, doubles to quadruples cardiovascular risk, and reduces life expectancy by ~10 years.",
                ref(
                    "Epidemiology",
                    "In the United States, diabetes is the leading cause of blindness and accounts for at least 40% of end-stage renal disease (ESRD).",
                ),
            ),
            note(
                f"{p}-n3",
                "Diagnostic Criteria",
                "Why retinopathy thresholds define diabetes diagnosis",
                "FPG, 2-hour PG, and HbA1c predict retinopathy and, by inference, define diagnostic hyperglycemia thresholds for diabetes and prediabetes.",
                ref(
                    "Diagnostic Criteria",
                    "All three commonly used tests—fasting plasma glucose (FPG), 2-hour plasma glucose after a 75-g oral glucose load (2-hour PG), and glycated hemoglobin  $ A_{1c} $ ( $ HbA_{1c} $)—predict the presence of retinopathy and, by inference, define the glucose levels that are diagnostic of diabetes.",
                ),
            ),
            note(
                f"{p}-n4",
                "Diagnostic Criteria",
                "How HbA1c compares with glucose measurements for reproducibility",
                "Repeated FPG and 2-hour PG vary more within individuals than HbA1c; HbA1c also avoids fasting timing and reflects average glycemia over ~3 months.",
                ref(
                    "Diagnostic Criteria",
                    "In one study, the coefficient of variation for measurements repeated in single individuals was 6.4% for FPG and 16.7% for 2-hour",
                ),
            ),
            note(
                f"{p}-n5",
                "General Approaches to Management",
                "Why hyperglycemia is a modifiable complication risk",
                "Controlled trials show intensive glycemic management reduces microvascular complications; hyperglycemia is accepted as modifiable for eye, kidney, nerve, and (to a lesser degree) cardiovascular outcomes.",
                ref(
                    "General Approaches to Management",
                    "The hyperglycemia that defines diabetes is accepted as a modifiable risk factor for microvascular (eye, kidney, and nerve) complications and, to a lesser degree, cardiovascular outcomes.",
                ),
            ),
            note(
                f"{p}-n6",
                "Interventional Study Results",
                "How UKPDS intensive therapy reduced microvascular disease",
                "UKPDS sulfonylurea/insulin arm achieved ~1 percentage point lower median HbA1c over 10 years and a significant 25% relative risk reduction in microvascular complications.",
                ref(
                    "Interventional Study Results",
                    "Associated with this improvement in glycemic control, there was a significant 25% reduction in the risk of microvascular complications (retinopathy, nephropathy, and neuropathy) in the group assigned treatment with a sulfonylurea or insulin",
                ),
            ),
            note(
                f"{p}-n7",
                "Glycemic Treatment Targets",
                "Why ADA generally targets HbA1c below 7%",
                "ADA guidelines recommend HbA1c <7% for many adults, with less stringent 7–8% targets when hypoglycemia risk, limited life expectancy, or advanced comorbidity dominate.",
                ref(
                    "Glycemic Treatment Targets",
                    "These guidelines suggest that the goal of treatment should generally be an HbA $ _{1c} $ value of less than 7% (53.0 mmol/mol).",
                ),
            ),
            note(
                f"{p}-n8",
                "Diabetes Self-Management Education and Support",
                "How DSMES improves glycemic and clinical outcomes",
                "Structured DSMES lowers HbA1c by ~0.45–0.57%, reduces complications and distress, and is recommended for all T2D patients—yet remains underutilized.",
                ref(
                    "Diabetes Self-Management Education and Support",
                    "For example, glucose control has improved with  $ HbA_{1c} $ reductions of 0.45% to 0.57%.",
                ),
            ),
            note(
                f"{p}-n9",
                "Medical Nutrition Therapy",
                "Why 5% weight loss is the MNT efficacy threshold",
                "Structured lifestyle programs yield 5–7% weight loss; metabolic benefits correlate with ≥5% loss—below that, HbA1c improvements often mirror control groups.",
                ref(
                    "Medical Nutrition Therapy",
                    "Achieving a 5% weight loss more consistently yields clinically relevant metabolic benefits than lower levels of weight loss.",
                ),
            ),
            note(
                f"{p}-n10",
                "Physical Activity and Exercise",
                "How exercise acts as glucose-lowering therapy",
                "Aerobic plus resistance training reduces HbA1c ~0.4–0.9% independent of weight loss; benefits appear immediately though insulin sensitivity gains may last only 48–72 hours.",
                ref(
                    "Physical Activity and Exercise",
                    "Self-directed structured exercise programs have been associated with mean HbA $ _{1c} $ reductions of 0.4% to 0.9%, with the largest reduction seen in those using combined aerobic and resistance exercise.",
                ),
            ),
            note(
                f"{p}-n11",
                "Biguanides",
                "Why metformin is first-line pharmacotherapy",
                "Metformin combines effective glucose lowering, essentially no hypoglycemia risk, prediabetes prevention, and UKPDS cardiovascular/mortality signals—start at diagnosis if no contraindication.",
                ref(
                    "Biguanides",
                    "Based on its good tolerability, safety, and effectiveness together with evidence for medical benefits in controlled trials, it is generally recommended that metformin therapy be started in all patients with T2D at or near the time of diagnosis of diabetes, provided no contraindications are present.",
                ),
            ),
            note(
                f"{p}-n12",
                "Sulfonylureas",
                "How sulfonylureas trade efficacy for hypoglycemia risk",
                "Modern long-acting sulfonylureas lower fasting glucose effectively but cause hypoglycemia and modest weight gain—especially concerning in elderly patients and CKD.",
                ref(
                    "Sulfonylureas",
                    "The leading disadvantages of sulfonylureas are their tendency to cause hypoglycemia and usually modest weight gain.",
                ),
            ),
            note(
                f"{p}-n13",
                "DPP4 Inhibitors",
                "Why DPP4 inhibitors rarely cause hypoglycemia",
                "DPP4i potentiate glucose-dependent insulin secretion and suppress glucagon without affecting gastric emptying or satiety—HbA1c falls ~0.5–1.0% with weight neutrality and low hypoglycemia risk with metformin.",
                ref(
                    "DPP4 Inhibitors",
                    "They have no consistent effect on weight and no tendency to cause hypoglycemia when used alone or with metformin.",
                ),
            ),
            note(
                f"{p}-n14",
                "Sodium-Glucose Transporter Inhibitors",
                "How EMPA-REG OUTCOME reshaped T2D therapeutics",
                "Empagliflozin in high-CV-risk T2D reduced all-cause mortality 32%, cardiovascular mortality 38%, and heart failure hospitalization 35% over ~3 years median follow-up.",
                ref(
                    "Sodium-Glucose Transporter Inhibitors",
                    "Treatment with empagliflozin for a median time of about 3 years was associated with a 32% relative risk reduction of all-cause mortality, 38% reduction of cardiovascular mortality, and 35% reduction of hospitalization for heart failure.",
                ),
            ),
            note(
                f"{p}-n15",
                "Sodium-Glucose Transporter Inhibitors",
                "Why SGLT2 inhibitors dominate HF and CKD care",
                "Beyond glycemic effects, SGLT2i consistently reduce HF hospitalization and renal composite endpoints (EMPA-REG, CANVAS, DECLARE, CREDENCE)—benefits persist even when eGFR limits glucose lowering.",
                ref(
                    "Sodium-Glucose Transporter Inhibitors",
                    "It appears that SGLT2 inhibitors will ultimately play a larger role in heart failure and chronic kidney disease than in glucose control but will be a mainstay in T2D care.",
                ),
            ),
            note(
                f"{p}-n16",
                "GLP1 Receptor Agonists",
                "How LEADER established GLP1RA cardiovascular benefit",
                "Liraglutide over >3 years reduced the primary MACE composite 13%, cardiovascular death 22%, all-cause mortality 15%, and albuminuria progression 26% in high-risk T2D.",
                ref(
                    "GLP1 Receptor Agonists",
                    "Significant reductions of risk were found for the primary composite cardiovascular endpoint (13%), cardiovascular death (22%), all-cause mortality (15%), and progression of albuminuria (26%).",
                ),
            ),
            note(
                f"{p}-n17",
                "GLP1 Receptor Agonists",
                "Why GLP1RAs promote weight loss without intrinsic hypoglycemia",
                "GLP1 agonists delay gastric emptying, reduce appetite, and lower HbA1c with consistent weight loss; hypoglycemia occurs only when combined with secretagogues or insulin.",
                ref(
                    "GLP1 Receptor Agonists",
                    "Weight loss is consistently seen with the various GLP1 receptor agonists, although the magnitude of weight loss varies with the agents",
                ),
            ),
            note(
                f"{p}-n18",
                "GLP1 Receptor Agonists",
                "How tirzepatide exceeds semaglutide in glycemic and weight endpoints",
                "Tirzepatide 15 mg weekly lowered HbA1c 2.3% from baseline 8.3%, with 46% reaching 5.7% and 57% achieving >10% weight loss versus 24% with semaglutide 1 mg.",
                ref(
                    "GLP1 Receptor Agonists",
                    "With the tirzepatide 15 mg weekly dose HbA $ _{1c} $ decreased 2.3% from a baseline of 8.3% (67.0 mmol/mol), with 46% of the treatment group reaching an HbA $ _{1c} $ of 5.7% (38.8 mmol/mol).",
                ),
            ),
            note(
                f"{p}-n19",
                "Metformin",
                "Why seven second-line options follow inadequate metformin response",
                "When metformin alone fails after 3–6 months, add or substitute among sulfonylurea, basal insulin, DPP4i, SGLT2i, GLP1RA, tirzepatide, or TZD—each with distinct advantages.",
                ref(
                    "KEY POINTS",
                    "If the response to metformin is inadequate initially or subsequently, one or more other agents can be added. There are seven recommended second-line therapies: sulfonylurea, glucagon-like peptide-1 (GLP1) receptor, basal insulin, dipeptidyl peptidase-4 (DPP4) inhibitor, sodium-glucose cotransporter 2 (SGLT2) inhibitor, glucose-dependent insulinotropic polypeptide (GIP)/GLP1 dual receptor agonist, and thiazolidinedione.",
                ),
            ),
            note(
                f"{p}-n20",
                "Considerations in Personalizing Therapy",
                "How ASCVD versus HF steers agent selection",
                "With established ASCVD without HF, either SGLT2i or GLP1RA is recommended; with heart failure, SGLT2 inhibitors are preferred over GLP1RAs based on trial evidence.",
                ref(
                    "Considerations in Personalizing Therapy",
                    "In patients with heart failure, SGLT2 inhibitors have demonstrated superiority over GLP1 receptor agonists and are now the preferred agents.",
                ),
            ),
            note(
                f"{p}-n21",
                "Reducing Progression of Kidney Disease",
                "Why SGLT2i lead renal protection in T2D with CKD",
                "CVOTs and dedicated renal trials show 30–50% improvements in renal composite endpoints with SGLT2i; benefits persist across eGFR ranges even when glycemic effect wanes.",
                ref(
                    "Reducing Progression of Kidney Disease",
                    "The greatest benefit is seen with SGLT2 inhibitors where improvement in secondary renal endpoints such as albuminuria, doubling of serum creatinine, or a composite of 40% decline in eGFR, ESRD, and death were observed.",
                ),
            ),
            note(
                f"{p}-n22",
                "Basal Insulin",
                "How basal insulin must be personalized and titrated",
                "Start basal insulin at 10 units or 0.1–0.2 U/kg, titrate to fasting glucose target (often 100–120 mg/dL early); typical maintenance ~0.4–0.5 U/kg when combined with oral agents.",
                ref(
                    "Basal Insulin",
                    "Treatment can be started either with a fixed daily dose of 10 units or with a dose calculated as 0.1 to 0.2 units per kilogram body weight.",
                ),
            ),
            note(
                f"{p}-n23",
                "Treating Postprandial Hyperglycemia",
                "Why postprandial glucose drives residual HbA1c elevation",
                "Once basal therapies optimize fasting glucose, residual hyperglycemia is often postprandial—especially after breakfast and dinner—requiring prandial agents or short-acting GLP1RA.",
                ref(
                    "Treating Postprandial Hyperglycemia",
                    "After therapy of basal glucose has been optimized, the postprandial glucose excursion is generally highest after breakfast and the highest postprandial glucose is after dinner.",
                ),
            ),
            note(
                f"{p}-n24",
                "Preventing Type 2 Diabetes Mellitus",
                "How DPP lifestyle intervention prevents diabetes",
                "Lifestyle intervention in high-risk adults reduces T2D progression 30–60% over 3–5 years, sustained and correlating with modest (~5%) weight loss.",
                ref(
                    "Preventing Type 2 Diabetes Mellitus",
                    "Lifestyle intervention can provide a 30% to 60% reduction in progression to diabetes over a 3- to 5-year time frame.",
                ),
            ),
            note(
                f"{p}-n25",
                "Preventing Type 2 Diabetes Mellitus",
                "Why metformin complements lifestyle in high-risk subgroups",
                "DPP metformin reduced progression especially in adults <60 years, BMI ≥35, FPG >110 mg/dL, HbA1c ≥6.0%, or prior gestational diabetes—durable and cost-effective.",
                ref(
                    "Preventing Type 2 Diabetes Mellitus",
                    "Intervention with metformin was associated with a somewhat smaller reduction in progression to diabetes, although the benefit was similar to that of lifestyle in persons younger than 60 years of age, those with BMI greater than 35 kg/m $ ^{2} $",
                ),
            ),
            note(
                f"{p}-n26",
                "Continuous Glucose Monitoring",
                "How CGM supports insulin-treated T2D and validates HbA1c",
                "Medicare covers CGM for insulin-treated T2D; real-time alerts reduce hypoglycemia (critical in older patients) and CGM mean glucose can expose glycation gaps versus HbA1c.",
                ref(
                    "Continuous Glucose Monitoring",
                    "Medicare covers CGM use for people with T2D on insulin therapy. A strong rationale for this decision is that protection against hypoglycemia is of heightened importance in older patients.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Epidemiology",
                "A 52-year-old man is newly diagnosed with T2D. Which complication burden statistic from U.S. epidemiology is most accurate?",
                [
                    "Diabetes accounts for at least 40% of ESRD",
                    "Diabetes rarely causes blindness in the United States",
                    "Stroke risk is unchanged compared with nondiabetes",
                    "Life expectancy is unchanged with diabetes",
                ],
                0,
                "Diabetes is the leading cause of blindness and accounts for ≥40% of ESRD; cardiovascular and amputation risks are markedly increased.",
                ref(
                    "Epidemiology",
                    "In the United States, diabetes is the leading cause of blindness and accounts for at least 40% of end-stage renal disease (ESRD).",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Diagnostic Criteria",
                "An asymptomatic adult has FPG 128 mg/dL on two occasions. Which diagnostic principle applies?",
                [
                    "Unequivocal hyperglycemia may be confirmed by repeat testing",
                    "Random glucose alone always suffices without symptoms",
                    "OGTT is required for every diagnosis",
                    "HbA1c cannot be used for diagnosis",
                ],
                0,
                "In the absence of unequivocal hyperglycemia, results should be confirmed by repeat testing; FPG ≥126 mg/dL defines diabetes.",
                ref(
                    "Diagnostic Criteria",
                    "In the absence of unequivocal hyperglycemia, results should be confirmed by repeat testing.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Screening",
                "Which screening recommendation best matches Box 34.1 for an overweight 40-year-old with no risk factors beyond BMI 31?",
                [
                    "Begin testing now; repeat at least every 3 years if normal",
                    "Never screen before age 45 regardless of BMI",
                    "Screen only if symptomatic polyuria is present",
                    "Test only once in lifetime at age 65",
                ],
                0,
                "All adults should begin testing at age 45; overweight/obese adults with risk factors should be tested earlier with 3-year intervals if normal.",
                ref(
                    "Screening",
                    "4. All other people—begin testing at age 45",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Interventional Study Results",
                "In UKPDS metformin-treated overweight patients, which outcome showed statistically significant benefit at trial end?",
                [
                    "39% relative reduction in myocardial infarction",
                    "50% relative reduction in all microvascular endpoints",
                    "No effect on all-cause mortality",
                    "Increased hypoglycemia versus lifestyle alone in all groups equally",
                ],
                0,
                "Metformin in UKPDS showed significant 39% MI reduction, 32% any diabetes endpoint reduction, and 36% all-cause mortality reduction.",
                ref(
                    "Interventional Study Results",
                    "Metformin treatment was associated with a nonsignificant 29% reduction of microvascular disease, but there were statistically and clinically significant reductions of any diabetes-related endpoint (32%), myocardial infarction (39%), and all-cause mortality (36%).",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Glycemic Treatment Targets",
                "A 78-year-old with recurrent severe hypoglycemia on sulfonylurea and CKD stage 4 seeks guidance. Most appropriate HbA1c target?",
                [
                    "7% to 8% or higher individualized to avoid hypoglycemia",
                    "Strict <6.5% regardless of hypoglycemia history",
                    "No monitoring needed once on oral agents",
                    "Maintain >9% to prevent hypoglycemia",
                ],
                0,
                "Less stringent targets (7–8% or higher) are appropriate with severe hypoglycemia history, limited life expectancy, or advanced comorbidity.",
                ref(
                    "Glycemic Treatment Targets",
                    "a less stringent HbA $ _{1c} $ target, such as 7% to 8% (53.0–63.9 mmol/mol) or even higher in some cases, may be appropriate for patients with evidence suggesting high risk, including a history of severe hypoglycemia",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Diabetes Self-Management Education and Support",
                "A newly diagnosed T2D patient has never received structured education. Best next step?",
                [
                    "Refer for DSMES emphasizing self-management at diagnosis",
                    "Defer education until insulin is required",
                    "DSMES is optional and rarely beneficial",
                    "Provide only a printed diet sheet without follow-up",
                ],
                0,
                "ADA, AADE, and Academy of Nutrition and Dietetics recommend DSMES for all T2D patients; it lowers HbA1c and improves outcomes.",
                ref(
                    "Diabetes Self-Management Education and Support",
                    "The ADA together with the AADE and the Academy of Nutrition and Dietetics recommend that all individuals with T2D receive DSMES.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Medical Nutrition Therapy",
                "An obese T2D patient loses 8% body weight over 6 months with MNT. Expected glycemic outcome?",
                [
                    "Clinically meaningful HbA1c reduction likely",
                    "No glycemic change unless bariatric surgery is done",
                    "Weight loss below 15% never affects HbA1c",
                    "MNT cannot reduce medication needs",
                ],
                0,
                "≥5% weight loss yields clinically relevant metabolic benefits; 5–10% loss often produces meaningful HbA1c reductions.",
                ref(
                    "Medical Nutrition Therapy",
                    "Of those in the intervention group who lost 5% to 10% of body weight, 34% ended with  $ HbA_{1c} $ below 6.5% (47.5 mmol/mol).",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Physical Activity and Exercise",
                "Which exercise prescription aligns with T2D guidelines?",
                [
                    "150 min/week moderate activity plus resistance training 2–3×/week",
                    "Avoid all exercise if HbA1c is elevated",
                    "Vigorous exercise only; no resistance training",
                    "Exercise once monthly is sufficient",
                ],
                0,
                "Guidelines recommend 150 min/week moderate (or 75 min vigorous) activity on ≥3 days/week plus resistance exercise 2–3 times weekly.",
                ref(
                    "Physical Activity and Exercise",
                    "It is recommended that individuals strive for 150 minutes of moderate-intensity physical activity (50%-70% of maximum heart rate) or 75 minutes per week of vigorous exercise (>70% of maximum heart rate) on at least 3 days per week with no more than 2 consecutive days without exercise.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Biguanides",
                "A patient with eGFR 38 mL/min/1.73 m² on metformin 2000 mg daily. Appropriate action?",
                [
                    "Consider dose reduction; avoid initiation at this eGFR",
                    "Continue full dose indefinitely",
                    "Metformin is contraindicated only above eGFR 60",
                    "Switch to sulfonylurea monotherapy without renal caution",
                ],
                0,
                "Initiation not recommended if eGFR <45; consider dose reduction if eGFR under 45 and stop if <30.",
                ref(
                    "Biguanides",
                    "Initiation is not recommended if the eGFR is <45 mL/min/1.73 m $ ^{2} $ and is contraindicated if the eGFR is <30 mL/min/1.73 m $ ^{2} $.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Sulfonylureas",
                "An 82-year-old with T2D and CKD stage 3 on glimepiride reports recurrent hypoglycemia. Which factor best explains risk?",
                [
                    "Sulfonylurea hypoglycemia risk is major in elderly and CKD",
                    "Glimepiride never causes hypoglycemia with metformin",
                    "Hypoglycemia occurs only with insulin, not secretagogues",
                    "Age does not affect secretagogue safety",
                ],
                0,
                "Hypoglycemia and weight gain are leading SU disadvantages; risk is especially high in elderly and CKD patients.",
                ref(
                    "Sulfonylureas",
                    "The risk of hypoglycemia is a major concern in the elderly and those with chronic kidney disease.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "DPP4 Inhibitors",
                "Metformin plus sitagliptin fails to reach HbA1c goal. Patient fears hypoglycemia and weight gain. Which statement about DPP4i is true?",
                [
                    "DPP4 inhibitors seldom cause hypoglycemia with metformin",
                    "DPP4 inhibitors always cause 3–5 kg weight loss",
                    "DPP4 inhibitors are more potent than GLP1RA for A1c",
                    "DPP4 inhibitors replace all prandial insulin needs",
                ],
                0,
                "DPP4i reduce HbA1c ~0.5–1.0% with weight neutrality and minimal hypoglycemia risk when combined with metformin.",
                ref(
                    "DPP4 Inhibitors",
                    "They have no consistent effect on weight and no tendency to cause hypoglycemia when used alone or with metformin.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Sodium-Glucose Transporter Inhibitors",
                "A T2D patient with HFrEF and ASCVD needs second-line therapy beyond metformin. Evidence-based choice?",
                [
                    "Empagliflozin or another SGLT2 inhibitor",
                    "Glyburide as preferred agent in heart failure",
                    "Avoid all SGLT2 inhibitors in cardiovascular disease",
                    "Pioglitazone as first choice in active heart failure",
                ],
                0,
                "SGLT2 inhibitors reduce HF hospitalization consistently and are preferred in heart failure over GLP1RAs.",
                ref(
                    "Considerations in Personalizing Therapy",
                    "In patients with heart failure, SGLT2 inhibitors have demonstrated superiority over GLP1 receptor agonists and are now the preferred agents.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Sodium-Glucose Transporter Inhibitors",
                "Which EMPA-REG OUTCOME finding best supports empagliflozin in high-risk T2D?",
                [
                    "35% reduction in heart failure hospitalization",
                    "Increased all-cause mortality",
                    "No renal endpoints were affected",
                    "Stroke reduction was the primary consistent benefit",
                ],
                0,
                "EMPA-REG showed 32% all-cause mortality, 38% CV mortality, and 35% HF hospitalization reductions with empagliflozin.",
                ref(
                    "Sodium-Glucose Transporter Inhibitors",
                    "35% reduction of hospitalization for heart failure.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "GLP1 Receptor Agonists",
                "A T2D patient with established ASCVD without HF needs injectable therapy. Which class has CV outcome trial benefit?",
                [
                    "Long-acting GLP1 receptor agonist (e.g., liraglutide)",
                    "Short-acting exenatide only",
                    "Pramlintide as first-line for ASCVD",
                    "Alpha-glucosidase inhibitor for MACE reduction",
                ],
                0,
                "Long-acting GLP1RAs (LEADER, SUSTAIN-6, REWIND, etc.) showed cardiovascular benefit in high-risk populations; short-acting agents lack CVOT benefit.",
                ref(
                    "GLP1 Receptor Agonists",
                    "Large randomized trials examining cardiovascular safety of liraglutide, semaglutide, dulaglutide, and albiglutide have shown cardiovascular benefit in populations selected for having high cardiovascular risk",
                ),
            ),
            mcq(
                f"{p}-m15",
                "GLP1 Receptor Agonists",
                "Semaglutide is added to basal insulin with HbA1c 7.4%. Recommended insulin adjustment?",
                [
                    "Reduce insulin dose ~20% unless HbA1c >8%",
                    "Double insulin dose simultaneously",
                    "No insulin change ever required",
                    "Stop all oral agents including metformin mandatorily",
                ],
                0,
                "When adding GLP1RA to insulin, reduce insulin ~20% unless HbA1c exceeds 8%; also reduce secretagogue to minimum if combined.",
                ref(
                    "GLP1 Receptor Agonists",
                    "When a GLP1 receptor agonist is added to insulin, a 20% reduction of insulin dosage is advised unless  $ HbA_{1c} $ is greater than 8% (63.9 mmol/mol).",
                ),
            ),
            mcq(
                f"{p}-m16",
                "GLP1 Receptor Agonists",
                "In SUSTAIN-6, semaglutide versus placebo showed which cardiovascular finding?",
                [
                    "26% reduction in primary MACE composite",
                    "Reduced HF hospitalizations significantly",
                    "Significant all-cause mortality reduction",
                    "No renal endpoint effects",
                ],
                0,
                "SUSTAIN-6 demonstrated 26% primary CV composite reduction and renal endpoint reduction but no mortality or HF hospitalization benefit.",
                ref(
                    "GLP1 Receptor Agonists",
                    "This study demonstrated somewhat greater reduction of risk for its primary cardiovascular composite endpoint (26%) compared with LEADER, and also showed a reduction of renal endpoints.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Insulins",
                "Metformin plus sulfonylurea fails; patient agrees to injectable therapy preferring once-daily dosing. Typical first insulin step?",
                [
                    "Basal insulin (glargine, detemir, degludec, or NPH)",
                    "Premixed 70/30 twice daily before any basal trial",
                    "Prandial insulin alone without basal",
                    "U-500 regular as mandatory first injection",
                ],
                0,
                "Long-acting insulins are usually initiated before short-acting; basal insulin added to oral agents is well-established after oral failure.",
                ref(
                    "Insulins",
                    "Long-acting insulins are usually initiated before short-acting ones.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Insulins",
                "A patient on basal glargine plus oral agents has fasting glucose at goal but HbA1c 8.2%. Next best step before full basal-bolus?",
                [
                    "Add GLP1 receptor agonist or single prandial insulin dose",
                    "Only increase basal insulin until nocturnal hypoglycemia",
                    "Stop metformin when any insulin is started",
                    "Add TZD only; postprandial glucose never contributes",
                ],
                0,
                "After basal optimization, postprandial excursions dominate; adding GLP1RA or one prandial injection matches basal-bolus efficacy with less hypoglycemia/weight gain.",
                ref(
                    "Treating Postprandial Hyperglycemia",
                    "While adding prandial insulin remains a common practice when basal insulin is not adequately effective in T2D, adding a GLP1 receptor agonist while continuing basal insulin is preferred if one is not already in use.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Metformin",
                "Newly diagnosed T2D with eGFR 90, no contraindications. Standard initial pharmacotherapy?",
                [
                    "Metformin plus lifestyle and DSMES",
                    "Basal insulin as mandatory first-line",
                    "Sulfonylurea monotherapy preferred over metformin",
                    "Defer all pharmacotherapy until HbA1c >10%",
                ],
                0,
                "Metformin with diet, exercise, and DSMES is first-line—essentially no hypoglycemia risk and strong evidence base.",
                ref(
                    "Metformin",
                    "Metformin is generally considered the choice for initial drug therapy for T2D in patients with adequate renal function.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Considerations in Personalizing Therapy",
                "GRADE trial: metformin plus which add-on showed greatest HbA1c durability and least severe hypoglycemia versus glimepiride?",
                [
                    "Liraglutide or glargine over glimepiride/sitagliptin",
                    "Sitagliptin over all other classes",
                    "Glimepiride over glargine for hypoglycemia safety",
                    "All four agents identical for A1c and safety",
                ],
                0,
                "GRADE: liraglutide and glargine maintained HbA1c <7% longer than glimepiride or sitagliptin; severe hypoglycemia was more frequent with glimepiride.",
                ref(
                    "Metformin",
                    "All four medications decreased HbA $ _{1c} $ but liraglutide and glargine were moderately more effective than glimepiride or sitagliptin in reducing and maintaining the value <7.0%.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Reducing Progression of Kidney Disease",
                "T2D patient with albuminuria and eGFR 55. Which glucose-lowering class has strongest renal outcome evidence?",
                [
                    "SGLT2 inhibitor",
                    "Short-acting sulfonylurea alone",
                    "Alpha-glucosidase inhibitor as sole renal therapy",
                    "Bromocriptine for nephroprotection",
                ],
                0,
                "SGLT2 inhibitors show greatest renal benefit (albuminuria, eGFR decline, ESRD composites) and are strongly recommended in diabetes with CKD.",
                ref(
                    "Reducing Progression of Kidney Disease",
                    "SGLT2 inhibitors are therefore strongly recommended for those with diabetes and chronic kidney disease.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Minimizing Hypoglycemia",
                "Elderly T2D patient with prior severe hypoglycemia on glimepiride. Safest pharmacologic adjustment after metformin continuation?",
                [
                    "Switch to DPP4 inhibitor, GLP1RA, or SGLT2i",
                    "Add second sulfonylurea for synergy",
                    "Increase glimepiride to maximum dose",
                    "Premixed insulin three times daily without monitoring",
                ],
                0,
                "After metformin, agents with little/no hypoglycemia risk include DPP4i, GLP1RA, SGLT2i, tirzepatide, and TZDs.",
                ref(
                    "Minimizing Hypoglycemia",
                    "Metformin does not cause hypoglycemia when used alone, and drug choices after metformin with little or no additional risk include DPP4 inhibitors, GLP1 receptor agonists, SGLT inhibitors, GLP1/GIP dual agonists, and TZDs.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Minimizing Weight Gain",
                "Obese T2D on metformin needs second agent prioritizing weight loss. Best options?",
                [
                    "Tirzepatide or long-acting GLP1RA or SGLT2i",
                    "Sulfonylurea plus pioglitazone",
                    "NPH insulin twice daily as first injectable",
                    "Premixed 70/30 insulin before lifestyle intensification",
                ],
                0,
                "Weight-minimizing strategy favors metformin then GLP1RA, GIP/GLP1 dual agonist, or SGLT2i; SU, pioglitazone, and prandial insulin promote gain.",
                ref(
                    "Minimizing Weight Gain",
                    "The GLP1 receptor agonists, GIP/GLP1 dual agonist, and SGLT inhibitors are all options as second-line therapy when weight is a major consideration.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Special Situations in Clinical Management",
                "New T2D diagnosis with HbA1c 11%, random glucose 340 mg/dL, mild dehydration, no acidosis. Recommended initial approach?",
                [
                    "Insulin (often with metformin) to rapidly reverse glucotoxicity",
                    "Lifestyle alone for 6 months before any drug",
                    "GLP1RA loading dose as sole initial therapy",
                    "Observation only until DKA develops",
                ],
                0,
                "Marked hyperglycemia at diagnosis usually warrants initial insulin; intensive early control may induce remission in some patients.",
                ref(
                    "Special Situations in Clinical Management",
                    "for most patients presenting with these very high glucose levels, most experts recommend initial insulin therapy.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Pregnancy",
                "A woman with prior gestational diabetes now has normal glucose postpartum. Follow-up plan?",
                [
                    "Test glucose or HbA1c every 1–3 years lifelong",
                    "No further testing unless symptomatic",
                    "Metformin prevention is contraindicated in all GDM history",
                    "Bariatric surgery required after any GDM",
                ],
                0,
                "After GDM, 50–70% develop T2D over 15–25 years; periodic glucose or HbA1c testing every 1–3 years enables early detection.",
                ref(
                    "Pregnancy",
                    "periodic follow-up with testing of glucose or HbA $ _{1c} $ is indicated every 1 to 3 years to allow early detection.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Preventing Type 2 Diabetes Mellitus",
                "A 48-year-old with prediabetes (HbA1c 6.1%), BMI 36, prior GDM. Besides lifestyle, which prevention strategy has evidence?",
                [
                    "Consider metformin given high-risk profile",
                    "Routine GLP1RA for all prediabetes",
                    "Acarbose is only approved prevention drug",
                    "No pharmacotherapy ever appropriate in prediabetes",
                ],
                0,
                "Metformin prevention is recommended for high-risk groups including BMI ≥35, age <60, elevated FPG/A1c, and prior GDM.",
                ref(
                    "Preventing Type 2 Diabetes Mellitus",
                    "On balance, therefore, consideration of metformin therapy is recommended in patients who are at particularly high risk.",
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
                "Metformin as initial therapy carries essentially no risk of hypoglycemia when combined with lifestyle measures.",
                True,
                "Key points emphasize metformin plus diet, exercise, and education lowers glucose with essentially no hypoglycemia risk.",
                ref(
                    "KEY POINTS",
                    "Metformin as initial therapy in combination with diet, exercise, and comprehensive diabetes education effectively lowers glucose with essentially no risk of hypoglycemia.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Epidemiology",
                "Approximately 38% of U.S. adults have prediabetes by fasting glucose or HbA1c criteria.",
                True,
                "CDC estimates 96 million adults (38%) have prediabetes and high diabetes risk.",
                ref(
                    "Epidemiology",
                    "Moreover, 38.0% of adults in the United States (96 million) were estimated to have prediabetes and thus be at high risk for developing diabetes.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Diagnostic Criteria",
                "The oral glucose tolerance test is recommended for routine diabetes diagnosis in most patients.",
                False,
                "OGTT is useful for research but inconvenient and variable; diagnosis usually made by FPG, symptomatic random glucose, or HbA1c.",
                ref(
                    "Diagnostic Criteria",
                    "Although the oral glucose tolerance test (OGTT) is very useful for research, it is not recommended for routine use in diagnosing diabetes.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Interventional Study Results",
                "UKPDS sulfonylurea/insulin intensive therapy reduced microvascular complications by about 25%.",
                True,
                "Associated glycemic improvement yielded significant 25% microvascular risk reduction versus conventional lifestyle-only policy.",
                ref(
                    "Interventional Study Results",
                    "there was a significant 25% reduction in the risk of microvascular complications (retinopathy, nephropathy, and neuropathy) in the group assigned treatment with a sulfonylurea or insulin",
                ),
            ),
            tf(
                f"{p}-t5",
                "Self-Monitoring of Blood Glucose",
                "SMBG is particularly recommended for T2D patients taking insulin or sulfonylureas.",
                True,
                "SMBG identifies asymptomatic hypoglycemia and guides insulin titration in secretagogue/insulin-treated T2D.",
                ref(
                    "Self-Monitoring of Blood Glucose",
                    "Use of SMBG is particularly recommended for patients with T2D who are taking insulin or sulfonylureas because it can identify minimal or asymptomatic episodes of hypoglycemia",
                ),
            ),
            tf(
                f"{p}-t6",
                "Thiazolidinediones",
                "Pioglitazone and rosiglitazone are equally effective in improving glycemic control.",
                True,
                "Head-to-head data show equivalent glycemic efficacy and insulin sensitivity marker improvements for the two available TZDs.",
                ref(
                    "Thiazolidinediones",
                    "Pioglitazone and rosiglitazone are equally effective in improving glycemic control and provide equivalent improvements in markers of insulin resistance and inflammation.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Sodium-Glucose Transporter Inhibitors",
                "CREDENCE was a cardiovascular outcomes trial without baseline nephropathy requirements.",
                False,
                "CREDENCE was a dedicated renal outcomes trial in patients with nephropathy at baseline (Table 34.10 footnote).",
                ref(
                    "Sodium-Glucose Transporter Inhibitors",
                    "CREDENCE trial was a renal outcomes trial in patients with nephropathy at baseline.",
                ),
            ),
            tf(
                f"{p}-t8",
                "GLP1 Receptor Agonists",
                "LEADER and SUSTAIN-6 both demonstrated significant reductions in heart failure hospitalization.",
                False,
                "Neither LEADER nor SUSTAIN-6 showed HF hospitalization reduction—HF benefit is chiefly an SGLT2i class effect.",
                ref(
                    "GLP1 Receptor Agonists",
                    "Neither LEADER nor SUSTAIN-6 showed a reduction of hospitalizations for heart failure.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Insulins",
                "Premixed 70/30 insulin improved control versus basal insulin but caused more hypoglycemia.",
                True,
                "Premixed insulin study in T2D showed better glucose control at cost of significantly more hypoglycemia versus basal alone.",
                ref(
                    "Insulins",
                    "use of 70/30 insulin in T2D showed greater improvement in glucose control but at the cost of significantly more hypoglycemia compared to basal insulin.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Metformin",
                "Two-drug therapy including metformin often maintains targets for 5–10 years after diagnosis.",
                True,
                "Combination with metformin and another class commonly sustains glycemic targets for 5–10 years from diagnosis.",
                ref(
                    "Metformin",
                    "Two-agent therapy including metformin and any of these other classes is likely to be successful in attaining glycemic targets for 5 to 10 years from diagnosis.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Preventing Type 2 Diabetes Mellitus",
                "DPP lifestyle intervention reduced diabetes progression by 30% to 60% over 3–5 years.",
                True,
                "Multiple prevention trials show sustained 30–60% relative risk reduction with lifestyle, correlating with modest weight loss.",
                ref(
                    "Preventing Type 2 Diabetes Mellitus",
                    "Lifestyle intervention can provide a 30% to 60% reduction in progression to diabetes over a 3- to 5-year time frame.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Type 2 Diabetes in Youth",
                "Youth-onset T2D may require basal insulin plus metformin when fasting glucose exceeds 250 mg/dL or HbA1c exceeds 8.5%.",
                True,
                "Pediatric T2D management adds basal insulin to metformin when glycemia is markedly elevated at presentation.",
                ref(
                    "Type 2 Diabetes in Youth",
                    "if blood glucose measurements are over 250 mg/dL (19.4 mmol/L) fasting or HbA $ _{1c} $ is over 8.5% (69.4 mmol/mol), it is most reasonable to start with basal insulin as well as metformin.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Minimizing Hypoglycemia",
                "Prior severe hypoglycemia may justify raising HbA1c target from 7% toward 8% or higher.",
                True,
                "Therapeutic tactics should avoid hypoglycemia; prior severe events may warrant less stringent A1c goals.",
                ref(
                    "Minimizing Hypoglycemia",
                    "Finally, prior occurrence of severe hypoglycemia may be sufficient reason to increase the HbA $ _{1c} $ target range from 7% to 8% (from 53.0 to 63.9 mmol/mol) or even higher.",
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
                "Assertion: Seven second-line therapies exist when metformin is inadequate.",
                "Reason: Metformin must be discontinued once HbA1c falls below 6.5%.",
                2,
                "Assertion true; reason false—metformin may continue even if HbA1c falls below 6.5%.",
                ref(
                    "Biguanides",
                    "Metformin has been shown to reduce progression from prediabetes to diabetes, $ ^{191,192} $ and it does not need to be discontinued if HbA $ _{1c} $ falls below 6.5%.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Diagnostic Criteria",
                "Assertion: FPG, 2-hour PG, and HbA1c all predict retinopathy.",
                "Reason: All three markers always agree in the same individual at one time point.",
                2,
                "Assertion true; reason false—glycemic parameters do not always correlate; confirmatory testing often required.",
                ref(
                    "Diagnostic Criteria",
                    "It is possible to see a diagnostic elevation of plasma glucose while the  $ HbA_{1c} $ is below 6.5% or vice versa.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Interventional Study Results",
                "Assertion: UKPDS intensive sulfonylurea/insulin therapy reduced microvascular complications.",
                "Reason: Intensive therapy maintained HbA1c at 6% for the full 10-year randomized period.",
                2,
                "Assertion true; reason false—HbA1c initially fell to ~6% but rose to ~8% over 10 years in the intensive arm.",
                ref(
                    "Interventional Study Results",
                    "HbA $ _{1c} $ fell initially to about 6% (42.1 mmol/mol) but gradually rose to approximately 8% (63.9 mmol/mol) over 10 years of randomized treatment.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Biguanides",
                "Assertion: Metformin is recommended at T2D diagnosis when no contraindications exist.",
                "Reason: Metformin works solely by increasing peripheral insulin sensitivity without hepatic effects.",
                2,
                "Assertion true; reason false—main clinical effect is reduced hepatic gluconeogenesis; peripheral sensitivity effects are less consistent.",
                ref(
                    "Biguanides",
                    "Although the main clinical effect of metformin is to reduce hepatic gluconeogenesis, this mechanism does not account for all if its effects.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Sulfonylureas",
                "Assertion: Modern long-acting sulfonylureas lower fasting glucose effectively.",
                "Reason: They stimulate insulin secretion independent of ambient glucose at all times without hypoglycemia risk.",
                2,
                "Assertion true; reason false—continued SUR1 occupancy limits glucose-independent secretion but hypoglycemia remains a leading disadvantage.",
                ref(
                    "Sulfonylureas",
                    "Due to these longer profiles, continued SUR1 occupancy limits glucose-independent insulin release accompanying each subsequent dose, while continuing to potentiate glucose-dependent basal insulin secretion.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Sodium-Glucose Transporter Inhibitors",
                "Assertion: SGLT2 inhibitors reduce heart failure hospitalizations in CVOTs.",
                "Reason: Their primary mechanism is maximal glycemic lowering superior to GLP1RA.",
                2,
                "Assertion true; reason false—glucose lowering is moderate, similar to SU/DPP4i and less than GLP1RA/insulin; HF benefit likely multifactorial beyond glycemia.",
                ref(
                    "Sodium-Glucose Transporter Inhibitors",
                    "yielding results that are similar to the efficacy of sulfonylureas and DPP4 inhibitors though less effective than the newest GLP1 receptor agonists or insulin.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "GLP1 Receptor Agonists",
                "Assertion: LEADER showed cardiovascular mortality reduction with liraglutide.",
                "Reason: LEADER also significantly reduced heart failure hospitalizations.",
                2,
                "Assertion true (22% CV death reduction); reason false—LEADER did not reduce HF hospitalizations.",
                ref(
                    "GLP1 Receptor Agonists",
                    "Neither LEADER nor SUSTAIN-6 showed a reduction of hospitalizations for heart failure.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Considerations in Personalizing Therapy",
                "Assertion: GLP1RA are preferred over insulin when ASCVD is present if no contraindications.",
                "Reason: GLP1RA always cause more hypoglycemia than basal insulin.",
                2,
                "Assertion true; reason false—GLP1RA have low hypoglycemia rates and weight loss versus insulin-associated gain and hypoglycemia risk.",
                ref(
                    "Considerations in Personalizing Therapy",
                    "GLP1 receptor agonists are also associated with significant weight loss rather than weight gain and low rates of hypoglycemia.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Basal Insulin",
                "Assertion: Basal insulin dosing must be individualized by titration to fasting glucose.",
                "Reason: All T2D patients require the same fixed 40 units daily basal dose.",
                2,
                "Assertion true; reason false—daily requirements range 10–200 units with wide interpatient variation.",
                ref(
                    "Basal Insulin",
                    "The necessary daily dosage ranges between 10 and 200 units, and a given patient’s requirement must be determined by titrating to a fasting glucose target.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Treating Postprandial Hyperglycemia",
                "Assertion: When HbA1c remains high despite good premeal glucose, postprandial increments may explain the gap.",
                "Reason: Postprandial glucose never contributes to HbA1c in T2D.",
                2,
                "Assertion true; reason false—postprandial testing becomes important when A1c exceeds expectations despite acceptable premeal values.",
                ref(
                    "Self-Monitoring of Blood Glucose",
                    "Postprandial testing also becomes important when the HbA $ _{1c} $ remains high despite attainment of reasonably good premeal glucose levels.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Preventing Type 2 Diabetes Mellitus",
                "Assertion: Lifestyle intervention prevents progression from prediabetes to diabetes.",
                "Reason: Average sustained weight loss in prevention trials exceeded 15% body weight.",
                2,
                "Assertion true; reason false—average sustained weight loss was modest (~5%).",
                ref(
                    "Preventing Type 2 Diabetes Mellitus",
                    "However, the average sustained weight loss in these trials was modest, on the order of 5%.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Special Situations in Clinical Management",
                "Assertion: Severely hyperglycemic newly diagnosed T2D may require hospitalization if acutely ill.",
                "Reason: All new T2D patients with any hyperglycemia always require ICU admission.",
                2,
                "Assertion true for ill/dehydrated/acidotic patients; reason false—outpatient therapy suffices for many high-glucose presentations without severe illness.",
                ref(
                    "Special Situations in Clinical Management",
                    "Those who are especially ill, with serious dehydration, acidosis, impaired mental status, or serious concomitant illness, will need hospitalization to receive intravenous fluids and insulin.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "34",
        "title": "Therapeutics of Type 2 Diabetes Mellitus",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Andrew J. Ahmann and Matthew C. Riddle",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_34_Therapeutics_of_Type_2_Diabetes_Mellitus.md",
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
