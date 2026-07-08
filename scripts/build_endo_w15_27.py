#!/usr/bin/env python3
"""Generate Williams 15e module w15-27 — Hormones and Disorders of Mineral Metabolism."""
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
OUT_NAME = "w15-27_Hormones_and_Disorders_of_Mineral_Metabolism.json"


def build() -> dict:
    p = "w15-27"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why calcium and phosphate homeostasis is hormone-driven",
                "Minute-to-minute stability of blood Ca and phosphate depends on interactive hormonal mechanisms—not passive equilibration—making PTH, active vitamin D, and FGF23 the clinical levers in mineral disorders.",
                ref(
                    "KEY POINTS",
                    "Interactive hormonal homeostatic mechanisms maintain the concentrations of calcium and phosphate in the blood within narrow limits.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How gut, kidney, and bone buffer mineral ions",
                "Physiologic challenges to Ca/P balance are met by coordinated changes in intestinal absorption, renal excretion, and skeletal buffering—not by any single organ in isolation.",
                ref(
                    "KEY POINTS",
                    "Adaptation of calcium and phosphate metabolism during physiologic challenges depends on alterations of absorption in the gut, excretion through the kidney, and buffering properties of bone.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why PHPT tops the hypercalcemia differential",
                "When PTH is inappropriately normal or elevated in hypercalcemia, think parathyroid disease first—primary hyperparathyroidism is the most common cause of hypercalcemia overall.",
                ref(
                    "KEY POINTS",
                    "Primary hyperparathyroidism is the most common cause of hypercalcemia.",
                ),
            ),
            note(
                f"{p}-n4",
                "KEY POINTS",
                "How to classify PTH-dependent vs PTH-independent hypercalcemia",
                "Measure intact PTH: suppressed PTH defines PTH-independent hypercalcemia (malignancy foremost); detectable or elevated PTH with hypercalcemia defines parathyroid-dependent disease.",
                ref(
                    "KEY POINTS",
                    "The most common cause of hypercalcemia that is not dependent on PTH is hypercalcemia of malignancy. Many other etiologies are included in this category of PTH-independent hypercalcemia, but they are uncommon.",
                ),
            ),
            note(
                f"{p}-n5",
                "Calcium",
                "Why ionized calcium—not total—is the physiologic signal",
                "Only the free ionized fraction enters cells and drives neuromuscular and enzymatic function; total Ca can mislead when albumin or pH shifts binding without changing ionized Ca.",
                ref(
                    "Calcium",
                    "The free or ionized fraction (45%) is the biologically functional component of total Ca, is tightly regulated by hormonal mechanisms, and can be measured clinically.",
                ),
            ),
            note(
                f"{p}-n6",
                "Calcium",
                "How to correct total calcium for albumin",
                "When albumin is high, subtract 0.8 mg/dL per 1.0 g/dL above 4 g/dL; when low, add 0.8 mg/dL per 1.0 g/dL below 4 g/dL—but measure ionized Ca when protein or pH is abnormal.",
                ref(
                    "Calcium",
                    "Such elevations in total Ca, when albumin levels are increased, can be “corrected” by subtracting 0.8 mg/dL from the total Ca for every 1.0 g/dL by which the serum albumin concentration is >4 g/dL. Conversely, when albumin levels are low, total Ca can be corrected by adding 0.8 mg/dL for every 1.0 g/dL by which the albumin is <4 g/dL.",
                ),
            ),
            note(
                f"{p}-n7",
                "Calcium",
                "Why the intracellular Ca gradient matters clinically",
                "A ~10,000:1 extracellular-to-intracellular free Ca gradient powers signaling; disruption of channel or pump function can produce profound cellular dysfunction beyond serum Ca alone.",
                ref(
                    "Calcium",
                    "A very large chemical gradient (i.e., 10,000:1), augmented by a large negative electrical potential, favors calcium entry into cells via calcium channels, where the intracellular free calcium concentrations are only approximately 100 nM.",
                ),
            ),
            note(
                f"{p}-n8",
                "Parathyroid Hormone Secretion",
                "How the CaSR sigmoid set-point governs PTH release",
                "PTH secretion follows an inverse sigmoid curve versus ionized Ca: the midpoint defines the set-point, and the steep lower limb ensures tight defense against hypocalcemia.",
                ref(
                    "Parathyroid Hormone Secretion",
                    "The physiologic relationship between extracellular calcium concentrations and PTH secretion is an inverse sigmoidal curve (Fig. 27.4). The level of calcium at the midpoint of this curve determines the set-point of serum calcium levels.",
                ),
            ),
            note(
                f"{p}-n9",
                "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                "Why PTH raises bone resorption via RANKL/OPG",
                "PTH on osteoblasts increases RANKL and decreases OPG, driving osteoclastogenesis and liberating skeletal Ca and phosphate into the circulation.",
                ref(
                    "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                    "Once PTH is secreted, the NH₂-terminal domain of the increased circulating PTH binds to the PTH/PTH-related protein (PTHrP) receptor (PTHR1), a G protein-coupled receptor (GPCR)⁷ in the osteoblasts of bone, increasing intracellular cyclic adenosine monophosphate (cAMP) production and thus enhancing the release of the tumor necrosis factor (TNF)-related cytokine receptor activator of nuclear factor κβ (RANKL) and decreasing the release of the RANKL antagonist osteoprotegerin (OPG).",
                ),
            ),
            note(
                f"{p}-n10",
                "Actions of Parathyroid Hormone on the Kidney",
                "How PTH conserves filtered calcium",
                "PTH enhances Ca reabsorption in the thick ascending limb and distal convoluted tubule while stimulating renal 1α-hydroxylase to produce active vitamin D.",
                ref(
                    "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                    "Increased PTH also augments calcium reabsorption in the kidney by its action in the distal renal tubule, including the cortical TAL of the loop of Henle and DCT.",
                ),
            ),
            note(
                f"{p}-n11",
                "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                "How FGF23 and Klotho regulate phosphate",
                "FGF23 binds FGFR1 with Klotho to inhibit proximal tubular NaPi-IIa/c, causing phosphaturia, and also suppresses renal 1α-hydroxylase—its phosphaturic effect exceeds that of PTH.",
                ref(
                    "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                    "FGF23 is a very potent regulator of PO₄ transport in the kidney, inhibiting the Na/P cotransporters, NaPT2a and NaPT2c, on the luminal surface of the proximal tubule cell and thus inhibiting PO₄ reabsorption and facilitating phosphaturia.",
                ),
            ),
            note(
                f"{p}-n12",
                "Actions of Vitamin D",
                "How 1,25(OH)₂D acts on gut, bone, and kidney",
                "Active vitamin D increases intestinal Ca absorption (transcellular and paracellular), modulates bone matrix and osteoclastogenesis via RANKL, and supports mineralization by optimizing the Ca-P microenvironment.",
                ref(
                    "Actions of Vitamin D",
                    "These observations indicate that the major role of vitamin D in bone is to provide the proper microenvironment for bone mineralization through stimulation of intestinal calcium and phosphate absorption.",
                ),
            ),
            note(
                f"{p}-n13",
                "Primary Hyperparathyroidism",
                "Why PHPT has three coexisting phenotypes today",
                "Classic symptomatic, asymptomatic hypercalcemic, and normocalcemic PHPT all persist in practice—screening patterns and vitamin D status determine which variant is seen.",
                ref(
                    "Primary Hyperparathyroidism",
                    "Not only do all three forms of PHPT coexist in the world today, but one might speculate also that these three forms have always been present.",
                ),
            ),
            note(
                f"{p}-n14",
                "Primary Hyperparathyroidism",
                "How adenoma differs from hyperplasia surgically",
                "A solitary adenoma is cured by removing one gland; hyperplasia requires multigland surgery—pathologic distinction is imperfect because clonal tumors can arise within hyperplastic glands.",
                ref(
                    "Primary Hyperparathyroidism",
                    "The distinction between adenoma and hyperplasia is clinically important because removal of the one abnormal gland can be expected to cure a parathyroid adenoma, whereas removal of multiple glands is required to successfully treat parathyroid hyperplasia.",
                ),
            ),
            note(
                f"{p}-n15",
                "Management of PHPT",
                "Why the 5th International Workshop guides parathyroidectomy",
                "Surgery is indicated for symptomatic PHPT and for asymptomatic disease meeting any of eight evidence-based criteria (calcium >1 mg/dL above ULN, T-score <−2.5, vertebral fracture, low creatinine clearance, hypercalciuria, stone risk, nephrolithiasis/nephrocalcinosis, age <50).",
                ref(
                    "Management of PHPT",
                    "The most recent guidelines recommend parathyroidectomy if any one of the following criteria is met and there are no medical contraindications: 1. Serum calcium >1.0 mg/dL above the upper normal limit",
                ),
            ),
            note(
                f"{p}-n16",
                "Surgical Treatment of PHPT",
                "How minimally invasive parathyroidectomy is validated",
                "Preoperative sestamibi/ultrasound/4D-CT plus intraoperative PTH fall ≥50% within ~10 minutes enables unilateral minimally invasive surgery with cure rates comparable to bilateral exploration in selected adenoma patients.",
                ref(
                    "Surgical Treatment of PHPT",
                    "Because the half-life of intact PTH in blood is very short (<2 minutes), a decline of 50% or more from baseline within 10 minutes or so, into the normal range, can signal successful removal of all hyperfunctioning parathyroid tissue.",
                ),
            ),
            note(
                f"{p}-n17",
                "Hypercalcemia of Malignancy",
                "Why PTHrP defines humoral hypercalcemia of malignancy",
                "PTHrP binds PTH1R, mimics PTH's amino-terminal actions, and is elevated in most solid tumors with humoral hypercalcemia—antibodies against PTHrP reverse hypercalcemia in animal models.",
                ref(
                    "Hypercalcemia of Malignancy",
                    "The evidence that PTHrP mediates the humoral hypercalcemia of malignancy in most patients is substantial. As noted previously, PTHrP binds to the PTH1R and mimics all of the actions of amino-terminal fragments of PTH.",
                ),
            ),
            note(
                f"{p}-n18",
                "Management of Severe Hypercalcemia",
                "How to treat acute severe hypercalcemia",
                "Rehydrate with isotonic saline (2–4 L/day), give IV bisphosphonate or denosumab for antiresorptive effect, and use calcitonin early for rapid but transient lowering; glucocorticoids help vitamin D–mediated hypercalcemia.",
                ref(
                    "Management of Severe Hypercalcemia",
                    "Treatment most often entails rehydration and administration of a bisphosphonate intravenously. Calcitonin can be useful as a temporary measure early in therapy, and glucocorticoids or dialysis may be indicated in some patients.",
                ),
            ),
            note(
                f"{p}-n19",
                "Familial Hypocalciuric Hypercalcemia",
                "Why FHH must not be mistaken for PHPT preoperatively",
                "FHH from CaSR loss-of-function causes hypocalciuria and mild hypercalcemia; parathyroidectomy fails to cure and can render the patient hypoparathyroid—genetic testing and family history are critical.",
                ref(
                    "Familial Hypocalciuric Hypercalcemia",
                    "The distinction between FHH and PHPT is a crucial one, however. Young patients with PHPT are usually treated surgically and cured. In contrast, hypercalcemia always occurs after surgery for FHH, unless the patient is rendered hypoparathyroid. Therefore, surgery is contraindicated as therapy for FHH, except in the very rare patient with severe, symptomatic hypercalcemia.",
                ),
            ),
            note(
                f"{p}-n20",
                "Hypoparathyroidism",
                "How postsurgical hypoparathyroidism presents",
                "Loss of PTH causes hypocalcemia, hyperphosphatemia, low 1,25(OH)₂D, and often hypercalciuria; Chvostek and Trousseau signs reflect neuromuscular irritability, with Trousseau being more specific.",
                ref(
                    "Hypoparathyroidism",
                    "In hypoparathyroidism, the serum calcium is low because the actions of PTH to resorb bone and conserve renal calcium are lost. Hypercalciuria can be a major issue in hypoparathyroidism, particularly in those who require large amounts of supplemental calcium to manage their hypocalcemia.",
                ),
            ),
            note(
                f"{p}-n21",
                "Genetic Parathyroid Disorders",
                "Why ADH1 therapy targets symptoms—not normocalcemia",
                "Activating CaSR mutations cause hypocalcemia with exaggerated hypercalciuria when treated with calcium and calcitriol; thiazides reduce urinary Ca loss while therapy aims to relieve symptoms rather than normalize Ca.",
                ref(
                    "Genetic Parathyroid Disorders",
                    "Treatment with calcium and vitamin D metabolites should be accompanied by the use of thiazide diuretics to decrease urinary calcium excretion, as well as ensuring adequate urinary volume to decrease urinary calcium concentration.",
                ),
            ),
            note(
                f"{p}-n22",
                "Vitamin D Deficiency",
                "How vitamin D deficiency produces hypocalcemia",
                "Impaired gut Ca absorption causes hypocalcemia with hypophosphatemia and secondary hyperPTH; mild deficiency may paradoxically show normal or high 1,25(OH)₂D because PTH stimulates renal 1α-hydroxylase.",
                ref(
                    "Vitamin D Deficiency",
                    "The primary cause of hypocalcemia in vitamin D deficiency is decreased intestinal absorption of calcium. In the setting of normal renal function, the hypocalcemia of vitamin D deficiency, unlike that of hypoparathyroidism, is accompanied by hypophosphatemia and increased renal phosphate clearance.",
                ),
            ),
            note(
                f"{p}-n23",
                "Hypophosphatemia",
                "Why refeeding risks severe hypophosphatemia",
                "Starvation mobilizes phosphate from tissues; abrupt refeeding with insulin and cellular uptake can precipitate profound hypophosphatemia especially when underlying depletion exists.",
                ref(
                    "Hypophosphatemia",
                    "Starvation does induce phosphate deficiency and therefore predisposes to subsequent hypophosphatemia upon refeeding.",
                ),
            ),
            note(
                f"{p}-n24",
                "Hypophosphatemia",
                "How FGF23 syndromes (XLH, TIO) waste phosphate",
                "Elevated FGF23 reduces renal phosphate reabsorption and suppresses 1,25(OH)₂D, producing hypophosphatemia with rickets/osteomalacia; TIO resolves after tumor resection when FGF23 normalizes.",
                ref(
                    "Hypophosphatemia",
                    "The elevated serum levels of FGF23 in patients with TIO have been shown to normalize after removal of the tumor, correlating with resolution of the hypophosphatemia that characterizes this disorder.",
                ),
            ),
            note(
                f"{p}-n25",
                "Hyperphosphatemia",
                "Why tumor lysis causes dangerous hyperphosphatemia",
                "Rapid cytolytic release of intracellular phosphate can raise serum phosphate above 20 mg/dL, precipitating hypocalcemia and soft-tissue calcification—hemodialysis is often required early.",
                ref(
                    "Hyperphosphatemia",
                    "Hyperphosphatemia due to cytolytic release of intracellular phosphate can be quite dramatic, with serum phosphate concentrations up to or exceeding 20 mg/dL. This disorder was described initially as a complication of rapid induction chemotherapy for certain hematologic malignancies (tumor lysis syndrome)",
                ),
            ),
            note(
                f"{p}-n26",
                "Consequences of Hypomagnesemia",
                "How hypomagnesemia mimics hypoparathyroidism",
                "Low Mg impairs PTH secretion and causes target-organ resistance to PTH and blunts vitamin D activation—hypocalcemia will not correct until magnesium is repleted.",
                ref(
                    "Consequences of Hypomagnesemia",
                    "Inappropriately normal or low serum PTH, despite hypocalcemia, is common and indicates a defect in PTH secretion, which is due to augmented signaling by CaSR-associated G proteins, normally inhibited by magnesium, within the parathyroid cell.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Calcium",
                "A 68-year-old man is admitted with confusion. Total serum calcium is 7.8 mg/dL (8.5–10.5), albumin 1.8 g/dL, pH 7.48. He has perioral tingling and a positive Trousseau sign. Which next step best determines whether true hypocalcemia is present?",
                [
                    "Repeat total calcium in 1 week",
                    "Measure ionized calcium",
                    "Start empiric IV calcium without labs",
                    "Order serum magnesium only",
                ],
                1,
                "Alkalosis and hypoalbuminemia alter total Ca without reflecting ionized Ca; neuromuscular signs warrant direct ionized measurement.",
                ref(
                    "Calcium",
                    "Consequently, a major shift in serum protein or pH requires direct measurement of the ionized Ca level to determine the physiologic serum calcium level.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Parathyroid Hormone",
                "A woman with recurrent kidney stones has serum Ca 11.2 mg/dL, PTH 92 pg/mL (upper normal ~65), and 24-hour urine Ca 320 mg. Phosphorus is 2.4 mg/dL. Which diagnosis is most likely?",
                [
                    "Humoral hypercalcemia of malignancy",
                    "Primary hyperparathyroidism",
                    "Vitamin D intoxication",
                    "Familial hypocalciuric hypercalcemia",
                ],
                1,
                "Hypercalcemia with inappropriately normal/elevated PTH, phosphaturia, and hypercalciuria is classic PHPT—the most common cause of hypercalcemia.",
                ref(
                    "Primary Hyperparathyroidism",
                    "In PHPT, the excessive secretion of PTH leads to actions on PTH's two major target organs: bone and kidney.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Hypercalcemic Disorders",
                "A 72-year-old man with metastatic squamous cell lung cancer has Ca 13.8 mg/dL, PTH <5 pg/mL, phosphorus 2.1 mg/dL, and elevated PTHrP. What is the best initial management?",
                [
                    "Urgent parathyroidectomy",
                    "Isotonic saline rehydration followed by IV bisphosphonate",
                    "High-dose oral vitamin D",
                    "Thiazide diuretic for calciuria",
                ],
                1,
                "PTH-independent malignancy hypercalcemia is treated with volume repletion and IV bisphosphonate or denosumab; PTH is suppressed.",
                ref(
                    "Hypercalcemia of Malignancy",
                    "Treatment consists of restoration of volume, followed by intravenous bisphosphonate or denosumab (see \"Management of Severe Hypercalcemia\").",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Familial Hypocalciuric Hypercalcemia",
                "A 28-year-old man has lifelong mild hypercalcemia (10.8–11.2 mg/dL), PTH mid-normal, and calcium clearance/creatinine clearance ratio 0.006. His father had hypercalcemia since childhood. Before neck exploration, what is the most appropriate step?",
                [
                    "Proceed to parathyroidectomy",
                    "Confirm FHH with CaSR genetic testing and avoid surgery",
                    "Start cinacalcet as definitive cure",
                    "Treat as vitamin D deficiency with high-dose ergocalciferol",
                ],
                1,
                "Low urinary Ca/Cr clearance ratio and familial neonatal hypercalcemia suggest FHH; surgery is contraindicated because hypercalcemia recurs unless hypoparathyroid.",
                ref(
                    "Familial Hypocalciuric Hypercalcemia",
                    "Therefore, surgery is contraindicated as therapy for FHH, except in the very rare patient with severe, symptomatic hypercalcemia.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Management of PHPT",
                "A 45-year-old woman with asymptomatic PHPT has adjusted Ca 11.4 mg/dL (ULN 10.2), DXA T-score −2.8 at distal radius, and eGFR 72 mL/min. She is otherwise healthy. What is the best management?",
                [
                    "Observation with annual calcium only",
                    "Parathyroidectomy",
                    "Cinacalcet as first-line for mild hypercalcemia",
                    "Restrict dietary calcium to <500 mg/day",
                ],
                1,
                "Calcium >1 mg/dL above ULN and T-score <−2.5 at any site are parathyroidectomy indications per 5th International Workshop guidelines.",
                ref(
                    "Management of PHPT",
                    "1. Serum calcium >1.0 mg/dL above the upper normal limit",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Surgical Treatment of PHPT",
                "A 52-year-old with sporadic PHPT has a concordant sestamibi and neck ultrasound localizing a single adenoma. Intraoperative PTH falls 65% at 8 minutes. What is the most appropriate conclusion?",
                [
                    "Continue bilateral neck exploration because MEN1 is likely",
                    "Successful excision of hyperfunctioning tissue; minimally invasive approach appropriate",
                    "Failure of surgery; immediate sternotomy required",
                    "Defer conclusion until 24-hour urine calcium returns",
                ],
                1,
                "A ≥50% intraoperative PTH decline within ~10 minutes indicates successful removal in minimally invasive surgery.",
                ref(
                    "Surgical Treatment of PHPT",
                    "a decline of 50% or more from baseline within 10 minutes or so, into the normal range, can signal successful removal of all hyperfunctioning parathyroid tissue.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Hypoparathyroidism",
                "Two weeks after total thyroidectomy, a patient has Ca 7.0 mg/dL, phosphorus 6.2 mg/dL, PTH undetectable, and 24-hour urine Ca 380 mg despite hypocalcemia. What complication must be anticipated during treatment?",
                [
                    "Hypophosphatemia from calcitriol",
                    "Nephrolithiasis/nephrocalcinosis from hypercalciuria during repletion",
                    "Hungry bone hyperphosphatemia",
                    "Primary hyperparathyroidism recurrence",
                ],
                1,
                "Hypoparathyroidism commonly causes hypercalciuria even when serum Ca is low; aggressive oral Ca and calcitriol risk renal calcifications.",
                ref(
                    "Hypoparathyroidism",
                    "Hypercalciuria can be a major issue in hypoparathyroidism, particularly in those who require large amounts of supplemental calcium to manage their hypocalcemia.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Clinical Presentation",
                "A patient with chronic hypocalcemia has perioral numbness. Chvostek sign is positive but Trousseau sign is negative. Which statement is most accurate?",
                [
                    "Hypocalcemia is excluded",
                    "Chvostek is nonspecific and can be positive in normal individuals; Trousseau is more specific",
                    "Trousseau is always positive when Ca <8 mg/dL",
                    "Both signs are pathognomonic for hypoparathyroidism",
                ],
                1,
                "Chvostek can be seen in up to 10% of normals; Trousseau is more specific, yet significant hypocalcemia can occur with negative signs.",
                ref(
                    "Clinical Presentation",
                    "The Chvostek sign is not a specific sign of hypocalcemia or latent tetany because it can be seen in up to 10% of completely normal individuals. The Trousseau sign is a much more specific sign.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Vitamin D Deficiency",
                "A vegan with limited sun exposure has Ca 8.0 mg/dL, phosphorus 2.0 mg/dL, PTH 110 pg/mL, and 25(OH)D 12 ng/mL. 1,25(OH)₂D is 45 pg/mL (normal). What explains the normal active vitamin D?",
                [
                    "Assay error only—1,25(OH)₂D must be low",
                    "Secondary hyperPTH stimulating renal 1α-hydroxylase in mild-moderate deficiency",
                    "Primary hyperparathyroidism unrelated to vitamin D",
                    "Excess FGF23 from tumor",
                ],
                1,
                "In mild/moderate vitamin D deficiency, compensatory hyperPTH can maintain or elevate 1,25(OH)₂D despite low 25(OH)D.",
                ref(
                    "Vitamin D Deficiency",
                    "In profound vitamin D deficiency, the level of 1,25(OH)₂D₃ is usually low, but in mild or moderate vitamin D deficiency, the renal 1α-hydroxylase is stimulated by PTH and the hypocalcemia, resulting in a normal or even elevated 1,25(OH)₂D₃ level.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Hypophosphatemia",
                "A malnourished patient is started on TPN after prolonged starvation. On day 2, phosphorus is 1.0 mg/dL with weakness. What mechanism best explains this?",
                [
                    "Primary hyperparathyroidism",
                    "Shift of extracellular phosphate into cells during refeeding with underlying depletion",
                    "Excess FGF23 from XLH",
                    "Renal Fanconi syndrome",
                ],
                1,
                "Starvation induces phosphate deficiency; refeeding with insulin drives intracellular phosphate uptake and acute hypophosphatemia.",
                ref(
                    "Hypophosphatemia",
                    "Rapid egress of extracellular phosphate into cells is the cause of hypophosphatemia that develops acutely during administration of intravenous glucose, insulin therapy for hyperglycemia",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Hypophosphatemia",
                "A 40-year-old with bone pain and fractures has phosphorus 1.8 mg/dL, normal Ca, low 1,25(OH)₂D, and elevated intact FGF23. After resection of a small mesenchymal thigh mass, labs normalize. Diagnosis?",
                [
                    "Primary hyperparathyroidism",
                    "Tumor-induced osteomalacia",
                    "Vitamin D intoxication",
                    "Familial tumoral calcinosis",
                ],
                1,
                "TIO features FGF23-secreting mesenchymal tumors; hypophosphatemia and low 1,25(OH)₂D resolve after tumor removal.",
                ref(
                    "Hypophosphatemia",
                    "TIO is a rare syndrome in which typically benign tumors of mesenchymal origin secrete FGF23 or, rarely, another phosphatonin.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Hyperphosphatemia",
                "A patient with AML begins induction chemotherapy and develops Ca 6.5 mg/dL, phosphorus 18 mg/dL, and acute kidney injury. Best immediate therapy?",
                [
                    "Oral phosphate binders alone",
                    "Early hemodialysis consideration with volume expansion",
                    "IV calcium gluconate without monitoring phosphate",
                    "High-dose vitamin D repletion",
                ],
                1,
                "Tumor lysis causes severe hyperphosphatemia with hypocalcemia; hemodialysis is most effective and should be considered early when symptomatic.",
                ref(
                    "Hyperphosphatemia",
                    "Hemodialysis is the most effective approach and should be considered early in severe hyperphosphatemia, especially in the tumor lysis syndrome",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Consequences of Hypomagnesemia",
                "A chronic alcoholic has Ca 7.5 mg/dL, Mg 0.9 mg/dL, and PTH 18 pg/mL (inappropriately low). IV calcium fails to correct hypocalcemia. Next best step?",
                [
                    "Increase IV calcium infusion rate alone",
                    "IV magnesium repletion before expecting PTH response",
                    "Emergency parathyroidectomy",
                    "Start loop diuretic for calciuria",
                ],
                1,
                "Profound hypomagnesemia impairs PTH secretion and action; magnesium must be repleted to correct hypocalcemia.",
                ref(
                    "Consequences of Hypomagnesemia",
                    "Sustained correction of hypocalcemia or hypokalemia cannot be achieved by administration of calcium or potassium alone, respectively, whereas both abnormalities respond to administration of magnesium.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Hypomagnesemia",
                "A hypertensive patient on long-term furosemide has Mg 1.2 mg/dL, hypokalemia refractory to potassium, and muscle cramps. Which mechanism contributes most?",
                [
                    "Increased intestinal Mg absorption",
                    "Loop diuretic-induced renal tubular Mg wasting",
                    "Primary hyperparathyroidism",
                    "Excess PTH from vitamin D toxicity",
                ],
                1,
                "Loop diuretics are a common cause of acquired renal Mg wasting and hypomagnesemia.",
                ref(
                    "Hypomagnesemia",
                    "These drugs include diuretics (especially loop diuretics), digoxin, cisplatin, cetuximab, pentamidine, cyclosporine, tacrolimus",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                "A patient with CKD has elevated FGF23, low 1,25(OH)₂D, and high PTH. Why does FGF23 not suppress PTH as expected?",
                [
                    "FGF23 never affects parathyroid cells",
                    "Downregulation of parathyroid FGFR1 and Klotho in renal failure",
                    "Excess calcitonin blocks FGF23",
                    "PTH gene is mutated in all CKD patients",
                ],
                1,
                "In renal failure both FGF23 and PTH rise; reduced parathyroid FGFR1/Klotho expression may explain impaired FGF23 suppression of PTH.",
                ref(
                    "Regulation of the Parathyroid Hormone Gene",
                    "In renal failure, both FGF23 levels and PTH levels are elevated. This paradoxical observation (given the role of FGF23 in suppressing PTH secretion) may be explained by the downregulation of parathyroid cell FGF receptor 1 and Klotho in renal failure.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Primary Hyperparathyroidism",
                "A 35-year-old has normal total and ionized calcium on three occasions but PTH persistently 95–110 pg/mL after excluding low 25(OH)D, CKD, and malabsorption. BMD is low. Most likely diagnosis?",
                [
                    "Secondary hyperparathyroidism from vitamin D deficiency",
                    "Normocalcemic primary hyperparathyroidism",
                    "Familial hypocalciuric hypercalcemia",
                    "Lithium-induced hypercalcemia",
                ],
                1,
                "NPHPT requires consistently normal Ca with elevated PTH after excluding secondary causes; skeletal involvement can mirror hypercalcemic PHPT.",
                ref(
                    "Primary Hyperparathyroidism",
                    "Normocalcemic hyperparathyroidism (NPHPT) is characterized by persistently normal albumin-adjusted total calcium and normal ionized serum calcium levels, on at least two consecutive measurements at least a week apart over a 3- to 6-month-period, along with consistently elevated levels of PTH.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Management of Severe Hypercalcemia",
                "A patient with myeloma and Ca 15 mg/dL is volume-repleted but still symptomatic. Renal function is moderate (GFR 35). Best antiresorptive choice?",
                [
                    "Oral phosphate repletion",
                    "IV zoledronate at reduced dose/rate or denosumab if bisphosphonate contraindicated",
                    "Prolonged furosemide calciuresis without antiresorptive",
                    "High-dose oral vitamin D",
                ],
                1,
                "IV bisphosphonates are first-line; dose/rate reduction is used with moderate renal insufficiency, and denosumab is an alternative though hypocalcemia risk is higher.",
                ref(
                    "Denosumab",
                    "Denosumab offers an alternative to intravenous bisphosphonates in patients with renal failure, but denosumab carries a greater risk of hypocalcemia.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Hyperphosphatemia",
                "A patient with ESRD on hemodialysis has phosphorus 7.5 mg/dL despite binders. PTH is low. Which additional factor commonly contributes in hypoparathyroidism?",
                [
                    "Excess FGF23 phosphaturia",
                    "Loss of PTH-mediated inhibition of proximal phosphate reabsorption",
                    "Primary intestinal phosphate malabsorption",
                    "Vitamin D intoxication with suppressed PTH",
                ],
                1,
                "Without PTH's phosphaturic action, serum phosphate can rise to 6–8 mg/dL in hypoparathyroidism despite some counter-regulation by FGF23.",
                ref(
                    "Hyperphosphatemia",
                    "In hypoparathyroidism (or PHP), serum phosphate may rise to levels as high as 6 to 8 mg/dL because of loss of the tonic inhibitory effect of PTH on phosphate reabsorption",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Parathyroid Hormone Secretion",
                "A patient has activating CaSR mutation with symptomatic hypocalcemia and nephrolithiasis on calcitriol therapy. Which adjunct best limits renal calcium loss?",
                [
                    "Loop diuretic",
                    "Thiazide diuretic",
                    "Denosumab",
                    "High-dose phosphate supplement",
                ],
                1,
                "ADH1 management pairs calcium/vitamin D with thiazides to reduce hypercalciuria and protect kidneys.",
                ref(
                    "Genetic Parathyroid Disorders",
                    "Treatment with calcium and vitamin D metabolites should be accompanied by the use of thiazide diuretics to decrease urinary calcium excretion",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Vitamin D Metabolism",
                "A sarcoidosis patient develops hypercalcemia with suppressed PTH and elevated 1,25(OH)₂D. Best initial treatment?",
                [
                    "Parathyroidectomy",
                    "Glucocorticoids",
                    "IV bisphosphonate only without addressing vitamin D",
                    "High-dose cholecalciferol",
                ],
                1,
                "Granulomatous 1,25(OH)₂D overproduction causes PTH-suppressed hypercalcemia; glucocorticoids lower 1,25(OH)₂D.",
                ref(
                    "Sarcoidosis and Other Granulomatous Diseases",
                    "Furthermore, the hypercalcemia and high levels of 1,25(OH)₂D₃ fall upon treatment with glucocorticoids.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Primary Hyperparathyroidism",
                "After parathyroidectomy for large adenoma and severe PHPT, a patient develops Ca 7.2 mg/dL, phosphorus 1.8 mg/dL, and low urine calcium. Most likely syndrome?",
                [
                    "Hungry bone syndrome",
                    "Persistent primary hyperparathyroidism",
                    "Humoral hypercalcemia of malignancy",
                    "Vitamin D intoxication",
                ],
                0,
                "Postoperative hypocalcemia with hypophosphatemia and hypocalciuria reflects avid skeletal remineralization (hungry bone), especially after severe PHPT.",
                ref(
                    "Other Causes of Hypocalcemia",
                    "Hungry bone syndrome presents as prolonged hypocalcemia, hypocalciuria, and hypophosphatemia after parathyroidectomy for primary hyperparathyroidism",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Laboratory Assessment of Mineral Metabolism",
                "A clinician orders 1,25(OH)₂D to screen for vitamin D deficiency in an otherwise healthy adult. Appropriate response?",
                [
                    "1,25(OH)₂D is the best screening test for deficiency",
                    "Measure 25(OH)D instead; 1,25(OH)₂D is not indicated for assessing vitamin D status",
                    "Both must be low to diagnose deficiency",
                    "1,25(OH)₂D is always elevated in deficiency",
                ],
                1,
                "25(OH)D reflects substrate supply; 1,25(OH)₂D is tightly regulated and reserved for suspected disorders of activation.",
                ref(
                    "Laboratory Assessment of Mineral Metabolism",
                    "Importantly, measurement of 1,25(OH)₂D₃ is not indicated to assess vitamin D status and indeed should be reserved for individuals in which excessive or impaired 1α-hydroxylation is suspect.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Hypercalcemic Disorders",
                "In evaluating hypercalcemia, PTH is 55 pg/mL (normal range) with Ca 11.0 mg/dL. What does this pattern indicate?",
                [
                    "PTH-independent hypercalcemia",
                    "PTH-dependent (parathyroid) hypercalcemia",
                    "Normal physiology—no further workup",
                    "Pseudohypoparathyroidism",
                ],
                1,
                "PTH should be suppressed in nonparathyroid hypercalcemia; normal-range PTH with hypercalcemia indicates inappropriate parathyroid function.",
                ref(
                    "Parathyroid-Dependent Hypercalcemia",
                    "If the PTH level is elevated or detectable within the normal range, the hypercalcemia is due to abnormal parathyroid gland function.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Nonsurgical Management of PHPT",
                "A patient with severe PHPT cannot undergo surgery. Cinacalcet is started. Which outcome should NOT be expected?",
                [
                    "Reduction in serum calcium",
                    "Long-term normocalcemia in many patients",
                    "Improved BMD and reduced urinary calcium",
                    "FDA-approved option for severe hypercalcemia when surgery not possible",
                ],
                2,
                "Cinacalcet lowers calcium but neither BMD nor urinary calcium improves, and nephrolithiasis benefit is unproven.",
                ref(
                    "Nonsurgical Management of PHPT",
                    "Neither BMD nor urinary calcium excretion improves with treatment. Further, there are no data regarding nephrolithiasis risk reduction.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Hypomagnesemia",
                "A patient on cisplatin develops persistent hypomagnesemia months after chemotherapy. Urinary Mg is >1 mEq/day while serum Mg is low. Mechanism?",
                [
                    "Dietary Mg excess",
                    "Cisplatin-induced isolated renal tubular Mg wasting",
                    "Primary intestinal hyperabsorption of Mg",
                    "Excess PTH-driven Mg retention",
                ],
                1,
                "Cisplatin commonly causes renal Mg wasting that may persist long after treatment.",
                ref(
                    "Hypomagnesemia",
                    "In over half of patients treated with cisplatin, hypomagnesemia occurs within days or weeks, and roughly half of those who develop it exhibit persistent hypomagnesemia many months or even years later.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Hyperphosphatemia",
                "A child with periarticular calcifications, hyperphosphatemia, and low intact FGF23 but high C-terminal FGF23 fragments is evaluated. Likely diagnosis?",
                [
                    "Tumor-induced osteomalacia",
                    "Familial tumoral calcinosis from impaired FGF23 bioactivity",
                    "Primary hyperparathyroidism",
                    "Vitamin D deficiency",
                ],
                1,
                "Tumoral calcinosis results from impaired active FGF23 (mutations in FGF23, GALNT3, or Klotho) with low intact hormone and high inactive fragments.",
                ref(
                    "Hyperphosphatemia",
                    "Familial tumoral calcinosis can result from inactivating mutations in either FGF23, the O-linked glycosyl transferase GalNAc-T3, or the FGF23 coreceptor α-Klotho.",
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
                "Hypoparathyroidism is a common cause of hypocalcemia characterized by low PTH.",
                False,
                "Hypoparathyroidism is rare, not common—though it is defined by hypocalcemia with inadequate or undetectable PTH.",
                ref(
                    "KEY POINTS",
                    "Hypoparathyroidism is a rare disorder characterized by hypocalcemia and an inadequate or undetectable concentration of parathyroid hormone.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Calcium",
                "Dehydration during venipuncture can falsely elevate total serum calcium by raising albumin concentration.",
                True,
                "Hemoconcentration increases albumin and can falsely raise total Ca while ionized Ca may be stable.",
                ref(
                    "Calcium",
                    "Dehydration or hemoconcentration during venipuncture may elevate serum albumin and falsely elevate total serum Ca.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Parathyroid Hormone Secretion",
                "Inactivating CaSR mutations cause familial hypocalciuric hypercalcemia.",
                True,
                "Loss-of-function CaSR mutations shift the set-point rightward, causing hypercalcemia with hypocalciuria (FHH).",
                ref(
                    "Parathyroid Hormone Secretion",
                    "Inactivating mutations cause familial hypocalciuric hypercalcemia (FHH), a disease of defective calcium sensing, whereas activating mutations cause autosomal-dominant hypocalcemia type 1.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                "FGF23 stimulates renal 1α-hydroxylase activity.",
                False,
                "FGF23 inhibits renal 1α,25(OH)₂D synthesis, unlike PTH which stimulates it.",
                ref(
                    "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                    "However, in contrast to PTH, FGF23 inhibits renal 1α,25(OH)₂D synthesis.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Primary Hyperparathyroidism",
                "A single benign parathyroid adenoma accounts for most PHPT cases.",
                True,
                "Sporadic adenoma is found in 75%–80% of PHPT; hyperplasia ~20%.",
                ref(
                    "Primary Hyperparathyroidism",
                    "In PHPT, a single benign adenoma is seen most often (75%–80%), but four-gland parathyroid hyperplasia can be seen in about 20% of patients.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Parathyroid-Independent Hypercalcemia",
                "In PTH-independent hypercalcemia, intact PTH is typically suppressed below 25 pg/mL.",
                True,
                "Appropriate parathyroid suppression defines PTH-independent hypercalcemia; levels are usually low or undetectable.",
                ref(
                    "Parathyroid-Independent Hypercalcemia",
                    "In parathyroid-independent hypercalcemia, PTH secretion is appropriately suppressed. PTH levels, measured using two-site assays, are invariably lower than 25 pg/mL and are usually lower than normal or undetectable.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Management of Severe Hypercalcemia",
                "Loop diuretics are recommended as first-line therapy to promote calciuresis in severe hypercalcemia.",
                False,
                "Saline rehydration and bisphosphonates/denosumab are preferred; loop diuretics risk volume depletion and are best avoided.",
                ref(
                    "Volume Repletion",
                    "In light of the availability of highly effective alternatives for the therapy of hypercalcemia, such drugs are probably best avoided, except in circumstances in which vigorous rehydration fails to improve severe hypercalcemia",
                ),
            ),
            tf(
                f"{p}-t8",
                "Etiologies of Hypoparathyroidism",
                "Postsurgical hypoparathyroidism is the most common cause of chronic hypocalcemia.",
                True,
                "Neck surgery—thyroidectomy, parathyroid surgery, radical dissection—is the leading cause of chronic hypoparathyroidism.",
                ref(
                    "Etiologies of Hypoparathyroidism",
                    "The most common cause of chronic hypocalcemia is postsurgical hypoparathyroidism.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Vitamin D Deficiency",
                "Vitamin D deficiency hypocalcemia is typically accompanied by hyperphosphatemia like hypoparathyroidism.",
                False,
                "Vitamin D deficiency causes hypophosphatemia with secondary hyperPTH, unlike hypoparathyroidism's hyperphosphatemia.",
                ref(
                    "Vitamin D Deficiency",
                    "In the setting of normal renal function, the hypocalcemia of vitamin D deficiency, unlike that of hypoparathyroidism, is accompanied by hypophosphatemia and increased renal phosphate clearance.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Hyperphosphatemia",
                "The most common cause of hyperphosphatemia is acute or chronic renal failure.",
                True,
                "Reduced GFR limits phosphate excretion despite maximal inhibition of proximal reabsorption.",
                ref(
                    "Hyperphosphatemia",
                    "The most common cause of hyperphosphatemia is acute or chronic renal failure in which GFR is so reduced that the daily load of phosphate cannot be excreted to maintain a normal level of serum phosphate",
                ),
            ),
            tf(
                f"{p}-t11",
                "Hypophosphatemia",
                "Rapid IV magnesium repletion in severe hypomagnesemia can provoke hypophosphatemia via stimulated PTH secretion.",
                True,
                "Correcting Mg rapidly can trigger phosphaturia and hypophosphatemia, especially with underlying phosphate depletion.",
                ref(
                    "Hypophosphatemia",
                    "When PTH secretion is compromised by severe hypomagnesemia, rapid intravenous administration of magnesium alone, without concurrent attention to coexisting hypocalcemia, can provoke massive phosphaturia and hypophosphatemia in patients with underlying phosphate depletion.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Consequences of Hypomagnesemia",
                "Hypomagnesemia can cause functional hypoparathyroidism reversible with magnesium repletion.",
                True,
                "Low Mg impairs PTH secretion and target organ responsiveness; both correct with repletion.",
                ref(
                    "Impaired PTH Secretion",
                    "Impaired secretion of PTH from the parathyroid glands by profound hypomagnesemia can lead to functional hypoparathyroidism and target organ resistance to PTH. Both of these abnormalities are reversible with magnesium repletion.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Consequences of Hypomagnesemia",
                "Vitamin D 1,25(OH)₂D therapy should be first-line to correct hypomagnesemic hypocalcemia.",
                False,
                "Mg repletion corrects hypocalcemia before 1,25(OH)₂D rises; active vitamin D can worsen hypomagnesemia by suppressing PTH.",
                ref(
                    "Therapy of Hypomagnesemia",
                    "Use of 1,25(OH)₂D is not necessary, does not hasten recovery, and may actually worsen hypomagnesemia by suppressing PTH secretion and thereby promoting renal magnesium excretion.",
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
                "Assertion: Primary hyperparathyroidism is the most common cause of hypercalcemia.",
                "Reason: Hypercalcemia of malignancy is PTH-dependent hypercalcemia.",
                2,
                "Assertion true; reason false—malignancy hypercalcemia is PTH-independent.",
                ref(
                    "KEY POINTS",
                    "The most common cause of hypercalcemia that is not dependent on PTH is hypercalcemia of malignancy.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Calcium",
                "Assertion: Ionized calcium is the biologically functional fraction of serum calcium.",
                "Reason: Most clinical laboratories report ionized calcium as the default serum calcium result.",
                2,
                "Assertion true; reason false—most labs report total calcium, not ionized.",
                ref(
                    "Calcium",
                    "Although only the ionized Ca is available to enter cells and activate cellular processes, most clinical laboratories report total serum Ca concentrations.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Parathyroid Hormone Secretion",
                "Assertion: The parathyroid CaSR relationship to PTH is an inverse sigmoidal curve.",
                "Reason: The system responds more dramatically to hypercalcemia than to hypocalcemia.",
                2,
                "Assertion true; reason false—steady-state values lie on the lower limb, favoring response to hypocalcemia.",
                ref(
                    "Parathyroid Hormone Secretion",
                    "Because values from normal persons in the steady state are located in the lower portion of the sigmoid curve, the system seems designed to respond more dramatically to hypocalcemia than to hypercalcemia.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                "Assertion: PTH promotes renal phosphate wasting by inhibiting NaPi-IIa/c.",
                "Reason: FGF23 and PTH both increase renal 1α-hydroxylase activity.",
                2,
                "Assertion true; reason false—FGF23 inhibits 1α-hydroxylase, unlike PTH.",
                ref(
                    "Hormonal Regulation of Calcium and Phosphate Homeostasis",
                    "PTH also decreases renal proximal tubule PO₄ reabsorption by inhibiting the NaPT2a and NaPT2c cotransporters and promoting renal PO₄ wasting. However, in contrast to PTH, FGF23 inhibits renal 1α,25(OH)₂D synthesis.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Actions of Vitamin D",
                "Assertion: 1,25(OH)₂D is required for efficient transcellular intestinal calcium absorption.",
                "Reason: The transcellular pathway is independent of vitamin D.",
                2,
                "Assertion true; reason false—the saturable transcellular pathway depends on 1,25(OH)₂D.",
                ref(
                    "Actions of Vitamin D",
                    "The transcellular pathway is dependent on 1,25(OH)₂D₃.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Primary Hyperparathyroidism",
                "Assertion: Normocalcemic PHPT is defined by normal calcium with persistently elevated PTH after excluding secondary causes.",
                "Reason: Normocalcemic PHPT always presents with hypercalciuria and nephrolithiasis.",
                2,
                "Assertion true; reason false—stone data in NPHPT are inconclusive.",
                ref(
                    "Primary Hyperparathyroidism",
                    "Normocalcemic hyperparathyroidism (NPHPT) is characterized by persistently normal albumin-adjusted total calcium and normal ionized serum calcium levels, on at least two consecutive measurements at least a week apart over a 3- to 6-month-period, along with consistently elevated levels of PTH.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Hypercalcemia of Malignancy",
                "Assertion: PTHrP mediates humoral hypercalcemia of malignancy in most affected patients.",
                "Reason: PTHrP always raises circulating 1,25(OH)₂D in these patients.",
                2,
                "Assertion true; reason false—patients with humoral hypercalcemia usually have low 1,25(OH)₂D despite PTHrP.",
                ref(
                    "Hypercalcemia of Malignancy",
                    "Nevertheless, patients with the humoral hypercalcemia of malignancy usually have low levels of 1,25(OH)₂D₃.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Familial Hypocalciuric Hypercalcemia",
                "Assertion: Parathyroidectomy is contraindicated for typical FHH.",
                "Reason: FHH patients always have undetectable PTH.",
                2,
                "Assertion true; reason false—PTH is inappropriately normal or modestly elevated, not undetectable.",
                ref(
                    "Familial Hypocalciuric Hypercalcemia",
                    "PTH levels are inappropriately normal for the degree of hypercalcemia and are occasionally modestly elevated.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Vitamin D Deficiency",
                "Assertion: Vitamin D deficiency causes hypocalcemia with secondary hyperparathyroidism.",
                "Reason: Hypocalcemia in vitamin D deficiency is accompanied by hyperphosphatemia like hypoparathyroidism.",
                2,
                "Assertion true; reason false—vitamin D deficiency causes hypophosphatemia, not hyperphosphatemia.",
                ref(
                    "Vitamin D Deficiency",
                    "In the setting of normal renal function, the hypocalcemia of vitamin D deficiency, unlike that of hypoparathyroidism, is accompanied by hypophosphatemia and increased renal phosphate clearance.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Hypophosphatemia",
                "Assertion: Elevated FGF23 causes renal phosphate wasting in XLH and TIO.",
                "Reason: FGF23 levels normalize after tumor removal in TIO.",
                0,
                "Both true and causally linked—FGF23 drives wasting and falls after curative TIO resection.",
                ref(
                    "Hypophosphatemia",
                    "The elevated serum levels of FGF23 in patients with TIO have been shown to normalize after removal of the tumor, correlating with resolution of the hypophosphatemia that characterizes this disorder.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Hyperphosphatemia",
                "Assertion: Tumor lysis syndrome can cause severe hyperphosphatemia.",
                "Reason: Severe hyperphosphatemia in tumor lysis is always asymptomatic.",
                2,
                "Assertion true; reason false—acute severe hyperphosphatemia manifests via hypocalcemia (tetany, seizures).",
                ref(
                    "Hyperphosphatemia",
                    "The clinical manifestations of acute, severe hyperphosphatemia are related mainly to those of the accompanying hypocalcemia, caused by formation of insoluble calcium phosphate precipitates. Thus, tetany, muscle cramps, paresthesias, and seizures may occur",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Consequences of Hypomagnesemia",
                "Assertion: Hypomagnesemia impairs PTH secretion and causes functional hypoparathyroidism.",
                "Reason: Hypocalcemia in hypomagnesemia cannot be corrected until magnesium is repleted.",
                0,
                "Both true and linked—Mg depletion blocks PTH release/action; repletion restores calcium homeostasis.",
                ref(
                    "Consequences of Hypomagnesemia",
                    "Sustained correction of hypocalcemia or hypokalemia cannot be achieved by administration of calcium or potassium alone, respectively, whereas both abnormalities respond to administration of magnesium.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "27",
        "title": "Hormones and Disorders of Mineral Metabolism",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "John P. Bilezikian, Marcella D. Walker, Neil Binkley, David Goltzman, and Michael Mannstadt",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_27_Hormones_and_Disorders_of_Mineral_Metabolism.md",
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
