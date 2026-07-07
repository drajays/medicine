#!/usr/bin/env python3
"""Generate Williams 15e module w15-18 — Sexual Function and Dysfunction."""
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
OUT_NAME = "w15-18_Sexual_Function_and_Dysfunction.json"


def build() -> dict:
    p = "w15-18"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why the sexual response cycle model matters clinically",
                "Sexual response is a motivation/incentive-based cycle of desire, arousal, and orgasm whose phases overlap and vary in order—this framework underpins ICD-11/DSM classification and directs assessment of hypoactive desire, arousal failure, orgasmic disorder, and pain syndromes.",
                ref(
                    "KEY POINTS",
                    "Sexual response is a motivation/incentive-based cycle comprising of phases of physiologic responses that include desire, arousal, and orgasm. These phases of the cycle can overlap, and their order can be variable, but this conceptualization of sexual response cycle has proven useful in classifying sexual dysfunctions.",
                ),
            ),
            note(
                f"{p}-n2",
                "Hemodynamic Changes During Penile Erection",
                "How penile erection achieves rigidity",
                "Erection follows CNS activation, cavernosal smooth-muscle relaxation, arterial inflow, and veno-occlusion: expanding sinusoids compress venules against the tunica albuginea, trapping blood and imparting rigidity.",
                ref(
                    "Hemodynamic Changes During Penile Erection",
                    "Penile erection results from a series of biochemical and hemodynamic events that are associated with activation of central nervous system sites involved in regulation of erections, relaxation of cavernosal smooth muscle, increased blood flow into the cavernosal sinuses, and venous occlusion resulting in penile engorgement and rigidity.",
                ),
            ),
            note(
                f"{p}-n3",
                "Biochemical Regulation of Cavernosal Smooth Muscle Tone",
                "Cavernosal smooth muscle tone regulators",
                "Flaccidity vs tumescence reflects intracellular calcium; tone is modulated by K⁺ channels, connexin43 gap junctions, and cholinergic, adrenergic, and nonadrenergic/noncholinergic mediators including nitric oxide.",
                ref(
                    "KEY POINTS",
                    "Corporal smooth muscle tone is regulated by transmembrane and intracellular calcium flux, which in turn is regulated by potassium channels; connexin43-derived gap junctions; and cholinergic, adrenergic, and nonadrenergic, noncholinergic mediators, including nitric oxide.",
                ),
            ),
            note(
                f"{p}-n4",
                "Nitric Oxide",
                "How the NO–cGMP–PDE5 pathway mediates erection",
                "Neuronal and endothelial NO activates guanylyl cyclase → cGMP → PKG, lowering intracellular calcium and relaxing cavernosal smooth muscle; PDE5 hydrolyzes cGMP—selective PDE5 inhibitors (sildenafil, tadalafil, etc.) prolong the erectile signal.",
                ref(
                    "KEY POINTS",
                    "Selective phosphodiesterase-5 inhibitors are safe and effective and have emerged as first-line therapy for men with erectile dysfunction.",
                ),
            ),
            note(
                f"{p}-n5",
                "Cyclic Nucleotide Phosphodiesterases",
                "Why PDE5 inhibitors need sexual stimulation",
                "PDE5 inhibitors block cGMP breakdown and restore the natural erectile response to stimulation but do not produce erections without erotic input because constitutive NO/cGMP generation requires arousal.",
                ref(
                    "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                    "By selectively inhibiting cGMP catabolism in the cavernosal smooth muscle cells, PDE5 inhibitors restore the natural erectile response to sexual stimulation but do not produce an erection in the absence of sexual stimulation.",
                ),
            ),
            note(
                f"{p}-n6",
                "The Sexual Response Cycle",
                "Why Basson's model fits women with dysfunction",
                "Beyond linear Masters–Johnson/Kaplan models, Basson emphasized emotional intimacy, stimuli, and relationship satisfaction as incentives—most aligned with women who have sexual dysfunction, guiding assessment of context and motivation.",
                ref(
                    "The Sexual Response Cycle",
                    "This model has since been found to be most aligned to women with sexual dysfunction, but not applicable to women without sexual dysfunction.",
                ),
            ),
            note(
                f"{p}-n7",
                "Erectile Dysfunction as a Marker of Cardiovascular Disease",
                "Why ED may predict cardiovascular disease",
                "ED shares risk factors with CVD and often precedes coronary symptoms by 2–3 years and MACE by 3–5 years; men with ED carry ~1.3–1.6× cardiovascular event risk over 10 years—treat ED workup as cardiometabolic case-finding.",
                ref(
                    "Erectile Dysfunction as a Marker of Cardiovascular Disease",
                    "ED precedes the symptoms of coronary artery disease by 2 to 3 years and major adverse cardiovascular events such as myocardial infarction or stroke by 3 to 5 years.",
                ),
            ),
            note(
                f"{p}-n8",
                "Evaluation of Men With Sexual Dysfunction (Table 18.2 and Box 18.2)",
                "How to screen men presenting with sexual dysfunction",
                "Use open, nonjudgmental prompts; distinguish desire vs erection vs orgasm/ejaculation problems; evaluate partner when relevant; screen for diabetes, CVD, depression, and medication culprits—~25% of impotence is drug-related.",
                ref(
                    "Evaluation of Men With Sexual Dysfunction (Table 18.2 and Box 18.2)",
                    "almost one fourth of all cases of impotence can be attributed to medications.",
                ),
            ),
            note(
                f"{p}-n9",
                "Male Hypoactive Sexual Desire Dysfunction",
                "How to evaluate male hypoactive sexual desire",
                "Diagnose MHSDD only with distressing low desire; exclude testosterone deficiency (morning total ± free T), hyperprolactinemia, SSRIs/antiandrogens/GnRH analogues, systemic illness, and depression—low desire often coexists with ED.",
                ref(
                    "Male Hypoactive Sexual Desire Dysfunction",
                    "Testosterone deficiency is an important, treatable cause of low desire in men and should be excluded by measuring serum total and free testosterone levels.",
                ),
            ),
            note(
                f"{p}-n10",
                "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                "Testosterone domains in male sexual function",
                "Testosterone drives sexual thoughts/desire, attentiveness to erotic cues, and sleep-entrained erections; RCTs show TRT improves desire, erectile function, and overall sexual activity in hypogonadal men but not in eugonadal men with ED.",
                ref(
                    "KEY POINTS",
                    "Testosterone regulates sexual thoughts and desire, sexual arousal, attentiveness to erotic stimuli, and sleep-entrained erections. Testosterone deficiency is a treatable cause of hypoactive sexual desire in men. In randomized trials, testosterone replacement therapy has been shown to improve sexual desire, erectile function, and overall sexual activity in men with hypogonadism.",
                ),
            ),
            note(
                f"{p}-n11",
                "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                "Why testosterone won't fix ED with normal testosterone",
                "Testosterone and ED are often comorbid but mechanistically distinct; PDE5 inhibitors are first-line for ED, whereas testosterone improves sexual function only in unequivocally hypogonadal men and does not augment PDE5i response consistently in trials.",
                ref(
                    "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                    "However, testosterone does not improve erectile response to visual erotic stimuli or erectile function in men with ED who have normal testosterone levels.",
                ),
            ),
            note(
                f"{p}-n12",
                "Diabetes and Sexual Dysfunction in Men",
                "How diabetes impairs erectile physiology",
                "Diabetes causes endothelial dysfunction, reduced eNOS, oxidative stress quenching NO, impaired K⁺ channels, and Rho-kinase–mediated hypercontractility—long-standing disease may render cavernosal tissue unresponsive to PDE5 inhibitors.",
                ref(
                    "Diabetes and Sexual Dysfunction in Men",
                    "Men with long duration of diabetes may not be able to generate sufficient nitric oxide and cGMP within the cavernosal smooth muscle, and consequently, they may become unresponsive to PDE5 inhibitors.",
                ),
            ),
            note(
                f"{p}-n13",
                "Hyperprolactinemia and Sexual Dysfunction",
                "Hyperprolactinemia and male sexual dysfunction",
                "Hyperprolactinemia presents with low libido/ED in up to 75% of macroprolactinoma patients; prolactin suppresses kisspeptin/GnRH → low testosterone, and dopamine-agonist therapy usually improves sexual function.",
                ref(
                    "Hyperprolactinemia and Sexual Dysfunction",
                    "Men with hyperprolactinemia often present with decreased libido or ED; 75% of men with macroprolactinomas and 50% of men with microprolactinomas report reduced sexual desire or ED, and almost all have subnormal nocturnal penile erections.",
                ),
            ),
            note(
                f"{p}-n14",
                "Evaluation of Men With Sexual Dysfunction (Table 18.2 and Box 18.2)",
                "How to structure ED laboratory workup",
                "Initial ED labs: fasting glucose/HbA1c, lipids, morning fasting total testosterone (± free T with LC-MS/MS), and LH if hypogonadal; reserve invasive vascular testing for PDE5i failures referred to specialists.",
                ref(
                    "Evaluation of Men With Sexual Dysfunction (Table 18.2 and Box 18.2)",
                    "The initial laboratory workup in most men presenting with ED usually includes the measurement of hemoglobin, blood glucose and hemoglobin A1C, blood urea nitrogen and creatinine, plasma lipids, and serum total and free testosterone levels (see Box 18.2).",
                ),
            ),
            note(
                f"{p}-n15",
                "Treatment of Erectile Dysfunction",
                "PDE5 inhibitors as ED first-line therapy",
                "Stepwise ED care optimizes comorbid disease, offers psychosexual counseling to all, and uses PDE5 inhibitors first (unless contraindicated); titrate to maximum tolerated dose because many 'failures' reflect underdosing or misuse.",
                ref(
                    "Treatment of Erectile Dysfunction",
                    "The standard of practice today is a stepwise approach that first utilizes minimally invasive therapies that are easy to use and have fewer adverse effects and progresses to more invasive therapies that may require injections or surgical intervention after the first-line choices have been exhausted (Fig. 18.8).",
                ),
            ),
            note(
                f"{p}-n16",
                "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                "How to optimize PDE5 inhibitor response",
                "Counsel on timing (1–2 h before sex for sildenafil/vardenafil), dose titration, food/alcohol effects, need for sexual stimulation, and drug interactions (nitrates, α-blockers, CYP3A4 inhibitors); consider daily low-dose tadalafil after on-demand failure.",
                ref(
                    "Treatment of Patients Who Do Not Respond to Phosphodiesterase-5 Inhibitors",
                    "Some men who do not optimally respond to on-demand PDE5 inhibitors may respond to daily low-dose tadalafil (2.5 or 5 mg), which is an FDA-approved regimen.",
                ),
            ),
            note(
                f"{p}-n17",
                "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                "PDE5 inhibitor cardiovascular cautions",
                "Absolute contraindication: regular nitrate use; relative cautions include unstable CVD, concurrent α-blockers/vasodilators, and recent nonarteritic anterior ischemic optic neuropathy—assess exercise tolerance before prescribing.",
                ref(
                    "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                    "Selective PDE5 inhibitors are contraindicated in men using nitrates on a regular basis, in those with severe heart disease in whom sexual activity may not be safe, and in those with nonarteritic anterior ischemic optic neuropathy.",
                ),
            ),
            note(
                f"{p}-n18",
                "Testosterone Replacement in Androgen-Deficient Men With Erectile Dysfunction",
                "Testosterone in hypogonadal men with ED",
                "TRT improves desire, activity, and erections in hypogonadal men with low libido but not in eugonadal ED; correcting androgen deficiency may still improve satisfaction and address anemia/BMD even when PDE5i is required for rigidity.",
                ref(
                    "Testosterone Replacement in Androgen-Deficient Men With Erectile Dysfunction",
                    "Randomized trials have shown that testosterone replacement therapy improves erectile function, sexual desire, overall sexual activity, and satisfaction with intercourse in hypogonadal men who have low sexual desire",
                ),
            ),
            note(
                f"{p}-n19",
                "Female Sexual Dysfunction",
                "ICD-11 female sexual dysfunction framework",
                "FSD applies only when symptoms cause substantial distress; ICD-11 classifies desire, arousal, and orgasmic dysfunction separately (unlike DSM-5), allows treatment despite attributable causes, and requires symptoms for several months.",
                ref(
                    "KEY POINTS",
                    "For a diagnosis of female sexual dysfunction (FSD), the symptoms need to be episodic or persistent over a period at least several months and associated with clinically significant distress.",
                ),
            ),
            note(
                f"{p}-n20",
                "Epidemiology of FSD",
                "HSDD epidemiology in women",
                "Hypoactive sexual desire dysfunction is the most common FSD; community studies show prevalence peaking at midlife (~33% estimated HSDD by age 40 in Australian data) with partner status and dyspareunia as major contributors.",
                ref(
                    "KEY POINTS",
                    "Hypoactive sexual desire dysfunction (HSDD) is the most common FSD. Other categories of sexual dysfunction in women include arousal and orgasm dysfunction. Sexual pain disorder is generally considered separately.",
                ),
            ),
            note(
                f"{p}-n21",
                "The Role of Hormones in Female Sexual Function",
                "Why dyspareunia drives hypoactive desire",
                "Estrogen insufficiency causes vulvovaginal atrophy with dryness, irritation, and dyspareunia; pain and urinary symptoms reduce desire, arousal, and relationship satisfaction—treat local estrogen before attributing low desire to androgen deficiency alone.",
                ref(
                    "The Role of Hormones in Female Sexual Function",
                    "Dyspareunia and urinary incontinence are both causes of diminished sexual desire, arousal difficulties, relationship problems, and diminished physical and emotional sexual satisfaction.",
                ),
            ),
            note(
                f"{p}-n22",
                "Treatment of Vulvovaginal Atrophy",
                "How to treat dyspareunia from vulvovaginal atrophy",
                "Low-dose vaginal estrogen (pessary, cream, or ring) reverses atrophy safely without routine progestogen; prasterone and ospemifene are alternatives; moisturizers/lubricants are less effective than estrogen for sustained VVA relief.",
                ref(
                    "Treatment of Vulvovaginal Atrophy",
                    "Dyspareunia due to VVA can be effectively and safely treated with low-dose topical vaginal estrogen therapy.",
                ),
            ),
            note(
                f"{p}-n23",
                "Testosterone Therapy for HSDD",
                "Postmenopausal testosterone for HSDD",
                "Transdermal testosterone restoring premenopausal levels is evidence-based for postmenopausal HSDD (not premenopausal FSD); measure total T for baseline/monitoring, trial 3–6 months, stop if no benefit, and avoid compounded pellets/injections.",
                ref(
                    "KEY POINTS",
                    "The most effective hormonal therapy for HSDD in postmenopausal women is physiologic transdermal testosterone therapy.",
                ),
            ),
            note(
                f"{p}-n24",
                "Erectile Dysfunction",
                "How medications cause sexual dysfunction",
                "Common ED culprits: β-blockers, thiazides, SSRIs/tricyclics, antipsychotics, antiandrogens, GnRH analogues, and abiraterone; in women SSRIs/SNRIs, β-blockers, opioids, and antiandrogens similarly impair desire/arousal—always review the medication list.",
                ref(
                    "Erectile Dysfunction",
                    "The drugs commonly associated with erectile dysfunction include antihypertensives such as β-adrenergic blockers and thiazide diuretics; antidepressants such as the SSRIs and tricyclic antidepressants; antipsychotic drugs used to treat schizophrenia; some antihistamines such as diphenhydramine; and medications that inhibit testosterone production, such as GnRH analogues, antiandrogens, and abiraterone, or block androgen action, such as bicalutamide, enzalutamide, darolutamide, and apalutamide.",
                ),
            ),
            note(
                f"{p}-n25",
                "Evaluation of Women With FSD",
                "How to initiate FSD screening in endocrine practice",
                "Proactively ask about sexual well-being; take a biopsychosocial history including relationship, abuse, mood/psychotropics, menstrual status, VVA, dyspareunia, and prolactin symptoms; hormones are not diagnostic biomarkers except when treating with testosterone.",
                ref(
                    "Evaluation of Women With FSD",
                    "As many women will not report their sexual concerns, the conversation often needs to be initiated by the clinician.",
                ),
            ),
            note(
                f"{p}-n26",
                "Prescription Nonhormonal Treatment Options for FSD",
                "Nonhormonal premenopausal HSDD options",
                "Flibanserin (5-HT1A agonist/5-HT2A antagonist) and bremelanotide are approved for premenopausal acquired HSDD in some countries; bupropion and buspirone are used off-label—counsel on hypotension/syncope risk with alcohol (f libanserin).",
                ref(
                    "KEY POINTS",
                    "Nonhormonal therapies for HSDD in premenopausal women include flibanserin and bremelanotide and, for all women, offlabel use of bupropion and buspirone.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                "A 62-year-old with stable angina takes sublingual nitroglycerin PRN and reports new ED. Best initial erectile therapy?",
                [
                    "Avoid PDE5 inhibitors; optimize cardiovascular care and consider non-nitrate alternatives (vacuum device, ICI, counseling)",
                    "Sildenafil 100 mg with nitroglycerin as needed",
                    "Testosterone gel without measuring morning testosterone",
                    "Immediate penile prosthesis",
                ],
                0,
                "PDE5 inhibitors are contraindicated with regular nitrate use because combined vasodilation can cause fatal hypotension; address CVD and choose second-line ED therapies.",
                ref(
                    "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                    "Selective PDE5 inhibitors are contraindicated in men using nitrates on a regular basis, in those with severe heart disease in whom sexual activity may not be safe, and in those with nonarteritic anterior ischemic optic neuropathy.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Evaluation of Men With Sexual Dysfunction (Table 18.2 and Box 18.2)",
                "A 55-year-old man with new ED has nocturnal erections, normal exam, and fasting glucose 118 mg/dL. Most appropriate next step after history?",
                [
                    "Morning fasting total testosterone, lipids, HbA1c, and empiric PDE5 inhibitor trial if no contraindications",
                    "Immediate penile angiography",
                    "Nocturnal penile tumescence recording in all patients",
                    "Start testosterone without repeat morning sample",
                ],
                0,
                "Standard ED workup includes cardiometabolic labs and morning testosterone; invasive testing is reserved for PDE5i nonresponders.",
                ref(
                    "Evaluation of Men With Sexual Dysfunction (Table 18.2 and Box 18.2)",
                    "If the history, physical examination, and laboratory tests do not identify medical problems needing further workup, then a cost-effective approach is to prescribe a trial of oral PDE5 inhibitor provided there are no contraindications (e.g., nitrate use).",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Diabetes and Sexual Dysfunction in Men",
                "A 58-year-old with type 2 diabetes (HbA1c 9.2%) has progressive ED unresponsive to optimized sildenafil dose. Most likely contributing mechanism?",
                [
                    "Endothelial dysfunction with impaired NO/cGMP generation in cavernosal smooth muscle",
                    "Excess testosterone suppressing desire",
                    "Hyperthyroidism causing premature ejaculation only",
                    "Primary hyperparathyroidism",
                ],
                0,
                "Chronic hyperglycemia impairs NO bioavailability and smooth-muscle relaxation, explaining poor PDE5i response in long-standing diabetes.",
                ref(
                    "Diabetes and Sexual Dysfunction in Men",
                    "Men with long duration of diabetes may not be able to generate sufficient nitric oxide and cGMP within the cavernosal smooth muscle, and consequently, they may become unresponsive to PDE5 inhibitors.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Male Hypoactive Sexual Desire Dysfunction",
                "A 48-year-old reports absent sexual fantasies causing marital distress. He takes escitalopram. Testosterone 420 ng/dL (morning). Best next step?",
                [
                    "Evaluate prolactin, depression control, and SSRI contribution; do not start TRT for isolated low desire with normal testosterone",
                    "Start high-dose testosterone immediately",
                    "PDE5 inhibitor monotherapy",
                    "No further workup because DSM-5 excludes medication causes",
                ],
                0,
                "MHSDD requires distressing low desire; exclude reversible causes (SSRIs, prolactin, depression) before androgen therapy when testosterone is normal.",
                ref(
                    "Male Hypoactive Sexual Desire Dysfunction",
                    "Although DSM-5 limits a diagnosis of MHSDD to cause other than medication, illness (including testosterone deficiency and depression), and relationship and addiction problems, in clinical practice, reduced or lack of sexual desire is often associated with multiple factors, including testosterone deficiency, prolactin excess, the use of medications (SSRIs, antiandrogens, GnRH analogues, antihypertensives, cancer chemotherapeutic agents, anticonvulsants), systemic illness, and depression",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Hyperprolactinemia and Sexual Dysfunction",
                "A 35-year-old man has low libido, testosterone 210 ng/dL, LH 2 IU/L, prolactin 180 ng/mL, and bitemporal field loss. Best management?",
                [
                    "Dopamine agonist therapy with pituitary imaging follow-up",
                    "Testosterone alone without treating prolactin",
                    "Varicocele repair",
                    "GnRH agonist therapy",
                ],
                0,
                "Hyperprolactinemia suppresses GnRH; dopamine agonists lower prolactin, shrink adenomas, and usually restore testosterone and sexual function.",
                ref(
                    "Hyperprolactinemia and Sexual Dysfunction",
                    "Erectile function generally improves in hyperprolactinemic men following treatment with dopamine agonists.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                "A 70-year-old with ED has morning testosterone 480 ng/dL on two samples. He asks for testosterone gel to improve erections. Best counseling?",
                [
                    "Testosterone is not shown to improve ED in men with normal testosterone; PDE5 inhibitor is appropriate first-line",
                    "Testosterone reliably augments PDE5 inhibitors in all men with ED",
                    "Testosterone cures ejaculatory disorders",
                    "No therapy exists for ED when testosterone is normal",
                ],
                0,
                "TRT benefits sexual function in unequivocal hypogonadism but not eugonadal ED; PDE5 inhibitors remain first-line.",
                ref(
                    "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                    "However, testosterone does not improve erectile response to visual erotic stimuli or erectile function in men with ED who have normal testosterone levels.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Erectile Dysfunction as a Marker of Cardiovascular Disease",
                "A 52-year-old nonsmoker develops ED over 6 months without chest pain. No diabetes. Best cardiovascular approach?",
                [
                    "Treat ED as a CVD risk marker—optimize risk factors and assess exercise tolerance before PDE5i",
                    "Ignore ED because it never relates to coronary disease",
                    "Defer all cardiac assessment until MI occurs",
                    "Withhold all ED therapy in every man over 50",
                ],
                0,
                "ED precedes symptomatic CAD and shares pathophysiology; baseline cardiometabolic screening is recommended when treating ED.",
                ref(
                    "Erectile Dysfunction as a Marker of Cardiovascular Disease",
                    "Men reporting ED are 1.3 to 1.6 times more likely to experience a cardiovascular event within 10 years than men without ED.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Treatment of Patients Who Do Not Respond to Phosphodiesterase-5 Inhibitors",
                "A man reports sildenafil 'doesn't work.' He took 50 mg immediately before intercourse after a large fatty meal without foreplay. Best adjustment?",
                [
                    "Counsel on 1–2 h pre-dose timing, dose titration to 100 mg, need for sexual stimulation, and food effects",
                    "Diagnose venous leak and proceed to prosthesis without retry",
                    "Add daily nitroglycerin to enhance effect",
                    "Switch to methyltestosterone orally",
                ],
                0,
                "Many PDE5i failures reflect misuse—timing, dose, stimulation, and meals—not true organic nonresponse.",
                ref(
                    "Treatment of Patients Who Do Not Respond to Phosphodiesterase-5 Inhibitors",
                    "Patients may not take the medication appropriately because of inadequate instructions, failure to understand the instructions, adverse effects, or fear of adverse effects.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Testosterone Deficiency Syndromes",
                "A 44-year-old on methadone has low libido, testosterone 230 ng/dL, LH 1.5 IU/L. Before TRT, best step?",
                [
                    "Confirm hypogonadism and address opioid cause; consider TRT if opioid cannot be stopped",
                    "Assume primary testicular failure and order karyotype first",
                    "Start finasteride for hair loss",
                    "Ignore hypogonadism because opioids are short-acting",
                ],
                0,
                "Chronic opioids suppress GnRH; testosterone deficiency is treatable when discontinuation is not feasible.",
                ref(
                    "Testosterone Deficiency Syndromes",
                    "Opioid use has emerged as an important cause of testosterone deficiency and sexual dysfunction.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Sexual Dysfunction in Patients With Thyroid Disease",
                "A 40-year-old man with new hypothyroidism reports low desire and delayed ejaculation. TSH 28 mIU/L. After levothyroxine, you expect:",
                [
                    "Improvement in sexual symptoms as euthyroidism is restored",
                    "Permanent ED requiring prosthesis regardless of thyroid treatment",
                    "Worsening premature ejaculation from levothyroxine",
                    "No relationship between thyroid disease and sexual function",
                ],
                0,
                "Majority of hypothyroid men report desire/erection/ejaculation problems that correct after thyroid hormone replacement.",
                ref(
                    "Sexual Dysfunction in Patients With Thyroid Disease",
                    "A majority of men with hypothyroidism report hypoactive sexual desire, ED, and delayed ejaculation, which are corrected in most patients after thyroid hormone replacement.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Treatment of Vulvovaginal Atrophy",
                "A 58-year-old postmenopausal woman has severe dyspareunia and vaginal dryness. No breast cancer history. Best first-line therapy?",
                [
                    "Low-dose vaginal estrogen",
                    "Systemic testosterone for all postmenopausal women with pain",
                    "Oral conjugated estrogen without progestogen in intact uterus",
                    "Reassurance only—VVA is untreatable",
                ],
                0,
                "Topical vaginal estrogen effectively treats VVA-related dyspareunia without routine systemic progestogen.",
                ref(
                    "Treatment of Vulvovaginal Atrophy",
                    "Dyspareunia due to VVA can be effectively and safely treated with low-dose topical vaginal estrogen therapy.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Testosterone Therapy for HSDD",
                "A 54-year-old postmenopausal woman on transdermal estradiol has distressing low desire meeting HSDD criteria. Total testosterone is normal for age. Next step?",
                [
                    "Trial physiologic transdermal testosterone with baseline and monitoring total testosterone",
                    "Diagnose androgen deficiency from a low female testosterone cutoff",
                    "Start intramuscular testosterone pellets",
                    "Measure testosterone to diagnose deficiency before any consideration of therapy",
                ],
                0,
                "Postmenopausal HSDD is the evidence-based indication for transdermal testosterone; measure total T for baseline/monitoring, not diagnosis.",
                ref(
                    "Investigations",
                    "Testosterone should only be measured to provide a baseline if testosterone therapy is to be initiated, not for a diagnostic purpose, as there is no level of testosterone below which a woman can be considered to be deficient.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Endocrine Therapy for Breast Cancer",
                "A 60-year-old on an aromatase inhibitor for breast cancer has dyspareunia and low desire. She asks about local estrogen. Best counseling?",
                [
                    "Vaginal estrogen is generally contraindicated on aromatase inhibitors; discuss prasterone, ospemifene, lubricants, and oncology input",
                    "High-dose systemic estrogen without oncology review",
                    "Testosterone pellets are first-line in all breast cancer survivors",
                    "No treatment exists for AI-associated VVA",
                ],
                0,
                "Aromatase inhibitors cause estrogen depletion and VVA; vaginal estrogen is usually avoided on AI therapy—nonhormonal and selected alternatives require individualized risk discussion.",
                ref(
                    "Treatment of Vulvovaginal Atrophy",
                    "Although vaginal estrogen therapy has not been associated with a greater risk of disease recurrence or mortality after breast cancer, it is generally considered contraindicated for women on aromatase inhibitor therapy.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Prescription Nonhormonal Treatment Options for FSD",
                "A 38-year-old premenopausal woman has acquired generalized HSDD. She drinks wine with dinner. Which therapy requires strict alcohol counseling?",
                [
                    "Flibanserin 100 mg at bedtime",
                    "Transdermal testosterone cream",
                    "Vaginal estradiol pessary",
                    "Daily tadalafil for HSDD",
                ],
                0,
                "Flibanserin is approved for premenopausal HSDD but carries hypotension/syncope risk with alcohol and CYP3A4 inhibitors.",
                ref(
                    "Prescription Nonhormonal Treatment Options for FSD",
                    "It is prescribed as a daily oral dose of 100 mg taken at bedtime, with the warning of potentially severe hypotension and syncope in women who, while taking the medication, consume alcohol within 2 hours, are taking a moderate or strong CYP3A4 inhibitor, and have liver impairment.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Hyperprolactinemia and Sexual Dysfunction",
                "A 32-year-old woman with amenorrhea and galactorrhea reports absent desire. Prolactin 95 ng/mL. First-line endocrine test besides prolactin?",
                [
                    "Already indicated—treat hyperprolactinemia; evaluate pituitary cause",
                    "Serum testosterone to diagnose female androgen deficiency",
                    "No evaluation—prolactin never affects female sexuality",
                    "Immediate bilateral oophorectomy",
                ],
                0,
                "Hyperprolactinemia commonly presents with amenorrhea and diminished desire; prolactin should be first-line in sexual dysfunction with amenorrhea/galactorrhea.",
                ref(
                    "Hyperprolactinemia",
                    "Serum prolactin should be a first-line investigation in women presenting with sexual dysfunction and amenorrhea and/or galactorrhea.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Lower Urinary Tract Symptoms and Erectile Dysfunction",
                "A 66-year-old with LUTS on tamsulosin develops delayed ejaculation but wants ED treatment. Counseling should include:",
                [
                    "PDE5 inhibitors may be used with α-blockers with blood pressure monitoring; tamsulosin itself can delay ejaculation",
                    "PDE5 inhibitors are absolutely contraindicated with any α-blocker",
                    "Stop tamsulosin and start finasteride to improve ejaculation always",
                    "ED and LUTS are never related",
                ],
                0,
                "LUTS and ED share pathophysiology; selective α-blockers cause ejaculatory dysfunction yet trials support cautious combined use of PDE5i and α-blockers with BP monitoring.",
                ref(
                    "Lower Urinary Tract Symptoms and Erectile Dysfunction",
                    "Second, there may be interactions between drugs used in the treatment of ED (PDE5 inhibitors) and LUTS (α-adrenergic blockers), both of which may lower blood pressure.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Retrograde Ejaculation",
                "A 50-year-old man with long-standing type 1 diabetes has dry orgasm and infertility. Most likely diagnosis?",
                [
                    "Retrograde ejaculation from autonomic neuropathy",
                    "Premature ejaculation",
                    "Klinefelter syndrome",
                    "Psychogenic anorgasmia only",
                ],
                0,
                "Diabetic autonomic neuropathy commonly causes retrograde ejaculation—semen enters bladder rather than urethra.",
                ref(
                    "Retrograde Ejaculation",
                    "Retrograde ejaculation due to diabetes-associated autonomic neuropathy is the second most prevalent ejaculatory disorder.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Treatment of Hypoactive Sexual Desire in Men",
                "A hypogonadal man (testosterone 180 ng/dL ×2) has low desire and ED. PDE5i helps rigidity but desire remains low. Best add-on?",
                [
                    "Testosterone replacement after shared decision-making and monitoring",
                    "Increase PDE5i dose only",
                    "Flibanserin (FDA-approved for men)",
                    "Spironolactone",
                ],
                0,
                "Testosterone improves desire and overall sexual activity in hypogonadal men; consider TRT when desire remains impaired despite PDE5i.",
                ref(
                    "Treatment of Hypoactive Sexual Desire in Men",
                    "Testosterone therapy should be considered in men with HSDD who have testosterone deficiency.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Endocrine Causes of FSD",
                "A 28-year-old with PCOS and obesity reports low arousal. Before attributing symptoms to hyperandrogenism, consider:",
                [
                    "Psychological impact of obesity/hyperandrogenism and comorbid mood disorders",
                    "That PCOS always causes high desire",
                    "That serum testosterone diagnostic cutoffs define FSD",
                    "That endocrine causes never contribute to FSD",
                ],
                0,
                "PCOS sexual difficulties may reflect psychological burden of obesity/hyperandrogenism; endocrine and psychosocial contributors overlap.",
                ref(
                    "Polycystic Ovarian Syndrome",
                    "It has been suggested that the psychological impact of obesity and hyperandrogenism in women with PCOS may contribute to sexual difficulties.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                "A man on ritonavir-based ART needs ED therapy. Adjustment for sildenafil?",
                [
                    "Reduce PDE5 inhibitor dose because of CYP3A4 interaction",
                    "Double sildenafil dose because ritonavir induces metabolism",
                    "Add nitroglycerin to overcome interaction",
                    "No interaction between PDE5 inhibitors and protease inhibitors",
                ],
                0,
                "Protease inhibitors inhibit CYP3A4 and raise PDE5 inhibitor levels—dose reduction is required.",
                ref(
                    "Drug-Drug Interactions",
                    "Therefore, the doses of PDE5 inhibitors should be reduced appropriately in men taking protease inhibitors or erythromycin.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Female Sexual Dysfunction",
                "A single 45-year-old woman reports low desire with distress for 8 months. She is unpartnered. Appropriate approach?",
                [
                    "Diagnose and treat FSD if criteria met—partnering is not required",
                    "Decline evaluation because she is not partnered",
                    "Require 75% failure rate on every encounter per DSM-5 only",
                    "Measure testosterone to confirm androgen deficiency syndrome",
                ],
                0,
                "ICD-11/Williams emphasize women need not be partnered to experience or receive treatment for sexual dysfunction.",
                ref(
                    "KEY POINTS",
                    "There is no normative standard for female sexual function, and women do not need to be partnered to be negatively affected by, or receive treatment for, sexual dysfunction.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Sexual Dysfunction in Men With Metabolic Syndrome",
                "A 49-year-old obese man has metabolic syndrome and new ED. Lifestyle intervention is advised because:",
                [
                    "Aerobic exercise of moderate/high intensity improves erectile function",
                    "Exercise worsens endothelial function",
                    "Metabolic syndrome never associates with ED",
                    "Only surgery improves ED in metabolic syndrome",
                ],
                0,
                "Physical activity interventions, especially aerobic exercise, are associated with improved erectile function alongside cardiometabolic risk reduction.",
                ref(
                    "Erectile Dysfunction",
                    "Physical activity and exercise interventions, particularly aerobic exercise of moderate or high intensity, are associated with improvements in erectile function.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Management of FSD",
                "A postmenopausal woman with HSDD and bothersome hot flashes. Before testosterone, consider:",
                [
                    "Systemic MHT for vasomotor symptoms which may improve sexual well-being",
                    "Testosterone as sole therapy for hot flashes",
                    "Avoid all hormonal therapy in every postmenopausal woman",
                    "Ospemifene as first-line for hot flashes",
                ],
                0,
                "Relief of vasomotor symptoms and sleep with systemic MHT may substantially reduce FSD symptoms before adding testosterone for HSDD.",
                ref(
                    "Management of FSD",
                    "For example, relief of vasomotor and VVA symptoms, and improvement in sleep with systemic menopausal hormone therapy, may result in substantial reduction in FSD symptoms in postmenopausal women.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Delayed Ejaculation",
                "A 55-year-old on paroxetine reports inability to ejaculate during intercourse. Best management option?",
                [
                    "Consider SSRI dose adjustment/switch or timed dosing strategies; SSRIs commonly delay ejaculation",
                    "Start testosterone to shorten ejaculatory latency",
                    "Emergency penile prosthesis",
                    "Ignore because SSRIs never affect ejaculation",
                ],
                0,
                "SSRIs prolong intravaginal ejaculatory latency and cause delayed ejaculation—medication review is central.",
                ref(
                    "Delayed Ejaculation",
                    "SSRIs can prolong intravaginal ejaculatory latency and cause delayed ejaculation in some middle-age and older men.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Endocrine Causes of FSD",
                "A 34-year-old woman with primary adrenal insufficiency reports low desire and arousal. Androgen status?",
                [
                    "Relative testosterone insufficiency from adrenal failure may contribute—consider replacement strategies",
                    "Adrenal insufficiency never affects sexual function",
                    "Only orgasm is impaired in adrenal insufficiency",
                    "DHEA supplementation is proven first-line for all FSD",
                ],
                0,
                "Adrenal insufficiency reduces adrenal androgen precursors; sexual difficulties are more common than in controls.",
                ref(
                    "Adrenal Insufficiency",
                    "The prevalence of sexual difficulties in women with primary adrenal insufficiency has been reported as being greater than in controls (68.2% vs. 8.7%, respectively) with more women with adrenal insufficiency reporting sexually related personal distress (45.5% vs. 8.7%).",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Treatment of Erectile Dysfunction",
                "A man with ED and well-controlled hypertension on losartan asks about first-line therapy. Best recommendation?",
                [
                    "PDE5 inhibitor with counseling on timing, dose titration, and blood pressure monitoring",
                    "β-blocker upgrade because ACE inhibitors/ARBs are most implicated in ED",
                    "Avoid all ED drugs in treated hypertension",
                    "Testosterone in every hypertensive man with ED",
                ],
                0,
                "PDE5 inhibitors are first-line; ACE inhibitors/ARBs have lower sexual adverse-event rates than many antihypertensives.",
                ref(
                    "Treatment of Erectile Dysfunction",
                    "This strategy is not always feasible, because almost all antihypertensive agents have been associated with sexual dysfunction; the frequency of this adverse event is less with angiotensin-converting enzyme inhibitors and angiotensin-receptor blockers than with other agents.",
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
                "Penile erection requires cavernosal smooth muscle relaxation, increased arterial inflow, and venous occlusion.",
                True,
                "KEY POINTS describe the biochemical and hemodynamic sequence culminating in engorgement and rigidity.",
                ref(
                    "KEY POINTS",
                    "Penile erection results from biochemical and hemodynamic events that are associated with activation of central nervous system sites, cavernosal smooth muscle relaxation, increased blood flow into cavernosal sinuses, and venous occlusion.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                "PDE5 inhibitors produce erections without any sexual stimulation.",
                False,
                "They restore the natural erectile response to stimulation but do not cause erections in its absence.",
                ref(
                    "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                    "PDE5 inhibitors restore the natural erectile response to sexual stimulation but do not produce an erection in the absence of sexual stimulation.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Erectile Dysfunction",
                "Diabetes mellitus is a major risk factor for erectile dysfunction.",
                True,
                "MMAS showed threefold higher complete ED risk with treated diabetes; up to 50% of diabetic men develop ED.",
                ref(
                    "Erectile Dysfunction",
                    "Among the chronic diseases associated with ED, diabetes mellitus is one of the most important risk factors.",
                ),
            ),
            tf(
                f"{p}-t4",
                "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                "Testosterone replacement improves erectile function in men with ED who have normal testosterone levels.",
                False,
                "RCTs show no benefit of testosterone on erectile function in eugonadal men with ED.",
                ref(
                    "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                    "testosterone does not improve erectile response to visual erotic stimuli or erectile function in men with ED who have normal testosterone levels.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Female Sexual Dysfunction",
                "Hypoactive sexual desire dysfunction is the most common female sexual dysfunction.",
                True,
                "KEY POINTS and epidemiology sections identify HSDD as the predominant FSD category.",
                ref(
                    "KEY POINTS",
                    "Hypoactive sexual desire dysfunction (HSDD) is the most common FSD.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Investigations",
                "A low serum testosterone level can diagnose androgen deficiency in women with sexual dysfunction.",
                False,
                "There is no testosterone cutoff defining deficiency in women; measure only for baseline/monitoring when initiating therapy.",
                ref(
                    "Investigations",
                    "Testosterone should only be measured to provide a baseline if testosterone therapy is to be initiated, not for a diagnostic purpose, as there is no level of testosterone below which a woman can be considered to be deficient.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Treatment of Vulvovaginal Atrophy",
                "Low-dose vaginal estrogen effectively treats dyspareunia due to vulvovaginal atrophy.",
                True,
                "Topical estrogen reverses atrophy and is first-line for VVA-related pain.",
                ref(
                    "Treatment of Vulvovaginal Atrophy",
                    "Dyspareunia due to VVA can be effectively and safely treated with low-dose topical vaginal estrogen therapy.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Hyperprolactinemia and Sexual Dysfunction",
                "Hyperprolactinemia affects up to 5% of men presenting with erectile dysfunction.",
                True,
                "Chapter cites 1–5% of men with ED have hyperprolactinemia, some from prolactinomas.",
                ref(
                    "Hyperprolactinemia and Sexual Dysfunction",
                    "Hyperprolactinemia affects 1% to 5% of men presenting with ED",
                ),
            ),
            tf(
                f"{p}-t9",
                "KEY POINTS",
                "Any condition causing sex hormone insufficiency may contribute to female sexual dysfunction.",
                True,
                "KEY POINTS list ovarian/adrenal insufficiency, hypopituitarism, hyperprolactinemia, diabetes, PCOS, and thyroid disease.",
                ref(
                    "KEY POINTS",
                    "Any condition that causes sex hormone insufficiency may contribute to FSD, including ovarian insufficiency due to spontaneous or iatrogenic causes, adrenal insufficiency, hypopituitarism, and hyperprolactinemia.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Testosterone Therapy for HSDD",
                "Oral testosterone is recommended for women with hypoactive sexual desire dysfunction.",
                False,
                "Task force recommends transdermal testosterone; oral therapy is not recommended because of lipoprotein effects and inconsistent absorption.",
                ref(
                    "Testosterone Therapy for HSDD",
                    "Oral testosterone therapy is not recommended because of potential adverse lipoprotein effects and inconsistent absorption.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Erectile Dysfunction as a Marker of Cardiovascular Disease",
                "Erectile dysfunction may precede symptomatic coronary artery disease by 2 to 3 years.",
                True,
                "Shared risk factors and endothelial dysfunction link ED and CAD temporally.",
                ref(
                    "Erectile Dysfunction as a Marker of Cardiovascular Disease",
                    "ED precedes the symptoms of coronary artery disease by 2 to 3 years",
                ),
            ),
            tf(
                f"{p}-t12",
                "Prescription Nonhormonal Treatment Options for FSD",
                "Flibanserin is approved for premenopausal women with hypoactive sexual desire dysfunction in some countries.",
                True,
                "Flibanserin has approval for premenopausal generalized acquired HSDD where regulators have accepted the indication.",
                ref(
                    "Prescription Nonhormonal Treatment Options for FSD",
                    "filbanserin has only been approved for the treatment of premenopausal women with generalized, acquired HSDD in some countries.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Evaluation of Men With Sexual Dysfunction (Table 18.2 and Box 18.2)",
                "Further invasive urologic testing is required in all men with newly diagnosed erectile dysfunction.",
                False,
                "Invasive testing is limited to PDE5 inhibitor nonresponders referred for specialist evaluation.",
                ref(
                    "Evaluation of Men With Sexual Dysfunction (Table 18.2 and Box 18.2)",
                    "Further evaluation using more invasive diagnostic testing is limited to those men who do not respond to an empiric trial of oral PDE5 inhibitors; these patients should be referred to a specialist for detailed urologic evaluation.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                "Assertion: PDE5 inhibitors are first-line therapy for erectile dysfunction.",
                "Reason: PDE5 inhibitors block degradation of cGMP in corpora cavernosa.",
                0,
                "Both true—selectivity for the NO/cGMP pathway underlies first-line efficacy.",
                ref(
                    "KEY POINTS",
                    "Selective phosphodiesterase-5 inhibitors are safe and effective and have emerged as first-line therapy for men with erectile dysfunction.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                "Assertion: Testosterone therapy should be considered for men with low desire and testosterone deficiency.",
                "Reason: Testosterone improves ejaculatory disorders in all hypogonadal men.",
                2,
                "Assertion true; reason false—testosterone has not been shown to improve ejaculatory dysfunction.",
                ref(
                    "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                    "Testosterone does not improve ejaculatory function in men with ejaculatory dysfunction and low testosterone levels.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Erectile Dysfunction as a Marker of Cardiovascular Disease",
                "Assertion: Men with erectile dysfunction have increased cardiovascular risk.",
                "Reason: Erectile dysfunction and coronary artery disease share common risk factors such as diabetes and smoking.",
                0,
                "Both true—shared risk factors and pathophysiology explain predictive value.",
                ref(
                    "Erectile Dysfunction as a Marker of Cardiovascular Disease",
                    "CVD and ED share common risk factors, such as diabetes mellitus, obesity, hypertension, smoking, and dyslipidemia.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Male Hypoactive Sexual Desire Dysfunction",
                "Assertion: Testosterone deficiency should be excluded in men with low sexual desire.",
                "Reason: Low sexual desire is always pathologic regardless of context.",
                2,
                "Assertion true; reason false—low desire may be adaptive and diagnosis requires distress.",
                ref(
                    "Male Hypoactive Sexual Desire Dysfunction",
                    "A diagnosis of MHSDD is appropriate only if the person reports distress due to low sexual desire.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Diabetes and Sexual Dysfunction in Men",
                "Assertion: Men with diabetes are at high risk of erectile dysfunction.",
                "Reason: Diabetes improves nitric oxide generation in cavernosal smooth muscle.",
                2,
                "Assertion true; reason false—diabetes impairs NO/cGMP pathways.",
                ref(
                    "Diabetes and Sexual Dysfunction in Men",
                    "The prevalence of ED in men with diabetes increases with age and has been reported to be as high as 75% in some studies.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Hyperprolactinemia and Sexual Dysfunction",
                "Assertion: Hyperprolactinemia commonly causes low testosterone in men.",
                "Reason: Prolactin stimulates pulsatile GnRH secretion.",
                2,
                "Assertion true; reason false—prolactin suppresses kisspeptin/GnRH and lowers gonadotropins.",
                ref(
                    "Hyperprolactinemia and Sexual Dysfunction",
                    "Prolactin lowers testosterone levels through its inhibitory effects on GnRH secretion.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Female Sexual Dysfunction",
                "Assertion: Female sexual dysfunction requires clinically significant distress.",
                "Reason: ICD-11 requires symptoms for at least several months with distress.",
                0,
                "Both true—duration and distress criteria define FSD.",
                ref(
                    "KEY POINTS",
                    "For a diagnosis of female sexual dysfunction (FSD), the symptoms need to be episodic or persistent over a period at least several months and associated with clinically significant distress.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Testosterone Therapy for HSDD",
                "Assertion: Transdermal testosterone is effective for postmenopausal hypoactive sexual desire dysfunction.",
                "Reason: Blood testosterone levels diagnose female androgen deficiency.",
                2,
                "Assertion true per task force; reason false—no diagnostic testosterone cutoff exists in women.",
                ref(
                    "Testosterone Therapy for HSDD",
                    "Blood testosterone levels should not be used to diagnose low testosterone in women.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Treatment of Vulvovaginal Atrophy",
                "Assertion: Vaginal estrogen relieves dyspareunia from vulvovaginal atrophy.",
                "Reason: Vaginal moisturizers are more effective than estrogen for all VVA symptoms.",
                2,
                "Assertion true; reason false—moisturizers are less effective than vaginal estrogen.",
                ref(
                    "Treatment of Vulvovaginal Atrophy",
                    "While these topical therapies hydrate the vaginal mucosa and decrease vaginal pH, they are less effective than vaginal estrogen therapy for VVA symptoms.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Selective Phosphodiesterase-5 Inhibitors (Table 18.3 and Box 18.4)",
                "Assertion: PDE5 inhibitors are contraindicated with regular nitrate use.",
                "Reason: Combined vasodilation from nitrates and PDE5 inhibitors can cause severe hypotension.",
                0,
                "Both true—nitrate interaction is the most serious drug-drug concern.",
                ref(
                    "Drug-Drug Interactions",
                    "Concomitant administration of the two vasodilator drugs can cause a potentially fatal decrease in blood pressure.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Endocrine Causes of FSD",
                "Assertion: Endocrine disorders such as hypopituitarism may cause female sexual dysfunction.",
                "Reason: Hypopituitarism only affects orgasm, not desire or arousal.",
                2,
                "Assertion true; reason false—hypopituitarism causes combined estrogen/androgen deficiency with broad sexual dysfunction.",
                ref(
                    "Hypopituitarism",
                    "Sexual dysfunction has been reported in over 90% of women with hypopituitarism due to Sheehan syndrome.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                "Assertion: Adding testosterone to optimized PDE5 inhibitor therapy has not consistently improved erectile function in RCTs.",
                "Reason: Testosterone always synergizes with PDE5 inhibitors regardless of baseline testosterone.",
                2,
                "Assertion true per Spitzer/TADTEST trials; reason false—combined therapy not superior in primary analyses.",
                ref(
                    "The Role of Testosterone in Regulating Sexual Function in Men (Box 18.1)",
                    "Thus, randomized trials have failed to support the hypothesis that addition of testosterone to PDE5 inhibitor improves erectile function in men with ED.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "18",
        "title": "Sexual Function and Dysfunction",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Shalender Bhasin and Susan R. Davis",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_18_Sexual_Function_and_Dysfunction.md",
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
