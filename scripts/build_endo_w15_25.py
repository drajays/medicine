#!/usr/bin/env python3
"""Generate Williams 15e module w15-25 — Hormones and Athletic Performance."""
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
OUT_NAME = "w15-25_Hormones_and_Athletic_Performance.json"


def build() -> dict:
    p = "w15-25"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why physical activity modulates the endocrine system",
                "Exercise influences synthesis and secretion of multiple hormones; almost every organ and system is affected mainly through endocrine and neuroendocrine pathways.",
                ref(
                    "KEY POINTS",
                    "Physical activity exerts an important influence on the endocrine system, modulating synthesis and secretion of several hormones. Almost every organ and system in the body is affected by physical activity and exercise, mainly mediated through the endocrine and neuroendocrine systems.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How exercise mode and intensity shape hormonal responses",
                "Exercise mode, intensity, duration, age, gender, fitness, and environmental/psychological factors all modify endocrine responses to physical activity.",
                ref(
                    "KEY POINTS",
                    "Exercise mode, intensity and duration, age, gender, individual fitness level, and environmental and psychological factors may affect endocrine responses to physical activity.",
                ),
            ),
            note(
                f"{p}-n3",
                "Catecholamines",
                "Why catecholamines rise with exercise workload",
                "Norepinephrine and epinephrine increase progressively with workload and oxygen uptake; spillover from active muscle is the primary contributor, with rapid sympathetic neural regulation.",
                ref(
                    "Catecholamines",
                    "Both these hormones progressively increase as workload increases.",
                ),
            ),
            note(
                f"{p}-n4",
                "Catecholamines",
                "How endurance training augments adrenaline secretion",
                "Endurance-trained subjects show higher adrenaline responses to intense exercise, hypoglycemia, and hypoxia than untrained subjects—partly explaining superior performance capacity.",
                ref(
                    "Catecholamines",
                    "Higher adrenaline response to exercise occurs in endurance-trained compared with untrained subjects in response to intense exercise at the same relative intensity as all-out exercise.",
                ),
            ),
            note(
                f"{p}-n5",
                "Fluid Homeostasis-Vasopressin-Renin-Angiotensin-Aldosterone System",
                "How AVP responds during exercise",
                "AVP rises during exercise (up to ~24 pg/mL) driven by increased plasma osmolality and reduced blood volume, persisting >60 minutes after maximal effort.",
                ref(
                    "Fluid Homeostasis-Vasopressin-Renin-Angiotensin-Aldosterone System",
                    "AVP concentrations increase during exercise up to 24 pg/mL, and this elevation persists for over 60 minutes following maximal exercise.",
                ),
            ),
            note(
                f"{p}-n6",
                "Glucocorticoids",
                "Why cortisol rises at ≥60% VO2 max",
                "HPA-axis cortisol secretion requires at least 60% maximal oxygen uptake, with linear increases above that threshold; below 60%, prolonged exercise (~90 min at 40%) can still raise ACTH/cortisol.",
                ref(
                    "Glucocorticoids",
                    "The minimum intensity of exercise necessary to produce a cortisol response from the HPA axis is 60% of maximal oxygen uptake ( $ \\dot{V}_{O_2} $ max), with a linear increase between the intensity of exercise and the increase in plasma cortisol concentrations for exercise above 60%  $ \\dot{V}_{O_2} $ max.",
                ),
            ),
            note(
                f"{p}-n7",
                "Glucocorticoids",
                "How hypohydration amplifies exercise cortisol",
                "Hypohydration up to 4.8% body mass loss greatly amplifies cortisol responses—likely via increased core temperature and cardiovascular demand from reduced plasma volume.",
                ref(
                    "Glucocorticoids",
                    "Independently of external thermal stress, hypohydration (up to 4.8% body mass loss) greatly amplifies the exercise-induced responses to cortisol to exercise.",
                ),
            ),
            note(
                f"{p}-n8",
                "Female Gonadal Axis",
                "Why low energy availability causes menstrual dysfunction",
                "Evidence indicates negative energy balance—not exercise stress per se—is the primary cause of reproductive impairment in female athletes; dietary supplementation prevents LH suppression from exercise energy expenditure.",
                ref(
                    "Female Gonadal Axis",
                    "Although factors such as physical and/or psychological stress of competition have been postulated to underlie exercise-induced reproductive disorders, evidence accumulated to date indicates that negative energy balance is the primary cause of the impairment of normal reproductive function commonly observed in female athletes.",
                ),
            ),
            note(
                f"{p}-n9",
                "Female Gonadal Axis",
                "How leptin links adipose stores to reproductive function",
                "Leptin signals adipose adequacy for GnRH secretion; low leptin in energy-deficient states associates with elevated NPY and hypogonadism—leptin therapy can restore ovulatory cycles in hypothalamic amenorrhea.",
                ref(
                    "Female Gonadal Axis",
                    "Leptin may serve as a signal to the central nervous system with information on the critical amount of adipose tissue stores that is necessary for gonadotropin-releasing hormone (GnRH) secretion and pubertal activation of the HPG axis.",
                ),
            ),
            note(
                f"{p}-n10",
                "Female Gonadal Axis",
                "Female athlete triad: energy, menses, bone",
                "The triad describes interrelated low energy availability, HPG-axis suppression with menstrual irregularity, and decreased BMD—revised ACSM guidance broadened it beyond disordered eating, amenorrhea, and osteoporosis alone.",
                ref(
                    "Female Gonadal Axis",
                    "In female athletes, low energy availability is a component of the female athlete triad, a term used to describe the interrelationship of decreased energy availability, subsequent HPG axis inhibition leading to menstrual irregularity, and decreased bone mineral density.",
                ),
            ),
            note(
                f"{p}-n11",
                "Female Gonadal Axis",
                "How RED-S expands the female athlete triad",
                "IOC relative energy deficiency in sport (RED-S) extends triad concepts to males and highlights performance and health consequences beyond bone—encouraging broader research across athlete populations.",
                ref(
                    "Female Gonadal Axis",
                    "More recently, the International Olympic Committee (IOC) has proposed an expansion of the concept of the female athlete triad to include males and has coined the term relative energy deficiency in sport.",
                ),
            ),
            note(
                f"{p}-n12",
                "Male Gonadal Axis",
                "How acute resistance exercise raises testosterone",
                "Short intense exercise increases testosterone (e.g., 13 to ~38 nmol/L at ~30 min post-resistance work) via LH-dependent and lactate-mediated testicular mechanisms, with androgen receptor upregulation lasting 1–2 days.",
                ref(
                    "Male Gonadal Axis",
                    "For example, immediately following resistance exercise, serum testosterone levels peak (from 13 nmol/L $ ^{-1} $ [resting levels] to 38 nmol/L $ ^{-1} $ [at  $ \\sim $30 minutes]), with a concomitant upregulation of androgen receptor mRNA and protein content within the muscle.",
                ),
            ),
            note(
                f"{p}-n13",
                "Male Gonadal Axis",
                "Why prolonged exercise suppresses testosterone",
                "Extended endurance exercise lowers testosterone with hypogonadotrophic characteristics (no compensatory LH rise); chronic exposure can produce persistently low-normal testosterone—the exercise-hypogonadal male.",
                ref(
                    "Male Gonadal Axis",
                    "In contrast to short-term testosterone increases, a suppression of serum testosterone levels occurs during and subsequent to more prolonged exercise, and to some extent in the hours following intense short-term exercise.",
                ),
            ),
            note(
                f"{p}-n14",
                "Male Gonadal Axis",
                "Exercise-hypogonadal male condition",
                "Chronic endurance training can yield persistently low basal testosterone with infertility and bone risks; prevalence appears low but studies are limited—the label 'exercise-hypogonadal male' has been proposed.",
                ref(
                    "Male Gonadal Axis",
                    "Research in exercising men demonstrates the existence of a select group who, through chronic exposure to endurance exercise training, have developed altered reproductive hormonal profiles (i.e., persistently low basal resting testosterone concentrations).",
                ),
            ),
            note(
                f"{p}-n15",
                "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "How exercise is the potent physiologic GH stimulus",
                "Exercise is the most potent physiologic GH releaser; GH rises 10–20 min after onset, peaks at exercise end, returns baseline ~60 min later, increasing pulse amplitude rather than frequency.",
                ref(
                    "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "In 1963, Roth et al $ ^{68} $ demonstrated that plasma levels of GH increase during exercise, and it was later shown that exercise is the most potent physiologic stimulus to GH release.",
                ),
            ),
            note(
                f"{p}-n16",
                "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "Why interval training elevates GH more than continuous work",
                "At equivalent total workload, interval protocols (higher intensity for shorter bursts) produce greater GH than continuous moderate exercise—reflecting greater metabolic stress and lactate.",
                ref(
                    "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "Comparing exercise at equivalent total workloads, GH levels are lower with continuous (40%–45%  $ \\dot{V}o_2 $ max) as opposed to interval protocols with twice the work rate for half the time, reflecting the greater metabolic stress and lactate levels in the latter.",
                ),
            ),
            note(
                f"{p}-n17",
                "Androgenic Steroids",
                "Anabolic-androgenic steroid abuse epidemiology",
                "Meta-analysis of 2.8 million participants shows highest AS prevalence in nonelite sports (18.4%) vs general population (1.0%); men predominate (6.4% vs 1.6% women).",
                ref(
                    "Androgenic Steroids",
                    "This study reported that men were the predominant users (6.4% vs. 1.6% in females) with the prevalence of androgen abuse highest among nonelite sports (18.4%), well ahead of athletes (13.4%), prisoners (12.4%), drug users (8.0%), and high school students (2.3%), compared with the general nonathlete population (1.0%).",
                ),
            ),
            note(
                f"{p}-n18",
                "Androgenic Steroids",
                "Why Bhasin changed the science of testosterone doping",
                "Bhasin et al showed supraphysiologic testosterone plus exercise produces additive gains in muscle size and strength beyond exercise or testosterone alone—dose-dependent effects require ≥300 mg/week for strength gains.",
                ref(
                    "Androgenic Steroids",
                    "In 1996, Bhasin et al $ ^{101} $ demonstrated that administration of supraphysiologic doses of testosterone in combination with exercise in male weightlifters induces a greater increase in muscle size and strength compared to exercise alone or testosterone treatment alone (i.e., the effects of combining supraphysiologic doses of testosterone with exercise are additive).",
                ),
            ),
            note(
                f"{p}-n19",
                "Androgenic Steroids",
                "How urinary steroid profiling detects testosterone abuse",
                "GC-MS steroid profiling (T/E ratio since 1983) uses multiple urinary androgen metabolite ratios to flag exogenous testosterone, precursors, or metabolite administration.",
                ref(
                    "Androgenic Steroids",
                    "The method of steroid profiling was first introduced into routine doping control in 1983 (testosterone to epistestosterone [T/E] ratio).",
                ),
            ),
            note(
                f"{p}-n20",
                "Androgenic Steroids",
                "AS-induced hypogonadism after cessation",
                "Former abusers commonly develop hypogonadotropic hypogonadism after abrupt AS withdrawal—testicular atrophy, low testosterone, impaired spermatogenesis, often resolving over 6–12 months.",
                ref(
                    "Androgenic Steroids",
                    "AS-induced hypogonadism (ASIH) is common among former AS abusers and usually presents as hypogonadotropic hypogonadism due to abrupt decreases in plasma androgen levels following AS cessation.",
                ),
            ),
            note(
                f"{p}-n21",
                "Growth Hormone",
                "Why the GH isoform test detects rhGH abuse",
                "Recombinant 22-kDa hGH shifts the serum isoform ratio because pituitary isoform diversity is suppressed by negative feedback—detectable within 12–24 hours of injection.",
                ref(
                    "Growth Hormone",
                    "After peripheral injection of recombinant 22-kDa hGH, the pituitary's production of GH isoforms is reduced by negative feedback via IGF1.",
                ),
            ),
            note(
                f"{p}-n22",
                "Erythropoietin and the Erythropoietin System",
                "EPO doping and aerobic performance",
                "Low-dose rhEPO raises VO2 max 6–12% when hematocrit reaches ~0.50 and prolongs time to exhaustion; benefits persist weeks after discontinuation but carry thrombotic risk when Hct exceeds 0.50–0.55.",
                ref(
                    "Erythropoietin and the Erythropoietin System",
                    "When rhEPO is applied to healthy volunteers in low dosages,  $ \\dot{V}_{O_2} $ max is increased by 6% to 12% when Hct is raised to approximately 0.50.",
                ),
            ),
            note(
                f"{p}-n23",
                "Erythropoietin and the Erythropoietin System",
                "How indirect blood models detect EPO misuse",
                "Indirect 'on' and 'off' models use reticulocyte hematocrit, serum EPO, hematocrit, soluble transferrin receptor, and macrocyte percentage to detect recent or retrospective rhEPO/analogue use.",
                ref(
                    "Erythropoietin and the Erythropoietin System",
                    "The \"on\" model used all parameters to detect recent use of EPO. The \"off\" model used three parameters to detect EPO use with more retrospectivity.",
                ),
            ),
            note(
                f"{p}-n24",
                "Erythropoietin and the Erythropoietin System",
                "Dangers of pharmacologic erythrocytosis",
                "Unlike training-induced plasma volume expansion, rhEPO selectively increases red cell mass—Hct >0.55 risks heart failure, MI, seizures, thromboembolism, and pulmonary embolism.",
                ref(
                    "Erythropoietin and the Erythropoietin System",
                    "If Hct exceeds 0.50, blood viscosity and cardiac afterload increase significantly. The main risks of erythrocytosis with Hct >0.55 include heart failure, myocardial infarction, seizures, peripheral thromboembolic events, and pulmonary embolism.",
                ),
            ),
            note(
                f"{p}-n25",
                "Transgender Persons and Sport Participation",
                "How transgender inclusion policies balance fairness",
                "Sport organizations restrict some transgender competitors over perceived testosterone advantage; IOC 2021 Framework seeks safe inclusion and fair competition without disproportionate advantage.",
                ref(
                    "Transgender Persons and Sport Participation",
                    "The Framework recognizes both the need to ensure that everyone, irrespective of gender identity or sex variations, can practice sport in a safe, harassment-free environment that recognizes and respects their needs and identities, and the interest of everyone—particularly elite athletes—to participate in fair competitions where no participant has an unfair and disproportionate advantage over others.",
                ),
            ),
            note(
                f"{p}-n26",
                "Glucocorticoids",
                "WADA glucocorticoid in-competition prohibition",
                "Injectable, oral, and rectal glucocorticoids are prohibited in-competition; topical/inhaled/intranasal routes are permitted within licensed doses—urinary reporting threshold is 30 ng/mL.",
                ref(
                    "Glucocorticoids",
                    "All GCs are prohibited when administered by any injectable, oral (including oromucosal), or rectal route during the in-competition period.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Female Gonadal Axis",
                "A 19-year-old collegiate distance runner has amenorrhea, stress fractures, and reports eating 'as little as possible' to stay lean. Labs show low leptin and low morning T3. Primary driver of her menstrual dysfunction?",
                [
                    "Low energy availability",
                    "Exercise stress independent of calories",
                    "Hyperandrogenism from swimming",
                    "Primary ovarian failure",
                ],
                0,
                "Loucks demonstrated LH pulsatility disruption from reduced energy availability regardless of whether restriction came from diet, exercise expenditure, or both—exercise stress alone did not add beyond energy cost.",
                ref(
                    "Female Gonadal Axis",
                    "Loucks et al $ ^{28} $ found that low-energy availability reduced luteinizing hormone (LH) pulse frequency and increased LH pulse amplitude, and that exercise stress had no suppressive effect on LH pulsatility beyond the impact of the energy cost of exercise on energy availability.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Female Gonadal Axis",
                "A team physician counsels a female athlete with functional hypothalamic amenorrhea from chronic energy deficit. Which intervention best addresses the root endocrine problem?",
                [
                    "Increase energy availability (caloric intake relative to expenditure)",
                    "Start combined oral contraceptives as first-line without addressing intake",
                    "Prescribe leptin before any nutritional rehabilitation",
                    "Stop all exercise permanently regardless of energy balance",
                ],
                0,
                "Dietary supplementation prevented LH suppression from exercise energy expenditure—restoring energy availability is the foundational treatment.",
                ref(
                    "Female Gonadal Axis",
                    "Dietary supplementation prevented the suppression of LH pulsatility by exercise energy expenditure.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Female Gonadal Axis",
                "A sports medicine fellow explains RED-S to coaches. Compared with the original female athlete triad, RED-S emphasizes:",
                [
                    "Energy deficiency consequences in both sexes beyond bone and menses alone",
                    "Amenorrhea as the only mandatory diagnostic criterion",
                    "Exclusively disordered eating as the sole cause",
                    "That male athletes are immune to energy-deficiency endocrinopathy",
                ],
                0,
                "IOC RED-S broadens awareness to men and to performance/health effects beyond the original triad bone-menstrual focus.",
                ref(
                    "Female Gonadal Axis",
                    "This had three main purposes: (1) to draw awareness to the fact that energy restriction can have negative consequences in men in addition to women; (2) to highlight other potential negative health and performance consequences of low energy availability in athletes besides bone problems; and (3) to encourage expansive research into the potential myriad effects of low energy availability in various populations, including Paralympic athletes.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Male Gonadal Axis",
                "A 32-year-old elite ultramarathoner has persistently low-normal testosterone, low-normal LH, and infertility workup planned. Most accurate label for this pattern?",
                [
                    "Exercise-hypogonadal male condition",
                    "Primary testicular failure",
                    "Pituitary prolactinoma as first diagnosis",
                    "Normal variant requiring no evaluation",
                ],
                0,
                "Chronic endurance exposure can produce persistently low basal testosterone with hypogonadotrophic characteristics—the exercise-hypogonadal male.",
                ref(
                    "Male Gonadal Axis",
                    "The specific terminology used to refer to this condition has not been universally agreed on, and the phrase \"the exercise-hypogonadal male\" has been proposed as a label for this condition.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Male Gonadal Axis",
                "A recreational lifter asks why post-workout testosterone spikes matter for hypertrophy. Best evidence-based answer?",
                [
                    "Acute testosterone rise plus sustained androgen receptor upregulation may potentiate muscle anabolism",
                    "Chronic resting testosterone stays elevated for months after each session",
                    "Testosterone never rises acutely with resistance training",
                    "Only oral anabolic steroids—not exercise—affect androgen receptors",
                ],
                0,
                "Acute testosterone elevation and 1–2 day AR upregulation together may enhance testosterone uptake and anabolic signaling in muscle.",
                ref(
                    "Male Gonadal Axis",
                    "The combined effects of acute testosterone elevation after exercise and sustained AR upregulation in the muscle may thus represent an additional mechanism through which resistance exercise might regulate muscle growth.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Glucocorticoids",
                "A marathon runner trains dehydrated in heat and has exaggerated cortisol rise at 65% VO2 max. Contributing factor?",
                [
                    "Hypohydration amplifying HPA response",
                    "Meal ingestion immediately before exercise",
                    "Morning versus evening timing only—no hydration effect",
                    "Resistance exercise volume",
                ],
                0,
                "Hypohydration up to 4.8% body mass loss greatly amplifies exercise-induced cortisol independently of ambient temperature.",
                ref(
                    "Glucocorticoids",
                    "Independently of external thermal stress, hypohydration (up to 4.8% body mass loss) greatly amplifies the exercise-induced responses to cortisol to exercise.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "An exercise physiologist compares continuous moderate cycling with matched-workload interval sessions. Expected GH finding?",
                [
                    "Higher GH with interval (higher-intensity) protocol",
                    "Higher GH with continuous low-intensity protocol",
                    "No GH response unless exercise exceeds 10 minutes",
                    "GH only rises with resistance—not aerobic—exercise",
                ],
                0,
                "Interval protocols at equivalent total workload produce greater GH than continuous moderate exercise due to higher metabolic stress and lactate.",
                ref(
                    "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "Comparing exercise at equivalent total workloads, GH levels are lower with continuous (40%–45%  $ \\dot{V}o_2 $ max) as opposed to interval protocols with twice the work rate for half the time, reflecting the greater metabolic stress and lactate levels in the latter.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Androgenic Steroids",
                "A 28-year-old bodybuilder presents with adult-onset truncal acne, testicular atrophy, and low testosterone 3 months after stopping injectable nandrolone. Most likely diagnosis?",
                [
                    "Anabolic steroid-induced hypogonadism",
                    "Classic Cushing syndrome",
                    "Primary hyperaldosteronism",
                    "Physiologic post-exercise suppression",
                ],
                0,
                "ASIH is common after AS cessation—hypogonadotropic hypogonadism with testicular atrophy; truncal acne in adults is nearly pathognomonic for androgen abuse.",
                ref(
                    "Androgenic Steroids",
                    "Hence, adult-onset truncal acne is almost pathognomonic for androgen abuse.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Androgenic Steroids",
                "An antidoping lab flags a urine sample with altered T/E ratio. Historical context for this screening approach?",
                [
                    "Steroid profiling introduced in 1983 for testosterone/epitestosterone ratio",
                    "T/E ratio first used only after 2010 WADA update",
                    "Urinary T/E cannot detect testosterone precursors",
                    "GC-MS is never used for androgen detection",
                ],
                0,
                "Urinary steroid profiling with T/E ratio entered routine doping control in 1983.",
                ref(
                    "Androgenic Steroids",
                    "The method of steroid profiling was first introduced into routine doping control in 1983 (testosterone to epistestosterone [T/E] ratio).",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Androgenic Steroids",
                "A physician counsels a patient who used oral methyltestosterone. Which hepatotoxicity pattern is class-specific?",
                [
                    "C17α-alkylated steroids—cholestasis, peliosis, hepatic tumors",
                    "All injectable testosterone esters cause peliosis hepatitis universally",
                    "Oxandrolone carries the highest C17α hepatotoxicity risk",
                    "Liver injury never occurs with androgen abuse",
                ],
                0,
                "C17α-alkyl substitution enables oral bioavailability but causes class-specific hepatotoxicity; oxandrolone is an exception among 17α-alkylated agents.",
                ref(
                    "Androgenic Steroids",
                    "Liver disease is a well-documented side effect of most, but not all, C17α-alkylated anabolic-androgenic steroids, the exception being oxandrolone.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Growth Hormone",
                "A healthy non-GHD athlete asks whether rhGH will improve strength for competition. Best evidence-based response?",
                [
                    "Systematic review: GH increased lean mass but not strength in healthy adults",
                    "GH reliably increases maximal strength in all trained athletes",
                    "GH is legal without restriction in all sports",
                    "GH improves aerobic capacity in all healthy adults",
                ],
                0,
                "Liu et al meta-analysis of 44 RCTs found GH increased lean body mass but not strength; Meinhardt showed no strength benefit in recreational athletes.",
                ref(
                    "Growth Hormone",
                    "Although GH increased lean body mass, strength was not increased.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Growth Hormone",
                "Antidoping collects an out-of-competition blood sample 18 hours after suspected rhGH injection. Most appropriate detection strategy?",
                [
                    "GH isoform ratio immunoassay",
                    "Urinary IGF1 alone",
                    "Serum insulin C-peptide ratio",
                    "T/E urinary steroid profile",
                ],
                0,
                "The isoform test exploits recombinant 22-kDa hGH shifting pituitary isoform ratios—realistically detectable within 12–24 hours; suited to unannounced out-of-competition testing.",
                ref(
                    "Growth Hormone",
                    "The isoform test is an excellent strategy to detect GH doping, provided it is administered shortly after the last GH dose (within 24–36 hours, depending on the dose), $ ^{138} $ realistically probably within 12 to 24 hours.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "GH Secretagogues",
                "An athlete uses a ghrelin-receptor secretagogue to avoid GH isoform testing. Why this may evade direct rhGH detection?",
                [
                    "Secretagogue-stimulated GH is endogenous and not detected by isoform test",
                    "Secretagogues permanently abolish all GH secretion",
                    "WADA does not prohibit any secretagogues",
                    "Secretagogues produce only urinary—not serum—GH",
                ],
                0,
                "GH secretagogues release endogenous GH, which is not distinguishable by the recombinant isoform assay—though marker methods may still raise suspicion.",
                ref(
                    "GH Secretagogues",
                    "Nevertheless, GH secretagogues may be attractive to athletes who want to avoid detection because the GH released is endogenous and therefore not detectable by the GH isoform test.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Erythropoietin and the Erythropoietin System",
                "A cyclist's hematologic passport shows elevated reticulocyte hematocrit and soluble transferrin receptor with suppressed serum EPO—pattern consistent with:",
                [
                    "Recent rhEPO or ESA use ('on' model)",
                    "Pure iron deficiency anemia only",
                    "Normal altitude training without pharmacologic ESA",
                    "Neocytolysis immediately after EPO withdrawal only",
                ],
                0,
                "The indirect 'on' model combines five blood parameters including reticulocyte Hct and soluble transferrin receptor to detect recent EPO misuse.",
                ref(
                    "Erythropoietin and the Erythropoietin System",
                    "An indirect test based on measurement of five blood parameters (reticulocyte Hct, serum EPO, Hct, soluble transferrin receptor, and the percentage macrocytes) was developed.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Erythropoietin and the Erythropoietin System",
                "A physician explains thrombotic risk to an athlete considering rhEPO. Critical hematocrit threshold cited for major complications?",
                [
                    "Hct >0.55",
                    "Hct >0.35",
                    "Hct exactly 0.42 in all athletes",
                    "Hct is irrelevant to viscosity",
                ],
                0,
                "Pharmacologic erythrocytosis with Hct >0.55 carries heart failure, MI, seizure, and thromboembolic risks unlike training-induced pseudoanemia from plasma expansion.",
                ref(
                    "Erythropoietin and the Erythropoietin System",
                    "The main risks of erythrocytosis with Hct >0.55 include heart failure, myocardial infarction, seizures, peripheral thromboembolic events, and pulmonary embolism.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Erythropoietin and the Erythropoietin System",
                "Direct urinary detection of rhEPO relies primarily on:",
                [
                    "Isoelectric focusing separating glycosylation isoforms",
                    "Serum testosterone profiling",
                    "Urinary ketone measurement",
                    "Bone density scanning",
                ],
                0,
                "Isoelectric separation of urinary EPO isoforms on polyacrylamide gel with double blotting distinguishes endogenous from recombinant EPO—valid within ~24 h of last injection.",
                ref(
                    "Erythropoietin and the Erythropoietin System",
                    "In June 2000, a few weeks before the Sydney Olympic games, an innovative test based on the isoelectric separation of urinary EPO isoforms on a polyacrylamide gel followed by a double blotting process was proposed.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Insulin",
                "Antidoping suspects subcutaneous insulin abuse in a non-diabetic athlete. Most useful initial laboratory approach?",
                [
                    "Elevated insulin-to-C-peptide ratio suggesting exogenous insulin",
                    "Urinary T/E ratio alone",
                    "Serum GH isoform ratio",
                    "Random blood glucose only without insulin assays",
                ],
                0,
                "Exogenous insulin raises insulin without equimolar C-peptide; sulfonylureas stimulate endogenous proinsulin yielding both analytes.",
                ref(
                    "Insulin",
                    "A high ratio of insulin to C-peptide may distinguish subcutaneous regular insulin use from insulin-stimulating medications such as the sulfonylureas.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Glucocorticoids",
                "An athlete with exercise-induced asthma uses inhaled budesonide at licensed doses during competition. Per WADA rules:",
                [
                    "Inhaled glucocorticoids within licensed doses are not prohibited",
                    "All glucocorticoids including inhaled are banned in and out of competition",
                    "Only intravenous glucocorticoids are monitored",
                    "Inhaled steroids require no TUE ever in any athlete",
                ],
                0,
                "Injectable/oral/rectal GCs are in-competition prohibited; inhaled, topical, intranasal, and other routes are permitted within manufacturer licensed doses and indications.",
                ref(
                    "Glucocorticoids",
                    "Other routes of administration (including topical, inhaled, intranasal, ophthalmologic, perianal, and dermal) are not prohibited when used within the manufacturer's licensed doses and therapeutic indications.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Transgender Persons and Sport Participation",
                "A transgender woman athlete on testosterone suppression still shows substantial muscular advantage over cisgender women per recent data. Clinical/policy implication?",
                [
                    "Testosterone suppression alone may not fully eliminate performance disparity—policies remain contested",
                    "No performance difference exists after 1 week of spironolactone",
                    "Transgender men always have unfair advantage over cisgender men",
                    "IOC prohibits all transgender participation without exception",
                ],
                0,
                "Hilton and Lundberg report muscular advantage is only minimally reduced after testosterone suppression—informing ongoing fairness debates.",
                ref(
                    "Transgender Persons and Sport Participation",
                    "Interestingly, the muscular advantage of transgender women over cisgender women is only minimally reduced after testosterone suppression.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Transgender Persons and Sport Participation",
                "A transgender male athlete on testosterone therapy competes. Which substance typically requires a therapeutic use exemption (TUE)?",
                [
                    "Testosterone",
                    "Spironolactone in transgender women",
                    "Estrogen preparations",
                    "Cyproterone acetate",
                ],
                0,
                "In transgender male athletes, testosterone is the administered prohibited substance requiring TUE once eligibility is established.",
                ref(
                    "Transgender Persons and Sport Participation",
                    "In transgender male athletes, testosterone is the administered prohibited substance.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Transgender Persons and Sport Participation",
                "A transgender female athlete eligible to compete as female uses a GnRH analogue for feminization. TUE requirement for the GnRH analogue?",
                [
                    "Not required—GnRH analogues are prohibited only in males",
                    "Always required for all athletes regardless of gender category",
                    "GnRH analogues are never prohibited substances",
                    "Required only if competing as male while feminizing",
                ],
                0,
                "Transgender female athletes competing as females do not need a TUE for GnRH analogues; TUE is needed if still competing as male during feminization.",
                ref(
                    "Transgender Persons and Sport Participation",
                    "Transgender female athletes eligible to participate as females in their sport do not require a TUE for GnRH analogues, because they are prohibited substances only in males.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Erythropoietin",
                "An endurance athlete has low hemoglobin despite high training volume. 'Sports anemia' mechanism?",
                [
                    "Pseudoanemia from expanded plasma volume",
                    "Primary bone marrow failure",
                    "Acute rhEPO overdose",
                    "Intrinsic red cell enzyme deficiency",
                ],
                0,
                "Endurance athletes may show relatively low Hb/Hct from plasma volume expansion rather than true erythropoietic failure.",
                ref(
                    "Erythropoietin",
                    "This \"sports anemia\" is usually a pseudoanemia due to an enlarged plasma volume.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Catecholamines",
                "A researcher compares catecholamine responses to graded vs prolonged continuous exercise at matched workloads. Expected finding?",
                [
                    "Lower catecholamine response with graded exercise than prolonged continuous",
                    "Higher catecholamine response with graded exercise",
                    "No catecholamine change with any aerobic exercise",
                    "Epinephrine only rises in resistance exercise",
                ],
                0,
                "Graded exercise produces lower catecholamine response than continuous prolonged exercise at comparable workloads.",
                ref(
                    "Catecholamines",
                    "Graded exercise produces a lower catecholamine response than continuous prolonged exercise.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Insulin-Like Growth Factor 1",
                "Antidoping develops IGF1 misuse detection mirroring GH marker strategy. Proposed marker combination includes:",
                [
                    "Serum IGF1 and procollagen III N-terminal extension peptide (PIIIP)",
                    "Urinary testosterone alone",
                    "Serum prolactin and TSH only",
                    "Hematocrit and reticulocyte count only",
                ],
                0,
                "GH-2000/2004 consortium identified IGF1 plus PIIIP as marker set for GH abuse detection—adapted for IGF1 misuse research.",
                ref(
                    "Growth Hormone",
                    "The combination of IGF1 and the procollagen III N-terminal extension peptide (PIIIP) is proposed to provide a set of markers that allow the detection of GH abuse in athletes for up to 2 weeks after the last application.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Androgenic Steroids",
                "A former steroid user seeks fertility counseling 6 months after stopping long-acting testosterone enanthate. Expected recovery timeline?",
                [
                    "Spermatogenesis often recovers within 1–2 years; longer with prolonged abuse and long-acting formulations",
                    "Permanent azoospermia in all former users",
                    "Immediate normal fertility within 48 hours of last injection",
                    "Recovery never occurs after any oral steroid exposure",
                ],
                0,
                "Male infertility from AS is generally reversible; recovery may be delayed with longer abuse duration and longer-acting androgen esters.",
                ref(
                    "Androgenic Steroids",
                    "The recovery of spermatogenic function has been shown to occur within 1 to 2 years of discontinuation of chronic AS abuse. However, there appears to be a delay in spermatogenic recovery with longer duration of androgen abuse and longer-acting formulations of androgens.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "KEY POINTS",
                "A sports endocrinologist educates residents on hormone doping health consequences. Central teaching point from Williams KEY POINTS?",
                [
                    "Hormone abuse in competitive and recreational sport harms long-term health",
                    "Hormone abuse affects only elite professionals—not recreational athletes",
                    "Detection methods are unnecessary because abuse is rare",
                    "Exercise never influences endocrine systems",
                ],
                0,
                "KEY POINTS emphasize widespread hormone misuse and negative long-term health consequences requiring clinician awareness.",
                ref(
                    "KEY POINTS",
                    "Hormone abuse in competitive and recreational sports exerts negative consequences for long-term health.",
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
                "Several hormones influence physical performance and body composition, with bidirectional relationships between exercise and hormones.",
                True,
                "KEY POINTS describe bidirectional exercise–hormone interrelationships affecting performance and composition.",
                ref(
                    "KEY POINTS",
                    "Several hormones influence physical performance and body composition, with a bidirectional interrelationship between exercise and hormones.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Female Gonadal Axis",
                "Low energy availability—not exercise stress beyond its energy cost—is the primary cause of exercise-induced reproductive dysfunction in women.",
                True,
                "Loucks demonstrated LH disruption from energy availability reduction regardless of exercise stress independent of energy cost.",
                ref(
                    "Female Gonadal Axis",
                    "Loucks et al $ ^{28} $ found that low-energy availability reduced luteinizing hormone (LH) pulse frequency and increased LH pulse amplitude, and that exercise stress had no suppressive effect on LH pulsatility beyond the impact of the energy cost of exercise on energy availability.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "Exercise is the most potent physiologic stimulus to growth hormone release.",
                True,
                "Landmark studies established exercise as the strongest physiologic GH secretagogue.",
                ref(
                    "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "In 1963, Roth et al $ ^{68} $ demonstrated that plasma levels of GH increase during exercise, and it was later shown that exercise is the most potent physiologic stimulus to GH release.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "GH exercise response requires at least 10 minutes of exercise duration.",
                True,
                "Shorter bouts below and above lactate threshold did not increase circulating GH.",
                ref(
                    "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "Exercise duration should be at least 10 minutes, because shorter duration both below and above the lactate threshold was not accompanied by increases in circulating GH levels.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Androgenic Steroids",
                "The IOC introduced antidoping regulations in 1967 and first performed antidoping testing at the 1972 Munich Olympics.",
                True,
                "Historical timeline: IOC antidoping rules 1967; first Olympic testing 1972 Munich; androgens on doping list 1976.",
                ref(
                    "Androgenic Steroids",
                    "The IOC introduced antidoping regulations for the first time in 1967 and performed the first antidoping testing in the 1972 Munich Olympics.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Androgenic Steroids",
                "Significant strength increases from exogenous testosterone occur only at doses of 300 mg per week and higher.",
                True,
                "Bhasin dose-response work showed meaningful strength gains require supraphysiologic doses ≥300 mg/week.",
                ref(
                    "Androgenic Steroids",
                    "In fact, significant increases in muscle strength occur only with doses of 300 mg per week and higher.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Growth Hormone",
                "In healthy adults, growth hormone administration increases lean body mass but does not increase muscle strength.",
                True,
                "Liu systematic review of 44 RCTs in healthy adults reached this conclusion.",
                ref(
                    "Growth Hormone",
                    "Although GH increased lean body mass, strength was not increased.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Growth Hormone",
                "The GH isoform test is well suited for routine in-competition testing because its detection window extends several weeks after injection.",
                False,
                "Isoform test window is short (12–24 h realistically); it is better suited to unannounced out-of-competition testing.",
                ref(
                    "Growth Hormone",
                    "Due to this short window of opportunity the test is not well suited for in-competition testing.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Erythropoietin and the Erythropoietin System",
                "WADA added hypoxia-inducible factor stabilizers to the prohibited list in 2011.",
                True,
                "HIF stabilizers were banned suggesting black-market availability; first athlete positive reported 2016.",
                ref(
                    "Erythropoietin and the Erythropoietin System",
                    "The World Anti-Doping Agency (WADA) added HIF stabilizers to the list of banned substances in 2011, suggesting that they have been available on the black market for some time.",
                ),
            ),
            tf(
                f"{p}-tf10",
                "Erythropoietin",
                "Single bouts of strenuous normoxic sea-level exercise usually do not materially change plasma erythropoietin levels.",
                True,
                "EPO synthesis is kidney O2-sensor driven; acute normoxic exercise generally does not majorly alter EPO.",
                ref(
                    "Erythropoietin",
                    "Plasma erythropoietin (EPO) levels are not usually affected by single bouts of strenuous exercise at sea level.",
                ),
            ),
            tf(
                f"{p}-tf11",
                "Glucocorticoids",
                "Injectable, oral, and rectal glucocorticoids are prohibited during the in-competition period under WADA rules.",
                True,
                "Multiple systemic routes are banned in-competition; other routes permitted within licensed therapeutic doses.",
                ref(
                    "Glucocorticoids",
                    "All GCs are prohibited when administered by any injectable, oral (including oromucosal), or rectal route during the in-competition period.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Transgender Persons and Sport Participation",
                "Transgender female athletes eligible to compete as females require a TUE for GnRH analogues because they are prohibited in all athletes.",
                False,
                "GnRH analogues are prohibited only in males; transgender women competing as females do not need a TUE for GnRH analogues.",
                ref(
                    "Transgender Persons and Sport Participation",
                    "Transgender female athletes eligible to participate as females in their sport do not require a TUE for GnRH analogues, because they are prohibited substances only in males.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "Transgender Persons and Sport Participation",
                "Estrogen preparations and cyproterone acetate are prohibited substances on the WADA list for transgender female athletes.",
                False,
                "Spironolactone is the commonly used prohibited antiandrogen; estrogen and cyproterone are not prohibited.",
                ref(
                    "Transgender Persons and Sport Participation",
                    "Notably, estrogen preparations and cyproterone acetate are not prohibited substances.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Female Gonadal Axis",
                "Assertion: Amenorrheic female athletes often have low energy availability.",
                "Reason: Exercise stress independently of energy cost suppresses LH pulsatility beyond the effect of energy availability.",
                2,
                "Assertion true; reason false—Loucks showed exercise stress added no LH suppression beyond energy availability impact.",
                ref(
                    "Female Gonadal Axis",
                    "Loucks et al $ ^{28} $ found that low-energy availability reduced luteinizing hormone (LH) pulse frequency and increased LH pulse amplitude, and that exercise stress had no suppressive effect on LH pulsatility beyond the impact of the energy cost of exercise on energy availability.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Male Gonadal Axis",
                "Assertion: Acute resistance exercise transiently raises serum testosterone.",
                "Reason: Chronic resistance training permanently elevates resting testosterone for months.",
                2,
                "Assertion true; reason false—acute testosterone returns to baseline rapidly; chronic resting elevation does not persist.",
                ref(
                    "Male Gonadal Axis",
                    "Whereas the acute testosterone response returns to baseline rapidly after exercise and is not elevated chronically following repeated bouts of resistance exercise, $ ^{47} $ acute upregulation of androgen receptor (AR) mRNA and protein content can last up to 1 to 2 days after exercise, $ ^{51} $ thus increasing testosterone uptake into muscle and potentiating anabolic effects of testosterone over longer periods.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                "Assertion: Exercise stimulates growth hormone secretion.",
                "Reason: Exercise is a weaker GH stimulus than sleep alone in all trained athletes.",
                2,
                "Assertion true; reason false—exercise is described as the most potent physiologic GH stimulus.",
                ref(
                    "Growth Hormone/Insulin-Like Growth Factor 1 Axis",
                    "In 1963, Roth et al $ ^{68} $ demonstrated that plasma levels of GH increase during exercise, and it was later shown that exercise is the most potent physiologic stimulus to GH release.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Androgenic Steroids",
                "Assertion: Supraphysiologic testosterone combined with exercise increases muscle size more than exercise alone.",
                "Reason: Early reviews concluded testosterone never affects muscle size in healthy men regardless of dose.",
                2,
                "Assertion true (Bhasin); reason false—early underpowered reviews were superseded by controlled supraphysiologic dosing studies.",
                ref(
                    "Androgenic Steroids",
                    "In 1996, Bhasin et al $ ^{101} $ demonstrated that administration of supraphysiologic doses of testosterone in combination with exercise in male weightlifters induces a greater increase in muscle size and strength compared to exercise alone or testosterone treatment alone (i.e., the effects of combining supraphysiologic doses of testosterone with exercise are additive).",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Androgenic Steroids",
                "Assertion: Urinary steroid profiling can screen for exogenous androgen administration.",
                "Reason: Endogenous androgens are absent from human urine so any androgen detected proves doping.",
                2,
                "Assertion true; reason false—endogenous steroids occur naturally; profiling uses ratio shifts (e.g., T/E) to detect exogenous use.",
                ref(
                    "Androgenic Steroids",
                    "Endogenous androgens and their metabolites occur naturally in the human body, and thus specific indicators for the detection of the exogenous administration of these steroids are required.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Growth Hormone",
                "Assertion: Recombinant hGH abuse can be detected using isoform immunoassays.",
                "Reason: Recombinant 22-kDa hGH increases pituitary isoform diversity in serum.",
                2,
                "Assertion true; reason false—injection suppresses pituitary isoform diversity via IGF1 negative feedback, shifting the isoform ratio.",
                ref(
                    "Growth Hormone",
                    "After peripheral injection of recombinant 22-kDa hGH, the pituitary's production of GH isoforms is reduced by negative feedback via IGF1.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Growth Hormone",
                "Assertion: GH secretagogues may appeal to dopers seeking to avoid isoform testing.",
                "Reason: Secretagogues inject exogenous 22-kDa hGH directly into circulation.",
                2,
                "Assertion true; reason false—secretagogues stimulate endogenous GH release, not exogenous rhGH injection.",
                ref(
                    "GH Secretagogues",
                    "Nevertheless, GH secretagogues may be attractive to athletes who want to avoid detection because the GH released is endogenous and therefore not detectable by the GH isoform test.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Erythropoietin and the Erythropoietin System",
                "Assertion: rhEPO can enhance maximal aerobic performance when hematocrit rises toward 0.50.",
                "Reason: rhEPO increases plasma volume more than red cell mass, mimicking sports anemia.",
                2,
                "Assertion true; reason false—rhEPO selectively increases red cell mass unlike training-induced plasma volume expansion.",
                ref(
                    "Erythropoietin and the Erythropoietin System",
                    "In contrast to the effect of endurance training, which results in increased plasma volume, administration of rhEPO produces a selective increase in red cell mass.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Erythropoietin and the Erythropoietin System",
                "Assertion: Indirect blood marker models can detect EPO misuse.",
                "Reason: Indirect methods cannot detect newer EPO analogues and mimetics.",
                2,
                "Assertion true; reason false—indirect methods offer universal coverage of analogues and mimetics.",
                ref(
                    "Erythropoietin and the Erythropoietin System",
                    "An advantage of indirect methods to detect rhEPO is its universal coverage of increasingly used different types of analogues and mimetics.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Glucocorticoids",
                "Assertion: Systemic glucocorticoids are prohibited in-competition under WADA rules.",
                "Reason: Inhaled glucocorticoids at licensed doses are also prohibited in all contexts.",
                2,
                "Assertion true for systemic routes; reason false—inhaled/topical routes within licensed doses are not prohibited.",
                ref(
                    "Glucocorticoids",
                    "Other routes of administration (including topical, inhaled, intranasal, ophthalmologic, perianal, and dermal) are not prohibited when used within the manufacturer's licensed doses and therapeutic indications.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Transgender Persons and Sport Participation",
                "Assertion: Transgender male athletes on testosterone need a TUE for testosterone.",
                "Reason: Testosterone is not a prohibited substance in any sport context.",
                2,
                "Assertion true; reason false—testosterone is prohibited and requires TUE when used by transgender male athletes.",
                ref(
                    "Transgender Persons and Sport Participation",
                    "In transgender male athletes, testosterone is the administered prohibited substance.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Catecholamines",
                "Assertion: Endurance-trained athletes show higher adrenaline responses to intense exercise than untrained subjects.",
                "Reason: Untrained subjects always have higher catecholamine responses at any workload.",
                2,
                "Assertion true; reason false—trained subjects demonstrate greater adrenaline secretory capacity at matched relative intensity.",
                ref(
                    "Catecholamines",
                    "Higher adrenaline response to exercise occurs in endurance-trained compared with untrained subjects in response to intense exercise at the same relative intensity as all-out exercise.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "25",
        "title": "Hormones and Athletic Performance",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Fabio Lanfranco, Ezio Ghigo, and Christian J. Strasburger",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_25_Hormones_and_Athletic_Performance.md",
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
