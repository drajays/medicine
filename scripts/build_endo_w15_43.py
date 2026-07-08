#!/usr/bin/env python3
"""Generate Williams 15e module w15-43 — Neuroendocrine Tumors and Disorders."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-43"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-43_Neuroendocrine_Tumors_and_Disorders.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why WHO 2022 grading drives NEN management",
                "G1/G2/G3 NET and NEC categories carry prognostic and therapeutic implications for gastroenteropancreatic and bronchopulmonary neoplasms.",
                ref(
                    "KEY POINTS",
                    "The World Health Organization (WHO) classification system (2022) of neuroendocrine tumors (NETs; G1 NET, G2 NET, and G3 NET) and neuroendocrine carcinoma (NEC) is informative and necessary for the clinical management of gastroenteropancreatic and lung neuroendocrine neoplasms.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How circulating biomarkers support NEN diagnosis and follow-up",
                "Chromogranin A and urinary 5-HIAA are general markers; hormone assays (insulin, gastrin, glucagon, VIP) localize functioning panNEN syndromes; NETest offers a multianalyte alternative.",
                ref(
                    "KEY POINTS",
                    "The most important and widely used circulating general biomarkers for neuroendocrine neoplasms are chromogranin A (general) and 5-hydroxyindoleacetic acid (5-HIAA) (carcinoid syndrome) and the less widely used NETest and neuron-specific enolase (NSE) for small cell lung cancer. Specific assays for hypersecreted hormones are commonly used in functioning pancreatic neuroendocrine tumor syndromes (insulin, gastrin, glucagon, vasoactive intestinal peptide).",
                ),
            ),
            note(
                f"{p}-n3",
                "Introduction",
                "How foregut, midgut, and hindgut map NEN primary sites",
                "Embryonic gut derivation stratifies bronchopulmonary/thymic/gastric/pancreatic foregut tumors from ileocecal midgut and rectal/colonic hindgut lesions—with distinct gastric types 1–4 biology.",
                ref(
                    "Introduction",
                    "As NENs predominantly derive from the embryonic gut, primary tumor sites are traditionally categorized into “foregut,” “midgut,” and “hindgut” NENs.",
                ),
            ),
            note(
                f"{p}-n4",
                "Genetic Syndromes With NENs",
                "Why hereditary syndromes mandate early NEN surveillance",
                "MEN1, MEN4, VHL, NF1, Pacak-Zhuang, Mahvash, and insulinomatosis predispose to pancreatic, gastric, duodenal, thymic, and bronchopulmonary NENs with syndrome-specific genetics.",
                ref(
                    "Genetic Syndromes With NENs",
                    "Primary pancreatic, gastric, duodenal, thymic, and BP NENs arise in patients with the multiple endocrine neoplasia type 1 syndrome (MEN1, Mendelian Inheritance in Man [MIM] number 131100).",
                ),
            ),
            note(
                f"{p}-n5",
                "Carcinoid Syndrome",
                "Why carcinoid syndrome usually requires hepatic bypass",
                "Serotonin and vasoactive peptides are metabolized in the liver; symptoms emerge when tumor drains outside portal circulation (e.g., bronchial, ovarian, extensive retroperitoneal disease).",
                ref(
                    "Carcinoid Syndrome",
                    "Since these hormones and peptides can be effectively metabolized by the liver, symptoms of the carcinoid syndrome generally only occur when tumor localizations are outside of, or bypass, the portal vein drainage system.",
                ),
            ),
            note(
                f"{p}-n6",
                "Carcinoid Syndrome",
                "How serotonin excess drives CHD and mesenteric fibrosis",
                "Systemic serotonin contributes to secretory diarrhea, tricuspid/pulmonary valve fibrosis (CHD), and desmoplastic mesenteric reactions in midgut metastases.",
                ref(
                    "KEY POINTS",
                    "The carcinoid syndrome includes flushing, secretory diarrhea, right-sided heart fibrosis eventually resulting in right-sided heart failure (carcinoid heart disease), mesenterial fibrosis eventually leading to small bowel obstruction, edema, and ischemia, and occasionally bronchial wheezing.",
                ),
            ),
            note(
                f"{p}-n7",
                "Carcinoid Syndrome",
                "Why all carcinoid syndrome patients need CHD screening",
                "Untreated CHD cuts 3-year survival by ~30%; echocardiography should be performed because patients may be asymptomatic until advanced right heart failure.",
                ref(
                    "Carcinoid Syndrome",
                    "All patients with carcinoid syndrome should be screened for CHD because this is a major prognostic factor limiting 3-year survival by 30% when left untreated.",
                ),
            ),
            note(
                f"{p}-n8",
                "Carcinoid Syndrome",
                "How carcinoid crisis threatens perioperative stability",
                "Stress or tumor manipulation can trigger massive vasoactive peptide release; IV somatostatin receptor ligands are used perioperatively though evidence remains debated.",
                ref(
                    "Carcinoid Syndrome",
                    "An acute life-threatening feature of (uncontrolled) carcinoid syndrome is “carcinoid crisis” characterized by abrupt onset of hemodynamic instability, usually accompanied by general features of the carcinoid syndrome with severe flushing and cardiovascular collapse; if left untreated, it may be fatal.",
                ),
            ),
            note(
                f"{p}-n9",
                "Insulinoma",
                "Why Whipple triad anchors insulinoma diagnosis",
                "Neuroglycopenic and adrenergic symptoms with glucose <2.2 mmol/L relieved by glucose define inappropriate insulin secretion; exclude factitious hypoglycemia and insulinomatosis.",
                ref(
                    "Insulinoma",
                    "Usually, the so-called Whipple's triad consisting of (1) symptoms of hypoglycemia, (2) plasma glucose levels <2.2 mmol/L (<40 mg/dL), and (3) relief of symptoms with the administration of glucose prevails.",
                ),
            ),
            note(
                f"{p}-n10",
                "Gastrinoma",
                "How chronic PPI use obscures Zollinger-Ellison diagnosis",
                "Fasting hypergastrinemia with gastric pH ≤2 confirms ZES, but widespread PPI therapy and faulty assays contribute to underdiagnosis; secretin stimulation helps when gastrin is <10× ULN.",
                ref(
                    "Gastrinoma",
                    "However, since the diagnosis of ZES is challenging, particularly being hampered by the abundant use of proton pump inhibitors (PPIs), it is generally believed that ZES is currently underdiagnosed.",
                ),
            ),
            note(
                f"{p}-n11",
                "VIPoma",
                "Why WDHA defines the VIPoma syndrome",
                "Profuse secretory diarrhea (6–8 L/day), hypokalemia, and achlorhydria from VIP hypersecretion constitute Verner-Morrison (WDHA) syndrome.",
                ref(
                    "VIPoma",
                    "Therefore, the VIPoma syndrome has also been termed watery diarrhea hypokalemia andichlorhydria (WDHA) syndrome.",
                ),
            ),
            note(
                f"{p}-n12",
                "Glucagonoma",
                "How necrolytic migratory erythema signals glucagonoma",
                "Catabolic glucagon excess causes diabetes, weight loss, and pathognomonic NME in ~80% of patients alongside thromboembolism and stomatitis.",
                ref(
                    "Glucagonoma",
                    "However, the most distinct feature of the glucagonoma syndrome occurring in approximately 80% of patients is necrolytic migratory erythema of the skin",
                ),
            ),
            note(
                f"{p}-n13",
                "NEN Pathology",
                "Why Ki-67 and differentiation separate G3 NET from NEC",
                "Proliferation index (Ki-67 <3%, 3–20%, >20%) grades GEP NENs; G3 NET remains well differentiated whereas G3 NEC is poorly differentiated with distinct outcomes.",
                ref(
                    "NEN Pathology",
                    "G3 is further divided into two different groups depending on tumor differentiation, with G3 neuroendocrine tumor (NET) having well-differentiated tumor cells and (G3) neuroendocrine carcinoma (NEC) having poorly differentiated tumor cells",
                ),
            ),
            note(
                f"{p}-n14",
                "Circulating Biomarkers",
                "Why chromogranin A is a poor first-line screening test",
                "Once NEN is established CgA is only 60–90% accurate with specificity <35% because PPIs, renal failure, atrophic gastritis, and other neoplasms elevate levels.",
                ref(
                    "Circulating Biomarkers",
                    "However, when the diagnosis of NEN has been established, elevated CgA levels in the blood are only 60% to 90% accurate. CgA is unsuitable as a first-line diagnostic or screening tool.",
                ),
            ),
            note(
                f"{p}-n15",
                "NETest and Other Blood-Based Tumor Markers",
                "How NETest outperforms single-analyte biomarkers",
                "A 51-gene blood transcript algorithm achieves 90–99% sensitivity and 85–95% specificity for GEP/BP NENs and is not confounded by PPI or SRL therapy.",
                ref(
                    "NETest and Other Blood-Based Tumor Markers",
                    "This approach is superior to single analyte tumor biomarkers and has high sensitivity (90%–99%) and specificity (85%–95%) for detection of GEP and BP NENs and significantly outperforms other monoanalytes such as CgA.",
                ),
            ),
            note(
                f"{p}-n16",
                "Carcinoid Syndrome Markers",
                "How urinary 5-HIAA tracks carcinoid syndrome activity",
                "5-HIAA reflects serotonin turnover and supports diagnosis and follow-up in symptomatic GEP/BP NEN patients, including those with CHD.",
                ref(
                    "Carcinoid Syndrome Markers",
                    "Plasma or urinary levels of the breakdown metabolite of serotonin, 5-HIAA, are used for diagnosis and follow-up of GEP NEN and BP NEN patients who demonstrate symptoms of the carcinoid syndrome and CHD",
                ),
            ),
            note(
                f"{p}-n17",
                "Somatostatin Receptor Imaging",
                "How 68Ga-DOTATATE PET enables theranostic staging",
                "SRI detects SST-expressing lesions throughout the body, often beyond CT/MRI, and quantifies uptake to select patients for PRRT with radiolabeled somatostatin analogs.",
                ref(
                    "KEY POINTS",
                    "Molecular imaging with  $ ^{68} $Ga-DOTA-labeled somatostatin receptor ligands in combination with three-phase computed tomography or magnetic resonance imaging is an important procedure for staging of the neuroendocrine tumor disease and is a theranostic tool for peptide receptor radionuclide therapy (PRRT) using beta-emitting radiolabeled somatostatin receptor ligands.",
                ),
            ),
            note(
                f"{p}-n18",
                "18F-Fluorodeoxyglucose PET",
                "How FDG-PET suits high-grade NEN imaging",
                "18FDG PET/CT or PET/MRI is the modality of choice for G3 NETs and NECs and can complement 68Ga-SRL PET in selected G2 tumors.",
                ref(
                    "18F-Fluorodeoxyglucose PET",
                    " $ ^{18} $FDG PET/CT and PET/MRI are the imaging modalities of choice for G3 NETs and NECs.",
                ),
            ),
            note(
                f"{p}-n19",
                "Management",
                "How watchful waiting fits indolent G1 NET disease",
                "Not every irresectable G1–2 NET needs immediate systemic therapy; PROMID showed similar median OS with octreotide versus placebo, and ≤2 cm NF-panNENs in MEN1/VHL may be observed.",
                ref(
                    "Management",
                    "Given the indolent growth patterns of a subset of G1-2 NET, not all patients with irresectable or metastasized disease require first-line antiproliferative therapy.",
                ),
            ),
            note(
                f"{p}-n20",
                "Therapy for Carcinoid Syndrome and Carcinoid Heart Disease",
                "Why somatostatin analogs are first-line for carcinoid syndrome",
                "Long-acting octreotide or lanreotide controls flushing/diarrhea in 65–70% of patients and lowers 5-HIAA; short-acting octreotide covers crisis and peri-interventional prophylaxis.",
                ref(
                    "Therapy for Carcinoid Syndrome and Carcinoid Heart Disease",
                    "SRLs are the most effective drugs for the carcinoid syndrome and induce a symptomatic response in 65% to 70% of cases (Fig. 43.9).",
                ),
            ),
            note(
                f"{p}-n21",
                "Therapy for Insulinoma",
                "How everolimus exploits mTOR-inhibitor hyperglycemia in insulinoma",
                "Surgical resection remains curative when feasible; among systemic options PRRT and everolimus are most successful, with everolimus-induced hyperglycemia clinically advantageous.",
                ref(
                    "Therapy for Insulinoma",
                    "The mTOR inhibitor class adverse event of hyperglycemia with everolimus is considered an advantage in the treatment of insulinoma.",
                ),
            ),
            note(
                f"{p}-n22",
                "Somatostatin Receptor Ligands",
                "How PROMID and CLARINET established first-line SRL antiproliferative therapy",
                "Octreotide LAR prolonged TTP in midgut NET (PROMID); lanreotide prolonged PFS in GEP NET (CLARINET)—both are approved first-line for G1–2 disease.",
                ref(
                    "KEY POINTS",
                    "Somatostatin receptor ligands are approved first-line therapies for patients with functioning (hormone-secreting) and nonfunctioning gastroenteropancreatic neuroendocrine tumors (G1 NET, G2 NET, and G3 NET).",
                ),
            ),
            note(
                f"{p}-n23",
                "Radionuclide Therapy",
                "Why NETTER-1 validated 177Lu-DOTATATE as second-line PRRT",
                "After SRL progression, 177Lu-DOTATATE plus octreotide LAR reduced PD/death risk 79% versus high-dose octreotide in metastatic G1–2 midgut NET.",
                ref(
                    "KEY POINTS",
                    "Second-line peptide receptor radionuclide therapy with  $ ^{177} $Lu-DOTATATE can be considered for patients with functioning (hormone-producing) and nonfunctioning somatostatin receptor-positive G1 NET and G2 NET and potentially for some selected patients with G3 NET.",
                ),
            ),
            note(
                f"{p}-n24",
                "Everolimus",
                "How RADIANT trials support second-line everolimus",
                "mTOR inhibition prolongs PFS to ~11 months in progressive G1–2 pancreatic, GI, and bronchopulmonary NET compared with ~4–5 months on placebo.",
                ref(
                    "KEY POINTS",
                    "Targeted therapy with everolimus is approved as second-line therapy in patients with G1-2 gastroenteropancreatic and bronchopulmonary NET, and sunitinib is approved as second-line therapy in patients with G1-2 pancreatic NET.",
                ),
            ),
            note(
                f"{p}-n25",
                "Sunitinib",
                "Why sunitinib targets pancreatic NET angiogenesis",
                "VEGF-driven vascular NENs respond to multitargeted TKI sunitinib (37.5 mg/day), prolonging PFS to ~11–13 months and improving OS in progressive panNEN.",
                ref(
                    "Sunitinib",
                    "In patients with advanced G1-2 panNENs and documented PD at baseline, sunitinib (37.5 mg/day) treatment prolonged the PFS to 11.4 months (later adjusted to 12.6 months) compared with 5.5 months (5.8 months) for placebo-treated patients.",
                ),
            ),
            note(
                f"{p}-n26",
                "Chemotherapy",
                "How cytotoxic therapy fits G3 NET and NEC",
                "Alkylating regimens (temozolomide/capecitabine) favor pancreatic G2–3 NET with MGMT deficiency; platinum-based chemotherapy remains first-line for NEC and SCLC.",
                ref(
                    "KEY POINTS",
                    "Cytotoxic chemotherapy is usually reserved for G2-3 pancreatic NET and NEC and small cell lung cancer, large cell neuroendocrine carcinomas of the lung, and metastatic and/or inoperable atypical bronchopulmonary carcinoids.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "NEN Pathology",
                "A 52-year-old with ileal NET biopsy shows Ki-67 8% and well-differentiated morphology. WHO 2022 grade?",
                [
                    "G2 NET (intermediate grade)",
                    "G1 NET (low grade)",
                    "G3 NEC (poorly differentiated carcinoma)",
                    "Typical carcinoid only—no grading applies",
                ],
                0,
                "Ki-67 3–20% with well-differentiated histology defines G2 NET per WHO 2022 GEP grading.",
                ref(
                    "NEN Pathology",
                    "G2 or intermediate grade having a Ki67 3% to 20% (2–20 mitoses/10 HPF)",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Introduction",
                "Multifocal gastric ECL-cell NETs in a patient with autoimmune atrophic gastritis represent:",
                [
                    "Type 1 gastric NEN from chronic hypergastrinemia",
                    "Type 2 gastric NEN from MEN1 gastrinoma",
                    "Type 3 sporadic aggressive gastric NET",
                    "Type 4 poorly differentiated gastric NEC",
                ],
                0,
                "Type 1 gastric NENs arise multifocally in ECL cells secondary to hypergastrinemia from autoimmune atrophic gastritis.",
                ref(
                    "Introduction",
                    "In the stomach, type 1 gastric NENs develop multifocally in enterochromaffin-like (ECL) cells of the stomach as a consequence of chronic hypergastrinemia resulting from autoimmune atrophic gastritis.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Carcinoid Syndrome",
                "A patient with metastatic midgut NET has flushing, secretory diarrhea, and elevated urinary 5-HIAA. Best initial syndrome-directed therapy?",
                [
                    "Long-acting somatostatin receptor ligand (octreotide or lanreotide)",
                    "High-dose PPI monotherapy",
                    "Immediate platinum chemotherapy",
                    "Observation without biochemical or cardiac workup",
                ],
                0,
                "SRLs are the most effective drugs for carcinoid syndrome, controlling symptoms in 65–70% and lowering 5-HIAA.",
                ref(
                    "Therapy for Carcinoid Syndrome and Carcinoid Heart Disease",
                    "Therefore, long-acting first generation SRLs (octreotide or lanreotide) are usually started once the diagnosis of carcinoid syndrome is confirmed.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Carcinoid Syndrome",
                "Before elective resection of a symptomatic midgut NET with carcinoid syndrome, which complication must be screened?",
                [
                    "Carcinoid heart disease with echocardiography",
                    "Primary hyperparathyroidism only",
                    "Adrenal insufficiency from glucocorticoid withdrawal",
                    "Pheochromocytoma in every NET patient",
                ],
                0,
                "CHD affects 20–50% of carcinoid syndrome patients and is a major prognostic factor requiring dedicated screening.",
                ref(
                    "Carcinoid Syndrome",
                    "All patients with carcinoid syndrome should be screened for CHD because this is a major prognostic factor limiting 3-year survival by 30% when left untreated.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Insulinoma",
                "Recurrent neuroglycopenia with glucose 1.8 mmol/L, insulin 8 μU/mL, and C-peptide 0.4 nmol/L during 72-hour fast. Next step?",
                [
                    "Tumor localization and surgical resection when localized",
                    "Start empiric diazoxide without imaging",
                    "Diagnose factitious insulin injection",
                    "Treat as nesidioblastosis without further workup",
                ],
                0,
                "Documented hyperinsulinemic hypoglycemia with elevated C-peptide confirms organic insulinoma requiring localization and surgery when feasible.",
                ref(
                    "Insulinoma Markers and Testing",
                    "Concomitant C-peptide levels  $ \\geq 0.2 $ nmol/L and/or concomitant pro-insulin levels  $ \\geq 5 $ pmol/L (in the presence of a hypoglycemia) are suggestive of an insulinoma.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Gastrinoma",
                "Fasting gastrin 1200 pg/mL (10× ULN) with gastric pH 1.5 off PPI for 1 week. Diagnosis?",
                [
                    "Zollinger-Ellison syndrome (gastrinoma)",
                    "Helicobacter pylori peptic ulcer disease only",
                    "Autoimmune atrophic gastritis without NET",
                    "VIPoma with achlorhydria",
                ],
                0,
                "FSG ≥10× ULN with gastric pH ≤2 establishes gastrinoma/ZES when retained antrum is excluded.",
                ref(
                    "Gastrinoma Markers and Testing",
                    "The following criteria are established for confirming the diagnosis of gastrinoma: fasting serum hypergastrinemia (FSG) ≥10-times upper limit of reference range (≥10 × ULN) in combination with gastric pH ≤2 (retained antrum excluded by history).",
                ),
            ),
            mcq(
                f"{p}-m7",
                "VIPoma",
                "Profuse watery diarrhea (>6 L/day), hypokalemia, and suppressed gastric acid in a middle-aged adult suggest:",
                [
                    "VIPoma (Verner-Morrison/WDHA syndrome)",
                    "Carcinoid syndrome from midgut NET",
                    "Gastrinoma with acid hypersecretion",
                    "Somatostatinoma with gallstones as sole feature",
                ],
                0,
                "Large-volume secretory diarrhea with hypokalemia and achlorhydria defines VIPoma/WDHA syndrome.",
                ref(
                    "VIPoma",
                    "Patients with VIPomas experience profuse large volumes (6–8 L) of watery (secretory) diarrhea leading to severe electrolyte disturbances caused by loss of stool bicarbonate and potassium (see Box 43.1).",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Glucagonoma",
                "A diabetic patient with weight loss, stomatitis, and annular erythematous skin lesions most likely has:",
                [
                    "Glucagonoma with necrolytic migratory erythema",
                    "Insulinoma with Whipple triad",
                    "Carcinoid syndrome with flushing only",
                    "Nonfunctioning panNEN without hormonal syndrome",
                ],
                0,
                "NME occurs in ~80% of glucagonoma patients alongside catabolic diabetes and weight loss.",
                ref(
                    "Glucagonoma",
                    "However, the most distinct feature of the glucagonoma syndrome occurring in approximately 80% of patients is necrolytic migratory erythema of the skin",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Circulating Biomarkers",
                "Which statement best describes chromogranin A in NEN care?",
                [
                    "Useful for follow-up after diagnosis but unsuitable as first-line screening",
                    "Highly specific (>90%) for detecting early NEN in asymptomatic adults",
                    "Unaffected by PPI therapy or renal failure",
                    "Replaces histology for initial diagnosis",
                ],
                0,
                "CgA accuracy is 60–90% after diagnosis is established; low specificity and PPI confounding limit screening utility.",
                ref(
                    "Circulating Biomarkers",
                    "CgA is unsuitable as a first-line diagnostic or screening tool.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "NETest and Other Blood-Based Tumor Markers",
                "A NET patient on lanreotide has equivocal chromogranin A. Alternative blood-based tool with high sensitivity?",
                [
                    "NETest multianalyte gene transcript assay",
                    "Serum calcitonin",
                    "Fasting glucose alone",
                    "Urinary cortisol",
                ],
                0,
                "NETest measures 51 NEN-specific transcripts with 90–99% sensitivity and is not hampered by SRL or PPI therapy.",
                ref(
                    "NETest and Other Blood-Based Tumor Markers",
                    "Furthermore, it is not hampered by concomitant treatment with PPIs and/or SRLs.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Somatostatin Receptor Imaging",
                "Staging a well-differentiated metastatic small-bowel NET before PRRT. Preferred molecular imaging?",
                [
                    "68Ga-DOTA somatostatin receptor PET/CT",
                    "18FDG PET alone without anatomic correlation",
                    "Bone scan only",
                    "Abdominal ultrasound as sole staging modality",
                ],
                0,
                "68Ga-DOTA-SRL PET/CT has replaced OctreoScan for SRI and guides PRRT patient selection via uptake quantification.",
                ref(
                    "Somatostatin Receptor Imaging",
                    "SRI with ¹¹¹In-pentetreotide along with SPECT (OctreoScan) was used in the past but has been replaced by ⁶⁸Ga-DOTA-SRLs along with positron emission tomography (PET)/CT or PET/MRI",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Other Imaging Tracers",
                "A localized insulinoma is negative on 68Ga-DOTATATE PET. Next preferred imaging tracer?",
                [
                    "68Ga-DOTA-exendin-4 PET/CT",
                    "18FDG PET as first choice for all insulinomas",
                    "Thyroid scintigraphy with radioiodine",
                    "No further imaging—insulinoma excluded",
                ],
                0,
                "Only ~50% of localized insulinomas express SST2; 68Ga-exendin-4 PET is preferred when SRL imaging is negative.",
                ref(
                    "Other Imaging Tracers",
                    "In such cases, imaging with  $ {}^{68}Ga $-DOTA-exendin-4 is preferred",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Somatostatin Receptor Ligands",
                "Progressive metastatic midgut G1 NET after observation only. First-line antiproliferative therapy per PROMID?",
                [
                    "Octreotide LAR 30 mg IM every 4 weeks",
                    "Sunitinib 37.5 mg daily as first-line",
                    "Platinum-etoposide chemotherapy",
                    "Everolimus without prior SRL trial",
                ],
                0,
                "PROMID established octreotide LAR as first-line antiproliferative therapy prolonging TTP in metastatic midgut NET.",
                ref(
                    "Somatostatin Receptor Ligands",
                    "In the PROMID trial, midgut NEN patients treated with monthly injections of 30 mg octreotide LAR IM had a significantly prolonged time to progression (TTP) (median 14.3 months) compared with placebo-treated patients (median 6.0 months).",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Somatostatin Receptor Ligands",
                "Metastatic GEP G2 NET progressing on observation. First-line therapy per CLARINET approval?",
                [
                    "Lanreotide autogel 120 mg deep SC every 4 weeks",
                    "Octreotide 100 μg SC three times daily only (no LAR)",
                    "Immediate 177Lu-DOTATATE without prior SRL",
                    "Streptozotocin-doxorubicin as mandatory first line",
                ],
                0,
                "CLARINET demonstrated lanreotide PFS benefit and led to approval as first-line for G1–2 GEP NET.",
                ref(
                    "Somatostatin Receptor Ligands",
                    "In the CLARINET trial, GEP NEN patients treated with 120 mg lanreotide monthly deep SC had a median PFS of 32.8 months compared with 18.0 months in placebo-treated patients.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Radionuclide Therapy",
                "Midgut G2 NET progressed on octreotide LAR 30 mg/month. Evidence-based second-line systemic option?",
                [
                    "177Lu-DOTATATE PRRT (NETTER-1 paradigm)",
                    "High-dose PPI therapy",
                    "Metformin for tumor cytoreduction",
                    "Thyroid hormone suppression",
                ],
                0,
                "177Lu-DOTATATE is approved second/third-line after SRL progression; NETTER-1 showed 79% lower PD/death risk versus high-dose octreotide.",
                ref(
                    "Radionuclide Therapy",
                    "The risk of progressive disease (PD) or death was 79% lower in patients treated with PRRT with  $ ^{177} $Lu-DOTATATE in combination with octreotide LAR 30 mg/4 weeks than those treated with a double-dose (60 mg/4 weeks) octreotide LAR.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Everolimus",
                "Progressive nonfunctional pancreatic G2 NET after SRL. Approved targeted second-line therapy?",
                [
                    "Everolimus 10 mg daily",
                    "Levothyroxine suppression",
                    "Metformin monotherapy",
                    "Bisphosphonate infusion only",
                ],
                0,
                "RADIANT-3 showed everolimus PFS 11.0 vs 4.6 months in advanced panNEN, supporting second-line use.",
                ref(
                    "Everolimus",
                    "In advanced G1-2 panNEN patients with PD, everolimus treatment (10 mg/day) increased PFS to 11.0 months compared to 4.6 months in the placebo group.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Sunitinib",
                "Progressive well-differentiated pancreatic G2 NET after SRL. TKI with demonstrated PFS benefit in panNEN?",
                [
                    "Sunitinib 37.5 mg daily",
                    "Imatinib 400 mg daily without trial evidence in NEN",
                    "Sorafenib as standard first-line for all GI NET",
                    "Cabozantinib as sole approved panNEN drug",
                ],
                0,
                "Sunitinib prolonged PFS to ~11–13 months versus ~5–6 months placebo in progressive panNEN.",
                ref(
                    "KEY POINTS",
                    "sunitinib is approved as second-line therapy in patients with G1-2 pancreatic NET.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Chemotherapy",
                "Poorly differentiated G3 pancreatic NEC with high Ki-67 and rapid progression. Typical first-line systemic approach?",
                [
                    "Platinum-based chemotherapy regimen",
                    "Octreotide LAR monotherapy",
                    "Watchful waiting for 12 months",
                    "Diazoxide for hypoglycemia prevention",
                ],
                0,
                "Cytotoxic chemotherapy is reserved for NEC; platinum-based regimens historically constitute first-line for NEC.",
                ref(
                    "Chemotherapy",
                    "In NEC, platinum-based regimens historically constitute the first line of choice.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Chemotherapy",
                "Metastatic well-differentiated G2 pancreatic NET with MGMT-deficient tumor. Preferred alkylating regimen?",
                [
                    "Temozolomide plus capecitabine",
                    "Octreotide alone without chemotherapy",
                    "High-dose PPI",
                    "Insulin infusion",
                ],
                0,
                "Temozolomide/capecitabine is superior and less toxic than older STZ combinations; MGMT deficiency predicts response.",
                ref(
                    "Chemotherapy",
                    "More recently, it was shown that temozolomide in combination with capecitabine is superior and less toxic.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Genetic Syndromes With NENs",
                "A young adult with MEN1 and multifocal small duodenal gastrinomas develops gastric NETs. These are best classified as:",
                [
                    "Type 2 gastric NEN from gastrin-driven ECL proliferation",
                    "Type 1 gastric NEN from autoimmune gastritis",
                    "Type 3 sporadic solitary gastric NET",
                    "Type 4 poorly differentiated gastric NEC",
                ],
                0,
                "Type 2 gastric NENs arise from chronic gastrin stimulation by gastrinoma, classically in MEN1.",
                ref(
                    "Introduction",
                    "Type 2 gastric NENs develop due to chronic stimulation by gastrin from a gastrin-secreting NEN (gastrinoma) in the context of the multiple endocrine neoplasia type 1 (MEN1) syndrome.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Genetic Syndromes With NENs",
                "Multiple insulinomas without MEN1 in a kindred with diabetes. Associated germline mutation?",
                [
                    "MAFA (insulinomatosis syndrome)",
                    "RET Met918Thr",
                    "GNAS mosaic activating variant",
                    "PRKAR1A in Carney complex",
                ],
                0,
                "Autosomal dominant insulinomatosis links to MAFA mutations causing multiple insulin-secreting panNENs.",
                ref(
                    "Genetic Syndromes With NENs",
                    "In patients with an autosomal dominant syndrome characterized by insulinomatosis (multiple insulinomas) of the pancreas, the MAF BZIP transcription factor A (MAFA) mutation (MIM number 147630) was found.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Therapy for Carcinoid Syndrome and Carcinoid Heart Disease",
                "SRL-refractory carcinoid diarrhea persists. Add-on therapy that reduces stool frequency without improving flushing?",
                [
                    "Telotristat ethyl (serotonin synthesis inhibitor)",
                    "High-dose PPI",
                    "Diazoxide",
                    "Insulin infusion",
                ],
                0,
                "Telotristat ethyl alleviates SRL-refractory diarrhea but has no significant effect on flushing.",
                ref(
                    "Therapy for Carcinoid Syndrome and Carcinoid Heart Disease",
                    "Telotristat ethyl is a serotonin synthesis inhibitor that alleviates SRL-refractory diarrhea episodes, but it has no significant effects on flushing episodes",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Management",
                "Asymptomatic 1.5 cm nonfunctioning panNEN in a VHL mutation carrier. Reasonable initial management?",
                [
                    "Surveillance without immediate resection",
                    "Mandatory total pancreatectomy",
                    "Start everolimus on diagnosis",
                    "Empiric chemotherapy",
                ],
                0,
                "Nonfunctioning panNENs ≤2 cm in MEN1/VHL may be followed without mandatory resection per prospective/retrospective data.",
                ref(
                    "Management",
                    "nonfunctioning panNENs with a diameter  $ \\leq $2 cm do not necessarily need to be resected and can undergo careful follow-up.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "18F-Fluorodeoxyglucose PET",
                "A poorly differentiated thoracic NEC with high proliferative index needs staging. Preferred PET tracer?",
                [
                    "18FDG PET/CT",
                    "68Ga-DOTATATE PET alone without FDG",
                    "Radioiodine thyroid scan",
                    "Gallium-67 citrate scan only",
                ],
                0,
                "18FDG PET/CT and PET/MRI are imaging modalities of choice for G3 NETs and NECs.",
                ref(
                    "18F-Fluorodeoxyglucose PET",
                    " $ ^{18} $FDG PET/CT and PET/MRI are the imaging modalities of choice for G3 NETs and NECs.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Therapy for Carcinoid Syndrome and Carcinoid Heart Disease",
                "Perioperative management of symptomatic carcinoid syndrome undergoing tumor debulking. Historical guideline recommendation?",
                [
                    "Perioperative IV octreotide bolus/infusion to prevent carcinoid crisis",
                    "Withhold all somatostatin analogs perioperatively",
                    "Routine beta-blocker monotherapy without alpha-blockade",
                    "High-dose PPI as sole prophylaxis",
                ],
                0,
                "Immediate-release octreotide is indicated peri-interventionally to prevent carcinoid crisis; guidelines still recommend this despite ongoing debate.",
                ref(
                    "Therapy for Carcinoid Syndrome and Carcinoid Heart Disease",
                    "At present, the immediate-release, short-acting form of octreotide is indicated in the management of refractory carcinoid syndrome as an adjunct to longer-acting formulations, or in the treatment of carcinoid crisis and in the peri-interventional setting to prevent the occurrence of carcinoid crisis.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Genetic Syndromes With NENs",
                "PanNENs and ampullary somatostatinomas in a patient with café-au-lait spots and cutaneous neurofibromas suggest:",
                [
                    "Neurofibromatosis type 1 (NF1)",
                    "Von Hippel-Lindau disease only",
                    "McCune-Albright syndrome",
                    "MEN2 with medullary thyroid carcinoma",
                ],
                0,
                "NF1 patients can develop ampullary somatostatinomas and panNENs alongside classic NF1 stigmata.",
                ref(
                    "Genetic Syndromes With NENs",
                    "Ampullary-type duodenal somatostatinomas and panNENs can be diagnosed in patients with neurofibromatosis 1 (MIM number 162200).",
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
                "The WHO 2022 classification distinguishes G1, G2, and G3 NET from NEC for gastroenteropancreatic and lung NENs.",
                True,
                "KEY POINTS explicitly state the 2022 WHO G1/G2/G3 NET and NEC framework guides clinical management.",
                ref(
                    "KEY POINTS",
                    "The World Health Organization (WHO) classification system (2022) of neuroendocrine tumors (NETs; G1 NET, G2 NET, and G3 NET) and neuroendocrine carcinoma (NEC) is informative and necessary for the clinical management of gastroenteropancreatic and lung neuroendocrine neoplasms.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Carcinoid Syndrome",
                "Carcinoid syndrome occurs in approximately 20% to 30% of patients with liver and/or bone metastases from midgut or bronchopulmonary NENs.",
                True,
                "Carcinoid syndrome is present in ~20–30% of patients with liver/bone metastases from these primaries.",
                ref(
                    "Carcinoid Syndrome",
                    "Carcinoid syndrome is present in approximately 20% to 30% of patients with liver and/or bone metastases from these tumors.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Functioning Pancreatic Neuroendocrine Neoplasms—PanNENs",
                "Nonfunctioning panNENs account for 60% to 80% of all pancreatic NEN cases.",
                True,
                "NF-panNENs are the majority of panNENs; insulinomas and gastrinomas are the commonest functioning types.",
                ref(
                    "Functioning Pancreatic Neuroendocrine Neoplasms—PanNENs",
                    "Nonfunctioning panNENs (NF-panNENs) make up 60% to 80% of all panNEN cases.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Circulating Biomarkers",
                "Chromogranin A specificity for NEN exceeds 90% in unselected screening populations.",
                False,
                "CgA specificity is low (<35%) because many non-NEN conditions elevate levels.",
                ref(
                    "Circulating Biomarkers",
                    "CgA specificity is low (<35%) because elevated levels can be found in many other conditions, including other neoplasms, cardiac and inflammatory diseases, renal failure, atrophic gastritis, and PPI or H2-blocker administration.",
                ),
            ),
            tf(
                f"{p}-t5",
                "NETest and Other Blood-Based Tumor Markers",
                "NETest performance is hampered by concurrent PPI and somatostatin analog therapy.",
                False,
                "NETest is specifically not confounded by PPIs or SRLs unlike CgA.",
                ref(
                    "NETest and Other Blood-Based Tumor Markers",
                    "Furthermore, it is not hampered by concomitant treatment with PPIs and/or SRLs.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Somatostatin Receptor Ligands",
                "In PROMID, octreotide LAR prolonged time to progression compared with placebo in metastatic midgut NET.",
                True,
                "Median TTP was 14.3 vs 6.0 months favoring octreotide LAR.",
                ref(
                    "Somatostatin Receptor Ligands",
                    "In the PROMID trial, midgut NEN patients treated with monthly injections of 30 mg octreotide LAR IM had a significantly prolonged time to progression (TTP) (median 14.3 months) compared with placebo-treated patients (median 6.0 months).",
                ),
            ),
            tf(
                f"{p}-t7",
                "Everolimus",
                "Everolimus is approved as second-line therapy for unresectable G1–2 gastroenteropancreatic and bronchopulmonary NET.",
                True,
                "RADIANT trials support everolimus as approved second-line in G1–2 GEP and BP NET.",
                ref(
                    "Everolimus",
                    "The mTOR inhibitor everolimus is an approved second-line therapy in patients with unresectable G1-2 GEP and BP NEN.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Chemotherapy",
                "Well-differentiated G1–2 small intestinal NET typically shows excellent response to cytotoxic chemotherapy.",
                False,
                "Chemotherapy has very poor response in well-differentiated G1–2 GI NET; panNEN and NEC behave differently.",
                ref(
                    "Chemotherapy",
                    "Chemotherapy has a very poor response rate in well-differentiated (G1-2) GI NEN.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Introduction",
                "Type 3 gastric NENs are sporadic solitary tumors that arise without elevated gastrin and behave aggressively.",
                True,
                "Type 3 gastric NETs are sporadic, non-gastrin-driven, and biologically aggressive despite well-differentiated morphology.",
                ref(
                    "Introduction",
                    "Type 3 gastric NENs are sporadic, solitary NENs, which develop in the absence of elevated gastrin levels and have an aggressive biologic behavior despite their well-differentiated morphology.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Genetic Syndromes With NENs",
                "Fifty percent of MEN1 patients harbor pancreatic neuroendocrine tumors.",
                True,
                "PanNENs are highly prevalent in MEN1, alongside duodenal and other foregut NENs.",
                ref(
                    "Functioning Pancreatic Neuroendocrine Neoplasms—PanNENs",
                    "Fifty percent of MEN1 patients harbor panNENs.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Radionuclide Therapy",
                "PRRT with 177Lu-DOTATATE can reduce hormonal hypersecretion in functioning GEP NEN.",
                True,
                "PRRT has antiproliferative and symptomatic benefits including hormone reduction in functioning tumors.",
                ref(
                    "Radionuclide Therapy",
                    "Apart from its effects on tumor progression, PRRT with  $ ^{177} $Lu-DOTATATE can further result in reduction of hormonal hypersecretion in hormone-producing GEP NEN.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Therapy for Insulinoma",
                "Somatostatin analog therapy for insulinoma should preferably be initiated in hospital because it may worsen hypoglycemia.",
                True,
                "SRLs can lower counterregulatory hormones and aggravate hypoglycemia—inpatient short-acting SRL initiation is preferred.",
                ref(
                    "Therapy for Insulinoma",
                    "SRL treatment of insulinoma patients should therefore preferably be started in an in-hospital setting with administration of an immediate-release, short-acting SRL formulation.",
                ),
            ),
            tf(
                f"{p}-t13",
                "KEY POINTS",
                "Genetic syndromes associated with NENs include MEN1, VHL, NF1, and insulinomatosis.",
                True,
                "KEY POINTS list MEN1, MEN4, VHL, NF1, Pacak-Zhuang, Mahvash, and insulinomatosis among NEN predisposition syndromes.",
                ref(
                    "KEY POINTS",
                    "Genetic syndromes associated with neuroendocrine neoplasms include multiple endocrine neoplasia type 1, multiple endocrine neoplasia type 4, von Hippel-Lindau disease, neurofibromatosis 1, the Pacak-Zhuang syndrome, Mahvash disease, and insulinomatosis.",
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
                "Assertion: Somatostatin receptor ligands are approved first-line therapy for functioning and nonfunctioning GEP NET.",
                "Reason: SRLs are approved only for poorly differentiated NEC and never for well-differentiated NET.",
                2,
                "Assertion true—KEY POINTS approve SRLs for G1–G3 functioning/nonfunctioning GEP NET; reason false—SRLs are cornerstone of well-differentiated NET care.",
                ref(
                    "KEY POINTS",
                    "Somatostatin receptor ligands are approved first-line therapies for patients with functioning (hormone-secreting) and nonfunctioning gastroenteropancreatic neuroendocrine tumors (G1 NET, G2 NET, and G3 NET).",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Carcinoid Syndrome",
                "Assertion: Carcinoid syndrome features flushing and secretory diarrhea.",
                "Reason: Carcinoid syndrome occurs only when the primary tumor is confined to the liver without extrahepatic disease.",
                2,
                "Assertion true—classic carcinoid syndrome symptoms; reason false—symptoms require bypass of portal metabolism, not isolated hepatic primaries only.",
                ref(
                    "Carcinoid Syndrome",
                    "The carcinoid syndrome is characterized by frequent watery (secretory) diarrhea and flushing and is occasionally also associated with wheezing",
                ),
            ),
            ar(
                f"{p}-ar3",
                "NEN Pathology",
                "Assertion: G3 NET and G3 NEC differ in differentiation and clinical behavior.",
                "Reason: All G3 lesions are poorly differentiated NEC by definition.",
                2,
                "Assertion true—G3 splits into well-differentiated NET vs poorly differentiated NEC; reason false—G3 NET exists as a distinct entity.",
                ref(
                    "NEN Pathology",
                    "G3 is further divided into two different groups depending on tumor differentiation, with G3 neuroendocrine tumor (NET) having well-differentiated tumor cells and (G3) neuroendocrine carcinoma (NEC) having poorly differentiated tumor cells",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Somatostatin Receptor Imaging",
                "Assertion: 68Ga-DOTA somatostatin receptor PET is used for NEN staging and PRRT selection.",
                "Reason: Somatostatin receptors are absent on all neuroendocrine neoplasms.",
                2,
                "Assertion true—SRI is theranostic for staging and PRRT; reason false—SSTs are widely expressed on NENs.",
                ref(
                    "Somatostatin Receptor Imaging",
                    "The rationale of performing somatostatin receptor imaging (SRI) is based on the widespread expression of SSTs by NENs",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Radionuclide Therapy",
                "Assertion: NETTER-1 showed 177Lu-DOTATATE reduced progressive disease or death versus high-dose octreotide.",
                "Reason: PRRT was compared against placebo alone without any somatostatin analog background.",
                2,
                "Assertion true—79% lower PD/death with 177Lu-DOTATATE plus octreotide LAR 30 mg; reason false—control arm received double-dose octreotide LAR 60 mg.",
                ref(
                    "Radionuclide Therapy",
                    "The risk of progressive disease (PD) or death was 79% lower in patients treated with PRRT with  $ ^{177} $Lu-DOTATATE in combination with octreotide LAR 30 mg/4 weeks than those treated with a double-dose (60 mg/4 weeks) octreotide LAR.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Everolimus",
                "Assertion: Everolimus prolongs progression-free survival in advanced G1–2 pancreatic NET.",
                "Reason: Everolimus activates mTOR signaling to accelerate tumor growth.",
                2,
                "Assertion true—RADIANT-3 PFS 11.0 vs 4.6 months; reason false—everolimus inhibits mTOR, it does not activate it.",
                ref(
                    "Everolimus",
                    "In advanced G1-2 panNEN patients with PD, everolimus treatment (10 mg/day) increased PFS to 11.0 months compared to 4.6 months in the placebo group.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Sunitinib",
                "Assertion: Sunitinib is approved for progressive well-differentiated pancreatic NET.",
                "Reason: Sunitinib inhibits VEGFR and other tyrosine kinases relevant to NEN angiogenesis.",
                0,
                "Both true and linked—antiangiogenic TKI activity underlies sunitinib efficacy in vascular panNEN.",
                ref(
                    "Sunitinib",
                    "Sunitinib is an oral multitargeted tyrosine kinase inhibitor (TKI) that inhibits PDGFR, VEGFR1/2, c-KIT, and FLT-3, among others.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Insulinoma",
                "Assertion: Insulinomas can cause severe hypoglycemia through inappropriate insulin secretion.",
                "Reason: Insulinomas always secrete insulin precursors without intact insulin or C-peptide.",
                2,
                "Assertion true—Whipple triad and hyperinsulinemic hypoglycemia define insulinoma; reason false—C-peptide and proinsulin are typically elevated.",
                ref(
                    "Insulinoma",
                    "These NENs usually cause severe hypoglycemia through inappropriately increased secretion of insulin, or insulin precursors.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Gastrinoma",
                "Assertion: MEN1 is found in 20% to 25% of Zollinger-Ellison syndrome patients.",
                "Reason: All gastrinomas arise exclusively in the pancreatic tail without duodenal involvement.",
                2,
                "Assertion true—MEN1 accounts for a substantial fraction of ZES; reason false—50–85% of gastrinomas are duodenal.",
                ref(
                    "Gastrinoma",
                    "MEN1 is found in 20% to 25% of ZES patients.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Chemotherapy",
                "Assertion: Temozolomide-based regimens can benefit selected advanced pancreatic NET.",
                "Reason: Midgut well-differentiated NET and pancreatic NET respond equally to alkylating chemotherapy.",
                2,
                "Assertion true—temozolomide/capecitabine benefits G2 panNEN especially with MGMT deficiency; reason false—panNEN responds more than midgut NET.",
                ref(
                    "Chemotherapy",
                    "This might also explain why panNENs respond to alkylating agents in contrast to midgut NENs.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Genetic Syndromes With NENs",
                "Assertion: Von Hippel-Lindau disease predisposes to pancreatic neuroendocrine tumors.",
                "Reason: VHL is caused by activating RET proto-oncogene mutations.",
                2,
                "Assertion true—panNENs occur in VHL; reason false—VHL is VHL tumor suppressor loss, not RET (MEN2).",
                ref(
                    "Genetic Syndromes With NENs",
                    "PanNENs can also be diagnosed in patients with von Hippel-Lindau disease (VHL, MIM number 193300).",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Carcinoid Syndrome",
                "Assertion: Carcinoid crisis may be fatal if untreated.",
                "Reason: Carcinoid crisis is a benign self-limited flush without hemodynamic consequences.",
                2,
                "Assertion true—crisis causes cardiovascular collapse; reason false—crisis is life-threatening hemodynamic instability.",
                ref(
                    "Carcinoid Syndrome",
                    "if left untreated, it may be fatal.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "43",
        "title": "Neuroendocrine Tumors and Disorders",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Wouter W. de Herder, Richard A. Feelders, and Johannes Hofland",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_43_Neuroendocrine_Tumors_and_Disorders.md",
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
