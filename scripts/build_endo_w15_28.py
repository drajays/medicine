#!/usr/bin/env python3
"""Generate Williams 15e module w15-28 — Endocrine Functions of Bone."""
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
OUT_NAME = "w15-28_Endocrine_Functions_of_Bone.json"


def build() -> dict:
    p = "w15-28"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why bone qualifies as an endocrine organ",
                "Bone secretes FGF23, osteocalcin, and lipocalin-2 into the circulation—hormones that regulate processes far beyond mineralization, establishing the skeleton as a true endocrine organ.",
                ref(
                    "KEY POINTS",
                    "Bone is an endocrine organ.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How bone-derived hormones gate organismal homeostasis",
                "Through glucose homeostasis, energy expenditure, stress responses, behavior, adrenal and testicular steroidogenesis, and exercise capacity, bone acts as a gatekeeper of mammalian homeostasis—not merely a passive mineral reservoir.",
                ref(
                    "KEY POINTS",
                    "The regulation of these physiologic functions by bone confers to the skeleton the role of a gatekeeper of organismal homeostasis in mammals.",
                ),
            ),
            note(
                f"{p}-n3",
                "Introduction",
                "Why kidney transplant failed to cure phosphate wasting",
                "When a healthy kidney transplant did not correct phosphate wasting, the phosphaturic factor had to originate outside the kidney—clinically foreshadowing a bone-derived phosphatonin.",
                ref(
                    "Introduction",
                    "The key observation in that regard was that transplanting a healthy kidney in a patient with phosphate wasting failed to correct the disease. This could only be explained if the mechanism accounting for phosphate wasting was not taking place in the kidney but rather originated from another organ.",
                ),
            ),
            note(
                f"{p}-n4",
                "Introduction",
                "Why FGF23 inverted the founding paradigm of bone biology",
                "PTH and active vitamin D are made outside bone and act on bone; FGF23 is synthesized by osteoblasts/osteocytes and acts on kidney—proving bone is a hormone provider, not only a recipient.",
                ref(
                    "Introduction",
                    "It is the search for this \"phosphaturic factor,\" or 'phosphatonin, as it was known for a while, that provided the first contradiction to the founding paradigm of bone biology—that is, bone is only a recipient of hormone input, not a provider of hormones, not an endocrine organ.",
                ),
            ),
            note(
                f"{p}-n5",
                "FGF23 and Phosphate Homeostasis",
                "How FGF23 lowers serum phosphate",
                "FGF23 is phosphaturic (inhibits proximal NaPi-IIa/c) and suppresses intestinal phosphate absorption indirectly by lowering renal 1α-hydroxylase and raising 24-hydroxylase—reducing circulating 1,25(OH)₂D.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "On the one hand, FGF23 is phosphaturic because it inhibits the expression in the proximal tubule of type IIa and IIc sodium phosphate cotransporters that allow the reabsorption of phosphate ions.",
                ),
            ),
            note(
                f"{p}-n6",
                "FGF23 and Phosphate Homeostasis",
                "Why FGF23 requires FGFR1c plus α-Klotho",
                "FGF23 lacks a heparin-binding site (facilitating endocrine release) and signals through a receptor complex of FGFR1c and α-Klotho—without Klotho, canonical FGF signaling cannot execute FGF23's hormonal actions.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "After its binding to a cell surface receptor complex comprising a conventional FGF receptor (FGFR), mostly FGFR1c, and a coreceptor named  $ \\alpha $-Khothlo, FGF23 fulfills its endocrine functions.",
                ),
            ),
            note(
                f"{p}-n7",
                "FGF23 and Phosphate Homeostasis",
                "How FGF23 suppresses active vitamin D production",
                "Renal FGF23 signaling inhibits Cyp27B1 (1α-hydroxylase) and enhances Cyp24A1 (24-hydroxylase), lowering 1,25(OH)₂D and thereby reducing intestinal phosphate absorption.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "Indeed, FGF23 inhibits the renal expression of  $ Cyp27B1 $, which encodes the 1 $ \\alpha $-hydroxylase, and on the other hand, it enhances the renal expression of  $ cyp24A1 $, which encodes the 24 hydroxylase.",
                ),
            ),
            note(
                f"{p}-n8",
                "FGF23 and Phosphate Homeostasis",
                "Why chronically elevated FGF23 in CKD extends beyond phosphate",
                "Massive FGF23 elevation in CKD associates with left ventricular hypertrophy, impaired iron metabolism, and suppressed erythropoiesis—some effects may occur independently of α-Klotho signaling.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "For instance, the chronic elevation of circulating FGF23 levels favors left ventricular hypertrophy in the heart; it can also affect iron metabolism and inhibit erythropoiesis in the bone marrow.",
                ),
            ),
            note(
                f"{p}-n9",
                "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                "How carboxylated vs uncarboxylated osteocalcin differ",
                "γ-carboxylation on three glutamate residues increases hydroxyapatite affinity—carboxylated osteocalcin accumulates in bone ECM as bone Gla protein (BGP); the smaller uncarboxylated fraction in circulation carries hormonal activity.",
                ref(
                    "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                    "Osteocalcin can be carboxylated on three glutamate residues, a posttranslational modification that increases the affinity of the protein for the hydroxyapatite crystals and the mineralized bone ECM, hence its other name, bone Gla protein (BGP).",
                ),
            ),
            note(
                f"{p}-n10",
                "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                "Why uncarboxylated osteocalcin—not the ECM pool—is bioactive",
                "The abundant carboxylated form was long assumed to drive mineralization (never convincingly proven in vivo); the less abundant uncarboxylated circulating fraction is the hormonally active species.",
                ref(
                    "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                    "As it turned out, this fraction is the one with the richest biological activity.",
                ),
            ),
            note(
                f"{p}-n11",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "How insulin drives osteocalcin decarboxylation",
                "Insulin signaling in osteoblasts increases osteoclast differentiation and resorption; the acidic pH of resorption lacunae decarboxylates osteocalcin, releasing bioactive hormone into circulation.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "A consequence of that function of insulin signaling in osteoblasts is that it allows the decarboxylation of osteocalcin through the acidic pH that exists in the resorption lacunae.",
                ),
            ),
            note(
                f"{p}-n12",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "Why osteocalcin raises energy expenditure",
                "Osteocalcin is necessary and sufficient to increase energy expenditure; Osteocalcin-deficient mice gain visceral fat—linking bone hormone output to whole-body energy balance.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "Through cellular and molecular mechanisms that have still not been elucidated, osteocalcin is necessary and sufficient to increase energy expenditure (see Fig. 28.2).",
                ),
            ),
            note(
                f"{p}-n13",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "How osteocalcin opposes insulin in the liver",
                "Via GPRC6A in hepatocytes, osteocalcin promotes Pepck and G6pc expression and de novo gluconeogenesis—an insulin-independent counter-regulatory arm of osteocalcin biology.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "signaling, also through Gprc6a in hepatocytes, favors de novo gluconeogenesis by promoting the expression of Pepck and G6pa, two genes that encode key enzymes implicated in this process.",
                ),
            ),
            note(
                f"{p}-n14",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "Why circulating osteocalcin rises during endurance exercise",
                "Exercise-associated osteocalcin elevation in mice and humans suggested a bone hormone regulating exercise capacity—confirmed by myofiber GPRC6A loss-of-function impairing muscle performance.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "its circulating levels increase during an endurance exercise, an observation made in mice and humans that suggested that osteocalcin may be a hormone regulating exercise.",
                ),
            ),
            note(
                f"{p}-n15",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "How the bone–muscle IL-6 feed-forward loop works",
                "During exercise, osteocalcin via GPRC6A in myofibers stimulates IL-6 (a myokine); IL-6 in turn upregulates bioactive osteocalcin release from bone—maximizing exercise capacity.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "In addition, and again only during exercise, osteocalcin signaling in myofibers favors the synthesis of interleukin 6 (IL6), a myokine that, in return, needs to upregulate the release of bioactive osteocalcin from bone to be able to enhance exercise capacity.",
                ),
            ),
            note(
                f"{p}-n16",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "Why osteocalcin promotes male fertility but not female steroidogenesis",
                "GPRC6A in Leydig cells is necessary for testosterone biosynthesis and male fertility even with intact pituitary function; GPRC6A is not expressed in ovary and osteocalcin does not promote female gonadal steroidogenesis.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "Gprc6a is not expressed in the ovary, and osteocalcin does not appear to promote steroidogenesis in the female gonad.",
                ),
            ),
            note(
                f"{p}-n17",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "How osteocalcin modulates anxiety and cognition via the brain",
                "Osteocalcin crosses the BBB, binds GPR158 in neurons (hippocampus, VTA, brainstem), favors BDNF and monoamine synthesis, inhibits GABA—preventing anxiety and promoting spatial learning.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "Behavioral analysis performed in mice lacking osteocalcin signaling in the brain or in wild-type (WT) mice receiving exogenous osteocalcin showed that osteocalcin is necessary and sufficient to prevent the development of anxiety and promote spatial learning, two functions that are particularly affected in older mice.",
                ),
            ),
            note(
                f"{p}-n18",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Why maternal placental osteocalcin shapes adult cognition",
                "Maternal osteocalcin crosses the placenta, prevents hippocampal neuronal apoptosis, and together with postnatal osteocalcin establishes anxiety/cognition circuits in offspring.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "These functions of osteocalcin rely, in part, on maternal osteocalcin that crosses the placenta and prevents neuronal apoptosis in the hippocampal region and postnatal osteocalcin.",
                ),
            ),
            note(
                f"{p}-n19",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "How osteocalcin initiates the acute stress response",
                "Stress glutamate from basolateral amygdala enters osteoblasts via Glast, allosterically inhibits γ-carboxylase → uncarboxylated osteocalcin → GPRC6A in parasympathetic neurons inhibits acetylcholine, unopposing sympathetic tone.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "Glutamate, intracellularly, acts as an allosteric inhibitor of  $ \\gamma $ carboxylase, the enzyme responsible for the carboxylation of osteocalcin.",
                ),
            ),
            note(
                f"{p}-n20",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Why embryonic osteocalcin programs lifelong adrenal steroidogenesis",
                "Embryo-derived osteocalcin via GPRC6A upregulates SF1 in adrenal cortex, enabling glucocorticoid (cortisol/corticosterone) and aldosterone biosynthesis throughout life—regulating BP and potassium independently of postnatal osteocalcin.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "This set of functions of osteocalcin is achieved by embryo-derived osteocalcin, which upregulates the transcription factor SF1, a master gene of adrenal development.",
                ),
            ),
            note(
                f"{p}-n21",
                "Lipocalin-2: Another Bone-Derived Hormone",
                "Lipocalin-2: osteoblast-derived anorexigenic hormone",
                "LCN2 is secreted by osteoblasts (not only adipose), signals via MC4R in paraventricular hypothalamic neurons to suppress appetite—an endocrine function osteocalcin does not share.",
                ref(
                    "Lipocalin-2: Another Bone-Derived Hormone",
                    "It is an anorexigenic molecule that acts by signaling in neurons of the paraventricular nucleus of the hypothalamus through the melanocortin-4 receptor (MC4R).",
                ),
            ),
            note(
                f"{p}-n22",
                "Lipocalin-2: Another Bone-Derived Hormone",
                "How LCN2 counter-regulates obesity-induced metabolic dysfunction",
                "Obesity raises circulating LCN2, which decreases food intake and promotes β-cell proliferation and insulin secretion—partially compensating for obesity-related glucose intolerance.",
                ref(
                    "Lipocalin-2: Another Bone-Derived Hormone",
                    "Experiments performed in rodents and humans indicate that the increase in circulating lipocalin-2 levels observed in the case of obesity may serve to counteract obesity-induced glucose intolerance by decreasing food intake and promoting pancreatic  $ \\beta $-cell proliferation (see Fig. 28.2).",
                ),
            ),
            note(
                f"{p}-n23",
                "Perspectives",
                "Why burosumab validates bone-hormone therapeutics",
                "Anti-FGF23 antibody (burosumab) raises serum phosphate in X-linked hypophosphatemia—first clinical proof that targeting a bone-derived hormone treats mineral metabolism disease.",
                ref(
                    "Perspectives",
                    "This question has already been, at least partially, answered positively in the case of FGF23 because a humanized anti-FGF23 antibody increased serum phosphate levels in patients with X-linked hypophosphatemia.",
                ),
            ),
            note(
                f"{p}-n24",
                "Perspectives",
                "Therapeutic potential of osteocalcin and LCN2 pathways",
                "Injection in primates and human cell studies show osteocalcin/LCN2 upregulate the processes mouse genetics identified—glucose homeostasis, exercise capacity, cognition, and appetite—targeting obesity, sarcopenia, and age-related memory loss.",
                ref(
                    "Perspectives",
                    "A second one is that both osteocalcin and lipocalin-2 regulate physiologic processes—such as glucose homeostasis for both, exercise capacity and cognition for osteocalcin, and appetite for lipocalin-2—that are affected in frequent human diseases, such as obesity, sarcopenia, and age-related memory loss, which, at least for the last two, represent areas of unmet medical needs.",
                ),
            ),
            note(
                f"{p}-n25",
                "FGF23 and Phosphate Homeostasis",
                "FGF23 production: feedback regulators",
                "High phosphate, 1,25(OH)₂D, iron deficiency, erythropoietin, and inflammatory cytokines promote FGF23; insulin and IGF-1 inhibit it—forming a multi-input feedback network.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "Moreover, in a classical feedback loop, FGF23 production is also promoted by 1,25 (OH) $ _2 $ vitamin D $ _3 $, iron deficiency (through transcriptional and posttranslational mechanisms), erythropoietin, and inflammatory cytokines, whereas it is inhibited by insulin and insulin-like growth factor 1 (IGF1) (Fig. 28.1).",
                ),
            ),
            note(
                f"{p}-n26",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "GPRC6A: central osteocalcin receptor in metabolism",
                "GPRC6A mediates osteocalcin effects in β-cells (insulin), hepatocytes (gluconeogenesis), myofibers (exercise), and Leydig cells (testosterone)—loss-of-function mutations link testicular failure and glucose intolerance in humans.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "The molecular analysis of patients demonstrating primary testicular failure identified a loss-of-function mutation in Gprc6a in two individuals who were also glucose intolerant.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "FGF23 and Phosphate Homeostasis",
                "A 6-year-old has rickets, low serum phosphate, normal calcium, and elevated FGF23. Family history is consistent with autosomal-dominant hypophosphatemic rickets. Where is the excess FGF23 produced?",
                [
                    "Proximal renal tubule",
                    "Osteoblasts and osteocytes",
                    "Parathyroid chief cells",
                    "Hepatocytes",
                ],
                1,
                "FGF23 is mainly expressed in and secreted by osteoblasts and osteocytes—identifying bone as the endocrine source of the phosphaturic hormone.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "FGF23 is mainly expressed in and secreted by osteoblasts and osteocytes, a finding that identified the de facto bone as an endocrine organ.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "FGF23 and Phosphate Homeostasis",
                "A patient with tumor-induced osteomalacia has very high FGF23 and low phosphate. After surgical resection of a mesenchymal tumor, phosphate normalizes. Which receptor complex mediates FGF23's renal phosphaturic effect?",
                [
                    "FGFR3 alone",
                    "FGFR1c with α-Klotho coreceptor",
                    "PTH/PTHrP receptor (PTHR1)",
                    "Calcium-sensing receptor (CaSR)",
                ],
                1,
                "FGF23 signals through FGFR1c plus α-Klotho; in the kidney this inhibits proximal phosphate reabsorption.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "After its binding to a cell surface receptor complex comprising a conventional FGF receptor (FGFR), mostly FGFR1c, and a coreceptor named  $ \\alpha $-Khothlo, FGF23 fulfills its endocrine functions.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "FGF23 and Phosphate Homeostasis",
                "A CKD stage 4 patient has markedly elevated FGF23, low 1,25(OH)₂D, and secondary hyperparathyroidism. Besides phosphaturia, how does FGF23 lower intestinal phosphate absorption?",
                [
                    "Direct inhibition of intestinal NaPi cotransporters",
                    "Suppression of renal Cyp27B1 and induction of Cyp24A1",
                    "Stimulation of calcitonin secretion",
                    "Increased PTH-mediated gut calcium absorption only",
                ],
                1,
                "FGF23 reduces active vitamin D by inhibiting 1α-hydroxylase and enhancing 24-hydroxylase, indirectly lowering intestinal phosphate absorption.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "The end result of these two actions is to lower the circulating levels of 1 $ \\alpha $25 ( $ OH)_2 $ vitamin  $ D_3 $, a hormone that favors intestinal absorption of phosphate.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "FGF23 and Phosphate Homeostasis",
                "A dialysis patient has extreme FGF23 elevation, anemia, and echocardiographic LVH. Which FGF23 effect is most likely independent of α-Klotho in this setting?",
                [
                    "Proximal tubular phosphate wasting",
                    "Left ventricular hypertrophy",
                    "Inhibition of NaPi-IIa",
                    "Suppression of Cyp27B1",
                ],
                1,
                "Several deleterious FGF23 effects in CKD (LVH, iron metabolism, erythropoiesis) may occur independently of α-Klotho signaling.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "Intriguingly, several of these effects of an increase in circulating FGF23 levels seem to occur independently of its signaling through the  $ \\alpha $-Klotho protein.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Perspectives",
                "A 12-year-old with X-linked hypophosphatemia has persistently low phosphate despite phosphate and calcitriol. Anti-FGF23 antibody therapy is considered. Expected mechanism?",
                [
                    "Stimulates osteoblast FGF23 secretion",
                    "Neutralizes circulating FGF23, reducing renal phosphate wasting",
                    "Directly activates renal 1α-hydroxylase",
                    "Blocks PTH secretion from parathyroids",
                ],
                1,
                "Burosumab (humanized anti-FGF23) increases serum phosphate in XLH by counteracting excess phosphaturic FGF23.",
                ref(
                    "Perspectives",
                    "This question has already been, at least partially, answered positively in the case of FGF23 because a humanized anti-FGF23 antibody increased serum phosphate levels in patients with X-linked hypophosphatemia.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                "A researcher measures total osteocalcin in serum and bone ECM. Which form is most abundant in mineralized matrix and binds hydroxyapatite?",
                [
                    "Uncarboxylated osteocalcin",
                    "Carboxylated osteocalcin (bone Gla protein)",
                    "Osteopontin",
                    "Matrix Gla protein only in circulation",
                ],
                1,
                "γ-carboxylation increases hydroxyapatite affinity; carboxylated osteocalcin accumulates in ECM as the most abundant noncollagenous protein.",
                ref(
                    "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                    "This explains why carboxylated osteocalcin accumulates in the bone ECM to the point where it is the most abundant noncollagenous protein found in the bone ECM.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "A mouse model lacks insulin signaling in osteoblasts and develops glucose intolerance on normal chow. Which downstream bone mechanism links osteoblast insulin to systemic glucose?",
                [
                    "Increased bone mineralization trapping glucose",
                    "Insulin-driven osteoclast activity and acidic decarboxylation of osteocalcin",
                    "Suppression of FGF23 in osteocytes",
                    "Direct pancreatic islet transplantation from bone marrow",
                ],
                1,
                "Osteoblast insulin signaling increases osteoclast differentiation/resorption; lacunar acid pH decarboxylates osteocalcin, releasing bioactive hormone.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "A consequence of that function of insulin signaling in osteoblasts is that it allows the decarboxylation of osteocalcin through the acidic pH that exists in the resorption lacunae.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "An Osteocalcin-deficient mouse on high-fat diet has worse glucose intolerance than wild-type littermates. Best explanation?",
                [
                    "Loss of osteoblast-dependent insulin resistance component",
                    "Osteocalcin normally promotes β-cell proliferation and insulin secretion",
                    "Excess FGF23 from bone",
                    "Complete absence of hepatic gluconeogenesis",
                ],
                1,
                "Osteocalcin favors β-cell proliferation and insulin secretion; its absence worsens metabolic adaptation to high-fat feeding.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "Both at rest and during exercise, osteocalcin favors pancreatic  $ \\beta $-cell proliferation, expression in and secretion by these cells of insulin, and therefore glucose homeostasis in rodents and primates.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "During a fasting study, hepatic GPRC6A is activated by osteocalcin. Which metabolic pathway is upregulated—counter to insulin's effect?",
                [
                    "Glycogen synthesis",
                    "De novo gluconeogenesis via Pepck and G6pc",
                    "Fatty acid synthesis",
                    "Ketogenesis suppression",
                ],
                1,
                "Osteocalcin via GPRC6A in hepatocytes promotes Pepck/G6pc and gluconeogenesis—an insulin-independent counter-regulatory function.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "signaling, also through Gprc6a in hepatocytes, favors de novo gluconeogenesis by promoting the expression of Pepck and G6pa, two genes that encode key enzymes implicated in this process.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "A 55-year-old marathon runner has higher osteocalcin than sedentary peers. Mice lacking osteocalcin signaling in myofibers show impaired exercise performance. Primary receptor in muscle?",
                [
                    "GPR158",
                    "GPRC6A",
                    "MC4R",
                    "FGFR1c",
                ],
                1,
                "Osteocalcin signals in myofibers through GPRC6A during exercise to enhance nutrient uptake and ATP production.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "To achieve its regulation of muscle function during exercise, osteocalcin signaling in myofibers through Gprc6a favors, only during exercise, uptake and catabolism of the two primary nutrients of myofibers, glucose and fatty acids (FAs).",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "An athlete's IL-6 rises during prolonged exercise. How does this myokine interact with bone to maximize exercise capacity?",
                [
                    "IL-6 suppresses all osteocalcin release",
                    "IL-6 upregulates bioactive osteocalcin release from bone in a feed-forward loop",
                    "IL-6 blocks GPRC6A in muscle",
                    "IL-6 converts carboxylated osteocalcin in plasma",
                ],
                1,
                "Exercise-induced IL-6 from muscle upregulates osteocalcin release from bone—completing a bone–muscle endocrine feed-forward loop.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "a myokine that, in return, needs to upregulate the release of bioactive osteocalcin from bone to be able to enhance exercise capacity.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "A man with primary testicular failure and impaired glucose tolerance is found to have a GPRC6A loss-of-function mutation. In which cell type does osteocalcin normally promote testosterone synthesis?",
                [
                    "Ovarian granulosa cells",
                    "Leydig cells of the testes",
                    "Adrenal zona glomerulosa only",
                    "Pituitary gonadotrophs",
                ],
                1,
                "Osteocalcin signaling through GPRC6A in Leydig cells is necessary for testosterone biosynthesis and male fertility.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "Indeed, osteocalcin signaling in Leydig cells of the testes through Gprc6a is necessary for testosterone biosynthesis and therefore for male fertility, even in animals with normal pituitary functions.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Osteocalcin-deficient mice are notably docile. Anxiety testing shows increased anxiety-like behavior correctable by exogenous osteocalcin. Which brain receptor mediates cognition/anxiety effects in neurons?",
                [
                    "GPR37 in oligodendrocytes only",
                    "GPR158 in neurons",
                    "MC4R in hypothalamus",
                    "α-Klotho in choroid plexus",
                ],
                1,
                "Osteocalcin binds GPR158 in neurons (and GPR37 in oligodendrocytes); GPR158 mediates anxiety prevention and spatial learning.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "osteocalcin can cross the blood-brain barrier and binds in specific regions in the brain through two distinct receptors, Gpr158 in neurons and Cpr37 in oligodendrocytes.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "A pregnant mouse model lacks maternal osteocalcin transfer. Adult offspring show hippocampal neuronal apoptosis and cognitive deficits. Which transport route is critical?",
                [
                    "Osteocalcin in breast milk",
                    "Maternal osteocalcin crossing the placenta",
                    "FGF23 from fetal liver",
                    "LCN2 from adipose tissue only",
                ],
                1,
                "Maternal osteocalcin crosses the placenta, prevents hippocampal neuronal apoptosis, and contributes to adult cognition.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "These functions of osteocalcin rely, in part, on maternal osteocalcin that crosses the placenta and prevents neuronal apoptosis in the hippocampal region and postnatal osteocalcin.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "A mouse exposed to acute predator stress fails to mount a normal sympathetic stress response when osteocalcin signaling is absent. First step in the osteocalcin stress cascade?",
                [
                    "Cortisol release from adrenal cortex",
                    "Glutamate from basolateral amygdala inhibits osteoblast γ-carboxylase via Glast",
                    "Insulin surge from pancreas",
                    "LCN2 suppression of appetite",
                ],
                1,
                "Stress glutamate enters osteoblasts via Glast, inhibiting γ-carboxylase and releasing uncarboxylated osteocalcin to initiate the acute stress response.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "Those neurons use glutamate as a neurotransmitter, which enters osteoblasts through the glutamate transporter Glast.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "A mouse with embryonic osteocalcin deficiency has low corticosterone and aldosterone despite intact HPA axis. Which transcription factor is upregulated by embryonic osteocalcin in adrenal cortex?",
                [
                    "SF1",
                    "FOXO1",
                    "PPARγ",
                    "CREB",
                ],
                0,
                "Embryo-derived osteocalcin upregulates SF1, the master transcription factor of adrenal development, programming lifelong steroidogenesis.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "This set of functions of osteocalcin is achieved by embryo-derived osteocalcin, which upregulates the transcription factor SF1, a master gene of adrenal development.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Lipocalin-2: Another Bone-Derived Hormone",
                "Inducible osteoblast ablation causes metabolic abnormalities beyond osteocalcin loss. LCN2 is identified as another bone hormone. Its anorexigenic effect is mediated through which receptor?",
                [
                    "GPRC6A in muscle",
                    "MC4R in paraventricular hypothalamic neurons",
                    "FGFR1c in kidney",
                    "GPR158 in hippocampus",
                ],
                1,
                "Bone-derived LCN2 signals via MC4R in PVN neurons to suppress appetite—distinct from osteocalcin's targets.",
                ref(
                    "Lipocalin-2: Another Bone-Derived Hormone",
                    "It is an anorexigenic molecule that acts by signaling in neurons of the paraventricular nucleus of the hypothalamus through the melanocortin-4 receptor (MC4R).",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Lipocalin-2: Another Bone-Derived Hormone",
                "An obese patient has elevated serum LCN2 with relatively preserved glucose tolerance. Best interpretation?",
                [
                    "LCN2 worsens insulin resistance",
                    "LCN2 may counteract obesity-induced glucose intolerance via anorexia and β-cell effects",
                    "LCN2 is only an adipokine unrelated to bone",
                    "LCN2 suppresses all insulin secretion",
                ],
                1,
                "Obesity-associated LCN2 rise may compensate by reducing food intake and promoting β-cell proliferation/insulin secretion.",
                ref(
                    "Lipocalin-2: Another Bone-Derived Hormone",
                    "Experiments performed in rodents and humans indicate that the increase in circulating lipocalin-2 levels observed in the case of obesity may serve to counteract obesity-induced glucose intolerance by decreasing food intake and promoting pancreatic  $ \\beta $-cell proliferation (see Fig. 28.2).",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Introduction",
                "A medical student states: 'Bone only receives hormonal input from PTH and vitamin D; it cannot secrete endocrine factors.' Which discovery refutes this?",
                [
                    "Discovery of calcitonin from thyroid C cells",
                    "Identification of FGF23 from osteoblasts/osteocytes as a phosphaturic hormone",
                    "RANKL expression on T lymphocytes",
                    "Leptin secretion from marrow adipocytes only",
                ],
                1,
                "FGF23 secretion by osteoblasts/osteocytes was the first definitive evidence that bone is an endocrine organ.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "FGF23 is mainly expressed in and secreted by osteoblasts and osteocytes, a finding that identified the de facto bone as an endocrine organ.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "FGF23 and Phosphate Homeostasis",
                "A patient with iron deficiency anemia has rising FGF23. Which regulators of FGF23 production are relevant?",
                [
                    "FGF23 is only inhibited by phosphate",
                    "Iron deficiency promotes FGF23; insulin and IGF-1 inhibit it",
                    "FGF23 is exclusively stimulated by PTH",
                    "Calcitonin is the main FGF23 inducer",
                ],
                1,
                "FGF23 is promoted by phosphate, vitamin D, iron deficiency, EPO, and cytokines; insulin/IGF-1 inhibit production.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "FGF23 production is also promoted by 1,25 (OH) $ _2 $ vitamin D $ _3 $, iron deficiency (through transcriptional and posttranslational mechanisms), erythropoietin, and inflammatory cytokines, whereas it is inhibited by insulin and insulin-like growth factor 1 (IGF1) (Fig. 28.1).",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "GPR37 signaling by osteocalcin in the CNS primarily affects which cell lineage?",
                [
                    "Neuronal monoamine synthesis only",
                    "Oligodendrocyte differentiation and myelination",
                    "Microglial phagocytosis",
                    "Astrocyte glutamate uptake exclusively",
                ],
                1,
                "Osteocalcin via GPR37 in oligodendrocytes promotes differentiation and CNS myelination.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "osteocalcin signals through another GPCR, GPR37, in oligodendrocytes to favor the differentiation of these cells and myelination in the CNS (see Fig. 28.3).",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "An older mouse receives osteocalcin supplementation and shows improved treadmill endurance. Why might older animals respond more than young?",
                [
                    "Older mice have higher circulating osteocalcin",
                    "Circulating osteocalcin drops steeply in adulthood when its regulated functions also decline",
                    "GPRC6A is absent in young muscle",
                    "IL-6 is only produced in aged muscle",
                ],
                1,
                "Postnatal osteocalcin falls steeply with age, paralleling decline in functions it regulates—creating therapeutic window in older animals.",
                ref(
                    "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                    "postnatally, circulating osteocalcin levels drop early and steeply during adulthood.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Uncarboxylated osteocalcin during acute stress signals in postganglionic parasympathetic neurons to inhibit acetylcholine synthesis/reuptake. Net physiologic effect?",
                [
                    "Enhanced parasympathetic tone",
                    "Unopposed sympathetic tone initiating acute stress response",
                    "Complete autonomic shutdown",
                    "Increased GABAergic inhibition only",
                ],
                1,
                "Reduced parasympathetic acetylcholine leaves sympathetic tone unopposed, allowing the acute stress response to unfold.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "this leaves the sympathetic tone unopposed, and the acute stress response can then start (see Fig. 28.3).",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Lipocalin-2: Another Bone-Derived Hormone",
                "Besides anorexia, LCN2 shares which metabolic function with osteocalcin?",
                [
                    "Promotion of male testosterone synthesis",
                    "Favoring pancreatic β-cell proliferation and insulin secretion",
                    "GPR158-mediated cognition",
                    "Adrenal SF1 upregulation",
                ],
                1,
                "Like osteocalcin, LCN2 promotes β-cell proliferation, insulin secretion, glucose tolerance, and insulin sensitivity.",
                ref(
                    "Lipocalin-2: Another Bone-Derived Hormone",
                    "In addition, and as osteocalcin does, lipocalin-2 favors pancreatic  $ \\beta $-cell proliferation, induces insulin secretion, and promotes glucose tolerance and insulin sensitivity.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "FGF23 and Phosphate Homeostasis",
                "Long-term FGF23 exposure vs acute FGF23 on parathyroid cells differs how?",
                [
                    "FGF23 never affects parathyroid glands",
                    "Acute FGF23 reduces PTH; chronic elevation may promote parathyroid hyperplasia",
                    "FGF23 always stimulates PTH within hours",
                    "FGF23 only acts when α-Klotho is absent",
                ],
                1,
                "FGF23 acutely suppresses PTH but chronic elevation may drive parathyroid proliferation—relevant to CKD secondary hyperparathyroidism.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "Although FGF23 can reduce the production and secretion of PTH within hours, a long-term treatment favors parathyroid cell proliferation.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Perspectives",
                "A biotech team proposes osteocalcin infusion for sarcopenia in older adults. What preclinical evidence supports this approach?",
                [
                    "Osteocalcin only affects bone mineral density",
                    "Pharmacologic osteocalcin enhances exercise capacity and muscle function, especially when endogenous levels are low",
                    "Osteocalcin cannot cross the blood-brain barrier",
                    "Human GPRC6A is not expressed in muscle",
                ],
                1,
                "Genetic and pharmacologic studies show osteocalcin is sufficient to enhance muscle function during exercise and capacity, particularly in older low-osteocalcin mice.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "Further genetic and pharmacologic studies showed that osteocalcin signaling in myofibers is also sufficient to enhance muscle function during exercise; increase the exercise capacity of young mice, and even more so in older mice, that have low circulating osteocalcin levels; and regulate muscle mass (Fig. 28.3).",
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
                "The main bone-derived hormones discussed in this chapter are FGF23, osteocalcin, and lipocalin-2.",
                True,
                "These three are the principal bone-secreted hormones covered in Williams Ch. 28.",
                ref(
                    "KEY POINTS",
                    "The main hormones made by bone are fibroblast growth factor 23 (FGF23), osteocalcin, and lipocalin-2.",
                ),
            ),
            tf(
                f"{p}-t2",
                "FGF23 and Phosphate Homeostasis",
                "FGF23, FGF19/15, and FGF21 lack heparin-binding sites, facilitating their release into the circulation as endocrine hormones.",
                True,
                "This subfamily lacks heparin-binding domains, distinguishing them from conventional autocrine/paracrine FGFs.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "Whereas conventional fibroblast growth factors (FGFs) have a heparin-binding site that is necessary for their autocrine and paracrine actions, FGF15/19, FGF21, and FGF23 lack this heparin-binding ability; this feature facilitates their release into the general circulation and defines in part their hormonal nature.",
                ),
            ),
            tf(
                f"{p}-t3",
                "FGF23 and Phosphate Homeostasis",
                "High circulating phosphate levels inhibit FGF23 production by osteoblasts and osteocytes.",
                False,
                "High phosphate is a positive regulator of FGF23 biosynthesis, not an inhibitor.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "Consistent with its physiologic functions, the production of FGF23 by osteoblasts/osteocytes is favored by high circulating phosphate levels through poorly elucidated mechanisms.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                "Osteocalcin is present in breast milk and is the main postnatal source of bioactive osteocalcin for the neonate.",
                False,
                "Osteocalcin crosses the placenta and BBB but is not present in milk.",
                ref(
                    "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                    "Maternal osteocalcin crosses the placenta; osteocalcin crosses the blood-brain barrier; it is not present in the milk; and postnatally, circulating osteocalcin levels drop early and steeply during adulthood.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "Osteocalcin signaling in Leydig cells through GPRC6A is necessary for testosterone biosynthesis and male fertility.",
                True,
                "This was demonstrated across multiple mouse models and conserved to humans with GPRC6A mutations.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "Indeed, osteocalcin signaling in Leydig cells of the testes through Gprc6a is necessary for testosterone biosynthesis and therefore for male fertility, even in animals with normal pituitary functions.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "Osteocalcin promotes steroidogenesis in ovarian granulosa cells via GPRC6A.",
                False,
                "GPRC6A is not expressed in ovary; osteocalcin does not promote female gonadal steroidogenesis.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "Gprc6a is not expressed in the ovary, and osteocalcin does not appear to promote steroidogenesis in the female gonad.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "Bone-specific insulin resistance on a high-fat diet worsens glucose intolerance partly through reduced osteocalcin activation.",
                True,
                "Osteoblast insulin resistance disrupts osteocalcin decarboxylation and whole-body glucose homeostasis.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "Pushing this investigation even further revealed that the severity of the glucose intolerance that mice develop when fed a high-fat diet is, in part, a consequence of osteoblast-dependent insulin resistance.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Osteocalcin-deficient mice display increased aggressivity compared with wild-type mice.",
                False,
                "The overt phenotype is docility and lack of aggressivity in both sexes.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "The most overt phenotype of mice lacking osteocalcin is their lack of aggressivity.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Acute stressors cause a peak in circulating osteocalcin, and without osteocalcin the acute stress response does not unfold normally.",
                True,
                "Osteocalcin meets criteria for a stress hormone: stress-induced peak and necessity for acute stress response.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "Osteocalcin has the two main features of a stress hormone: its circulating levels peak in response to a stressor, and in its absence, the acute stress response does not unfold.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Postnatal circulating osteocalcin regulates blood pressure and potassium homeostasis via adrenal mineralocorticoid production.",
                False,
                "BP and potassium regulation by osteocalcin depend on embryonic/developmental osteocalcin programming adrenal steroidogenesis, not the postnatal pool.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "This explains why and how developmental osteocalcin, through its regulation of adrenal steroidogenesis, regulates blood pressure and blood potassium concentrations, two functions that are not regulated by the postnatal pool of osteocalcin (see Fig. 28.3).",
                ),
            ),
            tf(
                f"{p}-t11",
                "Lipocalin-2: Another Bone-Derived Hormone",
                "Lipocalin-2 was previously considered only an adipokine before being identified as osteoblast-derived.",
                True,
                "Molecular/genetic work identified LCN2 as a bone-derived hormone with distinct functions from osteocalcin.",
                ref(
                    "Lipocalin-2: Another Bone-Derived Hormone",
                    "A molecular and genetic approach identified lipocalin-2, a molecule previously viewed as being an adipokine, as an osteoblast-derived polypeptide hormone.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Lipocalin-2: Another Bone-Derived Hormone",
                "The anorexigenic effect of lipocalin-2 has been demonstrated only in rodents, not in primates.",
                False,
                "The same anorexigenic function was subsequently demonstrated in primates.",
                ref(
                    "Lipocalin-2: Another Bone-Derived Hormone",
                    "The same anorexigenic function has subsequently been demonstrated for lipocalin-2 in primates.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Perspectives",
                "Anti-FGF23 antibody therapy has been shown to increase serum phosphate in patients with X-linked hypophosphatemia.",
                True,
                "Burosumab validated clinical targeting of bone-derived FGF23 in XLH.",
                ref(
                    "Perspectives",
                    "This question has already been, at least partially, answered positively in the case of FGF23 because a humanized anti-FGF23 antibody increased serum phosphate levels in patients with X-linked hypophosphatemia.",
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
                "Assertion: Bone is an endocrine organ that secretes hormones affecting extra-skeletal physiology.",
                "Reason: FGF23 is synthesized by osteoblasts and osteocytes and acts on the kidney to lower phosphate.",
                0,
                "Both true and causally linked—FGF23 secretion from bone and renal phosphaturia established bone as an endocrine organ.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "FGF23 is mainly expressed in and secreted by osteoblasts and osteocytes, a finding that identified the de facto bone as an endocrine organ.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "FGF23 and Phosphate Homeostasis",
                "Assertion: FGF23 lowers serum phosphate by inhibiting proximal tubular phosphate reabsorption.",
                "Reason: FGF23 directly stimulates intestinal phosphate absorption.",
                2,
                "Assertion true; reason false—FGF23 is phosphaturic and indirectly reduces intestinal phosphate absorption by lowering active vitamin D.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "On the other hand, through its signaling in the kidney, FGF23 indirectly inhibits phosphate intestinal absorption.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "FGF23 and Phosphate Homeostasis",
                "Assertion: Chronic FGF23 elevation in CKD may contribute to secondary hyperparathyroidism.",
                "Reason: Long-term FGF23 exposure can promote parathyroid cell proliferation.",
                0,
                "Both true and linked—chronic FGF23 may drive parathyroid hyperplasia despite acute PTH suppression.",
                ref(
                    "FGF23 and Phosphate Homeostasis",
                    "This latter function of FGF23 suggests that the elevation of circulating FGF23 levels seen in patients with chronic kidney disease may be a cause of secondary hyperparathyroidism.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                "Assertion: Uncarboxylated osteocalcin in circulation has greater biological activity than the carboxylated ECM pool.",
                "Reason: Carboxylated osteocalcin has high affinity for hydroxyapatite and accumulates abundantly in bone matrix.",
                1,
                "Both true but the reason explains ECM retention, not why uncarboxylated form is bioactive—the reason does not explain the assertion.",
                ref(
                    "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                    "Not surprisingly, the existence of a carboxylated form of osteocalcin, together with its remarkable abundance in the bone ECM, explains why osteocalcin was initially thought to be implicated in bone mineralization.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "Assertion: Insulin signaling in osteoblasts is necessary for whole-body glucose homeostasis on normal chow.",
                "Reason: Insulin increases osteoclast activity and acidic decarboxylation of osteocalcin in resorption lacunae.",
                0,
                "Both true and causally linked—osteoblast insulin drives resorption-dependent osteocalcin activation supporting glucose homeostasis.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "This work eventually led to the realization that insulin signaling in osteoblasts is necessary to maintain whole-body glucose homeostasis in animals fed normal chow.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "Assertion: Osteocalcin increases energy expenditure and its deficiency increases visceral fat.",
                "Reason: Osteocalcin's mechanism for increasing energy expenditure has been fully elucidated.",
                2,
                "Assertion true; reason false—the cellular/molecular mechanisms of osteocalcin on energy expenditure remain incompletely understood.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "Through cellular and molecular mechanisms that have still not been elucidated, osteocalcin is necessary and sufficient to increase energy expenditure (see Fig. 28.2).",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                "Assertion: Osteocalcin is necessary for optimum muscle function during exercise.",
                "Reason: During exercise, osteocalcin via GPRC6A in myofibers promotes glucose and fatty acid uptake and catabolism.",
                0,
                "Both true and causally linked—exercise-specific GPRC6A signaling in muscle mediates osteocalcin's ergogenic effects.",
                ref(
                    "Osteocalcin Regulation of Energy Metabolism and Male Fertility",
                    "analysis of mouse strains lacking osteocalcin signaling in myofibers revealed that osteocalcin is necessary for optimum muscle function during exercise.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Assertion: Osteocalcin prevents anxiety and promotes spatial learning.",
                "Reason: Osteocalcin cannot cross the blood-brain barrier.",
                3,
                "Assertion true; reason false—osteocalcin does cross the BBB and signals via brain receptors.",
                ref(
                    "Regulation of Whole-Organism Physiology by Bone-Derived Hormones",
                    "osteocalcin crosses the blood-brain barrier",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Assertion: Glutamate from stress-responsive amygdala neurons inhibits osteoblast γ-carboxylase.",
                "Reason: This leads to increased uncarboxylated osteocalcin that initiates the acute stress response.",
                0,
                "Both true and causally linked—glutamate via Glast inhibits carboxylation, releasing bioactive osteocalcin for stress signaling.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "Glutamate, intracellularly, acts as an allosteric inhibitor of  $ \\gamma $ carboxylase, the enzyme responsible for the carboxylation of osteocalcin.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Osteocalcin Regulation of Other Physiologic Functions",
                "Assertion: Embryonic osteocalcin is necessary for proper adrenal glucocorticoid and aldosterone biosynthesis.",
                "Reason: Embryonic osteocalcin upregulates SF1 in adrenal cortex.",
                0,
                "Both true and causally linked—SF1 is the master adrenal developmental transcription factor programmed by embryonic osteocalcin.",
                ref(
                    "Osteocalcin Regulation of Other Physiologic Functions",
                    "This set of functions of osteocalcin is achieved by embryo-derived osteocalcin, which upregulates the transcription factor SF1, a master gene of adrenal development.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Lipocalin-2: Another Bone-Derived Hormone",
                "Assertion: Bone-derived lipocalin-2 suppresses appetite via hypothalamic MC4R signaling.",
                "Reason: Lipocalin-2 and osteocalcin share identical endocrine target organs and functions.",
                1,
                "Both statements about LCN2 are true, but the reason is false—LCN2's anorexigenic MC4R function is distinct from osteocalcin's roles.",
                ref(
                    "Lipocalin-2: Another Bone-Derived Hormone",
                    "The functional characterization of bone-derived lipocalin-2 revealed that this hormone fulfills a function that osteocalcin does not have.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Perspectives",
                "Assertion: Osteocalcin and lipocalin-2 are promising therapeutic targets for obesity and age-related functional decline.",
                "Reason: Neither hormone's injection or cell treatment upregulates the processes identified in mouse genetics.",
                3,
                "Assertion true (supported by preclinical hope); reason false—primate/human cell studies do upregulate these regulated processes.",
                ref(
                    "Perspectives",
                    "The first and more practical one is that their injection in nonhuman primates or even treatment of human cells with osteocalcin and/or lipocalin-2 does upregulate the physiologic processes that mouse genetics showed are regulated by these two hormones.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "28",
        "title": "Endocrine Functions of Bone",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Gerard Karsenty",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_28_Endocrine_Functions_of_Bone.md",
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
