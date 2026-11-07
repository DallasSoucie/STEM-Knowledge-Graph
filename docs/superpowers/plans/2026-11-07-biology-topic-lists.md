# Topic lists: biology

Draft for approval. Covers all 15 biology courses. In the Needs column, a plain name is in the same course; a short prefix (`hs1.`, `cell-mol.`) names a biology course; chemistry, physics and math topics are written with their full course (`chem.gen2.`, `physics.hs1.`, `math.stats.`).

## Proposed manifest changes

Following the pattern already set for chemistry, each school course comes before the university course that would otherwise repeat it, and biology builds on chemistry and math where they already teach a skill.

| Course | Follows now | Proposed | Why |
|---|---|---|---|
| bio.elem | (none) | (none) | |
| bio.ms | bio.elem | + chem.ms, math.g7 | molecules and reactions for photosynthesis; probability for Punnett squares |
| bio.hs1 | bio.ms | + chem.ms, math.alg1 | molecules, pH and solutions; ratios and exponential growth |
| bio.hs2 | bio.hs1, chem.hs1 | unchanged | |
| bio.intro1 | bio.hs1 | bio.hs2 instead | otherwise intro biology and the AP-level course run in parallel and repeat each other |
| bio.cell-mol | bio.intro1, chem.gen1 | chem.gen2 instead | membrane potentials use the Nernst equation and pump energetics use nonstandard Gibbs energy, both in gen2 |
| bio.genetics | bio.intro1 | + math.stats | chi-square and binomial tests, heritability |
| bio.biochem | bio.cell-mol, chem.org1 | chem.org2 instead | amino acids, sugars, lipids and nucleotides are homed in organic II |
| bio.ecology | bio.intro2, math.stats | + math.calc1 | growth rates as derivatives, sustainable yield as optimization |
| bio.micro | bio.cell-mol | + bio.intro2 | prokaryote diversity and growth models live in intro II |
| bio.neuro | bio.cell-mol | + bio.anat-phys1 | action potentials and synapses are first taught in anatomy and physiology I |

**Move (as with chemistry, recorded in id-history):** `chem.pchem1.michaelis-menten` and `chem.pchem1.enzyme-inhibition` move to `bio.biochem`. Biochemistry is where most students first meet them, and nothing in pchem1 depends on them. Michaelis-Menten is rewired to `chem.gen2.steady-state-intermediates` and `chem.gen2.enzyme-kinetics-intro`.

## Budgets

Every course came in well under budget. The school courses absorb what the introductory courses would repeat, as in chemistry, so intro I is especially lean.

| Course | Topics | Budget now | Proposed |
|---|---|---|---|
| elem | 30 | 50 | 30 |
| ms | 43 | 90 | 45 |
| hs1 | 86 | 180 | 90 |
| hs2 | 66 | 180 | 70 |
| intro1 | 33 | 190 | 35 |
| intro2 | 54 | 190 | 55 |
| cell-mol | 53 | 170 | 55 |
| genetics | 41 | 170 | 45 |
| biochem | 52 (2 moved in) | 180 | 55 |
| ecology | 33 | 140 | 35 |
| evolution | 32 | 120 | 35 |
| micro | 37 | 160 | 40 |
| anat-phys1 | 59 | 180 | 60 |
| anat-phys2 | 57 | 180 | 60 |
| neuro | 42 | 130 | 45 |
| **Total** | **718** | **2,310** | **755** |

That brings biology to 755 and the full graph to about 12,500. The alternative is keeping larger budgets and splitting topics more finely. The best candidates for that are the anatomy courses (one topic per skeletal region or muscle group) and the high school courses, where real lessons are smaller than these topics.

## Overlap notes

- Ecology's population and competition topics interpret the same models that `math.diffeq` solves (predator-prey, competing species). Ecology follows calc1, not diffeq, so it teaches them graphically and biologically and does not reuse the diffeq topics.
- Immunity is split by level: an overview in `hs2`, inflammation and lymph in `anat-phys2`, and cellular and molecular immunology in `micro`.
- `genetics.chi-square-tests-of-crosses` applies `math.stats.chi-square-gof` to cross data rather than reteaching the test.

## Survey

Standards in refs: NGSS DCI (LS1 to LS4), BC Science K-9, Life Sciences 11 and Anatomy and Physiology 12, AP Biology with clarifications, MCAT outline. University sources are indexed in `refs/uni_syllabi/SOURCES.md` under the `bio-*` folders (20 of 27 downloads saved): UT Dallas, Toronto Scarborough, CUNY and UNT intro biology; Texas A&M San Antonio intro II; Edinburgh, Penn and UNT cell biology; Rutgers, Granada and Philadelphia genetics; Youngstown State, ESF and KTH biochemistry; SUNY Jamestown and the GALILEO open anatomy and physiology course; Brooklyn, Wayne State and Dartmouth course indexes and a New Orleans ecology syllabus for the upper-level courses.

Left out: botany and zoology as separate courses, developmental biology, immunology as its own course, and bioinformatics beyond genome analysis.

## bio.elem: 30 topics

### Living things and their needs

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Telling living from nonliving things | `living-and-nonliving` | gk |  |
| Describing what plants and animals need to live | `needs-of-plants-and-animals` | gk | `living-and-nonliving` |

### Structures and offspring

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Matching animal body parts to their jobs | `animal-parts-and-functions` | g1 | `needs-of-plants-and-animals` |
| Matching plant parts to their jobs | `plant-parts-and-functions` | g1 | `needs-of-plants-and-animals` |
| Comparing young plants and animals with their parents | `offspring-resemble-parents` | g1 | `living-and-nonliving` |
| Describing how parents help offspring survive | `parent-care-behaviours` | g1 | `offspring-resemble-parents` |
| Designing solutions inspired by plant and animal parts | `designs-inspired-by-nature` | g1 | `animal-parts-and-functions` |

### Plants and habitats

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Testing what plants need to grow | `plant-growth-needs-test` | g2 | `plant-parts-and-functions` |
| Describing how animals help plants spread | `seed-dispersal-and-pollination` | g2 | `plant-parts-and-functions` |
| Comparing living things in different habitats | `habitats-and-diversity` | g2 | `needs-of-plants-and-animals` |

### Life cycles, traits and survival

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing life cycles of plants and animals | `life-cycles` | g3 | `offspring-resemble-parents` |
| Describing traits inherited from parents | `inherited-traits` | g3 | `offspring-resemble-parents` |
| Explaining how environment affects traits | `traits-and-environment` | g3 | `inherited-traits`, `plant-growth-needs-test` |
| Explaining how variation helps survival | `variation-and-survival` | g3 | `traits-and-environment` |
| Explaining why some animals live in groups | `animal-groups` | g3 | `parent-care-behaviours` |
| Using fossils to describe past environments | `fossils-and-past-life` | g3 | `habitats-and-diversity` |
| Classifying living things by shared features | `classifying-living-things` | g3 | `habitats-and-diversity` |
| Predicting how habitat change affects living things | `environmental-change-and-survival` | g3 | `habitats-and-diversity`, `variation-and-survival` |
| Describing ways people protect environments | `protecting-environments` | g4 | `environmental-change-and-survival` |

### Structures, senses and body

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining how structures support survival | `internal-and-external-structures` | g4 | `animal-parts-and-functions`, `plant-parts-and-functions` |
| Explaining how animals use senses to respond | `senses-and-responses` | g4 | `internal-and-external-structures` |
| Describing skeletons and muscles in animals | `skeletons-and-muscles-intro` | g4 | `internal-and-external-structures` |
| Naming major human body systems | `human-body-systems-intro` | g5 | `internal-and-external-structures` |
| Linking healthy habits to body systems | `healthy-habits` | g5 | `human-body-systems-intro` |

### Energy and matter in ecosystems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining that plants get matter from air and water | `plants-make-food-from-sunlight` | g5 | `plant-growth-needs-test` |
| Explaining that animals get energy from food | `animals-get-energy-from-food` | g5 | `plants-make-food-from-sunlight` |
| Building food chains | `food-chains` | g5 | `animals-get-energy-from-food` |
| Building food webs | `food-webs` | g5 | `food-chains` |
| Describing the role of decomposers | `decomposers` | g5 | `food-webs` |
| Modelling matter moving through ecosystems | `matter-cycling-in-ecosystems` | g5 | `decomposers` |

## bio.ms: 43 topics

### Cells and organization

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing cells as the basic units of life | `cells-as-basic-units` | g6 | `elem.living-and-nonliving` |
| Using a microscope to observe cells | `microscope-use` | g6 | `cells-as-basic-units` |
| Comparing unicellular and multicellular organisms | `unicellular-and-multicellular` | g6 | `cells-as-basic-units` |
| Identifying cell parts and their jobs | `cell-parts` | g6 | `cells-as-basic-units` |
| Comparing plant and animal cells | `plant-and-animal-cells` | g6 | `cell-parts` |
| Stating the cell theory | `cell-theory` | g7 | `cells-as-basic-units` |
| Describing how the cell membrane controls what enters | `cell-membrane-role` | g7 | `cell-parts` |
| Ordering cells, tissues, organs and systems | `levels-of-organization` | g6 | `unicellular-and-multicellular` |
| Explaining how body systems work together | `body-systems-interact` | g7 | `levels-of-organization`, `elem.human-body-systems-intro` |
| Explaining how nerves carry messages | `nerves-carry-messages` | g7 | `body-systems-interact` |

### Matter and energy in organisms

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing photosynthesis inputs and outputs | `photosynthesis-intro` | g7 | `elem.plants-make-food-from-sunlight`, `ms.word-equations` |
| Describing cellular respiration inputs and outputs | `cellular-respiration-intro` | g7 | `photosynthesis-intro` |
| Explaining how food molecules are rearranged for growth | `food-molecules-rearranged` | g7 | `cellular-respiration-intro`, `ms.reactions-rearrange-atoms` |
| Describing how digestion breaks down food | `digestion-intro` | g7 | `body-systems-interact`, `food-molecules-rearranged` |

### Ecosystems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining how resources limit populations | `populations-and-resources` | g7 | `elem.food-webs` |
| Classifying predation, competition and mutualism | `ecological-interactions` | g7 | `populations-and-resources` |
| Building energy pyramids | `energy-pyramids` | g7 | `elem.food-webs`, `photosynthesis-intro` |
| Describing the carbon cycle | `carbon-cycle-intro` | g7 | `elem.matter-cycling-in-ecosystems`, `cellular-respiration-intro` |
| Predicting effects of ecosystem disruptions | `ecosystem-change` | g7 | `ecological-interactions` |
| Explaining the value of biodiversity | `biodiversity-and-ecosystem-services` | g7 | `ecosystem-change` |
| Evaluating solutions to protect ecosystems | `ecosystem-protection-solutions` | g7 | `biodiversity-and-ecosystem-services` |

### Growth and reproduction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing sexual and asexual reproduction | `sexual-and-asexual-reproduction` | g6 | `unicellular-and-multicellular`, `elem.life-cycles` |
| Describing flowers and plant reproduction | `plant-reproduction-structures` | g6 | `sexual-and-asexual-reproduction`, `elem.seed-dispersal-and-pollination` |
| Explaining behaviours that help reproduction | `reproductive-behaviours` | g6 | `sexual-and-asexual-reproduction`, `elem.animal-groups` |
| Explaining environmental and genetic effects on growth | `factors-affecting-growth` | g6 | `plant-reproduction-structures`, `elem.traits-and-environment` |
| Describing cell division for growth | `cell-division-intro` | g7 | `cell-parts` |

### Heredity

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing genes on chromosomes | `genes-and-chromosomes-intro` | g8 | `cell-division-intro`, `elem.inherited-traits` |
| Describing how mutations change proteins and traits | `mutations-intro` | g8 | `genes-and-chromosomes-intro` |
| Using dominant and recessive alleles | `dominant-and-recessive` | g8 | `genes-and-chromosomes-intro` |
| Predicting offspring with Punnett squares | `punnett-squares-intro` | g8 | `dominant-and-recessive`, `g7.compound-event-probability` |
| Explaining why sexual reproduction creates variation | `sexual-reproduction-variation` | g8 | `punnett-squares-intro`, `sexual-and-asexual-reproduction` |
| Describing genetic engineering and selective breeding | `genetic-engineering-intro` | g8 | `mutations-intro` |

