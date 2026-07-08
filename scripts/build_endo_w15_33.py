#!/usr/bin/env python3
"""Generate Williams 15e module w15-33 — Pathophysiology of Type 2 Diabetes Mellitus."""
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
OUT_NAME = "w15-33_Pathophysiology_of_Type_2_Diabetes_Mellitus.json"


def build() -> dict:
    p = "w15-33"
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why T2D is a global public health crisis",
                "IDF 2021 data estimate 537 million adults with diabetes worldwide, projected to 738 million by 2045—T2D accounts for 90–95% of cases and drives enormous health expenditures.",
                ref(
                    "KEY POINTS",
                    "The International Diabetes Federation estimated in 2021 that 537 million people have diabetes worldwide and that by 2045 this number will rise to 738 million.",
                ),
            ),
            note(
                f"{p}-n2",
                "Epidemiology",
                "How prediabetes defines a high-risk US population",
                "CDC 2022 estimates 96 million US adults (38% over age 20) have prediabetes by fasting glucose or HbA1c—most are at high risk of progressing to diabetes.",
                ref(
                    "Epidemiology",
                    "Based on fasting glucose or hemoglobin  $ A_{1c} $ levels, they also estimated that 96 million people (38% of adults over age 20) had prediabetes and thus are at high risk of developing diabetes.",
                ),
            ),
            note(
                f"{p}-n3",
                "Epidemiology",
                "Why Asian descent warrants T2D screening at BMI 23",
                "Southeast Asian individuals develop T2D at lower BMIs partly from greater visceral adipose stores—guidelines recommend screening when BMI exceeds 23 kg/m².",
                ref(
                    "Epidemiology",
                    "Likewise, individuals from Southeast Asia are at high risk of developing T2D at lower BMIs than other ethnicities, in part due to greater visceral adipose stores, leading to recommendations to increase screening for T2D in people of Asian descent if the BMI is above 23 kg/m $ ^{2} $.",
                ),
            ),
            note(
                f"{p}-n4",
                "Pathogenesis",
                "Why four cardinal abnormalities define T2D pathophysiology",
                "Consistent defects: peripheral insulin resistance (muscle, fat, liver), defective glucose-stimulated secretion, decreased muscle/fat glucose uptake, and increased hepatic glucose production.",
                ref(
                    "Pathogenesis",
                    "From a pathophysiologic standpoint, persons with T2D consistently demonstrate four cardinal abnormalities:",
                ),
            ),
            note(
                f"{p}-n5",
                "Pathogenesis",
                "Why insulin resistance precedes overt T2D by decades",
                "The earliest detectable abnormality in T2D-prone individuals is insulin resistance—it may antedate clinical diabetes by more than 20 years.",
                ref(
                    "Pathogenesis",
                    "What is clear is that the earliest detectable abnormality in those predisposed to T2D is insulin resistance. Indeed, insulin resistance may precede T2D by more than 20 years.",
                ),
            ),
            note(
                f"{p}-n6",
                "Pathogenesis",
                "How the β-cell failure debate frames T2D onset",
                "Controversy persists whether insulin resistance or inadequate β-cell compensation is primary—consensus holds both defects are present at clinical presentation.",
                ref(
                    "Pathogenesis",
                    "Therefore, although there is still controversy about whether insulin resistance or abnormal insulin secretion represents “the” primary defect in T2D, there is general consensus that both defects are present in most subjects with the disorder at clinical presentation.",
                ),
            ),
            note(
                f"{p}-n7",
                "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                "Why type A insulin resistance presents with acanthosis and hyperandrogenism",
                "Adolescents/young adults are often identified by acanthosis nigricans and androgen excess rather than glucose disturbances—despite severe resistance and hyperinsulinemia.",
                ref(
                    "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                    "Type A insulin resistance is defined by the presence of insulin resistance, acanthosis nigricans, and hyperandrogenism.",
                ),
            ),
            note(
                f"{p}-n8",
                "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                "How Donohue syndrome differs from Rabson-Mendenhall",
                "Donohue (leprechaunism) causes severe IUGR, dysmorphic facies, and death within 1–2 years; Rabson-Mendenhall features short stature, protuberant abdomen, and dental/nail abnormalities.",
                ref(
                    "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                    "Patients with Donohue syndrome (formerly called leprechaunism), on the other hand, have multiple early abnormalities, including severe intrauterine growth retardation, abnormal facies leading to the name leprechaunism, and death within the first 1 to 2 years of life.",
                ),
            ),
            note(
                f"{p}-n9",
                "Lipodystrophic Diabetes",
                "How leptin replacement treats generalized lipodystrophy",
                "Generalized lipodystrophy causes very low leptin and adiponectin—leptin therapy improves glycemia, reduces fatty liver, and lowers triglycerides in leptin-deficient patients.",
                ref(
                    "Lipodystrophic Diabetes",
                    "Leptin-replacement therapy improves glycemic control, decreases fatty liver disease, and decreases circulating triglyceride levels in patients with generalized lipodystrophy and leptin deficiency.",
                ),
            ),
            note(
                f"{p}-n10",
                "Insulin Receptor Substrate 1 Gene",
                "How IRS1 Gly972Arg impairs insulin signaling",
                "The first T2D-linked polymorphism (Gly972Arg in IRS-1) impairs insulin-stimulated PI3K signaling—though it contributes modestly to population risk.",
                ref(
                    "Insulin Receptor Substrate 1 Gene",
                    "Subsequent studies demonstrated that this polymorphism results in impaired insulin-stimulated phosphatidylinositol 3-kinase signaling.",
                ),
            ),
            note(
                f"{p}-n11",
                "Transcription Factor 7-Like 2 Gene",
                "Why TCF7L2 is the strongest common T2D susceptibility locus",
                "At-risk allele carriers have relative risks of 1.45 (heterozygous) and 2.41 (homozygous); variants accelerate IGT→T2D progression via reduced glucose-stimulated insulin secretion.",
                ref(
                    "Transcription Factor 7-Like 2 Gene",
                    "Compared with noncarriers, heterozygous and homozygous carriers of the at-risk alleles (38% and 7% of the population, respectively) have relative risks of 1.45 and 2.41 for development of T2D.",
                ),
            ),
            note(
                f"{p}-n12",
                "Peroxisome Proliferator-Activated Receptor  $ \\gamma $ Gene",
                "How PPARG Pro12Ala modulates T2D risk",
                "The common Pro12Ala missense variant decreases T2D risk (alanine allele RR ~0.79); homozygous Pro12 individuals are more insulin resistant with ~1.25-fold higher diabetes risk.",
                ref(
                    "Peroxisome Proliferator-Activated Receptor  $ \\gamma $ Gene",
                    "Meta-analyses show that a relatively common missense mutation Pro12Ala (P12A) in PPARG (the gene encoding PPAR $ \\gamma $2) is associated with decreased risk for T2D (estimated risk ratio for the alanine allele, 0.79).",
                ),
            ),
            note(
                f"{p}-n13",
                "Insulin Signaling",
                "How IRS-PI3K-AKT nodes mediate metabolic insulin action",
                "Insulin receptor phosphorylation activates IRS adaptor proteins → PI3K → PIP3 → AKT isoforms regulating lipid synthesis, glycogen synthesis, protein synthesis, and apoptosis.",
                ref(
                    "Insulin Signaling",
                    "Insulin receptor substrates (IRSs), phosphoinositide 3-kinase (PI3K), and AKT (also known as protein kinase B) represent three critical nodes of insulin signaling that regulate a majority of the metabolic and transcriptional effects downstream of insulin activation",
                ),
            ),
            note(
                f"{p}-n14",
                "Mechanisms of Insulin-Mediated Glucose Uptake in Muscle and Fat",
                "Why GLUT4 translocation is the key muscle/fat uptake step",
                "Insulin stimulates glucose uptake by translocating GLUT4 from intracellular pools to the cell surface—GLUT4 disruption in muscle or adipose causes insulin resistance.",
                ref(
                    "Mechanisms of Insulin-Mediated Glucose Uptake in Muscle and Fat",
                    "A primary effect of insulin in skeletal muscle and adipose tissue is to stimulate glucose uptake by translocation of glucose transporter type 4 (GLUT4) from an intracellular pool to the surface of cells",
                ),
            ),
            note(
                f"{p}-n15",
                "Insulin Regulation of Hepatic Carbohydrate Metabolism",
                "How hepatic insulin resistance drives fasting hyperglycemia",
                "Impaired suppression of hepatic glucose output correlates directly with fasting hyperglycemia—often quantitatively as large as or larger than peripheral disposal defects.",
                ref(
                    "Insulin Regulation of Hepatic Carbohydrate Metabolism",
                    "Clinically, hepatic insulin resistance plays a very important role in the fasting hyperglycemia of T2D, $ ^{158,159} $ and the impaired suppression of hepatic glucose output appears to be quantitatively similar to, or even larger than, the defect in stimulation of peripheral glucose disposal.",
                ),
            ),
            note(
                f"{p}-n16",
                "Insulin Resistance",
                "How the euglycemic clamp measures insulin sensitivity",
                "Constant insulin infusion with variable glucose to maintain euglycemia—the glucose infusion rate equals tissue glucose disposal under hyperinsulinemia (gold standard).",
                ref(
                    "Insulin Resistance",
                    "Because the individual is in steady state, the glucose infusion rate represents the rate of glucose uptake/disposal into muscle, fat, and other tissues under hyperinsulinemic conditions—that is, the insulin sensitivity of the patient.",
                ),
            ),
            note(
                f"{p}-n17",
                "Obesity and Type 2 Diabetes Mellitus",
                "Why visceral adiposity worsens insulin resistance more than subcutaneous fat",
                "Central/intraabdominal fat links more strongly to insulin resistance, ectopic liver/muscle fat, dyslipidemia, and hyperglycemia than total adiposity—subcutaneous fat may be protective.",
                ref(
                    "Obesity and Type 2 Diabetes Mellitus",
                    "Central (also referred to as intraabdominal or visceral) adiposity is more strongly linked to insulin resistance and to a number of important metabolic variables, including increased ectopic fat in liver and muscle, elevated plasma glucose, insulin, total plasma cholesterol and triglyceride concentrations, and decreased plasma high-density lipoprotein cholesterol concentration, than is total adiposity.",
                ),
            ),
            note(
                f"{p}-n18",
                "Adipose Tissue and Insulin Resistance",
                "How ectopic lipid causes lipotoxic insulin resistance",
                "When adipose storage capacity is exceeded, lipids enter muscle, liver, vascular cells, and β-cells—toxic metabolites (DAGs, ceramides) activate PKC and impair insulin signaling.",
                ref(
                    "Adipose Tissue and Insulin Resistance",
                    "This ectopic lipid accumulation occurs in myocytes, hepatocytes, vascular cells, and  $ \\beta $ cells, and can produce toxic lipid metabolites (e.g., diacylglycerols or ceramides) that trigger activation of PKC isoforms among other adaptive and maladaptive cellular responses that lead to insulin resistance.",
                ),
            ),
            note(
                f"{p}-n19",
                "Ectopic Lipid Accumulation",
                "How intramuscular triglycerides correlate with insulin resistance",
                "Insulin-stimulated muscle glucose uptake is inversely related to intramyocellular triglyceride content—first-degree T2D relatives show increased intramyocellular fat.",
                ref(
                    "Ectopic Lipid Accumulation",
                    "In muscle, insulin-stimulated glucose uptake is inversely related to the amount of intramuscular triglycerides measured by biopsy, computed tomography, and magnetic resonance imaging",
                ),
            ),
            note(
                f"{p}-n20",
                "Role of the Gut Microbiome and Metabolome in Diabetes and Insulin Resistance",
                "How the gut microbiome integrates diet and insulin resistance",
                "Gut bacteria mediate nutrient/xenobiotic metabolism, mucosal integrity, and immunomodulation—dysbiosis contributes to obesity, diabetes, metabolic syndrome, and insulin resistance.",
                ref(
                    "Role of the Gut Microbiome and Metabolome in Diabetes and Insulin Resistance",
                    "Over the past decade, it has become clear that the gut microbiome can also contribute to obesity, diabetes, metabolic syndrome, and insulin resistance in both rodents $ ^{356-358} $ and humans $ ^{359-362} $",
                ),
            ),
            note(
                f"{p}-n21",
                "Gestational Diabetes",
                "How pregnancy insulin resistance precipitates gestational diabetes",
                "Maternal insulin secretion may rise ~250% to compensate for progressive pregnancy insulin resistance—when compensation fails, gestational diabetes develops.",
                ref(
                    "Gestational Diabetes",
                    "As the pregnancy progresses and insulin resistance builds, maternal insulin secretion increases by as much as 250% to compensate. When this compensation is inadequate, gestational diabetes develops.",
                ),
            ),
            note(
                f"{p}-n22",
                "Glucocorticoid-Induced Insulin Resistance",
                "How glucocorticoids cause insulin resistance",
                "Prednisone >30 mg/day raises HbA1c in most nondiabetics—rapid hepatic glucose production via gluconeogenesis plus acute muscle IRS1 downregulation and long-term central fat redistribution.",
                ref(
                    "Glucocorticoid-Induced Insulin Resistance",
                    "Over 80% of nondiabetic individuals with rheumatoid arthritis treated with greater than 30 mg/day of prednisone have an increase in their hemoglobin  $ A_{1c} $.",
                ),
            ),
            note(
                f"{p}-n23",
                "Circadian Rhythms, Obesity, and Insulin Resistance",
                "Why sleep deprivation increases T2D risk",
                "Epidemiologic and experimental data link reduced sleep to obesity and metabolic disturbances including T2D—sleep disruption impairs insulin action and alters leptin/ghrelin.",
                ref(
                    "Circadian Rhythms, Obesity, and Insulin Resistance",
                    "There are significant epidemiologic associations in humans between reduction of sleep and increased rates of obesity and other metabolic disturbances, including T2D (Fig. 33.11).",
                ),
            ),
            note(
                f"{p}-n24",
                "Skeletal Muscle Insulin Resistance",
                "How fatty acids impair muscle glucose transport",
                "Elevated fatty acids reduce intracellular glucose and glucose-6-phosphate before glycogen falls—primarily decreasing glucose transport, challenging the classic Randle hypothesis sequence.",
                ref(
                    "Skeletal Muscle Insulin Resistance",
                    "In normal subjects, elevated fatty acids, achieved by infusion of triglyceride emulsions and heparin (which activates lipoprotein lipase resulting in the release of fatty acids into the circulation), resulted in a fall in intracellular glucose and glucose-6-phosphate concentrations that precede the fall in glycogen accumulation.",
                ),
            ),
            note(
                f"{p}-n25",
                "Epidemiology",
                "Why pediatric T2D is rising in the United States",
                "SEARCH data show T2D prevalence (per 10,000 youth age 10–19) rose from 3.4 in 2001 to 6.7 in 2017—a 95% relative increase; ~30% of newly diagnosed US children now have T2D.",
                ref(
                    "Epidemiology",
                    "Recent reports suggest almost 30% of children in the United States with newly diagnosed diabetes have T2D.",
                ),
            ),
            note(
                f"{p}-n26",
                "Pathogenesis",
                "How hyperglucagonemia and incretin defects contribute to T2D",
                "Beyond the four cardinal defects, T2D may feature hyperglucagonemia, altered incretin secretion/action, accelerated adipose lipolysis, renal glucose reabsorption changes, and CNS metabolic dysregulation.",
                ref(
                    "Pathogenesis",
                    "In addition, people with T2D may have hyperglucagonemia, alterations in incretin secretion or action, accelerated lipolysis in the fat cell, increased renal tubular reabsorption, and abnormalities in central nervous system regulation of metabolism.",
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
                "A public health analyst reviews global diabetes burden. Per IDF 2021 estimates, approximately how many adults worldwide have diabetes, and what fraction is T2D?",
                [
                    "~37 million; ~50% T2D",
                    "~537 million; 90–95% T2D",
                    "~96 million; 100% T2D",
                    "~738 million currently; 60% T2D",
                ],
                1,
                "IDF 2021: 537 million adults with diabetes; T2D is the predominant form (90–95% globally).",
                ref(
                    "Epidemiology",
                    "The International Diabetes Federation estimated in 2021 that 537 million adults age 20 to 79 years have diabetes worldwide",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Epidemiology",
                "A 42-year-old South Asian man with BMI 24 kg/m² and no symptoms asks about diabetes screening. Best approach per ethnicity-specific guidance?",
                [
                    "Defer screening until BMI ≥30",
                    "Screen now because Asian descent warrants testing above BMI 23",
                    "Screen only if fasting glucose already >126 mg/dL",
                    "No screening needed without polyuria",
                ],
                1,
                "Southeast Asian individuals are at higher T2D risk at lower BMIs; screening is recommended above BMI 23 kg/m².",
                ref(
                    "Epidemiology",
                    "leading to recommendations to increase screening for T2D in people of Asian descent if the BMI is above 23 kg/m $ ^{2} $.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Pathogenesis",
                "Which abnormality is the earliest detectable defect in individuals predisposed to T2D?",
                [
                    "Complete β-cell aplasia",
                    "Insulin resistance",
                    "Renal glycosuria only",
                    "Absent glucagon secretion",
                ],
                1,
                "Insulin resistance is the earliest detectable abnormality and may precede T2D by >20 years.",
                ref(
                    "Pathogenesis",
                    "What is clear is that the earliest detectable abnormality in those predisposed to T2D is insulin resistance.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                "A young woman has severe insulin resistance, acanthosis nigricans, and hyperandrogenism with marked hyperinsulinemia. Most likely monogenic syndrome?",
                [
                    "MODY2 (GCK mutation)",
                    "Type A insulin resistance",
                    "Donohue syndrome",
                    "KCNJ11 neonatal diabetes",
                ],
                1,
                "Type A insulin resistance is defined by insulin resistance, acanthosis nigricans, and hyperandrogenism.",
                ref(
                    "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                    "Type A insulin resistance is defined by the presence of insulin resistance, acanthosis nigricans, and hyperandrogenism.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Lipodystrophic Diabetes",
                "A patient with generalized lipodystrophy, severe fatty liver, and very low leptin has refractory hypertriglyceridemia. Evidence-based adjunctive therapy?",
                [
                    "Leptin-replacement therapy",
                    "High-dose sulfonylureas only",
                    "Growth hormone to increase fat mass",
                    "Complete insulin withdrawal",
                ],
                0,
                "Leptin replacement improves glycemic control, fatty liver, and triglycerides in generalized lipodystrophy with leptin deficiency.",
                ref(
                    "Lipodystrophic Diabetes",
                    "Leptin-replacement therapy improves glycemic control, decreases fatty liver disease, and decreases circulating triglyceride levels in patients with generalized lipodystrophy and leptin deficiency.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Transcription Factor 7-Like 2 Gene",
                "A heterozygous carrier of a TCF7L2 at-risk allele asks about diabetes risk compared with a noncarrier. Approximate relative risk?",
                [
                    "~0.5 (protective)",
                    "~1.45",
                    "~5.0",
                    "No increased risk",
                ],
                1,
                "Heterozygous TCF7L2 at-risk allele carriers have RR ~1.45; homozygous carriers ~2.41.",
                ref(
                    "Transcription Factor 7-Like 2 Gene",
                    "heterozygous and homozygous carriers of the at-risk alleles (38% and 7% of the population, respectively) have relative risks of 1.45 and 2.41 for development of T2D.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Peroxisome Proliferator-Activated Receptor  $ \\gamma $ Gene",
                "Which PPARG variant is associated with decreased T2D risk?",
                [
                    "Pro12Ala (alanine allele protective)",
                    "Complete loss-of-function in all carriers",
                    "C161→T always protective in all ethnicities",
                    "Pro12 homozygosity is protective",
                ],
                0,
                "Pro12Ala in PPARG decreases T2D risk (alanine allele RR ~0.79); Pro12 homozygotes are more insulin resistant.",
                ref(
                    "Peroxisome Proliferator-Activated Receptor  $ \\gamma $ Gene",
                    "a relatively common missense mutation Pro12Ala (P12A) in PPARG (the gene encoding PPAR $ \\gamma $2) is associated with decreased risk for T2D (estimated risk ratio for the alanine allele, 0.79).",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Insulin Signaling",
                "Blocking which downstream node in mice causes insulin resistance and diabetes?",
                [
                    "AKT2 disruption",
                    "GLUT1 in brain only",
                    "Complete insulin gene deletion in liver only",
                    "SIRT3 overexpression only",
                ],
                0,
                "AKT2 knockout mice develop insulin resistance and diabetes; AKT1 mainly affects growth.",
                ref(
                    "Insulin Signaling",
                    "whereas disruption of AKT2 results in insulin resistance and diabetes in mice.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Mechanisms of Insulin-Mediated Glucose Uptake in Muscle and Fat",
                "In insulin-resistant skeletal muscle, what is typically preserved vs impaired?",
                [
                    "GLUT4 protein number is increased; translocation is enhanced",
                    "GLUT4 number is largely unchanged; insulin-stimulated translocation is disrupted",
                    "Both GLUT4 number and translocation are abolished",
                    "Only hepatic GLUT2 is affected",
                ],
                1,
                "Muscle GLUT4 transporter number is usually unchanged in insulin resistance—the defect is impaired insulin-mediated translocation.",
                ref(
                    "Mechanisms of Insulin-Mediated Glucose Uptake in Muscle and Fat",
                    "it appears that the number of glucose transporters in skeletal muscle of insulin-resistant persons is not changed, but the ability of insulin to effect GLUT4 translocation is disrupted.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Insulin Regulation of Hepatic Carbohydrate Metabolism",
                "A T2D patient has elevated fasting glucose with increased hepatic glucose output. Which relationship is supported clinically?",
                [
                    "Fasting hyperglycemia correlates with increased hepatic glucose production",
                    "Hepatic output is always normal in T2D",
                    "Metformin worsens hepatic glucose production",
                    "Insulin never suppresses hepatic glycogenolysis",
                ],
                0,
                "Hepatic insulin resistance is central to fasting hyperglycemia; increased hepatic glucose output relates directly to fasting glucose.",
                ref(
                    "Insulin Regulation of Hepatic Carbohydrate Metabolism",
                    "There is a direct relationship between increased hepatic glucose output and fasting hyperglycemia",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Insulin Resistance",
                "Which test is the gold standard for measuring insulin sensitivity in an individual?",
                [
                    "Fasting C-peptide alone",
                    "Hyperinsulinemic euglycemic clamp",
                    "Random urinary glucose",
                    "Serum fructosamine only",
                ],
                1,
                "The hyperinsulinemic euglycemic clamp is the gold standard—glucose infusion rate equals disposal under hyperinsulinemia.",
                ref(
                    "Insulin Resistance",
                    "The gold standard for determining insulin sensitivity/resistance in an individual is a hyperinsulinemic euglycemic clamp.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Obesity and Type 2 Diabetes Mellitus",
                "Compared with subcutaneous adiposity, intraabdominal fat is more strongly associated with:",
                [
                    "Higher HDL cholesterol",
                    "Insulin resistance and ectopic fat in liver/muscle",
                    "Lower triglycerides",
                    "Improved glucose tolerance independent of BMI",
                ],
                1,
                "Visceral/central adiposity links more strongly to insulin resistance, ectopic fat, dyslipidemia, and hyperglycemia than total fat.",
                ref(
                    "Obesity and Type 2 Diabetes Mellitus",
                    "Central (also referred to as intraabdominal or visceral) adiposity is more strongly linked to insulin resistance",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Adipose Tissue and Insulin Resistance",
                "When adipose storage capacity is exceeded, what pathologic consequence drives insulin resistance?",
                [
                    "Ectopic lipid accumulation with toxic DAG/ceramide signaling",
                    "Complete absence of all adipose tissue always",
                    "Increased brown adipose thermogenesis only",
                    "Abolition of all lipolysis",
                ],
                0,
                "Overflow lipids deposit in muscle, liver, β-cells, etc., producing lipotoxic metabolites that impair insulin signaling.",
                ref(
                    "Adipose Tissue and Insulin Resistance",
                    "This ectopic lipid accumulation occurs in myocytes, hepatocytes, vascular cells, and  $ \\beta $ cells, and can produce toxic lipid metabolites (e.g., diacylglycerols or ceramides)",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Ectopic Lipid Accumulation",
                "First-degree relatives of T2D patients show which muscle finding correlating with insulin resistance?",
                [
                    "Decreased intramyocellular triglyceride",
                    "Increased intramyocellular fat",
                    "Absent CPT1 expression only",
                    "Doubled GLUT4 protein content",
                ],
                1,
                "First-degree relatives have increased intramyocellular fat correlating with insulin resistance.",
                ref(
                    "Ectopic Lipid Accumulation",
                    "First-degree relatives of T2D patients have an increase in intramycellular fat, and in this group there is also a correlation with insulin resistance.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Role of the Gut Microbiome and Metabolome in Diabetes and Insulin Resistance",
                "Which intervention class is discussed as a potential microbiome-targeted T2D strategy?",
                [
                    "Prebiotics, probiotics, or fecal microbiome transfer",
                    "Routine broad-spectrum antibiotics for all prediabetes",
                    "Complete bowel rest indefinitely",
                    "Elimination of all dietary fiber",
                ],
                0,
                "Therapeutic options include prebiotics, probiotics, and fecal transfer to modify gut microbiota.",
                ref(
                    "Role of the Gut Microbiome and Metabolome in Diabetes and Insulin Resistance",
                    "ranging from administration of prebiotics (nutrients that change the composition of gut microbiota), probiotics (mixtures of bacteria themselves), and even transplant of a healthy microbiome by fecal transfer.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Gestational Diabetes",
                "By how much may maternal insulin secretion increase during pregnancy to compensate for insulin resistance?",
                [
                    "~25%",
                    "Up to ~250%",
                    "No change",
                    "~1000%",
                ],
                1,
                "Maternal insulin secretion may increase by as much as 250% as pregnancy progresses.",
                ref(
                    "Gestational Diabetes",
                    "maternal insulin secretion increases by as much as 250% to compensate.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Glucocorticoid-Induced Insulin Resistance",
                "A rheumatoid arthritis patient starts prednisone 40 mg daily. Expected metabolic effect in most nondiabetic individuals?",
                [
                    "Decreased hemoglobin A1c",
                    "Increased hemoglobin A1c",
                    "No glycemic change",
                    "Immediate hypoglycemia requiring dextrose",
                ],
                1,
                "Over 80% of nondiabetics on >30 mg/day prednisone show increased HbA1c.",
                ref(
                    "Glucocorticoid-Induced Insulin Resistance",
                    "Over 80% of nondiabetic individuals with rheumatoid arthritis treated with greater than 30 mg/day of prednisone have an increase in their hemoglobin  $ A_{1c} $.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Circadian Rhythms, Obesity, and Insulin Resistance",
                "In prediabetic men, 5 weeks of 6-hour vs 12-hour time-restricted eating on isocaloric diet improved:",
                [
                    "Insulin sensitivity and blood pressure without significant weight loss",
                    "Only hair growth",
                    "Hepatic insulin sensitivity but worsened BP",
                    "Nothing unless paired with bariatric surgery",
                ],
                0,
                "Early TRE (6 vs 12 h eating window) improved insulin sensitivity and BP in prediabetic men without major weight change.",
                ref(
                    "Circadian Rhythms, Obesity, and Insulin Resistance",
                    "a 5-week dietary intervention of TRE using a duration of 6 hours versus 12 hours with an isocaloric diet improved insulin sensitivity and blood pressure in prediabetic men without significant weight changes.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Skeletal Muscle Insulin Resistance",
                "During hyperinsulinemic clamp studies in T2D, the primary defect in glucose disposal is:",
                [
                    "Excess oxidative glucose disposal",
                    "Deficiency in nonoxidative disposal related to impaired glycogen synthesis/uptake",
                    "Isolated renal glucose loss",
                    "Increased basal glucagon only",
                ],
                1,
                "Muscle insulin resistance manifests as deficient nonoxidative glucose disposal—secondary to decreased insulin-stimulated uptake/glycogen synthesis.",
                ref(
                    "Skeletal Muscle Insulin Resistance",
                    "in insulin-resistant people (with and without T2D), there is a deficiency in the nonoxidative disposal of glucose related primarily to a defect in glycogen synthesis, which itself is secondary to a decrease in insulin-stimulated glucose uptake",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Genetics of the Polygenic Forms of Type 2 Diabetes Mellitus",
                "Collectively, identified T2D genetic variants account for what fraction of familial risk?",
                [
                    "~50–70%",
                    "~5–10%",
                    "~90%",
                    "100%",
                ],
                1,
                "Although >500 variants are linked to T2D, they collectively explain only ~5–10% of familial risk—highlighting epigenetic/environmental contributions.",
                ref(
                    "KEY POINTS",
                    "these variants collectively account for 5% to 10% of the overall familial risk for disease, supporting the importance of epigenetic effects, as well as environmental influences.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "KATP Channel Genes: KCNJ11 and ABCC8",
                "The KCNJ11 E23K variant increases typical adult-onset T2D risk by approximately:",
                [
                    "~2% average (~13% per allele; KK homozygote highest)",
                    "~200%",
                    "No effect",
                    "Only in neonatal diabetes",
                ],
                0,
                "Glu23Lys in KCNJ11 increases T2D risk ~13% on average; KK homozygotes at greatest risk (RR 1.28).",
                ref(
                    "KATP Channel Genes: KCNJ11 and ABCC8",
                    "A missense mutation Glu23Lys (E23K) in KCNJ11 has also been associated with increased risk of typical adult-onset T2D by an average of 13%, and the KK homozygote is at greatest risk (relative risk, 1.28).",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Hyperinsulinemia and Insulin Resistance",
                "Sustained physiologic hyperinsulinemia in healthy volunteers primarily impairs:",
                [
                    "Nonoxidative glucose disposal and glycogen synthase activation",
                    "Renal glucose excretion only",
                    "Glucagon gene transcription only",
                    "Brown adipose UCP1 expression only",
                ],
                0,
                "24–72 h hyperinsulinemia inhibits insulin-stimulated nonoxidative disposal and glycogen synthase—hyperinsulinemia can cause resistance.",
                ref(
                    "Hyperinsulinemia and Insulin Resistance",
                    "24 and 72 hours of sustained physiologic hyperinsulinemia in normal persons specifically inhibited the ability of insulin to increase nonoxidative glucose disposal in association with an impaired ability of insulin to stimulate glycogen synthase",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Innate Immunity",
                "TLR4 signaling in response to saturated fatty acids contributes to insulin resistance because:",
                [
                    "Polyunsaturated fatty acids activate TLR4",
                    "Saturated fatty acids activate TLR2/TLR4; TLR4 disruption protects mice",
                    "TLR4 only responds to viral RNA",
                    "Fatty acids always improve insulin signaling",
                ],
                1,
                "Saturated fatty acids activate TLR2/TLR4 innate inflammatory pathways causing insulin resistance; genetic TLR4 disruption is protective in mice.",
                ref(
                    "Innate Immunity",
                    "Toll-like receptors, especially TLR2 and TLR4, which normally respond to bacterial cell wall lipids to induce the innate inflammatory response, are also activated by circulating saturated fatty acids.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Glucotoxicity, Glucosamine",
                "Chronic hyperglycemia can worsen insulin resistance partly through:",
                [
                    "Hexosamine pathway flux impairing GLUT4 translocation",
                    "Complete abolition of hepatic gluconeogenesis",
                    "Increased muscle GLUT4 translocation",
                    "Decreased glucosamine production always",
                ],
                0,
                "Glucosamine/hexosamine pathway activation induces insulin resistance and disrupts insulin-stimulated GLUT4 translocation.",
                ref(
                    "Glucotoxicity, Glucosamine",
                    "Hexosamines, such as glucosamine, when incubated with adipose tissue, induce insulin resistance in fat cells $ ^{423} $ and in skeletal muscle.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Epidemiology",
                "In the United States, Native American adults have approximately what diabetes prevalence compared with non-Hispanic White adults (2018–2019 data)?",
                [
                    "Equal (~7%)",
                    "About twice as high (14.5% vs 7.4%)",
                    "Tenfold higher",
                    "Near zero",
                ],
                1,
                "US T2D prevalence varies by race/ethnicity—Native American populations ~14.5% vs non-Hispanic White ~7.4%.",
                ref(
                    "Epidemiology",
                    "Native American populations having twice the rate of diabetes at 14.5% than non-Hispanic White patients at 7.4%",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Pathogenesis",
                "Which life stages/conditions add insulin resistance and increase β-cell secretory burden?",
                [
                    "Puberty, pregnancy, sedentary lifestyle, and weight gain",
                    "Only advanced age >80 years",
                    "Strict caloric restriction only",
                    "Cold exposure only",
                ],
                0,
                "Puberty, pregnancy, inactivity, and weight gain all worsen insulin resistance and stress β-cell compensation.",
                ref(
                    "Pathogenesis",
                    "puberty, pregnancy, a sedentary lifestyle, and weight gain all add to increased T2D risk.",
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
                "Type 2 diabetes accounts for 90% to 95% of diabetes cases worldwide.",
                True,
                "T2D is the predominant form globally per chapter epidemiology.",
                ref(
                    "KEY POINTS",
                    "T2D is the predominant form of diabetes worldwide, accounting for 90% to 95% of cases.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Epidemiology",
                "In the United States, 8.5 million people with diabetes (23.0%) were undiagnosed per CDC 2022 estimates.",
                True,
                "Of 37.3 million with diabetes, 8.5 million were undiagnosed.",
                ref(
                    "Epidemiology",
                    "8.5 million of them (23.0%) were undiagnosed.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Pathogenesis",
                "At clinical presentation of T2D, most patients have both insulin resistance and abnormal insulin secretion.",
                True,
                "General consensus: both defects coexist at presentation despite debate on which is primary.",
                ref(
                    "Pathogenesis",
                    "there is general consensus that both defects are present in most subjects with the disorder at clinical presentation.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                "Some patients with insulin receptor mutations require insulin doses exceeding 10,000 U/day without glycemic response.",
                True,
                "Severe receptor mutations can produce extreme insulin resistance unresponsive to massive insulin doses.",
                ref(
                    "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                    "others have presented with hyperglycemia, which fails to respond to insulin therapy, sometimes in doses exceeding 10,000 U/day.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Lipodystrophic Diabetes",
                "The majority of partial lipodystrophy patients respond well to leptin-replacement therapy.",
                False,
                "Leptin therapy helps generalized lipodystrophy with leptin deficiency; most partial lipodystrophy patients do not respond.",
                ref(
                    "Lipodystrophic Diabetes",
                    "The majority of these patients do not respond to leptin-replacement therapy.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Mechanisms of Insulin-Mediated Glucose Uptake in Muscle and Fat",
                "Exercise-regulated muscle glucose uptake via TBC1D1/AMPK remains intact in patients with T2D.",
                True,
                "AMPK-phosphorylated TBC1D1 mediates exercise-stimulated uptake, which is preserved in T2D unlike insulin-stimulated GLUT4 translocation.",
                ref(
                    "Mechanisms of Insulin-Mediated Glucose Uptake in Muscle and Fat",
                    "TBC1D1, however, is also phosphorylated by adenosine monophosphate-activated kinase (AMPK), and that appears to play a key role in exercise-regulated increases in muscle glucose uptake, which remain intact in patients with T2D.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Insulin Resistance",
                "HOMA-IR correlates favorably with clamp-measured insulin resistance with Rs ~0.88.",
                True,
                "Fasting glucose/insulin-derived HOMA-IR correlates well with clamp estimates for cohort/outpatient use.",
                ref(
                    "Insulin Resistance",
                    "HOMA-IR correlates favorably with insulin resistance estimated from the hyperinsulinemic euglycemic clamp with an R $ _s $ of 0.88.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Hyperinsulinemia and Insulin Resistance",
                "Hyperinsulinemia itself can cause insulin resistance by downregulating receptors and desensitizing postreceptor pathways.",
                True,
                "Chronic hyperinsulinemia feeds back to impair insulin signaling—relevant to obesity and compensation.",
                ref(
                    "Hyperinsulinemia and Insulin Resistance",
                    "Hyperinsulinemia itself can cause insulin resistance. Elevated concentrations of insulin downregulate insulin receptors and desensitize postreceptor pathways.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Gestational Diabetes",
                "Gestational diabetes is a significant risk factor for future development of T2D.",
                True,
                "GDM generally resolves postpartum but predicts later T2D risk.",
                ref(
                    "Gestational Diabetes",
                    "it is considered a significant risk factor for the future development of T2D.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Role of the Gut Microbiome and Metabolome in Diabetes and Insulin Resistance",
                "Low-dose antibiotics early in life may predispose to obesity and glucose intolerance by perturbing microbiome development.",
                True,
                "Mouse studies show early low-dose antibiotics can alter microbiome and metabolic outcomes.",
                ref(
                    "Role of the Gut Microbiome and Metabolome in Diabetes and Insulin Resistance",
                    "administration of low-dose antibiotics early in life may predispose to obesity and glucose intolerance by perturbing the development of a normal microbiome.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Ectopic Lipid Accumulation",
                "Exercise training always decreases intramuscular triglyceride content.",
                False,
                "Trained muscle can have increased triglyceride content yet improved insulin sensitivity—dissociation from resistance.",
                ref(
                    "Ectopic Lipid Accumulation",
                    "exercise training is associated with increased muscle triglyceride content, $ ^{270} $ and chronic exercise increases insulin sensitivity",
                ),
            ),
            tf(
                f"{p}-t12",
                "Genetics of the Polygenic Forms of Type 2 Diabetes Mellitus",
                "Individual T2D-associated polymorphisms typically confer odds ratios between 1.10 and 1.45.",
                True,
                "GWAS hits individually confer modest risk increments; polygenic burden matters.",
                ref(
                    "Diabetes Genes Identified by Genome-Wide Association Studies",
                    "Persons with these individual polymorphisms have odds ratios between 1.10 and 1.45 when compared with individuals who do not have the at-risk polymorphisms.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Epidemiology",
                "Pediatric T2D prevalence among US youth aged 10–19 years approximately doubled between 2001 and 2017.",
                True,
                "Prevalence rose from 3.4 to 6.7 per 10,000 (95% relative increase).",
                ref(
                    "Epidemiology",
                    "increased from 3.4 in 2001 to 6.7 in 2017, representing a 95% relative increase over this 16-year period.",
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
                "Assertion: More than 500 genetic variants have been linked with T2D risk.",
                "Reason: These variants collectively explain most of the familial risk for T2D.",
                2,
                "Assertion true; reason false—variants account for only ~5–10% of familial risk.",
                ref(
                    "KEY POINTS",
                    "these variants collectively account for 5% to 10% of the overall familial risk for disease",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Pathogenesis",
                "Assertion: Insulin resistance is the earliest detectable abnormality in T2D-prone individuals.",
                "Reason: Insulin resistance always appears only after overt hyperglycemia develops.",
                2,
                "Assertion true; reason false—insulin resistance may precede T2D by >20 years.",
                ref(
                    "Pathogenesis",
                    "Indeed, insulin resistance may precede T2D by more than 20 years.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                "Assertion: Donohue syndrome is associated with severe intrauterine growth retardation and early death.",
                "Reason: Donohue syndrome is diagnosed primarily in obese adults with mild hyperglycemia.",
                2,
                "Assertion true; reason false—Donohue presents neonatally with IUGR and lethality within 1–2 years.",
                ref(
                    "Monogenic Forms of Diabetes Associated With Insulin Resistance",
                    "severe intrauterine growth retardation, abnormal facies leading to the name leprechaunism, and death within the first 1 to 2 years of life.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Insulin Signaling",
                "Assertion: Insulin receptors are ubiquitously expressed.",
                "Reason: Insulin action is identical in all tissues because receptor expression is uniform in function.",
                2,
                "Assertion true; reason false—receptors are widespread but insulin action is highly tissue-specific.",
                ref(
                    "Insulin Signaling",
                    "Insulin receptors are ubiquitously expressed, yet insulin action is highly tissue-specific due to the varied composition of downstream targets of insulin signaling.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Mechanisms of Insulin-Mediated Glucose Uptake in Muscle and Fat",
                "Assertion: AS160/TBC1D4 is a Rab GAP that restrains GLUT4 translocation until insulin inhibits its activity.",
                "Reason: AS160 phosphorylation by AKT promotes GLUT4 retention intracellularly.",
                2,
                "Assertion true; reason false—AKT phosphorylation suppresses AS160 GAP activity, relieving inhibition of GLUT4 vesicle translocation.",
                ref(
                    "Mechanisms of Insulin-Mediated Glucose Uptake in Muscle and Fat",
                    "AS160 activity is suppressed by AKT phosphorylation in response to insulin stimulation and mediates translocation of GLUT4-containing vesicles to the plasma membrane",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Insulin Regulation of Hepatic Carbohydrate Metabolism",
                "Assertion: Insulin suppresses hepatic glucose production.",
                "Reason: Glucagon is dominant over insulin in regulating hepatic glucose output.",
                2,
                "Assertion true; reason false—insulin is dominant over glucagon in suppressing hepatic glucose production and glycogenolysis.",
                ref(
                    "Insulin Regulation of Hepatic Carbohydrate Metabolism",
                    "The production of glucose by the liver is regulated primarily by a balance between the actions of insulin to suppress glucose production and glucagon to activate glucose production, with insulin being dominant over glucagon",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Transcription Factor 7-Like 2 Gene",
                "Assertion: TCF7L2 variants increase progression from IGT to T2D.",
                "Reason: TCF7L2 effects are mediated solely by increased hepatic glucose production without any secretory defect.",
                2,
                "Assertion true; reason false—TCF7L2 risk associates with reduced glucose-stimulated insulin secretion.",
                ref(
                    "Transcription Factor 7-Like 2 Gene",
                    "specific polymorphisms in TCF7L2 increase the risk of progression from impaired glucose tolerance to T2D, and this effect is associated with a reduction of glucose-stimulated insulin secretion.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Obesity and Type 2 Diabetes Mellitus",
                "Assertion: Intraabdominal adiposity is more strongly linked to insulin resistance than total adiposity.",
                "Reason: Subcutaneous fat is always more lipolytic and pro-inflammatory than visceral fat.",
                2,
                "Assertion true; reason false—abdominal fat is more lipolytically active; subcutaneous fat may be protective and releases more adiponectin.",
                ref(
                    "Obesity and Type 2 Diabetes Mellitus",
                    "Indeed, some studies suggest subcutaneous fat may actually be protective against insulin resistance.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Adipose Tissue and Insulin Resistance",
                "Assertion: Obesity-associated adipose inflammation attracts proinflammatory macrophages releasing TNFα.",
                "Reason: Obesity exclusively increases anti-inflammatory M2 macrophages without cytokine release.",
                2,
                "Assertion true; reason false—M1 macrophages and cytokines like TNFα drive local/systemic inflammation.",
                ref(
                    "Adipose Tissue and Insulin Resistance",
                    "These and possibly other cytokines attract proinflammatory macrophages (M1 type), which release factors such as tumor necrosis factor  $ \\alpha $ (TNF $ \\alpha $)",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Gestational Diabetes",
                "Assertion: Insulin resistance is a normal consequence of pregnancy.",
                "Reason: Pregnancy insulin resistance is caused solely by gestational weight gain without placental factors.",
                2,
                "Assertion true; reason false—placenta-derived hormones/exosomes/miRNAs drive resistance; euglycemia returns days after delivery.",
                ref(
                    "Gestational Diabetes",
                    "The driver of insulin resistance in pregnancy is not simply the weight gain of pregnancy, as euglycemia generally returns within days of delivery. Rather, placenta-derived factors are believed to drive both the insulin resistance of pregnancy",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Role of the Gut Microbiome and Metabolome in Diabetes and Insulin Resistance",
                "Assertion: Gut microbiota can contribute to obesity and insulin resistance.",
                "Reason: Adult gut microbiome composition is fixed at birth and cannot be remodeled by diet or disease.",
                2,
                "Assertion true; reason false—microbiome is seeded at birth but can be remodeled by diet, antibiotics, and disease.",
                ref(
                    "Role of the Gut Microbiome and Metabolome in Diabetes and Insulin Resistance",
                    "then becomes relatively stable in adulthood, although it can be remodeled by diet, antibiotics, and a variety of disease states.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Circadian Rhythms, Obesity, and Insulin Resistance",
                "Assertion: Time-restricted feeding can improve metabolic health in rodent high-fat diet models.",
                "Reason: Time-restricted feeding requires reduced total caloric intake to prevent obesity in mice.",
                2,
                "Assertion true; reason false—8-hour feeding windows prevented obesity and insulin resistance despite equivalent calories.",
                ref(
                    "Circadian Rhythms, Obesity, and Insulin Resistance",
                    "limiting the same caloric intake to an 8-hour period prevents obesity, hyperinsulinemia, hepatic steatosis, and inflammatory markers, despite equivalent caloric intake.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "33",
        "title": "Pathophysiology of Type 2 Diabetes Mellitus",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "C. Ronald Kahn, Heather A. Ferris, and Brian T. O'Neill",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_33_Pathophysiology_of_Type_2_Diabetes_Mellitus.md",
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
