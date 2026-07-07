#!/usr/bin/env python3
"""Generate Williams 15e module w15-03 — Genetics of Endocrinology."""
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
OUT_NAME = "w15-03_Genetics_of_Endocrinology.json"


def build() -> dict:
    p = "w15-03"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "Genetic architecture",
                "Three axes defining genetic architecture",
                "The genetic basis of each heritable endocrine disease or trait is quantified by genetic architecture: the number of genetic variants and genes involved, their frequency in the population, and their respective contributions to disease risk or phenotypic variation.",
                ref(
                    "KEY POINTS",
                    "The genetic basis of each heritable endocrine disease/trait is quantified by its genetic architecture: (1) the number of genetic variants/genes, (2) their frequency in the population, and (3) their respective contributions to disease risk/phenotypic variation.",
                ),
            ),
            note(
                f"{p}-n2",
                "Monogenic disease",
                "Why Mendelian variants explain most risk in one individual",
                "Mendelian endocrine disorders arise from rare variants in relatively few genes, each with a large individual effect so that in any one person most disease risk is explained by variants in a single gene. Penetrance can be high but is not always complete.",
                ref(
                    "KEY POINTS",
                    "Mendelian endocrine disorders are caused by variants found rarely in the general population, usually from a relatively small number of genes, and each variant has a large individual effect on disease risk so that in any one individual, most of the disease risk is explained by variants in a single gene (monogenic). Mendelian variants can be highly penetrant, but this is not always the case.",
                ),
            ),
            note(
                f"{p}-n3",
                "Polygenic disease",
                "Why polygenic phenotypes result from many genes",
                "Common endocrine diseases and traits such as stature, obesity, type 2 diabetes, and serum lipids reflect combined effects of many variants in many genes, often common in the population, each contributing a small individual effect so the phenotype in any one individual results from variants in many different genes.",
                ref(
                    "KEY POINTS",
                    "Common endocrine diseases/traits such as stature, obesity, type 2 diabetes (T2D), and serum lipids are the result of combined, simultaneous effects of many variants in many genes, often found frequently in the general population, and with each variant contributing a small individual effect so that the phenotype in any one individual results from variants in many different genes (polygenic).",
                ),
            ),
            note(
                f"{p}-n4",
                "NGS technologies",
                "WES and WGS with next-generation sequencing",
                "Whole exome sequencing captures nearly every variant in protein-coding genes; whole genome sequencing covers the entire genome. Revolutionary advances in next-generation sequencing make both feasible, though interpretation lags behind variant detection.",
                ref(
                    "The Role of Genetics in Endocrinology",
                    "Moreover, it is now feasible to identify nearly every genetic variant in an individual's protein-coding genes with whole exome sequencing (WES) or in their entire genome with whole genome sequencing (WGS) due to revolutionary advances in sequencing technologies (collectively referred to as next generation sequencing [NGS]).",
                ),
            ),
            note(
                f"{p}-n5",
                "Precision medicine limits",
                "Why variant interpretation lags behind sequencing capacity",
                "Although sequencing can be standardized and automated, drawing valid clinically useful conclusions requires integration with patient history, physical examination, biochemical studies, and other laboratory examinations of candidate variants. Clinicians must understand both the power and the limits of genetic information.",
                ref(
                    "KEY POINTS",
                    "Comprehensive genetic testing (i.e., exome or genome sequencing) can be standardized and automated. However, drawing valid and clinically useful conclusions requires integration with patient history, physical examination, biochemical studies, and other laboratory examinations of the candidate variants.",
                ),
            ),
            note(
                f"{p}-n6",
                "Variant databases",
                "gnomAD, ClinVar, and population reference data",
                "Ongoing projects including the Genome Aggregation Database integrated with ExAC, UK Biobank, ClinVar, and Decipher are growing exponentially, increasing demand for methods to distinguish pathologic or likely pathologic variants from benign ones.",
                ref(
                    "The Role of Genetics in Endocrinology",
                    "Ongoing projects include the Genome Aggregation Database (gnomAD) integrated with Exome Aggregation Consortium (ExAC), United Kingdom Biobank, the National Center for Biotechnology Information's Single Nucleotide Polymorphism Database/ClinVar, and Decipher.",
                ),
            ),
            note(
                f"{p}-n7",
                "Heritability",
                "How heritability guides genetic interpretation",
                "Heritability quantifies as a proportion how much familial resemblance is due to genetic factors. Most clinically important endocrine traits range from 20% to 80%. Genetic factors are less influential for low-heritability traits and more predictive for high-heritability traits.",
                ref(
                    "Heritability: An Estimate of the Importance of Genetic Factors to Disease Causation",
                    "Appreciating the heritability of a trait is important when interpreting the contribution of genetic risk factors in disease: genetic factors are less influential for traits with low heritability and are likely to have more predictive or explanatory power for traits with high heritability.",
                ),
            ),
            note(
                f"{p}-n8",
                "Twin studies",
                "How twin concordance estimates heritability",
                "The classic approach compares monozygotic and dizygotic twin concordance rates: excess disease correlation in genetically identical twins compared with twins sharing 50% of genes points to genetic factors, assuming comparable environmental effects.",
                ref(
                    "Heritability: An Estimate of the Importance of Genetic Factors to Disease Causation",
                    "Such studies relied on the rationale that an excess of disease correlation between genetically identical individuals (monozygotic twin pairs) compared with those who share only 50% of their genes (digyotic twin pairs) pointed to the role of genetic factors.",
                ),
            ),
            note(
                f"{p}-n9",
                "Gene-environment interaction",
                "Karelia T1D rates and heritability context",
                "After Karelia was divided in 1940, Finnish Karelians developed sixfold higher T1D rates than Russian Karelians despite shared ancestry and likely similar genetic risk. Heritability estimates therefore depend on population, period, and environment—not a fixed property of disease.",
                ref(
                    "Heritability: An Estimate of the Importance of Genetic Factors to Disease Causation",
                    "Finnish Karelians have a sixfold increased rate of T1D compared with Russian Karelians. As a result, heritability for T1D will be different when estimated in the combined Karelian populations than when estimated in Finnish or Russian Karelians alone.",
                ),
            ),
            note(
                f"{p}-n10",
                "Sequence variation types",
                "SNPs, indels, and CNVs in the human genome",
                "About 1 in 1000 base pairs differ between any two human genomes. Common variation includes SNPs and indels; larger copy number variants may require chromosomal microarrays though WGS CNV detection is improving.",
                ref(
                    "Human DNA Sequence Variation: Molecular Forms and Biologic Effects",
                    "When comparing two versions of a human genome, either within the same person or between two different people, about 1/1000 of these bases vary (i.e., 99.9% of them are the same) (Table 3.2).",
                ),
            ),
            note(
                f"{p}-n11",
                "Coding SNP effects",
                "How missense and nonsense SNPs alter proteins",
                "Synonymous SNPs usually preserve amino acid sequence; missense SNPs such as HFE C282Y alter a single amino acid; nonsense SNPs introduce stop codons causing premature termination, nonsense-mediated decay, or truncated nonfunctional protein.",
                ref(
                    "Human DNA Sequence Variation: Molecular Forms and Biologic Effects",
                    "SNPs can be nonsynonymous (missense) changes (alteration of a single amino acid in a protein-coding gene), as is the case of the C282Y mutation in the HFE gene responsible for autosomal recessive hereditary hemochromatosis (see Chapter 17).",
                ),
            ),
            note(
                f"{p}-n12",
                "Splice-site mutations",
                "How GH1 splice donor mutations cause type II IGHD",
                "The most common cause of autosomal dominant isolated GH deficiency (type II IGHD) is single-base mutations inactivating the intron 3 splice donor site of GH1, causing exon 3 skipping and increased production of inactive 17 kDa GH isoform.",
                ref(
                    "Human DNA Sequence Variation: Molecular Forms and Biologic Effects",
                    "the most common cause of autosomal dominant isolated growth hormone (GH) deficiency (type II IGHD) is single-base mutations that inactivate a splice donor site of intron 3 in the GH1 gene, causing skipping of exon 3 in GH1 (see Chapter 22) that result in increased production of inactive 17 kDa GH isoform.",
                ),
            ),
            note(
                f"{p}-n13",
                "Frameshift and structural variants",
                "Indels, frameshifts, and CYP11B1 translocation",
                "Frameshift indels alter every subsequent codon with profound consequences—classic salt-wasting CAH often results from frameshift deletions in CYP21A2. Structural variation including translocations causes familial hyperaldosteronism type 1 by misplacing the CYP11B1 promoter adjacent to CYP11B2.",
                ref(
                    "Human DNA Sequence Variation: Molecular Forms and Biologic Effects",
                    "Structural variation causes familial hyperaldosteronism type 1; the adrenocorticotropic hormone (ACTH, corticotropin)-responsive promoter of the CYP11B1 gene is incorrectly located adjacent to the aldosterone synthase gene (CYP11B2), causing aldosterone to be produced by ACTH stimulation (see Chapter 14).",
                ),
            ),
            note(
                f"{p}-n14",
                "Penetrance and expressivity",
                "Why penetrance differs from expressivity",
                "Penetrance is the proportion of variant carriers who exhibit the phenotype; expressivity is the range of phenotypic severity among carriers of the same genotype. Both are modified by genetic background, environment, and chance.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "A common observation in members of a family carrying the same disease-causing genetic variant is that not all members of the family are equally affected. This range of phenotypic expression resulting from a particular genotype is referred to as variable expressivity and, as with penetrance, arises from the range of impacts of specific variants, as well as modifying influences of genetic background (gene-gene interactions), environment (gene-environment interactions), and random chance.",
                ),
            ),
            note(
                f"{p}-n15",
                "Context-dependent penetrance",
                "HFE C282Y biochemical versus clinical penetrance",
                "The hemochromatosis-associated C282Y allele in HFE shows high penetrance for elevated ferritin (>60% of homozygotes) but only 2% penetrance for clinical liver cirrhosis—penetrance is highly context dependent on phenotypic definition and age.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "the hemochromatosis-associated C282Y allele in the HFE gene exhibits high penetrance for the biochemical phenotype of high ferritin (>60% of homozygous carriers manifest increased ferritin levels) but only 2% penetrance for the clinical phenotype of liver cirrhosis.",
                ),
            ),
            note(
                f"{p}-n16",
                "Mosaicism",
                "Why mosaicism causes variable expressivity",
                "Somatic mutations after fertilization create mosaicism—only some cells carry the variant. McCune-Albright syndrome from activating GNAS mutations shows variable expressivity because which tissues and what fraction of cells carry the mutation determines clinical features; only 24% display the classic triad.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "The most familiar class of disease caused in large part by somatic mutations is neoplasia, including endocrine tumor syndromes, such as Conn syndrome and Cushing disease. Another classic example from endocrinology is the McCune-Albright syndrome, in which the same activating mutation in GNAS1 exhibits variable expressivity because of postzygotic mosaicism.",
                ),
            ),
            note(
                f"{p}-n17",
                "ccfDNA",
                "How circulating cell-free DNA aids mosaicism diagnosis",
                "Circulating cell-free DNA released by normal and tumor cells can be extracted from plasma and sequenced, offering a noninvasive source of DNA for diagnosing mosaicism when leukocyte DNA may not contain the somatic mutation.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "Because ccfDNA can be readily extracted from plasma and sequenced, ccfDNA has shown potential as a source of DNA for a noninvasive diagnosis of mosaicism.",
                ),
            ),
            note(
                f"{p}-n18",
                "Genomic imprinting",
                "Parent-of-origin expression: GNAS, SDHD, MKRN3",
                "Imprinting silences one parental allele. Paternally inherited inactivating GNAS1 causes pseudopseudohypoparathyroidism; maternally inherited GNAS1 causes PHP1a with hormone resistance. SDHD paraganglioma mutations are penetrant only when paternally inherited; MKRN3/DLK1 CPP mutations require paternal transmission.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "Inactivating mutations in SDHD cause familial paraganglioma type 1. SDHD is maternally imprinted, so the mutation does not cause disease when inherited from the mother but is highly penetrant when inherited from the father.",
                ),
            ),
            note(
                f"{p}-n19",
                "Common versus rare variants",
                "How evolution shapes variant frequency and effect",
                "Most inherited variants are common and ancient; rare variants arose recently after migration out of Africa. Natural selection keeps deleterious common variants modest in effect; rare recent variants can exert larger phenotypic effects, especially before reproductive age.",
                ref(
                    "BOX 3.1 Origins of DNA Sequence Variation in Human Populations: Common Versus Rare Variants",
                    "If a disease is at least mildly evolutionarily deleterious, then most common variants associated with that disease will only modestly increase disease risk. This is because those common variants, if they had strongly increased disease risk, would then have been subject to strong negative evolutionary selection and never would have risen in frequency to become common in the first place.",
                ),
            ),
            note(
                f"{p}-n20",
                "Linkage versus GWAS",
                "Mendelian linkage mapping versus population association",
                "Mendelian disorders were mapped by familial linkage in rare high-penetrance families. Common polygenic disorders are identified by comparing variant frequency in cases versus controls in unrelated individuals—genotype always precedes phenotype, implying causation in association studies.",
                ref(
                    "BOX 3.2 Performing and Interpreting Genetic Studies",
                    "Because of their simple genetic architectures, Mendelian endocrine disorders were ideally suited for genetic mapping using the techniques of familial linkage mapping developed in the 1980s.",
                ),
            ),
            note(
                f"{p}-n21",
                "Haplotypes",
                "Why GWAS SNPs mark haplotypes not causal variants",
                "The variant tested in a genetic study often marks a haplotype spanning millions of bases. The molecularly causal variant may lie anywhere on that haplotype, requiring fine-mapping and functional experiments to identify.",
                ref(
                    "BOX 3.2 Performing and Interpreting Genetic Studies",
                    "When interpreting a result from any genetic study, it is important to bear in mind that the actual variant (usually a single-nucleotide polymorphism) tested in the study marks a haplotype (a combination of genetic variants inherited together) that can span millions of bases.",
                ),
            ),
            note(
                f"{p}-n22",
                "Population penetrance",
                "NF1 penetrance in families versus general population",
                "Familial NF1 studies suggest nearly 100% penetrance after childhood, but population-based sequencing of predicted pathogenic NF1 variants shows incomplete penetrance—clinical diagnostic criteria remain critical.",
                ref(
                    "BOX 3.2 Performing and Interpreting Genetic Studies",
                    "However, identification of rare and predicted to be pathogenic variants from molecular testing has shown incomplete penetrance of pathogenic NF1 variants indicating that fulfilling the clinical diagnostic criteria is still critical for the diagnosis of NF1.",
                ),
            ),
            note(
                f"{p}-n23",
                "Height genetics",
                "Polygenic height and ACAN rare variants",
                "Height is 80% heritable with ~700 common SNPs identified by GWAS; rare coding variants in 83 genes including ACAN show more than 10 times the average effect of common SNPs. Pathogenic ACAN variants cause autosomal dominant short stature or skeletal dysplasia.",
                ref(
                    "Genetics of Endocrine Diseases",
                    "To date, approximately 700 \"common\" SNPs have been identified to be associated with height variation through genome-wide association studies (GWASs), but \"rare and low-frequency\" coding variants in 83 variants showed more than 10 times the average effect of common SNPs.",
                ),
            ),
            note(
                f"{p}-n24",
                "Obesity genetics",
                "Why metreleptin treats LEP deficiency but not common obesity",
                "Recessive LEP mutations causing Mendelian obesity respond to exogenous metreleptin, but most obese individuals have elevated leptin and do not respond to leptin therapy—the Mendelian therapeutic insight does not translate to the common polygenic form.",
                ref(
                    "Genetics of Endocrine Diseases",
                    "Mendelian obesity caused by recessive inactivating mutations in LEP (leptin gene) could be well treated by exogenous metreleptin, but this clinical insight did not apply to most obese individuals who actually demonstrate elevated leptin levels and do not respond to exogenous therapy with leptin (see Chapter 40).",
                ),
            ),
            note(
                f"{p}-n25",
                "CAH genotype-phenotype",
                "How CYP21A2 alleles map to CAH severity",
                "CYP21A2 variants from frameshifts to missense mutations map to a biochemical spectrum of 21-hydroxylase activity and clinical phenotypes from salt wasting (PPV ~100% for severe alleles) to nonclassic CAH (PPV ~60%).",
                ref(
                    "Mendelian Endocrine Diseases",
                    "Notably, the positive predictive value (PPV, the strength of the genotype-phenotype correlation) is strongest for variants that severely affect CYP21A2 gene function and are predicted to cause severe disease (salt wasting, PPV ~100%).",
                ),
            ),
            note(
                f"{p}-n26",
                "Clinical genetic testing",
                "When to suspect Mendelian disease and order WES",
                "Genetic testing is most informative for suspected Mendelian disorders. Clinical suspicion rises with the SSSS mnemonic: severe phenotype, segregating family history, syndromic features, and too-soon (early) onset. WES integrates phenotype, biochemistry, and family data for interpretation.",
                ref(
                    "Genetic Information and Sequencing in Individual Patients",
                    "We offer the following criteria and mnemonic (SSSS), which should raise clinical suspicion for a Mendelian disorder: (1) severe—more severe than usual for the disease; (2) segregating—multiple affected family members or family history of consanguinity; (3) syndromic—features such as dysmorphism, developmental abnormalities, and unusual biochemical phenotypes; and (4) too soon—early age of onset.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Genetic architecture",
                "A 12-year-old boy has familial glucocorticoid deficiency with a homozygous NR0B1 mutation. His cousin has polygenic short stature without a single-gene diagnosis. Which statement best contrasts their genetic architectures?",
                [
                    "Both conditions require hundreds of common variants of small effect",
                    "The boy's disorder is monogenic with a large effect rare variant; the cousin's stature reflects many common variants of modest effect",
                    "Polygenic traits always have higher penetrance than Mendelian traits",
                    "Mendelian disorders never show variable expressivity",
                ],
                1,
                "Mendelian disorders arise from rare variants with large individual effects in few genes; common traits like stature are polygenic with many modest-effect variants.",
                ref(
                    "KEY POINTS",
                    "Mendelian endocrine disorders are caused by variants found rarely in the general population, usually from a relatively small number of genes, and each variant has a large individual effect on disease risk so that in any one individual, most of the disease risk is explained by variants in a single gene (monogenic).",
                ),
            ),
            mcq(
                f"{p}-q2",
                "NGS clinical use",
                "An endocrinologist receives a patient's consumer WES report listing a VUS in a diabetes gene. What is the most appropriate next step?",
                [
                    "Start sulfonylureas based on the VUS alone",
                    "Integrate the variant with history, examination, biochemistry, and family segregation before clinical action",
                    "Assume all rare variants are pathogenic",
                    "Disregard sequencing because WES is never clinically useful",
                ],
                1,
                "Valid clinical conclusions require integration of genetic data with phenotype, biochemistry, and family context; VUS should not drive therapy alone.",
                ref(
                    "KEY POINTS",
                    "Comprehensive genetic testing (i.e., exome or genome sequencing) can be standardized and automated. However, drawing valid and clinically useful conclusions requires integration with patient history, physical examination, biochemical studies, and other laboratory examinations of the candidate variants.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Variant databases",
                "Before classifying a novel missense variant as pathogenic, which resource best establishes whether it is too common in healthy populations to cause a rare Mendelian disorder?",
                [
                    "GenBank sequence archives alone",
                    "gnomAD population allele frequency",
                    "Patient symptom diary",
                    "Serum cortisol level only",
                ],
                1,
                "Population databases like gnomAD provide reference allele frequencies essential for distinguishing pathologic from benign variation.",
                ref(
                    "The Role of Genetics in Endocrinology",
                    "Ongoing projects include the Genome Aggregation Database (gnomAD) integrated with Exome Aggregation Consortium (ExAC), United Kingdom Biobank, the National Center for Biotechnology Information's Single Nucleotide Polymorphism Database/ClinVar, and Decipher.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Heritability",
                "Height heritability is approximately 80% while serum calcium heritability is about 40%. What clinical implication follows?",
                [
                    "Genetic testing is equally predictive for both traits",
                    "Genetic factors likely have more explanatory power for height than for serum calcium",
                    "Low-heritability traits have no genetic contribution",
                    "Heritability is fixed regardless of environment",
                ],
                1,
                "Higher heritability implies genetic factors are more influential and potentially more predictive for that trait.",
                ref(
                    "Heritability: An Estimate of the Importance of Genetic Factors to Disease Causation",
                    "genetic factors are less influential for traits with low heritability and are likely to have more predictive or explanatory power for traits with high heritability.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Twin studies",
                "Monozygotic twins show higher T1D concordance than dizygotic twins. What does this primarily support?",
                [
                    "T1D is entirely environmental",
                    "Genetic factors contribute to familial resemblance beyond shared environment alone",
                    "Dizygotic twins share 100% of genes",
                    "Twin studies prove causation of specific SNPs",
                ],
                1,
                "Excess concordance in monozygotic versus dizygotic twins supports a genetic contribution to familial resemblance.",
                ref(
                    "Heritability: An Estimate of the Importance of Genetic Factors to Disease Causation",
                    "an excess of disease correlation between genetically identical individuals (monozygotic twin pairs) compared with those who share only 50% of their genes (digyotic twin pairs) pointed to the role of genetic factors.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Gene-environment",
                "Finnish and Russian Karelians share ancestry but differ sixfold in T1D incidence after decades of divergent environments. This illustrates that:",
                [
                    "Heritability estimates are independent of population context",
                    "Environmental change cannot alter disease rates in genetically similar populations",
                    "Heritability for T1D differs when estimated in combined versus separated Karelian populations",
                    "T1D has zero genetic contribution",
                ],
                2,
                "Heritability is population- and environment-dependent; the Karelia example shows environmental divergence altering disease rates despite shared ancestry.",
                ref(
                    "Heritability: An Estimate of the Importance of Genetic Factors to Disease Causation",
                    "As a result, heritability for T1D will be different when estimated in the combined Karelian populations than when estimated in Finnish or Russian Karelians alone.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "SNP classification",
                "A heterozygous HFE C282Y variant is identified in an adult with elevated ferritin. This variant is best classified as:",
                [
                    "A synonymous SNP with no protein change",
                    "A missense nonsynonymous SNP altering one amino acid",
                    "A frameshift indel",
                    "A copy number duplication",
                ],
                1,
                "C282Y is a classic missense SNP in HFE causing hereditary hemochromatosis.",
                ref(
                    "Human DNA Sequence Variation: Molecular Forms and Biologic Effects",
                    "SNPs can be nonsynonymous (missense) changes (alteration of a single amino acid in a protein-coding gene), as is the case of the C282Y mutation in the HFE gene responsible for autosomal recessive hereditary hemochromatosis (see Chapter 17).",
                ),
            ),
            mcq(
                f"{p}-q8",
                "GH1 splicing",
                "A child has autosomal dominant IGHD with low GH and elevated inactive 17 kDa GH isoform. The most likely molecular mechanism is:",
                [
                    "GNAS activating mutation",
                    "GH1 intron 3 splice donor site mutation with exon 3 skipping",
                    "HFE C282Y homozygosity",
                    "RET MEN2A mutation",
                ],
                1,
                "Type II IGHD commonly results from splice donor mutations in GH1 causing exon 3 skipping and inactive isoform production.",
                ref(
                    "Human DNA Sequence Variation: Molecular Forms and Biologic Effects",
                    "the most common cause of autosomal dominant isolated growth hormone (GH) deficiency (type II IGHD) is single-base mutations that inactivate a splice donor site of intron 3 in the GH1 gene, causing skipping of exon 3 in GH1 (see Chapter 22) that result in increased production of inactive 17 kDa GH isoform.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Penetrance",
                "An HFE C282Y homozygote has markedly elevated ferritin but no cirrhosis at age 45. Which concept best explains this?",
                [
                    "Complete penetrance for all HFE phenotypes",
                    "Context-dependent penetrance differing between biochemical and clinical phenotypes",
                    "The variant must be benign",
                    "Expressivity always equals 100% penetrance",
                ],
                1,
                "C282Y shows high biochemical penetrance for ferritin but only ~2% penetrance for cirrhosis—penetrance depends on phenotypic definition.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "the hemochromatosis-associated C282Y allele in the HFE gene exhibits high penetrance for the biochemical phenotype of high ferritin (>60% of homozygous carriers manifest increased ferritin levels) but only 2% penetrance for the clinical phenotype of liver cirrhosis.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Mosaicism",
                "A girl has café au lait spots and precocious puberty but normal bones. Blood GNAS testing is negative. What explains the discordant findings?",
                [
                    "GNAS mutations never cause McCune-Albright",
                    "Postzygotic GNAS mosaicism with mutation absent from sampled leukocytes",
                    "Complete germline homozygous GNAS deletion",
                    "Imprinting eliminates all GNAS expression",
                ],
                1,
                "McCune-Albright arises from somatic GNAS mosaicism; the mutation may be undetectable in blood but present in affected tissues.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "The GNAS1 mutation responsible for the McCune-Albright syndrome is detected in only 8% to 46% of blood samples from affected individuals but is found in 90% of affected tissue sampled irrespective of clinical presentation (see Chapter 23).",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Imprinting",
                "A man with an inactivating SDHD mutation inherited from his asymptomatic mother develops no paraganglioma. His brother with the paternally inherited same mutation is affected. Best explanation?",
                [
                    "SDHD is X-linked recessive",
                    "SDHD is maternally imprinted; paternal transmission is required for disease",
                    "Maternal transmission always causes severe disease",
                    "Imprinting affects only growth hormone genes",
                ],
                1,
                "SDHD is maternally imprinted—mutations are non-penetrant when inherited from the mother but highly penetrant from the father.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "SDHD is maternally imprinted, so the mutation does not cause disease when inherited from the mother but is highly penetrant when inherited from the father.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "GWAS interpretation",
                "A T2D GWAS identifies a significant SNP. The nearest gene is 500 kb away with no obvious function. What is the most accurate interpretation?",
                [
                    "The SNP is certainly the causal base change",
                    "The SNP tags a haplotype; the causal variant may lie elsewhere on that haplotype",
                    "GWAS cannot identify any true associations",
                    "Linkage analysis is required for all common diseases",
                ],
                1,
                "Association SNPs mark haplotypes; causal variants require fine-mapping and functional validation.",
                ref(
                    "BOX 3.2 Performing and Interpreting Genetic Studies",
                    "the actual variant (usually a single-nucleotide polymorphism) tested in the study marks a haplotype (a combination of genetic variants inherited together) that can span millions of bases.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "NF1 penetrance",
                "Population sequencing finds predicted pathogenic NF1 variants in individuals not meeting clinical NF1 criteria. What lesson applies?",
                [
                    "Molecular testing alone suffices for NF1 diagnosis",
                    "Clinical diagnostic criteria remain essential despite molecular findings",
                    "NF1 is never heritable",
                    "All NF1 variants are benign in the population",
                ],
                1,
                "Population-based data show incomplete penetrance of pathogenic NF1 variants—clinical criteria remain critical.",
                ref(
                    "BOX 3.2 Performing and Interpreting Genetic Studies",
                    "identification of rare and predicted to be pathogenic variants from molecular testing has shown incomplete penetrance of pathogenic NF1 variants indicating that fulfilling the clinical diagnostic criteria is still critical for the diagnosis of NF1.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Height genetics",
                "A child with disproportionate short stature and skeletal dysplasia carries a rare pathogenic ACAN variant. Compared with common height SNPs, this variant likely has:",
                [
                    "Smaller effect size than typical GWAS height SNPs",
                    "More than 10 times the average effect of common height-associated SNPs",
                    "No relationship to growth plate biology",
                    "Only polygenic not Mendelian implications",
                ],
                1,
                "Rare coding variants in height genes including ACAN show effect sizes more than 10 times common GWAS SNPs.",
                ref(
                    "Genetics of Endocrine Diseases",
                    "\"rare and low-frequency\" coding variants in 83 variants showed more than 10 times the average effect of common SNPs.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "MODY pharmacogenetics",
                "A young adult with mild fasting hyperglycemia, nonobese phenotype, and autosomal dominant family history is found to have HNF1A MODY. Best initial therapy?",
                [
                    "High-dose insulin only",
                    "Sulfonylureas with superior durability demonstrated in MODY3 trials",
                    "Metformin as sole agent preferred over sulfonylureas",
                    "No therapy because MODY never requires treatment",
                ],
                1,
                "HNF1A MODY carriers show superior glycemic control with sulfonylureas versus metformin in prospective trials.",
                ref(
                    "Genetic Information and Sequencing in Individual Patients",
                    "In clinical trials, these HNF1A mutation carriers were much more sensitive to sulfonylureas than noncarriers and maintained more durable glycemic control without additional agents.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Locus heterogeneity",
                "CAH can result from defects in CYP21A2, CYP11B1, CYP17A1, and other steroidogenic genes. When phenotype is refined by biochemistry, what happens to genetic architecture?",
                [
                    "Locus heterogeneity increases without limit",
                    "Biochemical subtyping reduces locus heterogeneity for each defined subtype",
                    "All CAH subtypes map to one gene",
                    "Biochemistry is irrelevant to genetic diagnosis",
                ],
                1,
                "Refining phenotype with biochemistry narrows candidate genes and decreases apparent locus heterogeneity.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "if the CAH phenotype is refined to include biochemical measurements (mineralocorticoid, sex hormone, and electrolyte levels), individual subtypes emerge, each of which possesses a simpler genetic architecture (i.e., decreased locus heterogeneity).",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Noonan syndrome",
                "A boy with short stature, delayed puberty, cryptorchidism, and pulmonic stenosis is diagnosed with Noonan syndrome. The underlying pathway most commonly involves:",
                [
                    "Inactivating GH1 splice mutations only",
                    "Activating RAS-MAPK pathway mutations (e.g., PTPN11, SOS1, KRAS)",
                    "Recessive LEP deficiency",
                    "RET tyrosine kinase extracellular domain mutations",
                ],
                1,
                "Noonan syndrome is typically caused by dominant gain-of-function mutations activating the RAS-MAPK signaling pathway.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "Noonan syndrome (characterized endocrinologically by variable short stature, delayed puberty, and cryptorchidism in the setting of dysmorphic facial features and variable cardiac defects [see Chapter 21]) is typically caused by mutations in genes activating the RAS-MAPK (mitogen-activated protein kinase) signaling pathway.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Kallmann syndrome",
                "An adolescent male has anosmia and hypogonadotropic hypogonadism. Genetic testing may reveal mutations in:",
                [
                    "HFE, TFR2, and SLC40A1 only",
                    "KAL1, FGFR1, or PROK2 among others affecting GnRH neuron migration",
                    "CYP21A2 exclusively",
                    "GNAS paternal imprinting only",
                ],
                1,
                "Kallmann syndrome demonstrates locus heterogeneity with X-linked KAL1, autosomal dominant FGFR1, and autosomal recessive PROK2 pathways.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "Kallmann syndrome (see Chapter 23), which arises from failure of migration of GnRH neurons during fetal development, demonstrates X-linked (KAL1), autosomal dominant (FGFR1), and autosomal recessive (PROK2) inheritance.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "Aldosterone genetics",
                "Primary hyperaldosteronism adenomas frequently harbor somatic KCNJ5 missense mutations. The proposed mechanism is:",
                [
                    "Loss of sodium channel selectivity causing membrane depolarization and aldosterone secretion",
                    "Complete ablation of 21-hydroxylase activity",
                    "RET kinase activation in thyroid C cells",
                    "GH1 exon 3 skipping",
                ],
                0,
                "KCNJ5 mutations eliminate ion selectivity, increasing sodium conductance, depolarizing zona glomerulosa cells, and stimulating aldosterone release.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "this series of somatic and inherited missense mutations eliminated ion selectivity in the KCNJ5 gene product, a potassium channel. The increased sodium conductance through these mutant channels caused membrane depolarization of adrenal cortical cells in the zona glomerulosa, stimulating aldosterone release and cell proliferation.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "RET MEN2",
                "A child carries a RET intracellular tyrosine kinase domain mutation. Compared with extracellular RET mutations, this genotype most strongly predicts:",
                [
                    "Mild familial MTC only",
                    "MEN2B with aggressive MTC requiring earliest prophylactic thyroidectomy",
                    "Isolated hyperparathyroidism without MTC",
                    "No need for thyroid surveillance",
                ],
                1,
                "Intracellular RET kinase domain mutations predispose to MEN2B with the most aggressive MTC, dictating earliest prophylactic thyroidectomy.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "Mutations in the extracellular domain predispose to MEN2A (characterized by MTC, pheochromocytomas, and hyperparathyroidism), whereas mutations in the intracellular tyrosine kinase domain predispose to MEN2B (characterized by MTC, pheochromocytomas, and mucosal neuromas) (see Chapter 42).",
                ),
            ),
            mcq(
                f"{p}-q21",
                "PHP1a mechanism",
                "A boy with PHP1a and testotoxicosis carries Gs Ala366Ser. Why does the same mutation cause hormone resistance in kidney but gain-of-function in testes?",
                [
                    "Different genes are mutated in each tissue",
                    "Temperature-sensitive Gs destabilization at 37°C but increased activity at lower Leydig cell temperature",
                    "Imprinting silences Gs in all tissues",
                    "The mutation is a frameshift not missense",
                ],
                1,
                "Ala366Ser Gs is destabilized at 37°C causing loss of function in most tissues but shows increased activity at the lower temperature of Leydig cells.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "In most body tissues maintained at 37°C, the mutant Gs protein was destabilized, whereas in Leydig cells (within the testes, maintained at a 3–5°C lower temperature), the mutant Gs demonstrated increased activity.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Therapeutic genetics",
                "Loss-of-function FGFR3 causes achondroplasia while loss-of-function elsewhere in the pathway can cause tall stature. Which therapeutic strategy follows from this allelic series?",
                [
                    "FGFR3 kinase inhibition or CNP analogues to reduce excessive FGFR3 signaling",
                    "Exogenous leptin for all short stature",
                    "Metreleptin for common obesity",
                    "Prophylactic thyroidectomy for all children",
                ],
                0,
                "Opposing gain- and loss-of-function FGFR3 phenotypes support therapeutically modulating FGFR3 signaling, including CNP analogues.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "activating mutations in the FGFR3 cause achondroplasia or hypochondroplasia, whereas loss-of-function mutations cause tall stature. C-natriuretic peptide (CNP), a negative regulator of FGFR3 signaling, was modified to increase its half-life and has been tested as a potential treatment for linear growth disorders due to an activating mutation in FGFR3 that increased the RAS-MAPK signaling.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "GCK MODY2",
                "A patient with GCK MODY2 has mild stable hyperglycemia. What management follows from the genetic diagnosis?",
                [
                    "Immediate insulin and aggressive HbA1c targeting below 6%",
                    "Avoid pharmacotherapy because glycemia is regulated at a higher set-point without secondary complication risk",
                    "Near-total pancreatectomy",
                    "High-dose metreleptin",
                ],
                1,
                "GCK MODY2 patients regulate glycemia at a higher set-point and neither require hypoglycemic therapy nor face elevated secondary complication risk.",
                ref(
                    "Genetic Information and Sequencing in Individual Patients",
                    "Individuals with diabetes from GCK mutations (MODY2) manifest hyperglycemia but are still able to regulate their blood sugar levels such that they neither require hypoglycemic therapy nor are at elevated risk for secondary complications of diabetes.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "WES selection",
                "A 4-year-old with severe syndromic short stature, consanguineous parents, and negative targeted panel. Best next genetic test strategy?",
                [
                    "Population newborn screening karyotype only",
                    "Systematic WES integrating phenotype and biochemistry given SSSS features",
                    "No testing because genetic diagnosis never changes management",
                    "Order every hormone level instead of any genetic test",
                ],
                1,
                "Severe, segregating, syndromic, early-onset presentations warrant NGS/WES with integrated clinical interpretation.",
                ref(
                    "Genetic Information and Sequencing in Individual Patients",
                    "For affected individuals with unknown syndromes, or for whom targeted sequencing has failed to make a diagnosis, systematic gene sequencing using NGS methods would be required, and diagnostic yields are typically lower.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "VUS management",
                "WES returns only variants of uncertain significance for a suspected Mendelian endocrine disorder. Appropriate action?",
                [
                    "Proceed with major surgery based on VUS alone",
                    "Do not use VUS for clinical decision making; pursue reclassification via segregation, functional studies, or additional cases",
                    "Report as definitively pathogenic",
                    "Ignore all genetic testing permanently",
                ],
                1,
                "ACMG guidelines recommend VUS generally not be used for clinical decisions; efforts to reclassify should be undertaken.",
                ref(
                    "Using a Genetics Laboratory Report to Make Clinical Decisions",
                    "VUS should generally not be used in clinical decision making. Efforts to resolve the classification of the variant as pathogenic or benign should be undertaken, and interpretation in the context of the patient's clinical scenario is critical.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "ClinVar and reporting",
                "When reviewing a laboratory genetics report, which element is essential for variant interpretation?",
                [
                    "Gene name, molecular change, zygosity, population frequency, and classification with justification",
                    "Patient height and weight only",
                    "Serum sodium alone",
                    "Absence of any family data requirement",
                ],
                0,
                "Clinical reports should provide gene, transcript, variant details, zygosity, population frequency, classification, and justification using databases including ClinVar and gnomAD.",
                ref(
                    "BOX 3.3 Examining a Clinical Genetics Laboratory Report",
                    "When applicable, the gene name, transcript, molecular form of variant (single-nucleotide polymorphism, indel, etc.), base changes, amino acid change, zygosity, population frequency, and classification (benign, likely benign, likely pathogenic, pathogenic, variants of uncertain significance) should be provided.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Mendelian genetics",
                "Mendelian endocrine disorders always have 100% penetrance.",
                False,
                "Mendelian variants can be highly penetrant but this is not always the case.",
                ref(
                    "KEY POINTS",
                    "Mendelian variants can be highly penetrant, but this is not always the case.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "NGS interpretation",
                "The ability to interpret genetic variation from NGS currently exceeds the ability to generate sequence data.",
                False,
                "Interpretation is less advanced than sequencing capacity though improving with larger databases.",
                ref(
                    "The Role of Genetics in Endocrinology",
                    "The ability to interpret this variation is less advanced but is improving with time, as databases of variants and their clinical associations increase in both size and accuracy.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Heritability",
                "Heritability is a fixed property of a disease that does not vary across populations or time.",
                False,
                "Heritability must be interpreted in population, historical, and environmental context.",
                ref(
                    "Heritability: An Estimate of the Importance of Genetic Factors to Disease Causation",
                    "it is critical to appreciate that heritability is not a fixed property of a disease/trait.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Synonymous SNPs",
                "Synonymous SNPs never affect gene function.",
                False,
                "Synonymous SNPs usually do not affect function unless they alter pre-mRNA splicing, which is rare but possible.",
                ref(
                    "Human DNA Sequence Variation: Molecular Forms and Biologic Effects",
                    "Consequently, this sort of variation usually does not affect function unless a synonymous SNP affects pre-mRNA splicing, which is rare.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Mosaicism detection",
                "GNAS mutations causing McCune-Albright are always detectable in peripheral blood DNA.",
                False,
                "GNAS mutations are detected in only 8% to 46% of blood samples but in 90% of affected tissue.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "The GNAS1 mutation responsible for the McCune-Albright syndrome is detected in only 8% to 46% of blood samples from affected individuals but is found in 90% of affected tissue sampled irrespective of clinical presentation (see Chapter 23).",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Imprinting",
                "Maternally inherited inactivating GNAS1 mutations cause PHP1a with hormone resistance in renal proximal tubules.",
                True,
                "Only the maternal copy of GNAS1 is expressed in renal proximal tubules; maternal inheritance causes PHP1a with hypocalcemia and hormone resistance.",
                ref(
                    "BOX 3.1 Origins of DNA Sequence Variation in Human Populations: Common Versus Rare Variants",
                    "The same mutation, when maternally inherited, manifests not only with Albright hereditary osteodystrophy but also with hypocalcemia secondary to parathyroid hormone resistance (pseudohypoparathyroidism type 1a [PHP1a]), because only the maternal copy of GNAS1 is expressed in renal proximal tubules.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "GWAS causation",
                "In genetic association studies, correlation between genotype and disease implies causation because genotype precedes phenotype.",
                True,
                "Unlike clinical risk factor associations, genetic associations imply causation since genotype always precedes phenotype.",
                ref(
                    "BOX 3.2 Performing and Interpreting Genetic Studies",
                    "Unlike clinical risk factors/biomarkers association studies, correlation in genetic association studies implies causation, because genotype always precedes phenotype.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Common variants",
                "Common variants associated with evolutionarily deleterious diseases typically confer only modest increases in disease risk.",
                True,
                "Strongly deleterious common variants would have been selected against and would not have become common.",
                ref(
                    "BOX 3.1 Origins of DNA Sequence Variation in Human Populations: Common Versus Rare Variants",
                    "If a disease is at least mildly evolutionarily deleterious, then most common variants associated with that disease will only modestly increase disease risk.",
                ),
            ),
            tf(
                f"{p}-tf9",
                "Obesity therapy",
                "Exogenous leptin therapy is effective for most patients with common polygenic obesity.",
                False,
                "Most obese individuals have elevated leptin and do not respond to exogenous leptin; metreleptin benefits Mendelian LEP deficiency.",
                ref(
                    "Genetics of Endocrine Diseases",
                    "most obese individuals who actually demonstrate elevated leptin levels and do not respond to exogenous therapy with leptin (see Chapter 40).",
                ),
            ),
            tf(
                f"{p}-tf10",
                "CAH genetics",
                "Genotype-phenotype correlation for CYP21A2 CAH is strongest for alleles predicted to cause severe salt-wasting disease.",
                True,
                "PPV for salt wasting is approximately 100% for severely deleterious CYP21A2 variants.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "Predictive power is weaker for genetic variants that are expected to have more moderate effects on gene function and therefore result in milder disease (nonclassic, PPV ~60%).",
                ),
            ),
            tf(
                f"{p}-tf11",
                "KISS1R therapeutics",
                "All patients with congenital hypogonadotropic hypogonadism show robust LH responses to exogenous kisspeptin.",
                False,
                "A series of patients with congenital hypogonadotropic hypogonadism failed to show expected LH response to exogenous kisspeptin.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "a series of patients with congenital hypogonadotropic hypogonadism failed to show an expected LH response with exogenous kisspeptin administration.",
                ),
            ),
            tf(
                f"{p}-tf12",
                "Population screening",
                "Current evidence supports routine genome sequencing for population-based screening of Mendelian mutations.",
                False,
                "Penetrance and genotype-phenotype correlations from families may not hold in the general population; current evidence does not support population genome screening.",
                ref(
                    "Genome Screening in the General Population",
                    "The current evidence and state of knowledge do not support genome sequencing for population-based screening.",
                ),
            ),
            tf(
                f"{p}-tf13",
                "WGS indiscriminate use",
                "Ordering whole genome sequencing for every endocrine patient maximizes diagnostic yield without increasing false positives.",
                False,
                "More tests increase false-positive probability; WGS is analogous to ordering every hormone level—not pursued indiscriminately.",
                ref(
                    "Selection of Genetic Tests: Targeted Versus Genome-Wide Approaches",
                    "Using genome sequencing in this way is tantamount to performing thousands of genetic tests at once and clinically analogous to ordering every possible hormone level for every endocrine patient.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Genetic architecture",
                "Assertion: Sporadic endocrine disorders can be caused by rare variants with large effects in a relatively small number of genes.",
                "Reason: All endocrine disease risk is always explained by hundreds of common polygenic variants in every individual.",
                2,
                "Both parts of the assertion are true for sporadic rare-variant disease, but the reason is false—monogenic and sporadic large-effect rare variants exist alongside polygenic architecture.",
                ref(
                    "KEY POINTS",
                    "Similarly, sporadic endocrine disorders can be caused by rare variants with a large individual effect on disease risk in a relatively small number of genes.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Clinical utility",
                "Assertion: Genetic information is most likely to be of direct clinical use in patients with suspected Mendelian or sporadic endocrine disorders.",
                "Reason: Comprehensive genetic testing conclusions require integration with history, examination, and biochemistry.",
                1,
                "Both are true; the reason correctly explains why careful clinical integration is needed even when Mendelian disease is suspected.",
                ref(
                    "KEY POINTS",
                    "Genetic information is most likely to be of direct clinical use in patients with suspected Mendelian or sporadic endocrine disorders.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Polygenic inheritance",
                "Assertion: R.A. Fisher's framework explained continuously varying traits as combined small additive effects of many genes.",
                "Reason: Mendelian inheritance was considered the general rule and polygenic inheritance a rare exception in Fisher's model.",
                2,
                "Assertion is true; reason is false—in Fisher's framework monogenic/Mendelian traits were the special case, not the rule.",
                ref(
                    "Principles of Genetics",
                    "In this framework, monogenic/Mendelian traits were a special case.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Nonsense variants",
                "Assertion: Nonsense SNPs typically dramatically impair or eliminate protein function.",
                "Reason: Nonsense variants always produce full-length functional proteins.",
                2,
                "Assertion is true; nonsense variants cause premature termination or decay—the reason is false.",
                ref(
                    "Human DNA Sequence Variation: Molecular Forms and Biologic Effects",
                    "These nonsense variants typically dramatically impair or eliminate the function of the protein.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Expressivity",
                "Assertion: Variable expressivity arises from genetic background, environment, and chance among carriers of the same variant.",
                "Reason: All family members with an identical pathogenic variant always have identical clinical severity.",
                2,
                "Assertion is true; identical severity in all carriers is false—expressivity varies.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "not all members of the family are equally affected.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "MKRN3 imprinting",
                "Assertion: Inactivating MKRN3 mutations cause GnRH-dependent central precocious puberty only when inherited from the father.",
                "Reason: MKRN3 is maternally imprinted so the maternal copy is silenced.",
                0,
                "Both are true and causally linked—paternal transmission is required because the maternal allele is imprinted/silenced.",
                ref(
                    "Factors Influencing the Biologic Impact of Genetic Variants in a Particular Gene",
                    "MKRN3 or DLK1 are maternally imprinted, so inactivating mutations in MKRN3 or DLK1 causes GnRH-dependent central precocious puberty only when the mutations were inherited from the father.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Linkage versus association",
                "Assertion: Mendelian disorders were ideally suited to familial linkage mapping.",
                "Reason: Common polygenic disorders require comparing variant frequency in unrelated cases and controls.",
                1,
                "Both true but independently stated mapping strategies—the reason describes association not linkage, so they are true but the reason does not explain why linkage suited Mendelian disease (answer 1: both true, R not correct explanation).",
                ref(
                    "BOX 3.2 Performing and Interpreting Genetic Studies",
                    "Genetic association studies do not require the identification of rare families segregating disease, because they simply compare the frequency of a given genetic variant in disease cases and controls.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Allelic heterogeneity",
                "Assertion: MEN2 demonstrates allelic heterogeneity with recurrent mutations in RET of different molecular forms.",
                "Reason: Locus heterogeneity means different genes on different chromosomes cause the same disease.",
                1,
                "Assertion true for MEN2/RET allelic heterogeneity; reason true statement about locus heterogeneity but does not explain allelic heterogeneity—both true, R not correct explanation.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "Some Mendelian disorders (e.g., MEN2) demonstrate recurrent mutations in the same gene but of different molecular forms and locations, a phenomenon termed allelic heterogeneity.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "CACNA1D aldosteronism",
                "Assertion: Gain-of-function mutations in KCNJ5 and CACNA1D were identified as causes of hyperaldosteronism.",
                "Reason: These mutations increase 21-hydroxylase activity in CYP21A2.",
                2,
                "Assertion is true; reason is false—the mechanism involves ion channel conductance and membrane depolarization in zona glomerulosa, not CYP21A2.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "A second example of synergy between NGS and classical genetic study design revealed gain-of-function mutations in the KCNJ5 and CACNA1D genes as causes of hyperaldosteronism.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "RET prophylaxis",
                "Assertion: RET genotype-phenotype correlation dictates timing of prophylactic thyroidectomy in MEN2 carriers.",
                "Reason: All RET mutations confer identical MTC aggressiveness regardless of domain location.",
                2,
                "Assertion is true; MTC aggressiveness varies by mutation domain—reason is false.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "The clinical aggressiveness of MTC, the sine qua non of all three syndromes, is greatest in MEN2B, then less in MEN2A, with familial MTC demonstrating the least propensity to grow and metastasize.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Neonatal diabetes",
                "Assertion: Permanent neonatal diabetes from ABCC8 or KCNJ11 mutations can be treated with high-dose sulfonylureas instead of insulin.",
                "Reason: These mutations confer gain-of-function channel activity responsive only to insulin therapy.",
                2,
                "Assertion is true; reason is false—activating mutations in these channels predict sulfonylurea responsiveness, not insulin-only therapy.",
                ref(
                    "Mendelian Endocrine Diseases",
                    "Individuals with permanent neonatal diabetes caused by ABCC8 or KCNJ11 mutations can be safely treated with high-dose sulfonylureas in place of insulin.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Genetic incidentaloma",
                "Assertion: An asymptomatic individual with a Mendelian-like mutation but no family history has low pretest disease probability despite high relative risk.",
                "Reason: Healthy individuals average ~100 disruptive Mendelian-like mutations in protein-coding genes, providing genomic redundancy.",
                0,
                "Both true and linked—the population carrier burden and incomplete penetrance explain why high relative risk still yields low absolute disease probability.",
                ref(
                    "Asymptomatic Individuals",
                    "the genome of an apparently healthy individual contains approximately 100 Mendelian-like disruptive mutations (i.e., frameshifting indels and SNPs resulting in premature stop codons), up to 20 of which are homozygously inactivated.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "3",
        "title": "Genetics of Endocrinology",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Youn Hee Jee, Joel N. Hirschhorn, Amit R. Majithia",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_03_Genetics_of_Endocrinology.md",
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
