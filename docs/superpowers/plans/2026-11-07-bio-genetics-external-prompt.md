# Prompt: generate the bio.genetics batch

Copy everything below the line into the other model.

---

You are helping build a knowledge graph for an adaptive learning app (in the style of Math Academy) that covers kindergarten through university STEM. The graph is made of **topics** (one lesson-sized skill each), the **knowledge points (KPs)** inside each topic, and weighted **prerequisite edges** between topics. Your job is to write the knowledge points and edge weights for one university course, **Genetics** (`bio.genetics`, upper-division undergraduate level). The topic list and prerequisite structure are already fixed; you fill in the details in an exact text format.

## Hard rules

1. **Original wording only.** Do not copy or closely mirror any textbook's table of contents, section titles or wording. Write from general knowledge of what strong university genetics courses teach.
2. **Graph only.** No lesson text, explanations, worked examples, practice problems or answers. Each KP is a single short "can do" statement.
3. **No laboratory protocols.** KPs describe concepts, calculations, analysis and interpretation (for example "Interpret Ames test results"), never step-by-step bench procedures for making organisms, mutagenizing anything, or handling hazardous agents.
4. **Do not add, remove, rename or reorder topics, and do not change their prerequisites.** Use the 41 topics exactly as listed below, in that order.

## What each topic needs

For each topic, write:

- **One weight and one confidence per direct prerequisite**, in the order listed.
  - **Weight** (0.05 to 0.9): the fraction of that prerequisite topic that a typical problem in this topic actually exercises. A prerequisite that is merely required first but barely practised gets about 0.2; one that is used heavily in every problem gets 0.5 to 0.65. Judge each edge individually. Do **not** reuse the same value everywhere; a course whose weights cluster on two or three values has been templated and will be rejected.
  - **Confidence**: `h` (the link is clearly essential), `m` (useful but a student could manage without it, or the overlap is partial) or `l` (weak or uncertain link). Be honest. Some edges should be `m`, and a few may be `l`.
- **Exactly 4 knowledge points** (3 or 5 only if the topic truly demands it). They form a ladder: the most basic version of the skill first, then a twist, then another twist, then the pieces combined or applied. Each KP:
  - is one line, about 5 to 12 words, starting with an action verb (Calculate, Find, Explain, Interpret, Predict, Analyze, Compare, Describe, Use, Map, Distinguish...);
  - is concrete and checkable ("Calculate interference from double crossover counts"), not vague ("Understand mapping");
  - stays inside the topic's scope and does not need knowledge beyond the topic plus its prerequisites;
  - lists its **key prerequisites** as digits (see the format below). A key prerequisite is a prerequisite the KP genuinely leans on. Use 1 to 3 digits per KP. Every direct prerequisite must be used by at least one KP in its topic.

## Output format (exact)

Output only the batch text, nothing else, no commentary or code fences. For each topic:

```
@slug W1 W2 ...
KP text |digits
KP text |digits
KP text |digits
KP text |digits
```

- `@slug` is the topic slug from the list. It is followed by one token per direct prerequisite, **in the listed order**: a weight then a confidence letter, written with no space, such as `.35h`, `.3m` or `.2l`. A topic with one prerequisite has one token.
- Each KP line is the KP text, a space, `|` and the key-prerequisite digits. Digits index the prerequisites in order, so `|1` is the first direct prerequisite, `|2` the second, and `|12` both. If a topic also has an **implied** link (marked below), it is numbered after the direct ones and has no weight token. Its weight is set automatically, but you may cite its digit in KPs.
- If you omit `|digits`, the KP defaults to `|1`.

### Two examples from already-built courses (match this style and quality)

The first topic has two direct prerequisites (a protein-topology prerequisite, then a side-chain-properties prerequisite):

```
@membrane-protein-topology .35h .3h
Predict transmembrane segments from hydrophobicity |12
Compare single-pass and multipass proteins |1
Explain orientation of membrane proteins |1
Read a hydropathy plot |2
```

The second has two direct prerequisites plus one implied link (digit 3):

```
@evidence-for-evolution .3h .35h
Use embryo similarities as evidence |1
Use homologous structures as evidence |3
Use DNA comparisons as evidence |2
Combine lines of evidence |123
```

## The course: bio.genetics (41 topics, all at upper-division university level)

Students arrive having taken high school biology, AP-level biology and introductory university biology, plus high school statistics. Each topic below shows its slug, name and numbered direct prerequisites. Prerequisites from other courses are given with their full names so you know exactly what students already know. "Implied" links have no weight token.

### Transmission genetics

1. `binomial-probability-in-families`: Using binomial probability for families
   - 1: Using product and sum rules in genetics (high school, grade 12)
   - 2: Calculating binomial probabilities (statistics, grade 12)
2. `chi-square-tests-of-crosses`: Testing cross data with chi-square
   - 1: Using chi-square goodness of fit (statistics, grade 12)
   - 2: Solving dihybrid crosses (high school, grade 10)
3. `lethal-alleles-and-penetrance`: Analyzing lethal alleles, penetrance and expressivity
   - 1: Analyzing epistasis ratios (intro university)
4. `complementation-tests`: Using complementation tests
   - 1: lethal-alleles-and-penetrance
5. `pedigree-risk`: Calculating risks from pedigrees
   - 1: Analyzing pedigrees (high school, grade 10)
   - 2: binomial-probability-in-families
6. `disorder-mechanisms`: Relating genetic disorders to molecular mechanisms
   - 1: pedigree-risk
   - 2: Describing common genetic disorders (high school, grade 10)

### Linkage and mapping

7. `three-point-mapping`: Mapping genes with three-point crosses
   - 1: Using recombination frequency to map genes (high school, grade 12)
