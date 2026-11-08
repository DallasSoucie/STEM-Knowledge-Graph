# Topic lists: degree-review additions (Tier 1 and Tier 2)

This draft is for approval. It covers the 15 new courses proposed in `2026-11-08-degree-coverage-review.md`: 695 topics against a combined budget of 775.

**How to read the Needs column.** A plain slug is a topic earlier in the same course. A full ID (`physics.quantum.fermi-golden-rule`) is a topic in another course. Every Needs entry has been checked:

- each one exists in the graph or in this plan;
- each same-course need comes earlier in the list;
- each cross-course need is in the proposed follows closure, so `learner-walk` will pass.

Knowledge points, weights and encompassed lists are written at build time, the same way as for engineering.

## Decisions made while drafting

- **Ethics stays out of scope.** It is FE content but not quantitative STEM, as the review recommended.
- **`chem.pchem2` is unchanged.** It still follows `physics.quantum`. That decision was left open in the review; nothing in this plan depends on it.
- **Surveying takes over two topics from transportation.** `engr.transportation.survey-leveling` and `engr.transportation.cross-sections-and-earthwork` move to `engr.surveying` through `rename-id`, which keeps every reference and records the move in `id-history.yaml`. Their level becomes uni-lower, and `engr.transportation` gains `engr.surveying` in its follows. Highway curves (horizontal, spiral and vertical) stay in transportation, because they are geometric design rather than surveying.
- **Construction builds on the scheduling that `engr.economics` already homes.** Critical path, float and crashing, earned value and cost estimation all live there. Construction adds precedence diagrams, PERT, resource leveling, linear scheduling and forecasting on top.
- **Number theory starts above what `math.discrete` and `math.proofs` already home.** Those courses cover the Euclidean algorithm, the Chinese remainder theorem, Fermat's little theorem, RSA, the fundamental theorem of arithmetic and Bezout's identity.
- **Topology builds on the metric-space topology in `math.analysis`.** That includes open and closed sets, compactness, connectedness and continuity through open sets. Topology follows `math.abstract` because of the fundamental group.
- **Physics courses don't repeat `physics.modern` or `physics.quantum`.** Already homed there are the free electron model, bands, doping, p-n junctions, the semi-empirical mass formula, the decay law, the quark model, Fermi's golden rule and Bloch bands in one dimension. The new courses deepen these topics and cite them.
- **Plant biology homes university-level photosynthesis.** This includes the Z-scheme, photophosphorylation, Calvin cycle regulation, Rubisco, and C4 and CAM. It fills the photosynthesis gap that the review found in `bio.biochem`.
- **Biology courses don't repeat their neighbours.** Each course below cites what is already homed elsewhere instead of reteaching it:

  | New course | Content already homed elsewhere |
  |---|---|
  | Molecular biology | sequencing, editing and transgenics (`bio.genetics`); transcription factors, splicing and chromatin (`bio.cell-mol`); polymerase and ribosome biochemistry (`bio.biochem`) |
  | Immunology | antibody structure, vaccine types and lymphocyte activation (`bio.micro`) |
  | Developmental biology | axon guidance (`bio.neuro`) |

## Manifest changes

| Course | Follows | Levels | Topics | Budget |
|---|---|---|---|---|
| math.number-theory | `math.proofs`, `math.discrete` | uni-upper | 68 | 75 |
| math.topology | `math.analysis`, `math.abstract` | uni-upper | 71 | 80 |
| math.geometry | `math.proofs`, `math.linalg` | uni-upper | 59 | 65 |
| math.optimization | `math.numerical`, `math.calc3`, `math.discrete` | uni-upper | 50 | 55 |
| physics.solid-state | `physics.quantum`, `physics.stat-thermal`, `physics.em-theory` | uni-upper | 61 | 65 |
| physics.nuclear-particle | `physics.quantum`, `physics.stat-thermal`, `math.probstat` | uni-upper | 51 | 55 |
| physics.optics | `physics.em-theory`, `physics.quantum`, `physics.stat-thermal` | uni-upper | 46 | 50 |
| bio.molecular-biology | `bio.genetics`, `bio.biochem`, `bio.cell-mol` | uni-upper | 44 | 50 |
| bio.immunology | `bio.cell-mol`, `bio.micro`, `bio.genetics` | uni-upper | 40 | 45 |
| bio.developmental | `bio.cell-mol`, `bio.genetics`, `bio.intro2` | uni-upper | 34 | 40 |
| bio.plant | `bio.biochem`, `bio.cell-mol`, `bio.intro2` | uni-upper | 40 | 45 |
| engr.surveying | `math.precalc`, `math.stats` | uni-lower | 31 | 35 |
| engr.construction | `engr.economics`, `engr.surveying`, `engr.soil-mechanics`, `math.probstat` | uni-upper | 30 | 35 |
| engr.programming-languages | `engr.theory` | uni-upper | 40 | 45 |
| engr.process-design-safety | `engr.reactors`, `engr.separations`, `engr.economics` | uni-upper | 30 | 35 |
| **Total** | | | **695** | **775** |

Other manifest and test changes:

- `engr.transportation` adds `engr.surveying` to its follows.
- The catalog goes from 110 courses to 125.
- The total budget goes from 9,350 to 10,125.
- `tests/test_manifest.py` and the `KG_PROMPT.md` catalog get updated to match.

Every course comes in under its budget, at the same grain as the courses already built. University math courses elsewhere in the catalog run 110 to 190 topics because they were built at a finer grain. If you want the new math courses at that grain, approve the structure first and I'll split them before building.

## Overlap notes

The duplicate scan against the existing graph found these overlaps. Each one is either renamed to a distinct skill or intentional, because the course can't depend on the other copy:

- **Kept as overlaps across disciplines.** `math.optimization.lp-formulation` and `max-flow-min-cut` overlap with `engr.algorithms.linear-programming-intro` and `engr.algorithms.max-flow-min-cut`. `physics.solid-state.drift-diffusion` and `diode-equation` overlap with the matching `engr.electronics` topics.
  - Math and physics must not depend on engineering courses.
  - The physics and optimization versions are derivations and proofs; the engineering versions are applications.
  - `find-duplicates` may flag these pairs.
- **Dropped:** `axon-guidance` (homed in `bio.neuro`), `contraction-mapping` (homed in `math.analysis`) and the augmenting-path max-flow topic (homed in `engr.algorithms`).
- **Renamed to the deeper skill, citing the earlier copy as a need.**
  - Water potential, the light reactions and the Calvin cycle are high school copies, now cited from `bio.hs2`.
  - Pythagorean triples are cited from `math.geom`.
  - Cross sections are cited from `physics.classical`.
  - T cell activation is cited from `bio.micro`.
- **Renamed to a distinct context:**
  - the cross ratio of collinear points (projective geometry), against `math.complex`;
  - multiplicative order modulo n, against `math.abstract`;
  - nitrogen assimilation in plants, against `bio.micro.nitrogen-fixation`;
  - atom economy and E-factors, against `chem.hs1` green chemistry.

## Survey

Sources are indexed in `refs/uni_syllabi/SOURCES.md`. 36 syllabi were saved under these new folders, with at least one per course:

- `phys-solid-state`, `phys-nuclear`, `phys-optics`;
- `math-number-theory`, `math-topology`, `math-geometry`, `math-optimization`;
- `bio-molecular`, `bio-immunology`, `bio-developmental`, `bio-plant`;
- `eng-surveying`, `eng-construction`, `eng-proglang`, `eng-process-safety`.

The topic lists are original. They follow the common ground of those syllabi, the FE Civil sections on surveying and construction, the FE Chemical section on safety, and the ABET CAC requirement for programming languages. No list follows any one source's order.

## math.number-theory: 68 topics

Follows `math.proofs`, `math.discrete`. Level uni-upper.


### Divisibility and arithmetic functions

| Topic | Slug | Needs |
|---|---|---|
| Proving divisibility facts with linear combinations | `divisibility-linear-combinations` | `math.proofs.bezout-proofs` |
| Solving linear Diophantine equations | `linear-diophantine` | `divisibility-linear-combinations`, `math.discrete.euclidean-algorithm` |
| Finding nonnegative solutions and the coin problem | `nonnegative-diophantine` | `linear-diophantine` |
| Counting and summing divisors | `divisor-functions` | `math.discrete.primes-fundamental-theorem` |
| Finding perfect numbers and Mersenne primes | `perfect-numbers` | `divisor-functions` |
| Using multiplicative functions | `multiplicative-functions` | `divisor-functions` |
| Computing Euler's phi function | `euler-phi` | `multiplicative-functions` |
| Proving Gauss's divisor sum for phi | `phi-divisor-sum` | `euler-phi` |
| Using the Mobius function | `mobius-function` | `multiplicative-functions` |
| Applying Mobius inversion | `mobius-inversion` | `mobius-function`, `phi-divisor-sum` |
| Using Dirichlet convolution | `dirichlet-convolution` | `mobius-inversion` |
| Counting with the floor function | `floor-function-counting` | `math.proofs.division-algorithm-proofs` |
| Finding prime powers dividing factorials | `legendre-formula` | `floor-function-counting` |
| Using p-adic valuations | `p-adic-valuations` | `legendre-formula` |
| Finding average orders of arithmetic functions | `average-orders` | `divisor-functions`, `floor-function-counting` |

### Congruences

| Topic | Slug | Needs |
|---|---|---|
| Solving congruence systems with non-coprime moduli | `general-crt` | `math.discrete.chinese-remainder` |
| Using Wilson's theorem | `wilson-theorem` | `math.discrete.fermat-little`, `math.discrete.modular-inverses` |
| Proving Euler's theorem with reduced residue systems | `euler-theorem-residues` | `euler-phi`, `math.discrete.fermat-little` |
| Testing primality with Fermat tests and pseudoprimes | `pseudoprimes` | `euler-theorem-residues`, `math.discrete.modular-exponentiation` |
| Finding Carmichael numbers | `carmichael-numbers` | `pseudoprimes`, `general-crt` |
| Testing primality with Miller-Rabin | `miller-rabin` | `pseudoprimes` |
| Solving polynomial congruences modulo a prime | `polynomial-congruences-prime` | `math.discrete.linear-congruences` |
| Bounding roots of polynomials modulo a prime | `lagrange-roots-mod-p` | `polynomial-congruences-prime` |
| Lifting solutions with Hensel's lemma | `hensel-lemma` | `polynomial-congruences-prime`, `general-crt` |

### Primitive roots

| Topic | Slug | Needs |
|---|---|---|
| Finding multiplicative orders modulo n | `multiplicative-order` | `euler-theorem-residues` |
| Finding periods of repeating decimals | `repeating-decimals` | `multiplicative-order` |
| Finding primitive roots modulo a prime | `primitive-roots-prime` | `multiplicative-order`, `lagrange-roots-mod-p` |
| Deciding which moduli have primitive roots | `primitive-root-existence` | `primitive-roots-prime`, `hensel-lemma` |
| Using discrete logarithms | `discrete-logarithms` | `primitive-roots-prime` |
| Solving power congruences with indices | `power-congruences` | `discrete-logarithms` |
| Applying Diffie-Hellman and ElGamal | `diffie-hellman-elgamal` | `discrete-logarithms`, `math.discrete.rsa-cryptography` |
| Testing Mersenne numbers with Lucas-Lehmer | `lucas-lehmer` | `perfect-numbers`, `multiplicative-order` |

