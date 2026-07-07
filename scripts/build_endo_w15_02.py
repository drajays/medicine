#!/usr/bin/env python3
"""Generate Williams 15e module w15-02 — Principles of Hormone Action."""
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
OUT_NAME = "w15-02_Principles_of_Hormone_Action.json"


def build() -> dict:
    p = "w15-02"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Signal transduction",
                "Signal transduction in endocrine signaling",
                "Hormones encode environmental or developmental information at one site and transmit it to distant targets. The target cell must detect vanishingly low circulating concentrations and convert ligand binding into altered cellular activity—a process termed signal transduction, shared with neurotransmitters, drugs, and metabolites.",
                ref(
                    "Introduction to Hormone Signaling",
                    "Specifically, the concentration of the substance must be detected by the target cell and converted into a change in cellular activity, a process known as signal transduction.",
                ),
            ),
            note(
                f"{p}-n2",
                "Receptor localization",
                "Why polypeptide hormones require cell-surface receptors",
                "The plasma membrane bilayer excludes water-soluble peptides and charged molecules. Receptors for such ligands must reside on the outer cell surface (or ligands must be actively transported), with hormone binding initiating intracellular signaling cascades.",
                ref(
                    "Basic Principles of Hormone Action",
                    "The impermeability of the plasma membrane to peptides and small, water-soluble, charged molecules requires that receptors that recognize such substances be located on the outer surface of the cell or that such substances be actively transported into the cell.",
                ),
            ),
            note(
                f"{p}-n3",
                "Dual hormone roles",
                "Why IGF1 and norepinephrine act as hormone and local signal",
                "IGF1 circulates from liver under GH stimulation but is also produced locally (e.g., chondrocytes). Norepinephrine acts as a synaptic neurotransmitter and as an adrenal medullary hormone in blood—illustrating that strict endocrine definitions understate signaling complexity.",
                ref(
                    "Introduction to Hormone Signaling",
                    "insulin-like growth factor 1 (IGF1) is produced and secreted by the liver under the positive influence of GH and circulates to target tissues such as bone, but it is also produced locally by some tissues (e.g., chondrocytes at bone growth plates) to exert effects on neighboring cells.",
                ),
            ),
            note(
                f"{p}-n4",
                "Peptide secretion",
                "How secretory granules enable rapid peptide release",
                "Peptide hormones are preformed in 200-nm secretory granules via the regulated secretory pathway. Secretion can be evoked within milliseconds and terminated abruptly; short circulating half-lives allow rapid blood-level changes matching fast receptor on-rates.",
                ref(
                    "Basic Principles of Hormone Action",
                    "The cytoplasm of endocrine glands containing such secretory vesicles, such as the endocrine pancreas, the anterior pituitary, and the parathyroid glands, is filled with 200-nm electron-dense granules that represent the packaged hormone awaiting secretion.",
                ),
            ),
            note(
                f"{p}-n5",
                "IGF1 binding proteins",
                "How IGF1 binding proteins alter hormone kinetics",
                "Unlike most peptides, circulating IGF1 is largely bound to binding proteins—raising total concentration above free active hormone and prolonging half-life over hours to days. IGF1 therefore influences growth and differentiation through predominantly transcriptional targets.",
                ref(
                    "Basic Principles of Hormone Action",
                    "Unlike most peptide hormones, IGF1 circulates in the bloodstream bound to one or more binding proteins, which has two important consequences.",
                ),
            ),
            note(
                f"{p}-n6",
                "Thyroid transport",
                "Why thyroid hormone needs transporters despite nuclear receptors",
                "Thyroid hormone is more hydrophilic than classic steroids; despite intracellular nuclear receptors it requires transporters such as MCT8 or OATP1 to enter target cells. MCT8 mutations cause neurologic disease with elevated serum T3.",
                ref(
                    "Regulation of Hormone Levels",
                    "T_3 and T_4, for example, do not penetrate the hydrophobic membrane by themselves; they require a transporter such as MCT8 or OATP1.",
                ),
            ),
            note(
                f"{p}-n7",
                "Ligand promiscuity",
                "Why the mineralocorticoid receptor binds cortisol and aldosterone",
                "Ligand-receptor relationships are not always 1:1. The mineralocorticoid receptor binds aldosterone and cortisol with equal affinity and may function as a glucocorticoid receptor in some tissues such as brain.",
                ref(
                    "Basic Principles of Hormone Action",
                    "the mineralocorticoid receptor, also known as the aldosterone receptor, has equal affinity for aldosterone and cortisol and probably functions as a glucocorticoid receptor in some tissues, such as the brain.",
                ),
            ),
            note(
                f"{p}-n8",
                "Prohormone activation",
                "How inactive prohormones become active hormones",
                "Many hormones arise from inactive precursors—ACTH from POMC, insulin from proinsulin, T4→T3 by deiodination. Deficient convertases or activating enzymes cause hormone deficiency; pharmacologic enzyme inhibition can mimic excess states.",
                ref(
                    "Regulation of Hormone Levels",
                    "Many ligands are enzymatically converted from inactive prohormones to biologically active hormones; many protein hormones, for example, are generated as cleavage products of larger molecules, such as adrenocorticotropic hormone (ACTH) deriving from pro-opiomelanocortin, or insulin from proinsulin.",
                ),
            ),
            note(
                f"{p}-n9",
                "11βHSD",
                "How 11βHSD prevents apparent mineralocorticoid excess",
                "Renal 11β-hydroxysteroid dehydrogenase inactivates cortisol. Insufficient activity—from licorice, mutation, or extreme cortisol—allows cortisol to activate the mineralocorticoid receptor, producing apparent mineralocorticoid excess.",
                ref(
                    "Regulation of Hormone Levels",
                    "Because cortisol can activate the mineralocorticoid receptor, insufficient 11βHSD activity due to licorice ingestion, mutation within the gene, or extremely high cortisol levels cause syndromes of apparent mineralocorticoid excess.",
                ),
            ),
            note(
                f"{p}-n10",
                "Occupancy theory",
                "Why spare receptors buffer receptor number loss",
                "Biologic effect is proportional to receptor occupancy. Spare receptors allow maximal response before all receptors are occupied—so receptor number loss shifts ED50 without necessarily reducing maximal response, as with insulin.",
                ref(
                    "Binding Properties of Cell Surface Receptors",
                    "A subtle but important modification to occupancy theory is the notion of spare receptors, which describes the situation in which a maximal biologic response is achieved by occupancy of only a portion of the available receptors.",
                ),
            ),
            note(
                f"{p}-n11",
                "Desensitization",
                "How arrestins and SOCS terminate hormone signals",
                "Slow hormone off-rates conflict with rapid peptide signaling termination. Mechanisms include receptor-mediated endocytosis, arrestin uncoupling of GPCRs, SOCS on cytokine receptors, and insulin-receptor serine/threonine phosphorylation reducing tyrosine kinase activity.",
                ref(
                    "Binding Properties of Cell Surface Receptors",
                    "Arrestins, described in more detail later, act as intracellular desensitizers of several GPCRs, and a similar role is played by SOCS proteins on cytokine-like receptors.",
                ),
            ),
            note(
                f"{p}-n12",
                "GPCR structure",
                "G protein-coupled receptor architecture",
                "GPCRs have seven transmembrane α-helices (7TM) with extracellular N-terminus and cytoplasmic C-terminus. More than 800 human GPCRs exist (>2% of protein-coding genes), binding ligands from photons to large proteins.",
                ref(
                    "Types of Hormone Receptors G Protein-Coupled Receptors",
                    "There are more than 800 GPCR family members (>2% of all protein-coding genes), with the vast majority being olfactory receptors.",
                ),
            ),
            note(
                f"{p}-n13",
                "G protein families",
                "Gs, Gi, and Gq heterotrimeric G proteins",
                "Gαs activates adenylyl cyclase; Gαi family members inhibit it; Gαq/11 activates phospholipase Cβ generating DAG and IP3. RGS proteins accelerate GTP hydrolysis, shortening signal duration and enabling pathway crosstalk.",
                ref(
                    "Signaling by Heterotrimeric G Proteins",
                    "The Gα_s family has only two members, Gα_s and the G protein for the olfactory receptor, Gα_olf, both of which activate adenylyl cyclase.",
                ),
            ),
            note(
                f"{p}-n14",
                "β-arrestins",
                "β-arrestin desensitization and biased signaling",
                "GRK phosphorylation of agonist-bound GPCRs recruits β-arrestins, uncoupling G proteins and promoting endocytosis. β-arrestins also scaffold Src, MAPK, PI3K, and Akt—enabling biased signaling where ligands preferentially activate distinct downstream pathways.",
                ref(
                    "Signaling by Heterotrimeric G Proteins",
                    "β-arrestins are now known to bind multiple members of the Src family of tyrosine kinases as well as other proteins, such as mitogen-activated protein kinases (MAPKs, also known as extracellular kinases [ERKs]), phosphoinositide 3-kinase (PI3K), Akt, PDE4, and c-Jun N-terminal kinase-3.",
                ),
            ),
            note(
                f"{p}-n15",
                "GPCR diseases",
                "Endocrine diseases from GPCR and G protein mutations",
                "Loss-of-function GPCR mutations cause recessive disease: TRH/TSH receptor hypothyroidism, melanocortin 2 glucocorticoid deficiency, melanocortin 4 extreme obesity. Gain-of-function includes activating TSH receptor hyperthyroidism and Gαs pituitary adenomas in McCune-Albright.",
                ref(
                    "Diseases Caused by Mutations in GPCRs and G Proteins",
                    "some examples include hypothyroidism from mutations in the thyrotropin-releasing hormone (TRH) or TSH receptor, glucocorticoid deficiency from mutations in the melanocortin 2 receptor, extreme obesity from dysfunction of the melanocortin 4 receptor",
                ),
            ),
            note(
                f"{p}-n16",
                "Gαs imprinting",
                "Why maternal Gαs mutation causes pseudohypoparathyroidism",
                "Loss of paternal Gαs causes Albright hereditary osteodystrophy; maternal inheritance adds pseudohypoparathyroidism type 1a because Gαs is preferentially expressed from the maternal allele in several hormone target tissues.",
                ref(
                    "Diseases Caused by Mutations in GPCRs and G Proteins",
                    "Patients who inherit a loss of a functional paternal allele in Gα_s develop Albright hereditary osteodystrophy (AHO); those who inherit the mutant allele from their mothers also have pseudohypoparathyroidism type 1a in addition to AHO.",
                ),
            ),
            note(
                f"{p}-n17",
                "Insulin receptor structure",
                "Insulin receptor tetramer and negative cooperativity",
                "The insulin receptor is a disulfide-linked heterotetramer (two α, two β subunits)—unlike most RTK monomers. Insulin binding shows negative cooperativity: four sites per holoreceptor (two low-, two high-affinity) with one insulin per receptor at high-affinity occupancy.",
                ref(
                    "Receptor Tyrosine Protein Kinases",
                    "Insulin binding has been long recognized to exhibit negative cooperativity, which means that the affinity for additional hormone decreases as the population of receptors binds more ligands.",
                ),
            ),
            note(
                f"{p}-n18",
                "RTK activation",
                "How transphosphorylation activates RTK kinase domains",
                "Ligand closes the insulin/IGF1 receptor inverted-V, juxtaposing kinase domains. The activation loop blocks the catalytic cleft until transphosphorylation by the partner β-subunit forces it open—converting brief open conformations into stable active kinase.",
                ref(
                    "Receptor Tyrosine Protein Kinases",
                    "When the contralateral kinase domain is brought sufficiently close, it can phosphorylate the activation loop during the brief period it is in the extended position, converting this to the more stable conformation.",
                ),
            ),
            note(
                f"{p}-n19",
                "Insulin signaling",
                "How IRS proteins couple insulin to PI3K and Ras",
                "Activated insulin receptor phosphorylates IRS1/2, recruiting PI3K (Akt/metabolic arm) and GRB2-SOS (Ras-MAPK mitogenic arm) via SH2 domains. Spatial recruitment to membrane lipids often matters more than changing intrinsic enzyme activity.",
                ref(
                    "Signaling by Receptor Tyrosine Protein Kinases",
                    "IRS1 and IRS2 are heavily tyrosine phosphorylated by activated insulin receptor, generating binding sites for the SH2 domains of PI3K, GRB2, and the phosphotyrosine phosphatase SHP2.",
                ),
            ),
            note(
                f"{p}-n20",
                "GRB10 feedback",
                "GRB10 negative feedback on insulin signaling",
                "GRB10 binds phosphorylated activation-loop tyrosines and inhibits insulin receptor kinase activity and PIP3 production. mTORC1 phosphorylates and stabilizes GRB10, linking nutrient sensing to downregulation of IGF1/insulin signaling.",
                ref(
                    "Signaling by Receptor Tyrosine Protein Kinases",
                    "GRB10 is stabilized via phosphorylation by mammalian (mechanistic) target of rapamycin complex 1 (mTORC1), itself activated downstream of insulin, providing another form of negative feedback.",
                ),
            ),
            note(
                f"{p}-n21",
                "Insulin resistance",
                "Leprechaunism and type A insulin resistance",
                "Severe insulin receptor loss-of-function causes leprechaunism with developmental defects, acanthosis nigricans, and hyperandrogenism. Type B resistance features anti-receptor antibodies. Obesity-associated resistance often spares some insulin actions—a selective postreceptor defect.",
                ref(
                    "Insulin Resistance Syndromes",
                    "The strongest loss-of-function mutations result in leprechaunism, in which there are severe developmental defects presenting at birth.",
                ),
            ),
            note(
                f"{p}-n22",
                "TGFβ receptors",
                "TGFβ family serine/threonine kinase receptors",
                "TGFβ ligands signal through type I and type II receptor heterotetramers. Type II phosphorylates the GS domain of type I, relieving FKBP12 inhibition and activating type I kinase. Inhibin sequesters type II via betaglycan.",
                ref(
                    "Receptor Serine/Threonine Protein Kinases",
                    "Activin interacts initially with type 2 receptors, which brings the type 1 and type 2 receptors into proximity so that the type 2 receptors can phosphorylate the GS domain of the partner type 1 receptors.",
                ),
            ),
            note(
                f"{p}-n23",
                "SMAD pathway",
                "SMAD signaling downstream of TGFβ receptors",
                "Type I receptors phosphorylate receptor-regulated SMADs (R-SMADs), which trimerize with SMAD4 and translocate to the nucleus to regulate transcription. Inhibitory SMADs promote receptor ubiquitination and degradation.",
                ref(
                    "Receptor Serine/Threonine Protein Kinases",
                    "Two R-SMADs then form a trimer with the common partner SMAD or co-SMAD (SMAD4) and are transported to the nucleus.",
                ),
            ),
            note(
                f"{p}-n24",
                "Myostatin",
                "Myostatin as negative regulator of muscle mass",
                "Myostatin (GDF8) from skeletal muscle binds ActR-IIB and ALK4/ALK5, phosphorylating SMAD2/3 to limit muscle growth. Deficiency produces double-muscled cattle and massive hypertrophy in mice and humans.",
                ref(
                    "Receptor Serine/Threonine Protein Kinases",
                    "A deficiency of myostatin is responsible for the \"double-muscled\" phenotype of Belgian Blue and Piedmontese cattle, and deletion of its gene in mice and humans leads to massive muscle hypertrophy and hyperplasia.",
                ),
            ),
            note(
                f"{p}-n25",
                "JAK-STAT",
                "How JAK2 activation drives GH and leptin signaling",
                "GH, prolactin, and leptin use class I cytokine receptors associating with JAK2. Ligand-induced conformational change relieves pseudokinase inhibition, enabling STAT phosphorylation, dimerization, and nuclear gene regulation. SOCS proteins provide negative feedback.",
                ref(
                    "Enzyme-Associated Receptors",
                    "Binding of GH to its receptor results in a conformational change in the extracellular domain of the receptor, which induces a motion intracellular like the opening of scissors, causing sliding of the two subunits of JAK in opposite directions.",
                ),
            ),
            note(
                f"{p}-n26",
                "Nuclear receptors",
                "Nuclear receptor domains and coactivators",
                "Forty-eight human nuclear receptors regulate transcription via DNA-binding and ligand-binding domains. Agonist binding repositions helix 12, recruiting coactivators with LxxLL NR boxes and HAT activity; unliganded receptors recruit corepressors NCoR/SMRT and HDAC3.",
                ref(
                    "Receptor Regulation of Gene Transcription",
                    "Positively acting coregulators, called coactivators, specifically recognize the ligand-bound conformation of the LBD and bind to the nuclear receptor on DNA only when an activating (agonist) hormone or ligand is bound.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Signal transduction",
                "A resident reviews a patient with very low circulating peptide hormone levels who nonetheless mounts a robust cellular response. Which property of the hormone-receptor interaction best explains detection at vanishingly low concentrations?",
                [
                    "Rapid on-rate and high equilibrium affinity with slow off-rate",
                    "Exclusive nuclear receptor binding without membrane proteins",
                    "Requirement for millimolar hormone concentrations",
                    "Complete absence of receptor saturation limits",
                ],
                0,
                "Peptide hormones have rapid on-rates and slow off-rates yielding high equilibrium binding constants that enable detection of low blood levels.",
                ref(
                    "Basic Principles of Hormone Action",
                    "initiation of signaling tends to be rapid, which is facilitated by high on rates for hormone binding to receptors. In contrast, the off rate is often slow, which results in a high equilibrium binding constant that enables the receptors to detect the relatively low levels of hormone in blood.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Receptor classes",
                "A biochemistry fellow classifies hormones by receptor location. Which pairing is correct?",
                [
                    "Insulin—intracellular nuclear receptor",
                    "Thyroid hormone—exclusively cell-surface GPCR only",
                    "Growth hormone—cell-surface receptor without gene effects",
                    "Cortisol—intracellular nuclear receptor regulating transcription",
                ],
                3,
                "Steroid hormones including cortisol use intracellular/nuclear receptors; polypeptides and GH use cell-surface receptors.",
                ref(
                    "Introduction to Hormone Signaling",
                    "Classic hormones that use intracellular receptors include thyroid and steroid hormones.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "IGF1 kinetics",
                "A child with GH deficiency has low IGF1 that changes slowly over days after GH therapy begins. Compared with insulin, what best explains this pharmacokinetic pattern?",
                [
                    "IGF1 is stored in thyroid follicles as thyroglobulin",
                    "Circulating IGF1 is bound to binding proteins prolonging half-life",
                    "IGF1 acts only via synaptic cleft diffusion",
                    "IGF1 receptors are exclusively intranuclear",
                ],
                1,
                "IGF1 binding proteins raise total concentration and extend half-life, slowing circulating level changes versus typical peptides.",
                ref(
                    "Basic Principles of Hormone Action",
                    "the lifetime of IGF1 is greatly extended, such that circulating levels of the hormone change slowly over the course of hours or days.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "MCT8 deficiency",
                "A boy has severe intellectual disability, movement disorder, and elevated serum T3 with neurologic features. Sequencing reveals MCT8 mutation. What is the most likely mechanism?",
                [
                    "Excess thyroid hormone synthesis in the pituitary",
                    "Impaired T3 entry into neurons despite high circulating T3",
                    "Complete loss of all thyroid hormone receptors",
                    "Constitutive activation of TSH receptor",
                ],
                1,
                "MCT8 mutations impair thyroid hormone transport into neurons, causing neurologic disease with elevated serum T3.",
                ref(
                    "Regulation of Hormone Levels",
                    "Mutations in MCT8, for example, lead to neurologic issues, including severe intellectual disability and movement disorders with elevated serum T_3.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "MR promiscuity",
                "A patient with hypertension and hypokalemia chews licorice daily. Plasma renin is suppressed. Cortisol levels are normal. Which mechanism best explains mineralocorticoid excess?",
                [
                    "Aldosterone-secreting adrenal adenoma",
                    "11βHSD inhibition allowing cortisol to activate MR",
                    "Activating mutation of the calcium-sensing receptor",
                    "Loss of androgen receptor function",
                ],
                1,
                "Licorice inhibits renal 11βHSD, preventing cortisol inactivation and causing apparent mineralocorticoid excess.",
                ref(
                    "Regulation of Hormone Levels",
                    "insufficient 11βHSD activity due to licorice ingestion, mutation within the gene, or extremely high cortisol levels cause syndromes of apparent mineralocorticoid excess.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Spare receptors",
                "An obese patient has half the insulin receptor number of a lean control, yet both achieve similar maximal glucose uptake at high insulin doses. The obese patient's insulin ED50 is higher. Which concept explains this?",
                [
                    "Spare receptors—maximal response before full occupancy",
                    "Complete insulin receptor kinase deletion",
                    "Constitutive Gαs activation",
                    "Leprechaunism from receptor overexpression",
                ],
                0,
                "Spare receptors permit maximal biologic response below full occupancy; receptor loss increases ED50 without necessarily reducing Vmax.",
                ref(
                    "Binding Properties of Cell Surface Receptors",
                    "One consequence of the existence of spare receptors is that a decrease in the number of cellular receptors results in a change in the ED_{50} (effective dose for eliciting a 50% response) for a hormone but does not necessarily alter the maximal biologic response",
                ),
            ),
            mcq(
                f"{p}-q7",
                "GPCR structure",
                "A pharmacology student describes a receptor with seven membrane-spanning helices coupling to heterotrimeric G proteins. Approximately how many such receptors exist in the human genome?",
                [
                    "Fewer than 50",
                    "About 200",
                    "More than 800 (>2% of protein-coding genes)",
                    "Exactly 48 matching nuclear receptors",
                ],
                2,
                "The GPCR superfamily comprises more than 800 members, over 2% of human protein-coding genes.",
                ref(
                    "Types of Hormone Receptors G Protein-Coupled Receptors",
                    "There are more than 800 GPCR family members (>2% of all protein-coding genes), with the vast majority being olfactory receptors.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "G protein signaling",
                "Epinephrine raises hepatic cAMP. Which G protein α-subunit family mediates adenylyl cyclase activation?",
                [
                    "Gαi inhibiting adenylyl cyclase",
                    "Gαs activating adenylyl cyclase",
                    "Gα12 inhibiting RhoGEF only",
                    "Gαq generating cGMP directly",
                ],
                1,
                "Gαs binds GTP and activates adenylyl cyclase—the pathway used by β-adrenergic and many glycoprotein hormone receptors.",
                ref(
                    "Signaling by Heterotrimeric G Proteins",
                    "The GTP-bound α-subunit of G_s is necessary and sufficient for activation of its downstream target, adenylyl cyclase.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "RGS proteins",
                "Prolonged TSH stimulation increases RGS2 expression in thyrotrophs, dampening Gαs signaling. What is the primary biochemical function of RGS proteins?",
                [
                    "Phosphorylate GPCR C-terminal serines",
                    "Accelerate Gα GTPase activity shortening signal duration",
                    "Synthesize cAMP from ATP",
                    "Transport receptors to the nucleus",
                ],
                1,
                "RGS proteins are GTPase-accelerating proteins that shorten G protein signaling by promoting GTP→GDP hydrolysis.",
                ref(
                    "Signaling by Heterotrimeric G Proteins",
                    "RGS proteins, which function as GTPase accelerating proteins (GAPs), serve to shorten the duration of signaling by G proteins",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Biased signaling",
                "A drug company develops an opioid that provides analgesia with less tolerance. Which GPCR concept guides this effort?",
                [
                    "Biased signaling favoring G protein over β-arrestin pathways",
                    "Elimination of all seven transmembrane helices",
                    "Constitutive receptor internalization without ligand",
                    "Exclusive nuclear translocation of β-arrestin",
                ],
                0,
                "Biased signaling exploits ligand-specific stabilization of receptor conformations that preferentially activate G protein versus arrestin pathways.",
                ref(
                    "Signaling by Heterotrimeric G Proteins",
                    "biased signaling,\" defined as the ability of ligands to stimulate distinct downstream signaling pathways, presumably due to stabilization of distinct conformational states of the receptor.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Melanocortin 4",
                "A teenager with severe early-onset obesity has no detectable MC4R-stimulating antibodies. Genetic testing is sent. Which receptor is most likely mutated?",
                [
                    "Melanocortin 4 receptor",
                    "Insulin receptor",
                    "Vitamin D receptor",
                    "GH receptor only",
                ],
                0,
                "Melanocortin 4 receptor dysfunction causes extreme obesity among recessive GPCR loss-of-function mutations.",
                ref(
                    "Diseases Caused by Mutations in GPCRs and G Proteins",
                    "extreme obesity from dysfunction of the melanocortin 4 receptor",
                ),
            ),
            mcq(
                f"{p}-q12",
                "McCune-Albright",
                "A girl has café-au-lait macules, precocious puberty, and GH-secreting pituitary adenoma. Which molecular defect is most likely?",
                [
                    "Loss-of-function TSH receptor",
                    "Activating Gαs mutation (somatic or mosaic)",
                    "MCT8 transporter deficiency",
                    "Recessive androgen receptor mutation",
                ],
                1,
                "Dominant activating Gαs mutations cause pituitary and other endocrine adenomas characteristic of McCune-Albright syndrome.",
                ref(
                    "Diseases Caused by Mutations in GPCRs and G Proteins",
                    "Dominant, activating mutations of Gα_s cause pituitary adenomas, most often secreting GH",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Insulin receptor",
                "A structural biology fellow models the insulin receptor. Which description is accurate?",
                [
                    "Monomeric RTK like the EGF receptor",
                    "Disulfide-linked α2β2 heterotetramer with negative cooperativity",
                    "Seven-transmembrane GPCR coupled to Gi",
                    "Ligand-gated pentameric ion channel",
                ],
                1,
                "The insulin receptor uniquely exists as a disulfide-linked heterotetramer exhibiting negative cooperativity in ligand binding.",
                ref(
                    "Receptor Tyrosine Protein Kinases",
                    "the insulin receptor, which, unlike other RTKs, exists as a disulfide-linked tetramer in the basal state.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Insulin signaling",
                "Insulin stimulation of a hepatocyte increases glucose uptake. Which downstream pathway is most directly involved in many metabolic insulin actions?",
                [
                    "IRS → PI3K → PIP3 → Akt",
                    "SMAD4 nuclear translocation only",
                    "Direct glucocorticoid receptor transactivation",
                    "JAK3 without STAT proteins",
                ],
                0,
                "IRS tyrosine phosphorylation recruits PI3K to generate PIP3 and activate Akt—central to insulin metabolic signaling.",
                ref(
                    "Signaling by Receptor Tyrosine Protein Kinases",
                    "Activation of PI3K leads to activation of phosphoinositide-dependent kinases (PDKs) 1 and 2, which activate multiple protein kinases, including Akt/protein kinase B",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Selective insulin resistance",
                "A woman with PCOS has hyperglycemia and hyperinsulinemia but preserved hepatic lipid regulation compared with a patient with type A insulin receptor mutation. What best explains this?",
                [
                    "Obesity-associated selective postreceptor insulin resistance",
                    "Complete loss of all insulin receptor signaling",
                    "Identical phenotype to leprechaunism",
                    "Exclusive nuclear receptor defect",
                ],
                0,
                "Obesity/PCOS insulin resistance selectively impairs some insulin actions whereas receptor mutations affect broader signaling including hepatic lipid regulation.",
                ref(
                    "Insulin Resistance Syndromes",
                    "in the insulin resistance of obesity or PCOS, some actions of insulin are preserved.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Activin/inhibin",
                "Inhibin suppresses FSH secretion while activin stimulates it. How does inhibin antagonize activin signaling?",
                [
                    "Recruits betaglycan to sequester type II receptors from type I partners",
                    "Activates insulin receptor tyrosine kinase directly",
                    "Blocks all SMAD4 gene transcription permanently",
                    "Opens ligand-gated chloride channels in gonadotrophs",
                ],
                0,
                "Inhibin recruits betaglycan (type III receptor) to complex with type II receptors, preventing type I receptor activation.",
                ref(
                    "Receptor Serine/Threonine Protein Kinases",
                    "Inhibin exerts its inhibitory action by recruiting the transmembrane glycoprotein betaglycan (also called the type III receptor) to form a stable complex with type 2 receptors",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Myostatin",
                "Belgian Blue cattle display marked muscle hypertrophy. Which signaling molecule is deficient?",
                [
                    "Myostatin (GDF8)",
                    "Leptin",
                    "TSH",
                    "Calcitonin",
                ],
                0,
                "Myostatin deficiency causes the double-muscled phenotype in cattle and massive hypertrophy when deleted in mice and humans.",
                ref(
                    "Receptor Serine/Threonine Protein Kinases",
                    "A deficiency of myostatin is responsible for the \"double-muscled\" phenotype of Belgian Blue and Piedmontese cattle",
                ),
            ),
            mcq(
                f"{p}-q18",
                "GH signaling",
                "Acromegaly is treated with pegvisomant, a GH antagonist. What is its mechanism at the receptor level?",
                [
                    "Prevents functional GH receptor dimerization",
                    "Activates JAK2 constitutively",
                    "Blocks MCT8 thyroid transport",
                    "Inhibits 11βHSD in liver",
                ],
                0,
                "Pegvisomant competes with native GH and prevents functional receptor dimerization, blocking GH signaling.",
                ref(
                    "Enzyme-Associated Receptors",
                    "Pegvisomant competes with native GH for its receptor and prevents functional dimerization.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Leptin signaling",
                "Leptin-deficient humans develop massive early obesity. Which STAT isoform is critical for leptin's effects on appetite and energy balance?",
                [
                    "STAT3 via YXXQ motif on LepRb",
                    "STAT5b exclusively without STAT3",
                    "SMAD2 only",
                    "CREB without JAK activation",
                ],
                0,
                "Mutating leptin receptor tyrosine 1138 blocks STAT3 recruitment and produces obesity similar to leptin receptor knockout.",
                ref(
                    "Enzyme-Associated Receptors",
                    "Replacement of tyrosine 1138 by serine completely blocks recruitment of STAT3, generating mice similar in their degree of obesity to those lacking leptin receptors",
                ),
            ),
            mcq(
                f"{p}-q20",
                "SOCS proteins",
                "SOCS2-null mice grow larger after weaning. What is SOCS2's role in cytokine signaling?",
                [
                    "Negative feedback inhibitor of JAK-STAT induced by STATs",
                    "Constitutive GH receptor agonist",
                    "Thyroid hormone transporter",
                    "Gαs GTPase accelerator",
                ],
                0,
                "SOCS proteins are STAT-inducible negative regulators that inhibit JAK activity and promote receptor degradation.",
                ref(
                    "Enzyme-Associated Receptors",
                    "The eight members of the SOCS family are direct targets of the STAT transcription factors and provide a potent negative feedback signal",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Ligand-gated channels",
                "Serotonin stimulates prolactin release from lactotrophs. Through which receptor class does this likely occur?",
                [
                    "Ligand-gated ion channel (5HT3R)",
                    "Nuclear vitamin D receptor homodimer",
                    "TGFβ type I serine kinase receptor",
                    "Insulin receptor tetramer",
                ],
                0,
                "Hypothalamic factors including serotonin may regulate pituitary secretion via ligand-gated ion channels such as 5HT3R.",
                ref(
                    "Ligand-Gated Ion Channels",
                    "it is thought that serotonin regulates release of prolactin by binding to the 5HT3R receptor in lactotrophs of the anterior pituitary.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "cAMP signaling",
                "Glucagon raises hepatic glucose output within minutes. Which second messenger mediates this classic response?",
                [
                    "cAMP produced by adenylyl cyclase",
                    "Vitamin D binding to VDR in nucleus only",
                    "Direct SMAD nuclear import without kinase",
                    "Passive steroid diffusion without receptors",
                ],
                0,
                "Glucagon and β-adrenergic agonists use Gαs-adenylyl cyclase to generate cAMP as the prototypical second messenger.",
                ref(
                    "Coupling of Cell Surface Receptors to Intracellular Signaling",
                    "For hepatic glycogen breakdown in response to glucagon or β-adrenergic agonists, the second messenger is cAMP, which is produced from ATP by a plasma membrane enzyme called adenylyl cyclase.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Nuclear receptors",
                "How many members comprise the human nuclear receptor superfamily?",
                [
                    "12 classic hormones only with no orphans",
                    "48 members including adopted orphan receptors",
                    "More than 800 identical to GPCRs",
                    "Four JAK family proteins",
                ],
                1,
                "Humans have 48 nuclear receptors; 12 bind classic hormones and many orphans have since been adopted with identified ligands.",
                ref(
                    "Nuclear Hormone Receptors",
                    "The nuclear receptor superfamily includes 48 members in humans, although many species have more",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Corepressors",
                "In hypothyroidism, unliganded thyroid receptor on DNA represses target genes. Which corepressor complex mediates this?",
                [
                    "NCoR/SMRT recruiting HDAC3",
                    "β-arrestin and clathrin only",
                    "SOCS box proteins degrading JAK2",
                    "GRB10 blocking insulin kinase",
                ],
                0,
                "Unliganded nuclear receptors recruit NCoR and SMRT, which activate HDAC3 to compact chromatin and repress transcription.",
                ref(
                    "Receptor Regulation of Gene Transcription",
                    "The two major corepressors are large (approximately 270 kDa) proteins: nuclear receptor corepressor (NCoR) and silencing mediator for retinoid and thyroid receptors (SMRT, also known as NCoR2).",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Nongenomic steroid action",
                "Estrogen increases endothelial nitric oxide within seconds—too fast for transcription. Which mechanism is supported?",
                [
                    "Membrane-associated nuclear receptor activating Src/ERK/Akt signalosome",
                    "Exclusive requirement for weeks of mRNA synthesis",
                    "Direct binding to nicotinic acetylcholine receptor only",
                    "Complete absence of any receptor protein",
                ],
                0,
                "Steroid and thyroid hormones can activate membrane-associated receptor signalosomes engaging classic kinase pathways within seconds.",
                ref(
                    "Nongenomic Actions of Nuclear Receptor Ligands",
                    "Often, nongenomic nuclear receptor action originates at the cell membrane, where the receptors physically interact with kinases in a signaling complex, referred to as the signalosome",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Nuclear receptor diseases",
                "A 46,XY individual has female external genitalia, normal breast development, and a blind vaginal pouch. Testosterone is elevated. Which diagnosis is most likely?",
                [
                    "Complete androgen insensitivity (X-linked AR mutation)",
                    "Resistance to thyroid hormone β",
                    "Hereditary calcitriol-resistant rickets (recessive VDR)",
                    "Activating TSH receptor mutation",
                ],
                0,
                "Androgen insensitivity from X-linked androgen receptor mutations causes female phenotype in 46,XY individuals despite elevated androgens.",
                ref(
                    "Diseases Caused by Mutations in Nuclear Hormone Receptors",
                    "Inheritance can also be X-linked, as with the mutated androgen receptor in androgen insensitivity syndromes.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Signal transduction",
                "Signal transduction is the process by which a target cell detects an extracellular substance and converts that recognition into altered cellular activity.",
                True,
                "This is the textbook definition of signal transduction in hormone action.",
                ref(
                    "Introduction to Hormone Signaling",
                    "the concentration of the substance must be detected by the target cell and converted into a change in cellular activity, a process known as signal transduction.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Membrane impermeability",
                "Water-soluble peptide hormones freely diffuse across the plasma membrane bilayer without surface receptors.",
                False,
                "Membrane impermeability to peptides requires cell-surface receptors or active transport.",
                ref(
                    "Basic Principles of Hormone Action",
                    "The strongly nonpolar environment prevents the diffusion of water-soluble molecules, including many hormones, across the membrane.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "IGF1",
                "IGF1 circulates unbound with a very short half-life similar to most peptide hormones.",
                False,
                "IGF1 is bound to binding proteins, extending its half-life over hours to days.",
                ref(
                    "Basic Principles of Hormone Action",
                    "IGF1 circulates in the bloodstream bound to one or more binding proteins",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Ligand promiscuity",
                "The mineralocorticoid receptor binds aldosterone and cortisol with equal affinity.",
                True,
                "MR promiscuity explains cortisol-mediated mineralocorticoid effects when 11βHSD is impaired.",
                ref(
                    "Basic Principles of Hormone Action",
                    "the mineralocorticoid receptor, also known as the aldosterone receptor, has equal affinity for aldosterone and cortisol",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Occupancy theory",
                "Biologic effect is directly proportional to ligand occupancy of the receptor.",
                True,
                "This is the fundamental occupancy rule governing extracellular agent action.",
                ref(
                    "Binding Properties of Cell Surface Receptors",
                    "a biologic effect is directly proportional to the ligand occupancy of the receptor.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "GPCRs",
                "GPCRs are seven-transmembrane receptors that couple to heterotrimeric G proteins.",
                True,
                "7TM architecture with G protein coupling defines the largest cell-surface receptor family.",
                ref(
                    "Types of Hormone Receptors G Protein-Coupled Receptors",
                    "These receptors have seven α-helical segments of about 25 amino acids that pass through the plasma membrane",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Gαq signaling",
                "Gαq/11 family members activate phospholipase Cβ generating DAG and IP3.",
                True,
                "Gαq/11 activates PLCβ, raising calcium and activating PKC via DAG.",
                ref(
                    "Signaling by Heterotrimeric G Proteins",
                    "The Gα_q/11 subfamily consists of six members, all of which activate the enzyme phospholipase C beta (PLCβ), generating the second messengers diacylglycerol (DAG) and inositol trisphosphate (IP_3).",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Insulin receptor",
                "The insulin receptor exists as a disulfide-linked heterotetramer unlike most other RTKs.",
                True,
                "Insulin and IGF1 receptors are unique heterotetrameric RTKs.",
                ref(
                    "Receptor Tyrosine Protein Kinases",
                    "the insulin receptor, which, unlike other RTKs, exists as a disulfide-linked tetramer in the basal state.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Leprechaunism",
                "Severe insulin receptor loss-of-function can cause leprechaunism with profound developmental defects at birth.",
                True,
                "Leprechaunism represents the most severe insulin receptor dysfunction phenotype.",
                ref(
                    "Insulin Resistance Syndromes",
                    "The strongest loss-of-function mutations result in leprechaunism, in which there are severe developmental defects presenting at birth.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "TGFβ signaling",
                "TGFβ family ligands signal through receptor serine/threonine kinases and SMAD transcription factors.",
                True,
                "Type I/II receptor kinases phosphorylate R-SMADs that partner with SMAD4 in the nucleus.",
                ref(
                    "Receptor Serine/Threonine Protein Kinases",
                    "The major intracellular signaling mechanism utilized by all members of the TGFβ family involves SMAD proteins",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Leptin",
                "Leptin signals primarily through LepRb activating JAK2 and STAT3 to regulate appetite and energy balance.",
                True,
                "STAT3 recruitment at Tyr1138 is critical for leptin's metabolic effects.",
                ref(
                    "Enzyme-Associated Receptors",
                    "In contrast to the GH receptor, LepRb recruits STAT3 as its primary signaling molecule",
                ),
            ),
            tf(
                f"{p}-tf12",
                "cAMP",
                "cAMP is the second messenger for glucagon-stimulated hepatic glycogen breakdown.",
                True,
                "Glucagon and β-adrenergic agonists raise cAMP via Gαs and adenylyl cyclase.",
                ref(
                    "Coupling of Cell Surface Receptors to Intracellular Signaling",
                    "For hepatic glycogen breakdown in response to glucagon or β-adrenergic agonists, the second messenger is cAMP",
                ),
            ),
            tf(
                f"{p}-tf13",
                "RTH inheritance",
                "Resistance to thyroid hormone is typically inherited in a dominant manner when mutant receptor inhibits normal receptor function.",
                True,
                "Dominant-negative LBD mutations that favor repression cause dominant RTH.",
                ref(
                    "Diseases Caused by Mutations in Nuclear Hormone Receptors",
                    "Inheritance of the hormone resistance phenotype is dominant if the mutant receptor inhibits the action of the normal receptor, as occurs with resistance to thyroid hormone (RTHβ and RTHα)",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Dual signaling molecules",
                "Assertion: Norepinephrine can act as both a neurotransmitter and a classic endocrine hormone.",
                "Reason: Norepinephrine is released only at synapses and cannot enter the bloodstream.",
                2,
                "Assertion is true (adrenal medullary secretion); the reason falsely denies endocrine hormone action.",
                ref(
                    "Introduction to Hormone Signaling",
                    "norepinephrine is a neurotransmitter that is released at nerve endings and binds to cell surface receptors at postsynaptic membranes, but it is also secreted into the blood by the adrenal medulla, allowing it to act as a classic endocrine hormone.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Peptide storage",
                "Assertion: Peptide hormones stored in secretory granules can be released within milliseconds of stimulation.",
                "Reason: Peptide hormones are synthesized de novo only after stimulation without preformed storage.",
                3,
                "Assertion is true; peptides are preformed in granules—the reason describing only on-demand synthesis is false.",
                ref(
                    "Basic Principles of Hormone Action",
                    "secretion of hormones stored within vesicles can be evoked quickly, often within milliseconds",
                ),
            ),
            ar(
                f"{p}-ar3",
                "MCT8",
                "Assertion: MCT8 mutations cause neurologic disease with elevated serum T3.",
                "Reason: MCT8 is required for thyroid hormone transport into cells such as neurons.",
                0,
                "Both are true; impaired neuronal T3 entry explains the phenotype despite high circulating T3.",
                ref(
                    "Regulation of Hormone Levels",
                    "In this condition, it seems likely that the pathology is secondary to the inability of T_3 to enter neurons.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "11βHSD",
                "Assertion: Licorice ingestion can cause apparent mineralocorticoid excess.",
                "Reason: Licorice inhibits 11βHSD allowing cortisol to activate the mineralocorticoid receptor.",
                0,
                "Both are true; insufficient cortisol inactivation at the renal MR causes the syndrome.",
                ref(
                    "Regulation of Hormone Levels",
                    "insufficient 11βHSD activity due to licorice ingestion, mutation within the gene, or extremely high cortisol levels cause syndromes of apparent mineralocorticoid excess.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "β-arrestins",
                "Assertion: β-arrestins terminate GPCR signaling by uncoupling receptors from G proteins.",
                "Reason: β-arrestins have no role beyond blocking G protein coupling and cannot scaffold other kinases.",
                1,
                "Assertion is true; β-arrestins also signal via Src, MAPK, PI3K—the reason denying this is false.",
                ref(
                    "Signaling by Heterotrimeric G Proteins",
                    "In addition to their role in the modulation of G protein signaling, β-arrestins function as signaling intermediates.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "TSH receptor",
                "Assertion: Activating TSH receptor mutations can cause nonautoimmune hyperthyroidism.",
                "Reason: Activating mutations produce constitutive receptor signaling without TSH ligand.",
                0,
                "Both are true; gain-of-function TSH receptor mutations are a known cause of hyperthyroidism.",
                ref(
                    "Diseases Caused by Mutations in GPCRs and G Proteins",
                    "Gain-of-function mutations include, for example, those in the TSH receptor causing nonautoimmune (sporadic or autosomal dominant) hyperthyroidism",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Insulin receptor",
                "Assertion: Insulin receptor activation requires transphosphorylation of the activation loop.",
                "Reason: Dimerization alone is sufficient to fully activate all RTKs without conformational change.",
                2,
                "Assertion is true; dimerization alone is insufficient—the reason is false for insulin/IGF1 receptors.",
                ref(
                    "Receptor Tyrosine Protein Kinases",
                    "In general, activation of RTKs requires the formation of a receptor dimer. In some cases, such as the insulin, IGF1, FGF, and EGF receptors, the unbound receptors appear to consist of preformed dimers. In other cases, bivalent ligand binding to two receptor monomers is thought to promote dimer formation.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "GRB10",
                "Assertion: GRB10 provides negative feedback on insulin receptor signaling.",
                "Reason: GRB10 enhances insulin receptor kinase activity and increases PIP3 production.",
                2,
                "Assertion is true; GRB10 binds the activation loop and inhibits receptor kinase—the reason states the opposite.",
                ref(
                    "Signaling by Receptor Tyrosine Protein Kinases",
                    "unlike the IRS proteins, GRB10 binds to the three phosphorylated tyrosine residues in the activation loop and blocks the activity of the insulin receptor, inhibiting the insulin-dependent production of PIP_3.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Obesity insulin resistance",
                "Assertion: Obesity-associated insulin resistance may spare some insulin actions.",
                "Reason: All forms of insulin resistance identically impair every downstream insulin output.",
                3,
                "Assertion is true; selective/postreceptor resistance differs from receptor mutations—the reason is false.",
                ref(
                    "Insulin Resistance Syndromes",
                    "in the insulin resistance of obesity or PCOS, some actions of insulin are preserved.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Myostatin",
                "Assertion: Myostatin deficiency causes increased muscle mass.",
                "Reason: Myostatin is a positive regulator of muscle hypertrophy through SMAD signaling.",
                2,
                "Assertion is true; myostatin negatively regulates muscle growth—the reason reverses its function.",
                ref(
                    "Receptor Serine/Threonine Protein Kinases",
                    "Myostatin is secreted by skeletal muscle and negatively regulates muscle growth",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Leptin resistance",
                "Assertion: SOCS proteins contribute to termination of cytokine and leptin receptor signaling.",
                "Reason: SOCS proteins are constitutively active without any transcriptional induction.",
                1,
                "Assertion is true; SOCS are STAT-inducible feedback inhibitors—the reason denying induction is false.",
                ref(
                    "Enzyme-Associated Receptors",
                    "Termination of class I cytokine signaling occurs in response to dephosphorylation of key phosphotyrosines; it is also promoted by the transcriptional induction of the suppressors of cytokine signaling, or SOCS proteins.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Vitamin D resistance",
                "Assertion: Hereditary calcitriol-resistant rickets results from recessive VDR loss-of-function mutations.",
                "Reason: VDR mutations causing resistance are always dominant-negative like RTH.",
                2,
                "Assertion is true; complete VDR loss is recessive—RTH-like dominance does not apply to all nuclear receptor diseases.",
                ref(
                    "Diseases Caused by Mutations in Nuclear Hormone Receptors",
                    "Inheritance is recessive if the mutation results in a complete loss of receptor function, as with the syndrome of hereditary calcitriol-resistant rickets, which is caused by mutations in the VDR.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "2",
        "title": "Principles of Hormone Action",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Evan D. Rosen, Lars C. Moeller, Liangyou Rui",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_02_Principles_of_Hormone_Action.md",
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
