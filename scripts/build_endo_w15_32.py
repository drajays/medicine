#!/usr/bin/env python3
"""Generate Williams 15e module w15-32 — Physiology of Insulin Secretion."""
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
OUT_NAME = "w15-32_Physiology_of_Insulin_Secretion.json"


def build() -> dict:
    p = "w15-32"
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why β-cell function is fundamental to glucose homeostasis",
                "ISR is finely regulated across meals, obesity, insulin resistance, and pregnancy—disruption at any level of mass, architecture, or secretory dynamics impairs tolerance.",
                ref(
                    "KEY POINTS",
                    "β-cell function is fundamental for glucose homeostasis: the insulin secretion rate (ISR) is finely regulated by multiple mechanisms to ensure appropriate hormone delivery under changing short-term conditions (e.g., variable nutrient intake) and longer-term circumstances (e.g., obesity, insulin resistance, pregnancy).",
                ),
            ),
            note(
                f"{p}-n2",
                "Introduction",
                "Why islet architecture adds complexity beyond β-cell mass",
                "Function reflects not only mass and quality of β-cells but also islet architecture and structural integrity—heterogeneous islet subsets, gap-junction coupling, and paracrine interactions modulate output.",
                ref(
                    "Introduction",
                    "Therefore, a novel concept emerging from these studies is that function is the result of not only the mass and quality of β-cells but also of the architecture and structural integrity of the islet as an organ.",
                ),
            ),
            note(
                f"{p}-n3",
                "Introduction",
                "How glucokinase serves as the β-cell glucose sensor",
                "GLUT1 transports glucose; glucokinase phosphorylation is rate-limiting for glycolysis—ATP rise closes KATP channels, depolarizes the membrane, and triggers Ca²⁺-mediated exocytosis from readily releasable granules.",
                ref(
                    "Introduction",
                    "This reaction is mediated by the enzyme glucokinase, which, by determining the rate of glycolysis, functions as the glucose sensor.",
                ),
            ),
            note(
                f"{p}-n4",
                "Introduction",
                "Why triggering and amplifying pathways are distinct",
                "Membrane KATP closure and Ca²⁺ influx constitute the triggering pathway; cAMP-driven amplification (GLP1, GIP, glucagon) potentiates exocytosis largely independent of KATP—both require glucose metabolism.",
                ref(
                    "Introduction",
                    "The overwhelming complexity of stimulatory and inhibitory signals and their intracellular transduction and modulation can be operationally reduced to two main physiologic domains: a triggering pathway, starting at the cell membrane level, and an amplifying pathway, which is mostly intracellular.",
                ),
            ),
            note(
                f"{p}-n5",
                "Introduction",
                "How SUR1/Kir6.2 KATP channels gate insulin bursts",
                "SUR1/Kir6.2 pairs form β-cell KATP; channel opening resets membrane potential below Ca²⁺ channel threshold—mutations cause hyperinsulinemic hypoglycemia or neonatal diabetes.",
                ref(
                    "Introduction",
                    "In the β-cell, the SUR1/Kir6.2 pairs constitute the KATP channel, which controls the flux of potassium ions (see Fig. 32.1).",
                ),
            ),
            note(
                f"{p}-n6",
                "Introduction",
                "How cAMP amplifies glucose-stimulated insulin secretion",
                "cAMP generated at the plasma membrane potentiates glucose-stimulated secretion—especially with glucagon, GLP1, and GIP—acting on the exocytotic machinery via PKA and Epac2.",
                ref(
                    "Introduction",
                    "In signal amplification, cyclic adenosine monophosphate (cAMP) plays an important role. This second messenger is generated at the plasma membrane from ATP and potentiates glucose-stimulated insulin secretion, particularly in response to glucagon, glucagon-like peptide-1 (GLP1), and glucose-dependent insulinotropic peptide (GIP).",
                ),
            ),
            note(
                f"{p}-n7",
                "Neural Regulation of β-Cell Function",
                "How autonomic nerves modulate islet hormone release",
                "Sympathetic α₂-mediated norepinephrine inhibits insulin and potentiates glucagon; parasympathetic M3 muscarinic acetylcholine enhances both—hypothalamic glucokinase neurons differentially tune these circuits.",
                ref(
                    "Neural Regulation of β-Cell Function",
                    "Sympathetic stimulation (through α2 receptor-mediated norepinephrine release) inhibits insulin secretion and potentiates glucagon secretion, whereas parasympathetic stimulation (through M3 muscarinic-mediated acetylcholine release) enhances insulin and glucagon release.",
                ),
            ),
            note(
                f"{p}-n8",
                "β-Cell Mass",
                "Why β-cell mass reflects dynamic balance not fixed endowment",
                "Neogenesis, replication, hyperplasia oppose apoptosis and dedifferentiation—most neogenesis occurs preterm; adult peripheral 'virgin' β-cells provide a lifelong reservoir.",
                ref(
                    "β-Cell Mass",
                    "β-cell mass is the net balance between positive factors, including islet neogenesis, β-cell proliferation, and β-cell hyperplasia, and negative factors, such as β-cell apoptosis and dedifferentiation.",
                ),
            ),
            note(
                f"{p}-n9",
                "β-Cell Insulin Content",
                "How granule pools underpin biphasic secretion",
                "Thousands of age-distinct granules exist per β-cell; younger, more mobile granules form the readily releasable pool—acute glucose releases <1% of granule insulin yet first-phase dynamics depend on this pool.",
                ref(
                    "β-Cell Insulin Content",
                    "younger granules are fewer but more mobile than older granules, even if they come from deep in the cytoplasm, and therefore form a readily releasable pool.",
                ),
            ),
            note(
                f"{p}-n10",
                "Insulin Secretion Versus Plasma Insulin",
                "Why C-peptide deconvolution is the state-of-the-art ISR measure",
                "C-peptide is co-secreted equimolar with insulin, not hepatically extracted, and has relatively constant clearance—deconvolution reconstructs pancreatic ISR before hepatic degradation.",
                ref(
                    "Insulin Secretion Versus Plasma Insulin",
                    "The principles of this method are that (1) C-peptide is co-secreted with insulin in equimolar amounts as a result of proinsulin cleavage, (2) C-peptide is not extracted by the liver, and (3) C-peptide clearance—half of which occurs through the kidney—is approximately constant in any given individual.",
                ),
            ),
            note(
                f"{p}-n11",
                "Insulin Secretion Versus Plasma Insulin",
                "How hepatic first-pass extraction distorts plasma insulin",
                "Roughly 65% (50–70%) of portal insulin is removed on first hepatic pass; fed-state saturation lowers extraction—peripheral insulin underestimates and mis-times true secretory bursts.",
                ref(
                    "Insulin Secretion Versus Plasma Insulin",
                    "The fraction of portal insulin that is removed by the liver in its first pass is about 65%, ranging between 50% and 70%.",
                ),
            ),
            note(
                f"{p}-n12",
                "Modes of β-Cell Response",
                "Why first-phase (AIR) insulin secretion curbs glycemic excursions",
                "The sharp initial burst (~3 nmol/m² during OGTT) primes tissue uptake and suppresses endogenous glucose production—even though small, it is crucial when glucose begins to rise.",
                ref(
                    "Modes of β-Cell Response",
                    "First-phase insulin secretion contributes only an estimated one-tenth (about 3 nmol/m2) of suprabasal secretion during a 2-hour OGTT; nevertheless, a prompt stimulation of insulin release as soon as glucose starts to rise is crucial to suppress endogenous glucose production and prime tissue glucose uptake, thereby curbing subsequent glycemic excursions.",
                ),
            ),
            note(
                f"{p}-n13",
                "Modes of β-Cell Response",
                "How β-cell glucose sensitivity defines meal insulin output",
                "Glucose sensitivity is the ISR increment per glucose increment—the dominant control of postprandial tolerance; its decrease is the hallmark of all glucose intolerance.",
                ref(
                    "Modes of β-Cell Response",
                    "β-cell glucose sensitivity measures the increase in secretion rate for any concomitant increase in plasma glucose concentration. This key mode of response determines the amount of insulin secreted during a meal and therefore is a major control of glucose tolerance.",
                ),
            ),
            note(
                f"{p}-n14",
                "Modes of β-Cell Response",
                "Why potentiation is an intrinsic β-cell memory",
                "Prior glucose, incretins, glucagon, cholinergic input, nutrients, or sulfonylureas steepen the glucose–ISR dose-response on subsequent exposure—time dynamics matter as much as absolute release.",
                ref(
                    "Modes of β-Cell Response",
                    "Potentiation of insulin secretion is an intrinsic feature of β-cell function. Potentiation occurs when the dose-response relationship between glucose level and insulin secretion is enhanced, as happens when prior exposure to glucose leads to greater insulin secretion on subsequent exposure.",
                ),
            ),
            note(
                f"{p}-n15",
                "Modes of β-Cell Response",
                "How rate sensitivity anticipates rising glucose",
                "First-phase magnitude also tracks the glucose rate of change (derivative component)—underlying mechanisms operate even with gradual rises, producing secretion anticipated beyond dose-response alone.",
                ref(
                    "Modes of β-Cell Response",
                    "Its magnitude depends on the size of the glucose stimulus and can also be represented as a function of the glucose rate of change (also called rate sensitivity, anticipation, or derivative component).",
                ),
            ),
            note(
                f"{p}-n16",
                "The Hyperglycemic Clamp and Biphasic Insulin Secretion",
                "How the hyperglycemic clamp exposes biphasic ISR",
                "A square-wave hyperglycemic step elicits a 5–8 min first-phase burst then progressive second-phase rise—first-phase AIR is a sensitive early marker of β-cell dysfunction.",
                ref(
                    "The Hyperglycemic Clamp and Biphasic Insulin Secretion",
                    "The insulin secretory response to this challenge typically is biphasic, with an initial sharp insulin secretory burst lasting about 5 to 8 min (first-phase secretion), followed by a transient decrease and then a progressive, slow increase, which continues as long as hyperglycemia is maintained (second-phase secretion)",
                ),
            ),
            note(
                f"{p}-n17",
                "The Graded Glucose Infusion Test and the β-Cell Dose Response",
                "How graded glucose infusion quantifies glucose sensitivity",
                "Ascending glucose infusion rates plot ISR vs glucose—the slope is β-cell glucose sensitivity (~80 pmol·min⁻¹·mM⁻¹ in health, fairly linear to high glucose).",
                ref(
                    "The Graded Glucose Infusion Test and the β-Cell Dose Response",
                    "The plot of insulin secretion rates against plasma glucose concentrations represents the β-cell dose response, whose slope quantifies the sensitivity of the β-cell to glucose (Fig. 32.7).",
                ),
            ),
            note(
                f"{p}-n18",
                "The Insulin Secretary Response to Oral Stimuli",
                "Why oral glucose stimulates more insulin than intravenous at matched glycemia",
                "GIP and GLP1 released from gut epithelium during ingestion potentiate ISR—the classic isoglycemic IV infusion vs OGTT isolates this incretin effect.",
                ref(
                    "The Insulin Secretary Response to Oral Stimuli",
                    "It has long been known that if glucose is ingested rather than infused, insulin secretion is higher at the same glucose levels.",
                ),
            ),
            note(
                f"{p}-n19",
                "The Insulin Secretary Response to Oral Stimuli",
                "How isoglycemic infusion quantifies the incretin effect",
                "Reproducing OGTT glucose kinetics with IV glucose while comparing ISR reveals oral-route potentiation—modeling shows steeper dose-response with enteral glucose.",
                ref(
                    "The Insulin Secretary Response to Oral Stimuli",
                    "The classic test to unveil and quantify the incretin effect is based on a standard OGTT and a separate test in the same subject, in which the time course of glucose concentration observed with the OGTT is reproduced by a controlled intravenous glucose infusion (also called isoglycemic glucose infusion).",
                ),
            ),
            note(
                f"{p}-n20",
                "The Insulin Secretary Response to Oral Stimuli",
                "Why the Staub-Traugott effect improves sequential meal tolerance",
                "Second carbohydrate loads show attenuated glycemic and secretory responses because first-load hyperglycemia/hyperinsulinemia suppresses EGP and enhances potentiation—even in T2D.",
                ref(
                    "The Insulin Secretary Response to Oral Stimuli",
                    "With consecutive nutrient loads, the plasma glucose and insulin secretory responses are attenuated during the second as compared to the first load (Staub-Traugott effect); this phenomenon, which is also observed in patients with T2D, is due to persistent suppression of endogenous glucose production by the hyperglycemia and hyperinsulinemia induced by the first load and to enhanced potentiation of insulin release.",
                ),
            ),
            note(
                f"{p}-n21",
                "Insulin Secretion and Insulin Sensitivity",
                "How the disposition index captures β-cell compensation",
                "AIR and insulin sensitivity relate hyperbolically across individuals—their product (disposition index) indexes intrinsic β-cell function adjusted for insulin resistance.",
                ref(
                    "Insulin Secretion and Insulin Sensitivity",
                    "By fitting equilateral hyperbola to these IVGTT data, it has been proposed that a more accurate index of intrinsic β-cell function is the product of the insulin secretion and sensitivity indices, or disposition index.",
                ),
            ),
            note(
                f"{p}-n22",
                "Genetic Influences on Insulin Secretion",
                "Why TCF7L2 variants impair incretin-mediated secretion",
                "Most T2D GWAS hits affect insulin secretion; TCF7L2 (Wnt pathway) variants specifically associate with defective incretin-induced insulin release.",
                ref(
                    "Genetic Influences on Insulin Secretion",
                    "For example, genetic variants of TCF7L2, a transcription factor that mediates the Wingless/Integrated (Wnt) pathway, have been associated with impaired incretin-induced insulin secretion.",
                ),
            ),
            note(
                f"{p}-n23",
                "Genetic Influences on Insulin Secretion",
                "How MODY2 GCK mutations shift the glucose dose-response",
                "Heterozygous glucokinase deficiency lowers β-cell glucose sensitivity—graded glucose infusion shows a rightward-shifted ISR–glucose relationship with mild stable hyperglycemia.",
                ref(
                    "Genetic Influences on Insulin Secretion",
                    "In MODY 2, a heterozygous private mutation of the gene (GCK) encoding glucokinase results in partial enzyme deficiency and a loss of β-cell glucose sensitivity, evidenced by a rightward shift in the dose response on a graded glucose infusion test.",
                ),
            ),
            note(
                f"{p}-n24",
                "Insulin Secretion in Dysglycemic States",
                "Why reduced glucose sensitivity dominates early dysglycemia",
                "IFG/IGT show increased absolute insulin output compensating for resistance while glucose sensitivity falls progressively—loss of AIR occurs early; sustained secretion loss defines overt T2D.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "Thus, β-cell glucose sensitivity is progressively reduced from the clinical category of impaired fasting glycemia (IFG) through IGT to overt diabetes regardless of the etiology of diabetes",
                ),
            ),
            note(
                f"{p}-n25",
                "Insulin Secretion in Dysglycemic States",
                "How bariatric surgery can reverse β-cell glucose sensitivity",
                "Poorly controlled T2D dose-response curves shift toward normal after bariatric surgery—ex vivo islet studies show recovery with normoglycemia plus metformin, supporting functional rather than purely loss-of-mass defects.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "The downward trajectory of glucose sensitivity can be reversed, at least in part, by spontaneous or therapeutic amelioration of glycemic control, as most strikingly demonstrated in diabetic patients undergoing bariatric surgery (Fig. 32.11).",
                ),
            ),
            note(
                f"{p}-n26",
                "Insulin Secretion in Dysglycemic States",
                "Why tirzepatide exploits GIP/GLP1 coagonism in T2D",
                "T2D shows selective loss of GIP potentiation (not hormone levels); tirzepatide—a biased dual agonist—may restore GIP effects and amplify GLP1-mediated weight loss and insulin secretion.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "Interestingly, a GLP1/GIP receptor coagonist, tirzepatide, offers a paradigm of multireceptor pharmacology for the treatment of metabolic diseases.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Introduction",
                "A researcher studies human β-cells and blocks GLUT1. Glucose-stimulated insulin release is abolished despite intact KATP channels. Which downstream step is most directly impaired?",
                [
                    "Glucokinase-mediated glycolytic flux and ATP generation",
                    "Direct sulfonylurea binding to SUR1",
                    "Hepatic insulin clearance",
                    "Renal C-peptide excretion",
                ],
                0,
                "Human β-cells take up glucose via GLUT1; glucokinase phosphorylation is rate-limiting for metabolism that closes KATP and triggers secretion.",
                ref(
                    "Introduction",
                    "Thus, glucose enters human β-cells via the isoform 1 of the glucose transporter (GLUT1) and is metabolized through the glycolytic pathway and, subsequently, in mitochondrial.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Introduction",
                "A neonate has persistent hyperinsulinemic hypoglycemia. Sequencing reveals an activating mutation in ABCC8 (SUR1). Mechanism?",
                [
                    "Constitutive KATP channel closure → depolarization → insulin hypersecretion",
                    "Complete loss of glucokinase activity",
                    "Absent GLP1 receptors only",
                    "Excess hepatic insulin-degrading enzyme",
                ],
                0,
                "SUR1/Kir6.2 KATP channel mutations cause hyperinsulinemic hypoglycemia or neonatal diabetes depending on gain- vs loss-of-function.",
                ref(
                    "Introduction",
                    "Mutations in both components of the β-cell KATP—SUR1 (encoded by the ABCC8 gene) and Kir6.2 (encoded by the KCNJ11 gene)—have been shown to lead to hypersecretion of insulin, resulting in clinical syndromes ranging from persistent hyperinsulinemic hypoglycemia of infancy to neonatal diabetes",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Neural Regulation of β-Cell Function",
                "During hypoglycemia, sympathetic output rises. Expected pancreatic islet effect?",
                [
                    "Increased insulin and decreased glucagon",
                    "Decreased insulin and increased glucagon",
                    "Increased both insulin and glucagon",
                    "No change in either hormone",
                ],
                1,
                "Sympathetic α₂-mediated norepinephrine inhibits insulin and potentiates glucagon—key counterregulatory physiology.",
                ref(
                    "Neural Regulation of β-Cell Function",
                    "Sympathetic stimulation (through α2 receptor-mediated norepinephrine release) inhibits insulin secretion and potentiates glucagon secretion",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Insulin Secretion Versus Plasma Insulin",
                "An endocrinologist measures fasting portal and peripheral insulin during a study. Approximately what fraction of portal insulin is removed on first hepatic pass in healthy adults?",
                [
                    "About 15%",
                    "About 35%",
                    "About 65%",
                    "About 95%",
                ],
                2,
                "Hepatic first-pass insulin extraction averages ~65% (range 50–70%); overall hepatic contribution to clearance ~80%.",
                ref(
                    "Insulin Secretion Versus Plasma Insulin",
                    "The fraction of portal insulin that is removed by the liver in its first pass is about 65%, ranging between 50% and 70%.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Insulin Secretion Versus Plasma Insulin",
                "A researcher wants true pancreatic insulin secretion rate (ISR) during an OGTT. Best approach?",
                [
                    "Fasting plasma insulin alone",
                    "C-peptide concentrations with deconvolution modeling",
                    "Urinary glucose-to-creatinine ratio",
                    "HOMA-IR from single fasting sample",
                ],
                1,
                "C-peptide is co-secreted equimolarly, not hepatically extracted—deconvolution reconstructs ISR before hepatic degradation.",
                ref(
                    "Insulin Secretion Versus Plasma Insulin",
                    "when assessing insulin secretion in vivo, methods based on the measurement of C-peptide currently are the state-of-the-art approach.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Modes of β-Cell Response",
                "Which β-cell response mode is most reduced across IFG, IGT, and diabetes regardless of etiology?",
                [
                    "Absolute fasting glucagon",
                    "β-cell glucose sensitivity",
                    "Renal glucose threshold",
                    "Hepatic glycogen synthase only",
                ],
                1,
                "Decreased glucose sensitivity is the hallmark of all forms of glucose intolerance—dose-response curves shift down and right.",
                ref(
                    "Modes of β-Cell Response",
                    "In fact, decreased glucose sensitivity is a hallmark of all forms of glucose intolerance.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "The Hyperglycemic Clamp and Biphasic Insulin Secretion",
                "A +126 mg/dL hyperglycemic clamp in a healthy adult produces first-phase insulin secretion of roughly what magnitude?",
                [
                    "~0.1 nmol/m²",
                    "~4 nmol/m² (~1 unit in a 70-kg adult)",
                    "~40 nmol/m²",
                    "No measurable first phase",
                ],
                1,
                "Typical clamp first-phase AIR ~4 nmol/m² BSA—10–15% of hourly second-phase secretion but physiologically critical.",
                ref(
                    "The Hyperglycemic Clamp and Biphasic Insulin Secretion",
                    "in a typical +126 mg/dL (+7 mmol/L) hyperglycemic clamp, it is ~4 nmol per square meter of body surface area (~1 unit in a 70-kg adult), representing 10% to 15% of what is secreted per hour during the second phase.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "The Hyperglycemic Clamp and Biphasic Insulin Secretion",
                "Attenuated first-phase insulin secretion during IVGTT in at-risk relatives predicts future diabetes because it reflects:",
                [
                    "Primary excess hepatic glucagon only",
                    "Early β-cell dysfunction sensitive to glycemic milieu",
                    "Increased muscle GLUT4 translocation",
                    "Enhanced incretin hormone release",
                ],
                1,
                "AIR loss is an early, predictive marker—may reflect readily releasable pool depletion with rising fasting glucose.",
                ref(
                    "The Hyperglycemic Clamp and Biphasic Insulin Secretion",
                    "attenuated first-phase insulin secretion is a very sensitive marker of early β-cell dysfunction.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "The Graded Glucose Infusion Test and the β-Cell Dose Response",
                "In a normoglycemic subject, graded glucose infusion from fasting to ~180 mg/dL typically increases insulin secretion by:",
                [
                    "Twofold",
                    "Fivefold to sixfold",
                    "Fiftyfold",
                    "No change until 360 mg/dL",
                ],
                1,
                "Healthy β-cells increase ISR five- to sixfold over this range; glucose sensitivity ~80 pmol·min⁻¹·mM⁻¹.",
                ref(
                    "The Graded Glucose Infusion Test and the β-Cell Dose Response",
                    "In healthy persons, insulin secretion increases by fivefold to sixfold as glucose is gradually raised from the fasting level to 180 mg/dL (10 mmol/L)",
                ),
            ),
            mcq(
                f"{p}-m10",
                "The Insulin Secretary Response to Oral Stimuli",
                "A subject undergoes OGTT and, on another day, isoglycemic IV glucose infusion matched to OGTT glucose profile. ISR is higher on OGTT. This difference defines:",
                [
                    "Hepatic insulin resistance index",
                    "The incretin effect",
                    "Staub-Traugott phenomenon only",
                    "Disposition index",
                ],
                1,
                "Oral-route potentiation of ISR at matched glycemia is the incretin effect—quantified by isoglycemic infusion comparison.",
                ref(
                    "The Insulin Secretary Response to Oral Stimuli",
                    "As illustrated in Fig. 32.9, insulin secretion is considerably potentiated by the oral route of glucose entry, thereby resulting in an increase in the slope of the β-cell dose response, as estimated by modeling analysis.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "The Insulin Secretary Response to Oral Stimuli",
                "During a standard OGTT in normoglycemic adults, which incretin contributes most to potentiation and why?",
                [
                    "GLP1 because its molar concentrations exceed GIP",
                    "GIP because its plasma concentrations are higher than GLP1",
                    "Ghrelin because it is islet-derived",
                    "Neither—both are absent during oral glucose",
                ],
                1,
                "Both GIP and GLP1 potentiate secretion; GIP molar levels are higher during OGTT though GLP1 is stronger per mole when infused.",
                ref(
                    "The Insulin Secretary Response to Oral Stimuli",
                    "In molar terms, GIP concentrations in response to an OGTT are higher compared to GLP1.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "The Insulin Secretary Response to Oral Stimuli",
                "A healthy volunteer receives two identical high-carbohydrate meals 3.5 hours apart. The second meal shows lower glycemic and insulin responses. This is best termed:",
                [
                    "Rebound hypoglycemia",
                    "Staub-Traugott effect",
                    "Somogyi phenomenon",
                    "Dawn phenomenon",
                ],
                1,
                "Staub-Traugott effect: first load suppresses EGP and enhances potentiation, attenuating second-load responses.",
                ref(
                    "The Insulin Secretary Response to Oral Stimuli",
                    "With consecutive nutrient loads, the plasma glucose and insulin secretory responses are attenuated during the second as compared to the first load (Staub-Traugott effect)",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Insulin Secretion and Insulin Sensitivity",
                "IVGTT analysis plots acute insulin response (AIR) vs insulin sensitivity forming a hyperbola. The product of these indices is called:",
                [
                    "Insulinogenic index",
                    "Disposition index",
                    "Proinsulin-to-insulin ratio",
                    "Matsuda index",
                ],
                1,
                "Disposition index = secretion × sensitivity product—indexes intrinsic β-cell function accounting for insulin resistance.",
                ref(
                    "Insulin Secretion and Insulin Sensitivity",
                    "it has been proposed that a more accurate index of intrinsic β-cell function is the product of the insulin secretion and sensitivity indices, or disposition index.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Insulin Secretion and Insulin Sensitivity",
                "In individuals with IGT on IVGTT, the AIR–sensitivity curve is displaced. When insulin sensitivity falls below ~50 μmol·min⁻¹·nM⁻¹ per kg FFM, AIR:",
                [
                    "Remains permanently zero",
                    "Rises back toward normal, likely from mild hyperglycemia",
                    "Exceeds lean control values by 10-fold always",
                    "Becomes unrelated to glucose",
                ],
                1,
                "IGT shows reduced compensation until sensitivity drops further—then hyperglycemia drives AIR back up.",
                ref(
                    "Insulin Secretion and Insulin Sensitivity",
                    "in individuals with impaired glucose tolerance (IGT), the curve is displaced as shown in Fig. 32.10, indicating that compensation is reduced until insulin sensitivity drops below ~50 μmol·min−1·nM−1 per kg of fat-free mass, at which level AIR rises back to normal, very probably as a consequence of the mild hyperglycemia of these individuals.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Genetic Influences on Insulin Secretion",
                "A 19-year-old lean patient has mild fasting hyperglycemia (~110 mg/dL), autosomal-dominant family history, and normal antibodies. GCK sequencing shows heterozygous mutation. Diagnosis?",
                [
                    "Type 1 diabetes",
                    "MODY 2 (glucokinase deficiency)",
                    "KATP neonatal diabetes",
                    "Cystic fibrosis-related diabetes",
                ],
                1,
                "MODY2 from GCK heterozygosity causes partial glucokinase deficiency and rightward-shifted glucose dose-response.",
                ref(
                    "Genetic Influences on Insulin Secretion",
                    "In MODY 2, a heterozygous private mutation of the gene (GCK) encoding glucokinase results in partial enzyme deficiency and a loss of β-cell glucose sensitivity",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Genetic Influences on Insulin Secretion",
                "A T2D risk allele in TCF7L2 is most strongly linked to which secretory defect?",
                [
                    "Excess basal glucagon only",
                    "Impaired incretin-induced insulin secretion",
                    "Increased hepatic glycogenolysis unrelated to islets",
                    "Complete absence of insulin gene transcription",
                ],
                1,
                "TCF7L2 variants associate with defective incretin-mediated insulin release among GWAS-linked secretion defects.",
                ref(
                    "Genetic Influences on Insulin Secretion",
                    "genetic variants of TCF7L2, a transcription factor that mediates the Wingless/Integrated (Wnt) pathway, have been associated with impaired incretin-induced insulin secretion.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Insulin Secretion in Dysglycemic States",
                "A patient with long-standing T2D has reduced incretin potentiation. GLP1RA and DPP-4 inhibitors do not restore GIP response, but after bariatric surgery GIP potentiation improves. Primary defect?",
                [
                    "Decreased GLP1 and GIP secretion",
                    "Selective loss of β-cell response to GIP",
                    "Absent GLUT1 in β-cells",
                    "Complete β-cell aplasia",
                ],
                1,
                "T2D incretin defect is lack of GIP response, not decreased hormone release—partially ameliorated by bariatric surgery.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "the underlying defect being a selective loss of incretin-induced potentiation.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Insulin Secretion in Dysglycemic States",
                "Twelve months after biliopancreatic diversion, an overweight T2D patient's mixed-meal ISR–glucose curve shifts toward nondiabetic controls. Best interpretation?",
                [
                    "β-cell mass necessarily doubled",
                    "β-cell glucose sensitivity can recover with improved glycemic control",
                    "Hepatic extraction fell to zero",
                    "Incretin hormones are no longer released",
                ],
                1,
                "Glucose sensitivity trajectory can reverse with glycemic improvement—bariatric surgery is the striking clinical demonstration.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "The downward trajectory of glucose sensitivity can be reversed, at least in part, by spontaneous or therapeutic amelioration of glycemic control, as most strikingly demonstrated in diabetic patients undergoing bariatric surgery",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Insulin Secretion in Dysglycemic States",
                "Tirzepatide differs from selective GLP1RA because it is:",
                [
                    "A DPP-4 inhibitor",
                    "A biased dual GIP and GLP1 receptor coagonist",
                    "A sulfonylurea SUR1 opener",
                    "An SGLT2 inhibitor",
                ],
                1,
                "Tirzepatide is a stronger GIP than GLP1 receptor agonist—multireceptor pharmacology with major T2D and obesity efficacy.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "A stronger agonist of the GIP than the GLP1 receptor, tirzepatide potentiates GLP1-induced weight loss (without GIP itself reducing energy intake).",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Insulin Secretion in the Fasting State",
                "Portal vein insulin sampling in healthy adults shows pulsatile secretion at intervals of:",
                [
                    "Every 2–3 seconds only",
                    "5 to 14 minutes",
                    "Exactly 60 minutes",
                    "No pulsatility in humans",
                ],
                1,
                "Pulsatile insulin occurs at 5–14 min intervals—intrinsic islet oscillations; ultradian 80–180 min cycles also exist.",
                ref(
                    "Insulin Secretion in the Fasting State",
                    "When frequently sampled from portal vein blood, insulin concentrations oscillate, with detectable pulses at 5- to 14-min intervals.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Insulin Secretion in the Fasting State",
                "An epidemiologic cohort shows elevated fasting proinsulin-to-insulin ratio. This marker suggests:",
                [
                    "Enhanced β-cell conversion efficiency",
                    "Defective proinsulin processing and β-cell stress",
                    "Excess hepatic C-peptide extraction",
                    "Primary glucagon deficiency",
                ],
                1,
                "Elevated proinsulin/insulin or proinsulin/C-peptide ratios mark defective conversion and predict incident diabetes.",
                ref(
                    "Insulin Secretion in the Fasting State",
                    "In epidemiologic studies, a higher ratio of proinsulin to insulin or proinsulin to C-peptide has been related to incident diabetes.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "β-Cell Insulin Content",
                "Acute in vitro glucose stimulation releases what fraction of total β-cell granule insulin?",
                [
                    "Less than 1%",
                    "About 25%",
                    "About 50%",
                    "Nearly 100%",
                ],
                0,
                "Only a small fraction (<1%) of granule insulin is acutely secreted—most granules turnover with intracellular degradation.",
                ref(
                    "β-Cell Insulin Content",
                    "only a small fraction (much less than 1%) of granule insulin is secreted in response to acute in vitro glucose stimulation",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Characteristics of Insulin Secretion In Vivo",
                "Compared with insulin sensitivity (which may double with intervention), insulin secretion in the same person can vary:",
                [
                    "Less than 10% over years",
                    "Many-fold within minutes to ~100-fold between individuals",
                    "Only with exogenous insulin infusion",
                    "Identically in all lean adults",
                ],
                1,
                "ISR spans ~6.5-fold with meals and ~100-fold between lean sensitive vs obese resistant individuals on standardized glucose.",
                ref(
                    "Characteristics of Insulin Secretion In Vivo",
                    "In contrast, insulin secretion can vary many-fold in the same person in a matter of minutes, as occurs with a large mixed meal (from ~60 to ~400 pmol·min−1·m−2, a ~6.5-fold increase), or over years, as happens with weight gain.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Insulin Secretion, Insulin Action, and Glucose Homeostasis",
                "In IFG, modeling shows insulin output increased ~15% while β-cell glucose sensitivity is reduced ~30%. This pattern illustrates:",
                [
                    "Opposite behavior of absolute insulin release vs glucose sensitivity across dysglycemia stages",
                    "Parallel decline of both output and sensitivity",
                    "Isolated glucagon defect only",
                    "Normal disposition index",
                ],
                0,
                "Early dysglycemia: compensatory hypersecretion with falling glucose sensitivity—key concept from OGTT modeling (Fig. 32.13, Table 32.2).",
                ref(
                    "Insulin Secretion, Insulin Action, and Glucose Homeostasis",
                    "In IFG, for example, insulin output is increased by 15%, insulin sensitivity (on an insulin clamp) is only slightly impaired, but glucose sensitivity is 30% lower (Table 32.2).",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Introduction",
                "Sulfonylureas stimulate insulin release by:",
                [
                    "Activating GLP1 receptors directly",
                    "Direct binding to KATP channels, bypassing glucose metabolism",
                    "Inhibiting hepatic insulin-degrading enzyme",
                    "Blocking parasympathetic M3 receptors",
                ],
                1,
                "SUs bind SUR subunits and close KATP independently of metabolic ATP—see Fig. 32.1 triggering pathway.",
                ref(
                    "Introduction",
                    "Sulphonylureas (SUs) inhibit the channel by direct binding, bypassing metabolism.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Slow β-Cell Response Modes and Adaptation Mechanisms",
                "Three to four days of mild IV hyperglycemia (+25 mg/dL) in healthy volunteers causes:",
                [
                    "Permanent β-cell apoptosis",
                    "Marked enhancement of insulin secretion and steeper clamp dose-response",
                    "Complete loss of first-phase secretion",
                    "Abolition of incretin hormones",
                ],
                1,
                "Chronic mild hyperglycemia potentiates β-cell response—steepening hyperglycemic clamp dose-response curves.",
                ref(
                    "Slow β-Cell Response Modes and Adaptation Mechanisms",
                    "Similarly, prolonged (3–4 days) exposure to mild hyperglycemia (+25 mg/dL or 1.4 mmol/L) markedly enhances insulin secretion, with a steepening of the dose-response curve on the hyperglycemic clamp.",
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
                "The insulin secretory response is polymorphic and requires different in vivo tests to assess distinct response modes.",
                True,
                "No single test captures all β-cell modes—first phase, glucose sensitivity, potentiation, and rate sensitivity need targeted protocols and modeling.",
                ref(
                    "KEY POINTS",
                    "The ISR response is polymorphic, and its in vivo study requires different tests to assess different response modes.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Introduction",
                "Human β-cells take up glucose primarily via GLUT2.",
                False,
                "Human β-cells use GLUT1 for glucose uptake; rodent β-cells predominantly use GLUT2.",
                ref(
                    "Introduction",
                    "Thus, glucose enters human β-cells via the isoform 1 of the glucose transporter (GLUT1) and is metabolized through the glycolytic pathway and, subsequently, in mitochondrial.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Introduction",
                "The amplifying pathway of insulin secretion requires KATP channel closure.",
                False,
                "Amplifying pathway requires glucose metabolism but is KATP-channel independent—cAMP mediates potentiation.",
                ref(
                    "Introduction",
                    "The amplifying pathway also requires glucose metabolism but is KATP-channel independent.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Insulin Secretion Versus Plasma Insulin",
                "C-peptide is co-secreted with insulin in equimolar amounts and is not extracted by the liver.",
                True,
                "These properties make C-peptide ideal for deconvolution-based ISR estimation.",
                ref(
                    "Insulin Secretion Versus Plasma Insulin",
                    "C-peptide is co-secreted with insulin in equimolar amounts as a result of proinsulin cleavage, (2) C-peptide is not extracted by the liver",
                ),
            ),
            tf(
                f"{p}-t5",
                "Modes of β-Cell Response",
                "Decreased β-cell glucose sensitivity is a hallmark of all forms of glucose intolerance.",
                True,
                "Glucose sensitivity decline is progressive from IFG through IGT to overt diabetes.",
                ref(
                    "Modes of β-Cell Response",
                    "In fact, decreased glucose sensitivity is a hallmark of all forms of glucose intolerance.",
                ),
            ),
            tf(
                f"{p}-t6",
                "The Hyperglycemic Clamp and Biphasic Insulin Secretion",
                "Attenuated first-phase insulin secretion is a sensitive marker of early β-cell dysfunction.",
                True,
                "AIR loss appears in at-risk individuals and predicts incident T2D.",
                ref(
                    "The Hyperglycemic Clamp and Biphasic Insulin Secretion",
                    "attenuated first-phase insulin secretion is a very sensitive marker of early β-cell dysfunction.",
                ),
            ),
            tf(
                f"{p}-t7",
                "The Insulin Secretary Response to Oral Stimuli",
                "Insulin secretion is higher when glucose is ingested than when it is infused intravenously at the same plasma glucose levels.",
                True,
                "This oral-vs-IV difference is the incretin effect, mediated mainly by GIP and GLP1.",
                ref(
                    "The Insulin Secretary Response to Oral Stimuli",
                    "It has long been known that if glucose is ingested rather than infused, insulin secretion is higher at the same glucose levels.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Insulin Secretion in Dysglycemic States",
                "In type 2 diabetes, the incretin defect is primarily due to decreased GLP1 and GIP secretion.",
                False,
                "Hormone release is not the main defect—selective loss of β-cell response to GIP predominates.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "The incretin defect is not due to decreased GLP1 or GIP release but to a lack of response to GIP",
                ),
            ),
            tf(
                f"{p}-t9",
                "Insulin Secretion in Dysglycemic States",
                "β-cell dysfunction rather than β-cell loss is the dominant defect in type 2 diabetes.",
                True,
                "Reversibility with glycemic control and bariatric surgery supports functional 'stunned β-cell' physiology.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "These and similar findings lend strong support to the notion that β-cell dysfunction rather than β-cell loss is the dominant defect in T2D.",
                ),
            ),
            tf(
                f"{p}-t10",
                "β-Cell Mass",
                "After the first 5 years of life, β-cell proliferation in humans is very low, with average β-cell lifetime about 25 years.",
                True,
                "Adult mass maintenance relies on low replication plus peripheral neogenic niche 'virgin' β-cells.",
                ref(
                    "β-Cell Mass",
                    "Thereafter, β-cell proliferation is very low, with the average lifetime of β-cells extending to about 25 years.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Insulin Secretion in the Fasting State",
                "Pulsatile insulin secretion is disrupted in hyperglycemic states.",
                True,
                "Loss of ultradian/pulsatile control occurs in IGT and T2D though impact on tissue insulin action remains uncertain.",
                ref(
                    "Insulin Secretion in the Fasting State",
                    "Pulsatile insulin secretion is disrupted in hyperglycemic states",
                ),
            ),
            tf(
                f"{p}-t12",
                "Insulin Secretion Versus Plasma Insulin",
                "Gut hormones GLP1 and GIP reduce hepatic insulin clearance.",
                False,
                "Meier et al. showed oral glucose reduction in hepatic insulin clearance is not mediated by incretins.",
                ref(
                    "Insulin Secretion Versus Plasma Insulin",
                    "Reduction of hepatic insulin clearance after oral glucose ingestion is not mediated by glucagon-like peptide 1 or gastric inhibitory polypeptide in humans.",
                ),
            ),
            tf(
                f"{p}-t13",
                "KEY POINTS",
                "Reduced β-cell glucose sensitivity and increased absolute insulin secretion characterize early glucose intolerance.",
                True,
                "Early dysglycemia shows compensatory hypersecretion with falling sensitivity—both predict progression to overt diabetes.",
                ref(
                    "KEY POINTS",
                    "Reduced β-cell glucose sensitivity and increased absolute insulin secretion characterize the early stages of glucose intolerance and predict progression to overt diabetes.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Introduction",
                "Assertion: Glucokinase functions as the β-cell glucose sensor.",
                "Reason: Glucokinase transports glucose across the β-cell plasma membrane.",
                2,
                "Assertion true; reason false—GLUT1 transports glucose; glucokinase phosphorylates it as the rate-limiting metabolic sensor.",
                ref(
                    "Introduction",
                    "Thus, glucose enters human β-cells via the isoform 1 of the glucose transporter (GLUT1) and is metabolized through the glycolytic pathway and, subsequently, in mitochondrial.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Introduction",
                "Assertion: Closure of KATP channels depolarizes β-cells and triggers insulin exocytosis.",
                "Reason: KATP channel opening is required for Ca²⁺ influx and insulin granule fusion.",
                2,
                "Assertion true; reason false—ATP closes KATP channels; opening resets potential below Ca²⁺ channel threshold and aborts bursts.",
                ref(
                    "Introduction",
                    "Glucose metabolism raises adenosine triphosphate (ATP) production, leading to closure of the ATP-sensitive potassium (KATP) channel and membrane depolarization.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Neural Regulation of β-Cell Function",
                "Assertion: Parasympathetic stimulation enhances insulin secretion.",
                "Reason: Parasympathetic stimulation acts via α₂-adrenergic norepinephrine release.",
                2,
                "Assertion true; reason false—parasympathetic effect is M3 muscarinic acetylcholine; α₂ sympathetic inhibits insulin.",
                ref(
                    "Neural Regulation of β-Cell Function",
                    "parasympathetic stimulation (through M3 muscarinic-mediated acetylcholine release) enhances insulin and glucagon release.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Insulin Secretion Versus Plasma Insulin",
                "Assertion: Plasma insulin concentrations can distort the time course of true insulin secretion.",
                "Reason: Insulin clearance is constant and unaffected by metabolic status.",
                2,
                "Assertion true; reason false—clearance varies with stimulation, saturation, insulin sensitivity, and obesity.",
                ref(
                    "Insulin Secretion Versus Plasma Insulin",
                    "However, insulin clearance may vary during stimulation of insulin secretion and may be lower or higher depending on the metabolic status. Hence, insulin concentrations may distort the actual time course of insulin secretion.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "The Insulin Secretary Response to Oral Stimuli",
                "Assertion: The incretin effect potentiates insulin secretion when glucose is ingested orally.",
                "Reason: GIP and GLP1 are released from intestinal epithelium in response to nutrient ingestion.",
                0,
                "Both true and causally linked—enteral hormones steepen glucose–ISR dose-response at matched glycemia.",
                ref(
                    "The Insulin Secretary Response to Oral Stimuli",
                    "GIP and GLP1, which are released by the intestinal epithelium in response to nutrient ingestion, are mainly responsible for the higher insulin release and have been collectively termed incretins.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Insulin Secretion and Insulin Sensitivity",
                "Assertion: The disposition index products insulin secretion and sensitivity indices.",
                "Reason: Insulin secretion and insulin sensitivity are unrelated across individuals.",
                2,
                "Assertion true; reason false—AIR and sensitivity show reciprocal hyperbolic relationship reflecting compensation.",
                ref(
                    "Insulin Secretion and Insulin Sensitivity",
                    "The reciprocal relationship between AIR and insulin sensitivity across individuals likely reflects adaptation of the β-cell to impaired insulin action",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Genetic Influences on Insulin Secretion",
                "Assertion: MODY2 results from heterozygous GCK mutations.",
                "Reason: MODY2 causes complete absence of insulin gene expression.",
                2,
                "Assertion true; reason false—partial glucokinase deficiency reduces glucose sensitivity with rightward-shifted dose-response.",
                ref(
                    "Genetic Influences on Insulin Secretion",
                    "In MODY 2, a heterozygous private mutation of the gene (GCK) encoding glucokinase results in partial enzyme deficiency and a loss of β-cell glucose sensitivity",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Insulin Secretion in Dysglycemic States",
                "Assertion: Loss of first-phase insulin secretion is an early marker in dysglycemia progression.",
                "Reason: First-phase loss is always a primary genetic defect unrelated to fasting hyperglycemia.",
                2,
                "Assertion true; reason false—AIR loss may reflect readily releasable pool depletion from increased fasting glucose.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "Loss of first-phase insulin secretion may not, however, be a primary defect but rather a consequence of increased fasting glucose and the resultant depletion of the pool of readily releasable insulin granules.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Insulin Secretion in Dysglycemic States",
                "Assertion: Bariatric surgery can improve β-cell glucose sensitivity in T2D.",
                "Reason: Surgery necessarily regenerates all lost β-cell mass within weeks.",
                2,
                "Assertion true; reason false—improvement reflects functional recovery from glucotoxicity, not mandatory mass regeneration.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "The downward trajectory of glucose sensitivity can be reversed, at least in part, by spontaneous or therapeutic amelioration of glycemic control, as most strikingly demonstrated in diabetic patients undergoing bariatric surgery",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Insulin Secretion in Dysglycemic States",
                "Assertion: Tirzepatide is a dual GIP and GLP1 receptor agonist with therapeutic potential in T2D.",
                "Reason: GIP receptor agonism alone always reduces energy intake in humans.",
                2,
                "Assertion true; reason false—tirzepatide is stronger at GIPR but GIP itself does not reduce energy intake; coagonism enables weight loss synergy.",
                ref(
                    "Insulin Secretion in Dysglycemic States",
                    "A stronger agonist of the GIP than the GLP1 receptor, tirzepatide potentiates GLP1-induced weight loss (without GIP itself reducing energy intake).",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Modes of β-Cell Response",
                "Assertion: Potentiation enhances insulin secretion on subsequent glucose exposure.",
                "Reason: Potentiation requires abolition of all prior glucose metabolism.",
                2,
                "Assertion true; reason false—potentiation is intrinsic β-cell memory from prior glucose, incretins, or other stimuli.",
                ref(
                    "Modes of β-Cell Response",
                    "Potentiation occurs when the dose-response relationship between glucose level and insulin secretion is enhanced, as happens when prior exposure to glucose leads to greater insulin secretion on subsequent exposure.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "β-Cell Insulin Content",
                "Assertion: Younger insulin granules form the readily releasable pool.",
                "Reason: Older granules are more mobile and preferentially secreted acutely.",
                2,
                "Assertion true; reason false—younger granules are fewer but more mobile than older granules from deep cytoplasm.",
                ref(
                    "β-Cell Insulin Content",
                    "younger granules are fewer but more mobile than older granules, even if they come from deep in the cytoplasm, and therefore form a readily releasable pool.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "32",
        "title": "Physiology of Insulin Secretion",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Ele Ferrannini and Andrea Mari",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_32_Physiology_of_Insulin_Secretion.md",
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