### Quadratic residues

| Topic | Slug | Needs |
|---|---|---|
| Identifying quadratic residues | `quadratic-residues` | `primitive-roots-prime` |
| Using Euler's criterion | `euler-criterion` | `quadratic-residues` |
| Computing Legendre symbols | `legendre-symbol` | `euler-criterion` |
| Using Gauss's lemma | `gauss-lemma` | `legendre-symbol` |
| Finding when -1 and 2 are quadratic residues | `supplementary-laws` | `gauss-lemma` |
| Proving quadratic reciprocity | `quadratic-reciprocity-proof` | `gauss-lemma` |
| Applying quadratic reciprocity | `quadratic-reciprocity-applications` | `quadratic-reciprocity-proof`, `supplementary-laws` |
| Computing Jacobi symbols | `jacobi-symbol` | `quadratic-reciprocity-applications` |
| Solving quadratic congruences modulo composites | `quadratic-congruences-composite` | `quadratic-reciprocity-applications`, `hensel-lemma` |

### Diophantine equations

| Topic | Slug | Needs |
|---|---|---|
| Parametrizing primitive Pythagorean triples | `pythagorean-triples` | `math.proofs.gcd-proofs`, `math.geom.pythagorean-triples` |
| Proving impossibility by infinite descent | `infinite-descent` | `pythagorean-triples` |
| Ruling out solutions with congruences | `congruence-obstructions` | `quadratic-residues` |
| Writing primes as sums of two squares | `sums-of-two-squares` | `supplementary-laws` |
| Deciding which integers are sums of two squares | `two-squares-characterization` | `sums-of-two-squares`, `divisor-functions` |
| Using Lagrange's four-square theorem | `four-squares` | `sums-of-two-squares` |
| Factoring in the Gaussian integers | `gaussian-integer-factorization` | `sums-of-two-squares` |
| Finding units and primes in quadratic integer rings | `quadratic-integer-rings` | `gaussian-integer-factorization` |
| Showing unique factorization can fail | `factorization-failure` | `quadratic-integer-rings` |

### Continued fractions and approximation

| Topic | Slug | Needs |
|---|---|---|
| Computing finite continued fractions | `finite-continued-fractions` | `math.discrete.euclidean-algorithm` |
| Using convergents and their recursions | `convergents` | `finite-continued-fractions` |
| Expanding irrationals as continued fractions | `infinite-continued-fractions` | `convergents` |
| Finding periodic continued fractions of quadratic irrationals | `periodic-continued-fractions` | `infinite-continued-fractions` |
| Finding best rational approximations | `best-approximations` | `infinite-continued-fractions` |
| Using Dirichlet's approximation theorem | `dirichlet-approximation` | `best-approximations`, `math.proofs.pigeonhole-proofs` |
| Solving Pell's equation | `pell-equation` | `periodic-continued-fractions` |

### Primes and partitions

| Topic | Slug | Needs |
|---|---|---|
| Estimating the prime counting function | `prime-counting-function` | `math.discrete.infinitely-many-primes` |
| Proving the sum of prime reciprocals diverges | `prime-reciprocals` | `prime-counting-function` |
| Proving Chebyshev's bounds on primes | `chebyshev-bounds` | `prime-counting-function`, `legendre-formula` |
| Using the prime number theorem | `prime-number-theorem` | `chebyshev-bounds` |
| Proving special cases of primes in progressions | `primes-in-progressions` | `prime-number-theorem`, `quadratic-reciprocity-applications` |
| Counting partitions with generating functions | `partitions` | `divisor-functions` |
| Proving partition identities with bijections | `partition-bijections` | `partitions` |

### Computational number theory

| Topic | Slug | Needs |
|---|---|---|
| Factoring with Pollard's rho and p-1 methods | `factoring-algorithms` | `pseudoprimes` |
| Breaking RSA with weak parameters | `rsa-attacks` | `best-approximations`, `math.discrete.rsa-cryptography` |
| Adding points on elliptic curves | `elliptic-curve-group-law` | `multiplicative-order` |
| Counting points on elliptic curves modulo p | `elliptic-curves-mod-p` | `elliptic-curve-group-law`, `legendre-symbol` |

## math.topology: 71 topics

Follows `math.analysis`, `math.abstract`. Level uni-upper.


### Topological spaces

| Topic | Slug | Needs |
|---|---|---|
| Defining topologies on a set | `topology-definition` | `math.analysis.open-sets-proofs`, `math.analysis.metric-space-definition` |
| Comparing finer and coarser topologies | `comparing-topologies` | `topology-definition` |
| Generating topologies from bases | `bases` | `topology-definition` |
| Generating topologies from subbases | `subbases` | `bases` |
| Using the order topology | `order-topology` | `bases` |
| Building the subspace topology | `subspace-topology` | `bases` |
| Building product topologies | `product-topology` | `bases` |
| Working with closed sets and limit points | `closed-sets-topological` | `topology-definition`, `math.analysis.limit-points` |
| Finding closure, interior and boundary | `closure-interior-boundary` | `closed-sets-topological`, `subspace-topology`, `math.analysis.closure-interior` |
| Using Hausdorff spaces | `hausdorff-spaces` | `closed-sets-topological` |
| Using convergent sequences in topological spaces | `sequences-topological` | `hausdorff-spaces` |
| Using the metric topology | `metric-topology` | `bases`, `math.analysis.open-balls-metric` |
| Showing a space is not metrizable | `nonmetrizable-spaces` | `metric-topology`, `hausdorff-spaces` |

### Continuous functions

| Topic | Slug | Needs |
|---|---|---|
| Defining continuity with open sets | `continuity-topological` | `topology-definition`, `math.analysis.continuity-open-sets` |
| Proving maps are homeomorphisms | `homeomorphisms` | `continuity-topological` |
| Building continuous maps by pasting | `pasting-lemma` | `continuity-topological`, `closed-sets-topological` |
| Using maps into products | `maps-into-products` | `product-topology`, `continuity-topological` |
| Comparing box and product topologies | `box-vs-product` | `maps-into-products` |
| Using uniform limits in metric spaces | `uniform-limit-theorem` | `metric-topology`, `math.analysis.uniform-limit-continuous` |
| Building quotient topologies | `quotient-topology` | `continuity-topological` |
| Recognizing quotient maps | `quotient-maps` | `quotient-topology` |
| Identifying spaces built by gluing | `gluing-spaces` | `quotient-topology` |

### Connectedness

| Topic | Slug | Needs |
|---|---|---|
| Proving spaces are connected | `connected-spaces` | `subspace-topology`, `math.analysis.connected-sets` |
| Proving unions and products are connected | `connected-unions-products` | `connected-spaces`, `product-topology` |
| Proving intervals are connected | `connected-real-line` | `connected-spaces`, `order-topology` |
| Using path-connectedness | `path-connected` | `connected-real-line`, `continuity-topological` |
| Telling connected from path-connected spaces | `topologist-sine-curve` | `path-connected`, `closure-interior-boundary` |
| Finding components and path components | `components` | `path-connected` |
| Using local connectedness | `local-connectedness` | `components` |
| Telling spaces apart with connectedness | `connectedness-invariants` | `homeomorphisms`, `components` |

### Compactness

| Topic | Slug | Needs |
|---|---|---|
| Proving compactness with open covers | `compact-spaces` | `subspace-topology`, `math.analysis.compact-sets-covers` |
| Proving closed subsets of compact spaces are compact | `compact-closed-subsets` | `compact-spaces`, `hausdorff-spaces` |
| Proving bijections from compact to Hausdorff spaces are homeomorphisms | `compact-to-hausdorff` | `compact-closed-subsets`, `homeomorphisms` |
| Proving finite products of compact spaces are compact | `tube-lemma` | `compact-spaces`, `product-topology` |
| Proving closed intervals are compact | `compact-intervals` | `compact-spaces`, `order-topology` |
| Characterizing compact subsets of real n-space | `heine-borel-general` | `compact-intervals`, `tube-lemma`, `metric-topology` |
| Using limit point and sequential compactness | `limit-point-compactness` | `compact-spaces`, `sequences-topological` |
| Using the Lebesgue number lemma | `lebesgue-number` | `limit-point-compactness`, `metric-topology` |
| Using local compactness | `local-compactness` | `compact-closed-subsets` |
| Building one-point compactifications | `one-point-compactification` | `local-compactness` |
| Using Tychonoff's theorem | `tychonoff` | `tube-lemma` |

### Countability and separation

| Topic | Slug | Needs |
|---|---|---|
| Using first and second countability | `countability-axioms` | `bases`, `sequences-topological` |
| Using separable and Lindelof spaces | `separable-lindelof` | `countability-axioms` |
| Using regular and normal spaces | `regular-normal` | `hausdorff-spaces` |
| Proving metric and compact Hausdorff spaces are normal | `normality-examples` | `regular-normal`, `compact-closed-subsets`, `metric-topology` |
| Using the Urysohn lemma | `urysohn-lemma` | `normality-examples` |
| Using the Urysohn metrization theorem | `urysohn-metrization` | `urysohn-lemma`, `countability-axioms` |
| Extending maps with the Tietze theorem | `tietze-extension` | `urysohn-lemma`, `uniform-limit-theorem` |
| Using the Baire category theorem | `baire-category` | `metric-topology`, `math.analysis.complete-metric-spaces` |

### Fundamental group

| Topic | Slug | Needs |
|---|---|---|
| Defining homotopies of maps | `homotopy` | `continuity-topological`, `pasting-lemma` |
| Composing paths up to homotopy | `path-homotopy` | `homotopy`, `path-connected` |
| Defining the fundamental group | `fundamental-group` | `path-homotopy` |
| Changing basepoints | `basepoint-change` | `fundamental-group` |
| Proving spaces are simply connected | `simply-connected` | `fundamental-group` |
| Using induced homomorphisms | `induced-homomorphisms` | `fundamental-group` |
| Using covering maps | `covering-maps` | `quotient-maps`, `homeomorphisms` |
| Lifting paths and homotopies | `path-lifting` | `covering-maps`, `lebesgue-number` |
| Computing the fundamental group of the circle | `fundamental-group-circle` | `path-lifting`, `simply-connected` |
| Proving the Brouwer fixed point theorem in the plane | `brouwer-fixed-point` | `fundamental-group-circle`, `induced-homomorphisms` |
| Proving the fundamental theorem of algebra topologically | `fta-topological` | `fundamental-group-circle` |
| Proving the two-dimensional Borsuk-Ulam theorem | `borsuk-ulam` | `fundamental-group-circle`, `induced-homomorphisms` |
| Using deformation retracts and homotopy equivalence | `deformation-retracts` | `induced-homomorphisms` |
| Finding fundamental groups of products and spheres | `products-and-spheres` | `deformation-retracts`, `simply-connected` |
| Using the Seifert-van Kampen theorem | `van-kampen` | `products-and-spheres` |

### Surfaces

