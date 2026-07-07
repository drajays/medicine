#!/usr/bin/env python3
"""Generate Williams 15e module w15-06 — Pituitary Physiology and Diagnostic Evaluation."""
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
OUT_NAME = "w15-06_Pituitary_Physiology_and_Diagnostic_Evaluation.json"


def build() -> dict:
    p = "w15-06"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Pituitary anatomy",
                "Five anterior pituitary cell types",
                "The mature anterior pituitary contains corticotrophs (POMC/ACTH), somatotrophs (GH), thyrotrophs (common α plus TSH β), gonadotrophs (α plus FSH/LH β), and lactotrophs (PRL), each under highly specific hypothalamic and peripheral controls.",
                ref(
                    "Anatomy",
                    "Five distinct hormone-secreting cell types are present in the mature anterior pituitary gland:",
                ),
            ),
            note(
                f"{p}-n2",
                "Portal circulation",
                "Why hypophyseal portal blood is essential for pituitary control",
                "Superior hypophyseal arteries form a median-eminence capillary plexus outside the blood-brain barrier; long and short portal vessels deliver hypothalamic releasing and inhibiting hormones to adenohypophysis without systemic dilution, enabling timed, sensitive regulation.",
                ref(
                    "Pituitary Blood Supply",
                    "They deliver hypothalamic-releasing and hypothalamic-inhibiting hormones to the hormone-producing cells of the adenohypophysis, without significant systemic dilution, allowing the pituitary cells to be sensitively regulated by timed hypothalamic hormone secretion.",
                ),
            ),
            note(
                f"{p}-n3",
                "Pituitary development",
                "Rathke pouch and anterior pituitary origin",
                "Rathke's pouch—a rostral ectodermal invagination anterior to the oral cavity roof—proliferates toward the third ventricle, fuses with the infundibulum, and gives rise to the anterior pituitary; the neurohypophysis derives from neural ectoderm.",
                ref(
                    "Pituitary Development",
                    "Rathke's pouch, a primitive ectodermal invagination anterior to the roof of the oral cavity, gives rise to the anterior pituitary gland (Fig. 6.2).",
                ),
            ),
            note(
                f"{p}-n4",
                "Transcription factors",
                "How PROP1, POU1F1, HESX1, and TBX19 commit pituitary lineages",
                "Early Hesx1 and Pitx expression precede a cascade in which Prop1 is prerequisite for Pit1-dependent somatotroph, lactotroph, and thyrotroph development, whereas corticotroph commitment is directed by Tbx19 (Tpit) for POMC expression.",
                ref(
                    "Pituitary Transcription Factors",
                    "Prop1, expressed early in the development of Rathke's pouch, is a pre-requisite for Pit1, a POU homeodomain transcription factor that activates and regulates somatotroph, lactotroph, and thyrotroph development",
                ),
            ),
            note(
                f"{p}-n5",
                "HESX1",
                "HESX1 and septo-optic dysplasia",
                "HESX1 is among the earliest transcriptional markers of Rathke's pouch; mutations cause septo-optic dysplasia with hypoplastic optic nerves, absent septum pellucidum, and variable panhypopituitarism or isolated GH deficiency.",
                ref(
                    "HESX1, SOX2, SOX3, and OTX2",
                    "The heterogeneous syndrome of septo-optic dysplasia (hypoplastic optic nerves, absent corpus callosum and septum pellucidum, and hypopituitarism) is associated with mutations in HESX1.",
                ),
            ),
            note(
                f"{p}-n6",
                "POU1F1",
                "POU1F1 (PIT1) and combined GH, PRL, TSH deficiency",
                "PIT1 activates GH, PRL, TSHβ, and GHRH receptor transcription; inactivating POU1F1 mutations cause combined deficiencies of somatotroph, lactotroph, and thyrotroph lineages.",
                ref(
                    "POU1F1",
                    "Because of the absolute requirement of PIT1 for somatotroph, lactotroph, and thyrotroph development and specific gene expression, inactivating mutations of the gene result in a spectrum of pituitary hormone deficiencies.",
                ),
            ),
            note(
                f"{p}-n7",
                "Pituitary control",
                "Why three tiers govern anterior pituitary secretion",
                "Hypothalamic hormones via portal vessels, peripheral hormone negative feedback, and intrapituitary paracrine/autocrine factors integrate to produce controlled pulsatile secretion of ACTH, GH, PRL, TSH, FSH, and LH.",
                ref(
                    "Pituitary Control",
                    "Three levels of control subserve the regulation of anterior pituitary hormone secretion (Fig. 6.3).",
                ),
            ),
            note(
                f"{p}-n8",
                "Prolactin regulation",
                "PRL under tonic dopamine inhibition",
                "PRL is produced primarily by lactotrophs and is tonically inhibited by hypothalamic dopamine from tuberoinfundibular neurons; dopamine reaches lactotrophs via portal vessels and binds D₂ receptors to inhibit secretion.",
                ref(
                    "Prolactin",
                    "PRL is produced primarily by pituitary lactotrophs and is tonically inhibited by hypothalamic dopamine.",
                ),
            ),
            note(
                f"{p}-n9",
                "Macroprolactin",
                "How macroprolactin causes apparent hyperprolactinemia",
                "PRL circulates as monomeric (23 kDa, most bioactive), dimeric (48–56 kDa), and macroprolactin (>100 kDa, bound to immunoglobulins); macroprolactin is often biologically inactive but detected by immunoassays, producing spurious hyperprolactinemia.",
                ref(
                    "Prolactin Structure",
                    "macroprolactin (also known as \"big, big prolactin,\" composed of prolactin bound to immunoglobulins; >100 kDa).",
                ),
            ),
            note(
                f"{p}-n10",
                "Lactotroph hyperplasia",
                "Pregnancy lactotroph expansion",
                "Although lactotroph numbers are similar in men and women and do not change with age, lactotroph hyperplasia occurs during pregnancy and lactation and resolves within several months of delivery.",
                ref(
                    "Prolactin",
                    "lactotroph hyperplasia does occur during pregnancy and lactation and resolves within several months of delivery.",
                ),
            ),
            note(
                f"{p}-n11",
                "GH axis",
                "How GHRH and somatostatin generate pulsatile GH",
                "Hypothalamic GHRH stimulates and somatostatin (SRIF) suppresses GH pulse amplitude and frequency; the two are secreted in independent waves about 180 degrees out of phase, and IGF-1 provides peripheral negative feedback on both hypothalamus and somatotroph.",
                ref(
                    "Regulation",
                    "GHRH and SRIF Interaction. Hypothalamic SRIF and GHRH are secreted in independent waves, which interact to generate pulsatile GH release.",
                ),
            ),
            note(
                f"{p}-n12",
                "IGF-1 feedback",
                "How IGF-1 feedback suppresses GH secretion",
                "IGF-1 participates in a hypothalamic-pituitary peripheral regulatory feedback system, stimulating hypothalamic SRIF release and inhibiting GH gene transcription and secretion; age-stratified IGF-1 is a valuable marker of GH status.",
                ref(
                    "Regulation",
                    "GH secretion is further regulated by IGF-1, which participates in a hypothalamic-pituitary peripheral regulatory feedback system, stimulating hypothalamic SRIF release and inhibiting GH gene transcription and secretion.",
                ),
            ),
            note(
                f"{p}-n13",
                "GH provocative testing",
                "Why adult GHD requires stimulation testing",
                "Adult GHD is established by provocative tests (ITT, glucagon, arginine-GHRH, GHRPs, macimorelin) because random GH is episodic and IGF-1 may be normal; thresholds vary by test and obesity lowers cutoffs.",
                ref(
                    "Provocative Testing",
                    "The diagnosis of adult GHD is established by provocative testing of GH secretion (Table 6.5).",
                ),
            ),
            note(
                f"{p}-n14",
                "ACTH axis",
                "CRH and glucocorticoid regulation of ACTH",
                "Pituitary POMC expression is positively regulated by CRH (and potentiated by AVP and catecholamines) and negatively regulated by glucocorticoids; three tiers—hypothalamic, paracrine, and glucocorticoid feedback—limit chronic ACTH hypersecretion.",
                ref(
                    "Regulation",
                    "Pituitary POMC expression is primarily under the positive regulation of CRH and negative regulation of glucocorticoids.",
                ),
            ),
            note(
                f"{p}-n15",
                "Circadian cortisol",
                "Circadian ACTH-cortisol coupling",
                "ACTH is secreted with circadian and ultradian pulsatility; cortisol follows ACTH by 5–10 minutes, peaking before 7 AM and reaching nadir between 11 PM and 3 AM—a rhythm lost in Cushing disease.",
                ref(
                    "Circadian Periodicity",
                    "The secretion of cortisol is tightly linked to and follows that of ACTH by 5 to 10 minutes (Fig. 6.27).",
                ),
            ),
            note(
                f"{p}-n16",
                "ACTH evaluation",
                "How morning cortisol and ACTH guide adrenal testing",
                "Concurrent cortisol and ACTH measurement is required; morning cortisol <3 µg/dL suggests ACTH deficiency whereas >18 µg/dL usually indicates adequate reserve; values between require ITT, metyrapone, CRH, or cosyntropin stimulation.",
                ref(
                    "Evaluation",
                    "Morning serum cortisol levels lower than 3 µg/dL suggest ACTH deficiency, but basal morning cortisol levels higher than 18 µg/dL usually indicate normal ACTH reserve.",
                ),
            ),
            note(
                f"{p}-n17",
                "TSH axis",
                "TRH-TSH-thyroid hormone feedback",
                "TRH neurons in the paraventricular nucleus drive TSH release; thyroid hormones (chiefly T₄ converted to T₃ in tanycytes) exert negative feedback at hypothalamus and pituitary, setting the axis set-point.",
                ref(
                    "Regulation",
                    "The TRH neuron plays a central role in determining the set-point of the hypothalamic-pituitary thyroid axis by regulating pituitary TSH release.",
                ),
            ),
            note(
                f"{p}-n18",
                "Central hypothyroidism",
                "Why central hypothyroidism requires free T₄ not TSH",
                "Ultrasensitive TSH cannot diagnose central hypothyroidism; low T₄ with low, normal, or minimally elevated TSH is typical, and dose titration targets mid-normal free T₄ because damaged thyrotrophs cannot reflect appropriate feedback.",
                ref(
                    "TSH Assays",
                    "TSH measurement alone is not helpful in diagnosing central hypothyroidism, which is identified by concurrent measurement of thyroid hormone levels.",
                ),
            ),
            note(
                f"{p}-n19",
                "Gonadotropin axis",
                "Pulsatile GnRH and LH/FSH secretion",
                "Hypothalamic GnRH is released in pulses—not continuously—into portal blood; pulsatile GnRH restores gonadotropins in deficiency whereas continuous exposure suppresses LH and FSH, and pulse frequency/amplitude differentially regulate the two hormones.",
                ref(
                    "Gonadotropin-Releasing Hormone",
                    "The hallmark of hypothalamic GnRH secretion is the pulsatile rather than continuous release into the hypophyseal portal circulation, resulting in episodic stimulation of the gonadotroph.",
                ),
            ),
            note(
                f"{p}-n20",
                "Estrogen feedback",
                "How estrogen exerts dual gonadotropin feedback",
                "In women estrogens exert negative feedback on gonadotropin secretion at pituitary and hypothalamic (kisspeptin) levels; during the late follicular phase feedback shifts to positive, triggering the midcycle LH/FSH surge.",
                ref(
                    "Sex Steroids",
                    "In women, estrogens can exert dual-feedback effects on gonadotropin secretion, depending on the reproductive state.",
                ),
            ),
            note(
                f"{p}-n21",
                "PROP1 CPHD",
                "PROP1 as most common genetic CPHD cause",
                "Mutations in PROP1 are the most common genetic cause of combined pituitary hormone deficiency, producing deficiencies in GH, PRL, TSH, and often gonadotropins, with variable ACTH deficiency.",
                ref(
                    "PROP1",
                    "Mutations in PROP1 are the most common genetic cause of combined pituitary hormone deficiency (CPHD) (Fig. 6.39).",
                ),
            ),
            note(
                f"{p}-n22",
                "PROP1 ACTH",
                "Why PROP1 patients need ongoing ACTH surveillance",
                "ACTH deficiency in PROP1 mutations may have later onset, suggesting a role in maintenance of corticotroph function and emphasizing the need for continued clinical and biochemical assessment.",
                ref(
                    "PROP1",
                    "ACTH deficiency can occur, frequently with a later onset, suggesting a role in maintenance of corticotroph function and emphasizing the necessity for complete and continued clinical assessment of patients with PROP1 mutations.",
                ),
            ),
            note(
                f"{p}-n23",
                "Dynamic testing",
                "Why each pituitary axis needs axis-specific testing",
                "Baseline hormones suffice for some axes (e.g., PRL, TSH in hyperthyroidism) but ACTH, GH, and gonadotropin deficits often require stimulation (ITT, glucagon, CRH, cosyntropin, GnRH) or suppression protocols; Table 6.9 summarizes validated tests per axis.",
                ref(
                    "Screening for Pituitary Insufficiency",
                    "all patients harboring hypothalamic or pituitary masses should be screened for hypopituitarism (Table 6.9).",
                ),
            ),
            note(
                f"{p}-n24",
                "Insulin tolerance test",
                "How ITT evaluates hypothalamic-pituitary integrity",
                "The ITT is the gold standard for adult GHD (peak GH >5 µg/L) and also stimulates ACTH—normal cortisol >20 µg/dL implies intact hypothalamic, pituitary, and adrenal tiers; GHRH/GHRP tests may miss hypothalamic GHD after irradiation.",
                ref(
                    "Provocative Testing",
                    "The ITT evaluates the integrity of the hypothalamic-pituitary axis and has the added advantage of also stimulating ACTH secretion.",
                ),
            ),
            note(
                f"{p}-n25",
                "Incidental sellar lesions",
                "Approach to incidental pituitary and sellar findings",
                "Incidental empty sella, stalk lesions, or pituitary masses warrant screening for hypopituitarism; up to two-thirds of macroadenomas and parasellar lesions have compromised reserve, and empty sella with >90% gland atrophy usually causes failure.",
                ref(
                    "Empty Sella Syndrome",
                    "Although an empty sella is usually an incidental finding, if more than 90% of pituitary tissue is compressed or atrophied, pituitary failure usually occurs.",
                ),
            ),
            note(
                f"{p}-n26",
                "Stalk transection",
                "Why pituitary stalk disruption causes diabetes insipidus",
                "The posterior pituitary is directly innervated by supraopticohypophyseal and tuberohypophyseal tracts; hypothalamic lesions, stalk disruption, or stalk interruption deprive anterior pituitary cells of hypothalamic input and often attenuate vasopressin secretion, causing AVP deficiency (diabetes insipidus).",
                ref(
                    "Anatomy",
                    "Hypothalamic neuronal lesions, stalk disruption, or systemically derived metastases to the hypothalamus are therefore often associated with attenuated vasopressin (arginine vasopressin [AVP] deficiency, or diabetes insipidus)",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Portal circulation",
                "A neurosurgeon resects a craniopharyngioma transecting the pituitary stalk. Which mechanism best explains subsequent anterior pituitary hormone loss?",
                [
                    "Loss of direct neural innervation of somatotrophs",
                    "Disruption of hypophyseal portal delivery of hypothalamic hormones",
                    "Autoimmune destruction of Rathke cleft remnants",
                    "Excess systemic dilution of pituitary hormones in cavernous sinus blood",
                ],
                1,
                "Anterior pituitary cells depend on portal hypothalamic hormones; stalk transection compromises portal flow and hypothalamic input.",
                ref(
                    "Pituitary Blood Supply",
                    "Disruption of stalk integrity may lead to compromised pituitary portal blood flow, depriving the anterior pituitary cells of hypothalamic hormone input.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Transcription factors",
                "A child with short stature, low GH, PRL, and TSH but normal ACTH has MRI showing hypoplastic anterior pituitary. Which gene defect is most likely?",
                [
                    "TBX19",
                    "POU1F1",
                    "NR5A1",
                    "HESX1 only if anosmia absent",
                ],
                1,
                "PIT1/POU1F1 is required for somatotroph, lactotroph, and thyrotroph development; TBX19 causes isolated ACTH deficiency.",
                ref(
                    "POU1F1",
                    "inactivating mutations of the gene result in a spectrum of pituitary hormone deficiencies.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "PROP1",
                "A teenager with delayed puberty has low GH, PRL, TSH, LH, and FSH. Genetic testing shows PROP1 mutation. Which additional deficit may emerge later?",
                [
                    "Mineralocorticoid excess",
                    "ACTH deficiency",
                    "Hyperthyroidism",
                    "Primary adrenal hyperplasia",
                ],
                1,
                "PROP1 mutations frequently include gonadotropin deficiency and ACTH deficiency may appear with later onset.",
                ref(
                    "PROP1",
                    "ACTH deficiency can occur, frequently with a later onset, suggesting a role in maintenance of corticotroph function",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Prolactin",
                "A woman has galactorrhea with PRL 180 µg/L on standard assay but no symptoms of mass effect; polyethylene glycol precipitation shows marked reduction. Best explanation?",
                [
                    "Prolactinoma secreting monomeric PRL",
                    "Macroprolactin with reduced bioactivity",
                    "Primary hypothyroidism",
                    "Pregnancy-related lactotroph hyperplasia",
                ],
                1,
                "Macroprolactin (>100 kDa, Ig-bound) is detected by immunoassay but is often biologically inactive.",
                ref(
                    "Prolactin Structure",
                    "macroprolactin (also known as \"big, big prolactin,\" composed of prolactin bound to immunoglobulins; >100 kDa).",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Prolactin",
                "A third-trimester woman has physiologic pituitary enlargement on MRI without visual field loss. Which cellular change explains elevated PRL capacity?",
                [
                    "Somatotroph hyperplasia",
                    "Lactotroph hyperplasia resolving postpartum",
                    "Corticotroph apoptosis",
                    "Gonadotroph stem-cell expansion",
                ],
                1,
                "Lactotroph hyperplasia occurs during pregnancy and lactation and resolves within months after delivery.",
                ref(
                    "Prolactin",
                    "lactotroph hyperplasia does occur during pregnancy and lactation and resolves within several months of delivery.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "GH axis",
                "An obese adult post pituitary surgery has low IGF-1 and failed glucagon stimulation (peak GH 1.8 µg/L). Which statement about diagnosis is correct?",
                [
                    "A single random GH <5 µg/L confirms GHD",
                    "Provocative test thresholds differ by stimulus and BMI may lower cutoffs",
                    "Normal IGF-1 excludes adult GHD",
                    "GHRH alone is superior to ITT after cranial irradiation",
                ],
                1,
                "GH stimulation cutoffs vary by test; obesity lowers thresholds; ITT remains gold standard when hypothalamic disease is suspected.",
                ref(
                    "Provocative Testing",
                    "Because provocative tests vary in the ability to evoke GH release, a single value cannot be applied as a diagnostic threshold across different tests.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "GH axis",
                "A patient with panhypopituitarism has three hormone deficits and subnormal IGF-1. When is formal GH stimulation unnecessary per guidelines?",
                [
                    "Never—ITT is always mandatory",
                    "When ≥3 pituitary hormone deficiencies and low IGF-1 (>97% probability of GHD)",
                    "Only if IGF-1 is above the upper reference limit",
                    "Only in children under 10 years",
                ],
                1,
                "Patients with three or more pituitary hormone deficiencies and low IGF-1 have >97% probability of GHD and need not undergo stimulation.",
                ref(
                    "Growth Hormone-Responsive Markers",
                    "Patients with three or more pituitary hormone deficiencies and an IGF-1 level below the reference range have a greater than 97% chance of being GH deficient",
                ),
            ),
            mcq(
                f"{p}-q8",
                "ACTH axis",
                "A 48-year-old with fatigue has 8 AM cortisol 2.1 µg/dL and ACTH 8 ng/L. Next best step to confirm secondary adrenal insufficiency?",
                [
                    "Dexamethasone suppression test",
                    "Insulin tolerance or cosyntropin stimulation after appropriate precautions",
                    "24-hour urinary free cortisol only",
                    "Salivary cortisol at midnight alone",
                ],
                1,
                "Morning cortisol <3 µg/dL suggests ACTH deficiency; provocative testing (ITT, cosyntropin) confirms impaired reserve.",
                ref(
                    "Evaluation",
                    "Morning serum cortisol levels lower than 3 µg/dL suggest ACTH deficiency, but basal morning cortisol levels higher than 18 µg/dL usually indicate normal ACTH reserve.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Circadian cortisol",
                "A resident draws cortisol at 11 PM in an unstressed ward patient. The value is 3 µg/dL. Appropriate interpretation?",
                [
                    "Definite adrenal insufficiency",
                    "Consistent with normal nadir; timing is critical for basal cortisol",
                    "Indicates Cushing syndrome",
                    "Proves adequate ACTH reserve",
                ],
                1,
                "Cortisol at 11 PM is usually <5 µg/dL in normals; circadian rhythm must be considered when interpreting basal levels.",
                ref(
                    "Measurement of ACTH",
                    "Cortisol values at 4 PM are about half those of morning levels, and at 11 PM levels are usually less than 5 µg/dL.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "ACTH stimulation",
                "A patient with long-standing pituitary ACTH deficiency receives 250 µg IV cosyntropin. Cortisol rises from 2 to 8 µg/dL at 60 minutes. Interpretation?",
                [
                    "Normal adrenal reserve",
                    "Blunted response consistent with chronic ACTH deprivation and adrenal atrophy",
                    "Primary adrenal hyperfunction",
                    "Excludes secondary adrenal insufficiency",
                ],
                1,
                "Chronic pituitary ACTH hyposecretion causes adrenal atrophy; acute ACTH stimulation may be blunted until primed by ambient ACTH.",
                ref(
                    "Adrenal Stimulation",
                    "the cortisol response to an acute ACTH injection will be blunted if the subject has experienced chronic pituitary ACTH hyposecretion, with resultant adrenal atrophy and diminished cortisol reserve.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "TSH axis",
                "A woman with pituitary macroadenoma has fatigue, low free T₄, and TSH 2.8 mU/L (reference 0.4–4.0). Best management principle?",
                [
                    "No treatment—TSH is normal",
                    "Start levothyroxine titrated to mid-normal free T₄; do not use TSH to guide dose",
                    "Propylthiouracil for suppressed TSH",
                    "TRH stimulation required before any therapy",
                ],
                1,
                "Central hypothyroidism shows low T₄ with inappropriately normal/low TSH; replacement targets free T₄ not TSH.",
                ref(
                    "Treatment",
                    "TSH cannot be used to guide dose titration in patients with secondary hypothyroidism because the damaged thyrotroph is unlikely to adequately reflect appropriate feedback suppression.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "TSH axis",
                "A patient has elevated free T₄ and T₃ with detectable TSH. TRH stimulation increases TSH. Most likely diagnosis?",
                [
                    "TSH-secreting pituitary adenoma",
                    "Thyroid hormone resistance",
                    "Primary Graves disease",
                    "Sick euthyroid syndrome",
                ],
                1,
                "TSH adenomas usually do not respond to TRH; thyroid hormone resistance shows TSH rise with TRH despite high thyroid hormones.",
                ref(
                    "TSH Assays",
                    "The TSH levels do not increase in response to TRH in most cases of TSH adenomas, whereas they do so in thyroid hormone resistance.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Gonadotropins",
                "A 16-year-old boy has micropenis and low LH/FSH with low testosterone. Continuous (not pulsatile) GnRH infusion would be expected to:",
                [
                    "Stimulate pubertal LH surge",
                    "Suppress gonadotropin secretion",
                    "Increase FSH more than LH",
                    "Have no effect on pituitary gonadotrophs",
                ],
                1,
                "Continuous GnRH exposure suppresses LH/FSH, whereas pulsatile GnRH restores secretion in GnRH deficiency.",
                ref(
                    "Gonadotropin-Releasing Hormone",
                    "whereas continuous GnRH exposure suppresses gonadotropin secretion.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Gonadotropins",
                "A breastfeeding woman has amenorrhea and low LH pulse frequency. Primary mechanism?",
                [
                    "Estrogen positive feedback on kisspeptin",
                    "PRL-mediated inhibition of GnRH pulsatility",
                    "Primary ovarian failure",
                    "Excess inhibin A from corpus luteum",
                ],
                1,
                "Lactation causes amenorrhea via PRL-mediated inhibition of hypothalamic GnRH and reduced LH pulse amplitude and frequency.",
                ref(
                    "Reproductive Function",
                    "Amenorrhea and infertility result from PRL-mediated inhibitory effects on hypothalamic gonadotropin-releasing hormone (GnRH) secretion",
                ),
            ),
            mcq(
                f"{p}-q15",
                "TBX19",
                "A neonate presents with hypoglycemia and hyperpigmentation absent; ACTH undetectable, cortisol low. Which genetic defect is most likely?",
                [
                    "PROP1",
                    "TBX19",
                    "POU1F1",
                    "IGSF1",
                ],
                1,
                "TBX19 (Tpit) mutations cause isolated ACTH deficiency; hyperpigmentation is absent unlike primary adrenal failure.",
                ref(
                    "TBX19",
                    "TBX19 (also referred to as TPIT) mutations result in early-onset isolated ACTH deficiency and hypocortisolism",
                ),
            ),
            mcq(
                f"{p}-q16",
                "HESX1",
                "An infant has optic nerve hypoplasia, absent septum pellucidum, and panhypopituitarism. Which transcription factor is implicated?",
                [
                    "PROP1",
                    "HESX1",
                    "NR0B1",
                    "ZBTB20",
                ],
                1,
                "HESX1 mutations cause septo-optic dysplasia with variable panhypopituitarism.",
                ref(
                    "HESX1, SOX2, SOX3, and OTX2",
                    "septo-optic dysplasia (hypoplastic optic nerves, absent corpus callosum and septum pellucidum, and hypopituitarism) is associated with mutations in HESX1.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "ITT",
                "During supervised ITT a patient's glucose nadir is 38 mg/dL. Peak cortisol 22 µg/dL and GH 1.2 µg/L. Interpretation?",
                [
                    "Normal ACTH-adrenal axis; GH deficiency likely",
                    "Adrenal insufficiency; normal GH axis",
                    "Both ACTH and GH axes intact",
                    "Test invalid—must repeat without glucose rescue",
                ],
                0,
                "ITT cortisol >20 µg/dL indicates adequate HPA response; peak GH <5 µg/L suggests GHD in adults.",
                ref(
                    "Hypothalamic Testing",
                    "Normal HPA response to this stressor evokes cortisol levels higher than 20 μg/dL.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "PRL testing",
                "A resident orders TRH stimulation to evaluate mild hyperprolactinemia in a patient on no medications. Appropriate response?",
                [
                    "Proceed—TRH is first-line for PRL",
                    "Measure baseline PRL only; PRL stimulation/suppression tests are largely abandoned",
                    "Start dopamine agonist before testing",
                    "Order macroprolactin only if PRL >500 µg/L",
                ],
                1,
                "PRL is measured by immunoassay; stimulation and suppression tests are nonspecific and largely abandoned.",
                ref(
                    "Prolactin Measurements",
                    "Stimulation and suppression tests yield nonspecific results and have been largely abandoned.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Incidentaloma",
                "MRI for headache reveals a 9 mm nonfunctioning pituitary lesion without chiasmal compression. Next evaluation step?",
                [
                    "Immediate transsphenoidal surgery",
                    "Screen anterior pituitary axes and prolactin",
                    "Observation only—no labs needed for microlesions",
                    "Petrosal sinus sampling",
                ],
                1,
                "All patients with hypothalamic or pituitary masses should be screened for hypopituitarism including PRL.",
                ref(
                    "Screening for Pituitary Insufficiency",
                    "all patients harboring hypothalamic or pituitary masses should be screened for hypopituitarism (Table 6.9).",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Stalk interruption",
                "A child with pituitary stalk interruption syndrome has anterior hypopituitarism. Which posterior pituitary finding is typical?",
                [
                    "Bright T1 signal in normal sellar position",
                    "Ectopic posterior pituitary bright spot with thin/absent stalk",
                    "Enlarged neurohypophysis with DI absent",
                    "Calcified posterior lobe only",
                ],
                1,
                "PSIS features thin/interrupted stalk, anterior hypoplasia, and ectopic posterior pituitary on MRI.",
                ref(
                    "Pituitary Stalk Interruption Syndrome",
                    "PSIS is a congenital defect of the pituitary gland characterized by a thin or interrupted pituitary stalk, anterior pituitary hypoplasia, and an ectopic posterior pituitary.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "GH physiology",
                "A fasting healthy male shows augmented nocturnal GH secretion. Which hypothalamic interaction best explains this?",
                [
                    "Continuous GHRH infusion",
                    "Coordinated GHRH peaks and somatostatin troughs",
                    "Dopamine excess inhibiting SRIF",
                    "IGF-1 stimulating GH gene transcription",
                ],
                1,
                "Pulsatile GH reflects interacting independent GHRH and SRIF waves; fasting amplifies GH secretion.",
                ref(
                    "Regulation",
                    "Hypothalamic SRIF and GHRH are secreted in independent waves, which interact to generate pulsatile GH release.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Glucocorticoid replacement",
                "A patient with secondary adrenal insufficiency prefers once-daily dexamethasone over hydrocortisone. Clinician concern?",
                [
                    "Dexamethasone lacks glucocorticoid activity",
                    "Long half-life makes biochemical monitoring difficult compared with hydrocortisone",
                    "Dexamethasone causes mineralocorticoid excess requiring fludrocortisone",
                    "Hydrocortisone cannot be divided into multiple daily doses",
                ],
                1,
                "Dexamethasone has a longer half-life and is difficult to monitor biochemically compared with hydrocortisone.",
                ref(
                    "Adrenal Steroid Replacement",
                    "dexamethasone (0.25–0.5 mg/day), are suitable alternatives. Having longer half-lives, they can be administered once daily but are difficult to monitor biochemically.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Radiation",
                "A patient received pituitary radiotherapy 4 years ago and feels fatigued. Which axis deficit typically appears first?",
                [
                    "TSH deficiency",
                    "GH deficiency",
                    "ACTH deficiency",
                    "AVP deficiency only",
                ],
                1,
                "After pituitary irradiation GH is most radiosensitive, then gonadotropins, ACTH, and TSH.",
                ref(
                    "Radiation",
                    "The GH axis is the most radiosensitive, followed by the gonadotropin, ACTH, and TSH axes (Fig. 6.40).",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Compression order",
                "A large nonfunctioning macroadenoma compresses the gland. Expected order of hormone loss?",
                [
                    "ACTH first, then GH",
                    "GH, then FSH/LH, then TSH, then ACTH last",
                    "TSH first, then PRL",
                    "All axes fail simultaneously",
                ],
                1,
                "Compressing lesions typically impair GH first, then gonadotropins, TSH, and ACTH last.",
                ref(
                    "Clinical Features of Hypopituitarism",
                    "The order of diminished trophic hormone reserve function by pituitary compression is usually as follows: GH > FSH > LH > TSH > ACTH.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Central hypothyroidism treatment",
                "A panhypopituitary patient is started on levothyroxine before glucocorticoid replacement and develops hypotension. Explanation?",
                [
                    "Levothyroxine is contraindicated in central hypothyroidism",
                    "Thyroid hormone accelerates cortisol metabolism and may unmask adrenal insufficiency",
                    "TSH surge causes adrenal hemorrhage",
                    "Free T₄ directly blocks ACTH secretion",
                ],
                1,
                "Thyroid hormone replacement accelerates cortisol metabolism; adrenal status must be assessed and treated before thyroid replacement if ACTH deficiency is suspected.",
                ref(
                    "Treatment",
                    "Thyroid hormone replacement accelerates cortisol metabolism and requirements and may therefore exacerbate primary hypoadrenalism or precipitate adrenal crisis in patients with coexisting perturbed adrenal function.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Diabetes insipidus",
                "After traumatic pituitary stalk section a patient develops polyuria and hypernatremia with low urine osmolality. Anterior pituitary hormones are low. Expected posterior pituitary problem?",
                [
                    "SIADH from excess AVP",
                    "AVP deficiency (diabetes insipidus) from disrupted hypothalamo-neurohypophyseal tract",
                    "Oxytocin excess only",
                    "Isolated GH deficiency without water balance change",
                ],
                1,
                "Stalk disruption interrupts AVP transport to posterior pituitary, commonly causing diabetes insipidus alongside anterior deficits.",
                ref(
                    "Anatomy",
                    "stalk disruption, or systemically derived metastases to the hypothalamus are therefore often associated with attenuated vasopressin (arginine vasopressin [AVP] deficiency, or diabetes insipidus)",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Anatomy",
                "The anterior pituitary receives its predominant blood supply via the hypothalamic portal circulation rather than direct arterial branches.",
                True,
                "Long and short hypophyseal portal vessels form the predominant anterior pituitary blood supply delivering hypothalamic hormones.",
                ref(
                    "Pituitary Blood Supply",
                    "These vessels form the hypothalamic portal circulation, the predominant blood supply to the anterior pituitary gland.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Development",
                "Fully differentiated lactotrophs are present before 8 weeks of gestation alongside somatotrophs.",
                False,
                "Lactotrophs appear late in gestation after 24 weeks; earlier PRL is only in mammosomatotrophs coexpressing GH.",
                ref(
                    "Pituitary Development",
                    "Fully differentiated PRL-expressing lactotrophs are only evident late in gestation, after 24 weeks.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Prolactin",
                "Dopamine agonists at the lactotroph D₂ receptor inhibit prolactin secretion.",
                True,
                "Dopamine from TIDA neurons binds D₂ receptors on lactotrophs to inhibit PRL secretion.",
                ref(
                    "Regulation",
                    "Dopamine reaches the lactotrophs via the hypothalamic-pituitary portal system and binds to type 2 dopamine (D₂) receptors on pituitary lactotrophs to inhibit PRL secretion.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Prolactin",
                "Monomeric 23-kDa prolactin is the most bioactive circulating form.",
                True,
                "Monomeric PRL is the most bioactive; macroprolactin is often clinically inactive.",
                ref(
                    "Prolactin Structure",
                    "The monomeric form is the most bioactive PRL.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "GH axis",
                "A normal IGF-1 level in an adult with pituitary disease excludes growth hormone deficiency.",
                False,
                "IGF-1 may be normal in adult GHD; provocative testing is required when clinical suspicion is high.",
                ref(
                    "Growth Hormone-Responsive Markers",
                    "Although IGF-1 levels are reduced in adult GHD, a normal concentration does not exclude the diagnosis",
                ),
            ),
            tf(
                f"{p}-tf6",
                "GH axis",
                "The insulin tolerance test is considered the gold standard provocative test for adult GH deficiency.",
                True,
                "ITT is the gold standard; it also stimulates ACTH.",
                ref(
                    "Provocative Testing",
                    "The ITT is the gold standard test for GHD.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "ACTH axis",
                "Secondary adrenal insufficiency typically causes hyperkalemia and hyperpigmentation like Addison disease.",
                False,
                "ACTH deficiency spares mineralocorticoids and lacks ACTH-related hyperpigmentation.",
                ref(
                    "Clinical Features",
                    "adrenal mineralocorticoid secretion is largely unimpaired, salt wasting, volume contraction, and hyperkalemia, commonly encountered features in Addison disease, are not manifest.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "ACTH axis",
                "Circadian ACTH and cortisol rhythms are lost in Cushing disease.",
                True,
                "Fig. 6.27 shows loss of concordant ultradian ACTH-cortisol patterns in Cushing disease.",
                ref(
                    "Circadian Periodicity",
                    "ACTH circadian rhythm is entrained by visual cues and the light-dark cycle, is centrally controlled by CRH and other factors, and is lost in Cushing disease",
                ),
            ),
            tf(
                f"{p}-tf9",
                "TSH axis",
                "Third-generation TSH assays with detection limits near 0.01 mU/L have largely replaced TRH testing for thyrotoxicosis evaluation.",
                True,
                "Ultrasensitive TSH revolutionized thyroid diagnosis and obsoleted TRH for thyrotoxicosis workup.",
                ref(
                    "TSH Assays",
                    "A major consequence of ultrasensitive TSH assay is the obsolescence of the TRH test for patients suspected of thyrotoxicosis.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Gonadotropins",
                "Pulsatile GnRH administration can restore gonadotropin secretion in GnRH-deficient patients.",
                True,
                "Pulsatile exogenous GnRH restores gonadotropins whereas continuous exposure suppresses them.",
                ref(
                    "Gonadotropin-Releasing Hormone",
                    "restoration of gonadotropin secretion can be achieved after exogenous pulsatile GnRH treatment",
                ),
            ),
            tf(
                f"{p}-tf11",
                "PROP1",
                "PROP1 mutations are the most common genetic cause of combined pituitary hormone deficiency.",
                True,
                "PROP1 is the most common CPHD gene in genetic screening cohorts.",
                ref(
                    "PROP1",
                    "Mutations in PROP1 are the most common genetic cause of combined pituitary hormone deficiency (CPHD)",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Incidental findings",
                "An incidental empty sella never requires evaluation for pituitary dysfunction.",
                False,
                "If >90% of pituitary tissue is atrophied, pituitary failure usually occurs; masses warrant screening.",
                ref(
                    "Empty Sella Syndrome",
                    "if more than 90% of pituitary tissue is compressed or atrophied, pituitary failure usually occurs.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Stalk injury",
                "Pituitary stalk disruption can cause both anterior hypopituitarism and diabetes insipidus.",
                True,
                "Stalk lesions deprive anterior pituitary of hypothalamic input and often attenuate AVP secretion.",
                ref(
                    "Pituitary Blood Supply",
                    "Disruption of stalk integrity may lead to compromised pituitary portal blood flow, depriving the anterior pituitary cells of hypothalamic hormone input.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Portal circulation",
                "Assertion: Hypothalamic hormones reach anterior pituitary cells without significant systemic dilution.",
                "Reason: Long and short hypophyseal portal vessels connect the median eminence capillary plexus to the adenohypophysis.",
                0,
                "Both are true and the portal anatomy directly explains concentrated hypothalamic hormone delivery.",
                ref(
                    "Pituitary Blood Supply",
                    "without significant systemic dilution, allowing the pituitary cells to be sensitively regulated by timed hypothalamic hormone secretion.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "PROP1",
                "Assertion: PROP1 mutations may cause deficiency of GH, PRL, TSH, and gonadotropins.",
                "Reason: PROP1 is a prerequisite for PIT1-dependent somatotroph, lactotroph, and thyrotroph development.",
                0,
                "Both true and causally linked—PROP1 acts upstream of POU1F1 lineages and affects gonadotroph function.",
                ref(
                    "Pituitary Transcription Factors",
                    "Prop1, expressed early in the development of Rathke's pouch, is a pre-requisite for Pit1",
                ),
            ),
            ar(
                f"{p}-ar3",
                "TBX19",
                "Assertion: TBX19 mutations cause isolated ACTH deficiency.",
                "Reason: TBX19 (Tpit) is required for POMC expression in corticotrophs.",
                0,
                "Both true; Tpit directs corticotroph commitment and POMC transcription.",
                ref(
                    "Pituitary Transcription Factors",
                    "corticotroph cell commitment is directed by Tbx19 protein (previously referred to as Tpit).",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Prolactin",
                "Assertion: Prolactin is under unique tonic inhibitory hypothalamic control.",
                "Reason: Dopamine from tuberoinfundibular neurons inhibits lactotroph secretion via D₂ receptors.",
                0,
                "Both true; dopamine is the principal physiologic PRL inhibitory signal.",
                ref(
                    "Regulation",
                    "PRL secretion is under inhibitory control by dopamine, produced by the tuberoinfundibular (TIDA) cells",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Macroprolactin",
                "Assertion: Macroprolactinemia may be detected without clinical hyperprolactinemia effects.",
                "Reason: Macroprolactin is composed of prolactin bound to immunoglobulins and is less bioactive than monomeric PRL.",
                0,
                "Both true; assay detects macroprolactin but biologic activity is low.",
                ref(
                    "Prolactin Structure",
                    "The monomeric form is the most bioactive PRL.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "GH axis",
                "Assertion: IGF-1 suppresses GH secretion.",
                "Reason: IGF-1 stimulates hypothalamic somatostatin release and inhibits pituitary GH gene transcription.",
                0,
                "Both true with direct causal linkage in negative feedback.",
                ref(
                    "Regulation",
                    "IGF-1, which participates in a hypothalamic-pituitary peripheral regulatory feedback system, stimulating hypothalamic SRIF release and inhibiting GH gene transcription and secretion.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "GH testing",
                "Assertion: GHRH plus arginine testing may miss GH deficiency from hypothalamic disease.",
                "Reason: GHRH acts directly on the pituitary and does not test hypothalamic GHRH neuronal integrity.",
                0,
                "Both true; ITT is preferred when hypothalamic disease is suspected (e.g., post-irradiation).",
                ref(
                    "Provocative Testing",
                    "Diagnostic tests employing GHRH or GHRPs, both of which directly stimulate GH release from the pituitary gland, may not identify GHD caused by hypothalamic disease.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "ACTH axis",
                "Assertion: Morning cortisol below 3 µg/dL suggests ACTH deficiency.",
                "Reason: Cortisol values above 18 µg/dL in the morning usually indicate normal ACTH reserve.",
                1,
                "Both statements are true but the reason does not explain the assertion—they describe opposite ends of the diagnostic spectrum.",
                ref(
                    "Evaluation",
                    "Morning serum cortisol levels lower than 3 µg/dL suggest ACTH deficiency, but basal morning cortisol levels higher than 18 µg/dL usually indicate normal ACTH reserve.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "TSH axis",
                "Assertion: Central hypothyroidism may present with low free T₄ and inappropriately normal TSH.",
                "Reason: Ultrasensitive TSH assays can reliably diagnose central hypothyroidism without measuring free T₄.",
                2,
                "Assertion true; reason false—TSH alone is not helpful for central hypothyroidism.",
                ref(
                    "TSH Assays",
                    "TSH measurement alone is not helpful in diagnosing central hypothyroidism, which is identified by concurrent measurement of thyroid hormone levels.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "GnRH",
                "Assertion: Continuous GnRH infusion suppresses LH and FSH secretion.",
                "Reason: GnRH must be secreted in pulses to stimulate gonadotrophs.",
                0,
                "Both true; pulsatility is required for stimulation whereas continuous exposure desensitizes/suppresses.",
                ref(
                    "Gonadotropin-Releasing Hormone",
                    "whereas continuous GnRH exposure suppresses gonadotropin secretion.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Screening",
                "Assertion: All patients with pituitary masses should be screened for hypopituitarism.",
                "Reason: Up to two-thirds of patients with macroadenomas or parasellar lesions have compromised pituitary reserve.",
                0,
                "Both true; high prevalence of subclinical deficits justifies screening.",
                ref(
                    "Screening for Pituitary Insufficiency",
                    "Up to two-thirds of patients harboring pituitary macroadenomas, craniopharyngiomas, and other parasellar lesions have compromised pituitary reserve function.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Stalk transection",
                "Assertion: Pituitary stalk transection can cause diabetes insipidus.",
                "Reason: The posterior pituitary is directly innervated by hypothalamic neurohypophyseal tracts, and stalk lesions disrupt AVP delivery.",
                0,
                "Both true; stalk/hypothalamic injury attenuates vasopressin secretion causing AVP deficiency.",
                ref(
                    "Anatomy",
                    "The posterior pituitary gland, in contrast to the anterior pituitary, is directly innervated by the supraopticohypophyseal and tuberohypophyseal nerve tracts of the posterior stalk.",
                ),
            ),
        ]
    )

    return {
        "id": "w15-06",
        "volume": 15,
        "chapterNo": "6",
        "title": "Pituitary Physiology and Diagnostic Evaluation",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Ursula Kaiser, Ken K. Y. Ho",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_06_Pituitary_Physiology_and_Diagnostic_Evaluation.md",
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