### Evolution

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading patterns in the fossil record | `fossil-record` | g8 | `elem.fossils-and-past-life` |
| Comparing anatomy to infer relatedness | `comparative-anatomy` | g8 | `fossil-record` |
| Comparing embryo development across species | `embryo-similarities` | g8 | `comparative-anatomy` |
| Explaining natural selection | `natural-selection-intro` | g8 | `sexual-reproduction-variation`, `elem.variation-and-survival` |
| Explaining how traits spread over generations | `traits-spread-over-generations` | g8 | `natural-selection-intro`, `g7.experimental-probability` |
| Comparing artificial and natural selection | `artificial-selection` | g8 | `natural-selection-intro` |

### Microbes, health and classification

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing microorganisms | `microorganisms-intro` | g7 | `unicellular-and-multicellular` |
| Classifying organisms into kingdoms | `classification-and-kingdoms` | g7 | `elem.classifying-living-things`, `unicellular-and-multicellular` |
| Using dichotomous keys | `dichotomous-keys` | g7 | `classification-and-kingdoms` |
| Describing how the body defends against pathogens | `body-defences-intro` | g8 | `microorganisms-intro`, `body-systems-interact` |
| Explaining vaccines and antibiotics | `vaccines-and-antibiotics-intro` | g8 | `body-defences-intro` |

## bio.hs1: 86 topics

### Chemistry of life

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining water's properties that support life | `water-properties-for-life` | g9 | `ms.covalent-molecules-intro`, `ms.cells-as-basic-units` |
| Describing carbon as the backbone of biological molecules | `carbon-based-molecules` | g9 | `ms.molecules-and-extended-structures` |
| Classifying carbohydrates, lipids, proteins and nucleic acids | `macromolecule-classes` | g9 | `carbon-based-molecules` |
| Describing sugars and starches in cells | `carbohydrates-in-cells` | g9 | `macromolecule-classes` |
| Describing fats, phospholipids and steroids | `lipids-in-cells` | g9 | `macromolecule-classes` |
| Describing protein functions in cells | `protein-functions` | g9 | `macromolecule-classes` |
| Describing DNA and RNA as nucleic acids | `nucleic-acids-intro` | g9 | `macromolecule-classes` |
| Testing foods for macromolecules | `testing-for-macromolecules` | g9 | `carbohydrates-in-cells`, `protein-functions` |
| Explaining how enzymes speed reactions | `enzymes-as-catalysts` | g9 | `protein-functions`, `ms.reaction-speed-factors` |
| Testing temperature and pH effects on enzymes | `enzyme-activity-factors` | g9 | `enzymes-as-catalysts`, `ms.ph-scale-intro` |

### Cell structure

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing prokaryotic and eukaryotic cells | `prokaryotic-and-eukaryotic` | g9 | `ms.cell-parts` |
| Describing organelle functions | `organelle-functions` | g9 | `prokaryotic-and-eukaryotic`, `ms.plant-and-animal-cells` |
| Tracing proteins through the endomembrane system | `endomembrane-pathway` | g9 | `organelle-functions`, `protein-functions` |
| Explaining limits on cell size with surface area | `cell-size-limits` | g9 | `organelle-functions`, `alg1.ratio-equations` |
| Explaining the endosymbiotic origin of organelles | `endosymbiosis` | g9 | `organelle-functions` |
| Calculating magnification and cell size | `microscopy-and-magnification` | g9 | `ms.microscope-use`, `alg1.ratio-equations` |

### Membranes and transport

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing the fluid mosaic membrane | `membrane-structure` | g9 | `lipids-in-cells`, `ms.cell-membrane-role` |
| Explaining diffusion and osmosis | `diffusion-and-osmosis` | g9 | `membrane-structure`, `ms.solutions-solute-solvent` |
| Predicting cell responses to hypertonic and hypotonic solutions | `tonicity` | g9 | `diffusion-and-osmosis` |
| Describing facilitated diffusion through channels | `facilitated-diffusion` | g9 | `diffusion-and-osmosis` |
| Describing active transport and pumps | `active-transport` | g9 | `facilitated-diffusion` |
| Describing endocytosis and exocytosis | `endocytosis-and-exocytosis` | g9 | `active-transport`, `endomembrane-pathway` |

### Cellular energy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining ATP as the energy currency | `atp-energy-currency` | g9 | `nucleic-acids-intro`, `ms.cellular-respiration-intro` |
| Describing light reactions and the Calvin cycle | `photosynthesis-overview` | g9 | `ms.photosynthesis-intro`, `organelle-functions`, `atp-energy-currency` |
| Testing factors that affect photosynthesis rate | `photosynthesis-rate-factors` | g9 | `photosynthesis-overview` |
| Describing glycolysis, the Krebs cycle and electron transport | `cellular-respiration-overview` | g9 | `ms.cellular-respiration-intro`, `atp-energy-currency`, `organelle-functions` |
| Comparing fermentation and aerobic respiration | `fermentation` | g9 | `cellular-respiration-overview` |
| Linking photosynthesis and respiration | `photosynthesis-respiration-link` | g9 | `photosynthesis-overview`, `cellular-respiration-overview` |

### Cell division

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing phases of the cell cycle | `cell-cycle-phases` | g10 | `ms.cell-division-intro`, `organelle-functions` |
| Identifying stages of mitosis | `mitosis-stages` | g10 | `cell-cycle-phases` |
| Explaining cell cycle control and cancer | `cell-cycle-control-and-cancer` | g10 | `cell-cycle-phases` |
| Describing stages of meiosis | `meiosis-stages` | g10 | `mitosis-stages`, `ms.genes-and-chromosomes-intro` |
| Comparing mitosis and meiosis | `mitosis-vs-meiosis` | g10 | `meiosis-stages` |
| Explaining how crossing over and independent assortment create variation | `meiosis-and-variation` | g10 | `meiosis-stages`, `ms.sexual-reproduction-variation` |
| Explaining nondisjunction and chromosome disorders | `nondisjunction` | g10 | `meiosis-stages` |
| Reading karyotypes | `karyotypes` | g10 | `nondisjunction` |
| Describing stem cells and differentiation | `stem-cells-and-differentiation` | g10 | `mitosis-stages` |

### Molecular genetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing the structure of DNA | `dna-structure` | g10 | `nucleic-acids-intro` |
| Describing DNA replication | `dna-replication-overview` | g10 | `dna-structure` |
| Comparing DNA and RNA and the types of RNA | `rna-types` | g10 | `dna-structure` |
| Describing transcription | `transcription-overview` | g10 | `rna-types` |
| Using the genetic code to translate codons | `genetic-code` | g10 | `transcription-overview` |
| Describing translation | `translation-overview` | g10 | `genetic-code`, `protein-functions` |
| Classifying point and frameshift mutations | `mutation-types` | g10 | `translation-overview`, `ms.mutations-intro` |
| Explaining that cells regulate which genes are expressed | `gene-expression-regulation-intro` | g10 | `transcription-overview`, `stem-cells-and-differentiation` |

### Mendelian genetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining Mendel's experiments | `mendels-experiments` | g10 | `ms.punnett-squares-intro` |
| Solving monohybrid crosses | `monohybrid-crosses` | g10 | `mendels-experiments` |
| Using test crosses | `test-crosses` | g10 | `monohybrid-crosses` |
| Solving dihybrid crosses | `dihybrid-crosses` | g10 | `monohybrid-crosses`, `meiosis-and-variation` |
| Solving incomplete dominance and codominance crosses | `incomplete-and-codominance` | g10 | `monohybrid-crosses` |
| Solving blood type crosses with multiple alleles | `blood-type-crosses` | g10 | `incomplete-and-codominance` |
| Solving sex-linked crosses | `sex-linked-traits` | g10 | `monohybrid-crosses`, `meiosis-stages` |
| Analyzing pedigrees | `pedigrees` | g10 | `sex-linked-traits` |
| Explaining polygenic and environmentally influenced traits | `polygenic-and-environmental-traits` | g10 | `dihybrid-crosses` |
| Describing common genetic disorders | `genetic-disorders` | g10 | `pedigrees`, `mutation-types` |

### Biotechnology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Interpreting gel electrophoresis | `gel-electrophoresis` | g10 | `dna-structure` |
| Describing PCR | `pcr-intro` | g10 | `dna-replication-overview` |
| Describing recombinant DNA and genetically modified organisms | `recombinant-dna` | g10 | `ms.genetic-engineering-intro`, `dna-structure` |
| Using DNA fingerprints | `dna-fingerprinting` | g10 | `gel-electrophoresis`, `pcr-intro` |
| Describing gene editing | `gene-editing-intro` | g10 | `recombinant-dna` |
| Evaluating ethical issues in biotechnology | `biotechnology-ethics` | g10 | `recombinant-dna` |

### Evolution

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using fossils, anatomy and molecules as evidence for evolution | `evidence-for-evolution` | g10 | `ms.comparative-anatomy`, `ms.embryo-similarities`, `dna-structure` |
| Explaining natural selection with variation, inheritance and selection | `natural-selection-mechanism` | g10 | `ms.natural-selection-intro`, `mutation-types` |
| Comparing stabilizing, directional and disruptive selection | `selection-patterns` | g10 | `natural-selection-mechanism` |
| Describing genetic drift and gene flow | `genetic-drift-and-gene-flow` | g10 | `natural-selection-mechanism` |
| Explaining speciation through isolation | `speciation-intro` | g10 | `genetic-drift-and-gene-flow` |
| Explaining evolution of antibiotic resistance | `antibiotic-resistance-evolution` | g10 | `natural-selection-mechanism`, `ms.vaccines-and-antibiotics-intro` |
| Describing hypotheses for the origin of life | `origin-of-life-hypotheses` | g10 | `evidence-for-evolution` |

### Classification and diversity

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using binomial nomenclature | `binomial-nomenclature` | g10 | `ms.classification-and-kingdoms` |
| Classifying organisms into three domains | `three-domains` | g10 | `binomial-nomenclature`, `prokaryotic-and-eukaryotic` |
| Reading cladograms | `cladograms` | g10 | `three-domains`, `evidence-for-evolution` |
| Describing virus structure and replication | `viruses` | g10 | `prokaryotic-and-eukaryotic`, `dna-structure` |
| Describing bacterial diversity and roles | `bacteria-diversity` | g10 | `three-domains` |
| Describing protists and fungi | `protists-and-fungi` | g10 | `three-domains` |
| Describing major plant groups | `plant-diversity` | g10 | `three-domains`, `ms.plant-reproduction-structures` |
| Describing major animal groups | `animal-diversity` | g10 | `three-domains`, `ms.comparative-anatomy` |

### Ecology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing major biomes | `biomes` | g9 | `ms.ecosystem-change` |
| Calculating energy transfer between trophic levels | `trophic-energy-transfer` | g9 | `ms.energy-pyramids`, `g7.percent-equation` |
| Describing carbon, nitrogen and water cycles | `biogeochemical-cycles` | g9 | `ms.carbon-cycle-intro`, `photosynthesis-respiration-link` |
| Comparing exponential and logistic growth | `population-growth-curves` | g9 | `ms.populations-and-resources`, `alg1.exponential-stories` |
| Explaining carrying capacity and limiting factors | `carrying-capacity-and-limiting-factors` | g9 | `population-growth-curves` |
| Analyzing symbiosis and competition | `community-interactions` | g9 | `ms.ecological-interactions` |
| Describing ecological succession | `ecological-succession` | g9 | `community-interactions` |
| Evaluating human impacts on ecosystems | `human-impacts-on-ecosystems` | g9 | `biogeochemical-cycles`, `ms.biodiversity-and-ecosystem-services` |
| Evaluating conservation strategies | `conservation-strategies` | g9 | `human-impacts-on-ecosystems` |
| Explaining homeostasis with feedback loops | `homeostasis-and-feedback` | g9 | `ms.body-systems-interact` |

## bio.hs2: 66 topics

### Biochemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing dehydration synthesis and hydrolysis | `dehydration-and-hydrolysis` | g11 | `hs1.macromolecule-classes`, `hs1.functional-groups-intro` |
| Relating carbohydrate structure to function | `carbohydrate-structure-and-function` | g11 | `dehydration-and-hydrolysis`, `hs1.carbohydrates-in-cells` |
| Relating lipid structure to function | `lipid-structure-and-function` | g11 | `dehydration-and-hydrolysis`, `hs1.lipids-in-cells` |
| Describing four levels of protein structure | `protein-structure-levels` | g11 | `dehydration-and-hydrolysis`, `hs1.protein-functions` |
| Classifying amino acids by side chain properties | `side-chain-properties` | g11 | `protein-structure-levels`, `hs1.molecular-polarity` |
| Describing nucleotide structure and strand direction | `nucleotide-structure-and-strand-direction` | g11 | `dehydration-and-hydrolysis`, `hs1.dna-structure` |
| Explaining enzyme specificity and active sites | `active-sites-and-specificity` | g11 | `protein-structure-levels`, `hs1.enzymes-as-catalysts` |
| Explaining competitive and allosteric regulation | `enzyme-regulation-intro` | g11 | `active-sites-and-specificity` |
| Showing enzymes lowering activation energy | `enzymes-and-activation-energy` | g11 | `active-sites-and-specificity`, `hs1.energy-diagrams-of-reactions` |

### Cells and membranes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Predicting membrane permeability from polarity | `membrane-permeability` | g11 | `hs1.membrane-structure`, `hs1.molecular-polarity` |
| Calculating water potential | `water-potential` | g11 | `hs1.tonicity` |
| Calculating surface area to volume ratios | `surface-area-to-volume-calculations` | g11 | `hs1.cell-size-limits` |
| Describing cytoskeleton functions | `cytoskeleton-intro` | g11 | `hs1.organelle-functions` |
| Explaining benefits of compartmentalization | `compartmentalization` | g11 | `hs1.endomembrane-pathway`, `hs1.endosymbiosis` |

### Cellular energetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Tracking electron carriers in metabolism | `electron-carriers-in-metabolism` | g12 | `hs1.cellular-respiration-overview` |
| Tracing glycolysis inputs and outputs | `glycolysis-details` | g12 | `electron-carriers-in-metabolism` |
| Tracing the Krebs cycle | `krebs-cycle-details` | g12 | `glycolysis-details` |
| Explaining chemiosmosis and ATP synthase | `chemiosmosis` | g12 | `krebs-cycle-details` |
| Counting ATP yield from glucose | `atp-yield-accounting` | g12 | `chemiosmosis` |
| Tracing electron flow in the light reactions | `light-reactions-details` | g12 | `hs1.photosynthesis-overview`, `chemiosmosis` |
| Tracing carbon fixation in the Calvin cycle | `calvin-cycle-details` | g12 | `light-reactions-details` |
| Comparing C3, C4 and CAM plants | `c4-and-cam-plants` | g12 | `calvin-cycle-details` |
| Relating pigments to absorption spectra | `pigments-and-absorption-spectra` | g12 | `hs1.photosynthesis-overview`, `hs1.emission-and-absorption` |
| Predicting effects of metabolic inhibitors | `metabolic-inhibitors` | g12 | `chemiosmosis` |

### Cell communication and the cell cycle

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing direct, local and long-distance signalling | `signalling-distances` | g11 | `hs1.homeostasis-and-feedback` |
| Describing reception, transduction and response | `signal-transduction-steps` | g11 | `signalling-distances`, `protein-structure-levels` |
| Explaining second messengers and amplification | `second-messengers` | g11 | `signal-transduction-steps` |
| Analyzing positive and negative feedback | `feedback-in-physiology` | g11 | `hs1.homeostasis-and-feedback` |
| Explaining checkpoints, cyclins and kinases | `cell-cycle-checkpoints` | g11 | `hs1.cell-cycle-control-and-cancer`, `signal-transduction-steps` |
| Describing apoptosis | `apoptosis` | g11 | `cell-cycle-checkpoints` |

### Gene expression

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing enzymes of DNA replication | `replication-enzymes` | g12 | `hs1.dna-replication-overview`, `nucleotide-structure-and-strand-direction` |
| Explaining leading and lagging strands | `leading-and-lagging-strands` | g12 | `replication-enzymes` |
| Describing RNA processing in eukaryotes | `rna-processing` | g12 | `hs1.transcription-overview` |
| Describing initiation, elongation and termination | `translation-steps` | g12 | `hs1.translation-overview` |
| Explaining lac and trp operons | `operons` | g12 | `hs1.gene-expression-regulation-intro` |
| Describing eukaryotic gene regulation | `eukaryotic-gene-regulation` | g12 | `rna-processing`, `hs1.gene-expression-regulation-intro` |
| Describing epigenetic changes | `epigenetics-intro` | g12 | `eukaryotic-gene-regulation` |
| Predicting effects of mutations on proteins | `mutation-effects-on-proteins` | g12 | `hs1.mutation-types`, `translation-steps` |
| Describing transformation, conjugation and plasmids | `plasmids-and-transformation` | g12 | `hs1.recombinant-dna`, `hs1.bacteria-diversity` |
| Describing DNA sequencing | `dna-sequencing-intro` | g12 | `hs1.pcr-intro` |

### Genetics and evolution

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using recombination frequency to map genes | `linked-genes-and-recombination` | g12 | `hs1.dihybrid-crosses`, `hs1.meiosis-and-variation` |
| Using product and sum rules in genetics | `probability-rules-in-genetics` | g12 | `hs1.dihybrid-crosses` |
| Explaining environmental effects on phenotype | `environmental-effects-on-phenotype` | g12 | `hs1.polygenic-and-environmental-traits` |
| Using Hardy-Weinberg equilibrium | `hardy-weinberg` | g12 | `hs1.genetic-drift-and-gene-flow`, `probability-rules-in-genetics` |
| Building phylogenetic trees from data | `phylogenetic-trees` | g12 | `hs1.cladograms` |
| Comparing allopatric and sympatric speciation | `speciation-mechanisms` | g12 | `hs1.speciation-intro` |
| Classifying reproductive isolation barriers | `reproductive-isolation` | g12 | `speciation-mechanisms` |
| Describing divergent, convergent and coevolution | `patterns-of-evolution` | g12 | `hs1.selection-patterns` |
| Explaining extinction and adaptive radiation | `extinction-and-adaptive-radiation` | g12 | `patterns-of-evolution` |

### Ecology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating population growth rates | `population-growth-calculations` | g12 | `hs1.population-growth-curves` |
| Classifying density-dependent and independent factors | `density-dependent-factors` | g12 | `hs1.carrying-capacity-and-limiting-factors` |
| Calculating species diversity | `species-diversity-indices` | g12 | `hs1.community-interactions`, `g7.percent-equation` |
| Explaining keystone species and trophic cascades | `keystone-species-and-trophic-cascades` | g12 | `hs1.community-interactions` |
| Calculating primary productivity | `primary-productivity` | g12 | `hs1.trophic-energy-transfer` |
| Explaining innate and learned behaviours | `animal-behaviour` | g12 | `hs1.animal-diversity` |
| Describing plant and animal responses to environment | `responses-to-environment` | g12 | `feedback-in-physiology` |

### Human physiology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing digestion and absorption | `digestive-system` | g12 | `active-sites-and-specificity` |
| Tracing blood through the heart and vessels | `circulatory-system` | g12 | `hs1.homeostasis-and-feedback` |
| Describing blood components | `blood-composition` | g12 | `circulatory-system` |
| Explaining gas exchange in the lungs | `respiratory-system` | g12 | `circulatory-system`, `hs1.diffusion-and-osmosis` |
| Explaining how kidneys filter blood | `excretory-system` | g12 | `circulatory-system`, `hs1.active-transport` |
| Describing neurons and nerve impulses | `nervous-system-overview` | g12 | `hs1.active-transport`, `signalling-distances` |
| Describing hormones and glands | `endocrine-system` | g12 | `signal-transduction-steps`, `feedback-in-physiology` |
| Describing innate and adaptive immunity | `immune-system` | g12 | `hs1.viruses`, `circulatory-system` |
| Describing human reproductive systems | `reproductive-system` | g12 | `endocrine-system`, `hs1.meiosis-stages` |
| Describing muscle contraction and the skeleton | `muscles-and-skeleton` | g12 | `nervous-system-overview` |

## bio.intro1: 33 topics

### Cells and energy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing channels, carriers and pumps | `transport-proteins-compared` | uni-lower | `hs2.membrane-permeability`, `hs1.active-transport` |
| Explaining electrochemical gradients across membranes | `electrochemical-gradients` | uni-lower | `transport-proteins-compared`, `hs2.chemiosmosis` |
| Describing resting membrane potential | `membrane-potential-intro` | uni-lower | `electrochemical-gradients` |
| Explaining signal sequences and protein sorting | `protein-sorting-signals` | uni-lower | `hs2.compartmentalization`, `hs2.translation-steps` |
| Describing vesicle trafficking between organelles | `vesicle-trafficking` | uni-lower | `protein-sorting-signals` |
| Describing microtubules, actin and motor proteins | `cytoskeleton-and-motor-proteins` | uni-lower | `hs2.cytoskeleton-intro` |
| Describing cell junctions and the extracellular matrix | `cell-junctions-and-matrix` | uni-lower | `cytoskeleton-and-motor-proteins` |
| Relating free energy to coupled cellular reactions | `free-energy-and-coupling` | uni-lower | `hs2.enzymes-and-activation-energy`, `hs1.atp-energy-currency` |
| Explaining feedback inhibition of pathways | `metabolic-pathway-regulation` | uni-lower | `hs2.enzyme-regulation-intro`, `hs2.atp-yield-accounting` |
| Explaining photorespiration | `photorespiration` | uni-lower | `hs2.c4-and-cam-plants` |
| Linking fat and protein breakdown to respiration | `fat-and-protein-catabolism` | uni-lower | `hs2.atp-yield-accounting` |

### Signalling and the cell cycle

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing G protein, kinase and ion channel receptors | `receptor-types` | uni-lower | `hs2.second-messengers` |
| Tracing a kinase cascade | `kinase-cascades` | uni-lower | `receptor-types` |
| Explaining cyclin-dependent kinase control of the cell cycle | `cdk-control-of-the-cycle` | uni-lower | `hs2.cell-cycle-checkpoints`, `kinase-cascades` |
| Explaining oncogenes and tumour suppressors | `oncogenes-and-tumour-suppressors` | uni-lower | `cdk-control-of-the-cycle`, `hs2.mutation-effects-on-proteins` |

### Genetics and genomes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Linking Mendel's laws to chromosome behaviour | `chromosome-theory-of-inheritance` | uni-lower | `hs1.meiosis-and-variation`, `hs1.sex-linked-traits` |
| Analyzing epistasis ratios | `epistasis` | uni-lower | `hs1.dihybrid-crosses`, `hs2.probability-rules-in-genetics` |
| Comparing sex determination systems | `sex-determination-systems` | uni-lower | `hs1.sex-linked-traits` |
| Explaining X inactivation | `x-inactivation` | uni-lower | `sex-determination-systems`, `hs2.epigenetics-intro` |
| Describing deletions, duplications, inversions and translocations | `chromosomal-rearrangements` | uni-lower | `hs1.karyotypes` |
| Describing DNA repair mechanisms | `dna-repair` | uni-lower | `hs2.replication-enzymes`, `hs2.mutation-effects-on-proteins` |
| Explaining telomeres and telomerase | `telomeres` | uni-lower | `hs2.leading-and-lagging-strands` |
| Describing chromatin packaging | `chromatin-structure` | uni-lower | `hs2.eukaryotic-gene-regulation` |
| Describing microRNA and RNA interference | `noncoding-rna` | uni-lower | `hs2.eukaryotic-gene-regulation` |
| Comparing genome size and organization | `genome-organization` | uni-lower | `hs2.dna-sequencing-intro` |
| Using vectors to clone genes | `cloning-vectors` | uni-lower | `hs2.plasmids-and-transformation` |
| Measuring gene expression with RNA methods | `measuring-gene-expression` | uni-lower | `cloning-vectors`, `hs2.dna-sequencing-intro` |
| Comparing lytic and lysogenic cycles | `viral-life-cycles` | uni-lower | `hs1.viruses` |
| Explaining retroviruses and reverse transcription | `retroviruses` | uni-lower | `viral-life-cycles` |
| Explaining homeotic genes and development | `developmental-gene-regulation` | uni-lower | `hs2.eukaryotic-gene-regulation`, `hs1.stem-cells-and-differentiation` |
| Describing model organisms in research | `model-organisms` | uni-lower | `genome-organization` |