| Topic | Slug | Needs |
|---|---|---|
| Building surfaces from polygons | `surfaces-from-polygons` | `gluing-spaces` |
| Telling orientable from non-orientable surfaces | `orientability` | `surfaces-from-polygons` |
| Computing Euler characteristics of surfaces | `euler-characteristic` | `surfaces-from-polygons` |
| Classifying compact surfaces | `classification-of-surfaces` | `euler-characteristic`, `orientability`, `connectedness-invariants` |
| Finding fundamental groups of surfaces | `surface-groups` | `van-kampen`, `surfaces-from-polygons` |
| Building simplicial complexes | `simplicial-complexes` | `euler-characteristic` |
| Computing simplicial homology of small complexes | `simplicial-homology-intro` | `simplicial-complexes`, `induced-homomorphisms` |

## math.geometry: 59 topics

Follows `math.proofs`, `math.linalg`. Level uni-upper.


### Axiom systems

| Topic | Slug | Needs |
|---|---|---|
| Testing axiom systems for consistency and independence | `axiom-systems` | `math.proofs.reading-proofs` |
| Building models of finite geometries | `finite-geometries` | `axiom-systems` |
| Using duality in finite projective planes | `projective-plane-duality` | `finite-geometries` |
| Proving theorems from incidence axioms | `incidence-geometry` | `finite-geometries` |
| Comparing parallel properties of incidence models | `incidence-parallel-properties` | `incidence-geometry` |

### Foundations of neutral geometry

| Topic | Slug | Needs |
|---|---|---|
| Using the ruler postulate and betweenness | `ruler-betweenness` | `incidence-geometry` |
| Using the plane separation postulate | `plane-separation` | `ruler-betweenness` |
| Proving Pasch's axiom and the crossbar theorem | `crossbar-theorem` | `plane-separation` |
| Using the protractor postulate | `protractor-postulate` | `crossbar-theorem` |
| Proving congruence criteria from the SAS axiom | `sas-axiom-proofs` | `protractor-postulate`, `math.geom.sss-and-sas` |
| Proving the exterior angle theorem in neutral geometry | `neutral-exterior-angle` | `sas-axiom-proofs` |
| Proving the triangle inequality in neutral geometry | `neutral-triangle-inequality` | `neutral-exterior-angle` |
| Proving parallels exist in neutral geometry | `neutral-parallels` | `neutral-exterior-angle` |
| Proving the Saccheri-Legendre theorem | `saccheri-legendre` | `neutral-triangle-inequality` |
| Using angle defect | `angle-defect` | `saccheri-legendre` |
| Using Saccheri and Lambert quadrilaterals | `saccheri-quadrilaterals` | `angle-defect` |
| Proving statements equivalent to the parallel postulate | `parallel-postulate-equivalents` | `saccheri-quadrilaterals`, `neutral-parallels` |
| Proving a neutral plane is Euclidean or hyperbolic | `all-or-none-theorem` | `parallel-postulate-equivalents` |

### Advanced Euclidean geometry

| Topic | Slug | Needs |
|---|---|---|
| Proving the similarity theorem from the parallel postulate | `euclidean-similarity` | `parallel-postulate-equivalents` |
| Using Ceva's theorem | `ceva` | `euclidean-similarity` |
| Using Menelaus's theorem | `menelaus` | `euclidean-similarity` |
| Proving triangle centers are concurrent | `concurrence-proofs` | `ceva`, `math.geom.triangle-centers` |
| Using the Euler line and nine-point circle | `euler-line-nine-point` | `concurrence-proofs` |
| Using the power of a point | `power-of-a-point` | `euclidean-similarity` |
| Proving theorems on cyclic quadrilaterals | `cyclic-quadrilaterals` | `power-of-a-point` |
| Using Ptolemy's theorem | `ptolemy` | `cyclic-quadrilaterals` |
| Using Simson lines | `simson-line` | `cyclic-quadrilaterals` |

### Transformations

| Topic | Slug | Needs |
|---|---|---|
| Classifying isometries of the plane | `isometry-classification` | `math.geom.compose-transformations`, `math.linalg.orthonormal-matrices` |
| Writing isometries as products of reflections | `three-reflections` | `isometry-classification` |
| Using similarity transformations | `similarity-transformations` | `isometry-classification` |
| Writing plane transformations with complex numbers | `complex-transformations` | `isometry-classification` |
| Finding symmetry groups of figures | `symmetry-groups` | `three-reflections` |
| Classifying frieze patterns | `frieze-patterns` | `symmetry-groups` |
| Classifying wallpaper patterns | `wallpaper-patterns` | `frieze-patterns` |
| Using inversion in a circle | `circle-inversion` | `power-of-a-point` |
| Using orthogonal circles | `orthogonal-circles` | `circle-inversion` |

### Hyperbolic geometry

| Topic | Slug | Needs |
|---|---|---|
| Building the Poincare disk model | `poincare-disk` | `orthogonal-circles`, `all-or-none-theorem` |
| Building the upper half-plane model | `upper-half-plane` | `poincare-disk`, `complex-transformations` |
| Building the Klein model | `klein-model` | `poincare-disk` |
| Measuring hyperbolic distance | `hyperbolic-distance` | `upper-half-plane` |
| Using limiting and ultraparallel lines | `hyperbolic-parallels` | `poincare-disk` |
| Finding the angle of parallelism | `angle-of-parallelism` | `hyperbolic-parallels`, `hyperbolic-distance` |
| Finding hyperbolic triangle area from defect | `hyperbolic-area` | `angle-defect`, `poincare-disk` |
| Proving similar hyperbolic triangles are congruent | `aaa-congruence` | `hyperbolic-area` |
| Using hyperbolic trigonometry | `hyperbolic-trigonometry` | `hyperbolic-distance` |
| Classifying hyperbolic isometries | `hyperbolic-isometries` | `upper-half-plane` |

### Spherical and other geometries

| Topic | Slug | Needs |
|---|---|---|
| Measuring distances and angles on the sphere | `spherical-geometry` | `axiom-systems` |
| Finding spherical triangle area by excess | `spherical-excess` | `spherical-geometry` |
| Using spherical trigonometry | `spherical-trigonometry` | `spherical-geometry` |
| Building elliptic geometry from the sphere | `elliptic-geometry` | `spherical-geometry` |
| Using taxicab geometry | `taxicab-geometry` | `axiom-systems` |
| Comparing geometries by their axioms | `comparing-geometries` | `elliptic-geometry`, `aaa-congruence`, `taxicab-geometry` |
| Proving limits of straightedge and compass constructions | `constructible-numbers` | `axiom-systems`, `math.geom.construct-bisectors` |

### Projective geometry

| Topic | Slug | Needs |
|---|---|---|
| Using homogeneous coordinates | `homogeneous-coordinates` | `projective-plane-duality`, `math.linalg.inner-product-rn` |
| Using projective transformations | `projective-transformations` | `homogeneous-coordinates` |
| Using the cross ratio of collinear points | `cross-ratio` | `projective-transformations` |
| Proving Desargues's theorem | `desargues` | `homogeneous-coordinates` |
| Proving Pappus's theorem | `pappus` | `desargues` |
| Classifying conics projectively | `projective-conics` | `projective-transformations` |

## math.optimization: 50 topics

Follows `math.numerical`, `math.calc3`, `math.discrete`. Level uni-upper.


### Linear programming

| Topic | Slug | Needs |
|---|---|---|
| Formulating linear programs | `lp-formulation` | `math.linalg.column-space` |
| Solving two-variable linear programs graphically | `lp-graphical` | `lp-formulation` |
| Converting linear programs to standard form | `lp-standard-form` | `lp-formulation` |
| Describing convex polyhedra | `polyhedra` | `lp-standard-form` |
| Finding basic feasible solutions | `basic-feasible-solutions` | `polyhedra`, `math.linalg.basis-of-column-space` |
| Proving optima occur at vertices | `vertex-optimality` | `basic-feasible-solutions` |
| Running the simplex method with tableaux | `simplex-tableau` | `vertex-optimality` |
| Choosing entering and leaving variables | `pivot-rules` | `simplex-tableau` |
| Finding starting solutions with two-phase simplex | `two-phase-simplex` | `simplex-tableau` |
| Using the big-M method | `big-m` | `two-phase-simplex` |
| Handling degeneracy and cycling | `degeneracy-cycling` | `pivot-rules` |
| Detecting unbounded and infeasible programs | `unbounded-infeasible` | `two-phase-simplex` |
| Using the revised simplex method | `revised-simplex` | `simplex-tableau` |

### Duality and sensitivity

| Topic | Slug | Needs |
|---|---|---|
| Writing the dual of a linear program | `lp-duality` | `lp-standard-form` |
| Proving weak and strong duality | `duality-theorems` | `lp-duality`, `vertex-optimality` |
| Using complementary slackness | `complementary-slackness` | `duality-theorems` |
| Interpreting dual variables as shadow prices | `shadow-prices` | `complementary-slackness` |
| Using the dual simplex method | `dual-simplex` | `complementary-slackness`, `simplex-tableau` |
| Finding ranges for cost coefficients | `sensitivity-costs` | `shadow-prices` |
| Finding ranges for right-hand sides | `sensitivity-rhs` | `shadow-prices` |
| Using Farkas's lemma | `farkas-lemma` | `duality-theorems` |
| Describing interior-point methods | `interior-point-intro` | `duality-theorems` |

### Network models

| Topic | Slug | Needs |
|---|---|---|
| Solving transportation problems | `transportation-problem` | `lp-formulation`, `dual-simplex` |
| Solving assignment problems with the Hungarian method | `assignment-problem` | `transportation-problem` |
| Formulating minimum-cost network flows | `min-cost-flow` | `transportation-problem` |
| Proving max-flow min-cut with LP duality | `max-flow-min-cut` | `min-cost-flow`, `duality-theorems` |
| Using total unimodularity | `total-unimodularity` | `max-flow-min-cut` |

### Integer and dynamic programming

| Topic | Slug | Needs |
|---|---|---|
| Formulating integer programs with binary variables | `ip-formulation` | `lp-formulation` |
| Modelling logical constraints with binary variables | `logical-constraints` | `ip-formulation` |
| Bounding integer programs with relaxations | `lp-relaxation` | `ip-formulation`, `duality-theorems` |
| Solving integer programs by branch and bound | `branch-and-bound` | `lp-relaxation`, `dual-simplex` |
| Using cutting planes | `cutting-planes` | `branch-and-bound` |
| Solving knapsack problems by dynamic programming | `knapsack-dp` | `ip-formulation` |
| Using dynamic programming for staged decisions | `dynamic-programming-opt` | `knapsack-dp` |

### Nonlinear optimization