8. `interference-and-coincidence`: Calculating interference
   - 1: three-point-mapping
9. `mapping-functions`: Correcting map distances for multiple crossovers
   - 1: interference-and-coincidence
10. `tetrad-analysis`: Mapping with tetrad analysis
    - 1: three-point-mapping
11. `lod-scores`: Using LOD scores for human linkage
    - 1: three-point-mapping
    - 2: pedigree-risk

### Chromosomes

12. `cytogenetics`: Describing centromeres, banding and chromosome structure
    - 1: Describing deletions, duplications, inversions and translocations (intro university)
13. `aneuploidy-and-polyploidy`: Explaining aneuploidy and polyploidy
    - 1: cytogenetics
    - implied 2: Explaining nondisjunction and chromosome disorders (high school, grade 10)
14. `rearrangements-in-meiosis`: Predicting meiotic consequences of inversions and translocations
    - 1: aneuploidy-and-polyploidy
15. `organelle-inheritance`: Explaining mitochondrial and chloroplast inheritance
    - 1: Linking Mendel's laws to chromosome behaviour (intro university)
16. `genomic-imprinting`: Explaining genomic imprinting
    - 1: Explaining X inactivation (intro university)

### Bacterial and viral genetics

17. `conjugation-mapping`: Mapping genes by conjugation
    - 1: Describing transformation, conjugation and plasmids (high school, grade 12)
18. `transduction-mapping`: Mapping genes by transduction and transformation
    - 1: conjugation-mapping
19. `phage-genetics`: Analyzing phage crosses
    - 1: Comparing lytic and lysogenic cycles (intro university)
20. `transposable-elements`: Describing transposable elements
    - 1: Comparing genome size and organization (intro university)

### Molecular genetics

21. `mutation-rates-and-mutagens`: Calculating mutation rates and testing mutagens (analysis and interpretation only)
    - 1: Predicting effects of mutations on proteins (high school, grade 12)
22. `forward-genetic-screens`: Designing forward genetic screens (logic of screen design and analysis, not bench protocol)
    - 1: mutation-rates-and-mutagens
    - 2: complementation-tests
23. `recombination-mechanisms`: Describing homologous recombination
    - 1: Describing DNA repair mechanisms (intro university)
24. `operon-mutant-analysis`: Analyzing operon mutants with partial diploids
    - 1: Explaining lac and trp operons (high school, grade 12)
    - 2: complementation-tests
25. `eukaryotic-regulatory-mutants`: Analyzing regulatory mutations in eukaryotes
    - 1: operon-mutant-analysis
    - 2: Describing chromatin packaging (intro university)
26. `epigenetic-inheritance`: Explaining epigenetic inheritance
    - 1: genomic-imprinting

### Genomics and biotechnology

27. `sequencing-technologies`: Comparing sequencing technologies
    - 1: Comparing genome size and organization (intro university)
28. `genome-assembly-and-annotation`: Describing genome assembly and annotation
    - 1: sequencing-technologies
29. `comparative-genomics`: Using comparative genomics
    - 1: genome-assembly-and-annotation
30. `reverse-genetics-and-editing`: Using reverse genetics and gene editing (concepts and experimental logic)
    - 1: Using vectors to clone genes (intro university)
    - 2: Describing gene editing (high school, grade 10)
31. `transgenic-organisms`: Making transgenic organisms (concepts, uses and analysis; no protocols)
    - 1: reverse-genetics-and-editing
32. `gene-therapy`: Describing gene therapy
    - 1: transgenic-organisms
33. `genetic-testing`: Evaluating genetic testing and its ethics
    - 1: disorder-mechanisms

### Quantitative and population genetics

34. `quantitative-traits`: Analyzing quantitative traits
    - 1: Explaining polygenic and environmentally influenced traits (high school, grade 10)
    - 2: Calculating standard deviation (statistics, grade 12)
35. `heritability`: Estimating heritability
    - 1: quantitative-traits
    - 2: Using properties of correlation (statistics, grade 12)
36. `qtl-mapping`: Describing QTL mapping
    - 1: heritability
    - 2: three-point-mapping
37. `association-studies`: Interpreting genome-wide association studies
    - 1: lod-scores
    - 2: quantitative-traits
38. `allele-frequency-calculations`: Calculating allele and genotype frequencies
    - 1: Using Hardy-Weinberg equilibrium (high school, grade 12)
39. `inbreeding`: Calculating inbreeding coefficients
    - 1: allele-frequency-calculations
40. `mutation-selection-balance`: Finding mutation-selection balance
    - 1: allele-frequency-calculations
41. `drift-and-effective-size`: Calculating effects of drift and effective population size
    - 1: allele-frequency-calculations

## Scope notes

- Keep calculations to what the listed statistics prerequisites support: probability rules, binomial probabilities, chi-square goodness of fit, mean, standard deviation and correlation. No calculus.
- Population genetics topics here are the genetics-side calculations. Selection models, fixation probability and coalescent theory belong to a later Evolution course, so leave them out.
- Avoid repeating what the prerequisites already teach. For example, `three-point-mapping` should go beyond simple two-gene recombination frequency, and `chi-square-tests-of-crosses` applies the test to cross data rather than reteaching the test.

## Self-check before you answer

- [ ] 41 topics, in the listed order, slugs spelled exactly.
- [ ] Each `@` line has exactly one weight token per direct prerequisite (not counting implied links).
- [ ] Weights vary across the course (many different values between 0.2 and 0.65), and several confidences are `m`.
- [ ] 4 KPs per topic, forming a basic-to-combined ladder, each a short action-verb line.
- [ ] Every digit refers to an existing prerequisite (or the implied link), and every direct prerequisite is used by at least one KP.
- [ ] No lesson text, no problems, no bench protocols, no textbook wording.