### Doing biology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing controlled biology experiments | `experimental-design-in-biology` | uni-lower | `hs1.enzyme-activity-factors` |
| Interpreting graphs and error bars in biological data | `interpreting-biological-data` | uni-lower | `experimental-design-in-biology` |

## bio.intro2: 54 topics

### Evolutionary processes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing mutation, selection, drift and gene flow | `population-genetics-forces` | uni-lower | `hs2.hardy-weinberg` |
| Explaining sexual selection | `sexual-selection` | uni-lower | `hs1.natural-selection-mechanism` |
| Explaining altruism with kin selection | `kin-selection-and-altruism` | uni-lower | `hs2.animal-behaviour`, `hs2.probability-rules-in-genetics` |
| Comparing species concepts | `species-concepts` | uni-lower | `hs2.reproductive-isolation` |
| Describing hybrid zones | `hybrid-zones` | uni-lower | `species-concepts` |
| Reading the geologic time scale | `geologic-time` | uni-lower | `hs2.extinction-and-adaptive-radiation` |
| Explaining evolution of development | `evo-devo` | uni-lower | `intro1.developmental-gene-regulation` |
| Building trees from sequence data | `molecular-phylogenetics` | uni-lower | `hs2.phylogenetic-trees`, `intro1.genome-organization` |
| Explaining horizontal gene transfer in trees | `horizontal-gene-transfer` | uni-lower | `molecular-phylogenetics` |

### Diversity of life

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing prokaryotic structure and metabolic diversity | `prokaryote-structure-and-metabolism` | uni-lower | `hs1.bacteria-diversity` |
| Describing archaea | `archaea` | uni-lower | `prokaryote-structure-and-metabolism` |
| Classifying major protist groups | `protist-diversity` | uni-lower | `hs1.protists-and-fungi`, `hs1.endosymbiosis` |
| Describing fungal life cycles | `fungal-life-cycles` | uni-lower | `hs1.protists-and-fungi` |
| Tracing plant adaptations to land | `plants-move-to-land` | uni-lower | `hs1.plant-diversity` |
| Explaining alternation of generations | `alternation-of-generations` | uni-lower | `plants-move-to-land`, `hs1.meiosis-stages` |
| Comparing gymnosperms and angiosperms | `seed-plants` | uni-lower | `alternation-of-generations` |
| Classifying animal body plans | `animal-body-plans` | uni-lower | `hs1.animal-diversity` |
| Describing major invertebrate phyla | `invertebrate-diversity` | uni-lower | `animal-body-plans` |
| Tracing vertebrate evolution | `vertebrate-evolution` | uni-lower | `animal-body-plans`, `geologic-time` |
| Tracing hominin evolution | `human-evolution` | uni-lower | `vertebrate-evolution` |

### Plant form and function

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing plant tissues and organs | `plant-tissues-and-organs` | uni-lower | `hs1.plant-diversity` |
| Explaining primary and secondary growth | `plant-growth-meristems` | uni-lower | `plant-tissues-and-organs` |
| Explaining water transport in xylem | `xylem-water-transport` | uni-lower | `plant-tissues-and-organs`, `hs2.water-potential` |
| Explaining sugar transport in phloem | `phloem-translocation` | uni-lower | `xylem-water-transport` |
| Describing plant nutrients and soil | `plant-nutrition-and-soil` | uni-lower | `plant-tissues-and-organs` |
| Describing flower structure and pollination | `flower-structure-and-pollination` | uni-lower | `seed-plants` |
| Describing seed development and germination | `seed-development-and-germination` | uni-lower | `flower-structure-and-pollination` |
| Describing plant hormones | `plant-hormones` | uni-lower | `plant-growth-meristems`, `hs2.signal-transduction-steps` |
| Explaining tropisms and photoperiodism | `tropisms-and-photoperiodism` | uni-lower | `plant-hormones` |
| Describing plant defences | `plant-defences` | uni-lower | `plant-hormones` |

### Animal form and function

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Relating animal tissues to homeostasis | `animal-tissues-and-homeostasis` | uni-lower | `hs2.feedback-in-physiology` |
| Comparing thermoregulation strategies | `thermoregulation` | uni-lower | `animal-tissues-and-homeostasis` |
| Comparing digestive systems across animals | `comparative-digestion` | uni-lower | `hs2.digestive-system` |
| Comparing circulatory systems across animals | `comparative-circulation` | uni-lower | `hs2.circulatory-system` |
| Comparing gas exchange across animals | `comparative-gas-exchange` | uni-lower | `hs2.respiratory-system` |
| Comparing osmoregulation and nitrogenous wastes | `osmoregulation-and-nitrogenous-wastes` | uni-lower | `hs2.excretory-system` |
| Comparing animal reproductive strategies | `reproductive-strategies` | uni-lower | `hs2.reproductive-system` |
| Describing fertilization, cleavage and gastrulation | `early-animal-development` | uni-lower | `reproductive-strategies` |
| Comparing nervous systems across animals | `comparative-nervous-systems` | uni-lower | `hs2.nervous-system-overview` |
| Classifying sensory receptors | `sensory-receptor-types` | uni-lower | `comparative-nervous-systems` |
| Explaining muscle contraction with sliding filaments | `sliding-filament-model` | uni-lower | `hs2.muscles-and-skeleton` |
| Explaining behaviour with fitness costs and benefits | `behavioural-ecology` | uni-lower | `hs2.animal-behaviour`, `kin-selection-and-altruism` |

### Ecology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining biome distribution with climate | `climate-and-biome-distribution` | uni-lower | `hs1.biomes` |
| Using life tables and survivorship curves | `life-tables-and-survivorship` | uni-lower | `hs2.population-growth-calculations` |
| Comparing r and K strategies | `life-history-strategies` | uni-lower | `life-tables-and-survivorship` |
| Using exponential and logistic growth equations | `growth-model-equations` | uni-lower | `hs2.population-growth-calculations`, `alg1.exponential-stories` |
| Predicting outcomes of species interactions | `interaction-outcomes` | uni-lower | `hs1.community-interactions` |
| Explaining niches and competitive exclusion | `niches-and-competitive-exclusion` | uni-lower | `interaction-outcomes` |
| Explaining community diversity and disturbance | `diversity-and-disturbance` | uni-lower | `hs2.species-diversity-indices`, `hs1.ecological-succession` |
| Using island biogeography | `island-biogeography` | uni-lower | `diversity-and-disturbance` |
| Calculating ecosystem energy budgets | `ecosystem-energy-budgets` | uni-lower | `hs2.primary-productivity` |
| Tracing nitrogen and phosphorus cycling | `nitrogen-and-phosphorus-cycling` | uni-lower | `hs1.biogeochemical-cycles` |
| Explaining biological impacts of climate change | `climate-change-biology` | uni-lower | `nitrogen-and-phosphorus-cycling`, `hs1.human-impacts-on-ecosystems` |
| Applying principles of conservation biology | `conservation-biology` | uni-lower | `climate-change-biology`, `hs1.conservation-strategies` |

## bio.cell-mol: 53 topics

### Membranes and transport

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining membrane fluidity and lipid rafts | `membrane-fluidity` | uni-upper | `hs2.membrane-permeability` |
| Predicting membrane protein topology | `membrane-protein-topology` | uni-upper | `membrane-fluidity`, `hs2.side-chain-properties` |
| Comparing transporter saturation kinetics | `transporter-kinetics` | uni-upper | `intro1.transport-proteins-compared`, `gen2.enzyme-kinetics-intro` |
| Calculating energetics of ion pumps | `ion-pump-energetics` | uni-upper | `intro1.electrochemical-gradients`, `gen2.gibbs-energy-nonstandard` |
| Calculating equilibrium potentials for ions | `equilibrium-potentials` | uni-upper | `intro1.membrane-potential-intro`, `gen2.nernst-equation` |
| Calculating resting potential with the Goldman equation | `goldman-equation` | uni-upper | `equilibrium-potentials` |
| Explaining cotransport | `secondary-active-transport` | uni-upper | `ion-pump-energetics` |

### Protein targeting and trafficking

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining nuclear import and export | `nuclear-transport` | uni-upper | `intro1.protein-sorting-signals` |
| Describing cotranslational import into the ER | `er-translocation` | uni-upper | `intro1.protein-sorting-signals` |
| Describing chaperones and ER quality control | `folding-quality-control` | uni-upper | `er-translocation` |
| Describing glycosylation in the ER and Golgi | `glycosylation` | uni-upper | `er-translocation` |
| Describing coat proteins and SNAREs | `vesicle-coats-and-fusion` | uni-upper | `intro1.vesicle-trafficking` |
| Comparing constitutive and regulated secretion | `regulated-secretion` | uni-upper | `vesicle-coats-and-fusion` |
| Tracing receptor-mediated endocytosis | `receptor-mediated-endocytosis` | uni-upper | `vesicle-coats-and-fusion` |
| Describing lysosomes and autophagy | `lysosomes-and-autophagy` | uni-upper | `receptor-mediated-endocytosis` |
| Explaining protein import into mitochondria and chloroplasts | `mitochondrial-protein-import` | uni-upper | `intro1.protein-sorting-signals` |
| Describing peroxisome function | `peroxisomes` | uni-upper | `mitochondrial-protein-import` |
| Describing ubiquitin-mediated degradation | `ubiquitin-proteasome` | uni-upper | `folding-quality-control` |

### Cytoskeleton and motility

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining actin polymerization and treadmilling | `actin-dynamics` | uni-upper | `intro1.cytoskeleton-and-motor-proteins` |
| Explaining dynamic instability of microtubules | `microtubule-dynamics` | uni-upper | `intro1.cytoskeleton-and-motor-proteins` |
| Explaining myosin, kinesin and dynein stepping | `motor-protein-mechanisms` | uni-upper | `actin-dynamics`, `microtubule-dynamics` |
| Describing cilia and flagella structure | `cilia-and-flagella` | uni-upper | `microtubule-dynamics`, `motor-protein-mechanisms` |
| Explaining cell migration | `cell-migration` | uni-upper | `actin-dynamics` |
| Describing intermediate filaments | `intermediate-filaments` | uni-upper | `intro1.cytoskeleton-and-motor-proteins` |

### Cell signalling

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing receptor binding and affinity | `receptor-ligand-binding` | uni-upper | `intro1.receptor-types`, `hs2.equilibrium-expressions` |
| Tracing G protein-coupled receptor pathways | `gpcr-signalling` | uni-upper | `receptor-ligand-binding`, `intro1.kinase-cascades` |
| Tracing receptor tyrosine kinase and Ras pathways | `rtk-and-ras-pathway` | uni-upper | `gpcr-signalling` |
| Explaining calcium and phosphoinositide signalling | `calcium-and-lipid-signalling` | uni-upper | `gpcr-signalling` |
| Explaining crosstalk between pathways | `signal-crosstalk` | uni-upper | `rtk-and-ras-pathway`, `calcium-and-lipid-signalling` |
| Describing nuclear hormone receptors | `nuclear-receptors` | uni-upper | `receptor-ligand-binding` |
| Explaining signal termination and desensitization | `signal-termination` | uni-upper | `gpcr-signalling` |
| Describing Wnt, Notch and Hedgehog signalling | `developmental-signalling-pathways` | uni-upper | `signal-crosstalk` |