| Topic | Slug | Needs |
|---|---|---|
| Identifying convex sets | `convex-sets` | `polyhedra` |
| Testing convexity of functions | `convex-functions` | `convex-sets`, `math.linalg.positive-definite` |
| Using optimality conditions without constraints | `unconstrained-conditions` | `convex-functions`, `math.calc3.second-derivatives-test-two` |
| Proving local minima of convex functions are global | `convex-global` | `convex-functions` |
| Using line searches | `line-search` | `math.numerical.optimization-gradient-descent` |
| Analyzing convergence of gradient descent | `gradient-descent-convergence` | `line-search`, `convex-global` |
| Using Newton and quasi-Newton methods | `quasi-newton` | `math.numerical.newton-for-optimization`, `line-search` |
| Solving least squares as an optimization problem | `least-squares-opt` | `unconstrained-conditions`, `math.linalg.least-squares-normal` |
| Using Lagrange conditions for equality constraints | `equality-constrained` | `math.calc3.lagrange-two-constraints`, `unconstrained-conditions` |
| Using the KKT conditions | `kkt-conditions` | `equality-constrained`, `complementary-slackness` |
| Checking constraint qualifications | `constraint-qualifications` | `kkt-conditions` |
| Using Lagrangian duality | `lagrangian-duality` | `kkt-conditions`, `duality-theorems` |
| Solving quadratic programs | `quadratic-programs` | `kkt-conditions` |
| Using penalty and barrier methods | `penalty-barrier` | `kkt-conditions`, `line-search` |
| Using projected gradient methods | `projected-gradient` | `gradient-descent-convergence`, `convex-sets` |
| Solving multiobjective problems with weights | `multiobjective` | `lp-formulation`, `convex-sets` |

## physics.solid-state: 61 topics

Follows `physics.quantum`, `physics.stat-thermal`, `physics.em-theory`. Level uni-upper.


### Crystal structure

| Topic | Slug | Needs |
|---|---|---|
| Describing Bravais lattices | `bravais-lattices` | `physics.waves-thermo-optics.x-ray-diffraction`, `math.linalg.basis-of-column-space` |
| Finding primitive and Wigner-Seitz cells | `primitive-cells` | `bravais-lattices` |
| Describing common crystal structures | `crystal-structures` | `bravais-lattices` |
| Finding packing fractions and coordination numbers | `packing-fractions` | `crystal-structures` |
| Using Miller indices | `miller-indices` | `bravais-lattices` |
| Classifying bonding in crystals | `crystal-bonding` | `crystal-structures` |
| Finding cohesive energy of ionic crystals | `madelung-energy` | `crystal-bonding` |
| Describing point defects and dislocations | `crystal-defects` | `crystal-structures` |

### Reciprocal lattice and diffraction

| Topic | Slug | Needs |
|---|---|---|
| Building the reciprocal lattice | `reciprocal-lattice` | `miller-indices` |
| Constructing Brillouin zones | `brillouin-zones` | `reciprocal-lattice`, `primitive-cells` |
| Using the Laue condition for diffraction | `laue-condition` | `reciprocal-lattice`, `physics.waves-thermo-optics.x-ray-diffraction` |
| Using the Ewald construction | `ewald-construction` | `laue-condition` |
| Computing structure factors and systematic absences | `structure-factor` | `laue-condition`, `crystal-structures` |
| Comparing x-ray, electron and neutron diffraction | `diffraction-probes` | `structure-factor` |

### Lattice vibrations

| Topic | Slug | Needs |
|---|---|---|
| Finding dispersion of a monatomic chain | `monatomic-chain` | `brillouin-zones`, `physics.classical.normal-modes-by-eigenvalues` |
| Finding acoustic and optical branches | `diatomic-chain` | `monatomic-chain` |
| Quantizing lattice vibrations as phonons | `phonons` | `monatomic-chain`, `physics.quantum.ladder-operators-oscillator` |
| Finding phonon densities of states | `phonon-density-of-states` | `phonons`, `physics.stat-thermal.density-of-states` |
| Finding lattice heat capacity from phonons | `lattice-heat-capacity` | `phonon-density-of-states`, `physics.stat-thermal.debye-model` |
| Finding thermal conductivity from phonons | `phonon-thermal-conductivity` | `lattice-heat-capacity`, `physics.stat-thermal.transport-coefficients` |
| Explaining thermal expansion from anharmonicity | `anharmonic-effects` | `phonons` |
| Measuring phonons by inelastic scattering | `phonon-scattering-measurement` | `phonons`, `diffraction-probes` |

### Free electrons

| Topic | Slug | Needs |
|---|---|---|
| Using the Drude model of conduction | `drude-model` | `physics.em-theory.waves-in-conductors` |
| Finding Hall coefficients | `hall-effect` | `drude-model` |
| Finding metal properties with the Sommerfeld model | `sommerfeld-model` | `drude-model`, `physics.stat-thermal.degenerate-fermi-gas` |
| Using the Wiedemann-Franz law | `wiedemann-franz` | `sommerfeld-model`, `physics.stat-thermal.electron-heat-capacity` |
| Finding work functions and thermionic emission | `thermionic-emission` | `sommerfeld-model` |

### Electronic bands

| Topic | Slug | Needs |
|---|---|---|
| Applying Bloch's theorem in three dimensions | `bloch-theorem-3d` | `reciprocal-lattice`, `physics.quantum.periodic-potentials-and-bloch` |
| Finding band gaps with the nearly free electron model | `nearly-free-electron` | `bloch-theorem-3d`, `brillouin-zones`, `physics.quantum.degenerate-perturbation` |
| Using the tight-binding model | `tight-binding` | `bloch-theorem-3d` |
| Counting states in a band | `states-per-band` | `bloch-theorem-3d`, `brillouin-zones` |
| Classifying solids by band filling | `band-filling` | `states-per-band`, `physics.modern.band-classification-of-solids` |
| Constructing Fermi surfaces | `fermi-surfaces` | `nearly-free-electron`, `band-filling` |
| Using effective mass | `effective-mass` | `tight-binding` |
| Describing holes | `holes` | `effective-mass` |
| Finding electron motion in applied fields | `semiclassical-dynamics` | `effective-mass` |
| Explaining cyclotron resonance and quantum oscillations | `cyclotron-resonance` | `semiclassical-dynamics`, `fermi-surfaces` |

### Semiconductors

| Topic | Slug | Needs |
|---|---|---|
| Finding intrinsic carrier concentrations | `intrinsic-carriers` | `holes`, `physics.stat-thermal.semiconductor-carrier-statistics` |
| Finding carrier concentrations in doped semiconductors | `doped-carriers` | `intrinsic-carriers`, `physics.modern.doped-semiconductors` |
| Finding mobility and conductivity of semiconductors | `semiconductor-mobility` | `doped-carriers`, `drude-model` |
| Deriving drift and diffusion currents from carrier transport | `drift-diffusion` | `semiconductor-mobility` |
| Finding fields and widths of p-n junctions | `pn-junction-electrostatics` | `doped-carriers`, `physics.modern.pn-junctions` |
| Deriving the ideal diode equation from carrier injection | `diode-equation` | `pn-junction-electrostatics`, `drift-diffusion` |
| Telling direct from indirect band gaps | `direct-indirect-gaps` | `effective-mass` |
| Describing optical absorption and emission in semiconductors | `semiconductor-optics` | `direct-indirect-gaps` |
| Describing quantum wells and low-dimensional systems | `quantum-wells` | `effective-mass`, `physics.quantum.finite-well-exact` |

### Dielectric and optical properties

| Topic | Slug | Needs |
|---|---|---|
| Finding the plasma frequency of metals | `plasma-frequency` | `drude-model`, `physics.em-theory.dispersion-in-dielectrics` |
| Finding local fields in dielectrics | `local-field` | `physics.em-theory.clausius-mossotti` |
| Describing ferroelectrics | `ferroelectrics` | `local-field` |

### Magnetism

| Topic | Slug | Needs |
|---|---|---|
| Explaining diamagnetism | `diamagnetism` | `physics.em-theory.magnetization-and-bound-currents` |
| Explaining paramagnetism with Curie's law | `curie-paramagnetism` | `physics.stat-thermal.paramagnet-thermodynamics` |
| Explaining Pauli paramagnetism of metals | `pauli-paramagnetism` | `sommerfeld-model`, `curie-paramagnetism` |
| Explaining ferromagnetic order from exchange | `exchange-ferromagnetism` | `physics.quantum.exchange-force` |
| Finding the Curie temperature in mean field theory | `mean-field-ferromagnet` | `exchange-ferromagnetism`, `physics.stat-thermal.ising-mean-field` |
| Describing antiferromagnetism and ferrimagnetism | `antiferromagnetism` | `mean-field-ferromagnet` |
| Finding spin wave dispersion | `spin-waves` | `exchange-ferromagnetism`, `monatomic-chain` |
| Explaining domains and hysteresis | `magnetic-domains` | `exchange-ferromagnetism` |

### Superconductivity

| Topic | Slug | Needs |
|---|---|---|
| Describing the Meissner effect and critical fields | `meissner-effect` | `physics.modern.superconductivity-overview` |
| Using the London equations | `london-equations` | `meissner-effect`, `physics.em-theory.waves-in-conductors` |
| Describing BCS theory qualitatively | `bcs-theory` | `london-equations`, `phonons` |
| Explaining flux quantization and Josephson effects | `josephson-effects` | `bcs-theory` |

## physics.nuclear-particle: 51 topics

Follows `physics.quantum`, `physics.stat-thermal`, `math.probstat`. Level uni-upper.


### Nuclear properties

| Topic | Slug | Needs |
|---|---|---|
| Using natural units | `natural-units` | `physics.modern.energy-momentum-relation` |
| Measuring nuclear size by electron scattering | `nuclear-form-factors` | `physics.modern.nuclear-size-and-density`, `physics.quantum.born-approximation` |
| Finding nuclear spin, parity and moments | `nuclear-spin-moments` | `physics.quantum.addition-of-angular-momentum` |
| Describing the deuteron | `deuteron` | `physics.quantum.infinite-spherical-well`, `physics.quantum.finite-well-exact` |
| Describing properties of the nuclear force | `nuclear-force` | `deuteron` |
| Using isospin | `isospin` | `nuclear-force`, `physics.quantum.addition-of-angular-momentum` |
| Explaining the range of forces from meson exchange | `yukawa-exchange` | `nuclear-force`, `physics.quantum.yukawa-and-coulomb-scattering` |

### Nuclear models

| Topic | Slug | Needs |
|---|---|---|
| Predicting stability with the liquid drop model | `liquid-drop-stability` | `physics.modern.semi-empirical-mass-formula` |
| Using the Fermi gas model of nuclei | `nuclear-fermi-gas` | `physics.stat-thermal.degenerate-fermi-gas` |
| Predicting magic numbers with the shell model | `shell-model` | `physics.quantum.infinite-spherical-well`, `physics.quantum.fine-structure-hydrogen` |
| Predicting ground-state spins and parities | `shell-model-spins` | `shell-model`, `nuclear-spin-moments` |
| Describing collective rotations and vibrations | `collective-models` | `shell-model`, `physics.quantum.rigid-rotor` |

### Decays

| Topic | Slug | Needs |
|---|---|---|
| Relating decay widths and lifetimes | `decay-widths` | `physics.modern.decay-law-derivation`, `physics.modern.energy-time-uncertainty` |
| Finding alpha decay rates with Gamow theory | `gamow-alpha` | `physics.quantum.wkb-tunneling`, `physics.modern.alpha-decay-energetics` |
| Deriving beta spectra with Fermi theory | `fermi-beta-theory` | `physics.quantum.fermi-golden-rule`, `physics.modern.beta-decay-and-neutrinos` |
| Classifying allowed and forbidden beta decays | `beta-selection-rules` | `fermi-beta-theory`, `nuclear-spin-moments` |
| Explaining parity violation in beta decay | `parity-violation-beta` | `beta-selection-rules` |
| Classifying gamma transitions by multipolarity | `gamma-multipolarity` | `physics.modern.gamma-decay`, `nuclear-spin-moments` |
| Describing internal conversion | `internal-conversion` | `gamma-multipolarity` |
| Using radioactive dating | `radioactive-dating` | `physics.modern.decay-chains-with-equations` |

