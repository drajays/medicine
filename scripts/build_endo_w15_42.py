#!/usr/bin/env python3
"""Generate Williams 15e module w15-42 — Endocrine Neoplasia Syndromes."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-42"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-42_Endocrine_Neoplasia_Syndromes.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why MEN syndromes mandate systematic genetic evaluation",
                "MEN and MEON syndromes are autosomal-dominant (except mosaic MAS) multisystem tumor predispositions; early genetic diagnosis enables cascade testing and presymptomatic surveillance.",
                ref(
                    "KEY POINTS",
                    "Genetic testing should be offered to the majority of patients suspected of having a MEN or MEON syndrome.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How mutation carriers enter tumor surveillance",
                "Germline pathogenic variants identify at-risk relatives who need periodic clinical, biochemical, and radiologic screening for early tumor detection and treatment.",
                ref(
                    "KEY POINTS",
                    "Individuals harboring a mutation, who are at risk of developing tumors, should be offered periodic clinical, biochemical, and/or radiologic screening for the early detection and treatment of tumors.",
                ),
            ),
            note(
                f"{p}-n3",
                "Multiple Endocrine Neoplasia Type 1 (MEN1)",
                "Why hyperparathyroidism usually presents first in MEN1",
                "PHPT is the commonest and typically earliest MEN1 manifestation (75–90% first), though childhood insulinoma or pituitary tumors can antedate it.",
                ref(
                    "KEY POINTS",
                    "Parathyroid tumors are typically the first manifestation of disease in 75% to 90% of patients with MEN1",
                ),
            ),
            note(
                f"{p}-n4",
                "Multiple Endocrine Neoplasia Type 1 (MEN1)",
                "How menin loss drives the MEN1 tumor triad",
                "Germline MEN1 mutations encode the nuclear tumor suppressor menin; biallelic inactivation in parathyroid, pituitary, and duodenopancreatic tissue underlies the classic MEN1 phenotype.",
                ref(
                    "KEY POINTS",
                    "MEN1 is characterized by the occurrence of parathyroid, anterior pituitary, and duodenopancreatic neuroendocrine tumors and is caused by mutations of the MEN1 gene, which encodes the tumor-suppressor protein menin.",
                ),
            ),
            note(
                f"{p}-n5",
                "Parathyroid Tumors",
                "How MEN1 parathyroid surgery differs from sporadic PHPT",
                "All four glands are usually involved; bilateral exploration with subtotal (≥3.5 gland) or total parathyroidectomy plus transcervical thymectomy balances cure against hypoparathyroidism.",
                ref(
                    "Parathyroid Tumors",
                    "Most experts agree that bilateral neck exploration with subtotal parathyroidectomy (i.e., of at least 3.5 glands) with concomitant transcervical thymectomy is the preferred operation that strikes the best balance of achieving long-term eucalcemia.",
                ),
            ),
            note(
                f"{p}-n6",
                "Pancreatic Neuroendocrine Tumors",
                "Why pancreatic NETs dominate MEN1 mortality",
                "Duodenopancreatic NETs (functioning and nonfunctioning) cause the greatest premature death in MEN1, especially malignant gastrinomas and thymic NETs.",
                ref(
                    "Pancreatic Neuroendocrine Tumors",
                    "Pancreatic NETs remain the leading cause of premature death in patients with MEN1.",
                ),
            ),
            note(
                f"{p}-n7",
                "Gastrinoma",
                "How PPI therapy changed MEN1 gastrinoma outcomes",
                "Proton pump inhibitors suppress acid hypersecretion in Zollinger-Ellison syndrome, dramatically reducing ulcer-related morbidity when curative resection of multiple small duodenal gastrinomas is impractical.",
                ref(
                    "Gastrinoma",
                    "These therapies represent the mainstay of treatment for controlling symptoms and have resulted in a marked reduction in the morbidity and mortality previously associated with ZES in patients with MEN1.",
                ),
            ),
            note(
                f"{p}-n8",
                "Genetic Testing and Tumor Surveillance",
                "Why proactive MEN1 cascade testing reduces morbidity",
                "Delayed genetic diagnosis in first-degree relatives allows preventable tumors to present symptomatically; early mutation testing triggers guideline-based biochemical and imaging surveillance.",
                ref(
                    "Genetic Testing and Tumor Surveillance",
                    "Indeed, delays in the genetic diagnosis of first-degree relatives of an affected index case are reported to result in increased morbidity, highlighting the need for proactive cascade testing within MEN1 kindreds.",
                ),
            ),
            note(
                f"{p}-n9",
                "MEN1 Phenocopies and Mutations in Other Genes",
                "How AIP mutations mimic MEN1 pituitary disease",
                "~5–10% of apparent MEN1 kindreds are phenocopies; germline AIP variants cause familial isolated pituitary adenoma (FIPA) and may present with pituitary tumors without MEN1 mutations.",
                ref(
                    "MEN1 Phenocopies and Mutations in Other Genes",
                    "AIP, which encodes the aryl hydrocarbon receptor interacting protein, mutations of which are associated with familial isolated pituitary adenoma (FIPA).",
                ),
            ),
            note(
                f"{p}-n10",
                "Multiple Endocrine Neoplasia Type 2 (MEN2) and Type 3 (MEN3)",
                "Why RET genotype dictates MTC aggressiveness",
                "Constitutively active RET receptor tyrosine kinase signaling from germline mutations causes medullary thyroid carcinoma; ATA highest-/high-/moderate-risk categories guide prophylactic thyroidectomy timing.",
                ref(
                    "Multiple Endocrine Neoplasia Type 2 (MEN2) and Type 3 (MEN3)",
                    "MEN2 and MEN3 are due to RET proto-oncogene mutations that lead to constitutive activation of the encoded receptor tyrosine kinase (TK).",
                ),
            ),
            note(
                f"{p}-n11",
                "Prophylactic Thyroidectomy in MEN2",
                "How early thyroidectomy prevents hereditary MTC",
                "RET mutation testing identifies presymptomatic carriers; prophylactic total thyroidectomy in childhood eliminates or markedly reduces advanced MTC when timed to ATA risk category.",
                ref(
                    "Prophylactic Thyroidectomy in MEN2",
                    "For example, in 2005 a study reported that prophylactic thyroidectomy in 50 patients, who were <19 years of age with MEN2-associated RET mutations, resulted in no evidence of residual or recurrent disease in ~90% of cases at a mean follow-up period of 7 years.",
                ),
            ),
            note(
                f"{p}-n12",
                "Medullary Thyroid Cancer (MTC)",
                "Why pheochromocytoma must be excluded before thyroid surgery",
                "Synchronous MTC and pheochromocytoma are common in MEN2/MEN3; undiagnosed catecholamine excess can precipitate intraoperative hypertensive crisis during thyroidectomy.",
                ref(
                    "Medullary Thyroid Cancer (MTC)",
                    "Finally, for the investigation of MTC, it is important to undertake RET germline genetic testing in all patients, and for those who have a mutation (or for those in whom there is likely to be a significant delay in testing), the presence of pheochromocytoma and PHPT should be excluded before surgery.",
                ),
            ),
            note(
                f"{p}-n13",
                "Pheochromocytoma",
                "How MEN2 pheochromocytoma differs biochemically from VHL",
                "MEN2-associated tumors are adrenergic with disproportionate epinephrine/metanephrine secretion, whereas VHL and SDHx familial paraganglioma syndromes favor norepinephrine profiles.",
                ref(
                    "Pheochromocytoma",
                    "MEN2-associated pheochromocytomas are typically adrenergic and are reported to secrete disproportionate amounts of epinephrine, and elevated epinephrine (and associated metanephrine) concentrations may help distinguish MEN2 from other hereditary pheochromocytoma/paraganglioma syndromes, such as VHL and familial paraganglioma syndromes,",
                ),
            ),
            note(
                f"{p}-n14",
                "Pheochromocytoma",
                "Why bilateral adrenal disease complicates MEN2 surgery",
                "Bilateral synchronous or metachronous pheochromocytomas occur in ~50% of MEN2 patients; adrenal-sparing subtotal resection may preserve cortical function but requires lifelong surveillance.",
                ref(
                    "Pheochromocytoma",
                    "A key characteristic of MEN2-associated pheochromocytoma is that in 50% of patients, they occur as bilateral disease, which can occur synchronously or metachronously.",
                ),
            ),
            note(
                f"{p}-n15",
                "Multiple Endocrine Neoplasia Type 2 (MEN2) and Type 3 (MEN3)",
                "How MEN3 phenotype extends beyond endocrine tumors",
                "MEN2B/MEN3 combines aggressive MTC and pheochromocytoma with marfanoid habitus, mucosal neuromas, medullated corneal fibers, and intestinal ganglioneuromatosis—often from de novo RET Met918Thr mutations.",
                ref(
                    "Multiple Endocrine Neoplasia Type 2 (MEN2) and Type 3 (MEN3)",
                    "MEN3, also referred to as MEN2B, is characterized by the occurrence of MTC and pheochromocytoma without PHPT but in association with a marfanoid habitus, mucosal neuromas, medullated corneal fibers, and intestinal autonomic ganglion dysfunction leading to mega-colon (Fig. 42.6).",
                ),
            ),
            note(
                f"{p}-n16",
                "Von Hippel-Lindau Syndrome (VHL)",
                "Why VHL spans vascular and solid-organ neoplasia",
                "Germline VHL loss causes retinal/CNS hemangioblastomas, RCC, pancreatic cysts/NETs, pheochromocytoma, and ELSTs—often manifesting in the second to third decade with near-complete penetrance by age 75.",
                ref(
                    "Von Hippel-Lindau Syndrome (VHL)",
                    "The cardinal clinical features of VHL include hemangioblastomas of the retina and central nervous system (CNS), renal cysts and renal cell carcinomas (RCCs), pancreas cysts and pancreatic NETs, pheochromocytomas (and less commonly paragangliomas), epididymal and broad ligament cysts, and endolymphatic sac tumors (ELSTs).",
                ),
            ),
            note(
                f"{p}-n17",
                "Molecular Genetics",
                "How mutant pVHL drives HIF-mediated tumorigenesis",
                "Loss of functional pVHL prevents normoxic degradation of HIF-α, causing constitutive expression of angiogenic and metabolic target genes including VEGF.",
                ref(
                    "Molecular Genetics",
                    "In the presence of mutant (or absent) pVHL, aberrant stabilization of HIF-1 $ \\alpha $ (and HIF-2 $ \\alpha $) occurs even under normoxic conditions, giving rise to the inappropriate expression of hundreds of HIF target genes.",
                ),
            ),
            note(
                f"{p}-n18",
                "Genetic Testing and Tumor Surveillance",
                "How VHL surveillance begins in infancy",
                "Confirmed or suspected VHL carriers receive lifelong multidisciplinary follow-up with annual exams, infant ophthalmology, and staged MRI/metanephrine screening per VHL Alliance schedules.",
                ref(
                    "Genetic Testing and Tumor Surveillance",
                    "Individuals identified to have a clinical diagnosis of VHL or carrying a germline pathogenic VHL variant should be offered an integrated specialist multidisciplinary follow-up that includes periodic surveillance for presymptomatic tumor detection.",
                ),
            ),
            note(
                f"{p}-n19",
                "Neurofibromatosis Type 1 (NF1)",
                "Why NF1 patients need pheochromocytoma vigilance",
                "Although café-au-lait macules and neurofibromas dominate NF1, lifetime pheochromocytoma/paraganglioma risk reaches 0.6–6% with median presentation ~40 years.",
                ref(
                    "Neurofibromatosis Type 1 (NF1)",
                    "Individuals with NF1 have a 0.6% to 6% lifetime risk of developing pheochromocytoma or paraganglioma, with a median age of presentation of ~40 years.",
                ),
            ),
            note(
                f"{p}-n20",
                "Molecular Genetics",
                "How neurofibromin suppresses RAS signaling",
                "NF1 encodes neurofibromin, a RAS-GAP that inactivates RAS-GTP; LOF variants cause neurofibromas, optic pathway gliomas, and endocrine tumors through unchecked RAS-MAPK activity.",
                ref(
                    "Molecular Genetics",
                    "Neurofibromin harbors a RAS-GTPase activating (RAS-GAP) related domain (amino acids 1198–1530) and acts as a negative regulator of RAS by converting the active RAS-GTP bound form to its inactive RAS-GDP form.",
                ),
            ),
            note(
                f"{p}-n21",
                "Carney Complex",
                "Why PPNAD is the hallmark endocrine lesion in CNC",
                "PRKAR1A loss causes primary pigmented nodular adrenal disease with ACTH-independent Cushing—often subtle, periodic, or paradoxically dexamethasone-responsive.",
                ref(
                    "Carney Complex",
                    "ACTH-independent Cushing syndromes resulting from primary pigmented nodular adrenal disease (PPNAD) is the most common endocrine manifestation of CNC, occurring in ~25% to 60% of individuals.",
                ),
            ),
            note(
                f"{p}-n22",
                "Molecular Genetics",
                "How PRKAR1A mutations activate PKA signaling",
                "Inactivating PRKAR1A variants reduce regulatory subunit availability, unleashing PKA catalytic activity and cAMP-driven tumorigenesis in adrenal, pituitary, thyroid, and myxoma tissues.",
                ref(
                    "Molecular Genetics",
                    "Inactivating mutations in PRKAR1A result in constitutive activation of the cAMP/PKA signaling pathway through the increased availability of PKA catalytic subunits.",
                ),
            ),
            note(
                f"{p}-n23",
                "Cowden Syndrome",
                "How SDHx genes link to hereditary paraganglioma risk",
                "Cowden syndrome is genetically heterogeneous; beyond PTEN, pathogenic SDHB/SDHD (SDHX) variants can produce paraganglioma-pheochromocytoma predisposition overlapping PPGL syndromes.",
                ref(
                    "Molecular Genetics",
                    "CS is a genetically heterogeneous disorder, and for those individuals with no pathogenic variant in PTEN, a variety of alternate genetic etiologies may be responsible, including pathogenic variants in genes within the PTEN pathway (e.g., AKT1, PIK3CA) or independent of it (e.g., SDHX, KLLN, SEC23B)",
                ),
            ),
            note(
                f"{p}-n24",
                "McCune-Albright Syndrome",
                "Why MAS is a mosaic GNAS disorder",
                "Postzygotic activating GNAS mutations cause polyostotic fibrous dysplasia, café-au-lait macules, and autonomous endocrine hyperfunction—not inherited in classic Mendelian fashion.",
                ref(
                    "McCune-Albright Syndrome",
                    "MAS is characterized by the triad of fibrous dysplasia, café-au-lait skin pigmentation, and autonomous/excessive function of multiple endocrine glands.",
                ),
            ),
            note(
                f"{p}-n25",
                "McCune-Albright Syndrome",
                "How MAS café-au-lait patches differ from NF1",
                "MAS macules have irregular 'coast of Maine' borders, often stop at the midline, and lie ipsilateral to fibrous dysplasia—contrasting with NF1's smooth 'coast of California' lesions.",
                ref(
                    "McCune-Albright Syndrome",
                    "They can be variable in size; have a characteristic irregular, jagged border (“coast of Maine” appearance); tend not to cross the midline of the body; and most frequently occur ipsilateral to the skeletal lesions.",
                ),
            ),
            note(
                f"{p}-n26",
                "Introduction to the Endocrine Neoplasia Syndromes",
                "How multidisciplinary care optimizes MEN/MEON outcomes",
                "Balancing tumor control against quality of life requires coordinated endocrine, surgical, oncologic, radiologic, and genetic expertise with shared decision-making.",
                ref(
                    "KEY POINTS",
                    "Treatment of MEN and MEON patients, which aims to minimize the disease-associated morbidity and mortality while maintaining the quality of life, requires a multidisciplinary approach.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Multiple Endocrine Neoplasia Type 1 (MEN1)",
                "A 28-year-old with hypercalcemia, elevated PTH, and multigland parathyroid disease also has a prolactinoma and duodenal gastrinoma. Most likely diagnosis?",
                [
                    "Multiple endocrine neoplasia type 1 (MEN1)",
                    "Multiple endocrine neoplasia type 2A (RET mutation)",
                    "Von Hippel-Lindau syndrome",
                    "McCune-Albright syndrome",
                ],
                0,
                "Parathyroid, pituitary, and duodenopancreatic NETs define MEN1 from germline MEN1/menin loss.",
                ref(
                    "KEY POINTS",
                    "MEN1 is characterized by the occurrence of parathyroid, anterior pituitary, and duodenopancreatic neuroendocrine tumors and is caused by mutations of the MEN1 gene, which encodes the tumor-suppressor protein menin.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Parathyroid Tumors",
                "Preferred parathyroid operation for symptomatic MEN1-associated PHPT at most expert centers?",
                [
                    "Bilateral neck exploration with subtotal parathyroidectomy (≥3.5 glands) plus transcervical thymectomy",
                    "Minimally invasive single-gland excision without neck exploration",
                    "Total thyroidectomy",
                    "Observation until calcium exceeds 4.0 mmol/L regardless of symptoms",
                ],
                0,
                "Subtotal parathyroidectomy with thymectomy achieves the best long-term eucalcemia balance in multigland MEN1 disease.",
                ref(
                    "Parathyroid Tumors",
                    "Most experts agree that bilateral neck exploration with subtotal parathyroidectomy (i.e., of at least 3.5 glands) with concomitant transcervical thymectomy is the preferred operation that strikes the best balance of achieving long-term eucalcemia.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Gastrinoma",
                "A MEN1 patient with Zollinger-Ellison syndrome and multiple small duodenal gastrinomas has excellent symptom control on high-dose PPI. Best ongoing strategy?",
                [
                    "Continue PPI therapy with tumor surveillance; surgery reserved for selected larger tumors",
                    "Stop PPI to confirm gastrinoma diagnosis",
                    "Immediate total pancreaticoduodenectomy for all MEN1 gastrinomas",
                    "Thyroidectomy to lower gastrin secretion",
                ],
                0,
                "PPIs are the mainstay for MEN1 gastrinoma symptom control; surgery remains controversial for small multifocal duodenal disease.",
                ref(
                    "Gastrinoma",
                    "These therapies represent the mainstay of treatment for controlling symptoms and have resulted in a marked reduction in the morbidity and mortality previously associated with ZES in patients with MEN1.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Genetic Testing and Tumor Surveillance",
                "An index MEN1 patient with a pathogenic MEN1 variant is identified. Next step for at-risk relatives?",
                [
                    "Offer predictive MEN1 testing to all first-degree relatives regardless of symptoms",
                    "Test relatives only after they develop hypercalcemia",
                    "Screen relatives with annual CT chest only",
                    "Defer all testing until age 50 years",
                ],
                0,
                "Guidelines recommend earliest-possible cascade genetic testing of first-degree relatives of MEN1 mutation carriers.",
                ref(
                    "Genetic Testing and Tumor Surveillance",
                    "Following the genetic diagnosis of MEN1, predictive genetic testing should be offered to all first-degree relatives (see Fig. 42.5), and current guidelines recommend that this should be undertaken at the earliest opportunity.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "MEN1 Phenocopies and Mutations in Other Genes",
                "A kindred with pituitary macroadenomas lacks MEN1 mutations but harbors a germline AIP variant. This represents:",
                [
                    "Familial isolated pituitary adenoma (FIPA) phenocopy",
                    "Confirmed MEN1 with false-negative sequencing",
                    "McCune-Albright syndrome",
                    "Carney complex",
                ],
                0,
                "AIP mutations cause FIPA and are an important MEN1 phenocopy when pituitary disease appears familial without MEN1.",
                ref(
                    "MEN1 Phenocopies and Mutations in Other Genes",
                    "AIP, which encodes the aryl hydrocarbon receptor interacting protein, mutations of which are associated with familial isolated pituitary adenoma (FIPA).",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Multiple Endocrine Neoplasia Type 2 (MEN2) and Type 3 (MEN3)",
                "A child with mucosal neuromas, marfanoid habitus, and elevated calcitonin most likely has:",
                [
                    "MEN3 (MEN2B) with RET Met918Thr mutation",
                    "MEN1 with gastrinoma",
                    "VHL type 1 without pheochromocytoma",
                    "NF1 with optic glioma only",
                ],
                0,
                "MEN2B/MEN3 combines MTC and pheochromocytoma with distinctive mucosal neuromas and skeletal features from activating RET ICD mutations.",
                ref(
                    "KEY POINTS",
                    "MEN3 (also referred to as MEN2B) is characterized by the occurrence of MTC and pheochromocytomas in association with a marfanoid habitus, mucosal neuromas, medullated corneal fibers, and intestinal ganglioneumatosis.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Prophylactic Thyroidectomy in MEN2",
                "An asymptomatic 10-month-old with RET Met918Thr mutation requires:",
                [
                    "Prophylactic total thyroidectomy as soon as possible (ATA highest-risk category)",
                    "Observation until age 30 without calcitonin testing",
                    "Hemithyroidectomy only",
                    "Radioiodine ablation instead of surgery",
                ],
                0,
                "ATA highest-risk RET mutations (Met918Thr) warrant prophylactic thyroidectomy within the first year of life.",
                ref(
                    "Prophylactic Thyroidectomy in MEN2",
                    "Thus, children identified to harbor the ATA highest-risk RET mutations (i.e., Met918Thr) are recommended to undergo total thyroidectomy in the first year of life",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Medullary Thyroid Cancer (MTC)",
                "Before thyroidectomy for MEN2-associated MTC, which coexisting tumor must be excluded?",
                [
                    "Pheochromocytoma (and primary hyperparathyroidism when applicable)",
                    "Pheochromocytoma only after age 60 years",
                    "Pituitary prolactinoma",
                    "Renal cell carcinoma",
                ],
                0,
                "Undiagnosed pheochromocytoma risks fatal intraoperative catecholamine crisis; PHPT should also be excluded in MEN2A.",
                ref(
                    "Medullary Thyroid Cancer (MTC)",
                    "Finally, for the investigation of MTC, it is important to undertake RET germline genetic testing in all patients, and for those who have a mutation (or for those in whom there is likely to be a significant delay in testing), the presence of pheochromocytoma and PHPT should be excluded before surgery.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Pheochromocytoma",
                "Biochemical confirmation of pheochromocytoma in MEN2 relies on:",
                [
                    "Elevated plasma or urinary fractionated metanephrines",
                    "Serum calcitonin alone",
                    "Fasting gastrin",
                    "IGF-1 measurement",
                ],
                0,
                "Plasma/urinary fractionated metanephrines are the diagnostic standard for MEN2-associated pheochromocytoma.",
                ref(
                    "Pheochromocytoma",
                    "The diagnosis of pheochromocytoma is confirmed by demonstrating elevated concentrations of plasma and/or urinary free fractionated metanephrines.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Pheochromocytoma",
                "A MEN2A patient with synchronous bilateral pheochromocytomas wishes to minimize adrenal insufficiency risk. Reasonable surgical option?",
                [
                    "Adrenal-sparing (subtotal) adrenalectomy when technically feasible",
                    "Bilateral complete adrenalectomy without steroid plan",
                    "Medical therapy alone without surgery",
                    "Unilateral adrenalectomy ignoring contralateral tumor",
                ],
                0,
                "Adrenal-sparing surgery leaving 10–30% cortical tissue may preserve glucocorticoid/mineralocorticoid function with acceptable recurrence rates.",
                ref(
                    "Pheochromocytoma",
                    "Adrenal-sparing surgery involves removal of the pheochromocytoma while aiming to leave 10% to 30% residual adrenal cortical tissue to provide sufficient adrenal reserve for glucocorticoid and mineralocorticoid function.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Von Hippel-Lindau Syndrome (VHL)",
                "A 25-year-old with retinal angioma, cerebellar hemangioblastoma, and clear cell RCC most likely has:",
                [
                    "Von Hippel-Lindau syndrome (VHL gene mutation)",
                    "MEN1",
                    "Carney complex",
                    "McCune-Albright syndrome",
                ],
                0,
                "Retinal/CNS hemangioblastomas with RCC are cardinal VHL manifestations from germline VHL loss.",
                ref(
                    "Von Hippel-Lindau Syndrome (VHL)",
                    "The cardinal clinical features of VHL include hemangioblastomas of the retina and central nervous system (CNS), renal cysts and renal cell carcinomas (RCCs)",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Von Hippel-Lindau Syndrome (VHL)",
                "VHL-associated pheochromocytomas characteristically secrete predominantly:",
                [
                    "Norepinephrine (noradrenaline)",
                    "Epinephrine exclusively without norepinephrine",
                    "Serotonin",
                    "ACTH",
                ],
                0,
                "VHL pheochromocytomas are biochemically noradrenergic, distinguishing them from MEN2 adrenergic tumors.",
                ref(
                    "Von Hippel-Lindau Syndrome (VHL)",
                    "Biochemically, the pheochromocytomas in VHL disease secrete predominantly nor-epinephrine",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Neurofibromatosis Type 1 (NF1)",
                "Revised NF1 diagnostic criteria (2021) include which feature?",
                [
                    "≥6 café-au-lait macules (≥5 mm prepubertal or ≥15 mm postpubertal)",
                    "Mandatory bilateral pheochromocytoma",
                    "RET mutation",
                    "PRKAR1A mutation",
                ],
                0,
                "Café-au-lait macules with specified size thresholds remain a core NIH/revised NF1 diagnostic criterion.",
                ref(
                    "Neurofibromatosis Type 1 (NF1)",
                    "≥6 café-au-lait macules (≥5 mm prepuberty or ≥15 mm after puberty)",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Neurofibromatosis Type 1 (NF1)",
                "A 42-year-old with NF1 develops episodic hypertension and palpitations. Best initial biochemical test?",
                [
                    "Plasma or urinary fractionated metanephrines",
                    "Serum calcium and PTH",
                    "Fasting insulin",
                    "24-hour urinary cortisol for PPNAD",
                ],
                0,
                "NF1 carries up to 6% lifetime pheochromocytoma/paraganglioma risk; metanephrines screen for catecholamine excess.",
                ref(
                    "Neurofibromatosis Type 1 (NF1)",
                    "Individuals with NF1 have a 0.6% to 6% lifetime risk of developing pheochromocytoma or paraganglioma, with a median age of presentation of ~40 years.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Carney Complex",
                "The most common endocrine manifestation of Carney complex is:",
                [
                    "Primary pigmented nodular adrenal disease (PPNAD) causing ACTH-independent Cushing",
                    "Medullary thyroid carcinoma",
                    "Insulinoma",
                    "Primary hyperparathyroidism",
                ],
                0,
                "PPNAD with ACTH-independent Cushing affects 25–60% of CNC patients from PRKAR1A pathway dysregulation.",
                ref(
                    "Carney Complex",
                    "ACTH-independent Cushing syndromes resulting from primary pigmented nodular adrenal disease (PPNAD) is the most common endocrine manifestation of CNC, occurring in ~25% to 60% of individuals.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Carney Complex",
                "Carney complex type 1 is caused by mutations in:",
                [
                    "PRKAR1A",
                    "MEN1",
                    "RET",
                    "GNAS",
                ],
                0,
                "CNC1 results from germline PRKAR1A inactivating variants encoding the PKA regulatory subunit R1α.",
                ref(
                    "Molecular Genetics",
                    "Carney complex type 1 (CNC1) results from pathogenic variants in the PRKAR1A gene, which encodes the protein kinase A (PKA) regulatory subunit 1 α (R1α) tumor-suppressor protein.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Cowden Syndrome",
                "In Cowden syndrome without a PTEN mutation, hereditary paraganglioma risk may involve:",
                [
                    "SDHX (e.g., SDHB, SDHD) pathogenic variants",
                    "MEN1 only",
                    "GNAS mosaicism",
                    "CDC73 exclusively",
                ],
                0,
                "CS genetic heterogeneity includes SDHX and other non-PTEN genes linked to PPGL predisposition.",
                ref(
                    "Molecular Genetics",
                    "CS is a genetically heterogeneous disorder, and for those individuals with no pathogenic variant in PTEN, a variety of alternate genetic etiologies may be responsible, including pathogenic variants in genes within the PTEN pathway (e.g., AKT1, PIK3CA) or independent of it (e.g., SDHX, KLLN, SEC23B)",
                ),
            ),
            mcq(
                f"{p}-m18",
                "McCune-Albright Syndrome",
                "McCune-Albright syndrome results from:",
                [
                    "Postzygotic activating GNAS mutations (mosaic)",
                    "Inherited autosomal-dominant GNAS germline mutations",
                    "Biallelic MEN1 loss",
                    "RET codon 634 mutation",
                ],
                0,
                "MAS is not inherited; somatic GNAS activating variants produce fibrous dysplasia, café-au-lait spots, and autonomous endocrinopathies.",
                ref(
                    "McCune-Albright Syndrome",
                    "It is not inherited but results from postzygotic activating (gain-of-function) variants of the G-protein stimulatory subunit (GNAS) gene.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "McCune-Albright Syndrome",
                "Precocious puberty in girls with McCune-Albright syndrome is driven by:",
                [
                    "Autonomous ovarian estrogen secretion from ovarian cysts (gonadotropin-independent)",
                    "Central GnRH-dependent precocious puberty only",
                    "Adrenal androgen excess from NF1",
                    "TSH-secreting pituitary adenoma",
                ],
                0,
                "MAS precocious puberty is gonadotropin-independent from autonomous ovarian estrogen production.",
                ref(
                    "McCune-Albright Syndrome",
                    "Precocious puberty is common in MAS, occurring in >60% of patients as a result of autonomous activation of gonadal tissue (i.e., gonadotrophin-independent rather than central precocious puberty).",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Genetic Testing and Tumor Surveillance",
                "MEN1 surveillance for nonfunctioning pancreatic NETs should begin at approximately:",
                [
                    "Age 10 years with annual MRI abdomen and/or EUS",
                    "Age 50 years with bone scan only",
                    "Age 30 years with mammography",
                    "No imaging is ever recommended",
                ],
                0,
                "Guidelines recommend pancreatic imaging from age 10 years because clinically relevant NF-PNETs emerge in childhood/adolescence.",
                ref(
                    "Nonfunctioning Pancreatic NETs",
                    "The current guidelines therefore recommend surveillance imaging for NF pancreatic NETs from age 10 years,",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Multiple Endocrine Neoplasia Type 2 (MEN2) and Type 3 (MEN3)",
                "Germline RET testing is indicated in all patients presenting with:",
                [
                    "Medullary thyroid carcinoma or pheochromocytoma",
                    "Graves disease",
                    "TSH-secreting adenoma only",
                    "Isolated prolactinoma",
                ],
                0,
                "Apparently sporadic MTC and pheochromocytoma require RET analysis because MEN2/MEN3 may present without family history.",
                ref(
                    "Genetic Testing and Tumor Surveillance",
                    "In addition, all patients presenting with apparently sporadic MTC or unilateral or bilateral adrenal pheochromocytoma should undergo RET mutational analysis.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Insulinoma",
                "Hypoglycemia with inappropriately elevated insulin, proinsulin, and C-peptide in a young MEN1 patient confirms:",
                [
                    "Insulinoma requiring localization and surgical resection when nonmetastatic",
                    "Factitious insulin injection",
                    "Sulfonylurea overdose only",
                    "Non-islet cell tumor hypoglycemia",
                ],
                0,
                "MEN1 insulinomas present with documented hypoglycemia and elevated β-cell peptides; surgery is treatment of choice when localized.",
                ref(
                    "Insulinoma",
                    "hypoglycemia (i.e., glucose <2.2 mmol/L [40 mg/dL]) is documented in the presence of inappropriately elevated concentrations of insulin (together with pro-insulin and C-peptide).",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Von Hippel-Lindau Syndrome (VHL)",
                "VHL genotype-phenotype correlations predict that missense surface VHL variants are associated with:",
                [
                    "Higher risk of pheochromocytoma compared with truncating variants",
                    "Absence of all VHL manifestations",
                    "Only pancreatic cysts without RCC",
                    "Mandatory MEN1 phenotype",
                ],
                0,
                "Amino acid substitutions affecting the VHL protein surface confer higher pheochromocytoma risk than large deletions/truncations (type 2 VHL).",
                ref(
                    "Molecular Genetics",
                    "Thus, in contrast to large-scale deletions and protein-truncating VHL variants, which are associated with a low incidence of pheochromocytoma, amino acid substitutions affecting the surface of the VHL protein are associated with a higher risk of pheochromocytoma",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Pheochromocytoma",
                "When MEN2 patient has concurrent MTC and pheochromocytoma, usual operative sequence is:",
                [
                    "Adrenalectomy (pheochromocytoma) before thyroidectomy",
                    "Thyroidectomy before adrenalectomy without alpha-blockade",
                    "Simultaneous thyroid and bilateral nephrectomy",
                    "Medical therapy only indefinitely",
                ],
                0,
                "Pheochromocytoma must be resected (with alpha/beta blockade) before thyroid surgery to prevent hypertensive crisis.",
                ref(
                    "Pheochromocytoma",
                    "Finally, in patients who have pheochromocytoma concurrently with MTC, the usual practice is to remove the adrenal tumor(s) before thyroidectomy.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Neurofibromatosis Type 1 (NF1)",
                "A diagnostic NF1 criterion distinguishing it from MAS café-au-lait patches is:",
                [
                    "≥1 plexiform neurofibroma (or ≥2 any-type neurofibromas)",
                    "Polyostotic fibrous dysplasia only",
                    "PRKAR1A mutation",
                    "Elevated calcitonin",
                ],
                0,
                "Plexiform or multiple cutaneous neurofibromas are major revised NF1 diagnostic features alongside café-au-lait macules.",
                ref(
                    "Neurofibromatosis Type 1 (NF1)",
                    "≥2 neurofibromas of any type or ≥1 plexiform neurofibroma",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Genetic Testing and Tumor Surveillance",
                "VHL predictive testing should be offered to:",
                [
                    "All first-degree relatives of known pathogenic VHL variant carriers",
                    "Only relatives with retinal symptoms",
                    "Second cousins only after age 60",
                    "No relatives—VHL is never familial",
                ],
                0,
                "Predictive VHL testing enables early surveillance in at-risk first-degree relatives of carriers.",
                ref(
                    "Genetic Testing and Tumor Surveillance",
                    "In addition to diagnostic testing, predictive VHL genetic testing should be offered to all first-degree relatives of known carriers of pathogenic VHL variants, and where possible, this should be offered.",
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
                "Multiple endocrine neoplasia syndromes may be inherited as autosomal-dominant traits.",
                True,
                "KEY POINTS state MEN syndromes are often autosomal-dominant multisystem tumor predispositions.",
                ref(
                    "KEY POINTS",
                    "Multiple endocrine neoplasia (MEN) syndromes, which may be inherited as autosomal-dominant traits, are characterized by the occurrence of two or more endocrine tumors in a patient.",
                ),
            ),
            tf(
                f"{p}-t2",
                "KEY POINTS",
                "McCune-Albright syndrome results from a postzygotic somatic GNAS mutation.",
                True,
                "MEONs are usually autosomal dominant except MAS, which is mosaic GNAS activation.",
                ref(
                    "KEY POINTS",
                    "The MEONs represent a heterogeneous group of monogenic disorders, each inherited as autosomal-dominant traits, with the exception of MAS, which results from a postzygotic somatic mutation of the GNAS gene.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Multiple Endocrine Neoplasia Type 1 (MEN1)",
                "MEN1 has an estimated prevalence of approximately 1:30,000.",
                True,
                "MEN1 (Werner syndrome) prevalence is ~1 in 30,000.",
                ref(
                    "Multiple Endocrine Neoplasia Type 1 (MEN1)",
                    "MEN1, which has also been referred to as Werner syndrome, is an autosomal-dominant disorder with an estimated prevalence of 1:30,000.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Multiple Endocrine Neoplasia Type 1 (MEN1)",
                "Virtually all MEN1 mutation carriers develop clinical or biochemical evidence of tumors by age 50 years.",
                True,
                "MEN1 is highly penetrant with near-universal tumor expression by midlife.",
                ref(
                    "Clinical Features and Management",
                    "MEN1 is a highly penetrant genetic disorder, such that virtually all patients with a MEN1 mutation develop clinical or biochemical evidence of tumor development by the age of 50 years.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Multiple Endocrine Neoplasia Type 2 (MEN2) and Type 3 (MEN3)",
                "MEN2 is more common than MEN3, accounting for more than 90% of RET-mutation syndromes.",
                True,
                "MEN2A predominates; MEN2B/MEN3 represents 5–10% of cases.",
                ref(
                    "Multiple Endocrine Neoplasia Type 2 (MEN2) and Type 3 (MEN3)",
                    "MEN2 is more common than MEN3, with MEN2 accounting for >90% and MEN3 between 5% and 10% of patients",
                ),
            ),
            tf(
                f"{p}-t6",
                "Pheochromocytoma",
                "More than 95% of MEN2- and MEN3-associated pheochromocytomas are benign.",
                True,
                "Malignant pheochromocytoma is rare (<5%) in MEN2/MEN3 large series.",
                ref(
                    "Pheochromocytoma",
                    "The overwhelming majority (>95%) of MEN2- and MEN3-associated pheochromocytomas are benign",
                ),
            ),
            tf(
                f"{p}-t7",
                "Von Hippel-Lindau Syndrome (VHL)",
                "VHL has an incidence of approximately 1:36,000.",
                True,
                "VHL incidence is cited as 1 per 36,000.",
                ref(
                    "Von Hippel-Lindau Syndrome (VHL)",
                    "VHL is an autosomal-dominant disorder with an incidence of 1:36,000",
                ),
            ),
            tf(
                f"{p}-t8",
                "Neurofibromatosis Type 1 (NF1)",
                "NF1 affects approximately 1 in 3000 individuals.",
                True,
                "NF1 population frequency is ~1:3000.",
                ref(
                    "Neurofibromatosis Type 1 (NF1)",
                    "NF1 is an autosomal-dominant disorder affecting 1:3000 individuals",
                ),
            ),
            tf(
                f"{p}-t9",
                "Carney Complex",
                "Cardiac myxomas occur in 30% to 45% of Carney complex patients.",
                True,
                "Cardiac myxomas are a major morbidity/mortality source in CNC.",
                ref(
                    "Carney Complex",
                    "Cardiac myxomas occur in 30% to 45% of patients with CNC and account for considerable morbidity and premature mortality.",
                ),
            ),
            tf(
                f"{p}-t10",
                "McCune-Albright Syndrome",
                "McCune-Albright syndrome is inherited in an autosomal-dominant Mendelian pattern.",
                False,
                "MAS arises from postzygotic GNAS mosaicism and is not inherited.",
                ref(
                    "McCune-Albright Syndrome",
                    "It is not inherited but results from postzygotic activating (gain-of-function) variants of the G-protein stimulatory subunit (GNAS) gene.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Genetic Testing and Tumor Surveillance",
                "RET genetic testing has reduced index-case presentations of MEN2 with established MTC.",
                True,
                "Cascade RET testing and prophylactic thyroidectomy shifted presentation to presymptomatic carriers.",
                ref(
                    "Medullary Thyroid Cancer (MTC)",
                    "Furthermore, widespread availability of RET genetic testing that identifies presymptomatic individuals who then undergo a prophylactic thyroidectomy has resulted in a significant fall in the proportion of MEN2 cases who present as index cases with MTC.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Neurofibromatosis Type 1 (NF1)",
                "Approximately 10% of NF1-associated pheochromocytomas may be malignant.",
                True,
                "NF1 PPGL tumors are usually benign adrenal lesions but ~10% can be malignant.",
                ref(
                    "Neurofibromatosis Type 1 (NF1)",
                    "a subset of tumors (~10%) are malignant",
                ),
            ),
            tf(
                f"{p}-t13",
                "MEN1 Phenocopies and Mutations in Other Genes",
                "Phenocopies occur in approximately 5% to 10% of MEN1 kindreds.",
                True,
                "Non-MEN1 mutations and sporadic tumors can mimic familial MEN1.",
                ref(
                    "MEN1 Phenocopies and Mutations in Other Genes",
                    "Phenocopies are reported in ~5% to 10% of MEN1 kindreds and may occur in different clinical settings.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Multiple Endocrine Neoplasia Type 1 (MEN1)",
                "Assertion: MEN1 is associated with parathyroid, pituitary, and duodenopancreatic tumors.",
                "Reason: MEN1 is caused by activating RET proto-oncogene mutations.",
                2,
                "Assertion true—classic MEN1 triad; reason false—MEN1 is MEN1/menin, not RET (RET causes MEN2/3).",
                ref(
                    "KEY POINTS",
                    "MEN1 is characterized by the occurrence of parathyroid, anterior pituitary, and duodenopancreatic neuroendocrine tumors and is caused by mutations of the MEN1 gene, which encodes the tumor-suppressor protein menin.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Prophylactic Thyroidectomy in MEN2",
                "Assertion: Prophylactic thyroidectomy prevents advanced medullary thyroid carcinoma in RET mutation carriers.",
                "Reason: RET mutations are loss-of-function alleles that abolish receptor signaling.",
                2,
                "Assertion true—early thyroidectomy dramatically improves MTC outcomes; reason false—MEN2 RET mutations are gain-of-function.",
                ref(
                    "Multiple Endocrine Neoplasia Type 2 (MEN2) and Type 3 (MEN3)",
                    "MEN2 and MEN3 are due to RET proto-oncogene mutations that lead to constitutive activation of the encoded receptor tyrosine kinase (TK).",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Pheochromocytoma",
                "Assertion: Pheochromocytoma must be excluded before thyroid surgery in MEN2 patients with MTC.",
                "Reason: Concurrent pheochromocytoma poses no anesthetic risk if undiagnosed.",
                2,
                "Assertion true—catecholamine crisis risk mandates preoperative exclusion; reason false—undiagnosed pheochromocytoma is catastrophic perioperatively.",
                ref(
                    "Pheochromocytoma",
                    "Thus, the possibility of pheochromocytoma due to MEN2 should be considered in all patients diagnosed with MTC before surgery (irrespective of signs or symptoms) because failure to diagnose and treat a concurrent pheochromocytoma may result in catastrophic outcomes due to an intraoperative adrenergic crisis.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Von Hippel-Lindau Syndrome (VHL)",
                "Assertion: VHL patients develop hemangioblastomas and renal cell carcinoma.",
                "Reason: VHL is caused by gain-of-function GNAS mutations.",
                2,
                "Assertion true—cardinal VHL tumors; reason false—VHL is VHL tumor suppressor loss, not GNAS (MAS).",
                ref(
                    "Von Hippel-Lindau Syndrome (VHL)",
                    "The cardinal clinical features of VHL include hemangioblastomas of the retina and central nervous system (CNS), renal cysts and renal cell carcinomas (RCCs)",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Molecular Genetics",
                "Assertion: Loss of functional pVHL stabilizes HIF-α under normoxic conditions.",
                "Reason: Wild-type pVHL promotes HIF-α degradation via ubiquitination.",
                0,
                "Both true and causally linked—pVHL normally targets hydroxylated HIF-α for proteasomal degradation; mutant pVHL fails, stabilizing HIF.",
                ref(
                    "Molecular Genetics",
                    "which facilitates binding to pVHL, leading to recruitment of an E3 ubiquitin-ligase complex that targets HIF-1 $ \\alpha $ for ubiquitination and proteosomal degradation.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Neurofibromatosis Type 1 (NF1)",
                "Assertion: NF1 patients can develop pheochromocytoma.",
                "Reason: NF1 never causes adrenal medullary tumors.",
                2,
                "Assertion true—lifetime PPGL risk up to 6%; reason false—pheochromocytoma is a recognized NF1 endocrine manifestation.",
                ref(
                    "Neurofibromatosis Type 1 (NF1)",
                    "The endocrine abnormalities in NF1 include pheochromocytoma (and less commonly paraganglioma), gastropancreatic NETs, and disorders of growth and puberty relating to hypothalamic and pituitary dysfunction",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Carney Complex",
                "Assertion: Carney complex may cause ACTH-independent Cushing syndrome from PPNAD.",
                "Reason: PPNAD is the most common endocrine manifestation of CNC.",
                1,
                "Both true but reason does not explain mechanism—PPNAD prevalence supports association but is not the causal explanation of ACTH independence.",
                ref(
                    "Carney Complex",
                    "ACTH-independent Cushing syndromes resulting from primary pigmented nodular adrenal disease (PPNAD) is the most common endocrine manifestation of CNC, occurring in ~25% to 60% of individuals.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "McCune-Albright Syndrome",
                "Assertion: McCune-Albright syndrome features fibrous dysplasia and café-au-lait pigmentation.",
                "Reason: MAS is inherited as a classic autosomal-dominant germline disorder.",
                2,
                "Assertion true—clinical triad includes fibrous dysplasia and café-au-lait spots; reason false—MAS is mosaic postzygotic GNAS, not inherited.",
                ref(
                    "McCune-Albright Syndrome",
                    "MAS is characterized by the triad of fibrous dysplasia, café-au-lait skin pigmentation, and autonomous/excessive function of multiple endocrine glands.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "MEN1 Phenocopies and Mutations in Other Genes",
                "Assertion: Some patients with apparent MEN1 lack MEN1 mutations but harbor AIP variants.",
                "Reason: AIP mutations cause familial isolated pituitary adenoma.",
                0,
                "Both true and linked—AIP mutations explain pituitary-predominant phenocopies mistaken for MEN1.",
                ref(
                    "MEN1 Phenocopies and Mutations in Other Genes",
                    "AIP, which encodes the aryl hydrocarbon receptor interacting protein, mutations of which are associated with familial isolated pituitary adenoma (FIPA).",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Pheochromocytoma",
                "Assertion: MEN2-associated pheochromocytomas are frequently bilateral.",
                "Reason: Bilateral disease occurs in about 50% of MEN2 pheochromocytoma patients.",
                0,
                "Both true—bilateral synchronous/metachronous adrenal disease is a hallmark of hereditary MEN2 PPGL.",
                ref(
                    "Pheochromocytoma",
                    "A key characteristic of MEN2-associated pheochromocytoma is that in 50% of patients, they occur as bilateral disease, which can occur synchronously or metachronously.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Genetic Testing and Tumor Surveillance",
                "Assertion: Genetic testing should be offered to first-degree relatives of MEN/MEON mutation carriers.",
                "Reason: Relatives without the familial mutation require the same intensive surveillance as carriers.",
                2,
                "Assertion true—cascade testing is standard; reason false—mutation-negative relatives are reassured and need not undergo carrier surveillance.",
                ref(
                    "KEY POINTS",
                    "Genetic testing should also be offered to relatives considered to be at high risk of disease (i.e., first-degree relatives of those harboring a germline pathogenic variant [\"mutation\"] in the respective gene).",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Gastrinoma",
                "Assertion: MEN1-associated gastrinomas are often small duodenal mucosal tumors.",
                "Reason: MEN1 gastrinomas arise exclusively as large solitary pancreatic tumors.",
                2,
                "Assertion true—duodenal microgastrinomas predominate; reason false—pancreatic gastrinoma is exceptional in MEN1.",
                ref(
                    "Gastrinoma",
                    "MEN1-associated gastrinomas frequently occur as small (<5 mm in diameter), multiple nodular lesions deep within the duodenal mucosa and are only rarely observed in the pancreas,",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "42",
        "title": "Endocrine Neoplasia Syndromes",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Paul J. Newey and Rajesh V. Thakker",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_42_Endocrine_Neoplasia_Syndromes.md",
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