### Cell cycle and cell death

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining cyclin-CDK oscillations | `cyclin-cdk-oscillations` | uni-upper | `intro1.cdk-control-of-the-cycle` |
| Explaining DNA damage checkpoints and p53 | `dna-damage-checkpoints` | uni-upper | `cyclin-cdk-oscillations`, `intro1.dna-repair` |
| Explaining spindle assembly and chromosome segregation | `spindle-mechanics` | uni-upper | `cyclin-cdk-oscillations`, `microtubule-dynamics` |
| Describing cytokinesis | `cytokinesis` | uni-upper | `spindle-mechanics`, `actin-dynamics` |
| Comparing intrinsic and extrinsic apoptosis | `apoptosis-pathways` | uni-upper | `hs2.apoptosis`, `dna-damage-checkpoints` |
| Explaining hallmarks of cancer cells | `cancer-cell-biology` | uni-upper | `intro1.oncogenes-and-tumour-suppressors`, `apoptosis-pathways`, `signal-crosstalk` |

### Gene expression mechanisms

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing RNA polymerases and transcription factors | `transcription-machinery` | uni-upper | `intro1.chromatin-structure` |
| Explaining enhancers and combinatorial control | `enhancers-and-combinatorial-control` | uni-upper | `transcription-machinery` |
| Explaining chromatin remodelling and histone modification | `histone-modification` | uni-upper | `transcription-machinery` |
| Explaining spliceosome function and alternative splicing | `splicing-mechanisms` | uni-upper | `hs2.rna-processing` |
| Explaining mRNA stability and localization | `mrna-stability-and-localization` | uni-upper | `splicing-mechanisms`, `intro1.noncoding-rna` |
| Explaining translational regulation | `translational-control` | uni-upper | `mrna-stability-and-localization` |
| Explaining replication origin licensing | `replication-licensing` | uni-upper | `hs2.replication-enzymes`, `cyclin-cdk-oscillations` |

### Cells in tissues

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing cadherins and integrins | `adhesion-molecules` | uni-upper | `intro1.cell-junctions-and-matrix` |
| Describing collagen and matrix proteins | `matrix-composition` | uni-upper | `intro1.cell-junctions-and-matrix` |
| Explaining stem cell niches | `stem-cell-niches` | uni-upper | `adhesion-molecules`, `developmental-signalling-pathways` |

### Methods

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing light, fluorescence and electron microscopy | `microscopy-techniques` | uni-upper | `hs1.microscopy-and-magnification` |
| Using fluorescent protein tags | `fluorescent-protein-tagging` | uni-upper | `microscopy-techniques`, `intro1.cloning-vectors` |
| Separating organelles by centrifugation | `cell-fractionation` | uni-upper | `hs1.organelle-functions` |
| Detecting proteins by western blot and immunostaining | `protein-detection-methods` | uni-upper | `cell-fractionation` |
| Using knockouts and RNA interference to test function | `loss-of-function-methods` | uni-upper | `intro1.noncoding-rna`, `intro1.model-organisms` |

## bio.genetics: 41 topics

### Transmission genetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using binomial probability for families | `binomial-probability-in-families` | uni-upper | `hs2.probability-rules-in-genetics`, `stats.binomial-calculations` |
| Testing cross data with chi-square | `chi-square-tests-of-crosses` | uni-upper | `stats.chi-square-gof`, `hs1.dihybrid-crosses` |
| Analyzing lethal alleles, penetrance and expressivity | `lethal-alleles-and-penetrance` | uni-upper | `intro1.epistasis` |
| Using complementation tests | `complementation-tests` | uni-upper | `lethal-alleles-and-penetrance` |
| Calculating risks from pedigrees | `pedigree-risk` | uni-upper | `hs1.pedigrees`, `binomial-probability-in-families` |
| Relating genetic disorders to molecular mechanisms | `disorder-mechanisms` | uni-upper | `pedigree-risk`, `hs1.genetic-disorders` |

### Linkage and mapping

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Mapping genes with three-point crosses | `three-point-mapping` | uni-upper | `hs2.linked-genes-and-recombination` |
| Calculating interference | `interference-and-coincidence` | uni-upper | `three-point-mapping` |
| Correcting map distances for multiple crossovers | `mapping-functions` | uni-upper | `interference-and-coincidence` |
| Mapping with tetrad analysis | `tetrad-analysis` | uni-upper | `three-point-mapping` |
| Using LOD scores for human linkage | `lod-scores` | uni-upper | `three-point-mapping`, `pedigree-risk` |

### Chromosomes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing centromeres, banding and chromosome structure | `cytogenetics` | uni-upper | `intro1.chromosomal-rearrangements` |
| Explaining aneuploidy and polyploidy | `aneuploidy-and-polyploidy` | uni-upper | `cytogenetics`, `hs1.nondisjunction` |
| Predicting meiotic consequences of inversions and translocations | `rearrangements-in-meiosis` | uni-upper | `aneuploidy-and-polyploidy` |
| Explaining mitochondrial and chloroplast inheritance | `organelle-inheritance` | uni-upper | `intro1.chromosome-theory-of-inheritance` |
| Explaining genomic imprinting | `genomic-imprinting` | uni-upper | `intro1.x-inactivation` |

### Bacterial and viral genetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Mapping genes by conjugation | `conjugation-mapping` | uni-upper | `hs2.plasmids-and-transformation` |
| Mapping genes by transduction and transformation | `transduction-mapping` | uni-upper | `conjugation-mapping` |
| Analyzing phage crosses | `phage-genetics` | uni-upper | `intro1.viral-life-cycles` |
| Describing transposable elements | `transposable-elements` | uni-upper | `intro1.genome-organization` |

### Molecular genetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating mutation rates and testing mutagens | `mutation-rates-and-mutagens` | uni-upper | `hs2.mutation-effects-on-proteins` |
| Designing forward genetic screens | `forward-genetic-screens` | uni-upper | `mutation-rates-and-mutagens`, `complementation-tests` |
| Describing homologous recombination | `recombination-mechanisms` | uni-upper | `intro1.dna-repair` |
| Analyzing operon mutants with partial diploids | `operon-mutant-analysis` | uni-upper | `hs2.operons`, `complementation-tests` |
| Analyzing regulatory mutations in eukaryotes | `eukaryotic-regulatory-mutants` | uni-upper | `operon-mutant-analysis`, `intro1.chromatin-structure` |
| Explaining epigenetic inheritance | `epigenetic-inheritance` | uni-upper | `genomic-imprinting` |

### Genomics and biotechnology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing sequencing technologies | `sequencing-technologies` | uni-upper | `intro1.genome-organization` |
| Describing genome assembly and annotation | `genome-assembly-and-annotation` | uni-upper | `sequencing-technologies` |
| Using comparative genomics | `comparative-genomics` | uni-upper | `genome-assembly-and-annotation` |
| Using reverse genetics and gene editing | `reverse-genetics-and-editing` | uni-upper | `intro1.cloning-vectors`, `hs1.gene-editing-intro` |
| Making transgenic organisms | `transgenic-organisms` | uni-upper | `reverse-genetics-and-editing` |
| Describing gene therapy | `gene-therapy` | uni-upper | `transgenic-organisms` |
| Evaluating genetic testing and its ethics | `genetic-testing` | uni-upper | `disorder-mechanisms` |

### Quantitative and population genetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing quantitative traits | `quantitative-traits` | uni-upper | `hs1.polygenic-and-environmental-traits`, `stats.standard-deviation-calc` |
| Estimating heritability | `heritability` | uni-upper | `quantitative-traits`, `stats.correlation-properties` |
| Describing QTL mapping | `qtl-mapping` | uni-upper | `heritability`, `three-point-mapping` |
| Interpreting genome-wide association studies | `association-studies` | uni-upper | `lod-scores`, `quantitative-traits` |
| Calculating allele and genotype frequencies | `allele-frequency-calculations` | uni-upper | `hs2.hardy-weinberg` |
| Calculating inbreeding coefficients | `inbreeding` | uni-upper | `allele-frequency-calculations` |
| Finding mutation-selection balance | `mutation-selection-balance` | uni-upper | `allele-frequency-calculations` |
| Calculating effects of drift and effective population size | `drift-and-effective-size` | uni-upper | `allele-frequency-calculations` |

## bio.biochem: 52 topics

### Proteins

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating amino acid charge and isoelectric point | `amino-acid-charge-and-pi` | uni-upper | `org2.amino-acids-and-peptides`, `gen2.fractional-composition` |
| Explaining peptide bond planarity and torsion angles | `peptide-bond-geometry` | uni-upper | `org2.amino-acids-and-peptides` |
| Describing alpha helices and beta sheets | `secondary-structure` | uni-upper | `peptide-bond-geometry`, `hs2.protein-structure-levels` |
| Explaining forces that stabilize protein folds | `folding-forces` | uni-upper | `secondary-structure` |
| Explaining protein folding energetics | `folding-thermodynamics` | uni-upper | `folding-forces`, `gen2.gibbs-energy-and-k` |
| Purifying proteins by chromatography and electrophoresis | `protein-purification` | uni-upper | `amino-acid-charge-and-pi` |
| Determining protein sequences by mass spectrometry | `protein-sequencing` | uni-upper | `protein-purification` |
| Comparing crystallography, NMR and cryo-electron microscopy | `structure-determination` | uni-upper | `folding-forces` |
| Comparing oxygen binding by myoglobin and hemoglobin | `myoglobin-and-hemoglobin` | uni-upper | `folding-forces` |
| Explaining cooperative binding and allostery | `allostery-and-cooperativity` | uni-upper | `myoglobin-and-hemoglobin` |

### Enzymes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining enzyme catalytic strategies | `catalytic-strategies` | uni-upper | `hs2.active-sites-and-specificity`, `folding-forces` |
| Deriving the Michaelis-Menten equation (moved from `chem.pchem1.michaelis-menten`) | `michaelis-menten` | uni-upper | `gen2.steady-state-intermediates`, `gen2.enzyme-kinetics-intro` |
| Analyzing enzyme inhibition (moved from `chem.pchem1.enzyme-inhibition`) | `enzyme-inhibition` | uni-upper | `michaelis-menten` |
| Interpreting turnover number, Km and catalytic efficiency | `kinetic-parameters` | uni-upper | `michaelis-menten` |
| Distinguishing sequential and ping-pong mechanisms | `multisubstrate-kinetics` | uni-upper | `michaelis-menten` |
| Explaining the serine protease mechanism | `serine-protease-mechanism` | uni-upper | `catalytic-strategies` |
| Describing coenzymes and vitamins | `coenzymes-and-vitamins` | uni-upper | `catalytic-strategies` |
| Explaining allosteric and covalent enzyme regulation | `enzyme-regulation-mechanisms` | uni-upper | `allostery-and-cooperativity`, `enzyme-inhibition` |

### Carbohydrates, lipids and nucleic acids

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing polysaccharides and glycoproteins | `polysaccharides-and-glycoconjugates` | uni-upper | `org2.glycosidic-bonds` |
| Classifying membrane lipids | `membrane-lipid-classes` | uni-upper | `org2.lipids-and-saponification` |
| Calculating free energy of membrane transport | `transport-thermodynamics` | uni-upper | `cell-mol.ion-pump-energetics` |
| Describing nucleic acid stability and hybridization | `nucleic-acid-stability` | uni-upper | `org2.nucleic-acid-structure` |

### Bioenergetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using biochemical standard Gibbs energies | `biochemical-standard-states` | uni-upper | `gen2.gibbs-energy-nonstandard` |
| Explaining phosphoryl transfer potential | `phosphoryl-transfer-potential` | uni-upper | `biochemical-standard-states` |
| Relating reduction potential to free energy in biology | `biological-redox-energetics` | uni-upper | `biochemical-standard-states`, `gen2.gibbs-energy-and-cell-potential` |

### Carbohydrate metabolism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Tracing glycolysis enzymes and regulation | `glycolysis-regulation` | uni-upper | `hs2.glycolysis-details`, `enzyme-regulation-mechanisms` |
| Describing fates of pyruvate | `fates-of-pyruvate` | uni-upper | `glycolysis-regulation` |
| Tracing gluconeogenesis | `gluconeogenesis` | uni-upper | `glycolysis-regulation` |
| Explaining reciprocal regulation of glycolysis and gluconeogenesis | `reciprocal-regulation` | uni-upper | `gluconeogenesis` |
| Explaining glycogen synthesis and breakdown | `glycogen-metabolism` | uni-upper | `reciprocal-regulation` |
| Tracing the pentose phosphate pathway | `pentose-phosphate-pathway` | uni-upper | `glycolysis-regulation` |

