#!/usr/bin/env python3
"""Generate Williams 15e module w15-35 — Type 1 Diabetes Mellitus."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-35"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-35_Type_1_Diabetes_Mellitus.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why T1D is defined by autoimmune β-cell destruction",
                "T1D results from islet dysfunction and chronic autoimmune destruction of insulin-producing pancreatic β-cells, with rising worldwide incidence and MHC-driven polygenic susceptibility.",
                ref(
                    "KEY POINTS",
                    "Type 1 diabetes mellitus (T1D) is a disorder resulting from islet dysfunction and chronic autoimmune destruction of the insulin-producing pancreatic  $ \\beta $-cells.",
                ),
            ),
            note(
                f"{p}-n2",
                "Natural History of Type 1 Diabetes",
                "How insulitis links histology to autoimmune pathogenesis",
                "Martin Schmidt's peri-islet infiltrate, termed insulitis, together with islet autoantibodies and MHC susceptibility, formed three lines of evidence for autoimmune T1D.",
                ref(
                    "Introduction",
                    "The term used to define this pancreatic feature, insulitis, was coined in 1940 by yet another pathologist, Hanns von Meyenburg.",
                ),
            ),
            note(
                f"{p}-n3",
                "Natural History of Type 1 Diabetes",
                "Why symptoms appear only after massive β-cell loss",
                "In the Eisenbarth model, classical symptoms emerge when 85–90% of β-cells are destroyed; the autoimmune process then ends with complete β-cell elimination.",
                ref(
                    "Natural History of Type 1 Diabetes",
                    "Symptoms of the disease were thought to appear when 85% to 90% of pancreatic  $ \\beta $-cells had met their demise.",
                ),
            ),
            note(
                f"{p}-n4",
                "Epidemiology",
                "How Finland exemplifies rising T1D incidence",
                "Finland has the highest known childhood T1D incidence—approaching 60 per 100,000—with almost fivefold increase since the 1950s and doubling every 10–15 years in many Western countries.",
                ref(
                    "Disease Incidence and Prevalence",
                    "Finland now has an annual incidence approaching 60 per 100,000 children.",
                ),
            ),
            note(
                f"{p}-n5",
                "Epidemiology",
                "Why most new T1D cases lack a affected first-degree relative",
                "Despite 15-fold higher risk in first-degree relatives versus the general population, >85% of incident T1D occurs without a family history—partly because ~40% of the population carries high-risk HLA alleles.",
                ref(
                    "Disease Incidence and Prevalence",
                    "it is important to realize that most persons (>85%) in whom T1D develops do not have a first-degree relative with the disease.",
                ),
            ),
            note(
                f"{p}-n6",
                "Stages in the Natural History of Type 1 Diabetes",
                "How ADA/JDRF staging defines pre-symptomatic T1D",
                "Stage 1: ≥2 islet autoantibodies with normoglycemia; stage 2: dysglycemia with ≥2 autoantibodies; stage 3: ADA diagnostic diabetes.",
                ref(
                    "Stages in the Natural History of Type 1 Diabetes",
                    "Stage 1 is defined by the presence of two or more anti-islet autoantibodies with normoglycemia (normal glucose tolerance on 2-hour oral glucose tolerance test [OGTT]).",
                ),
            ),
            note(
                f"{p}-n7",
                "Type 1 Diabetes Progression From Asymptomatic to Diagnosis",
                "Why two or more autoantibodies predict progression",
                "Once two or more anti-islet autoantibodies are present, 10-year diabetes risk ranges from 60% in older seroconverters to 75% in those seroconverting before age 3.",
                ref(
                    "Type 1 Diabetes Progression From Asymptomatic to Diagnosis",
                    "once two or more anti-islet autoantibodies are present in a given individual, the individual's 10-year risk for developing diabetes ranges from 60% in older seroconverters (>3 years) to 75% in those who seroconvert before 3 years of age.",
                ),
            ),
            note(
                f"{p}-n8",
                "Histopathology",
                "How insulitis immunotype differs by age at onset",
                "Younger-onset T1D shows more inflamed islets, fewer residual β-cell islets, and higher CD8⁺ T-cell and CD20⁺ B-cell infiltrates than older-onset disease.",
                ref(
                    "Histopathology",
                    "patients with T1D with a disease onset at age 0 to 14 years and within 1 year of diagnosis show more inflamed islets (68%) and fewer islets with residual  $ \\beta $-cells (39%) than in patients with onset at 15 to 39 years of age.",
                ),
            ),
            note(
                f"{p}-n9",
                "The Major Histocompatibility Complex",
                "Why HLA-DR/DQ haplotypes dominate T1D susceptibility",
                "More than half of genetic susceptibility resides in the MHC; DR3-DQ2/DR4-DQ8 heterozygosity confers highest risk, while DQA1*01:02-DQB1*06:02 (DQ6) provides dominant protection.",
                ref(
                    "KEY POINTS",
                    "More than half of genetic disease susceptibility for T1D is provided by the major histocompatibility complex (MHC), yet the disorder is clearly polygenic",
                ),
            ),
            note(
                f"{p}-n10",
                "Genetic Risk Scores",
                "How polygenic risk scores improve T1D prediction",
                "GRS models combining HLA and non-HLA alleles discriminate T1D from T2D/MODY, predict progression, and—when combined with autoantibodies and family history—outperform autoantibodies alone in young children.",
                ref(
                    "Genetic Risk Scores",
                    "a combined risk score, which includes GRS2, islet autoantibody status, and family history of T1D, provides marked improvement on autoantibodies alone for the prediction of T1D in young children.",
                ),
            ),
            note(
                f"{p}-n11",
                "Autoantibodies",
                "Why IAA, GADA, IA-2A, and ZnT8A distinguish T1D",
                "These four islet autoantibodies are positive in ~90% of White children at presentation and in <1–2% of unaffected individuals, though prevalence varies by ethnicity and wanes over time.",
                ref(
                    "Autoantibodies",
                    "anti-insulin [IA], anti-glutamic acid decarboxylase [GADA], anti-insulinoma-associated antigen 2 [IA2A], or anti-zinc-transporter 8 [ZnT8A]).",
                ),
            ),
            note(
                f"{p}-n12",
                "Environmental Factors",
                "Why environmental change is implicated in rising T1D",
                "The fivefold increase in T1D rates over the past half century suggests changing environmental factors—either increased causative exposures or decreased protective ones.",
                ref(
                    "Environmental Factors",
                    "The fivefold increase in T1D rates over the past half century has been considered strong evidence that environmental factors related to diabetes risk have changed since the 1960s.",
                ),
            ),
            note(
                f"{p}-n13",
                "Infection",
                "How enteroviral infection may influence islet autoimmunity",
                "TEDDY data show prolonged—but not short-duration—enteroviral shedding associates with islet autoimmunity in genetically at-risk children, supporting a role for persistent infection in some cases.",
                ref(
                    "Infection",
                    "Longitudinal data collected through the TEDDY study demonstrate that prolonged, but not short-duration, enteroviral shedding is associated with islet autoimmunity in genetically at-risk children",
                ),
            ),
            note(
                f"{p}-n14",
                "Vaccines",
                "Why childhood vaccines do not cause T1D",
                "Multiple studies found no evidence that childhood vaccination timing influences T1D development—an important public-health reassurance against vaccine hesitancy.",
                ref(
                    "Vaccines",
                    "none has provided any evidence that childhood vaccinations influence the development of diabetes.",
                ),
            ),
            note(
                f"{p}-n15",
                "Diagnosis",
                "How stage 3 T1D is diagnosed clinically",
                "At symptomatic onset, diagnosis relies on insulin requirement for hyperglycemia control, low C-peptide, and β-cell-directed autoantibodies after substantial β-cell destruction.",
                ref(
                    "Diagnosis",
                    "During the latter stage, the clinical diagnosis of T1D relies mainly on the need for insulin to control hyperglycemia, low C-peptide levels, and presence of  $ \\beta $-cell-directed autoantibodies.",
                ),
            ),
            note(
                f"{p}-n16",
                "Type 2 Diabetes",
                "Why adult-onset T1D is frequently misclassified as T2D",
                "An estimated 5–15% of adults diagnosed with T2D may have T1D; misdiagnosis leads to higher HbA1c, DKA risk on noninsulin therapy, and accelerated complications.",
                ref(
                    "Type 2 Diabetes",
                    "it is conceivable that 5% to 15% of adults diagnosed with T2D may have T1D, given the frequency of T1D-associated autoantibodies in populations diagnosed with T2D.",
                ),
            ),
            note(
                f"{p}-n17",
                "Monogenetic Forms of Diabetes",
                "How MODY differs from autoimmune T1D therapeutically",
                "Monogenic diabetes accounts for 1–5% of youth diabetes; correct genetic diagnosis enables oral therapy in some forms versus mandatory insulin in classic T1D.",
                ref(
                    "Monogenetic Forms of Diabetes",
                    "Monogenic forms of diabetes account for about 1% to 5% of all cases of diabetes in young individuals.",
                ),
            ),
            note(
                f"{p}-n18",
                "Chronic Complications of Type 1 Diabetes",
                "Why tight glycemic control prevents microvascular complications",
                "T1D complications include retinopathy, nephropathy, neuropathy, and cardiovascular disease; tight glycemic control with multifactorial risk management reduces these risks.",
                ref(
                    "Chronic Complications of Type 1 Diabetes",
                    "Tight glycemic control has been shown to prevent or delay the onset of microvascular complications, and a multifactorial approach, including tight glycemic control and lipid and blood pressure management, reduces the risk of cardiovascular disease in those living with T1D.",
                ),
            ),
            note(
                f"{p}-n19",
                "Principles of Type 1 Diabetes Management",
                "How multidisciplinary teams center the person with T1D",
                "T1D care integrates insulin replacement mimicking physiologic profiles, glucose monitoring, nutrition, exercise, and DSMES—with the patient as integral manager supported by educators, dietitians, and mental health professionals.",
                ref(
                    "Principles of Type 1 Diabetes Management",
                    "Care for people with T1D builds on integrated approaches by multidisciplinary teams, where structured diabetes education, provided by certified educators, elevates the person living with T1D to an integral member of the disease management team.",
                ),
            ),
            note(
                f"{p}-n20",
                "Insulin Therapy",
                "Why basal-bolus therapy is standard intensive care",
                "DCCT-established intensive therapy uses MDI basal-bolus or CSII with rapid-acting meal boluses and basal insulin—about 50% of TDD as basal and 50% as boluses at initiation.",
                ref(
                    "Insulin Therapy",
                    "intensive insulin therapy has become the standard of care for treatment of T1D and can be achieved with multiple daily injections (MDIs) basabolus therapy or insulin pump therapy.",
                ),
            ),
            note(
                f"{p}-n21",
                "Principles of Insulin Pump Use",
                "How hybrid closed-loop systems reduce hypoglycemia",
                "CSII integrated with CGM and control algorithms suspends or adjusts basal insulin from sensor glucose and trends—approaching an artificial pancreas and lowering severe hypoglycemia across age groups.",
                ref(
                    "Principles of Insulin Pump Use",
                    "The largest advantage of pump technology is the availability of smarter devices that integrate CGM functionality, as well as algorithms that enable insulin suspension based on a fixed threshold or predictive design, to minimize hypoglycemia and improve glycemic outcomes.",
                ),
            ),
            note(
                f"{p}-n22",
                "Nutrition Therapy",
                "How carbohydrate counting guides prandial insulin",
                "Carbohydrate counting allows flexible meals and insulin dosing; consistency matters more than exactitude—±5–7 g (≈15%) errors rarely cause major hypo/hyperglycemia.",
                ref(
                    "Nutrition Therapy",
                    "So-called carbohydrate counting can provide flexible diet management by allowing for a wide range of food choices.",
                ),
            ),
            note(
                f"{p}-n23",
                "Physical Activity and Exercise",
                "Why exercise causes both hypo- and hyperglycemia in T1D",
                "Exogenous insulin cannot be acutely reduced like endogenous secretion—promoting exercise hypoglycemia—while intense anaerobic activity with insufficient circulating insulin can raise glucose via counterregulatory hormones.",
                ref(
                    "Physical Activity and Exercise",
                    "In T1D, it is not possible to reduce insulin production after the administration of an insulin dose; therefore, the circulating insulin can lead to hypoglycemia by both inhibiting hepatic glucose production and promoting exercise-related glucose uptake.",
                ),
            ),
            note(
                f"{p}-n24",
                "Continuous Glucose Monitoring",
                "How CGM improves time-in-range and hypoglycemia safety",
                "CGM with alerts improves TIR, reduces hypoglycemia, and supports meal bolus titration; consensus targets ~70% TIR (70–180 mg/dL) with <4% time below range.",
                ref(
                    "Continuous Glucose Monitoring",
                    "CGM is increasingly used for routine diabetes care in adults, children, and adolescents with T1D.",
                ),
            ),
            note(
                f"{p}-n25",
                "Hypoglycemia",
                "Why glucagon is used for unconscious hypoglycemia",
                "Conscious hypoglycemia is treated with 15 g oral glucose; loss of consciousness requires IV glucose or parenteral glucagon, with soluble and intranasal glucagon now available.",
                ref(
                    "Hypoglycemia",
                    "In cases of loss of consciousness, intravenous (IV) glucose or parenteral glucagon should be administered.",
                ),
            ),
            note(
                f"{p}-n26",
                "Prevention and Reversal of Type 1 Diabetes",
                "How teplizumab delays stage 3 T1D in TrialNet",
                "A short course of anti-CD3 teplizumab delayed clinical T1D by ~3 years in high-risk autoantibody-positive individuals; FDA approved it in 2022 as the first disease-modifying T1D therapy.",
                ref(
                    "Immunosuppression $ ^{39} $",
                    "a recent study demonstrated that a short course of the anti-CD3 monoclonal antibody teplizumab delayed progression to clinical T1D by approximately 3 years in high-risk patients.",
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
                "A 6-year-old in Finland is evaluated after a sibling developed T1D. Which epidemiologic statement is most accurate?",
                [
                    "Finland has among the highest childhood T1D incidence worldwide",
                    "T1D incidence in Finland has fallen fivefold since the 1950s",
                    "Sibling risk is lower than general population risk",
                    "Monozygotic twin concordance is negligible",
                ],
                0,
                "Finland has annual incidence approaching 60/100,000 children with marked secular increase; sibling and twin risks far exceed population risk.",
                ref(
                    "Disease Incidence and Prevalence",
                    "The highest known incidence of T1D is observed in Finland and Sardinia.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Epidemiology",
                "Using Table 35.1, what is approximate lifetime T1D risk for a monozygotic twin of a T1D patient?",
                [
                    "About 50%, varying with index twin age",
                    "About 3.2% through adolescence only",
                    "About 0.3% like the general population",
                    "About 10% when both parents have T1D",
                ],
                0,
                "Monozygotic twin concordance exceeds 50% with long follow-up; dizygotic twins ~6%, siblings 6% lifetime.",
                ref(
                    "Twin Studies",
                    "With long-term follow-up, the overall rate of concordance for monozygotic twins exceeds 50%.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Stages in the Natural History of Type 1 Diabetes",
                "A 4-year-old has two islet autoantibodies and normal OGTT. Current T1D stage?",
                [
                    "Stage 1",
                    "Stage 2",
                    "Stage 3",
                    "No staging applies without symptoms",
                ],
                0,
                "Stage 1 = ≥2 autoantibodies with normoglycemia; stage 2 adds dysglycemia; stage 3 meets ADA diabetes criteria.",
                ref(
                    "Stages in the Natural History of Type 1 Diabetes",
                    "Stage 1 is defined by the presence of two or more anti-islet autoantibodies with normoglycemia",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Autoantibodies",
                "Which autoantibody pattern best predicts T1D in a child under 5 years?",
                [
                    "High-level IAA, often appearing first",
                    "Isolated GADA without other antibodies",
                    "ZnT8A alone in all ethnic groups",
                    "Negative all four antibodies confirms T1D",
                ],
                0,
                "IAA is the best single marker in young children; GADA predominates in adult-onset T1D; rapid progression requires IAA plus another antibody.",
                ref(
                    "Autoantibodies",
                    "The high levels and frequent positivity of IAA make measurement of these autoantibodies the best single marker for diabetes development in young children.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "The Major Histocompatibility Complex",
                "Which HLA genotype confers strongest protection from T1D in the general population?",
                [
                    "DQA1*01:02-DQB1*06:02 (DQ6)",
                    "DR3-DQ2 with DR4-DQ8 heterozygosity",
                    "HLA-DRB1*04:05 alone",
                    "Absence of any DR or DQ typing",
                ],
                0,
                "DQ6 (DQA1*01:02-DQB1*06:02) provides dominant protection, present in ~20% of the population but <3% of T1D patients.",
                ref(
                    "The Major Histocompatibility Complex",
                    "A common DQ molecule, HLA-DQA1*01:02-DQB1*06:02, provides dominant protection from T1D and is termed DQ6.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Genetic Risk Scores",
                "A research cohort uses GRS2 plus autoantibodies. Primary advantage over autoantibodies alone?",
                [
                    "Improved prediction of T1D in young children",
                    "Eliminates need for OGTT entirely",
                    "Replaces insulin therapy decisions at diagnosis",
                    "Diagnoses MODY without genetic testing",
                ],
                0,
                "Combined GRS2, autoantibody status, and family history markedly improves prediction versus autoantibodies alone.",
                ref(
                    "Genetic Risk Scores",
                    "a combined risk score, which includes GRS2, islet autoantibody status, and family history of T1D, provides marked improvement on autoantibodies alone for the prediction of T1D in young children.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Infection",
                "Regarding environmental triggers, which statement has the strongest evidence?",
                [
                    "Congenital rubella greatly increases T1D risk",
                    "Routine childhood vaccines increase T1D incidence",
                    "All enterovirus infections at diagnosis prove causation",
                    "COVID-19 has definitively been shown to cause T1D via direct β-cell infection only",
                ],
                0,
                "Congenital (not postnatal) rubella has strong evidence; vaccines do not cause T1D; enterovirus and COVID associations remain complex and partly controversial.",
                ref(
                    "Infection",
                    "The best evidence, if not the only strong evidence, for a specific environmental agent to contribute to T1D pathogenesis involves congenital rubella infection, which, in contrast to noncongenital infection, greatly increases risk for development of T1D.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Diagnosis",
                "A teenager presents with polyuria, weight loss, glucose 420 mg/dL, and GADA positivity. Best classification?",
                [
                    "Stage 3 type 1 diabetes mellitus",
                    "Stage 1 presymptomatic T1D only",
                    "Type 2 diabetes until age 18",
                    "MODY without further testing",
                ],
                0,
                "Symptomatic hyperglycemia meeting ADA criteria with insulin need, low C-peptide, and autoantibodies defines stage 3 T1D.",
                ref(
                    "Diagnosis",
                    "Most patients present during stage 3, the classical definition of T1D onset, when significant  $ \\beta $-cell destruction has taken place to afford symptomatic disease.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Symptoms",
                "A 12-year-old develops polyuria and polydipsia over 2 weeks with DKA. How common is DKA at pediatric T1D diagnosis?",
                [
                    "Occurs in about one-third of children at diagnosis",
                    "Occurs in fewer than 1% at diagnosis",
                    "Never occurs with autoimmune T1D",
                    "Only occurs in established T1D, not at onset",
                ],
                0,
                "DKA accompanies onset in roughly one-third of children; overall new-onset DKA rates vary 15–70% by country.",
                ref(
                    "Symptoms",
                    "If onset of T1D is associated with DKA (discussed later in the chapter), which occurs in a third of children at diagnosis",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Type 2 Diabetes",
                "A 35-year-old with BMI 32, mild hyperglycemia, and GADA positivity was started on metformin and later developed DKA. Most likely error?",
                [
                    "Misclassification of autoimmune T1D as T2D",
                    "Metformin always causes DKA in any diabetes",
                    "GADA positivity excludes insulin requirement",
                    "Adult diabetes is always T2D regardless of antibodies",
                ],
                0,
                "5–15% of adult 'T2D' may be T1D; misdiagnosis risks DKA on noninsulin therapy and worse long-term outcomes.",
                ref(
                    "Type 2 Diabetes",
                    "persons misdiagnosed as having T2D when they indeed have T1D experience higher HbA $ _{1c} $, have a risk of DKA from the use of noninsulin therapies",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Monogenetic Forms of Diabetes",
                "A 9-month-old with permanent neonatal diabetes should undergo genetic testing primarily because:",
                [
                    "Some monogenic forms respond to sulfonylureas instead of lifelong insulin",
                    "All neonatal hyperglycemia is autoimmune T1D",
                    "MODY always requires insulin only",
                    "Genetic testing never changes neonatal diabetes treatment",
                ],
                0,
                "KCNJ11/ABCC8 mutations may allow sulfonylurea therapy; correct monogenic diagnosis guides treatment and prognosis.",
                ref(
                    "Monogenetic Forms of Diabetes",
                    "Importantly, some monogenic forms of diabetes can be treated with oral diabetes medications, whereas other forms require insulin injections.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Chronic Complications of Type 1 Diabetes",
                "In DCCT, intensive versus conventional insulin therapy primarily reduced which outcomes?",
                [
                    "Microvascular complications (retinopathy, nephropathy, neuropathy)",
                    "All-cause mortality by 50% within 10 years",
                    "Hypoglycemia rates",
                    "Weight loss",
                ],
                0,
                "Intensive therapy lowered median HbA1c ~2% (7% vs 9%) with 35–76% microvascular risk reduction but increased severe hypoglycemia and weight gain.",
                ref(
                    "Hemoglobin  $ A_{1c} $",
                    "The intensively treated group experienced a 35% to 76% reduction in the occurrence of microvascular complications, including retinopathy, nephropathy, and neuropathy, compared with the conventionally treated group.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Initiation of Insulin Therapy",
                "A newly diagnosed non-obese prepubertal child without DKA needs insulin. Typical starting total daily dose?",
                [
                    "0.3 to 0.5 units/kg per day split basal-bolus",
                    "2 units/kg per day as NPH only twice daily",
                    "No insulin until HbA1c exceeds 10%",
                    "0.05 units/kg per day basal only lifelong",
                ],
                0,
                "Typical start 0.3–0.5 U/kg/day (~50% basal, 50% boluses); higher doses for obesity, puberty, or post-DKA recovery.",
                ref(
                    "Initiation of Insulin Therapy",
                    "For young children and postpubertal adults who are not obese and do not present in DKA, a typical starting dose is 0.3 to 0.5 units/kg per day.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Insulin Dose Adjustments",
                "When using rapid-acting analogues for meal boluses, minimum interval between correction boluses to avoid stacking?",
                [
                    "Every 2 to 3 hours",
                    "Every 15 minutes",
                    "Once weekly",
                    "Only at bedtime regardless of glucose",
                ],
                0,
                "Rapid-acting insulin lasts 2–3 hours; correction boluses should not be given more frequently to prevent hypoglycemia from stacked insulin action.",
                ref(
                    "Insulin Dose Adjustments",
                    "Because rapid-acting insulin has a 2- to 3-hour action time, a correction bolus is usually not given any more frequently than every 2 to 3 hours to avoid hypoglycemia from \"stacking\" of insulin action.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Principles of Insulin Pump Use",
                "A patient on CSII develops hyperglycemia and ketones after a dislodged infusion set. Best counseling point?",
                [
                    "Infusion site failure can cause DKA if undetected",
                    "Pump use always increases overall DKA risk versus MDI",
                    "Ketones never occur with pump therapy",
                    "Basal rates cannot be modified on pumps",
                ],
                0,
                "Site failure causes hyperglycemia/ketonemia and potential DKA; overall pump use may decrease DKA risk when used properly.",
                ref(
                    "Principles of Insulin Pump Use",
                    "A failure of the infusion site can lead to hyperglycemia—and potentially DKA if the problem is not detected in time.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Nutrition Therapy",
                "A family asks about very-low-carbohydrate ketogenic diets in T1D on CSII. Most appropriate advice?",
                [
                    "Extreme carb elimination increases DKA risk and should be avoided",
                    "Ketogenic diets are guideline-recommended for all T1D",
                    "Carbohydrate content does not affect glycemia in T1D",
                    "SGLT2 inhibitors are FDA-approved to pair with ketogenic diets in T1D",
                ],
                0,
                "Very low carbohydrate diets risk ketosis—especially with insulin dose reduction, disordered eating, or SGLT2i; extreme ketosis-prone diets should be avoided on CSII.",
                ref(
                    "Nutrition Therapy",
                    "Very low carbohydrates should be avoided because such diets can lead to elevations in lipid levels, and there can be a risk for ketosis, especially with insulin dose reductions, disordered eating behaviors, or use of the sodium-glucose cotransporter 2 (SGLT2) class of oral agents",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Physical Activity and Exercise",
                "To reduce exercise-related hypoglycemia, which pre-exercise strategy is evidence-based?",
                [
                    "Begin with glucose ≥100 mg/dL and plan carb intake during prolonged activity",
                    "Exercise only when ketones are large",
                    "Always suspend all insulin for 24 hours before exercise",
                    "Avoid CGM during exercise because it is inaccurate",
                ],
                0,
                "Start exercise ≥100 mg/dL; provide 0.25–1.00 g carb/min for activities ≥40 minutes; reduce bolus 25–75% for meals within 2 hours of activity.",
                ref(
                    "Physical Activity and Exercise",
                    "To prevent hypoglycemia, one should begin exercise with a glucose of at least 100 mg/dL (5.6 mmol/L) or higher and plan to ingest carbohydrates during and/or after the exercise according to its duration and intensity.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Continuous Glucose Monitoring",
                "Per international consensus, an appropriate TIR target for most adults with T1D is:",
                [
                    "70% time between 70 and 180 mg/dL",
                    "100% time below 70 mg/dL",
                    "50% time above 250 mg/dL",
                    "No target; HbA1c alone suffices",
                ],
                0,
                "Consensus proposes ~70% TIR (70–180 mg/dL), <4% below range (<1% <54 mg/dL), and <25% above range.",
                ref(
                    "Outcomes Beyond HbA $ _{1c} $",
                    "An international consensus group proposed that for most people living with T1D, an appropriate target is 70% TIR (between 70 and 180 mg/dL; 3.9-10.0 mmol/L)",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Hypoglycemia",
                "A conscious T1D patient with glucose 55 mg/dL and tremor. Immediate management?",
                [
                    "15 g oral glucose with reassessment",
                    "Immediate intubation without glucose",
                    "High-dose IV insulin bolus",
                    "Wait 6 hours before any treatment",
                ],
                0,
                "Conscious hypoglycemia: 15 g glucose; repeat based on capillary glucose; unconscious patients need IV glucose or glucagon.",
                ref(
                    "Hypoglycemia",
                    "An acute hypoglycemic attack needs to be dealt with swiftly by taking glucose (15 g) in cases where the person is conscious.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Pathophysiology of Diabetic Ketoacidosis",
                "Which triad defines DKA?",
                [
                    "Hyperglycemia, ketonemia, and acidosis",
                    "Hypoglycemia, bradycardia, and hypertension",
                    "Normal glucose, absent ketones, pH 7.45",
                    "Hypernatremia alone",
                ],
                0,
                "DKA = glucose >200–250 mg/dL, β-hydroxybutyrate ≥3 mmol/L (or moderate/large urine ketones), pH <7.3 or bicarbonate <15 mmol/L.",
                ref(
                    "Pathophysiology of Diabetic Ketoacidosis",
                    "DKA is defined by hyperglycemia (blood glucose over 200–250 mg/dL, 11–13.9 mmol/L), ketonemia (blood  $ \\beta $-hydroxybutyrate  $ \\geq $3 mmol/L or moderate/large urine ketones), and acidosis (venous pH below 7.3 or serum bicarbonate below 15 mmol/L).",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Treatment of Diabetic Ketoacidosis",
                "During DKA treatment, insulin infusion should typically:",
                [
                    "Start 0.05–0.1 U/kg/h at least 1 hour after fluids, without bolus",
                    "Begin before any fluid resuscitation as a large IV bolus",
                    "Be withheld until glucose is below 100 mg/dL",
                    "Replace potassium before any fluids",
                ],
                0,
                "Fluids first (10 mL/kg NS boluses), then insulin drip 0.05–0.1 U/kg/h without bolus; glucose should fall 50–75 mg/dL/h.",
                ref(
                    "Treatment of Diabetic Ketoacidosis",
                    "Initiation of an insulin drip at a rate of 0.05 to 0.1 units/kg per hour, without an insulin bolus, should begin at least 1 hour after fluid replacement is started.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Sodium-Glucose Cotransporter Inhibitors",
                "An adult with T1D on MDI asks about adjunct dapagliflozin. Most important counseling?",
                [
                    "Two- to fourfold higher DKA risk including euglycemic DKA",
                    "SGLT2 inhibitors are FDA-approved for all T1D in the U.S.",
                    "No need to monitor ketones or adjust insulin",
                    "Genital mycotic infections never occur",
                ],
                0,
                "Trials show improved HbA1c/TIR/weight but 2–4× DKA and genital mycotic infections; not FDA-approved for T1D in the U.S.",
                ref(
                    "Sodium-Glucose Cotransporter Inhibitors",
                    "those treated with SGLT inhibitors also had higher rates of genital mycotic infections and DKA (two- to fourfold increase).",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Pramlintide",
                "Which benefit has FDA-approved pramlintide shown as T1D adjunct in adults?",
                [
                    "Modest HbA1c reduction and decreased postprandial excursions",
                    "Mandatory use in all children with T1D",
                    "Elimination of all insulin requirements",
                    "Cure of autoimmune β-cell destruction",
                ],
                0,
                "Pramlintide slows gastric emptying, suppresses postprandial glucagon, lowers HbA1c ~0.3–0.6%, aids weight loss; nausea is common; not approved in children.",
                ref(
                    "Pramlintide",
                    "Addition of pramlintide to insulin at mealtime in adults with T1D improves glycemic control, including modest reductions in HbA $ _{1c} $ by 0.3% to 0.6%, and decreases postprandial glucose excursions.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Pancreas Transplantation",
                "Current preferred pancreas transplant setting for T1D with ESRD is:",
                [
                    "Simultaneous pancreas-kidney (SPK) transplant",
                    "Pancreas transplant alone in all T1D regardless of renal function",
                    "Islet transplant without immunosuppression as first line",
                    "No role for transplantation in T1D",
                ],
                0,
                "SPK is preferred when kidney transplant is needed; PTA remains debated; organ shortage limits procedures.",
                ref(
                    "Pancreas Transplantation",
                    "Pancreatic transplantation for people with T1D requiring a kidney transplant has therefore become the preferred clinical procedure",
                ),
            ),
            mcq(
                f"{p}-m25",
                "β-Cell Transplantation From Islet Isolation",
                "Islet transplantation is most established for which T1D subgroup?",
                [
                    "Severe recurrent hypoglycemia despite optimized therapy",
                    "All newly diagnosed children as first-line cure",
                    "Asymptomatic stage 1 autoantibody-positive relatives",
                    "Patients who refuse any immunosuppression regardless of indication",
                ],
                0,
                "Edmonton protocol enables ~60% insulin independence at 1 year in selected centers, especially for refractory hypoglycemia; graft function often wanes by 5 years.",
                ref(
                    "β-Cell Transplantation From Islet Isolation",
                    "islet  $ \\beta $-cell transplant can prove effective (i.e., about 60% insulin independent at 1 year), especially for patients with severe hypoglycemia when the goal is long-term prevention of severe hypoglycemic episodes.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Prevention and Reversal of Type 1 Diabetes",
                "A TrialNet participant has two autoantibodies and dysglycemia. Evidence-based disease-modifying option in research/clinical approval context?",
                [
                    "Teplizumab anti-CD3 course to delay stage 3 onset",
                    "Routine cyclosporine for all at-risk relatives",
                    "Oral insulin proven to prevent T1D in all TrialNet participants",
                    "No immunotherapy has any delay effect in humans",
                ],
                0,
                "Teplizumab delayed clinical T1D ~3 years in high-risk individuals and is FDA-approved as first disease-modifying T1D therapy; oral insulin prevention trials were negative overall.",
                ref(
                    "Immunosuppression $ ^{39} $",
                    "In November 2022, the FDA approved teplizumab as the first disease-modifying therapy in type 1 diabetes",
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
                "Worldwide T1D incidence is increasing by approximately 2% to 5% per year.",
                True,
                "Key points note rising global incidence, especially in underdeveloped nations.",
                ref(
                    "KEY POINTS",
                    "Worldwide, the incidence of T1D is increasing by 2% to 5% per year, especially in underdeveloped nations.",
                ),
            ),
            tf(
                f"{p}-t2",
                "KEY POINTS",
                "People with T1D still have a reduced life expectancy of about 10 years compared with the general population.",
                True,
                "Technologic advances improved outcomes, yet ~10-year life-expectancy reduction persists, especially with young-age diagnosis.",
                ref(
                    "KEY POINTS",
                    "those with T1D still have a reduced life expectancy of about 10 years, especially when diagnosed at a young age.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Stages in the Natural History of Type 1 Diabetes",
                "Stage 2 pre-T1D is defined by two or more islet autoantibodies with dysglycemia.",
                True,
                "Stage 2 adds impaired glucose tolerance to persistent autoimmunity; stage 3 is overt diabetes.",
                ref(
                    "Stages in the Natural History of Type 1 Diabetes",
                    "Stage 2 shows progression to dysglycemia (impaired glucose tolerance) in the setting of two or more anti-islet autoantibodies.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Histopathology",
                "Human T1D insulitis is defined as at least three islets with more than 15 infiltrating immune cells.",
                True,
                "Expert panel standardized human insulitis definition; lesions are quantitatively limited compared with NOD mice.",
                ref(
                    "Histopathology",
                    "an expert panel establishing a standardized definition for this lesion of three islets containing more than 15 CD45 $ ^{+} $ cells in a pancreas.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Autoantibodies",
                "Approximately 90% of White children with new-onset diabetes express at least one of the four T1D-associated autoantibodies.",
                True,
                "Sensitivity is high in White children but lower in some ethnic groups; antibody negativity can occur at diagnosis in adults.",
                ref(
                    "Autoantibodies",
                    "approximately 90% of White children presenting with diabetes express at least one of these four T1D-associated autoantibodies",
                ),
            ),
            tf(
                f"{p}-t6",
                "Vaccines",
                "Childhood vaccination schedules have been shown to increase T1D development.",
                False,
                "Multiple studies found no link between childhood vaccines and T1D incidence.",
                ref(
                    "Vaccines",
                    "none has provided any evidence that childhood vaccinations influence the development of diabetes.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Diagnosis",
                "Most patients with T1D present during stage 3 when symptomatic hyperglycemia occurs.",
                True,
                "Stages 1–2 are presymptomatic; clinical diagnosis usually occurs at stage 3 after major β-cell loss.",
                ref(
                    "Diagnosis",
                    "Most patients present during stage 3, the classical definition of T1D onset, when significant  $ \\beta $-cell destruction has taken place to afford symptomatic disease.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Insulin Therapy",
                "Intensive insulin therapy per DCCT can be delivered by MDI basal-bolus or insulin pump (CSII).",
                True,
                "Standard intensive care uses basal-bolus MDI or CSII with rapid-acting meal boluses.",
                ref(
                    "Insulin Therapy",
                    "intensive insulin therapy has become the standard of care for treatment of T1D and can be achieved with multiple daily injections (MDIs) basabolus therapy or insulin pump therapy.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Self-Monitoring of Blood Glucose",
                "For T1D, blood glucose monitoring is generally recommended at least 4 times daily and up to 10–12 times daily.",
                True,
                "Frequency individualizes to goals; CGM increasingly supplants frequent fingersticks when available.",
                ref(
                    "Self-Monitoring of Blood Glucose",
                    "For persons with T1D, BGM is generally recommended at least 4 times daily and up to 10 to 12 times daily.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Hypoglycemia",
                "Level 3 hypoglycemia requires third-party assistance due to altered mental or physical status.",
                True,
                "Level 1 <70 mg/dL; level 2 <54 mg/dL; level 3 is severe with impaired consciousness requiring assistance.",
                ref(
                    "Hypoglycemia",
                    "level 3 hypoglycemia (any hypoglycemia characterized by altered mental state and/or physical status needing the intervention of a third party for recovery), should be avoided.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Epidemiology and Risk Factors for Diabetic Ketoacidosis",
                "Autoantibody screening programs can reduce DKA at T1D presentation through education of at-risk individuals.",
                True,
                "Prospective natural history follow-up lowers DKA frequency at diagnosis; most DKA later occurs in established T1D.",
                ref(
                    "Epidemiology and Risk Factors for Diabetic Ketoacidosis",
                    "Screening programs for presence of autoantibodies to detect people at risk for T1D reduce the risk for DKA at presentation through education of those identified to be at risk.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Pramlintide",
                "Pramlintide is FDA-approved as adjunct therapy for children with T1D.",
                False,
                "Pramlintide is FDA-approved for adults with T1D only; no adjunct is FDA-approved for pediatric T1D.",
                ref(
                    "Pramlintide",
                    "Pramlintide is approved by the FDA for adjunctive use in adults with T1D but not in children.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Prevention and Reversal of Type 1 Diabetes",
                "Teplizumab was FDA-approved in November 2022 as the first disease-modifying therapy for type 1 diabetes.",
                True,
                "Anti-CD3 teplizumab delays progression to clinical T1D in high-risk stage 2 individuals.",
                ref(
                    "Immunosuppression $ ^{39} $",
                    "In November 2022, the FDA approved teplizumab as the first disease-modifying therapy in type 1 diabetes",
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
                "Assertion: T1D natural history can be ascertained using immunologic, genetic, and metabolic staging markers.",
                "Reason: T1D always presents acutely without any prodromal autoimmunity.",
                2,
                "Assertion true; reason false—onset often follows months to years of presymptomatic autoimmunity and dysglycemia.",
                ref(
                    "KEY POINTS",
                    "The risk for the disease can be ascertained through a combination of immunologic, genetic, and metabolic markers of disease, with the natural history now defined by a series of \"stages.\"",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Natural History of Type 1 Diabetes",
                "Assertion: Symptoms historically were thought to appear after 85–90% β-cell loss.",
                "Reason: C-peptide production is completely absent at T1D onset in all patients by modern assays.",
                2,
                "Assertion true; reason false—residual C-peptide may persist and ultrasensitive assays detect low-level secretion even after diagnosis.",
                ref(
                    "Natural History of Type 1 Diabetes",
                    "some constituents are under states of correction (e.g., the aforementioned notion that C-peptide production is lost in T1D at onset, as demonstrated using newer C-peptide assays with accurate lower levels of detection)",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Epidemiology",
                "Assertion: First-degree relatives have substantially higher T1D risk than the general population.",
                "Reason: Most incident T1D cases occur in people with an affected first-degree relative.",
                2,
                "Assertion true (15× general population risk); reason false—>85% of new cases are sporadic without affected first-degree relatives.",
                ref(
                    "Disease Incidence and Prevalence",
                    "it is important to realize that most persons (>85%) in whom T1D develops do not have a first-degree relative with the disease.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "The Major Histocompatibility Complex",
                "Assertion: HLA-DR and HLA-DQ haplotypes strongly influence T1D susceptibility.",
                "Reason: HLA class I loci never influence T1D risk.",
                2,
                "Assertion true; reason false—class I HLA alleles (e.g., A24) also influence age of onset and risk.",
                ref(
                    "The Major Histocompatibility Complex",
                    "In addition, HLA class I loci (HLA-A, HLA-B, and HLA-C) influence disease, and it is likely that additional loci within or linked to the MHC influence immune function and contribute to risk.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Autoantibodies",
                "Assertion: Islet autoantibodies help distinguish T1D from other diabetes types.",
                "Reason: All commercial laboratories provide equally sensitive assays for all four autoantibodies.",
                2,
                "Assertion true; reason false—many labs lack full sensitive/specific panels, causing false negatives/positives especially in adults.",
                ref(
                    "Autoantibodies",
                    "most commercial laboratories do not provide either the full spectrum of assays or equivalently sensitive or specific assays, resulting in both false-negative and, on rare occasion, false-positive results",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Type 2 Diabetes",
                "Assertion: Islet autoantibody testing helps differentiate adult T1D from T2D.",
                "Reason: Patients with T1D never manifest insulin resistance.",
                2,
                "Assertion true; reason false—T1D patients may show insulin resistance and HOMA-IR, complicating phenotypic separation.",
                ref(
                    "Type 2 Diabetes",
                    "It is also important to note that patients with T1D can manifest insulin resistance, a feature most often associated with T2D.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Hemoglobin  $ A_{1c} $",
                "Assertion: DCCT intensive therapy reduced microvascular complications.",
                "Reason: Intensive therapy eliminated severe hypoglycemia compared with conventional therapy.",
                2,
                "Assertion true; reason false—intensive therapy increased severe hypoglycemia two- to threefold despite glycemic benefit.",
                ref(
                    "Hemoglobin  $ A_{1c} $",
                    "The cost of intensive management was, however, a two- to threefold increase in the rates of severe hypoglycemia, as well as weight gain.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Principles of Insulin Pump Use",
                "Assertion: Hybrid closed-loop CSII systems can reduce hypoglycemia risk.",
                "Reason: Insulin pumps eliminate the need for any diabetes education or nutrition counseling.",
                2,
                "Assertion true; reason false—CSII requires dedicated DSMES including nutrition and exercise refresh when switching devices.",
                ref(
                    "Principles of Insulin Pump Use",
                    "Use of CSII, from its simplest to its most complex, integrated format, requires specific education that should be embedded in the individualized DSMES program of the patient and their family",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Pathophysiology of Diabetic Ketoacidosis",
                "Assertion: DKA requires hyperglycemia, ketonemia, and acidosis.",
                "Reason: Bicarbonate infusion is routinely recommended for all DKA cases.",
                2,
                "Assertion true; reason false—bicarbonate is not typically recommended except unusual severe acidosis or hyperkalemia.",
                ref(
                    "Treatment of Diabetic Ketoacidosis",
                    "Bicarbonate is not typically recommended in the treatment of DKA, except in unusual circumstances related to severe acidosis or hyperkalemia.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Sodium-Glucose Cotransporter Inhibitors",
                "Assertion: SGLT inhibitors as T1D adjuncts can improve HbA1c and weight without increased hypoglycemia.",
                "Reason: SGLT inhibitors carry no increased DKA risk in T1D.",
                2,
                "Assertion true in trials; reason false—DKA risk increases two- to fourfold, including euglycemic DKA.",
                ref(
                    "Sodium-Glucose Cotransporter Inhibitors",
                    "DKA (two- to fourfold increase).",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Immunosuppression $ ^{39} $",
                "Assertion: Teplizumab delays progression to clinical T1D in high-risk individuals.",
                "Reason: Teplizumab permanently cures T1D after a single course in all treated patients.",
                2,
                "Assertion true (~3-year delay); reason false—no proven cure; effect is delay, not eradication of autoimmunity.",
                ref(
                    "Immunosuppression $ ^{39} $",
                    "teplizumab delayed progression to clinical T1D by approximately 3 years in high-risk patients.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Immunologic Vaccination",
                "Assertion: TrialNet oral insulin prevention study showed no overall benefit for T1D delay.",
                "Reason: DPT-1 oral insulin trial demonstrated clear overall benefit in all participants regardless of IAA status.",
                2,
                "Assertion true for TrialNet follow-up; reason false—DPT-1 oral insulin showed benefit only in an IAA-high subgroup, not overall.",
                ref(
                    "Immunologic Vaccination",
                    "The oral trial did not document an overall benefit of insulin, but in the subgroup with higher levels of IAA at entry, a statistically significant delay in progression to diabetes was observed.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "35",
        "title": "Type 1 Diabetes Mellitus",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Pieter Gillard, Mark A. Atkinson, and Chantal Mathieu",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_35_Type_1_Diabetes_Mellitus.md",
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
