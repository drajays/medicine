#!/usr/bin/env python3
"""Generate Williams 15e module w15-29 — Osteoporosis: Basic and Clinical Aspects."""
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
OUT_NAME = "w15-29_Osteoporosis_Basic_and_Clinical_Aspects.json"


def build() -> dict:
    p = "w15-29"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why the skeleton is now viewed as endocrine tissue",
                "Beyond mechanical support and mineral storage, mineralized mesenchymal tissue exports peptides that regulate circulating phosphate and whole-body energy metabolism—redefining bone as an active endocrine organ.",
                ref(
                    "KEY POINTS",
                    "In addition to the well-known mechanical support and storage of mineral, mineralized mesenchymal tissue also exports peptides critical for regulation of circulating phosphate and whole-body energy metabolism.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How online fracture algorithms fit clinical practice",
                "After decades of risk-factor research, readily available online algorithms predict long-term fracture risk and are an important evaluation tool alongside BMD and biochemical markers.",
                ref(
                    "KEY POINTS",
                    "Online algorithms have been developed to help predict long-term fracture risk and are a readily available and important tool for evaluating patients.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why osteoporosis faces a treatment crisis",
                "Despite effective drugs, rare adverse events have been overemphasized relative to fracture-prevention benefits, driving physician underprescription and patient reluctance—the 'crisis in osteoporosis treatment.'",
                ref(
                    "Historical Context",
                    "Unfortunately, in the past few years, this auspicious trend has reversed, attracting great interest in what has been coined the \"crisis in osteoporosis treatment.\"",
                ),
            ),
            note(
                f"{p}-n4",
                "KEY POINTS",
                "How osteoporosis dosing differs from other chronic drugs",
                "Unlike most chronic therapies requiring daily adherence, successful osteoporosis treatment may need only weekly, monthly, biannual, or even annual dosing—an advantage for long-term compliance.",
                ref(
                    "KEY POINTS",
                    "Unlike available therapeutic options for other chronic disorders, osteoporosis therapy is unique in that weekly, monthly, biannual, or even annual dosing may be sufficient to accomplish successful treatment.",
                ),
            ),
            note(
                f"{p}-n5",
                "Structure and Function of the Skeleton",
                "How BMUs execute skeletal remodeling",
                "Bone remodeling units—BMUs—comprise osteoblasts, osteoclasts, lining cells, and osteocytes; they are more active in trabecular than cortical bone and maintain skeletal stability and calcium supply.",
                ref(
                    "Structure and Function of the Skeleton",
                    "Basic multicellular units (BMUs) carry out bone remodeling and consist of osteoblasts, osteoclasts, bone lining cells, and osteocytes.",
                ),
            ),
            note(
                f"{p}-n6",
                "Structure and Function of the Skeleton",
                "Why osteocytes initiate remodeling",
                "Osteocytes communicate through canaliculi and are thought to initiate remodeling by signaling lining cells and osteoblasts—often in response to microdamage or mechanical sensing.",
                ref(
                    "Structure and Function of the Skeleton",
                    "The osteocyte, communicating by release of factors through tiny canaliculi, is thought to initiate the remodeling process, providing signals to both the lining cell and the osteoblast.",
                ),
            ),
            note(
                f"{p}-n7",
                "Embryology and Anatomy",
                "How modeling differs from remodeling",
                "Modeling shapes cortical bone through uncoupled osteoblast activity (especially during growth), whereas remodeling maintains adult bone mass through coupled resorption and formation within BMUs.",
                ref(
                    "Embryology and Anatomy",
                    "New cortical bone is shaped by a process called modeling, in which osteoblast activity occurs uncoupled to osteoclastic bone resorption.",
                ),
            ),
            note(
                f"{p}-n8",
                "Osteoclast Differentiation and Function",
                "Why the RANKL/OPG ratio governs resorption",
                "PTH, vitamin D, and prostaglandins reciprocally increase RANKL and decrease OPG on osteoblast-lineage cells; the resulting RANKL/OPG balance is the key switch for osteoclastogenesis.",
                ref(
                    "Osteoclast Differentiation and Function",
                    "For these factors, there is a reciprocal relationship between RANKL stimulation and OPG inhibition that causes activation of osteoclastogenesis and enhanced resorption.",
                ),
            ),
            note(
                f"{p}-n9",
                "Overview of Remodeling",
                "How sclerostin blocks Wnt/LRP5 bone formation",
                "Osteocyte-derived sclerostin antagonizes Wnt signaling by binding LRP4/5/6 (with Dkk1), inhibiting osteoblast activity—making sclerostin neutralization a therapeutic target.",
                ref(
                    "Overview of Remodeling",
                    "Sclerostin (the product of the SOST gene), the osteocyte-specific protein that inhibits bone formation, and another important Wnt inhibitor, dickkopf 1 (Dkk1), work by binding to LRP4, LRP5, and LRP6, thereby blocking Wnt signaling.",
                ),
            ),
            note(
                f"{p}-n10",
                "Overview of Remodeling",
                "Why romosozumab was FDA-approved",
                "Anti-sclerostin monoclonal antibodies increase bone formation; romosozumab gained FDA approval in 2019 for high-risk postmenopausal osteoporosis based on two pivotal fracture trials.",
                ref(
                    "Overview of Remodeling",
                    "Monoclonal antibodies that bind to sclerostin have been developed. Based on the results of two pivotal studies, romosozumab was approved by the FDA in 2019 to treat osteoporosis in postmenopausal women at high risk of fracture.",
                ),
            ),
            note(
                f"{p}-n11",
                "Dual-Energy X-Ray Absorptiometry",
                "How DXA T-scores define osteoporosis categories",
                "T-score compares BMD to young-adult mean: normal within 1 SD; osteopenia >1 to <2.5 SD below; osteoporosis ≥2.5 SD below; severe osteoporosis adds fragility fracture.",
                ref(
                    "Dual-Energy X-Ray Absorptiometry",
                    "A value below -2.5 SD is usually considered osteoporotic in women or men 50 years of age and older.",
                ),
            ),
            note(
                f"{p}-n12",
                "Dual-Energy X-Ray Absorptiometry",
                "Why spine DXA can mislead in older patients",
                "Osteophytes, aortic calcification, and degenerative disease falsely elevate apparent spinal BMD—spine DXA is less reliable in patients older than 65–70 years, especially men.",
                ref(
                    "Dual-Energy X-Ray Absorptiometry",
                    "Spine BMD measurements can be useful; however, in older women and especially men, they can be confounded by osteophytes, aortic calcification, degenerative disease, and other conditions that increase the apparent spinal BMD and therefore are less reliable in those older than 65 to 70 years.",
                ),
            ),
            note(
                f"{p}-n13",
                "Trabecular Bone Score",
                "How TBS refines FRAX fracture prediction",
                "TBS gray-scale texture analysis from spine DXA images reflects trabecular microarchitecture and, combined with BMD, improves fracture-risk estimation beyond FRAX or BMD alone.",
                ref(
                    "Trabecular Bone Score",
                    "The TBS has also been shown to enhance the power of fracture prediction obtained by the use of the algorithm FRAX, which was designed to estimate a 10-year probability of fracture.",
                ),
            ),
            note(
                f"{p}-n14",
                "Bone Turnover Markers",
                "Why PINP and CTX have limited standalone utility",
                "Formation (PINP, osteocalcin) and resorption (serum CTX) markers change rapidly with therapy but suffer high analytic and biologic variability—limiting independent fracture prediction.",
                ref(
                    "Bone Turnover Markers",
                    "However, all of them must take into account the high analytic variability (both within individuals and between assays and laboratories) for these markers.",
                ),
            ),
            note(
                f"{p}-n15",
                "Hip Fractures",
                "Why every hip fracture warrants osteoporosis workup",
                "Hip fracture carries 5–20% one-year mortality and high disability; it also predicts future fractures—mandating BMD assessment and treatment consideration.",
                ref(
                    "Hip Fractures",
                    "After a hip fracture, there is also a substantial risk of other fractures, including a second hip fracture, and it is therefore important that further assessment and possible treatment be considered in patients with fractures at the hip (and other sites).",
                ),
            ),
            note(
                f"{p}-n16",
                "Fracture Epidemiology",
                "How ethnicity and BMI modify fracture risk",
                "White individuals have highest hip-fracture risk; low BMI and sarcopenia increase risk independent of FRAX, while higher BMI is generally protective except in diabetes.",
                ref(
                    "Fracture Epidemiology",
                    "For hip fractures, White individuals are at higher risk, Hispanic and Asian people are at medium risk, and Black individuals are at lowest risk.",
                ),
            ),
            note(
                f"{p}-n17",
                "Clinical Risk Factors and Their Combination With BMD",
                "FRAX and multifactorial fracture risk",
                "Fracture risk is multifactorial; FRAX combines age, sex, weight, prior fracture, parental hip fracture, smoking, glucocorticoids, rheumatoid arthritis, secondary osteoporosis, alcohol, and optional BMD.",
                ref(
                    "Clinical Risk Factors and Their Combination With BMD",
                    "The most widely used and available is the FRAX fracture risk assessment tool, which includes the risk factors in Table 29.3 and has been implemented with country-specific versions for predicting risk of hip and major osteoporotic fractures.",
                ),
            ),
            note(
                f"{p}-n18",
                "Estrogen",
                "Menopause bone loss via RANKL",
                "Estrogen withdrawal increases RANKL (with IL-6, TNF, IL1) and uncouples remodeling—resorption outpaces formation because formation requires a longer, multi-step process.",
                ref(
                    "Estrogen",
                    "RANKL has been identified as a major regulator of osteoclast differentiation, and increases (both locally and systemically) likely contribute to the rapid increase in osteoclastogenesis after estrogen withdrawal.",
                ),
            ),
            note(
                f"{p}-n19",
                "Age-Related Bone Loss",
                "Calcium, vitamin D, and secondary hyperparathyroidism",
                "Elderly low calcium intake and 25(OH)D <20 ng/mL drive secondary hyperparathyroidism; PTH stimulates resorption but often fails to enhance formation—accelerating uncoupled bone loss.",
                ref(
                    "Age-Related Bone Loss",
                    "If vitamin D intake is also suboptimal and serum levels of 25-hydroxyvitamin D are less than 20 ng/mL or 50 nmol/L, secondary hyperparathyroidism may occur, although there are other causes in the elderly for increases in PTH, including a low glomerular filtration rate and low calcium intake.",
                ),
            ),
            note(
                f"{p}-n20",
                "Glucocorticoid-Induced Bone Loss",
                "Glucocorticoid effects on RANKL, OPG, and marrow fat",
                "Glucocorticoids increase RANKL and decrease OPG, suppress osteoblast precursors, and shift marrow stromal cells toward adipocytes—producing rapid uncoupled trabecular loss.",
                ref(
                    "Glucocorticoid-Induced Bone Loss",
                    "Besides the indirect suppressive effects of glucocorticoids on the hypothalamic-gonadal axis and inhibition of calcium absorption in the gut as a result of impaired 1,25(OH)2D production, high doses of steroids can stimulate osteoclastogenesis, increase RANKL production, and decrease OPG.",
                ),
            ),
            note(
                f"{p}-n21",
                "Osteoporosis Associated With Diabetes Mellitus",
                "The type 2 diabetes fracture paradox",
                "T2DM preserves or increases BMD yet raises fracture risk at any given BMD—bone quality (microarchitecture, AGE-modified collagen, reduced turnover) dominates over quantity.",
                ref(
                    "Osteoporosis Associated With Diabetes Mellitus",
                    "Bone mass is preserved or increased in T2DM, although peripheral fractures are increased, meaning that bone quality instead of quantity is the primordial mechanism affecting bone strength in this disorder.",
                ),
            ),
            note(
                f"{p}-n22",
                "Approach to Management of Osteoporosis",
                "Fracture liaison services",
                "A minimal-trauma fracture should trigger comprehensive risk assessment including DXA; fracture liaison services have expanded rapidly to close the secondary-prevention gap.",
                ref(
                    "Approach to Management of Osteoporosis",
                    "In addition, there is a growing appreciation that the occurrence of a fracture, particularly one due to minimal trauma, should be a signal for more comprehensive risk assessment, including BMD, and has led to the explosion in development of fracture liaison services over the past 5 years and the emphasis on their importance by many groups.",
                ),
            ),
            note(
                f"{p}-n23",
                "Diet",
                "Calcium and vitamin D targets in elders",
                "Meta-analyses support 1200 mg calcium with >800 IU vitamin D for modest BMD gain and nonvertebral fracture reduction; IOM recommends 800 IU/day vitamin D for adults >70 years.",
                ref(
                    "Diet",
                    "a recent meta-analysis of calcium and vitamin D intervention trials demonstrated a consistent, albeit small, increase in BMD and a reduction in nonvertebral fractures when 1200 mg of calcium was combined with more than 800 units of vitamin D.",
                ),
            ),
            note(
                f"{p}-n24",
                "Physical Activity",
                "Fall prevention as osteoporosis management",
                "Because falls cause most fragility fractures, muscle strengthening, balance retraining, home hazard review, and psychotropic withdrawal reduce fall risk and belong in every osteoporosis plan.",
                ref(
                    "Physical Activity",
                    "A meta-analysis by the Cochrane Review Group demonstrated that muscle strengthening, balance retraining, home hazard assessment, withdrawal of psychotropic medications, and use of a multidisciplinary risk factor assessment program are beneficial in protecting against falls.",
                ),
            ),
            note(
                f"{p}-n25",
                "Antiresorptive Agents",
                "Atypical femur fracture and ONJ at osteoporosis doses",
                "At antiresorptive doses for osteoporosis, atypical femur fractures and osteonecrosis of the jaw are very uncommon (ONJ estimated <1 per 100,000)—far outweighed by fracture prevention.",
                ref(
                    "Antiresorptive Agents",
                    "The prevalence of ONJ is very low when bisphosphonates are used in the doses needed to treat osteoporosis.",
                ),
            ),
            note(
                f"{p}-n26",
                "Antiresorptive Agents",
                "Denosumab discontinuation rebound",
                "Unlike bisphosphonates, denosumab does not persist in bone; stopping therapy causes rebound resorption and increased vertebral fracture risk—transition to another antiresorptive is advised.",
                ref(
                    "Antiresorptive Agents",
                    "In fact, discontinuation of denosumab can lead to a rebound increase in bone resorption and an increase in vertebral fractures.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Dual-Energy X-Ray Absorptiometry",
                "A 72-year-old man has lumbar spine T-score -1.8 but total hip T-score -2.7 after minimal-trauma vertebral compression on chest radiograph. He has no glucocorticoid use. Best DXA-based diagnosis?",
                [
                    "Normal BMD at both sites",
                    "Osteopenia only—hip value is artifact",
                    "Osteoporosis based on hip T-score ≤-2.5",
                    "Osteomalacia—DXA cannot be interpreted",
                ],
                2,
                "Use the lowest qualifying site among total hip, femoral neck, or lumbar spine; spine may be falsely high in elderly men from degenerative changes.",
                ref(
                    "Dual-Energy X-Ray Absorptiometry",
                    "Clinically, three regions are usually used for diagnosis: BMD at the total hip, the femoral neck, and the lumbar spine.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Clinical Risk Factors and Their Combination With BMD",
                "A 68-year-old woman has femoral neck T-score -1.9, prior wrist fracture at 60, mother with hip fracture, and 10 pack-year smoking. FRAX 10-year major osteoporotic fracture risk is 22%. Next step?",
                [
                    "Reassure—T-score above -2.5 needs no therapy",
                    "Calcium alone without pharmacotherapy",
                    "Initiate osteoporosis pharmacotherapy per guideline thresholds",
                    "Repeat DXA in 10 years regardless of risk",
                ],
                2,
                "Prior fragility fracture and elevated FRAX justify treatment even when BMD is osteopenic—not osteoporosis by T-score alone.",
                ref(
                    "Approach to Management of Osteoporosis",
                    "In these guidelines, FRAX is used for patients with BMD that is low but not in the osteoporotic range.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Trabecular Bone Score",
                "Postmenopausal woman: lumbar T-score -2.0, normal hip BMD, but TBS shows degraded microarchitecture. FRAX underestimates risk. Best adjustment?",
                [
                    "Ignore TBS—BMD is sufficient",
                    "Incorporate TBS into FRAX or downgrade T-score per IOF guidance for diabetes-like states",
                    "Order bone biopsy before any decision",
                    "Start high-dose vitamin D analogue routinely",
                ],
                1,
                "TBS independently predicts fracture and enhances FRAX; degraded TBS signals fragility beyond areal BMD.",
                ref(
                    "Trabecular Bone Score",
                    "Moreover, it demonstrated that the combination of BMD with TBS assessment provides a better estimate of fracture risk than either evaluation by itself.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Bone Turnover Markers",
                "After starting oral bisphosphonate, which marker pair best documents early antiresorptive response if drawn fasting morning serum?",
                [
                    "Serum calcium and phosphate",
                    "PINP rise and CTX rise",
                    "PINP fall or stable with CTX fall",
                    "PTH and 25(OH)D only",
                ],
                2,
                "Antiresorptives suppress resorption (CTX ↓) within weeks; formation markers (PINP) may fall later—use consistent preanalytic conditions.",
                ref(
                    "Bone Turnover Markers",
                    "Bone resorption has traditionally been assessed with urinary N-terminal cross-linked telopeptide (NTX) but is now more commonly assessed by serum C-terminal cross-linked telopeptide (CTX), both being collagen cross-linked peptides assessed with antibodies (Table 29.2).",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Osteoporosis Associated With Diabetes Mellitus",
                "A 65-year-old woman with T2DM, BMI 34, lumbar T-score -0.5, and prior low-trauma ankle fracture. FRAX is low. Most appropriate fracture-risk approach?",
                [
                    "No treatment—BMD is normal",
                    "Adjust FRAX/TBS per IOF T2DM recommendations and consider therapy",
                    "Teriparatide only—bisphosphonates contraindicated in diabetes",
                    "DXA wrist as sole management guide",
                ],
                1,
                "T2DM increases fracture risk at given BMD; FRAX underestimates risk—TBS and FRAX adjustments (T-score -0.5, +10 years age, or RA flag) are recommended.",
                ref(
                    "Osteoporosis Associated With Diabetes Mellitus",
                    "the Bone and Diabetes Working Group of the International Osteoporosis Foundation (IOF) proposed that one of the following adaptations can be used to correct the estimation of fracture by FRAX: (1) decrease the T-score obtained in the DXA exam by 0.5, (2) increase the age by 10 years, or (3) consider that the patient has rheumatoid arthritis.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Glucocorticoid-Induced Bone Loss",
                "A 58-year-old woman on prednisone 15 mg daily for polymyalgia rheumatica for 4 months has new thoracic vertebral fracture; spine T-score -1.2. Best initial bone-specific therapy?",
                [
                    "Calcium/vitamin D only—BMD is not osteoporotic",
                    "Bisphosphonate (e.g., alendronate or risedronate) plus Ca/vit D",
                    "Observation until prednisone stopped",
                    "Romosozumab without antiresorptive follow-up",
                ],
                1,
                "Glucocorticoid-induced osteoporosis causes fractures despite near-normal BMD; bisphosphonates are approved for prevention/treatment with adequate Ca/vit D.",
                ref(
                    "Glucocorticoid-Induced Bone Loss",
                    "Indeed, in this syndrome, baseline BMD is not predictive of fractures and can often be normal even in the presence of ongoing resorption and recurrent fractures.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Antiresorptive Agents",
                "A postmenopausal woman with severe osteoporosis and GERD cannot tolerate oral bisphosphonates. eGFR 55 mL/min. Best antiresorptive?",
                [
                    "IV zoledronate 5 mg once yearly (over ≥15 min) with Ca/vit D",
                    "Denosumab is contraindicated with eGFR <60",
                    "Raloxifene as sole therapy for hip fracture prevention",
                    "Calcitonin as first-line antifracture therapy",
                ],
                0,
                "IV zoledronate is effective when oral therapy fails; use caution if GFR <30 and infuse over adequate time to limit renal risk.",
                ref(
                    "Antiresorptive Agents",
                    "Zoledronate is also approved for the prevention and treatment of osteoporosis. It is administered as a single intravenous infusion over 15 minutes (5 mg) once yearly.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Antiresorptive Agents",
                "After 3 years of denosumab, a patient wishes to stop injections. What minimizes vertebral fracture rebound?",
                [
                    "Stop denosumab abruptly—effects wear off safely",
                    "Transition to oral or IV bisphosphonate after last denosumab dose",
                    "Switch to raloxifene alone",
                    "No follow-up antiresorptive needed if BMD improved",
                ],
                1,
                "Denosumab discontinuation causes rebound high turnover and vertebral fractures; another antiresorptive should follow.",
                ref(
                    "Antiresorptive Agents",
                    "This effect suggests that women coming off denosumab should take another antiresorptive.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Anabolic Agents",
                "A 70-year-old woman with multiple vertebral fractures and T-score -3.5 has not had prior osteoporosis drug therapy. Best sequence per pivotal romosozumab trials?",
                [
                    "Romosozumab 12 months then antiresorptive (e.g., alendronate or denosumab)",
                    "Romosozumab indefinitely without follow-on therapy",
                    "Alendronate for 2 years then romosozumab alone",
                    "Concurrent daily teriparatide and weekly alendronate from day 1",
                ],
                0,
                "FDA-approved romosozumab course is 12 monthly doses followed by antiresorptive to maintain gains and limit rebound.",
                ref(
                    "Anabolic Agents",
                    "In the second clinical trial, the authors defined the following design: monthly subcutaneous romosozumab (210 mg) or weekly oral alendronate (70 mg) administered in a blinded fashion for 12 months, followed by open-label alendronate in both groups.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Anabolic Agents",
                "Teriparatide and alendronate started together in treatment-naïve severe osteoporosis. Compared with teriparatide alone, BMD gain is:",
                [
                    "Synergistically greater at spine and hip",
                    "Not greater—combination is not additive",
                    "Greater only at cortical sites",
                    "Greater only if denosumab replaces alendronate on day 1",
                ],
                1,
                "Concurrent PTH plus bisphosphonate does not exceed PTH-alone BMD gains; sequencing matters for anabolic effect.",
                ref(
                    "Anabolic Agents",
                    "PTH plus bisphosphonates initiated together do not raise BMD more than PTH alone in either men or women.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Anabolic Agents",
                "After completing 24 months of teriparatide, which strategy prevents the typical 3–4% first-year BMD loss?",
                [
                    "No further therapy—anabolic effect is permanent",
                    "Start an antiresorptive agent at PTH cessation",
                    "Repeat teriparatide immediately without interval",
                    "Calcium supplementation alone",
                ],
                1,
                "Post-PTH bone loss is prevented by following with antiresorptive therapy.",
                ref(
                    "Anabolic Agents",
                    "This posttreatment effect is prevented by adding an antiresorptive agent once PTH is stopped.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Vertebral Fractures",
                "Incidental moderate wedge deformity on chest radiograph in a 67-year-old woman without trauma. Next step?",
                [
                    "Ignore—vertebral fractures require symptoms",
                    "DXA and fracture risk assessment; consider treatment",
                    "Emergency MRI only—no BMD needed",
                    "Teriparatide before any BMD measurement",
                ],
                1,
                "Vertebral fractures are hallmarks of osteoporosis, increase future fracture risk 5–10×, and warrant DXA and treatment consideration even if asymptomatic.",
                ref(
                    "Vertebral Fractures",
                    "Therefore, like hip fractures, they should lead to further assessment (e.g., dual-energy x-ray absorptiometry [DXA]) and consideration of osteoporosis prevention and treatment.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Wrist Fractures",
                "A 58-year-old perimenopausal woman sustains a Colles fracture from a standing-height fall. BMD not yet done. Best counseling?",
                [
                    "Isolated wrist injury—no systemic bone evaluation needed",
                    "Wrist fracture signals systemic fragility; evaluate and treat osteoporosis risk",
                    "Only men need evaluation after wrist fracture",
                    "Wrist fractures never predict hip fracture",
                ],
                1,
                "Untreated wrist fractures predict high risk for future osteoporotic fractures at other sites.",
                ref(
                    "Wrist Fractures",
                    "Untreated wrist fractures predict a high risk for more osteoporotic fractures at other skeletal sites; they are symbolic of systemic skeletal fragility.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Overview of Remodeling",
                "Romosozumab mechanism at the osteocyte–osteoblast level?",
                [
                    "Activates RANKL to stimulate osteoclasts",
                    "Neutralizes sclerostin, disinhibiting Wnt/LRP5/6 and increasing bone formation",
                    "Blocks PTH receptor signaling",
                    "Inhibits all Wnt pathways permanently",
                ],
                1,
                "Romosozumab is a humanized anti-sclerostin antibody that releases Wnt-mediated osteoblast stimulation and reduces RANKL indirectly.",
                ref(
                    "Monoclonal Antibodies to Sclerostin",
                    "sclerostin is produced by osteocytes and inhibits bone formation by blocking canonical Wnt signaling.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Osteoclast Differentiation and Function",
                "A researcher notes OPG knockout mice phenotype. Expected skeletal finding?",
                [
                    "Osteopetrosis from absent osteoclasts",
                    "Osteoporosis from unchecked RANKL-driven resorption",
                    "Normal bone mass",
                    "High bone mass like SOST mutation",
                ],
                1,
                "OPG-deficient mice have osteoporosis; OPG overexpression increases bone mass—confirming RANKL/OPG balance controls resorption.",
                ref(
                    "Osteoclast Differentiation and Function",
                    "Mice that are deficient in OPG have osteoporosis, whereas mice that overexpress OPG have increased bone mass.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Estrogen",
                "Early postmenopausal woman with rapid BMD decline. Which cytokine axis best explains uncoupled resorption?",
                [
                    "Estrogen withdrawal → ↑RANKL and pro-resorptive cytokines with formation lag",
                    "Estrogen directly stimulates osteoblasts only",
                    "Estrogen blocks all osteoclast RANK expression",
                    "Estrogen increases OPG exclusively",
                ],
                0,
                "Menopause shifts RANKL/OPG toward resorption; formation cannot match the faster resorptive phase of the remodeling cycle.",
                ref(
                    "Estrogen",
                    "Enhanced bone resorption eventually leads to bone loss from estrogen deprivation because bone formation rates cannot keep up with the high rates of bone resorption (see Fig. 29.15).",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Diet",
                "Nursing-home resident, 84 years, hip fracture. 25(OH)D 14 ng/mL. Evidence-based supplementation to reduce future fractures?",
                [
                    "Vitamin D alone 400 IU daily is sufficient",
                    "Calcium 1200 mg/day with vitamin D ≥800 IU/day",
                    "Avoid calcium—WHI showed only harm",
                    "Monthly 500,000 IU vitamin D bolus",
                ],
                1,
                "Meta-analyses support 1200 mg calcium with >800 IU vitamin D in high-risk elders; avoid mega-bolus vitamin D (increases falls/fractures).",
                ref(
                    "Diet",
                    "At least one meta-analysis suggests that 800 IU/day of vitamin D plus 1200 mg of calcium per day is needed to reduce hip fractures by about 10%.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Antiresorptive Agents",
                "Long-term oral bisphosphonate patient reports prodromal thigh pain and lateral cortical thickening on radiograph. Best management?",
                [
                    "Continue bisphosphonate—increase dose",
                    "Evaluate for atypical femur fracture; consider drug holiday or prophylactic fixation",
                    "Switch to calcitonin only",
                    "Ignore—thigh pain is never bisphosphonate-related",
                ],
                1,
                "Prodromal thigh pain and cortical beaking signal atypical femur fracture risk with prolonged bisphosphonate use.",
                ref(
                    "Antiresorptive Agents",
                    "Prodromal symptoms of hip or thigh pain and associated cortical thickening or beaking in the shaft of the proximal femur are risk indicators of these fractures, which, with minimal trauma, can have devastating consequences in terms of quality of life and mobility.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Antiresorptive Agents",
                "Postmenopausal woman with osteoporosis needs antiresorptive but has history of DVT on estrogen. Best agent class?",
                [
                    "Raloxifene—lowest thrombosis risk",
                    "Raloxifene also increases DVT risk like estrogen",
                    "High-dose nasal calcitonin as sole therapy",
                    "Strontium ranelate first-line in the U.S.",
                ],
                1,
                "Raloxifene reduces vertebral fractures but carries increased DVT risk—problematic with prior thrombosis; bisphosphonate or denosumab may be preferred.",
                ref(
                    "Antiresorptive Agents",
                    "Hot flashes, leg cramps, and a greater risk of deep venous thrombosis can occur with raloxifene therapy.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Pathogenesis of Osteoporosis",
                "Elderly patient with recurrent falls, not on bone drugs. Which intervention addresses both falls and bone?",
                [
                    "Bisphosphonate without fall assessment",
                    "Multifactorial fall-prevention program plus osteoporosis evaluation",
                    "Bed rest to prevent fractures",
                    "Hip protectors alone replace pharmacotherapy",
                ],
                1,
                "Falls are a primary cause of osteoporotic fractures; prevention mandates fall reduction alongside bone-targeted therapy.",
                ref(
                    "Pathogenesis of Osteoporosis",
                    "Although the primary focus of this chapter is on the endocrine and metabolic aspects of this disease, it should be noted that falls cause fractures and that one of the primary causes of osteoporotic fractures is falling.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Fracture Epidemiology",
                "Compared with women, men at the same age have hip fracture incidence:",
                [
                    "Identical",
                    "Approximately 50% lower",
                    "Threefold higher",
                    "Only higher after age 90",
                ],
                1,
                "Age-specific hip and spine fracture risk in men parallels women but at roughly half the rate—gender is a key epidemiologic determinant.",
                ref(
                    "Fracture Epidemiology",
                    "However, importantly, the age-specific risk of hip and spine fractures in men is much lower than that in women (approximately 50%), highlighting the key role of gender in the epidemiology of osteoporotic fractures.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Anabolic Agents",
                "Patient with severe postmenopausal osteoporosis and eGFR 25 mL/min needs anabolic therapy. Consideration?",
                [
                    "Teriparatide is absolutely contraindicated in all CKD",
                    "Teriparatide may be used with caution; avoid bisphosphonate if GFR <30",
                    "Romosozumab is first choice with recent MI",
                    "Abaloparatide requires daily IV infusion",
                ],
                1,
                "Teriparatide is an option in moderate CKD; zoledronate should not be used if GFR <30; romosozumab is avoided with recent cardiovascular events.",
                ref(
                    "Antiresorptive Agents",
                    "In addition, it should not be used in patients with a reduced glomerular filtration rate (<30 mL/minute) and should be used with caution in the elderly.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Approach to Management of Osteoporosis",
                "Woman age 66, no fractures, femoral neck T-score -2.6. Per NOF-style guidance, best approach?",
                [
                    "Defer treatment until fracture occurs",
                    "Consider pharmacotherapy—T-score ≤-2.5 is treatment indication",
                    "FRAX must be low to treat osteoporosis by BMD",
                    "Calcium alone is adequate for T-score -2.6",
                ],
                1,
                "T-score ≤-2.5 or hip/spine fragility fracture are clear treatment indications in major U.S. guidelines.",
                ref(
                    "Approach to Management of Osteoporosis",
                    "which strongly emphasize that patients with a BMD T-score below -2.5 or a history of hip or spine fracture be considered for treatment.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Historical Context",
                "A resident cites declining U.S. fracture rates since 1995 but notes recent reversal. Best explanation for undertreatment?",
                [
                    "No effective drugs exist",
                    "Emphasis on rare AEs overshadowing proven fracture prevention benefits",
                    "DXA is unavailable worldwide",
                    "Osteoporosis only affects trabecular bone without clinical impact",
                ],
                1,
                "The treatment crisis reflects underprescription driven by overstated rare risks (atypical femur, ONJ) versus large population benefit.",
                ref(
                    "Historical Context",
                    "Although the incidence of adverse events is rare, their significance has served to understate the vast fracture prevention benefits enjoyed by the majority of patients, leading to physician underprescription and patient reluctance to use the medication.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Bone Remodeling and Its Regulation",
                "In the healthy adult remodeling cycle, typical duration of resorption vs formation phases?",
                [
                    "Resorption ~10–13 days; formation up to ~3 months",
                    "Both phases complete in 24 hours",
                    "Formation is always shorter than resorption",
                    "Resorption takes 6 months; formation 1 week",
                ],
                0,
                "Resorption is brief (~2 weeks) while matrix formation and mineralization extend months—explaining transient uncoupling after menopause or antiresorptive therapy.",
                ref(
                    "Overview of Remodeling",
                    "In general, resorption takes only 10 to 13 days, whereas formation is much more deliberate and can take upward of 3 months (see Fig. 29.2).",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Anabolic Agents",
                "Abaloparatide vs teriparatide in ACTIVE trial: notable advantage of abaloparatide?",
                [
                    "Lower lumbar BMD gain",
                    "Significant reduction in nonvertebral fractures vs placebo (not seen with teriparatide in that comparison)",
                    "Higher hypercalcemia rate than teriparatide",
                    "Oral weekly dosing",
                ],
                1,
                "Abaloparatide reduced vertebral and nonvertebral fractures with less hypercalcemia than teriparatide in head-to-head analyses.",
                ref(
                    "Anabolic Agents",
                    "However, abaloparatide was associated with a significant reduction in nonvertebral fractures when compared with placebo—an effect not observed in teriparatide therapy.",
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
                "Osteoporosis pharmacotherapy typically requires daily dosing like most other chronic disease medications.",
                False,
                "Weekly, monthly, biannual, or annual dosing can suffice—unlike many chronic therapies.",
                ref(
                    "KEY POINTS",
                    "Unlike available therapeutic options for other chronic disorders, osteoporosis therapy is unique in that weekly, monthly, biannual, or even annual dosing may be sufficient to accomplish successful treatment.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Dual-Energy X-Ray Absorptiometry",
                "A T-score between -1.0 and -2.5 defines low bone mass (osteopenia).",
                True,
                "WHO/IOF classification: osteopenia is >1 SD and <2.5 SD below young-adult mean.",
                ref(
                    "Dual-Energy X-Ray Absorptiometry",
                    "Low bone mass (osteopenia)",
                ),
            ),
            tf(
                f"{p}-t3",
                "Dual-Energy X-Ray Absorptiometry",
                "DXA is most often performed at the spine and hip for osteoporosis assessment.",
                True,
                "Spine and hip are standard sites; distal radius and whole body are optional.",
                ref(
                    "Dual-Energy X-Ray Absorptiometry",
                    "DXA is most often performed at the spine and hip, although other sites (whole body, distal radius) can also be assessed.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Bone Turnover Markers",
                "Serum CTX is now more commonly used than urinary NTX to assess bone resorption.",
                True,
                "Collagen cross-linked telopeptides in serum (β-CTX) largely replaced urinary NTX in practice.",
                ref(
                    "Bone Turnover Markers",
                    "Bone resorption has traditionally been assessed with urinary N-terminal cross-linked telopeptide (NTX) but is now more commonly assessed by serum C-terminal cross-linked telopeptide (CTX), both being collagen cross-linked peptides assessed with antibodies (Table 29.2).",
                ),
            ),
            tf(
                f"{p}-t5",
                "Fracture Epidemiology",
                "Vertebral fractures are the most common radiographic manifestation of osteoporosis.",
                True,
                "Vertebral fractures outnumber hip and wrist fractures in aggregate prevalence.",
                ref(
                    "Vertebral Fractures",
                    "Vertebral fractures are the most common manifestation of osteoporosis.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Fracture Epidemiology",
                "Higher BMI is generally protective against hip and spine fractures.",
                True,
                "Greater adiposity, estrogen from fat, and cushioning on fall attenuate hip/spine fracture risk—low BMI is high risk.",
                ref(
                    "Fracture Epidemiology",
                    "In general, higher-BMI individuals are at lower risk of hip and spine fractures, owing to several factors, including a larger number of fat cells that produce greater amounts of estrogen, which is protective, and the higher amount of padding in higher-BMI patients, which produces a larger distribution of the forces in the event of a fall.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Osteoporosis Associated With Diabetes Mellitus",
                "Type 2 diabetes is consistently associated with low BMD and easy DXA-based fracture prediction.",
                False,
                "T2DM preserves or increases BMD while increasing fracture risk—quality, not quantity, is impaired.",
                ref(
                    "Osteoporosis Associated With Diabetes Mellitus",
                    "Bone mass is preserved or increased in T2DM, although peripheral fractures are increased, meaning that bone quality instead of quantity is the primordial mechanism affecting bone strength in this disorder.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Glucocorticoid-Induced Bone Loss",
                "Glucocorticoids increase RANKL and decrease OPG on osteoblastic cells.",
                True,
                "This paracrine shift stimulates osteoclastogenesis alongside direct osteoblast suppression.",
                ref(
                    "Glucocorticoid-Induced Bone Loss",
                    "high doses of steroids can stimulate osteoclastogenesis, increase RANKL production, and decrease OPG.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Diet",
                "The IOM recommends 800 IU/day of vitamin D for men and women older than 70 years.",
                True,
                "600 IU/day for younger adults; 800 IU/day for those >70 years.",
                ref(
                    "Diet",
                    "The IOM recommends an average intake of 600 IU/day, except for men and women older than 70 years, for which the IOM recommends 800 IU of vitamin D per day.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Antiresorptive Agents",
                "IV zoledronate for osteoporosis is given once yearly at 5 mg.",
                True,
                "Annual 5 mg IV infusion (≥15–60 min per label updates) is standard treatment dosing.",
                ref(
                    "Antiresorptive Agents",
                    "It is administered as a single intravenous infusion over 15 minutes (5 mg) once yearly.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Antiresorptive Agents",
                "Osteonecrosis of the jaw is common when bisphosphonates are used at standard osteoporosis doses.",
                False,
                "ONJ prevalence is very low at osteoporosis doses—higher with oncology dosing.",
                ref(
                    "Antiresorptive Agents",
                    "However, in patients with osteoporosis, the prevalence is estimated to be less than 1 in 100,000 patients exposed to oral or intravenous bisphosphonates who are otherwise healthy.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Anabolic Agents",
                "Starting teriparatide and alendronate together produces greater BMD gain than teriparatide alone.",
                False,
                "Concurrent initiation is not additive; sequencing strategies differ for denosumab combinations.",
                ref(
                    "Anabolic Agents",
                    "PTH plus bisphosphonates initiated together do not raise BMD more than PTH alone in either men or women.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Historical Context",
                "Since FDA approval of antiosteoporotic drugs beginning in 1995, U.S. fracture rates had only increased without interruption.",
                False,
                "Fracture rates declined for years before a recent reversal—the 'treatment crisis.'",
                ref(
                    "Historical Context",
                    "Since 1995, when U.S. Food and Drug Administration (FDA) approval for new antiosteoporotic drugs first began, there has been a significant decline in the rate of fracture in the U.S. population.",
                ),
            ),
        ]
    )

    # --- Assertion–Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Structure and Function of the Skeleton",
                "Assertion: Osteocytes initiate bone remodeling through canalicular signaling.",
                "Reason: Osteocytes are buried in mineralized matrix and lack receptors for PTH.",
                2,
                "Assertion true; reason false—osteocytes possess PTH receptors and metabolic activity.",
                ref(
                    "Collagen Degradation by Osteoblasts and Osteocytes",
                    "Osteocytes are terminally differentiated osteoblasts that are buried within the matrix of the skeleton but possess receptors for PTH and have metabolic activity.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Osteoclast Differentiation and Function",
                "Assertion: Mice deficient in RANKL do not form osteoclasts and develop osteopetrosis.",
                "Reason: RANKL is the principal stimulator of osteoclast formation from osteoblast-lineage cells.",
                0,
                "Both true and causally linked—RANKL is essential for osteoclastogenesis.",
                ref(
                    "Osteoclast Differentiation and Function",
                    "Mice that are deficient in RANKL do not form osteoclasts and have osteopetrosis.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Overview of Remodeling",
                "Assertion: Uncoupled remodeling with resorption exceeding formation causes bone loss.",
                "Reason: During peak bone acquisition, formation always exceeds resorption.",
                1,
                "Both true but reason does not explain assertion—peak acquisition is a different physiologic state.",
                ref(
                    "Overview of Remodeling",
                    "When the remodeling process is uncoupled so that resorption exceeds formation, bone is lost.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Dual-Energy X-Ray Absorptiometry",
                "Assertion: DXA BMD strongly predicts future fracture risk.",
                "Reason: DXA captures all aspects of bone quality including microarchitecture.",
                2,
                "Assertion true; reason false—DXA measures areal BMD, not full bone quality.",
                ref(
                    "Dual-Energy X-Ray Absorptiometry",
                    "Most likely, these events are related to bone quality, a component not captured by DXA measurements.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Vertebral Fractures",
                "Assertion: Vertebral fractures increase future vertebral fracture risk 5- to 10-fold.",
                "Reason: Vertebral fractures only occur after high-energy trauma.",
                2,
                "Assertion true; reason false—vertebral fragility fractures often follow minimal or no trauma.",
                ref(
                    "Vertebral Fractures",
                    "Vertebral fractures increase the future risk of additional vertebral fractures by 5 to 10 times and are associated with a much higher risk of nonvertebral fractures, including hip fractures.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Estrogen",
                "Assertion: Estrogen deprivation accelerates bone resorption via increased RANKL.",
                "Reason: Bone formation immediately and fully compensates after menopause in all women.",
                2,
                "Assertion true; reason false—formation cannot keep pace with accelerated resorption.",
                ref(
                    "Estrogen",
                    "Enhanced bone resorption eventually leads to bone loss from estrogen deprivation because bone formation rates cannot keep up with the high rates of bone resorption (see Fig. 29.15).",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Glucocorticoid-Induced Bone Loss",
                "Assertion: Glucocorticoid-induced osteoporosis can fracture patients with normal BMD.",
                "Reason: Glucocorticoids shift marrow stromal cells toward adipocytes and away from osteoblasts.",
                0,
                "Both true and linked—marrow fat expansion and uncoupled remodeling weaken bone despite preserved BMD.",
                ref(
                    "Glucocorticoid-Induced Bone Loss",
                    "Indeed, in this syndrome, baseline BMD is not predictive of fractures and can often be normal even in the presence of ongoing resorption and recurrent fractures.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Osteoporosis Associated With Diabetes Mellitus",
                "Assertion: T2DM patients have higher fracture risk at the same BMD as normoglycemic individuals.",
                "Reason: T2DM uniformly causes severe osteopenia on DXA.",
                2,
                "Assertion true; reason false—BMD is normal or high in T2DM.",
                ref(
                    "Osteoporosis Associated With Diabetes Mellitus",
                    "At the same level of BMD and age, individuals with T2DM have increased fracture risk when compared with normoglycemic individuals (Fig. 29.21).",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Antiresorptive Agents",
                "Assertion: Denosumab must be given every 6 months to maintain efficacy.",
                "Reason: Denosumab binds hydroxyapatite and persists in bone for decades like bisphosphonates.",
                2,
                "Assertion true; reason false—denosumab does not persist in skeleton; stopping causes rebound.",
                ref(
                    "Antiresorptive Agents",
                    "Unlike bisphosphonates, denosumab does not persist in the skeleton and hence needs to be administered once every 6 months to maintain its efficacy.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Anabolic Agents",
                "Assertion: Intermittent PTH (teriparatide) increases bone formation and reduces fractures.",
                "Reason: Continuous high PTH levels, as in primary hyperparathyroidism, always build cortical bone mass.",
                2,
                "Assertion true; reason false—chronic PTH excess causes cortical bone loss.",
                ref(
                    "Anabolic Agents",
                    "However, chronically high levels of PTH cause bone loss in the cortical compartment, as noted for primary and secondary hyperparathyroidism.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Monoclonal Antibodies to Sclerostin",
                "Assertion: Romosozumab reduces vertebral fractures compared with alendronate in clinical trials.",
                "Reason: Romosozumab works solely by increasing osteoclast activity.",
                2,
                "Assertion true; reason false—romosozumab increases formation and decreases resorption via anti-sclerostin/Wnt effects.",
                ref(
                    "Anabolic Agents",
                    "The romosozumab/alendronate group showed a 48% and 19% reduction, respectively, in incident vertebral and nonvertebral fractures compared with the alendronate-only group.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Historical Context",
                "Assertion: Effective osteoporosis drugs exist but remain underused.",
                "Reason: Clinical awareness for diagnosing and treating osteoporosis remains underdeveloped.",
                0,
                "Both true and causally linked—underawareness limits uptake despite available technology and therapies.",
                ref(
                    "KEY POINTS",
                    "Curiously, clinical awareness for diagnosing and treating osteoporosis remains underdeveloped; unfortunately, few individuals benefit from the level of knowledge and technology available to diagnose and manage the disorder.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "29",
        "title": "Osteoporosis: Basic and Clinical Aspects",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Francisco J.A. de Paula, Dennis M. Black, Paul D. Miller, and Clifford J. Rosen",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_29_Basic_and_Clinical_Aspects.md",
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
