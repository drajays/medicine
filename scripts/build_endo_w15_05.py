#!/usr/bin/env python3
"""Generate Williams 15e module w15-05 — Neuroendocrinology."""
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
OUT_NAME = "w15-05_Neuroendocrinology.json"


def build() -> dict:
    p = "w15-05"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Neurosecretion",
                "Neurosecretion and hypothalamic hormone release",
                "Neurosecretory cells are neurons whose axon terminals release signaling molecules directly into the bloodstream. Hypophysiotropic neurons secrete into pituitary portal vessels at the median eminence; magnocellular PVH/SON neurons release AVP and oxytocin from the neural lobe.",
                ref(
                    "Neurosecretion",
                    "In the most basic sense, neurosecretory cells are neurons that secrete substances directly into the bloodstream to act as hormones.",
                ),
            ),
            note(
                f"{p}-n2",
                "Harris portal system",
                "Why Harris's portal experiments established hypothalamic pituitary control",
                "Wislocki, King, and Harris showed portal blood flows from the median eminence to the pituitary and that hypothalamic stimulation fails to elicit a pituitary response after stalk section—proving hypothalamic factors reach the adenohypophysis via portal vessels, not axonal transport alone.",
                ref(
                    "Historical Perspective",
                    "evidence by Wislocki and King and Harris that the blood flow in portal vessels is directed to the pituitary gland from the hypothalamic median eminence and electric stimulation of the hypothalamus is ineffective in eliciting a pituitary response if the pituitary stalk is severed",
                ),
            ),
            note(
                f"{p}-n3",
                "Historical perspective",
                "Galen, Fröhlich syndrome, and early hypothalamic-pituitary links",
                "Galen described the infundibulum–pituitary connection in the 2nd century AD. Medial basal hypothalamic lesions recapitulate Fröhlich's 1901 syndrome of obesity, hypogonadotropic hypogonadism, and growth retardation. Schally and Guillemin later identified hypothalamic releasing factors (Nobel 1977).",
                ref(
                    "Historical Perspective",
                    "destruction of the medial basal hypothalamus sparing the pituitary gland results in morbid obesity and neuroendocrine derangements recapitulating the syndrome of obesity, hypogonadotropic hypogonadism, and growth retardation described by Alfred Fröhlich in 1901.",
                ),
            ),
            note(
                f"{p}-n4",
                "Releasing factors",
                "How Schally and Guillemin identified hypothalamic releasing factors",
                "Both groups purified peptide releasing factors from enormous numbers of hypothalamic fragments—approximately 250,000 fragments for TRH alone—establishing that the anterior pituitary is tightly controlled by hypothalamic hormones secreted into portal circulation.",
                ref(
                    "Hypophysiotropic Hormones and Neuroendocrine Axes",
                    "approximately 250,000 hypothalamic fragments were required to purify and characterize the first such factor, TRH.",
                ),
            ),
            note(
                f"{p}-n5",
                "Neuron subtypes",
                "Why magnocellular and hypophysiotropic neurons differ anatomically",
                "Magnocellular PVH/SON neurons project to the neural lobe for AVP/oxytocin release into systemic circulation. Hypophysiotropic parvocellular neurons terminate at fenestrated portal capillaries in the median eminence external zone to regulate adenohypophysis secretion.",
                ref(
                    "Neurosecretion",
                    "Hypophysiotropic cells encompass all neurons that secrete their products into the pituitary portal vessels at the median eminence",
                ),
            ),
            note(
                f"{p}-n6",
                "Autonomic endocrine control",
                "Autonomic innervation of endocrine glands",
                "Beyond hypophysiotropic hormones, pancreas, adrenal, pineal, and salivary glands receive direct cholinergic and noradrenergic autonomic innervation. Sympathetic postganglionic neurons are noradrenergic (except sweat glands); parasympathetic postganglionic neurons are cholinergic.",
                ref(
                    "Contribution of the Autonomic Nervous System to Endocrine Control",
                    "Other endocrine and exocrine organs (e.g., pancreas and adrenal, pineal, and salivary glands) are also regulated through direct innervation from the cholinergic and noradrenergic inputs from the autonomic nervous system.",
                ),
            ),
            note(
                f"{p}-n7",
                "Cephalic phase insulin",
                "How vagal cholinergic tone modulates insulin secretion",
                "Parasympathetic vagal input from the dorsal motor nucleus modulates β-cell insulin secretion before, during, and after food ingestion—the cephalic phase. Noradrenergic sympathetic input can stimulate glucagon and inhibit insulin release.",
                ref(
                    "Contribution of the Autonomic Nervous System to Endocrine Control",
                    "vagal input is thought to modulate insulin secretion before (cephalic phase), during, and after ingestion of food.",
                ),
            ),
            note(
                f"{p}-n8",
                "Glucose sensing",
                "How hypothalamic glucose sensors initiate counterregulation",
                "Ventromedial and perifornical hypothalamic neurons and rostral ventrolateral medulla catecholamine neurons sense blood glucose like pancreatic β-cells. They activate autonomic output to pancreas and adrenal, project to tuberomammillary histaminergic neurons for arousal, and facilitate feeding to prevent hypoglycemia.",
                ref(
                    "Contribution of the Autonomic Nervous System to Endocrine Control",
                    "populations of neurons in the hypothalamus, including ventromedial and perifrontal hypothalamic neurons, and catecholamine neurons in the rostral ventral lateral medulla of the brainstem, like the pancreatic β-cell, have the ability to sense glucose levels in the bloodstream.",
                ),
            ),
            note(
                f"{p}-n9",
                "Hypothalamic-pituitary anatomy",
                "Adenohypophysis versus neurohypophysis",
                "The adenohypophysis (anterior epithelial lobe) contains hormone-secreting cells of the pars distalis. The neurohypophysis comprises pars nervosa, infundibular stalk, and median eminence; T1 MRI shows a hyperintense posterior pituitary signal from the neural lobe.",
                ref(
                    "Anatomy of the Hypothalamic-Pituitary Unit",
                    "In humans, the pituitary gland (hypophysia) can be divided into two major parts, an anterior, epithelial lobe, or adenohypophysis, and a posterior neural lobe, or neurohypophysis",
                ),
            ),
            note(
                f"{p}-n10",
                "Median eminence",
                "How the median eminence portal system links hypothalamus to adenohypophysis",
                "Superior hypophyseal artery branches form fenestrated capillary loops in the median eminence that drain into pituitary portal veins. Blood flow is predominantly hypothalamic-to-pituitary, allowing releasing factors to diffuse to anterior pituitary targets.",
                ref(
                    "The Median Eminence and Hypophysiotropic Neuronal System",
                    "The flow of blood in these short loops is thought to be predominantly (if not exclusively) in a hypothalamic-to-pituitary direction.",
                ),
            ),
            note(
                f"{p}-n11",
                "Circumventricular organs",
                "Why circumventricular organs sense blood-borne signals",
                "Most brain vasculature excludes polar macromolecules via the blood-brain barrier. CVOs have fenestrated capillaries permitting peptide and hormone access, acting as windows on the circulation for homeostatic neurons that cannot otherwise sample blood composition.",
                ref(
                    "Circumventricular Organs",
                    "However, to exert homeostatic control, the brain must assess key sensory information from the bloodstream, including hormone levels, metabolites, and potential toxins.",
                ),
            ),
            note(
                f"{p}-n12",
                "OVLT",
                "How OVLT senses osmolality and drives fever",
                "The organum vasculosum of the lamina terminalis lies at the ventral third ventricle tip, surrounded by preoptic neurons. It expresses prostaglandin E₂ receptors and osmoreceptor TRPV channels; lesions attenuate LPS fever and osmotic AVP/oxytocin responses.",
                ref(
                    "Circumventricular Organs",
                    "Because prostaglandin E₂ is thought to be an obligate endogenous pyrogen, the OVLT may be a critical regulator of febrile responses.",
                ),
            ),
            note(
                f"{p}-n13",
                "SFO",
                "Subfornical organ and fluid homeostasis",
                "The SFO in the roof of the third ventricle is an osmosensory CVO with angiotensin II and atrial natriuretic peptide receptors. It projects to PVH, SON, and sympathetic centers to induce vasopressin release, vasoconstriction, and integrated fluid/blood pressure control.",
                ref(
                    "Circumventricular Organs",
                    "This CVO is an osmosensory site and critically regulates fluid homeostasis and contributes to blood pressure regulation.",
                ),
            ),
            note(
                f"{p}-n14",
                "Area postrema",
                "Area postrema as visceral and cardiovascular sensor",
                "The area postrema overlies the nucleus tractus solitarius, receives vagal and glossopharyngeal visceral afferents, and is enriched with receptors for GLP-1, angiotensin II, ghrelin, and amylin. Optogenetic GLP-1 neuron activation raises heart rate and blood pressure.",
                ref(
                    "Circumventricular Organs",
                    "The best-described physiologic role of the area postrema is the coordinated control of blood pressure.",
                ),
            ),
            note(
                f"{p}-n15",
                "Pineal melatonin",
                "Pineal gland and melatonin biosynthesis",
                "The pineal is both an endocrine gland and a CVO, synthesizing melatonin from tryptophan via serotonin. Rate-limiting AANAT converts serotonin to N-acetylserotonin; HIOMT methylates to melatonin. Melatonin is released promptly after synthesis with a very short half-life.",
                ref(
                    "The Pineal Is the Source of Melatonin",
                    "Pineal-derived melatonin is synthesized from tryptophan, which is first converted into 5-hydroxytrophan by tryptophan hydroxylase and then decarboxylated into serotonin (5-HT).",
                ),
            ),
            note(
                f"{p}-n16",
                "Light and melatonin",
                "How retinohypothalamic light suppresses melatonin",
                "Retinal ganglion cells innervate the SCN via the retinohypothalamic tract; SCN output reaches sympathetic preganglionic neurons and superior cervical ganglion noradrenergic terminals at the pineal. Light inhibits norepinephrine release, shutting down AANAT and melatonin synthesis.",
                ref(
                    "Pineal Gland",
                    "In the presence of light, whether morning light or a light impulse, norepinephrine release is inhibited, resulting in the shutdown of melatonin synthesis.",
                ),
            ),
            note(
                f"{p}-n17",
                "SCN circadian clock",
                "SCN as master circadian pacemaker",
                "Paired SCN nuclei above the optic chiasm orchestrate circadian rhythms via a cell-autonomous CLOCK/BMAL1–PER/CRY transcription-translation loop. Bilateral SCN lesions abolish sleep-wake, feeding, drinking, melatonin, and pituitary hormone rhythms; grafted SCN restores rhythmicity.",
                ref(
                    "Endocrine Rhythms",
                    "The best-understood neural structures responsible for circadian rhythms are the SCNs, paired structures in the anterior hypothalamus above the optic chiasm, which function as the central circadian clock, orchestrating multiple biological rhythms.",
                ),
            ),
            note(
                f"{p}-n18",
                "Hypophysiotropic hormones",
                "Principal hypophysiotropic releasing and inhibiting factors",
                "Peptide releasers TRH, CRH, GHRH, GnRH, and somatostatin plus monoamine dopamine (major prolactin-inhibiting factor) regulate anterior pituitary secretion. Dual stimulatory/inhibitory control (e.g., GHRH vs somatostatin for GH; CRH plus AVP synergism for ACTH) fine-tunes each axis.",
                ref(
                    "Hypophysiotropic Hormones and Neuroendocrine Axes",
                    "All of the principal hypothalamic-pituitary regulating hormones are peptides, with the notable exception of dopamine, which is a biogenic amine and the major prolactin-inhibiting factor (PIF)",
                ),
            ),
            note(
                f"{p}-n19",
                "Leptin and starvation",
                "Why leptin fall suppresses thyroid and reproductive axes in starvation",
                "Reduction in circulating leptin during starvation suppresses thyroid and reproductive neuroendocrine circuits, conserving energy. Leptin replacement can reverse fasting hypothyroidism in rodents by upregulating hypophysiotropic TRH in the PVH.",
                ref(
                    "Historical Perspective",
                    "Reduction in circulating leptin is responsible for suppression of the thyroid and reproductive axes during the starvation response.",
                ),
            ),
            note(
                f"{p}-n20",
                "Arcuate POMC/AgRP",
                "How arcuate POMC and AgRP neurons modulate hypothalamic axes",
                "Arcuate POMC (α-MSH/CART) and AgRP/NPY neurons respond to leptin, ghrelin, insulin, and glucose. They contact hypophysiotropic neurons and reset thyroid hormone feedback set-points during nutritional insufficiency, with evolutionary conservation in human infundibular nucleus.",
                ref(
                    "Feedback Control: Hypothalamic-Pituitary-Thyroid Axis",
                    "Neurons in the arcuate nucleus containing NPY, AgRP, α-MSH, and cocaine-regulated and amphetamine-regulated transcript (CART) have important roles in the regulation of energy homeostasis and respond to feeding-related signals in the bloodstream, including leptin, ghrelin, insulin, and glucose.",
                ),
            ),
            note(
                f"{p}-n21",
                "Pulsatile GnRH",
                "Why GnRH must be pulsatile for optimal LH stimulation",
                "LH pulsatility reflects pulsatile GnRH release. The ~90-minute interval between LH peaks corresponds to optimal GnRH pulse timing for maximal pituitary stimulation; continuous GnRH paradoxically desensitizes gonadotrophs.",
                ref(
                    "Endocrine Rhythms",
                    "The period of ~90 minutes between LH peaks corresponds to the optimal timing of GnRH pulses to induce maximal pituitary stimulation.",
                ),
            ),
            note(
                f"{p}-n22",
                "Stress and HPA",
                "How stress and CRH activate the HPA axis",
                "CRH from parvocellular PVH neurons is the primary ACTH secretagogue; AVP from magnocellular and parvocellular neurons synergizes. Nonhypophysiotropic CRH circuits in limbic and brainstem structures mediate behavioral stress responses. Emotional stress can activate pituitary-adrenal output and suppress gonadotropins.",
                ref(
                    "Neuroendocrine Disease",
                    "At the highest level of control, emotional stress and psychologic disorders can activate the pituitary-adrenal stress response and suppress gonadotropin secretion (e.g., psychogenic amenorrhea)",
                ),
            ),
            note(
                f"{p}-n23",
                "Thermoregulation",
                "Preoptic area thermoregulatory center",
                "The preoptic area integrates skin, spinal, and visceral thermoreceptor input. Warm-sensitive neurons outnumber cold-sensitive neurons; POA lesions typically cause hyperthermia. Downstream targets include DMH, rostral raphe pallidus, and spinal sympathetic preganglionic neurons controlling BAT, shivering, and vasomotor responses.",
                ref(
                    "Preoptic Area Is the Primary Hypothalamic Thermoregulatory Center",
                    "Because the number of warm-sensitive neurons is significantly greater than the number of cold-sensitive neurons in the POA, lesioning this region of the hypothalamus typically results in hyperthermia.",
                ),
            ),
            note(
                f"{p}-n24",
                "Orexin narcolepsy",
                "Why orexin/hypocretin loss causes narcolepsy",
                "Orexin-A (hypocretin-1) derives from lateral hypothalamic neurons that promote arousal. Canine narcolepsy maps to hypocretin receptor-2 mutations; human narcolepsy with cataplexy shows selective loss of orexin neurons. Absent CSF orexin is a sensitive diagnostic test.",
                ref(
                    "Hypothalamic Regulation",
                    "The absence of immunoreactive orexin-hypocretin in CSF is a sensitive diagnostic test for the disease.",
                ),
            ),
            note(
                f"{p}-n25",
                "Diencephalic syndrome",
                "Diencephalic syndrome of infancy",
                "Children with third-ventricle region tumors develop cachexia despite alert/euphoric appearance, often with elevated GH and paradoxical GH responses. Most cases are chiasmatic-hypothalamic gliomas (astrocytomas). Pituitary-adrenal deficits are less common than in classic hypothalamic failure.",
                ref(
                    "Diencephalic Syndrome",
                    "Children and infants with tumors in and around the third ventricle frequently become cachectic, which is often associated with elevated hGH levels and paradoxical GH secretory responses to glucose and insulin.",
                ),
            ),
            note(
                f"{p}-n26",
                "ROHHAD",
                "ROHHAD and hypothalamic tumor syndromes",
                "ROHHAD (rapid-onset obesity with hypothalamic dysfunction, hypoventilation, and autonomic dysregulation) presents in children with central alveolar hypoventilation, sleep apnea, temperature dysregulation, GH deficiency, central hypothyroidism, and SIADH. Craniopharyngioma remains a leading hypothalamic tumor cause of combined endocrine and neurologic disease in childhood.",
                ref(
                    "Other Hypothalamic Syndromes Associated With Sleep Disorders",
                    "Rapid-onset obesity with hypothalamic dysfunction, hypoventilation, and autonomic dysregulation (ROHHAD) is a rare syndrome observed in children associated with central alveolar hypoventilation and obstructive sleep apnea.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Portal system",
                "A researcher severs the pituitary stalk in an animal model but preserves the median eminence vasculature. Electrical stimulation of the medial basal hypothalamus no longer raises ACTH. What is the best explanation?",
                [
                    "Magnocellular AVP release is abolished",
                    "Hypophysiotropic peptides cannot reach adenohypophysis portal circulation",
                    "Posterior pituitary is the sole source of CRH",
                    "Adrenal gland denervation blocks the HPA axis",
                ],
                1,
                "Harris showed hypothalamic stimulation fails after stalk section because releasing factors must reach the anterior pituitary via hypothalamo-hypophyseal portal vessels from the median eminence.",
                ref(
                    "Historical Perspective",
                    "electric stimulation of the hypothalamus is ineffective in eliciting a pituitary response if the pituitary stalk is severed",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Neurosecretion history",
                "Cutting the pituitary stalk causes secretory granule accumulation in hypothalamic SON/PVH neurons. This observation best supports which hypothesis?",
                [
                    "Pituitary hormones are synthesized in the adenohypophysis alone",
                    "Hypothalamic neurons are the source of posterior pituitary hormones",
                    "Portal vessels carry hormones from pituitary to hypothalamus",
                    "CVOs synthesize oxytocin de novo",
                ],
                1,
                "Scharrer's granule accumulation after stalk section established that hypothalamic magnocellular neurons supply the neural lobe—foundational neurosecretion evidence.",
                ref(
                    "Neurosecretion",
                    "Scharrer found that cutting the pituitary stalk led to an accumulation of these granules in the hypothalamus, which led to the hypothesis that hypothalamic neurons were the source of substances secreted by the neural lobe (posterior pituitary).",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Cephalic phase",
                "A patient with vagotomy still has normal fasting glucose but blunted insulin rise when merely seeing and smelling a meal before eating. Which mechanism is most impaired?",
                [
                    "Enteroendocrine GLP-1 secretion",
                    "Parasympathetic cephalic-phase modulation of β-cell insulin release",
                    "Hepatic insulin clearance",
                    "Pancreatic α-cell glucagon suppression",
                ],
                1,
                "Vagal cholinergic tone from the dorsal motor nucleus modulates insulin before food ingestion—the cephalic phase of insulin secretion.",
                ref(
                    "Contribution of the Autonomic Nervous System to Endocrine Control",
                    "vagal input is thought to modulate insulin secretion before (cephalic phase), during, and after ingestion of food.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Hypoglycemia sensing",
                "During insulin-induced hypoglycemia, which CNS region coordinates autonomic activation of adrenal medulla and pancreatic counterregulation while promoting arousal?",
                [
                    "Cerebellar cortex",
                    "Hypothalamic and brainstem glucose-sensing neurons including VMH and rostral ventrolateral medulla",
                    "Primary motor cortex",
                    "Hippocampal CA1 exclusively",
                ],
                1,
                "Hypothalamic and medullary glucose-sensing neurons initiate counterregulatory autonomic responses and projections to histaminergic TMN neurons for arousal and feeding.",
                ref(
                    "Contribution of the Autonomic Nervous System to Endocrine Control",
                    "This information is particularly important to initiate counterregulatory responses to prevent hypoglycemia by altering the activity of the autonomic nervous system innervating the pancreas and adrenal glands while simultaneously facilitating arousal",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Pituitary anatomy",
                "On sagittal T1 MRI, the bright posterior pituitary signal corresponds to which structure?",
                [
                    "Pars distalis of adenohypophysis",
                    "Pars tuberalis",
                    "Neurohypophysis (pars nervosa)",
                    "Rathke cleft cyst",
                ],
                2,
                "The neurohypophysis (posterior/neural lobe) appears hyperintense on T1-weighted MRI; the adenohypophysis is the anterior epithelial lobe.",
                ref(
                    "Anatomy of the Hypothalamic-Pituitary Unit",
                    "easily distinguishable from each other by T1-weighted magnetic resonance imaging (MRI) by the hyperintense signal denoting the neurohypophysis",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Median eminence",
                "A peptide-releasing factor is injected into median eminence portal blood. Which anatomic feature most enables its access to anterior pituitary gonadotrophs?",
                [
                    "Tight junctions of median eminence capillaries",
                    "Fenestrated portal capillaries with large vascular surface area",
                    "Direct axonal synapses on every pituitary cell",
                    "Absence of any blood supply to pars distalis",
                ],
                1,
                "Median eminence capillaries are fenestrated with tremendous vascular surface area, allowing releasing factors to diffuse into portal veins supplying the adenohypophysis.",
                ref(
                    "The Median Eminence and Hypophysiotropic Neuronal System",
                    "the vessels are fenestrated, allowing diffusion of the peptide-releasing factors to their site of action in the anterior pituitary gland.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "CVO physiology",
                "Leptin acts on arcuate POMC and AgRP neurons after crossing into the mediobasal hypothalamus. Through which anatomic portal does circulating leptin most likely gain access?",
                [
                    "Blood-brain barrier of cerebral cortex",
                    "Median eminence and circumventricular organ fenestrated vasculature",
                    "Olfactory bulb exclusively",
                    "Internal carotid baroreceptors",
                ],
                1,
                "The median eminence is a portal for hormones like leptin and ghrelin to reach arcuate regulatory neurons; CVOs have fenestrated capillaries unlike the rest of the brain.",
                ref(
                    "Circumventricular Organs",
                    "it is a portal of entry for hormones circulating in the bloodstream, such as leptin and several gut-derived circulating hormones, including ghrelin.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "SFO function",
                "A patient with hypernatremia and elevated angiotensin II has increased Fos expression in a midline CVO below the fornix projecting to PVH and SON. Which structure is most likely activated?",
                [
                    "Area postrema",
                    "Subfornical organ",
                    "Pineal gland",
                    "Subcommissural organ",
                ],
                1,
                "The SFO is an osmosensory CVO below the fornix with angiotensin II receptors; it drives vasopressin release and sympathetic outflow for fluid and blood pressure homeostasis.",
                ref(
                    "Circumventricular Organs",
                    "The SFO is located in the roof of the third ventricle below the fornix.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Melatonin rhythm",
                "A night-shift worker sleeps in a brightly lit room during the day. Which hormonal change is expected?",
                [
                    "Elevated daytime melatonin",
                    "Suppressed melatonin synthesis due to inhibited pineal norepinephrine release",
                    "Increased AANAT only at midnight regardless of light",
                    "Loss of all SCN rhythmicity permanently",
                ],
                1,
                "Light inhibits sympathetic norepinephrine release at the pineal, shutting down AANAT and melatonin synthesis regardless of circadian phase.",
                ref(
                    "Pineal Gland",
                    "In the presence of light, whether morning light or a light impulse, norepinephrine release is inhibited, resulting in the shutdown of melatonin synthesis.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "SCN lesions",
                "Bilateral destruction of which nucleus abolishes circadian sleep-wake, feeding, and melatonin rhythms in experimental animals?",
                [
                    "Arcuate nucleus",
                    "Suprachiasmatic nucleus",
                    "Dorsal motor nucleus of vagus",
                    "Locus coeruleus",
                ],
                1,
                "The SCN above the optic chiasm is the central circadian pacemaker; bilateral lesions produce free-running disruption of multiple rhythms restorable by SCN graft.",
                ref(
                    "Endocrine Rhythms",
                    "If lesioned bilaterally, free-running circadian rhythmicity is produced, characterized by disruption of the sleep-wake cycle and loss of predictable daily oscillations in feeding, drinking, melatonin secretion",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Dopamine PIF",
                "Which hypothalamic substance is the principal physiologic inhibitor of prolactin secretion?",
                [
                    "Somatostatin",
                    "Dopamine",
                    "GnRH",
                    "TRH",
                ],
                1,
                "Dopamine is the major prolactin-inhibiting factor (PIF), the notable non-peptide among hypophysiotropic regulators.",
                ref(
                    "Hypophysiotropic Hormones and Neuroendocrine Axes",
                    "dopamine, which is a biogenic amine and the major prolactin-inhibiting factor (PIF)",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Starvation axes",
                "A woman with anorexia nervosa has low T₃, inappropriately low TSH, and amenorrhea. Which mediator best explains coordinated suppression of thyroid and reproductive axes?",
                [
                    "Elevated leptin",
                    "Reduced leptin signaling to hypothalamic circuits including arcuate POMC/AgRP",
                    "Excess GHRH",
                    "Primary adrenal hyperplasia",
                ],
                1,
                "Starvation lowers leptin, suppressing thyroid and reproductive axes; arcuate NPY/AgRP and POMC neurons reset hypophysiotropic TRH and GnRH drive.",
                ref(
                    "Historical Perspective",
                    "Reduction in circulating leptin is responsible for suppression of the thyroid and reproductive axes during the starvation response.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "GnRH pulsatility",
                "An infertility specialist administers GnRH continuously rather than pulsatilely to a woman with hypothalamic amenorrhea. What pituitary response is expected?",
                [
                    "Progressive LH/FSH stimulation",
                    "Desensitization and suppressed gonadotropin secretion",
                    "Isolated prolactin hypersecretion",
                    "AVP-dependent SIADH",
                ],
                1,
                "Pulsatile GnRH (~90-minute intervals) optimally stimulates LH; continuous GnRH downregulates pituitary responsiveness—the basis of GnRH agonist therapy.",
                ref(
                    "Endocrine Rhythms",
                    "The period of ~90 minutes between LH peaks corresponds to the optimal timing of GnRH pulses to induce maximal pituitary stimulation.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Feedback loops",
                "Glucocorticoids inhibit CRH/TRH neurons while emotional stress activates the HPA axis. This illustrates which feedback concept?",
                [
                    "Closed-loop endocrine feedback without neural input",
                    "Open-loop nervous system override of closed-loop hormonal feedback",
                    "Positive feedback only",
                    "Absence of any set-point",
                ],
                1,
                "All pituitary feedback systems receive neural inputs that alter set-points or introduce open-loop elements overriding closed-loop glandular control.",
                ref(
                    "Feedback Concepts in Neuroendocrinology",
                    "All pituitary feedback systems have nervous system inputs that either alter the set-point of the feedback control system or introduce open-loop elements that can influence or override the closed-loop control elements.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Thermoregulation",
                "Destruction of the preoptic thermoregulatory area in an experimental animal most commonly produces:",
                [
                    "Profound hypothermia only",
                    "Hyperthermia, because warm-sensitive neurons outnumber cold-sensitive neurons",
                    "Complete loss of sweating with preserved shivering",
                    "Isolated hyperglycemia",
                ],
                1,
                "Warm-sensitive neurons predominate in the POA; lesions typically cause hyperthermia rather than hypothermia.",
                ref(
                    "Preoptic Area Is the Primary Hypothalamic Thermoregulatory Center",
                    "Because the number of warm-sensitive neurons is significantly greater than the number of cold-sensitive neurons in the POA, lesioning this region of the hypothalamus typically results in hyperthermia.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Narcolepsy diagnosis",
                "A 22-year-old has cataplexy and excessive daytime sleepiness. Which test most specifically supports type 1 narcolepsy?",
                [
                    "Elevated CSF orexin/hypocretin",
                    "Absent or very low CSF orexin/hypocretin immunoreactivity",
                    "Elevated midnight cortisol",
                    "Blunted TRH-stimulated TSH",
                ],
                1,
                "Loss of orexin/hypocretin in CSF is a sensitive diagnostic marker for narcolepsy with cataplexy from selective lateral hypothalamic neuron destruction.",
                ref(
                    "Hypothalamic Regulation",
                    "The absence of immunoreactive orexin-hypocretin in CSF is a sensitive diagnostic test for the disease.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Pituitary stalk injury",
                "After traumatic pituitary stalk section, which pattern is characteristic?",
                [
                    "Isolated hyperthyroidism",
                    "Central DI, hyperprolactinemia, and gradual loss of other anterior pituitary hormones",
                    "Primary adrenal hyperplasia",
                    "Permanent SIADH without DI",
                ],
                1,
                "Pituitary isolation from stalk damage causes DI (depending on section level), loss of hypothalamic dopamine restraint (hyperprolactinemia), and progressive anterior pituitary hormone deficiency.",
                ref(
                    "Pituitary Isolation Syndrome",
                    "Destructive lesions of the pituitary stalk, as occur with head injury, surgical transection, tumor, granuloma, or infiltrative disease associated with histiocytosis and sarcoidosis, produce a characteristic pattern of pituitary dysfunction.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Craniopharyngioma",
                "A 7-year-old has bitemporal hemianopia, growth failure, and diabetes insipidus. MRI shows a suprasellar calcified cystic mass. Most likely diagnosis?",
                [
                    "Prolactinoma",
                    "Craniopharyngioma",
                    "Lymphocytic hypophysitis",
                    "Empty sella syndrome",
                ],
                1,
                "Craniopharyngioma is a leading hypothalamic-pituitary region tumor in children (2–10 years), causing visual field defects and combined hypothalamic/pituitary dysfunction.",
                ref(
                    "BOX 5.4 Etiology of Hypothalamic Disease by Age",
                    "Tumors: craniopharyngioma, glioma, germinoma, hamartoma, leukemia, histiocytosis X, ganglioneuroma, ependymoma, medulloblastoma",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Diencephalic syndrome",
                "An infant with a chiasmatic glioma is emaciated yet alert and euphoric, with elevated GH. This presentation defines:",
                [
                    "Prader-Willi syndrome",
                    "Diencephalic syndrome",
                    "ROHHAD",
                    "Kallmann syndrome",
                ],
                1,
                "Diencephalic syndrome features cachexia with paradoxical GH hypersecretion and preserved alertness, typically from chiasmatic-hypothalamic gliomas.",
                ref(
                    "Diencephalic Syndrome",
                    "A striking feature is an alert appearance and seeming euphoria despite the profound emaciation.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "ROHHAD",
                "A 6-year-old develops rapid obesity, alveolar hypoventilation, autonomic instability, and central hypothyroidism over months. Most likely diagnosis?",
                [
                    "Constitutional obesity",
                    "ROHHAD syndrome",
                    "Cushing disease",
                    "Congenital adrenal hyperplasia",
                ],
                1,
                "ROHHAD combines rapid-onset obesity, hypothalamic dysfunction, central hypoventilation, and autonomic dysregulation including temperature and endocrine abnormalities.",
                ref(
                    "Other Hypothalamic Syndromes Associated With Sleep Disorders",
                    "Rapid-onset obesity with hypothalamic dysfunction, hypoventilation, and autonomic dysregulation (ROHHAD) is a rare syndrome observed in children associated with central alveolar hypoventilation and obstructive sleep apnea.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Area postrema",
                "Chemotherapy-induced vomiting is mediated in part by which circumventricular structure that lacks a blood-brain barrier and receives vagal input?",
                [
                    "Subcommissural organ",
                    "Area postrema",
                    "Posterior commissure",
                    "Corpus callosum",
                ],
                1,
                "The area postrema overlies the NTS, receives visceral afferents, and contains chemosensitive neurons implicated in emesis and cardiovascular responses.",
                ref(
                    "Circumventricular Organs",
                    "The area postrema lies at the caudal end of the fourth ventricle adjacent to the nucleus of the tractus solitarius (NTS)",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Ghrelin and orexin",
                "During fasting, which signaling pattern promotes arousal and wakefulness via lateral hypothalamic neurons?",
                [
                    "Leptin activation and orexin inhibition",
                    "Ghrelin activation of orexin neurons that excite wake-promoting centers",
                    "Melatonin stimulation of VLPO",
                    "Somatostatin activation of TMN",
                ],
                1,
                "Orexin neurons are inhibited by glucose and leptin but activated by ghrelin, maintaining arousal during food deprivation by exciting wakefulness centers.",
                ref(
                    "Modifying Factors Influencing Sleep",
                    "They are inhibited by glucose and leptin and activated by ghrelin, humeral signals that promote increased food intake and reduced energy expenditure",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Hypothalamic injury pattern",
                "Compared with primary pituitary destruction, hypothalamic or stalk injury uniquely may cause:",
                [
                    "Only GH deficiency without other deficits",
                    "Hyperprolactinemia from loss of dopamine inhibitory tone",
                    "Primary hyperaldosteronism",
                    "Thyroid hormone receptor mutation",
                ],
                1,
                "Hypothalamic injury decreases most pituitary hormones but can increase prolactin when stalk damage interrupts hypothalamic dopamine delivery to lactotrophs.",
                ref(
                    "Neuroendocrine Disease",
                    "Hypothalamic injury causes decreased secretion of most pituitary hormones but can cause hypersecretion of hormones normally under inhibitory control by the hypothalamus, as in hypersecretion of PRL after damage to the pituitary stalk",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Circadian hormone sampling",
                "Loss of nocturnal ACTH and GH surges may be an early sign of:",
                [
                    "Primary adrenal insufficiency only",
                    "Hypothalamic dysfunction before complete pituitary reserve loss",
                    "Hyperparathyroidism",
                    "Diabetes insipidus from V2 receptor mutation",
                ],
                1,
                "Disruption of diurnal GH and ACTH rhythms can precede overt pituitary secretory failure and signals impaired hypothalamic circadian control.",
                ref(
                    "Endocrine Rhythms",
                    "the loss of diurnal rhythm of GH and ACTH secretion may be an early sign of hypothalamic dysfunction.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "CRH and AVP synergy",
                "During acute stress, which combination most potently drives ACTH release?",
                [
                    "Dopamine plus somatostatin",
                    "CRH plus AVP acting synergistically on corticotrophs",
                    "GnRH plus TRH",
                    "Melatonin plus GHRH",
                ],
                1,
                "CRH is the primary ACTH secretagogue; AVP from magnocellular and parvocellular sources synergizes with CRH to amplify ACTH release during stress.",
                ref(
                    "Hypophysiotropic Hormones and Neuroendocrine Axes",
                    "Some hypothalamic hormones act synergistically; for example, CRH and AVP cooperatively regulate the release of pituitary ACTH.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Sleep-wake centers",
                "Bilateral lesion of which hypothalamic nucleus causes profound loss of NREM sleep?",
                [
                    "Ventrolateral preoptic nucleus (VLPO)",
                    "Suprachiasmatic nucleus only",
                    "Mammillary bodies",
                    "Zona incerta exclusively",
                ],
                0,
                "VLPO and MnPO GABA/galanin neurons promote NREM sleep by inhibiting wake centers; VLPO lesion profoundly reduces NREM sleep.",
                ref(
                    "Central Circuitries Mediating the Sleep-Wake Cycle",
                    "if the VLPO is lesioned, there is a profound reduction in NREM sleep.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Neurosecretion",
                "All neurosecretory hypothalamic neurons release their products only at classical chemical synapses.",
                False,
                "Neurohumoral cells include magnocellular and hypophysiotropic neurons whose terminals release into blood or portal vessels, not exclusively at synapses.",
                ref(
                    "Neurosecretion",
                    "Neurohumoral or neurosecretory cells constitute a unique subset of neurons whose axon terminals are not associated with classic synapses.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Portal flow",
                "Hypothalamo-hypophyseal portal blood flow is directed from the median eminence toward the pituitary gland.",
                True,
                "Portal vessel blood flow runs from hypothalamic median eminence to the anterior pituitary—foundational to Harris's neuroendocrine model.",
                ref(
                    "Historical Perspective",
                    "the blood flow in portal vessels is directed to the pituitary gland from the hypothalamic median eminence",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Autonomic pancreas",
                "Sympathetic noradrenergic input to the endocrine pancreas can inhibit insulin release.",
                True,
                "Dual autonomic innervation modulates insulin and glucagon; noradrenergic stimulation inhibits insulin secretion.",
                ref(
                    "Contribution of the Autonomic Nervous System to Endocrine Control",
                    "noradrenergic stimulation of the endocrine pancreas can alter the secretion of glucagon and inhibit insulin release.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Blood-brain barrier",
                "Circumventricular organs have fenestrated capillaries allowing passage of peptides and proteins from blood.",
                True,
                "Unlike most brain vasculature, CVO capillaries are fenestrated, permitting macromolecule access to specialized sensory neurons.",
                ref(
                    "Circumventricular Organs",
                    "Unlike the vasculature in the rest of the brain, the blood vessels in CVOs have fenestrated capillaries that allow relatively free passage of molecules such as proteins and peptide hormones.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Melatonin storage",
                "The pineal gland stores large quantities of melatonin for release over hours.",
                False,
                "Melatonin is not stored significantly; it is released proportionally to AANAT activity and has a very rapid half-life.",
                ref(
                    "The Pineal Is the Source of Melatonin",
                    "Melatonin is not stored to any significant degree; it is released into the blood or CSF directly after its biosynthesis in proportion to AANAT activity but has a very rapid half-life (minutes)",
                ),
            ),
            tf(
                f"{p}-tf6",
                "SCN function",
                "Bilateral SCN lesions abolish circadian sleep-wake and feeding rhythms.",
                True,
                "Bilateral SCN destruction produces free-running loss of circadian rhythms in sleep, feeding, drinking, melatonin, and some pituitary hormones.",
                ref(
                    "Endocrine Rhythms",
                    "If lesioned bilaterally, free-running circadian rhythmicity is produced, characterized by disruption of the sleep-wake cycle and loss of predictable daily oscillations in feeding, drinking, melatonin secretion",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Dopamine PRL",
                "Dopamine is the major prolactin-inhibiting factor from the hypothalamus.",
                True,
                "Among hypophysiotropic regulators, dopamine is the principal PIF inhibiting prolactin secretion.",
                ref(
                    "Hypophysiotropic Hormones and Neuroendocrine Axes",
                    "dopamine, which is a biogenic amine and the major prolactin-inhibiting factor (PIF)",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Starvation leptin",
                "Reduced leptin during starvation contributes to suppression of thyroid and reproductive axes.",
                True,
                "Leptin signals nutritional state; its fall during starvation suppresses multiple neuroendocrine circuits including thyroid and reproduction.",
                ref(
                    "Historical Perspective",
                    "Reduction in circulating leptin is responsible for suppression of the thyroid and reproductive axes during the starvation response.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Continuous GnRH",
                "Continuous GnRH infusion is the optimal mode to stimulate gonadotropin secretion long term.",
                False,
                "Pulsatile GnRH (~90-minute intervals) maximally stimulates LH; continuous exposure desensitizes gonadotrophs.",
                ref(
                    "Endocrine Rhythms",
                    "The period of ~90 minutes between LH peaks corresponds to the optimal timing of GnRH pulses to induce maximal pituitary stimulation.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Narcolepsy orexin",
                "Low or absent CSF orexin/hypocretin is a sensitive diagnostic marker for narcolepsy with cataplexy.",
                True,
                "Selective loss of orexin neurons in narcolepsy produces absent CSF orexin immunoreactivity—a sensitive diagnostic test.",
                ref(
                    "Hypothalamic Regulation",
                    "The absence of immunoreactive orexin-hypocretin in CSF is a sensitive diagnostic test for the disease.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Stalk section prolactin",
                "Pituitary stalk section can cause hyperprolactinemia.",
                True,
                "Stalk damage interrupts hypothalamic dopamine delivery to lactotrophs, removing prolactin inhibitory tone.",
                ref(
                    "Neuroendocrine Disease",
                    "hypersecretion of PRL after damage to the pituitary stalk",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Diencephalic syndrome",
                "Diencephalic syndrome typically presents with obesity and somnolence.",
                False,
                "Diencephalic syndrome features cachexia with alert/euphoric appearance and often elevated GH—not obesity.",
                ref(
                    "Diencephalic Syndrome",
                    "Children and infants with tumors in and around the third ventricle frequently become cachectic",
                ),
            ),
            tf(
                f"{p}-tf13",
                "ROHHAD",
                "ROHHAD includes central hypoventilation and hypothalamic endocrine dysfunction.",
                True,
                "ROHHAD presents with rapid obesity, hypothalamic dysfunction, alveolar hypoventilation, autonomic dysregulation, and endocrine abnormalities.",
                ref(
                    "Other Hypothalamic Syndromes Associated With Sleep Disorders",
                    "Hypothalamic dysfunction can also include disruption of body temperature, GH deficiency, central hypothyroidism, and SIADH.",
                ),
            ),
        ]
    )

    # --- Assertion/Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Portal system",
                "Assertion: Severing the pituitary stalk prevents hypothalamic electrical stimulation from raising pituitary hormone secretion.",
                "Reason: Hypophysiotropic hormones reach the adenohypophysis primarily via portal vessels from the median eminence.",
                0,
                "Both are true and causally linked—Harris's stalk-section experiments established portal delivery of hypothalamic releasing factors.",
                ref(
                    "Historical Perspective",
                    "electric stimulation of the hypothalamus is ineffective in eliciting a pituitary response if the pituitary stalk is severed",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Neurosecretion",
                "Assertion: Magnocellular SON/PVH neurons release AVP and oxytocin into the systemic circulation.",
                "Reason: Magnocellular axons terminate exclusively at synapses on other hypothalamic neurons without neurohormonal release.",
                2,
                "Assertion is true; magnocellular terminals release into the neural lobe capillary plexus—the reason falsely denies neurohormonal secretion.",
                ref(
                    "Neurosecretion",
                    "It is now well established that the axon terminals in the neural lobe arise from the SON and PVH magnocellular neurons that contain oxytocin and the antidiuretic hormone arginine vasopressin (AVP).",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Cephalic phase",
                "Assertion: Vagal parasympathetic input can increase insulin secretion before food ingestion.",
                "Reason: The cephalic phase of insulin secretion is mediated by cholinergic vagal tone on pancreatic β-cells.",
                0,
                "Both are true; dorsal motor nucleus vagal cholinergic activity modulates insulin before and during meals.",
                ref(
                    "Contribution of the Autonomic Nervous System to Endocrine Control",
                    "vagal input is thought to modulate insulin secretion before (cephalic phase), during, and after ingestion of food.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "CVOs",
                "Assertion: Circumventricular organs allow the brain to monitor circulating hormones and metabolites.",
                "Reason: CVO capillaries have tight junctions that exclude all blood-borne substances.",
                2,
                "Assertion is true; CVO fenestrated capillaries permit macromolecule access—the reason describing tight exclusion is false.",
                ref(
                    "Circumventricular Organs",
                    "the blood vessels in CVOs have fenestrated capillaries that allow relatively free passage of molecules such as proteins and peptide hormones.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Melatonin and light",
                "Assertion: Bright light suppresses nocturnal melatonin secretion.",
                "Reason: Light inhibits norepinephrine release at the pineal, reducing AANAT activity and melatonin synthesis.",
                0,
                "Both are true and mechanistically linked through the retinohypothalamic–sympathetic pineal pathway.",
                ref(
                    "Pineal Gland",
                    "In the presence of light, whether morning light or a light impulse, norepinephrine release is inhibited, resulting in the shutdown of melatonin synthesis.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Leptin starvation",
                "Assertion: Starvation suppresses the thyroid axis partly through reduced leptin signaling.",
                "Reason: Leptin deficiency during fasting upregulates hypophysiotropic TRH in the PVH in all species including humans.",
                1,
                "Both relate to leptin and starvation, but direct leptin effects on TRH show species differences—rodents differ from leptin-deficient euthyroid children.",
                ref(
                    "Starvation",
                    "the direct effects of leptin may be species dependent.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "GnRH pulsatility",
                "Assertion: LH secretion reflects pulsatile GnRH release from the hypothalamus.",
                "Reason: Continuous GnRH infusion maximally stimulates gonadotropin secretion long term.",
                2,
                "Assertion is true; pulsatile GnRH drives LH pulses—continuous GnRH desensitizes gonadotrophs, so the reason is false.",
                ref(
                    "Endocrine Rhythms",
                    "In the case of LH, the normal endogenous rhythm of pituitary secretion reflects the pulsatile release of GnRH.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Stress HPA",
                "Assertion: Emotional stress can activate the pituitary-adrenal axis.",
                "Reason: Stress exclusively inhibits CRH secretion from the hypothalamus.",
                2,
                "Assertion is true; stress activates HPA output—CRH is stimulated, not exclusively inhibited, so the reason is false.",
                ref(
                    "Neuroendocrine Disease",
                    "emotional stress and psychologic disorders can activate the pituitary-adrenal stress response",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Thermoregulation",
                "Assertion: Preoptic area lesions often cause hyperthermia.",
                "Reason: Warm-sensitive neurons outnumber cold-sensitive neurons in the preoptic area.",
                0,
                "Both are true; loss of warm-sensitive predominance disrupts heat-dissipation balance toward hyperthermia.",
                ref(
                    "Preoptic Area Is the Primary Hypothalamic Thermoregulatory Center",
                    "Because the number of warm-sensitive neurons is significantly greater than the number of cold-sensitive neurons in the POA, lesioning this region of the hypothalamus typically results in hyperthermia.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Narcolepsy",
                "Assertion: Narcolepsy with cataplexy is associated with loss of orexin/hypocretin neurons.",
                "Reason: CSF orexin levels are typically elevated in narcolepsy.",
                2,
                "Assertion is true from human and animal models—CSF orexin is absent/low, not elevated, so the reason is false.",
                ref(
                    "Hypothalamic Regulation",
                    "The absence of immunoreactive orexin-hypocretin in CSF is a sensitive diagnostic test for the disease.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Stalk injury",
                "Assertion: Pituitary stalk damage can cause hyperprolactinemia.",
                "Reason: Stalk section increases dopamine delivery to lactotrophs.",
                2,
                "Assertion is true—stalk damage interrupts inhibitory dopamine—but the reason falsely claims increased dopamine delivery.",
                ref(
                    "Neuroendocrine Disease",
                    "hypersecretion of PRL after damage to the pituitary stalk",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Diencephalic syndrome",
                "Assertion: Diencephalic syndrome can present with cachexia despite an alert appearance.",
                "Reason: Diencephalic syndrome is always caused by craniopharyngioma in adults.",
                2,
                "Assertion is true for third-ventricle region tumors—most pediatric cases are chiasmatic-hypothalamic gliomas, not exclusively adult craniopharyngioma, so the reason is false.",
                ref(
                    "Diencephalic Syndrome",
                    "Most cases are caused by chiasmatic-hypothalamic gliomas, with the majority classified as astrocytomas.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "5",
        "title": "Neuroendocrinology",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Ronald M. Lechan",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_05_Neuroendocrinology.md",
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