### Aerobic metabolism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining pyruvate dehydrogenase | `pyruvate-dehydrogenase` | uni-upper | `fates-of-pyruvate`, `coenzymes-and-vitamins` |
| Tracing citric acid cycle reactions | `citric-acid-cycle-reactions` | uni-upper | `pyruvate-dehydrogenase`, `hs2.krebs-cycle-details` |
| Explaining citric acid cycle regulation | `citric-acid-cycle-regulation` | uni-upper | `citric-acid-cycle-reactions` |
| Tracing electrons through the respiratory complexes | `respiratory-complexes` | uni-upper | `citric-acid-cycle-reactions`, `biological-redox-energetics` |
| Explaining the ATP synthase rotary mechanism | `atp-synthase-mechanism` | uni-upper | `respiratory-complexes` |
| Explaining respiratory control and uncoupling | `respiratory-control-and-uncoupling` | uni-upper | `atp-synthase-mechanism` |

### Lipid and nitrogen metabolism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Tracing beta-oxidation of fatty acids | `beta-oxidation` | uni-upper | `membrane-lipid-classes`, `citric-acid-cycle-reactions` |
| Describing ketone body metabolism | `ketone-bodies` | uni-upper | `beta-oxidation` |
| Tracing fatty acid synthesis | `fatty-acid-synthesis` | uni-upper | `beta-oxidation`, `pentose-phosphate-pathway` |
| Describing cholesterol synthesis and regulation | `cholesterol-metabolism` | uni-upper | `fatty-acid-synthesis` |
| Explaining transamination and deamination | `amino-acid-degradation` | uni-upper | `citric-acid-cycle-reactions`, `coenzymes-and-vitamins` |
| Tracing the urea cycle | `urea-cycle` | uni-upper | `amino-acid-degradation` |
| Describing amino acid biosynthesis | `amino-acid-biosynthesis` | uni-upper | `amino-acid-degradation` |
| Describing nucleotide synthesis and salvage | `nucleotide-metabolism` | uni-upper | `amino-acid-biosynthesis`, `pentose-phosphate-pathway` |

### Integration and information flow

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Integrating metabolism in fed and fasted states | `fed-and-fasted-metabolism` | uni-upper | `glycogen-metabolism`, `fatty-acid-synthesis`, `ketone-bodies` |
| Explaining insulin and glucagon signalling | `hormonal-control-of-metabolism` | uni-upper | `fed-and-fasted-metabolism`, `cell-mol.rtk-and-ras-pathway` |
| Explaining diabetes and inborn errors of metabolism | `metabolic-diseases` | uni-upper | `hormonal-control-of-metabolism`, `urea-cycle` |
| Explaining polymerase fidelity and proofreading | `polymerase-fidelity` | uni-upper | `nucleic-acid-stability`, `cell-mol.replication-licensing` |
| Explaining RNA polymerase mechanism | `rna-polymerase-mechanism` | uni-upper | `nucleic-acid-stability`, `cell-mol.transcription-machinery` |
| Explaining aminoacyl-tRNA synthetases and ribosome catalysis | `ribosome-and-trna-biochemistry` | uni-upper | `rna-polymerase-mechanism` |
| Expressing and analyzing recombinant proteins | `recombinant-protein-expression` | uni-upper | `protein-purification`, `intro1.cloning-vectors` |

## bio.ecology: 33 topics

### Organisms and environment

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Relating physiology to environmental tolerance | `physiological-ecology` | uni-upper | `intro2.thermoregulation` |
| Explaining climate drivers of ecological patterns | `climate-drivers-of-ecology` | uni-upper | `intro2.climate-and-biome-distribution` |

### Populations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Modelling population growth with derivatives | `continuous-population-growth` | uni-upper | `intro2.growth-model-equations`, `calc1.derivative-of-exponential` |
| Projecting populations with matrix models | `matrix-population-models` | uni-upper | `intro2.life-tables-and-survivorship`, `precalc.matrix-transformations` |
| Testing for density dependence | `population-regulation` | uni-upper | `continuous-population-growth` |
| Modelling metapopulations | `metapopulations` | uni-upper | `continuous-population-growth` |
| Finding maximum sustainable yield | `sustainable-harvest` | uni-upper | `continuous-population-growth`, `calc1.optimization-setup` |
| Assessing population viability | `population-viability` | uni-upper | `metapopulations`, `matrix-population-models` |

### Species interactions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Predicting competition outcomes with isoclines | `competition-isoclines` | uni-upper | `intro2.niches-and-competitive-exclusion`, `continuous-population-growth` |
| Interpreting predator-prey cycles | `predator-prey-cycles` | uni-upper | `continuous-population-growth`, `intro2.interaction-outcomes` |
| Comparing predator functional responses | `functional-responses` | uni-upper | `predator-prey-cycles` |
| Analyzing mutualism and facilitation | `mutualism-and-facilitation` | uni-upper | `intro2.interaction-outcomes` |
| Modelling disease spread in populations | `disease-ecology` | uni-upper | `predator-prey-cycles` |
| Analyzing herbivory and plant responses | `herbivory-ecology` | uni-upper | `intro2.plant-defences` |

### Communities

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing food web structure | `food-web-structure` | uni-upper | `hs2.keystone-species-and-trophic-cascades` |
| Comparing diversity with rarefaction curves | `rarefaction` | uni-upper | `hs2.species-diversity-indices` |
| Using species-area relationships | `species-area-relationships` | uni-upper | `intro2.island-biogeography` |
| Comparing models of succession | `succession-models` | uni-upper | `intro2.diversity-and-disturbance` |
| Explaining the intermediate disturbance hypothesis | `intermediate-disturbance` | uni-upper | `succession-models` |
| Explaining community assembly | `community-assembly` | uni-upper | `species-area-relationships`, `competition-isoclines` |

### Ecosystems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining controls on ecosystem productivity | `productivity-controls` | uni-upper | `intro2.ecosystem-energy-budgets` |
| Explaining decomposition rates and nutrient release | `decomposition` | uni-upper | `intro2.nitrogen-and-phosphorus-cycling` |
| Calculating ecosystem carbon budgets | `carbon-budgets` | uni-upper | `decomposition`, `intro2.climate-change-biology` |
| Valuing ecosystem services | `ecosystem-services` | uni-upper | `productivity-controls` |
| Describing landscape patterns and connectivity | `landscape-ecology` | uni-upper | `metapopulations` |

### Ecological methods

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing ecological sampling | `ecological-sampling` | uni-upper | `stats.sampling-methods` |
| Estimating population size by mark-recapture | `mark-recapture` | uni-upper | `ecological-sampling` |
| Analyzing ecological data with regression | `ecological-regression` | uni-upper | `stats.least-squares-regression`, `ecological-sampling` |
| Describing species distribution models | `species-distribution-models` | uni-upper | `ecological-regression`, `intro2.climate-and-biome-distribution` |

### Applied ecology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing invasive species | `invasive-species` | uni-upper | `community-assembly` |
| Planning ecological restoration | `restoration-ecology` | uni-upper | `succession-models` |
| Designing nature reserves | `reserve-design` | uni-upper | `population-viability`, `landscape-ecology` |
| Predicting ecological responses to climate change | `climate-change-ecology` | uni-upper | `carbon-budgets`, `species-distribution-models` |

## bio.evolution: 32 topics

### Population genetic models

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Modelling selection on allele frequencies | `selection-models` | uni-upper | `genetics.allele-frequency-calculations` |
| Explaining heterozygote advantage | `heterozygote-advantage` | uni-upper | `selection-models` |
| Explaining frequency-dependent selection | `frequency-dependent-selection` | uni-upper | `selection-models` |
| Finding fixation probability under drift | `fixation-probability` | uni-upper | `genetics.drift-and-effective-size` |
| Describing coalescent theory | `coalescent-theory` | uni-upper | `fixation-probability` |
| Explaining the neutral theory | `neutral-theory` | uni-upper | `fixation-probability` |
| Dating divergences with molecular clocks | `molecular-clocks` | uni-upper | `neutral-theory`, `intro2.molecular-phylogenetics` |
| Detecting selection in sequence data | `detecting-selection` | uni-upper | `neutral-theory`, `genetics.comparative-genomics` |
| Measuring population structure | `population-structure` | uni-upper | `genetics.allele-frequency-calculations`, `intro2.population-genetics-forces` |
| Explaining linkage disequilibrium | `linkage-disequilibrium` | uni-upper | `genetics.three-point-mapping`, `selection-models` |
| Predicting response to selection with the breeder's equation | `breeders-equation` | uni-upper | `genetics.heritability` |

### Adaptation and behaviour

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Testing adaptive hypotheses | `testing-adaptations` | uni-upper | `intro2.sexual-selection` |
| Analyzing mechanisms of sexual selection | `sexual-selection-mechanisms` | uni-upper | `intro2.sexual-selection` |
| Explaining the evolution of sex and recombination | `evolution-of-sex` | uni-upper | `selection-models` |
| Explaining life history trade-offs | `life-history-evolution` | uni-upper | `intro2.life-history-strategies` |
| Using Hamilton's rule | `hamiltons-rule` | uni-upper | `intro2.kin-selection-and-altruism` |
| Using evolutionarily stable strategies | `evolutionary-game-theory` | uni-upper | `frequency-dependent-selection` |
| Explaining coevolutionary arms races | `coevolution` | uni-upper | `intro2.interaction-outcomes` |

### Speciation and phylogenetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining genetic causes of reproductive isolation | `genetics-of-isolation` | uni-upper | `intro2.hybrid-zones` |
| Explaining ecological speciation | `ecological-speciation` | uni-upper | `genetics-of-isolation` |
| Comparing parsimony, distance and likelihood trees | `tree-building-methods` | uni-upper | `intro2.molecular-phylogenetics` |
| Identifying homology and homoplasy on trees | `homology-and-homoplasy` | uni-upper | `tree-building-methods` |
| Using phylogenetic comparative methods | `comparative-methods` | uni-upper | `homology-and-homoplasy` |
| Explaining patterns of biogeography | `biogeography` | uni-upper | `intro2.island-biogeography`, `homology-and-homoplasy` |

### Macroevolution

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Dating fossils and reading the fossil record | `fossil-dating` | uni-upper | `intro2.geologic-time` |
| Analyzing mass extinctions | `mass-extinctions` | uni-upper | `fossil-dating` |
| Explaining adaptive radiations and key innovations | `key-innovations` | uni-upper | `mass-extinctions` |
| Explaining gene regulatory changes in evolution | `regulatory-evolution` | uni-upper | `intro2.evo-devo` |
| Describing major evolutionary transitions | `major-transitions` | uni-upper | `intro2.archaea`, `intro2.horizontal-gene-transfer` |
| Using genomics to study human evolution | `human-evolutionary-genomics` | uni-upper | `intro2.human-evolution`, `population-structure` |

### Applied evolution

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Applying evolution to medicine | `evolutionary-medicine` | uni-upper | `coevolution` |
| Interpreting experimental evolution studies | `experimental-evolution` | uni-upper | `selection-models` |

## bio.micro: 37 topics

### Microbial cells

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing Gram-positive and Gram-negative cell walls | `bacterial-cell-walls` | uni-upper | `intro2.prokaryote-structure-and-metabolism` |
| Identifying bacteria by staining and microscopy | `staining-and-identification` | uni-upper | `bacterial-cell-walls`, `cell-mol.microscopy-techniques` |
| Describing capsules, pili, flagella and endospores | `bacterial-surface-structures` | uni-upper | `bacterial-cell-walls` |
| Comparing archaeal and bacterial cells | `archaeal-cell-features` | uni-upper | `intro2.archaea` |

