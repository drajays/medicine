#!/usr/bin/env python3
"""Generate Williams 15e module w15-37 — Monogenic Diabetes."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-37"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-37_Monogenic_Diabetes.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why monogenic diabetes matters in precision medicine",
                "Monogenic forms account for 1–2% of diabetes, arise from single-gene defects in β-cell function or insulin action, and now have defined molecular genetics with specific therapies.",
                ref(
                    "KEY POINTS",
                    "Monogenic forms of diabetes account for 1% to 2% of diabetes cases and are often a consequence of gene defects that either interfere with  $ \\beta $-cell development and function, including insulin production and secretion, or insulin action and result in clinical diabetes.",
                ),
            ),
            note(
                f"{p}-n2",
                "Monogenic Diabetes and Precision Medicine",
                "How precision diagnosis uses biomarker screening",
                "The three-stage pathway assesses C-peptide/UCPCR, then GAD and IA-2 autoantibodies if C-peptide is preserved, then molecular genetic testing if autoantibody-negative.",
                ref(
                    "Monogenic Diabetes and Precision Medicine",
                    "The biomarker screening pathway comprises three stages: (1) assessment of endogenous insulin secretion using serum or urinary C-peptide/creatinine ratio (UCPCR); (2) if serum C-peptide is ≥0.60 mg/mL (0.2 nmol/L) or UCPCR is ≥0.2 nmol/mmol, measurement of glutamic acid decarboxylase and insulinoma-associated protein-2 islet autoantibodies; and (3) if negative for both autoantibodies, molecular genetic diagnostic testing for monogenic diabetes subtypes.",
                ),
            ),
            note(
                f"{p}-n3",
                "Monogenic Diabetes and Precision Medicine",
                "Why K-ATP neonatal diabetes exemplifies precision therapeutics",
                "Sulfonylurea treatment of K-ATP-related neonatal diabetes improves neurocognitive outcomes—an example of prognosis and monitoring tied to molecular diagnosis.",
                ref(
                    "Monogenic Diabetes and Precision Medicine",
                    "Two exemplars of this include the improved neurocognitive outcomes seen in K-ATP-related neonatal diabetes based on early implementation of precision treatment with sulfonylureas and recognition of increased cardiovascular risk warranting statin therapy in those with HNF1A-MODY.",
                ),
            ),
            note(
                f"{p}-n4",
                "Epidemiology",
                "How common is monogenic diabetes before age 30",
                "European cohort data estimate 1–4% of diabetes diagnosed before 30 years among patients suspected of MODY by phenotype.",
                ref(
                    "Epidemiology",
                    "Monogenic diabetes prevalence rates are largely based on European cohorts and estimated at approximately 1% to 4% of all patients diagnosed with diabetes before the age of 30 years, among patients suspected as having MODY based on their predominant phenotype.",
                ),
            ),
            note(
                f"{p}-n5",
                "Epidemiology",
                "Why SEARCH data changed MODY recognition in U.S. youth",
                "Only 3 of 47 genetically confirmed MODY patients had a clinical MODY diagnosis; most were on insulin, showing massive underdiagnosis without genetic testing.",
                ref(
                    "Epidemiology",
                    "Overall, 1.2% of the original cohort of children had genetically confirmed monogenic diabetes.",
                ),
            ),
            note(
                f"{p}-n6",
                "Clinical Characteristics",
                "How Table 37.1 flags MODY versus type 1 diabetes",
                "Features atypical for T1D include absent islet autoantibodies, measurable C-peptide ≥0.60 ng/mL with hyperglycemia, low insulin requirements, and no ketoacidosis when insulin is omitted.",
                ref(
                    "TABLE 37.1",
                    "Measurable C-peptide ( $ \\geq $0.60 ng/mL [ $ \\geq $0.2 nmol/L]) in the presence of hyperglycemia",
                ),
            ),
            note(
                f"{p}-n7",
                "Clinical Characteristics",
                "Why MODY can mimic type 2 diabetes in youth",
                "Onset before 45 years without significant obesity, acanthosis, or typical dyslipidemia should raise suspicion for monogenic diabetes over classic T2D.",
                ref(
                    "TABLE 37.1",
                    "Onset of diabetes before age of 45 years",
                ),
            ),
            note(
                f"{p}-n8",
                "Clinical Characteristics",
                "How the MODY Calculator guides genetic testing",
                "The Exeter MODY Calculator (diabetesgenes.org) integrates age, treatment, BMI, HbA1c, family history, and syndromic features to estimate MODY probability in patients diagnosed under 35.",
                ref(
                    "Clinical Characteristics",
                    "A clinical prediction tool (MODY Calculator) to calculate an individual's probability of having MODY is available at https://www.diabetesgenes.org/exeter-diabetes-app and as a phone-based app.",
                ),
            ),
            note(
                f"{p}-n9",
                "MODY",
                "Why GCK-MODY usually needs no glucose-lowering therapy",
                "Stable mild fasting hyperglycemia (99–144 mg/dL) from birth reflects a glucose-sensing defect; oral agents and insulin lack glycemic benefit and are contraindicated outside pregnancy exceptions.",
                ref(
                    "MODY",
                    "Treatment with these agents in GCK-MODY is not recommended and is even contraindicated because of the lack of most long-term microvascular and macrovascular complications of diabetes and the side effects of potential glycemic-reduction interventions.",
                ),
            ),
            note(
                f"{p}-n10",
                "MODY",
                "How HNF1A-MODY presents before overt diabetes",
                "Reduced SGLT2 expression causes renal glucosuria at lower thresholds—glucose appears in urine before diabetes onset, a hallmark of HNF1A insufficiency.",
                ref(
                    "MODY",
                    "In fact, because HNF1A is a key factor for SGLT2 expression, the appearance of glucose in the urine before onset of diabetes is a hallmark of HNF1A insufficiency (Fig. 37.5).",
                ),
            ),
            note(
                f"{p}-n11",
                "MODY",
                "Why HNF1A-MODY warrants cardiovascular risk management",
                "HNF1A-MODY carriers have increased all-cause and cardiovascular mortality compared with unaffected family members—statin therapy is recommended.",
                ref(
                    "Monogenic Diabetes and Precision Medicine",
                    "recognition of increased cardiovascular risk warranting statin therapy in those with HNF1A-MODY.",
                ),
            ),
            note(
                f"{p}-n12",
                "MODY",
                "How HNF4A-MODY differs at birth and in treatment",
                "Affected infants weigh ~800 g more than unaffected siblings; neonatal hypoglycemia may occur, and low-dose sulfonylureas often work before later insulin requirement.",
                ref(
                    "MODY",
                    "Affected individuals have been found to weigh about 800 g more at birth than their unaffected siblings, and hyperinsulinemia at birth with symptomatic neonatal hypoglycemia that resolves spontaneously may occur.",
                ),
            ),
            note(
                f"{p}-n13",
                "MODY",
                "Why HNF1B-MODY requires multisystem surveillance",
                "Renal cysts, pancreatic hypoplasia with exocrine deficiency, hypomagnesemia, and reproductive tract anomalies define this syndrome; sulfonylureas fail and insulin is preferred.",
                ref(
                    "MODY",
                    "Clinical features most frequently observed include abnormally developed kidneys, and a common presentation is the renal cysts and diabetes syndrome.",
                ),
            ),
            note(
                f"{p}-n14",
                "Neonatal Diabetes Mellitus",
                "How INS versus K-ATP genes dictate neonatal diabetes therapy",
                "INS pathogenic variants require insulin; KCNJ11 and ABCC8 K-ATP channel defects usually respond to high-dose sulfonylureas.",
                ref(
                    "KEY POINTS",
                    "The most common causes of neonatal diabetes include pathogenic variants in the insulin gene (requiring insulin treatment) and in KCNJ11 and ABCC8 genes, which encode the subunits of the K-ATP channel and are usually responsive to high doses of sulfonylureas.",
                ),
            ),
            note(
                f"{p}-n15",
                "Neonatal Diabetes Mellitus",
                "How to order comprehensive neonatal diabetes genetic testing",
                "Test all diabetes diagnosed under 9 months—and ages 6–12 months if antibody-negative or monogenic features are present—for KCNJ11, ABCC8, INS, and 6q24 imprinting defects.",
                ref(
                    "Neonatal Diabetes Mellitus",
                    "Comprehensive genetic testing that preferably includes all known causes or, at the very least, KCNJ11, ABCC8, and INS, along with determination of 6q24 imprinting defects, should be undertaken in all individuals with diabetes diagnosed under 9 months of age",
                ),
            ),
            note(
                f"{p}-n16",
                "Syndromic Diabetes",
                "How mitochondrial MIDD presents beyond diabetes",
                "m.3243A>G in mitochondrial tRNA causes maternally inherited diabetes and deafness; high-energy tissues including pancreatic islets and cochlear stria are affected.",
                ref(
                    "Syndromic Diabetes",
                    "Maternally inherited diabetes and deafness (MIDD) is estimated to affect up to 1% of patients with diabetes and results from an A to G substitution at position 3243 (m.3243A>G) of the mitochondrial DNA encoding the gene for tRNA.",
                ),
            ),
            note(
                f"{p}-n17",
                "Syndromic Diabetes",
                "Why metformin is avoided in MIDD",
                "Metformin interferes with mitochondrial function and may increase lactic acidosis risk in mitochondrial diabetes, though reports in MIDD remain limited.",
                ref(
                    "Syndromic Diabetes",
                    "Metformin is best avoided as it is known to interfere with mitochondrial function and the risk of lactic acidosis may be increased, although this has not been reported to date.",
                ),
            ),
            note(
                f"{p}-n18",
                "Syndromic Diabetes",
                "How Wolfram syndrome (WFS1) progresses clinically",
                "Insulin-dependent nonautoimmune diabetes is the first manifestation (mean age 6 years), followed by optic atrophy, central diabetes insipidus, and neurologic degeneration by the third decade.",
                ref(
                    "Syndromic Diabetes",
                    "Insulin-dependent nonautoimmune diabetes mellitus is the first clinical manifestation with onset at the mean age of 6 years (range 3 weeks–16 years).",
                ),
            ),
            note(
                f"{p}-n19",
                "GCK-MODY",
                "How GCK-MODY pregnancy management depends on fetal genotype",
                "If the fetus lacks the GCK mutation it senses maternal hyperglycemia as high and secretes insulin—insulin therapy is recommended to prevent macrosomia; affected mother-fetus pairs need no treatment.",
                ref(
                    "GCK-MODY",
                    "If the fetus does not carry the GCK mutation, it will sense the maternal glucose to be high and increase insulin secretion. Thus, insulin therapy is recommended in these pregnancies with an unaffected fetus to attempt to normalize maternal blood sugar to prevent development of macrosomia.",
                ),
            ),
            note(
                f"{p}-n20",
                "HNF4A and HNF1A",
                "Why HNF4A-MODY pregnancies need early delivery planning",
                "Fetal HNF4A inheritance increases birth weight ~790 g with risk of macrosomia and prolonged neonatal hypoglycemia—ultrasound from 28 weeks and delivery at 35–38 weeks are recommended.",
                ref(
                    "HNF4A and HNF1A",
                    "For HNF4A-MODY mutation carriers, birthweight is significantly increased by a median of 790 g compared with family members without the mutation.",
                ),
            ),
            note(
                f"{p}-n21",
                "HNF4A and HNF1A",
                "How sulfonylureas are managed in HNF1A/HNF4A pregnancy",
                "Preferred approach: switch to insulin before conception; alternative: continue glyburide in first trimester then insulin in second/third trimester because placental transfer risks macrosomia and neonatal hypoglycemia.",
                ref(
                    "HNF4A and HNF1A",
                    "Shepherd et al reviewed the available evidence and recommended that in women with HNF1A/HNF4A MODY, those with good glycemic control who are on a sulfonylurea periconception either transfer to insulin before conception (at the risk of a short-term deterioration of glycemic control) or continue with sulfonylurea (glyburide) treatment in the first trimester and transfer to insulin during the second trimester.",
                ),
            ),
            note(
                f"{p}-n22",
                "KEY POINTS",
                "Why lipodystrophy syndromes belong in the monogenic diabetes differential",
                "Monogenic lipodystrophy, insulin resistance, and obesity syndromes can include diabetes as part of the phenotype and appear on commercial gene panels (e.g., LIPE, LMNA).",
                ref(
                    "KEY POINTS",
                    "Monogenic causes of lipodystrophies, insulin resistance, and obesity may also include diabetes as part of the syndrome.",
                ),
            ),
            note(
                f"{p}-n23",
                "Challenges in Diagnosing Monogenic Diabetes",
                "How obesity no longer excludes MODY",
                "TODAY trial found pathogenic MODY variants in 4.5% of overweight/obese antibody-negative, C-peptide-positive youth labeled as T2D—systematic testing is needed.",
                ref(
                    "Clinical Characteristics",
                    "Pathogenic or likely pathogenic variants in MODY genes were found in 4.5% of the cohort, providing evidence that monogenic diabetes occurs in overweight and obese individuals and is likely underdiagnosed in the absence of systematic assessment.",
                ),
            ),
            note(
                f"{p}-n24",
                "Introduction",
                "How MODY nomenclature has evolved beyond MODY-X",
                "With >30 monogenic diabetes genes identified, gene-specific names (e.g., HNF1A-MODY) replace the historical MODY-X designation for clarity.",
                ref(
                    "Introduction",
                    "The total number of such genes now exceeds 30, so we will avoid use of the \"MODY-X\" nomenclature and for clarity will instead use the generally preferred terminology with gene name itself (e.g., HNF1A-MODY rather than MODY1).",
                ),
            ),
            note(
                f"{p}-n25",
                "MODY",
                "Why HNF1A-MODY responds to low-dose sulfonylureas",
                "Pearson et al showed genetic cause determines treatment response—HNF1A-MODY patients are exquisitely sensitive to sulfonylureas, often achieving control at doses a fraction of T2D requirements.",
                ref(
                    "MODY",
                    "Most patients are initially quite responsive to sulfonylureas, even to the point of hypoglycemia with low doses.",
                ),
            ),
            note(
                f"{p}-n26",
                "Conclusions",
                "How monogenic diabetes serves as a precision-medicine exemplar",
                "Identification, molecular diagnosis, and targeted treatment of neonatal diabetes and MODY now model what precision medicine can achieve in broader diabetes care.",
                ref(
                    "Conclusions",
                    "Now the identification, molecular diagnosis, and treatment of neonatal diabetes and MODY serve as an exemplar of diabetes precision medicine.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Monogenic Diabetes and Precision Medicine",
                "A 22-year-old with lean build, diabetes since age 16, and C-peptide 1.2 ng/mL during hyperglycemia has negative GAD and IA-2 antibodies. Next best step?",
                [
                    "Molecular genetic testing for monogenic diabetes subtypes",
                    "Start empiric insulin without further workup",
                    "Repeat HbA1c in 6 months only",
                    "Assume type 2 diabetes and add metformin only",
                ],
                0,
                "Biomarker pathway stage 3: antibody-negative preserved C-peptide warrants monogenic genetic testing.",
                ref(
                    "Monogenic Diabetes and Precision Medicine",
                    "if negative for both autoantibodies, molecular genetic diagnostic testing for monogenic diabetes subtypes.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Epidemiology",
                "In SEARCH for Diabetes in Youth, what proportion of the full pediatric cohort had genetically confirmed MODY in GCK, HNF1A, or HNF4A?",
                [
                    "1.2%",
                    "8.2%",
                    "12%",
                    "25%",
                ],
                0,
                "1.2% of ~5000 participants had confirmed monogenic diabetes; 8.2% was among the 586 sequenced subset.",
                ref(
                    "Epidemiology",
                    "Overall, 1.2% of the original cohort of children had genetically confirmed monogenic diabetes.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Clinical Characteristics",
                "Which feature is atypical for type 1 diabetes and should prompt MODY testing?",
                [
                    "Measurable C-peptide ≥0.2 nmol/L with hyperglycemia after the honeymoon period",
                    "Positive glutamic acid decarboxylase autoantibodies",
                    "Presentation with diabetic ketoacidosis at diagnosis",
                    "Insulin requirement from diagnosis",
                ],
                0,
                "Table 37.1 lists preserved C-peptide, absent autoantibodies, low insulin needs, and no DKA off insulin as T1D-atypical.",
                ref(
                    "TABLE 37.1",
                    "Evidence of endogenous insulin production beyond the honeymoon period",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Clinical Characteristics",
                "A 28-year-old diagnosed at age 32 with BMI 24, normal lipids, and autosomal-dominant family history. Which tool estimates MODY probability?",
                [
                    "Exeter MODY Calculator (diabetesgenes.org app)",
                    "Framingham cardiovascular risk score only",
                    "HOMA-IR alone without clinical context",
                    "Random urinary microalbumin ratio",
                ],
                0,
                "MODY Calculator integrates clinical features and is applicable to patients diagnosed under 35 years.",
                ref(
                    "Clinical Characteristics",
                    "It takes into account commonly available clinical information (age at diagnosis, sex, diabetes treatment, body mass index [BMI], glycated hemoglobin, current age), first-degree family history, and other clinical features",
                ),
            ),
            mcq(
                f"{p}-m5",
                "MODY",
                "A teenager has stable fasting glucose 110–125 mg/dL since childhood, negative antibodies, and no response to metformin. Most likely diagnosis?",
                [
                    "GCK-MODY",
                    "HNF1B-MODY with renal cysts",
                    "Type 1 diabetes in honeymoon",
                    "Mitochondrial MIDD",
                ],
                0,
                "GCK-MODY causes mild stable fasting hyperglycemia from birth without benefit from glucose-lowering agents.",
                ref(
                    "MODY",
                    "These patients have stable fasting hyperglycemia (generally in the range of 99–144 mg/dL [5.5–8.0 mmol/L]) present at birth.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "MODY",
                "A 19-year-old with glucosuria at normal blood glucose and later diabetes is found to have HNF1A-MODY. Best initial therapy?",
                [
                    "Low-dose sulfonylurea",
                    "High-dose insulin only without trial of oral agents",
                    "SGLT2 inhibitor as first-line (large trials support routine use)",
                    "No treatment ever required",
                ],
                0,
                "HNF1A-MODY is highly sulfonylurea-sensitive; SGLT2 inhibitors lack large systematic studies and carry DKA/dehydration risk.",
                ref(
                    "MODY",
                    "Most patients are initially quite responsive to sulfonylureas, even to the point of hypoglycemia with low doses.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "MODY",
                "An adult with HNF1A-MODY asks about cardiovascular prevention beyond glucose control. Evidence-based addition?",
                [
                    "Statin therapy for increased cardiovascular mortality risk",
                    "Routine high-dose aspirin regardless of risk factors",
                    "No additional therapy because MODY never causes vascular disease",
                    "Metformin mandatory despite sulfonylurea response",
                ],
                0,
                "HNF1A-MODY carries increased all-cause and cardiovascular mortality—statin therapy is part of precision prognosis.",
                ref(
                    "Monogenic Diabetes and Precision Medicine",
                    "recognition of increased cardiovascular risk warranting statin therapy in those with HNF1A-MODY.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "MODY",
                "Neonatal hypoglycemia that resolved, macrosomia at birth, and young-adult diabetes in one family suggests:",
                [
                    "HNF4A-MODY",
                    "GCK-MODY",
                    "Wolfram syndrome (WFS1)",
                    "Permanent INS neonatal diabetes",
                ],
                0,
                "HNF4A-MODY features include increased birth weight (~800 g), transient neonatal hypoglycemia, and later sulfonylurea-responsive diabetes.",
                ref(
                    "MODY",
                    "Affected individuals have been found to weigh about 800 g more at birth than their unaffected siblings, and hyperinsulinemia at birth with symptomatic neonatal hypoglycemia that resolves spontaneously may occur.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "MODY",
                "A 26-year-old with diabetes, renal cysts, hypomagnesemia, and elevated liver enzymes most likely has:",
                [
                    "HNF1B-MODY (renal cysts and diabetes syndrome)",
                    "HNF1A-MODY with isolated glucosuria",
                    "GCK-MODY",
                    "KCNJ11 permanent neonatal diabetes",
                ],
                0,
                "HNF1B-MODY presents with renal developmental anomalies, pancreatic hypoplasia, hypomagnesemia, and does not respond to sulfonylureas.",
                ref(
                    "MODY",
                    "Other presenting features include anomalies of the exocrine pancreas (reduced size and pancreatic exocrine deficiency), reproductive tract abnormalities, abnormal liver tests, hyperuricemia, hypomagnesemia due to renal wasting",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Neonatal Diabetes Mellitus",
                "A 4-month-old with permanent diabetes and KCNJ11 mutation. Optimal treatment transition?",
                [
                    "High-dose oral sulfonylurea with insulin wean as tolerated",
                    "Lifelong insulin only; sulfonylureas are contraindicated",
                    "Metformin monotherapy",
                    "No therapy until age 10 years",
                ],
                0,
                "K-ATP channel neonatal diabetes (KCNJ11/ABCC8) usually responds to high-dose sulfonylureas, improving glycemia and neurodevelopment.",
                ref(
                    "KEY POINTS",
                    "in KCNJ11 and ABCC8 genes, which encode the subunits of the K-ATP channel and are usually responsive to high doses of sulfonylureas.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Neonatal Diabetes Mellitus",
                "A 7-month-old with antibody-negative diabetes should undergo genetic testing including at minimum:",
                [
                    "KCNJ11, ABCC8, INS, and 6q24 imprinting assessment",
                    "HLA typing only",
                    "GCK alone",
                    "WFS1 as first-line single-gene test only",
                ],
                0,
                "Comprehensive neonatal diabetes testing includes KATP genes, INS, and 6q24 imprinting for diabetes diagnosed under 9 months.",
                ref(
                    "Neonatal Diabetes Mellitus",
                    "Comprehensive genetic testing that preferably includes all known causes or, at the very least, KCNJ11, ABCC8, and INS, along with determination of 6q24 imprinting defects, should be undertaken in all individuals with diabetes diagnosed under 9 months of age",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Neonatal Diabetes Mellitus",
                "Permanent neonatal diabetes due to heterozygous INS mutations typically requires:",
                [
                    "Insulin therapy",
                    "High-dose sulfonylurea as definitive cure",
                    "No treatment because diabetes is always transient",
                    "Metformin only",
                ],
                0,
                "INS pathogenic variants are a leading cause of permanent neonatal diabetes and require insulin treatment.",
                ref(
                    "KEY POINTS",
                    "The most common causes of neonatal diabetes include pathogenic variants in the insulin gene (requiring insulin treatment)",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Syndromic Diabetes",
                "A 35-year-old with diabetes, sensorineural deafness, and maternal family history should be tested for:",
                [
                    "Mitochondrial m.3243A>G (MIDD)",
                    "GCK heterozygous MODY only",
                    "HNF1B deletion as first test",
                    "WFS1 homozygous mutation only",
                ],
                0,
                "MIDD results from m.3243A>G in mitochondrial tRNA and includes diabetes with deafness.",
                ref(
                    "Syndromic Diabetes",
                    "Maternally inherited diabetes and deafness (MIDD) is estimated to affect up to 1% of patients with diabetes and results from an A to G substitution at position 3243 (m.3243A>G) of the mitochondrial DNA encoding the gene for tRNA.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Syndromic Diabetes",
                "A 10-year-old with insulin-dependent diabetes and progressive optic atrophy should be evaluated for:",
                [
                    "Wolfram syndrome (WFS1)",
                    "GCK-MODY",
                    "HNF4A-MODY alone",
                    "Alström syndrome as the only possibility",
                ],
                0,
                "Wolfram syndrome presents with insulin-dependent diabetes followed by optic atrophy, then DI and deafness.",
                ref(
                    "Syndromic Diabetes",
                    "In the syndromic forms, optic atrophy closely follows or precedes the onset of diabetes, and affected individuals have worsening insulin deficiency and require insulin for treatment.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "GCK-MODY",
                "A pregnant woman with GCK-MODY has fetal ultrasound showing accelerated growth. Fetus likely:",
                [
                    "Did not inherit the GCK mutation—maternal insulin therapy is indicated",
                    "Inherited GCK mutation—requires high-dose insulin immediately",
                    "Has Wolfram syndrome regardless of genotype",
                    "Should receive fetal sulfonylurea therapy",
                ],
                0,
                "Unaffected fetuses of GCK mothers are at macrosomia risk; insulin is recommended when the fetus has not inherited the mutation.",
                ref(
                    "GCK-MODY",
                    "Thus, insulin therapy is recommended in these pregnancies with an unaffected fetus to attempt to normalize maternal blood sugar to prevent development of macrosomia.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "HNF4A and HNF1A",
                "A woman with HNF4A-MODY at 30 weeks gestation with large-for-gestational-age fetus. Recommended delivery planning?",
                [
                    "Elective delivery between 35 and 38 weeks with neonatal glucose monitoring",
                    "Routine delivery at 41 weeks without surveillance",
                    "Continue sulfonylurea through third trimester without insulin switch",
                    "No fetal growth monitoring needed",
                ],
                0,
                "HNF4A pregnancies need ultrasound from 28 weeks and delivery 35–38 weeks because of macrosomia and neonatal hypoglycemia risk.",
                ref(
                    "HNF4A and HNF1A",
                    "Monitoring fetal growth at 2-week intervals after 28 weeks of gestation and early delivery (elective cesarean section or induction of labor between 35 and 38 weeks) if the fetus inherits an HNF4A mutation from either parent is recommended",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Clinical Characteristics",
                "An obese adolescent with antibody-negative diabetes and positive C-peptide in TODAY trial had MODY variants in what proportion?",
                [
                    "4.5%",
                    "0%",
                    "25%",
                    "50%",
                ],
                0,
                "Monogenic diabetes is underdiagnosed in obese youth—4.5% of TODAY participants had MODY gene variants.",
                ref(
                    "Clinical Characteristics",
                    "Pathogenic or likely pathogenic variants in MODY genes were found in 4.5% of the cohort, providing evidence that monogenic diabetes occurs in overweight and obese individuals and is likely underdiagnosed in the absence of systematic assessment.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Epidemiology",
                "In the University of Chicago Monogenic Diabetes Registry, the most common MODY gene was:",
                [
                    "GCK (59% of known genetic causes)",
                    "HNF1B",
                    "INS",
                    "WFS1",
                ],
                0,
                "Among known genetic causes in the U.S. registry, GCK was most common (59%), then HNF1A (28%); KCNJ11 led neonatal causes.",
                ref(
                    "Epidemiology",
                    "Among genes that cause a MODY phenotype, glucokinase (GCK) pathogenic variants were the most common (59%), followed by HNF1A (28%)",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Challenges in Diagnosing Monogenic Diabetes",
                "Major barriers to correct MODY classification include:",
                [
                    "Clinical overlap with T1D/T2D and limited access to genetic testing",
                    "Universal newborn MODY screening in all countries",
                    "MODY never being misdiagnosed as T1D",
                    "Absence of any commercial gene panels",
                ],
                0,
                "Overlap with common diabetes types, low referral rates, and unavailable testing drive frequent MODY misdiagnosis.",
                ref(
                    "Challenges in Diagnosing Monogenic Diabetes",
                    "There are multiple challenges in diagnosing monogenetic diabetes that contribute to frequent misdiagnosis of MODY, including the overlap of clinical features with type 1 and type 2 diabetes, low rates of referral for early comprehensive genetic testing, and the inability to obtain any genetic testing in many patients.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "MODY",
                "A patient with HNF1A-MODY is started on an SGLT2 inhibitor and develops euglycemic DKA. Mechanism?",
                [
                    "Baseline reduced SGLT2 expression with further pharmacologic inhibition",
                    "GCK mutation causing absolute insulin deficiency only",
                    "Mitochondrial metformin toxicity",
                    "Excess sulfonylurea from prior therapy alone",
                ],
                0,
                "HNF1A controls SGLT2 expression; additional SGLT2 inhibition may cause euglycemic DKA or dehydration—large trials are lacking.",
                ref(
                    "MODY",
                    "Further inhibition of SGLT2 with small molecule inhibitors could lead to euglycemia diabetic ketoacidosis or dehydration.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Neonatal Diabetes Mellitus",
                "Population-based U.S. data estimate permanent neonatal diabetes prevalence at approximately:",
                [
                    "1 in 252,000 youth",
                    "1 in 2,500 youth",
                    "1 in 10,000 adults only",
                    "1 in 1,000,000 (never confirmed)",
                ],
                0,
                "SEARCH population-based study estimated permanent neonatal diabetes at 1 in 252,000 in U.S. youth.",
                ref(
                    "Epidemiology",
                    "the prevalence of permanent neonatal diabetes in the United States in youth was estimated to be 1 in 252,000 in a population-based study of diabetes.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Clinical Characteristics",
                "At diagnosis, MODY can be distinguished from T1D and T2D by clinical features alone:",
                [
                    "No—clinical characteristics alone are unreliable; biomarkers and genetics are needed",
                    "Yes—always by age of onset alone",
                    "Yes—obesity definitively excludes MODY",
                    "Yes—family history is never useful",
                ],
                0,
                "MODY cannot reliably be distinguished from T1D/T2D on clinical grounds alone; atypical features prompt testing.",
                ref(
                    "Clinical Characteristics",
                    "At diagnosis, MODY cannot reliably be distinguished from type 1 and type 2 diabetes based on clinical characteristics alone.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Syndromic Diabetes",
                "Syndromic forms of diabetes in pediatric clinics account for approximately:",
                [
                    "Less than 1% of children with diabetes",
                    "10–15% of all diabetes",
                    "50% of neonatal diabetes only",
                    "All antibody-negative youth diabetes",
                ],
                0,
                "Syndromic diabetes is rare—<1% of pediatric diabetes clinic patients, often misdiagnosed or missed.",
                ref(
                    "Syndromic Diabetes",
                    "Syndromic forms of diabetes are rare, accounting for less than 1% of children seen in diabetes clinics.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "KEY POINTS",
                "The four most common MODY subtypes include all EXCEPT which pattern?",
                [
                    "Mitochondrial m.3243A>G as a dominant MODY transcription-factor defect",
                    "GCK with mild fasting hyperglycemia and usually no treatment",
                    "HNF1A with glycosuria and sulfonylurea responsiveness",
                    "HNF1B with renal cysts and hypomagnesemia without clear precision therapy",
                ],
                0,
                "Common MODY genes are GCK, HNF1A, HNF4A, HNF1B; mitochondrial MIDD is syndromic, not a classic MODY transcription-factor subtype.",
                ref(
                    "KEY POINTS",
                    "The four most common causes of MODY include heterozygous pathogenic variants in glucokinase (GCK), characterized by mild fasting hyperglycemia with low to no incidence of related diabetes complications and generally requiring no glucose-lowering treatment; hepatocyte nuclear factor-1α (HNF1A) associated with glycosuria with progressive hyperglycemia and frequently response to low doses of sulfonylureas; hepatocyte nuclear factor-4α (HNF4A) with history of transient neonatal hypoglycemia with progressive hyperglycemia, also frequently responsive to low doses of sulfonylureas; and hepatocyte nuclear factor-1β (HNF1B) with renal cysts, pancreatic hypoplasia and exocrine dysfunction, and hypomagnesemia, which lacks clear precision therapy.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Clinical Characteristics",
                "The MODY Calculator incorporates partial lipodystrophy because:",
                [
                    "Syndromic insulin-resistance features help discriminate monogenic from common diabetes",
                    "Lipodystrophy excludes all genetic testing",
                    "It confirms type 1 diabetes genetically",
                    "It replaces C-peptide measurement entirely",
                ],
                0,
                "Calculator includes renal cysts, deafness, partial lipodystrophy, and severe insulin resistance among predictive clinical features.",
                ref(
                    "Clinical Characteristics",
                    "other clinical features (history and presence of renal cysts, deafness, partial lipodystrophy, severe insulin resistance in absence of obesity, severe obesity with other syndromic features) to predict MODY and guide molecular genetic testing.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Monogenic Diabetes and Precision Medicine",
                "Precision therapeutics in common monogenic diabetes forms are notable because they are:",
                [
                    "Cost-effective or cost-saving while improving stable glycemic control",
                    "Always more expensive than lifelong insulin with no glycemic benefit",
                    "Limited to mitochondrial diabetes only",
                    "Proven harmful in neonatal K-ATP cases",
                ],
                0,
                "Gene-targeted therapy (e.g., sulfonylureas in K-ATP/HNF MODY) improves control and can be cost-saving—rare in healthcare.",
                ref(
                    "Monogenic Diabetes and Precision Medicine",
                    "The most common forms of monogenic diabetes are amenable to therapies targeting the molecular etiology of diabetes, result in stable or improved diabetes control, and are cost-effective or cost-saving, which is an almost unheard of feat in health care practice.",
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
                "Monogenic forms of diabetes include neonatal diabetes with onset generally under 9 months and MODY with diagnosis typically before 30 years.",
                True,
                "Key points define neonatal diabetes (<9 months) and MODY (childhood/young adult onset, usually diagnosed before 30).",
                ref(
                    "KEY POINTS",
                    "Monogenic forms of diabetes include neonatal diabetes with onset generally under 9 months of age and maturity-onset diabetes of the young (MODY), characterized by childhood or young adult–onset of diabetes, with diagnosis typically occurring before 30 years of age.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Monogenic Diabetes and Precision Medicine",
                "Clinical implementation of precision medicine is already a reality for monogenic forms of diabetes per ADA/EASD PMDI.",
                True,
                "PMDI recognizes monogenic diabetes as an area where precision medicine is already implemented clinically.",
                ref(
                    "Monogenic Diabetes and Precision Medicine",
                    "The Precision Medicine in Diabetes Initiative (PMDI) of the American Diabetes Association (ADA) and European Association for the Study of Diabetes (EASD) recognize \"clinical implementation [is] already a reality for precision medicine in monogenic forms of diabetes.\"",
                ),
            ),
            tf(
                f"{p}-t3",
                "Epidemiology",
                "In SEARCH, most participants with genetically confirmed MODY variants had already received a clinical diagnosis of MODY.",
                False,
                "Only 3 of 47 genetically confirmed patients had a clinical MODY diagnosis—the majority were treated with insulin.",
                ref(
                    "Epidemiology",
                    "Of these 47 patients identified to have a MODY variant, only 3 had a clinical diagnosis of MODY, and the majority were treated with insulin demonstrating the individual value of a precision diagnosis.",
                ),
            ),
            tf(
                f"{p}-t4",
                "MODY",
                "GCK-MODY patients should routinely receive insulin or oral hypoglycemic agents to prevent long-term complications.",
                False,
                "Treatment is not recommended and is contraindicated outside pregnancy exceptions because complications are rare and therapy carries side effects without benefit.",
                ref(
                    "MODY",
                    "Treatment with these agents in GCK-MODY is not recommended and is even contraindicated because of the lack of most long-term microvascular and macrovascular complications of diabetes and the side effects of potential glycemic-reduction interventions.",
                ),
            ),
            tf(
                f"{p}-t5",
                "MODY",
                "HNF1B-MODY patients typically respond well to low-dose sulfonylureas like HNF1A-MODY.",
                False,
                "Unlike HNF1A and HNF4A, HNF1B-MODY does not respond to sulfonylureas and insulin is preferred.",
                ref(
                    "MODY",
                    "Unlike the other transcription factor causes of MODY (HNF1A and HNF4A), these patients do not respond to sulfonylureas and frequently require insulin for management.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Neonatal Diabetes Mellitus",
                "KCNJ11 and ABCC8 permanent neonatal diabetes usually responds to high-dose sulfonylureas.",
                True,
                "K-ATP channel mutations are the most common treatable neonatal diabetes cause with sulfonylurea transfer from insulin.",
                ref(
                    "KEY POINTS",
                    "in KCNJ11 and ABCC8 genes, which encode the subunits of the K-ATP channel and are usually responsive to high doses of sulfonylureas.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Syndromic Diabetes",
                "Metformin is the preferred first-line agent for mitochondrial MIDD.",
                False,
                "Metformin is best avoided in MIDD because it interferes with mitochondrial function and may increase lactic acidosis risk.",
                ref(
                    "Syndromic Diabetes",
                    "Metformin is best avoided as it is known to interfere with mitochondrial function and the risk of lactic acidosis may be increased, although this has not been reported to date.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Syndromic Diabetes",
                "Wolfram syndrome (WFS1) currently has no cure; management remains largely supportive.",
                True,
                "WS management addresses diabetes, vision, hearing, and neurologic complications supportively.",
                ref(
                    "Syndromic Diabetes",
                    "There is currently no cure for WS; management remains largely supportive.",
                ),
            ),
            tf(
                f"{p}-t9",
                "GCK-MODY",
                "When both mother and fetus carry a GCK mutation, insulin treatment during pregnancy is required.",
                False,
                "Mother and fetus both affected: no treatment is needed per pregnancy management table.",
                ref(
                    "TABLE 37.5 Management of GCK, HNF1A, and HNF4A During Pregnancy",
                    "Mother and fetus carry a GCK mutation: no treatment is needed",
                ),
            ),
            tf(
                f"{p}-t10",
                "Clinical Characteristics",
                "Obesity definitively excludes MODY in all patients.",
                False,
                "Obesity was historically counted against MODY, but TODAY and registry data show MODY in overweight/obese antibody-negative youth.",
                ref(
                    "Clinical Characteristics",
                    "providing evidence that monogenic diabetes occurs in overweight and obese individuals and is likely underdiagnosed in the absence of systematic assessment.",
                ),
            ),
            tf(
                f"{p}-t11",
                "TABLE 37.1",
                "Lack of ketoacidosis when insulin is omitted from treatment is a feature atypical for type 1 diabetes.",
                True,
                "Table 37.1 lists absence of DKA off insulin among features suggesting MODY over T1D.",
                ref(
                    "TABLE 37.1",
                    "Lack of ketoacidosis when insulin is omitted from treatment",
                ),
            ),
            tf(
                f"{p}-t12",
                "Introduction",
                "MODY specifically refers to autosomal-dominant monogenic diabetes including GCK, HNF1A, HNF4A, and HNF1B subtypes.",
                True,
                "Chapter defines MODY as autosomal-dominant monogenic diabetes family including the four major transcription-factor/glucokinase subtypes.",
                ref(
                    "Introduction",
                    "MODY specifically refers to a family of autosomal-dominant monogenic diabetes that includes GCK-MODY, HNF1A-MODY, HNF4A-MODY, and HNF1B-MODY.",
                ),
            ),
            tf(
                f"{p}-t13",
                "KEY POINTS",
                "Syndromic forms of diabetes account for less than 1% of children with diabetes.",
                True,
                "Key points note syndromic diabetes is <1% of pediatric diabetes; examples include MIDD and Wolfram syndrome.",
                ref(
                    "KEY POINTS",
                    "Syndromic forms of diabetes account for less than 1% of children with diabetes.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Monogenic Diabetes and Precision Medicine",
                "Assertion: Biomarker screening should precede broad monogenic genetic testing in antibody-negative diabetes with preserved C-peptide.",
                "Reason: C-peptide measurement has no role in distinguishing MODY from type 1 diabetes.",
                2,
                "Assertion true per Fig. 37.2 pathway; reason false—measurable C-peptide is a key Table 37.1 discriminator from T1D.",
                ref(
                    "TABLE 37.1",
                    "Measurable C-peptide ( $ \\geq $0.60 ng/mL [ $ \\geq $0.2 nmol/L]) in the presence of hyperglycemia",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Epidemiology",
                "Assertion: Genetically confirmed MODY is frequently missed in clinical practice.",
                "Reason: In SEARCH, nearly all patients with MODY variants had already been correctly labeled MODY before sequencing.",
                2,
                "Assertion true—only 3/47 had clinical MODY diagnosis; reason false—most were misclassified and on insulin.",
                ref(
                    "Epidemiology",
                    "Of these 47 patients identified to have a MODY variant, only 3 had a clinical diagnosis of MODY, and the majority were treated with insulin demonstrating the individual value of a precision diagnosis.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "MODY",
                "Assertion: GCK-MODY causes stable mild fasting hyperglycemia usually requiring no treatment.",
                "Reason: GCK-MODY uniformly causes severe hyperglycemia requiring immediate insulin therapy from infancy.",
                2,
                "Assertion true; reason false—GCK-MODY is mild (99–144 mg/dL) and treatment is not recommended.",
                ref(
                    "MODY",
                    "These patients have stable fasting hyperglycemia (generally in the range of 99–144 mg/dL [5.5–8.0 mmol/L]) present at birth.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "MODY",
                "Assertion: HNF1A-MODY patients may have glucosuria before diabetes onset.",
                "Reason: HNF1A has no role in renal glucose reabsorption or SGLT2 expression.",
                2,
                "Assertion true—glucosuria is hallmark; reason false—HNF1A directly controls SGLT2 expression.",
                ref(
                    "MODY",
                    "because HNF1A is a key factor for SGLT2 expression, the appearance of glucose in the urine before onset of diabetes is a hallmark of HNF1A insufficiency",
                ),
            ),
            ar(
                f"{p}-ar5",
                "MODY",
                "Assertion: HNF4A-MODY may present with neonatal hypoglycemia and increased birth weight.",
                "Reason: HNF4A-MODY is identical to GCK-MODY with no perinatal metabolic abnormalities.",
                2,
                "Assertion true (~800 g heavier, neonatal hypo); reason false—HNF4A has distinct perinatal phenotype.",
                ref(
                    "MODY",
                    "Affected individuals have been found to weigh about 800 g more at birth than their unaffected siblings, and hyperinsulinemia at birth with symptomatic neonatal hypoglycemia that resolves spontaneously may occur.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "MODY",
                "Assertion: HNF1B-MODY requires insulin rather than sulfonylurea therapy.",
                "Reason: HNF1B-MODY responds to sulfonylureas like HNF1A-MODY.",
                2,
                "Assertion true; reason false—HNF1B does not respond to sulfonylureas unlike HNF1A/HNF4A.",
                ref(
                    "MODY",
                    "Unlike the other transcription factor causes of MODY (HNF1A and HNF4A), these patients do not respond to sulfonylureas and frequently require insulin for management.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Neonatal Diabetes Mellitus",
                "Assertion: KCNJ11-related permanent neonatal diabetes can be treated with high-dose sulfonylureas.",
                "Reason: All neonatal diabetes subtypes require lifelong insulin and never respond to oral agents.",
                2,
                "Assertion true; reason false—K-ATP neonatal diabetes is sulfonylurea-responsive.",
                ref(
                    "KEY POINTS",
                    "in KCNJ11 and ABCC8 genes, which encode the subunits of the K-ATP channel and are usually responsive to high doses of sulfonylureas.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Syndromic Diabetes",
                "Assertion: MIDD results from a mitochondrial DNA point mutation.",
                "Reason: MIDD is caused solely by heterozygous nuclear GCK mutations.",
                2,
                "Assertion true (m.3243A>G); reason false—MIDD is mitochondrial, not GCK-MODY.",
                ref(
                    "Syndromic Diabetes",
                    "results from an A to G substitution at position 3243 (m.3243A>G) of the mitochondrial DNA encoding the gene for tRNA.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Syndromic Diabetes",
                "Assertion: Wolfram syndrome diabetes is typically insulin-dependent and nonautoimmune.",
                "Reason: Wolfram syndrome always presents as autoimmune type 1 diabetes with positive islet antibodies.",
                2,
                "Assertion true; reason false—WS causes insulin-dependent nonautoimmune diabetes.",
                ref(
                    "Syndromic Diabetes",
                    "Insulin-dependent nonautoimmune diabetes mellitus is the first clinical manifestation with onset at the mean age of 6 years (range 3 weeks–16 years).",
                ),
            ),
            ar(
                f"{p}-ar10",
                "GCK-MODY",
                "Assertion: Insulin may be needed in GCK-MODY pregnancy when the fetus has not inherited the mutation.",
                "Reason: Fetal genotype never influences birth weight in GCK-MODY pregnancies.",
                2,
                "Assertion true; reason false—unaffected fetuses are at macrosomia risk driving insulin therapy.",
                ref(
                    "GCK-MODY",
                    "If the fetus does not carry the GCK mutation, it will sense the maternal glucose to be high and increase insulin secretion.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Clinical Characteristics",
                "Assertion: The MODY Calculator helps prioritize patients for genetic testing.",
                "Reason: The MODY Calculator is validated for all ages and all ethnic groups without limitation.",
                2,
                "Assertion true; reason false—calculator was developed in White Europeans and applies only to diagnosis under 35 years.",
                ref(
                    "Clinical Characteristics",
                    "This calculator was developed using data from a White European population.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "KEY POINTS",
                "Assertion: Monogenic lipodystrophy syndromes may include diabetes as part of the phenotype.",
                "Reason: Lipodystrophy never causes diabetes and is excluded from monogenic diabetes panels.",
                2,
                "Assertion true per key points; reason false—commercial panels include lipodystrophy genes (e.g., LIPE, LMNA).",
                ref(
                    "KEY POINTS",
                    "Monogenic causes of lipodystrophies, insulin resistance, and obesity may also include diabetes as part of the syndrome.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "37",
        "title": "Monogenic Diabetes",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Maria V. Salguero, Marilyn Arosemena, Rochelle N. Naylor, and Louis H. Philipson",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_37_Monogenic_Diabetes.md",
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
