#!/usr/bin/env python3
"""Generate Williams 15e module w15-30 — Rickets and Osteomalacia."""
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
OUT_NAME = "w15-30_Rickets_and_Osteomalacia.json"


def build() -> dict:
    p = "w15-30"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why rickets and osteomalacia are not interchangeable terms",
                "Rickets is a growth-plate disorder of children with characteristic deformities; osteomalacia is generalized defective mineralization of mature bone at any age—conflating them misleads therapy.",
                ref(
                    "KEY POINTS",
                    "Rickets is a specific bone disorder of growing children and adolescents and is associated with characteristic skeletal deformities.",
                ),
            ),
            note(
                f"{p}-n2",
                "Introduction",
                "How Table 30.1 separates the four major metabolic bone diseases",
                "Rickets/osteomalacia = defective mineralization; osteoporosis = insufficient bone replacement; osteitis fibrosa = woven bone and fibrous tissue with high Ca; Paget = abnormal woven bone with normal Ca—labs and radiographs diverge accordingly.",
                ref(
                    "Introduction",
                    "Of the four major metabolic bone diseases, osteoporosis is by far the most common (see Chapter 27), whereas rickets and osteomalacia combined are a distant second, followed by osteitis deformans (also known as Paget disease of bone; see Chapter 29).",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why FGF23-mediated disease resists conventional vitamin D",
                "Ectopic or excess FGF23 drives renal phosphate wasting and suppresses 1α-hydroxylase—nutritional vitamin D doses (even 10–100×) do not cure XLH, TIO, or related hypophosphatemic syndromes.",
                ref(
                    "Introduction",
                    "In fact, almost all are resistant to even 10- to 100-fold the therapeutic doses of vitamin D used to treat vitamin D–deficiency rickets and osteomalacia.",
                ),
            ),
            note(
                f"{p}-n4",
                "Definition and Histologic Evolution of Osteomalacia",
                "How HVO stage I presents before frank osteomalacia",
                "HVO I (preosteomalacia): increased osteoid surface/volume from 2°HPT but normal osteoid thickness and mineralization—normal Ca/P, low 25(OH)D, elevated PTH and often ALP; cortical loss may already be irreversible.",
                ref(
                    "Definition and Histologic Evolution of Osteomalacia",
                    "The first stage is characterized by an increased bone remodeling due to secondary hyperparathyroidism (2°HPT), associated with increased osteoid surface and osteoid volume, but not the thickness of osteoid, and normal mineralization of bone. This represents the earliest bone histologic phenotype of vitamin D deficiency, designated as hypovitaminosis D osteopathy stage I (HVO I) or preosteomalacia",
                ),
            ),
            note(
                f"{p}-n5",
                "Definition and Histologic Evolution of Osteomalacia",
                "Why osteoid thickness >12.5 µm and MLT >100 days define osteomalacia",
                "HVO III shows mineralization arrest with >90% osteoid-covered surfaces, invariable hypocalcemia, and the histologic thresholds (osteoid thickness >12.5 µm, mineralization lag >100 days) that separate true osteomalacia from high-turnover hyperosteoidosis.",
                ref(
                    "Definition and Histologic Evolution of Osteomalacia",
                    "Osteomalacia defined by an osteoid thickness greater than 12.5  $ \\mu $m and a mineralization lag time of more than 100 days (see Fig. 30.1) conforms to the conventional clinical and radiologic descriptions of osteomalacia.",
                ),
            ),
            note(
                f"{p}-n6",
                "Treatment of Nutritional Rickets and Osteomalacia",
                "How to dose vitamin D for moderate-severe nutritional disease",
                "Give 50,000 IU D2 or D3 weekly for 8–12 weeks, then maintain 1000–2000 IU/day; target 25(OH)D >30 ng/mL and normalize PTH—symptoms improve weeks before radiology/histology.",
                ref(
                    "Treatment of Nutritional Rickets and Osteomalacia",
                    "In symptomatic patients with moderate to severe rickets and osteomalacia, we recommend 50,000 IU of either ergocalciferol (vitamin  $ D_{2} $) or cholecalciferol (vitamin  $ D_{3} $) weekly for 8 to 12 weeks followed by a maintenance dose of 1000 to 2000 units daily.",
                ),
            ),
            note(
                f"{p}-n7",
                "Treatment of Nutritional Rickets and Osteomalacia",
                "Why calcitriol is not first-line for nutritional rickets",
                "Parent vitamin D plus calcium is preferred; calcitriol is adjunctive for severe 2°HPT, malabsorption, marrow fibrosis, or CKD—not sole or first-line therapy for straightforward deficiency.",
                ref(
                    "Treatment of Nutritional Rickets and Osteomalacia",
                    "However, calcitriol should not be either the first-line or sole therapy for vitamin D-deficiency rickets and osteomalacia.",
                ),
            ),
            note(
                f"{p}-n8",
                "Treatment of Nutritional Rickets and Osteomalacia",
                "Calcium co-therapy with vitamin D repletion",
                "Deficiency severe enough for osteomalacia always impairs gut Ca absorption—prescribe calcium carbonate or citrate 1000–1500 mg/day in divided doses alongside vitamin D for biochemical and histologic healing.",
                ref(
                    "Treatment of Nutritional Rickets and Osteomalacia",
                    "Accordingly, oral calcium supplements in the form of calcium carbonate (or citrate) 1000 to 1500 mg/day in divided doses must be prescribed with vitamin D administration to accomplish not only clinical and biochemical but also radiologic and bone histologic responses.",
                ),
            ),
            note(
                f"{p}-n9",
                "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                "How VDDR1A (CYP27B1) responds to calcitriol",
                "Low 1,25(OH)₂D from 1α-hydroxylase deficiency heals with physiologic calcitriol (~0.04 µg/kg/day) though parent vitamin D requires ~10,000 IU/day—lifelong therapy with Ca/P support.",
                ref(
                    "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                    "As can be predicted, the condition responds to the physiologic doses (0.04 μg/kg per day) of active vitamin D metabolite, 1,25-dihydroxyvitamin D or calcitriol, but requires much higher doses of the parent compound vitamin D (~10,000 units/day) to heal rickets—hence the name vitamin D-dependent rickets.",
                ),
            ),
            note(
                f"{p}-n10",
                "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                "Why VDDR2 alopecia is a critical diagnostic clue",
                "VDR defects cause end-organ resistance needing high calcitriol doses; alopecia (variable, sometimes universalis) distinguishes VDDR2 from VDDR1A/1B and does not reverse with treatment.",
                ref(
                    "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                    "Children with VDDR2 have alopecia, a very unique feature that distinguishes VDDR2 from both VDDR1A and VDDR1B.",
                ),
            ),
            note(
                f"{p}-n11",
                "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                "VDDR1B: CYP2R1 25-hydroxylase defect",
                "CYP2R1 mutations cause very low 25(OH)D resembling nutritional deficiency but fail standard repletion—suspect when intake is adequate yet 25(OH)D does not rise with vitamin D.",
                ref(
                    "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                    "Recent genetic studies suggest that mutations in the CYP2R1 gene, $ ^{112,113} $ the principal 25-hydroxylase in humans, are responsible for the severe atypical form of vitamin D deficiency and rickets, although no mutations were found in another child with a similar phenotype. $ ^{118} $ The genetic transmission appears to be both autosomal dominant and recessive, and this rare atypical form rickets is now designated as vitamin D-dependent rickets type 1B (VDDR1B). $ ^{205} $",
                ),
            ),
            note(
                f"{p}-n12",
                "X-Linked Hypophosphatemic Rickets and Osteomalacia",
                "How XLH biochemistry differs from nutritional rickets",
                "XLH (PHEX mutation): very low phosphate, normal Ca and 25(OH)D, low 1,25(OH)₂D, inappropriately elevated FGF23—vitamin D alone cannot correct renal phosphate wasting.",
                ref(
                    "X-Linked Hypophosphatemic Rickets and Osteomalacia",
                    "The most common and consistent biochemical findings are hypophosphatemia, renal phosphate wasting as assessed by tubular reabsorption of phosphate or tubular maximum for phosphate reabsorption adjusted for glomerular filtration rate (GFR; TmP/dlGFR), and elevated serum alkaline phosphatase levels. Serum calcium, 25-hydroxyvitamin D, and PTH levels are characteristically normal in the untreated state. Serum FGF23 levels are inappropriately elevated in the context of chronic hypophosphatemia.",
                ),
            ),
            note(
                f"{p}-n13",
                "Treatment of Hereditary Hypophosphatemic Rickets and Osteomalacia",
                "Standard XLH therapy: calcitriol plus oral phosphate",
                "Children and adults with XLH need active vitamin D metabolites plus divided oral phosphate—not nutritional vitamin D doses; burosumab is now an anti-FGF23 alternative especially when phosphate/calcitriol side effects limit therapy.",
                ref(
                    "Treatment of Hereditary Hypophosphatemic Rickets and Osteomalacia",
                    "The standard of practice for the treatment of XLH in children includes a combination of active vitamin D metabolites (calcitriol or alphacalcidol) and oral phosphate supplementation.",
                ),
            ),
            note(
                f"{p}-n14",
                "Human Anti-FGF23 Monoclonal Antibody (Burosumab)",
                "How burosumab treats FGF23 excess in XLH and TIO",
                "Burosumab binds FGF23, restoring renal phosphate reabsorption and 1,25(OH)₂D—approved for XLH and unresectable TIO when conventional phosphate/calcitriol is inadequate or intolerable.",
                ref(
                    "Human Anti-FGF23 Monoclonal Antibody (Burosumab)",
                    "Burosumab is a recombinant human immunoglobulin G1 monoclonal antibody that binds to the FGF23 receptor and inhibits its activity, counteracting the effects of FGF23 excess.",
                ),
            ),
            note(
                f"{p}-n15",
                "Tumor-Induced Osteomalacia",
                "Why tumor resection is curative in TIO",
                "Mesenchymal tumors ectopically secrete FGF23; wide resection normalizes phosphate and FGF23 within hours—medical therapy is lifelong only when the tumor cannot be found or removed.",
                ref(
                    "Tumor-Induced Osteomalacia",
                    "The treatment of choice for TIO is resection of the tumor, which results in clinical, biochemical, radiologic, and bone histologic improvements.",
                ),
            ),
            note(
                f"{p}-n16",
                "Tumor-Induced Osteomalacia",
                "How Ga-DOTATATE localizes phosphaturic mesenchymal tumors",
                "Small FGF23-secreting tumors are often occult—functional imaging with Ga-DOTATATE PET is increasingly the modality of choice when somatostatin receptor–expressing tumors are suspected.",
                ref(
                    "Tumor-Induced Osteomalacia",
                    "Gallium-DOTATATE positron emission tomography is an emerging imaging modality for tumors producing TIO, is now more widely available, and may be the imaging modality of choice.",
                ),
            ),
            note(
                f"{p}-n17",
                "Conditions That Resemble Rickets and Osteomalacia",
                "How hypophosphatasia is distinguished by low alkaline phosphatase",
                "Despite rickets-like radiographs, hypophosphatasia shows low ALP (<40 IU/L)—the opposite of vitamin D or phosphate-deficiency disease where ALP is almost always high.",
                ref(
                    "Conditions That Resemble Rickets and Osteomalacia",
                    "Although radiologic and bone histologic findings may resemble rickets and osteomalacia, the condition is easily distinguished by the low serum alkaline phosphatase levels (<40 IU/L).",
                ),
            ),
            note(
                f"{p}-n18",
                "Conditions That Resemble Rickets and Osteomalacia",
                "Why bisphosphonates are contraindicated in hypophosphatasia",
                "Low tissue-nonspecific alkaline phosphatase impairs mineralization—bisphosphonates worsen the defect; enzyme replacement with asfotase alfa is approved for childhood-onset disease.",
                ref(
                    "Conditions That Resemble Rickets and Osteomalacia",
                    "Nevertheless, it is clear that patients with hypophosphatasia should not receive bisphosphonate therapy for their “osteoporosis.”",
                ),
            ),
            note(
                f"{p}-n19",
                "Drug-Induced Osteomalacia",
                "Tenofovir/adefovir Fanconi: normal FGF23 trap",
                "NRTI-induced proximal tubular injury causes phosphaturia and osteomalacia like XLH/TIO but FGF23 stays normal—do not anchor on FGF23 alone when evaluating drug-related hypophosphatemia.",
                ref(
                    "Drug-Induced Osteomalacia",
                    "However, unlike other hypophosphatemic syndromes, serum FGF23 levels are characteristically normal in NRTI-related hypophosphatemia.",
                ),
            ),
            note(
                f"{p}-n20",
                "Drug-Induced Osteomalacia",
                "Anticonvulsant-induced conditional vitamin D deficiency",
                "Phenytoin, phenobarbital, primidone, and carbamazepine induce CYP450 catabolism of vitamin D to inactive polar metabolites—prolonged use causes rickets/osteomalacia treatable with standard D + Ca without stopping the anticonvulsant.",
                ref(
                    "Drug-Induced Osteomalacia",
                    "Anticonvulsants, phenytoin, primidone, phenobarbital, and rifampin induce the hepatic cytochrome P450 oxidase enzyme system, which increases the conversion of vitamin D to polar inactive metabolites in the liver, reducing the bioavailable 25-hydroxyvitamin D.",
                ),
            ),
            note(
                f"{p}-n21",
                "Drug-Induced Osteomalacia",
                "Aluminum and direct mineralization inhibitors",
                "Aluminum, fluoride, iron, and etidronate uncouple matrix synthesis from mineralization producing atypical or focal osteomalacia that does not respond to vitamin D—withdraw the offending agent.",
                ref(
                    "Drug-Induced Osteomalacia",
                    "Aluminum is preferentially deposited at the interface of mineralized and unmineralized (osteoid) bone, and uncouples matrix synthesis and its subsequent mineralization, resulting in excess osteoid accumulation.",
                ),
            ),
            note(
                f"{p}-n22",
                "Renal Tubular Acidosis",
                "How type 2 vs type 1 RTA differ in urine pH and alkali dose",
                "Type 2 (proximal): urine pH <5.5, Fanconi features, rickets more common, alkali 10–15 mEq/kg/day. Type 1 (distal): urine pH >6.5 despite acidosis, nephrocalcinosis, alkali 1–3 mEq/kg/day.",
                ref(
                    "Renal Tubular Acidosis",
                    "If urine pH is less than 5.5, type 2 RTA is most likely; if the urine pH is less than 6.5, type 1 or distal RTA is most likely.",
                ),
            ),
            note(
                f"{p}-n23",
                "Calcium-Deficiency Rickets",
                "Calcium-deficiency rickets in sunny geographies",
                "True calcium-deficiency rickets occurs with normal/near-normal 25(OH)D, low Ca, high PTH—think of it when rickets appears in high-sunlight regions with poor dietary calcium (<200 mg/day threshold).",
                ref(
                    "Calcium-Deficiency Rickets",
                    "Unlike nutritional vitamin D and phosphate deficiency, which cause both rickets and osteomalacia, only rickets has been convincingly documented resulting from nutritional calcium deficiency without associated vitamin D deficiency as assessed by normal or low normal serum 25-hydroxyvitamin D levels.",
                ),
            ),
            note(
                f"{p}-n24",
                "Epidemiology and Demographics",
                "Immigrant osteomalacia: dark skin, diet, low sunlight",
                "Immigrants with pigmented skin, vegetarian/high-phytate diets, or cultural covering moving to temperate climates are at high risk—diagnosis is often delayed where deficiency is thought rare.",
                ref(
                    "Epidemiology and Demographics",
                    "Immigrants, particularly those with darkly pigmented skin or specific dietary habits (vegetarians, high phytate intake) moving to temperate zones with limited or reduced sunlight exposure, are at risk of developing rickets and osteomalacia—so-called immigrant osteomalacia.",
                ),
            ),
            note(
                f"{p}-n25",
                "Long-Term Management",
                "Tertiary HPT after long-term oral phosphate therapy",
                "Years of phosphate supplementation in hypophosphatemic osteomalacia can drive hypercalcemic tertiary HPT requiring parathyroidectomy—mirror the risk after nutritional osteomalacia with persistent 2°HPT.",
                ref(
                    "Long-Term Management",
                    "An unintended consequence of long-term (usually years) oral phosphate therapy is the development of 2°HPT, which may evolve into hypercalcemic 2°HPT (also referred to as tertiary hyperparathyroidism).",
                ),
            ),
            note(
                f"{p}-n26",
                "Radiologic Imaging Features",
                "Cod fish vertebrae: virtually diagnostic of osteomalacia",
                "Symmetric biconcave vertebral bodies differ from random wedge/compression fractures of osteoporosis—when present, cod fish vertebrae strongly support osteomalacia over osteoporosis.",
                ref(
                    "Radiologic Imaging Features",
                    "Symmetric biconcavity of vertebrae, referred to as cod fish vertebrae because they resemble vertebrae in cod fish, involves almost all vertebrae.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "X-Linked Hypophosphatemic Rickets and Osteomalacia",
                "A 6-year-old boy has genu varum, phosphate 1.6 mg/dL, calcium 9.4 mg/dL, 25(OH)D 32 ng/mL, and elevated FGF23. The pediatrician starts cholecalciferol 2000 IU daily. Best critique?",
                [
                    "Appropriate—vitamin D deficiency is the cause",
                    "Wrong—XLH needs calcitriol plus oral phosphate or burosumab, not nutritional vitamin D alone",
                    "Wrong—start IV bisphosphonates for bowing",
                    "Wrong—restrict dietary phosphate",
                ],
                1,
                "Normal Ca with hypophosphatemia and high FGF23 defines FGF23-mediated rickets; parent vitamin D does not correct renal phosphate wasting.",
                ref(
                    "X-Linked Hypophosphatemic Rickets and Osteomalacia",
                    "Serum calcium, 25-hydroxyvitamin D, and PTH levels are characteristically normal in the untreated state. Serum FGF23 levels are inappropriately elevated in the context of chronic hypophosphatemia.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Conditions That Resemble Rickets and Osteomalacia",
                "A 45-year-old woman with low BMD has ALP 28 IU/L, recurrent fractures, and metaphyseal lucencies. The rheumatologist plans zoledronate. Most appropriate action?",
                [
                    "Proceed—ALP is irrelevant to treatment choice",
                    "Defer bisphosphonate; evaluate for hypophosphatasia and consider asfotase alfa if confirmed",
                    "Start high-dose vitamin D 50,000 IU weekly only",
                    "Add oral phosphate for presumed XLH",
                ],
                1,
                "Low ALP with osteomalacia-like imaging is hypophosphatasia until proven otherwise—bisphosphonates are contraindicated.",
                ref(
                    "Conditions That Resemble Rickets and Osteomalacia",
                    "Nevertheless, it is clear that patients with hypophosphatasia should not receive bisphosphonate therapy for their “osteoporosis.”",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Treatment of Nutritional Rickets and Osteomalacia",
                "A vegan with osteomalacia (25(OH)D 8 ng/mL, PTH 180 pg/mL) is started on calcitriol 0.5 µg daily without parent vitamin D or calcium. What is the main error?",
                [
                    "Calcitriol dose is too low",
                    "Calcitriol should not be first-line or sole therapy—replete with D2/D3 and oral calcium",
                    "Should use phosphate instead of calcium",
                    "Should stop PTH monitoring",
                ],
                1,
                "Nutritional deficiency requires parent vitamin D repletion plus calcium; calcitriol is adjunctive, not sole first-line therapy.",
                ref(
                    "Treatment of Nutritional Rickets and Osteomalacia",
                    "However, calcitriol should not be either the first-line or sole therapy for vitamin D-deficiency rickets and osteomalacia.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Tumor-Induced Osteomalacia",
                "A 52-year-old man has 3 years of bone pain, phosphate 1.4 mg/dL, normal Ca, low 1,25(OH)₂D, and elevated FGF23. CT shows a 1.2-cm mesenchymal foot mass. Best management?",
                [
                    "Lifelong oral phosphate and calcitriol without surgery",
                    "Wide surgical resection of the tumor",
                    "High-dose ergocalciferol 50,000 IU weekly indefinitely",
                    "Bisphosphonate infusion for low BMD",
                ],
                1,
                "Tumor resection is treatment of choice; phosphate and FGF23 normalize rapidly after curative excision.",
                ref(
                    "Tumor-Induced Osteomalacia",
                    "The treatment of choice for TIO is resection of the tumor, which results in clinical, biochemical, radiologic, and bone histologic improvements.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Drug-Induced Osteomalacia",
                "An HIV patient on tenofovir develops phosphate 1.8 mg/dL, glycosuria, and proximal tubular dysfunction. FGF23 is normal. Diagnosis?",
                [
                    "Tumor-induced osteomalacia",
                    "NRTI-related Fanconi syndrome with hypophosphatemic osteomalacia",
                    "Primary hyperparathyroidism",
                    "XLH with false-normal FGF23 assay",
                ],
                1,
                "Tenofovir causes proximal tubular injury and phosphaturia with characteristically normal FGF23—unlike FGF23-mediated genetic or tumor disease.",
                ref(
                    "Drug-Induced Osteomalacia",
                    "However, unlike other hypophosphatemic syndromes, serum FGF23 levels are characteristically normal in NRTI-related hypophosphatemia.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                "An infant has rickets, low Ca, low 1,25(OH)₂D, normal 25(OH)D, and total-body alopecia. Which therapy is most appropriate?",
                [
                    "Standard nutritional vitamin D 1000 IU daily",
                    "High-dose calcitriol for VDDR2 end-organ resistance",
                    "Oral phosphate alone",
                    "Burosumab",
                ],
                1,
                "Alopecia with normal 25(OH)D points to VDDR2 (VDR defect) requiring high-dose active vitamin D, not nutritional repletion.",
                ref(
                    "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                    "Children with VDDR2 have alopecia, a very unique feature that distinguishes VDDR2 from both VDDR1A and VDDR1B.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                "A child has rickets, low Ca, low 1,25(OH)₂D, and normal 25(OH)D without alopecia. CYP27B1 mutation is found. Best treatment?",
                [
                    "Calcitriol 0.04 µg/kg/day lifelong with Ca/P support",
                    "Sun exposure alone",
                    "Oral phosphate without vitamin D",
                    "Parathyroidectomy",
                ],
                0,
                "VDDR1A (1α-hydroxylase deficiency) responds to physiologic calcitriol replacement.",
                ref(
                    "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                    "As can be predicted, the condition responds to the physiologic doses (0.04 μg/kg per day) of active vitamin D metabolite, 1,25-dihydroxyvitamin D or calcitriol, but requires much higher doses of the parent compound vitamin D (~10,000 units/day) to heal rickets—hence the name vitamin D-dependent rickets.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Renal Tubular Acidosis",
                "A child with normal anion gap metabolic acidosis has fasting urine pH 7.0, nephrocalcinosis, and rickets. Most likely RTA type and initial alkali dose?",
                [
                    "Type 2 RTA; 10–15 mEq/kg/day alkali",
                    "Type 1 (distal) RTA; 1–3 mEq/kg/day alkali",
                    "Type 4 RTA; fludrocortisone only",
                    "No alkali—phosphate binders only",
                ],
                1,
                "Inability to acidify urine (pH >6.5) with nephrocalcinosis indicates distal type 1 RTA; lower alkali doses than proximal type 2.",
                ref(
                    "Renal Tubular Acidosis",
                    "Alkali therapy with either sodium or potassium bicarbonate (1–2 mmol/kg/day for type 1 RTA and 10–15 mmol/kg/day for type 2 RTA) is generally recommended and the dose adjusted as dictated by the clinical response and prevailing biochemical abnormalities.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Renal Tubular Acidosis",
                "A patient with Fanconi syndrome, urine pH 5.0 during acidosis, and hypophosphatemic rickets is evaluated. RTA type?",
                [
                    "Type 1 distal RTA",
                    "Type 2 proximal RTA",
                    "Type 4 hyperkalemic RTA",
                    "Type 3 combined RTA only",
                ],
                1,
                "Proximal RTA (type 2) acidifies urine to <5.5 and commonly accompanies Fanconi syndrome with phosphate wasting and rickets.",
                ref(
                    "Renal Tubular Acidosis",
                    "If urine pH is less than 5.5, type 2 RTA is most likely; if the urine pH is less than 6.5, type 1 or distal RTA is most likely.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Calcium-Deficiency Rickets",
                "A 5-year-old in Nigeria has rickets, Ca 7.2 mg/dL, PTH elevated, and 25(OH)D 28 ng/mL. Best initial therapy?",
                [
                    "High-dose vitamin D only",
                    "Calcium supplementation with or without modest vitamin D",
                    "Burosumab",
                    "Tumor localization imaging",
                ],
                1,
                "Normal/near-normal 25(OH)D with low Ca and rickets suggests calcium-deficiency rickets—calcium is primary therapy.",
                ref(
                    "Calcium-Deficiency Rickets",
                    "Nevertheless, when a child is encountered with rickets and if the serum level of 25-hydroxyvitamin D is normal, think of calcium-deficiency rickets, particularly if serum calcium is low and PTH is elevated.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Introduction",
                "A resident confuses osteomalacia with osteoporosis on biopsy. Which feature best distinguishes osteomalacia?",
                [
                    "Low bone turnover only",
                    "Defective mineralization with excess unmineralized osteoid",
                    "Replacement by woven bone and fibrous tissue",
                    "Abnormal local woven bone remodeling only",
                ],
                1,
                "Osteomalacia = defective mineralization of lamellar matrix; osteoporosis = insufficient replacement of normal bone; osteitis fibrosa = woven bone/fibrous tissue.",
                ref(
                    "Introduction",
                    "By contrast, osteomalacia is a generalized softening of bones regardless of age or cause and thus occurs in both children and adults.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Definition and Histologic Evolution of Osteomalacia",
                "Bone biopsy shows osteoid thickness 15 µm and mineralization lag 120 days. Stage of hypovitaminosis D osteopathy?",
                [
                    "HVO stage I (preosteomalacia)",
                    "HVO stage III with classical osteomalacia criteria met",
                    "Normal bone remodeling",
                    "Osteoporosis only",
                ],
                1,
                "Osteoid thickness >12.5 µm and MLT >100 days define classical osteomalacia, corresponding to advanced HVO III.",
                ref(
                    "Definition and Histologic Evolution of Osteomalacia",
                    "Osteomalacia defined by an osteoid thickness greater than 12.5  $ \\mu $m and a mineralization lag time of more than 100 days (see Fig. 30.1) conforms to the conventional clinical and radiologic descriptions of osteomalacia.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Treatment of Nutritional Rickets and Osteomalacia",
                "After 10 weeks of 50,000 IU vitamin D weekly, a patient with osteomalacia has symptom relief but still elevated ALP. Next step?",
                [
                    "Stop all therapy—patient is cured",
                    "Continue maintenance D 1000–2000 IU/day with calcium; monitor until ALP and PTH normalize",
                    "Switch to calcitriol monotherapy permanently",
                    "Add bisphosphonate immediately",
                ],
                1,
                "Symptoms improve before biochemistry/radiology; maintenance D + Ca with monitoring is required—antifracture therapy waits until osteomalacia heals.",
                ref(
                    "Treatment of Nutritional Rickets and Osteomalacia",
                    "With effective therapy, symptoms of osteomalacia start improving within a few weeks, but complete disappearance of symptoms usually takes a few months and sometimes years.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Long-Term Management",
                "An adult with XLH on oral phosphate for 8 years develops Ca 11.2 mg/dL and PTH 250 pg/mL. Most likely complication?",
                [
                    "Primary vitamin D deficiency",
                    "Tertiary hyperparathyroidism from long-term phosphate therapy",
                    "Hypophosphatasia",
                    "Tumor lysis syndrome",
                ],
                1,
                "Chronic oral phosphate can evolve to hypercalcemic tertiary HPT requiring specialized management including possible parathyroidectomy.",
                ref(
                    "Long-Term Management",
                    "An unintended consequence of long-term (usually years) oral phosphate therapy is the development of 2°HPT, which may evolve into hypercalcemic 2°HPT (also referred to as tertiary hyperparathyroidism).",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Tumor-Induced Osteomalacia",
                "FGF23-secreting tumor cannot be localized after Ga-DOTATATE and venous sampling. Symptomatic hypophosphatemia persists. Approved targeted therapy?",
                [
                    "High-dose ergocalciferol alone",
                    "Burosumab anti-FGF23 antibody",
                    "IV bisphosphonates",
                    "Thiazide diuretic for hypercalciuria only",
                ],
                1,
                "When tumors are unresectable or occult, burosumab (anti-FGF23) is approved alongside phosphate/calcitriol options.",
                ref(
                    "Human Anti-FGF23 Monoclonal Antibody (Burosumab)",
                    "Several other clinical trials with burosumab in children and adults with XLH have demonstrated efficacy, and burosumab is now approved for treatment of TIO (see next section).",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Epidemiology and Demographics",
                "A Somali woman in Michigan wears full covering, is vegetarian, and presents with proximal weakness and diffuse bone pain. 25(OH)D is 6 ng/mL. Likely scenario?",
                [
                    "Primary hyperparathyroidism",
                    "Immigrant osteomalacia from combined low sun and dietary risk",
                    "Paget disease of bone",
                    "Hypophosphatasia",
                ],
                1,
                "Dark skin, dietary habits, covering, and migration to low-sun latitudes define high-risk immigrant osteomalacia often diagnosed late.",
                ref(
                    "Epidemiology and Demographics",
                    "Immigrants, particularly those with darkly pigmented skin or specific dietary habits (vegetarians, high phytate intake) moving to temperate zones with limited or reduced sunlight exposure, are at risk of developing rickets and osteomalacia—so-called immigrant osteomalacia.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Drug-Induced Osteomalacia",
                "A patient on long-term phenytoin has low 25(OH)D and rickets. FGF23 is normal. Management?",
                [
                    "Stop phenytoin immediately regardless of seizure control",
                    "Vitamin D and calcium repletion with lifelong monitoring; anticonvulsant may continue",
                    "Burosumab",
                    "Aluminum chelation only",
                ],
                1,
                "Anticonvulsants cause conditional vitamin D deficiency via increased catabolism—treat with standard D + Ca; discontinuation of anticonvulsant is not required.",
                ref(
                    "Drug-Induced Osteomalacia",
                    "Unlike in the case of NRTIs, there is no need to discontinue the drugs that caused the problem in the first place, but lifelong monitoring for vitamin D deficiency is required.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Radiologic Imaging Features",
                "Lateral spine radiograph shows uniform biconcave vertebrae ('cod fish'). DEXA shows low BMD. Most likely diagnosis?",
                [
                    "Postmenopausal osteoporosis",
                    "Osteomalacia",
                    "Paget disease",
                    "Osteitis fibrosa cystica",
                ],
                1,
                "Symmetric biconcave vertebrae are virtually diagnostic of osteomalacia and contrast with random wedge deformities of osteoporosis.",
                ref(
                    "Radiologic Imaging Features",
                    "When present, the cod fish vertebrae-like appearance of the spine is virtually diagnostic of osteomalacia (see Fig. 30.4A).",
                ),
            ),
            mcq(
                f"{p}-m19",
                "X-Linked Hypophosphatemic Rickets and Osteomalacia",
                "Which radiographic feature is seen almost exclusively in XLH among rickets types?",
                [
                    "Metaphyseal fraying and cupping",
                    "Enthesopathy",
                    "Pseudofractures in ribs",
                    "Cortical thinning",
                ],
                1,
                "Enthesopathy is almost exclusive to XLH; XLH paradoxically has thick cortices unlike nutritional rickets.",
                ref(
                    "Radiologic and Biochemical Findings",
                    "However, none of these findings is specific enough to distinguish the type of rickets, but enthesopathy occurs almost exclusively in XLH and is almost never seen in other types of rickets and osteomalacia.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Biochemical Changes",
                "Which statement about hypophosphatemic rickets is correct?",
                [
                    "Serum calcium is always low",
                    "Serum calcium is characteristically normal",
                    "25(OH)D is always low",
                    "Alkaline phosphatase is usually normal",
                ],
                1,
                "Hypophosphatemic syndromes maintain normal Ca (except some renal tubular defects); ALP is elevated despite low phosphate.",
                ref(
                    "Biochemical Changes",
                    "Most important, serum calcium is always normal in all forms of hypophosphatemic rickets and osteomalacia, except in certain types of renal tubular defects.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Tumor-Induced Osteomalacia",
                "After successful TIO tumor resection, how quickly may FGF23 normalize?",
                [
                    "6–12 months",
                    "Within ~24 hours (half-life ~45 minutes)",
                    "Never—FGF23 stays elevated lifelong",
                    "Only after 5 years of phosphate therapy",
                ],
                1,
                "FGF23 has a short half-life; levels and phosphate often normalize within a day of curative resection.",
                ref(
                    "Tumor-Induced Osteomalacia",
                    "Levels of serum phosphate and FGF23, which has a half-life of ~45 minutes, return to normal rapidly, often within 24 hours, after tumor resection, but healing of osteomalacia may take several months.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                "A child with adequate vitamin D intake has very low 25(OH)D that does not rise with standard supplementation. Gene to suspect?",
                [
                    "PHEX",
                    "CYP2R1 (VDDR1B)",
                    "FGF23",
                    "TNSALP",
                ],
                1,
                "CYP2R1 encodes principal 25-hydroxylase; VDDR1B mimics nutritional deficiency but resists conventional repletion.",
                ref(
                    "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                    "Recent genetic studies suggest that mutations in the CYP2R1 gene, $ ^{112,113} $ the principal 25-hydroxylase in humans, are responsible for the severe atypical form of vitamin D deficiency and rickets",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Drug-Induced Osteomalacia",
                "A dialysis patient in the 1980s on aluminum-containing phosphate binders has low-turnover bone disease unresponsive to vitamin D. Mechanism?",
                [
                    "Excess FGF23 production",
                    "Aluminum uncouples matrix synthesis from mineralization at the osteoid interface",
                    "Primary hyperparathyroidism",
                    "CYP2R1 mutation",
                ],
                1,
                "Aluminum deposits at the mineralized–osteoid interface causing atypical osteomalacia that does not respond to vitamin D.",
                ref(
                    "Drug-Induced Osteomalacia",
                    "Aluminum is preferentially deposited at the interface of mineralized and unmineralized (osteoid) bone, and uncouples matrix synthesis and its subsequent mineralization, resulting in excess osteoid accumulation.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Muscle Weakness",
                "An adult with vitamin D-deficiency osteomalacia vs XLH typically differs in which dominant symptom?",
                [
                    "Vitamin D deficiency: more muscle weakness than bone pain",
                    "Vitamin D deficiency: more bone pain; XLH: more prominent muscle weakness",
                    "Both always have identical symptoms",
                    "Neither causes muscle weakness",
                ],
                1,
                "Bone pain predominates in vitamin D-deficiency osteomalacia; muscle weakness is more prominent in hypophosphatemic disease.",
                ref(
                    "Muscle Weakness",
                    "In general, muscle weakness is more prominent in hypophosphatemic rickets and osteomalacia, whereas bone pain is more common in vitamin D-deficiency osteomalacia.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Pathogenesis of Rickets and Osteomalacia",
                "Order of frequency for rickets/osteomalacia pathogenesis worldwide is:",
                [
                    "Calcium deficiency, then vitamin D, then phosphate depletion",
                    "Vitamin D depletion/deficiency, then phosphate depletion, then calcium deficiency",
                    "Phosphate depletion first in all regions",
                    "Drug-induced causes are most common globally",
                ],
                1,
                "Vitamin D deficiency is first; phosphate depletion (genetic/acquired) is second and dominates where D deficiency is not endemic.",
                ref(
                    "Pathogenesis of Rickets and Osteomalacia",
                    "The three principal mechanisms by which rickets and osteomalacia develop are vitamin D depletion or deficiency, phosphate depletion or deficiency, and calcium deficiency—in that order of frequency.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Treatment of Nutritional Rickets and Osteomalacia",
                "A post–gastric bypass patient has osteomalacia. Initial vitamin D repletion strategy?",
                [
                    "400 IU daily only",
                    "Higher doses (often 10,000–50,000 IU/day) or injectable cholecalciferol due to malabsorption",
                    "Phosphate alone without vitamin D",
                    "Calcitriol monotherapy without parent vitamin D",
                ],
                1,
                "Malabsorptive states need much higher oral or parenteral vitamin D doses to replete stores.",
                ref(
                    "Treatment of Nutritional Rickets and Osteomalacia",
                    "In malabsorptive states, particularly in patients with small intestinal resection or gastric bypass surgery, higher doses of vitamin D (10,000–50,000 IU/day) may be required to replete vitamin D stores.",
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
                "Osteomalacia can occur in both children and adults, whereas classical rickets occurs only before epiphyseal fusion.",
                True,
                "Rickets is confined to the growing skeleton; osteomalacia is age-independent defective mineralization of mature bone.",
                ref(
                    "KEY POINTS",
                    "Osteomalacia is a generalized softening of the bones regardless of age or cause and thus occurs both in children and adults.",
                ),
            ),
            tf(
                f"{p}-t2",
                "KEY POINTS",
                "In countries with routine vitamin D food fortification, genetic and acquired rickets/osteomalacia become relatively more common.",
                True,
                "Fortification reduces nutritional disease, shifting the observed spectrum toward genetic and acquired forms.",
                ref(
                    "KEY POINTS",
                    "However, in countries where routine fortification of dairy and food products is implemented, genetic and acquired forms of rickets and osteomalacia are relatively more common.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Definition and Histologic Evolution of Osteomalacia",
                "HVO stage I already shows increased osteoid thickness meeting criteria for classical osteomalacia.",
                False,
                "HVO I has increased osteoid surface/volume but normal osteoid thickness and mineralization—preosteomalacia.",
                ref(
                    "Definition and Histologic Evolution of Osteomalacia",
                    "The first stage is characterized by an increased bone remodeling due to secondary hyperparathyroidism (2°HPT), associated with increased osteoid surface and osteoid volume, but not the thickness of osteoid, and normal mineralization of bone.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Treatment of Nutritional Rickets and Osteomalacia",
                "Ergocalciferol (D2) and cholecalciferol (D3) are equally effective for treating nutritional rickets and osteomalacia.",
                True,
                "Despite debate, both preparations replenish stores and heal disease comparably in clinical practice.",
                ref(
                    "Treatment of Nutritional Rickets and Osteomalacia",
                    "there is not much difference between vitamin  $ D_{2} $ and vitamin  $ D_{3} $ in replenishing depleted vitamin D stores, $ ^{203} $ and both vitamin D preparations are equally effective in treating rickets and osteomalacia.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                "In VDDR1A and VDDR1B, serum 25-hydroxyvitamin D levels are always normal.",
                False,
                "VDDR1A and VDDR2 have normal 25(OH)D; VDDR1B has low or very low 25(OH)D resembling nutritional deficiency.",
                ref(
                    "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                    "Biochemical and radiologic features of vitamin D-dependent rickets are similar to those seen in nutritional rickets, except serum 25-hydroxyvitamin D levels are normal in VDDR1A and VDDR2, and low or very low in VDDR1B (see Table 30.2).",
                ),
            ),
            tf(
                f"{p}-t6",
                "X-Linked Hypophosphatemic Rickets and Osteomalacia",
                "XLH is caused by inactivating mutations in the PHEX gene leading to excess FGF23 activity.",
                True,
                "PHEX loss impairs FGF23 degradation; FGF23 excess drives renal phosphate wasting.",
                ref(
                    "X-Linked Hypophosphatemic Rickets and Osteomalacia",
                    "XLH (OMIM #307800) is an X-linked dominantly inherited disorder with an estimated prevalence of about 1 in 20,000 live births. $ ^{7} $ It is the most common form of hereditary hypophosphatemic rickets, caused by an inactivating mutation in the phosphate-regulating gene with homologies to endopeptidases on the X chromosome (PHEX).",
                ),
            ),
            tf(
                f"{p}-t7",
                "Tumor-Induced Osteomalacia",
                "A normal serum FGF23 level definitively excludes tumor-induced osteomalacia.",
                False,
                "FGF23 may be normal in some TIO cases depending on assay; hypophosphatemia with appropriate clinical context still warrants tumor search.",
                ref(
                    "Tumor-Induced Osteomalacia",
                    "Although an elevated level of FGF23 supports diagnostic suspicion, a normal serum FGF23 level does not exclude the diagnosis.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Conditions That Resemble Rickets and Osteomalacia",
                "Asfotase alfa enzyme replacement is available for childhood-onset hypophosphatasia.",
                True,
                "Enzyme replacement targets tissue-nonspecific alkaline phosphatase deficiency.",
                ref(
                    "Conditions That Resemble Rickets and Osteomalacia",
                    "Enzyme replacement therapy with asfotase alfa is now available for childhood-onset hypophosphatasia.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Drug-Induced Osteomalacia",
                "Tenofovir-induced hypophosphatemia is typically associated with elevated FGF23.",
                False,
                "NRTI-related Fanconi syndrome causes phosphaturia with characteristically normal FGF23.",
                ref(
                    "Drug-Induced Osteomalacia",
                    "However, unlike other hypophosphatemic syndromes, serum FGF23 levels are characteristically normal in NRTI-related hypophosphatemia.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Renal Tubular Acidosis",
                "Type 4 RTA commonly causes rickets and osteomalacia.",
                False,
                "Type 4 hyperkalemic RTA is not associated with rickets or osteomalacia.",
                ref(
                    "Renal Tubular Acidosis",
                    "Type 4 RTA, also known as hyperkalemic RTA, does not cause either rickets or osteomalacia.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Calcium-Deficiency Rickets",
                "Adult osteomalacia due to isolated dietary calcium deficiency has been well documented.",
                False,
                "Only rickets—not adult osteomalacia—has been convincingly documented from calcium deficiency alone.",
                ref(
                    "Calcium-Deficiency Rickets",
                    "Although much has been learned on the role of calcium nutrition in the pathogenesis of osteoporosis (see Chapter 29), no case of osteomalacia in an adult due to calcium deficiency alone has been reported; the reasons for this discordant effect of calcium nutrition on the skeleton in children and adults is perplexing.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Radiologic Imaging Features",
                "Cortical thinning on long-bone radiographs is typically absent in XLH.",
                True,
                "XLH shows thick cortices rather than the cortical thinning seen in nutritional rickets.",
                ref(
                    "Radiologic Imaging Features",
                    "Cortical thinning in long bones is not seen in XLH, and, in fact, thick cortices are the rule rather than the exception.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Concluding Remarks",
                "After healing nutritional osteomalacia, irreversible cortical bone loss may leave patients at ongoing fracture risk.",
                True,
                "2°HPT-mediated cortical loss before diagnosis is not fully reversible despite clinical cure.",
                ref(
                    "Concluding Remarks",
                    "In nutritional rickets and osteomalacia,  $ 2^{\\circ} $HPT may persist for months or years despite clinical improvement and confers an increased fracture risk due to irreversible cortical bone loss that has already occurred by the time of diagnosis.",
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
                "Assertion: Rickets and osteomalacia are the second most common metabolic bone diseases after osteoporosis.",
                "Reason: Osteomalacia involves defective mineralization of mature lamellar bone.",
                0,
                "Both true and linked—rickets/osteomalacia rank second in prevalence among the four major metabolic bone diseases defined by mineralization defects.",
                ref(
                    "Introduction",
                    "Of the four major metabolic bone diseases, osteoporosis is by far the most common (see Chapter 27), whereas rickets and osteomalacia combined are a distant second, followed by osteitis deformans (also known as Paget disease of bone; see Chapter 29).",
                ),
            ),
            ar(
                f"{p}-ar2",
                "KEY POINTS",
                "Assertion: Removal of FGF23-secreting mesenchymal tumors can cure acquired rickets/osteomalacia.",
                "Reason: FGF23 inhibits renal phosphate reabsorption and 1α-hydroxylase activity.",
                0,
                "Both true and causally linked—tumor FGF23 drives phosphaturia; resection removes the source.",
                ref(
                    "KEY POINTS",
                    "Several acquired forms of rickets and osteomalacia occur due to ectopic production of fibroblast growth factor 23, mostly by benign mesenchymal or skeletal tumors—the removal of which cures the bone disease.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Definition and Histologic Evolution of Osteomalacia",
                "Assertion: In HVO stage III, hypocalcemia becomes invariable.",
                "Reason: Osteoid-covered bone resists osteoclastic resorption needed to maintain serum calcium.",
                0,
                "Both true and linked—extensive osteoid coating impairs calcium mobilization from bone.",
                ref(
                    "Definition and Histologic Evolution of Osteomalacia",
                    "It is at this stage that hypocalcemia is invariable, as the osteoid-covered bone is resistant to osteoclastic bone resorption, which is a necessary mechanism to maintain normal serum calcium levels.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Treatment of Nutritional Rickets and Osteomalacia",
                "Assertion: Calcitriol should not be first-line sole therapy for nutritional vitamin D-deficiency osteomalacia.",
                "Reason: Parent vitamin D and calcium repletion adequately restores substrate and gut absorption in most cases.",
                0,
                "Both true—standard repletion achieves goals; calcitriol is adjunctive for select severe cases.",
                ref(
                    "Treatment of Nutritional Rickets and Osteomalacia",
                    "However, calcitriol should not be either the first-line or sole therapy for vitamin D-deficiency rickets and osteomalacia.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                "Assertion: VDDR1A responds to physiologic doses of calcitriol.",
                "Reason: VDDR1A is caused by defective vitamin D receptor preventing hormone action.",
                2,
                "Assertion true (CYP27B1/1α-hydroxylase defect); reason false—that describes VDDR2, not VDDR1A.",
                ref(
                    "Vitamin D-Dependent Rickets Types 1A, 1B, and 2",
                    "Genetic defect in the 25-hydroxyvitamin D  $ 1\\alpha $-hydroxylase enzyme, VDDR1A, or pseudo-vitamin D deficiency, is a rare autosomal-recessive disorder due to mutations in the cytochrome P450 (CYP27B1) gene for the  $ 1\\alpha $-hydroxylase enzyme located on the chromosome 12q13.3, resulting in decreased serum levels of 1,25-dihydroxyvitamin D.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "X-Linked Hypophosphatemic Rickets and Osteomalacia",
                "Assertion: XLH features hypophosphatemia with normal serum calcium.",
                "Reason: PHEX mutations directly increase intestinal calcium absorption.",
                2,
                "Assertion true; reason false—hypophosphatemia reflects FGF23-mediated renal wasting, not increased gut Ca absorption.",
                ref(
                    "X-Linked Hypophosphatemic Rickets and Osteomalacia",
                    "Serum calcium, 25-hydroxyvitamin D, and PTH levels are characteristically normal in the untreated state.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Tumor-Induced Osteomalacia",
                "Assertion: TIO biochemical hallmarks include hypophosphatemia, low/normal 1,25(OH)₂D, and elevated FGF23.",
                "Reason: Tumor removal has no effect on FGF23 levels.",
                2,
                "Assertion true; reason false—FGF23 and phosphate normalize rapidly after curative resection.",
                ref(
                    "Tumor-Induced Osteomalacia",
                    "The biochemical hallmark of TIO is the triad of hypophosphatemia due to renal phosphate wasting, inappropriately low or normal serum 1,25-dihydroxyvitamin D level, and elevated or inappropriately normal serum FGF23 level.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Conditions That Resemble Rickets and Osteomalacia",
                "Assertion: Hypophosphatasia resembles osteomalacia radiographically but has low alkaline phosphatase.",
                "Reason: Low alkaline phosphatase is also typical of nutritional vitamin D-deficiency osteomalacia.",
                2,
                "Assertion true; reason false—ALP is almost always elevated in vitamin D and phosphate-deficiency disease.",
                ref(
                    "Conditions That Resemble Rickets and Osteomalacia",
                    "As noted previously, the serum alkaline phosphatase is almost always elevated in vitamin D- and phosphate-deficiency rickets and osteomalacia.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Drug-Induced Osteomalacia",
                "Assertion: Anticonvulsants can cause rickets through conditional vitamin D deficiency.",
                "Reason: Anticonvulsants must always be discontinued to correct the bone disease.",
                2,
                "Assertion true; reason false—vitamin D and calcium therapy suffices without stopping anticonvulsants.",
                ref(
                    "Drug-Induced Osteomalacia",
                    "Unlike in the case of NRTIs, there is no need to discontinue the drugs that caused the problem in the first place, but lifelong monitoring for vitamin D deficiency is required.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Renal Tubular Acidosis",
                "Assertion: Type 2 RTA is more commonly associated with rickets than type 1 RTA.",
                "Reason: Type 2 RTA features urine pH <5.5 during metabolic acidosis.",
                0,
                "Both true and linked—proximal RTA with Fanconi features causes more rickets; acidifies urine appropriately.",
                ref(
                    "Renal Tubular Acidosis",
                    "Among the four forms of RTA, type 2 RTA, with or without Fanconi syndrome, is characterized by impaired proximal renal tubular reabsorption of phosphate in addition to glucose, uric acid, amino acids, and low-molecular-weight proteins and can present with rickets and osteomalacia.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Long-Term Management",
                "Assertion: Long-term oral phosphate in hypophosphatemic osteomalacia can cause tertiary hyperparathyroidism.",
                "Reason: This complication is unique to nutritional vitamin D deficiency and never occurs with phosphate therapy.",
                3,
                "Assertion true; reason false—tertiary HPT also follows long phosphate therapy in hypophosphatemic disease.",
                ref(
                    "Concluding Remarks",
                    "In a few patients, particularly those with hypophosphatemic rickets and osteomalacia, long-term oral phosphate therapy leads to hypercalcemic  $ 2^{\\circ} $HPT (or tertiary hyperparathyroidism) requiring parathyroidectomy.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Calcium-Deficiency Rickets",
                "Assertion: Calcium-deficiency rickets can occur with normal serum 25-hydroxyvitamin D.",
                "Reason: Calcium-deficiency osteomalacia is equally well documented in adults.",
                2,
                "Assertion true; reason false—adult osteomalacia from isolated calcium deficiency has not been reported.",
                ref(
                    "Calcium-Deficiency Rickets",
                    "no case of osteomalacia in an adult due to calcium deficiency alone has been reported; the reasons for this discordant effect of calcium nutrition on the skeleton in children and adults is perplexing.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "30",
        "title": "Rickets and Osteomalacia",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Arti Bhan, Ajay D. Rao, Sanjay K. Bhadada, and Sudhaker D. Rao",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_30_Rickets_and_Osteomalacia.md",
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