### Microbial growth and control

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Interpreting bacterial growth curves | `bacterial-growth-curves` | uni-upper | `intro2.growth-model-equations` |
| Calculating generation time | `generation-time` | uni-upper | `bacterial-growth-curves` |
| Choosing culture media and aseptic technique | `culture-techniques` | uni-upper | `bacterial-growth-curves` |
| Explaining temperature, pH and oxygen requirements | `growth-requirements` | uni-upper | `bacterial-growth-curves` |
| Comparing sterilization and disinfection | `sterilization-and-disinfection` | uni-upper | `growth-requirements` |
| Explaining antibiotic mechanisms | `antibiotic-mechanisms` | uni-upper | `sterilization-and-disinfection`, `bacterial-cell-walls` |
| Explaining antibiotic resistance mechanisms | `resistance-mechanisms` | uni-upper | `antibiotic-mechanisms`, `hs1.antibiotic-resistance-evolution` |

### Microbial metabolism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying microbes by energy and carbon source | `metabolic-diversity` | uni-upper | `intro2.prokaryote-structure-and-metabolism`, `hs2.electron-carriers-in-metabolism` |
| Explaining anaerobic respiration | `anaerobic-respiration` | uni-upper | `metabolic-diversity` |
| Comparing fermentation pathways | `fermentation-pathways` | uni-upper | `metabolic-diversity`, `hs1.fermentation` |
| Describing chemolithotrophy | `chemolithotrophy` | uni-upper | `metabolic-diversity` |
| Describing nitrogen fixation | `nitrogen-fixation` | uni-upper | `chemolithotrophy` |
| Comparing bacterial photosynthesis | `bacterial-photosynthesis` | uni-upper | `metabolic-diversity` |

### Microbial genetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining regulons and global regulation | `global-regulation` | uni-upper | `hs2.operons` |
| Explaining quorum sensing | `quorum-sensing` | uni-upper | `global-regulation` |
| Comparing transformation, transduction and conjugation | `horizontal-transfer-mechanisms` | uni-upper | `hs2.plasmids-and-transformation` |
| Describing biofilms | `biofilms` | uni-upper | `quorum-sensing` |
| Describing endospore formation | `sporulation` | uni-upper | `bacterial-surface-structures`, `global-regulation` |

### Viruses

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying viruses by genome type | `virus-classification` | uni-upper | `intro1.viral-life-cycles` |
| Comparing virus replication strategies | `virus-replication-strategies` | uni-upper | `virus-classification`, `intro1.retroviruses` |
| Counting viruses with plaque assays | `plaque-assays` | uni-upper | `virus-replication-strategies` |
| Describing prions | `prions` | uni-upper | `virus-classification` |

### Immunology and disease

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing innate immune defence mechanisms | `innate-defence-mechanisms` | uni-upper | `hs2.immune-system` |
| Describing B and T cell activation | `lymphocyte-activation` | uni-upper | `innate-defence-mechanisms` |
| Relating antibody structure to function | `antibody-structure` | uni-upper | `lymphocyte-activation` |
| Explaining vaccine types and immunization | `vaccine-types` | uni-upper | `antibody-structure` |
| Explaining virulence factors and pathogenesis | `virulence-factors` | uni-upper | `bacterial-surface-structures`, `innate-defence-mechanisms` |
| Calculating epidemiological rates | `epidemiology` | uni-upper | `virulence-factors` |
| Identifying pathogens in the lab | `diagnostic-microbiology` | uni-upper | `staining-and-identification`, `culture-techniques` |

### Applied microbiology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing microbiomes | `microbiomes` | uni-upper | `biofilms`, `metabolic-diversity` |
| Describing microbial roles in nutrient cycles | `microbes-in-nutrient-cycles` | uni-upper | `nitrogen-fixation` |
| Describing industrial and food microbiology | `industrial-microbiology` | uni-upper | `fermentation-pathways` |
| Describing bioremediation | `bioremediation` | uni-upper | `microbes-in-nutrient-cycles` |

## bio.anat-phys1: 59 topics

### Foundations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using anatomical position, planes and directions | `anatomical-terminology` | uni-lower | `hs1.homeostasis-and-feedback` |
| Naming body cavities and regions | `body-cavities-and-regions` | uni-lower | `anatomical-terminology` |
| Analyzing homeostatic control systems | `homeostatic-control-systems` | uni-lower | `hs2.feedback-in-physiology` |

### Tissues

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying epithelial tissues | `epithelial-tissue` | uni-lower | `intro1.cell-junctions-and-matrix` |
| Classifying connective tissues | `connective-tissue` | uni-lower | `epithelial-tissue` |
| Comparing muscle tissue types | `muscle-tissue-types` | uni-lower | `connective-tissue` |
| Describing nervous tissue | `nervous-tissue` | uni-lower | `muscle-tissue-types` |
| Describing body membranes | `body-membranes` | uni-lower | `epithelial-tissue`, `connective-tissue` |
| Describing tissue repair | `tissue-repair` | uni-lower | `connective-tissue` |

### Integumentary system

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing skin layers | `skin-layers` | uni-lower | `epithelial-tissue` |
| Describing hair, nails and glands | `skin-accessory-structures` | uni-lower | `skin-layers` |
| Explaining the skin's role in thermoregulation | `skin-and-thermoregulation` | uni-lower | `skin-layers`, `homeostatic-control-systems` |
| Classifying burns and skin cancers | `burns-and-skin-cancer` | uni-lower | `skin-layers` |

### Skeletal system

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing compact and spongy bone | `bone-tissue` | uni-lower | `connective-tissue` |
| Describing ossification and bone growth | `bone-growth` | uni-lower | `bone-tissue` |
| Explaining bone remodelling and calcium balance | `bone-remodelling` | uni-lower | `bone-growth`, `homeostatic-control-systems` |
| Identifying bones of the axial skeleton | `axial-skeleton` | uni-lower | `bone-tissue`, `body-cavities-and-regions` |
| Identifying bones of the appendicular skeleton | `appendicular-skeleton` | uni-lower | `axial-skeleton` |
| Classifying joints | `joint-classification` | uni-lower | `appendicular-skeleton` |
| Describing synovial joint movements | `synovial-joint-movements` | uni-lower | `joint-classification` |
| Describing fractures and bone disorders | `bone-disorders` | uni-lower | `bone-remodelling` |

### Muscular system

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing skeletal muscle structure | `skeletal-muscle-structure` | uni-lower | `muscle-tissue-types` |
| Describing the neuromuscular junction | `neuromuscular-junction` | uni-lower | `skeletal-muscle-structure`, `intro1.membrane-potential-intro` |
| Explaining cross-bridge cycling | `cross-bridge-cycle` | uni-lower | `skeletal-muscle-structure`, `intro1.cytoskeleton-and-motor-proteins` |
| Explaining excitation-contraction coupling | `excitation-contraction-coupling` | uni-lower | `cross-bridge-cycle`, `neuromuscular-junction` |
| Explaining twitch, summation and tetanus | `twitch-and-summation` | uni-lower | `excitation-contraction-coupling` |
| Explaining the length-tension relationship | `length-tension-relationship` | uni-lower | `cross-bridge-cycle` |
| Explaining muscle energy sources and fatigue | `muscle-energy-and-fatigue` | uni-lower | `twitch-and-summation`, `hs2.atp-yield-accounting` |
| Comparing slow and fast muscle fibres | `muscle-fibre-types` | uni-lower | `muscle-energy-and-fatigue` |
| Comparing smooth and cardiac muscle contraction | `smooth-and-cardiac-contraction` | uni-lower | `excitation-contraction-coupling` |
| Analyzing lever systems in the body | `body-levers` | uni-lower | `synovial-joint-movements`, `hs1.torque` |
| Identifying major skeletal muscles and their actions | `major-skeletal-muscles` | uni-lower | `synovial-joint-movements`, `skeletal-muscle-structure` |

### Nervous system

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing CNS and PNS organization | `nervous-system-organization` | uni-lower | `nervous-tissue` |
| Explaining the resting membrane potential of neurons | `resting-membrane-potential` | uni-lower | `intro1.membrane-potential-intro`, `nervous-tissue` |
| Explaining graded and action potentials | `graded-and-action-potentials` | uni-lower | `resting-membrane-potential` |
| Explaining propagation and myelination | `action-potential-propagation` | uni-lower | `graded-and-action-potentials` |
| Describing chemical synaptic transmission | `synaptic-transmission` | uni-lower | `action-potential-propagation` |
| Classifying neurotransmitters | `neurotransmitters` | uni-lower | `synaptic-transmission` |
| Explaining summation and neural circuits | `neural-integration` | uni-lower | `synaptic-transmission` |
| Identifying brain regions and functions | `brain-regions` | uni-lower | `nervous-system-organization` |
| Describing the spinal cord and reflexes | `spinal-cord-and-reflexes` | uni-lower | `nervous-system-organization`, `neural-integration` |
| Identifying cranial and spinal nerves | `cranial-and-spinal-nerves` | uni-lower | `spinal-cord-and-reflexes` |
| Comparing sympathetic and parasympathetic divisions | `autonomic-nervous-system` | uni-lower | `nervous-system-organization`, `neurotransmitters` |
| Tracing sensory pathways | `sensory-pathways` | uni-lower | `spinal-cord-and-reflexes`, `brain-regions` |
| Tracing motor pathways | `motor-pathways` | uni-lower | `sensory-pathways` |
| Describing memory, language and sleep | `higher-brain-functions` | uni-lower | `brain-regions` |
| Describing meninges and cerebrospinal fluid | `meninges-and-csf` | uni-lower | `brain-regions` |

### Special senses

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing eye anatomy | `eye-anatomy` | uni-lower | `sensory-pathways` |
| Explaining phototransduction | `phototransduction` | uni-lower | `eye-anatomy`, `intro1.kinase-cascades` |
| Explaining hearing and equilibrium | `hearing-and-balance` | uni-lower | `sensory-pathways`, `hs1.sound-speed-factors` |
| Explaining taste and smell | `taste-and-smell` | uni-lower | `sensory-pathways` |
| Describing touch, pain and temperature receptors | `general-senses` | uni-lower | `sensory-pathways` |

### Endocrine system

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing steroid and peptide hormone action | `hormone-mechanisms` | uni-lower | `intro1.receptor-types`, `hs2.endocrine-system` |
| Explaining hypothalamic-pituitary control | `hypothalamus-pituitary-axis` | uni-lower | `hormone-mechanisms` |
| Describing thyroid and parathyroid hormones | `thyroid-and-parathyroid` | uni-lower | `hypothalamus-pituitary-axis`, `bone-remodelling` |
| Describing adrenal hormones and the stress response | `adrenal-hormones-and-stress` | uni-lower | `hypothalamus-pituitary-axis` |
| Explaining blood glucose regulation | `blood-glucose-regulation` | uni-lower | `hormone-mechanisms`, `homeostatic-control-systems` |
| Describing endocrine disorders | `endocrine-disorders` | uni-lower | `blood-glucose-regulation`, `thyroid-and-parathyroid` |
| Describing pineal, gonadal and other hormones | `other-endocrine-glands` | uni-lower | `hypothalamus-pituitary-axis` |

## bio.anat-phys2: 57 topics

### Blood

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing plasma and formed elements | `plasma-and-formed-elements` | uni-lower | `anat-phys1.connective-tissue`, `hs2.blood-composition` |
| Explaining red blood cells and hemoglobin | `erythrocytes-and-hemoglobin` | uni-lower | `plasma-and-formed-elements` |
| Explaining hemostasis and clotting | `hemostasis` | uni-lower | `plasma-and-formed-elements` |
| Explaining blood typing and transfusion | `blood-typing-and-transfusion` | uni-lower | `erythrocytes-and-hemoglobin`, `hs1.blood-type-crosses` |
| Classifying white blood cells | `leukocytes` | uni-lower | `plasma-and-formed-elements` |

### Heart

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing heart chambers and valves | `heart-anatomy` | uni-lower | `hs2.circulatory-system`, `anat-phys1.body-cavities-and-regions` |
| Explaining the cardiac conduction system | `cardiac-conduction` | uni-lower | `heart-anatomy`, `anat-phys1.smooth-and-cardiac-contraction` |
| Reading an electrocardiogram | `electrocardiograms` | uni-lower | `cardiac-conduction` |
| Explaining the cardiac cycle and heart sounds | `cardiac-cycle` | uni-lower | `cardiac-conduction` |
| Calculating cardiac output | `cardiac-output` | uni-lower | `cardiac-cycle` |
| Explaining regulation of heart rate and stroke volume | `heart-rate-and-stroke-volume` | uni-lower | `cardiac-output`, `anat-phys1.autonomic-nervous-system` |