### Nuclear reactions

| Topic | Slug | Needs |
|---|---|---|
| Finding reaction kinematics and Q values | `reaction-kinematics` | `physics.modern.q-values-of-decays`, `physics.modern.relativistic-collisions` |
| Measuring nuclear reaction cross sections | `differential-cross-sections` | `physics.modern.nuclear-reactions-and-cross-sections`, `physics.quantum.scattering-amplitude`, `physics.classical.scattering-cross-sections` |
| Using the Breit-Wigner resonance formula | `breit-wigner` | `differential-cross-sections`, `decay-widths` |
| Comparing compound nucleus and direct reactions | `compound-nucleus` | `breit-wigner` |
| Analyzing neutron moderation and criticality | `reactor-physics` | `physics.modern.chain-reactions`, `differential-cross-sections` |
| Finding fusion rates in stars and reactors | `fusion-rates` | `physics.modern.fusion-energetics`, `gamow-alpha`, `physics.stat-thermal.maxwell-distribution-derived` |

### Radiation and detection

| Topic | Slug | Needs |
|---|---|---|
| Finding energy loss of charged particles | `bethe-bloch` | `physics.modern.radiation-attenuation` |
| Finding ranges and Bragg peaks | `ranges-bragg-peak` | `bethe-bloch` |
| Describing photon interactions in matter | `photon-interactions` | `physics.modern.radiation-attenuation`, `physics.modern.pair-production-and-annihilation` |
| Describing electromagnetic showers | `em-showers` | `photon-interactions`, `bethe-bloch` |
| Comparing gas, scintillation and semiconductor detectors | `radiation-detectors` | `photon-interactions` |
| Using counting statistics for radiation | `counting-statistics` | `math.probstat.poisson` |
| Finding dose and biological effects of radiation | `radiation-dosimetry` | `ranges-bragg-peak`, `photon-interactions` |

### Particle kinematics and symmetries

| Topic | Slug | Needs |
|---|---|---|
| Finding particles from invariant mass | `invariant-mass` | `natural-units`, `physics.modern.four-vectors` |
| Finding two-body decay kinematics | `two-body-decays` | `invariant-mass` |
| Finding event rates from luminosity | `luminosity` | `invariant-mass`, `differential-cross-sections` |
| Using parity and charge conjugation | `c-and-p-symmetry` | `nuclear-spin-moments` |
| Explaining CP violation in neutral kaons | `cp-violation` | `c-and-p-symmetry`, `physics.quantum.two-level-systems` |
| Using quantum numbers in particle reactions | `particle-quantum-numbers` | `physics.modern.conservation-laws-in-reactions`, `isospin` |

### Quarks, leptons and forces

| Topic | Slug | Needs |
|---|---|---|
| Building meson and baryon multiplets | `hadron-multiplets` | `particle-quantum-numbers`, `physics.modern.quark-model` |
| Explaining color and confinement | `color-confinement` | `hadron-multiplets` |
| Explaining deep inelastic scattering and partons | `deep-inelastic` | `color-confinement`, `nuclear-form-factors` |
| Explaining running couplings and jets | `asymptotic-freedom` | `deep-inelastic` |
| Reading Feynman diagrams for QED processes | `qed-diagrams` | `physics.modern.feynman-diagrams-intro`, `natural-units` |
| Estimating rates from coupling constants | `coupling-estimates` | `qed-diagrams`, `physics.quantum.fermi-golden-rule` |
| Describing W and Z bosons in weak processes | `weak-bosons` | `coupling-estimates`, `fermi-beta-theory` |
| Using lepton universality and quark mixing | `quark-mixing` | `weak-bosons` |
| Explaining neutrino oscillations | `neutrino-oscillations` | `quark-mixing`, `physics.quantum.two-level-systems` |
| Describing electroweak unification | `electroweak-unification` | `weak-bosons` |
| Explaining the Higgs mechanism qualitatively | `higgs-mechanism` | `electroweak-unification` |
| Summarizing the standard model and its open problems | `standard-model-summary` | `higgs-mechanism`, `neutrino-oscillations`, `asymptotic-freedom` |

## physics.optics: 46 topics

Follows `physics.em-theory`, `physics.quantum`, `physics.stat-thermal`. Level uni-upper.


### Polarization and anisotropic media

| Topic | Slug | Needs |
|---|---|---|
| Using Jones vectors and matrices | `jones-calculus` | `physics.waves-thermo-optics.wave-plates`, `physics.em-theory.polarization-of-em-waves` |
| Finding eigenpolarizations of optical elements | `eigenpolarizations` | `jones-calculus` |
| Using Stokes parameters and the Poincare sphere | `stokes-parameters` | `jones-calculus` |
| Describing partially polarized light | `partial-polarization` | `stokes-parameters` |
| Propagating light in uniaxial crystals | `birefringence` | `physics.em-theory.waves-in-linear-media` |
| Using optical activity and Faraday rotation | `optical-activity` | `jones-calculus` |
| Designing electro-optic modulators | `electro-optic-modulators` | `birefringence`, `jones-calculus` |

### Interference

| Topic | Slug | Needs |
|---|---|---|
| Analyzing amplitude-splitting interferometers | `interferometers` | `physics.waves-thermo-optics.michelson-interferometer` |
| Analyzing multiple-beam interference in a Fabry-Perot | `fabry-perot` | `interferometers`, `physics.em-theory.normal-incidence-reflection` |
| Finding finesse and resolving power of etalons | `etalon-resolution` | `fabry-perot` |
| Designing coatings with characteristic matrices | `thin-film-matrices` | `physics.waves-thermo-optics.thin-films-with-phase-shifts`, `physics.em-theory.fresnel-equations` |
| Using Fourier transform spectroscopy | `fourier-spectroscopy` | `interferometers`, `math.pde.fourier-transform-properties` |

### Coherence

| Topic | Slug | Needs |
|---|---|---|
| Finding temporal coherence from spectra | `temporal-coherence` | `physics.waves-thermo-optics.coherence`, `fourier-spectroscopy` |
| Using fringe visibility | `fringe-visibility` | `temporal-coherence` |
| Finding spatial coherence of extended sources | `spatial-coherence` | `temporal-coherence` |
| Measuring source sizes by interferometry | `stellar-interferometry` | `spatial-coherence` |

### Diffraction

| Topic | Slug | Needs |
|---|---|---|
| Using the Fresnel-Kirchhoff diffraction integral | `kirchhoff-integral` | `physics.waves-thermo-optics.huygens-principle` |
| Finding Fraunhofer patterns as Fourier transforms | `fraunhofer-fourier` | `kirchhoff-integral`, `math.pde.fourier-transform-properties` |
| Finding Fraunhofer patterns of apertures and arrays | `aperture-patterns` | `fraunhofer-fourier` |
| Using Fresnel zones and zone plates | `fresnel-zones` | `kirchhoff-integral` |
| Finding Fresnel diffraction from edges and slits | `fresnel-edge-diffraction` | `fresnel-zones` |
| Analyzing grating spectrometers | `grating-spectrometers` | `aperture-patterns`, `physics.waves-thermo-optics.grating-resolving-power` |

### Fourier optics and imaging

| Topic | Slug | Needs |
|---|---|---|
| Showing a lens performs a Fourier transform | `lens-fourier-transform` | `fraunhofer-fourier` |
| Using spatial filtering in 4f systems | `spatial-filtering` | `lens-fourier-transform` |
| Finding coherent transfer functions | `coherent-transfer-function` | `spatial-filtering` |
| Finding optical transfer functions for incoherent imaging | `optical-transfer-function` | `coherent-transfer-function` |
| Finding resolution limits of imaging systems | `imaging-resolution` | `optical-transfer-function`, `physics.waves-thermo-optics.circular-aperture-and-rayleigh` |
| Explaining holography | `holography` | `spatial-filtering`, `fringe-visibility` |
| Explaining phase-contrast imaging | `phase-contrast` | `spatial-filtering` |

### Beams and resonators

| Topic | Slug | Needs |
|---|---|---|
| Describing Gaussian beams | `gaussian-beams` | `kirchhoff-integral` |
| Propagating Gaussian beams with ABCD matrices | `gaussian-abcd` | `gaussian-beams`, `physics.waves-thermo-optics.ray-transfer-matrices` |
| Finding stability of optical resonators | `resonator-stability` | `gaussian-abcd` |
| Finding longitudinal and transverse modes of resonators | `resonator-modes` | `resonator-stability`, `fabry-perot` |

### Lasers

| Topic | Slug | Needs |
|---|---|---|
| Using Einstein coefficients | `einstein-coefficients` | `physics.modern.laser-principles`, `physics.stat-thermal.photon-gas` |
| Describing homogeneous and inhomogeneous broadening | `line-broadening` | `einstein-coefficients` |
| Finding laser gain and threshold | `laser-threshold` | `line-broadening`, `resonator-modes` |
| Using laser rate equations | `laser-rate-equations` | `laser-threshold` |
| Explaining Q-switching and mode locking | `pulsed-lasers` | `laser-rate-equations` |
| Comparing laser types | `laser-types` | `laser-threshold` |

### Guided waves, dispersion and nonlinear optics

| Topic | Slug | Needs |
|---|---|---|
| Finding modes of a slab waveguide | `slab-waveguide` | `physics.em-theory.brewster-and-evanescent-waves` |
| Finding modes of step-index fibers | `fiber-modes` | `slab-waveguide`, `physics.waves-thermo-optics.fiber-acceptance-angle` |
| Finding pulse spreading from dispersion | `pulse-dispersion` | `physics.waves-thermo-optics.group-and-phase-velocity`, `physics.em-theory.dispersion-in-dielectrics` |
| Explaining second-harmonic generation | `second-harmonic` | `physics.em-theory.polarization-and-bound-charge` |
| Using phase matching | `phase-matching` | `second-harmonic`, `birefringence` |
| Describing the Kerr effect and self-focusing | `kerr-effect` | `second-harmonic` |
| Describing photon statistics of light sources | `photon-statistics` | `physics.quantum.coherent-states`, `math.probstat.poisson` |

## bio.molecular-biology: 44 topics

Follows `bio.genetics`, `bio.biochem`, `bio.cell-mol`. Level uni-upper.


### DNA structure and replication

| Topic | Slug | Needs |
|---|---|---|
| Explaining DNA supercoiling and topoisomerases | `dna-supercoiling` | `bio.biochem.nucleic-acid-stability` |
| Describing alternative DNA and RNA structures | `alternative-dna-structures` | `dna-supercoiling` |
| Explaining nucleosome positioning | `nucleosome-positioning` | `bio.intro1.chromatin-structure`, `bio.cell-mol.histone-modification` |
| Tracing proteins at the bacterial replication fork | `bacterial-replication-fork` | `bio.biochem.polymerase-fidelity` |
| Explaining initiation of bacterial replication | `replication-initiation-bacteria` | `bacterial-replication-fork` |
| Explaining replication termination and decatenation | `replication-termination` | `bacterial-replication-fork`, `dna-supercoiling` |
| Comparing the eukaryotic replisome | `eukaryotic-replisome` | `bacterial-replication-fork`, `bio.cell-mol.replication-licensing` |
| Explaining replication through chromatin | `replication-chromatin` | `eukaryotic-replisome`, `nucleosome-positioning` |
| Interpreting classic replication experiments | `replication-experiments` | `bacterial-replication-fork` |

