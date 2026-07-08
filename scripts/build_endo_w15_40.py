#!/usr/bin/env python3
"""Generate Williams 15e module w15-40 — Obesity and Neuroendocrine Control of Energy Stores."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-40"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-40_Obesity_and_Neuroendocrine_Control_of_Energy_Stores.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why BMI stratifies obesity risk but healthy ranges differ by ethnicity",
                "BMI permits population risk stratification, yet thresholds for normal weight, overweight, and obesity vary between European and Asian populations.",
                ref(
                    "KEY POINTS",
                    "Body mass index permits stratification of risk for obesity, but healthy ranges are specific to different ethnic groups.",
                ),
            ),
            note(
                f"{p}-n2",
                "Definition of Obesity",
                "How visceral fat confers higher metabolic risk than subcutaneous fat at the same BMI",
                "BMI does not distinguish fat distribution; intraabdominal visceral adiposity imparts greater cardiometabolic risk than subcutaneous depots, so two people with identical BMI may differ markedly in risk.",
                ref(
                    "Definition of Obesity",
                    "BMI calculations also do not differentiate body fat distribution, with increased metabolic disease risk imparted from intraabdominal, visceral fat than from subcutaneous fat.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why the modern obesity epidemic reflects genes interacting with environment",
                "Human genetics have not changed substantially since the 1960s rise in obesity; environmental shifts—especially industrialized, calorie-dense diets—interact with inherited susceptibility.",
                ref(
                    "KEY POINTS",
                    "Both environmental and genetic factors contribute to energy homeostasis.",
                ),
            ),
            note(
                f"{p}-n4",
                "Physiology of Body Energy Homeostasis",
                "How energy homeostasis integrates peripheral and central signals",
                "Weight balance requires coordinated input from liver, brain, adipose tissue, muscle, gut nutrients, and postprandial neural/hormonal cues—not a single isolated pathway.",
                ref(
                    "Physiology of Body Energy Homeostasis",
                    "Control of energy homeostasis requires physiologic integration of biologic signals from organs, such as the liver and brain, and from fat, muscle, and gut; nutrient-related signals; and postprandial neural and hormonal influences.",
                ),
            ),
            note(
                f"{p}-n5",
                "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                "Why arcuate NPY/AgRP neurons drive hunger",
                "Pro-orexigenic arcuate neurons expressing NPY and AgRP increase food intake when stimulated; they oppose POMC/CART satiety neurons in inverse regulation of energy storage.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                    "Pro-orexigenic neurons in the arcuate nucleus, which express neuropeptide Y (NPY) and agouti-related protein (AgRP), and appetite-inhibiting neurons, which express the pro-opiomelanocortin (POMC) gene",
                ),
            ),
            note(
                f"{p}-n6",
                "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                "How α-MSH acting on MC4R suppresses feeding",
                "POMC is processed to α-MSH, which inhibits eating; MC4R downstream of arcuate melanocortin signaling is critical—MC4R mutations are the most common monogenic obesity cause in humans.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                    "The precursor protein POMC is processed to  $ \\alpha $MSH, which suppresses feeding.",
                ),
            ),
            note(
                f"{p}-n7",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "Why leptin is required for weight maintenance but ineffective in common obesity",
                "Leptin absence causes morbid obesity, yet most obese individuals have high circulating leptin with attenuated downstream signaling—leptin resistance rather than deficiency.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "Although leptin is necessary for weight maintenance, it is not sufficient.",
                ),
            ),
            note(
                f"{p}-n8",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "How ghrelin promotes meal initiation and weight gain",
                "Stomach-derived ghrelin rises before meals, acutely increases intake, and chronic administration causes obesity in rodents.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "Ghrelin is a potent orexigenic hormone derived from the stomach that increases before meals and decreases after feeding.",
                ),
            ),
            note(
                f"{p}-n9",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "How GLP-1 and PYY from intestinal L cells induce satiety",
                "GLP-1 and PYY are co-secreted postprandially; central GLP-1 opposes orexigenic peptides including MCH and NPY.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "GLP1 and PYY are co-secreted after a meal and induce satiety.",
                ),
            ),
            note(
                f"{p}-n10",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "Why dual GIP/GLP-1 agonism (tirzepatide) enhances weight loss beyond GLP-1 alone",
                "GIP receptor ligands alone poorly suppress intake, but combined GIP/GLP-1-receptor agonism produces marked appetite suppression and weight loss, as seen with tirzepatide.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "In contrast, when combined with GLP1-receptor agonists in a single peptide, appetite suppression and weight loss are enhanced, as seen with tirzepatide (discussed later).",
                ),
            ),
            note(
                f"{p}-n11",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "How amylin limits meal size and restores leptin sensitivity",
                "Amylin co-secreted with insulin slows gastric emptying peripherally and stimulates hindbrain anorexia centrally; long-acting amylin analogues are being combined with semaglutide in trials.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "Amylin is a B-cell hormone co-secreted with insulin. It slows gastric emptying and thereby reduces meal size.",
                ),
            ),
            note(
                f"{p}-n12",
                "Energy Expenditure",
                "How total daily energy expenditure is partitioned",
                "Resting energy expenditure (~70%), physical activity (~20%), and thermic effect of food (~10%) together determine daily energy output.",
                ref(
                    "Energy Expenditure",
                    "Resting energy expenditure accounts for approximately 70% of total energy expenditure.",
                ),
            ),
            note(
                f"{p}-n13",
                "Body Weight Set-Point",
                "Why set-point theory explains stable weight over years",
                "Many individuals maintain constant weight for decades, supporting physiologic adaptations that balance intake and expenditure around a defended weight.",
                ref(
                    "Body Weight Set-Point",
                    "Many individuals will maintain a constant weight over years and even decades, supporting the theory that there is a set-point regulating food intake and energy expenditure so that weight stays constant.",
                ),
            ),
            note(
                f"{p}-n14",
                "Body Weight Set-Point",
                "How hypocaloric feeding reduces energy expenditure during weight loss",
                "Energy restriction lowers expenditure by ~15–20% daily in obese individuals—partly beyond what body-composition change alone would predict.",
                ref(
                    "Body Weight Set-Point",
                    "Hypocaloric feeding reduces energy expenditure by an average of 8 kcal/kg of lean body mass in obese individuals but only 6 kcal/kg of lean body mass in normal-weight individuals, amounting to a 15% to 20% daily decrease.",
                ),
            ),
            note(
                f"{p}-n15",
                "Environmental Effects in High-Risk Populations",
                "Why urbanized Pima Indians developed epidemic obesity and diabetes",
                "Arizona Pima exposed to high-fat modern diets and sedentary lifestyles have far higher obesity/diabetes rates than Mexican kindred maintaining traditional diet and physical activity.",
                ref(
                    "Environmental Effects in High-Risk Populations",
                    "These rural Pima Indians eat a traditional diet and are physically active as farmers and sawmill workers; they have a much lower incidence of obesity and diabetes than their Arizona kindred.",
                ),
            ),
            note(
                f"{p}-n16",
                "Monogenic Causes of Obesity",
                "Why MC4R is the most common monogenic obesity gene",
                "α-MSH from arcuate POMC neurons inhibits appetite via MC4R; loss-of-function MC4R mutations impair this melanocortin brake on feeding.",
                ref(
                    "Monogenic Causes of Obesity",
                    "The effect of  $ \\alpha $MSH released from the arcuate nucleus on MC4R inhibits appetite, so a functional MC4R is essential to maintain normal body weight.",
                ),
            ),
            note(
                f"{p}-n17",
                "Monogenic Causes of Obesity",
                "How congenital leptin deficiency presents and responds to replacement",
                "Absolute leptin deficiency causes massive early obesity, hyperphagia, and hypogonadism; exogenous leptin normalizes weight, permits puberty, and restores insulin sensitivity—but not in leptin receptor deficiency.",
                ref(
                    "Monogenic Causes of Obesity",
                    "The handful of individuals with leptin deficiency can be treated with exogenous leptin, which normalizes weight and food intake, permits puberty,",
                ),
            ),
            note(
                f"{p}-n18",
                "Monogenic Causes of Obesity",
                "Why POMC mutations cause obesity with adrenal insufficiency",
                "POMC loss eliminates ACTH and α-MSH products—patients may present with adrenal insufficiency, red hair, and pale skin from reduced melanocyte stimulation.",
                ref(
                    "Monogenic Causes of Obesity",
                    "The presentation of patients with POMC mutations is typically secondary to adrenal insufficiency from low levels of ACTH, usually observed in early life, and they tend to have red hair and pale skin from reduced melanocyte pigment production attributable to decreased  $ \\alpha $MSH production.",
                ),
            ),
            note(
                f"{p}-n19",
                "Single-Minded Homolog 1 (SIM1) Gene Mutation",
                "How SIM1 disruption can cause severe early obesity",
                "SIM1 encodes a transcription factor for paraventricular/supraoptic nucleus development; chromosomal disruption causing haploinsufficiency may stimulate food intake with normal resting energy expenditure.",
                ref(
                    "Single-Minded Homolog 1 (SIM1) Gene Mutation",
                    "It is likely that this mutation altered energy balance in this patient by stimulating food intake, because measured resting energy expenditure was normal.",
                ),
            ),
            note(
                f"{p}-n20",
                "Obesity Syndromes",
                "Why Prader-Willi syndrome causes morbid obesity with hyperphagia",
                "Prader-Willi results from absent paternal chromosome 15q11.2-q12 segment, linking MAGEL2 and related genes to a syndrome of obesity, short stature, hypogonadism, and cognitive impairment.",
                ref(
                    "Obesity Syndromes",
                    "Prader-Willi results from a chromosomal abnormality in which the paternal segment of chromosome 15q11.2-q12 is either deleted or absent.",
                ),
            ),
            note(
                f"{p}-n21",
                "Obesity Syndromes",
                "How Bardet-Biedl syndrome presents beyond obesity",
                "This rare ciliopathy features obesity with hypogonadism, limb dysmorphism, renal disease, and retinopathy with severe vision loss.",
                ref(
                    "Obesity Syndromes",
                    "The disorder is clinically heterogeneous and includes obesity, hypogonadism, and abnormalities that include dysmorphic extremities, renal impairments, and retinopathies.",
                ),
            ),
            note(
                f"{p}-n22",
                "Polygenic Causes of Obesity",
                "Why epigenetic regulation may modulate obesity gene expression",
                "Beyond common SNPs with small individual effects, epigenetic mechanisms may regulate expression of obesity-associated genes and contribute to polygenic weight risk.",
                ref(
                    "Polygenic Causes of Obesity",
                    "Epigenetic factors may also contribute by regulating the expression of obesity-associated genes.",
                ),
            ),
            note(
                f"{p}-n23",
                "Brown Adipose Tissue",
                "How brown adipose tissue dissipates energy as heat",
                "BAT activation increases uncoupling protein 1 (UCP1), creating a mitochondrial proton leak that wastes energy as heat rather than ATP.",
                ref(
                    "Brown Adipose Tissue",
                    "Under these conditions, BAT is activated; as a result, there is an increase in the levels of the factor uncoupling protein 1 (UCP1), which generates a mitochondrial proton leak that results in less production of adenosine triphosphate and energy wastage through the generation of heat.",
                ),
            ),
            note(
                f"{p}-n24",
                "Brief History of Ineffective Obesity Interventions",
                "Why bariatric surgery works primarily through gut-hormone–mediated appetite suppression",
                "Surgery is no longer viewed as restriction/malabsorption alone; altered incretin and satiety signals to the arcuate nucleus suppress appetite.",
                ref(
                    "Brief History of Ineffective Obesity Interventions",
                    "it is now understood that bariatric surgery's mechanism of action (MOA) is driven by appetite suppression via alteration of the gut hormone milieu.",
                ),
            ),
            note(
                f"{p}-n25",
                "Pharmacotherapy",
                "How GLP-1 receptor agonists became the most effective tolerated obesity drugs",
                "Originally diabetes therapies, continuous GLP-1 signaling produces anorexia; liraglutide 3.0 mg was first FDA-approved for obesity, followed by semaglutide 2.4 mg with substantially greater weight loss.",
                ref(
                    "Pharmacotherapy",
                    "To date, the most tolerated and effective class of medications for weight loss are GLP1-receptor agonists.",
                ),
            ),
            note(
                f"{p}-n26",
                "Pharmacotherapy",
                "Why chronic pharmacotherapy is needed to sustain obesity treatment response",
                "Semaglutide STEP trials show large placebo-subtracted loss, but weight is regained after blinded withdrawal—obesity requires ongoing management like other chronic diseases.",
                ref(
                    "Pharmacotherapy",
                    "Furthermore, participants regained weight when the medication was blindly withdrawn, emphasizing the chronic nature of obesity and affirming the need for chronic management.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Definition of Obesity",
                "A muscular athlete and a sedentary adult both have BMI 28 kg/m². The athlete has lower cardiometabolic risk primarily because:",
                [
                    "The athlete likely has more muscle and less visceral fat than the sedentary adult at the same BMI",
                    "BMI always overestimates adiposity in athletes but never in sedentary adults",
                    "Subcutaneous fat carries higher metabolic risk than visceral fat",
                    "BMI directly measures intraabdominal fat volume",
                ],
                0,
                "BMI cannot distinguish muscle from fat or visceral from subcutaneous depots—distribution and composition matter.",
                ref(
                    "Definition of Obesity",
                    "Therefore, two individuals with the same BMI may have entirely different body compositions if one has more muscle mass or subcutaneous fat than the other and, thus, lower metabolic risk.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Body Fat Distribution",
                "Per WHO guidance for Asian populations, waist circumference thresholds indicating increased cardiometabolic risk are:",
                [
                    "90 cm in men and 80 cm in women",
                    "102 cm in men and 88 cm in women",
                    "85 cm in men and 70 cm in women",
                    "Identical to European thresholds for all ethnicities",
                ],
                0,
                "Asian populations have greater visceral adiposity at lower BMI; WHO defines lower waist cutoffs than European-origin values.",
                ref(
                    "Body Fat Distribution",
                    "World Health Organization guidelines define waist circumference thresholds in the Asian population as 35.4 inches (90 cm) for men and 31.5 inches (80 cm) for women.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                "A child with early-onset severe obesity and hyperphagia has a heterozygous MC4R mutation. Best mechanistic explanation?",
                [
                    "Impaired central melanocortin satiety signaling downstream of arcuate α-MSH",
                    "Excess ghrelin secretion from gastric tumors",
                    "Primary leptin deficiency with undetectable serum leptin",
                    "Isolated POMC overexpression causing excessive ACTH",
                ],
                0,
                "MC4R is the principal human monogenic obesity gene; α-MSH normally inhibits appetite via MC4R.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                    "Indeed, in humans, MC4R mutations are the most common cause of monogenic obesity.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                "Direct brain administration of NPY or AgRP in satiated rodents causes:",
                [
                    "Marked increase in food intake",
                    "Immediate cessation of feeding",
                    "No change in feeding behavior",
                    "Exclusive reduction in energy expenditure without eating",
                ],
                0,
                "NPY/AgRP arcuate neurons are pro-orexigenic; their peptides stimulate feeding even when animals are satiated.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                    "Administration of both NPY and AgRP peptides into rodent brains markedly increased food intake, even in satiated rats.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "An adult with common obesity has high serum leptin but continued hyperphagia. Best unifying concept?",
                [
                    "Leptin resistance with failure of adiposity signals to suppress intake",
                    "Absolute leptin deficiency requiring leptin replacement",
                    "Leptin receptor overactivity causing satiety",
                    "Absent leptin synthesis from adipocytes",
                ],
                0,
                "Most obesity is associated with high leptin and attenuated leptin action—resistance, not deficiency.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "Likewise, most people with increased adiposity have high circulating leptin concentrations. Therefore, it is concluded that obesity is often associated with resistance to the action of leptin.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "Ghrelin levels are highest at which point in the feeding cycle?",
                [
                    "Before meals, falling after feeding",
                    "Immediately after a large meal",
                    "Only during sleep with no diurnal pattern",
                    "Exclusively during exercise-induced hypoglycemia",
                ],
                0,
                "Ghrelin is orexigenic, rises preprandially, and acutely increases meal size.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "Ghrelin is a potent orexigenic hormone derived from the stomach that increases before meals and decreases after feeding.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "GLP-1 and PYY are co-secreted from intestinal L cells primarily to:",
                [
                    "Induce postprandial satiety",
                    "Stimulate hepatic gluconeogenesis during fasting",
                    "Increase gastric acid secretion before meals",
                    "Block insulin secretion from β-cells",
                ],
                0,
                "These incretin gut hormones are secreted after meals and promote satiety.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "GLP1 and PYY are co-secreted after a meal and induce satiety.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Pharmacotherapy",
                "In STEP 1, adults without diabetes treated with semaglutide 2.4 mg weekly for 68 weeks had mean body-weight reduction of approximately:",
                [
                    "14.9% (~15.3 kg) versus 2.4% with placebo",
                    "5% versus 4% with placebo",
                    "25% versus 10% with placebo",
                    "No difference from placebo",
                ],
                0,
                "STEP 1 showed ~12.4% placebo-corrected treatment difference with semaglutide 2.4 mg.",
                ref(
                    "Pharmacotherapy",
                    "In the STEP 1 trial involving 1961 individuals without type 2 diabetes, those randomized to the semaglutide group had a mean reduction in body weight of 14.9% or 15.3 kg versus the placebo group, which had an average weight loss of 2.4% reduction in body weight after 68 weeks.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Pharmacotherapy",
                "Liraglutide 3.0 mg daily (Saxenda) was the first GLP-1 agonist FDA-approved for obesity management with placebo-corrected weight loss of approximately:",
                [
                    "5.24 kg",
                    "15.3 kg",
                    "2.63 kg",
                    "0.5 kg",
                ],
                0,
                "Table 40.5 lists liraglutide 3 mg with placebo-corrected loss ~5.24 kg.",
                ref(
                    "Pharmacotherapy",
                    "The GLP1-receptor agonist liraglutide 3.0 mg was the first to receive an FDA-approved indication for obesity management in the United States, Europe, and Japan.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Pharmacotherapy",
                "Orlistat promotes weight loss primarily by:",
                [
                    "Inhibiting pancreatic lipase and reducing intestinal fat absorption",
                    "Stimulating MC4R in the paraventricular nucleus",
                    "Blocking gastric ghrelin secretion",
                    "Uncoupling mitochondrial oxidative phosphorylation",
                ],
                0,
                "Orlistat causes fat malabsorption (~30% of ingested triglycerides at standard dose) with fatty diarrhea limiting use.",
                ref(
                    "Pharmacotherapy",
                    "Orlistat inhibits pancreatic lipase and thereby reduces enteric absorption of fatty acids.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Pharmacotherapy",
                "Phentermine-topiramate extended release (Qsymia) at the top dose produced approximately what placebo-subtracted weight loss at 1 year?",
                [
                    "9%",
                    "2%",
                    "20%",
                    "No loss beyond placebo",
                ],
                0,
                "Top-dose phentermine-topiramate ER yielded ~9% placebo-subtracted loss; recommended dose ~6.5%.",
                ref(
                    "Pharmacotherapy",
                    "In an intention-to-treat analysis after 1 year of therapy, the placebo-subtracted weight loss was approximately 9% for the top dose and approximately 6.5% for the recommended dose.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Pharmacotherapy",
                "Tirzepatide is distinguished from selective GLP-1 agonists because it:",
                [
                    "Activates both GIP and GLP-1 receptors in a single peptide",
                    "Blocks pancreatic lipase exclusively",
                    "Is a pure ghrelin receptor antagonist",
                    "Works only by gastric restriction without hormonal effects",
                ],
                0,
                "Tirzepatide is a dual GIP/GLP-1 receptor co-agonist approved for diabetes and obesity with large weight-loss effects.",
                ref(
                    "Pharmacotherapy",
                    "The dual GIP/GLP1-receptor agonist tirzepatide is a 39-amino-acid linear peptide conjugated to a C20 fatty acid moiety that binds to and activates two incretin receptors: GIP and GLP1.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Body Weight Set-Point",
                "After intentional weight loss, resting energy expenditure often falls more than predicted from body-composition change alone. This adaptation:",
                [
                    "May promote weight regain and is a normal response to negative energy balance",
                    "Persists indefinitely at the same magnitude during long-term weight maintenance in all studies",
                    "Only occurs in lean individuals, never in obesity",
                    "Eliminates the need for ongoing lifestyle or drug therapy",
                ],
                0,
                "Hypocaloric feeding reduces expenditure ~15–20%; this adaptive drop may favor regain though long-term persistence is debated.",
                ref(
                    "Body Weight Set-Point",
                    "The decrease in energy metabolism with weight loss is largely appropriate for concomitant changes in body composition, and a persistent decrease might promote weight regain.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Environmental Effects in High-Risk Populations",
                "Urbanized Australian Aborigines with type 2 diabetes who re-exposed to a traditional lifestyle for 7 weeks showed:",
                [
                    "Weight loss and improved or normalized glucose tolerance and lipids",
                    "No metabolic change compared with urban diet",
                    "Worsening insulin resistance despite activity",
                    "Exclusive lean-mass loss without glucose improvement",
                ],
                0,
                "Short-term return to traditional low-fat diet and high activity improved weight and glycemia in urbanized Aborigines.",
                ref(
                    "Environmental Effects in High-Risk Populations",
                    "Short-term (7 weeks) reexposure to the traditional lifestyle can result in weight loss and significant improvements or normalization of glucose tolerance and fasting glucose, insulin, and triglyceride.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Monogenic Causes of Obesity",
                "A consanguineous child has undetectable leptin, massive obesity, and hypogonadotropic hypogonadism. Best treatment?",
                [
                    "Recombinant leptin replacement",
                    "Setmelanotide MC4R agonist",
                    "High-dose orlistat",
                    "Phentermine monotherapy",
                ],
                0,
                "Congenital leptin deficiency responds dramatically to exogenous leptin; leptin is ineffective in common obesity and leptin receptor deficiency.",
                ref(
                    "Monogenic Causes of Obesity",
                    "The handful of individuals with leptin deficiency can be treated with exogenous leptin, which normalizes weight and food intake, permits puberty,",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Monogenic Causes of Obesity",
                "POMC deficiency in humans classically presents with obesity plus:",
                [
                    "Adrenal insufficiency and hypopigmented skin/red hair",
                    "Primary hyperaldosteronism and hypertension",
                    "Isolated growth hormone excess",
                    "Normal ACTH with excess α-MSH",
                ],
                0,
                "Loss of POMC-derived ACTH causes adrenal insufficiency; reduced α-MSH affects pigmentation.",
                ref(
                    "Monogenic Causes of Obesity",
                    "The presentation of patients with POMC mutations is typically secondary to adrenal insufficiency from low levels of ACTH, usually observed in early life, and they tend to have red hair and pale skin",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Obesity Syndromes",
                "Prader-Willi syndrome results from:",
                [
                    "Absence or deletion of the paternal chromosome 15q11.2-q12 segment",
                    "Maternal duplication of chromosome 15q11.2-q12 causing Angelman phenotype",
                    "Homozygous MC4R loss-of-function",
                    "Leptin receptor gain-of-function",
                ],
                0,
                "Paternal 15q11-q12 deletion causes Prader-Willi; maternal deletion causes Angelman syndrome.",
                ref(
                    "Obesity Syndromes",
                    "Prader-Willi results from a chromosomal abnormality in which the paternal segment of chromosome 15q11.2-q12 is either deleted or absent.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Obesity Syndromes",
                "Bardet-Biedl syndrome is best characterized as:",
                [
                    "A rare ciliopathy with obesity, hypogonadism, renal disease, and retinopathy",
                    "A common polygenic trait linked only to FTO",
                    "An acquired form of leptin resistance from diet alone",
                    "A GH excess state with lean mass preservation",
                ],
                0,
                "Bardet-Biedl is rare, often in consanguineous populations, with multi-organ ciliary dysfunction.",
                ref(
                    "Obesity Syndromes",
                    "Bardet-Biedl syndrome is rare, with a prevalence of less than 1 in 100,000, mostly seen in consanguineous populations.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Brown Adipose Tissue",
                "Human brown adipose tissue can be activated by:",
                [
                    "Cold exposure and increased adrenergic activity",
                    "High-carbohydrate overfeeding alone without sympathetic input",
                    "Chronic cannabinoid agonism",
                    "Leptin deficiency",
                ],
                0,
                "Human BAT depots exist but are small; cold and adrenergic stimuli activate thermogenic UCP1 pathways.",
                ref(
                    "Brown Adipose Tissue",
                    "Human BAT can be activated by cold exposure  $ ^{127} $ and increased adrenergic activity.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Bariatric Surgery",
                "Accepted indications for metabolic/bariatric surgery include BMI:",
                [
                    ">40 kg/m², or 35–40 kg/m² with an associated comorbidity",
                    "25–27 kg/m² without comorbidity in all patients",
                    ">20 kg/m² in any adult",
                    "Only when BMI exceeds 50 regardless of comorbidities",
                ],
                0,
                "Guidelines recommend surgery at BMI >40 or 35–40 with weight-related comorbidity after failed conventional therapy.",
                ref(
                    "Bariatric Surgery",
                    "the accepted indications for surgery are a BMI greater than 40 kg/m  $ ^{2} $ or a BMI between 35 and 40 kg/m  $ ^{2} $ with an associated comorbidity.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Bariatric Surgery",
                "The leading bariatric procedure currently performed in the United States is:",
                [
                    "Sleeve gastrectomy",
                    "Jejunoileal bypass",
                    "Adjustable gastric banding as first-line for all patients",
                    "Biliopancreatic diversion as the most common procedure",
                ],
                0,
                "Sleeve gastrectomy has become the predominant U.S. procedure; banding and biliopancreatic diversion are less common.",
                ref(
                    "Bariatric Surgery",
                    "Sleeve gastrectomy is the current leading procedure in the United States.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Physiology of Body Energy Homeostasis",
                "Hedonic feeding differs from homeostatic feeding because it involves:",
                [
                    "Excess eating in the satiated state driven by palatability or social cues",
                    "Eating only in response to falling leptin during prolonged fasting",
                    "Exclusive regulation by thyroid hormone on resting expenditure",
                    "Meal initiation solely from ghrelin deficiency",
                ],
                0,
                "Homeostatic feeding maintains weight; hedonic feeding occurs despite satiety when highly palatable food is available.",
                ref(
                    "Physiology of Body Energy Homeostasis",
                    "hedonic feeding is defined as excess eating in the satiated state based on availability of highly palatable food or social cues that encourage eating.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Polygenic Causes of Obesity",
                "Homozygosity for the FTO risk allele rs9939609 is associated with approximately:",
                [
                    "3 kg greater weight and 1.67-fold increased odds of obesity",
                    "30 kg greater weight and universal diabetes",
                    "No difference in fat mass from non-carriers",
                    "Protection against obesity",
                ],
                0,
                "FTO is the best-studied common obesity locus with modest but reproducible effect size.",
                ref(
                    "Polygenic Causes of Obesity",
                    "The 16% of individuals homozygous for the risk allele SNP rs9939609 weigh about 3 kg more and have 1.67-fold increased odds of obesity when compared with those not inheriting a risk allele.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Energy Expenditure",
                "The largest component of total daily energy expenditure in most people is:",
                [
                    "Resting (basal) energy expenditure (~70%)",
                    "Voluntary exercise alone (~50%)",
                    "Thermic effect of food (~40%)",
                    "Nonexercise activity thermogenesis exclusively (~60%)",
                ],
                0,
                "Resting expenditure dominates (~70%), activity ~20%, thermic effect of food ~10%.",
                ref(
                    "Energy Expenditure",
                    "Resting energy expenditure accounts for approximately 70% of total energy expenditure.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Pharmacotherapy",
                "Phentermine is FDA-approved for obesity as:",
                [
                    "A short-term sympathomimetic appetite suppressant (since 1959)",
                    "A long-term MC4R agonist for monogenic obesity",
                    "An oral GLP-1 receptor agonist for chronic use",
                    "A pancreatic lipase inhibitor taken with each meal",
                ],
                0,
                "Phentermine releases norepinephrine (and some 5HT/dopamine), typically used short-term with ~5% loss at 8–12 weeks.",
                ref(
                    "Pharmacotherapy",
                    "Phentermine is a sympathomimetic that was approved for obesity treatment in 1959.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Metabolically Normal Obesity",
                "Metabolically healthy obese individuals, based on lipid, BP, and insulin resistance measures:",
                [
                    "Do not appear to have increased cardiovascular mortality risk",
                    "Always develop diabetes within 5 years",
                    "Have mandatory visceral obesity by definition",
                    "Cannot exist because all high-BMI patients are metabolically abnormal",
                ],
                0,
                "A subset with obesity remains metabolically normal, though the concept is debated and confounded by selection bias.",
                ref(
                    "Metabolically Normal Obesity",
                    "Metabolically healthy obese individuals do not appear to have increased risk for cardiovascular mortality.",
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
                "Body mass index is an imprecise measure of adiposity.",
                True,
                "Key points explicitly state BMI is imprecise and does not capture muscle mass or fat distribution.",
                ref(
                    "KEY POINTS",
                    "Body mass index is an imprecise measure of adiposity.",
                ),
            ),
            tf(
                f"{p}-t2",
                "KEY POINTS",
                "Most human obesity is polygenic, and single-gene mutations account for a relatively small number of cases.",
                True,
                "Monogenic obesity exists but is uncommon compared with polygenic/environmental obesity.",
                ref(
                    "KEY POINTS",
                    "Most human obesity is polygenic, and single gene mutations are responsible for a relatively small number of cases of obesity",
                ),
            ),
            tf(
                f"{p}-t3",
                "KEY POINTS",
                "Currently available weight-loss treatments include only dietary intervention and exercise without pharmacotherapy or surgery.",
                False,
                "Key points list diet, activity, behavior modification, pharmacotherapy, and endoscopic/surgical approaches.",
                ref(
                    "KEY POINTS",
                    "Currently available weight-loss treatments include dietary intervention, increased physical activity, behavior modification, pharmacotherapy, and endoscopic and surgical approaches and combinations thereof.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                "Elimination of POMC expression leads to obesity in both rodents and humans.",
                True,
                "POMC neurons inhibit eating via α-MSH; loss causes obesity.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                    "Elimination of POMC expression leads to obesity in both rodents and humans.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "Leptin replacement is effective for most common forms of obesity with high circulating leptin.",
                False,
                "Leptin treats congenital leptin deficiency but not leptin resistance or receptor deficiency in common obesity.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "Leptin is also not effective in most common forms of obesity, which, as previously noted, is a state of leptin resistance.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Body Weight Set-Point",
                "According to set-point theory, weight loss promotes a decrease while weight gain promotes an increase in metabolic rate that acts to restore body weight to a preset level.",
                True,
                "Set-point theory posits coordinated adaptations defending a predetermined weight.",
                ref(
                    "Body Weight Set-Point",
                    "According to the set-point theory, body weight is predetermined such that weight loss promotes a decrease while weight gain promotes an increase in metabolic rate that acts to restore body weight to a preset level.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Environmental Effects in High-Risk Populations",
                "Rural Pima Indians in Mexico have higher obesity and diabetes rates than urbanized Arizona Pima kindred.",
                False,
                "Arizona Pima with modern diet/sedentary lifestyle have epidemic obesity/diabetes; rural Mexican Pima remain leaner.",
                ref(
                    "Environmental Effects in High-Risk Populations",
                    "they have a much lower incidence of obesity and diabetes than their Arizona kindred.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Monogenic Causes of Obesity",
                "MC4R frameshift mutations may account for about 5% of early-onset obesity.",
                True,
                "MC4R is the most common monogenic obesity gene with heterozygous mutations and gene-dosage effects.",
                ref(
                    "Monogenic Causes of Obesity",
                    "Frameshift mutations in MC4R in individuals with childhood obesity, reported by multiple groups,  $ ^{65,66} $ may account for about 5% of early-onset obesity.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Brown Adipose Tissue",
                "Human brown adipose tissue depots are relatively large and likely the dominant determinant of energy expenditure in healthy humans.",
                False,
                "Human BAT exists and is activatable but depots are relatively small with limited impact on total expenditure.",
                ref(
                    "Brown Adipose Tissue",
                    "However, human BAT depots are relatively small, and it is unlikely that BAT plays a significant role in energy expenditure in otherwise healthy humans.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Brief History of Ineffective Obesity Interventions",
                "Bariatric surgery's mechanism of action is now understood to include appetite suppression via altered gut hormone signaling to the hypothalamus.",
                True,
                "Gut hormone milieu changes after surgery inform modern incretin-based pharmacotherapy.",
                ref(
                    "Brief History of Ineffective Obesity Interventions",
                    "it is now understood that bariatric surgery's mechanism of action (MOA) is driven by appetite suppression via alteration of the gut hormone milieu.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Pharmacotherapy",
                "In STEP 1, semaglutide 2.4 mg produced substantially greater weight loss than placebo over 68 weeks.",
                True,
                "Mean ~14.9% body-weight reduction with semaglutide vs 2.4% with placebo.",
                ref(
                    "Pharmacotherapy",
                    "those randomized to the semaglutide group had a mean reduction in body weight of 14.9% or 15.3 kg versus the placebo group, which had an average weight loss of 2.4% reduction in body weight after 68 weeks.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Pharmacotherapy",
                "Orlistat is systemically absorbed and causes frequent central nervous system toxicity as its main limitation.",
                False,
                "Orlistat acts locally in the gut; fatty diarrhea limits compliance; systemic absorption is minimal.",
                ref(
                    "Pharmacotherapy",
                    "Systemic side effects directly related to the drug are uncommon because orlistat is not absorbed.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Polygenic Causes of Obesity",
                "Epigenetic factors may contribute to obesity by regulating expression of obesity-associated genes.",
                True,
                "Chapter cites epigenetic regulation alongside polygenic risk in obesity pathogenesis.",
                ref(
                    "Polygenic Causes of Obesity",
                    "Epigenetic factors may also contribute by regulating the expression of obesity-associated genes.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                "Assertion: MC4R mutations cause obesity in humans.",
                "Reason: MC4R is regulated only by AgRP with no influence from α-MSH.",
                2,
                "Assertion true—MC4R loss causes obesity; reason false—MC4R integrates both α-MSH (inhibitory) and AgRP (antagonistic) melanocortin signaling.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                    "MC4R is regulated by both  $ \\alpha $MSH and agouti, and the output of MC4R neurons in the paraventricular nucleus and other locations represents a balance of AgRP and MSH signaling.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                "Assertion: Ablation of NPY/AgRP neurons decreases feeding in mice.",
                "Reason: NPY and AgRP peptides are always the sole essential mediators of appetite from these neurons.",
                2,
                "Assertion true—full neuronal ablation reduces feeding; reason false—GABA from these neurons may be more important than either peptide alone.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Central Nervous System",
                    "Full ablation of the neuronal population is required to observe decreased feeding, suggesting that the neurotransmitter expressed by these neurons,  $ \\gamma $-aminobutyric acid, is more important than either peptide in regulating appetite.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "Assertion: Most obese humans have elevated circulating leptin.",
                "Reason: Elevated leptin in obesity always suppresses appetite effectively.",
                2,
                "Assertion true—adiposity correlates with high leptin; reason false—obesity is commonly a state of leptin resistance.",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "Therefore, it is concluded that obesity is often associated with resistance to the action of leptin.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                "Assertion: Ghrelin administration can increase food intake in humans.",
                "Reason: Ghrelin levels peak after large meals and promote satiety.",
                2,
                "Assertion true—ghrelin enhances intake acutely; reason false—ghrelin rises before meals and falls after feeding (orexigenic).",
                ref(
                    "Homeostatic Regulation of Energy Intake—Role of the Peripheral Signals",
                    "Ghrelin is a potent orexigenic hormone derived from the stomach that increases before meals and decreases after feeding.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Body Weight Set-Point",
                "Assertion: Weight loss triggers adaptive reductions in energy expenditure.",
                "Reason: These reductions always persist unchanged during long-term maintenance of a lower body weight.",
                2,
                "Assertion true—hypocaloric feeding lowers expenditure; reason false—long-term maintenance data suggest adaptation may not persist when adjusted for composition, though debated.",
                ref(
                    "Body Weight Set-Point",
                    "Long-term maintenance of weight loss is not associated with an abnormal decrease in either resting or total energy expenditure when adjustments are made for changes in body composition,",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Monogenic Causes of Obesity",
                "Assertion: Congenital leptin deficiency causes severe early-onset obesity.",
                "Reason: Leptin deficiency is a common cause of adult obesity in the general population.",
                2,
                "Assertion true—rare leptin mutations cause massive obesity; reason false—leptin mutations are extremely rare.",
                ref(
                    "Monogenic Causes of Obesity",
                    "Although leptin is critical for the normal maintenance of energy balance, very few leptin-deficient humans have been identified, and leptin mutations are extremely rare.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Obesity Syndromes",
                "Assertion: Prader-Willi syndrome is associated with morbid obesity and hyperphagia.",
                "Reason: Prader-Willi results from maternal deletion of chromosome 15q11.2-q12.",
                2,
                "Assertion true—classic Prader-Willi features include obesity; reason false—paternal, not maternal, 15q deletion causes Prader-Willi (maternal deletion causes Angelman).",
                ref(
                    "Obesity Syndromes",
                    "Interestingly, maternal deletion of the same segment is associated with a distinct phenotype known as Angelman syndrome, which is an autistic spectrum disorder.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Brown Adipose Tissue",
                "Assertion: Brown adipose tissue can be activated in humans.",
                "Reason: Human BAT depots are so large that they dominate total energy expenditure in healthy adults.",
                2,
                "Assertion true—cold and adrenergic activity activate human BAT; reason false—human BAT depots are relatively small.",
                ref(
                    "Brown Adipose Tissue",
                    "However, human BAT depots are relatively small, and it is unlikely that BAT plays a significant role in energy expenditure in otherwise healthy humans.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Pharmacotherapy",
                "Assertion: Semaglutide 2.4 mg is FDA-approved for chronic weight management.",
                "Reason: Semaglutide produces no greater weight loss than placebo in STEP 1.",
                2,
                "Assertion true—semaglutide 2.4 mg (Wegovy) is approved; reason false—STEP 1 showed ~14.9% mean weight loss vs 2.4% placebo.",
                ref(
                    "Pharmacotherapy",
                    "Semaglutide 2.4 mg is the second GLP1-receptor agonist to receive FDA approval for long-term weight management in adults with obesity or overweight with at least one weight-related comorbidity.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Pharmacotherapy",
                "Assertion: Tirzepatide activates both GIP and GLP-1 receptors.",
                "Reason: Tirzepatide is a selective pancreatic lipase inhibitor.",
                2,
                "Assertion true—dual incretin agonist; reason false—that describes orlistat, not tirzepatide.",
                ref(
                    "Pharmacotherapy",
                    "The dual GIP/GLP1-receptor agonist tirzepatide is a 39-amino-acid linear peptide conjugated to a C20 fatty acid moiety that binds to and activates two incretin receptors: GIP and GLP1.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Bariatric Surgery",
                "Assertion: Bariatric surgery can produce substantial sustained weight loss and improve comorbidities.",
                "Reason: Bariatric surgery works exclusively by mechanical restriction and malabsorption without hormonal effects.",
                2,
                "Assertion true—surgery improves diabetes, lipids, hypertension; reason false—MOA includes gut hormone–mediated appetite suppression.",
                ref(
                    "Bariatric Surgery",
                    "weight loss is substantial and sustained, and it is associated with remission or improvement of type 2 diabetes, dyslipidemia, hypertension, and other weight-related comorbidities",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Polygenic Causes of Obesity",
                "Assertion: Environmental changes since the 1960s likely contributed to rising obesity prevalence.",
                "Reason: Human genetics changed dramatically over the same period to cause the epidemic.",
                2,
                "Assertion true—processed food environment interacts with stable genetics; reason false—genetics have not changed substantially during the obesity rise.",
                ref(
                    "Obesity and Neuroendocrine Control of Energy Stores",
                    "Considering that the genetics of humans have not changed substantially during the time in which the dramatic rise in rates of obesity has occurred, the increase in obesity prevalence most likely has resulted from a complex interplay of genes and environment.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "40",
        "title": "Obesity and Neuroendocrine Control of Energy Stores",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Samar Hafida and Caroline M. Apovian",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_40_Obesity_and_Neuroendocrine_Control_of_Energy_Stores.md",
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
