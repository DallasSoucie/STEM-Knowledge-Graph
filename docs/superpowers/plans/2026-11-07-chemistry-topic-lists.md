# Topic lists: chemistry

Draft for approval. Covers all 12 chemistry courses. In the Needs column, a plain name is in the same course. A prefix names a course: chemistry first (`hs1.`, `gen2.` and so on), then physics where no chemistry topic has that name (`ms.density` is physics), then math (`alg2.`, `stats.`).

## Decisions already made

- Shared high-school basics move from physics into chemistry, and `physics.hs2` follows `chem.hs1`.
- Physical chemistry builds on physics: `pchem1` follows `physics.waves-thermo-optics` and `pchem2` follows `physics.modern`.

## Proposed changes that follow from those decisions

**Moves (rename-id, so every physics reference follows automatically).** Each moved topic keeps its name and knowledge points. Its prerequisites are rewired so they stay reachable from its new course.

| From | To | Topics |
|---|---|---|
| `physics.hs2` | `chem.hs1` | specific-heat, calorimetry, latent-heat, heating-curves, calorimetry-with-phase-change, photon-energy, energy-level-diagrams, emission-and-absorption, hydrogen-spectrum, nuclear-notation, alpha-beta-gamma, decay-equations, half-life, gas-law-relationships |
| `physics.waves-thermo-optics` | `chem.gen1` | real-gases, phase-diagrams, enthalpy |

The last three move because first-year general chemistry comes before second-year waves and thermodynamics, so `physics.waves-thermo-optics` gains `chem.gen1` in `follows`.

Knock-on edits in physics:
- `physics.hs2.bohr-model` stays in physics (it needs force balance and electron volts) and gains the new `chem.hs1.electron-energy-levels` as a prerequisite.
- `physics.hs2.ideal-gas-law` is renamed "Using the ideal gas law with particle counts" and gains `chem.hs1.ideal-gas-law-with-moles` as a prerequisite.
- In `half-life`, the knowledge point "Find a time from a remainder" needs logarithms, which `chem.hs1` cannot reach. It becomes "Find elapsed time from a number of half-lives"; solving for time with logs stays in `physics.hs2.decay-curves`.

**`follows` for chemistry:**

| Course | Follows |
|---|---|
| chem.elem | physics.elem |
| chem.ms | chem.elem, physics.ms |
| chem.hs1 | chem.ms, physics.hs1, math.alg1 |
| chem.hs2 | chem.hs1, math.alg2 |
| chem.gen1 | chem.hs2, physics.hs2 |
| chem.gen2 | chem.gen1 |
| chem.org1 | chem.gen2 |
| chem.org2 | chem.org1 |
| chem.analytical | chem.gen2, math.stats |
| chem.inorganic | chem.gen2, chem.org1, math.linalg |
| chem.pchem1 | chem.gen2, math.calc2, physics.mechanics, physics.waves-thermo-optics, physics.stat-thermal, math.diffeq, chem.analytical |
| chem.pchem2 | chem.pchem1, math.linalg, physics.modern, physics.quantum, chem.org2 |