### Repair and recombination

| Topic | Slug | Needs |
|---|---|---|
| Comparing mismatch, base and nucleotide excision repair | `excision-repair` | `bio.intro1.dna-repair` |
| Comparing double-strand break repair pathways | `dsb-repair` | `excision-repair`, `bio.genetics.recombination-mechanisms` |
| Explaining translesion synthesis and the SOS response | `sos-response` | `excision-repair` |
| Explaining site-specific recombination | `site-specific-recombination` | `bio.genetics.recombination-mechanisms` |
| Explaining transposition mechanisms | `transposition-mechanisms` | `bio.genetics.transposable-elements` |
| Explaining CRISPR as bacterial immunity | `crispr-immunity` | `bio.genetics.reverse-genetics-and-editing` |

### Transcription and RNA processing

| Topic | Slug | Needs |
|---|---|---|
| Explaining bacterial promoters and sigma factors | `bacterial-promoters` | `bio.biochem.rna-polymerase-mechanism` |
| Explaining transcription termination in bacteria | `bacterial-termination` | `bacterial-promoters` |
| Explaining lac operon regulation mechanistically | `lac-operon-mechanism` | `bacterial-promoters`, `bio.genetics.operon-mutant-analysis` |
| Explaining attenuation in the trp operon | `trp-attenuation` | `bacterial-termination`, `lac-operon-mechanism` |
| Explaining riboswitches and small regulatory RNAs | `riboswitches-srnas` | `trp-attenuation` |
| Describing general transcription factors and Mediator | `general-transcription-factors` | `bio.cell-mol.transcription-machinery` |
| Explaining capping and polyadenylation | `capping-polyadenylation` | `general-transcription-factors` |
| Explaining splicing chemistry and self-splicing introns | `splicing-chemistry` | `bio.cell-mol.splicing-mechanisms` |
| Explaining RNA editing | `rna-editing` | `splicing-chemistry` |
| Explaining nonsense-mediated decay and RNA surveillance | `rna-surveillance` | `capping-polyadenylation`, `bio.cell-mol.mrna-stability-and-localization` |
| Explaining RNA interference pathways | `rnai-pathways` | `bio.intro1.noncoding-rna` |

### Translation

| Topic | Slug | Needs |
|---|---|---|
| Explaining the genetic code and wobble pairing | `genetic-code-wobble` | `bio.biochem.ribosome-and-trna-biochemistry` |
| Comparing translation initiation in bacteria and eukaryotes | `translation-initiation` | `genetic-code-wobble` |
| Tracing elongation and termination | `translation-elongation-termination` | `translation-initiation` |

### Molecular techniques

| Topic | Slug | Needs |
|---|---|---|
| Using restriction enzymes and maps | `restriction-mapping` | `bio.intro1.cloning-vectors` |
| Designing cloning strategies | `cloning-strategies` | `restriction-mapping` |
| Designing PCR primers and reactions | `pcr-design` | `bio.biochem.nucleic-acid-stability` |
| Quantifying nucleic acids by qPCR | `qpcr` | `pcr-design`, `bio.intro1.measuring-gene-expression` |
| Making site-directed mutants | `site-directed-mutagenesis` | `pcr-design`, `cloning-strategies` |
| Detecting sequences by Southern and northern blots | `nucleic-acid-blotting` | `restriction-mapping` |
| Explaining Sanger sequencing chemistry | `sanger-sequencing` | `pcr-design`, `bio.genetics.sequencing-technologies` |
| Building genomic and cDNA libraries | `dna-libraries` | `cloning-strategies` |
| Measuring regulation with reporter genes | `reporter-assays` | `cloning-strategies` |
| Detecting protein interactions with two-hybrid and pull-down assays | `protein-interaction-assays` | `cloning-strategies` |
| Detecting protein-DNA binding with mobility shift assays | `emsa` | `general-transcription-factors` |
| Mapping protein-DNA binding with ChIP | `chip-assays` | `qpcr`, `general-transcription-factors` |
| Analyzing RNA-seq experiments | `rna-seq` | `qpcr`, `bio.genetics.genome-assembly-and-annotation` |
| Aligning sequences and searching databases | `sequence-alignment` | `bio.genetics.comparative-genomics` |
| Designing experiments to test gene function | `gene-function-experiments` | `reporter-assays`, `site-directed-mutagenesis`, `rna-seq` |

## bio.immunology: 40 topics

Follows `bio.cell-mol`, `bio.micro`, `bio.genetics`. Level uni-upper.


### Innate immunity

| Topic | Slug | Needs |
|---|---|---|
| Describing immune cells and lymphoid organs | `immune-cells-organs` | `bio.micro.innate-defence-mechanisms` |
| Explaining pattern recognition receptors | `pattern-recognition` | `immune-cells-organs`, `bio.cell-mol.receptor-ligand-binding` |
| Tracing complement pathways | `complement` | `pattern-recognition` |
| Explaining phagocytosis and inflammatory signals | `inflammation-mechanisms` | `pattern-recognition` |
| Explaining natural killer cell recognition | `nk-cells` | `inflammation-mechanisms` |
| Explaining interferons and antiviral responses | `interferons` | `pattern-recognition`, `bio.micro.virus-replication-strategies` |

### Antibodies and receptor diversity

| Topic | Slug | Needs |
|---|---|---|
| Relating antibody classes to functions | `antibody-classes` | `bio.micro.antibody-structure` |
| Analyzing antigen-antibody binding | `antigen-antibody-binding` | `antibody-classes`, `bio.cell-mol.receptor-ligand-binding` |
| Explaining V(D)J recombination | `vdj-recombination` | `antibody-classes`, `bio.genetics.recombination-mechanisms` |
| Calculating antigen receptor diversity | `receptor-diversity` | `vdj-recombination` |
| Explaining class switching and somatic hypermutation | `class-switching-shm` | `vdj-recombination` |

### Antigen presentation

| Topic | Slug | Needs |
|---|---|---|
| Describing MHC structure and polymorphism | `mhc-structure` | `immune-cells-organs` |
| Tracing class I antigen processing | `class-i-processing` | `mhc-structure`, `bio.cell-mol.ubiquitin-proteasome` |
| Tracing class II antigen processing | `class-ii-processing` | `mhc-structure`, `bio.cell-mol.receptor-mediated-endocytosis` |
| Explaining cross-presentation | `cross-presentation` | `class-i-processing`, `class-ii-processing` |

### Lymphocyte development and activation

| Topic | Slug | Needs |
|---|---|---|
| Describing T cell receptor structure and signalling | `tcr-signalling` | `mhc-structure`, `bio.cell-mol.rtk-and-ras-pathway` |
| Explaining thymic selection | `thymic-selection` | `tcr-signalling` |
| Explaining B cell development | `b-cell-development` | `vdj-recombination` |
| Explaining T cell activation and costimulation | `t-cell-activation` | `tcr-signalling`, `cross-presentation`, `bio.micro.lymphocyte-activation` |
| Comparing helper T cell subsets | `helper-subsets` | `t-cell-activation` |
| Describing cytokines and their receptors | `cytokines` | `helper-subsets` |
| Explaining cytotoxic T cell killing | `ctl-killing` | `t-cell-activation`, `bio.cell-mol.apoptosis-pathways` |
| Explaining B cell activation and germinal centers | `germinal-centers` | `helper-subsets`, `class-switching-shm` |
| Explaining immunological memory | `immune-memory` | `germinal-centers`, `ctl-killing` |
| Describing mucosal immunity | `mucosal-immunity` | `antibody-classes`, `helper-subsets` |

### Tolerance and disease

| Topic | Slug | Needs |
|---|---|---|
| Explaining central and peripheral tolerance | `tolerance` | `thymic-selection`, `b-cell-development` |
| Explaining regulatory T cells | `regulatory-t-cells` | `tolerance`, `helper-subsets` |
| Comparing hypersensitivity types | `hypersensitivity` | `antibody-classes`, `helper-subsets`, `complement` |
| Explaining autoimmune disease mechanisms | `autoimmunity-mechanisms` | `regulatory-t-cells` |
| Explaining primary immunodeficiencies | `primary-immunodeficiency` | `b-cell-development`, `thymic-selection` |
| Explaining HIV and acquired immunodeficiency | `hiv-immunology` | `bio.intro1.retroviruses`, `helper-subsets` |
| Explaining transplant rejection | `transplant-rejection` | `mhc-structure`, `t-cell-activation` |
| Explaining blood group and Rh immunology | `blood-group-immunology` | `antibody-classes`, `complement` |
| Explaining tumor immunity and checkpoint therapy | `tumor-immunology` | `ctl-killing`, `regulatory-t-cells` |
| Explaining immune evasion by pathogens | `immune-evasion` | `immune-memory`, `bio.micro.virulence-factors` |

### Applied immunology

| Topic | Slug | Needs |
|---|---|---|
| Designing vaccines from immunological principles | `vaccine-design` | `immune-memory`, `bio.micro.vaccine-types` |
| Making monoclonal antibodies | `monoclonal-antibodies` | `germinal-centers` |
| Describing antibody therapeutics | `antibody-therapeutics` | `monoclonal-antibodies` |
| Using ELISA and other immunoassays | `elisa` | `antigen-antibody-binding` |
| Analyzing cells by flow cytometry | `flow-cytometry` | `antigen-antibody-binding` |

## bio.developmental: 34 topics

Follows `bio.cell-mol`, `bio.genetics`, `bio.intro2`. Level uni-upper.


### Principles

| Topic | Slug | Needs |
|---|---|---|
| Comparing modes of cell fate specification | `fate-specification-modes` | `bio.intro1.developmental-gene-regulation`, `bio.intro2.early-animal-development` |
| Tracing fate maps and cell lineages | `fate-mapping` | `fate-specification-modes` |
| Explaining induction and competence | `induction-competence` | `fate-specification-modes`, `bio.cell-mol.receptor-ligand-binding` |
| Explaining morphogen gradients | `morphogen-gradients` | `induction-competence` |
| Using signalling families in development | `developmental-signalling` | `morphogen-gradients`, `bio.cell-mol.developmental-signalling-pathways` |
| Explaining lateral inhibition with Notch | `lateral-inhibition` | `developmental-signalling` |
| Using model organisms and experimental embryology | `experimental-embryology` | `fate-mapping`, `bio.intro1.model-organisms` |

### Early development

| Topic | Slug | Needs |
|---|---|---|
| Explaining fertilization and egg activation | `fertilization` | `bio.intro2.early-animal-development` |
| Comparing cleavage patterns | `cleavage-patterns` | `fertilization` |
| Describing sea urchin gastrulation | `sea-urchin-gastrulation` | `cleavage-patterns` |
| Describing amphibian gastrulation and the organizer | `amphibian-organizer` | `cleavage-patterns`, `induction-competence` |
| Describing gastrulation in birds and mammals | `amniote-gastrulation` | `amphibian-organizer` |

