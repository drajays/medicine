#!/usr/bin/env python3
"""Generate Williams 15e module w15-39 — Hypoglycemia."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-39"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-39_Hypoglycemia.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why hypoglycemia is uncommon without diabetes but frequent with insulin therapy",
                "In persons without diabetes, effective counterregulatory defenses make hypoglycemia rare; in insulin-, sulfonylurea-, or glinide-treated diabetes it is common and often iatrogenic.",
                ref(
                    "KEY POINTS",
                    "Hypoglycemia—a plasma glucose concentration low enough to cause symptoms or signs—is a rare occurrence in individuals without diabetes but is common in insulin-, sulfonylurea-, or glinide-treated diabetes or in children with some metabolic conditions.",
                ),
            ),
            note(
                f"{p}-n2",
                "Physiology of Glucose Counterregulation: Responses to Hypoglycemia",
                "How the three physiologic defenses against falling glucose are sequenced",
                "Healthy individuals mount (1) decreased insulin, (2) increased glucagon, and when glucagon is deficient (3) increased epinephrine, before behavioral carbohydrate ingestion.",
                ref(
                    "Physiology of Glucose Counterregulation: Responses to Hypoglycemia",
                    "Falling plasma glucose concentrations cause a sequence of key physiologic and behavioral responses, with defined glycemic thresholds, in healthy individuals: (1) a decrease in insulin, (2) an increase in glucagon, and, in the absence of the latter, (3) an increase in epinephrine.",
                ),
            ),
            note(
                f"{p}-n3",
                "Systemic Glucose Balance",
                "Why insulin and counterregulatory hormones maintain minute-to-minute glucose balance",
                "Endogenous glucose production and peripheral utilization are regulated primarily by insulin (lowering glucose) and glucagon and epinephrine (raising glucose) despite wide variation in meals and exercise.",
                ref(
                    "Systemic Glucose Balance",
                    "This regulation is exerted primarily by the plasma glucose-lowering (regulatory) hormone insulin and the plasma glucose-raising (counterregulatory) hormones glucagon and epinephrine",
                ),
            ),
            note(
                f"{p}-n4",
                "Pathophysiology of Glucose Counterregulation in Diabetes",
                "Why exogenous insulin abolishes the first defense against hypoglycemia",
                "After insulin administration, circulating insulin does not fall as glucose declines—especially with absolute β-cell failure—so the primary regulatory decrease in insulin is lost.",
                ref(
                    "Pathophysiology of Glucose Counterregulation in Diabetes",
                    "Importantly, after insulin administration circulating (exogenous) insulin concentrations do not decrease as plasma glucose concentrations fall.",
                ),
            ),
            note(
                f"{p}-n5",
                "Pathophysiology of Glucose Counterregulation in Diabetes",
                "How β-cell failure eliminates the glucagon counterregulatory response",
                "Despite functional α-cells, glucagon does not rise during hypoglycemia in insulin-deficient diabetes because the intraislet insulin decrement that normally signals α-cells is absent.",
                ref(
                    "Pathophysiology of Glucose Counterregulation in Diabetes",
                    "Furthermore, despite the presence of functional  $ \\alpha $-cells, there is no increase in glucagon secretion (Fig. 39.6).",
                ),
            ),
            note(
                f"{p}-n6",
                "Pathophysiology of Glucose Counterregulation in Diabetes",
                "Why defective glucose counterregulation dramatically raises severe hypoglycemia risk",
                "With absent insulin and glucagon responses, attenuated epinephrine causes defective glucose counterregulation associated with ≥25-fold increased severe hypoglycemia risk in T1D.",
                ref(
                    "Pathophysiology of Glucose Counterregulation in Diabetes",
                    "In the setting of absent insulin and glucagon responses, the attenuated epinephrine response causes the clinical syndrome of defective glucose counterregulation (see Fig. 39.5),  $ ^{77-79} $ which is associated with a 25-fold  $ ^{79} $ or greater  $ ^{80} $ increased risk of severe hypoglycemia in T1D.",
                ),
            ),
            note(
                f"{p}-n7",
                "Pathophysiology of Glucose Counterregulation in Diabetes",
                "How impaired awareness of hypoglycemia develops in diabetes",
                "Attenuated sympathoadrenal responses—especially reduced sympathetic neural norepinephrine and acetylcholine release—blunt neurogenic symptoms that normally prompt carbohydrate ingestion.",
                ref(
                    "Pathophysiology of Glucose Counterregulation in Diabetes",
                    "impaired awareness of hypoglycemia is largely the result of reduced release of the sympathetic neurotransmitters norepinephrine and acetylcholine.",
                ),
            ),
            note(
                f"{p}-n8",
                "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                "Why recent antecedent hypoglycemia induces HAAF",
                "In absolute insulin deficiency, recurrent hypoglycemia attenuates epinephrine and sympathetic neural responses to subsequent falling glucose, perpetuating a vicious cycle.",
                ref(
                    "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                    "Those episodes  $ ^{83} $ (as well as sleep  $ ^{85,86} $ or prior exercise  $ ^{84} $) attenuate adrenomedullary epinephrine secretion and sympathetic neural activation in response to subsequent hypoglycemia.",
                ),
            ),
            note(
                f"{p}-n9",
                "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                "How scrupulous avoidance of hypoglycemia can restore awareness",
                "Three or more weeks of rigorous hypoglycemia avoidance can reverse impaired awareness of hypoglycemia, though epinephrine responses may remain blunted in long-duration diabetes.",
                ref(
                    "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                    "3 or more weeks of scrupulous avoidance of hypoglycemia can reverse impaired awareness of hypoglycemia, although may not improve the attenuated epinephrine component of defective glucose counterregulation in individuals with longer (>10 years) diabetes duration (Fig. 39.8).",
                ),
            ),
            note(
                f"{p}-n10",
                "BOX 39.1 Whipple Triad",
                "Why Whipple triad must be documented before evaluating nondiabetic hypoglycemia",
                "Systematic evaluation for endogenous hyperinsulinism is recommended only when symptoms/signs, low reliable plasma glucose, and resolution after glucose raising are all documented.",
                ref(
                    "KEY POINTS",
                    "The decision to evaluate a given nondiabetic person systematically—seeking evidence of a metabolic disorder or an endogenous insulin excess during hypoglycemia—is recommended only for persons in whom Whipple triad (signs, symptoms, or both consistent with hypoglycemia; a low reliably measured plasma glucose concentration; and resolution of those symptoms or signs after the glucose concentrations is raised) can be documented.",
                ),
            ),
            note(
                f"{p}-n11",
                "Frequency of Hypoglycemia in Diabetes",
                "Why iatrogenic hypoglycemia limits glycemic targets in diabetes",
                "Therapeutic hyperinsulinemia from imperfect insulin or secretagogue therapy is the limiting factor in glycemic management and precludes lifelong normoglycemia despite vascular benefits.",
                ref(
                    "The Clinical Problem of Hypoglycemia in Diabetes",
                    "Iatrogenic hypoglycemia is the limiting factor in the glycemic management of diabetes with insulin, a sulfonylurea, or a glinide.",
                ),
            ),
            note(
                f"{p}-n12",
                "Clinical Definition and Classification of Hypoglycemia in Diabetes",
                "How the International Hypoglycaemia Study Group classifies iatrogenic hypoglycemia",
                "Level 1 alert <70 mg/dL, Level 2 serious <54 mg/dL, and Level 3 severe hypoglycemia requiring assistance—endorsed by ADA and EASD.",
                ref(
                    "Clinical Definition and Classification of Hypoglycemia in Diabetes",
                    "Level 1 is a glucose alert value less than 70 mg/dL (3.9 mmol/L), which is less than the physiologic lower limit",
                ),
            ),
            note(
                f"{p}-n13",
                "Treatment of Hypoglycemia in Diabetes",
                "How to treat most self-detected hypoglycemic episodes in diabetes",
                "Ingest 15–20 g fast-acting carbohydrate; clinical improvement expected in 15–20 minutes; avoid overtreatment; follow with snack/meal after symptomatic or serious episodes when hyperinsulinemia persists.",
                ref(
                    "Treatment of Hypoglycemia in Diabetes",
                    "A reasonable dose is 15 to 20 g of glucose.",
                ),
            ),
            note(
                f"{p}-n14",
                "Treatment of Hypoglycemia in Diabetes",
                "Why glucagon is indicated when oral carbohydrate is not possible",
                "Neuroglycopenic patients unable or unwilling to eat need glucagon (SC/IM or intranasal) administered by an associate; IV dextrose is standard when medical personnel are present.",
                ref(
                    "Treatment of Hypoglycemia in Diabetes",
                    "In a patient who is unable or unwilling (because of neuroglycopenia) to take carbohydrate orally, glucagon therapy is necessary.",
                ),
            ),
            note(
                f"{p}-n15",
                "Treatment of Hypoglycemia in Diabetes",
                "How glucagon dosing differs by route and body weight",
                "IM glucagon 0.5 mg if <25 kg and 1 mg if >25 kg; alternative 3 mg intranasal glucagon for age ≥4 years; dasiglucagon 0.6 mg SC pen for age ≥6 years.",
                ref(
                    "Treatment of Hypoglycemia in Diabetes",
                    "Intramuscular (IM) glucagon is given at a dose of 0.5 mg for children <25 kg and at 1 mg for patients >25 kg.",
                ),
            ),
            note(
                f"{p}-n16",
                "III or Medicated Individual",
                "Why drugs are the leading cause of hypoglycemia in ill adults",
                "Beyond insulin secretagogues and alcohol, many medications (e.g., quinine, pentamidine, gatifloxacin) cause hypoglycemia—often in hospitalized patients with renal failure.",
                ref(
                    "III or Medicated Individual",
                    "Drugs are the most common cause of hypoglycemia.",
                ),
            ),
            note(
                f"{p}-n17",
                "BOX 39.5 Drugs, Other Than Antihyperglycemic Agents and Alcohol, Reported to Cause Hypoglycemia",
                "How quinine and pentamidine can provoke hypoglycemia",
                "Endocrine Society guideline lists quinine and pentamidine among moderate-quality-evidence non-antihyperglycemic drugs associated with hypoglycemia.",
                ref(
                    "BOX 39.5 Drugs, Other Than Antihyperglycemic Agents and Alcohol, Reported to Cause Hypoglycemia",
                    "Quinine",
                ),
            ),
            note(
                f"{p}-n18",
                "III or Medicated Individual",
                "Why adrenal and pituitary hormone deficiency cause fasting hypoglycemia",
                "Cortisol supports gluconeogenesis; deficiency after caloric deprivation causes reduced glucose production with glycogen depletion—Addison disease should be considered in T1D with worsening hypoglycemia.",
                ref(
                    "III or Medicated Individual",
                    "Primary autoimmune adrenal insufficiency (Addison disease) should be considered in T1D presenting with worsening hypoglycemia and additional signs of primary adrenal insufficiency (hyperpigmentation, salt craving, orthostasis, hyponatremia).",
                ),
            ),
            note(
                f"{p}-n19",
                "III or Medicated Individual",
                "How non-islet cell tumor hypoglycemia (NICTH) produces hypoglycemia",
                "Large mesenchymal tumors overproduce pro-IGF2 that escapes binding proteins, exerts insulin-like actions, suppresses GH/IGF1, and appropriately suppresses endogenous insulin during hypoglycemia.",
                ref(
                    "III or Medicated Individual",
                    "NICTH is often the result of overproduction of incompletely processed pro–insulin-like growth factor 2 (pro-IGF2),",
                ),
            ),
            note(
                f"{p}-n20",
                "Seemingly Well Individual",
                "Why insulinoma classically presents with fasting neuroglycopenia",
                "Insulin-secreting β-cell tumors cause postabsorptive hypoglycemia with weight gain; incidence ~1 per 250,000 patient-years; surgical resection of benign lesions is usually curative.",
                ref(
                    "Seemingly Well Individual",
                    "Patients with an insulinoma typically present with a history of episodes of neuroglycopenia occurring in the postabsorptive (fasting) state.",
                ),
            ),
            note(
                f"{p}-n21",
                "Seemingly Well Individual",
                "How nesidioblastosis differs anatomically from insulinoma",
                "Diffuse islet hypertrophy/hyperplasia with enlarged β-cell nuclei causes fasting hyperinsulinemic hypoglycemia clinically indistinguishable from insulinoma but without a discrete tumor.",
                ref(
                    "Seemingly Well Individual",
                    "Some patients (4% of one series  $ ^{233} $) with fasting endogenous hyperinsulinemic hypoglycemia do not have an insulinoma but have diffuse islet involvement with islet hypertrophy, sometimes with hyperplasia, and enlarged and hyperchromatic  $ \\beta $-cell nuclei.",
                ),
            ),
            note(
                f"{p}-n22",
                "Seemingly Well Individual",
                "Why insulin autoimmune (Hirata) hypoglycemia occurs postprandially",
                "Meal-stimulated insulin binds anti-insulin antibodies then dissociates unregulatedly in the late postprandial period; very high insulin with insulin-to-C-peptide molar ratio >1 is a clue.",
                ref(
                    "Seemingly Well Individual",
                    "Hypoglycemia occurs in the late postprandial period as insulin, which is secreted in response to the meal, and then bound to the circulating antibody, spontaneously dissociates from the antibody in an unregulated fashion.",
                ),
            ),
            note(
                f"{p}-n23",
                "Seemingly Well Individual",
                "How factitious or surreptitious insulin is distinguished from insulinoma",
                "Elevated insulin without C-peptide or proinsulin during hypoglycemia supports exogenous insulin; oral secretagogue ingestion is distinguished by measurable sulfonylurea/glinide in circulation.",
                ref(
                    "Diagnostic Approach",
                    "Finding an elevated insulin level during hypoglycemia without elevation of C-peptide or proinsulin concentrations supports surreptitious or malicious administration of exogenous insulin, which may potentially be confirmed using an insulin-analogue specific immunoassay.",
                ),
            ),
            note(
                f"{p}-n24",
                "BOX 39.6",
                "How the prolonged supervised diagnostic fast is conducted",
                "Fast until Whipple triad or glucose <45 mg/dL with symptoms (or <55 mg/dL if prior documented triad); sample q6h until glucose <60 mg/dL then q1–2h; end at 72 h; obtain glucagon stimulation at termination.",
                ref(
                    "BOX 39.6",
                    "End the fast when the plasma glucose concentration is <45 mg/dL (<2.5 mmol/L) and the patient has symptoms and/or signs of hypoglycemia (or if 72 h have elapsed without symptoms).",
                ),
            ),
            note(
                f"{p}-n25",
                "BOX 39.7 Suggested Protocol for a Mixed-Meal Diagnostic Test",
                "How the mixed-meal test evaluates postprandial hypoglycemia",
                "After overnight fast, ingest symptom-provoking mixed meal; sample glucose, insulin, C-peptide every 30 min for 5 hours; apply fasting diagnostic criteria to low-glucose samples.",
                ref(
                    "BOX 39.7 Suggested Protocol for a Mixed-Meal Diagnostic Test",
                    "Collect samples for plasma glucose, insulin, and C-peptide before ingestion and every 30 min through 300 min after ingestion of the meal.",
                ),
            ),
            note(
                f"{p}-n26",
                "Intolerance of Fasting",
                "Why ketotic hypoglycemia of childhood is a diagnosis of exclusion",
                "Toddlers with limited fasting tolerance may develop overnight hypoglycemia with ketosis; syndrome typically ages 2–5 years and remits before age 10 after excluding GH deficiency, hypopituitarism, and glycogen synthase deficiency.",
                ref(
                    "Intolerance of Fasting",
                    "The syndrome of ketotic hypoglycemia of childhood typically occurs in 2- to 5-year-old children and remits spontaneously before age 10 years with a lower brain-to-body weight ratio.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Physiology of Glucose Counterregulation: Responses to Hypoglycemia",
                "A healthy adult develops falling plasma glucose during a hyperinsulinemic clamp. Which counterregulatory response occurs first at the highest glycemic threshold?",
                [
                    "Decrease in insulin secretion",
                    "Increase in glucagon secretion",
                    "Increase in epinephrine secretion",
                    "Carbohydrate ingestion prompted by symptoms",
                ],
                0,
                "↓ insulin (80–85 mg/dL) is the first defense, then ↑ glucagon (~70–75), then ↑ epinephrine (~65–70), then symptoms (~50–55).",
                ref(
                    "Physiology of Glucose Counterregulation: Responses to Hypoglycemia",
                    "The first physiologic defense against hypoglycemia is a decrease in insulin secretion by the pancreatic islet  $ \\beta $-cells.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Physiology of Glucose Counterregulation: Responses to Hypoglycemia",
                "When glucagon secretion is deficient, which hormone becomes critical as the third defense against hypoglycemia?",
                [
                    "Epinephrine",
                    "Cortisol alone",
                    "Growth hormone alone",
                    "Somatostatin",
                ],
                0,
                "Epinephrine-mediated hepatic/renal glucose production and reduced peripheral clearance become critical when glucagon is absent.",
                ref(
                    "Physiology of Glucose Counterregulation: Responses to Hypoglycemia",
                    "This becomes critical when glucagon is deficient.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Pathophysiology of Glucose Counterregulation in Diabetes",
                "A patient with long-standing T1D on basal-bolus insulin has recurrent severe hypoglycemia despite CGM. Best unifying pathophysiology?",
                [
                    "Therapeutic hyperinsulinemia with loss of insulin and glucagon responses plus attenuated epinephrine (HAAF)",
                    "Isolated growth hormone deficiency only",
                    "Excessive endogenous glucagon secretion during hypoglycemia",
                    "Primary adrenal Cushing syndrome",
                ],
                0,
                "Iatrogenic hypoglycemia in T1D reflects insulin excess plus defective counterregulation and impaired awareness from HAAF.",
                ref(
                    "Pathophysiology of Glucose Counterregulation in Diabetes",
                    "iatrogenic hypoglycemia is typically the result of the interplay of relative or mild to moderate absolute therapeutic hyperinsulinemia and compromised physiologic and behavioral defenses against falling plasma glucose concentrations",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                "A T1D patient with hypoglycemia unawareness asks about restoring symptoms. Evidence-based first step?",
                [
                    "At least 3 weeks of scrupulous hypoglycemia avoidance, often with temporarily higher glycemic targets",
                    "Immediate doubling of basal insulin dose",
                    "Routine β-blocker therapy to enhance adrenergic symptoms",
                    "Oral glucagon tablets before each meal",
                ],
                0,
                "Scrupulous avoidance of hypoglycemia for ≥3 weeks can reverse impaired awareness though epinephrine may remain blunted.",
                ref(
                    "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                    "3 or more weeks of scrupulous avoidance of hypoglycemia can reverse impaired awareness of hypoglycemia",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Frequency of Hypoglycemia in Diabetes",
                "Compared with T1D, hypoglycemia in insulin-treated T2D is generally:",
                [
                    "Less frequent early in insulin therapy but approaches T1D rates in advanced insulin-deficient T2D",
                    "Absent because endogenous insulin always compensates",
                    "More frequent from disease onset regardless of duration",
                    "Unrelated to β-cell failure",
                ],
                0,
                "T2D defenses are intact early but become compromised as patients approach absolute insulin deficiency.",
                ref(
                    "Frequency of Hypoglycemia in Diabetes",
                    "In T1D  $ \\beta $-cell failure and loss of both insulin and glucagon responses result in compromised defenses against hypoglycemia from disease onset,  $ ^{35} $ whereas in T2D defenses against hypoglycemia are intact early in the disease course but become compromised over time",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Clinical Definition and Classification of Hypoglycemia in Diabetes",
                "Per International Hypoglycaemia Study Group/ADA, a glucose of 52 mg/dL without symptoms in an insulin-treated patient is classified as:",
                [
                    "Level 2 serious hypoglycemia",
                    "Level 1 alert only (not Level 2)",
                    "Not hypoglycemia because asymptomatic",
                    "Pseudohypoglycemia by definition",
                ],
                0,
                "Level 2 is glucose <54 mg/dL whether or not symptoms are present; Level 1 is <70 mg/dL.",
                ref(
                    "Clinical Definition and Classification of Hypoglycemia in Diabetes",
                    "Level 2 is a glucose level less than 54 mg/dL (3.0 mmol/L), which is sufficiently low to indicate serious clinically important hypoglycemia.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "BOX 39.1 Whipple Triad",
                "A nondiabetic patient reports shakiness after meals but glucose was 92 mg/dL when symptomatic. Next step?",
                [
                    "Do not pursue systematic hypoglycemia evaluation—Whipple triad not documented",
                    "Proceed immediately to 72-hour fast",
                    "Start empiric diazoxide",
                    "Order insulinoma PET scan without biochemical testing",
                ],
                0,
                "Unequivocally normal glucose during symptoms argues against hypoglycemia; Whipple triad is required before systematic evaluation.",
                ref(
                    "Hypoglycemia in Persons Without Diabetes The Decision to Evaluate for Hypoglycemia",
                    "a reliably measured, unequivocally normal plasma glucose concentration (e.g., >70 mg/dL [3.9 mmol/L]) during a symptomatic episode provides strong evidence that the symptoms were not the result of hypoglycemia.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Treatment of Hypoglycemia in Diabetes",
                "A conscious T1D patient with glucose 58 mg/dL and mild symptoms can self-treat with:",
                [
                    "15–20 g fast-acting carbohydrate (e.g., glucose tablets)",
                    "1 mg IM glucagon as first-line therapy",
                    "25 g IV dextrose at home without IV access",
                    "High-fat meal only without carbohydrate",
                ],
                0,
                "Most episodes are self-treated with 15–20 g glucose with improvement expected in 15–20 minutes.",
                ref(
                    "Treatment of Hypoglycemia in Diabetes",
                    "Most episodes of symptomatic or asymptomatic hypoglycemia detected by self-monitoring or CGM are effectively self-treated by ingestion of glucose tablets, glucose gel, or other fast-acting carbohydrates.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Treatment of Hypoglycemia in Diabetes",
                "A 30-kg child with severe hypoglycemia and altered mental status needs emergency glucagon IM. Dose?",
                [
                    "0.5 mg IM glucagon",
                    "1 mg IM glucagon",
                    "3 mg intranasal glucagon only if age ≥4 years",
                    "0.03 mg/kg IV insulin",
                ],
                0,
                "IM glucagon 0.5 mg for children <25 kg; 1 mg for patients >25 kg.",
                ref(
                    "Treatment of Hypoglycemia in Diabetes",
                    "Intramuscular (IM) glucagon is given at a dose of 0.5 mg for children <25 kg and at 1 mg for patients >25 kg.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Treatment of Hypoglycemia in Diabetes",
                "Glucagon emergency therapy may be ineffective after which scenario?",
                [
                    "Alcohol binge with poor oral intake (glycogen depletion)",
                    "Missed breakfast in well-nourished adult",
                    "Post-exercise hypoglycemia with normal glycogen stores",
                    "Sulfonylurea overdose with adequate hepatic glycogen",
                ],
                0,
                "Glucagon stimulates glycogenolysis and is ineffective when glycogen is depleted (e.g., after alcohol binge).",
                ref(
                    "Treatment of Hypoglycemia in Diabetes",
                    "Because it acts by stimulating glycogenolysis, glucagon is ineffective in glycogen-depleted individuals (e.g., after a binge of alcohol ingestion).",
                ),
            ),
            mcq(
                f"{p}-m11",
                "III or Medicated Individual",
                "A hospitalized patient on quinine for malaria develops hypoglycemia. Mechanism category?",
                [
                    "Drug-induced hypoglycemia (non-antihyperglycemic agent)",
                    "Insulinoma until proven otherwise in all patients",
                    "Factitious insulin administration only",
                    "Physiologic postprandial reactive hypoglycemia",
                ],
                0,
                "Quinine is listed among drugs with moderate-quality evidence for causing hypoglycemia.",
                ref(
                    "BOX 39.5 Drugs, Other Than Antihyperglycemic Agents and Alcohol, Reported to Cause Hypoglycemia",
                    "Quinine",
                ),
            ),
            mcq(
                f"{p}-m12",
                "III or Medicated Individual",
                "A patient with metastatic fibrous tumor and fasting hypoglycemia has low insulin and low β-hydroxybutyrate. Most likely cause?",
                [
                    "Non-islet cell tumor hypoglycemia from pro-IGF2 overproduction",
                    "Insulinoma with inappropriately high insulin",
                    "Surreptitious sulfonylurea ingestion",
                    "Ketotic hypoglycemia of childhood",
                ],
                0,
                "NICTH from pro-IGF2 causes insulin-like hypoglycemia with appropriately suppressed endogenous insulin.",
                ref(
                    "III or Medicated Individual",
                    "Endogenous insulin secretion is suppressed appropriately during hypoglycemia in NICTH.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "III or Medicated Individual",
                "A T1D patient develops recurrent fasting hypoglycemia with hyperpigmentation and hyponatremia. Consider:",
                [
                    "Primary adrenal insufficiency (Addison disease)",
                    "Insulin autoimmune (Hirata) syndrome only",
                    "Post-gastric bypass hypoglycemia",
                    "GSD type VI as first diagnosis",
                ],
                0,
                "Addison disease should be considered in T1D with worsening hypoglycemia and signs of primary adrenal insufficiency.",
                ref(
                    "III or Medicated Individual",
                    "Primary autoimmune adrenal insufficiency (Addison disease) should be considered in T1D presenting with worsening hypoglycemia and additional signs of primary adrenal insufficiency (hyperpigmentation, salt craving, orthostasis, hyponatremia).",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Seemingly Well Individual",
                "During documented hypoglycemia (glucose 48 mg/dL), labs show insulin 8 μU/mL, C-peptide 0.1 nmol/L, proinsulin <5 pmol/L. Diagnosis?",
                [
                    "Exogenous (surreptitious) insulin administration",
                    "Insulinoma",
                    "Insulin autoimmune hypoglycemia",
                    "IGF-mediated non-islet cell tumor hypoglycemia",
                ],
                0,
                "Elevated insulin without C-peptide/proinsulin indicates exogenous insulin.",
                ref(
                    "Diagnostic Approach",
                    "Finding an elevated insulin level during hypoglycemia without elevation of C-peptide or proinsulin concentrations supports surreptitious or malicious administration of exogenous insulin",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Seemingly Well Individual",
                "A patient with fasting neuroglycopenia, weight gain, and inappropriately high insulin/C-peptide/proinsulin during hypoglycemia most likely has:",
                [
                    "Endogenous hyperinsulinism (e.g., insulinoma)",
                    "Addison disease with low insulin",
                    "Alcohol-induced hypoglycemia with ketosis",
                    "Isolated growth hormone deficiency without hyperinsulinism",
                ],
                0,
                "Insulinoma is prototypical endogenous hyperinsulinemic hypoglycemia with fasting neuroglycopenia and weight gain.",
                ref(
                    "Seemingly Well Individual",
                    "Insulinomas (insulin-secreting pancreatic  $ \\beta $-cell tumors) are the prototypical, but not the only, cause of endogenous hyperinsulinemic hypoglycemia.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Seemingly Well Individual",
                "Diffuse β-cell hyperplasia without discrete tumor causing fasting hyperinsulinemic hypoglycemia is termed:",
                [
                    "Nesidioblastosis (functional β-cell disorder)",
                    "Noninsulinoma pancreatogenous hypoglycemia (NIPHS) exclusively postprandial",
                    "Insulin autoimmune (Hirata) syndrome",
                    "Ketotic hypoglycemia of childhood",
                ],
                0,
                "Nesidioblastosis describes diffuse islet involvement with hypertrophy/hyperplasia mimicking insulinoma clinically.",
                ref(
                    "Seemingly Well Individual",
                    "This condition is often termed nesidioblastosis",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Seemingly Well Individual",
                "An Asian patient has late postprandial hypoglycemia with extremely high insulin and insulin-to-C-peptide ratio >1. Best diagnosis?",
                [
                    "Insulin autoimmune hypoglycemia (anti-insulin antibody)",
                    "Insulinoma with low insulin levels",
                    "Exogenous insulin without antibodies",
                    "Medium-chain acyl-CoA dehydrogenase deficiency",
                ],
                0,
                "Anti-insulin antibody causes late postprandial hypoglycemia with very high measured insulin and insulin/C-peptide ratio >1.",
                ref(
                    "Seemingly Well Individual",
                    "A clue to the diagnosis is the finding of very high measured plasma insulin levels during hypoglycemia with a molar ratio of insulin-to-C-peptide >1.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Diagnostic Approach",
                "Traditional Endocrine Society criteria during hypoglycemia (glucose <55 mg/dL) for endogenous hyperinsulinism include insulin:",
                [
                    "≥3 μU/mL with C-peptide ≥0.2 nmol/L and proinsulin ≥5 pmol/L",
                    "<3 μU/mL with elevated β-hydroxybutyrate",
                    "Any detectable level regardless of glucose",
                    "Suppressed with glucagon stimulation test increment <25 mg/dL",
                ],
                0,
                "Inappropriately elevated β-cell peptides at low glucose define endogenous hyperinsulinism per Table 39.4.",
                ref(
                    "Diagnostic Approach",
                    "plasma insulin concentrations equal to or greater than 3 μU/mL (18 pmol/L), plasma C-peptide concentrations of 0.6 ng/mL (0.2 nmol/L) or higher, and plasma proinsulin concentrations of 5.0 pmol/L or higher when plasma glucose concentrations are less than 55 ng/dL (3.0 mmol/L)",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Diagnostic Approach",
                "About what proportion of insulinoma patients meet diagnostic criteria within 24 hours of a supervised fast?",
                [
                    "Approximately two-thirds",
                    "Essentially none—72 hours required for all",
                    "100% within 6 hours",
                    "Less than 10%",
                ],
                0,
                "About two-thirds meet criteria in <24 h; most but not all within 48 h.",
                ref(
                    "Diagnostic Approach",
                    "About two-thirds of patients with an insulinoma meet the diagnostic criteria during a fast of less than 24 hours; most, but not all, do so in less than 48 hours.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "BOX 39.7 Suggested Protocol for a Mixed-Meal Diagnostic Test",
                "A patient has postprandial hypoglycemia symptoms 2–3 hours after meals. Best provocative test?",
                [
                    "Mixed-meal test with sampling every 30 minutes for 5 hours",
                    "Oral glucose tolerance test for reactive hypoglycemia without Whipple triad",
                    "Immediate total pancreatectomy",
                    "72-hour fast only regardless of symptom timing",
                ],
                0,
                "Mixed-meal test recreates postprandial symptoms; OGT without Whipple triad is discouraged for reactive symptoms.",
                ref(
                    "Clinical Classification of Hypoglycemic Disorders",
                    "The presence of postprandial symptoms without Whipple triad, previously called “reactive hypoglycemia,” is now considered a functional disorder in which symptoms are not due to hypoglycemia and for which oral glucose tolerance testing should not be performed.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Diagnosing Hypoglycemia in Infants and Children",
                "A neonate >48 hours old with documented hypoglycemia triggers further diagnostic testing at plasma glucose:",
                [
                    "≤60 mg/dL per Pediatric Endocrine Society guidance",
                    "≤40 mg/dL only in all ages",
                    ">100 mg/dL",
                    "Any value if asymptomatic without threshold",
                ],
                0,
                "PES suggests ≤50 mg/dL if <48 h old and ≤60 mg/dL after 48 hours of age.",
                ref(
                    "Diagnosing Hypoglycemia in Infants and Children",
                    "The PES suggests a plasma glucose concentration of 50 mg/dL (2.8 mmol/L) or lower as an appropriate threshold to trigger further diagnostic testing in a child less than 48 hours old and 60 mg/dL (3.3 mmol/L) or lower after 48 hours of age.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Intolerance of Fasting",
                "A 3-year-old develops morning hypoglycemia with ketosis after overnight fast, normal growth, and remitting course. Likely diagnosis after exclusion of other causes?",
                [
                    "Ketotic hypoglycemia of childhood",
                    "Insulinoma",
                    "GSD type 1a with hepatomegaly and lactic acidosis",
                    "Congenital hyperinsulinism requiring pancreatectomy",
                ],
                0,
                "Ketotic hypoglycemia typically affects 2–5 year-olds and remits before age 10.",
                ref(
                    "Intolerance of Fasting",
                    "The syndrome of ketotic hypoglycemia of childhood typically occurs in 2- to 5-year-old children and remits spontaneously before age 10 years",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Inborn Errors of Metabolism (Enzyme Deficiencies)",
                "GSD type 1a (glucose-6-phosphatase deficiency) is characterized by:",
                [
                    "Severe fasting hypoglycemia, hepatomegaly, lactic acidosis, and no glycemic response to glucagon",
                    "Postprandial hypoglycemia only with normal fasting glucose",
                    "Hypoketotic hypoglycemia with detectable insulin during fasting",
                    "Exercise-induced hypoglycemia responsive to diazoxide",
                ],
                0,
                "G6Pase deficiency blocks hepatic glucose release causing severe fasting hypoglycemia, hepatomegaly, and lactic acidosis.",
                ref(
                    "Inborn Errors of Metabolism (Enzyme Deficiencies)",
                    "absence of its activity results in low rates of endogenous glucose production and severe fasting hypoglycemia  $ ^{338} $ with no glycemic response to administered glucagon.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Inborn Errors of Metabolism (Enzyme Deficiencies)",
                "Before performing a diagnostic fast in an infant with hypoglycemia of unknown cause, essential safety step:",
                [
                    "Ensure normal acylcarnitine profile—fasting can cause coma in fatty acid oxidation defects",
                    "Start prophylactic insulin infusion",
                    "Obtain insulinoma PET scan first",
                    "Administer oral fructose challenge",
                ],
                0,
                "Normal acylcarnitine should be documented before diagnostic fast because coma can occur in FAOD.",
                ref(
                    "Diagnosing Hypoglycemia in Infants and Children",
                    "always ensure that acylcarnitine level is normal before performing a diagnostic fast because coma can occur during fasting in children with inborn errors of metabolism including defects in fatty acid oxidation.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Hyperinsulinism",
                "Congenital hyperinsulinism (CHI) affects approximately:",
                [
                    "1 in 30,000 to 50,000 live births (higher in consanguineous communities)",
                    "1 in 2 live births universally",
                    "Only adults after age 60",
                    "Every infant of a diabetic mother permanently",
                ],
                0,
                "CHI is the most common cause of non-transient neonatal hypoglycemia though overall rare.",
                ref(
                    "Hyperinsulinism",
                    "CHI is the most common cause of non-transient neonatal hypoglycemia, although it occurs in only 1 of every 30,000 to 50,000 live births.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Impact of Hypoglycemia in Diabetes",
                "Severe hypoglycemia mortality in diabetes is thought to often result from:",
                [
                    "Fatal cardiac arrhythmias triggered by sympathoadrenal response",
                    "Isolated chronic cognitive decline without acute events",
                    "Hyperkalemia from glucagon therapy",
                    "Hepatic glycogen overload",
                ],
                0,
                "Holter/CGM studies show arrhythmias during iatrogenic hypoglycemia; fatal arrhythmias likely underlie cardiovascular mortality.",
                ref(
                    "Impact of Hypoglycemia in Diabetes",
                    "Thus, fatal cardiac arrhythmias almost assuredly underlie hypoglycemic cardiovascular mortality in diabetes.",
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
                "Short-term treatment of hypoglycemia includes oral carbohydrates, parenteral glucagon or glucose, or intranasal glucagon.",
                True,
                "Key points list these acute therapies; long-term care requires correcting the underlying mechanism.",
                ref(
                    "KEY POINTS",
                    "Short-term treatment of hypoglycemia includes oral carbohydrates, parenteral glucagon or glucose, or intranasal glucagon; long-term treatment requires correction of the hypoglycemic mechanism.",
                ),
            ),
            tf(
                f"{p}-t2",
                "KEY POINTS",
                "Hypoglycemia-associated autonomic failure (HAAF) may be reversible through scrupulous avoidance of hypoglycemia.",
                True,
                "HAAF from antecedent hypoglycemia, sleep, or exercise may reverse with rigorous hypoglycemia avoidance.",
                ref(
                    "KEY POINTS",
                    "An attenuated sympathoadrenal response to falling glucose levels, the key feature of hypoglycemia-associated autonomic failure (HAAF), is induced by recent antecedent hypoglycemia, sleep, or prior exercise, and may be reversible through scrupulous avoidance of hypoglycemia.",
                ),
            ),
            tf(
                f"{p}-t3",
                "KEY POINTS",
                "Iatrogenic hypoglycemia is associated with morbidity but not mortality in type 1 and type 2 diabetes.",
                False,
                "Key points state iatrogenic hypoglycemia is associated with both morbidity and mortality in T1D and T2D.",
                ref(
                    "KEY POINTS",
                    "Iatrogenic hypoglycemia is associated with both morbidity and mortality in type 1 and type 2 diabetes mellitus.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Physiology of Glucose Counterregulation: Responses to Hypoglycemia",
                "The behavioral defense against hypoglycemia—carbohydrate ingestion—is prompted largely by autonomic (neurogenic) symptoms.",
                True,
                "Symptoms, largely sympathetic neural in origin, are the last defense prompting food ingestion.",
                ref(
                    "Physiology of Glucose Counterregulation: Responses to Hypoglycemia",
                    "The behavioral defense is carbohydrate ingestion prompted by autonomic symptoms that are largely sympathetic neural in origin",
                ),
            ),
            tf(
                f"{p}-t5",
                "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                "HAAF is identical to classic diabetic autonomic neuropathy and shares the same irreversible pathogenesis.",
                False,
                "HAAF is a functional autonomic failure distinct from classic diabetic autonomic neuropathy.",
                ref(
                    "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                    "Notably, HAAF is a functional form of autonomic failure, distinct from classic diabetic autonomic neuropathy.",
                ),
            ),
            tf(
                f"{p}-t6",
                "BOX 39.1 Whipple Triad",
                "A plasma glucose concentration less than 55 mg/dL (3.0 mmol/L) is considered unequivocally low for Whipple triad documentation.",
                True,
                "Box 39.1 defines 'low' judgmentally but <55 mg/dL is unequivocally low.",
                ref(
                    "BOX 39.1 Whipple Triad",
                    "The definition of “low” is judgmental, but a plasma glucose concentration of less than 55 mg/dL (3.0 mmol/L) is unequivocally low.",
                ),
            ),
            tf(
                f"{p}-t7",
                "III or Medicated Individual",
                "Ethanol inhibits gluconeogenesis and clinical alcohol-induced hypoglycemia typically follows a binge with poor food intake.",
                True,
                "Alcohol hypoglycemia occurs with glycogen depletion after binge drinking and little food.",
                ref(
                    "III or Medicated Individual",
                    "Ethanol inhibits gluconeogenesis. Clinical alcohol-induced hypoglycemia typically follows a binge of alcohol consumption during which the person eats little food (i.e., in the setting of glycogen depletion).",
                ),
            ),
            tf(
                f"{p}-t8",
                "III or Medicated Individual",
                "Isolated growth hormone deficiency commonly causes hypoglycemia in adults.",
                False,
                "Cortisol deficiency can cause hypoglycemia especially in children; isolated GH deficiency does not cause hypoglycemia in adults.",
                ref(
                    "III or Medicated Individual",
                    "isolated growth hormone deficiency does not cause hypoglycemia in adults.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Seemingly Well Individual",
                "Insulinoma incidence is approximately 1 in 250,000 patient-years.",
                True,
                "Insulinomas are rare with reported incidence 1 per 250,000 patient-years.",
                ref(
                    "Seemingly Well Individual",
                    "Insulinomas are rare; an incidence of 1 in 250,000 patient-years has been reported.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Seemingly Well Individual",
                "Surgical resection of a benign insulinoma is typically curative.",
                True,
                "Benign insulinoma resection is usually curative with excellent long-term survival.",
                ref(
                    "Seemingly Well Individual",
                    "Surgical resection of a benign insulinoma is typically curative, and long-term survival is the rule after successful operation.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Diagnostic Approach",
                "A supervised diagnostic fast should be ended based solely on a low point-of-care glucose without laboratory confirmation.",
                False,
                "Decisions to end the fast require laboratory-measured plasma glucose, not point-of-care monitors alone.",
                ref(
                    "BOX 39.6",
                    "The decision to end the fast should be based on laboratory-measured plasma glucose concentrations, not those estimated with a point-of-care blood glucose monitor.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Inborn Errors of Metabolism (Enzyme Deficiencies)",
                "Medium-chain acyl-CoA dehydrogenase (MCAD) deficiency is among the most common fatty acid oxidation disorders causing hypoketonemic hypoglycemia.",
                True,
                "MCAD deficiency is the most common FAOD presenting with hypoketonemic hypoglycemia during fasting stress.",
                ref(
                    "Inborn Errors of Metabolism (Enzyme Deficiencies)",
                    "The most common is medium-chain acyl-CoA dehydrogenase deficiency.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Diagnosing Hypoglycemia in Infants and Children",
                "For children with persistent hypoglycemia disorders, treatment goal is to maintain plasma glucose above 70 mg/dL (3.9 mmol/L).",
                True,
                "After 48 hours, postabsorptive glucose in children aligns with adults; persistent disorders target >70 mg/dL.",
                ref(
                    "Diagnosing Hypoglycemia in Infants and Children",
                    "in children with the diagnosis of a disorder causing persistent hypoglycemia or a known risk of a persistent hypoglycemic disorder, the goal of treatment is to maintain a plasma glucose concentration above 70 mg/dL (3.9 mmol/L).",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Pathophysiology of Glucose Counterregulation in Diabetes",
                "Assertion: Patients with T1D lose the glucagon response to hypoglycemia.",
                "Reason: T1D patients have absent α-cells and cannot secrete glucagon.",
                2,
                "Assertion true—glucagon does not rise during hypoglycemia; reason false—functional α-cells are present but fail to respond due to β-cell failure/loss of intraislet insulin signal.",
                ref(
                    "Pathophysiology of Glucose Counterregulation in Diabetes",
                    "despite the presence of functional  $ \\alpha $-cells, there is no increase in glucagon secretion",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Pathophysiology of Glucose Counterregulation in Diabetes",
                "Assertion: Impaired awareness of hypoglycemia increases severe hypoglycemia risk in T1D.",
                "Reason: Impaired awareness enhances sympathoadrenal responses to falling glucose.",
                2,
                "Assertion true—sixfold (up to 20-fold with unawareness) increased severe hypoglycemia risk; reason false—awareness loss reflects attenuated, not enhanced, sympathoadrenal responses.",
                ref(
                    "Pathophysiology of Glucose Counterregulation in Diabetes",
                    "impaired awareness of hypoglycemia (see Fig. 39.5),  $ ^{1,2} $ which is associated with a sixfold increase of severe iatrogenic hypoglycemia",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                "Assertion: Recent antecedent hypoglycemia can cause HAAF.",
                "Reason: Antecedent hypoglycemia permanently destroys all adrenal chromaffin cells.",
                2,
                "Assertion true—antecedent hypoglycemia attenuates subsequent sympathoadrenal responses; reason false—HAAF is functional/reversible, not irreversible adrenal destruction.",
                ref(
                    "Hypoglycemia-Associated Autonomic Failure in Diabetes",
                    "Recent antecedent hypoglycemia, even asymptomatic nocturnal hypoglycemia, reduces epinephrine and autonomic symptom responses to a given level of subsequent hypoglycemia",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Frequency of Hypoglycemia in Diabetes",
                "Assertion: Most episodes of severe iatrogenic hypoglycemia occur in persons with T2D.",
                "Reason: T2D is approximately 20-fold more prevalent than T1D and most T2D patients ultimately require insulin.",
                0,
                "Both true—population data suggest most iatrogenic hypoglycemia, including severe episodes, occurs in T2D given prevalence and insulin use.",
                ref(
                    "Frequency of Hypoglycemia in Diabetes",
                    "data suggest most episodes of iatrogenic hypoglycemia, including severe hypoglycemia, occur in persons with T2D.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "BOX 39.1 Whipple Triad",
                "Assertion: Whipple triad should be documented before systematic evaluation for hypoglycemia in nondiabetic patients.",
                "Reason: Hypoglycemic disorders are common in persons without diabetes.",
                2,
                "Assertion true per guideline; reason false—hypoglycemia is distinctly uncommon without diabetes, making Whipple triad documentation essential.",
                ref(
                    "Hypoglycemia in Persons Without Diabetes The Decision to Evaluate for Hypoglycemia",
                    "hypoglycemia is a distinctly uncommon clinical event in persons who do not have diabetes",
                ),
            ),
            ar(
                f"{p}-ar6",
                "III or Medicated Individual",
                "Assertion: Pentamidine can cause hypoglycemia.",
                "Reason: Pentamidine is not listed among drugs reported to cause hypoglycemia.",
                2,
                "Assertion true—pentamidine is in Box 39.5 moderate-evidence list; reason false.",
                ref(
                    "BOX 39.5 Drugs, Other Than Antihyperglycemic Agents and Alcohol, Reported to Cause Hypoglycemia",
                    "Pentamidine",
                ),
            ),
            ar(
                f"{p}-ar7",
                "III or Medicated Individual",
                "Assertion: Non-islet cell tumor hypoglycemia can result from pro-IGF2 overproduction.",
                "Reason: NICTH always presents with inappropriately elevated insulin secretion during hypoglycemia.",
                2,
                "Assertion true—pro-IGF2 mediates many NICTH cases; reason false—endogenous insulin is appropriately suppressed.",
                ref(
                    "III or Medicated Individual",
                    "Endogenous insulin secretion is suppressed appropriately during hypoglycemia in NICTH.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Seemingly Well Individual",
                "Assertion: Surreptitious insulin administration can mimic insulinoma biochemically.",
                "Reason: Surreptitious insulin elevates C-peptide and proinsulin during hypoglycemia.",
                2,
                "Assertion true—clinical presentation can overlap; reason false—exogenous insulin shows high insulin with suppressed C-peptide/proinsulin.",
                ref(
                    "Seemingly Well Individual",
                    "Malicious hypoglycemia  $ ^{224,225} $ can be accomplished by administration of insulin or an insulin secretagogue.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Diagnostic Approach",
                "Assertion: A 72-hour supervised fast can diagnose insulinoma when spontaneous hypoglycemia has not been captured.",
                "Reason: No insulinoma patient ever meets criteria before 72 hours of fasting.",
                2,
                "Assertion true—prolonged fast is standard when spontaneous samples unavailable; reason false—~two-thirds meet criteria within 24 hours.",
                ref(
                    "Diagnostic Approach",
                    "About two-thirds of patients with an insulinoma meet the diagnostic criteria during a fast of less than 24 hours",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Treatment of Hypoglycemia in Diabetes",
                "Assertion: IV dextrose is standard parenteral therapy for severe hypoglycemia in medical settings.",
                "Reason: IV glucose provides a sustained correction without need for follow-up infusion when hyperinsulinemia is present.",
                2,
                "Assertion true—IV dextrose is standard; reason false—IV glucose response is transient with ongoing hyperinsulinemia and often requires continued infusion/feeding.",
                ref(
                    "Treatment of Hypoglycemia in Diabetes",
                    "The glycemic response to IV glucose is transient in the setting of ongoing hyperinsulinemia.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Hyperinsulinism",
                "Assertion: Infants of diabetic mothers commonly develop neonatal hypoglycemia from transient hyperinsulinism.",
                "Reason: Fetal hyperinsulinemia resolves immediately at birth with normal insulin suppression as glucose falls.",
                2,
                "Assertion true—chronic in utero hyperglycemia stimulates fetal insulin; reason false—insulin fails to fall normally after birth causing transient neonatal hypoglycemia.",
                ref(
                    "Hyperinsulinism",
                    "shortly after birth there is failure of insulin to fall normally as glucose levels decline and transient",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Inborn Errors of Metabolism (Enzyme Deficiencies)",
                "Assertion: GSD type 1a causes severe fasting hypoglycemia.",
                "Reason: Glucose-6-phosphatase deficiency increases hepatic glucose release during fasting.",
                2,
                "Assertion true—severe fasting hypoglycemia with no glucagon response; reason false—absence of G6Pase blocks hepatic glucose release from glycogenolysis/gluconeogenesis.",
                ref(
                    "Inborn Errors of Metabolism (Enzyme Deficiencies)",
                    "Given that glucose-6-phosphatase is the final enzyme in the hepatic release of glucose from gluconeogenic and glycogenolytic pathways, absence of its activity results in low rates of endogenous glucose production and severe fasting hypoglycemia",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "39",
        "title": "Hypoglycemia",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Ana María Arbeláez and Michael R. Rickels",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_39_Hypoglycemia.md",
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
