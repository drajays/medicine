#!/usr/bin/env python3
"""Generate Williams 15e module w15-07 — Pituitary Adenomas and Masses."""
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
OUT_NAME = "w15-07_Pituitary_Adenomas_and_Masses.json"


def build() -> dict:
    p = "w15-07"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Mass effects",
                "Bitemporal hemianopia from chiasmal compression",
                "As sellar masses impinge upon the optic chiasm, pressure from below affects temporal visual fields, starting superiorly and ultimately extending to the entire temporal field; continued growth may extend visual loss to the nasal field and cause blindness with optic disc atrophy.",
                ref(
                    "Pituitary Mass Effects",
                    "As sellar masses impinge upon the optic chiasm, they may interfere with vision. Because of the anatomy of the chiasm, pressure from below affects temporal visual fields, starting superiorly and ultimately extending to the entire temporal field.",
                ),
            ),
            note(
                f"{p}-n2",
                "Mass effects",
                "Why pituitary masses preferentially cause superior bitemporal field loss",
                "Decussation of nasal retinal fibers at the chiasm segregates superior and inferior fibers; inferior crossing chiasmal fibers are most vulnerable to upward sellar expansion, so pituitary-related defects usually begin in the superior temporal quadrants before progressing.",
                ref(
                    "Neuroophthalmologic Assessment",
                    "Most pituitary-related visual defects involve impingement of the inferior crossing chiasmal fibers leading to bitemporal visual loss, especially in the superior field portions.",
                ),
            ),
            note(
                f"{p}-n3",
                "Mass effects",
                "How cavernous sinus invasion produces cranial neuropathy",
                "Lateral extension may impinge on or invade the dural wall of the cavernous sinus, compromising the third, fourth, and sixth cranial nerves and ophthalmic and maxillary branches of the fifth nerve—causing diplopia, ptosis, ophthalmoplegia, and facial numbness depending on extent of involvement.",
                ref(
                    "Pituitary Mass Effects",
                    "Extension of pituitary lesions laterally may also impinge on or invade the dural wall of the cavernous sinus.",
                ),
            ),
            note(
                f"{p}-n4",
                "Stalk compression",
                "How stalk compression causes hyperprolactinemia with hypopituitarism",
                "Stalk compression encroaches on portal vessels delivering hypothalamic trophic hormones and simultaneously blocks hypothalamic dopamine access to lactotrophs, producing modest hyperprolactinemia alongside failure of other anterior pituitary axes.",
                ref(
                    "Pituitary Mass Effects",
                    "Stalk compression also usually leads to hyperprolactinemia due to compromised dopamine access, with concomitant failure of other pituitary trophic hormones.",
                ),
            ),
            note(
                f"{p}-n5",
                "Hypopituitarism",
                "Hypopituitarism from sellar mass compression",
                "Pituitary masses compress surrounding healthy tissue and cause hypopituitarism; elevated intrasellar pressure correlates with headache and elevated PRL, suggesting interrupted portal delivery of hypothalamic hormones, and surgical decompression may recover compromised anterior function.",
                ref(
                    "Pituitary Mass Effects",
                    "Regardless of cause or size, pituitary masses may compress surrounding healthy pituitary tissue and result in hypopituitarism.",
                ),
            ),
            note(
                f"{p}-n6",
                "Differential diagnosis",
                "Why adenoma is the default sellar mass diagnosis",
                "Pituitary adenomas account for 82–91% of sellar lesions on MRI and surgery series; management and prognosis differ markedly from nonpituitary masses, so the differential should first aim to confirm or exclude adenoma before rare alternatives.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "Thus, the differential diagnosis of a pituitary mass should be aimed at excluding the diagnosis of a pituitary adenoma before considering the presence of other rare sellar lesions.",
                ),
            ),
            note(
                f"{p}-n7",
                "Differential diagnosis",
                "Adenoma versus Rathke cleft cyst, craniopharyngioma, meningioma",
                "Most commonly encountered nonadenomatous lesions include Rathke's cleft cyst, craniopharyngioma, and meningioma, with Rathke's cysts accounting for up to 40% of such masses; MRI features including calcification, distinct noninvolved pituitary tissue, and consistency often suggest the diagnosis before histology.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "Most commonly encountered nonadenomatous lesions include Rathke's cleft cyst, craniopharyngioma, and meningioma, with Rathke's cysts accounting for up to 40% of all such masses.",
                ),
            ),
            note(
                f"{p}-n8",
                "Incidentaloma workup",
                "How to screen incidentally discovered pituitary masses",
                "Endocrine function should always be tested at presentation; in the absence of a hypersecretory syndrome, cost-effective screening includes serum PRL, age-matched IGF-1, and 24-hour UFC or nighttime salivary cortisol, while assessing local compressive effects and growth potential.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "In the absence of clinical features of a humoral hypersecretory syndrome, cost-effective laboratory screening should be performed.",
                ),
            ),
            note(
                f"{p}-n9",
                "Stalk effect",
                "Why mild hyperprolactinemia does not prove prolactinoma",
                "A minimal to moderate PRL elevation can indicate stalk interruption by a nonfunctioning macroadenoma; only very high levels (>500 ng/mL in a nonpregnant individual) are pathognomonic of prolactinoma, as drugs and other causes can also elevate PRL.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "A minimal to moderate elevation can also indicate secondary stalk interruption by a pituitary mass (usually a nonfunctioning macroadenoma).",
                ),
            ),
            note(
                f"{p}-n10",
                "Prolactin thresholds",
                "Serum PRL levels distinguishing prolactinoma from stalk effect",
                "Serum PRL >200 ng/mL strongly suggests micro- or macroprolactinoma; stalk-effect hyperprolactinemia from NFA compression is usually modest (often up to ~100 ng/mL), whereas prolactinoma typically drives much higher levels when pathognomonic.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "Serum PRL levels >200 ng/mL strongly suggest the presence of a micro- or macroprolactinoma.",
                ),
            ),
            note(
                f"{p}-n11",
                "Prolactinoma",
                "Why cabergoline is first-line for prolactinoma",
                "Cabergoline is better tolerated, more potent, longer acting, and usually given once or twice weekly compared with bromocriptine; large studies show superior PRL normalization, tumor shrinkage, and restoration of gonadal function.",
                ref(
                    "Cabergoline",
                    "Cabergoline is considered the first-line therapeutic choice for most patients harboring prolactinomas.",
                ),
            ),
            note(
                f"{p}-n12",
                "Prolactinoma surgery",
                "Surgery indications for prolactinoma",
                "Surgery is indicated for progressive visual loss, DA-induced CSF rhinorrhea, hemorrhagic components threatening vision, DA resistance or intolerance, and prepregnancy debulking of macroprolactinomas; microprolactinoma resection by experienced surgeons normalizes PRL in up to ~90% of selected cases.",
                ref(
                    "Surgery",
                    "Surgery is also indicated for risk of progressive visual loss or for DA-induced CSF rhinorrhea, as well as for adenomas with hemorrhagic components endangering visual pathways.",
                ),
            ),
            note(
                f"{p}-n13",
                "Nonfunctioning adenoma",
                "How NFA stalk blockade mimics prolactinoma",
                "In NFAs, portal-vein dopamine delivery may be disrupted by stalk blockade, raising PRL usually to levels up to 100 ng/mL; mildly elevated PRL at diagnosis correlates with greater postoperative pituitary recovery, supporting reversible hypothalamic rather than intrinsic lactotroph disease.",
                ref(
                    "Hormonal Manifestations",
                    "in fact, stalk blockade of portal vein dopamine delivery (see Fig. 7.27) may increase PRL usually to levels up to 100 ng/mL, and prolactinoma should be considered in the differential diagnosis.",
                ),
            ),
            note(
                f"{p}-n14",
                "Nonfunctioning adenoma",
                "NFA and macroadenoma management",
                "NFAs are usually gonadotroph or null-cell macroadenomas presenting with compression or as incidentalomas; transsphenoidal resection is primary therapy when vision is threatened or mass grows, as medical treatment is ineffective, with observation reasonable for stable microadenomas.",
                ref(
                    "Treatment",
                    "As medical treatment of NFAs is not effective, transphenoidal surgical resection is the primary treatment modality.",
                ),
            ),
            note(
                f"{p}-n15",
                "Surgery",
                "Why transsphenoidal surgery is the standard approach",
                "The transsphenoidal approach avoids craniotomy, permits high-magnification microdissection, and is associated with minimal morbidity—most patients are ambulatory within 6–9 hours with ~2-day hospital stays—while decompressing chiasm and restoring hormone function.",
                ref(
                    "Surgical",
                    "Thus, transsphenoidal surgery is associated with minimal morbidity and mortality, most patients are ambulatory within 6 to 9 hours, and the hospital stay is generally about 2 days.",
                ),
            ),
            note(
                f"{p}-n16",
                "Apoplexy",
                "Pituitary apoplexy presentation",
                "Pituitary apoplexy is an endocrine emergency evolving over 1–2 days with severe headache, ocular palsies or visual field defects, cardiovascular collapse, and frequent acute adrenal insufficiency from ACTH loss; MRI shows intrapituitary hemorrhage and stalk deviation.",
                ref(
                    "Clinical Features",
                    "Pituitary apoplexy is an endocrine emergency.",
                ),
            ),
            note(
                f"{p}-n17",
                "Apoplexy",
                "How to manage pituitary apoplexy",
                "Patients with visual field compromise require urgent transsphenoidal surgery; alert patients without visual symptoms may be observed, but most need glucocorticoid replacement or stress-dose cortisol because adrenal dysfunction is common before and after treatment.",
                ref(
                    "Management",
                    "Patients with visual field compromise require urgent transsphenoidal surgery.",
                ),
            ),
            note(
                f"{p}-n18",
                "Radiation",
                "How pituitary radiation controls residual disease",
                "Fractionated radiotherapy (45–50 Gy) halts growth in over 90% of nonsecreting adenomas by 10 years; radiation is adjuvant for persistent hormone hypersecretion, residual mass effects, or when surgery is contraindicated, with secretory adenomas generally more resistant.",
                ref(
                    "Indications",
                    "Overall, fractionated radiotherapy (45–50 Gy) halts growth in over 90% of nonsecreting adenomas by 10 years, whereas secretory adenomas are usually more resistant.",
                ),
            ),
            note(
                f"{p}-n19",
                "Radiation",
                "Why radiation causes late hypopituitarism",
                "Within 10 years after pituitary irradiation, up to 80% of patients may develop one or more trophic hormone deficits; hypopituitarism likely reflects hypothalamic releasing-cell damage, mandating lifelong pituitary reserve testing and replacement.",
                ref(
                    "Side Effects",
                    "Within 10 years, up to 80% of patients may have one or more of FSH, LH, GH, TSH, or ACTH deficits.",
                ),
            ),
            note(
                f"{p}-n20",
                "Acromegaly",
                "Somatostatin receptor ligands in acromegaly",
                "SRLs (octreotide, lanreotide, pasireotide) inhibit GH secretion via SST2/SST5 on somatotrophs; meta-analyses show ~55–65% GH and IGF-1 control, with tumor mass stabilized or reduced in about half of patients, and IGF-1 is the key biochemical marker of response.",
                ref(
                    "Determinants of SRL Responsiveness",
                    "In a meta-analysis of 4464 patients treated with an SRL, average GH control rates and IGF1 normalization rates were 56% and 55%, respectively.",
                ),
            ),
            note(
                f"{p}-n21",
                "Acromegaly",
                "Why pegvisomant efficacy is tracked by IGF-1 not GH",
                "Pegvisomant blocks peripheral GH receptor signaling without targeting the adenoma, so GH rises as IGF-1 negative feedback is lost; IGF-1 normalization (~60–90% in trials) is the appropriate efficacy marker, especially for SRL-resistant disease.",
                ref(
                    "Growth Hormone Receptor Antagonist",
                    "Measuring GH is therefore not an efficacy marker and IGF1 measurement is the appropriate marker of patient responsiveness.",
                ),
            ),
            note(
                f"{p}-n22",
                "Cushing disease",
                "ACTH adenoma and biochemical diagnosis of Cushing disease",
                "Cushing disease is pituitary ACTH hypersecretion causing hypercortisolism; diagnosis rests on elevated UFC and late-night salivary cortisol with nonsuppressed ACTH and failure to suppress morning cortisol to <1.8 µg/dL after 1 mg overnight dexamethasone.",
                ref(
                    "ACTH-Secreting Adenomas (Cushing Disease)",
                    "Failure to suppress morning 0800 h cortisol levels to less than 1.8 µg/dL after 1 mg dexamethasone administered between 2300 h and midnight supports the Cushing disease diagnosis.",
                ),
            ),
            note(
                f"{p}-n23",
                "Cushing disease",
                "How bilateral inferior petrosal sinus sampling localizes ACTH",
                "When MRI fails to show a microadenoma, bilateral inferior petrosal sinus ACTH sampling with peripheral levels lateralizes secretion—gradient to one side guides hemihypophysectomy, whereas equal petrosal and peripheral elevation suggests ectopic ACTH production.",
                ref(
                    "ACTH-Secreting Adenomas (Cushing Disease)",
                    "Localization techniques using inferior bilateral petrosal sinus venography enables measuring ACTH secretion from the adenoma, which is usually unilateral; therefore, right and left petrosal samples and a peripheral vein are analyzed for ACTH levels, and the gradient compared to systemic levels.",
                ),
            ),
            note(
                f"{p}-n24",
                "Parasellar masses",
                "Hypophysitis as a sellar mass mimic",
                "Primary hypophysitis presents with anterior hypopituitarism and MRI showing enlarged homogeneously enhancing gland with stalk thickening; it may mimic adenoma and definitive diagnosis sometimes requires biopsy, with glucocorticoids or other immunotherapy for symptomatic disease.",
                ref(
                    "Hypophysitis",
                    "Pituitary mass lesions may be composed of inflammatory cells and may arise as primary hypophysitis disorders.",
                ),
            ),
            note(
                f"{p}-n25",
                "Parasellar masses",
                "Sarcoidosis, chordoma, and parasellar aneurysm",
                "CNS sarcoidosis may diffusely invade hypothalamus, stalk, and posterior pituitary with thickened stalk on MRI; chordomas arise from notochord remnants with calcification and bony erosion; parasellar aneurysms may mimic adenoma and require preoperative MR angiography to avoid catastrophic rupture.",
                ref(
                    "Sarcoidosis",
                    "The hypothalamus, pituitary stalk, and posterior pituitary are diffusely invaded by noncaseating granulomas, consisting of giant cells, macrophages, and lymphocytes.",
                ),
            ),
            note(
                f"{p}-n26",
                "Pregnancy",
                "Why pregnancy causes physiologic pituitary enlargement",
                "Lactotroph hyperplasia occurs during pregnancy as estrogen stimulates the gland, which normally should not exceed 10–12 mm with stalk ≤4 mm; this physiologic enlargement must be distinguished from prolactinoma, especially when imaging is obtained for unrelated indications.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "Lactotroph hyperplasia occurs during pregnancy, and thyrotroph, gonadotroph, or rarely corticotroph hyperplasias occur in the presence of long-standing primary thyroid, gonadal, or adrenal failure, respectively.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Mass effects",
                "A 52-year-old man with progressive peripheral vision loss undergoes perimetry showing bitemporal superior quadrantanopia. MRI shows a homogeneously enhancing sellar mass elevating the optic chiasm. Which anatomic relationship best explains the field defect?",
                [
                    "Compression of uncrossed temporal retinal fibers at the lateral chiasm",
                    "Compression of inferior crossing nasal retinal fibers at the chiasm",
                    "Optic tract lesion posterior to the chiasm",
                    "Monocular retinal detachment",
                ],
                1,
                "Pituitary masses compress from below; inferior crossing chiasmal fibers produce bitemporal loss beginning in superior temporal fields.",
                ref(
                    "Neuroophthalmologic Assessment",
                    "Most pituitary-related visual defects involve impingement of the inferior crossing chiasmal fibers leading to bitemporal visual loss, especially in the superior field portions.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Mass effects",
                "A woman with a large pituitary macroadenoma reports diplopia and right facial numbness. MRI shows tumor surrounding the right internal carotid artery within the cavernous sinus. Which finding is most likely?",
                [
                    "Bilateral papilledema without cranial neuropathy",
                    "Ophthalmoplegia with decreased maxillary sensation",
                    "Isolated bitemporal hemianopia only",
                    "Primary hyperaldosteronism",
                ],
                1,
                "Cavernous sinus invasion can affect III, IV, VI and V2 branches, causing ophthalmoplegia and facial numbness.",
                ref(
                    "Pituitary Mass Effects",
                    "Varying degrees of diplopia, ptosis, ophthalmoplegia, and decreased facial sensation may occur infrequently, depending on the extent of neural involvement by the cavernous sinus mass.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Hypopituitarism",
                "After transsphenoidal debulking of a nonfunctioning macroadenoma, a patient's morning cortisol and free T4 normalize within weeks. Preoperative PRL was 85 ng/mL with low testosterone. What best explains the preoperative endocrinopathy?",
                [
                    "Autonomous prolactin secretion from a lactotroph adenoma",
                    "Stalk compression with portal vessel disruption and dopamine blockade",
                    "Primary adrenal insufficiency unrelated to the pituitary",
                    "Ectopic GHRH secretion",
                ],
                1,
                "Stalk/mass compression interrupts portal hypothalamic hormones and dopamine, causing hypopituitarism with modest hyperPRL; decompression can restore function.",
                ref(
                    "Pituitary Mass Effects",
                    "Stalk compression may result in pituitary failure caused by encroachment of the portal vessels that normally provide pituitary access to hypothalamic trophic hormones.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Differential diagnosis",
                "MRI for headaches reveals a sellar mass. Which statement best guides initial diagnostic thinking?",
                [
                    "Craniopharyngioma is more common than pituitary adenoma",
                    "Assume pituitary adenoma until proven otherwise",
                    "Meningioma accounts for >80% of sellar lesions",
                    "No hormonal testing is needed if the patient is asymptomatic",
                ],
                1,
                "Adenomas dominate sellar pathology; the workup first confirms or excludes adenoma because management differs from other masses.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "Thus, the differential diagnosis of a pituitary mass should be aimed at excluding the diagnosis of a pituitary adenoma before considering the presence of other rare sellar lesions.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Differential diagnosis",
                "A cystic suprasellar mass in a young adult shows calcification on CT and distinct pituitary tissue on MRI. Which diagnosis is most likely?",
                [
                    "Prolactinoma",
                    "Craniopharyngioma",
                    "Lymphocytic hypophysitis",
                    "Internal carotid aneurysm",
                ],
                1,
                "Craniopharyngiomas often calcify and are among the common nonadenomatous sellar masses; CT helps identify calcification.",
                ref(
                    "Imaging",
                    "CT also recognizes calcifications that characterize craniopharyngiomas, meningiomas, and rarely aneurysms not evident on MRI.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Incidentaloma",
                "A 45-year-old woman has a 7-mm pituitary lesion found on MRI after minor head trauma. She has no visual symptoms. Best next step?",
                [
                    "Immediate transsphenoidal surgery",
                    "Screen PRL, IGF-1, and cortisol; assess vision if macroadenoma or growth",
                    "Therapeutic radiation",
                    "No follow-up ever required",
                ],
                1,
                "All pituitary masses need endocrine screening and assessment of compressive risk; microadenomas rarely need immediate intervention.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "As the onset of clinical features associated with disordered hormone secretion is insidious and may be unnoticed for years or decades, endocrine function should always be tested at presentation.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Stalk effect",
                "A man with a 3.5-cm sellar mass has PRL 95 ng/mL, low testosterone, and low free T4. Which finding most strongly favors stalk-effect hyperprolactinemia over prolactinoma?",
                [
                    "PRL >500 ng/mL",
                    "Galactorrhea with normal gonadotropins",
                    "Concurrent panhypopituitarism with modest PRL elevation",
                    "Microadenoma on MRI",
                ],
                2,
                "Stalk interruption by NFA commonly raises PRL only modestly (often ≤100 ng/mL) with other axis failure; prolactinoma drives higher PRL.",
                ref(
                    "Hormonal Manifestations",
                    "stalk blockade of portal vein dopamine delivery (see Fig. 7.27) may increase PRL usually to levels up to 100 ng/mL, and prolactinoma should be considered in the differential diagnosis.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Prolactinoma",
                "A 28-year-old woman with amenorrhea has PRL 320 ng/mL and a 12-mm pituitary microadenoma. First-line management?",
                [
                    "Immediate transsphenoidal surgery",
                    "Cabergoline",
                    "External-beam pituitary radiation",
                    "Observation only without therapy",
                ],
                1,
                "Dopamine agonists, especially cabergoline, are first-line for most prolactinomas with excellent biochemical and tumor responses.",
                ref(
                    "Prolactin-Secreting Adenomas",
                    "Medical management of prolactinomas with DAs has been widely recommended as the treatment of choice",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Prolactinoma",
                "A prolactinoma patient on cabergoline develops persistent visual field loss despite biochemical improvement. Next step?",
                [
                    "Increase cabergoline to maximum dose indefinitely",
                    "Refer for transsphenoidal surgery",
                    "Start pegvisomant",
                    "Bilateral adrenalectomy",
                ],
                1,
                "Progressive visual compromise is a surgical indication even when on dopamine agonist therapy.",
                ref(
                    "Surgery",
                    "Surgery is also indicated for risk of progressive visual loss or for DA-induced CSF rhinorrhea, as well as for adenomas with hemorrhagic components endangering visual pathways.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Nonfunctioning adenoma",
                "A 60-year-old man has an incidental 2.8-cm pituitary mass without visual symptoms and mild GH deficiency only. Most appropriate management?",
                [
                    "Cabergoline monotherapy",
                    "Serial MRI and formal perimetry with surgery if growth or vision threatened",
                    "Immediate radiation",
                    "Pegvisomant",
                ],
                1,
                "NFAs without threatening features may be observed; macroadenomas need visual testing and surgery when compressive indications arise.",
                ref(
                    "Natural History",
                    "Expectant follow-up could be undertaken for patients with microadenomas and few hormonal disturbances as macroadenomas exhibit a greater propensity to grow, induce more hypopituitarism, and have more visual disturbances requiring surgery.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Surgery",
                "Which pituitary tumor type is primarily managed with transsphenoidal resection rather than medical monotherapy?",
                [
                    "Microprolactinoma in a woman seeking fertility",
                    "ACTH-secreting microadenoma (Cushing disease)",
                    "Incidental 5-mm nonfunctioning microadenoma",
                    "Giant prolactinoma responding to cabergoline",
                ],
                1,
                "Surgery is primary for ACTH adenomas, GH adenomas, TSH adenomas, and often nonfunctioning macroadenomas; prolactinomas usually start with DAs.",
                ref(
                    "Indications for Transsphenoidal Surgery",
                    "Surgery is primarily indicated for well-circumscribed GH-secreting adenomas, TSH-secreting adenomas, all ACTH-secreting adenomas, and often for nonfunctioning macroadenomas.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Apoplexy",
                "A man with known pituitary macroadenoma presents with sudden severe headache, left third-nerve palsy, and bitemporal field loss. BP 80/50 mmHg. Immediate priority?",
                [
                    "Schedule elective surgery in 4 weeks",
                    "Urgent glucocorticoids and transsphenoidal decompression",
                    "Start cabergoline only",
                    "Observation without steroids",
                ],
                1,
                "Apoplexy with visual compromise is surgical emergency; adrenal crisis is common and requires corticosteroid support.",
                ref(
                    "Management",
                    "Patients with visual field compromise require urgent transsphenoidal surgery.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Radiation",
                "A patient with residual functioning acromegaly after subtotal transsphenoidal resection and inadequate SRL response is considering radiation. Counseling should include which risk?",
                [
                    "Immediate IGF-1 normalization within days",
                    "High likelihood of new hypopituitarism within 10 years",
                    "No risk of second intracranial neoplasm",
                    "Contraindication if tumor is near optic chiasm",
                ],
                1,
                "Radiation is slow and adjuvant; up to 80% develop pituitary hormone deficits within a decade, among other risks.",
                ref(
                    "Side Effects",
                    "Within 10 years, up to 80% of patients may have one or more of FSH, LH, GH, TSH, or ACTH deficits.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Acromegaly",
                "A 48-year-old with acromegaly has persistent elevated IGF-1 despite maximal injectable SRL. He has diabetes and bulky soft-tissue features. Best add-on therapy?",
                [
                    "Bromocriptine monotherapy",
                    "Pegvisomant",
                    "Levothyroxine suppression",
                    "Observation only",
                ],
                1,
                "Pegvisomant blocks peripheral GH action and normalizes IGF-1 in most SRL-resistant patients; it may also improve insulin sensitivity.",
                ref(
                    "Growth Hormone Receptor Antagonist",
                    "The drug may be used as primary therapy monotherapy and is particularly useful in patients resistant to SRL therapy, because it effectively normalizes IGF1 levels in these patients.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Acromegaly",
                "A patient with acromegaly achieves normal IGF-1 on octreotide LAR but GH remains detectable. Appropriate monitoring marker?",
                [
                    "Serum GH alone",
                    "Age-matched IGF-1",
                    "Random prolactin only",
                    "Serum cortisol at midnight",
                ],
                1,
                "IGF-1 is the rigorous marker for SRL efficacy; pegvisomant likewise uses IGF-1 because GH may rise when peripheral blockade is used.",
                ref(
                    "Determinants of SRL Responsiveness",
                    "Measurement of serum IGF1 levels was the most rigorous marker to assess effectiveness of SRL therapy.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Cushing disease",
                "Biochemical testing shows elevated 24-hour UFC, elevated late-night salivary cortisol, and ACTH 45 pg/mL (midnormal) with 8 AM cortisol 22 µg/dL after 1 mg overnight dexamethasone. Diagnosis?",
                [
                    "Adrenal adenoma",
                    "Cushing disease (pituitary ACTH adenoma)",
                    "Exogenous glucocorticoid use only",
                    "Primary hypothyroidism",
                ],
                1,
                "Nonsuppressed cortisol after low-dose dexamethasone with ACTH dependence supports Cushing disease over adrenal causes.",
                ref(
                    "ACTH-Secreting Adenomas (Cushing Disease)",
                    "Failure to suppress morning 0800 h cortisol levels to less than 1.8 µg/dL after 1 mg dexamethasone administered between 2300 h and midnight supports the Cushing disease diagnosis.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Cushing disease",
                "MRI is negative in a patient with confirmed ACTH-dependent Cushing syndrome. Bilateral inferior petrosal sinus sampling shows central-to-peripheral ACTH gradient >3 on the right only. Next step?",
                [
                    "Chest CT for ectopic ACTH only; no pituitary surgery",
                    "Right-sided transsphenoidal exploration or hemihypophysectomy",
                    "Bilateral adrenalectomy without pituitary exploration",
                    "Therapeutic radiation without localization",
                ],
                1,
                "BIPSS lateralizes pituitary ACTH secretion to guide surgical exploration when MRI is unrevealing.",
                ref(
                    "ACTH-Secreting Adenomas (Cushing Disease)",
                    "If high levels are observed on one side, the neurosurgeon is guided to operate on that side of the pituitary gland or even perform a hemipituitary-erectomy.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Parasellar masses",
                "A young woman postpartum has polyuria, low cortisol, and MRI showing homogeneously enlarged pituitary with thickened stalk. Most likely diagnosis?",
                [
                    "Prolactinoma",
                    "Lymphocytic hypophysitis",
                    "GH-secreting adenoma",
                    "Rathke cleft cyst only",
                ],
                1,
                "Hypophysitis often affects women in the third decade, peripartum, with stalk thickening and hypopituitarism on MRI.",
                ref(
                    "Hypophysitis",
                    "Pituitary mass lesions may be composed of inflammatory cells and may arise as primary hypophysitis disorders.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Parasellar masses",
                "A patient with known pulmonary sarcoidosis develops AVP deficiency and anterior pituitary failure. MRI shows thickened infundibulum. Mechanism?",
                [
                    "Autoimmune destruction of adrenal cortex only",
                    "Granulomatous infiltration of hypothalamic-pituitary axis",
                    "Ectopic ACTH from lung only without CNS involvement",
                    "Sheehan syndrome",
                ],
                1,
                "CNS sarcoidosis commonly involves hypothalamus, stalk, and posterior pituitary with granulomatous infiltration.",
                ref(
                    "Sarcoidosis",
                    "The hypothalamus, pituitary stalk, and posterior pituitary are diffusely invaded by noncaseating granulomas, consisting of giant cells, macrophages, and lymphocytes.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Parasellar masses",
                "Preoperative MRI suggests pituitary macroadenoma, but MR angiography shows a vascular flow void in the sella. Critical concern?",
                [
                    "Start cabergoline immediately",
                    "Avoid mistaken transsphenoidal resection of an aneurysm",
                    "Begin pegvisomant",
                    "No need to alter surgical plan",
                ],
                1,
                "Parasellar aneurysms mimic adenomas; preoperative diagnosis is essential because intraoperative rupture may be catastrophic.",
                ref(
                    "Parasellar Aneurysms",
                    "A parasellar aneurysm may mimic a pituitary adenoma, and intraoperative rupture may be catastrophic, underlying the absolute need for preoperative diagnosis.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Pregnancy",
                "A pregnant woman at 20 weeks has pituitary height 11 mm and no visual symptoms. Previously known microprolactinoma on cabergoline stopped at conception. Management?",
                [
                    "Resume high-dose cabergoline routinely in all trimesters without monitoring",
                    "Serial clinical and visual assessment; intervene if headache or visual change",
                    "Mandatory radiation during pregnancy",
                    "Immediate craniotomy",
                ],
                1,
                "Physiologic pituitary enlargement occurs in pregnancy; microprolactinoma expansion risk is low but vigilance for neurologic/visual symptoms is required.",
                ref(
                    "Pregnancy",
                    "In a prospective analysis in which 57 patients with microprolactinomas were followed by formal visual field examinations during pregnancy, none developed visual disturbances.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Prolactinoma",
                "A patient requires >3 mg/week cabergoline for >6 months with incomplete PRL control and tumor shrinkage <50%. Best next step?",
                [
                    "Continue escalating cabergoline indefinitely as only option",
                    "Consider surgery or radiotherapy",
                    "Observation without change",
                    "Thyroid hormone suppression",
                ],
                1,
                "When high-dose cabergoline is needed long term without adequate response, surgery or radiotherapy should be considered.",
                ref(
                    "Cabergoline",
                    "When high doses of cabergoline for resistant prolactinomas are required for more than 6 months, surgery or radiotherapy should be considered.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Imaging",
                "Routine brain MRI with 5-mm slices misses a suspected microadenoma. Best imaging approach?",
                [
                    "Repeat routine brain MRI in 10 years",
                    "Dedicated pituitary MRI with <3 mm coronal and sagittal T1 pre- and post-gadolinium",
                    "Abdominal CT only",
                    "Skull radiograph",
                ],
                1,
                "Pituitary-focused MRI with thin sections is required because routine brain protocols often miss small sellar lesions.",
                ref(
                    "Imaging",
                    "When a sellar mass is suspected, an MRI specifically focused on the pituitary should be performed, as more widely spaced cuts during a routine brain MRI are often inadequate to visualize relatively small pituitary masses.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Acromegaly",
                "A 35-year-old with invasive acromegaly after failed surgery needs medical therapy. Which agent directly inhibits pituitary GH secretion via SST2?",
                [
                    "Pegvisomant",
                    "Octreotide LAR",
                    "Levothyroxine",
                    "Metyrapone",
                ],
                1,
                "SRLs such as octreotide act on pituitary somatostatin receptors to suppress GH; pegvisomant blocks peripheral GH receptor instead.",
                ref(
                    "SRLs",
                    "SRLs have been safely employed as approved drugs for acromegaly.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Cushing disease",
                "After transsphenoidal resection for Cushing disease, morning cortisol is undetectable on postoperative day 2. Interpretation?",
                [
                    "Surgical failure requiring immediate reoperation",
                    "Suggestive of remission; monitor for adrenal insufficiency and late recurrence",
                    "Proves ectopic ACTH source",
                    "Indicates need for immediate bilateral adrenalectomy",
                ],
                1,
                "Low immediate postoperative cortisol suggests remission but mandates glucocorticoid replacement and long-term surveillance for recurrence.",
                ref(
                    "Assessment of Surgical Outcomes",
                    "Remission after surgical adenomectomy, defined as postoperative serum cortisol levels <2 ng/dL, is observed in approximately 80% and 60% of patients with microadenomas and macroadenomas, respectively.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Chordoma",
                "A middle-aged man has clival mass with bony erosion, heterogeneous MRI appearance, and calcification. Distinct pituitary gland is seen separately. Likely diagnosis?",
                [
                    "Prolactinoma",
                    "Chordoma",
                    "Primary hypophysitis",
                    "Physiologic pregnancy hyperplasia",
                ],
                1,
                "Chordomas arise from notochord remnants, often clival, with erosion/calcification and heterogeneous MRI distinct from the normal gland.",
                ref(
                    "Chordomas",
                    "The slow-growing cartilaginous chordomas arise from midline notochord remnants, are locally invasive, and may metastasize.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Mass effects",
                "Long-standing optic chiasm compression from a pituitary mass can cause irreversible optic atrophy.",
                True,
                "Continued chiasmal pressure leads to optic disc atrophy and visual loss that may not fully reverse.",
                ref(
                    "Pituitary Mass Effects",
                    "Continued growth and pressure on the optic apparatus can extend visual loss to the nasal field and may ultimately result in blindness. Long-standing optic chiasm pressure results in optic disc atrophy.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Differential",
                "Rathke cleft cysts may account for up to 40% of nonadenomatous sellar masses.",
                True,
                "Among nonadenomatous lesions, Rathke's cleft cyst is the most common category in surgical/imaging series cited.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "with Rathke's cysts accounting for up to 40% of all such masses.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Incidentaloma",
                "Functional hormone-secreting adenomas are common in asymptomatic patients with incidentally discovered pituitary masses.",
                False,
                "Overall incidence of functional secreting adenomas in asymptomatic incidentalomas is low despite screening.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "Nevertheless, the overall incidence of functional hormone-secreting adenomas in asymptomatic subjects with incidentally discovered pituitary masses is low.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Stalk effect",
                "Stalk compression typically produces prolactin levels >500 ng/mL in nonpregnant adults.",
                False,
                "Stalk effect causes modest hyperprolactinemia; only very high levels are pathognomonic for prolactinoma.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "Only a very elevated PRL level >500 ng/mL in a nonpregnant individual is considered pathognomonic of a prolactinoma, as significant PRL elevations can be caused by drugs such as risperidone and other antipsychotics.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Prolactinoma",
                "Cabergoline is generally preferred over bromocriptine for prolactinoma because of better tolerability and potency.",
                True,
                "Comparative studies favor cabergoline for efficacy, convenience, and side-effect profile.",
                ref(
                    "Cabergoline",
                    "Compared to daily or more frequently dosed bromocriptine, the drug is better tolerated, is more potent, has a longer duration of action, and is usually administered once or twice weekly.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "NFA",
                "Medical therapy is effective first-line treatment for nonfunctioning pituitary macroadenomas.",
                False,
                "NFAs do not respond to medical therapy; surgery is the primary modality when intervention is needed.",
                ref(
                    "Treatment",
                    "As medical treatment of NFAs is not effective, transphenoidal surgical resection is the primary treatment modality.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Apoplexy",
                "Pituitary apoplexy commonly presents with hyperprolactinemia as a distinguishing feature.",
                False,
                "Unlike many adenomas, apoplexy usually does not feature hyperprolactinemia unless infarction occurs within a prolactinoma.",
                ref(
                    "Clinical Features",
                    "Apoplexy, like Sheehan syndrome, is one of the few pituitary tumor presentations in which hyperprolactinemia is not a feature unless infarction occurs within a prolactinoma.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Radiation",
                "Fractionated pituitary radiotherapy typically normalizes hormone hypersecretion within days.",
                False,
                "Radiation is slow-acting adjuvant therapy; hormonal control may take years, especially in secretory adenomas.",
                ref(
                    "Indications",
                    "Most indications for radiation are adjuvant to either surgical or medical treatment.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Acromegaly",
                "Pegvisomant lowers serum GH concentrations and is monitored using GH levels.",
                False,
                "Pegvisomant blocks peripheral GH action; GH may rise and IGF-1 is the efficacy marker.",
                ref(
                    "Growth Hormone Receptor Antagonist",
                    "The drug blocks peripheral GH action and does not target the pituitary adenoma. Measuring GH is therefore not an efficacy marker and IGF1 measurement is the appropriate marker of patient responsiveness.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Cushing disease",
                "With standard 1.5T MRI, only about half of ACTH-secreting microadenomas may be visualized.",
                True,
                "Many Cushing disease adenomas are <2 mm and escape standard MRI, prompting BIPSS.",
                ref(
                    "ACTH-Secreting Adenomas (Cushing Disease)",
                    "With standard 1.5T MRI, only 50% of adenomas are detected; if available, 3T or even 7T MRI or PET may be employed.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Pregnancy",
                "Lactotroph hyperplasia during pregnancy commonly progresses to prolactinoma formation.",
                False,
                "Physiologic lactotroph hyperplasia in pregnancy does not increase prolactinoma frequency.",
                ref(
                    "Pituitary Trophic Activity",
                    "However, lactotroph hyperplasia occurring with pregnancy does not lead to increased frequency of prolactinomas, and somatotroph hyperplasia caused by ectopic GHRH production is not commonly associated with true adenoma formation.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Surgery",
                "Transsphenoidal surgery is indicated for all microprolactinomas at initial diagnosis.",
                False,
                "Prolactinomas are usually treated first with dopamine agonists; surgery is selected for specific indications.",
                ref(
                    "Surgery",
                    "Especially for microprolactinomas, surgery may be a viable alternative to pharmacologic treatment.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Parasellar masses",
                "Visualization of a distinct normal pituitary gland adjacent to a parasellar mass suggests the mass is not of pituitary adenoma origin.",
                True,
                "Separate noninvolved pituitary tissue favors a nonadenomatous parasellar lesion.",
                ref(
                    "Imaging",
                    "Visualization of a distinct pituitary gland adjacent to a parasellar mass suggests that the mass is not of pituitary origin.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Mass effects",
                "Assertion: Pituitary macroadenomas can cause bitemporal hemianopia.",
                "Reason: The optic chiasm lies above the sella and nasal retinal fibers decussate there.",
                0,
                "Both are true and causally linked—suprasellar extension compresses decussating fibers producing bitemporal defects.",
                ref(
                    "Pituitary Mass Effects",
                    "As sellar masses impinge upon the optic chiasm, they may interfere with vision.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Stalk effect",
                "Assertion: Nonfunctioning macroadenomas may cause mild hyperprolactinemia.",
                "Reason: Stalk compression interrupts dopamine delivery to lactotrophs.",
                0,
                "Both true—stalk effect explains modest PRL elevation with other axis failure.",
                ref(
                    "Pituitary Mass Effects",
                    "Stalk compression also usually leads to hyperprolactinemia due to compromised dopamine access, with concomitant failure of other pituitary trophic hormones.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Incidentaloma",
                "Assertion: All patients with pituitary incidentalomas require immediate surgery.",
                "Reason: Microadenoma progression to compressive macroadenoma is uncommon.",
                2,
                "Assertion is false—many incidentalomas are observed; reason is true about low microadenoma progression risk.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "Because the risk for microadenoma progression to a compressive macroadenoma is low, no direct intervention may be warranted.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Prolactinoma",
                "Assertion: Cabergoline is first-line therapy for most prolactinomas.",
                "Reason: Cabergoline has no effect on pituitary D2 receptors.",
                2,
                "Assertion true; reason false—cabergoline binds lactotroph D2 receptors to suppress PRL and shrink tumors.",
                ref(
                    "Prolactin-Secreting Adenomas",
                    "Oral administration of these drugs binds to lactotroph DA receptors to normalize PRL production and significantly reduce or shrink the prolactinoma mass.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Prolactinoma surgery",
                "Assertion: Transsphenoidal surgery may be indicated for DA-resistant prolactinoma.",
                "Reason: Surgery normalizes PRL in every macroprolactinoma regardless of size and invasion.",
                1,
                "Both true but reason overstates remission—macroprolactinoma surgical cure rates are lower than for microadenomas.",
                ref(
                    "Surgery",
                    "Results for macroprolactinoma resections are less favorable.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "NFA",
                "Assertion: Nonfunctioning pituitary adenomas are often diagnosed as incidentalomas.",
                "Reason: They lack clinical hormone hypersecretion syndromes and may be clinically silent until large.",
                0,
                "Both true—absence of hormonal phenotype delays detection until mass effects or incidental imaging.",
                ref(
                    "KEY POINTS",
                    "Nonfunctioning pituitary adenomas are usually of gonadotroph or null cell origin and usually present with compressive features or are diagnosed as incidentalomas.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Apoplexy",
                "Assertion: Pituitary apoplexy requires urgent evaluation for adrenal insufficiency.",
                "Reason: Acute adrenal insufficiency is frequent due to ACTH loss in apoplexy.",
                0,
                "Both true—ACTH loss commonly causes acute adrenal crisis needing corticosteroids.",
                ref(
                    "Clinical Features",
                    "Acute adrenal insufficiency is a frequent occurrence due to loss of ACTH.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Radiation",
                "Assertion: Pituitary irradiation is often adjuvant after incomplete surgery or persistent secretion.",
                "Reason: Radiation never causes hypopituitarism.",
                2,
                "Assertion true; reason false—hypopituitarism develops in most irradiated patients over time.",
                ref(
                    "Side Effects",
                    "Pituitary failure occurs commonly in patients who have received pituitary irradiation.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Acromegaly",
                "Assertion: Somatostatin receptor ligands are effective medical therapy for acromegaly.",
                "Reason: SRLs stimulate GH secretion from somatotroph adenomas.",
                2,
                "Assertion true; reason false—SRLs inhibit GH secretion via somatostatin receptors.",
                ref(
                    "SRLs",
                    "SRLs have been safely employed as approved drugs for acromegaly.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Acromegaly",
                "Assertion: Pegvisomant is useful when SRL therapy fails to control IGF-1.",
                "Reason: Pegvisomant antagonizes the GH receptor peripherally without targeting the adenoma.",
                0,
                "Both true—peripheral GH receptor blockade normalizes IGF-1 even when pituitary GH secretion persists.",
                ref(
                    "Growth Hormone Receptor Antagonist",
                    "The drug may be used as primary therapy monotherapy and is particularly useful in patients resistant to SRL therapy, because it effectively normalizes IGF1 levels in these patients.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Cushing disease",
                "Assertion: Bilateral inferior petrosal sinus sampling helps distinguish pituitary from ectopic ACTH secretion.",
                "Reason: A central-to-peripheral ACTH gradient supports a pituitary source.",
                0,
                "Both true—lateralizing or central gradients guide pituitary exploration versus ectopic workup.",
                ref(
                    "ACTH-Secreting Adenomas (Cushing Disease)",
                    "By contrast, if peripheral ACTH levels are similarly elevated as those of the cavernous sinus, the disease most probably is caused by ectopic ACTH production.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Pregnancy",
                "Assertion: Pituitary enlargement during pregnancy can mimic tumor growth on MRI.",
                "Reason: Lactotroph hyperplasia occurs physiologically during pregnancy.",
                0,
                "Both true—estrogen-driven lactotroph hyperplasia enlarges the gland and must be distinguished from prolactinoma.",
                ref(
                    "Approach to the Patient Harboring a Pituitary Mass",
                    "Lactotroph hyperplasia occurs during pregnancy, and thyrotroph, gonadotroph, or rarely corticotroph hyperplasias occur in the presence of long-standing primary thyroid, gonadal, or adrenal failure, respectively.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "7",
        "title": "Pituitary Adenomas and Masses",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Shlomo Melmed, Felipe F. Casanueva",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_07_Pituitary_Adenomas_and_Masses.md",
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
