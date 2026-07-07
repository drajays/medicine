#!/usr/bin/env python3
"""Generate Williams 15e module w15-22 — Normal and Aberrant Growth in Children."""
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
OUT_NAME = "w15-22_Normal_and_Aberrant_Growth_in_Children.json"


def build() -> dict:
    p = "w15-22"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why height is a vital sign in childhood",
                "Deviations from normal linear growth may be the first clue to endocrine or systemic disease; routine accurate height assessment is essential.",
                ref(
                    "KEY POINTS",
                    "Height is an important vital sign to obtain during childhood because deviations from the normal linear growth pattern may indicate an underlying disorder.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How to begin evaluating abnormal growth",
                "A thorough past medical, family, and social history with accurate growth velocity precedes labs and imaging to exclude occult systemic disease and hormonal disorders.",
                ref(
                    "KEY POINTS",
                    "A comprehensive past medical, family, and social history with assessment of an accurate growth velocity is required for the initial investigation of abnormal growth.",
                ),
            ),
            note(
                f"{p}-n3",
                "Growth Charts",
                "How height velocity flags pathology between ages 2 and puberty",
                "Between age 2 and puberty, a child typically tracks a growth channel; crossing percentile lines during this period is abnormal and warrants evaluation.",
                ref(
                    "Growth Charts",
                    "Any crossing of percentile curves on the height chart during this age period should be considered abnormal and warrants further evaluation.",
                ),
            ),
            note(
                f"{p}-n4",
                "Parental Target Height",
                "How to calculate midparental (genetic target) height",
                "Midparental height averages parental heights adjusted for the 13-cm sex difference: boys +6.5 cm, girls −6.5 cm; >95% of adults fall within 10 cm of the calculated target.",
                ref(
                    "Parental Target Height",
                    "In other words, a boy's midparental height equals the average of his parents' heights plus 6.5 cm, and a girl's midparental height equals the average of her parents' heights minus 6.5 cm.",
                ),
            ),
            note(
                f"{p}-n5",
                "KEY POINTS",
                "Why intact GHRH/GH/IGF-1 axis is required for normal growth",
                "Normal linear growth depends on an intact hypothalamic-pituitary-IGF-1 axis, adequate nutrition, and absence of significant systemic disease.",
                ref(
                    "KEY POINTS",
                    "An intact hypothalamic (growth hormone-releasing hormone [GHRH])/pituitary (growth hormone [GH])/insulin-like growth factor 1 (IGF1) axis, adequate nutrition, and absence of significant systemic disease are requirements for normal linear growth.",
                ),
            ),
            note(
                f"{p}-n6",
                "Growth Hormone-Releasing Hormone",
                "How GHRH generates pulsatile GH secretion",
                "Arcuate GHRH neurons are the main hypophysiotropic drive for pulsatile GH via GHRHR/cAMP signaling on somatotrophs; ARC ablation abolishes GH secretion.",
                ref(
                    "Growth Hormone-Releasing Hormone",
                    "GHRH is the main hypophysiotropic neuropeptide responsible for the generation and maintenance of pulsatile GH secretion.",
                ),
            ),
            note(
                f"{p}-n7",
                "Growth Hormone Pulsatility",
                "How somatostatin and GHRH shape GH pulses",
                "Pulsatile GH reflects the interplay of stimulatory GHRH and inhibitory somatostatin (SST); SST antagonizes GHRH and ghrelin at pituitary SST2/5 receptors.",
                ref(
                    "Somatostatin",
                    "SST inhibits GH release and antagonizes the stimulatory effects from GHRH or ghrelin.",
                ),
            ),
            note(
                f"{p}-n8",
                "Insulin-Like Growth Factor 1",
                "Why GH is the primary regulator of hepatic IGF-1",
                "GH drives a ~20-fold rise in Igf1 mRNA; STAT5B is the critical mediator of GH-induced IGF1 transcription, mediating many anabolic GH actions.",
                ref(
                    "Insulin-Like Growth Factor 1",
                    "GH is the primary regulator of Igf1 transcription, resulting in a 20-fold rise in Igf1 mRNA.",
                ),
            ),
            note(
                f"{p}-n9",
                "Constitutional Delay of Growth and Development",
                "How CDGD tracks on growth charts before puberty",
                "CDGD children often cross downward in infancy, then grow parallel to the ~5th percentile until a late pubertal spurt brings final height into the normal genetic range.",
                ref(
                    "Constitutional Delay of Growth and Development",
                    "After age 3 years, their growth rate is typically normal, so that their height growth usually remains parallel to the 5th percentile until adolescence, although the height SDS may gradually drift slightly lower during the middle childhood years in some cases.",
                ),
            ),
            note(
                f"{p}-n10",
                "Constitutional Delay of Growth and Development",
                "Why delayed bone age supports CDGD over pathologic short stature",
                "In CDGD, bone age is delayed—consistent with late puberty and late epiphyseal fusion—whereas intrinsic short-stature syndromes (e.g., Turner, familial short stature) usually have bone age appropriate for chronologic age.",
                ref(
                    "Screening Tests",
                    "In CDGD, the bone age is delayed, consistent with the future delay in puberty and late epiphyseal fusion.",
                ),
            ),
            note(
                f"{p}-n11",
                "Genetic Short Stature",
                "Familial short stature as a normal growth variant",
                "Genetic short stature (familial short stature) describes healthy children below the 3rd percentile whose height SDS lies within the midparental target range after regression-to-mean adjustment.",
                ref(
                    "Genetic Short Stature",
                    "Genetic short stature (GSS), also called familial short stature, is a normal growth pattern that describes the growth of healthy individuals who fall at the lower extreme of the distribution of height (i.e., below the 3rd percentile).",
                ),
            ),
            note(
                f"{p}-n12",
                "Growth Hormone Deficiency",
                "How congenital GHD appears on pituitary MRI",
                "Early-diagnosed congenital GHD often shows pituitary stalk dysgenesis, ectopic posterior pituitary, and anterior pituitary hypoplasia—more severe with combined pituitary hormone deficiency.",
                ref(
                    "The Hypothalamus",
                    "As noted earlier, patients with early-diagnosed congenital GHD frequently have an abnormal pituitary stalk, ectopia of the posterior pituitary, and hypoplasia of the anterior pituitary (Fig. 22.34).",
                ),
            ),
            note(
                f"{p}-n13",
                "Turner Syndrome",
                "Why Turner girls need syndrome-specific growth charts",
                "Short stature affects 95–100% of 45,X girls; plotting on Turner-specific curves detects deviation suggesting a second cause (e.g., acquired hypothyroidism).",
                ref(
                    "Turner Syndrome",
                    "Short stature occurs in 95% to 100% of girls with a 45,X karyotype.",
                ),
            ),
            note(
                f"{p}-n14",
                "Osteochondrodysplasias",
                "How achondroplasia presents beyond short stature",
                "Achondroplasia (FGFR3 activating mutations, often de novo) causes rhizomelia, macrocephaly, lumbar stenosis risk, and mean adult heights ~130 cm (males) and ~120 cm (females); GH secretion is normal.",
                ref(
                    "Osteochondrodysplasias",
                    "Achondroplasia is the most common of the osteochondrodysplasias, with a frequency of 1 in 26,000 individuals.",
                ),
            ),
            note(
                f"{p}-n15",
                "Gonadal Steroids",
                "Why estrogen terminates long-bone growth",
                "Estrogen accelerates growth-plate senescence and epiphyseal fusion; estrogen-receptor or aromatase mutations cause tall stature with open epiphyses.",
                ref(
                    "Gonadal Steroids",
                    "Both androgens and estrogens increase skeletal maturation and accelerate growth plate senescence.",
                ),
            ),
            note(
                f"{p}-n16",
                "Treatment of Growth Hormone Deficiency",
                "How to dose daily GH in childhood GHD",
                "Start 0.16–0.24 mg/kg/week in seven daily subcutaneous doses; daily administration outperforms thrice-weekly dosing at the same weekly total.",
                ref(
                    "Treatment Regimens for Daily GH in GHD",
                    "The recommended therapeutic starting dose of daily GH in children with GHD is 0.16 to 0.24 mg/kg BW per week, administered in seven daily doses.",
                ),
            ),
            note(
                f"{p}-n17",
                "Treatment of Constitutional Delay",
                "How oxandrolone is used in CDGD boys",
                "Oxandrolone 0.05–0.1 mg/kg/day accelerates growth velocity in prepubertal boys with CDGD but does not increase final adult height.",
                ref(
                    "Treatment of Constitutional Delay",
                    "Currently recommended treatment is 0.05 to 0.1 mg/kg orally per day.",
                ),
            ),
            note(
                f"{p}-n18",
                "Growth Hormone Insensitivity",
                "Laron syndrome (primary IGF-1 deficiency) phenotype",
                "Classic GH insensitivity: growth failure from birth, −4 to −10 SD stature, low IGF-1, elevated GH, undetectable GHBP, and no response to exogenous GH.",
                ref(
                    "Growth Hormone Insensitivity",
                    "GH insensitivity, also known as primary IGF1 deficiency, encompasses a variety of genetic conditions characterized by growth failure, high serum GH levels, and very low serum IGF1 levels.",
                ),
            ),
            note(
                f"{p}-n19",
                "Normal Growth",
                "Why growth deviation may signal multisystem disease",
                "Even though growth is multifactorial, children usually follow predictable channels; deviation can be the first manifestation of endocrine or nonendocrine disorders involving virtually any organ system.",
                ref(
                    "Normal Growth",
                    "Deviation from such a normal pattern of growth can be the first manifestation of a wide variety of disease processes, including endocrine and nonendocrine disorders and involving virtually any organ system.",
                ),
            ),
            note(
                f"{p}-n20",
                "Body Proportions",
                "How to assess disproportionate short stature",
                "Measure occipitofrontal circumference, sitting height, lower body segment, and arm span; upper:lower segment ratio falls from ~1.7 in neonates to <1.0 in adults.",
                ref(
                    "Body Proportions",
                    "The following determinations should be made as part of the evaluation of short stature:",
                ),
            ),
            note(
                f"{p}-n21",
                "Skeletal Maturation",
                "How bone age estimates remaining growth opportunity",
                "Bone age mirrors somatic maturation tempo and growth-plate senescence; it helps estimate growth opportunity and adult height when interpreted with chronologic age.",
                ref(
                    "Skeletal Maturation",
                    "The bone age also reflects the degree of growth plate senescence and is therefore a useful adjunct in estimating growth opportunity (i.e., the ultimate adult height), as discussed later in this chapter.",
                ),
            ),
            note(
                f"{p}-n22",
                "Phases of Normal Growth",
                "Karlberg three-phase model of linear growth",
                "Normal growth resolves into infancy (rapid deceleration), childhood (slow deceleration), and pubertal (sigmoid spurt) phases that partially overlap.",
                ref(
                    "Phases of Normal Growth",
                    "Karlberg and associates resolved the normal linear growth curve into three additive, partially superimposable phases: an \"infancy\" phase, starting in midgestation and then rapidly decelerating until about 3 to 4 years of age; a \"childhood\" phase, of slowly decelerating growth through early adolescence; and a sigmoid-shaped \"puberty\" phase that comprises the adolescent growth spurt.",
                ),
            ),
            note(
                f"{p}-n23",
                "Turner Syndrome",
                "Why GH therapy is standard in Turner syndrome",
                "Turner girls have normal childhood GH/IGF-1; multiple studies show GH accelerates short-term growth and increases final adult height despite SHOX haploinsufficiency.",
                ref(
                    "Turner Syndrome",
                    "Multiple studies have shown that GH therapy is capable of accelerating short-term growth and increasing final adult height.",
                ),
            ),
            note(
                f"{p}-n24",
                "Tall Stature",
                "Familial tall stature and upper-normal GH-IGF-1",
                "In familial tall stature, GH and IGF-1/IGFBP3 are often upper-normal; subsets have high GH pulse amplitude with higher IGF-1 versus lower-secretors.",
                ref(
                    "Tall Stature",
                    "GH secretion and levels of IGF1 and IGFBP3 in familial tall stature are often in the upper-normal range.",
                ),
            ),
            note(
                f"{p}-n25",
                "Adverse Effects of Growth Hormone",
                "Why GH recipients need structured safety monitoring",
                "Recombinant GH lacks CJD risk but requires vigilance for pseudotumor cerebri, slipped capital femoral epiphysis, glucose intolerance, and scoliosis progression—large postmarketing registries guide surveillance.",
                ref(
                    "Adverse Effects of Growth Hormone",
                    "Extensive experience with recombinant GH over nearly 30 years has been encouraging.",
                ),
            ),
            note(
                f"{p}-n26",
                "Idiopathic Short Stature",
                "Why ISS is a heterogeneous diagnostic bucket",
                "ISS includes constitutional delay, familial short stature, and subtle GH-IGF axis or growth-plate defects not captured by current testing—distinction from partial GHD is partly arbitrary.",
                ref(
                    "Idiopathic Short Stature",
                    "ISS is defined as \"a condition in which the height of the individual is more than 2 SD below the corresponding mean height for a given age, sex and population group, and in whom no identifiable disorder is present.\"",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Clinical Evaluation of Growth Retardation",
                "A 7-year-old tracks just below the 3rd percentile with height velocity consistently at the 30th percentile. Midparental height is on the 10th percentile. Best next step?",
                [
                    "Reassurance with continued serial heights—velocity is adequate for current percentile",
                    "Immediate GH stimulation testing",
                    "Start recombinant GH without labs",
                    "Bone marrow biopsy",
                ],
                0,
                "A short child maintaining appropriate velocity for their channel may have familial short stature; isolated low GH stimulation in this context is often a false positive.",
                ref(
                    "Tests of the GH-IGF1 Axis",
                    "For example, a child growing consistently just below the 3rd percentile for height, with a growth rate that is accordingly above the 25th percentile for age, is very unlikely to be GH deficient.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Constitutional Delay of Growth and Development",
                "A 13-year-old boy is 5th percentile for height, bone age 11 years, prepubertal, and father had late puberty. Most likely diagnosis?",
                [
                    "Constitutional delay of growth and development",
                    "Cushing syndrome",
                    "Primary hypothyroidism",
                    "Achondroplasia",
                ],
                0,
                "CDGD: normal birth size, delayed bone age, parallel growth below genetic expectation, family history of late puberty, and eventual normal adult height.",
                ref(
                    "Constitutional Delay of Growth and Development",
                    "CDGD is a normal variant of growth. It describes the growth pattern of children who will experience a later than average timing of puberty.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Growth Hormone Deficiency",
                "A 4-year-old with height −3.5 SDS has low IGF-1, failed GH stimulation, and MRI showing ectopic posterior pituitary and absent stalk. Next priority?",
                [
                    "Evaluate for additional pituitary hormone deficiencies and initiate GH replacement",
                    "Observe without treatment until adolescence",
                    "IGF-1 therapy as first-line",
                    "Thyroidectomy",
                ],
                0,
                "Structural congenital GHD warrants full hypopituitarism workup (ACTH, TSH, ADH) and GH therapy; ectopic neurohypophysis/stalk agenesis is classic.",
                ref(
                    "The Hypothalamus",
                    "In a number of reports, idiopathic GHD is associated with magnetic resonance imaging (MRI) findings of an ectopic neurohypophysis, pituitary stalk dysgenesis, and hypoplasia or aplasia of the anterior pituitary.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Turner Syndrome",
                "A 9-year-old girl with short stature, cubitus valgus, and widely spaced nipples has normal GH stimulation. Best growth management?",
                [
                    "Recombinant GH without requiring failed GH stimulation",
                    "Withhold GH because stimulation test is normal",
                    "High-dose estrogen to close growth plates immediately",
                    "No follow-up—Turner stature is untreatable",
                ],
                0,
                "Turner syndrome: GH secretion is typically normal; GH therapy improves growth velocity and final height—use Turner-specific growth charts.",
                ref(
                    "Turner Syndrome",
                    "Girls with TS have normal GH and IGF levels during childhood; reports of low levels of GH or IGF, or both, in adolescents are likely due to low serum levels of gonadal steroids.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Osteochondrodysplasias",
                "A 3-year-old with rhizomelia, frontal bossing, and lumbar stenosis symptoms has disproportionate short stature and normal GH axis. Diagnosis?",
                [
                    "Achondroplasia (FGFR3 mutation)",
                    "Isolated GH deficiency",
                    "Constitutional delay",
                    "Marfan syndrome",
                ],
                0,
                "Achondroplasia: rhizomelic shortening, macrocephaly, FGFR3 gain-of-function; GH levels are normal and GH therapy does not correct the skeletal dysplasia.",
                ref(
                    "Osteochondrodysplasias",
                    "Characteristic abnormalities of the skeleton include megalocephaly, low nasal bridge, lumbar lordosis, short trident hand, and rhizomelia (shortness of the proximal legs and arms) with skin redundancy.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Growth Charts",
                "A healthy 8-year-old has crossed from the 50th to the 25th percentile over 18 months with weight stable. Most appropriate action?",
                [
                    "Evaluate for pathologic growth failure—percentile crossing between 2 years and puberty is abnormal",
                    "Reassure—any single percentile change is normal",
                    "Start GH empirically",
                    "Ignore until age 16",
                ],
                0,
                "Between age 2 and puberty, children should track a channel; downward crossing of height percentiles warrants evaluation even if absolute height remains 'normal.'",
                ref(
                    "Growth Charts",
                    "Any crossing of percentile curves on the height chart during this age period should be considered abnormal and warrants further evaluation.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Tests of the GH-IGF1 Axis",
                "A 10-year-old with suspected GHD has low IGF-1 but recent poor oral intake for 5 days. Best interpretation?",
                [
                    "Repeat IGF-1 after nutritional recovery—short-term caloric deficit lowers IGF-1",
                    "Diagnose GHD and start GH immediately",
                    "IGF-1 is unaffected by nutrition",
                    "Proceed to cranial irradiation",
                ],
                0,
                "IGF-1 is nutrition-dependent; even brief decreased intake lowers levels and reduces specificity for GHD.",
                ref(
                    "Insulin-Like Growth Factor 1",
                    "Even a few days of decreased caloric intake can lower IGF1 levels.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Growth Hormone Insensitivity",
                "A child with −6 SDS height, elevated GH, undetectable IGF-1 and GHBP, and no growth response to GH most likely has:",
                [
                    "Growth hormone receptor defect (Laron syndrome)",
                    "Constitutional delay",
                    "Hyperthyroidism",
                    "Familial tall stature",
                ],
                0,
                "Classic GH insensitivity: high GH, very low IGF-1, absent GHBP, and failure to respond to exogenous GH—treat with recombinant IGF-1.",
                ref(
                    "Growth Hormone Insensitivity",
                    "Individuals do not respond to exogenous GH, as determined by growth velocity, hypoglycemia incidence, or serum IGF1 or IGFBP1 levels.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Tall Stature",
                "A 17-year-old man is 195 cm tall with open epiphyses, eunuchoid proportions, and low estradiol. Most likely mechanism?",
                [
                    "Estrogen deficiency preventing epiphyseal fusion",
                    "GH deficiency",
                    "Turner syndrome",
                    "Achondroplasia",
                ],
                0,
                "Estrogen is primarily responsible for epiphyseal fusion; aromatase or estrogen-receptor defects cause sustained growth and tall eunuchoid habitus.",
                ref(
                    "Tall Stature",
                    "Failure to enter puberty and complete sexual maturation may result in sustained growth during adult life, with ultimate tall stature and a characteristic eunuchoid habitus.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Treatment of Growth Hormone Deficiency",
                "A newly diagnosed GHD child is started on GH 0.20 mg/kg/week given thrice weekly. Growth response is suboptimal. Best adjustment?",
                [
                    "Switch to daily divided dosing at the same weekly total dose",
                    "Stop GH permanently",
                    "Double dose but keep thrice-weekly schedule",
                    "Replace with testosterone",
                ],
                0,
                "Daily GH administration produces substantially greater height gain than thrice-weekly injections at identical weekly dosage.",
                ref(
                    "Treatment Regimens for Daily GH in GHD",
                    "Alternative regimens include a 6-day/week and a 3-day/week schedule, with the same weekly dosage, but the 3-day/week schedule is not as successful.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Treatment of Constitutional Delay",
                "Parents ask whether oxandrolone will help their 12-year-old CDGD son reach his father's height. Best counseling?",
                [
                    "Oxandrolone may accelerate growth velocity but does not increase final adult height",
                    "Oxandrolone reliably adds 15 cm to final height",
                    "Oxandrolone is contraindicated in all short boys",
                    "Oxandrolone permanently advances bone age without growth benefit",
                ],
                0,
                "Oxandrolone increases linear growth velocity in CDGD but does not improve predicted or actual final height.",
                ref(
                    "Treatment of Constitutional Delay",
                    "(This treatment does not increase the final height of these boys.)",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Genetic Short Stature",
                "A 6-year-old girl is 3rd percentile for height; both parents are short (mother 148 cm, father 163 cm); bone age matches chronologic age; exam normal. Diagnosis?",
                [
                    "Familial (genetic) short stature",
                    "GH deficiency",
                    "Celiac disease until proven otherwise",
                    "Turner syndrome without stigmata",
                ],
                0,
                "Height appropriate for midparental target with normal bone age and no disproportion suggests familial short stature—a normal variant.",
                ref(
                    "Genetic Short Stature",
                    "Their height is appropriate for their genetic potential based on the parents' heights; that is, their height SDS is within the target height SDS range.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Malnutrition",
                "A refugee child has height −2.5 SDS, weight −3 SDS, elevated GH, and low IGF-1. Mechanism?",
                [
                    "Nutritional GH resistance with low IGF-1 despite high GH",
                    "Primary pituitary GH deficiency",
                    "Excess IGF-1 production",
                    "Estrogen excess",
                ],
                0,
                "Malnutrition causes GH resistance: high GH, low IGF-1 and GHBP—an adaptive diversion of energy from growth.",
                ref(
                    "Malnutrition",
                    "With serum IGF1 levels reduced despite normal or elevated GH levels, malnutrition is a form of GH insensitivity.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Septo-Optic Dysplasia",
                "A newborn with nystagmus and midline brain defects has growth failure. Highest-yield evaluation?",
                [
                    "MRI brain/pituitary and full pituitary hormone panel including GH axis",
                    "Growth chart only—no labs until age 10",
                    "Karyotype expecting 47,XXY",
                    "Renal biopsy",
                ],
                0,
                "Septo-optic dysplasia combines optic hypoplasia, midline defects, and hypopituitarism—screen any infant with congenital blindness/nystagmus for hypopituitarism.",
                ref(
                    "Terminal Cell Differentiation in the Pituitary",
                    "For this reason, children with congenital blindness or nystagmus should be monitored for hypopituitarism.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Obesity",
                "An obese 10-year-old has rapid linear growth and advanced bone age but parents worry about 'short stature' because he is below midparental target. Best approach?",
                [
                    "Recognize obesity-associated rapid growth; short obese child needs pathology search",
                    "Diagnose GH deficiency by definition",
                    "Start GH for all obese children",
                    "Ignore bone age",
                ],
                0,
                "Obesity accelerates growth and bone age; an obese child who is short despite this pattern warrants evaluation for hypothyroidism, GHD, Cushing, or Prader-Willi.",
                ref(
                    "Obesity",
                    "This association between obesity and rapid growth is so characteristic that a child with obesity and short stature should always be evaluated for underlying pathology, such as hypothyroidism, GHD, Cushing syndrome, or PWS.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Growth Hormone Secretion in Humans",
                "During normal puberty, the rise in circulating GH is driven mainly by:",
                [
                    "Increased GH mass per secretory burst (pulse amplitude), not pulse frequency",
                    "Doubling of GH pulse frequency only",
                    "Complete loss of GH pulsatility",
                    "Placental GH-V secretion",
                ],
                0,
                "Pubertal GH increase reflects greater amount of GH per pulse; greater irregularity correlates with greater linear growth.",
                ref(
                    "Growth Hormone Secretion in Humans",
                    "The increase in GH production during middle to late puberty is caused by enhanced pulse amplitude and increased mass of GH per secretory burst, rather than by a change in pulse frequency (Figs. 22.17 and 22.18).",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Turner Syndrome",
                "A girl with Turner syndrome on GH develops progressive hearing loss and new thyroid antibodies. Most likely added diagnosis?",
                [
                    "Autoimmune hypothyroidism—common comorbidity requiring treatment",
                    "GH-induced leukemia",
                    "Pituitary adenoma from GH",
                    "No action—expected Turner course",
                ],
                0,
                "Deviation from Turner-specific growth curves should prompt search for second causes; autoimmune hypothyroidism is common in TS and Down syndrome.",
                ref(
                    "Growth Charts",
                    "Deviation of growth from the appropriate disease-related growth curve suggests the possibility of a second underlying cause, such as acquired autoimmune hypothyroidism in children with Down syndrome or TS.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Small for Gestational Age",
                "A 4-year-old born SGA remains −2.5 SDS without catch-up. GH therapy consideration requires:",
                [
                    "Documented growth failure persisting after age 2–4 years with failed catch-up",
                    "SGA diagnosis alone at birth regardless of current growth",
                    "Normal height velocity on 90th percentile",
                    "Confirmed GH receptor mutation first",
                ],
                0,
                "Most SGA infants catch up by age 2; persistent short stature in ~10–15% may warrant GH after documenting continued growth failure.",
                ref(
                    "Small for Gestational Age",
                    "However, up to 10% of SGA infants do not show such catch-up growth.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Tumors",
                "A 14-year-old boy has rapid height gain (>8 cm/year), headaches, and enlarged hands. Best initial test?",
                [
                    "IGF-1 level and pituitary MRI for GH-secreting adenoma",
                    "Bone age only",
                    "Constitutional delay reassurance",
                    "Thyroidectomy",
                ],
                0,
                "Pre-fusion GH excess causes pituitary gigantism—evaluate IGF-1 and imaging; also consider McCune-Albright or MEN in appropriate contexts.",
                ref(
                    "Tumors",
                    "GH excess that occurs before epiphyseal fusion results in rapid growth and attainment of adult heights above expected adult potential.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Treatment of Growth Hormone Deficiency",
                "A GH-treated GHD child has poor first-year growth despite good compliance. Before increasing dose, check:",
                [
                    "Undiagnosed hypothyroidism unmasked by GH therapy",
                    "Serum sodium only",
                    "Bone marrow aspirate",
                    "Discontinue GH for 2 years",
                ],
                0,
                "GH therapy unmasks central hypothyroidism; TSH deficiency may appear in first 3 months—annual thyroid monitoring is required.",
                ref(
                    "Combined Pituitary Hormone Deficiencies",
                    "TSH deficiency is often \"unmasked\" during the initial phase of therapy, and thyroid function should be assessed before the onset of therapy during the first 3 months of GH treatment and at least on an annual basis thereafter.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Screening Tests",
                "Bone age 9 years in a 12-year-old with short stature most strongly suggests:",
                [
                    "Delayed skeletal maturation seen in CDGD, hypothyroidism, or GHD",
                    "Intrinsic skeletal dysplasia like Turner syndrome",
                    "Familial short stature with normal bone age",
                    "Precocious puberty",
                ],
                0,
                "Delayed bone age accompanies CDGD, hypothyroidism, and GHD; Turner/familial short stature typically have bone age matching chronologic age.",
                ref(
                    "Screening Tests",
                    "Similarly, hypothyroidism and GHD are associated with a delayed bone age.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Adverse Effects of Growth Hormone",
                "A GH-treated child develops headache and papilledema 3 months after starting therapy. First step?",
                [
                    "Evaluate for pseudotumor cerebri—may require GH dose reduction or pause",
                    "Continue GH and add aspirin only",
                    "Emergency craniotomy",
                    "Ignore if blood pressure normal",
                ],
                0,
                "Pseudotumor cerebri is reported with GH—especially in renal failure; assess for headache, visual changes; may need dose adjustment.",
                ref(
                    "Adverse Effects of Growth Hormone",
                    "Pseudotumor cerebri (idiopathic intracranial hypertension) has been reported in GH-treated patients.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Measurement",
                "When calculating height velocity for a short child, minimum interval between measurements should be:",
                [
                    "At least 6 months (9–12 months preferred)",
                    "2 weeks",
                    "1 day",
                    "5 years",
                ],
                0,
                "Height velocity needs ≥6 months between measurements to minimize measurement error and seasonal variation.",
                ref(
                    "Measurement",
                    "Even when every effort is made to obtain accurate height measurements, a minimum interval of 6 months is necessary for meaningful height velocity computation.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Idiopathic Short Stature",
                "A child meets ISS criteria with normal GH stimulation and normal IGF-1. Before labeling idiopathic, you should:",
                [
                    "Exclude subtle GH resistance, SHOX defects, and NPR2 variants among other causes",
                    "Assume no further testing is ever needed",
                    "Diagnose acromegaly",
                    "Start IGF-1 without workup",
                ],
                0,
                "ISS is heterogeneous—partial GH insensitivity, GHR heterozygosity, SHOX/NPR2 mutations may be missed on standard testing.",
                ref(
                    "Idiopathic Short Stature",
                    "Heterozygous mutations in the GHR have been found in significant numbers of children with ISS.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Treatment of Constitutional Delay",
                "A 15-year-old CDGD boy received brief testosterone injections and now has pubertal testosterone but testes remain prepubertal. Next step?",
                [
                    "Evaluate for hypogonadotropic hypogonadism—CDGD should progress to true puberty",
                    "Repeat testosterone indefinitely",
                    "Diagnose constitutional delay confirmed—no follow-up",
                    "Start estrogen",
                ],
                0,
                "After short testosterone course, testicular enlargement and pubertal testosterone should follow; failure suggests hypothalamic-pituitary insufficiency.",
                ref(
                    "Treatment of Constitutional Delay",
                    "One year after testosterone treatment, boys should have testicular enlargement and a serum testosterone level in the pubertal range.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Growth Charts",
                "For children under 2 years, which growth standard is preferred for length monitoring per Williams?",
                [
                    "WHO growth charts (especially for weight/length under 2 years)",
                    "Adult BMI charts",
                    "Syndrome-specific Turner charts only",
                    "No charts—percentiles invalid under age 2",
                ],
                0,
                "WHO curves (1997–2003) are recommended under age 2; CDC weight curves may overestimate optimal gain.",
                ref(
                    "Growth Charts",
                    "Growth charts based on the World Health Organization (WHO) data gathered from 1997 throughout 2003 should be used to monitor the growth of children under 2 years of age.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "KEY POINTS",
                "Treating the underlying disorder or hormone deficiency can improve linear growth.",
                True,
                "Correcting the primary cause restores growth when the growth plates remain open.",
                ref(
                    "KEY POINTS",
                    "Successful treatment of the underlying disorder or correction of hormone deficiency(ies) improves linear growth.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Growth Hormone-Releasing Hormone",
                "GHRH is secreted from the arcuate nucleus and drives pulsatile GH secretion.",
                True,
                "Arcuate GHRH neurons are the principal hypothalamic stimulus for somatotroph GH release.",
                ref(
                    "Growth Hormone-Releasing Hormone",
                    "Growth hormone-releasing hormone (GHRH) is a 44-amino acid peptide hormone secreted by neurons located in the arcuate nucleus (ARC) of the hypothalamus.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Constitutional Delay of Growth and Development",
                "Children with CDGD usually have a final adult height well above their genetic target.",
                False,
                "Final height is often in the lower part of the parental target range; few exceed parental target.",
                ref(
                    "Constitutional Delay of Growth and Development",
                    "Final height is often in the lower part of the parental target height range, and few patients exceed the parental target height, although this finding is probably at least in part the result of a selection bias of the children examined for such studies.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Turner Syndrome",
                "Most girls with Turner syndrome have normal GH and IGF-1 levels during childhood.",
                True,
                "Short stature in TS is not from classic GHD; low GH/IGF in adolescence often reflects gonadal steroid deficiency.",
                ref(
                    "Turner Syndrome",
                    "Girls with TS have normal GH and IGF levels during childhood; reports of low levels of GH or IGF, or both, in adolescents are likely due to low serum levels of gonadal steroids.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Osteochondrodysplasias",
                "Achondroplasia is caused by inactivating mutations in FGFR3.",
                False,
                "Achondroplasia results from activating FGFR3 mutations (often de novo at nucleotide 1138) that impair endochondral ossification.",
                ref(
                    "Osteochondrodysplasias",
                    "Achondroplasia is caused by mutations in the transmembrane domain of the FGF receptor 3 gene (FGFR3).",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Treatment of Constitutional Delay",
                "Recombinant GH is required for children with CDGD to reach a normal adult height.",
                False,
                "CDGD final height is expected in the normal range without GH; diagnosis cannot be confirmed until late puberty.",
                ref(
                    "Treatment of Constitutional Delay",
                    "The final height of a child with CDGD will be in the normal range and appropriate for the child's genetic potential. No treatment is needed for these children to achieve a normal height.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Growth Hormone Insensitivity",
                "Patients with classic GH insensitivity respond to standard doses of exogenous GH with increased growth velocity.",
                False,
                "Laron syndrome patients do not respond to GH; treatment is recombinant IGF-1.",
                ref(
                    "Growth Hormone Insensitivity",
                    "Individuals do not respond to exogenous GH, as determined by growth velocity, hypoglycemia incidence, or serum IGF1 or IGFBP1 levels.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Tall Stature",
                "Estrogen is primarily responsible for epiphyseal fusion in humans.",
                True,
                "Estrogen receptor and aromatase mutations cause tall stature with open epiphyses despite androgen exposure.",
                ref(
                    "Skeletal Maturation",
                    "studies in patients with mutations of the gene for the estrogen receptor or for the aromatase enzyme demonstrated that estrogen is primarily responsible for epiphyseal fusion.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Tests of the GH-IGF1 Axis",
                "A single provocative GH test provides a definitive gold-standard diagnosis of GHD.",
                False,
                "No test is definitive; provocative tests have limited specificity and must be interpreted with clinical context.",
                ref(
                    "Tests of the GH-IGF1 Axis",
                    "There is no test that definitively diagnoses GHD. Because there is no gold standard, it is impossible to precisely define the sensitivity or specificity of any test for GHD.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Malnutrition",
                "Malnutrition typically causes low GH and high IGF-1 levels.",
                False,
                "Malnutrition produces elevated GH with low IGF-1—nutritional GH resistance.",
                ref(
                    "Malnutrition",
                    "The impaired growth seen in malnutrition is usually associated with elevated basal or stimulated serum GH levels with reduced IGF1 levels.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Adverse Effects of Growth Hormone",
                "Recombinant GH carries the same Creutzfeldt-Jakob disease risk as pituitary-derived GH.",
                False,
                "CJD was linked to pituitary-derived GH; recombinant GH does not carry that prion transmission risk.",
                ref(
                    "Adverse Effects of Growth Hormone",
                    "Although recombinant DNA-derived GH does not carry this risk, the experience with pit-GH serves as a grim reminder of the potential toxicity that can reside in products used for physiologic replacement.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Genetic Short Stature",
                "In familial short stature, bone age is typically delayed relative to chronologic age.",
                False,
                "Familial short stature has bone age within normal range for chronologic age, unlike CDGD or GHD.",
                ref(
                    "Screening Tests",
                    "If short stature is intrinsic to the condition, however, bone age is not delayed and is within the range of normal for the chronologic age. This is true for genetic disorders such as TS, Noonan syndrome, and RSS and also for familial short stature.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Treatment of Growth Hormone Deficiency",
                "Daily GH dosing produces greater height gain than thrice-weekly dosing at the same weekly total dose.",
                True,
                "Randomized data show ~9.7 cm greater 4-year height gain with daily vs thrice-weekly administration.",
                ref(
                    "Treatment Regimens for Daily GH in GHD",
                    "The mean total height gain during this period was 9.7 cm greater in the patients treated daily (38.4 vs. 28.7 cm, p < 0.0002), with similar increments in skeletal maturation and no",
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
                "Assertion: Growth-promoting agents may improve linear growth in select patients with intact GHRH/GH/IGF1 axis function.",
                "Reason: GH therapy is ineffective whenever any component of the GH-IGF axis is intact.",
                2,
                "Assertion true; reason false—intact axis function is a prerequisite for responsiveness, not a contraindication.",
                ref(
                    "KEY POINTS",
                    "Treatment of short stature with growth-promoting agents may improve linear growth in select patients with intact GHRH/GH/IGF1 axis function.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Insulin-Like Growth Factor 1",
                "Assertion: Pubertal IGF-1 levels rise to two to three times the adult range.",
                "Reason: Pubertal IGF-1 rise is unrelated to gonadal steroids or GH secretion.",
                2,
                "Assertion true; reason false—pubertal rise reflects augmented GH pulses and direct gonadal steroid effects on hepatic IGF-1.",
                ref(
                    "Insulin-Like Growth Factor 1",
                    "During puberty, IGF1 levels rise to two to three times the adult range.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Constitutional Delay of Growth and Development",
                "Assertion: CDGD is a normal growth variant with delayed puberty and normal final height.",
                "Reason: All children with CDGD require lifelong GH replacement to reach normal adult height.",
                2,
                "Assertion true; reason false—CDGD achieves normal height without GH in most cases.",
                ref(
                    "Constitutional Delay of Growth and Development",
                    "CDGD is a normal variant of growth. It describes the growth pattern of children who will experience a later than average timing of puberty.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Turner Syndrome",
                "Assertion: Turner syndrome is the most common feature of short stature in affected girls.",
                "Reason: Turner girls typically have severe GH deficiency causing their height deficit.",
                2,
                "Assertion true (short stature is nearly universal); reason false—childhood GH/IGF-1 are usually normal.",
                ref(
                    "Turner Syndrome",
                    "In girls with TS, short stature is the single most common feature, occurring more frequently than delayed puberty, cubitus valgus, or webbing of the neck.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Growth Hormone Deficiency",
                "Assertion: Idiopathic GHD is often associated with ectopic posterior pituitary on MRI.",
                "Reason: All children with short stature have ectopic posterior pituitary.",
                2,
                "Assertion true for many congenital GHD cases; reason false—ectopic PP is not universal in all short children.",
                ref(
                    "The Hypothalamus",
                    "In a number of reports, idiopathic GHD is associated with magnetic resonance imaging (MRI) findings of an ectopic neurohypophysis, pituitary stalk dysgenesis, and hypoplasia or aplasia of the anterior pituitary.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Osteochondrodysplasias",
                "Assertion: Achondroplasia is the most common osteochondrodysplasia.",
                "Reason: Achondroplasia results from loss-of-function mutations that abolish FGFR3 signaling.",
                2,
                "Assertion true; reason false—achondroplasia involves FGFR3 gain-of-function/activation mutations.",
                ref(
                    "Osteochondrodysplasias",
                    "Achondroplasia is the most common of the osteochondrodysplasias, with a frequency of 1 in 26,000 individuals.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Tall Stature",
                "Assertion: Estrogen receptor mutations can cause tall stature with open epiphyses.",
                "Reason: Estrogen has no role in growth plate fusion.",
                2,
                "Assertion true; reason false—estrogen is primarily responsible for epiphyseal fusion.",
                ref(
                    "Gonadal Steroids",
                    "A mutation of the estrogen receptor was found in a man with tall stature and open epiphyses;",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Treatment of Growth Hormone Deficiency",
                "Assertion: Younger age at GH initiation correlates with better adult height outcomes in GHD.",
                "Reason: GH has no effect on growth in prepubertal children.",
                2,
                "Assertion true; reason false—GH markedly accelerates growth in prepubertal GHD, especially when started young.",
                ref(
                    "Adult Height Outcomes",
                    "Factors that have been found to correlate with enhanced adult height in GH-treated, GH-deficient children include baseline height, younger age at onset of treatment, longer treatment duration (especially during prepubertal years), and a greater growth velocity during the first year of treatment (Figs. 22.48 and 22.49).",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Growth Hormone Insensitivity",
                "Assertion: Classic GH insensitivity features elevated GH and very low IGF-1.",
                "Reason: GH insensitivity is defined by high IGF-1 and low GH levels.",
                2,
                "Assertion true; reason false—the hallmark is high GH with low IGF-1 (primary IGF-1 deficiency).",
                ref(
                    "Growth Hormone Insensitivity",
                    "GH insensitivity, also known as primary IGF1 deficiency, encompasses a variety of genetic conditions characterized by growth failure, high serum GH levels, and very low serum IGF1 levels.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Malnutrition",
                "Assertion: Malnutrition causes GH resistance with low IGF-1 despite elevated GH.",
                "Reason: Malnutrition suppresses both GH secretion and IGF-1 production equally.",
                2,
                "Assertion true; reason false—GH is elevated while IGF-1 is reduced in malnutrition.",
                ref(
                    "Malnutrition",
                    "With serum IGF1 levels reduced despite normal or elevated GH levels, malnutrition is a form of GH insensitivity.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Screening Tests",
                "Assertion: In Turner syndrome, bone age is typically not delayed relative to chronologic age.",
                "Reason: Turner syndrome always causes markedly delayed bone age.",
                2,
                "Assertion true for intrinsic short stature syndromes; reason false—TS bone age is usually normal for age (delayed bone age suggests another disorder).",
                ref(
                    "Screening Tests",
                    "If short stature is intrinsic to the condition, however, bone age is not delayed and is within the range of normal for the chronologic age. This is true for genetic disorders such as TS, Noonan syndrome, and RSS and also for familial short stature.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Treatment of Constitutional Delay",
                "Assertion: Brief testosterone therapy in adolescent CDGD boys can induce early virilization without compromising final height.",
                "Reason: Testosterone always causes rapid skeletal maturation that invariably reduces adult height in CDGD.",
                2,
                "Assertion true per short-course protocols; reason false—brief regimens do not overly accelerate bone age or reduce final height.",
                ref(
                    "Treatment of Constitutional Delay",
                    "Brief testosterone regimens do not cause overly rapid skeletal maturation, compromise adult height, or suppress pubertal maturation.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "22",
        "title": "Normal and Aberrant Growth in Children",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Sara A. Divall and Sally Radovick",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_22_Normal_and_Aberrant_Growth_in_Children.md",
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
