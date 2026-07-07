#!/usr/bin/env python3
"""Generate Williams 15e module w15-01 — Principles of Endocrinology."""
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
OUT_NAME = "w15-01_Principles_of_Endocrinology.json"


def build() -> dict:
    p = "w15-01"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Hormone definition",
                "Starling's definition of a hormone",
                "In 1902 E. H. Starling coined the term hormone for secretin—a substance secreted by the small intestine into the bloodstream to stimulate pancreatic secretion. He distinguished endocrine coordination from nervous control, establishing endocrinology within mammalian physiology.",
                ref(
                    "Introduction",
                    "In 1902, more than 100 years ago, E. H. Starling coined the term hormone to describe secretin, a substance secreted by the small intestine into the bloodstream to stimulate pancreatic secretion.",
                ),
            ),
            note(
                f"{p}-n2",
                "Endocrine vs paracrine",
                "Why hormones must be produced in larger amounts than paracrine factors",
                "Hormones travel through blood to distant targets and must reach effective concentrations after transit and degradation. Paracrine signals act locally in much smaller amounts; site of origin determines paracrine specificity, whereas hormone site of production is often divorced from function.",
                ref(
                    "The Evolutionary Perspective",
                    "hormones must be produced in much larger amounts to act as hormones, in contrast to much smaller amounts needed to act as paracrine factors acting locally.",
                ),
            ),
            note(
                f"{p}-n3",
                "Evolutionary signaling",
                "Conserved G protein signaling from yeast to mammals",
                "Even Saccharomyces cerevisiae uses seven membrane-spanning receptors and heterotrimeric G proteins resembling mammalian photon and glycoprotein hormone pathways—likely present in the common ancestor of yeast and humans.",
                ref(
                    "The Evolutionary Perspective",
                    "These yeast receptors trigger activation of heterotrimeric G proteins just as mammalian receptors do; thus, this conserved signaling pathway was likely present in the common ancestor of yeast and humans.",
                ),
            ),
            note(
                f"{p}-n4",
                "IGF1 dual roles",
                "Why IGF1 requires elaborate binding protein regulation",
                "IGF1 acts as a circulating hormone from liver and other tissues and as a local paracrine proliferative signal. Unlike insulin, IGF1 mandates multiple binding proteins to enable appropriate signaling in both endocrine and paracrine contexts.",
                ref(
                    "The Evolutionary Perspective",
                    "Presumably, IGF1 actions mandate an elaborate binding protein apparatus to enable appropriate hormone signaling as either a hormone or paracrine factor.",
                ),
            ),
            note(
                f"{p}-n5",
                "BMP4 specificity",
                "How site of origin determines BMP4 physiologic role",
                "When BMP4 is secreted by developing kidney cells it regulates renal differentiation; when secreted by bone cells it regulates bone formation. Paracrine specificity depends on precise site of origin, unlike blood-borne hormones.",
                ref(
                    "The Evolutionary Perspective",
                    "When the paracrine factor bone morphogenetic protein 4 (BMP4) is secreted by cells in the developing kidney, BMP4 regulates differentiation of renal cells; when the same factor is secreted by cells in bone, it regulates bone formation.",
                ),
            ),
            note(
                f"{p}-n6",
                "Orphan receptors",
                "How orphan receptor discovery broadened hormone definitions",
                "Orphan nuclear receptor discovery showed oxygenated cholesterol derivatives activate LXR to regulate cholesterol and fatty acid metabolism. Cholesterol uses hormonal signaling to regulate its own metabolism—expanding what constitutes a hormone beyond discrete glandular products.",
                ref(
                    "The Evolutionary Perspective",
                    "Subsequent experiments found that oxygenated derivatives of cholesterol are the ligands for LXR, which regulates genes involved in cholesterol and fatty acid metabolism.",
                ),
            ),
            note(
                f"{p}-n7",
                "Calcium-sensing receptor",
                "Nonclassical ligand GPCR signaling",
                "The calcium-sensing receptor responds to ionic calcium released from bone, kidney, and intestine, coordinating parathyroid, renal tubular, and other cellular responses—an example of metabolic ions acting as hormonal ligands.",
                ref(
                    "The Evolutionary Perspective",
                    "The calcium-sensing receptor is an example from the G protein-coupled receptor family that responds to a nonclassical ligand, ionic calcium.",
                ),
            ),
            note(
                f"{p}-n8",
                "Expanded endocrine organs",
                "Classic versus expanded endocrine systems",
                "Classic endocrine glands produce dedicated hormones in secretory granules. Adipose, enteroendocrine, and other tissues now qualify as complex endocrine systems—adipokines, myokines, hepatokines, and gut hormones regulating metabolism and body weight.",
                ref(
                    "Endocrine Glands",
                    "However, not all hormones are formed in dedicated and specialized endocrine glands; the adipose, enteroendocrine, and other systems are now recognized to be complex endocrine systems.",
                ),
            ),
            note(
                f"{p}-n9",
                "Leptin and enteroendocrine",
                "Leptin and enteroendocrine nutrient signaling",
                "Leptin from adipocytes signals nutritional state to the CNS. Enteroendocrine cells scattered through intestinal epithelium secrete peptides regulating appetite, satiety, and metabolic responses to oral nutrients.",
                ref(
                    "Endocrine Glands",
                    "the protein hormone leptin, which regulates appetite and energy expenditure, is formed in adipocytes, providing a specific signal reflecting the nutritional state of the organism to the central nervous system.",
                ),
            ),
            note(
                f"{p}-n10",
                "Thyroid synthesis",
                "Thyroglobulin iodination and thyroid hormone storage",
                "Thyroid hormone synthesis begins with thyroglobulin iodination at specific tyrosines; iodotyrosines combine to form iodothyronines stored in the follicle lumen. Release requires phagocytosis, cathepsin digestion, and basolateral secretion—enough stored hormone for ~2 months.",
                ref(
                    "Endocrine Glands",
                    "Thyroid hormone synthesis occurs via the synthesis of a 660,000-kDa homodimer, thyroglobulin, which is iodinated at specific tyrosines.",
                ),
            ),
            note(
                f"{p}-n11",
                "Postsecretory activation",
                "How T4 becomes active T3 in target tissues",
                "T4 released from thyroid is a prohormone requiring deiodination to active T3 in CNS, thyrotrophs (feedback on TSH), or liver/kidney with release into circulation. Similar tissue-specific activation applies to testosterone→DHT and vitamin D hydroxylation.",
                ref(
                    "Endocrine Glands",
                    "T_4 released from the thyroid cell is a prohormone that must undergo specific deiodination to form the active 3,5,3'-triiodothyronine ( T_3 ).",
                ),
            ),
            note(
                f"{p}-n12",
                "Vitamin D activation",
                "Why vitamin D requires sequential hepatic and renal hydroxylation",
                "Vitamin D requires 25-hydroxylation in liver and 1α-hydroxylation in kidney to form active 1,25-dihydroxyvitamin D. 1α-hydroxylase is stimulated by PTH and hypophosphatemia and inhibited by calcium, 1,25-dihydroxyvitamin D, and FGF23.",
                ref(
                    "Endocrine Glands",
                    "Activity of 1α-hydroxylase, but not 25-hydroxylase, is stimulated by PTH and hypophosphatemia but is inhibited by calcium, 1,25-dihydroxyvitamin D, and fibroblast growth factor 23 (FGF23).",
                ),
            ),
            note(
                f"{p}-n13",
                "Hormone transport",
                "Binding proteins for lipophilic hormones",
                "Steroid and thyroid hormones bind TBG, SHBG, CBG, or albumin. Ligand-protein complexes serve as reservoirs, distribute water-insoluble hormones, and protect against rapid inactivation or urinary/biliary excretion.",
                ref(
                    "Transport of Hormones in Blood",
                    "Such molecules are tightly bound to 50-kDa to 60-kDa carrier plasma glycoproteins, such as thyroxine-binding globulin (TBG), sex hormone-binding globulin (SHBG), and corticosteroid-binding globulin (CBG), or weakly bound to abundant albumin.",
                ),
            ),
            note(
                f"{p}-n14",
                "Free hormone hypothesis",
                "Why the hypothalamic-pituitary axis defends free hormone",
                "Protein-bound hormones exist in equilibrium with minute free aqueous fractions taken up by target cells. In congenital TBG deficiency, transthyretin and albumin compensate; free thyroid hormone remains normal because feedback defends the active moiety.",
                ref(
                    "Transport of Hormones in Blood",
                    "The fact that the free hormone concentration is normal in individuals with TBG deficiency indicates that the hypothalamic-pituitary axis defends the free, active hormone.",
                ),
            ),
            note(
                f"{p}-n15",
                "DBP knockout mice",
                "Vitamin D-binding protein physiologic role",
                "DBP-null mice have markedly reduced circulating vitamin D yet are otherwise normal, with enhanced susceptibility to dietary deficiency but reduced risk of vitamin D intoxication due to shortened 25-hydroxyvitamin D half-life.",
                ref(
                    "Transport of Hormones in Blood",
                    "in mice with targeted inactivation of the vitamin D-binding protein (DBP), the absence of DBP markedly reduces circulating concentrations of vitamin D, yet the mice are otherwise normal.",
                ),
            ),
            note(
                f"{p}-n16",
                "Target cell receptors",
                "Membrane versus intracellular hormone receptors",
                "Polypeptide hormones bind cell-surface receptors; steroid and thyroid hormones enter cells to bind cytosolic or nuclear receptors. Responsiveness depends on receptor expression and downstream signaling—not passive reception.",
                ref(
                    "Target Cells as Active Participants",
                    "Broadly, polypeptide hormone receptors are cell membrane associated, but steroid hormones selectively bind soluble intracellular proteins (Fig. 1.2).",
                ),
            ),
            note(
                f"{p}-n17",
                "Receptor regulation",
                "How desensitization and downregulation limit signaling",
                "Receptor endocytosis, lysosomal degradation, and ligand-mediated phosphorylation (homologous or heterologous desensitization) attenuate signaling. SOCS proteins and phosphatases provide intracellular negative feedback on pathways such as JAK-STAT.",
                ref(
                    "Target Cells as Active Participants",
                    "Desensitization mechanisms can be activated by a receptor's ligand (homologous desensitization) or by another signal (heterologous desensitization), thereby attenuating receptor signaling in the continued presence of the ligand.",
                ),
            ),
            note(
                f"{p}-n18",
                "Receptor mutations",
                "Gain- and loss-of-function receptor mutations",
                "Activating mutations (e.g., TSH receptor) cause hyperfunction without ligand; inactivating mutations (e.g., androgen or vasopressin receptors) cause hypofunction. Tables 1.1 and 1.2 catalog GPCR and nuclear receptor disorders.",
                ref(
                    "Target Cells as Active Participants",
                    "Constitutive receptor activation may be induced by activating mutations (e.g., TSH receptor) leading to endocrine organ hyperfunction, even in the absence of ligand.",
                ),
            ),
            note(
                f"{p}-n19",
                "Secretion rhythms",
                "Why circadian and pulsatile patterns matter clinically",
                "Insulin pulses with nutrients; gonadotrophins follow a hypothalamic pulse generator; ~70% of GH occurs in slow-wave sleep. Loss of circadian ACTH rhythm with midnight cortisol elevation characterizes Cushing disease.",
                ref(
                    "Control of Hormone Secretion",
                    "About 70% of overall GH secretion occurs during slow-wave sleep, and increasing age is associated with declining slow-wave sleep and a concomitant decline in GH and elevation of cortisol secretion.",
                ),
            ),
            note(
                f"{p}-n20",
                "HP axis control",
                "How three tiers regulate anterior pituitary secretion",
                "Tier 1: hypothalamic releasing hormones (GHRH, CRH, TRH, GnRH) and inhibitors (somatostatin, dopamine). Tier 2: intrapituitary paracrine factors. Tier 3: peripheral hormone negative feedback on pituitary and hypothalamus.",
                ref(
                    "Control of Hormone Secretion",
                    "Several tiers of control subserve the ultimate net glandular secretion. First, central nervous system signals, including afferent stimuli, neuropeptides, and stress, signal the synthesis and secretion of hypothalamic hormones and neuropeptides (Fig. 1.4).",
                ),
            ),
            note(
                f"{p}-n21",
                "SOCS-3",
                "Intraglandular feedback: corticotroph SOCS-3",
                "Corticotroph SOCS-3 induction by gp130-linked cytokines abrogates JAK-STAT signaling and blocks POMC transcription and ACTH secretion—providing rapid on-off plasticity for environmental stress responses.",
                ref(
                    "Control of Hormone Secretion",
                    "corticotroph SOCS-3 induction by gp130-linked cytokines serves to abrogate the ligand-induced JAK-STAT cascade and block pro-opiomelanocortin (POMC) transcription and ACTH secretion.",
                ),
            ),
            note(
                f"{p}-n22",
                "Hormone measurement",
                "Why timing matters for hormone assays",
                "Random fasting samples suffice when hormones are stable (thyroid hormones, PRL, IGF1). Episodic secretors require timed sampling—early-morning and late-evening cortisol, or frequent GH sampling—to avoid misinterpreting peaks or nadirs.",
                ref(
                    "Hormone Measurement",
                    "when hormone secretion is clearly episodic, timed samples may be required over a defined time course to reflect hormone bioavailability.",
                ),
            ),
            note(
                f"{p}-n23",
                "Dynamic testing",
                "How stimulation and suppression tests diagnose dysfunction",
                "Hypofunction is tested by evoking secretion with hypothalamic-releasing hormones, trophic hormones, or pharmacologic stimuli (macimorelin, metoclopramide). Hypersecretion is diagnosed by failure to suppress (e.g., GH after glucose, insulin during hypoglycemia).",
                ref(
                    "Hormone Measurement",
                    "In general, confirmation of failed glandular function is made by attempting to evoke hormone secretion by recognized stimuli.",
                ),
            ),
            note(
                f"{p}-n24",
                "Assay methods",
                "Immunoassays versus LC-MS for hormone measurement",
                "Radioimmunoassays, ELISAs, and two-site immunometric assays enable ultrasensitive polypeptide measurement but may yield artifactual discordant results. LC-MS now measures many small-molecule hormones including steroids with high sensitivity.",
                ref(
                    "Hormone Measurement",
                    "Many hormones, in particular small molecules such as steroid hormones, can now be measured with high sensitivity using liquid chromatography–mass spectrometry technology.",
                ),
            ),
            note(
                f"{p}-n25",
                "Endocrine disease categories",
                "How endocrine diseases are classified",
                "Endocrine disorders include hormone overproduction, underproduction, altered tissue responses, and endocrine gland tumors. A fifth atypical category is consumptive hypothyroidism from tumor D3 overexpression inactivating thyroid hormones.",
                ref(
                    "Endocrine Diseases",
                    "Endocrine diseases fall into four broad categories: (1) hormone overproduction, (2) hormone underproduction, (3) altered tissue responses to hormones, and (4) tumors of endocrine glands.",
                ),
            ),
            note(
                f"{p}-n26",
                "Consumptive hypothyroidism",
                "How D3 overexpression causes consumptive hypothyroidism",
                "Type 3 iodothyronine deiodinase (D3) inactivates T3 and T4 to reverse T3. Paraneoplastic D3 overexpression in infantile hemangiomas (and some drug-induced tumors) destroys thyroid hormone faster than production—causing severe hypothyroidism.",
                ref(
                    "Excessive Hormone Inactivation or Destruction",
                    "Consumptive hypothyroidism is a rare paraneoplastic condition, most commonly associated with infantile hemangiomas, caused by overexpression of D3 and an inactivation rate of thyroid hormones that exceeds its production.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "IGF1 signaling",
                "A 14-year-old with tall stature has elevated serum IGF1 but normal GH after glucose suppression. Liver MRI is normal. Which concept best explains local versus systemic IGF1 actions?",
                [
                    "IGF1 acts only as an endocrine hormone from liver",
                    "IGF1 can function as both circulating hormone and local paracrine factor",
                    "IGF1 signaling requires Notch membrane ligands",
                    "IGF1 cannot share receptors with paracrine factors",
                ],
                1,
                "IGF1 is secreted into blood from liver and produced locally in most tissues; binding proteins regulate its dual roles—unlike purely local paracrine factors.",
                ref(
                    "The Evolutionary Perspective",
                    "Insulin-like growth factor 1 (IGF1) is a polypeptide hormone secreted into the bloodstream from the liver and other tissues but is also a paracrine factor produced locally in most tissues to control cell proliferation.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Paracrine specificity",
                "Researchers delete BMP4 from renal mesenchyme but not osteoblasts in mice. Which outcome is expected?",
                [
                    "Impaired bone formation with normal renal differentiation",
                    "Impaired renal differentiation with preserved bone formation",
                    "Loss of both renal and bone BMP4 signaling equally",
                    "No phenotype because BMP4 acts only as a hormone",
                ],
                1,
                "BMP4 site of origin determines function—renal BMP4 regulates renal cells; bone BMP4 regulates bone formation.",
                ref(
                    "The Evolutionary Perspective",
                    "when the same factor is secreted by cells in bone, it regulates bone formation. Thus, the site of origin of BMP4 determines its physiologic role.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Orphan receptors",
                "A nuclear receptor initially classified as orphan is later found to bind oxygenated cholesterol metabolites regulating hepatic lipid genes. Which receptor paradigm does this illustrate?",
                [
                    "Liver X receptor (LXR) broadening hormonal signaling definitions",
                    "Calcium-sensing receptor responding to peptide hormones",
                    "Notch responding to blood-borne ligands",
                    "Rhodopsin activating nuclear transcription directly",
                ],
                0,
                "LXR discovery showed metabolic precursors can act as hormonal ligands regulating their own metabolism.",
                ref(
                    "The Evolutionary Perspective",
                    "the liver X receptor (LXR) was one such orphan receptor found when searching for unknown putative nuclear receptors.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Calcium receptor",
                "A patient with familial hypocalciuric hypercalcemia has a gain-of-function mutation. Which receptor is most likely affected?",
                [
                    "Parathyroid calcium-sensing receptor",
                    "Vitamin D receptor",
                    "PTH/PTHrP receptor tyrosine kinase",
                    "FGF23 receptor",
                ],
                0,
                "Calcium-sensing receptor gain-of-function causes autosomal-dominant hypocalcemia; loss-of-function causes familial hypercalcemia (Table 1.1).",
                ref(
                    "TABLE 1.1 Selected Diseases Caused by Mutations in G Protein-Coupled Receptors",
                    "Autosomal-dominant hypocalcemia ... Ca^{2+} sensing ... Gain",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Expanded endocrinology",
                "A woman with obesity has elevated leptin but continues to gain weight. Which statement best describes leptin's endocrine role?",
                [
                    "Leptin is synthesized only in the pituitary",
                    "Leptin from adipocytes signals nutritional state to the CNS",
                    "Leptin acts exclusively as a paracrine factor within fat depots",
                    "Leptin replaces insulin in glucose homeostasis",
                ],
                1,
                "Leptin is an adipocyte hormone reflecting nutritional state and regulating appetite and energy expenditure centrally.",
                ref(
                    "Endocrine Glands",
                    "the protein hormone leptin, which regulates appetite and energy expenditure, is formed in adipocytes, providing a specific signal reflecting the nutritional state of the organism to the central nervous system.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Thyroid storage",
                "After thyroidectomy for cancer, a patient asks how long preoperative thyroid hormone stores might have lasted. Based on thyroid physiology, what is the best answer?",
                [
                    "Hours, because thyroid hormone is not stored",
                    "About 2 months of stored hormone in the gland",
                    "Years, because thyroglobulin is never degraded",
                    "Days only, matching insulin granule turnover",
                ],
                1,
                "The thyroid contains enough stored hormone to last about 2 months—an exception to minimal intracellular storage.",
                ref(
                    "Endocrine Glands",
                    "One is the thyroid gland, which contains enough stored hormone to last for about 2 months.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "T4 activation",
                "A patient on levothyroxine monotherapy has normal TSH but persistent hypothyroid symptoms. T3 is low-normal. Which mechanism is most relevant?",
                [
                    "Peripheral deiodination of T4 to T3 in target tissues",
                    "Direct secretion of active T3 from thyroid follicles only",
                    "Hepatic conversion of T3 to reverse T3 as sole activation step",
                    "Testosterone 5α-reductase converting T4 to T3",
                ],
                0,
                "T4 is a prohormone requiring tissue-specific deiodination to active T3 in CNS, pituitary, liver, kidney, and other tissues.",
                ref(
                    "Endocrine Glands",
                    "T_4 released from the thyroid cell is a prohormone that must undergo specific deiodination to form the active 3,5,3'-triiodothyronine ( T_3 ).",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Vitamin D regulation",
                "In CKD with secondary hyperparathyroidism, which factor most directly stimulates renal 1α-hydroxylase?",
                [
                    "Elevated FGF23 and hypercalcemia",
                    "PTH and hypophosphatemia",
                    "High 25-hydroxylase activity alone",
                    "Suppressed 1,25-dihydroxyvitamin D feedback only",
                ],
                1,
                "1α-hydroxylase is stimulated by PTH and hypophosphatemia and inhibited by calcium, active vitamin D, and FGF23.",
                ref(
                    "Endocrine Glands",
                    "Activity of 1α-hydroxylase, but not 25-hydroxylase, is stimulated by PTH and hypophosphatemia but is inhibited by calcium, 1,25-dihydroxyvitamin D, and fibroblast growth factor 23 (FGF23).",
                ),
            ),
            mcq(
                f"{p}-q9",
                "TBG deficiency",
                "A euthyroid woman has low total T4 but normal TSH and free T4. She has congenital TBG deficiency. What compensates for absent TBG?",
                [
                    "Increased thyroid hormone synthesis only",
                    "Transthyretin and albumin binding with defended free hormone",
                    "Complete absence of circulating thyroid hormone binding",
                    "SHBG replacing TBG for all thyroid transport",
                ],
                1,
                "Secondary transport proteins compensate; the HP axis maintains normal free thyroid hormone despite lower total concentrations.",
                ref(
                    "Transport of Hormones in Blood",
                    "in humans with congenital TBG deficiency, other proteins—transthyretin (TTR) and albumin—fulfill its function.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Free hormone hypothesis",
                "A hepatologist perfuses tracer T4 into portal vein in protein-free versus protein-containing solution. What difference is observed?",
                [
                    "Protein-free solution causes peripheral hepatic binding only",
                    "Protein-containing solution permits uniform hepatic lobule distribution",
                    "Both solutions exclude thyroid hormone from hepatocytes",
                    "Protein binding abolishes all hepatocyte uptake",
                ],
                1,
                "Binding proteins facilitate uniform distribution of lipophilic hormones within tissues; free tracer binds peripherally in protein-free perfusion.",
                ref(
                    "Transport of Hormones in Blood",
                    "if tracer thyroid hormone is injected into the portal vein in a protein-free solution, it binds to hepatocytes at the periphery of the hepatic sinusoid. When the same experiment is repeated with a protein-containing solution, uniform distribution of the tracer hormone occurs throughout the hepatic lobule.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "DBP knockout",
                "DBP-null mice are placed on a vitamin D-deficient diet compared with wild-type littermates. Expected finding?",
                [
                    "Resistance to dietary vitamin D deficiency",
                    "Enhanced susceptibility to vitamin D deficiency",
                    "No change in 25-hydroxyvitamin D half-life",
                    "Increased risk of vitamin D intoxication on normal diet",
                ],
                1,
                "Absent DBP reduces vitamin D reservoir and half-life—mice are more susceptible to deficiency but less prone to intoxication.",
                ref(
                    "Transport of Hormones in Blood",
                    "they have enhanced susceptibility to a vitamin D-deficient diet due to the reduced reservoir of this sterol.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Receptor localization",
                "A lipophilic hormone acts by binding a receptor that directly modulates gene transcription in the nucleus. Which hormone-receptor pair fits best?",
                [
                    "Insulin—cell-surface tyrosine kinase receptor",
                    "LH—G protein-coupled membrane receptor generating cAMP",
                    "Progesterone—intracellular nuclear receptor",
                    "IGF1—cytokine receptor without gene effects",
                ],
                2,
                "Steroid hormones including progesterone bind nuclear receptors that directly regulate transcription; polypeptide hormones use membrane receptors.",
                ref(
                    "Fig. 1.2 Hormonal signaling by cell surface and intracellular receptors",
                    "the receptor for the lipophilic steroid hormone progesterone resides in the cell nucleus. It binds the hormone and becomes activated and capable of directly modulating target gene transcription.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Receptor desensitization",
                "A patient on chronic β-agonist therapy has diminished bronchodilator response despite continued drug exposure. Which mechanism best explains this?",
                [
                    "Homologous receptor desensitization from ligand-mediated phosphorylation",
                    "Constitutive activating mutation of the β-receptor",
                    "Complete receptor gene deletion",
                    "Increased receptor synthesis on the cell surface",
                ],
                0,
                "Ligand-mediated receptor phosphorylation causes reversible homologous desensitization—exemplified by epinephrine receptors.",
                ref(
                    "Target Cells as Active Participants",
                    "Receptor function may also be limited by the action of specific phosphatases (e.g., Src homology phosphatase [SHP]) or by intracellular negative regulation of the signaling cascade",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Activating mutations",
                "A neonate has congenital hyperthyroidism without detectable TSH receptor antibodies. Germline sequencing is planned. Which mutation class is most likely?",
                [
                    "Inactivating androgen receptor mutation",
                    "Activating TSH receptor mutation",
                    "Loss-of-function vasopressin V2 receptor",
                    "Dominant-negative thyroid-beta receptor",
                ],
                1,
                "Activating TSH receptor mutations cause congenital hyperthyroidism and hyperfunctioning adenomas (Table 1.1).",
                ref(
                    "TABLE 1.1 Selected Diseases Caused by Mutations in G Protein-Coupled Receptors",
                    "Congenital hyperthyroidism ... TSH ... Gain",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Nuclear receptor resistance",
                "A child has elevated TSH and T4 with goiter but no thyrotoxic symptoms. Which diagnosis should be considered?",
                [
                    "Resistance to thyroid hormone (thyroid-beta receptor)",
                    "Activating TSH receptor mutation",
                    "Complete androgen insensitivity",
                    "Vitamin D-dependent rickets type 1",
                ],
                0,
                "Resistance to thyroid hormone from thyroid-beta receptor mutations causes elevated thyroid hormones with inappropriate TSH (Table 1.2).",
                ref(
                    "TABLE 1.2 Selected Diseases Caused by Mutations in Nuclear Receptors",
                    "Resistance to thyroid hormone (generalized/pituitary) ... Thyroid-beta ... Dominant-negative or loss",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Circadian secretion",
                "Polysomnography shows reduced slow-wave sleep in an older man with low IGF1 and elevated evening cortisol. Which relationship is best supported?",
                [
                    "Aging reduces slow-wave sleep, lowering GH and raising cortisol",
                    "GH hypersecretion causes slow-wave sleep loss",
                    "Cortisol suppression always increases GH during REM sleep",
                    "Circadian rhythms do not affect pituitary hormones",
                ],
                0,
                "Age-related decline in slow-wave sleep parallels reduced GH and increased cortisol secretion.",
                ref(
                    "Control of Hormone Secretion",
                    "increasing age is associated with declining slow-wave sleep and a concomitant decline in GH and elevation of cortisol secretion.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Cushing circadian rhythm",
                "A patient has loss of nocturnal cortisol nadir with elevated midnight cortisol. ACTH is unsuppressed. Most likely diagnosis?",
                [
                    "Physiologic stress response only",
                    "Cushing disease with disrupted circadian ACTH secretion",
                    "Primary adrenal insufficiency",
                    "Normal aging pattern",
                ],
                1,
                "Loss of circadian ACTH secretion with high midnight cortisol is a feature of Cushing disease.",
                ref(
                    "Control of Hormone Secretion",
                    "loss of circadian ACTH secretion with high midnight cortisol levels is a feature of Cushing disease.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "HP axis feedback",
                "Primary hypothyroidism develops in a patient. Before starting levothyroxine, which pituitary change is expected?",
                [
                    "Suppressed TSH from negative feedback",
                    "Elevated TSH from loss of thyroid hormone negative feedback",
                    "Elevated TRH with suppressed TSH",
                    "Normal TSH because hypothalamus is unaffected",
                ],
                1,
                "Target hormones negatively feedback on trophic hormones; hypothyroidism raises TSH, and prolonged TSH stimulation can cause thyroid hyperplasia.",
                ref(
                    "Control of Hormone Secretion",
                    "Target hormones, in turn, serve as powerful negative feedback regulators of their respective trophic hormones, often also suppressing the secretion of hypothalamic-releasing hormones.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "SOCS-3",
                "During systemic inflammation, which intrapituitary mechanism rapidly limits ACTH secretion?",
                [
                    "SOCS-3 induction blocking JAK-STAT and POMC transcription",
                    "Permanent destruction of all corticotrophs",
                    "GnRH pulse generator activation",
                    "Increased 1α-hydroxylase in corticotrophs",
                ],
                0,
                "Corticotroph SOCS-3 provides rapid intracellular feedback abrogating cytokine-driven JAK-STAT and ACTH production.",
                ref(
                    "Control of Hormone Secretion",
                    "corticotroph SOCS-3 induction by gp130-linked cytokines serves to abrogate the ligand-induced JAK-STAT cascade and block pro-opiomelanocortin (POMC) transcription and ACTH secretion.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Hormone assay timing",
                "A resident orders a random afternoon serum cortisol to screen for Cushing syndrome in an unstressed outpatient. What is the pitfall?",
                [
                    "Cortisol is stable throughout the day; timing never matters",
                    "Episodic and circadian cortisol requires timed sampling",
                    "Cortisol can only be measured in 24-hour urine",
                    "IGF1 and cortisol share identical secretion patterns",
                ],
                1,
                "Episodic and circadian hormones need appropriately timed samples; random values may reflect peaks or nadirs.",
                ref(
                    "Hormone Measurement",
                    "Random sampling may also reflect secretion peaks or nadirs, thus confounding adequate interpretation of results.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Dynamic testing",
                "A patient with suspected acromegaly has elevated random GH. Which test best confirms inappropriate secretion?",
                [
                    "Failure to suppress GH after standardized oral glucose load",
                    "Macimorelin stimulation test for GH deficiency",
                    "Metoclopramide-induced PRL secretion",
                    "TRH stimulation of TSH",
                ],
                0,
                "GH hypersecretion is diagnosed by failure to suppress after glucose; stimulation tests assess deficiency.",
                ref(
                    "Hormone Measurement",
                    "Failure to appropriately suppress GH levels after a standardized glucose load implies inappropriate GH hypersecretion.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Assay artifacts",
                "Immunometric TSH results are markedly discordant with clinical hyperthyroidism. Free T4 by LC-MS is elevated. Best explanation?",
                [
                    "Antibody-based assay artifact; LC-MS may be more reliable for small molecules",
                    "LC-MS always underestimates steroid and thyroid hormones",
                    "Immunometric assays cannot measure polypeptide hormones",
                    "Discordance proves laboratory error in LC-MS only",
                ],
                0,
                "All antibody-based assays may produce artifacts discordant with the clinical picture; LC-MS offers sensitive small-molecule measurement.",
                ref(
                    "Hormone Measurement",
                    "However, all antibody-based assays may be subject to artifacts, which should be kept in mind, especially when the assay results are discordant with the clinical picture.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Monoclonal endocrine tumors",
                "A somatotroph adenoma shows a somatic Gα mutation. Which paired outcome is typical?",
                [
                    "Polyclonal thyroid hyperplasia from TSH antibodies",
                    "Monoclonal expansion with increased GH secretion per cell",
                    "Autoimmune destruction of GH-producing cells",
                    "Consumptive hypothyroidism from D3 overexpression",
                ],
                1,
                "Most endocrine tumors are monoclonal; mutant Gα in somatotrophs increases proliferation and GH secretion.",
                ref(
                    "Hormone Overproduction",
                    "mutant Gα proteins in somatotrophs can lead to both increased cellular proliferation and increased secretion of GH from the monoclonal tumor.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Hormone resistance",
                "A boy has short stature, normal GH levels, but low IGF1. GH receptor sequencing is planned. Likely diagnosis?",
                [
                    "Laron dwarfism from GH receptor loss-of-function",
                    "McCune-Albright activating Gsα mutation",
                    "Androgen insensitivity syndrome",
                    "Glucocorticoid resistance with elevated cortisol",
                ],
                0,
                "GH receptor mutations cause Laron dwarfism—a classic hormone resistance syndrome.",
                ref(
                    "Altered Tissue Responses to Hormones",
                    "Examples include mutations in the GH receptor in Laron dwarfism",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Therapeutic replacement",
                "A patient with primary hypothyroidism asks why levothyroxine is oral but insulin is injected. Best explanation?",
                [
                    "All peptide hormones are orally bioavailable",
                    "Thyroid hormones can be replaced orally; peptide hormones usually require parenteral or mucosal routes",
                    "Insulin is a steroid requiring intracellular receptors",
                    "Oral desmopressin is never absorbed",
                ],
                1,
                "Thyroid hormones and some steroids can be replaced orally; peptide hormones and analogues are usually parenteral or mucosal, though oral formulations are emerging.",
                ref(
                    "Diagnostic and Therapeutic Uses of Hormones",
                    "Thyroid hormones and some steroids can be replaced orally, whereas peptide hormones and analogues (e.g., insulin, PTH, GH) are administered parenterally or absorbed through mucous membranes",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Closed-loop insulin",
                "A type 1 diabetes patient uses a sensor-augmented pump with automated basal adjustments from interstitial glucose. This exemplifies which therapeutic advance?",
                [
                    "Closed-loop coupling of continuous glucose sensing with variable insulin delivery",
                    "Once-weekly GLP-1 replacing all insulin needs",
                    "Oral somatostatin for insulin secretion",
                    "Designer insulin that permanently suppresses all activity",
                ],
                0,
                "Algorithms coupling continuous glucose monitoring with pump insulin dosing automatically adjust to interstitial glucose—closed-loop systems reducing disease burden.",
                ref(
                    "Diagnostic and Therapeutic Uses of Hormones",
                    "Novel algorithms have now been developed that can couple continuous glucose-sensing technology with variable rates of insulin delivery via insulin pumps, such that the dose of insulin via the pump is automatically adjusted",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Hormone definition",
                "Starling defined hormones as chemical signals secreted into the bloodstream that act on distant tissues.",
                True,
                "Starling coined hormone for secretin—a blood-borne intestinal signal acting at a distance.",
                ref(
                    "The Evolutionary Perspective",
                    "Hormones are broadly defined as chemical signals secreted into the bloodstream that act on distant tissues, usually in a regulatory fashion.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Paracrine vs endocrine",
                "Target cells can distinguish intracellular response machinery based on whether a signal arrived via blood or from an adjacent cell.",
                False,
                "Cellular response machinery does not distinguish sites of origin; hormonal and paracrine signals share final common pathways.",
                ref(
                    "The Evolutionary Perspective",
                    "Target cells respond similarly to signals that reach them from the bloodstream (hormones) or from adjacent cells (paracrine factors); the cellular response machinery does not distinguish between sites of origin of hormone signals.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "PTH and PTHrP",
                "One receptor can mediate actions of both parathyroid hormone and parathyroid hormone-related protein.",
                True,
                "PTH and PTHrP share receptor mediation—an example of hormone and paracrine factor using the same receptor.",
                ref(
                    "The Evolutionary Perspective",
                    "one receptor can mediate the actions of a hormone, such as parathyroid hormone (PTH), and of a paracrine factor, such as parathyroid hormone-related protein.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Notch signaling",
                "Notch receptors respond to known blood-borne hormone ligands.",
                False,
                "Notch responds to membrane-based ligands for cell fate; no known blood-borne ligands—too rigid for hormonal purposes.",
                ref(
                    "The Evolutionary Perspective",
                    "Notch receptors respond to membrane-based ligands to control cell fate, but they do not respond to known blood-borne ligands.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "TBG essential",
                "Congenital TBG deficiency always causes symptomatic hypothyroidism because TBG is essential for thyroid hormone distribution.",
                False,
                "TBG is not essential; other proteins compensate and free hormone remains normal via HP axis defense.",
                ref(
                    "Transport of Hormones in Blood",
                    "a specific protein may not be essential for hormone distribution. For example, in humans with congenital TBG deficiency, other proteins—transthyretin (TTR) and albumin—fulfill its function.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "miRNA signaling",
                "Exosomal miRNA from adipose tissue can regulate distant tissue gene expression and glucose tolerance.",
                True,
                "Adipose-derived exosomal miRNAs act as circulating adipokines with remote metabolic effects.",
                ref(
                    "Transport of Hormones in Blood",
                    "exosomal miRNA derived from adipose tissue regulates distant tissue gene expression, glucose tolerance, and levels of circulating fibroblast growth factor 21 (FGF21).",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Receptor downregulation",
                "Receptor endocytosis after ligand binding can lead to lysosomal degradation and impaired hormone signaling.",
                True,
                "Internalization followed by degradation downregulates receptors and attenuates signaling.",
                ref(
                    "Target Cells as Active Participants",
                    "the internalized receptor may undergo lysosomal degradation. Both of these mechanisms triggered by receptor activation effectively lead to impaired hormone signaling and receptor downregulation.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "GH and sleep",
                "Approximately 70% of daily GH secretion occurs during slow-wave sleep.",
                True,
                "Sleep is a major cue for GH pulsatility; aging reduces slow-wave sleep and GH.",
                ref(
                    "Control of Hormone Secretion",
                    "About 70% of overall GH secretion occurs during slow-wave sleep",
                ),
            ),
            tf(
                f"{p}-tf9",
                "TSH in hypothyroidism",
                "In iodine-deficient hypothyroidism, prolonged TSH stimulation can cause marked thyroid hyperplasia.",
                True,
                "TSH-driven hyperplasia in iodine deficiency can enlarge the thyroid 20–50 times normal.",
                ref(
                    "Endocrine Glands",
                    "in hypothyroid individuals living in iodine-deficient areas of the world, TSH secretion causes a marked hyperplasia of thyroid cells.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Stimulation testing",
                "Hormone hypersecretion is best diagnosed by attempting to evoke secretion with trophic hormones.",
                False,
                "Hypersecretion is diagnosed by failure to suppress; stimulation tests assess failed glandular function.",
                ref(
                    "Hormone Measurement",
                    "By contrast, hormone hypersecretion can best be diagnosed by suppressing glandular function.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Graves disease",
                "Graves hyperthyroidism involves polyclonal thyroid cell expansion stimulated by TSH-receptor antibodies.",
                True,
                "TSH-receptor antibodies cause polyclonal thyroid cell proliferation and hormone overproduction.",
                ref(
                    "Hormone Overproduction",
                    "hyperthyroidism associated with Graves disease, in which antibodies mimic TSH and activate the TSH receptors on thyroid cells, is accompanied by an increase in thyroid cell proliferation",
                ),
            ),
            tf(
                f"{p}-tf12",
                "GLP-1 formulations",
                "Once-weekly GLP-1 analogues exploit modified pharmacokinetics to reduce dosing frequency in type 2 diabetes.",
                True,
                "Fatty acid or antibody conjugation and peptide modification prolong half-life—enabling weekly GLP-1 administration.",
                ref(
                    "Diagnostic and Therapeutic Uses of Hormones",
                    "For example, a once-weekly preparation of glucagon-like peptide-1 (GLP1) analogue is used in the treatment of type 2 diabetes.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Hormone overreplacement",
                "Hormone therapies should be prescribed without restriction because replacement always restores normal physiology.",
                False,
                "Hormones are powerful; overreplacement causes disease and requires clear indications and qualified oversight.",
                ref(
                    "Diagnostic and Therapeutic Uses of Hormones",
                    "However, overreplacement is also associated with disease; thus, hormone therapies should not be prescribed without clear-cut indications",
                ),
            ),
        ]
    )

    # --- Assertion/Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Endocrine vs paracrine",
                "Assertion: Hormones must be produced in larger quantities than paracrine factors acting locally.",
                "Reason: Hormones travel through blood to distant targets and must survive transit and degradation to reach effective concentrations.",
                0,
                "Both are true and causally linked—distance and transport constraints drive higher hormonal production.",
                ref(
                    "The Evolutionary Perspective",
                    "hormones must be produced in much larger amounts to act as hormones, in contrast to much smaller amounts needed to act as paracrine factors acting locally.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "IGF1 binding proteins",
                "Assertion: IGF1 requires elaborate binding proteins for appropriate tissue signaling.",
                "Reason: IGF1 acts only as a circulating endocrine hormone and never as a local paracrine factor.",
                2,
                "Assertion is true; IGF1 also acts locally—the reason falsely denies paracrine function.",
                ref(
                    "The Evolutionary Perspective",
                    "IGF1 actions mandate an elaborate binding protein apparatus to enable appropriate hormone signaling as either a hormone or paracrine factor.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Free hormone hypothesis",
                "Assertion: Free thyroid hormone concentration is normal in congenital TBG deficiency.",
                "Reason: The hypothalamic-pituitary axis adjusts total hormone production to defend the free, biologically active fraction.",
                0,
                "Both are true; feedback maintains euthyroidism at lower total hormone when binding protein is absent.",
                ref(
                    "Transport of Hormones in Blood",
                    "The fact that the free hormone concentration is normal in individuals with TBG deficiency indicates that the hypothalamic-pituitary axis defends the free, active hormone.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Membrane receptors",
                "Assertion: Polypeptide hormones such as insulin act via cell-surface receptors.",
                "Reason: Steroid hormones use the same exclusively membrane-bound receptor mechanism.",
                1,
                "Assertion is true; steroids bind intracellular/nuclear receptors—the reason is false.",
                ref(
                    "Target Cells as Active Participants",
                    "Broadly, polypeptide hormone receptors are cell membrane associated, but steroid hormones selectively bind soluble intracellular proteins",
                ),
            ),
            ar(
                f"{p}-ar5",
                "TSH receptor mutations",
                "Assertion: Activating TSH receptor mutations can cause congenital hyperthyroidism.",
                "Reason: Activating mutations cause receptor hyperfunction even in the absence of TSH ligand.",
                0,
                "Both are true; constitutive activation explains autonomous thyroid hyperfunction.",
                ref(
                    "Target Cells as Active Participants",
                    "Constitutive receptor activation may be induced by activating mutations (e.g., TSH receptor) leading to endocrine organ hyperfunction, even in the absence of ligand.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Circadian ACTH",
                "Assertion: Loss of circadian ACTH rhythm with elevated midnight cortisol suggests Cushing disease.",
                "Reason: All pituitary hormones are secreted continuously without day-night variation.",
                3,
                "Assertion is true; most pituitary hormones follow circadian rhythms—the reason is false.",
                ref(
                    "Control of Hormone Secretion",
                    "loss of circadian ACTH secretion with high midnight cortisol levels is a feature of Cushing disease.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "HP axis tiers",
                "Assertion: Peripheral target hormones negatively feedback on pituitary trophic hormone secretion.",
                "Reason: Hypothalamic releasing hormones are secreted in milligram amounts with half-lives of days.",
                2,
                "Assertion is true; hypothalamic hormones are nanogram-scale with minute half-lives—the reason is false.",
                ref(
                    "Control of Hormone Secretion",
                    "Target hormones, in turn, serve as powerful negative feedback regulators of their respective trophic hormones",
                ),
            ),
            ar(
                f"{p}-ar8",
                "GH measurement",
                "Assertion: Random single GH samples may misrepresent true secretion because GH is episodic.",
                "Reason: GH is secreted at constant steady levels throughout the day like thyroid hormone.",
                3,
                "Assertion is true; GH is pulsatile and often requires timed or frequent sampling—the reason is false.",
                ref(
                    "Hormone Measurement",
                    "A 24-hour sampling for GH measurements, with samples collected every 2, 10, or 20 minutes, is expensive and cumbersome, yet it may yield valuable diagnostic information.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Consumptive hypothyroidism",
                "Assertion: Tumor overexpression of type 3 deiodinase can cause consumptive hypothyroidism.",
                "Reason: D3 activates T4 to T3 in target tissues.",
                2,
                "Assertion is true; D3 inactivates T3/T4 to reverse T3—the reason describes activation, not inactivation.",
                ref(
                    "Excessive Hormone Inactivation or Destruction",
                    "type 3 iodothyronine deiodinase (D3), which inactivates T_3 and T_4 by removing an inner ring iodine atom from the iodothyronine",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Autoimmune underproduction",
                "Assertion: Autoimmune destruction is a frequent cause of hormone underproduction.",
                "Reason: Type 1 diabetes and Hashimoto thyroiditis exemplify autoimmune gland destruction.",
                0,
                "Both are true; autoimmunity is among the most common endocrine disorders treated clinically.",
                ref(
                    "Hormone Underproduction",
                    "Autoimmune destruction of β-cells in type 1 diabetes mellitus and of thyroid cells in chronic lymphocytic (Hashimoto) thyroiditis are two of the most common disorders treated by endocrinologists.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Closed-loop insulin",
                "Assertion: Closed-loop insulin delivery systems can automatically adjust pump doses from continuous glucose monitoring.",
                "Reason: Closed-loop systems eliminate all hypoglycemia risk permanently.",
                1,
                "Assertion is true; closed-loop reduces burden but does not eliminate all hypoglycemia—the reason overstates benefit.",
                ref(
                    "Diagnostic and Therapeutic Uses of Hormones",
                    "Implementation of such closed-loop systems has the potential to substantially reduce the burden of this disease",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Orphan receptors",
                "Assertion: Discovery of ligands for orphan receptors has broadened understanding of hormonal signaling.",
                "Reason: All orphan receptors have now been fully characterized with no remaining unidentified ligands.",
                2,
                "Assertion is true (LXR and others); many orphan receptors and ligands remain to be discovered—the reason is false.",
                ref(
                    "Future Perspectives",
                    "New hormones are continually being discovered, from the recent focus on major regulators of metabolism and phosphate homeostasis (FGF19, FGF21, and FGF23) to the continued quest to identify ligands for orphan nuclear and G protein-coupled receptors.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "1",
        "title": "Principles of Endocrinology",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Shlomo Melmed, Richard J. Auchus, Allison B. Goldfine, Peter A. Kopp, Clifford J. Rosen",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_01_Principles_of_Endocrinology.md",
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