Beyond the approved two, these add: `physics.hs1` before `chem.hs1` (significant figures and uncertainty live there); `physics.hs2` before `gen1` (Coulomb's law, the first law, de Broglie); `stat-thermal` before `pchem1` (free energies and chemical potential live there); `quantum` before `pchem2` (perturbation theory, angular momentum and the hydrogen molecule ion live there); and organic before `inorganic` and `pchem2`.

## Budgets

Every course came in under budget. The high-school courses absorbed much of what a general chemistry course repeats, so `gen1` and `gen2` are lean by design.

| Course | Topics | Budget now | Proposed |
|---|---|---|---|
| elem | 24 | 30 | 25 |
| ms | 51 | 70 | 55 |
| hs1 | 123 (14 moved in) | 180 | 125 |
| hs2 | 84 | 180 | 90 |
| gen1 | 50 (3 moved in) | 190 | 55 |
| gen2 | 50 | 190 | 55 |
| org1 | 98 | 190 | 100 |
| org2 | 78 | 190 | 80 |
| analytical | 52 | 140 | 55 |
| inorganic | 49 | 150 | 50 |
| pchem1 | 47 | 170 | 50 |
| pchem2 | 49 | 170 | 50 |
| **Total** | **755** | **1,850** | **790** |

Physics loses 17 topics: `physics.hs2` drops from 166 to 152, so its budget of 200 should become 165 to stay inside the 20% warning band, and `waves-thermo-optics` drops from 112 to 109 (budget 115, fine). Chemistry would total 790, physics 1,335, and the full graph about 14,285.

## Survey

Standards in refs: NGSS DCI (PS1), BC Science K-9 and Chemistry 11 and 12, AP Chemistry with clarifications, ACS guidelines, MCAT outline. University sources are indexed in `refs/uni_syllabi/SOURCES.md` under the `chem-*` folders (24 of 35 downloads saved), anchored by MIT 5.111, 5.60 and 5.61, CUNY Kingsborough organic I and II, Pitt, York, Hawaii and Normandale analytical, Minnesota Duluth, Pitt and Carleton inorganic, and Kansas, UNT, Point Loma and Belgrade physical chemistry. Course order follows the common pattern: atom and bonding, then gases and solutions, then thermochemistry in gen1; kinetics, equilibrium, acid-base, thermodynamics and electrochemistry in gen2; statistics first in analytical; symmetry before coordination chemistry in inorganic.

## Scope notes

- Biochemistry stays in `bio.biochem`; `org2` covers only the organic chemistry of carbohydrates, amino acids, lipids and nucleotides.
- Group theory is homed in `inorganic`; `pchem2` counts normal modes without it.
- Band theory stays in `physics.modern`; no chemistry course repeats it.
- Left out: polymer chemistry beyond mechanisms, environmental chemistry, medicinal chemistry, nuclear chemistry beyond high school, and advanced synthesis.

## chem.elem: 24 topics

### Materials and their properties

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Sorting objects by colour, shape and texture | `sorting-objects-by-property` | gk |  |
| Naming the materials objects are made of | `materials-objects-are-made-of` | g1 | `sorting-objects-by-property` |
| Testing hardness, flexibility and absorbency | `testing-material-properties` | g2 | `materials-objects-are-made-of` |
| Choosing materials for a purpose | `choosing-materials-for-a-purpose` | g2 | `testing-material-properties` |
| Building objects from smaller pieces | `building-from-small-pieces` | g2 | `materials-objects-are-made-of` |
| Telling solids from liquids | `solids-and-liquids` | g2 | `testing-material-properties` |
| Observing changes from heating and cooling | `heating-and-cooling-changes` | g2 | `solids-and-liquids`, `elem.sources-of-heat` |
| Telling reversible from irreversible changes | `reversible-and-irreversible-changes` | g2 | `heating-and-cooling-changes` |

### States of matter

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Showing that air is matter | `gases-as-matter` | g3 | `solids-and-liquids` |
| Describing solids, liquids and gases | `states-of-matter` | g3 | `gases-as-matter` |
| Describing melting, freezing and boiling | `melting-freezing-boiling` | g3 | `states-of-matter`, `heating-and-cooling-changes` |
| Describing evaporation and condensation | `evaporation-and-condensation` | g4 | `melting-freezing-boiling` |
| Describing cooking, rusting and burning as changes | `everyday-chemical-changes` | g4 | `reversible-and-irreversible-changes` |

### Particles, mixtures and changes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining matter as made of tiny particles | `matter-made-of-particles` | g5 | `states-of-matter` |
| Measuring mass and volume of materials | `measuring-mass-and-volume-of-matter` | g5 | `states-of-matter`, `g4.relative-metric-mass-capacity` |
| Showing mass is conserved in changes | `conservation-of-mass-in-changes` | g5 | `measuring-mass-and-volume-of-matter`, `reversible-and-irreversible-changes` |
| Identifying materials by measured properties | `identifying-materials-by-properties` | g5 | `measuring-mass-and-volume-of-matter`, `testing-material-properties` |
| Making simple mixtures | `making-mixtures` | g5 | `identifying-materials-by-properties` |
| Separating mixtures by sieving, filtering and evaporating | `separating-mixtures` | g5 | `making-mixtures`, `evaporation-and-condensation` |
| Observing dissolving in water | `dissolving` | g5 | `making-mixtures`, `matter-made-of-particles` |
| Testing what speeds up dissolving | `factors-affecting-dissolving` | g5 | `dissolving` |
| Recognizing when mixing makes a new substance | `mixing-to-make-new-substances` | g5 | `conservation-of-mass-in-changes`, `dissolving` |
| Identifying signs of a chemical change | `signs-of-chemical-change` | g5 | `mixing-to-make-new-substances`, `everyday-chemical-changes` |
| Telling physical from chemical changes | `physical-vs-chemical-change` | g5 | `signs-of-chemical-change`, `separating-mixtures` |

## chem.ms: 51 topics

### Particle model

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining states of matter with particle motion | `particle-model-of-states` | g6 | `elem.matter-made-of-particles`, `elem.states-of-matter` |
| Linking particle motion to temperature | `particle-motion-and-temperature` | g7 | `particle-model-of-states`, `ms.temperature-scales` |
| Explaining phase changes with particles | `phase-changes-and-particles` | g7 | `particle-motion-and-temperature`, `elem.melting-freezing-boiling` |
| Reading the shape of a heating curve | `heating-curve-shape` | g8 | `phase-changes-and-particles`, `ms.heat-vs-temperature` |
| Explaining gas pressure with particle collisions | `gas-pressure-particles` | g7 | `particle-model-of-states` |
| Predicting how gases respond to heating and squeezing | `gas-behaviour-qualitative` | g8 | `gas-pressure-particles`, `particle-motion-and-temperature` |
| Explaining expansion with particle spacing | `thermal-expansion-particles` | g7 | `particle-motion-and-temperature` |

### Properties of substances

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using physical properties to identify substances | `physical-properties` | g6 | `elem.identifying-materials-by-properties` |
| Using melting and boiling points to identify substances | `melting-and-boiling-points` | g7 | `physical-properties`, `phase-changes-and-particles` |
| Identifying substances by density | `density-to-identify-substances` | g7 | `physical-properties`, `ms.density` |
| Telling intensive from extensive properties | `intensive-and-extensive-properties` | g7 | `density-to-identify-substances` |

### Pure substances and mixtures

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying matter as pure substances or mixtures | `pure-substances-and-mixtures` | g6 | `elem.making-mixtures`, `physical-properties` |
| Telling homogeneous from heterogeneous mixtures | `homogeneous-and-heterogeneous` | g6 | `pure-substances-and-mixtures` |
| Describing solutions with solute and solvent | `solutions-solute-solvent` | g7 | `homogeneous-and-heterogeneous`, `elem.dissolving` |
| Describing solubility and saturated solutions | `solubility-and-saturation` | g7 | `solutions-solute-solvent`, `elem.factors-affecting-dissolving` |
| Comparing concentrations of solutions | `concentration-intro` | g7 | `solutions-solute-solvent`, `g6.unit-rates` |
| Reading solubility curves | `solubility-curves` | g8 | `solubility-and-saturation`, `particle-motion-and-temperature` |
| Choosing separation techniques by property | `separation-techniques` | g7 | `homogeneous-and-heterogeneous`, `elem.separating-mixtures` |
| Separating mixtures by paper chromatography | `paper-chromatography` | g7 | `separation-techniques` |
| Separating liquids by distillation | `simple-distillation` | g8 | `separation-techniques`, `melting-and-boiling-points` |

### Atoms and elements

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing atoms as building blocks of matter | `atoms-as-building-blocks` | g7 | `particle-model-of-states` |
| Telling elements from compounds | `elements-and-compounds` | g7 | `atoms-as-building-blocks`, `pure-substances-and-mixtures` |
| Modelling molecules and extended structures | `molecules-and-extended-structures` | g8 | `elements-and-compounds` |
| Reading chemical symbols and simple formulas | `chemical-symbols-and-formulas` | g7 | `elements-and-compounds` |
| Counting atoms in chemical formulas | `counting-atoms-in-formulas` | g8 | `chemical-symbols-and-formulas` |
| Comparing early models of the atom | `early-atomic-models` | g8 | `atoms-as-building-blocks` |
| Describing protons, neutrons and electrons | `subatomic-particles` | g8 | `early-atomic-models`, `ms.electric-charge` |
| Using atomic number and mass number | `atomic-number-and-mass-number` | g8 | `subatomic-particles` |
| Describing isotopes | `isotopes-intro` | g8 | `atomic-number-and-mass-number` |
| Drawing Bohr diagrams of light atoms | `bohr-diagrams` | g8 | `atomic-number-and-mass-number` |

### Periodic table

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading groups and periods on the periodic table | `periodic-table-layout` | g8 | `atomic-number-and-mass-number` |
| Classifying elements as metals, nonmetals and metalloids | `metals-nonmetals-metalloids` | g8 | `periodic-table-layout`, `physical-properties` |
| Describing alkali metals, halogens and noble gases | `element-families` | g8 | `periodic-table-layout` |
| Linking valence electrons to groups | `valence-electrons-and-groups` | g8 | `bohr-diagrams`, `periodic-table-layout` |

### Compounds

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Forming ions by gaining or losing electrons | `ions-from-atoms` | g8 | `valence-electrons-and-groups` |
| Describing ionic compounds | `ionic-compounds-intro` | g8 | `ions-from-atoms`, `molecules-and-extended-structures` |
| Describing covalent molecules | `covalent-molecules-intro` | g8 | `valence-electrons-and-groups`, `molecules-and-extended-structures` |
| Naming simple binary compounds | `naming-binary-compounds` | g8 | `ionic-compounds-intro`, `covalent-molecules-intro` |

### Chemical reactions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing reactions as rearranging atoms | `reactions-rearrange-atoms` | g7 | `elements-and-compounds`, `elem.physical-vs-chemical-change` |
| Using properties to show a reaction occurred | `evidence-of-reactions` | g7 | `reactions-rearrange-atoms`, `physical-properties` |
| Writing word equations for reactions | `word-equations` | g7 | `reactions-rearrange-atoms` |
| Explaining conservation of mass with atoms | `conservation-of-mass-atoms` | g8 | `counting-atoms-in-formulas`, `elem.conservation-of-mass-in-changes` |
| Balancing simple chemical equations | `balancing-simple-equations` | g8 | `conservation-of-mass-atoms`, `word-equations` |
| Classifying reactions as releasing or absorbing heat | `exothermic-and-endothermic-intro` | g8 | `evidence-of-reactions`, `ms.energy-transformations` |
| Designing a device that releases or absorbs heat | `heat-and-cold-packs` | g8 | `exothermic-and-endothermic-intro` |
| Testing factors that change reaction speed | `reaction-speed-factors` | g8 | `evidence-of-reactions`, `particle-motion-and-temperature` |
| Describing properties of acids and bases | `acids-and-bases-intro` | g7 | `evidence-of-reactions` |
| Using the pH scale and indicators | `ph-scale-intro` | g7 | `acids-and-bases-intro` |
| Describing neutralization | `neutralization-intro` | g8 | `ph-scale-intro`, `word-equations` |
| Describing combustion reactions | `combustion-intro` | g8 | `word-equations`, `exothermic-and-endothermic-intro` |
| Describing synthetic materials made from natural resources | `synthetic-materials` | g8 | `reactions-rearrange-atoms` |

## chem.hs1: 123 topics

### Measurement and calculations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Converting units with conversion factors | `dimensional-analysis` | g9 | `g6.convert-with-ratios`, `hs1.si-units-and-prefixes` |
| Converting units in several steps | `multistep-dimensional-analysis` | g9 | `dimensional-analysis` |
| Converting area and volume units | `converting-area-and-volume-units` | g9 | `dimensional-analysis` |
| Calculating with scientific notation and significant figures | `scientific-notation-with-figures` | g9 | `hs1.significant-figures`, `g8.scientific-notation-write` |
| Calculating density, mass and volume | `density-calculations` | g9 | `dimensional-analysis`, `ms.density-to-identify-substances` |
| Finding percent error of lab results | `percent-error-in-lab` | g9 | `hs1.measurement-uncertainty`, `g7.percent-error` |

### Atomic structure

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Tracing evidence for atomic models | `evidence-for-atomic-models` | g9 | `ms.early-atomic-models` |
| Explaining the gold foil experiment | `gold-foil-experiment` | g9 | `evidence-for-atomic-models` |
| Finding average atomic mass from isotopes | `isotopes-and-atomic-mass` | g10 | `ms.isotopes-intro`, `g7.percent-equation` |
| Reading mass spectra of elements | `mass-spectra-of-elements` | g11 | `isotopes-and-atomic-mass` |
| Calculating photon energy (moved from `physics.hs2.photon-energy`) | `photon-energy` | g11 | `ms.electromagnetic-spectrum`, `ms.light-wave-and-particle`, `hs1.wave-equation-problems` |
| Describing electrons in Bohr energy levels | `electron-energy-levels` | g10 | `ms.bohr-diagrams`, `gold-foil-experiment` |
| Reading energy level diagrams (moved from `physics.hs2.energy-level-diagrams`) | `energy-level-diagrams` | g10 | `electron-energy-levels` |
| Explaining emission and absorption spectra (moved from `physics.hs2.emission-and-absorption`) | `emission-and-absorption` | g11 | `energy-level-diagrams`, `photon-energy` |
| Finding hydrogen spectral lines (moved from `physics.hs2.hydrogen-spectrum`) | `hydrogen-spectrum` | g11 | `emission-and-absorption` |
| Identifying elements by flame colour | `flame-tests` | g11 | `emission-and-absorption` |
| Describing orbitals in the quantum model | `quantum-model-orbitals` | g10 | `electron-energy-levels` |
| Using quantum numbers to label electrons | `quantum-numbers` | g11 | `quantum-model-orbitals` |
| Writing electron configurations | `electron-configurations` | g10 | `quantum-model-orbitals`, `ms.periodic-table-layout` |
| Drawing orbital diagrams | `orbital-diagrams` | g10 | `electron-configurations` |
| Writing noble gas shorthand configurations | `noble-gas-configurations` | g10 | `electron-configurations` |
| Writing configurations of ions | `configurations-of-ions` | g10 | `noble-gas-configurations`, `ms.ions-from-atoms` |
| Explaining configuration exceptions like chromium and copper | `configuration-exceptions` | g11 | `orbital-diagrams` |

### Periodic trends

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Linking periodic table blocks to configurations | `periodic-table-blocks` | g10 | `electron-configurations` |
| Estimating effective nuclear charge | `effective-nuclear-charge` | g10 | `periodic-table-blocks` |
| Explaining trends in atomic radius | `atomic-radius-trend` | g10 | `effective-nuclear-charge` |
| Explaining trends in ionization energy | `ionization-energy-trend` | g10 | `atomic-radius-trend` |
| Using successive ionization energies | `successive-ionization-energies` | g11 | `ionization-energy-trend`, `noble-gas-configurations` |
| Explaining trends in electronegativity | `electronegativity-trend` | g10 | `atomic-radius-trend` |
| Comparing ion and atom sizes | `ionic-radius-trend` | g10 | `atomic-radius-trend`, `configurations-of-ions` |
| Explaining trends in metallic character | `metallic-character-trend` | g10 | `ionization-energy-trend`, `ms.metals-nonmetals-metalloids` |

### Nuclear chemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading nuclear notation (moved from `physics.hs2.nuclear-notation`) | `nuclear-notation` | g10 | `isotopes-and-atomic-mass` |
| Comparing alpha, beta and gamma radiation (moved from `physics.hs2.alpha-beta-gamma`) | `alpha-beta-gamma` | g10 | `nuclear-notation` |
| Balancing nuclear decay equations (moved from `physics.hs2.decay-equations`) | `decay-equations` | g10 | `alpha-beta-gamma` |
| Calculating with half-life (moved from `physics.hs2.half-life`) | `half-life` | g10 | `decay-equations`, `alg1.graph-exponential-decay` |
| Predicting decay type from the band of stability | `band-of-stability` | g11 | `decay-equations` |
| Describing uses of radioisotopes | `radioisotope-uses` | g10 | `half-life` |

### Chemical bonding

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying bonds from electronegativity difference | `bond-type-from-electronegativity` | g10 | `electronegativity-trend`, `ms.ionic-compounds-intro`, `ms.covalent-molecules-intro` |
| Showing ionic bond formation with Lewis symbols | `ionic-bonding-with-lewis-symbols` | g10 | `configurations-of-ions`, `bond-type-from-electronegativity` |
| Explaining properties of ionic solids | `ionic-solid-properties` | g10 | `ionic-bonding-with-lewis-symbols` |
| Drawing Lewis structures of simple molecules | `lewis-structures-simple` | g10 | `ms.covalent-molecules-intro`, `ms.valence-electrons-and-groups` |
| Drawing Lewis structures with multiple bonds | `lewis-structures-multiple-bonds` | g10 | `lewis-structures-simple` |
| Drawing Lewis structures of polyatomic ions | `lewis-structures-polyatomic-ions` | g10 | `lewis-structures-multiple-bonds` |
| Drawing resonance structures | `resonance-structures` | g11 | `lewis-structures-polyatomic-ions` |
| Using formal charge to choose structures | `formal-charge` | g11 | `resonance-structures` |
| Drawing molecules that break the octet rule | `octet-exceptions` | g11 | `lewis-structures-multiple-bonds` |
| Predicting molecular shapes with VSEPR | `vsepr-shapes` | g10 | `lewis-structures-multiple-bonds` |
| Predicting bond angles from shape | `bond-angles` | g10 | `vsepr-shapes` |
| Finding bond polarity | `bond-polarity` | g10 | `bond-type-from-electronegativity` |
| Predicting molecular polarity | `molecular-polarity` | g10 | `vsepr-shapes`, `bond-polarity` |
| Explaining metallic bonding and properties | `metallic-bonding` | g10 | `bond-type-from-electronegativity`, `metallic-character-trend` |
| Explaining network covalent solids | `network-covalent-solids` | g10 | `lewis-structures-simple`, `ionic-solid-properties` |
| Identifying intermolecular forces | `intermolecular-forces` | g10 | `molecular-polarity` |
| Explaining hydrogen bonding | `hydrogen-bonding` | g10 | `intermolecular-forces` |
| Predicting boiling points from intermolecular forces | `forces-and-boiling-points` | g10 | `hydrogen-bonding`, `ms.melting-and-boiling-points` |
| Predicting solubility from polarity | `like-dissolves-like` | g10 | `intermolecular-forces`, `ms.solubility-and-saturation` |
| Comparing ionic, molecular, metallic and network solids | `comparing-solid-types` | g10 | `ionic-solid-properties`, `metallic-bonding`, `network-covalent-solids`, `forces-and-boiling-points` |

### Formulas and names

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing formulas of ionic compounds | `ionic-formulas-from-charges` | g10 | `ms.ionic-compounds-intro`, `configurations-of-ions` |
| Naming ionic compounds | `naming-ionic-compounds` | g10 | `ionic-formulas-from-charges`, `ms.naming-binary-compounds` |
| Using common polyatomic ions | `polyatomic-ions` | g10 | `naming-ionic-compounds` |
| Naming compounds with transition metals | `transition-metal-names` | g10 | `naming-ionic-compounds` |
| Naming molecular compounds with prefixes | `naming-molecular-compounds` | g10 | `ms.naming-binary-compounds` |
| Naming acids | `naming-acids` | g10 | `polyatomic-ions`, `naming-molecular-compounds` |
| Naming hydrates | `naming-hydrates` | g10 | `naming-ionic-compounds` |

### The mole

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining the mole and Avogadro's number | `mole-concept` | g10 | `scientific-notation-with-figures` |
| Finding molar mass | `molar-mass` | g10 | `mole-concept`, `ms.counting-atoms-in-formulas` |
| Converting between mass, moles and particles | `mass-mole-particle-conversions` | g10 | `molar-mass`, `multistep-dimensional-analysis` |
| Finding percent composition | `percent-composition` | g10 | `molar-mass`, `g7.percent-equation` |
| Finding empirical formulas | `empirical-formulas` | g10 | `percent-composition`, `mass-mole-particle-conversions` |
| Finding molecular formulas | `molecular-formulas` | g10 | `empirical-formulas` |
| Finding the formula of a hydrate | `hydrate-formulas` | g10 | `empirical-formulas`, `naming-hydrates` |

### Chemical reactions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Balancing chemical equations | `balancing-equations` | g10 | `ms.balancing-simple-equations`, `polyatomic-ions` |
| Writing states in chemical equations | `states-in-equations` | g10 | `balancing-equations` |
| Classifying synthesis and decomposition reactions | `synthesis-and-decomposition` | g10 | `balancing-equations` |
| Using solubility rules | `solubility-rules` | g10 | `naming-ionic-compounds`, `ms.solubility-and-saturation` |
| Predicting single replacement with an activity series | `single-replacement-activity` | g10 | `synthesis-and-decomposition`, `metallic-character-trend` |
| Predicting precipitates in double replacement | `double-replacement-precipitation` | g10 | `synthesis-and-decomposition`, `solubility-rules` |
| Writing combustion equations | `combustion-equations` | g10 | `balancing-equations`, `ms.combustion-intro` |
| Writing neutralization equations | `neutralization-equations` | g10 | `double-replacement-precipitation`, `naming-acids`, `ms.neutralization-intro` |
| Writing net ionic equations | `net-ionic-equations` | g10 | `double-replacement-precipitation`, `states-in-equations` |
| Predicting products of reaction types | `predicting-products` | g10 | `single-replacement-activity`, `double-replacement-precipitation`, `combustion-equations`, `neutralization-equations` |

### Stoichiometry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using mole ratios from equations | `mole-ratios` | g10 | `balancing-equations`, `mass-mole-particle-conversions` |
| Solving mass-to-mass stoichiometry | `mass-to-mass-stoichiometry` | g10 | `mole-ratios` |
| Finding the limiting reactant | `limiting-reactant` | g10 | `mass-to-mass-stoichiometry` |
| Finding excess reactant left over | `excess-reactant-remaining` | g10 | `limiting-reactant` |
| Finding theoretical and percent yield | `percent-yield` | g10 | `limiting-reactant`, `g7.percent-equation` |

### Solutions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating molarity | `molarity` | g10 | `mass-mole-particle-conversions`, `ms.concentration-intro` |
| Preparing a solution of given molarity | `preparing-solutions` | g10 | `molarity` |
| Calculating dilutions | `dilution` | g10 | `molarity` |
| Solving stoichiometry with solutions | `solution-stoichiometry` | g10 | `molarity`, `mass-to-mass-stoichiometry` |
| Using percent by mass and parts per million | `percent-and-ppm-concentration` | g10 | `molarity`, `g7.percent-equation` |
| Finding ion concentrations from dissociation | `ion-concentrations` | g10 | `molarity`, `solubility-rules` |
| Classifying electrolytes | `electrolytes` | g10 | `ion-concentrations` |
| Finding concentration by titration | `titration-intro` | g11 | `solution-stoichiometry`, `neutralization-equations` |

### Gases

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Converting between pressure units | `pressure-units` | g10 | `dimensional-analysis`, `hs1.pressure-in-fluids` |
| Stating the kinetic molecular theory | `kinetic-molecular-theory` | g10 | `ms.gas-pressure-particles`, `ms.particle-motion-and-temperature` |
| Solving gas problems with two states (moved from `physics.hs2.gas-law-relationships`) | `gas-law-relationships` | g10 | `pressure-units`, `kinetic-molecular-theory`, `ms.temperature-scales` |
| Using the combined gas law | `combined-gas-law` | g10 | `gas-law-relationships` |
| Relating gas volume to amount | `avogadros-law` | g10 | `gas-law-relationships`, `mole-concept` |
| Using molar volume at standard conditions | `molar-volume` | g10 | `avogadros-law` |
| Using the ideal gas law with moles | `ideal-gas-law-with-moles` | g10 | `combined-gas-law`, `avogadros-law` |
| Finding gas density and molar mass | `gas-density-and-molar-mass` | g11 | `ideal-gas-law-with-moles`, `molar-mass` |
| Solving stoichiometry with gases | `gas-stoichiometry` | g10 | `ideal-gas-law-with-moles`, `mass-to-mass-stoichiometry` |
| Using Dalton's law of partial pressures | `partial-pressures` | g10 | `ideal-gas-law-with-moles` |
| Correcting for water vapour pressure | `gas-collected-over-water` | g11 | `partial-pressures` |
| Comparing effusion rates with Graham's law | `grahams-law` | g11 | `kinetic-molecular-theory`, `molar-mass` |

### Thermochemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating with specific heat (moved from `physics.hs2.specific-heat`) | `specific-heat` | g11 | `ms.heat-capacity-factors`, `hs1.rearranging-physics-formulas` |
| Solving calorimetry problems (moved from `physics.hs2.calorimetry`) | `calorimetry` | g11 | `specific-heat`, `ms.thermal-equilibrium` |
| Calculating with latent heat (moved from `physics.hs2.latent-heat`) | `latent-heat` | g11 | `specific-heat` |
| Reading heating curves (moved from `physics.hs2.heating-curves`) | `heating-curves` | g11 | `latent-heat`, `calorimetry`, `ms.heating-curve-shape` |
| Solving calorimetry with a phase change (moved from `physics.hs2.calorimetry-with-phase-change`) | `calorimetry-with-phase-change` | g11 | `calorimetry`, `latent-heat` |
| Drawing energy diagrams for exothermic and endothermic reactions | `energy-diagrams-of-reactions` | g10 | `ms.exothermic-and-endothermic-intro` |
| Using enthalpy changes of reactions | `enthalpy-of-reaction` | g10 | `energy-diagrams-of-reactions` |
| Using thermochemical equations | `thermochemical-equations` | g10 | `enthalpy-of-reaction`, `mole-ratios` |
| Finding enthalpy of reaction by calorimetry | `reaction-calorimetry` | g11 | `calorimetry`, `thermochemical-equations` |

### Introductory organic chemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing carbon's bonding patterns | `carbon-bonding` | g10 | `lewis-structures-simple` |
| Naming simple alkanes | `naming-alkanes` | g10 | `carbon-bonding` |
| Naming simple alkenes and alkynes | `naming-alkenes-and-alkynes` | g10 | `naming-alkanes`, `lewis-structures-multiple-bonds` |
| Drawing condensed and skeletal formulas | `structural-formulas` | g10 | `naming-alkanes` |
| Recognizing structural isomers | `structural-isomers` | g10 | `structural-formulas` |
| Recognizing common functional groups | `functional-groups-intro` | g10 | `structural-formulas` |
| Describing polymers and monomers | `polymers-intro` | g10 | `functional-groups-intro`, `ms.synthetic-materials` |
| Applying green chemistry principles | `green-chemistry` | g10 | `percent-yield` |

## chem.hs2: 84 topics

### Thermochemistry and thermodynamics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Combining equations with Hess's law | `hess-law` | g11 | `hs1.thermochemical-equations` |
| Using enthalpies of formation | `enthalpy-of-formation` | g11 | `hess-law` |
| Estimating enthalpy change from bond enthalpies | `bond-enthalpies` | g11 | `hs1.enthalpy-of-reaction`, `hs1.lewis-structures-multiple-bonds` |
| Predicting the sign of entropy change in reactions | `entropy-of-reactions` | g12 | `hs1.kinetic-molecular-theory`, `hs1.states-in-equations` |
| Calculating entropy change from standard entropies | `standard-entropies` | g12 | `entropy-of-reactions` |
| Predicting spontaneity with Gibbs energy | `gibbs-energy-spontaneity` | g12 | `standard-entropies`, `enthalpy-of-formation` |
| Finding the temperature where spontaneity changes | `spontaneity-temperature` | g12 | `gibbs-energy-spontaneity` |

### Reaction rates

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Measuring reaction rates | `measuring-reaction-rates` | g11 | `hs1.molarity`, `ms.reaction-speed-factors` |
| Relating rates of different species | `rates-from-stoichiometry` | g11 | `measuring-reaction-rates`, `hs1.mole-ratios` |
| Finding average and instantaneous rates from graphs | `average-and-instantaneous-rates` | g11 | `measuring-reaction-rates` |
| Explaining rates with collision theory | `collision-theory` | g11 | `measuring-reaction-rates`, `hs1.kinetic-molecular-theory` |
| Reading activation energy on energy diagrams | `activation-energy-diagrams` | g11 | `collision-theory`, `hs1.energy-diagrams-of-reactions` |
| Using energy distributions to explain temperature effects | `energy-distributions-and-temperature` | g11 | `activation-energy-diagrams` |
| Explaining how catalysts change rates | `catalysts` | g11 | `activation-energy-diagrams` |
| Writing rate laws | `rate-laws-intro` | g12 | `rates-from-stoichiometry` |
| Finding reaction orders from initial rate data | `reaction-order-from-data` | g12 | `rate-laws-intro`, `alg2.solve-exponential-with-logs` |
| Finding rate constants and their units | `rate-constant-units` | g12 | `reaction-order-from-data` |
| Using the first-order integrated rate law | `first-order-integrated-law` | g12 | `rate-constant-units`, `alg2.common-natural-logs` |
| Using zero-order and second-order integrated rate laws | `zero-and-second-order-laws` | g12 | `first-order-integrated-law` |
| Finding half-lives of reactions | `half-life-of-reactions` | g12 | `first-order-integrated-law`, `hs1.half-life` |
| Finding order from linear plots | `order-from-linear-plots` | g12 | `zero-and-second-order-laws`, `alg2.linearize-with-logs` |
| Writing reaction mechanisms from elementary steps | `reaction-mechanisms` | g12 | `rate-laws-intro`, `catalysts` |
| Linking the slow step to the rate law | `rate-determining-step` | g12 | `reaction-mechanisms` |

### Equilibrium

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing dynamic equilibrium | `dynamic-equilibrium` | g11 | `collision-theory` |
| Writing equilibrium expressions | `equilibrium-expressions` | g11 | `dynamic-equilibrium`, `hs1.states-in-equations` |
| Interpreting the size of the equilibrium constant | `equilibrium-constant-size` | g11 | `equilibrium-expressions` |
| Predicting direction with the reaction quotient | `reaction-quotient` | g11 | `equilibrium-expressions` |
| Changing K when equations are reversed or combined | `combining-equilibrium-constants` | g12 | `equilibrium-expressions`, `hess-law` |
| Calculating K from equilibrium concentrations | `k-from-concentrations` | g11 | `equilibrium-expressions` |
| Finding equilibrium concentrations with ICE tables | `ice-tables` | g11 | `k-from-concentrations` |
| Solving ICE tables with quadratics or small-x approximations | `ice-with-quadratics` | g12 | `ice-tables`, `alg1.quadratic-formula` |
| Converting between Kp and Kc | `kp-and-kc` | g12 | `equilibrium-expressions`, `hs1.ideal-gas-law-with-moles` |
| Predicting shifts from concentration changes | `le-chatelier-concentration` | g11 | `reaction-quotient` |
| Predicting shifts from pressure and temperature changes | `le-chatelier-pressure-temperature` | g11 | `le-chatelier-concentration`, `hs1.thermochemical-equations` |
| Reading concentration-time graphs at equilibrium | `equilibrium-graphs` | g11 | `le-chatelier-pressure-temperature` |
| Choosing conditions for industrial yield | `industrial-equilibria` | g11 | `le-chatelier-pressure-temperature`, `catalysts` |

### Solubility equilibrium

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing solubility product expressions | `solubility-product` | g11 | `equilibrium-expressions`, `hs1.solubility-rules` |
| Converting between solubility and Ksp | `ksp-and-solubility` | g12 | `solubility-product`, `ice-tables` |
| Predicting precipitation with ion products | `predicting-precipitation` | g12 | `ksp-and-solubility`, `reaction-quotient` |
| Finding solubility with a common ion | `common-ion-effect` | g12 | `ksp-and-solubility`, `le-chatelier-concentration` |

### Acids and bases

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using Arrhenius and Bronsted-Lowry definitions | `acid-base-definitions` | g11 | `hs1.neutralization-equations`, `dynamic-equilibrium` |
| Identifying conjugate acid-base pairs | `conjugate-pairs` | g11 | `acid-base-definitions` |
| Identifying amphiprotic species | `amphiprotic-species` | g11 | `conjugate-pairs` |
| Using the ion product of water | `water-ion-product` | g11 | `equilibrium-expressions`, `acid-base-definitions` |
| Calculating pH and pOH | `ph-and-poh` | g11 | `water-ion-product`, `alg2.common-natural-logs` |
| Finding pH of strong acids and bases | `strong-acid-and-base-ph` | g11 | `ph-and-poh`, `hs1.ion-concentrations` |
| Finding pH after mixing strong acids and bases | `mixing-strong-acids-and-bases` | g11 | `strong-acid-and-base-ph`, `hs1.solution-stoichiometry` |
| Using Ka and Kb | `ka-and-kb` | g12 | `strong-acid-and-base-ph`, `ice-tables` |
| Finding pH of weak acid solutions | `weak-acid-ph` | g12 | `ka-and-kb`, `ice-with-quadratics` |
| Finding pH of weak base solutions | `weak-base-ph` | g12 | `weak-acid-ph` |
| Relating Ka and Kb of conjugates | `ka-kb-relationship` | g12 | `ka-and-kb`, `combining-equilibrium-constants` |
| Finding percent ionization | `percent-ionization` | g12 | `weak-acid-ph` |
| Explaining acid strength from structure | `acid-strength-and-structure` | g12 | `ka-and-kb`, `hs1.electronegativity-trend` |
| Predicting acidity of salt solutions | `salt-solutions-ph` | g12 | `ka-kb-relationship` |
| Describing stepwise ionization of polyprotic acids | `polyprotic-acids` | g12 | `ka-and-kb` |
| Explaining how buffers resist pH change | `buffers` | g12 | `conjugate-pairs`, `le-chatelier-concentration` |
| Finding buffer pH with Henderson-Hasselbalch | `henderson-hasselbalch` | g12 | `buffers`, `weak-acid-ph` |
| Analyzing strong acid-strong base titrations | `strong-acid-strong-base-titration` | g11 | `mixing-strong-acids-and-bases`, `hs1.titration-intro` |
| Analyzing weak acid-strong base titrations | `weak-acid-strong-base-titration` | g12 | `strong-acid-strong-base-titration`, `henderson-hasselbalch`, `salt-solutions-ph` |
| Choosing indicators for titrations | `choosing-indicators` | g12 | `weak-acid-strong-base-titration` |
| Using Lewis acid-base definitions | `lewis-acids-and-bases` | g12 | `acid-base-definitions`, `hs1.lewis-structures-simple` |

### Redox and electrochemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Assigning oxidation numbers | `oxidation-numbers` | g11 | `hs1.naming-ionic-compounds`, `hs1.electronegativity-trend` |
| Identifying oxidation, reduction and agents | `identifying-redox` | g11 | `oxidation-numbers` |
| Writing half-reactions | `half-reactions` | g11 | `identifying-redox` |
| Balancing redox in acidic solution | `balancing-redox-acidic` | g12 | `half-reactions` |
| Balancing redox in basic solution | `balancing-redox-basic` | g12 | `balancing-redox-acidic` |
| Calculating with redox titrations | `redox-titrations` | g12 | `balancing-redox-acidic`, `hs1.titration-intro` |
| Describing galvanic cells | `galvanic-cells` | g12 | `half-reactions`, `hs1.single-replacement-activity` |
| Writing cell notation | `cell-notation` | g12 | `galvanic-cells` |
| Using standard reduction potentials | `standard-reduction-potentials` | g12 | `galvanic-cells` |
| Calculating standard cell potentials | `standard-cell-potential` | g12 | `standard-reduction-potentials` |
| Predicting spontaneous redox reactions | `spontaneous-redox-prediction` | g12 | `standard-cell-potential` |
| Describing electrolytic cells | `electrolytic-cells` | g12 | `galvanic-cells` |
| Calculating products of electrolysis | `electrolysis-calculations` | g12 | `electrolytic-cells`, `hs1.mass-mole-particle-conversions`, `ms.current-and-voltage` |
| Explaining corrosion and its prevention | `corrosion` | g12 | `spontaneous-redox-prediction` |
| Comparing batteries and fuel cells | `batteries-and-fuel-cells` | g12 | `standard-cell-potential` |

### Spectroscopy and structure

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading photoelectron spectra | `photoelectron-spectroscopy` | g12 | `hs1.successive-ionization-energies`, `hs1.electron-configurations` |
| Using the Beer-Lambert law | `beer-lambert-law` | g12 | `hs1.molarity`, `hs1.photon-energy` |
| Linking spectrum regions to molecular transitions | `spectrum-regions-and-transitions` | g12 | `hs1.emission-and-absorption`, `hs1.molecular-polarity` |

### Solutions and phases

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining energy changes in dissolving | `dissolving-energetics` | g11 | `hs1.like-dissolves-like`, `hs1.energy-diagrams-of-reactions` |
| Explaining vapour pressure and boiling | `vapor-pressure-intro` | g11 | `hs1.forces-and-boiling-points` |
| Describing colligative properties | `colligative-properties-intro` | g11 | `hs1.molarity`, `vapor-pressure-intro` |
| Separating mixtures by intermolecular forces | `separation-by-intermolecular-forces` | g11 | `hs1.forces-and-boiling-points`, `ms.paper-chromatography` |
| Explaining deviations from ideal gas behaviour | `real-gas-deviations` | g12 | `hs1.ideal-gas-law-with-moles`, `hs1.intermolecular-forces` |

## chem.gen1: 50 topics

### Quantum atom

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing the quantum mechanical model of the atom | `quantum-mechanical-atom` | uni-lower | `hs1.quantum-numbers`, `hs2.de-broglie-wavelength`, `hs2.uncertainty-idea` |
| Describing orbital shapes and nodes | `orbital-shapes-and-nodes` | uni-lower | `quantum-mechanical-atom` |
| Explaining penetration and shielding with orbital plots | `penetration-and-shielding` | uni-lower | `orbital-shapes-and-nodes`, `hs1.effective-nuclear-charge` |
| Estimating effective nuclear charge with Slater's rules | `slaters-rules` | uni-lower | `penetration-and-shielding` |
| Predicting paramagnetism from configurations | `atomic-magnetism` | uni-lower | `hs1.orbital-diagrams` |
| Explaining trends in electron affinity | `electron-affinity-trend` | uni-lower | `hs1.ionization-energy-trend`, `penetration-and-shielding` |

### Ionic and covalent bonding

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing lattice energies with Coulomb's law | `lattice-energy` | uni-lower | `hs1.ionic-solid-properties`, `hs2.coulombs-law` |
| Calculating lattice energy with a Born-Haber cycle | `born-haber-cycle` | uni-lower | `lattice-energy`, `hs2.hess-law`, `electron-affinity-trend` |
| Relating bond order, length and strength | `bond-order-length-strength` | uni-lower | `hs1.lewis-structures-multiple-bonds`, `hs2.bond-enthalpies` |
| Predicting shapes with expanded octets | `expanded-octet-shapes` | uni-lower | `hs1.vsepr-shapes`, `hs1.octet-exceptions` |
| Estimating molecular dipole moments | `dipole-moments` | uni-lower | `hs1.molecular-polarity`, `hs2.electric-dipoles` |
| Describing bonds as orbital overlap | `valence-bond-theory` | uni-lower | `hs1.lewis-structures-simple`, `orbital-shapes-and-nodes` |
| Assigning hybridization to atoms | `hybridization` | uni-lower | `valence-bond-theory`, `expanded-octet-shapes` |
| Counting sigma and pi bonds | `sigma-and-pi-bonds` | uni-lower | `hybridization` |
| Drawing molecular orbital diagrams for diatomic molecules | `molecular-orbitals-diatomic` | uni-lower | `valence-bond-theory` |
| Finding bond order and magnetism from orbital diagrams | `bond-order-and-magnetism-from-mo` | uni-lower | `molecular-orbitals-diatomic`, `atomic-magnetism` |
| Drawing orbital diagrams for heteronuclear diatomics | `heteronuclear-diatomic-orbitals` | uni-lower | `bond-order-and-magnetism-from-mo`, `hs1.electronegativity-trend` |
| Explaining delocalized pi bonding | `delocalized-pi-bonding` | uni-lower | `sigma-and-pi-bonds`, `hs1.resonance-structures` |

### Gases and liquids

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using mole fractions with partial pressures | `mole-fractions` | uni-lower | `hs1.partial-pressures` |
| Using the van der Waals equation (moved from `physics.waves-thermo-optics.real-gases`) | `real-gases` | uni-lower | `hs1.ideal-gas-law-with-moles`, `hs2.real-gas-deviations` |
| Explaining dispersion forces with polarizability | `dispersion-and-polarizability` | uni-lower | `hs1.intermolecular-forces` |
| Linking surface tension and viscosity to intermolecular forces | `surface-tension-and-viscosity-of-liquids` | uni-lower | `hs1.forces-and-boiling-points` |
| Using the Clausius-Clapeyron equation for vapour pressure | `vapor-pressure-and-temperature` | uni-lower | `hs2.vapor-pressure-intro`, `alg2.common-natural-logs` |
| Reading phase diagrams and critical points (moved from `physics.waves-thermo-optics.phase-diagrams`) | `phase-diagrams` | uni-lower | `real-gases`, `hs1.latent-heat`, `vapor-pressure-and-temperature` |

### Solids

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing crystal lattices and unit cells | `crystal-lattices-and-unit-cells` | uni-lower | `hs1.comparing-solid-types` |
| Counting atoms in cubic unit cells | `atoms-per-unit-cell` | uni-lower | `crystal-lattices-and-unit-cells` |
| Finding density and radius from unit cell dimensions | `density-from-unit-cell` | uni-lower | `atoms-per-unit-cell`, `hs1.density-calculations` |
| Comparing packing efficiency of structures | `packing-efficiency` | uni-lower | `atoms-per-unit-cell` |
| Describing common ionic crystal structures | `ionic-crystal-structures` | uni-lower | `atoms-per-unit-cell`, `lattice-energy` |
| Describing substitutional and interstitial alloys | `alloys` | uni-lower | `crystal-lattices-and-unit-cells`, `hs1.metallic-bonding` |
| Finding lattice spacing from x-ray diffraction | `x-ray-crystallography-in-chemistry` | uni-lower | `crystal-lattices-and-unit-cells`, `hs2.diffraction-gratings` |

### Solutions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Converting among molarity, molality and mole fraction | `molality-and-mole-fraction` | uni-lower | `hs1.molarity`, `mole-fractions` |
| Using Henry's law for gas solubility | `henrys-law` | uni-lower | `molality-and-mole-fraction`, `hs1.partial-pressures` |
| Finding vapour pressure lowering with Raoult's law | `raoults-law` | uni-lower | `molality-and-mole-fraction`, `hs2.colligative-properties-intro` |
| Calculating boiling point elevation and freezing point depression | `boiling-and-freezing-point-changes` | uni-lower | `molality-and-mole-fraction`, `hs2.colligative-properties-intro` |
| Calculating osmotic pressure | `osmotic-pressure` | uni-lower | `boiling-and-freezing-point-changes`, `hs1.ideal-gas-law-with-moles` |
| Using the van't Hoff factor for electrolytes | `vant-hoff-factor` | uni-lower | `boiling-and-freezing-point-changes`, `hs1.electrolytes` |
| Finding molar mass from colligative properties | `molar-mass-from-colligative-properties` | uni-lower | `boiling-and-freezing-point-changes`, `osmotic-pressure` |
| Finding vapour composition of ideal liquid mixtures | `ideal-solutions-and-distillation` | uni-lower | `raoults-law` |
| Describing colloids and their properties | `colloids` | uni-lower | `hs1.like-dissolves-like` |

### Thermochemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using state functions in chemical processes | `state-functions-in-chemistry` | uni-lower | `hs2.first-law-of-thermodynamics`, `hs1.enthalpy-of-reaction` |
| Finding pressure-volume work in reactions | `pressure-volume-work-in-reactions` | uni-lower | `state-functions-in-chemistry`, `hs2.work-on-a-gas` |
| Using enthalpy for constant pressure processes (moved from `physics.waves-thermo-optics.enthalpy`) | `enthalpy` | uni-lower | `pressure-volume-work-in-reactions` |
| Relating enthalpy and internal energy changes of reactions | `enthalpy-and-internal-energy` | uni-lower | `enthalpy`, `hs1.gas-stoichiometry` |
| Finding internal energy change with a bomb calorimeter | `bomb-calorimetry` | uni-lower | `enthalpy-and-internal-energy`, `hs1.reaction-calorimetry` |
| Building thermochemical cycles | `thermochemical-cycles` | uni-lower | `hs2.hess-law`, `hs2.enthalpy-of-formation` |
| Comparing energy content of fuels and foods | `fuel-and-food-energy` | uni-lower | `thermochemical-cycles` |

### Quantitative analysis of compounds

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding empirical formulas by combustion analysis | `combustion-analysis` | uni-lower | `hs1.empirical-formulas`, `hs1.combustion-equations` |
| Finding overall yield of multistep processes | `multistep-yield` | uni-lower | `hs1.percent-yield` |
| Analyzing back titrations | `back-titration` | uni-lower | `hs1.titration-intro`, `hs1.solution-stoichiometry` |

## chem.gen2: 50 topics

### Chemical kinetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the Arrhenius equation | `arrhenius-equation` | uni-lower | `hs2.energy-distributions-and-temperature`, `hs2.rate-constant-units` |
| Finding activation energy from rate data | `activation-energy-from-data` | uni-lower | `arrhenius-equation`, `alg2.linearize-with-logs` |
| Explaining the orientation factor in collisions | `orientation-factor` | uni-lower | `arrhenius-equation`, `hs2.collision-theory` |
| Deriving rate laws with a fast pre-equilibrium | `mechanisms-with-fast-equilibrium` | uni-lower | `hs2.rate-determining-step`, `hs2.equilibrium-expressions` |
| Using the steady-state approximation for intermediates | `steady-state-intermediates` | uni-lower | `mechanisms-with-fast-equilibrium` |
| Using pseudo-first-order conditions | `pseudo-first-order` | uni-lower | `hs2.first-order-integrated-law` |
| Comparing homogeneous and heterogeneous catalysis | `homogeneous-and-heterogeneous-catalysis` | uni-lower | `hs2.catalysts`, `hs2.reaction-mechanisms` |
| Describing enzyme kinetics and saturation | `enzyme-kinetics-intro` | uni-lower | `homogeneous-and-heterogeneous-catalysis` |

### Chemical equilibrium

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing expressions for heterogeneous equilibria | `heterogeneous-equilibria` | uni-lower | `hs2.equilibrium-expressions` |
| Solving coupled equilibria | `simultaneous-equilibria` | uni-lower | `hs2.combining-equilibrium-constants`, `hs2.ice-with-quadratics` |
| Finding new equilibria after volume changes | `equilibrium-with-changing-volume` | uni-lower | `hs2.le-chatelier-pressure-temperature`, `hs2.kp-and-kc` |

### Acid-base equilibria

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding species concentrations in polyprotic solutions | `polyprotic-species-concentrations` | uni-lower | `hs2.polyprotic-acids`, `hs2.weak-acid-ph` |
| Finding pH of amphiprotic salt solutions | `amphiprotic-salt-ph` | uni-lower | `polyprotic-species-concentrations`, `hs2.amphiprotic-species` |
| Finding fractions of acid species against pH | `fractional-composition` | uni-lower | `polyprotic-species-concentrations`, `hs2.henderson-hasselbalch` |
| Preparing a buffer of given pH | `buffer-preparation` | uni-lower | `hs2.henderson-hasselbalch`, `hs1.preparing-solutions` |
| Finding pH change when acid or base is added to a buffer | `buffer-capacity` | uni-lower | `buffer-preparation`, `hs1.solution-stoichiometry` |
| Calculating pH throughout a weak acid titration | `titration-curve-calculations` | uni-lower | `hs2.weak-acid-strong-base-titration`, `buffer-capacity` |
| Analyzing titrations of polyprotic acids | `polyprotic-titrations` | uni-lower | `titration-curve-calculations`, `polyprotic-species-concentrations` |
| Analyzing weak base-strong acid titrations | `weak-base-strong-acid-titration` | uni-lower | `titration-curve-calculations`, `hs2.weak-base-ph` |

### Solubility and complex ions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Separating ions by selective precipitation | `selective-precipitation` | uni-lower | `hs2.predicting-precipitation` |
| Finding how pH changes solubility | `ph-and-solubility` | uni-lower | `hs2.ksp-and-solubility`, `hs2.salt-solutions-ph` |
| Using formation constants for complex ions | `complex-ion-formation` | uni-lower | `hs2.lewis-acids-and-bases`, `hs2.equilibrium-expressions` |
| Finding solubility when complexes form | `solubility-with-complexation` | uni-lower | `complex-ion-formation`, `hs2.ksp-and-solubility`, `hs2.combining-equilibrium-constants` |
| Identifying ions by qualitative analysis | `qualitative-analysis` | uni-lower | `selective-precipitation`, `complex-ion-formation` |

### Chemical thermodynamics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Applying the second law to chemical systems | `second-law-in-chemistry` | uni-lower | `hs2.standard-entropies`, `hs2.entropy-and-second-law` |
| Finding entropy change of surroundings from enthalpy | `entropy-of-surroundings` | uni-lower | `second-law-in-chemistry`, `hs1.enthalpy-of-reaction` |
| Using standard Gibbs energies of formation | `standard-gibbs-of-formation` | uni-lower | `hs2.gibbs-energy-spontaneity`, `hs2.enthalpy-of-formation` |
| Finding Gibbs energy change under nonstandard conditions | `gibbs-energy-nonstandard` | uni-lower | `standard-gibbs-of-formation`, `hs2.reaction-quotient` |
| Relating standard Gibbs energy to the equilibrium constant | `gibbs-energy-and-k` | uni-lower | `gibbs-energy-nonstandard`, `hs2.equilibrium-constant-size` |
| Finding how K changes with temperature | `vant-hoff-equation` | uni-lower | `gibbs-energy-and-k`, `hs2.le-chatelier-pressure-temperature` |
| Driving reactions by coupling | `coupled-reactions` | uni-lower | `gibbs-energy-and-k` |

### Electrochemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Relating cell potential to Gibbs energy | `gibbs-energy-and-cell-potential` | uni-lower | `hs2.standard-cell-potential`, `standard-gibbs-of-formation` |
| Relating cell potential to the equilibrium constant | `cell-potential-and-k` | uni-lower | `gibbs-energy-and-cell-potential`, `gibbs-energy-and-k` |
| Using the Nernst equation | `nernst-equation` | uni-lower | `gibbs-energy-and-cell-potential`, `gibbs-energy-nonstandard` |
| Analyzing concentration cells | `concentration-cells` | uni-lower | `nernst-equation` |
| Finding pH from cell potential | `ph-from-cell-potential` | uni-lower | `nernst-equation`, `hs2.ph-and-poh` |
| Finding Ksp from standard potentials | `ksp-from-cell-potential` | uni-lower | `cell-potential-and-k`, `hs2.solubility-product` |
| Describing industrial electrolysis processes | `industrial-electrolysis` | uni-lower | `hs2.electrolysis-calculations` |

### Coordination chemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing coordination compounds and ligands | `coordination-compound-structure` | uni-lower | `complex-ion-formation` |
| Naming coordination compounds | `naming-coordination-compounds` | uni-lower | `coordination-compound-structure`, `hs1.transition-metal-names` |
| Identifying isomers of coordination compounds | `isomers-of-complexes` | uni-lower | `coordination-compound-structure`, `hs1.vsepr-shapes` |
| Describing crystal field splitting | `crystal-field-splitting` | uni-lower | `coordination-compound-structure`, `gen1.orbital-shapes-and-nodes` |
| Predicting high-spin and low-spin complexes | `high-and-low-spin` | uni-lower | `crystal-field-splitting`, `gen1.atomic-magnetism` |
| Explaining colours of complexes | `color-of-complexes` | uni-lower | `crystal-field-splitting`, `hs1.emission-and-absorption` |
| Explaining the chelate effect | `chelate-effect` | uni-lower | `complex-ion-formation`, `second-law-in-chemistry` |

### Main group and transition elements

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying oxides as acidic, basic or amphoteric | `periodic-properties-of-oxides` | uni-lower | `hs2.acid-base-definitions`, `hs1.metallic-character-trend` |
| Predicting reactions of alkali and alkaline earth metals | `alkali-and-alkaline-earth-reactions` | uni-lower | `hs1.single-replacement-activity`, `periodic-properties-of-oxides` |
| Describing halogen and noble gas chemistry | `halogen-and-noble-gas-chemistry` | uni-lower | `hs2.oxidation-numbers`, `hs1.electronegativity-trend` |
| Describing properties of transition metals | `transition-metal-properties` | uni-lower | `hs1.configurations-of-ions`, `crystal-field-splitting` |
| Describing extraction and refining of metals | `metallurgy` | uni-lower | `transition-metal-properties`, `industrial-electrolysis` |

## chem.org1: 98 topics

### Structure and bonding in organic molecules

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading and drawing skeletal structures | `skeletal-structures` | uni-lower | `hs1.structural-formulas`, `gen1.hybridization` |
| Assigning formal charges in organic molecules | `formal-charges-in-organic-molecules` | uni-lower | `skeletal-structures`, `hs1.formal-charge` |
| Using curved arrows to show electron movement | `curved-arrow-notation` | uni-lower | `formal-charges-in-organic-molecules` |
| Drawing resonance forms of organic species | `resonance-in-organic-molecules` | uni-lower | `curved-arrow-notation`, `gen1.delocalized-pi-bonding` |
| Ranking resonance contributors | `resonance-contributor-ranking` | uni-lower | `resonance-in-organic-molecules` |
| Predicting hybridization and geometry in organic molecules | `hybridization-and-geometry-in-organics` | uni-lower | `skeletal-structures`, `gen1.sigma-and-pi-bonds` |
| Predicting physical properties of organic compounds | `intermolecular-forces-of-organics` | uni-lower | `skeletal-structures`, `hs1.forces-and-boiling-points` |

### Organic acids and bases

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using a pKa table to predict acid-base equilibria | `pka-table-use` | uni-lower | `curved-arrow-notation`, `hs2.ka-and-kb` |
| Ranking organic acids by atom, resonance, induction and orbital | `acid-strength-factors-organic` | uni-lower | `pka-table-use`, `resonance-in-organic-molecules`, `hs2.acid-strength-and-structure` |
| Identifying nucleophiles and electrophiles | `lewis-acid-base-in-organics` | uni-lower | `curved-arrow-notation`, `hs2.lewis-acids-and-bases` |

### Alkanes and cycloalkanes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming branched alkanes and cycloalkanes | `iupac-naming-alkanes` | uni-lower | `skeletal-structures`, `hs1.naming-alkanes` |
| Drawing Newman projections and conformations | `newman-projections` | uni-lower | `skeletal-structures` |
| Comparing energies of conformations | `conformational-energy` | uni-lower | `newman-projections` |
| Explaining ring strain in cycloalkanes | `ring-strain` | uni-lower | `conformational-energy` |
| Drawing cyclohexane chair conformations | `cyclohexane-chairs` | uni-lower | `ring-strain` |
| Comparing axial and equatorial substituents | `substituted-cyclohexanes` | uni-lower | `cyclohexane-chairs` |
| Identifying cis-trans isomers of rings | `cis-trans-rings` | uni-lower | `substituted-cyclohexanes` |

### Stereochemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Identifying chiral centres and molecules | `chirality` | uni-lower | `skeletal-structures`, `hs1.structural-isomers` |
| Assigning R and S configurations | `cahn-ingold-prelog` | uni-lower | `chirality` |
| Telling enantiomers from diastereomers | `enantiomers-and-diastereomers` | uni-lower | `cahn-ingold-prelog` |
| Identifying meso compounds | `meso-compounds` | uni-lower | `enantiomers-and-diastereomers` |
| Using Fischer projections | `fischer-projections` | uni-lower | `cahn-ingold-prelog` |
| Calculating specific rotation and enantiomeric excess | `optical-activity` | uni-lower | `enantiomers-and-diastereomers` |
| Describing resolution of enantiomers | `resolution-of-enantiomers` | uni-lower | `optical-activity` |
| Assigning stereochemistry in rings | `stereochemistry-of-rings` | uni-lower | `cahn-ingold-prelog`, `cis-trans-rings` |

### Reaction fundamentals

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying organic reactions | `reaction-types-organic` | uni-lower | `lewis-acid-base-in-organics` |
| Reading energy diagrams with intermediates | `energy-diagrams-for-organic-reactions` | uni-lower | `reaction-types-organic`, `hs2.activation-energy-diagrams` |
| Ranking carbocation stability | `carbocation-stability` | uni-lower | `reaction-types-organic`, `hybridization-and-geometry-in-organics` |
| Ranking radical stability | `radical-stability` | uni-lower | `carbocation-stability` |
| Telling thermodynamic from kinetic control | `thermodynamic-vs-kinetic-control` | uni-lower | `energy-diagrams-for-organic-reactions` |

### Substitution and elimination

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming alkyl halides | `alkyl-halide-naming-and-properties` | uni-lower | `iupac-naming-alkanes` |
| Drawing the SN2 mechanism | `sn2-mechanism` | uni-lower | `alkyl-halide-naming-and-properties`, `lewis-acid-base-in-organics`, `cahn-ingold-prelog` |
| Predicting SN2 rates from substrate, nucleophile and leaving group | `sn2-rate-factors` | uni-lower | `sn2-mechanism` |
| Drawing the SN1 mechanism | `sn1-mechanism` | uni-lower | `sn2-mechanism`, `carbocation-stability` |
| Predicting carbocation rearrangements | `carbocation-rearrangements` | uni-lower | `sn1-mechanism` |
| Choosing solvents for substitution | `solvent-effects` | uni-lower | `sn2-rate-factors`, `sn1-mechanism` |
| Drawing the E2 mechanism | `e2-mechanism` | uni-lower | `sn2-mechanism`, `newman-projections` |
| Predicting Zaitsev and Hofmann products | `zaitsev-and-hofmann` | uni-lower | `e2-mechanism` |
| Predicting E2 products in cyclohexanes | `e2-in-cyclohexanes` | uni-lower | `e2-mechanism`, `substituted-cyclohexanes` |
| Drawing the E1 mechanism | `e1-mechanism` | uni-lower | `sn1-mechanism`, `zaitsev-and-hofmann` |
| Predicting substitution or elimination | `substitution-vs-elimination` | uni-lower | `solvent-effects`, `e2-mechanism`, `e1-mechanism` |

### Alcohols, ethers and epoxides

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming alcohols and ethers | `naming-alcohols-and-ethers` | uni-lower | `iupac-naming-alkanes`, `hs1.functional-groups-intro` |
| Converting alcohols to alkyl halides | `alcohols-to-alkyl-halides` | uni-lower | `naming-alcohols-and-ethers`, `substitution-vs-elimination` |
| Making sulfonate esters as leaving groups | `sulfonate-leaving-groups` | uni-lower | `alcohols-to-alkyl-halides` |
| Dehydrating alcohols to alkenes | `dehydration-of-alcohols` | uni-lower | `e1-mechanism`, `naming-alcohols-and-ethers` |
| Oxidizing alcohols | `oxidation-of-alcohols` | uni-lower | `naming-alcohols-and-ethers`, `hs2.oxidation-numbers` |
| Making ethers by Williamson synthesis | `williamson-ether-synthesis` | uni-lower | `sn2-rate-factors`, `naming-alcohols-and-ethers` |
| Cleaving ethers with strong acid | `ether-cleavage` | uni-lower | `williamson-ether-synthesis` |
| Opening epoxides under acid and base | `epoxide-ring-opening` | uni-lower | `ether-cleavage`, `stereochemistry-of-rings` |
| Describing thiols and sulfides | `thiols-and-sulfides` | uni-lower | `naming-alcohols-and-ethers` |

### Alkenes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming alkenes with E and Z | `naming-alkenes-e-z` | uni-lower | `cahn-ingold-prelog`, `hs1.naming-alkenes-and-alkynes` |
| Comparing alkene stability | `alkene-stability` | uni-lower | `naming-alkenes-e-z`, `zaitsev-and-hofmann` |
| Adding hydrogen halides with Markovnikov selectivity | `hydrohalogenation` | uni-lower | `alkene-stability`, `carbocation-rearrangements` |
| Hydrating alkenes with acid | `acid-catalyzed-hydration` | uni-lower | `hydrohalogenation` |
| Hydrating alkenes by oxymercuration | `oxymercuration` | uni-lower | `acid-catalyzed-hydration` |
| Hydrating alkenes by hydroboration | `hydroboration-oxidation` | uni-lower | `acid-catalyzed-hydration`, `enantiomers-and-diastereomers` |
| Adding halogens across alkenes | `halogenation-of-alkenes` | uni-lower | `alkene-stability`, `stereochemistry-of-rings` |
| Forming halohydrins | `halohydrin-formation` | uni-lower | `halogenation-of-alkenes` |
| Hydrogenating alkenes | `catalytic-hydrogenation` | uni-lower | `alkene-stability`, `gen2.homogeneous-and-heterogeneous-catalysis` |
| Making epoxides and diols from alkenes | `epoxidation-and-dihydroxylation` | uni-lower | `halogenation-of-alkenes`, `epoxide-ring-opening` |
| Cleaving alkenes by ozonolysis | `ozonolysis` | uni-lower | `epoxidation-and-dihydroxylation` |
| Adding HBr by a radical mechanism | `radical-addition-of-hbr` | uni-lower | `hydrohalogenation`, `radical-stability` |
| Predicting stereochemistry of alkene additions | `alkene-addition-stereochemistry` | uni-lower | `halogenation-of-alkenes`, `hydroboration-oxidation`, `epoxidation-and-dihydroxylation` |

### Alkynes and radicals

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using acetylide ions in synthesis | `alkyne-acidity-and-acetylides` | uni-lower | `naming-alkenes-e-z`, `pka-table-use`, `sn2-rate-factors` |
| Adding to alkynes | `alkyne-additions` | uni-lower | `hydrohalogenation`, `alkyne-acidity-and-acetylides` |
| Reducing alkynes to cis and trans alkenes | `alkyne-reductions` | uni-lower | `alkyne-additions`, `catalytic-hydrogenation` |
| Halogenating alkanes by radical chain reactions | `radical-halogenation` | uni-lower | `radical-stability`, `iupac-naming-alkanes` |
| Brominating allylic positions | `allylic-bromination` | uni-lower | `radical-halogenation`, `resonance-in-organic-molecules` |

### Spectroscopy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Interpreting mass spectra of organic compounds | `mass-spectrometry-organic` | uni-lower | `skeletal-structures`, `hs1.mass-spectra-of-elements` |
| Identifying functional groups by infrared spectroscopy | `infrared-spectroscopy` | uni-lower | `skeletal-structures`, `hs2.spectrum-regions-and-transitions` |
| Finding degrees of unsaturation | `degree-of-unsaturation` | uni-lower | `skeletal-structures`, `hs1.molecular-formulas` |
| Predicting proton NMR chemical shifts | `proton-nmr-shifts` | uni-lower | `skeletal-structures`, `hs2.spectrum-regions-and-transitions` |
| Using integration and splitting in proton NMR | `proton-nmr-integration-and-splitting` | uni-lower | `proton-nmr-shifts` |
| Interpreting carbon-13 NMR spectra | `carbon-13-nmr` | uni-lower | `proton-nmr-shifts` |
| Determining structures from combined spectra | `structure-from-spectra` | uni-lower | `mass-spectrometry-organic`, `infrared-spectroscopy`, `proton-nmr-integration-and-splitting`, `carbon-13-nmr` |

### Synthesis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Interconverting functional groups | `functional-group-interconversion` | uni-lower | `alkene-addition-stereochemistry`, `substitution-vs-elimination`, `oxidation-of-alcohols` |
| Planning syntheses backwards | `retrosynthesis-basics` | uni-lower | `functional-group-interconversion` |
| Designing multistep syntheses with chain extension | `multistep-synthesis-org1` | uni-lower | `retrosynthesis-basics`, `alkyne-acidity-and-acetylides` |

### More practice with structure

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Drawing structures from IUPAC names | `structures-from-names` | uni-lower | `iupac-naming-alkanes`, `naming-alcohols-and-ethers` |
| Naming substituted cycloalkanes | `naming-substituted-cycloalkanes` | uni-lower | `iupac-naming-alkanes`, `cis-trans-rings` |
| Ranking conformers of disubstituted cyclohexanes | `disubstituted-cyclohexane-stability` | uni-lower | `substituted-cyclohexanes`, `cis-trans-rings` |
| Counting possible stereoisomers | `counting-stereoisomers` | uni-lower | `meso-compounds` |
| Predicting racemic and diastereomeric products | `stereocentres-formed-in-reactions` | uni-lower | `enantiomers-and-diastereomers`, `sn1-mechanism` |
| Drawing proton transfer steps | `proton-transfer-mechanisms` | uni-lower | `curved-arrow-notation`, `pka-table-use` |
| Telling nucleophilicity from basicity | `nucleophilicity-vs-basicity` | uni-lower | `sn2-rate-factors`, `pka-table-use` |
| Choosing bases to control elimination products | `bulky-bases-in-elimination` | uni-lower | `zaitsev-and-hofmann`, `nucleophilicity-vs-basicity` |
| Predicting intramolecular substitution and ring formation | `intramolecular-reactions` | uni-lower | `sn2-rate-factors`, `ring-strain` |
| Making alcohols by substitution | `alcohols-by-substitution` | uni-lower | `sn2-rate-factors`, `naming-alcohols-and-ethers` |
| Making cyclopropanes from alkenes | `carbene-cyclopropanation` | uni-lower | `halogenation-of-alkenes` |
| Making alkynes by double elimination | `alkynes-by-double-elimination` | uni-lower | `e2-mechanism`, `alkyne-acidity-and-acetylides` |
| Hydrating alkynes to ketones and aldehydes | `alkyne-hydration` | uni-lower | `alkyne-additions`, `oxymercuration`, `hydroboration-oxidation` |
| Cleaving alkynes by ozonolysis | `alkyne-cleavage` | uni-lower | `alkyne-additions`, `ozonolysis` |
| Comparing selectivity of chlorination and bromination | `halogenation-selectivity` | uni-lower | `radical-halogenation` |
| Identifying chemically equivalent protons | `equivalent-protons` | uni-lower | `proton-nmr-shifts`, `enantiomers-and-diastereomers` |
| Interpreting complex splitting patterns | `complex-splitting-patterns` | uni-lower | `proton-nmr-integration-and-splitting` |
| Choosing reagents for Markovnikov or anti-Markovnikov products | `anti-markovnikov-summary` | uni-lower | `hydroboration-oxidation`, `radical-addition-of-hbr`, `oxymercuration` |
| Connecting functional groups on a reaction map | `reaction-maps-org1` | uni-lower | `functional-group-interconversion`, `alkyne-hydration` |
| Planning syntheses with stereochemical control | `stereospecific-synthesis` | uni-lower | `multistep-synthesis-org1`, `alkene-addition-stereochemistry`, `stereocentres-formed-in-reactions` |

## chem.org2: 78 topics

### Conjugated systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing stability of conjugated dienes | `conjugated-dienes` | uni-upper | `org1.alkene-stability`, `org1.resonance-in-organic-molecules` |
| Predicting 1,2- and 1,4-addition to dienes | `addition-to-dienes` | uni-upper | `conjugated-dienes`, `org1.thermodynamic-vs-kinetic-control` |
| Predicting Diels-Alder products | `diels-alder-reaction` | uni-upper | `conjugated-dienes`, `org1.alkene-addition-stereochemistry` |
| Relating conjugation to UV-visible absorption | `uv-vis-of-conjugated-systems` | uni-upper | `conjugated-dienes`, `hs2.beer-lambert-law` |
| Describing electrocyclic and sigmatropic reactions | `pericyclic-reactions-intro` | uni-upper | `diels-alder-reaction`, `gen1.molecular-orbitals-diatomic` |

### Aromatic compounds

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Identifying aromatic compounds with Huckel's rule | `aromaticity-rules` | uni-upper | `conjugated-dienes`, `gen1.delocalized-pi-bonding` |
| Naming substituted benzenes | `naming-aromatic-compounds` | uni-upper | `aromaticity-rules`, `org1.iupac-naming-alkanes` |
| Identifying aromatic ions and heterocycles | `aromatic-ions-and-heterocycles` | uni-upper | `aromaticity-rules` |
| Drawing electrophilic aromatic substitution | `electrophilic-aromatic-substitution` | uni-upper | `aromaticity-rules`, `org1.carbocation-stability` |
| Halogenating, nitrating and sulfonating benzene | `halogenation-nitration-sulfonation` | uni-upper | `electrophilic-aromatic-substitution` |
| Using Friedel-Crafts alkylation and acylation | `friedel-crafts-reactions` | uni-upper | `electrophilic-aromatic-substitution`, `org1.carbocation-rearrangements` |
| Predicting directing effects of substituents | `directing-effects` | uni-upper | `halogenation-nitration-sulfonation`, `org1.resonance-contributor-ranking` |
| Predicting substitution on disubstituted rings | `multiple-substituents` | uni-upper | `directing-effects` |
| Planning syntheses of substituted benzenes | `aromatic-synthesis-planning` | uni-upper | `multiple-substituents`, `friedel-crafts-reactions`, `org1.retrosynthesis-basics` |
| Drawing nucleophilic aromatic substitution | `nucleophilic-aromatic-substitution` | uni-upper | `directing-effects` |
| Reacting at benzylic positions | `benzylic-reactions` | uni-upper | `naming-aromatic-compounds`, `org1.allylic-bromination` |
| Interpreting spectra of aromatic compounds | `aromatic-nmr-and-ir` | uni-upper | `naming-aromatic-compounds`, `org1.structure-from-spectra` |

### Aldehydes and ketones

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming aldehydes and ketones | `naming-aldehydes-and-ketones` | uni-upper | `org1.naming-alcohols-and-ethers`, `hs1.functional-groups-intro` |
| Drawing nucleophilic addition to carbonyls | `nucleophilic-addition-to-carbonyls` | uni-upper | `naming-aldehydes-and-ketones`, `org1.lewis-acid-base-in-organics` |
| Forming hydrates, hemiacetals and acetals | `hydrates-and-acetals` | uni-upper | `nucleophilic-addition-to-carbonyls` |
| Using protecting groups | `protecting-groups` | uni-upper | `hydrates-and-acetals`, `org1.retrosynthesis-basics` |
| Forming imines and enamines | `imines-and-enamines` | uni-upper | `nucleophilic-addition-to-carbonyls` |
| Reducing carbonyls with hydride reagents | `hydride-reductions` | uni-upper | `nucleophilic-addition-to-carbonyls`, `org1.oxidation-of-alcohols` |
| Adding Grignard and organolithium reagents to carbonyls | `grignard-and-organolithium-reagents` | uni-upper | `nucleophilic-addition-to-carbonyls`, `org1.pka-table-use` |
| Making alkenes with the Wittig reaction | `wittig-reaction` | uni-upper | `nucleophilic-addition-to-carbonyls`, `org1.naming-alkenes-e-z` |
| Forming cyanohydrins | `cyanohydrins` | uni-upper | `nucleophilic-addition-to-carbonyls` |
| Oxidizing ketones to esters | `baeyer-villiger-oxidation` | uni-upper | `nucleophilic-addition-to-carbonyls` |
| Interpreting spectra of carbonyl compounds | `carbonyl-spectroscopy` | uni-upper | `naming-aldehydes-and-ketones`, `org1.structure-from-spectra` |

### Carboxylic acids and derivatives

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming carboxylic acids and their derivatives | `naming-carboxylic-acids-and-derivatives` | uni-upper | `naming-aldehydes-and-ketones` |
| Explaining acidity of carboxylic acids | `carboxylic-acid-acidity` | uni-upper | `naming-carboxylic-acids-and-derivatives`, `org1.acid-strength-factors-organic` |
| Drawing nucleophilic acyl substitution | `nucleophilic-acyl-substitution` | uni-upper | `naming-carboxylic-acids-and-derivatives`, `nucleophilic-addition-to-carbonyls` |
| Ranking reactivity of acid derivatives | `derivative-reactivity-order` | uni-upper | `nucleophilic-acyl-substitution`, `org1.resonance-contributor-ranking` |
| Making and using acid chlorides and anhydrides | `acid-chlorides-and-anhydrides` | uni-upper | `derivative-reactivity-order` |
| Making and hydrolyzing esters | `esters-and-fischer-esterification` | uni-upper | `derivative-reactivity-order` |
| Making and hydrolyzing amides and nitriles | `amides-and-nitriles` | uni-upper | `derivative-reactivity-order` |
| Reducing carboxylic acids and derivatives | `reducing-acid-derivatives` | uni-upper | `hydride-reductions`, `derivative-reactivity-order` |
| Adding organometallic reagents to esters and acid chlorides | `organometallics-with-derivatives` | uni-upper | `grignard-and-organolithium-reagents`, `derivative-reactivity-order` |

### Enols and enolates

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Drawing keto-enol tautomerism | `keto-enol-tautomerism` | uni-upper | `naming-aldehydes-and-ketones`, `org1.pka-table-use` |
| Halogenating alpha carbons | `alpha-halogenation` | uni-upper | `keto-enol-tautomerism` |
| Forming enolates with strong bases | `enolate-formation` | uni-upper | `keto-enol-tautomerism`, `org1.thermodynamic-vs-kinetic-control` |
| Alkylating enolates | `enolate-alkylation` | uni-upper | `enolate-formation`, `org1.sn2-rate-factors` |
| Predicting aldol additions and condensations | `aldol-reaction` | uni-upper | `enolate-formation`, `nucleophilic-addition-to-carbonyls` |
| Planning crossed aldol reactions | `crossed-aldol-reactions` | uni-upper | `aldol-reaction` |
| Predicting Claisen condensations | `claisen-condensation` | uni-upper | `aldol-reaction`, `nucleophilic-acyl-substitution` |
| Using malonic and acetoacetic ester syntheses | `malonic-and-acetoacetic-ester-synthesis` | uni-upper | `enolate-alkylation`, `esters-and-fischer-esterification` |
| Predicting conjugate additions | `conjugate-addition` | uni-upper | `aldol-reaction`, `grignard-and-organolithium-reagents` |
| Predicting Robinson annulations | `robinson-annulation` | uni-upper | `conjugate-addition`, `aldol-reaction` |

### Amines

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming amines | `naming-amines` | uni-upper | `org1.naming-alcohols-and-ethers` |
| Ranking amine basicity | `amine-basicity` | uni-upper | `naming-amines`, `org1.acid-strength-factors-organic` |
| Making amines by alkylation and reductive amination | `amine-synthesis` | uni-upper | `amine-basicity`, `imines-and-enamines`, `amides-and-nitriles` |
| Predicting Hofmann elimination products | `hofmann-elimination` | uni-upper | `amine-synthesis`, `org1.zaitsev-and-hofmann` |
| Using arenediazonium salts in synthesis | `diazonium-salts` | uni-upper | `amine-synthesis`, `nucleophilic-aromatic-substitution` |

### Organometallic and coupling reactions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using organocuprates | `gilman-reagents` | uni-upper | `grignard-and-organolithium-reagents`, `conjugate-addition` |
| Predicting palladium cross-coupling products | `palladium-cross-coupling` | uni-upper | `gilman-reagents`, `naming-aromatic-compounds` |

### More carbonyl, aromatic and nitrogen chemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing acidity and reactions of phenols | `phenols` | uni-upper | `naming-aromatic-compounds`, `org1.acid-strength-factors-organic` |
| Describing polycyclic aromatic compounds | `polycyclic-aromatics` | uni-upper | `aromaticity-rules` |
| Reducing nitro groups to amines | `nitro-group-reduction` | uni-upper | `halogenation-nitration-sulfonation`, `naming-amines` |
| Oxidizing aldehydes to acids | `aldehyde-oxidation` | uni-upper | `naming-aldehydes-and-ketones`, `org1.oxidation-of-alcohols` |
| Reducing carbonyls to methylene groups | `deoxygenation-of-carbonyls` | uni-upper | `hydride-reductions`, `friedel-crafts-reactions` |
| Forming and using thioacetals | `thioacetals` | uni-upper | `hydrates-and-acetals`, `org1.thiols-and-sulfides` |
| Choosing routes to carboxylic acids | `carboxylic-acid-synthesis-routes` | uni-upper | `aldehyde-oxidation`, `amides-and-nitriles`, `grignard-and-organolithium-reagents` |
| Forming lactones and lactams | `lactones-and-lactams` | uni-upper | `esters-and-fischer-esterification`, `amides-and-nitriles`, `org1.intramolecular-reactions` |
| Decarboxylating beta-keto acids | `decarboxylation` | uni-upper | `malonic-and-acetoacetic-ester-synthesis` |
| Predicting Dieckmann condensations | `dieckmann-condensation` | uni-upper | `claisen-condensation`, `lactones-and-lactams` |
| Alkylating ketones through enamines | `stork-enamine-alkylation` | uni-upper | `imines-and-enamines`, `enolate-alkylation` |
| Making primary amines by Gabriel synthesis | `gabriel-synthesis` | uni-upper | `amine-synthesis`, `amides-and-nitriles` |
| Converting amides to amines by rearrangement | `amide-rearrangements` | uni-upper | `amine-synthesis`, `amides-and-nitriles` |
| Replacing diazonium groups with Sandmeyer reactions | `sandmeyer-reactions` | uni-upper | `diazonium-salts` |
| Connecting carbonyl compounds on a reaction map | `carbonyl-reaction-maps` | uni-upper | `reducing-acid-derivatives`, `conjugate-addition`, `amine-synthesis` |

### Biomolecules and polymers

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Drawing carbohydrate structures | `carbohydrate-structures` | uni-upper | `hydrates-and-acetals`, `org1.fischer-projections` |
| Forming glycosidic bonds | `glycosidic-bonds` | uni-upper | `carbohydrate-structures` |
| Describing amino acids and peptide bonds | `amino-acids-and-peptides` | uni-upper | `amides-and-nitriles`, `amine-basicity` |
| Planning peptide synthesis | `peptide-synthesis` | uni-upper | `amino-acids-and-peptides`, `protecting-groups` |
| Describing lipids and saponification | `lipids-and-saponification` | uni-upper | `esters-and-fischer-esterification` |
| Describing nucleotide structure | `nucleic-acid-structure` | uni-upper | `carbohydrate-structures`, `aromatic-ions-and-heterocycles` |
| Comparing chain-growth and step-growth polymerization | `polymerization-mechanisms` | uni-upper | `hs1.polymers-intro`, `org1.radical-addition-of-hbr`, `esters-and-fischer-esterification` |

### Synthesis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing multistep syntheses with carbonyl chemistry | `multistep-carbonyl-synthesis` | uni-upper | `crossed-aldol-reactions`, `organometallics-with-derivatives`, `protecting-groups` |
| Planning retrosyntheses of complex targets | `complex-retrosynthesis` | uni-upper | `multistep-carbonyl-synthesis`, `aromatic-synthesis-planning`, `malonic-and-acetoacetic-ester-synthesis` |

## chem.analytical: 52 topics

### Data and statistics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying systematic and random errors | `analytical-errors` | uni-upper | `hs1.percent-error-in-lab`, `stats.standard-deviation-calc` |
| Propagating uncertainty through calculations | `error-propagation` | uni-upper | `analytical-errors`, `hs1.measurement-uncertainty` |
| Reporting confidence intervals for replicate measurements | `confidence-intervals-for-measurements` | uni-upper | `analytical-errors`, `stats.ci-mean-t` |
| Comparing analytical results with t tests | `comparing-means-t-tests` | uni-upper | `confidence-intervals-for-measurements`, `stats.two-mean-t-test` |
| Comparing precision with the F test | `f-test-for-precision` | uni-upper | `comparing-means-t-tests` |
| Rejecting outliers with Grubbs or Q tests | `outlier-tests` | uni-upper | `analytical-errors`, `stats.outlier-rule` |
| Building calibration curves by least squares | `calibration-curves` | uni-upper | `stats.least-squares-regression`, `hs2.beer-lambert-law` |
| Finding uncertainty of a result from a calibration curve | `calibration-uncertainty` | uni-upper | `calibration-curves`, `error-propagation` |
| Finding detection and quantitation limits | `detection-limits` | uni-upper | `calibration-curves` |
| Analyzing samples by standard addition | `standard-addition` | uni-upper | `calibration-curves` |
| Using internal standards | `internal-standards` | uni-upper | `calibration-curves` |
| Validating analytical methods | `method-validation` | uni-upper | `detection-limits`, `comparing-means-t-tests` |
| Planning sampling and sample preparation | `sampling-and-sample-preparation` | uni-upper | `analytical-errors` |

### Equilibrium for analysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating ionic strength | `ionic-strength` | uni-upper | `hs1.ion-concentrations` |
| Finding activity coefficients with the extended Debye-Huckel equation | `activity-coefficients` | uni-upper | `ionic-strength`, `hs2.equilibrium-expressions` |
| Solving equilibria with charge and mass balances | `systematic-equilibrium-treatment` | uni-upper | `activity-coefficients`, `gen2.simultaneous-equilibria` |
| Calculating results of gravimetric analysis | `gravimetric-analysis` | uni-upper | `hs1.mass-to-mass-stoichiometry`, `gen2.selective-precipitation` |
| Analyzing precipitation titrations | `precipitation-titrations` | uni-upper | `hs2.ksp-and-solubility`, `gen2.titration-curve-calculations` |

### Acid-base and complexometric titrations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing titrations of acid mixtures | `titration-of-mixtures` | uni-upper | `gen2.polyprotic-titrations`, `systematic-equilibrium-treatment` |
| Locating end points with derivative and Gran plots | `end-point-detection` | uni-upper | `gen2.titration-curve-calculations` |
| Finding nitrogen by Kjeldahl analysis | `kjeldahl-analysis` | uni-upper | `gen1.back-titration` |
| Analyzing EDTA titrations | `edta-titrations` | uni-upper | `gen2.complex-ion-formation`, `gen2.fractional-composition` |
| Using conditional formation constants | `conditional-formation-constants` | uni-upper | `edta-titrations` |
| Choosing metal ion indicators | `metal-ion-indicators` | uni-upper | `edta-titrations` |
| Using auxiliary complexing agents | `auxiliary-complexing-agents` | uni-upper | `conditional-formation-constants` |

### Redox titrations and electroanalysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating redox titration curves | `redox-titration-curves` | uni-upper | `gen2.nernst-equation`, `hs2.redox-titrations` |
| Analyzing iodometric and permanganate titrations | `iodometry-and-permanganate` | uni-upper | `redox-titration-curves` |
| Describing reference electrodes | `reference-electrodes` | uni-upper | `gen2.nernst-equation` |
| Measuring concentrations with indicator electrodes | `indicator-electrodes` | uni-upper | `reference-electrodes` |
| Using ion-selective electrodes | `ion-selective-electrodes` | uni-upper | `indicator-electrodes`, `activity-coefficients` |
| Explaining the glass pH electrode | `glass-ph-electrode` | uni-upper | `ion-selective-electrodes` |
| Analyzing samples by electrogravimetry and coulometry | `electrogravimetry-and-coulometry` | uni-upper | `hs2.electrolysis-calculations`, `reference-electrodes` |
| Interpreting voltammograms | `voltammetry` | uni-upper | `indicator-electrodes` |

### Spectroscopic methods

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing spectrophotometer components | `spectrophotometer-components` | uni-upper | `hs2.beer-lambert-law` |
| Explaining deviations from Beer's law | `beer-law-deviations` | uni-upper | `spectrophotometer-components`, `calibration-curves` |
| Analyzing mixtures by spectrophotometry | `spectrophotometric-mixture-analysis` | uni-upper | `beer-law-deviations` |
| Following titrations by absorbance | `spectrophotometric-titrations` | uni-upper | `beer-law-deviations`, `edta-titrations` |
| Analyzing samples by fluorescence | `fluorescence-analysis` | uni-upper | `spectrophotometer-components`, `hs1.emission-and-absorption` |
| Analyzing metals by atomic absorption | `atomic-absorption` | uni-upper | `spectrophotometer-components`, `hs1.flame-tests` |
| Analyzing metals by atomic emission and plasma methods | `atomic-emission-and-plasma` | uni-upper | `atomic-absorption` |
| Correcting interferences in atomic spectroscopy | `atomic-spectroscopy-interferences` | uni-upper | `atomic-emission-and-plasma`, `standard-addition` |

### Separations and mass spectrometry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating extraction efficiency | `solvent-extraction` | uni-upper | `hs2.separation-by-intermolecular-forces`, `hs2.equilibrium-expressions` |
| Controlling extraction with pH | `ph-controlled-extraction` | uni-upper | `solvent-extraction`, `gen2.fractional-composition` |
| Describing retention and partition in chromatography | `chromatography-principles` | uni-upper | `solvent-extraction` |
| Finding plate number and resolution | `plate-theory-and-resolution` | uni-upper | `chromatography-principles` |
| Optimizing flow with the van Deemter equation | `van-deemter-equation` | uni-upper | `plate-theory-and-resolution` |
| Describing gas chromatography | `gas-chromatography` | uni-upper | `plate-theory-and-resolution` |
| Describing high-performance liquid chromatography | `hplc` | uni-upper | `plate-theory-and-resolution` |
| Describing ion-exchange and size-exclusion chromatography | `ion-exchange-and-size-exclusion` | uni-upper | `hplc` |
| Describing capillary electrophoresis | `capillary-electrophoresis` | uni-upper | `chromatography-principles` |
| Describing ionization methods and mass analyzers | `mass-spectrometer-instrumentation` | uni-upper | `hs1.mass-spectra-of-elements` |
| Interpreting GC-MS and LC-MS data | `hyphenated-methods` | uni-upper | `mass-spectrometer-instrumentation`, `gas-chromatography`, `hplc` |

## chem.inorganic: 49 topics

### Symmetry and group theory

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Identifying symmetry elements and operations | `symmetry-elements` | uni-upper | `gen1.expanded-octet-shapes` |
| Assigning point groups | `point-groups` | uni-upper | `symmetry-elements` |
| Predicting chirality and polarity from point groups | `symmetry-chirality-and-polarity` | uni-upper | `point-groups`, `org1.chirality` |
| Representing symmetry operations with matrices | `symmetry-operation-matrices` | uni-upper | `point-groups`, `linalg.matrix-product-three-views` |
| Reading character tables | `character-tables` | uni-upper | `symmetry-operation-matrices` |
| Reducing representations | `reducing-representations` | uni-upper | `character-tables` |
| Finding IR and Raman active modes by symmetry | `vibrational-modes-by-symmetry` | uni-upper | `reducing-representations` |
| Building symmetry-adapted linear combinations | `salc-construction` | uni-upper | `reducing-representations` |

### Bonding and acid-base models

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Building molecular orbitals of polyatomic molecules | `polyatomic-molecular-orbitals` | uni-upper | `salc-construction`, `gen1.heteronuclear-diatomic-orbitals` |
| Predicting reactions with hard and soft acid-base theory | `hsab-theory` | uni-upper | `hs2.lewis-acids-and-bases`, `gen2.complex-ion-formation` |
| Predicting oxoacid strength | `oxoacid-strength` | uni-upper | `hs2.acid-strength-and-structure` |
| Describing acid-base chemistry in nonaqueous solvents and superacids | `nonaqueous-acid-base-chemistry` | uni-upper | `hsab-theory`, `oxoacid-strength` |

### Solid state

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Predicting ionic structures from radius ratios | `radius-ratio-rules` | uni-upper | `gen1.ionic-crystal-structures`, `hs1.ionic-radius-trend` |
| Estimating lattice energies with Born-Lande and Kapustinskii equations | `lattice-energy-equations` | uni-upper | `gen1.born-haber-cycle` |
| Describing defects and nonstoichiometry in crystals | `crystal-defects` | uni-upper | `radius-ratio-rules` |

### Main group chemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying hydrides | `hydrides` | uni-upper | `gen2.periodic-properties-of-oxides` |
| Describing boranes with Wade's rules | `boranes-and-wades-rules` | uni-upper | `hydrides`, `polyatomic-molecular-orbitals` |
| Describing chemistry of carbon to lead | `group-14-chemistry` | uni-upper | `gen2.periodic-properties-of-oxides` |
| Describing chemistry of nitrogen and phosphorus | `group-15-chemistry` | uni-upper | `group-14-chemistry` |
| Describing chemistry of oxygen and sulfur | `group-16-chemistry` | uni-upper | `group-15-chemistry` |
| Describing interhalogens and halogen oxoanions | `interhalogens-and-oxoanions` | uni-upper | `gen2.halogen-and-noble-gas-chemistry` |
| Predicting structures of noble gas compounds | `noble-gas-compounds` | uni-upper | `interhalogens-and-oxoanions`, `gen1.expanded-octet-shapes` |
| Using Latimer and Frost diagrams | `latimer-and-frost-diagrams` | uni-upper | `gen2.nernst-equation`, `hs2.oxidation-numbers` |

### Coordination chemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Predicting coordination numbers and geometries | `coordination-geometries` | uni-upper | `gen2.coordination-compound-structure`, `point-groups` |
| Identifying all isomers of a complex | `complete-isomer-enumeration` | uni-upper | `gen2.isomers-of-complexes`, `symmetry-chirality-and-polarity` |
| Finding crystal field stabilization energy in octahedral complexes | `octahedral-crystal-field-energy` | uni-upper | `gen2.high-and-low-spin` |
| Splitting d orbitals in tetrahedral and square planar fields | `tetrahedral-and-square-planar-fields` | uni-upper | `octahedral-crystal-field-energy` |
| Using the spectrochemical series | `spectrochemical-series` | uni-upper | `octahedral-crystal-field-energy` |
| Predicting Jahn-Teller distortions | `jahn-teller-distortion` | uni-upper | `tetrahedral-and-square-planar-fields` |
| Building molecular orbital diagrams of complexes | `ligand-field-orbitals` | uni-upper | `polyatomic-molecular-orbitals`, `octahedral-crystal-field-energy` |
| Explaining pi donor and pi acceptor ligands | `pi-donor-and-acceptor-ligands` | uni-upper | `ligand-field-orbitals`, `spectrochemical-series` |
| Calculating spin-only magnetic moments | `magnetic-moments-of-complexes` | uni-upper | `gen2.high-and-low-spin` |
| Finding term symbols of d-electron ions | `d-electron-term-symbols` | uni-upper | `octahedral-crystal-field-energy`, `hs1.quantum-numbers` |
| Interpreting electronic spectra with Tanabe-Sugano diagrams | `tanabe-sugano-spectra` | uni-upper | `d-electron-term-symbols`, `spectrochemical-series` |
| Identifying charge transfer transitions | `charge-transfer-bands` | uni-upper | `tanabe-sugano-spectra` |
| Explaining stability trends of complexes | `complex-stability-trends` | uni-upper | `gen2.chelate-effect`, `octahedral-crystal-field-energy` |

### Reactions of complexes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying ligand substitution mechanisms | `ligand-substitution-mechanisms` | uni-upper | `gen2.coordination-compound-structure`, `gen2.mechanisms-with-fast-equilibrium` |
| Predicting inert and labile complexes | `inert-and-labile-complexes` | uni-upper | `ligand-substitution-mechanisms`, `octahedral-crystal-field-energy` |
| Using the trans effect in synthesis | `trans-effect` | uni-upper | `ligand-substitution-mechanisms`, `tetrahedral-and-square-planar-fields` |
| Comparing inner-sphere and outer-sphere electron transfer | `electron-transfer-mechanisms` | uni-upper | `ligand-substitution-mechanisms`, `latimer-and-frost-diagrams` |

### Organometallic chemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Counting electrons with the 18-electron rule | `eighteen-electron-rule` | uni-upper | `coordination-geometries`, `hs2.oxidation-numbers` |
| Describing metal carbonyl bonding and spectra | `metal-carbonyls` | uni-upper | `eighteen-electron-rule`, `pi-donor-and-acceptor-ligands`, `vibrational-modes-by-symmetry` |
| Describing metallocenes and pi ligands | `metallocenes-and-pi-ligands` | uni-upper | `eighteen-electron-rule`, `gen1.delocalized-pi-bonding` |
| Recognizing oxidative addition and reductive elimination | `oxidative-addition-and-reductive-elimination` | uni-upper | `eighteen-electron-rule` |
| Recognizing migratory insertion and beta elimination | `migratory-insertion` | uni-upper | `oxidative-addition-and-reductive-elimination` |
| Tracing organometallic catalytic cycles | `catalytic-cycles` | uni-upper | `migratory-insertion`, `gen2.homogeneous-and-heterogeneous-catalysis` |

### Further topics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing lanthanide and actinide chemistry | `f-block-chemistry` | uni-upper | `hs1.electron-configurations`, `gen2.transition-metal-properties` |
| Describing metal ions in biological systems | `bioinorganic-chemistry` | uni-upper | `complex-stability-trends`, `electron-transfer-mechanisms` |
| Describing inorganic materials and nanomaterials | `inorganic-materials` | uni-upper | `crystal-defects` |

## chem.pchem1: 47 topics

### Real gases and thermochemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the compressibility factor | `compressibility-factor` | uni-upper | `gen1.real-gases` |
| Using the virial equation of state | `virial-equation` | uni-upper | `compressibility-factor`, `calc2.power-series-intro` |
| Using reduced variables and corresponding states | `corresponding-states` | uni-upper | `compressibility-factor`, `gen1.phase-diagrams` |
| Finding reaction enthalpy at other temperatures | `kirchhoff-law` | uni-upper | `gen1.thermochemical-cycles`, `waves-thermo-optics.heat-capacity-with-calculus` |
| Finding reaction entropy and Gibbs energy at other temperatures | `reaction-entropy-at-other-temperatures` | uni-upper | `kirchhoff-law`, `waves-thermo-optics.entropy-in-heating-and-melting` |

### Chemical potential and equilibrium

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing chemical potentials of ideal gases with standard states | `chemical-potential-of-gases` | uni-upper | `stat-thermal.pressure-and-chemical-potential`, `gen2.gibbs-energy-nonstandard` |
| Using fugacity for real gases | `fugacity` | uni-upper | `chemical-potential-of-gases`, `virial-equation` |
| Finding Gibbs energy against extent of reaction | `gibbs-energy-and-extent-of-reaction` | uni-upper | `chemical-potential-of-gases`, `gen2.gibbs-energy-and-k` |
| Calculating K from thermodynamic tables | `k-from-thermodynamic-tables` | uni-upper | `gibbs-energy-and-extent-of-reaction`, `reaction-entropy-at-other-temperatures` |
| Deriving the Gibbs-Helmholtz and van't Hoff equations | `gibbs-helmholtz-and-vant-hoff` | uni-upper | `k-from-thermodynamic-tables`, `stat-thermal.maxwell-relations`, `gen2.vant-hoff-equation` |
| Finding how pressure and inert gases affect equilibrium | `pressure-and-inert-gas-effects` | uni-upper | `k-from-thermodynamic-tables`, `gen2.equilibrium-with-changing-volume` |

### Phase equilibria

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the Gibbs phase rule | `gibbs-phase-rule` | uni-upper | `stat-thermal.phase-equilibrium`, `gen1.phase-diagrams` |
| Finding how pressure shifts melting points | `pressure-and-melting-point` | uni-upper | `stat-thermal.clausius-clapeyron`, `gibbs-phase-rule` |
| Reading binary liquid-vapour phase diagrams | `binary-liquid-vapor-diagrams` | uni-upper | `gen1.ideal-solutions-and-distillation`, `gibbs-phase-rule` |
| Finding phase amounts with the lever rule | `lever-rule` | uni-upper | `binary-liquid-vapor-diagrams` |
| Reading solid-liquid phase diagrams with eutectics | `solid-liquid-diagrams` | uni-upper | `lever-rule` |
| Reading diagrams of partially miscible liquids | `partially-miscible-liquids` | uni-upper | `lever-rule` |

### Solutions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using partial molar quantities | `partial-molar-quantities` | uni-upper | `stat-thermal.gibbs-duhem`, `gen1.molality-and-mole-fraction` |
| Writing chemical potentials of solution components | `chemical-potential-in-solutions` | uni-upper | `partial-molar-quantities`, `stat-thermal.ideal-mixtures` |
| Using activities and standard states for real solutions | `real-solutions-and-activity` | uni-upper | `chemical-potential-in-solutions`, `gen1.henrys-law`, `analytical.activity-coefficients` |
| Using excess thermodynamic functions | `excess-functions` | uni-upper | `real-solutions-and-activity` |
| Explaining azeotropes and fractional distillation | `azeotropes` | uni-upper | `real-solutions-and-activity`, `lever-rule` |
| Deriving colligative properties from chemical potential | `colligative-properties-derived` | uni-upper | `chemical-potential-in-solutions`, `gen1.boiling-and-freezing-point-changes` |

### Electrolytes and electrochemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving the Debye-Huckel limiting law | `debye-huckel-derivation` | uni-upper | `real-solutions-and-activity`, `em.potential-of-point-charges-derivation` |
| Using electrochemical potentials | `electrochemical-potential` | uni-upper | `chemical-potential-in-solutions`, `gen2.nernst-equation` |
| Finding entropy and enthalpy from cell potential against temperature | `cell-thermodynamics-from-temperature` | uni-upper | `gen2.gibbs-energy-and-cell-potential`, `gibbs-helmholtz-and-vant-hoff` |
| Finding standard potentials by extrapolation | `standard-potentials-by-extrapolation` | uni-upper | `debye-huckel-derivation`, `electrochemical-potential` |
| Describing conductivity and ion mobility | `ion-mobility-and-conductivity` | uni-upper | `debye-huckel-derivation`, `stat-thermal.transport-coefficients` |

### Surfaces

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Relating surface tension to surface Gibbs energy | `surface-gibbs-energy` | uni-upper | `waves-thermo-optics.surface-tension`, `stat-thermal.free-energies` |
| Finding vapour pressure over curved surfaces | `curved-surface-vapor-pressure` | uni-upper | `surface-gibbs-energy`, `gen1.vapor-pressure-and-temperature` |
| Deriving the Langmuir adsorption isotherm | `langmuir-isotherm` | uni-upper | `surface-gibbs-energy`, `hs2.dynamic-equilibrium` |
| Using the BET isotherm for surface area | `bet-isotherm` | uni-upper | `langmuir-isotherm` |

### Kinetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing rate laws as differential equations | `rate-laws-as-differential-equations` | uni-upper | `gen2.pseudo-first-order`, `calc2.separable-equations` |
| Deriving integrated rate laws | `integrated-rate-law-derivations` | uni-upper | `rate-laws-as-differential-equations` |
| Solving kinetics of reversible reactions | `reversible-reaction-kinetics` | uni-upper | `integrated-rate-law-derivations`, `hs2.dynamic-equilibrium` |
| Solving kinetics of parallel reactions | `parallel-reactions` | uni-upper | `integrated-rate-law-derivations` |
| Solving kinetics of consecutive reactions | `consecutive-reactions` | uni-upper | `integrated-rate-law-derivations`, `diffeq.linear-first-order` |
| Applying the steady-state approximation rigorously | `steady-state-kinetics` | uni-upper | `consecutive-reactions`, `gen2.steady-state-intermediates` |
| Explaining unimolecular reactions with the Lindemann mechanism | `lindemann-mechanism` | uni-upper | `steady-state-kinetics` |
| Deriving rate laws of chain reactions | `chain-reaction-kinetics` | uni-upper | `steady-state-kinetics` |
| Deriving the Michaelis-Menten equation | `michaelis-menten` | uni-upper | `steady-state-kinetics`, `gen2.enzyme-kinetics-intro` |
| Analyzing enzyme inhibition | `enzyme-inhibition` | uni-upper | `michaelis-menten` |
| Calculating rate constants with collision theory | `collision-theory-rate-constants` | uni-upper | `gen2.orientation-factor`, `waves-thermo-optics.mean-free-path`, `waves-thermo-optics.average-and-rms-speeds` |
| Finding rates of diffusion-controlled reactions | `diffusion-controlled-reactions` | uni-upper | `collision-theory-rate-constants`, `stat-thermal.diffusion-equation-from-random-walks` |
| Finding rate constants by relaxation methods | `relaxation-kinetics` | uni-upper | `reversible-reaction-kinetics` |
| Analyzing surface-catalyzed reaction rates | `surface-catalysis-kinetics` | uni-upper | `langmuir-isotherm`, `steady-state-kinetics` |
| Interpreting curved Arrhenius plots | `curved-arrhenius-plots` | uni-upper | `gen2.activation-energy-from-data`, `collision-theory-rate-constants` |

## chem.pchem2: 49 topics

### Molecular quantum mechanics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Applying the Born-Oppenheimer approximation | `born-oppenheimer-approximation` | uni-upper | `quantum.hydrogen-molecule-ion`, `quantum.two-particle-wave-functions` |
| Evaluating overlap, Coulomb and exchange integrals | `lcao-integrals` | uni-upper | `quantum.hydrogen-molecule-ion` |
| Setting up secular determinants | `secular-determinants` | uni-upper | `lcao-integrals`, `linalg.determinant-cofactors` |
| Comparing molecular orbital and valence bond descriptions of hydrogen | `hydrogen-molecule-mo-and-vb` | uni-upper | `lcao-integrals`, `quantum.symmetrization`, `gen1.valence-bond-theory` |
| Building diatomic molecular orbitals from atomic orbitals | `diatomic-orbitals-from-quantum` | uni-upper | `secular-determinants`, `gen1.heteronuclear-diatomic-orbitals` |
| Assigning atomic term symbols | `atomic-term-symbols` | uni-upper | `quantum.addition-of-angular-momentum`, `quantum.shell-structure-from-quantum` |
| Assigning molecular term symbols | `molecular-term-symbols` | uni-upper | `diatomic-orbitals-from-quantum`, `atomic-term-symbols` |
| Building hybrid orbitals as combinations of atomic orbitals | `hybrid-orbitals-from-quantum` | uni-upper | `lcao-integrals`, `gen1.hybridization` |
| Finding pi energies with Huckel theory | `huckel-theory` | uni-upper | `secular-determinants`, `linalg.find-eigenvalues` |
| Applying Huckel theory to rings and chains | `huckel-rings-and-chains` | uni-upper | `huckel-theory`, `org2.aromaticity-rules` |
| Describing the Hartree-Fock method | `hartree-fock-method` | uni-upper | `quantum.helium-atom`, `quantum.variational-principle` |
| Choosing basis sets for calculations | `basis-sets` | uni-upper | `hartree-fock-method` |
| Describing electron correlation and density functional methods | `correlation-and-density-functionals` | uni-upper | `hartree-fock-method` |
| Interpreting results of quantum chemistry calculations | `computational-chemistry-results` | uni-upper | `basis-sets`, `correlation-and-density-functionals` |

### Rotational and vibrational spectroscopy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using rotational selection rules | `rotational-selection-rules` | uni-upper | `quantum.rigid-rotor`, `quantum.selection-rules-derived`, `modern.molecular-rotation-spectra` |
| Correcting rotational lines for centrifugal distortion | `centrifugal-distortion` | uni-upper | `rotational-selection-rules` |
| Using the Morse potential for anharmonic vibrations | `morse-oscillator` | uni-upper | `modern.molecular-vibration-spectra`, `quantum.oscillator-matrix-elements` |
| Using vibrational selection rules | `vibrational-selection-rules` | uni-upper | `quantum.oscillator-matrix-elements`, `quantum.selection-rules-derived` |
| Interpreting vibration-rotation spectra | `vibration-rotation-spectra` | uni-upper | `vibrational-selection-rules`, `rotational-selection-rules` |
| Predicting isotope shifts in spectra | `isotope-shifts-in-spectra` | uni-upper | `vibration-rotation-spectra` |
| Counting normal modes of polyatomic molecules | `polyatomic-normal-modes` | uni-upper | `vibrational-selection-rules` |
| Interpreting Raman spectra | `raman-spectroscopy` | uni-upper | `polyatomic-normal-modes` |
| Explaining intensity alternation from nuclear spin statistics | `nuclear-spin-statistics` | uni-upper | `vibration-rotation-spectra`, `quantum.symmetrization` |

### Electronic spectroscopy and photochemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Applying the Franck-Condon principle | `franck-condon-principle` | uni-upper | `morse-oscillator`, `quantum.absorption-and-stimulated-emission` |
| Using Jablonski diagrams for fluorescence and phosphorescence | `jablonski-diagrams` | uni-upper | `franck-condon-principle`, `quantum.spontaneous-emission-and-lifetimes` |
| Predicting electronic spectra of conjugated molecules | `conjugated-molecule-spectra` | uni-upper | `huckel-rings-and-chains`, `org2.uv-vis-of-conjugated-systems` |
| Calculating quantum yields | `quantum-yield` | uni-upper | `jablonski-diagrams` |
| Analyzing photochemical kinetics and quenching | `photochemical-kinetics` | uni-upper | `quantum-yield`, `pchem1.steady-state-kinetics` |
| Describing lasers used in chemistry | `lasers-in-chemistry` | uni-upper | `jablonski-diagrams`, `modern.laser-principles` |
| Interpreting molecular photoelectron spectra | `molecular-photoelectron-spectra` | uni-upper | `diatomic-orbitals-from-quantum`, `hs2.photoelectron-spectroscopy` |

### Magnetic resonance

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining NMR with nuclear spin in a field | `nmr-theory` | uni-upper | `quantum.magnetic-resonance`, `org1.proton-nmr-shifts` |
| Explaining chemical shifts as shielding | `chemical-shift-shielding` | uni-upper | `nmr-theory` |
| Explaining spin-spin coupling | `spin-coupling-theory` | uni-upper | `nmr-theory`, `quantum.addition-of-angular-momentum` |
| Describing NMR relaxation times | `nmr-relaxation` | uni-upper | `nmr-theory` |
| Describing pulsed Fourier transform NMR | `pulsed-fourier-nmr` | uni-upper | `nmr-theory`, `pde.fourier-transform-definition` |
| Interpreting EPR spectra | `epr-spectroscopy` | uni-upper | `spin-coupling-theory` |

### Statistical thermodynamics of chemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using symmetry numbers in rotational partition functions | `rotational-partition-symmetry-numbers` | uni-upper | `stat-thermal.molecular-heat-capacities`, `rotational-selection-rules` |
| Finding electronic partition functions | `electronic-partition-function` | uni-upper | `stat-thermal.partition-function`, `atomic-term-symbols` |
| Combining partition functions of a molecule | `molecular-partition-function` | uni-upper | `rotational-partition-symmetry-numbers`, `electronic-partition-function`, `stat-thermal.ideal-gas-partition-function` |
| Finding entropy and heat capacity of real molecules from partition functions | `thermodynamic-functions-of-real-gases` | uni-upper | `molecular-partition-function`, `stat-thermal.free-energy-from-partition-function` |
| Calculating equilibrium constants from partition functions | `equilibrium-constants-from-partition-functions` | uni-upper | `molecular-partition-function`, `stat-thermal.law-of-mass-action` |
| Predicting isotope exchange equilibria | `isotope-exchange-equilibria` | uni-upper | `equilibrium-constants-from-partition-functions`, `isotope-shifts-in-spectra` |
| Explaining residual entropy of crystals | `residual-entropy` | uni-upper | `thermodynamic-functions-of-real-gases`, `stat-thermal.third-law` |

### Reaction dynamics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading potential energy surfaces | `potential-energy-surfaces` | uni-upper | `born-oppenheimer-approximation`, `pchem1.collision-theory-rate-constants` |
| Deriving rate constants with transition state theory | `transition-state-theory` | uni-upper | `potential-energy-surfaces`, `equilibrium-constants-from-partition-functions` |
| Finding activation enthalpy and entropy with the Eyring equation | `eyring-activation-parameters` | uni-upper | `transition-state-theory` |
| Predicting kinetic isotope effects | `kinetic-isotope-effects` | uni-upper | `transition-state-theory`, `isotope-shifts-in-spectra` |
| Describing molecular beam experiments | `molecular-beam-dynamics` | uni-upper | `potential-energy-surfaces` |
| Using Marcus theory for electron transfer | `marcus-theory` | uni-upper | `transition-state-theory` |