### Blood vessels

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing arteries, veins and capillaries | `vessel-structure` | uni-lower | `heart-anatomy` |
| Relating blood pressure, flow and resistance | `pressure-flow-resistance` | uni-lower | `vessel-structure`, `hs1.pressure-in-fluids` |
| Explaining capillary exchange forces | `capillary-exchange` | uni-lower | `pressure-flow-resistance`, `hs1.diffusion-and-osmosis` |
| Explaining short- and long-term blood pressure regulation | `blood-pressure-regulation` | uni-lower | `pressure-flow-resistance`, `heart-rate-and-stroke-volume` |
| Tracing systemic and pulmonary circuits | `circulatory-routes` | uni-lower | `vessel-structure` |
| Describing cardiovascular disorders | `cardiovascular-disorders` | uni-lower | `blood-pressure-regulation` |

### Lymphatic and immune systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing lymph formation and lymphoid organs | `lymphatic-system` | uni-lower | `capillary-exchange` |
| Explaining inflammation and fever | `inflammation-and-fever` | uni-lower | `lymphatic-system`, `hs2.immune-system` |
| Tracing humoral and cell-mediated responses | `humoral-and-cell-mediated-responses` | uni-lower | `inflammation-and-fever` |
| Describing allergies, autoimmunity and immunodeficiency | `immune-disorders` | uni-lower | `humoral-and-cell-mediated-responses` |

### Respiratory system

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing respiratory anatomy | `respiratory-anatomy` | uni-lower | `hs2.respiratory-system` |
| Explaining ventilation with pressure changes | `pulmonary-ventilation` | uni-lower | `respiratory-anatomy`, `hs1.gas-law-relationships` |
| Interpreting lung volumes and capacities | `lung-volumes` | uni-lower | `pulmonary-ventilation` |
| Explaining gas exchange with partial pressures | `gas-exchange-and-partial-pressures` | uni-lower | `pulmonary-ventilation`, `hs1.partial-pressures` |
| Interpreting the oxygen-hemoglobin dissociation curve | `oxygen-dissociation-curve` | uni-lower | `gas-exchange-and-partial-pressures`, `erythrocytes-and-hemoglobin` |
| Explaining carbon dioxide transport | `carbon-dioxide-transport` | uni-lower | `gas-exchange-and-partial-pressures` |
| Explaining neural and chemical control of breathing | `control-of-breathing` | uni-lower | `carbon-dioxide-transport`, `anat-phys1.brain-regions` |
| Describing respiratory disorders | `respiratory-disorders` | uni-lower | `lung-volumes` |

### Digestive system

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing digestive tract layers and organs | `digestive-tract-anatomy` | uni-lower | `hs2.digestive-system`, `anat-phys1.body-membranes` |
| Explaining digestion in the mouth and stomach | `mouth-and-stomach` | uni-lower | `digestive-tract-anatomy` |
| Explaining roles of the liver, pancreas and gallbladder | `liver-pancreas-gallbladder` | uni-lower | `mouth-and-stomach` |
| Tracing digestion and absorption of nutrients | `nutrient-absorption` | uni-lower | `liver-pancreas-gallbladder` |
| Describing large intestine functions | `large-intestine` | uni-lower | `nutrient-absorption` |
| Explaining neural and hormonal control of digestion | `digestive-regulation` | uni-lower | `liver-pancreas-gallbladder`, `anat-phys1.hormone-mechanisms` |

### Nutrition and metabolism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing absorptive and postabsorptive states | `absorptive-and-fasting-states` | uni-lower | `nutrient-absorption`, `anat-phys1.blood-glucose-regulation` |
| Describing metabolic functions of the liver | `liver-metabolic-roles` | uni-lower | `absorptive-and-fasting-states` |
| Calculating energy balance and metabolic rate | `energy-balance` | uni-lower | `absorptive-and-fasting-states` |
| Describing roles of vitamins and minerals | `vitamins-and-minerals` | uni-lower | `nutrient-absorption` |

### Urinary system

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing kidney and nephron structure | `nephron-structure` | uni-lower | `hs2.excretory-system` |
| Explaining glomerular filtration rate | `glomerular-filtration` | uni-lower | `nephron-structure`, `pressure-flow-resistance` |
| Explaining tubular reabsorption and secretion | `reabsorption-and-secretion` | uni-lower | `glomerular-filtration` |
| Explaining countercurrent concentration of urine | `urine-concentration` | uni-lower | `reabsorption-and-secretion` |
| Calculating renal clearance | `renal-clearance` | uni-lower | `glomerular-filtration` |
| Describing urine storage and micturition | `micturition` | uni-lower | `nephron-structure` |

### Fluid, electrolyte and acid-base balance

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing body fluid compartments | `fluid-compartments` | uni-lower | `capillary-exchange` |
| Explaining sodium and potassium balance | `electrolyte-balance` | uni-lower | `fluid-compartments`, `urine-concentration` |
| Explaining ADH, aldosterone and natriuretic peptide | `fluid-balance-hormones` | uni-lower | `electrolyte-balance`, `anat-phys1.adrenal-hormones-and-stress` |
| Explaining blood buffer systems | `blood-buffer-systems` | uni-lower | `carbon-dioxide-transport`, `ms.ph-scale-intro` |
| Explaining respiratory and renal compensation | `acid-base-compensation` | uni-lower | `blood-buffer-systems`, `reabsorption-and-secretion` |
| Interpreting acid-base disorders | `acid-base-disorders` | uni-lower | `acid-base-compensation` |

### Reproduction and development

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing male reproductive physiology | `male-reproductive-physiology` | uni-lower | `hs2.reproductive-system`, `anat-phys1.hypothalamus-pituitary-axis` |
| Describing ovarian and uterine cycles | `ovarian-and-uterine-cycles` | uni-lower | `hs2.reproductive-system`, `anat-phys1.hypothalamus-pituitary-axis` |
| Describing fertilization and implantation | `fertilization-and-implantation` | uni-lower | `ovarian-and-uterine-cycles` |
| Describing placental function and pregnancy hormones | `pregnancy-and-placenta` | uni-lower | `fertilization-and-implantation` |
| Describing stages of fetal development | `fetal-development` | uni-lower | `pregnancy-and-placenta` |
| Explaining labour and lactation | `labour-and-lactation` | uni-lower | `pregnancy-and-placenta` |

## bio.neuro: 42 topics

### Cellular neurophysiology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using membrane capacitance and resistance | `passive-membrane-properties` | uni-upper | `anat-phys1.resting-membrane-potential` |
| Explaining length and time constants | `cable-properties` | uni-upper | `passive-membrane-properties` |
| Explaining voltage-gated channel gating | `voltage-gated-channels` | uni-upper | `anat-phys1.graded-and-action-potentials`, `cell-mol.goldman-equation` |
| Describing the Hodgkin-Huxley model | `hodgkin-huxley-model` | uni-upper | `voltage-gated-channels`, `cable-properties` |
| Interpreting voltage-clamp and patch-clamp data | `voltage-and-patch-clamp` | uni-upper | `voltage-gated-channels` |
| Explaining refractory periods and firing patterns | `firing-patterns` | uni-upper | `hodgkin-huxley-model` |
| Comparing ion channel families | `ion-channel-families` | uni-upper | `voltage-gated-channels` |

### Synapses

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining calcium-triggered vesicle release | `vesicle-release-mechanisms` | uni-upper | `anat-phys1.synaptic-transmission`, `cell-mol.vesicle-coats-and-fusion` |
| Analyzing quantal release | `quantal-analysis` | uni-upper | `vesicle-release-mechanisms` |
| Explaining ionotropic receptor function | `ionotropic-receptors` | uni-upper | `anat-phys1.neurotransmitters` |
| Explaining metabotropic receptor signalling | `metabotropic-receptors` | uni-upper | `ionotropic-receptors`, `cell-mol.gpcr-signalling` |
| Calculating synaptic potentials and their integration | `synaptic-integration` | uni-upper | `ionotropic-receptors`, `anat-phys1.neural-integration` |
| Describing dopamine, serotonin and other neuromodulatory systems | `neuromodulatory-systems` | uni-upper | `metabotropic-receptors` |
| Explaining long-term potentiation and depression | `synaptic-plasticity` | uni-upper | `synaptic-integration` |
| Describing electrical synapses | `electrical-synapses` | uni-upper | `ionotropic-receptors` |
| Explaining drug actions at synapses | `neuropharmacology` | uni-upper | `neuromodulatory-systems` |

### Sensory systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining sensory transduction and coding | `sensory-coding` | uni-upper | `anat-phys1.general-senses` |
| Explaining retinal processing | `retinal-processing` | uni-upper | `anat-phys1.phototransduction` |
| Explaining receptive fields in visual cortex | `visual-cortex` | uni-upper | `retinal-processing` |
| Explaining cochlear tuning and auditory pathways | `auditory-processing` | uni-upper | `anat-phys1.hearing-and-balance` |
| Explaining somatotopic maps | `somatosensory-maps` | uni-upper | `anat-phys1.sensory-pathways` |
| Explaining pain pathways and modulation | `pain-modulation` | uni-upper | `somatosensory-maps` |
| Explaining coding of taste and smell | `chemosensory-coding` | uni-upper | `anat-phys1.taste-and-smell` |

### Motor systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining motor units and spinal circuits | `spinal-motor-circuits` | uni-upper | `anat-phys1.spinal-cord-and-reflexes` |
| Describing central pattern generators | `central-pattern-generators` | uni-upper | `spinal-motor-circuits` |
| Explaining motor cortex and movement planning | `motor-cortex` | uni-upper | `anat-phys1.motor-pathways` |
| Explaining basal ganglia function | `basal-ganglia` | uni-upper | `motor-cortex`, `neuromodulatory-systems` |
| Explaining cerebellar function | `cerebellum` | uni-upper | `motor-cortex` |
| Explaining Parkinson's disease and other movement disorders | `movement-disorders` | uni-upper | `basal-ganglia` |

### Neural development

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining neural induction and patterning | `neural-induction` | uni-upper | `cell-mol.developmental-signalling-pathways` |
| Describing neurogenesis and neuronal migration | `neurogenesis-and-migration` | uni-upper | `neural-induction` |
| Explaining axon guidance | `axon-guidance` | uni-upper | `neurogenesis-and-migration`, `cell-mol.cell-migration` |
| Explaining synapse formation and pruning | `synapse-formation-and-pruning` | uni-upper | `axon-guidance`, `synaptic-plasticity` |
| Explaining critical periods | `critical-periods` | uni-upper | `synapse-formation-and-pruning` |

### Systems and cognition

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining hypothalamic control of behaviour | `motivation-and-the-hypothalamus` | uni-upper | `anat-phys1.hypothalamus-pituitary-axis` |
| Explaining sleep and circadian rhythms | `sleep-and-circadian-rhythms` | uni-upper | `motivation-and-the-hypothalamus` |
| Explaining memory systems and the hippocampus | `memory-systems` | uni-upper | `synaptic-plasticity`, `anat-phys1.higher-brain-functions` |
| Explaining emotion circuits and the amygdala | `emotion-circuits` | uni-upper | `motivation-and-the-hypothalamus` |
| Explaining language areas and lateralization | `language-and-lateralization` | uni-upper | `anat-phys1.higher-brain-functions` |
| Explaining neurodegenerative diseases | `neurodegeneration` | uni-upper | `memory-systems`, `cell-mol.ubiquitin-proteasome` |

### Methods

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing EEG, MRI and PET | `neuroimaging` | uni-upper | `anat-phys1.brain-regions` |
| Describing electrophysiology and optogenetics | `recording-and-optogenetics` | uni-upper | `voltage-and-patch-clamp`, `cell-mol.fluorescent-protein-tagging` |