### Axis formation

| Topic | Slug | Needs |
|---|---|---|
| Specifying the Drosophila anterior-posterior axis | `drosophila-ap-axis` | `morphogen-gradients` |
| Tracing the Drosophila segmentation gene hierarchy | `segmentation-genes` | `drosophila-ap-axis` |
| Explaining Hox genes and segment identity | `hox-genes` | `segmentation-genes` |
| Specifying the Drosophila dorsal-ventral axis | `drosophila-dv-axis` | `drosophila-ap-axis` |
| Specifying vertebrate body axes | `vertebrate-axes` | `amniote-gastrulation`, `hox-genes` |
| Explaining left-right asymmetry | `left-right-asymmetry` | `vertebrate-axes` |
| Explaining planar cell polarity | `planar-cell-polarity` | `developmental-signalling` |

### Organogenesis

| Topic | Slug | Needs |
|---|---|---|
| Explaining neural induction and neurulation | `neurulation` | `amphibian-organizer` |
| Patterning the neural tube | `neural-tube-patterning` | `neurulation`, `morphogen-gradients` |
| Describing neural crest migration and fates | `neural-crest` | `neurulation` |
| Describing somitogenesis and the segmentation clock | `somitogenesis` | `vertebrate-axes` |
| Explaining limb bud patterning | `limb-patterning` | `developmental-signalling`, `hox-genes` |
| Describing heart development | `heart-development` | `amniote-gastrulation` |
| Describing kidney development by reciprocal induction | `kidney-development` | `induction-competence` |
| Explaining epithelial-mesenchymal transitions and tissue folding | `morphogenesis-mechanics` | `bio.cell-mol.cell-migration`, `bio.cell-mol.adhesion-molecules` |
| Explaining apoptosis in shaping tissues | `developmental-apoptosis` | `bio.cell-mol.apoptosis-pathways`, `limb-patterning` |

### Germ line, growth and regeneration

| Topic | Slug | Needs |
|---|---|---|
| Explaining germ cell specification | `germ-cells` | `fate-specification-modes` |
| Explaining gonad development and sex determination | `sex-determination-development` | `bio.intro1.sex-determination-systems`, `germ-cells` |
| Explaining metamorphosis and hormonal control | `metamorphosis` | `bio.cell-mol.nuclear-receptors` |
| Explaining stem cells and regeneration | `regeneration` | `bio.cell-mol.stem-cell-niches` |
| Explaining pluripotency and reprogramming | `pluripotency-reprogramming` | `regeneration` |
| Explaining teratogens and birth defects | `teratogens` | `neural-tube-patterning`, `heart-development` |

## bio.plant: 40 topics

Follows `bio.biochem`, `bio.cell-mol`, `bio.intro2`. Level uni-upper.


### Plant cells and water

| Topic | Slug | Needs |
|---|---|---|
| Describing plant cell walls | `plant-cell-walls` | `bio.intro2.plant-tissues-and-organs` |
| Describing vacuoles and plastids | `vacuoles-plastids` | `plant-cell-walls` |
| Finding solute and pressure potentials in plant cells | `water-potential` | `bio.hs2.water-potential`, `bio.intro2.xylem-water-transport` |
| Explaining water uptake by roots | `root-water-uptake` | `water-potential` |
| Explaining the cohesion-tension mechanism | `cohesion-tension` | `water-potential` |
| Explaining stomatal regulation | `stomatal-regulation` | `cohesion-tension` |
| Calculating transpiration and water-use efficiency | `transpiration-rates` | `stomatal-regulation` |
| Explaining pressure flow in phloem | `phloem-translocation` | `water-potential` |
| Explaining phloem loading and unloading | `phloem-loading` | `phloem-translocation`, `bio.cell-mol.secondary-active-transport` |

### Nutrition

| Topic | Slug | Needs |
|---|---|---|
| Explaining mineral nutrient roles and deficiencies | `mineral-nutrition` | `bio.intro2.plant-nutrition-and-soil` |
| Explaining ion uptake by roots | `ion-uptake` | `mineral-nutrition`, `bio.cell-mol.ion-pump-energetics` |
| Explaining nitrogen assimilation in plants | `nitrogen-assimilation` | `mineral-nutrition` |
| Explaining legume-rhizobium signalling | `rhizobium-signalling` | `nitrogen-assimilation` |
| Explaining mycorrhizal symbiosis | `mycorrhizae` | `ion-uptake`, `bio.intro2.fungal-life-cycles` |

### Photosynthesis and carbon metabolism

| Topic | Slug | Needs |
|---|---|---|
| Explaining light absorption by pigments | `photosynthetic-pigments` | `vacuoles-plastids`, `bio.biochem.biological-redox-energetics` |
| Tracing the Z-scheme through both photosystems | `light-reactions` | `photosynthetic-pigments`, `bio.biochem.respiratory-complexes`, `bio.hs2.light-reactions-details` |
| Explaining photophosphorylation | `photophosphorylation` | `light-reactions`, `bio.biochem.atp-synthase-mechanism` |
| Explaining Calvin cycle regeneration and regulation | `calvin-cycle` | `photophosphorylation`, `bio.hs2.calvin-cycle-details` |
| Explaining Rubisco and photorespiration | `rubisco-photorespiration` | `calvin-cycle`, `bio.intro1.photorespiration` |
| Comparing C4 and CAM photosynthesis | `c4-cam` | `rubisco-photorespiration` |
| Analyzing photosynthesis responses to light and CO2 | `photosynthesis-responses` | `c4-cam` |
| Explaining starch and sucrose synthesis | `starch-sucrose` | `calvin-cycle` |
| Explaining plant respiration and the alternative oxidase | `plant-respiration` | `bio.biochem.citric-acid-cycle-reactions` |

### Hormones and signals

| Topic | Slug | Needs |
|---|---|---|
| Explaining auxin transport and action | `auxin` | `bio.intro2.plant-hormones` |
| Explaining gibberellins and cytokinins | `gibberellins-cytokinins` | `auxin` |
| Explaining ethylene and abscisic acid | `ethylene-aba` | `auxin` |
| Explaining brassinosteroids and jasmonates | `brassinosteroids-jasmonates` | `ethylene-aba` |
| Explaining phytochrome signalling | `phytochrome` | `bio.intro2.tropisms-and-photoperiodism` |
| Explaining blue-light responses | `blue-light-responses` | `phytochrome`, `stomatal-regulation` |
| Explaining circadian clocks in plants | `plant-circadian` | `phytochrome` |

### Development

| Topic | Slug | Needs |
|---|---|---|
| Describing plant embryogenesis | `plant-embryogenesis` | `auxin`, `bio.intro2.seed-development-and-germination` |
| Explaining shoot and root meristem maintenance | `meristem-maintenance` | `plant-embryogenesis`, `gibberellins-cytokinins` |
| Explaining control of flowering | `flowering-control` | `plant-circadian`, `gibberellins-cytokinins` |
| Explaining floral organ identity with the ABC model | `abc-model` | `bio.intro2.flower-structure-and-pollination` |
| Explaining seed dormancy and germination control | `seed-dormancy` | `ethylene-aba`, `gibberellins-cytokinins` |
| Explaining senescence and abscission | `senescence-abscission` | `ethylene-aba` |

### Stress and defence

| Topic | Slug | Needs |
|---|---|---|
| Explaining drought and salt stress responses | `abiotic-stress` | `ethylene-aba`, `transpiration-rates` |
| Explaining heat and cold stress responses | `temperature-stress` | `abiotic-stress` |
| Explaining plant immunity | `plant-immunity` | `bio.intro2.plant-defences`, `brassinosteroids-jasmonates` |
| Describing plant secondary metabolites | `secondary-metabolites` | `plant-immunity` |

## engr.surveying: 31 topics

Follows `math.precalc`, `math.stats`. Level uni-lower.


### Measurements and errors

| Topic | Slug | Needs |
|---|---|---|
| Classifying surveys, datums and units | `survey-fundamentals` | `math.precalc.law-sines-review-applications` |
| Propagating errors in survey measurements | `survey-error-propagation` | `survey-fundamentals`, `math.stats.combine-random-variables` |
| Weighting and adjusting repeated observations | `weighted-observations` | `survey-error-propagation` |
| Correcting taped distances | `taping-corrections` | `survey-fundamentals` |
| Measuring distances electronically | `edm` | `taping-corrections` |

### Leveling

| Topic | Slug | Needs |
|---|---|---|
| Finding elevations by differential leveling | `survey-leveling` | moved from `engr.transportation`, keeps its needs; level becomes uni-lower |
| Adjusting level circuits | `level-circuit-adjustment` | `survey-leveling`, `weighted-observations` |
| Running profile and cross-section leveling | `profile-leveling` | `survey-leveling` |
| Finding elevations by trigonometric leveling | `trigonometric-leveling` | `survey-leveling`, `edm` |
| Correcting for curvature and refraction | `curvature-refraction` | `trigonometric-leveling` |

### Angles and traverses

| Topic | Slug | Needs |
|---|---|---|
| Measuring horizontal and vertical angles | `angles-and-directions` | `survey-fundamentals` |
| Collecting data with total stations | `total-station-surveys` | `edm`, `angles-and-directions` |
| Converting bearings and azimuths | `bearings-azimuths` | `angles-and-directions` |
| Computing traverse latitudes and departures | `latitudes-departures` | `bearings-azimuths` |
| Finding traverse misclosure and precision | `traverse-misclosure` | `latitudes-departures` |
| Adjusting traverses by the compass rule | `compass-rule` | `traverse-misclosure` |
| Computing coordinates from adjusted traverses | `traverse-coordinates` | `compass-rule` |
| Solving inverse and intersection problems | `coordinate-geometry-survey` | `traverse-coordinates` |
| Reading metes-and-bounds property descriptions | `property-descriptions` | `bearings-azimuths` |

### Areas and volumes

| Topic | Slug | Needs |
|---|---|---|
| Computing areas by coordinates | `area-by-coordinates` | `traverse-coordinates` |
| Computing areas of irregular boundaries | `irregular-areas` | `area-by-coordinates` |
| Partitioning land areas | `area-partitioning` | `area-by-coordinates` |
| Drawing contours from spot elevations | `contouring` | `profile-leveling` |
| Computing earthwork volumes | `cross-sections-and-earthwork` | moved from `engr.transportation`, keeps its needs; level becomes uni-lower |
| Balancing cut and fill with mass diagrams | `mass-diagrams` | `cross-sections-and-earthwork` |
| Computing borrow-pit volumes | `borrow-pit-volumes` | `contouring` |

### Coordinate systems and layout

| Topic | Slug | Needs |
|---|---|---|
| Using state plane and UTM coordinates | `map-projections-coordinates` | `traverse-coordinates` |
| Converting latitude and longitude | `geodetic-coordinates` | `map-projections-coordinates` |
| Positioning with GNSS | `gnss-positioning` | `geodetic-coordinates` |
| Describing lidar and photogrammetry | `remote-sensing-survey` | `gnss-positioning` |
| Staking out construction layout | `construction-staking` | `coordinate-geometry-survey` |

