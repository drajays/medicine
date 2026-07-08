#!/usr/bin/env python3
"""Generate Williams 15e module w15-38 — Complications of Diabetes Mellitus."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-38"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-38_Complications_of_Diabetes_Mellitus.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why chronic hyperglycemia drives microvascular complications",
                "Hyperglycemia is the main risk factor for diabetic retinopathy and nephropathy; susceptibility varies by heritable factors and metabolic memory from epigenetic stem-cell changes.",
                ref(
                    "KEY POINTS",
                    "Chronic hyperglycemia is the main risk factor for diabetic retinopathy (DR) and nephropathy.",
                ),
            ),
            note(
                f"{p}-n2",
                "Clinical Overview of Diabetes Complications",
                "How DCCT and UKPDS link glycemia to complication risk",
                "Large prospective studies in T1D (DCCT) and T2D (UKPDS) demonstrate a continuous relationship between glycemia and development and progression of microvascular complications.",
                ref(
                    "Clinical Overview of Diabetes Complications",
                    "A strong relationship between hyperglycemia and diabetic retinopathy (DR) and nephropathy has been demonstrated in both T1D and T2D large prospective clinical studies—the Diabetes Control and Complications Trial (DCCT) and the United Kingdom Prospective Diabetes Study (UKPDS), respectively.",
                ),
            ),
            note(
                f"{p}-n3",
                "Clinical Overview of Diabetes Complications",
                "Why metabolic memory persists after glycemic improvement",
                "Former high HbA1c effects on retinopathy, nephropathy, neuropathy, and MACE can persist for years after HbA1c is lowered—termed metabolic memory (DCCT/EDIC) or legacy effect (UKPDS).",
                ref(
                    "Clinical Overview of Diabetes Complications",
                    "For each complication of diabetes, adverse effects of former high hemoglobin  $ A_{1c} $ ( $ HbA_{1c} $) levels can persist for years after  $ HbA_{1c} $ values have been lowered (called metabolic memory by the DCCT and long-term observational follow-up Epidemiology of Diabetes Interventions and Complications [EDIC] study investigators and a legacy effect by the UKPDS investigators).",
                ),
            ),
            note(
                f"{p}-n4",
                "Clinical Overview of Diabetes Complications",
                "How ROS overproduction links complication mechanisms",
                "Prolonged increases in reactive oxygen species production in retina, kidney, nerve, arteries, and heart are critical for diabetic complications; mitochondrial superoxide dismutase or catalase overexpression prevents multiple complications in mouse models.",
                ref(
                    "Clinical Overview of Diabetes Complications",
                    "Many of the multiple mechanisms discussed in this section share a common concept: prolonged increases in reactive oxygen species (ROS) production in cells are critical for the development of diabetic complications in the retina, kidney, peripheral nerve, arteries, and heart.",
                ),
            ),
            note(
                f"{p}-n5",
                "Increased Aldose Reductase Substrate Conversion",
                "Why the polyol pathway role is nuanced",
                "Aldose reductase reduces glucose slowly but efficiently reduces lipid aldehydes; dog studies showed neuropathy prevention but failed retinopathy prevention, and clinical aldose reductase inhibitor trials showed no efficacy.",
                ref(
                    "Increased Aldose Reductase Substrate Conversion",
                    "In vivo studies of aldose reductase inhibition in a 5-year study in dogs showed prevention of diabetic neuropathy, but aldose reductase inhibition failed to prevent retinopathy or capillary basement membrane thickening in the retina, kidney, or muscle.",
                ),
            ),
            note(
                f"{p}-n6",
                "Increased Intracellular Formation of the Major Advanced Glycation End Products—Precursor Methylglyoxal",
                "How methylglyoxal damages diabetic tissues",
                "Methylglyoxal from glycolytic intermediates forms the major AGE epitope MG-H1, damages proteins intracellularly and in matrix, and activates RAGE/TLR4 inflammatory signaling.",
                ref(
                    "Increased Intracellular Formation of the Major Advanced Glycation End Products—Precursor Methylglyoxal",
                    "Methylglyoxal, formed by nonenzymatic fragmentation of the glycolytic intermediate triose phosphate, accounts for the majority of the hyperglycemia-induced increase in AGE adducts in diabetic tissues.",
                ),
            ),
            note(
                f"{p}-n7",
                "Activation of Protein Kinase C  $ \\alpha $,  $ \\beta $,  $ \\delta $, and  $ \\theta $",
                "Why PKC activation worsens microvascular disease",
                "Hyperglycemia increases diacylglycerol and activates PKCβ/δ (and other isoforms), promoting VEGF expression, endothelial permeability, matrix accumulation, and vascular inflammation in retina and glomeruli.",
                ref(
                    "Activation of Protein Kinase C  $ \\alpha $,  $ \\beta $,  $ \\delta $, and  $ \\theta $",
                    "Hyperglycemia primarily activates the β and δ isoforms of PKC, but increases in activity of PKCα and several other isoforms have also been found (Fig. 38.7).",
                ),
            ),
            note(
                f"{p}-n8",
                "Molecular Basis for Metabolic Memory",
                "How epigenetics may explain metabolic memory",
                "DCCT/EDIC DNA methylation at HbA1c-associated sites in hematopoietic stem cell enhancers may explain 70–85% of the association between mean DCCT HbA1c and EDIC complication risk.",
                ref(
                    "Molecular Basis for Metabolic Memory",
                    "Several associated methylation sites together explain as much as 70% to 85% of the association between mean DCCT HbA $ _{1c} $ and risk of complications during EDIC.",
                ),
            ),
            note(
                f"{p}-n9",
                "Diabetic Retinopathy and Other Ocular Complications of Diabetes",
                "Why anti-VEGF changed DME management",
                "Phase 3 trials established intravitreous anti-VEGF as standard of care for center-involved DME with visual impairment, substantially improving long-term visual acuity versus laser alone.",
                ref(
                    "KEY POINTS",
                    "Treatment of DME with intraocular injection of vascular endothelial growth factor (VEGF) inhibitors—medications that inhibit VEGF—reduces diabetes-induced abnormal retinal thickening and substantially improves long-term visual acuity outcomes.",
                ),
            ),
            note(
                f"{p}-n10",
                "Evaluation and Treatment of Proliferative Diabetic Retinopathy",
                "How PRP and anti-VEGF prevent PDR blindness",
                "Panretinal photocoagulation reduces severe vision loss from high-risk PDR to less than 4%; DRCR Protocol S showed ranibizumab noninferior to scatter laser with several advantages in selected patients.",
                ref(
                    "Evaluation and Treatment of Proliferative Diabetic Retinopathy",
                    "The ETDRS further demonstrated that panretinal laser photocoagulation applied when an eye approaches or just reaches high-risk PDR reduces the risk of severe vision loss to less than 4%.",
                ),
            ),
            note(
                f"{p}-n11",
                "Initial Ophthalmic Evaluation",
                "How to time diabetic eye screening",
                "Initial dilated examination begins 5 years after T1D diagnosis and immediately after T2D diagnosis because severe retinal disease can be present at T2D diagnosis.",
                ref(
                    "Initial Ophthalmic Evaluation",
                    "Thus, in patients older than 10 years, initial ophthalmic examination is recommended beginning 5 years after the diagnosis of T1D and immediately after diagnosis of T2D (see Fig. 38.28).",
                ),
            ),
            note(
                f"{p}-n12",
                "Follow-Up Ophthalmic Examination",
                "Why asymptomatic patients still need annual eye exams",
                "Sight-threatening retinopathy can occur without symptoms; even patients with no clinically evident DR require annual comprehensive ophthalmic examinations.",
                ref(
                    "Follow-Up Ophthalmic Examination",
                    "Because significant sight-threatening retinopathy can initially occur with no or minimal visual symptoms, patients with no clinically evident DR and no known ocular problems still require annual comprehensive ophthalmic examinations even if they are totally asymptomatic.",
                ),
            ),
            note(
                f"{p}-n13",
                "Screening for and Classification of Chronic Kidney Disease",
                "How to screen CKD in diabetes",
                "Screen from T2D diagnosis and ≥5 years after T1D diagnosis; measure UACR (≥2 of 3 abnormal samples) and annual eGFR using CKD-EPI; KDIGO classifies GFR and albuminuria jointly.",
                ref(
                    "Screening for and Classification of Chronic Kidney Disease",
                    "Guidelines suggest systematic screening, as part of the annual clinical review, from diagnosis in T2D and at least 5 years after diagnosis in T1D.",
                ),
            ),
            note(
                f"{p}-n14",
                "Diagnosis of Diabetic Nephropathy",
                "Why albuminuria defines classical diabetic nephropathy",
                "Persistent albuminuria above 300 mg/g with DR and no other kidney disease supports clinical diabetic nephropathy; moderately increased albuminuria replaced microalbuminuria per KDIGO.",
                ref(
                    "Diagnosis of Diabetic Nephropathy",
                    "Persistent albuminuria (above 300 mg/24 hour in a 24-hour collection or UACR above 300 mg/g creatinine) is the hallmark of diabetic nephropathy, which can be diagnosed clinically if the following additional criteria are fulfilled: presence of DR and absence of clinical or laboratory evidence of other kidney or renal tract disease.",
                ),
            ),
            note(
                f"{p}-n15",
                "Glucose-Lowering Medications With Organ Protection",
                "How SGLT2 inhibitors protect kidney and heart",
                "CREDENCE and DAPA-CKD demonstrated hard renal endpoints benefit independent of baseline eGFR and albuminuria; mechanisms include reduced intraglomerular pressure via tubuloglomerular feedback.",
                ref(
                    "Glucose-Lowering Medications With Organ Protection",
                    "The first study with hard renal endpoints (ESKD or significant loss of renal function) as a primary endpoint using an SGLT2i was Canagliflozin and Renal Events in Diabetes With Established Nephropathy Clinical Evaluation (CREDENCE), which showed a major benefit on kidney outcome and also on heart failure and MACEs in people with T2D, urine albumin creatinine ratio over 300 mg/g, and eGFR of 30 to 90 mL/min/1.73 m $ ^{2} $.",
                ),
            ),
            note(
                f"{p}-n16",
                "Blood Pressure Control in Prevention and Management of Diabetic Nephropathy",
                "Why RAS blockade is nephropathy backbone",
                "Once moderately or severely increased albuminuria is present, RAS inhibition reduces intraglomerular pressure; ACEi reduced progression to severely increased albuminuria (OR 0.35) in T1D meta-analysis.",
                ref(
                    "Blood Pressure in Type 1 Diabetes",
                    "Once moderately or severely increased albuminuria is present, inhibition of the RAS is the backbone of management of kidney disease because it reduces intraglomerular pressure.",
                ),
            ),
            note(
                f"{p}-n17",
                "Prevention and Management of Diabetic Nephropathy",
                "How finerenone adds organ protection in T2D CKD",
                "Nonsteroidal MRAs (finerenone) reduce kidney and heart disease progression in T2D with CKD on background RAS blockade with less hyperkalemia than steroidal MRAs.",
                ref(
                    "KEY POINTS",
                    "New nonsteroidal mineralocorticoid-receptor antagonists (MRAs) reduce the progression of kidney and heart disease in T2D with less risk of hyperkalemia.",
                ),
            ),
            note(
                f"{p}-n18",
                "Classification of Diabetic Distal Symmetric Polyneuropathy",
                "How Toronto criteria stage DSPN",
                "Possible DSPN needs symptoms or signs; probable DSPN needs symptoms plus signs; confirmed DSPN requires abnormal nerve conduction plus clinical features.",
                ref(
                    "Classification of Diabetic Distal Symmetric Polyneuropathy",
                    "3. Confirmed DSPN. The presence of an abnormality of nerve conduction and a symptom(s) or sign(s) of neuropathy confirm DSPN.",
                ),
            ),
            note(
                f"{p}-n19",
                "Treatment of Distal Symmetric Polyneuropathy",
                "Why glucose control differs for T1D vs T2D neuropathy",
                "Tight glucose control dramatically reduces DSPN incidence in T1D; in T2D intensive glucose alone is only modestly effective—metabolic syndrome components must also be modified.",
                ref(
                    "BOX 38.5 American Diabetes Association Recommendations for Distal Symmetric Polyneuropathy (DSPN)",
                    "Tight glucose control targeting near-normal glycemia in patients with type 1 diabetes dramatically reduces the incidence of distal symmetric polyneuropathy and is recommended for distal symmetric polyneuropathy prevention in type 1 diabetes.",
                ),
            ),
            note(
                f"{p}-n20",
                "Treatment of Distal Symmetric Polyneuropathy",
                "How to treat painful diabetic neuropathy",
                "FDA-approved options include pregabalin and duloxetine; three effective classes are α2δ ligands, SNRIs, and tricyclic antidepressants—titrate one class then add another if needed.",
                ref(
                    "Treatment of Painful Neuropathy",
                    "of painful DSPN: the voltage-gated  $ \\alpha_{2}\\delta $ ligands (pregabalin, gabapentin), the serotonin-norepinephrine reuptake inhibitors (duloxetine, venlafaxine), and the secondary amine tricyclic antidepressants (amitriptyline, nortriptyline, desipramine).",
                ),
            ),
            note(
                f"{p}-n21",
                "Clinical Features of Diabetic Autonomic Neuropathy",
                "Why cardiac autonomic neuropathy matters",
                "CAN associates with arrhythmia, silent MI, and early mortality; loss of heart rate variability from autonomic neuropathy increases cardiac event risk more than fourfold.",
                ref(
                    "KEY POINTS",
                    "Loss of heart rate variability as a result of autonomic neuropathy increases the risk of cardiac events more than fourfold.",
                ),
            ),
            note(
                f"{p}-n22",
                "Diabetic Heart Disease",
                "How T2D amplifies cardiovascular risk",
                "T2D approximately doubles adjusted cardiovascular risk; multifactorial reduction—statins, ACEi/ARB, and glucose-lowering agents with proven cardiovascular benefit—is required beyond glycemia alone.",
                ref(
                    "KEY POINTS",
                    "T2D substantially increases the risk of coronary artery disease, congestive heart failure, and stroke.",
                ),
            ),
            note(
                f"{p}-n23",
                "Diabetic Heart Disease",
                "Why GLP-1RAs and SGLT2is differ in CV outcomes",
                "GLP-1RAs have more consistent MACE subcomponent benefits including stroke; SGLT2is do not reduce stroke but lower heart failure hospitalization and cardiovascular death across ejection fractions.",
                ref(
                    "KEY POINTS",
                    "GLP-1RAs have more consistent benefits in reducing major adverse cardiovascular event (MACE) subcomponents, including stroke, than do SGLT2is, which do not reduce stroke.",
                ),
            ),
            note(
                f"{p}-n24",
                "Diabetic Heart Disease",
                "How microvascular disease signals macrovascular risk",
                "Presence of microvascular complications (retinopathy, nephropathy, neuropathy) predicts higher CVD risk better than cross-sectional traditional risk factors; ESC lists severe target-organ damage as very-high-risk equivalent.",
                ref(
                    "Presence of Microvascular Disease",
                    "The presence of microvascular diabetes complications signals excess vascular risk better than differences in usual risk factors measured at the same time, as demonstrated in the UK Clinical Practice Research Datalink.",
                ),
            ),
            note(
                f"{p}-n25",
                "The Diabetic Foot",
                "How to prevent diabetic foot amputation",
                "Neuropathy plus PAD drive ulcers; simple interventions reduce amputation up to 80%; management requires off-loading, antibiotics for infection, and timely revascularization within 2 weeks.",
                ref(
                    "KEY POINTS",
                    "Simple clinical interventions reduce amputation by up to 80%.",
                ),
            ),
            note(
                f"{p}-n26",
                "The Diabetic Foot",
                "Why annual comprehensive foot examination is essential",
                "Remove shoes and socks to inspect callus, deformity, and dry skin; 10-g monofilament loss plus PAD are strongest predictors of future ulceration.",
                ref(
                    "The Diabetic Foot",
                    "The most important message is for practitioners to have patients remove shoes and socks to examine feet for the presence of callus, deformity, muscle wasting, and dry skin, all of which are clearly visible on inspection.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Clinical Overview of Diabetes Complications",
                "A 28-year-old with T1D asks why intensive control during the DCCT still matters 15 years later despite similar current HbA1c. Best explanation?",
                [
                    "Metabolic memory—prior hyperglycemia-induced epigenetic changes persist in stem cells and differentiated tissues",
                    "Current HbA1c is irrelevant to all microvascular complications",
                    "UKPDS showed no legacy effect in T2D",
                    "ROS effects reverse completely within weeks of normoglycemia",
                ],
                0,
                "DCCT/EDIC and UKPDS show complication rates track prior glycemic exposure despite later identical HbA1c—metabolic memory/legacy effect.",
                ref(
                    "Clinical Overview of Diabetes Complications",
                    "effects of previous high  $ HbA_{1c} $ on poststudy retinopathy, nephropathy, neuropathy, and major adverse cardiovascular event (MACE)",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Clinical Overview of Diabetes Complications",
                "Which trial pair established the continuous relationship between glycemia and microvascular complications in T1D and T2D respectively?",
                [
                    "DCCT (T1D) and UKPDS (T2D)",
                    "ACCORD and ORIGIN only",
                    "CREDENCE and DAPA-CKD",
                    "DRS and ETDRS exclusively",
                ],
                0,
                "DCCT in T1D and UKPDS in T2D demonstrated hyperglycemia–microvascular complication relationships.",
                ref(
                    "Clinical Overview of Diabetes Complications",
                    "A strong relationship between hyperglycemia and diabetic retinopathy (DR) and nephropathy has been demonstrated in both T1D and T2D large prospective clinical studies—the Diabetes Control and Complications Trial (DCCT) and the United Kingdom Prospective Diabetes Study (UKPDS), respectively.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Increased Intracellular Formation of the Major Advanced Glycation End Products—Precursor Methylglyoxal",
                "A researcher notes increased MG-H1 in diabetic glomeruli despite stable hyperglycemia. Overexpressing which enzyme prevented diabetic kidney pathology in mice?",
                [
                    "Glyoxalase I (GLO1)",
                    "Aldose reductase",
                    "Protein kinase Cβ inhibitor only",
                    "Soluble epoxide hydrolase",
                ],
                0,
                "GLO1 overexpression in diabetic mouse kidneys prevented methylglyoxal modification, oxidative stress, and pathology despite unchanged hyperglycemia.",
                ref(
                    "Increased Intracellular Formation of the Major Advanced Glycation End Products—Precursor Methylglyoxal",
                    "in kidneys of diabetic mice, GLO1 overexpression completely prevents diabetes-induced increases in methylglyoxal modification of glomerular proteins, increases in oxidative stress, and development of diabetic kidney pathology, despite unchanged levels of diabetic hyperglycemia.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Activation of Protein Kinase C  $ \\alpha $,  $ \\beta $,  $ \\delta $, and  $ \\theta $",
                "Hyperglycemia in retinal pericytes activates PKC leading to PDGF receptor-β dephosphorylation and pericyte apoptosis. Which phosphatase mediates this cascade?",
                [
                    "Src homology-2 domain-containing phosphatase-1 (SHP1)",
                    "Glyoxalase I",
                    "TET2 dioxygenase",
                    "O-GlcNAcase",
                ],
                0,
                "PKC/p38α MAPK signaling increases SHP1, dephosphorylating PDGF receptor-β and causing pericyte apoptosis.",
                ref(
                    "Activation of Protein Kinase C  $ \\alpha $,  $ \\beta $,  $ \\delta $, and  $ \\theta $",
                    "hyperglycemia persistently activates PKC and p38α mitogen-activated protein kinase (MAPK) to increase expression of a previously unknown target of PKC signaling, Src homology-2 domain-containing phosphatase-1 (SHP1), a protein tyrosine phosphatase.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Diabetic Retinopathy and Other Ocular Complications of Diabetes",
                "A 55-year-old with T2D and center-involved DME, vision 20/50. Per current evidence, first-line therapy is:",
                [
                    "Intravitreal anti-VEGF injections per DRCR protocol",
                    "Observation only regardless of center involvement",
                    "Routine oral fenofibrate as sole therapy",
                    "Immediate bilateral enucleation",
                ],
                0,
                "Anti-VEGF is standard of care for center-involved DME with visual impairment; aflibercept superior to bevacizumab at 1–2 years for worse baseline vision.",
                ref(
                    "Treatment of Diabetic Macular Edema",
                    "Current first-line therapy for most eyes with center-involved DME and DME-related visual impairment of 20/32 or worse is intravitreous injections of VEGF inhibitors following a defined protocol such as that described by the DRCR Network (Fig. 38.34).",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Evaluation and Treatment of Proliferative Diabetic Retinopathy",
                "An eye with high-risk PDR and poor follow-up reliability is best managed with:",
                [
                    "Panretinal photocoagulation (possibly with anti-VEGF) rather than anti-VEGF alone",
                    "No treatment until vitreous hemorrhage occurs",
                    "Oral metformin only",
                    "Focal macular laser without evaluating periphery",
                ],
                0,
                "If compliance with anti-VEGF follow-up is expected to be poor, PRP alone or combined with VEGF inhibitor is preferred over anti-VEGF monotherapy.",
                ref(
                    "Evaluation and Treatment of Proliferative Diabetic Retinopathy",
                    "If compliance is expected to be a problem for a specific patient, then treatment with laser panretinal photocoagulation alone, or in combination with a VEGF inhibitor, is the preferred therapeutic approach.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Initial Ophthalmic Evaluation",
                "A 24-year-old diagnosed with T1D at age 14 should have first dilated retinal examination:",
                [
                    "Now (≥5 years after diagnosis)",
                    "At age 40 only",
                    "Never unless symptomatic",
                    "Only if HbA1c > 10%",
                ],
                0,
                "Initial exam ≥5 years after T1D diagnosis in patients older than 10 years.",
                ref(
                    "Initial Ophthalmic Evaluation",
                    "initial ophthalmic examination is recommended beginning 5 years after the diagnosis of T1D",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Initial Ophthalmic Evaluation",
                "A 52-year-old newly diagnosed T2D with no visual symptoms needs eye evaluation:",
                [
                    "Immediately after diabetes diagnosis",
                    "After 5 years of diabetes duration only",
                    "Only if glucose > 300 mg/dL",
                    "Never—T2D does not cause retinopathy",
                ],
                0,
                "Up to 3% may have CSME or high-risk PDR at T2D diagnosis—immediate examination is recommended.",
                ref(
                    "Initial Ophthalmic Evaluation",
                    "initial ophthalmic examination is recommended beginning 5 years after the diagnosis of T1D and immediately after diagnosis of T2D",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Screening for and Classification of Chronic Kidney Disease",
                "To confirm elevated albuminuria in diabetes, how many abnormal UACR measurements are required?",
                [
                    "At least 2 of 3 samples within ~3 months",
                    "A single random spot urine only",
                    "One 24-hour urine always sufficient",
                    "No repeat testing if patient is asymptomatic",
                ],
                0,
                "Because UACR varies up to 30% day-to-day, ≥2 of 3 abnormal measurements are needed for diagnosis.",
                ref(
                    "Screening for and Classification of Chronic Kidney Disease",
                    "At least two out of three measurements should be abnormal before a diagnosis of elevated albuminuria is made.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Diagnosis of Diabetic Nephropathy",
                "CKD in diabetes is diagnosed when which criteria are met?",
                [
                    "Two eGFR <60 mL/min/1.73 m² ≥3 months apart and/or 2 of 3 abnormal UACR ≥30 mg/g",
                    "Single creatinine above upper lab limit",
                    "Dipstick trace protein once",
                    "eGFR 62 on one occasion only",
                ],
                0,
                "CKD requires persistent eGFR <60 and/or persistent albuminuria absent acute illness.",
                ref(
                    "Diagnosis of Diabetic Nephropathy",
                    "CKD is diagnosed when two eGFR measurements, at least 3 months apart, are below 60 mL/min/1.73 m² and/or 2 out of 3 albuminuria measurements are abnormal (UACR ≥30 mg/g creatinine).",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Glucose Control in Type 1 Diabetes",
                "In DCCT participants with baseline normoalbuminuria, intensive therapy reduced risk of severely increased albuminuria by:",
                [
                    "54% relative risk reduction vs conventional therapy",
                    "0%—no nephropathy benefit",
                    "100%—no albuminuria ever in intensive group",
                    "10% only",
                ],
                0,
                "Intensive group: 39% RRR for moderately elevated and 54% for severely increased albuminuria over 6.5 years.",
                ref(
                    "Glucose Control in Type 1 Diabetes",
                    "the intensively treated glycemia group had a relative risk reduction of 39% for developing moderately elevated albuminuria and a relative risk reduction of 54% for developing severely increased albuminuria (macroalbuminuria) compared to those in the conventionally managed group over the 6.5-year study.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Glucose-Lowering Medications With Organ Protection",
                "A patient with T2D, UACR 450 mg/g, eGFR 38 mL/min/1.73 m² on ACEi. Which add-on has RCT evidence for hard renal outcomes?",
                [
                    "SGLT2 inhibitor (e.g., canagliflozin per CREDENCE)",
                    "Sulfonylurea as sole renoprotective strategy",
                    "Pioglitazone only without RAS blockade",
                    "DPP-4 inhibitor as first-line organ protection",
                ],
                0,
                "CREDENCE showed canagliflozin benefit on kidney failure/doubling creatinine composite in established nephropathy.",
                ref(
                    "Glucose-Lowering Medications With Organ Protection",
                    "CREDENCE), which showed a major benefit on kidney outcome and also on heart failure and MACEs",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Blood Pressure in Type 1 Diabetes",
                "A normotensive T1D patient with normoalbuminuria asks about starting ACEi solely to prevent nephropathy. Evidence supports:",
                [
                    "No—RAS inhibitors do not prevent moderately elevated albuminuria in normotensive normoalbuminuric T1D",
                    "Yes—mandatory ACEi for all T1D regardless of albuminuria",
                    "Yes—ARB superior and required from diagnosis",
                    "Only if eGFR < 30",
                ],
                0,
                "RAS inhibitors do not prevent moderately elevated albuminuria in normotensive normoalbuminuric T1D; treat hypertension when present.",
                ref(
                    "Blood Pressure in Type 1 Diabetes",
                    "RAS inhibitors do not prevent moderately elevated albuminuria in normotensive people with T1D.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Prevention and Management of Diabetic Nephropathy",
                "Finerenone in T2D with CKD on RAS blockade primarily reduces progression through:",
                [
                    "Nonsteroidal mineralocorticoid receptor antagonism with less hyperkalemia than spironolactone",
                    "SGLT2 inhibition in proximal tubule",
                    "GLP-1 receptor agonism",
                    "Direct ACE enzyme inhibition",
                ],
                0,
                "Finerenone (FIDELIO-DKD, FIGARO-DKD) is a nonsteroidal MRA reducing kidney and CV events in T2D CKD.",
                ref(
                    "Prevention and Management of Diabetic Nephropathy",
                    "In T2D, SGLT2is and new aldosterone antagonists are important new options (Fig. 38.40).",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Classification of Diabetic Distal Symmetric Polyneuropathy",
                "A patient has burning foot pain, absent ankle reflexes, and reduced pinprick at toes but normal nerve conduction. Toronto classification:",
                [
                    "Probable DSPN (symptoms + signs without confirmatory electrophysiology)",
                    "Confirmed DSPN",
                    "Definite small-fiber neuropathy by IENF density",
                    "No neuropathy—normal conduction excludes DSPN",
                ],
                0,
                "Probable DSPN = combination of symptoms and signs (≥2 of symptoms, decreased sensation, absent ankle reflexes) without required NCS abnormality.",
                ref(
                    "Classification of Diabetic Distal Symmetric Polyneuropathy",
                    "Probable DSPN. The presence of a combination of symptoms and signs of neuropathy, including any two or more of the following: neuropathic symptoms, decreased distal sensation, or unequivocally decreased or absent ankle reflexes.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Treatment of Painful Neuropathy",
                "A 60-year-old with painful DSPN and no contraindications needs first-line pharmacotherapy. Best initial choice per guidelines:",
                [
                    "Pregabalin or duloxetine (titrate to effective dose)",
                    "Long-acting opioid monotherapy",
                    "High-dose insulin bolus for pain",
                    "Metoclopramide for neuropathic pain",
                ],
                0,
                "FDA-approved pregabalin and duloxetine have class I evidence; opioids are discouraged for chronic painful DSPN.",
                ref(
                    "Treatment of Painful Neuropathy",
                    "There are three FDA-approved drugs for the treatment of painful DSPN, pregabapentin, duloxetine, and tapentadol, with better evidence for duloxetine and pregabalin than the opioid tapentadol.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Clinical Features of Diabetic Autonomic Neuropathy",
                "Orthostatic hypotension in diabetic autonomic neuropathy is defined as a drop in blood pressure when standing of:",
                [
                    ">20 mm Hg systolic or >10 mm Hg diastolic",
                    ">5 mm Hg systolic only",
                    ">40 mm Hg diastolic only",
                    "Any measurable change regardless of magnitude",
                ],
                0,
                "CAN later features include orthostatic hypotension with these thresholds.",
                ref(
                    "Clinical Features of Diabetic Autonomic Neuropathy",
                    "orthostatic hypotension, defined as a reduction of more than 20 mm Hg in systolic or 10 mm Hg in diastolic pressure when going from a lying to a standing position.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Diabetic Heart Disease",
                "A 58-year-old with T2D and HFrEF but no prior MI. Which drug class has strongest RCT evidence for reducing HF hospitalization?",
                [
                    "SGLT2 inhibitor",
                    "Short-acting sulfonylurea",
                    "Niacin monotherapy",
                    "Thiazolidinedione",
                ],
                0,
                "SGLT2is reduce HF hospitalization and cardiovascular death across EF spectrum including HFrEF and HFpEF.",
                ref(
                    "KEY POINTS",
                    "SGLT2is reduce heart failure hospitalization and cardiovascular death in patients with heart failure across the spectrum of ejection fractions",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Diabetic Heart Disease",
                "For reducing stroke in T2D with established ASCVD, which class has more consistent trial benefit?",
                [
                    "GLP-1 receptor agonist",
                    "SGLT2 inhibitor",
                    "Basal insulin glargine alone",
                    "Alpha-glucosidase inhibitor",
                ],
                0,
                "GLP-1RAs show more consistent MACE subcomponent benefits including stroke; SGLT2is do not reduce stroke.",
                ref(
                    "KEY POINTS",
                    "GLP-1RAs have more consistent benefits in reducing major adverse cardiovascular event (MACE) subcomponents, including stroke, than do SGLT2is, which do not reduce stroke.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Diabetic Heart Disease",
                "Optimal T1D therapy per chapter targets includes HbA1c, blood pressure, and statin when:",
                [
                    "HbA1c 6.5–7.5%, BP <130/80, statin if LDL-c >160 mg/dL",
                    "HbA1c <5.0% always, no BP target, no statins in T1D",
                    "HbA1c >9% to avoid hypoglycemia, BP <160/100",
                    "Statin only after second MI regardless of LDL",
                ],
                0,
                "Key points specify intensive hyperglycemia treatment, ACEi/ARB to <130/80, and statins for LDL >160 in T1D.",
                ref(
                    "KEY POINTS",
                    "Optimal therapy includes intensive treatment of hyperglycemia to achieve hemoglobin  $ A_{1c} $ ( $ HbA_{1c} $) levels of 6.5% to 7.5%, treatment with ACEIs or ARBs to maintain a target blood pressure below 130/80, and statins for people with T1D with LDL-c above 160 mg/dL.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "The Diabetic Foot",
                "A neuropathic foot ulcer with good perfusion and no infection (Wagner 1). Initial management emphasizes:",
                [
                    "Pressure off-loading (e.g., total-contact cast)",
                    "Immediate below-knee amputation",
                    "Broad IV antibiotics for all Wagner 1 ulcers",
                    "No off-loading until osteomyelitis confirmed",
                ],
                0,
                "TCC is gold standard off-loading; antibiotics not indicated without clinical infection in neuropathic ulcers with good circulation.",
                ref(
                    "KEY POINTS",
                    "Management involves pressure off-loading, parenteral antibiotics for infection, and ensuring adequate arterial inflow.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "The Diabetic Foot",
                "A patient with diabetic foot ulcer and PAD undergoes vascular evaluation on day 12. Compared with revascularization within 2 weeks, delayed care:",
                [
                    "Increases amputation risk toward diabetic PAD rates",
                    "Has no effect on limb salvage",
                    "Eliminates need for off-loading",
                    "Guarantees ulcer healing without revascularization",
                ],
                0,
                "Prompt vascular evaluation and revascularization within 2 weeks significantly reduce amputation rates.",
                ref(
                    "KEY POINTS",
                    "Prompt vascular evaluation and revascularization within 2 weeks significantly reduce the rate of amputation.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "The Diabetic Foot",
                "Annual diabetic foot screening should include:",
                [
                    "Barefoot inspection, monofilament, and pulse assessment",
                    "HbA1c only without foot exam",
                    "MRI of both feet for all patients yearly",
                    "Skin biopsy for all patients with diabetes",
                ],
                0,
                "CDFE includes visual inspection and 10-g monofilament; sensory neuropathy plus PAD predicts ulceration.",
                ref(
                    "The Diabetic Foot",
                    "A simple neurologic examination includes assessment of pressure perception using a 10-g monofilament.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Monitoring Kidney Disease",
                "Once severely increased albuminuria is present, recommended monitoring frequency is:",
                [
                    "UACR every 3 months; eGFR every 3–6 months",
                    "No further urine testing needed",
                    "eGFR once per decade",
                    "UACR only if patient develops edema",
                ],
                0,
                "Severely increased albuminuria warrants quarterly UACR and eGFR every 3–6 months depending on stage.",
                ref(
                    "Monitoring Kidney Disease",
                    "Once urinary albumin excretion is severely increased, the UACR should be measured every 3 months and the eGFR every 3 to 6 months, depending on the CKD stage and rate of progression of the disease.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Treatment of Diabetic Macular Edema",
                "A patient with center-involving DME and good vision (20/25) may initially be managed by:",
                [
                    "Close observation with OCT and acuity—many do not need immediate anti-VEGF",
                    "Mandatory monthly anti-VEGF regardless of vision",
                    "Bilateral vitrectomy first line",
                    "Systemic corticosteroids only",
                ],
                0,
                "DRCR data support observation for ciDME with good vision; ~66% avoid anti-VEGF over 2 years with monitoring at least every 16 weeks.",
                ref(
                    "Treatment of Diabetic Macular Edema",
                    "patients with center-involving DME and good vision can confidently be managed by observation alone, with only 34% requiring anti-VEGF injections due to later visual deterioration.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Glucose Control in Type 2 Diabetes",
                "UKPDS intensive glucose control in T2D reduced risk of moderately or severely increased albuminuria by approximately:",
                [
                    "30% over 9–12 years",
                    "0%",
                    "90% within 1 year",
                    "75% only in patients with baseline eGFR <15",
                ],
                0,
                "UKPDS mean HbA1c 7.0% vs 7.9% yielded 30% relative risk reduction for albuminuria progression.",
                ref(
                    "Glucose Control in Type 2 Diabetes",
                    "which translated to a 30% reduction in the relative risk of developing moderately or severely increased albuminuria after 9 to 12 years.",
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
                "Treatment with panretinal photocoagulation or intraocular anti-VEGF therapy reduces blindness from PDR by over 90%.",
                True,
                "Key points state PRP or anti-VEGF reduces PDR-related blindness by >90%.",
                ref(
                    "KEY POINTS",
                    "Treatment with panretinal photocoagulation or intraocular anti-VEGF therapy reduces blindness from PDR by over 90%.",
                ),
            ),
            tf(
                f"{p}-t2",
                "KEY POINTS",
                "Intraocular anti-VEGF therapy substantially improves underlying retinal nonperfusion in NPDR.",
                False,
                "Anti-VEGF reduces NPDR severity but does not substantially improve underlying retinal nonperfusion.",
                ref(
                    "KEY POINTS",
                    "Treatment with intraocular anti-VEGF therapy reduces the severity of nonproliferative diabetic retinopathy (NPDR) but does not substantially improve underlying retinal nonperfusion.",
                ),
            ),
            tf(
                f"{p}-t3",
                "KEY POINTS",
                "In T2D with CKD, organ protection is seen with SGLT2 inhibitors and GLP-1 receptor agonists.",
                True,
                "Key points endorse SGLT2i and GLP-1RAs for organ protection in T2D with CKD.",
                ref(
                    "KEY POINTS",
                    "In type 2 diabetes (T2D) with CKD, organ protection is seen with sodium-glucose cotransporter-2 inhibitors (SGLT2i) and glucagon-like peptide-1 (GLP-1) receptor agonists (GLP-1RAs).",
                ),
            ),
            tf(
                f"{p}-t4",
                "Clinical Overview of Diabetes Complications",
                "Diabetic neuropathy affects more than 60% of patients with diabetes.",
                True,
                "Clinical overview cites >60% neuropathy prevalence with diverse subtypes.",
                ref(
                    "Clinical Overview of Diabetes Complications",
                    "Diabetic neuropathy affects more than 60% of patients with diabetes",
                ),
            ),
            tf(
                f"{p}-t5",
                "Increased Aldose Reductase Substrate Conversion",
                "Clinical trials of aldose reductase inhibitors in the 1990s–2000s demonstrated clear efficacy for diabetic complications.",
                False,
                "32 clinical trials showed no clinical efficacy despite preclinical neuropathy benefit in dogs.",
                ref(
                    "Increased Aldose Reductase Substrate Conversion",
                    "None of these trials showed clinical efficacy.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Molecular Basis for Metabolic Memory",
                "Metabolic memory may arise from hyperglycemia-induced epigenetic changes in stem cells that persist in differentiated cells.",
                True,
                "KEY POINTS and molecular section link enhancer DNA methylation in HSCs to persistent complication risk.",
                ref(
                    "KEY POINTS",
                    "Metabolic memory appears to arise from hyperglycemia-induced epigenetic changes in stem cells, probably through modifying enhancer activity, which persist in differentiated cells.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Comprehensive Eye Examination",
                "Dilated ophthalmic examination is superior to undilated evaluation for classifying retinopathy severity.",
                True,
                "Only 50% of eyes correctly classified through undilated pupils.",
                ref(
                    "Comprehensive Eye Examination",
                    "Dilated ophthalmic examination is superior to undilated evaluation because only 50% of eyes are correctly classified as to the presence and severity of retinopathy through undilated pupils.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Definitions in Diabetic Nephropathy",
                "For every 20 patients with diabetes and CKD, less than 1 will survive to end-stage renal disease.",
                True,
                "Most succumb to CVD, heart failure, or infection before ESKD.",
                ref(
                    "Definitions in Diabetic Nephropathy",
                    "for every 20 patients with diabetes and CKD, less than 1 will survive to end-stage renal disease, succumbing instead to atherosclerotic CVD, heart failure, or infection.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Treatment of Painful Neuropathy",
                "Opioid use is encouraged as first-line therapy for chronic painful diabetic peripheral neuropathy.",
                False,
                "Despite tapentadol approval, opioids are discouraged for chronic painful DSPN.",
                ref(
                    "Treatment of Painful Neuropathy",
                    "opioid use is discouraged in the treatment of painful DSPN.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Disease-Modifying Therapy in Distal Symmetric Polyneuropathy",
                "There are FDA-approved disease-modifying therapies that directly halt progression of DSPN.",
                False,
                "No FDA-approved agents directly address DSPN as a disease entity; lifestyle and glucose control are mainstays.",
                ref(
                    "Disease-Modifying Therapy in Distal Symmetric Polyneuropathy",
                    "There are no U.S. Food and Drug Administration (FDA)-approved therapies that directly address DSPN as a disease entity.",
                ),
            ),
            tf(
                f"{p}-t11",
                "The Diabetic Foot",
                "More than 80% of lower-limb amputations in diabetes are preceded by foot ulcers.",
                True,
                "Foot ulcer precedes most amputations; screening reduces amputation rates.",
                ref(
                    "The Diabetic Foot",
                    "More than 80% of amputations are preceded by foot ulcers, and reduced amputation rates occur after implementation of foot screening and education programs.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Blood Pressure Control in Prevention and Management of Diabetic Nephropathy",
                "Benefits of blood pressure reduction for diabetic nephropathy are lost rapidly when blood pressure control deteriorates.",
                True,
                "Unlike glucose metabolic memory, BP benefits do not persist after control is lost.",
                ref(
                    "Blood Pressure Control in Prevention and Management of Diabetic Nephropathy",
                    "In contrast to glucose \"metabolic memory,\" the benefits of blood pressure reduction are lost rapidly when blood pressure control deteriorates.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Diabetic Heart Disease",
                "T2D in high-income countries is associated with an approximate doubling in cardiovascular risk after adjusting for traditional risk factors.",
                True,
                "Adjusted ~twofold excess CVD risk in T2D meta-analyses.",
                ref(
                    "Cardiovascular Risk Associated With Prediabetes and Type 2 Diabetes",
                    "T2D in high-income countries is associated with an approximate doubling in cardiovascular risk compared to those without diabetes after adjusting for traditional risk factors",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Clinical Overview of Diabetes Complications",
                "Assertion: Intensive glycemic control in DCCT reduced microvascular complication rates in T1D.",
                "Reason: DCCT found no relationship between HbA1c and diabetic retinopathy or nephropathy.",
                2,
                "Assertion true per DCCT; reason false—continuous glycemia–complication relationship was demonstrated.",
                ref(
                    "Clinical Overview of Diabetes Complications",
                    "A strong relationship between hyperglycemia and diabetic retinopathy (DR) and nephropathy has been demonstrated in both T1D and T2D large prospective clinical studies—the Diabetes Control and Complications Trial (DCCT) and the United Kingdom Prospective Diabetes Study (UKPDS), respectively.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Molecular Basis for Metabolic Memory",
                "Assertion: Metabolic memory may involve epigenetic changes in hematopoietic stem cells.",
                "Reason: DCCT/EDIC showed identical complication rates immediately when HbA1c equalized post-DCCT.",
                2,
                "Assertion true—HSC enhancer methylation persists; reason false—complication gaps persisted despite identical post-study HbA1c.",
                ref(
                    "Clinical Overview of Diabetes Complications",
                    "In the former conventional therapy group, whose post-DCCT  $ HbA_{1c} $ levels were identical to those in the former intensive therapy group, effects of previous high  $ HbA_{1c} $ on poststudy retinopathy, nephropathy, neuropathy, and major adverse cardiovascular event (MACE)",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Increased Intracellular Formation of the Major Advanced Glycation End Products—Precursor Methylglyoxal",
                "Assertion: Methylglyoxal contributes to painful diabetic neuropathy via Nav1.8 modification.",
                "Reason: Methylglyoxal has no effect on sensory neuron excitability.",
                2,
                "Assertion true—MG modifies Nav1.8 in C fibers; reason false—it depolarizes neurons and facilitates firing.",
                ref(
                    "Increased Intracellular Formation of the Major Advanced Glycation End Products—Precursor Methylglyoxal",
                    "Posttranslational modification of Nav1.8 by methylglyoxal depolarizes sensory neurons, facilitating firing of these pain pathway neurons.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Evaluation and Treatment of Proliferative Diabetic Retinopathy",
                "Assertion: Anti-VEGF therapy can be first-line for selected PDR eyes.",
                "Reason: Neovascularization is insensitive to VEGF inhibition.",
                2,
                "Assertion true per DRCR Protocol S; reason false—neovascular processes are exquisitely sensitive to anti-VEGF.",
                ref(
                    "Evaluation and Treatment of Proliferative Diabetic Retinopathy",
                    "Neovascular processes are exquisitely sensitive to anti-VEGF agents, and eyes with severe neovascularization of the retina or anterior segment have dramatic and rapid improvement with anti-VEGF therapy.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Screening for and Classification of Chronic Kidney Disease",
                "Assertion: Moderately increased albuminuria has replaced the term microalbuminuria in KDIGO.",
                "Reason: KDIGO still recommends the term microalbuminuria for clinical use.",
                2,
                "Assertion true; reason false—macroalbuminuria term also replaced by severely increased albuminuria.",
                ref(
                    "Screening for and Classification of Chronic Kidney Disease",
                    "The term moderately increased albuminuria has replaced microalbuminuria, and severely increased albuminuria replaced macroalbuminuria.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Glucose-Lowering Medications With Organ Protection",
                "Assertion: SGLT2 inhibitors provide kidney protection independent of baseline eGFR down to 20 mL/min/1.73 m².",
                "Reason: SGLT2i renal benefits require eGFR >90 and UACR <30 only.",
                2,
                "Assertion true per trials; reason false—benefits span eGFR 20 to >90 and all UACR strata.",
                ref(
                    "Glucose-Lowering Medications With Organ Protection",
                    "Importantly, the benefits on kidney outcomes are independent of baseline eGFR from 20 mL/min/1.73 m $ ^{2} $ to >90 mL/min/1.73 m $ ^{2} $",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Treatment of Distal Symmetric Polyneuropathy",
                "Assertion: Tight glucose control prevents DSPN in T1D.",
                "Reason: Intensive glucose control has identical strong preventive effects on DSPN in T2D as in T1D.",
                2,
                "Assertion true per ADA grade A; reason false—T2D intensive glucose alone is only modestly effective.",
                ref(
                    "BOX 38.5 American Diabetes Association Recommendations for Distal Symmetric Polyneuropathy (DSPN)",
                    "In patients with type 2 diabetes with more advanced disease and multiple risk factors and comorbidities, intensive glucose control alone is modestly effective in preventing distal symmetric polyneuropathy, and patient-centered goals should be targeted.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Clinical Features of Diabetic Autonomic Neuropathy",
                "Assertion: Cardiac autonomic neuropathy is associated with increased mortality.",
                "Reason: CAN only causes symptoms and never affects cardiac arrhythmia risk.",
                2,
                "Assertion true; reason false—CAN links to arrhythmia, silent MI, and early mortality.",
                ref(
                    "Clinical Features of Diabetic Autonomic Neuropathy",
                    "CAN is clinically the most important of the autonomic neuropathies because of its association with early cardiac arrhythmia, silent myocardial infarctions, and early mortality.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "KEY POINTS",
                "Assertion: SGLT2 inhibitors reduce heart failure hospitalization in patients with heart failure.",
                "Reason: SGLT2 inhibitors consistently reduce stroke in cardiovascular outcome trials.",
                2,
                "Assertion true across EF spectrum; reason false—SGLT2is do not reduce stroke per key points.",
                ref(
                    "KEY POINTS",
                    "SGLT2is reduce heart failure hospitalization and cardiovascular death in patients with heart failure across the spectrum of ejection fractions",
                ),
            ),
            ar(
                f"{p}-ar10",
                "The Diabetic Foot",
                "Assertion: Total-contact casting is effective off-loading for neuropathic foot ulcers.",
                "Reason: Repetitive pressure on neuropathic wounds promotes healing rather than chronic inflammation.",
                2,
                "Assertion true—TCC gold standard; reason false—repetitive pressure causes chronic inflammation; off-loading enables repair.",
                ref(
                    "The Diabetic Foot",
                    "These important observations support that repetitive pressure on a neuropathic wound contributes to the chronicity of the wound, whereas pressure relief results in a reparative phase.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Differential Diagnosis of Diabetic Neuropathy",
                "Assertion: Up to 10% of neuropathy in diabetes patients may be non-diabetic in etiology.",
                "Reason: All peripheral neuropathy in diabetes is always caused by hyperglycemia alone.",
                2,
                "Assertion true per Rochester study; reason false—B12, paraproteinemia, hypothyroidism, and other causes must be excluded.",
                ref(
                    "Differential Diagnosis of Diabetic Neuropathy",
                    "up to 10% of peripheral neuropathy in patients with diabetes was determined not to be secondary to diabetes.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Clinical Overview of Diabetes Complications",
                "Assertion: Diabetes is the leading cause of end-stage renal disease.",
                "Reason: Diabetes never causes kidney failure requiring replacement therapy.",
                2,
                "Assertion true in clinical overview; reason false—diabetes is leading cause of ESRD.",
                ref(
                    "Clinical Overview of Diabetes Complications",
                    "the leading cause of end-stage renal disease",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "38",
        "title": "Complications of Diabetes Mellitus",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Michael Brownlee, Lloyd Paul Aiello, Jennifer K. Sun, Paolo Sandico Silva, Peter Rossing, Eva L. Feldman, Naveed Sattar, and Andrew JM Boulton",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_38_Complications_of_Diabetes_Mellitus.md",
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