## engr.construction: 30 topics

Follows `engr.economics`, `engr.surveying`, `engr.soil-mechanics`, `math.probstat`. Level uni-upper.


### Project delivery and contracts

| Topic | Slug | Needs |
|---|---|---|
| Comparing project delivery methods | `project-delivery` | `engr.economics.cost-types` |
| Comparing construction contract types | `contract-types` | `project-delivery` |
| Reading contract documents and specifications | `contract-documents` | `contract-types` |
| Interpreting construction drawings | `construction-drawings` | `engr.surveying.construction-staking` |

### Estimating

| Topic | Slug | Needs |
|---|---|---|
| Taking off quantities | `quantity-takeoff` | `construction-drawings`, `engr.surveying.cross-sections-and-earthwork` |
| Building unit-price estimates | `unit-price-estimates` | `quantity-takeoff`, `engr.economics.cost-estimation` |
| Estimating labor and equipment costs | `labor-equipment-costs` | `unit-price-estimates` |
| Adding overhead, contingency and markup | `bid-pricing` | `labor-equipment-costs` |
| Finding owning and operating costs of equipment | `equipment-costs` | `engr.economics.depreciation-methods` |

### Planning and scheduling

| Topic | Slug | Needs |
|---|---|---|
| Building work breakdown structures | `work-breakdown` | `project-delivery` |
| Scheduling with precedence diagrams and lags | `precedence-diagrams` | `work-breakdown`, `engr.economics.critical-path-method` |
| Estimating schedule risk with PERT | `pert` | `precedence-diagrams`, `math.probstat.normal-linear-combinations` |
| Leveling resources | `resource-leveling` | `precedence-diagrams`, `engr.economics.float-and-crashing` |
| Finding least-cost schedules by crashing | `time-cost-tradeoff` | `engr.economics.float-and-crashing`, `labor-equipment-costs` |
| Scheduling repetitive work with linear scheduling | `linear-scheduling` | `precedence-diagrams` |
| Building cost-loaded schedules and cash flow curves | `cash-flow-curves` | `precedence-diagrams`, `bid-pricing` |
| Forecasting cost and schedule with earned value | `earned-value-forecasts` | `engr.economics.earned-value`, `cash-flow-curves` |
| Managing change orders and delay claims | `change-orders` | `contract-documents`, `earned-value-forecasts` |

### Operations and productivity

| Topic | Slug | Needs |
|---|---|---|
| Finding equipment productivity | `equipment-productivity` | `labor-equipment-costs` |
| Finding soil swell and shrinkage | `soil-swell-shrink` | `engr.soil-mechanics.phase-relations` |
| Planning earthmoving operations | `earthmoving-operations` | `equipment-productivity`, `soil-swell-shrink`, `engr.surveying.mass-diagrams` |
| Balancing hauling and loading fleets | `fleet-balancing` | `earthmoving-operations` |
| Measuring labor productivity | `labor-productivity` | `labor-equipment-costs` |
| Designing formwork for concrete pressure | `formwork-pressure` | `engr.mech-materials.flexure-formula` |
| Planning concrete placement | `concrete-operations` | `formwork-pressure` |
| Planning crane lifts | `crane-lifts` | `engr.statics.moment-about-an-axis` |

### Safety and quality

| Topic | Slug | Needs |
|---|---|---|
| Applying construction safety regulations | `construction-safety` | `project-delivery` |
| Analyzing excavation and trench safety | `trench-safety` | `construction-safety`, `engr.soil-mechanics.rankine-earth-pressure` |
| Planning temporary erosion and sediment control | `erosion-control` | `engr.surveying.contouring` |
| Applying quality control sampling | `construction-quality-control` | `contract-documents`, `math.stats.standard-deviation-calc` |

## engr.programming-languages: 40 topics

Follows `engr.theory`. Level uni-upper.


### Syntax

| Topic | Slug | Needs |
|---|---|---|
| Comparing programming paradigms | `programming-paradigms` | `engr.programming.functions-as-values` |
| Describing syntax with BNF | `bnf-syntax` | `engr.theory.context-free-grammars` |
| Tokenizing source code | `lexical-analysis` | `engr.theory.regular-expressions`, `engr.theory.dfa` |
| Writing recursive-descent parsers | `recursive-descent-parsing` | `bnf-syntax`, `engr.theory.parse-trees-and-ambiguity` |
| Handling precedence and associativity | `precedence-associativity` | `recursive-descent-parsing` |
| Building abstract syntax trees | `abstract-syntax-trees` | `recursive-descent-parsing` |
| Using macros and metaprogramming | `macros` | `abstract-syntax-trees` |

### Interpreters and semantics

| Topic | Slug | Needs |
|---|---|---|
| Writing an expression interpreter | `expression-interpreter` | `abstract-syntax-trees` |
| Binding variables with environments | `environments` | `expression-interpreter` |
| Comparing static and dynamic scope | `static-dynamic-scope` | `environments`, `engr.programming.local-and-global-scope` |
| Implementing closures | `closures` | `static-dynamic-scope` |
| Adding first-class functions to an interpreter | `first-class-functions-interpreter` | `closures` |
| Comparing parameter passing modes | `parameter-passing` | `environments` |
| Implementing mutable state with stores | `stores-and-mutation` | `environments` |
| Writing operational semantics | `operational-semantics` | `expression-interpreter` |
| Evaluating lambda calculus terms | `lambda-calculus` | `operational-semantics`, `engr.programming.lambda-expressions` |
| Encoding data in the lambda calculus | `church-encodings` | `lambda-calculus` |
| Comparing evaluation strategies | `evaluation-strategies` | `lambda-calculus` |
| Implementing exceptions and continuations | `continuations` | `first-class-functions-interpreter`, `engr.programming.exceptions` |

### Functional programming

| Topic | Slug | Needs |
|---|---|---|
| Writing pure functional programs | `pure-functional-programming` | `programming-paradigms`, `engr.programming.recursion-on-lists` |
| Using map, filter and fold | `map-filter-fold` | `pure-functional-programming` |
| Using algebraic data types and pattern matching | `algebraic-data-types` | `pure-functional-programming` |
| Writing tail-recursive functions | `tail-recursion` | `pure-functional-programming`, `engr.programming.recursion-vs-iteration` |
| Using lazy evaluation | `lazy-evaluation` | `evaluation-strategies`, `map-filter-fold` |

### Types

| Topic | Slug | Needs |
|---|---|---|
| Writing type rules | `type-rules` | `operational-semantics` |
| Type checking expressions | `type-checking` | `type-rules`, `abstract-syntax-trees` |
| Proving type safety by progress and preservation | `type-safety` | `type-checking` |
| Using parametric polymorphism | `parametric-polymorphism` | `type-checking` |
| Inferring types by unification | `type-inference` | `parametric-polymorphism` |
| Using subtyping | `subtyping` | `type-checking` |
| Comparing static and dynamic typing | `static-vs-dynamic-typing` | `type-checking` |
| Comparing nominal and structural typing | `nominal-structural-typing` | `subtyping` |

### Objects, memory and other paradigms

| Topic | Slug | Needs |
|---|---|---|
| Implementing objects and dynamic dispatch | `dynamic-dispatch` | `subtyping`, `engr.programming.inheritance` |
| Comparing inheritance, composition and mixins | `inheritance-mixins` | `dynamic-dispatch` |
| Describing garbage collection | `garbage-collection` | `stores-and-mutation` |
| Comparing ownership and reference counting | `ownership-refcounting` | `garbage-collection` |
| Writing logic programs | `logic-programming` | `programming-paradigms`, `type-inference` |
| Comparing concurrency models in languages | `language-concurrency` | `closures` |
| Comparing compilation and interpretation | `compilation-pipeline` | `abstract-syntax-trees` |
| Compiling expressions to stack machine code | `stack-code-generation` | `compilation-pipeline`, `engr.data-structures.stacks` |

## engr.process-design-safety: 30 topics

Follows `engr.reactors`, `engr.separations`, `engr.economics`. Level uni-upper.


### Process synthesis

| Topic | Slug | Needs |
|---|---|---|
| Developing flowsheets from reaction routes | `flowsheet-synthesis` | `engr.mass-energy-balances.process-flowsheets`, `engr.reactors.complex-reaction-networks` |
| Using the design hierarchy | `design-hierarchy` | `flowsheet-synthesis` |
| Choosing recycle and purge structure | `recycle-structure` | `design-hierarchy`, `engr.mass-energy-balances.reactive-recycle-and-purge` |
| Sequencing distillation columns | `column-sequencing` | `design-hierarchy`, `engr.separations.key-components` |
| Finding minimum utilities by pinch analysis | `pinch-analysis` | `engr.mass-energy-balances.nonreactive-energy-balances` |
| Designing heat exchanger networks | `heat-exchanger-networks` | `pinch-analysis` |
| Using process simulators | `process-simulators` | `engr.mass-energy-balances.process-simulation-sequential` |
| Choosing thermodynamic models in simulation | `simulation-thermo-models` | `process-simulators`, `engr.cheme-thermo.activity-coefficients` |

### Economics of design

| Topic | Slug | Needs |
|---|---|---|
| Sizing equipment for cost estimates | `equipment-sizing` | `flowsheet-synthesis` |
| Estimating capital cost with factored methods | `capital-cost-estimation` | `equipment-sizing`, `engr.economics.cost-estimation` |
| Estimating operating costs | `operating-costs` | `capital-cost-estimation` |
| Evaluating process profitability | `process-profitability` | `operating-costs`, `engr.economics.after-tax-cash-flows` |
| Optimizing design variables economically | `design-optimization` | `process-profitability`, `engr.separations.optimum-feed-and-reflux` |
| Assessing environmental impact of processes | `process-environmental-impact` | `process-profitability` |
| Calculating atom economy and E-factors for processes | `green-metrics` | `flowsheet-synthesis` |

### Hazards and consequences

| Topic | Slug | Needs |
|---|---|---|
| Finding flammability limits of mixtures | `flammability-limits` | `engr.mass-energy-balances.process-safety-basics` |
| Designing inerting and purging | `inerting-purging` | `flammability-limits` |
| Estimating toxic exposure against limits | `toxic-exposure` | `engr.mass-energy-balances.process-safety-basics` |
| Modeling release rates | `source-models` | `toxic-exposure` |
| Modeling dispersion of releases | `dispersion-models` | `source-models` |
| Estimating fire and explosion consequences | `fire-explosion` | `flammability-limits` |
| Sizing pressure relief devices | `relief-sizing` | `source-models` |
| Assessing reactive hazards with calorimetry | `reactive-hazards` | `engr.reactors.runaway-reactions` |

### Hazard analysis and risk

| Topic | Slug | Needs |
|---|---|---|
| Conducting HAZOP studies | `hazop` | `flowsheet-synthesis`, `engr.mass-energy-balances.process-safety-basics` |
| Building fault trees | `fault-trees` | `hazop` |
| Building event trees | `event-trees` | `fault-trees` |
| Using layers of protection analysis | `lopa` | `event-trees` |
| Calculating individual and societal risk | `risk-calculation` | `lopa` |
| Applying inherently safer design | `inherently-safer-design` | `hazop` |
| Applying process safety management | `process-safety-management` | `hazop` |

