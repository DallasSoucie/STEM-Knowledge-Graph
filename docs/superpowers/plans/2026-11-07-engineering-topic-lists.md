# Topic lists: engineering

Draft for approval. Covers all 44 engineering courses: the common core, the shared controls course, and the civil, chemical, mechanical, electrical and computer/software courses. In the Needs column, a plain name is in the same course, a short prefix (`statics.`, `circuits.`) names an engineering course, and math, physics, chemistry and biology topics are written with their full ID (`math.calc3.divergence`).

## Decisions already made

These came from the questions before drafting:

- **One shared controls course.** `engr.controls` serves mechanical, electrical and chemical students. `engr.process-control` builds on it with only process-specific topics. The electrical slot freed by dropping `control-systems` becomes `engr.dsp`.
- **Six new courses:** `economics` (every FE exam), `environmental` (civil), `cheme-thermo` (chemical), `measurements` (mechanical), `embedded` (computer engineering), `theory` (ABET's computer science theory requirement).
- **Civil design split:** `steel-design` and `concrete-design` are separate courses.
- **Chemical transport renamed:** `transport` becomes `mass-transfer`, building on core fluids and mechanical heat transfer rather than repeating them.
- **One plan:** every course is drafted here for a single approval.

## What each discipline needs, and where it lives

- **Civil** needs statics, mechanics of materials, fluids, materials (concrete, asphalt, aggregates, wood), probability for hydrology and traffic, surveying-style geometry, project scheduling and economics. Surveying topics (leveling, earthwork, curve layout) sit in transportation. Scheduling (critical path, earned value) sits in economics, so every discipline reaches it.
- **Chemical** needs the most chemistry: physical chemistry I is a prerequisite of mass and energy balances. The thermodynamics chain runs from physics to core thermo, then pchem1, then cheme-thermo, then separations. Bioprocess kinetics (Monod) is homed in environmental, and reactors leaves bioreactors out.
- **Mechanical** needs both thermal and mechanical depth, as ABET requires. Mechanisms (linkage synthesis, cams, balancing) sit in machine design. Instrumentation, uncertainty and sensors get their own measurements course, matching the FE Mechanical spec.
- **Electrical** leans on physics more than any other discipline. University electromagnetism theory (`physics.em-theory`) already homes Maxwell's equations, boundary conditions, plane waves, waveguides and dipole radiation. So `em-fields` follows it and adds only engineering topics: transmission lines, the Smith chart, matching, antennas, skin effect and shielding.
- **Computer and software** builds on discrete math, which already homes Boolean algebra, K-maps, number bases, big-O, BFS/DFS, shortest paths, spanning trees, binary search trees and Huffman codes. Data structures and algorithms implement and prove these rather than reteach them.

## Course sequence choices

- **Controls follows signals and dynamics.** Bode plots are homed in circuits, because electronics needs them before controls. Mechanical and chemical students therefore reach the circuits and signals topics that controls actually uses: the graph only asks for those ancestors, not the whole courses.
- **Mass and energy balances follows thermo.** Property tables and steady-flow energy balances are homed in core thermo, so balances use them rather than reteach steam tables.
- **Reactors follows mass transfer and cheme-thermo**, for catalyst effectiveness and equilibrium conversion. **Process control follows controls and reactors.**
- **Measurements follows controls**, for instrument dynamics, and uses signals topics for sampling and aliasing.
- **Databases follows operating systems** (storage devices and buffer management). **Networks, software engineering and theory follow algorithms.**

## Budgets

Every course comes in well under the catalog budget, as biology and chemistry did. These topics are written at the same grain as the biology courses you accepted: one lesson-sized skill with four knowledge points.

The catalog budgets assumed a finer grain, closer to the university physics courses (110 to 135 topics each). The best candidates for a finer split are the problem-solving core: statics, dynamics, mechanics of materials, thermo, fluids and circuits. There, a topic like "Analyzing frames" could become frames with two-force members, frames with pulleys, and machines. If you want that, approve the structure first and I'll split those courses before building.

| Course | Follows now | Proposed follows | Topics | Budget now | Proposed budget |
|---|---|---|---|---|---|
| programming | `math.alg2` | `math.precalc` | 91 | 170 | 100 |
| data-structures | `engr.programming` | `engr.programming`, `math.discrete` | 54 | 170 | 60 |
| statics | `physics.mechanics` | `physics.mechanics`, `math.calc3`, `math.linalg` | 60 | 130 | 65 |
| dynamics | `engr.statics` | `engr.statics` | 46 | 140 | 50 |
| mech-materials | `engr.statics` | `engr.statics`, `math.diffeq`, `physics.waves-thermo-optics` | 54 | 150 | 60 |
| thermo | `physics.waves-thermo-optics`, `math.calc2` | `physics.waves-thermo-optics`, `math.calc3` | 70 | 160 | 80 |
| fluids | `engr.dynamics`, `math.calc3` | `engr.dynamics`, `engr.thermo`, `math.calc3` | 57 | 150 | 65 |
| circuits | `physics.em`, `math.diffeq` | `physics.em`, `math.diffeq`, `math.linalg` | 62 | 170 | 70 |
| materials | `chem.gen1`, `engr.mech-materials` | `chem.gen2`, `engr.mech-materials`, `math.stats` | 56 | 120 | 65 |
| digital-logic | `math.discrete` | `math.discrete`, `engr.programming` | 44 | 130 | 50 |
| signals | `engr.circuits`, `math.diffeq` | `engr.circuits` | 42 | 140 | 50 |
| economics | (new) | `math.precalc`, `math.stats` | 34 | - | 40 |
| controls | `engr.signals`, `engr.dynamics` | `engr.signals`, `engr.dynamics` | 43 | 140 | 50 |
| structural-analysis | `engr.statics`, `engr.mech-materials` | `engr.mech-materials`, `engr.dynamics`, `math.linalg` | 47 | 130 | 55 |
| soil-mechanics | `engr.mech-materials`, `engr.fluids` | `engr.materials`, `engr.fluids` | 52 | 130 | 60 |
| hydraulics | `engr.fluids` | `engr.soil-mechanics`, `math.probstat` | 41 | 130 | 45 |
| steel-design | (new) | `engr.structural-analysis`, `engr.materials` | 31 | - | 35 |
| concrete-design | `engr.structural-analysis` | `engr.structural-analysis`, `engr.soil-mechanics` | 35 | 130 | 40 |
| transportation | `math.probstat` | `engr.soil-mechanics`, `math.probstat` | 35 | 130 | 40 |
| environmental | (new) | `engr.hydraulics`, `chem.gen2`, `bio.micro` | 32 | - | 35 |
| mass-energy-balances | `chem.gen1`, `math.calc2` | `engr.thermo`, `chem.pchem1`, `math.diffeq`, `math.linalg` | 36 | 140 | 40 |
| cheme-thermo | (new) | `engr.mass-energy-balances`, `chem.pchem1` | 33 | - | 40 |
| mass-transfer | (new) | `engr.mass-energy-balances`, `engr.heat-transfer` | 24 | - | 30 |
| separations | `engr.transport`, `engr.thermo` | `engr.mass-transfer`, `engr.cheme-thermo` | 34 | 140 | 40 |
| reactors | `engr.mass-energy-balances`, `chem.pchem1` | `engr.mass-transfer`, `engr.cheme-thermo` | 37 | 140 | 40 |
| process-control | `engr.mass-energy-balances`, `math.diffeq` | `engr.controls`, `engr.reactors` | 27 | 140 | 30 |
| heat-transfer | `engr.thermo`, `engr.fluids` | `engr.thermo`, `engr.fluids`, `math.diffeq` | 56 | 140 | 65 |
| machine-design | `engr.mech-materials`, `engr.dynamics` | `engr.materials`, `engr.fluids`, `math.probstat` | 47 | 140 | 55 |
| vibrations | `engr.dynamics`, `math.diffeq` | `engr.dynamics`, `math.diffeq`, `math.linalg` | 28 | 140 | 35 |
| manufacturing | `engr.materials` | `engr.machine-design` | 32 | 140 | 35 |
| measurements | (new) | `engr.controls`, `engr.fluids`, `engr.mech-materials`, `math.probstat`, `engr.programming` | 23 | - | 25 |
| electronics | `engr.circuits` | `engr.controls`, `engr.digital-logic`, `physics.modern` | 58 | 150 | 65 |
| em-fields | `physics.em`, `math.calc3` | `physics.em-theory`, `engr.circuits` | 35 | 150 | 40 |
| power | `engr.circuits`, `engr.em-fields` | `engr.em-fields`, `engr.electronics`, `math.numerical` | 43 | 150 | 50 |
| communications | `engr.signals`, `math.probstat` | `engr.em-fields`, `engr.signals`, `math.probstat`, `math.discrete` | 40 | 150 | 45 |
| dsp | (new) | `engr.signals`, `engr.digital-logic`, `math.numerical` | 35 | - | 40 |
| algorithms | `engr.data-structures`, `math.discrete` | `engr.data-structures`, `math.discrete`, `math.probstat`, `math.linalg` | 44 | 140 | 50 |
| architecture | `engr.digital-logic`, `engr.programming` | `engr.digital-logic`, `engr.programming` | 39 | 140 | 45 |
| operating-systems | `engr.architecture`, `engr.data-structures` | `engr.architecture`, `engr.data-structures` | 42 | 140 | 50 |
| databases | `engr.data-structures` | `engr.operating-systems` | 34 | 140 | 40 |
| networks | `engr.operating-systems` | `engr.operating-systems`, `engr.algorithms` | 32 | 140 | 35 |
| software-engineering | `engr.data-structures` | `engr.algorithms` | 30 | 140 | 35 |
| embedded | (new) | `engr.operating-systems`, `engr.electronics` | 23 | - | 25 |
| theory | (new) | `engr.algorithms` | 27 | - | 30 |
| **Total** | | | **1845** | **4980** | **2100** |

Removed from the manifest: `engr.transport`, `engr.control-systems` (budget 290)

## Overlap notes

- **Fourier transforms:** `signals` homes the engineering Fourier transform (spectra, filtering, modulation, sampling). `math.pde` keeps its transform topics for solving PDEs. The names differ, but the core skill overlaps, and `find-duplicates` may flag the pairs. The alternative is moving the PDE transform topics into signals, which would make PDE depend on an engineering course.
- **Physics already covers** RC transients, phasors, resonance and transformers (physics.em); Bernoulli, Poiseuille flow, buoyancy, plane-surface forces, the Otto, Diesel and Carnot cycles, entropy, simple conduction and radiation (physics.waves-thermo-optics); and composite moments of inertia and 3D rigid statics (physics.mechanics). Engineering courses depend on these rather than repeating them. Three duplicates the check found are already removed.
- **Fluids and heat transfer** each home their own differential equations in engineering form (the Navier-Stokes solutions and the heat diffusion equation with generation). Math PDE topics are not prerequisites, because most engineering students don't take PDEs.
- **The FFT** is homed in `dsp` as the radix-2 algorithm, building on `math.numerical.fft-intro`.
- **Feedforward control** appears twice by design: `controls.feedforward-control` is the general idea, and `process-control.feedforward-process-control` designs it for measured process disturbances.

## Survey

The standards in refs are the FE CBT specifications (civil, chemical, mechanical, electrical and computer, environmental, industrial, other disciplines) and the ABET EAC and CAC criteria, including the civil, chemical, electrical/computer, mechanical, software and computer science program criteria. University sources are indexed in `refs/uni_syllabi/SOURCES.md` under the `eng-*` folders: 140 of 198 downloads saved, at least one per course, and usually three to five.

Left out: aerospace, biomedical, industrial and materials engineering as disciplines; engineering graphics and CAD practice; programming languages and compilers; computer security as its own course (security appears in networks, operating systems and software engineering); machine learning; and second-course material such as advanced structural dynamics, finite element methods, and PDE-based transport phenomena.

## engr.programming: 91 topics

Follows `math.precalc`.

### Values and expressions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Running a program and reading its output | `running-programs` | uni-lower | `math.alg1.evaluate-for-expressions` |
| Using variables and assignment | `variables-and-assignment` | uni-lower | `running-programs` |
| Working with integer and floating-point values | `numeric-types` | uni-lower | `variables-and-assignment` |
| Using arithmetic operators and precedence | `arithmetic-operators` | uni-lower | `numeric-types` |
| Using integer division and remainder | `integer-division-and-remainder` | uni-lower | `arithmetic-operators` |
| Recognizing floating-point rounding in programs | `floating-point-pitfalls` | uni-lower | `numeric-types` |
| Building and joining strings | `strings-basics` | uni-lower | `variables-and-assignment` |
| Indexing and slicing strings | `string-indexing-and-slicing` | uni-lower | `strings-basics` |
| Reading input and formatting output | `input-and-output` | uni-lower | `strings-basics`, `numeric-types` |
| Converting between types | `type-conversion` | uni-lower | `input-and-output` |
| Writing boolean expressions | `boolean-expressions` | uni-lower | `arithmetic-operators` |
| Combining comparisons with and, or and not | `comparison-chains` | uni-lower | `boolean-expressions` |

### Control flow

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Branching with if statements | `if-statements` | uni-lower | `boolean-expressions` |
| Choosing among several cases | `if-else-chains` | uni-lower | `if-statements` |
| Nesting conditionals | `nested-conditionals` | uni-lower | `if-else-chains` |
| Repeating with while loops | `while-loops` | uni-lower | `if-statements` |
| Counting with for loops | `for-loops-over-ranges` | uni-lower | `while-loops` |
| Accumulating a sum or count in a loop | `accumulator-pattern` | uni-lower | `for-loops-over-ranges` |
| Filtering inside a loop | `loop-with-conditions` | uni-lower | `accumulator-pattern`, `if-else-chains` |
| Writing nested loops | `nested-loops` | uni-lower | `for-loops-over-ranges` |
| Leaving or skipping loop iterations | `break-and-continue` | uni-lower | `while-loops`, `loop-with-conditions` |
| Tracing code by hand | `tracing-code` | uni-lower | `nested-loops`, `nested-conditionals` |
| Finding off-by-one errors in loops | `off-by-one-errors` | uni-lower | `tracing-code` |

### Functions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining and calling functions | `defining-functions` | uni-lower | `accumulator-pattern` |
| Passing parameters and returning values | `parameters-and-return` | uni-lower | `defining-functions` |
| Telling local from global scope | `local-and-global-scope` | uni-lower | `parameters-and-return` |
| Using default and keyword arguments | `default-and-keyword-arguments` | uni-lower | `parameters-and-return` |
| Building programs from small functions | `functions-calling-functions` | uni-lower | `local-and-global-scope` |
| Tracing the call stack | `call-stack` | uni-lower | `functions-calling-functions` |
| Writing preconditions and postconditions | `docstrings-and-contracts` | uni-lower | `parameters-and-return` |
| Testing functions with assertions | `testing-functions` | uni-lower | `docstrings-and-contracts` |
| Passing functions as arguments | `functions-as-values` | uni-lower | `functions-calling-functions` |
| Writing anonymous functions | `lambda-expressions` | uni-lower | `functions-as-values` |

### Sequences and collections

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Creating and indexing lists | `lists-basics` | uni-lower | `string-indexing-and-slicing`, `for-loops-over-ranges` |
| Changing lists in place | `list-mutation` | uni-lower | `lists-basics` |
| Looping over list elements | `iterating-over-lists` | uni-lower | `lists-basics`, `accumulator-pattern` |
| Finding maximum, minimum and position in a list | `list-algorithms-by-hand` | uni-lower | `iterating-over-lists`, `loop-with-conditions` |
| Telling aliases from copies | `aliasing-and-copying` | uni-lower | `list-mutation`, `local-and-global-scope` |
| Working with lists of lists | `nested-lists` | uni-lower | `nested-loops`, `iterating-over-lists` |
| Using tuples and unpacking | `tuples` | uni-lower | `lists-basics` |
| Storing key-value pairs | `dictionaries` | uni-lower | `iterating-over-lists` |
| Counting occurrences with a dictionary | `counting-with-dictionaries` | uni-lower | `dictionaries`, `accumulator-pattern` |
| Using sets for membership and duplicates | `sets-in-programs` | uni-lower | `dictionaries` |
| Building collections with comprehensions | `comprehensions` | uni-lower | `iterating-over-lists`, `loop-with-conditions` |
| Splitting and searching strings | `string-methods` | uni-lower | `string-indexing-and-slicing`, `lists-basics` |
| Choosing a collection for a task | `choosing-a-collection` | uni-lower | `dictionaries`, `sets-in-programs`, `tuples` |

### Recursion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing recursive functions | `recursive-functions` | uni-lower | `call-stack` |
| Choosing base and recursive cases | `base-and-recursive-cases` | uni-lower | `recursive-functions` |
| Recursing over lists and strings | `recursion-on-lists` | uni-lower | `base-and-recursive-cases`, `lists-basics` |
| Tracing recursive calls | `tracing-recursion` | uni-lower | `recursion-on-lists` |
| Writing recursion with several calls | `tree-recursion` | uni-lower | `tracing-recursion` |
| Caching results of recursive calls | `memoization` | uni-lower | `tree-recursion`, `dictionaries` |
| Converting between recursion and loops | `recursion-vs-iteration` | uni-lower | `tracing-recursion`, `while-loops` |

### Files and errors

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading text files | `reading-files` | uni-lower | `string-methods` |
| Writing text files | `writing-files` | uni-lower | `reading-files` |
| Processing comma-separated data | `csv-data` | uni-lower | `reading-files`, `nested-lists` |
| Raising and catching exceptions | `exceptions` | uni-lower | `testing-functions` |
| Validating input with exceptions | `input-validation` | uni-lower | `exceptions`, `type-conversion` |
| Debugging with prints and a debugger | `debugging-strategies` | uni-lower | `tracing-code`, `exceptions` |

### Algorithms and efficiency

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Coding a linear search | `linear-search-code` | uni-lower | `list-algorithms-by-hand` |
| Coding a binary search | `binary-search-code` | uni-lower | `linear-search-code` |
| Coding selection sort | `selection-sort-code` | uni-lower | `list-algorithms-by-hand`, `nested-loops` |
| Coding insertion sort | `insertion-sort-code` | uni-lower | `selection-sort-code` |
| Coding merge sort | `merge-sort-code` | uni-lower | `insertion-sort-code`, `tree-recursion` |
| Counting operations to compare algorithms | `counting-operations` | uni-lower | `selection-sort-code` |
| Measuring running time empirically | `timing-programs` | uni-lower | `counting-operations` |

### Objects and classes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calling methods on objects | `objects-and-methods` | uni-lower | `string-methods`, `list-mutation` |
| Defining a class with attributes | `defining-classes` | uni-lower | `objects-and-methods`, `defining-functions` |
| Initializing objects with constructors | `constructors` | uni-lower | `defining-classes` |
| Writing instance methods | `instance-methods` | uni-lower | `constructors` |
| Hiding data behind methods | `encapsulation` | uni-lower | `instance-methods` |
| Defining printing and equality for objects | `special-methods` | uni-lower | `instance-methods` |
| Building objects from other objects | `class-composition` | uni-lower | `instance-methods`, `choosing-a-collection` |
| Extending a class with inheritance | `inheritance` | uni-lower | `class-composition` |
| Overriding methods | `method-overriding` | uni-lower | `inheritance` |
| Using polymorphism | `polymorphism` | uni-lower | `method-overriding` |
| Designing an abstract interface | `abstract-interfaces` | uni-lower | `polymorphism` |

### Numerical and scientific computing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Computing with numerical arrays | `array-computation` | uni-lower | `nested-lists`, `numeric-types` |
| Replacing loops with array operations | `vectorized-operations` | uni-lower | `array-computation` |
| Plotting data and functions | `plotting-data` | uni-lower | `array-computation` |
| Simulating a process step by step | `simulation-loops` | uni-lower | `accumulator-pattern`, `math.alg1.growth-decay-rate` |
| Using pseudorandom numbers | `random-numbers` | uni-lower | `simulation-loops` |
| Estimating quantities by random sampling | `monte-carlo-estimates` | uni-lower | `random-numbers` |
| Coding a bisection root search | `root-finding-code` | uni-lower | `binary-search-code`, `math.alg1.solving-by-table-technology` |
| Solving linear systems with a library | `solving-linear-systems-code` | uni-lower | `array-computation`, `math.alg2.matrix-row-reduction-intro` |

### Program design

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Breaking a problem into functions | `decomposing-problems` | uni-lower | `functions-calling-functions`, `choosing-a-collection` |
| Planning with pseudocode and flowcharts | `pseudocode-and-flowcharts` | uni-lower | `decomposing-problems` |
| Splitting code into modules | `modules-and-imports` | uni-lower | `decomposing-problems` |
| Writing readable code | `code-style` | uni-lower | `modules-and-imports` |
| Writing unit test suites | `unit-test-suites` | uni-lower | `testing-functions`, `modules-and-imports` |
| Tracking changes with version control | `version-control-basics` | uni-lower | `modules-and-imports` |

## engr.data-structures: 54 topics

Follows `engr.programming`, `math.discrete`.

### Abstract data types and analysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Separating an interface from its implementation | `abstract-data-types` | uni-lower | `programming.abstract-interfaces` |
| Analyzing running time of code | `asymptotic-analysis-of-code` | uni-lower | `programming.counting-operations`, `math.discrete.big-theta-omega` |
| Analyzing memory use | `space-complexity` | uni-lower | `asymptotic-analysis-of-code` |
| Using amortized analysis | `amortized-analysis` | uni-lower | `asymptotic-analysis-of-code` |
| Finding running times of recursive code | `recurrence-runtime` | uni-lower | `asymptotic-analysis-of-code`, `math.discrete.master-theorem-intro` |
| Telling best, worst and average cases | `best-worst-average-case` | uni-lower | `asymptotic-analysis-of-code` |

### Arrays and lists

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Implementing a resizable array | `dynamic-arrays` | uni-lower | `abstract-data-types`, `amortized-analysis` |
| Implementing a singly linked list | `singly-linked-lists` | uni-lower | `abstract-data-types`, `programming.class-composition` |
| Inserting and deleting in linked lists | `linked-list-operations` | uni-lower | `singly-linked-lists` |
| Implementing a doubly linked list | `doubly-linked-lists` | uni-lower | `linked-list-operations` |
| Comparing arrays and linked lists | `array-vs-linked-list` | uni-lower | `dynamic-arrays`, `linked-list-operations` |
| Implementing iterators | `iterators` | uni-lower | `singly-linked-lists` |

### Stacks and queues

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Implementing a stack | `stacks` | uni-lower | `array-vs-linked-list` |
| Using stacks for matching and evaluation | `stack-applications` | uni-lower | `stacks` |
| Implementing a queue | `queues` | uni-lower | `array-vs-linked-list` |
| Implementing a circular buffer | `circular-buffers` | uni-lower | `queues`, `dynamic-arrays` |
| Using double-ended queues | `deques` | uni-lower | `queues` |

### Recursion and sorting

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing recursion over linked structures | `recursive-structures` | uni-lower | `singly-linked-lists`, `programming.recursion-on-lists` |
| Implementing quicksort | `quicksort` | uni-lower | `programming.merge-sort-code`, `recurrence-runtime` |
| Comparing sorting algorithms | `sort-comparisons` | uni-lower | `quicksort`, `best-worst-average-case` |
| Explaining the lower bound for comparison sorting | `comparison-sort-lower-bound` | uni-lower | `sort-comparisons` |
| Sorting in linear time with counting and radix sort | `counting-and-radix-sort` | uni-lower | `comparison-sort-lower-bound` |
| Using stable sorting | `stable-sorting` | uni-lower | `sort-comparisons` |

### Trees

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Implementing binary tree nodes | `binary-tree-nodes` | uni-lower | `recursive-structures`, `math.discrete.rooted-binary-trees` |
| Coding tree traversals | `tree-traversal-code` | uni-lower | `binary-tree-nodes`, `math.discrete.tree-traversals` |
| Implementing a binary search tree | `bst-implementation` | uni-lower | `tree-traversal-code`, `math.discrete.binary-search-trees` |
| Deleting from a binary search tree | `bst-deletion` | uni-lower | `bst-implementation` |
| Relating tree height to running time | `bst-height-analysis` | uni-lower | `bst-implementation` |
| Balancing with AVL rotations | `avl-trees` | uni-lower | `bst-height-analysis` |
| Explaining red-black trees | `red-black-trees` | uni-lower | `avl-trees` |
| Using B-trees | `b-trees` | uni-lower | `bst-height-analysis` |
| Implementing tries | `tries` | uni-lower | `binary-tree-nodes`, `programming.dictionaries` |

### Priority queues and heaps

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Implementing a binary heap | `binary-heaps` | uni-lower | `binary-tree-nodes`, `dynamic-arrays` |
| Inserting and removing from a heap | `heap-operations` | uni-lower | `binary-heaps` |
| Building a heap in linear time | `heapify` | uni-lower | `heap-operations` |
| Sorting with a heap | `heapsort` | uni-lower | `heapify` |
| Using priority queues | `priority-queue-applications` | uni-lower | `heap-operations` |

### Hashing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing hash functions | `hash-functions` | uni-lower | `abstract-data-types`, `math.discrete.modular-arithmetic` |
| Resolving collisions by chaining | `separate-chaining` | uni-lower | `hash-functions`, `singly-linked-lists` |
| Resolving collisions by open addressing | `open-addressing` | uni-lower | `hash-functions` |
| Resizing hash tables by load factor | `load-factor-and-resizing` | uni-lower | `separate-chaining`, `open-addressing`, `amortized-analysis` |
| Implementing maps and sets with hashing | `hash-maps-and-sets` | uni-lower | `load-factor-and-resizing` |
| Choosing between hash maps and search trees | `choosing-maps` | uni-lower | `hash-maps-and-sets`, `avl-trees` |

### Graphs

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Implementing adjacency lists and matrices | `graph-representations-code` | uni-lower | `programming.dictionaries`, `math.discrete.graph-representations` |
| Coding breadth-first search | `bfs-code` | uni-lower | `graph-representations-code`, `queues`, `math.discrete.breadth-depth-search` |
| Coding depth-first search | `dfs-code` | uni-lower | `graph-representations-code`, `stacks` |
| Finding connected components in code | `connected-components-code` | uni-lower | `bfs-code`, `dfs-code` |
| Detecting cycles in graphs | `cycle-detection` | uni-lower | `dfs-code` |
| Coding a topological sort | `topological-sort-code` | uni-lower | `dfs-code`, `math.discrete.topological-sort` |
| Coding Dijkstra's algorithm with a heap | `dijkstra-code` | uni-lower | `bfs-code`, `priority-queue-applications`, `math.discrete.shortest-paths` |
| Implementing union-find | `union-find` | uni-lower | `graph-representations-code` |
| Coding minimum spanning tree algorithms | `mst-code` | uni-lower | `union-find`, `priority-queue-applications`, `math.discrete.minimum-spanning-trees` |

### Applying data structures

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing a data structure for a problem | `choosing-data-structures` | uni-lower | `choosing-maps`, `priority-queue-applications`, `graph-representations-code` |
| Building an LRU cache | `caching-structures` | uni-lower | `doubly-linked-lists`, `hash-maps-and-sets` |

## engr.digital-logic: 44 topics

Follows `math.discrete`, `engr.programming`.

### Number representation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Converting among binary, octal and hexadecimal | `binary-and-hex-codes` | uni-lower | `math.discrete.number-bases` |
| Adding and subtracting unsigned binary | `unsigned-binary-arithmetic` | uni-lower | `binary-and-hex-codes`, `math.discrete.base-arithmetic` |
| Representing signed numbers in two's complement | `twos-complement` | uni-lower | `unsigned-binary-arithmetic` |
| Detecting overflow | `overflow-detection` | uni-lower | `twos-complement` |
| Using BCD, Gray and character codes | `binary-codes` | uni-lower | `binary-and-hex-codes` |
| Detecting errors with parity bits | `error-detecting-codes` | uni-lower | `binary-codes` |
| Representing fractions in fixed point | `fixed-point-numbers` | uni-lower | `twos-complement` |

### Combinational logic

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing gate-level circuits | `gate-level-circuits` | uni-lower | `math.discrete.digital-logic-gates`, `math.discrete.boolean-algebra` |
| Designing a circuit from a truth table | `truth-table-to-circuit` | uni-lower | `gate-level-circuits`, `math.discrete.normal-forms` |
| Writing minterm and maxterm expansions | `minterms-and-maxterms` | uni-lower | `truth-table-to-circuit` |
| Minimizing with don't-care conditions | `kmap-with-dont-cares` | uni-lower | `minterms-and-maxterms`, `math.discrete.karnaugh-maps` |
| Implementing logic with NAND and NOR gates | `multilevel-nand-nor` | uni-lower | `truth-table-to-circuit` |
| Minimizing multiple-output circuits | `multiple-output-circuits` | uni-lower | `kmap-with-dont-cares` |
| Finding propagation delays and hazards | `gate-delays-and-hazards` | uni-lower | `gate-level-circuits` |

### Combinational building blocks

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing with multiplexers | `multiplexers` | uni-lower | `truth-table-to-circuit` |
| Using decoders and encoders | `decoders-and-encoders` | uni-lower | `truth-table-to-circuit` |
| Building half and full adders | `adders` | uni-lower | `truth-table-to-circuit`, `unsigned-binary-arithmetic` |
| Building ripple-carry adders and subtractors | `ripple-carry-adders` | uni-lower | `adders`, `twos-complement` |
| Speeding addition with carry lookahead | `carry-lookahead` | uni-lower | `ripple-carry-adders`, `gate-delays-and-hazards` |
| Building magnitude comparators | `comparators` | uni-lower | `adders` |
| Designing a simple arithmetic logic unit | `alu-design` | uni-lower | `ripple-carry-adders`, `multiplexers` |
| Building array multipliers | `multipliers` | uni-lower | `ripple-carry-adders` |

### Sequential logic

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Building SR and D latches | `latches` | uni-lower | `gate-level-circuits` |
| Using edge-triggered flip-flops | `flip-flops` | uni-lower | `latches` |
| Converting among D, JK and T flip-flops | `flip-flop-types` | uni-lower | `flip-flops` |
| Reading timing diagrams for sequential circuits | `timing-diagrams` | uni-lower | `flip-flops` |
| Checking setup and hold times | `setup-and-hold` | uni-lower | `timing-diagrams`, `gate-delays-and-hazards` |
| Building registers and shift registers | `registers` | uni-lower | `flip-flops` |
| Designing synchronous counters | `counters` | uni-lower | `flip-flop-types`, `registers` |
| Analyzing a clocked sequential circuit | `sequential-circuit-analysis` | uni-lower | `flip-flop-types` |

### Finite state machines

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Drawing state diagrams | `state-diagrams` | uni-lower | `sequential-circuit-analysis` |
| Comparing Moore and Mealy machines | `moore-and-mealy` | uni-lower | `state-diagrams` |
| Designing a finite state machine | `fsm-design` | uni-lower | `moore-and-mealy`, `kmap-with-dont-cares` |
| Choosing state encodings | `state-assignment` | uni-lower | `fsm-design` |
| Minimizing states | `state-minimization` | uni-lower | `fsm-design` |
| Designing sequence detectors | `sequence-detectors` | uni-lower | `fsm-design` |
| Splitting a design into datapath and controller | `datapath-and-controller` | uni-lower | `fsm-design`, `alu-design`, `registers` |

### Hardware description and devices

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing combinational logic in a hardware description language | `hdl-combinational` | uni-lower | `multiplexers`, `programming.if-else-chains` |
| Describing registers and state machines in a hardware description language | `hdl-sequential` | uni-lower | `hdl-combinational`, `fsm-design` |
| Writing testbenches | `hdl-testbenches` | uni-lower | `hdl-sequential` |
| Explaining programmable logic devices and FPGAs | `programmable-logic` | uni-lower | `hdl-combinational` |
| Organizing ROM and RAM arrays | `memory-arrays` | uni-lower | `decoders-and-encoders`, `registers` |
| Synchronizing asynchronous inputs | `asynchronous-inputs` | uni-lower | `setup-and-hold` |
| Building gates from CMOS transistors | `cmos-gates` | uni-lower | `gate-level-circuits` |

## engr.economics: 34 topics

Follows `math.precalc`, `math.stats`.

### Interest and equivalence

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Drawing cash flow diagrams | `cash-flow-diagrams` | uni-lower | `math.alg2.compound-interest-periods` |
| Comparing simple and compound interest | `simple-and-compound-interest` | uni-lower | `cash-flow-diagrams` |
| Using single-payment factors | `single-payment-factors` | uni-lower | `simple-and-compound-interest` |
| Using uniform series factors | `uniform-series-factors` | uni-lower | `single-payment-factors`, `math.precalc.annuities-loan-series` |
| Using arithmetic and geometric gradients | `gradient-series` | uni-lower | `uniform-series-factors`, `math.alg2.geometric-series-finite` |
| Converting nominal and effective rates | `nominal-and-effective-rates` | uni-lower | `single-payment-factors`, `math.alg2.effective-annual-rate` |
| Using continuous compounding factors | `continuous-compounding-factors` | uni-lower | `nominal-and-effective-rates`, `math.alg2.continuous-compounding` |
| Finding equivalence for shifted cash flows | `shifted-cash-flows` | uni-lower | `gradient-series` |
| Building loan amortization schedules | `loans-and-amortization` | uni-lower | `uniform-series-factors` |

### Comparing alternatives

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing alternatives by present worth | `present-worth` | uni-lower | `shifted-cash-flows` |
| Comparing alternatives with unequal lives | `unequal-lives` | uni-lower | `present-worth` |
| Comparing by future and annual worth | `future-and-annual-worth` | uni-lower | `present-worth` |
| Finding capitalized cost | `capitalized-cost` | uni-lower | `future-and-annual-worth` |
| Finding an internal rate of return | `rate-of-return` | uni-lower | `present-worth`, `math.alg1.solving-by-table-technology` |
| Comparing alternatives by incremental rate of return | `incremental-rate-of-return` | uni-lower | `rate-of-return` |
| Using benefit-cost ratios | `benefit-cost-ratio` | uni-lower | `present-worth` |
| Finding payback periods | `payback-period` | uni-lower | `shifted-cash-flows` |
| Choosing a minimum attractive rate of return | `minimum-attractive-rate` | uni-lower | `rate-of-return` |

### Costs and decisions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying fixed, variable, sunk and incremental costs | `cost-types` | uni-lower | `cash-flow-diagrams` |
| Finding break-even points | `break-even-analysis` | uni-lower | `cost-types` |
| Deciding when to replace equipment | `replacement-analysis` | uni-lower | `future-and-annual-worth`, `cost-types` |
| Finding the economic service life | `economic-life` | uni-lower | `replacement-analysis` |
| Analyzing make-or-buy and lease-or-buy decisions | `make-or-buy` | uni-lower | `present-worth`, `cost-types` |
| Estimating costs with indices and scaling | `cost-estimation` | uni-lower | `cost-types` |
| Finding life-cycle cost | `life-cycle-cost` | uni-lower | `present-worth`, `cost-estimation` |

### Taxes, inflation and risk

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding depreciation by straight-line and declining balance | `depreciation-methods` | uni-lower | `cost-types` |
| Building after-tax cash flows | `after-tax-cash-flows` | uni-lower | `depreciation-methods`, `present-worth` |
| Adjusting cash flows for inflation | `inflation` | uni-lower | `present-worth`, `nominal-and-effective-rates` |
| Testing sensitivity of a decision | `sensitivity-analysis` | uni-lower | `present-worth` |
| Making decisions with expected value | `expected-value-decisions` | uni-lower | `present-worth`, `math.stats.random-variables` |
| Analyzing decisions with decision trees | `decision-trees` | uni-lower | `expected-value-decisions` |

### Project scheduling

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Scheduling with the critical path method | `critical-path-method` | uni-lower | `cash-flow-diagrams` |
| Finding float and crashing a schedule | `float-and-crashing` | uni-lower | `critical-path-method` |
| Tracking projects with earned value | `earned-value` | uni-lower | `critical-path-method`, `cost-estimation` |

## engr.statics: 60 topics

Follows `physics.mechanics`, `math.calc3`, `math.linalg`.

### Force systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing forces as Cartesian vectors | `force-vectors-in-components` | uni-lower | `physics.mechanics.unit-vector-notation`, `physics.mechanics.position-vectors` |
| Writing a force directed along a line | `force-along-a-line` | uni-lower | `force-vectors-in-components` |
| Finding the resultant of concurrent forces | `resultant-of-concurrent-forces` | uni-lower | `force-along-a-line` |
| Finding moments about a point in two dimensions | `moment-about-a-point-2d` | uni-lower | `force-vectors-in-components` |
| Finding moments about a point with the cross product | `moment-about-a-point-3d` | uni-lower | `moment-about-a-point-2d`, `physics.mechanics.torque-as-a-cross-product` |
| Finding the moment of a force about an axis | `moment-about-an-axis` | uni-lower | `moment-about-a-point-3d`, `math.calc3.triple-scalar-product` |
| Using components to find moments | `varignon-principle` | uni-lower | `moment-about-a-point-2d` |
| Finding couple moments | `couple-moments` | uni-lower | `moment-about-a-point-3d` |
| Replacing a force with a force-couple system | `equivalent-force-couple-systems` | uni-lower | `couple-moments` |
| Reducing a force system to a single resultant | `reducing-force-systems` | uni-lower | `equivalent-force-couple-systems`, `resultant-of-concurrent-forces` |
| Reducing three-dimensional systems to a wrench | `wrench-resultants` | uni-lower | `reducing-force-systems` |

### Distributed loads

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding resultants of distributed loads | `distributed-load-resultants` | uni-lower | `reducing-force-systems`, `math.calc1.definite-integral-definition` |
| Finding resultants of nonuniform loads by integration | `nonuniform-distributed-loads` | uni-lower | `distributed-load-resultants` |

### Particle and rigid-body equilibrium

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving particle equilibrium in two dimensions | `particle-equilibrium-2d` | uni-lower | `resultant-of-concurrent-forces`, `physics.mechanics.statics-of-rigid-bodies` |
| Solving particle equilibrium in three dimensions | `particle-equilibrium-3d` | uni-lower | `particle-equilibrium-2d`, `force-along-a-line` |
| Using springs and cables in equilibrium problems | `springs-and-cables-in-equilibrium` | uni-lower | `particle-equilibrium-2d` |
| Modelling supports and their reactions in two dimensions | `support-reactions-2d` | uni-lower | `particle-equilibrium-2d`, `moment-about-a-point-2d` |
| Drawing free-body diagrams of rigid bodies | `free-body-diagrams-rigid` | uni-lower | `support-reactions-2d` |
| Solving rigid-body equilibrium in two dimensions | `rigid-equilibrium-2d` | uni-lower | `free-body-diagrams-rigid`, `distributed-load-resultants` |
| Using two-force and three-force members | `two-and-three-force-members` | uni-lower | `rigid-equilibrium-2d` |
| Modelling supports in three dimensions | `support-reactions-3d` | uni-lower | `support-reactions-2d`, `moment-about-an-axis`, `physics.mechanics.statics-of-rigid-bodies` |
| Checking determinacy and proper constraints | `determinacy-and-constraints` | uni-lower | `rigid-equilibrium-2d` |

### Structures

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Recognizing simple plane trusses | `plane-trusses` | uni-lower | `two-and-three-force-members` |
| Analyzing trusses by the method of joints | `method-of-joints` | uni-lower | `plane-trusses` |
| Identifying zero-force members | `zero-force-members` | uni-lower | `method-of-joints` |
| Analyzing trusses by the method of sections | `method-of-sections` | uni-lower | `method-of-joints` |
| Analyzing space trusses | `space-trusses` | uni-lower | `method-of-joints`, `particle-equilibrium-3d` |
| Analyzing frames | `frames` | uni-lower | `two-and-three-force-members`, `rigid-equilibrium-2d` |
| Analyzing machines and mechanisms | `machines` | uni-lower | `frames` |
| Solving truss equations with matrices | `truss-matrix-solution` | uni-lower | `method-of-joints`, `math.linalg.gaussian-elimination` |

### Internal forces

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding internal forces at a section | `internal-forces-at-a-point` | uni-lower | `rigid-equilibrium-2d`, `method-of-sections` |
| Writing shear and moment equations for beams | `shear-and-moment-equations` | uni-lower | `internal-forces-at-a-point`, `distributed-load-resultants` |
| Using load, shear and moment relations | `load-shear-moment-relations` | uni-lower | `shear-and-moment-equations`, `math.calc1.ftc-part-2` |
| Drawing shear and moment diagrams | `shear-moment-diagrams` | uni-lower | `load-shear-moment-relations` |
| Analyzing cables under point loads | `cables-with-point-loads` | uni-lower | `rigid-equilibrium-2d` |
| Analyzing cables under uniform horizontal loads | `parabolic-cables` | uni-lower | `cables-with-point-loads`, `nonuniform-distributed-loads` |
| Analyzing cables under their own weight | `catenary-cables` | uni-lower | `parabolic-cables`, `math.calc2.catenary` |

### Friction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving equilibrium with dry friction | `dry-friction` | uni-lower | `rigid-equilibrium-2d`, `physics.mechanics.tipping-and-sliding` |
| Deciding between tipping and slipping | `impending-motion-cases` | uni-lower | `dry-friction` |
| Analyzing wedges | `wedges` | uni-lower | `dry-friction` |
| Analyzing square-threaded screws | `square-threaded-screws` | uni-lower | `wedges` |
| Analyzing flat belt friction | `belt-friction` | uni-lower | `dry-friction`, `math.calc2.separable-equations` |
| Finding friction torque in bearings and disks | `bearing-and-disk-friction` | uni-lower | `dry-friction`, `nonuniform-distributed-loads` |
| Estimating rolling resistance | `rolling-resistance` | uni-lower | `dry-friction` |

### Centroids and area moments

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding centroids of composite areas | `centroids-of-composite-areas` | uni-lower | `distributed-load-resultants`, `physics.mechanics.center-of-gravity` |
| Finding centroids of areas by integration | `centroids-by-integration` | uni-lower | `centroids-of-composite-areas`, `math.calc2.centroid-between-curves` |
| Finding centroids of lines and volumes | `centroids-of-lines-and-volumes` | uni-lower | `centroids-by-integration` |
| Using the theorems of Pappus and Guldinus | `pappus-guldinus` | uni-lower | `centroids-of-lines-and-volumes`, `math.calc2.pappus-theorem` |
| Finding resultant forces of fluid pressure on surfaces | `fluid-pressure-resultants` | uni-lower | `nonuniform-distributed-loads`, `centroids-of-composite-areas` |
| Finding area moments of inertia by integration | `area-moments-by-integration` | uni-lower | `centroids-by-integration` |
| Using the parallel-axis theorem for areas | `parallel-axis-for-areas` | uni-lower | `area-moments-by-integration` |
| Finding moments of inertia of composite areas | `composite-area-moments` | uni-lower | `parallel-axis-for-areas` |
| Finding polar moments of area | `polar-moment-of-area` | uni-lower | `area-moments-by-integration` |
| Finding products of inertia of areas | `product-of-inertia` | uni-lower | `parallel-axis-for-areas` |
| Finding principal axes and moments of areas | `principal-axes-of-areas` | uni-lower | `product-of-inertia` |
| Using Mohr's circle for moments of inertia | `mohrs-circle-for-inertia` | uni-lower | `principal-axes-of-areas` |
| Finding radius of gyration | `radius-of-gyration` | uni-lower | `composite-area-moments` |

### Virtual work

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing virtual displacements | `virtual-displacements` | uni-lower | `machines`, `math.calc1.differentials` |
| Solving equilibrium by virtual work | `virtual-work-equilibrium` | uni-lower | `virtual-displacements` |
| Judging stability of equilibrium with potential energy | `potential-energy-stability` | uni-lower | `virtual-work-equilibrium`, `physics.mechanics.equilibrium-from-potential` |

## engr.dynamics: 46 topics

Follows `engr.statics`.

### Particle kinematics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving rectilinear motion with variable acceleration | `rectilinear-kinematics-review` | uni-lower | `physics.mechanics.position-dependent-acceleration` |
| Constructing motion from piecewise graphs | `erratic-motion-graphs` | uni-lower | `rectilinear-kinematics-review` |
| Describing curvilinear motion in rectangular components | `curvilinear-rectangular` | uni-lower | `physics.mechanics.integrating-vector-motion` |
| Using normal and tangential components | `normal-tangential-kinematics` | uni-lower | `curvilinear-rectangular`, `math.calc3.curvature` |
| Using radial and transverse components | `polar-cylindrical-kinematics` | uni-lower | `curvilinear-rectangular`, `math.calc2.polar-derivatives` |
| Analyzing dependent motion of connected particles | `dependent-motion` | uni-lower | `rectilinear-kinematics-review` |
| Using relative motion with translating axes | `relative-motion-translating-axes` | uni-lower | `curvilinear-rectangular`, `physics.mechanics.relative-position-vectors` |

### Particle kinetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing equations of motion in rectangular components | `equations-of-motion-rectangular` | uni-lower | `curvilinear-rectangular`, `statics.particle-equilibrium-3d` |
| Writing equations of motion in normal and tangential components | `equations-of-motion-nt` | uni-lower | `normal-tangential-kinematics`, `equations-of-motion-rectangular` |
| Writing equations of motion in polar components | `equations-of-motion-polar` | uni-lower | `polar-cylindrical-kinematics`, `equations-of-motion-rectangular` |
| Solving kinetics problems with friction | `kinetics-with-friction` | uni-lower | `equations-of-motion-rectangular`, `statics.dry-friction` |
| Analyzing central-force motion | `central-force-motion` | uni-lower | `equations-of-motion-polar`, `physics.mechanics.effective-potential-orbits` |

### Energy and momentum for particles

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Applying work and energy to particles | `particle-work-energy` | uni-lower | `equations-of-motion-nt`, `physics.mechanics.work-along-a-path` |
| Using energy conservation with springs and gravity | `particle-energy-conservation` | uni-lower | `particle-work-energy` |
| Finding power and mechanical efficiency | `power-and-efficiency` | uni-lower | `particle-work-energy` |
| Applying impulse and momentum to particles | `particle-impulse-momentum` | uni-lower | `equations-of-motion-rectangular`, `physics.mechanics.impulse-as-an-integral` |
| Solving direct and oblique impact | `impact-problems` | uni-lower | `particle-impulse-momentum`, `physics.mechanics.coefficient-of-restitution` |
| Applying angular impulse and momentum to particles | `particle-angular-momentum` | uni-lower | `particle-impulse-momentum`, `physics.mechanics.angular-momentum-of-a-particle` |
| Finding forces from steady mass flow streams | `steady-mass-flow` | uni-lower | `particle-impulse-momentum` |
| Analyzing systems that gain or lose mass | `variable-mass-propulsion` | uni-lower | `steady-mass-flow`, `physics.mechanics.variable-mass-systems` |
| Choosing between force, energy and momentum methods | `choosing-a-method-particles` | uni-lower | `particle-energy-conservation`, `impact-problems` |

### Planar rigid-body kinematics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing translation and fixed-axis rotation | `rigid-translation-rotation` | uni-lower | `physics.mechanics.angular-kinematics-with-calculus` |
| Analyzing linkages by absolute motion | `absolute-motion-analysis` | uni-lower | `rigid-translation-rotation` |
| Finding velocities with relative motion | `relative-velocity-rigid` | uni-lower | `rigid-translation-rotation`, `physics.mechanics.angular-velocity-vectors` |
| Finding velocities with the instantaneous center | `instant-center` | uni-lower | `relative-velocity-rigid` |
| Finding accelerations with relative motion | `relative-acceleration-rigid` | uni-lower | `relative-velocity-rigid`, `physics.mechanics.acceleration-on-a-rigid-body` |
| Finding velocities in four-bar and slider-crank linkages | `linkage-velocity-analysis` | uni-lower | `instant-center` |
| Finding accelerations in linkages | `linkage-acceleration-analysis` | uni-lower | `relative-acceleration-rigid`, `linkage-velocity-analysis` |
| Using rotating reference frames | `rotating-axes-kinematics` | uni-lower | `relative-acceleration-rigid`, `physics.mechanics.rotating-frames` |

### Planar rigid-body kinetics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing planar equations of motion for rigid bodies | `planar-equations-of-motion` | uni-lower | `physics.mechanics.inertia-of-composite-bodies`, `statics.free-body-diagrams-rigid` |
| Solving rigid bodies in translation | `rigid-translation-kinetics` | uni-lower | `planar-equations-of-motion` |
| Solving rigid bodies rotating about a fixed axis | `fixed-axis-kinetics` | uni-lower | `planar-equations-of-motion`, `physics.mechanics.fixed-axis-dynamics` |
| Solving rigid bodies in general plane motion | `general-plane-motion-kinetics` | uni-lower | `fixed-axis-kinetics`, `relative-acceleration-rigid` |
| Solving systems of connected rigid bodies | `connected-rigid-bodies` | uni-lower | `general-plane-motion-kinetics` |
| Applying work and energy to rigid bodies | `rigid-work-energy` | uni-lower | `general-plane-motion-kinetics`, `particle-energy-conservation` |
| Applying impulse and momentum to rigid bodies | `rigid-impulse-momentum` | uni-lower | `general-plane-motion-kinetics`, `particle-angular-momentum` |
| Solving eccentric impact | `eccentric-impact` | uni-lower | `rigid-impulse-momentum`, `impact-problems` |

### Three-dimensional rigid bodies

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing three-dimensional rigid-body kinematics | `three-d-rigid-kinematics` | uni-lower | `rotating-axes-kinematics` |
| Finding products of inertia of composite bodies | `products-of-inertia-of-bodies` | uni-lower | `physics.mechanics.inertia-of-composite-bodies`, `math.linalg.eigen-definition` |
| Finding angular momentum in three dimensions | `three-d-angular-momentum` | uni-lower | `products-of-inertia-of-bodies`, `three-d-rigid-kinematics` |
| Using Euler's equations of motion | `euler-equations-of-motion` | uni-lower | `three-d-angular-momentum` |
| Analyzing gyroscopic motion | `gyroscopic-motion` | uni-lower | `euler-equations-of-motion`, `physics.mechanics.precession` |

### Vibration basics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding natural frequencies of particles and rigid bodies | `undamped-free-vibration` | uni-lower | `planar-equations-of-motion`, `physics.mechanics.shm-differential-equation` |
| Finding natural frequencies by the energy method | `energy-method-vibration` | uni-lower | `undamped-free-vibration`, `rigid-work-energy` |
| Analyzing viscous damped free vibration | `viscous-damped-vibration` | uni-lower | `undamped-free-vibration`, `physics.mechanics.damping-regimes` |
| Analyzing forced vibration of a single body | `forced-vibration-basics` | uni-lower | `viscous-damped-vibration`, `physics.mechanics.driven-oscillator` |

## engr.mech-materials: 54 topics

Follows `engr.statics`, `math.diffeq`, `physics.waves-thermo-optics`.

### Stress and strain

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding average normal stress | `normal-stress` | uni-lower | `statics.internal-forces-at-a-point` |
| Finding average shear and bearing stress | `shear-and-bearing-stress` | uni-lower | `normal-stress` |
| Designing with allowable stress and factors of safety | `allowable-stress-design` | uni-lower | `shear-and-bearing-stress` |
| Finding normal and shear strain | `normal-and-shear-strain` | uni-lower | `normal-stress` |
| Reading stress-strain diagrams | `stress-strain-diagrams` | uni-lower | `normal-and-shear-strain`, `physics.mechanics.stress-and-strain` |
| Using Hooke's law and Poisson's ratio | `hookes-law-and-poisson` | uni-lower | `stress-strain-diagrams` |
| Using the generalized Hooke's law | `generalized-hookes-law` | uni-lower | `hookes-law-and-poisson` |
| Finding strain energy in axial members | `strain-energy` | uni-lower | `stress-strain-diagrams` |

### Axial loading

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding deformation of axially loaded members | `axial-deformation` | uni-lower | `hookes-law-and-poisson` |
| Finding deformation of members with varying load or area | `varying-axial-members` | uni-lower | `axial-deformation`, `math.calc1.definite-integral-definition` |
| Solving statically indeterminate axial members | `indeterminate-axial-members` | uni-lower | `axial-deformation`, `statics.determinacy-and-constraints` |
| Finding thermal stress in axial members | `thermal-stress-axial` | uni-lower | `indeterminate-axial-members`, `physics.waves-thermo-optics.thermal-stress` |
| Using stress concentration factors | `stress-concentrations-axial` | uni-lower | `axial-deformation` |
| Analyzing elastic-plastic axial loading | `inelastic-axial-loading` | uni-lower | `indeterminate-axial-members` |

### Torsion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding shear stress in circular shafts | `torsion-of-circular-shafts` | uni-lower | `shear-and-bearing-stress`, `statics.polar-moment-of-area` |
| Finding angle of twist | `angle-of-twist` | uni-lower | `torsion-of-circular-shafts` |
| Designing shafts for power transmission | `power-transmission-shafts` | uni-lower | `torsion-of-circular-shafts` |
| Solving statically indeterminate torsion | `indeterminate-torsion` | uni-lower | `angle-of-twist` |
| Analyzing torsion of thin-walled tubes | `thin-walled-torsion` | uni-lower | `torsion-of-circular-shafts` |
| Estimating torsion of noncircular shafts | `noncircular-torsion` | uni-lower | `torsion-of-circular-shafts` |

### Bending

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding bending stress with the flexure formula | `flexure-formula` | uni-lower | `normal-stress`, `statics.shear-moment-diagrams`, `statics.composite-area-moments` |
| Selecting beam sections for bending | `beam-section-design` | uni-lower | `flexure-formula` |
| Analyzing unsymmetric bending | `unsymmetric-bending` | uni-lower | `flexure-formula`, `statics.principal-axes-of-areas` |
| Analyzing composite beams by transformed sections | `composite-beams` | uni-lower | `flexure-formula` |
| Analyzing curved beams | `curved-beams` | uni-lower | `flexure-formula` |
| Finding plastic moment of beams | `plastic-bending` | uni-lower | `flexure-formula`, `inelastic-axial-loading` |

### Transverse shear

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding shear stress in beams with the shear formula | `shear-formula` | uni-lower | `flexure-formula` |
| Finding shear flow in built-up members | `shear-flow-built-up` | uni-lower | `shear-formula` |
| Finding shear flow in thin-walled sections | `shear-flow-thin-walled` | uni-lower | `shear-flow-built-up` |
| Locating the shear center | `shear-center` | uni-lower | `shear-flow-thin-walled` |

### Combined loading and stress transformation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding stress under combined loadings | `combined-loadings` | uni-lower | `power-transmission-shafts`, `shear-formula`, `axial-deformation` |
| Finding stress in thin-walled pressure vessels | `thin-walled-pressure-vessels` | uni-lower | `normal-stress` |
| Transforming plane stress | `plane-stress-transformation` | uni-lower | `combined-loadings` |
| Finding principal stresses and maximum shear | `principal-stresses` | uni-lower | `plane-stress-transformation` |
| Using Mohr's circle for stress | `mohrs-circle-stress` | uni-lower | `principal-stresses` |
| Finding absolute maximum shear stress | `three-d-mohrs-circle` | uni-lower | `mohrs-circle-stress` |
| Transforming plane strain | `plane-strain-transformation` | uni-lower | `mohrs-circle-stress`, `normal-and-shear-strain` |
| Reducing strain rosette data | `strain-rosettes` | uni-lower | `plane-strain-transformation` |
| Relating elastic constants | `material-property-relations` | uni-lower | `generalized-hookes-law`, `plane-strain-transformation` |
| Applying static failure theories | `failure-theories-intro` | uni-lower | `principal-stresses` |

### Beam deflection

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing the elastic curve equation | `elastic-curve` | uni-lower | `flexure-formula`, `math.calc1.ftc-part-2` |
| Finding beam deflection by integration | `deflection-by-integration` | uni-lower | `elastic-curve` |
| Finding deflection with discontinuity functions | `discontinuity-functions` | uni-lower | `deflection-by-integration`, `math.diffeq.step-functions-laplace` |
| Finding deflection by the moment-area method | `moment-area-method` | uni-lower | `deflection-by-integration` |
| Finding deflection by superposition | `deflection-by-superposition` | uni-lower | `deflection-by-integration` |
| Solving statically indeterminate beams | `indeterminate-beams` | uni-lower | `deflection-by-superposition` |

### Buckling

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding critical loads of pin-ended columns | `euler-buckling` | uni-lower | `deflection-by-integration`, `math.diffeq.constant-coefficients-complex` |
| Using effective length for other end conditions | `effective-length` | uni-lower | `euler-buckling` |
| Using the secant formula for eccentric loads | `secant-formula` | uni-lower | `effective-length` |
| Designing columns with empirical formulas | `column-design` | uni-lower | `effective-length` |

### Energy methods

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding strain energy for bending and torsion | `strain-energy-general` | uni-lower | `strain-energy`, `angle-of-twist`, `flexure-formula` |
| Finding stress under impact loading | `impact-loading` | uni-lower | `strain-energy-general` |
| Finding deflections with Castigliano's theorem | `castiglianos-theorem` | uni-lower | `strain-energy-general` |
| Finding deflections with the virtual work method | `virtual-work-deflection` | uni-lower | `strain-energy-general`, `statics.virtual-work-equilibrium` |

## engr.materials: 56 topics

Follows `chem.gen2`, `engr.mech-materials`, `math.stats`.

### Structure of materials

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying metals, ceramics, polymers and composites | `material-classes` | uni-lower | `chem.gen1.lattice-energy` |
| Relating bonding to material properties | `bonding-and-properties` | uni-lower | `material-classes`, `chem.gen1.bond-order-length-strength` |
| Describing FCC, BCC and HCP structures | `metallic-crystal-structures` | uni-lower | `chem.gen1.packing-efficiency` |
| Writing crystallographic directions and planes | `crystallographic-directions` | uni-lower | `metallic-crystal-structures` |
| Finding linear and planar densities | `linear-and-planar-density` | uni-lower | `crystallographic-directions` |
| Identifying crystal structures by X-ray diffraction | `xrd-for-materials` | uni-lower | `crystallographic-directions`, `chem.gen1.x-ray-crystallography-in-chemistry` |
| Explaining polymorphism and anisotropy | `polymorphism-and-anisotropy` | uni-lower | `metallic-crystal-structures` |

### Imperfections and diffusion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding vacancy concentrations | `point-defects` | uni-lower | `metallic-crystal-structures`, `chem.gen2.arrhenius-equation` |
| Describing edge and screw dislocations | `dislocations` | uni-lower | `point-defects` |
| Describing grain boundaries and grain size | `grain-boundaries` | uni-lower | `dislocations` |
| Using Fick's first law in solids | `fick-first-law-solids` | uni-lower | `point-defects` |
| Using error-function solutions for diffusion | `fick-second-law-solids` | uni-lower | `fick-first-law-solids` |
| Finding how diffusivity depends on temperature | `diffusion-temperature` | uni-lower | `fick-first-law-solids` |

### Mechanical behaviour

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding properties from a tensile test | `tensile-testing` | uni-lower | `mech-materials.stress-strain-diagrams` |
| Converting to true stress and strain | `true-stress-strain` | uni-lower | `tensile-testing` |
| Relating hardness to strength | `hardness-testing` | uni-lower | `tensile-testing` |
| Handling variability in material properties | `property-variability` | uni-lower | `tensile-testing`, `math.stats.normal-calculations` |
| Explaining slip and resolved shear stress | `slip-systems` | uni-lower | `dislocations`, `crystallographic-directions` |
| Explaining strengthening mechanisms | `strengthening-mechanisms` | uni-lower | `slip-systems`, `grain-boundaries` |
| Explaining recovery, recrystallization and grain growth | `recovery-recrystallization` | uni-lower | `strengthening-mechanisms` |

### Failure

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing ductile and brittle fracture | `fracture-modes` | uni-lower | `tensile-testing` |
| Using fracture toughness | `fracture-toughness` | uni-lower | `fracture-modes`, `mech-materials.stress-concentrations-axial` |
| Interpreting impact tests and transition temperature | `impact-testing` | uni-lower | `fracture-modes` |
| Reading S-N curves | `fatigue-basics` | uni-lower | `fracture-modes` |
| Predicting fatigue crack growth | `crack-growth` | uni-lower | `fatigue-basics`, `fracture-toughness` |
| Analyzing creep behaviour | `creep` | uni-lower | `diffusion-temperature`, `tensile-testing` |

### Phase diagrams

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining phases and solubility limits | `solubility-and-phases` | uni-lower | `chem.gen1.alloys` |
| Reading isomorphous phase diagrams | `isomorphous-diagrams` | uni-lower | `solubility-and-phases`, `chem.gen1.phase-diagrams` |
| Reading eutectic phase diagrams | `eutectic-diagrams` | uni-lower | `isomorphous-diagrams` |
| Predicting microstructure on cooling | `microstructure-development` | uni-lower | `eutectic-diagrams` |
| Reading the iron-carbon phase diagram | `iron-carbon-diagram` | uni-lower | `microstructure-development` |

### Phase transformations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing transformation rate with the Avrami equation | `transformation-kinetics` | uni-lower | `iron-carbon-diagram`, `diffusion-temperature` |
| Reading isothermal transformation diagrams | `ttt-diagrams` | uni-lower | `transformation-kinetics` |
| Reading continuous cooling diagrams | `cct-diagrams` | uni-lower | `ttt-diagrams` |
| Explaining martensite and tempering | `martensite-and-tempering` | uni-lower | `ttt-diagrams` |
| Choosing heat treatments for steels | `heat-treatment-of-steels` | uni-lower | `cct-diagrams`, `martensite-and-tempering` |
| Using hardenability curves | `hardenability` | uni-lower | `heat-treatment-of-steels` |
| Explaining precipitation hardening | `precipitation-hardening` | uni-lower | `microstructure-development`, `strengthening-mechanisms` |

### Classes of materials

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying steels and cast irons | `ferrous-alloys` | uni-lower | `iron-carbon-diagram` |
| Describing aluminum, copper and titanium alloys | `nonferrous-alloys` | uni-lower | `precipitation-hardening` |
| Describing ceramic structures | `ceramic-structures` | uni-lower | `chem.gen1.ionic-crystal-structures`, `material-classes` |
| Explaining brittle behaviour of ceramics | `ceramic-properties` | uni-lower | `ceramic-structures`, `fracture-toughness` |
| Describing glass structure and properties | `glasses` | uni-lower | `ceramic-structures` |
| Describing polymer chains and molecular weight | `polymer-structures` | uni-lower | `material-classes` |
| Describing viscoelastic behaviour of polymers | `polymer-mechanical-behaviour` | uni-lower | `polymer-structures`, `tensile-testing` |
| Relating crystallinity to polymer properties | `polymer-crystallinity` | uni-lower | `polymer-structures` |
| Finding composite properties by the rule of mixtures | `composites-rule-of-mixtures` | uni-lower | `tensile-testing`, `material-classes` |
| Analyzing fiber-reinforced composites | `fiber-composites` | uni-lower | `composites-rule-of-mixtures` |
| Describing concrete, asphalt, aggregates and wood | `construction-materials` | uni-lower | `material-classes`, `tensile-testing` |

### Functional properties and selection

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Relating conductivity to structure | `electrical-conductivity` | uni-lower | `bonding-and-properties` |
| Describing semiconductor materials | `semiconductor-materials` | uni-lower | `electrical-conductivity` |
| Describing heat capacity, expansion and conductivity | `thermal-properties` | uni-lower | `bonding-and-properties` |
| Describing magnetic materials | `magnetic-materials-engineering` | uni-lower | `bonding-and-properties` |
| Explaining corrosion mechanisms | `corrosion` | uni-lower | `chem.gen2.nernst-equation`, `material-classes` |
| Choosing corrosion protection | `corrosion-prevention` | uni-lower | `corrosion` |
| Selecting materials with property charts | `materials-selection` | uni-lower | `composites-rule-of-mixtures`, `ceramic-properties`, `ferrous-alloys` |

## engr.thermo: 70 topics

Follows `physics.waves-thermo-optics`, `math.calc3`.

### Properties of pure substances

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining systems, states and properties for engineering analysis | `systems-and-properties` | uni-lower | `physics.waves-thermo-optics.state-functions-and-path-dependence` |
| Describing phase-change processes of pure substances | `phase-change-processes` | uni-lower | `systems-and-properties`, `chem.gen1.phase-diagrams` |
| Reading T-v and P-v diagrams | `property-diagrams` | uni-lower | `phase-change-processes` |
| Using saturated property tables | `saturated-property-tables` | uni-lower | `property-diagrams` |
| Finding properties of saturated mixtures from quality | `quality-of-mixtures` | uni-lower | `saturated-property-tables` |
| Using superheated and compressed liquid tables | `superheated-and-compressed-tables` | uni-lower | `saturated-property-tables` |
| Interpolating in property tables | `table-interpolation` | uni-lower | `superheated-and-compressed-tables` |
| Using ideal-gas specific heats and property tables | `ideal-gas-specific-heats` | uni-lower | `systems-and-properties`, `physics.waves-thermo-optics.internal-energy-of-ideal-gases` |
| Using the compressibility factor and generalized charts | `compressibility-charts` | uni-lower | `ideal-gas-specific-heats`, `chem.gen1.real-gases` |
| Finding properties of liquids and solids | `incompressible-substances` | uni-lower | `saturated-property-tables` |

### First law for closed systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding boundary work for polytropic processes | `boundary-work` | uni-lower | `property-diagrams`, `physics.waves-thermo-optics.work-as-pressure-integral` |
| Applying the energy balance to closed systems | `closed-system-energy-balance` | uni-lower | `boundary-work`, `quality-of-mixtures` |
| Solving closed-system problems with ideal gases | `closed-systems-with-ideal-gases` | uni-lower | `closed-system-energy-balance`, `ideal-gas-specific-heats` |
| Solving closed-system problems with property tables | `closed-systems-with-tables` | uni-lower | `closed-system-energy-balance`, `table-interpolation` |

### First law for control volumes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding mass and volume flow rates | `mass-flow-rate` | uni-lower | `systems-and-properties` |
| Explaining flow work and enthalpy | `flow-work-and-enthalpy` | uni-lower | `mass-flow-rate` |
| Writing the steady-flow energy balance | `steady-flow-energy-balance` | uni-lower | `flow-work-and-enthalpy`, `closed-system-energy-balance` |
| Analyzing nozzles and diffusers | `nozzles-and-diffusers` | uni-lower | `steady-flow-energy-balance` |
| Analyzing turbines, compressors and pumps | `turbines-and-compressors` | uni-lower | `steady-flow-energy-balance` |
| Analyzing throttling valves | `throttling-valves` | uni-lower | `steady-flow-energy-balance` |
| Analyzing mixing chambers | `mixing-chambers` | uni-lower | `steady-flow-energy-balance` |
| Writing energy balances for heat exchangers | `heat-exchanger-energy-balance` | uni-lower | `steady-flow-energy-balance` |
| Analyzing systems of several devices | `multi-device-systems` | uni-lower | `turbines-and-compressors`, `heat-exchanger-energy-balance`, `throttling-valves` |
| Analyzing tank filling and emptying | `transient-filling-and-emptying` | uni-lower | `steady-flow-energy-balance`, `math.calc2.separable-equations` |

### Second law and entropy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Applying the second law to engines and refrigerators | `second-law-for-devices` | uni-lower | `closed-system-energy-balance`, `physics.waves-thermo-optics.second-law-statements` |
| Identifying irreversibilities | `reversible-and-irreversible` | uni-lower | `second-law-for-devices` |
| Finding entropy changes from property tables | `entropy-from-tables` | uni-lower | `reversible-and-irreversible`, `physics.waves-thermo-optics.entropy-definition` |
| Using T-s and h-s diagrams | `ts-and-hs-diagrams` | uni-lower | `entropy-from-tables` |
| Finding entropy changes of ideal gases with variable specific heats | `entropy-of-ideal-gases-variable-cp` | uni-lower | `entropy-from-tables`, `ideal-gas-specific-heats` |
| Analyzing isentropic processes | `isentropic-processes` | uni-lower | `entropy-of-ideal-gases-variable-cp`, `ts-and-hs-diagrams` |
| Using isentropic efficiencies of devices | `isentropic-efficiency` | uni-lower | `isentropic-processes`, `turbines-and-compressors` |
| Finding reversible steady-flow work | `reversible-steady-flow-work` | uni-lower | `isentropic-processes` |
| Finding entropy generation in control volumes | `entropy-generation` | uni-lower | `isentropic-efficiency` |

### Exergy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding exergy of a system and a flow stream | `exergy-of-a-state` | uni-lower | `entropy-generation` |
| Finding exergy destruction | `exergy-destruction` | uni-lower | `exergy-of-a-state` |
| Finding second-law efficiency | `second-law-efficiency` | uni-lower | `exergy-destruction` |
| Writing exergy balances for devices | `exergy-balances` | uni-lower | `exergy-destruction` |

### Vapor power cycles

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing the ideal Rankine cycle | `ideal-rankine-cycle` | uni-lower | `isentropic-processes`, `multi-device-systems` |
| Analyzing actual Rankine cycles | `actual-rankine-deviations` | uni-lower | `ideal-rankine-cycle`, `isentropic-efficiency` |
| Analyzing reheat Rankine cycles | `reheat-rankine` | uni-lower | `actual-rankine-deviations` |
| Analyzing regenerative feedwater heating | `regenerative-rankine` | uni-lower | `reheat-rankine`, `mixing-chambers` |
| Analyzing cogeneration plants | `cogeneration` | uni-lower | `regenerative-rankine` |

### Gas power cycles

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using air-standard assumptions | `air-standard-assumptions` | uni-lower | `isentropic-processes`, `physics.waves-thermo-optics.otto-and-diesel-cycles` |
| Analyzing Otto and Diesel cycles with variable specific heats | `otto-diesel-with-tables` | uni-lower | `air-standard-assumptions` |
| Analyzing dual, Stirling and Ericsson cycles | `dual-and-stirling-cycles` | uni-lower | `otto-diesel-with-tables` |
| Analyzing the Brayton cycle | `brayton-cycle` | uni-lower | `air-standard-assumptions`, `isentropic-efficiency` |
| Analyzing Brayton cycles with regeneration, reheat and intercooling | `brayton-regeneration` | uni-lower | `brayton-cycle` |
| Analyzing ideal jet propulsion cycles | `jet-propulsion-cycle` | uni-lower | `brayton-cycle`, `nozzles-and-diffusers` |
| Analyzing combined gas-vapor cycles | `combined-cycles` | uni-lower | `brayton-regeneration`, `actual-rankine-deviations` |

### Refrigeration

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing the vapor-compression refrigeration cycle | `vapor-compression-cycle` | uni-lower | `ideal-rankine-cycle`, `throttling-valves` |
| Analyzing actual refrigeration cycles and refrigerant choice | `actual-refrigeration-cycles` | uni-lower | `vapor-compression-cycle` |
| Analyzing heat pump systems | `heat-pump-systems` | uni-lower | `vapor-compression-cycle` |
| Analyzing cascade and multistage refrigeration | `cascade-and-multistage-refrigeration` | uni-lower | `actual-refrigeration-cycles` |
| Analyzing gas refrigeration cycles | `gas-refrigeration` | uni-lower | `brayton-cycle`, `vapor-compression-cycle` |

### Property relations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using Maxwell relations to find property changes | `maxwell-relations-engineering` | uni-lower | `entropy-of-ideal-gases-variable-cp`, `math.calc3.partial-derivatives-compute` |
| Using the Clapeyron equation | `clapeyron-equation` | uni-lower | `maxwell-relations-engineering` |
| Finding the Joule-Thomson coefficient | `joule-thomson-coefficient` | uni-lower | `maxwell-relations-engineering`, `throttling-valves` |
| Finding real-gas enthalpy and entropy from departure charts | `departure-functions` | uni-lower | `maxwell-relations-engineering`, `compressibility-charts` |

### Gas mixtures and psychrometrics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding properties of ideal-gas mixtures | `ideal-gas-mixtures` | uni-lower | `ideal-gas-specific-heats`, `chem.gen1.mole-fractions` |
| Analyzing processes with gas mixtures | `mixture-processes` | uni-lower | `ideal-gas-mixtures`, `steady-flow-energy-balance` |
| Finding specific and relative humidity | `humidity-measures` | uni-lower | `ideal-gas-mixtures` |
| Reading the psychrometric chart | `psychrometric-chart` | uni-lower | `humidity-measures` |
| Analyzing heating, cooling and humidifying air | `air-conditioning-processes` | uni-lower | `psychrometric-chart`, `mixture-processes` |
| Analyzing wet cooling towers | `cooling-towers` | uni-lower | `air-conditioning-processes` |

### Combustion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Balancing combustion reactions with excess air | `combustion-stoichiometry` | uni-lower | `mass-flow-rate`, `chem.gen1.combustion-analysis` |
| Finding air-fuel ratio and dew point of products | `air-fuel-ratio-and-dew-point` | uni-lower | `combustion-stoichiometry`, `humidity-measures` |
| Using enthalpy of formation and combustion | `enthalpy-of-formation` | uni-lower | `combustion-stoichiometry`, `chem.gen1.enthalpy` |
| Applying the first law to reacting systems | `first-law-reacting-systems` | uni-lower | `enthalpy-of-formation`, `steady-flow-energy-balance` |
| Finding adiabatic flame temperature | `adiabatic-flame-temperature` | uni-lower | `first-law-reacting-systems` |
| Finding entropy generation in combustion | `entropy-of-reacting-systems` | uni-lower | `first-law-reacting-systems`, `entropy-generation` |

## engr.fluids: 57 topics

Follows `engr.dynamics`, `engr.thermo`, `math.calc3`.

### Fluid properties and statics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using density, viscosity and other fluid properties | `fluid-properties` | uni-lower | `physics.waves-thermo-optics.viscosity` |
| Finding shear stress in Newtonian fluids | `newtonian-shear-stress` | uni-lower | `fluid-properties` |
| Describing non-Newtonian fluids | `non-newtonian-fluids` | uni-lower | `newtonian-shear-stress` |
| Measuring pressure with manometers | `manometers` | uni-lower | `physics.waves-thermo-optics.pressure-variation-by-integration` |
| Finding forces and centre of pressure on submerged plane surfaces | `forces-on-plane-surfaces` | uni-lower | `manometers`, `statics.fluid-pressure-resultants` |
| Finding forces on submerged curved surfaces | `forces-on-curved-surfaces` | uni-lower | `forces-on-plane-surfaces` |
| Finding stability of floating bodies with metacentric height | `buoyancy-and-stability-engineering` | uni-lower | `forces-on-curved-surfaces`, `physics.waves-thermo-optics.buoyancy-and-stability` |
| Analyzing fluids in rigid-body acceleration and rotation | `rigid-body-fluid-motion` | uni-lower | `manometers`, `physics.waves-thermo-optics.rotating-fluids` |

### Kinematics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing Lagrangian and Eulerian descriptions | `lagrangian-eulerian` | uni-lower | `fluid-properties`, `math.calc3.vector-fields` |
| Using the material derivative | `material-derivative` | uni-lower | `lagrangian-eulerian`, `math.calc3.chain-rule-multivariable` |
| Finding streamlines, pathlines and streaklines | `streamlines-and-pathlines` | uni-lower | `lagrangian-eulerian` |
| Using the Reynolds transport theorem | `reynolds-transport-theorem` | uni-lower | `material-derivative` |

### Integral analysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Applying conservation of mass to control volumes | `control-volume-mass` | uni-lower | `reynolds-transport-theorem`, `thermo.mass-flow-rate` |
| Applying Bernoulli's equation along a streamline | `bernoulli-applications` | uni-lower | `control-volume-mass`, `physics.waves-thermo-optics.bernoulli-derivation` |
| Measuring flow with pitot tubes, venturis and orifices | `flow-measurement` | uni-lower | `bernoulli-applications` |
| Drawing energy and hydraulic grade lines | `energy-grade-lines` | uni-lower | `bernoulli-applications` |
| Applying the mechanical energy equation with losses | `mechanical-energy-equation` | uni-lower | `energy-grade-lines`, `thermo.steady-flow-energy-balance` |
| Applying linear momentum to control volumes | `linear-momentum-cv` | uni-lower | `control-volume-mass`, `dynamics.steady-mass-flow` |
| Applying momentum to moving control volumes | `momentum-moving-cv` | uni-lower | `linear-momentum-cv` |
| Applying angular momentum to control volumes | `angular-momentum-cv` | uni-lower | `linear-momentum-cv` |

### Differential analysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving the differential continuity equation | `continuity-equation` | uni-lower | `control-volume-mass`, `math.calc3.divergence` |
| Using the stream function | `stream-function` | uni-lower | `continuity-equation` |
| Finding vorticity and rotationality | `vorticity-and-rotation` | uni-lower | `continuity-equation`, `math.calc3.curl` |
| Writing the Navier-Stokes equations | `navier-stokes` | uni-lower | `continuity-equation`, `newtonian-shear-stress` |
| Solving Couette flow | `couette-flow` | uni-lower | `navier-stokes` |
| Solving pressure-driven flow between plates and in pipes | `poiseuille-solutions` | uni-lower | `navier-stokes`, `physics.waves-thermo-optics.poiseuille-flow` |
| Superposing elementary potential flows | `potential-flow` | uni-lower | `stream-function`, `vorticity-and-rotation` |

### Dimensional analysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding dimensionless groups with the Buckingham pi theorem | `buckingham-pi` | uni-lower | `fluid-properties`, `physics.mechanics.dimensional-analysis` |
| Interpreting Reynolds, Froude, Mach and other numbers | `dimensionless-numbers` | uni-lower | `buckingham-pi` |
| Scaling model tests by similitude | `similitude-and-models` | uni-lower | `dimensionless-numbers` |

### Internal flow

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Telling laminar from turbulent pipe flow | `laminar-turbulent-pipe-flow` | uni-lower | `dimensionless-numbers`, `poiseuille-solutions` |
| Finding entrance length | `entrance-length` | uni-lower | `laminar-turbulent-pipe-flow` |
| Finding friction factors from the Moody chart | `moody-chart` | uni-lower | `laminar-turbulent-pipe-flow`, `mechanical-energy-equation` |
| Solving the Colebrook equation | `colebrook-equation` | uni-lower | `moody-chart`, `math.calc1.newtons-method` |
| Finding minor losses | `minor-losses` | uni-lower | `moody-chart` |
| Solving the three types of pipe flow problems | `pipe-flow-problem-types` | uni-lower | `minor-losses`, `colebrook-equation` |
| Analyzing pipes in series and parallel | `pipes-in-series-parallel` | uni-lower | `pipe-flow-problem-types` |
| Solving pipe networks iteratively | `pipe-networks` | uni-lower | `pipes-in-series-parallel` |
| Using hydraulic diameter for noncircular ducts | `noncircular-ducts` | uni-lower | `moody-chart` |

### External flow

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing laminar and turbulent boundary layers | `boundary-layer-concepts` | uni-lower | `laminar-turbulent-pipe-flow` |
| Finding boundary-layer thickness and skin friction on a flat plate | `flat-plate-boundary-layer` | uni-lower | `boundary-layer-concepts`, `math.calc1.definite-integral-definition` |
| Using the momentum integral method | `momentum-integral` | uni-lower | `flat-plate-boundary-layer`, `linear-momentum-cv` |
| Explaining separation and pressure gradients | `flow-separation` | uni-lower | `flat-plate-boundary-layer` |
| Finding drag from drag coefficients | `drag-coefficients` | uni-lower | `flow-separation`, `dimensionless-numbers` |
| Finding lift on airfoils | `lift-and-airfoils` | uni-lower | `drag-coefficients`, `potential-flow` |

### Turbomachinery

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading pump performance curves | `pump-performance-curves` | uni-lower | `mechanical-energy-equation`, `thermo.turbines-and-compressors` |
| Matching pumps to systems | `system-curves-and-operating-point` | uni-lower | `pump-performance-curves`, `pipe-flow-problem-types` |
| Checking net positive suction head | `pump-cavitation` | uni-lower | `pump-performance-curves`, `thermo.saturated-property-tables` |
| Using pump and fan scaling laws | `pump-scaling-laws` | uni-lower | `pump-performance-curves`, `similitude-and-models` |
| Combining pumps in series and parallel | `pumps-in-series-parallel` | uni-lower | `system-curves-and-operating-point` |
| Analyzing turbomachines with velocity triangles | `turbine-velocity-triangles` | uni-lower | `angular-momentum-cv`, `pump-performance-curves` |

### Compressible flow

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding Mach number and speed of sound in gases | `speed-of-sound-and-mach` | uni-lower | `dimensionless-numbers`, `thermo.isentropic-processes` |
| Finding stagnation properties | `stagnation-properties` | uni-lower | `speed-of-sound-and-mach`, `thermo.nozzles-and-diffusers` |
| Analyzing isentropic flow in varying-area ducts | `isentropic-duct-flow` | uni-lower | `stagnation-properties` |
| Analyzing converging-diverging nozzles and choking | `converging-diverging-nozzles` | uni-lower | `isentropic-duct-flow` |
| Analyzing normal shocks | `normal-shocks` | uni-lower | `converging-diverging-nozzles` |
| Describing duct flow with friction or heating | `fanno-and-rayleigh-flow` | uni-lower | `normal-shocks` |

## engr.circuits: 62 topics

Follows `physics.em`, `math.diffeq`, `math.linalg`.

### Resistive circuits

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using passive sign convention for power | `circuit-variables-and-sign-convention` | uni-lower | `physics.em.kirchhoff-general` |
| Analyzing circuits with dependent sources | `dependent-sources` | uni-lower | `circuit-variables-and-sign-convention` |
| Reducing series-parallel resistor networks | `series-parallel-reduction` | uni-lower | `circuit-variables-and-sign-convention` |
| Using current dividers and loaded voltage dividers | `voltage-and-current-dividers` | uni-lower | `series-parallel-reduction`, `physics.hs2.voltage-dividers` |
| Using wye-delta transformations | `wye-delta-transformation` | uni-lower | `series-parallel-reduction` |
| Analyzing circuits by nodal analysis | `nodal-analysis` | uni-lower | `voltage-and-current-dividers`, `math.linalg.gaussian-elimination` |
| Handling voltage sources with supernodes | `supernodes` | uni-lower | `nodal-analysis` |
| Analyzing circuits by mesh analysis | `mesh-analysis` | uni-lower | `voltage-and-current-dividers`, `math.linalg.gaussian-elimination` |
| Handling current sources with supermeshes | `supermeshes` | uni-lower | `mesh-analysis` |
| Choosing between nodal and mesh analysis | `choosing-nodal-or-mesh` | uni-lower | `supernodes`, `supermeshes` |

### Network theorems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing circuits by superposition | `superposition-theorem` | uni-lower | `nodal-analysis`, `dependent-sources` |
| Using source transformations | `source-transformation` | uni-lower | `voltage-and-current-dividers` |
| Finding Thevenin equivalents | `thevenin-equivalent` | uni-lower | `source-transformation`, `nodal-analysis` |
| Finding Norton equivalents | `norton-equivalent` | uni-lower | `thevenin-equivalent` |
| Finding equivalents with dependent sources | `thevenin-with-dependent-sources` | uni-lower | `thevenin-equivalent`, `dependent-sources` |
| Designing for maximum power transfer | `maximum-power-transfer-circuits` | uni-lower | `thevenin-equivalent`, `physics.em.power-in-a-resistor-maximum` |

### Operational amplifiers

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the ideal op-amp model | `ideal-op-amp-model` | uni-lower | `nodal-analysis` |
| Analyzing inverting and noninverting amplifiers | `inverting-and-noninverting` | uni-lower | `ideal-op-amp-model` |
| Analyzing summing and difference amplifiers | `summing-and-difference-amps` | uni-lower | `inverting-and-noninverting` |
| Analyzing cascaded op-amp circuits | `cascaded-op-amps` | uni-lower | `summing-and-difference-amps` |
| Checking op-amp saturation limits | `op-amp-saturation` | uni-lower | `inverting-and-noninverting` |

### Energy storage elements

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the capacitor current-voltage relation | `capacitor-iv-relation` | uni-lower | `circuit-variables-and-sign-convention`, `physics.em.capacitor-energy-integral` |
| Using the inductor current-voltage relation | `inductor-iv-relation` | uni-lower | `circuit-variables-and-sign-convention`, `physics.em.self-inductance` |
| Combining capacitors and inductors | `series-parallel-storage` | uni-lower | `capacitor-iv-relation`, `inductor-iv-relation` |
| Analyzing op-amp integrators and differentiators | `op-amp-integrators` | uni-lower | `capacitor-iv-relation`, `inverting-and-noninverting` |

### Transient response

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding natural response of RC and RL circuits | `first-order-natural-response` | uni-lower | `series-parallel-storage`, `physics.em.rc-solving-discharging` |
| Finding step response of first-order circuits | `first-order-step-response` | uni-lower | `first-order-natural-response`, `thevenin-equivalent` |
| Analyzing sequentially switched first-order circuits | `switched-first-order` | uni-lower | `first-order-step-response` |
| Writing differential equations for RLC circuits | `second-order-circuit-equations` | uni-lower | `series-parallel-storage`, `math.diffeq.rlc-circuits` |
| Finding natural response of RLC circuits | `second-order-natural-response` | uni-lower | `second-order-circuit-equations`, `math.diffeq.overdamped-critical` |
| Finding step response of RLC circuits | `second-order-step-response` | uni-lower | `second-order-natural-response` |

### Sinusoidal steady state

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing sinusoids by amplitude, frequency and phase | `sinusoid-parameters` | uni-lower | `first-order-step-response`, `physics.em.ac-sources-and-phase` |
| Transforming circuits with phasors and impedance | `phasors-and-impedance` | uni-lower | `sinusoid-parameters`, `math.alg2.complex-divide` |
| Applying nodal and mesh analysis to phasor circuits | `ac-nodal-mesh` | uni-lower | `phasors-and-impedance`, `choosing-nodal-or-mesh` |
| Finding Thevenin equivalents in the phasor domain | `ac-thevenin` | uni-lower | `ac-nodal-mesh`, `thevenin-equivalent` |
| Analyzing op-amp circuits in sinusoidal steady state | `ac-op-amp-circuits` | uni-lower | `ac-nodal-mesh`, `cascaded-op-amps` |

### AC power

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding instantaneous and average power | `instantaneous-and-average-power` | uni-lower | `phasors-and-impedance` |
| Finding effective values of waveforms | `rms-values` | uni-lower | `instantaneous-and-average-power` |
| Using complex, real and reactive power | `complex-power` | uni-lower | `rms-values`, `physics.em.ac-power-factor` |
| Correcting power factor | `power-factor-correction` | uni-lower | `complex-power` |
| Matching loads for maximum average power | `ac-maximum-power-transfer` | uni-lower | `complex-power`, `ac-thevenin` |
| Describing balanced three-phase sources | `three-phase-sources` | uni-lower | `phasors-and-impedance` |
| Analyzing balanced wye and delta loads | `wye-wye-and-delta-loads` | uni-lower | `three-phase-sources` |
| Finding power in balanced three-phase systems | `three-phase-power` | uni-lower | `wye-wye-and-delta-loads`, `complex-power` |

### Magnetically coupled circuits

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using mutual inductance and the dot convention | `mutual-inductance-dot-convention` | uni-lower | `inductor-iv-relation`, `physics.em.mutual-inductance` |
| Analyzing linear transformers | `linear-transformers` | uni-lower | `mutual-inductance-dot-convention`, `ac-nodal-mesh` |
| Analyzing ideal transformers and reflected impedance | `ideal-transformers` | uni-lower | `linear-transformers`, `physics.em.transformers-derivation` |

### Frequency response

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding transfer functions of networks | `network-transfer-functions` | uni-lower | `ac-op-amp-circuits` |
| Expressing gain in decibels | `decibels-and-log-scales` | uni-lower | `network-transfer-functions`, `math.alg2.log-scales` |
| Sketching Bode magnitude plots | `bode-magnitude` | uni-lower | `decibels-and-log-scales` |
| Sketching Bode phase plots | `bode-phase` | uni-lower | `bode-magnitude` |
| Analyzing series and parallel resonance | `series-and-parallel-resonance` | uni-lower | `network-transfer-functions`, `physics.em.ac-resonance` |
| Finding quality factor and bandwidth | `quality-factor-and-bandwidth` | uni-lower | `series-and-parallel-resonance` |
| Designing first-order and second-order passive filters | `passive-filters` | uni-lower | `bode-phase`, `quality-factor-and-bandwidth` |
| Designing active filters | `active-filters` | uni-lower | `passive-filters`, `ac-op-amp-circuits` |

### Laplace-domain circuit analysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Modelling circuit elements in the s-domain | `s-domain-elements` | uni-lower | `second-order-step-response`, `math.diffeq.laplace-of-derivatives` |
| Analyzing circuits in the s-domain | `s-domain-analysis` | uni-lower | `s-domain-elements`, `ac-nodal-mesh` |
| Relating poles and zeros to circuit response | `poles-zeros-circuits` | uni-lower | `s-domain-analysis`, `network-transfer-functions` |
| Finding impulse and step responses with transfer functions | `impulse-and-step-response-s` | uni-lower | `poles-zeros-circuits`, `math.diffeq.impulse-delta` |

### Two-port networks

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding impedance and admittance parameters | `two-port-parameters` | uni-lower | `ac-nodal-mesh` |
| Finding hybrid and transmission parameters | `hybrid-and-transmission-parameters` | uni-lower | `two-port-parameters` |
| Interconnecting two-port networks | `interconnected-two-ports` | uni-lower | `hybrid-and-transmission-parameters` |

## engr.signals: 42 topics

Follows `engr.circuits`.

### Signals

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying continuous and discrete signals | `signal-classification` | uni-lower | `circuits.sinusoid-parameters` |
| Shifting, scaling and reversing signals | `signal-transformations` | uni-lower | `signal-classification` |
| Decomposing signals into even and odd parts | `even-odd-periodic-signals` | uni-lower | `signal-transformations` |
| Finding energy and power of signals | `energy-and-power-signals` | uni-lower | `signal-classification` |
| Using unit step and impulse signals | `singularity-functions` | uni-lower | `signal-transformations`, `math.diffeq.impulse-delta` |
| Using complex exponential signals | `complex-exponential-signals` | uni-lower | `signal-classification`, `math.diffeq.euler-formula` |
| Working with discrete-time sequences | `discrete-time-sequences` | uni-lower | `signal-transformations`, `singularity-functions` |

### Systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Testing linearity, time invariance, causality and stability | `system-properties` | uni-lower | `signal-transformations` |
| Computing discrete-time convolution | `discrete-convolution` | uni-lower | `discrete-time-sequences`, `system-properties` |
| Computing continuous-time convolution | `continuous-convolution` | uni-lower | `singularity-functions`, `system-properties`, `math.diffeq.convolution` |
| Relating impulse response to system properties | `impulse-response-properties` | uni-lower | `discrete-convolution`, `continuous-convolution` |
| Solving linear difference equations | `difference-equations` | uni-lower | `discrete-convolution` |
| Representing LTI systems by differential equations | `lti-differential-equations` | uni-lower | `continuous-convolution` |
| Drawing system block diagrams | `block-diagram-systems` | uni-lower | `difference-equations`, `lti-differential-equations` |

### Fourier series

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using complex exponentials as eigenfunctions of LTI systems | `eigenfunctions-of-lti` | uni-lower | `complex-exponential-signals`, `impulse-response-properties` |
| Finding exponential Fourier series of signals | `continuous-fourier-series` | uni-lower | `eigenfunctions-of-lti`, `math.diffeq.fourier-series-intro` |
| Drawing line spectra | `line-spectra` | uni-lower | `continuous-fourier-series` |
| Using Fourier series properties | `fourier-series-properties` | uni-lower | `continuous-fourier-series` |
| Finding LTI responses to periodic inputs | `lti-response-periodic` | uni-lower | `fourier-series-properties`, `circuits.network-transfer-functions` |
| Finding discrete-time Fourier series | `discrete-fourier-series` | uni-lower | `continuous-fourier-series`, `discrete-time-sequences` |

### Continuous-time Fourier transform

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding continuous-time Fourier transforms of signals | `ct-fourier-transform` | uni-lower | `continuous-fourier-series` |
| Using common transform pairs | `fourier-transform-pairs-signals` | uni-lower | `ct-fourier-transform` |
| Using Fourier transform properties | `ct-fourier-properties` | uni-lower | `fourier-transform-pairs-signals` |
| Filtering signals with frequency response | `frequency-response-and-filtering` | uni-lower | `ct-fourier-properties`, `circuits.bode-phase` |
| Using the modulation property | `modulation-property` | uni-lower | `ct-fourier-properties` |
| Finding energy spectral density and bandwidth | `parseval-and-bandwidth` | uni-lower | `ct-fourier-properties` |
| Comparing ideal and practical filters | `ideal-and-practical-filters` | uni-lower | `frequency-response-and-filtering` |

### Discrete-time Fourier transform

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding discrete-time Fourier transforms | `dtft` | uni-lower | `discrete-fourier-series`, `ct-fourier-transform` |
| Using DTFT properties | `dtft-properties` | uni-lower | `dtft` |
| Finding frequency response of discrete systems | `discrete-frequency-response` | uni-lower | `dtft-properties`, `difference-equations` |

### Sampling

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Applying the sampling theorem | `sampling-theorem` | uni-lower | `ct-fourier-properties`, `dtft` |
| Predicting aliasing | `aliasing` | uni-lower | `sampling-theorem` |
| Reconstructing signals from samples | `reconstruction` | uni-lower | `sampling-theorem` |
| Processing continuous signals with discrete systems | `discrete-processing-of-ct-signals` | uni-lower | `reconstruction`, `discrete-frequency-response` |
| Analyzing quantization error | `quantization` | uni-lower | `sampling-theorem` |

### Laplace and z-transforms

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using regions of convergence for Laplace transforms | `bilateral-laplace-and-roc` | uni-lower | `ct-fourier-transform`, `math.diffeq.laplace-table` |
| Analyzing causality and stability from system functions | `system-functions-laplace` | uni-lower | `bilateral-laplace-and-roc`, `circuits.poles-zeros-circuits` |
| Finding z-transforms and regions of convergence | `z-transform` | uni-lower | `dtft`, `bilateral-laplace-and-roc` |
| Finding inverse z-transforms by partial fractions | `inverse-z-transform` | uni-lower | `z-transform`, `math.calc2.partial-fractions-setup` |
| Using z-transform properties | `z-transform-properties` | uni-lower | `z-transform` |
| Analyzing discrete systems with system functions | `system-functions-z` | uni-lower | `z-transform-properties`, `inverse-z-transform`, `difference-equations` |
| Sketching frequency response from poles and zeros | `pole-zero-frequency-response` | uni-lower | `system-functions-z`, `system-functions-laplace` |

## engr.controls: 43 topics

Follows `engr.signals`, `engr.dynamics`.

### Modelling dynamic systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing open-loop and closed-loop control | `control-system-concepts` | uni-upper | `circuits.network-transfer-functions` |
| Modelling translational mechanical systems | `translational-mechanical-models` | uni-upper | `control-system-concepts`, `dynamics.equations-of-motion-rectangular` |
| Modelling rotational systems with gears | `rotational-mechanical-models` | uni-upper | `translational-mechanical-models`, `dynamics.fixed-axis-kinetics` |
| Modelling electrical networks with transfer functions | `electrical-network-models` | uni-upper | `control-system-concepts`, `circuits.s-domain-analysis` |
| Modelling DC motors | `electromechanical-models` | uni-upper | `rotational-mechanical-models`, `electrical-network-models` |
| Modelling thermal and fluid systems | `thermal-and-fluid-models` | uni-upper | `translational-mechanical-models` |
| Linearizing nonlinear models about an operating point | `linearization-for-control` | uni-upper | `translational-mechanical-models`, `math.calc3.linearization-multivariable` |
| Reducing block diagrams | `block-diagram-reduction` | uni-upper | `control-system-concepts` |
| Using signal-flow graphs and Mason's rule | `signal-flow-graphs` | uni-upper | `block-diagram-reduction` |

### Time response

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding first-order system response | `first-order-system-response` | uni-upper | `block-diagram-reduction`, `circuits.impulse-and-step-response-s` |
| Finding second-order system response | `second-order-system-response` | uni-upper | `first-order-system-response` |
| Relating overshoot, settling and rise time to poles | `transient-specifications` | uni-upper | `second-order-system-response` |
| Approximating higher-order systems and effects of zeros | `higher-order-and-zeros` | uni-upper | `transient-specifications` |

### Stability and error

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Testing stability with the Routh-Hurwitz criterion | `routh-hurwitz` | uni-upper | `block-diagram-reduction` |
| Handling special cases in the Routh array | `routh-special-cases` | uni-upper | `routh-hurwitz` |
| Finding gain ranges for stability | `stability-with-gain` | uni-upper | `routh-special-cases` |
| Finding steady-state error from system type | `system-type-and-error-constants` | uni-upper | `block-diagram-reduction`, `math.diffeq.laplace-properties` |
| Finding steady-state error due to disturbances | `disturbance-rejection` | uni-upper | `system-type-and-error-constants` |
| Finding sensitivity to parameter changes | `sensitivity-to-parameters` | uni-upper | `system-type-and-error-constants` |

### Root locus

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Sketching the root locus | `root-locus-sketching` | uni-upper | `stability-with-gain`, `transient-specifications` |
| Finding breakaway points and jω crossings | `root-locus-refinements` | uni-upper | `root-locus-sketching` |
| Choosing gain from the root locus | `gain-from-root-locus` | uni-upper | `root-locus-refinements` |
| Describing proportional, integral and derivative action | `pid-controller-actions` | uni-upper | `system-type-and-error-constants`, `transient-specifications` |
| Designing lead compensators with the root locus | `lead-compensation-root-locus` | uni-upper | `gain-from-root-locus` |
| Designing lag compensators with the root locus | `lag-compensation-root-locus` | uni-upper | `gain-from-root-locus` |
| Designing PID controllers with the root locus | `pid-design-root-locus` | uni-upper | `lead-compensation-root-locus`, `lag-compensation-root-locus`, `pid-controller-actions` |

### Frequency response methods

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding open-loop frequency response | `frequency-response-of-loops` | uni-upper | `circuits.bode-phase`, `block-diagram-reduction` |
| Applying the Nyquist stability criterion | `nyquist-criterion` | uni-upper | `frequency-response-of-loops` |
| Finding gain and phase margins | `gain-and-phase-margins` | uni-upper | `nyquist-criterion` |
| Relating margins to closed-loop transient response | `margins-and-transient-response` | uni-upper | `gain-and-phase-margins`, `transient-specifications` |
| Analyzing systems with time delay | `time-delay-systems` | uni-upper | `gain-and-phase-margins` |
| Designing lead and lag compensators with Bode plots | `lead-lag-design-frequency` | uni-upper | `margins-and-transient-response` |

### PID in practice

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Tuning PID controllers with empirical rules | `pid-tuning-rules` | uni-upper | `pid-design-root-locus` |
| Preventing integrator windup | `integrator-windup` | uni-upper | `pid-tuning-rules` |
| Adding feedforward control | `feedforward-control` | uni-upper | `disturbance-rejection` |

### State space

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing state-space models | `state-space-models` | uni-upper | `linearization-for-control`, `math.linalg.matrix-times-vector` |
| Converting between transfer functions and state space | `transfer-function-to-state-space` | uni-upper | `state-space-models` |
| Solving state equations | `state-space-response` | uni-upper | `transfer-function-to-state-space`, `math.diffeq.matrix-exponential` |
| Testing controllability | `controllability` | uni-upper | `state-space-response`, `math.linalg.rank-from-pivots` |
| Designing state feedback by pole placement | `pole-placement` | uni-upper | `controllability` |
| Designing observers | `observability-and-observers` | uni-upper | `pole-placement` |

### Digital control

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Modelling sampled-data control systems | `sampled-data-systems` | uni-upper | `signals.system-functions-z`, `first-order-system-response` |
| Implementing digital controllers | `digital-controller-implementation` | uni-upper | `sampled-data-systems`, `pid-tuning-rules` |

## engr.structural-analysis: 47 topics

Follows `engr.mech-materials`, `engr.dynamics`, `math.linalg`.

### Loads and structural idealization

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Estimating dead, live and environmental loads | `structural-loads` | uni-upper | `statics.distributed-load-resultants` |
| Distributing floor loads by tributary area | `tributary-areas` | uni-upper | `structural-loads` |
| Applying load combinations | `load-combinations` | uni-upper | `structural-loads` |
| Idealizing supports and members for analysis | `idealizing-structures` | uni-upper | `statics.determinacy-and-constraints` |
| Classifying structures by determinacy and stability | `determinacy-and-stability` | uni-upper | `idealizing-structures` |

### Statically determinate structures

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing determinate beams | `determinate-beam-analysis` | uni-upper | `determinacy-and-stability`, `statics.shear-moment-diagrams` |
| Analyzing compound and complex trusses | `compound-trusses` | uni-upper | `determinacy-and-stability`, `statics.method-of-sections` |
| Analyzing determinate frames | `determinate-frames` | uni-upper | `determinate-beam-analysis` |
| Drawing moment diagrams for frames | `frame-moment-diagrams` | uni-upper | `determinate-frames` |
| Analyzing three-hinged arches | `three-hinged-arches` | uni-upper | `determinate-frames` |

### Deflections

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Sketching deflected shapes | `deflected-shapes` | uni-upper | `frame-moment-diagrams`, `mech-materials.elastic-curve` |
| Finding deflections by the conjugate-beam method | `conjugate-beam-method` | uni-upper | `deflected-shapes`, `mech-materials.moment-area-method` |
| Finding truss deflections by virtual work | `virtual-work-trusses` | uni-upper | `compound-trusses`, `mech-materials.virtual-work-deflection` |
| Finding beam and frame deflections by virtual work | `virtual-work-beams-frames` | uni-upper | `virtual-work-trusses`, `frame-moment-diagrams` |
| Evaluating virtual work integrals with tables | `visual-integration-tables` | uni-upper | `virtual-work-beams-frames` |
| Finding deflections with Castigliano's theorem for structures | `castigliano-structures` | uni-upper | `virtual-work-beams-frames`, `mech-materials.castiglianos-theorem` |

### Influence lines

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Constructing influence lines by equilibrium | `influence-lines-by-equilibrium` | uni-upper | `determinate-beam-analysis` |
| Constructing influence lines with the Muller-Breslau principle | `muller-breslau` | uni-upper | `influence-lines-by-equilibrium`, `deflected-shapes` |
| Constructing influence lines for trusses | `truss-influence-lines` | uni-upper | `influence-lines-by-equilibrium`, `compound-trusses` |
| Finding maximum effects of moving loads | `moving-load-maxima` | uni-upper | `influence-lines-by-equilibrium` |
| Finding absolute maximum moment from a series of loads | `absolute-maximum-moment` | uni-upper | `moving-load-maxima` |

### Approximate analysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing frames approximately for vertical loads | `approximate-vertical-loads` | uni-upper | `frame-moment-diagrams` |
| Analyzing frames for lateral loads by the portal method | `portal-method` | uni-upper | `approximate-vertical-loads` |
| Analyzing frames by the cantilever method | `cantilever-method` | uni-upper | `portal-method` |

### Force method

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing indeterminate beams by the force method | `force-method-beams` | uni-upper | `virtual-work-beams-frames`, `mech-materials.indeterminate-beams` |
| Analyzing indeterminate frames by the force method | `force-method-frames` | uni-upper | `force-method-beams` |
| Analyzing indeterminate trusses by the force method | `force-method-trusses` | uni-upper | `force-method-beams`, `virtual-work-trusses` |
| Using Maxwell's reciprocal theorem | `maxwell-betti` | uni-upper | `force-method-beams` |
| Finding effects of support settlement and temperature | `support-settlement-effects` | uni-upper | `force-method-frames` |
| Sketching influence lines for indeterminate beams | `indeterminate-influence-lines` | uni-upper | `muller-breslau`, `force-method-beams` |

### Displacement methods

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing beams by slope-deflection | `slope-deflection-beams` | uni-upper | `force-method-beams` |
| Analyzing frames by slope-deflection | `slope-deflection-frames` | uni-upper | `slope-deflection-beams` |
| Analyzing frames with sidesway | `sidesway-frames` | uni-upper | `slope-deflection-frames` |
| Analyzing beams by moment distribution | `moment-distribution-beams` | uni-upper | `slope-deflection-beams` |
| Analyzing frames by moment distribution | `moment-distribution-frames` | uni-upper | `moment-distribution-beams`, `sidesway-frames` |
| Analyzing nonprismatic members | `nonprismatic-members` | uni-upper | `moment-distribution-beams` |

### Matrix stiffness method

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing truss member stiffness matrices | `member-stiffness-truss` | uni-upper | `force-method-trusses`, `statics.truss-matrix-solution` |
| Transforming member stiffness to global coordinates | `coordinate-transformation` | uni-upper | `member-stiffness-truss`, `math.linalg.matrix-product-three-views` |
| Assembling the global stiffness matrix | `global-stiffness-assembly` | uni-upper | `coordinate-transformation` |
| Solving trusses by the stiffness method | `truss-stiffness-solution` | uni-upper | `global-stiffness-assembly` |
| Solving beams by the stiffness method | `beam-stiffness-method` | uni-upper | `truss-stiffness-solution`, `slope-deflection-beams` |
| Solving plane frames by the stiffness method | `frame-stiffness-method` | uni-upper | `beam-stiffness-method` |
| Including member loads and settlements in stiffness analysis | `member-loads-and-settlement` | uni-upper | `frame-stiffness-method` |
| Checking computer analysis results | `structural-software-checks` | uni-upper | `frame-stiffness-method`, `portal-method` |

### Lateral loads and stability

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Estimating wind loads | `wind-loads` | uni-upper | `load-combinations` |
| Estimating seismic loads by equivalent lateral force | `seismic-equivalent-lateral-force` | uni-upper | `load-combinations`, `dynamics.undamped-free-vibration` |
| Explaining frame stability and second-order effects | `frame-buckling-concepts` | uni-upper | `sidesway-frames`, `mech-materials.effective-length` |

## engr.soil-mechanics: 52 topics

Follows `engr.materials`, `engr.fluids`.

### Soil composition and classification

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing soil formation and clay minerals | `soil-formation-and-minerals` | uni-upper | `materials.material-classes` |
| Using weight-volume phase relations | `phase-relations` | uni-upper | `soil-formation-and-minerals` |
| Interpreting grain-size distribution curves | `grain-size-distribution` | uni-upper | `phase-relations` |
| Finding Atterberg limits and indices | `atterberg-limits` | uni-upper | `phase-relations` |
| Classifying soils with the Unified system | `uscs-classification` | uni-upper | `grain-size-distribution`, `atterberg-limits` |
| Classifying soils with the AASHTO system | `aashto-classification` | uni-upper | `uscs-classification` |

### Compaction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Interpreting compaction test curves | `compaction-curves` | uni-upper | `phase-relations` |
| Specifying and checking field compaction | `field-compaction-control` | uni-upper | `compaction-curves` |
| Choosing soil stabilization methods | `soil-stabilization` | uni-upper | `field-compaction-control` |

### Water in soils

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using Darcy's law | `darcys-law` | uni-upper | `phase-relations`, `fluids.energy-grade-lines` |
| Finding hydraulic conductivity from tests | `permeability-tests` | uni-upper | `darcys-law` |
| Finding equivalent permeability of layered soils | `layered-soil-permeability` | uni-upper | `darcys-law` |
| Analyzing one-dimensional seepage | `one-dimensional-seepage` | uni-upper | `darcys-law` |
| Analyzing seepage with flow nets | `flow-nets` | uni-upper | `one-dimensional-seepage`, `fluids.stream-function` |
| Checking seepage forces and quick conditions | `seepage-forces-and-piping` | uni-upper | `flow-nets` |

### Stresses in soil

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding total stress, pore pressure and effective stress | `effective-stress` | uni-upper | `phase-relations` |
| Finding effective stress under seepage | `effective-stress-with-seepage` | uni-upper | `effective-stress`, `one-dimensional-seepage` |
| Including capillary rise in effective stress | `capillary-effects` | uni-upper | `effective-stress`, `physics.waves-thermo-optics.capillary-rise` |
| Finding stress increase from point loads | `stress-from-point-loads` | uni-upper | `effective-stress` |
| Finding stress increase under loaded areas | `stress-from-loaded-areas` | uni-upper | `stress-from-point-loads` |

### Consolidation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Interpreting oedometer test results | `consolidation-test` | uni-upper | `effective-stress` |
| Finding preconsolidation pressure and overconsolidation ratio | `preconsolidation-pressure` | uni-upper | `consolidation-test` |
| Finding primary consolidation settlement | `primary-consolidation-settlement` | uni-upper | `preconsolidation-pressure`, `stress-from-loaded-areas` |
| Finding time rate of consolidation | `consolidation-rate` | uni-upper | `primary-consolidation-settlement` |
| Finding the coefficient of consolidation from test data | `coefficient-of-consolidation` | uni-upper | `consolidation-rate` |
| Finding secondary compression settlement | `secondary-compression` | uni-upper | `primary-consolidation-settlement` |
| Speeding consolidation with preloading and drains | `preloading-and-drains` | uni-upper | `consolidation-rate` |

### Shear strength

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the Mohr-Coulomb failure criterion | `mohr-coulomb-failure` | uni-upper | `effective-stress`, `mech-materials.mohrs-circle-stress` |
| Interpreting direct shear tests | `direct-shear-test` | uni-upper | `mohr-coulomb-failure` |
| Interpreting drained and undrained triaxial tests | `triaxial-tests` | uni-upper | `mohr-coulomb-failure` |
| Using pore pressure parameters | `pore-pressure-parameters` | uni-upper | `triaxial-tests` |
| Using undrained shear strength of clays | `undrained-strength` | uni-upper | `triaxial-tests` |
| Drawing stress paths | `stress-paths` | uni-upper | `triaxial-tests` |

### Site investigation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Planning subsurface exploration | `subsurface-exploration` | uni-upper | `uscs-classification` |
| Interpreting standard penetration and cone tests | `in-situ-tests` | uni-upper | `subsurface-exploration`, `undrained-strength` |

### Lateral earth pressure

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding at-rest earth pressure | `at-rest-pressure` | uni-upper | `effective-stress`, `mohr-coulomb-failure` |
| Finding Rankine active and passive pressures | `rankine-earth-pressure` | uni-upper | `at-rest-pressure` |
| Finding Coulomb active and passive pressures | `coulomb-earth-pressure` | uni-upper | `rankine-earth-pressure`, `statics.particle-equilibrium-2d` |
| Checking retaining walls for overturning and sliding | `retaining-wall-stability` | uni-upper | `rankine-earth-pressure` |
| Analyzing cantilever sheet pile walls | `sheet-pile-walls` | uni-upper | `rankine-earth-pressure` |

### Foundations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing shallow or deep foundations | `foundation-types` | uni-upper | `subsurface-exploration` |
| Finding bearing capacity with Terzaghi's equation | `bearing-capacity-terzaghi` | uni-upper | `mohr-coulomb-failure`, `foundation-types` |
| Using the general bearing capacity equation | `general-bearing-capacity` | uni-upper | `bearing-capacity-terzaghi` |
| Finding bearing capacity under eccentric loads | `eccentric-footing-loads` | uni-upper | `general-bearing-capacity` |
| Finding immediate settlement of footings | `immediate-settlement` | uni-upper | `stress-from-loaded-areas` |
| Sizing footings for capacity and settlement | `footing-sizing` | uni-upper | `eccentric-footing-loads`, `primary-consolidation-settlement`, `immediate-settlement` |
| Describing mat foundations | `mat-foundations` | uni-upper | `footing-sizing` |
| Finding pile capacity from end bearing and friction | `pile-capacity` | uni-upper | `general-bearing-capacity` |
| Analyzing pile groups | `pile-groups` | uni-upper | `pile-capacity` |

### Slope stability

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing stability of infinite slopes | `infinite-slopes` | uni-upper | `mohr-coulomb-failure`, `effective-stress-with-seepage` |
| Analyzing planar and circular slope failures | `planar-and-circular-failure` | uni-upper | `infinite-slopes` |
| Analyzing slopes by the method of slices | `method-of-slices` | uni-upper | `planar-and-circular-failure` |

## engr.hydraulics: 41 topics

Follows `engr.soil-mechanics`, `math.probstat`.

### Hydrology

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing hydrologic budgets | `hydrologic-cycle-budgets` | uni-upper | `fluids.control-volume-mass` |
| Finding average precipitation over a watershed | `precipitation-analysis` | uni-upper | `hydrologic-cycle-budgets` |
| Using intensity-duration-frequency curves | `idf-curves` | uni-upper | `precipitation-analysis` |
| Estimating infiltration with Horton and Green-Ampt models | `infiltration-models` | uni-upper | `hydrologic-cycle-budgets` |
| Estimating evaporation and evapotranspiration | `evaporation-and-et` | uni-upper | `hydrologic-cycle-budgets` |
| Estimating peak runoff with the rational method | `rational-method` | uni-upper | `idf-curves` |
| Estimating runoff with the curve number method | `scs-curve-number` | uni-upper | `infiltration-models` |
| Finding time of concentration | `time-of-concentration` | uni-upper | `rational-method` |
| Separating hydrograph components | `hydrograph-components` | uni-upper | `scs-curve-number` |
| Deriving and applying unit hydrographs | `unit-hydrograph` | uni-upper | `hydrograph-components` |
| Changing unit hydrograph duration with the S-curve | `s-curve-hydrograph` | uni-upper | `unit-hydrograph` |
| Building synthetic unit hydrographs | `synthetic-unit-hydrographs` | uni-upper | `unit-hydrograph`, `time-of-concentration` |

### Frequency analysis and routing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Relating return period to risk | `return-periods-and-risk` | uni-upper | `math.probstat.geometric-distribution` |
| Fitting flood frequency distributions | `flood-frequency-analysis` | uni-upper | `return-periods-and-risk`, `math.probstat.lognormal` |
| Routing floods through reservoirs | `reservoir-routing` | uni-upper | `unit-hydrograph`, `math.calc2.eulers-method-intro` |
| Routing floods through channels with Muskingum | `channel-routing` | uni-upper | `reservoir-routing` |
| Sizing stormwater detention ponds | `detention-pond-design` | uni-upper | `reservoir-routing`, `rational-method` |

### Open-channel flow

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding hydraulic radius and channel geometry | `open-channel-geometry` | uni-upper | `fluids.noncircular-ducts` |
| Finding uniform flow with Manning's equation | `uniform-flow-manning` | uni-upper | `open-channel-geometry`, `fluids.moody-chart` |
| Finding the best hydraulic section | `best-hydraulic-section` | uni-upper | `uniform-flow-manning` |
| Using specific energy and critical depth | `specific-energy` | uni-upper | `open-channel-geometry`, `fluids.dimensionless-numbers` |
| Analyzing channel transitions and humps | `transitions-and-humps` | uni-upper | `specific-energy` |
| Using the momentum function | `momentum-function` | uni-upper | `specific-energy`, `fluids.linear-momentum-cv` |
| Analyzing hydraulic jumps | `hydraulic-jump` | uni-upper | `momentum-function` |
| Classifying gradually varied flow profiles | `gradually-varied-flow` | uni-upper | `uniform-flow-manning`, `specific-energy` |
| Computing water surface profiles by the step method | `gvf-computation` | uni-upper | `gradually-varied-flow` |
| Measuring flow with weirs | `weirs` | uni-upper | `specific-energy` |
| Designing spillways and stilling basins | `spillways-and-energy-dissipation` | uni-upper | `hydraulic-jump`, `weirs` |
| Analyzing culvert flow | `culverts` | uni-upper | `specific-energy`, `fluids.minor-losses` |

### Closed-conduit systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Estimating water demand | `water-demand` | uni-upper | `hydrologic-cycle-budgets` |
| Selecting pumps for water systems | `pump-station-design` | uni-upper | `fluids.pumps-in-series-parallel`, `water-demand` |
| Analyzing water distribution networks | `distribution-network-analysis` | uni-upper | `fluids.pipe-networks`, `water-demand` |
| Sizing distribution storage | `storage-tanks` | uni-upper | `distribution-network-analysis` |
| Estimating water hammer pressures | `water-hammer` | uni-upper | `fluids.pipe-flow-problem-types`, `physics.waves-thermo-optics.speed-of-sound-derivation` |
| Designing gravity sewers | `sewer-design` | uni-upper | `uniform-flow-manning`, `water-demand` |
| Designing storm sewers | `storm-sewer-design` | uni-upper | `sewer-design`, `rational-method` |

### Groundwater

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing aquifer properties | `aquifer-properties` | uni-upper | `soil-mechanics.darcys-law` |
| Finding steady flow to wells in confined aquifers | `confined-well-flow` | uni-upper | `aquifer-properties` |
| Finding steady flow to wells in unconfined aquifers | `unconfined-well-flow` | uni-upper | `confined-well-flow` |
| Analyzing transient well flow with the Theis method | `transient-well-flow` | uni-upper | `confined-well-flow` |
| Superposing drawdown from multiple wells | `well-interference` | uni-upper | `transient-well-flow` |

## engr.steel-design: 31 topics

Follows `engr.structural-analysis`, `engr.materials`.

### Design philosophy and materials

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing LRFD and ASD design philosophies | `lrfd-and-asd` | uni-upper | `structural-analysis.load-combinations` |
| Describing structural steel grades and shapes | `structural-steel-properties` | uni-upper | `materials.ferrous-alloys`, `mech-materials.stress-strain-diagrams` |

### Tension members

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Checking tension members for yielding and rupture | `tension-yielding-and-rupture` | uni-upper | `lrfd-and-asd`, `structural-steel-properties` |
| Finding net and effective net area | `net-and-effective-area` | uni-upper | `tension-yielding-and-rupture` |
| Finding net area with staggered holes | `staggered-holes` | uni-upper | `net-and-effective-area` |
| Checking block shear rupture | `block-shear` | uni-upper | `net-and-effective-area` |
| Designing tension members | `tension-member-design` | uni-upper | `block-shear`, `staggered-holes` |

### Compression members

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding compressive strength from column curves | `column-strength-curves` | uni-upper | `lrfd-and-asd`, `mech-materials.effective-length` |
| Classifying sections for local buckling | `local-buckling-classification` | uni-upper | `column-strength-curves` |
| Designing steel columns | `column-design-steel` | uni-upper | `local-buckling-classification` |
| Finding effective length factors with alignment charts | `alignment-charts` | uni-upper | `column-design-steel`, `structural-analysis.frame-buckling-concepts` |
| Designing built-up compression members | `built-up-columns` | uni-upper | `column-design-steel` |

### Beams

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding plastic moment capacity of beams | `plastic-moment-capacity` | uni-upper | `lrfd-and-asd`, `mech-materials.plastic-bending` |
| Checking lateral-torsional buckling | `lateral-torsional-buckling` | uni-upper | `plastic-moment-capacity` |
| Using the moment gradient factor | `moment-gradient-factor` | uni-upper | `lateral-torsional-buckling` |
| Checking shear strength of steel beams | `beam-shear-steel` | uni-upper | `plastic-moment-capacity` |
| Checking serviceability deflection | `beam-deflection-limits` | uni-upper | `plastic-moment-capacity`, `mech-materials.deflection-by-superposition` |
| Designing steel beams | `beam-design-steel` | uni-upper | `moment-gradient-factor`, `beam-shear-steel`, `beam-deflection-limits` |

### Beam-columns

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Amplifying moments for second-order effects | `second-order-amplification` | uni-upper | `beam-design-steel`, `column-design-steel` |
| Checking beam-columns with interaction equations | `interaction-equations` | uni-upper | `second-order-amplification` |
| Designing beam-columns | `beam-column-design` | uni-upper | `interaction-equations` |

### Connections

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Checking bolt shear and bearing strength | `bolt-shear-and-bearing` | uni-upper | `tension-member-design` |
| Designing slip-critical connections | `slip-critical-connections` | uni-upper | `bolt-shear-and-bearing` |
| Analyzing eccentrically loaded bolt groups | `eccentric-bolt-groups` | uni-upper | `bolt-shear-and-bearing`, `statics.polar-moment-of-area` |
| Designing fillet welds | `fillet-welds` | uni-upper | `tension-member-design` |
| Analyzing eccentrically loaded welds | `eccentric-welds` | uni-upper | `fillet-welds`, `eccentric-bolt-groups` |
| Designing simple shear connections | `simple-shear-connections` | uni-upper | `bolt-shear-and-bearing`, `fillet-welds` |
| Describing moment connections | `moment-connections` | uni-upper | `simple-shear-connections` |
| Designing column base plates | `base-plates` | uni-upper | `column-design-steel` |

### Composite construction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing composite steel-concrete beams | `composite-beams-steel` | uni-upper | `beam-design-steel`, `mech-materials.composite-beams` |
| Designing shear connectors | `shear-studs` | uni-upper | `composite-beams-steel` |

## engr.concrete-design: 35 topics

Follows `engr.structural-analysis`, `engr.soil-mechanics`.

### Materials and philosophy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing concrete strength and stress-strain behaviour | `concrete-properties` | uni-upper | `materials.construction-materials` |
| Describing reinforcing bars | `reinforcing-steel` | uni-upper | `concrete-properties` |
| Proportioning concrete mixes | `concrete-mix-design` | uni-upper | `concrete-properties` |
| Explaining the strength design method | `strength-design-method` | uni-upper | `concrete-properties`, `structural-analysis.load-combinations` |

### Flexure

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing uncracked and cracked sections | `cracked-section-behaviour` | uni-upper | `reinforcing-steel`, `mech-materials.composite-beams` |
| Using the equivalent rectangular stress block | `whitney-stress-block` | uni-upper | `cracked-section-behaviour`, `strength-design-method` |
| Finding flexural strength of singly reinforced beams | `singly-reinforced-analysis` | uni-upper | `whitney-stress-block` |
| Classifying sections by strain and finding strength reduction factors | `strain-limits-and-phi` | uni-upper | `singly-reinforced-analysis` |
| Designing singly reinforced beams | `singly-reinforced-design` | uni-upper | `strain-limits-and-phi` |
| Analyzing and designing doubly reinforced beams | `doubly-reinforced-beams` | uni-upper | `singly-reinforced-design` |
| Analyzing and designing T-beams | `t-beams` | uni-upper | `singly-reinforced-design` |
| Designing one-way slabs | `one-way-slabs` | uni-upper | `singly-reinforced-design` |
| Designing continuous beams with moment coefficients | `continuous-beams-concrete` | uni-upper | `t-beams`, `structural-analysis.moment-distribution-beams` |

### Shear and torsion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding concrete shear strength | `shear-strength-concrete` | uni-upper | `singly-reinforced-analysis` |
| Designing shear reinforcement | `stirrup-design` | uni-upper | `shear-strength-concrete` |
| Designing for torsion | `torsion-in-concrete` | uni-upper | `stirrup-design` |

### Bond and detailing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding development length of bars | `development-length` | uni-upper | `reinforcing-steel`, `singly-reinforced-design` |
| Detailing hooks and splices | `hooks-and-splices` | uni-upper | `development-length` |
| Locating bar cutoffs | `bar-cutoffs` | uni-upper | `development-length`, `continuous-beams-concrete` |

### Serviceability

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding immediate deflection with effective moment of inertia | `immediate-deflection-concrete` | uni-upper | `cracked-section-behaviour`, `mech-materials.deflection-by-superposition` |
| Finding long-term deflection | `long-term-deflection` | uni-upper | `immediate-deflection-concrete` |
| Controlling cracking by bar spacing | `crack-control` | uni-upper | `singly-reinforced-design` |

### Columns

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding axial strength of short columns | `short-column-axial` | uni-upper | `strength-design-method` |
| Detailing tied and spiral columns | `tied-and-spiral-columns` | uni-upper | `short-column-axial` |
| Constructing column interaction diagrams | `interaction-diagrams` | uni-upper | `short-column-axial`, `strain-limits-and-phi` |
| Designing columns for axial load and moment | `column-design-with-moment` | uni-upper | `interaction-diagrams` |
| Designing slender columns by moment magnification | `slender-columns` | uni-upper | `column-design-with-moment`, `structural-analysis.frame-buckling-concepts` |

### Slabs and footings

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing two-way slabs | `two-way-slabs` | uni-upper | `one-way-slabs` |
| Checking punching shear | `punching-shear` | uni-upper | `two-way-slabs`, `shear-strength-concrete` |
| Designing wall footings | `wall-footings` | uni-upper | `soil-mechanics.footing-sizing`, `shear-strength-concrete` |
| Designing isolated column footings | `column-footings` | uni-upper | `wall-footings`, `punching-shear` |
| Designing reinforced retaining walls | `retaining-wall-design` | uni-upper | `soil-mechanics.retaining-wall-stability`, `singly-reinforced-design` |

### Prestressed concrete

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining prestressing | `prestressing-concepts` | uni-upper | `singly-reinforced-analysis` |
| Finding stresses in prestressed beams | `prestress-stresses` | uni-upper | `prestressing-concepts`, `mech-materials.combined-loadings` |
| Estimating prestress losses | `prestress-losses` | uni-upper | `prestress-stresses` |

## engr.transportation: 35 topics

Follows `engr.soil-mechanics`, `math.probstat`.

### Vehicle and driver

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding vehicle forces and acceleration | `vehicle-performance` | uni-upper | `dynamics.kinetics-with-friction` |
| Finding braking distance | `braking-distance` | uni-upper | `vehicle-performance` |
| Finding stopping sight distance | `stopping-sight-distance` | uni-upper | `braking-distance` |

### Geometric design

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Laying out horizontal curves | `horizontal-curves` | uni-upper | `stopping-sight-distance`, `math.geom.trig-find-side` |
| Designing superelevation and side friction | `superelevation` | uni-upper | `horizontal-curves`, `dynamics.equations-of-motion-nt` |
| Finding sight distance on horizontal curves | `sight-distance-on-horizontal-curves` | uni-upper | `horizontal-curves` |
| Using spiral transition curves | `spiral-curves` | uni-upper | `superelevation` |
| Designing crest and sag vertical curves | `vertical-curves` | uni-upper | `stopping-sight-distance`, `math.calc1.second-derivative-test` |
| Finding high and low points of vertical curves | `vertical-curve-high-low-points` | uni-upper | `vertical-curves` |
| Computing earthwork volumes | `cross-sections-and-earthwork` | uni-upper | `vertical-curves` |
| Using mass haul diagrams | `mass-haul-diagrams` | uni-upper | `cross-sections-and-earthwork` |
| Finding elevations by differential leveling | `survey-leveling` | uni-upper | `cross-sections-and-earthwork` |

### Traffic flow

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Relating flow, density and speed | `traffic-stream-parameters` | uni-upper | `vehicle-performance` |
| Using the Greenshields model | `greenshields-model` | uni-upper | `traffic-stream-parameters` |
| Analyzing traffic shock waves | `shock-waves-traffic` | uni-upper | `greenshields-model` |
| Analyzing queues at bottlenecks | `queueing-models` | uni-upper | `traffic-stream-parameters`, `math.probstat.poisson-process-intro` |
| Modelling headways with the exponential distribution | `headway-distributions` | uni-upper | `traffic-stream-parameters`, `math.probstat.exponential-distribution` |

### Capacity and level of service

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding freeway level of service | `freeway-level-of-service` | uni-upper | `greenshields-model` |
| Finding level of service on multilane and two-lane highways | `multilane-and-two-lane-highways` | uni-upper | `freeway-level-of-service` |

### Intersections

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing intersection control | `intersection-control-types` | uni-upper | `traffic-stream-parameters` |
| Finding cycle length and green splits | `signal-timing-basics` | uni-upper | `intersection-control-types` |
| Finding delay and level of service at signals | `signalized-intersection-delay` | uni-upper | `signal-timing-basics`, `queueing-models` |
| Analyzing roundabout capacity | `roundabouts` | uni-upper | `intersection-control-types` |

### Pavements

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing flexible and rigid pavements | `pavement-types` | uni-upper | `materials.construction-materials` |
| Finding equivalent single-axle loads | `equivalent-single-axle-loads` | uni-upper | `pavement-types` |
| Characterizing subgrade for pavement design | `subgrade-characterization` | uni-upper | `soil-mechanics.aashto-classification`, `pavement-types` |
| Designing flexible pavements | `flexible-pavement-design` | uni-upper | `equivalent-single-axle-loads`, `subgrade-characterization` |
| Designing rigid pavements | `rigid-pavement-design` | uni-upper | `equivalent-single-axle-loads`, `subgrade-characterization` |
| Proportioning asphalt mixes | `asphalt-mix-design` | uni-upper | `pavement-types` |
| Planning pavement drainage and rehabilitation | `pavement-drainage-and-rehab` | uni-upper | `flexible-pavement-design` |

### Planning and safety

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Estimating trip generation | `trip-generation` | uni-upper | `traffic-stream-parameters`, `math.probstat.simple-linear-model` |
| Distributing trips with the gravity model | `trip-distribution` | uni-upper | `trip-generation` |
| Modelling mode choice with logit models | `mode-choice` | uni-upper | `trip-distribution` |
| Assigning traffic to routes | `traffic-assignment` | uni-upper | `mode-choice` |
| Analyzing crash rates and countermeasures | `crash-analysis` | uni-upper | `traffic-stream-parameters` |

## engr.environmental: 32 topics

Follows `engr.hydraulics`, `chem.gen2`, `bio.micro`.

### Water chemistry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Converting environmental concentration units | `concentration-units-environmental` | uni-upper | `chem.gen2.fractional-composition` |
| Analyzing the carbonate system and alkalinity | `carbonate-system` | uni-upper | `concentration-units-environmental`, `chem.gen2.polyprotic-species-concentrations` |
| Finding water hardness | `hardness` | uni-upper | `carbonate-system` |
| Finding gas solubility with Henry's law | `gas-transfer-and-henry` | uni-upper | `concentration-units-environmental`, `chem.gen1.henrys-law` |

### Mass balance and reactors

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing mass balances for environmental systems | `environmental-mass-balance` | uni-upper | `concentration-units-environmental`, `fluids.control-volume-mass` |
| Modelling first-order decay | `first-order-decay` | uni-upper | `environmental-mass-balance`, `math.calc2.exponential-growth-de` |
| Modelling mixed-flow and plug-flow reactors | `cmfr-and-pfr-models` | uni-upper | `first-order-decay` |
| Analyzing reactors in series | `reactors-in-series` | uni-upper | `cmfr-and-pfr-models` |

### Water quality

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Modelling biochemical oxygen demand | `bod-kinetics` | uni-upper | `first-order-decay`, `bio.micro.bacterial-growth-curves` |
| Modelling oxygen sag in rivers | `dissolved-oxygen-sag` | uni-upper | `bod-kinetics`, `gas-transfer-and-henry` |
| Modelling phosphorus in lakes | `lake-nutrients` | uni-upper | `environmental-mass-balance` |
| Interpreting water quality standards | `water-quality-standards` | uni-upper | `concentration-units-environmental` |

### Drinking water treatment

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Laying out a drinking water treatment train | `treatment-train` | uni-upper | `water-quality-standards` |
| Designing coagulation and flocculation | `coagulation-flocculation` | uni-upper | `treatment-train` |
| Designing sedimentation basins | `sedimentation` | uni-upper | `coagulation-flocculation`, `fluids.drag-coefficients` |
| Designing granular media filters | `filtration` | uni-upper | `sedimentation`, `soil-mechanics.darcys-law` |
| Designing disinfection with CT values | `disinfection` | uni-upper | `filtration`, `first-order-decay` |
| Designing lime-soda softening | `softening` | uni-upper | `hardness` |
| Choosing adsorption and membrane processes | `adsorption-and-membranes-water` | uni-upper | `filtration` |

### Wastewater treatment

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Characterizing municipal wastewater | `wastewater-characteristics` | uni-upper | `bod-kinetics` |
| Designing preliminary and primary treatment | `preliminary-and-primary` | uni-upper | `wastewater-characteristics`, `sedimentation` |
| Modelling microbial growth with Monod kinetics | `monod-kinetics` | uni-upper | `bod-kinetics` |
| Designing activated sludge systems | `activated-sludge` | uni-upper | `monod-kinetics`, `cmfr-and-pfr-models` |
| Designing secondary clarifiers | `secondary-clarifiers` | uni-upper | `activated-sludge`, `sedimentation` |
| Describing biological nitrogen and phosphorus removal | `nutrient-removal` | uni-upper | `activated-sludge` |
| Designing sludge thickening and digestion | `sludge-treatment` | uni-upper | `activated-sludge` |

### Air, waste and impact

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing air pollutants and sources | `air-pollutant-sources` | uni-upper | `concentration-units-environmental` |
| Estimating concentrations with the Gaussian plume model | `gaussian-plume` | uni-upper | `air-pollutant-sources`, `math.probstat.normal-distribution-pdf` |
| Choosing air pollution control devices | `air-pollution-control` | uni-upper | `air-pollutant-sources` |
| Planning solid waste collection and landfills | `solid-waste-management` | uni-upper | `environmental-mass-balance` |
| Modelling contaminant transport in groundwater | `groundwater-contamination` | uni-upper | `hydraulics.aquifer-properties`, `first-order-decay` |
| Estimating risk from exposure | `risk-assessment-environmental` | uni-upper | `concentration-units-environmental` |

## engr.heat-transfer: 56 topics

Follows `engr.thermo`, `engr.fluids`, `math.diffeq`.

### Conduction fundamentals

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Combining conduction, convection and radiation in energy balances | `heat-transfer-modes` | uni-upper | `thermo.closed-system-energy-balance`, `physics.waves-thermo-optics.conduction-through-layers` |
| Using Fourier's law and thermal conductivity | `fourier-law-and-conductivity` | uni-upper | `heat-transfer-modes` |
| Writing the heat diffusion equation with generation | `heat-diffusion-equation` | uni-upper | `fourier-law-and-conductivity`, `math.calc3.divergence` |
| Writing thermal boundary conditions | `conduction-boundary-conditions` | uni-upper | `heat-diffusion-equation` |

### Steady one-dimensional conduction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving conduction in plane walls | `plane-wall-conduction` | uni-upper | `conduction-boundary-conditions` |
| Using thermal resistance networks | `thermal-resistance-networks` | uni-upper | `plane-wall-conduction` |
| Including contact resistance | `contact-resistance` | uni-upper | `thermal-resistance-networks` |
| Solving conduction in cylinders and spheres | `radial-systems` | uni-upper | `thermal-resistance-networks`, `physics.waves-thermo-optics.radial-conduction` |
| Finding the critical radius of insulation | `critical-insulation-radius` | uni-upper | `radial-systems` |
| Solving conduction with internal heat generation | `conduction-with-generation` | uni-upper | `plane-wall-conduction`, `radial-systems` |

### Extended surfaces

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving the fin equation | `fin-equation` | uni-upper | `conduction-boundary-conditions`, `math.diffeq.constant-coefficients-real` |
| Finding temperature and heat rate for fins | `fin-solutions` | uni-upper | `fin-equation` |
| Using fin efficiency and effectiveness | `fin-efficiency` | uni-upper | `fin-solutions` |
| Analyzing fin arrays | `fin-arrays` | uni-upper | `fin-efficiency`, `thermal-resistance-networks` |

### Multidimensional conduction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using conduction shape factors | `shape-factors` | uni-upper | `thermal-resistance-networks` |
| Solving steady conduction by finite differences | `finite-difference-conduction` | uni-upper | `conduction-with-generation`, `math.linalg.gaussian-elimination` |

### Transient conduction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the lumped capacitance method | `lumped-capacitance` | uni-upper | `heat-transfer-modes`, `physics.waves-thermo-optics.cooling-with-differential-equations` |
| Checking lumped capacitance with the Biot number | `biot-number` | uni-upper | `lumped-capacitance`, `thermal-resistance-networks` |
| Using one-term solutions for plane walls, cylinders and spheres | `one-term-solutions` | uni-upper | `biot-number` |
| Analyzing transient conduction in semi-infinite solids | `semi-infinite-solids` | uni-upper | `biot-number` |
| Combining one-dimensional transient solutions | `multidimensional-transient` | uni-upper | `one-term-solutions` |
| Solving transient conduction by finite differences | `transient-finite-difference` | uni-upper | `finite-difference-conduction`, `one-term-solutions` |

### Convection fundamentals

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining local and average convection coefficients | `convection-coefficients` | uni-upper | `heat-transfer-modes` |
| Describing velocity and thermal boundary layers | `thermal-boundary-layers` | uni-upper | `convection-coefficients`, `fluids.boundary-layer-concepts` |
| Using Nusselt, Prandtl and Reynolds numbers | `convection-dimensionless-groups` | uni-upper | `thermal-boundary-layers`, `fluids.dimensionless-numbers` |
| Using the Reynolds and Chilton-Colburn analogies | `reynolds-analogy` | uni-upper | `convection-dimensionless-groups` |

### External forced convection

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding convection on flat plates | `flat-plate-convection` | uni-upper | `convection-dimensionless-groups`, `fluids.flat-plate-boundary-layer` |
| Finding convection with mixed laminar and turbulent flow | `mixed-boundary-layer-plates` | uni-upper | `flat-plate-convection` |
| Finding convection for cylinders in crossflow | `cylinders-in-crossflow` | uni-upper | `flat-plate-convection` |
| Finding convection for spheres and tube banks | `spheres-and-tube-banks` | uni-upper | `cylinders-in-crossflow` |

### Internal forced convection

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing energy balances with mean fluid temperature | `mean-temperature-energy-balance` | uni-upper | `convection-coefficients`, `thermo.steady-flow-energy-balance` |
| Analyzing tubes with constant heat flux or surface temperature | `constant-flux-and-temperature` | uni-upper | `mean-temperature-energy-balance` |
| Using log-mean temperature difference in tubes | `log-mean-temperature-difference` | uni-upper | `constant-flux-and-temperature` |
| Finding convection in laminar tube flow | `laminar-internal-convection` | uni-upper | `constant-flux-and-temperature`, `fluids.entrance-length` |
| Finding convection in turbulent tube flow | `turbulent-internal-convection` | uni-upper | `laminar-internal-convection` |

### Free convection

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using Grashof and Rayleigh numbers | `grashof-and-rayleigh` | uni-upper | `convection-dimensionless-groups` |
| Finding free convection on vertical plates | `vertical-plate-free-convection` | uni-upper | `grashof-and-rayleigh` |
| Finding free convection on horizontal surfaces and cylinders | `free-convection-other-geometries` | uni-upper | `vertical-plate-free-convection` |
| Finding free convection in enclosures | `enclosure-free-convection` | uni-upper | `free-convection-other-geometries` |
| Judging when forced and free convection combine | `mixed-convection` | uni-upper | `vertical-plate-free-convection`, `flat-plate-convection` |

### Boiling and condensation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing the boiling curve | `boiling-curve` | uni-upper | `convection-coefficients`, `thermo.phase-change-processes` |
| Finding nucleate boiling heat flux and critical heat flux | `nucleate-boiling` | uni-upper | `boiling-curve` |
| Finding heat transfer in film condensation | `film-condensation` | uni-upper | `boiling-curve`, `vertical-plate-free-convection` |

### Heat exchangers

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing heat exchanger types | `heat-exchanger-types` | uni-upper | `thermo.heat-exchanger-energy-balance` |
| Finding overall heat transfer coefficients with fouling | `overall-heat-transfer-coefficient` | uni-upper | `heat-exchanger-types`, `radial-systems` |
| Sizing heat exchangers by the LMTD method | `lmtd-method` | uni-upper | `overall-heat-transfer-coefficient`, `log-mean-temperature-difference` |
| Using LMTD correction factors | `lmtd-correction-factors` | uni-upper | `lmtd-method` |
| Rating heat exchangers by the effectiveness-NTU method | `effectiveness-ntu` | uni-upper | `lmtd-method` |
| Choosing between LMTD and effectiveness-NTU | `choosing-hx-method` | uni-upper | `effectiveness-ntu`, `lmtd-correction-factors` |

### Radiation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using Planck's law and blackbody functions | `blackbody-radiation` | uni-upper | `heat-transfer-modes`, `physics.waves-thermo-optics.radiation-exchange` |
| Using emissivity, absorptivity and reflectivity | `surface-radiative-properties` | uni-upper | `blackbody-radiation` |
| Finding view factors with relations and charts | `view-factors` | uni-upper | `surface-radiative-properties` |
| Finding radiation exchange between black surfaces | `blackbody-exchange` | uni-upper | `view-factors` |
| Solving radiation exchange in gray enclosures | `gray-surface-networks` | uni-upper | `blackbody-exchange` |
| Analyzing radiation shields | `radiation-shields` | uni-upper | `gray-surface-networks` |
| Solving problems with combined convection and radiation | `combined-modes` | uni-upper | `radiation-shields`, `flat-plate-convection` |

## engr.machine-design: 47 topics

Follows `engr.materials`, `engr.fluids`, `math.probstat`.

### Design for strength

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing design factors and estimating reliability | `design-factors-and-reliability` | uni-upper | `mech-materials.allowable-stress-design`, `math.probstat.normal-distribution-pdf` |
| Applying distortion-energy and maximum-shear theories | `static-failure-ductile` | uni-upper | `mech-materials.failure-theories-intro` |
| Applying Coulomb-Mohr and modified Mohr theories | `static-failure-brittle` | uni-upper | `static-failure-ductile` |
| Using stress concentration and notch sensitivity | `stress-concentration-design` | uni-upper | `static-failure-ductile`, `materials.fracture-toughness` |

### Fatigue

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Estimating endurance limits | `endurance-limit` | uni-upper | `materials.fatigue-basics` |
| Modifying endurance limits with Marin factors | `marin-factors` | uni-upper | `endurance-limit` |
| Applying fatigue stress concentration factors | `fatigue-stress-concentration` | uni-upper | `marin-factors`, `stress-concentration-design` |
| Analyzing fluctuating stresses with Goodman and Gerber criteria | `fluctuating-stresses` | uni-upper | `fatigue-stress-concentration` |
| Analyzing combined fatigue loading | `combined-fatigue-loading` | uni-upper | `fluctuating-stresses` |
| Using Miner's rule | `cumulative-fatigue-damage` | uni-upper | `fluctuating-stresses` |

### Shafts

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Laying out shafts and attachments | `shaft-layout` | uni-upper | `mech-materials.power-transmission-shafts` |
| Designing shafts for fatigue | `shaft-stress-design` | uni-upper | `shaft-layout`, `combined-fatigue-loading` |
| Checking shaft deflection and slope | `shaft-deflection` | uni-upper | `shaft-stress-design`, `mech-materials.deflection-by-superposition` |
| Finding critical speeds of shafts | `critical-speeds` | uni-upper | `shaft-deflection`, `dynamics.undamped-free-vibration` |
| Designing keys and couplings | `keys-and-couplings` | uni-upper | `shaft-stress-design` |
| Choosing limits and fits | `limits-and-fits` | uni-upper | `shaft-layout` |

### Screws and fasteners

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing power screws | `power-screws` | uni-upper | `statics.square-threaded-screws` |
| Finding bolt and member stiffness | `bolted-joint-stiffness` | uni-upper | `mech-materials.axial-deformation` |
| Designing bolt preload for static loads | `bolt-preload` | uni-upper | `bolted-joint-stiffness` |
| Analyzing fatigue of bolted joints | `fatigue-of-bolted-joints` | uni-upper | `bolt-preload`, `fluctuating-stresses` |
| Analyzing bolted joints in shear | `bolts-in-shear` | uni-upper | `bolt-preload` |
| Designing welded joints | `welded-joints` | uni-upper | `static-failure-ductile`, `mech-materials.shear-flow-built-up` |

### Springs

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding stress and deflection of helical springs | `helical-compression-springs` | uni-upper | `mech-materials.torsion-of-circular-shafts` |
| Designing helical compression springs | `spring-design` | uni-upper | `helical-compression-springs` |
| Designing springs for fatigue | `spring-fatigue` | uni-upper | `spring-design`, `fluctuating-stresses` |
| Designing extension and torsion springs | `extension-and-torsion-springs` | uni-upper | `spring-design` |

### Bearings

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding rolling bearing life | `rolling-bearing-life` | uni-upper | `design-factors-and-reliability` |
| Selecting rolling bearings for combined loads | `rolling-bearing-selection` | uni-upper | `rolling-bearing-life` |
| Analyzing hydrodynamic journal bearings | `journal-bearing-lubrication` | uni-upper | `fluids.couette-flow` |

### Gears

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing spur gear geometry | `gear-geometry` | uni-upper | `dynamics.linkage-velocity-analysis` |
| Analyzing simple, compound and planetary gear trains | `gear-trains` | uni-upper | `gear-geometry` |
| Finding forces on spur and helical gears | `gear-force-analysis` | uni-upper | `gear-geometry` |
| Finding gear bending stress with the Lewis equation | `lewis-bending-stress` | uni-upper | `gear-force-analysis` |
| Checking gears with AGMA bending and contact equations | `agma-bending-and-contact` | uni-upper | `lewis-bending-stress` |
| Describing helical, bevel and worm gears | `helical-bevel-worm-gears` | uni-upper | `gear-force-analysis` |

### Flexible elements and clutches

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing flat and V-belt drives | `belt-drives` | uni-upper | `statics.belt-friction` |
| Selecting roller chains | `chain-drives` | uni-upper | `belt-drives` |
| Analyzing clutches and brakes | `clutches-and-brakes` | uni-upper | `statics.bearing-and-disk-friction` |
| Sizing flywheels | `flywheels` | uni-upper | `dynamics.rigid-work-energy` |

### Mechanisms

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Synthesizing four-bar linkages graphically | `linkage-synthesis` | uni-upper | `dynamics.linkage-velocity-analysis` |
| Classifying linkages with the Grashof condition | `grashof-condition` | uni-upper | `linkage-synthesis` |
| Designing cam displacement profiles | `cam-profiles` | uni-upper | `dynamics.linkage-acceleration-analysis` |
| Finding dynamic forces in mechanisms | `dynamic-force-analysis` | uni-upper | `dynamics.linkage-acceleration-analysis`, `dynamics.general-plane-motion-kinetics` |
| Balancing rotating and reciprocating masses | `balancing` | uni-upper | `dynamic-force-analysis` |

### Design tools

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing thick-walled cylinders and press fits | `pressure-vessels-and-press-fits` | uni-upper | `mech-materials.thin-walled-pressure-vessels`, `limits-and-fits` |
| Explaining finite element analysis for machine parts | `finite-element-basics` | uni-upper | `statics.truss-matrix-solution`, `mech-materials.axial-deformation` |
| Reading geometric dimensioning and tolerancing | `gdt-basics` | uni-upper | `limits-and-fits` |

## engr.vibrations: 28 topics

Follows `engr.dynamics`, `math.diffeq`, `math.linalg`.

### Single degree of freedom

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Modelling systems with equivalent mass, stiffness and damping | `sdof-modelling` | uni-upper | `dynamics.energy-method-vibration` |
| Finding free response of damped systems | `free-damped-response` | uni-upper | `sdof-modelling`, `dynamics.viscous-damped-vibration` |
| Finding damping from logarithmic decrement | `logarithmic-decrement` | uni-upper | `free-damped-response` |
| Analyzing Coulomb damping | `coulomb-damping` | uni-upper | `free-damped-response` |
| Finding harmonic forced response | `harmonic-forced-response` | uni-upper | `free-damped-response`, `dynamics.forced-vibration-basics` |
| Analyzing rotating unbalance | `rotating-unbalance` | uni-upper | `harmonic-forced-response` |
| Analyzing base excitation | `base-excitation` | uni-upper | `harmonic-forced-response` |
| Designing vibration isolators | `vibration-isolation` | uni-upper | `base-excitation`, `rotating-unbalance` |
| Explaining vibration sensors | `vibration-measurement` | uni-upper | `base-excitation` |

### General forcing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding response to periodic forcing with Fourier series | `periodic-forcing` | uni-upper | `harmonic-forced-response`, `math.diffeq.fourier-series-intro` |
| Finding impulse response | `impulse-response-vibration` | uni-upper | `free-damped-response`, `math.diffeq.impulse-delta` |
| Finding response by the convolution integral | `convolution-response` | uni-upper | `impulse-response-vibration`, `math.diffeq.convolution` |
| Finding shock response spectra | `shock-response` | uni-upper | `convolution-response` |
| Solving vibration problems with Laplace transforms | `laplace-vibration` | uni-upper | `harmonic-forced-response`, `math.diffeq.solve-ivp-laplace` |

### Multiple degrees of freedom

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing equations of motion for two degrees of freedom | `two-dof-equations` | uni-upper | `sdof-modelling`, `math.diffeq.matrix-form-systems` |
| Finding natural frequencies and mode shapes | `natural-frequencies-mode-shapes` | uni-upper | `two-dof-equations`, `math.linalg.find-eigenvectors` |
| Finding free response of multi-degree systems | `free-response-mdof` | uni-upper | `natural-frequencies-mode-shapes` |
| Finding forced response of two-degree systems | `forced-response-mdof` | uni-upper | `natural-frequencies-mode-shapes` |
| Designing tuned vibration absorbers | `vibration-absorbers` | uni-upper | `forced-response-mdof` |
| Decoupling equations by modal analysis | `modal-analysis` | uni-upper | `free-response-mdof`, `math.linalg.orthogonal-diagonalization` |
| Using proportional damping | `proportional-damping` | uni-upper | `modal-analysis` |
| Deriving equations of motion with Lagrange's equations | `lagrange-equations-vibration` | uni-upper | `two-dof-equations` |

### Continuous systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding modes of strings and bars | `string-and-bar-vibration` | uni-upper | `natural-frequencies-mode-shapes`, `math.diffeq.boundary-value-eigenproblems` |
| Finding natural frequencies of beams | `beam-vibration` | uni-upper | `string-and-bar-vibration` |
| Estimating fundamental frequency by Rayleigh's method | `rayleigh-method` | uni-upper | `beam-vibration` |

### Numerical and experimental methods

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Simulating vibration numerically | `numerical-vibration` | uni-upper | `harmonic-forced-response`, `math.diffeq.improved-euler-rk4` |
| Measuring frequency response functions | `frequency-response-functions` | uni-upper | `harmonic-forced-response` |
| Extracting modal parameters from tests | `experimental-modal-analysis` | uni-upper | `frequency-response-functions`, `modal-analysis` |

## engr.manufacturing: 32 topics

Follows `engr.machine-design`.

### Measurement and quality

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Measuring parts and surface finish | `dimensional-metrology` | uni-upper | `machine-design.limits-and-fits` |
| Finding process capability indices | `process-capability` | uni-upper | `dimensional-metrology`, `math.probstat.normal-distribution-pdf` |
| Using control charts | `statistical-process-control` | uni-upper | `process-capability` |

### Casting

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing casting processes | `casting-processes` | uni-upper | `materials.microstructure-development` |
| Finding solidification time with Chvorinov's rule | `solidification-time` | uni-upper | `casting-processes` |
| Designing gating systems and risers | `gating-and-risers` | uni-upper | `solidification-time`, `fluids.bernoulli-applications` |
| Diagnosing casting defects | `casting-defects` | uni-upper | `gating-and-risers` |

### Forming

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using flow stress and strain hardening | `plastic-flow-stress` | uni-upper | `materials.true-stress-strain` |
| Finding forces and power in rolling | `rolling-process` | uni-upper | `plastic-flow-stress` |
| Finding forging forces | `forging` | uni-upper | `plastic-flow-stress` |
| Finding extrusion and drawing forces | `extrusion-and-drawing` | uni-upper | `plastic-flow-stress` |
| Analyzing shearing, bending and deep drawing | `sheet-metal-forming` | uni-upper | `plastic-flow-stress` |
| Using forming limit diagrams | `forming-limits` | uni-upper | `sheet-metal-forming` |

### Machining

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing orthogonal cutting | `cutting-mechanics` | uni-upper | `plastic-flow-stress` |
| Finding cutting forces and power | `cutting-forces-and-power` | uni-upper | `cutting-mechanics` |
| Predicting tool life with Taylor's equation | `tool-life` | uni-upper | `cutting-forces-and-power` |
| Finding machining time for turning, milling and drilling | `turning-milling-drilling` | uni-upper | `cutting-forces-and-power` |
| Choosing cutting speed for minimum cost | `machining-economics` | uni-upper | `tool-life`, `turning-milling-drilling` |
| Describing grinding and finishing processes | `grinding-and-finishing` | uni-upper | `cutting-mechanics` |
| Describing EDM, laser and waterjet machining | `nontraditional-machining` | uni-upper | `turning-milling-drilling` |

### Polymer, powder and additive processes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing injection molding | `injection-molding` | uni-upper | `materials.polymer-mechanical-behaviour` |
| Describing extrusion, blow molding and thermoforming | `other-polymer-processes` | uni-upper | `injection-molding` |
| Describing powder metallurgy | `powder-metallurgy` | uni-upper | `materials.ceramic-structures` |
| Comparing additive manufacturing processes | `additive-manufacturing` | uni-upper | `injection-molding` |
| Describing composite fabrication | `composite-fabrication` | uni-upper | `materials.fiber-composites` |

### Joining

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing fusion welding processes | `fusion-welding` | uni-upper | `materials.microstructure-development` |
| Finding welding heat input | `welding-heat-input` | uni-upper | `fusion-welding` |
| Describing brazing, soldering and solid-state joining | `solid-state-joining` | uni-upper | `fusion-welding` |

### Systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing basic CNC part programs | `cnc-programming` | uni-upper | `turning-milling-drilling` |
| Selecting a manufacturing process | `process-selection` | uni-upper | `casting-defects`, `forming-limits`, `machining-economics`, `additive-manufacturing` |
| Applying design for manufacture and assembly | `design-for-manufacture` | uni-upper | `process-selection` |
| Analyzing production rates and line balancing | `production-systems` | uni-upper | `process-selection` |

## engr.measurements: 23 topics

Follows `engr.controls`, `engr.fluids`, `engr.mech-materials`, `math.probstat`, `engr.programming`.

### Measurement systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing elements of a measurement system | `measurement-system-elements` | uni-upper | `math.probstat.sample-mean-moments` |
| Finding sensitivity and linearity from calibration | `static-calibration` | uni-upper | `measurement-system-elements`, `math.probstat.simple-linear-model` |
| Finding time constants of first-order instruments | `first-order-instruments` | uni-upper | `static-calibration`, `controls.first-order-system-response` |
| Finding response of second-order instruments | `second-order-instruments` | uni-upper | `first-order-instruments`, `controls.second-order-system-response` |

### Statistics and uncertainty

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing measurements with finite statistics | `measurement-statistics` | uni-upper | `measurement-system-elements`, `math.probstat.ci-small-sample-t` |
| Rejecting outliers with Chauvenet's criterion | `outlier-rejection` | uni-upper | `measurement-statistics` |
| Propagating uncertainty in calculated results | `uncertainty-propagation` | uni-upper | `measurement-statistics`, `math.calc3.partial-derivatives-compute` |
| Estimating design-stage uncertainty | `design-stage-uncertainty` | uni-upper | `uncertainty-propagation` |
| Finding uncertainty in curve fits | `regression-uncertainty` | uni-upper | `uncertainty-propagation`, `math.probstat.inference-for-regression` |

### Signal conditioning and acquisition

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing Wheatstone bridges | `wheatstone-bridges` | uni-upper | `circuits.voltage-and-current-dividers` |
| Using instrumentation amplifiers | `instrumentation-amplifiers` | uni-upper | `circuits.summing-and-difference-amps` |
| Choosing analog filters for measurement | `analog-filters-for-measurement` | uni-upper | `circuits.active-filters` |
| Finding ADC resolution and quantization error | `adc-resolution` | uni-upper | `signals.quantization` |
| Choosing sampling rate and anti-alias filters | `daq-sampling` | uni-upper | `signals.aliasing`, `analog-filters-for-measurement` |
| Finding frequency content of measured signals | `spectral-analysis-of-data` | uni-upper | `daq-sampling`, `signals.parseval-and-bandwidth` |

### Sensors

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Measuring strain with strain gauges | `strain-gauges` | uni-upper | `wheatstone-bridges`, `mech-materials.strain-rosettes` |
| Measuring temperature with thermocouples, RTDs and thermistors | `temperature-sensors` | uni-upper | `wheatstone-bridges` |
| Measuring pressure with transducers | `pressure-transducers` | uni-upper | `strain-gauges` |
| Choosing flow measurement devices | `flow-sensors` | uni-upper | `fluids.flow-measurement` |
| Measuring displacement and acceleration | `motion-sensors` | uni-upper | `second-order-instruments` |
| Measuring force and torque | `force-and-torque-sensors` | uni-upper | `strain-gauges` |

### Actuators and mechatronics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing motors and actuators | `actuators` | uni-upper | `controls.electromechanical-models` |
| Interfacing sensors with microcontrollers | `microcontroller-interfacing` | uni-upper | `adc-resolution`, `programming.simulation-loops` |

## engr.mass-energy-balances: 36 topics

Follows `engr.thermo`, `chem.pchem1`, `math.diffeq`, `math.linalg`.

### Process variables

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Converting process units including gauge and absolute pressure | `process-units-and-conversions` | uni-upper | `thermo.systems-and-properties` |
| Converting mass, molar and volumetric flow rates | `flow-rates-and-composition` | uni-upper | `process-units-and-conversions`, `chem.gen1.mole-fractions` |
| Reading process flowsheets and labelling streams | `process-flowsheets` | uni-upper | `flow-rates-and-composition` |

### Nonreactive material balances

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing the general balance equation | `general-balance-equation` | uni-upper | `process-flowsheets` |
| Doing degree-of-freedom analysis | `degrees-of-freedom` | uni-upper | `general-balance-equation` |
| Solving single-unit material balances | `single-unit-balances` | uni-upper | `degrees-of-freedom` |
| Solving multiple-unit material balances | `multiple-unit-balances` | uni-upper | `single-unit-balances` |
| Solving balances with recycle and bypass | `recycle-and-bypass` | uni-upper | `multiple-unit-balances` |
| Solving material balances as linear systems | `balances-as-linear-systems` | uni-upper | `multiple-unit-balances`, `math.linalg.gaussian-elimination` |

### Reactive material balances

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using extent of reaction | `extent-of-reaction` | uni-upper | `single-unit-balances`, `chem.gen1.multistep-yield` |
| Finding conversion, yield and selectivity | `conversion-yield-selectivity` | uni-upper | `extent-of-reaction` |
| Solving reactive systems with atomic balances | `atomic-species-balances` | uni-upper | `extent-of-reaction` |
| Solving reactive systems with recycle and purge | `reactive-recycle-and-purge` | uni-upper | `conversion-yield-selectivity`, `recycle-and-bypass` |
| Solving combustion material balances | `combustion-balances` | uni-upper | `atomic-species-balances`, `thermo.combustion-stoichiometry` |
| Combining material balances with reaction equilibrium | `reaction-equilibrium-balances` | uni-upper | `extent-of-reaction`, `chem.pchem1.gibbs-energy-and-extent-of-reaction` |

### Multiphase systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the Antoine equation | `vapor-pressure-correlations` | uni-upper | `flow-rates-and-composition`, `chem.gen1.vapor-pressure-and-temperature` |
| Solving balances with one condensable species | `single-condensable-systems` | uni-upper | `vapor-pressure-correlations` |
| Using relative and absolute saturation in balances | `saturation-and-humidity-balances` | uni-upper | `single-condensable-systems`, `thermo.humidity-measures` |
| Solving vapor-liquid balances with Raoult's law | `raoults-law-balances` | uni-upper | `single-condensable-systems`, `chem.gen1.raoults-law` |
| Solving absorption balances with Henry's law | `gas-liquid-solubility-balances` | uni-upper | `raoults-law-balances`, `chem.gen1.henrys-law` |
| Solving crystallization and dissolution balances | `solid-liquid-balances` | uni-upper | `single-unit-balances` |

### Energy balances

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing closed or open system energy balances | `energy-balance-forms` | uni-upper | `general-balance-equation`, `thermo.steady-flow-energy-balance` |
| Choosing reference states and finding enthalpy changes | `reference-states-and-enthalpy` | uni-upper | `energy-balance-forms`, `thermo.table-interpolation` |
| Finding sensible heat with heat capacity polynomials | `heat-capacity-polynomials` | uni-upper | `reference-states-and-enthalpy`, `chem.pchem1.kirchhoff-law` |
| Including latent heats in energy balances | `phase-change-enthalpy` | uni-upper | `heat-capacity-polynomials` |
| Solving nonreactive energy balances | `nonreactive-energy-balances` | uni-upper | `phase-change-enthalpy` |
| Using heats of mixing and solution | `mixing-and-solution-enthalpy` | uni-upper | `nonreactive-energy-balances` |
| Solving humidification balances with the psychrometric chart | `psychrometric-balances` | uni-upper | `nonreactive-energy-balances`, `thermo.psychrometric-chart` |
| Solving reactive energy balances by the heat of reaction method | `heat-of-reaction-method` | uni-upper | `nonreactive-energy-balances`, `thermo.enthalpy-of-formation` |
| Solving reactive energy balances by the heat of formation method | `heat-of-formation-method` | uni-upper | `heat-of-reaction-method` |
| Finding adiabatic reaction temperature | `adiabatic-reactors` | uni-upper | `heat-of-formation-method`, `thermo.adiabatic-flame-temperature` |
| Solving simultaneous material and energy balances | `simultaneous-material-energy` | uni-upper | `adiabatic-reactors`, `reactive-recycle-and-purge` |

### Transient balances

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving transient material balances | `transient-material-balances` | uni-upper | `general-balance-equation`, `math.diffeq.linear-first-order` |
| Solving transient energy balances | `transient-energy-balances` | uni-upper | `transient-material-balances`, `nonreactive-energy-balances` |

### Process design basics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving flowsheets by sequential modular simulation | `process-simulation-sequential` | uni-upper | `simultaneous-material-energy` |
| Identifying process hazards | `process-safety-basics` | uni-upper | `process-flowsheets` |

## engr.cheme-thermo: 33 topics

Follows `engr.mass-energy-balances`, `chem.pchem1`.

### Pure-fluid properties

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using cubic equations of state | `cubic-equations-of-state` | uni-upper | `thermo.compressibility-charts`, `chem.pchem1.virial-equation` |
| Finding residual enthalpy and entropy from equations of state | `residual-properties` | uni-upper | `cubic-equations-of-state`, `thermo.departure-functions` |
| Finding fugacity coefficients from equations of state | `fugacity-coefficients-eos` | uni-upper | `residual-properties`, `chem.pchem1.fugacity` |
| Finding fugacity of pure liquids with Poynting correction | `liquid-fugacity` | uni-upper | `fugacity-coefficients-eos` |
| Estimating properties with group contribution | `property-estimation` | uni-upper | `cubic-equations-of-state` |

### Mixture properties

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding partial molar properties from data | `partial-molar-properties-engineering` | uni-upper | `chem.pchem1.partial-molar-quantities`, `mass-energy-balances.mixing-and-solution-enthalpy` |
| Finding fugacity in mixtures | `mixture-fugacity` | uni-upper | `fugacity-coefficients-eos`, `partial-molar-properties-engineering` |
| Using mixing rules for equations of state | `mixing-rules` | uni-upper | `mixture-fugacity` |
| Using the ideal solution model | `ideal-solution-model` | uni-upper | `mixture-fugacity` |
| Defining activity coefficients and excess Gibbs energy | `activity-coefficients` | uni-upper | `ideal-solution-model`, `chem.pchem1.excess-functions` |
| Using Margules and van Laar models | `margules-and-van-laar` | uni-upper | `activity-coefficients` |
| Using Wilson and NRTL models | `local-composition-models` | uni-upper | `margules-and-van-laar` |
| Estimating activity coefficients by group contribution | `unifac-estimation` | uni-upper | `local-composition-models`, `property-estimation` |
| Testing data with the Gibbs-Duhem equation | `gibbs-duhem-consistency` | uni-upper | `activity-coefficients` |

### Vapor-liquid equilibrium

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing equilibrium criteria for vapor-liquid systems | `vle-criteria` | uni-upper | `mixture-fugacity` |
| Using modified Raoult's law | `modified-raoults-law` | uni-upper | `vle-criteria`, `activity-coefficients` |
| Doing bubble and dew point calculations | `bubble-and-dew-calculations` | uni-upper | `modified-raoults-law` |
| Doing isothermal flash calculations | `flash-calculations` | uni-upper | `bubble-and-dew-calculations`, `math.calc1.newtons-method` |
| Using K-value charts and correlations | `k-value-correlations` | uni-upper | `flash-calculations` |
| Choosing gamma-phi or phi-phi formulations | `gamma-phi-and-phi-phi` | uni-upper | `modified-raoults-law`, `mixing-rules` |
| Fitting activity model parameters to VLE data | `fitting-activity-parameters` | uni-upper | `margules-and-van-laar`, `bubble-and-dew-calculations` |
| Predicting azeotropes from activity models | `azeotrope-prediction` | uni-upper | `fitting-activity-parameters`, `chem.pchem1.azeotropes` |
| Analyzing high-pressure VLE with equations of state | `high-pressure-vle` | uni-upper | `gamma-phi-and-phi-phi` |

### Other phase equilibria

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Predicting liquid-liquid equilibrium | `liquid-liquid-equilibrium` | uni-upper | `activity-coefficients`, `chem.pchem1.partially-miscible-liquids` |
| Analyzing vapor-liquid-liquid equilibrium | `vlle` | uni-upper | `liquid-liquid-equilibrium`, `bubble-and-dew-calculations` |
| Predicting solid solubility | `solid-liquid-equilibrium` | uni-upper | `activity-coefficients`, `chem.pchem1.solid-liquid-diagrams` |
| Predicting gas solubility in liquids | `gas-solubility-engineering` | uni-upper | `modified-raoults-law` |
| Applying thermodynamics to osmotic processes | `osmotic-and-colligative` | uni-upper | `activity-coefficients` |

### Chemical reaction equilibrium

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding equilibrium constants at process temperatures | `equilibrium-constants-engineering` | uni-upper | `chem.pchem1.k-from-thermodynamic-tables`, `chem.pchem1.gibbs-helmholtz-and-vant-hoff` |
| Finding equilibrium compositions for nonideal gases | `nonideal-gas-equilibrium` | uni-upper | `equilibrium-constants-engineering`, `fugacity-coefficients-eos` |
| Finding equilibrium in liquid-phase reactions | `liquid-phase-equilibrium-reactions` | uni-upper | `equilibrium-constants-engineering`, `activity-coefficients` |
| Finding equilibrium with multiple reactions | `multireaction-equilibrium` | uni-upper | `nonideal-gas-equilibrium` |
| Finding equilibrium by Gibbs energy minimization | `gibbs-minimization` | uni-upper | `multireaction-equilibrium` |

## engr.mass-transfer: 24 topics

Follows `engr.mass-energy-balances`, `engr.heat-transfer`.

### Molecular diffusion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining molar and mass diffusion fluxes | `diffusion-fluxes` | uni-upper | `mass-energy-balances.flow-rates-and-composition` |
| Using Fick's law for binary mixtures | `ficks-law-binary` | uni-upper | `diffusion-fluxes` |
| Analyzing diffusion through a stagnant film | `diffusion-through-stagnant-film` | uni-upper | `ficks-law-binary` |
| Analyzing equimolar counterdiffusion | `equimolar-counterdiffusion` | uni-upper | `ficks-law-binary` |
| Estimating gas and liquid diffusivities | `diffusivity-estimation` | uni-upper | `ficks-law-binary` |
| Analyzing diffusion with chemical reaction | `diffusion-with-reaction` | uni-upper | `diffusion-through-stagnant-film` |
| Analyzing diffusion in porous solids | `diffusion-in-porous-solids` | uni-upper | `ficks-law-binary` |
| Analyzing transient diffusion | `transient-diffusion` | uni-upper | `ficks-law-binary`, `heat-transfer.one-term-solutions` |

### Convective mass transfer

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining mass transfer coefficients | `mass-transfer-coefficients` | uni-upper | `diffusion-through-stagnant-film`, `heat-transfer.convection-coefficients` |
| Using Sherwood number correlations | `mass-transfer-correlations` | uni-upper | `mass-transfer-coefficients`, `heat-transfer.convection-dimensionless-groups` |
| Using the heat and mass transfer analogy | `heat-mass-analogy` | uni-upper | `mass-transfer-correlations`, `heat-transfer.reynolds-analogy` |
| Comparing film, penetration and surface renewal theories | `film-penetration-theories` | uni-upper | `mass-transfer-coefficients` |

### Interphase mass transfer

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Applying the two-resistance theory | `two-resistance-theory` | uni-upper | `mass-transfer-coefficients`, `mass-energy-balances.gas-liquid-solubility-balances` |
| Finding overall mass transfer coefficients | `overall-coefficients` | uni-upper | `two-resistance-theory` |
| Identifying the controlling resistance | `controlling-resistance` | uni-upper | `overall-coefficients` |

### Continuous-contact equipment

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing operating lines for packed columns | `packed-column-operating-lines` | uni-upper | `overall-coefficients`, `mass-energy-balances.single-unit-balances` |
| Sizing packed columns with HTU and NTU | `htu-ntu-method` | uni-upper | `packed-column-operating-lines` |
| Finding minimum solvent rate | `minimum-liquid-rate` | uni-upper | `packed-column-operating-lines` |
| Finding flooding and pressure drop in packed columns | `packed-column-hydraulics` | uni-upper | `htu-ntu-method`, `fluids.mechanical-energy-equation` |

### Simultaneous heat and mass transfer

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing humidification and dehumidification | `humidification-operations` | uni-upper | `heat-mass-analogy`, `thermo.psychrometric-chart` |
| Sizing cooling towers | `cooling-tower-design` | uni-upper | `humidification-operations`, `htu-ntu-method` |
| Finding drying rates and times | `drying-rates` | uni-upper | `heat-mass-analogy`, `mass-energy-balances.saturation-and-humidity-balances` |
| Analyzing single-effect evaporators | `evaporation-units` | uni-upper | `mass-energy-balances.nonreactive-energy-balances`, `heat-transfer.overall-heat-transfer-coefficient` |
| Analyzing multiple-effect evaporators | `multiple-effect-evaporators` | uni-upper | `evaporation-units` |

## engr.separations: 34 topics

Follows `engr.mass-transfer`, `engr.cheme-thermo`.

### Equilibrium stages

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying separation processes by driving force | `separation-principles` | uni-upper | `mass-transfer.two-resistance-theory` |
| Using the equilibrium stage concept | `equilibrium-stage-concept` | uni-upper | `separation-principles`, `cheme-thermo.flash-calculations` |
| Solving binary flash problems graphically | `binary-flash-graphical` | uni-upper | `equilibrium-stage-concept` |
| Solving multicomponent flash with Rachford-Rice | `multicomponent-flash` | uni-upper | `equilibrium-stage-concept`, `cheme-thermo.k-value-correlations` |

### Binary distillation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing column material balances | `column-material-balances` | uni-upper | `equilibrium-stage-concept` |
| Drawing operating lines and the feed line | `mccabe-thiele-operating-lines` | uni-upper | `column-material-balances` |
| Stepping off stages by McCabe-Thiele | `mccabe-thiele-stepping` | uni-upper | `mccabe-thiele-operating-lines` |
| Finding minimum reflux and minimum stages | `minimum-reflux-and-stages` | uni-upper | `mccabe-thiele-stepping` |
| Choosing feed location and reflux ratio | `optimum-feed-and-reflux` | uni-upper | `minimum-reflux-and-stages` |
| Analyzing side streams and multiple feeds | `side-streams-and-multiple-feeds` | uni-upper | `mccabe-thiele-stepping` |
| Using Murphree and overall efficiencies | `stage-efficiency` | uni-upper | `mccabe-thiele-stepping` |
| Using enthalpy-composition diagrams | `enthalpy-concentration-methods` | uni-upper | `mccabe-thiele-stepping`, `mass-energy-balances.nonreactive-energy-balances` |
| Analyzing batch distillation with the Rayleigh equation | `batch-distillation` | uni-upper | `column-material-balances`, `math.calc2.separable-equations` |

### Multicomponent distillation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing light and heavy key components | `key-components` | uni-upper | `minimum-reflux-and-stages`, `multicomponent-flash` |
| Estimating stages by Fenske, Underwood and Gilliland | `fenske-underwood-gilliland` | uni-upper | `key-components` |
| Describing rigorous stage-by-stage methods | `rigorous-stage-methods` | uni-upper | `fenske-underwood-gilliland` |
| Describing azeotropic and extractive distillation | `azeotropic-and-extractive-distillation` | uni-upper | `key-components`, `cheme-thermo.azeotrope-prediction` |
| Sizing column diameter from flooding | `column-sizing` | uni-upper | `stage-efficiency`, `fluids.drag-coefficients` |

### Absorption and stripping

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing staged absorbers graphically | `absorption-stage-design` | uni-upper | `equilibrium-stage-concept`, `mass-transfer.minimum-liquid-rate` |
| Using the Kremser equation | `kremser-equation` | uni-upper | `absorption-stage-design` |
| Designing strippers | `stripping-design` | uni-upper | `kremser-equation` |

### Extraction and leaching

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading ternary phase diagrams | `ternary-diagrams` | uni-upper | `cheme-thermo.liquid-liquid-equilibrium` |
| Solving single-stage extraction | `single-stage-extraction` | uni-upper | `ternary-diagrams` |
| Solving countercurrent extraction | `countercurrent-extraction` | uni-upper | `single-stage-extraction` |
| Solving extraction with immiscible solvents | `immiscible-extraction` | uni-upper | `countercurrent-extraction`, `kremser-equation` |
| Solving leaching problems | `leaching` | uni-upper | `single-stage-extraction` |

### Other separations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Fitting adsorption isotherms | `adsorption-isotherms` | uni-upper | `chem.pchem1.langmuir-isotherm`, `separation-principles` |
| Analyzing breakthrough in fixed-bed adsorption | `fixed-bed-adsorption` | uni-upper | `adsorption-isotherms`, `mass-transfer.overall-coefficients` |
| Analyzing membrane separations | `membrane-separations` | uni-upper | `separation-principles`, `mass-transfer.ficks-law-binary` |
| Analyzing crystallization yield | `crystallization` | uni-upper | `mass-energy-balances.solid-liquid-balances` |
| Describing particle size distributions | `particle-size-distributions` | uni-upper | `separation-principles` |
| Analyzing settling, filtration and centrifugation | `mechanical-separations` | uni-upper | `particle-size-distributions`, `fluids.drag-coefficients` |
| Finding energy for size reduction | `size-reduction` | uni-upper | `particle-size-distributions` |
| Choosing a separation process | `choosing-a-separation` | uni-upper | `fixed-bed-adsorption`, `membrane-separations`, `countercurrent-extraction`, `fenske-underwood-gilliland` |

## engr.reactors: 37 topics

Follows `engr.mass-transfer`, `engr.cheme-thermo`.

### Rates and stoichiometry

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing rate laws for reactor design | `rate-laws-engineering` | uni-upper | `mass-energy-balances.extent-of-reaction`, `chem.pchem1.rate-laws-as-differential-equations` |
| Building stoichiometric tables for batch and flow systems | `stoichiometric-tables` | uni-upper | `rate-laws-engineering` |
| Including volume change in gas-phase reactions | `gas-phase-volume-change` | uni-upper | `stoichiometric-tables` |

### Ideal reactor design

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing the general mole balance | `general-mole-balance` | uni-upper | `mass-energy-balances.general-balance-equation`, `rate-laws-engineering` |
| Designing batch reactors | `batch-reactor-design` | uni-upper | `general-mole-balance`, `stoichiometric-tables` |
| Designing continuous stirred-tank reactors | `cstr-design` | uni-upper | `general-mole-balance`, `stoichiometric-tables` |
| Designing plug flow reactors | `pfr-design` | uni-upper | `general-mole-balance`, `gas-phase-volume-change` |
| Sizing reactors with Levenspiel plots | `levenspiel-plots` | uni-upper | `cstr-design`, `pfr-design` |
| Sizing reactors in series | `reactors-in-series-chem` | uni-upper | `levenspiel-plots` |
| Including pressure drop in packed-bed reactors | `pressure-drop-in-pbr` | uni-upper | `pfr-design`, `fluids.pipe-flow-problem-types` |
| Designing semibatch reactors | `semibatch-reactors` | uni-upper | `batch-reactor-design` |
| Analyzing recycle reactors | `recycle-reactors` | uni-upper | `pfr-design`, `mass-energy-balances.recycle-and-bypass` |
| Analyzing membrane reactors | `membrane-reactors` | uni-upper | `pfr-design` |

### Kinetic data

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding rate laws by the integral method | `batch-data-integral` | uni-upper | `batch-reactor-design`, `chem.pchem1.integrated-rate-law-derivations` |
| Finding rate laws by the differential method | `batch-data-differential` | uni-upper | `batch-data-integral` |
| Fitting rate parameters by nonlinear regression | `regression-of-rate-data` | uni-upper | `batch-data-differential`, `math.probstat.simple-linear-model` |

### Multiple reactions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Maximizing selectivity for parallel reactions | `parallel-reaction-selectivity` | uni-upper | `cstr-design`, `pfr-design`, `chem.pchem1.parallel-reactions` |
| Maximizing yield for series reactions | `series-reaction-yield` | uni-upper | `parallel-reaction-selectivity`, `chem.pchem1.consecutive-reactions` |
| Designing reactors for complex reaction networks | `complex-reaction-networks` | uni-upper | `series-reaction-yield`, `math.diffeq.numerical-systems` |

### Mechanisms and catalysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving rate laws with the pseudo-steady-state hypothesis | `pssh-in-reactors` | uni-upper | `rate-laws-engineering`, `chem.pchem1.steady-state-kinetics` |
| Deriving Langmuir-Hinshelwood rate laws | `catalytic-mechanisms` | uni-upper | `pssh-in-reactors`, `chem.pchem1.surface-catalysis-kinetics` |
| Finding the rate-limiting step from data | `rate-limiting-step` | uni-upper | `catalytic-mechanisms` |
| Modelling catalyst deactivation | `catalyst-deactivation` | uni-upper | `catalytic-mechanisms` |
| Using Thiele modulus and effectiveness factor | `internal-diffusion-effectiveness` | uni-upper | `catalytic-mechanisms`, `mass-transfer.diffusion-with-reaction` |
| Including external mass transfer in catalytic reactors | `external-mass-transfer-limits` | uni-upper | `internal-diffusion-effectiveness`, `mass-transfer.mass-transfer-correlations` |

### Nonisothermal reactors

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing energy balances for reactors | `reactor-energy-balance` | uni-upper | `cstr-design`, `mass-energy-balances.heat-of-formation-method` |
| Designing adiabatic reactors | `adiabatic-pfr-and-cstr` | uni-upper | `reactor-energy-balance` |
| Finding adiabatic equilibrium conversion | `equilibrium-conversion-temperature` | uni-upper | `adiabatic-pfr-and-cstr`, `cheme-thermo.equilibrium-constants-engineering` |
| Designing interstage cooling | `interstage-cooling` | uni-upper | `equilibrium-conversion-temperature` |
| Designing PFRs with heat exchange | `pfr-with-heat-exchange` | uni-upper | `adiabatic-pfr-and-cstr`, `heat-transfer.overall-heat-transfer-coefficient` |
| Finding multiple steady states in CSTRs | `cstr-multiple-steady-states` | uni-upper | `adiabatic-pfr-and-cstr` |
| Analyzing thermal runaway | `runaway-reactions` | uni-upper | `cstr-multiple-steady-states` |

### Nonideal reactors

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Measuring residence time distributions | `residence-time-distribution` | uni-upper | `cstr-design`, `pfr-design` |
| Finding mean residence time and variance | `rtd-moments` | uni-upper | `residence-time-distribution` |
| Predicting conversion with the segregation model | `segregation-model` | uni-upper | `rtd-moments` |
| Modelling nonideal flow with tanks in series | `tanks-in-series-model` | uni-upper | `rtd-moments` |
| Modelling nonideal flow with dispersion | `dispersion-model` | uni-upper | `tanks-in-series-model` |

## engr.process-control: 27 topics

Follows `engr.controls`, `engr.reactors`.

### Process models

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving dynamic models of tanks and heaters | `process-dynamic-models` | uni-upper | `mass-energy-balances.transient-energy-balances`, `controls.thermal-and-fluid-models` |
| Finding transfer functions of process models | `process-transfer-functions` | uni-upper | `process-dynamic-models`, `controls.linearization-for-control` |
| Analyzing first-order processes | `first-order-processes` | uni-upper | `process-transfer-functions`, `controls.first-order-system-response` |
| Analyzing integrating processes | `integrating-processes` | uni-upper | `first-order-processes` |
| Analyzing interacting and noninteracting tanks | `interacting-tanks` | uni-upper | `first-order-processes` |
| Approximating dead time | `dead-time-and-pade` | uni-upper | `first-order-processes`, `controls.time-delay-systems` |
| Analyzing inverse response | `inverse-response` | uni-upper | `interacting-tanks` |
| Fitting first-order-plus-dead-time models to step tests | `fopdt-identification` | uni-upper | `dead-time-and-pade` |

### Control hardware

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing process sensors and transmitters | `sensors-and-transmitters` | uni-upper | `process-dynamic-models` |
| Sizing control valves and choosing characteristics | `control-valves` | uni-upper | `sensors-and-transmitters`, `fluids.minor-losses` |
| Reading piping and instrumentation diagrams | `piping-and-instrumentation-diagrams` | uni-upper | `sensors-and-transmitters`, `mass-energy-balances.process-flowsheets` |

### Feedback control of processes

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding closed-loop responses of process loops | `closed-loop-process-response` | uni-upper | `fopdt-identification`, `controls.pid-controller-actions` |
| Choosing controller action | `direct-and-reverse-action` | uni-upper | `closed-loop-process-response`, `control-valves` |
| Tuning PID controllers with IMC and other correlations | `pid-tuning-correlations` | uni-upper | `closed-loop-process-response`, `controls.pid-tuning-rules` |
| Designing controllers by direct synthesis | `direct-synthesis` | uni-upper | `pid-tuning-correlations` |
| Tuning process controllers with frequency response | `frequency-response-process-tuning` | uni-upper | `pid-tuning-correlations`, `controls.gain-and-phase-margins` |

### Enhanced control strategies

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing cascade control | `cascade-control` | uni-upper | `pid-tuning-correlations` |
| Designing feedforward control | `feedforward-process-control` | uni-upper | `pid-tuning-correlations`, `controls.feedforward-control` |
| Designing ratio control | `ratio-control` | uni-upper | `feedforward-process-control` |
| Designing override and split-range control | `override-and-split-range` | uni-upper | `cascade-control` |
| Compensating dead time with a Smith predictor | `smith-predictor` | uni-upper | `dead-time-and-pade`, `pid-tuning-correlations` |

### Plantwide and multivariable control

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing loop interaction with the relative gain array | `multiloop-interaction` | uni-upper | `pid-tuning-correlations` |
| Designing decoupling control | `decoupling-control` | uni-upper | `multiloop-interaction` |
| Explaining model predictive control | `model-predictive-control-intro` | uni-upper | `multiloop-interaction` |
| Choosing controlled and manipulated variables plantwide | `plantwide-control` | uni-upper | `multiloop-interaction`, `piping-and-instrumentation-diagrams` |
| Describing alarms, interlocks and safety systems | `safety-instrumented-systems` | uni-upper | `piping-and-instrumentation-diagrams` |
| Writing logic for batch sequences | `batch-and-discrete-control` | uni-upper | `safety-instrumented-systems` |

## engr.electronics: 58 topics

Follows `engr.controls`, `engr.digital-logic`, `physics.modern`.

### Semiconductor devices

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding drift and diffusion currents in semiconductors | `carrier-drift-and-diffusion` | uni-upper | `physics.modern.doped-semiconductors`, `physics.modern.band-theory` |
| Finding depletion width and built-in potential | `pn-junction-electrostatics` | uni-upper | `carrier-drift-and-diffusion`, `physics.modern.pn-junctions` |
| Using the diode current equation | `diode-equation` | uni-upper | `pn-junction-electrostatics` |
| Describing junction capacitance and breakdown | `junction-capacitance-and-breakdown` | uni-upper | `diode-equation` |

### Diode circuits

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing circuits with diode models | `diode-models` | uni-upper | `diode-equation`, `circuits.thevenin-equivalent` |
| Solving diode circuits iteratively | `iterative-diode-analysis` | uni-upper | `diode-models`, `math.calc1.newtons-method` |
| Analyzing half-wave and full-wave rectifiers | `rectifier-circuits` | uni-upper | `diode-models` |
| Finding ripple in filtered rectifiers | `filtered-rectifiers` | uni-upper | `rectifier-circuits`, `circuits.first-order-natural-response` |
| Designing Zener regulators | `zener-regulators` | uni-upper | `diode-models`, `junction-capacitance-and-breakdown` |
| Analyzing clipping and clamping circuits | `clippers-and-clampers` | uni-upper | `diode-models` |
| Using the diode small-signal model | `diode-small-signal` | uni-upper | `diode-equation` |

### MOSFETs

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing MOSFET structure and operation | `mosfet-structure` | uni-upper | `pn-junction-electrostatics` |
| Using MOSFET current-voltage equations | `mosfet-iv-characteristics` | uni-upper | `mosfet-structure` |
| Finding MOSFET operating points | `mosfet-dc-analysis` | uni-upper | `mosfet-iv-characteristics`, `circuits.nodal-analysis` |
| Designing MOSFET bias circuits | `mosfet-biasing` | uni-upper | `mosfet-dc-analysis` |
| Analyzing MOSFET switches and CMOS inverters | `mosfet-switch-and-inverter` | uni-upper | `mosfet-dc-analysis`, `digital-logic.cmos-gates` |

### BJTs

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing BJT structure and operation | `bjt-structure` | uni-upper | `pn-junction-electrostatics`, `diode-equation` |
| Using BJT current relations | `bjt-iv-characteristics` | uni-upper | `bjt-structure` |
| Finding BJT operating points | `bjt-dc-analysis` | uni-upper | `bjt-iv-characteristics`, `circuits.nodal-analysis` |
| Designing BJT bias circuits | `bjt-biasing` | uni-upper | `bjt-dc-analysis` |
| Analyzing BJT switches | `bjt-switches` | uni-upper | `bjt-dc-analysis` |

### Single-stage amplifiers

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using voltage, current, transconductance and transresistance amplifier models | `amplifier-models` | uni-upper | `circuits.dependent-sources` |
| Using the MOSFET small-signal model | `small-signal-mosfet` | uni-upper | `mosfet-biasing`, `amplifier-models` |
| Using the BJT small-signal model | `small-signal-bjt` | uni-upper | `bjt-biasing`, `amplifier-models` |
| Analyzing common-source and common-emitter amplifiers | `common-source-and-emitter` | uni-upper | `small-signal-mosfet`, `small-signal-bjt` |
| Analyzing amplifiers with source or emitter degeneration | `degenerated-amplifiers` | uni-upper | `common-source-and-emitter` |
| Analyzing common-gate and common-base amplifiers | `common-gate-and-base` | uni-upper | `common-source-and-emitter` |
| Analyzing source and emitter followers | `followers` | uni-upper | `common-source-and-emitter` |
| Choosing amplifier configurations | `choosing-amplifier-configurations` | uni-upper | `degenerated-amplifiers`, `common-gate-and-base`, `followers` |

### Multistage and integrated amplifiers

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing cascaded amplifier stages | `multistage-amplifiers` | uni-upper | `choosing-amplifier-configurations` |
| Analyzing current mirrors | `current-mirrors` | uni-upper | `mosfet-biasing`, `bjt-biasing` |
| Analyzing amplifiers with active loads | `active-loads` | uni-upper | `current-mirrors`, `common-source-and-emitter` |
| Analyzing cascode amplifiers | `cascode-amplifiers` | uni-upper | `active-loads`, `common-gate-and-base` |
| Analyzing differential pairs | `differential-pairs` | uni-upper | `current-mirrors`, `common-source-and-emitter` |
| Finding common-mode rejection | `common-mode-rejection` | uni-upper | `differential-pairs` |
| Analyzing a two-stage op-amp | `two-stage-op-amp` | uni-upper | `differential-pairs`, `active-loads` |

### Frequency response

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding low-frequency response from coupling capacitors | `amplifier-low-frequency-response` | uni-upper | `common-source-and-emitter`, `circuits.bode-magnitude` |
| Modelling device capacitances | `device-capacitances` | uni-upper | `small-signal-mosfet`, `small-signal-bjt` |
| Using the Miller effect | `miller-effect` | uni-upper | `device-capacitances` |
| Finding high-frequency response and bandwidth | `amplifier-high-frequency-response` | uni-upper | `miller-effect` |
| Estimating bandwidth with open-circuit time constants | `open-circuit-time-constants` | uni-upper | `amplifier-high-frequency-response` |

### Feedback

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Identifying feedback topologies | `feedback-topologies` | uni-upper | `multistage-amplifiers`, `controls.block-diagram-reduction` |
| Finding effects of feedback on gain, bandwidth and impedance | `feedback-effects` | uni-upper | `feedback-topologies` |
| Checking amplifier stability and frequency compensation | `feedback-stability` | uni-upper | `feedback-effects`, `controls.gain-and-phase-margins` |

### Nonideal op-amps

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing offset voltage and bias currents | `op-amp-dc-imperfections` | uni-upper | `circuits.inverting-and-noninverting` |
| Using finite gain and gain-bandwidth product | `op-amp-gain-bandwidth` | uni-upper | `op-amp-dc-imperfections`, `amplifier-high-frequency-response` |
| Checking slew-rate limits | `slew-rate` | uni-upper | `op-amp-gain-bandwidth` |

### Output stages and power electronics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing class A, B and AB output stages | `class-a-b-ab-stages` | uni-upper | `followers` |
| Sizing heat sinks for power devices | `power-dissipation-and-heat-sinks` | uni-upper | `class-a-b-ab-stages`, `physics.waves-thermo-optics.conduction-through-layers` |
| Analyzing linear voltage regulators | `linear-regulators` | uni-upper | `zener-regulators`, `feedback-effects` |
| Analyzing buck converters | `buck-converters` | uni-upper | `bjt-switches`, `mosfet-switch-and-inverter`, `circuits.inductor-iv-relation` |
| Analyzing boost and buck-boost converters | `boost-and-buck-boost` | uni-upper | `buck-converters` |
| Describing inverters and thyristor circuits | `inverters-and-thyristors` | uni-upper | `buck-converters` |

### Waveform and digital circuits

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing comparators and Schmitt triggers | `comparators-and-schmitt-triggers` | uni-upper | `op-amp-dc-imperfections` |
| Analyzing oscillators with the Barkhausen criterion | `oscillators` | uni-upper | `feedback-effects` |
| Designing timer circuits | `timer-circuits` | uni-upper | `comparators-and-schmitt-triggers`, `circuits.switched-first-order` |
| Finding CMOS gate delay and power | `cmos-logic-timing` | uni-upper | `mosfet-switch-and-inverter` |
| Analyzing DAC and ADC circuits | `data-converters` | uni-upper | `comparators-and-schmitt-triggers`, `signals.quantization` |

## engr.em-fields: 35 topics

Follows `physics.em-theory`, `engr.circuits`.

### Transmission lines

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Modelling transmission lines with distributed parameters | `distributed-line-model` | uni-upper | `physics.em-theory.coaxial-transmission-lines`, `circuits.phasors-and-impedance` |
| Finding line parameters for coaxial and two-wire lines | `line-parameters` | uni-upper | `distributed-line-model`, `physics.em.inductance-of-coax-and-toroid` |
| Solving the telegrapher's equations | `telegrapher-equations` | uni-upper | `distributed-line-model`, `math.pde.deriving-wave-equation` |
| Finding characteristic impedance and propagation constant | `characteristic-impedance` | uni-upper | `telegrapher-equations` |
| Finding reflection coefficient and standing wave ratio | `reflection-coefficient-and-swr` | uni-upper | `characteristic-impedance` |
| Finding input impedance of terminated lines | `input-impedance` | uni-upper | `reflection-coefficient-and-swr` |
| Analyzing shorted, open and quarter-wave lines | `special-terminations` | uni-upper | `input-impedance` |
| Finding power flow on lossless and lossy lines | `power-flow-on-lines` | uni-upper | `input-impedance` |
| Using the Smith chart | `smith-chart` | uni-upper | `input-impedance` |
| Matching with quarter-wave transformers | `quarter-wave-matching` | uni-upper | `special-terminations` |
| Matching with single stubs | `stub-matching` | uni-upper | `smith-chart` |
| Matching with lumped elements | `lumped-element-matching` | uni-upper | `smith-chart` |
| Analyzing transients with bounce diagrams | `line-transients` | uni-upper | `reflection-coefficient-and-swr` |
| Using scattering parameters | `scattering-parameters` | uni-upper | `power-flow-on-lines`, `circuits.two-port-parameters` |
| Designing microstrip lines | `microstrip-lines` | uni-upper | `characteristic-impedance` |

### Field applications

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding capacitance of engineering geometries | `capacitance-by-field-methods` | uni-upper | `physics.em-theory.poisson-and-laplace-equations` |
| Solving Laplace's equation numerically | `numerical-field-solutions` | uni-upper | `capacitance-by-field-methods`, `physics.em-theory.relaxation-method` |
| Finding inductance of engineering conductors | `inductance-calculations` | uni-upper | `physics.em-theory.vector-potential`, `line-parameters` |
| Analyzing magnetic circuits with air gaps | `magnetic-circuits-engineering` | uni-upper | `physics.em-theory.magnetic-circuits` |
| Finding AC resistance from skin depth | `skin-effect-resistance` | uni-upper | `physics.em-theory.waves-in-conductors` |
| Estimating shielding effectiveness | `shielding` | uni-upper | `skin-effect-resistance` |
| Describing crosstalk and electromagnetic compatibility | `emc-basics` | uni-upper | `line-parameters`, `shielding` |

### Waves and guides

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding plane-wave parameters in lossy media | `plane-waves-engineering` | uni-upper | `physics.em-theory.waves-in-linear-media`, `physics.em-theory.waves-in-conductors` |
| Finding reflection at dielectric boundaries for design | `oblique-incidence-engineering` | uni-upper | `plane-waves-engineering`, `physics.em-theory.fresnel-equations` |
| Designing antireflection layers with impedance transformation | `multilayer-reflection` | uni-upper | `oblique-incidence-engineering`, `quarter-wave-matching` |
| Choosing waveguide dimensions for single-mode operation | `waveguide-mode-design` | uni-upper | `physics.em-theory.waveguide-cutoff-and-group-velocity` |
| Finding waveguide attenuation | `waveguide-attenuation` | uni-upper | `waveguide-mode-design`, `skin-effect-resistance` |
| Describing optical fiber modes and dispersion | `optical-fibers` | uni-upper | `waveguide-mode-design`, `physics.waves-thermo-optics.fiber-acceptance-angle` |

### Antennas

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using directivity, gain and efficiency | `antenna-parameters` | uni-upper | `physics.em-theory.radiated-power-and-pattern` |
| Analyzing short and half-wave dipoles | `dipole-antennas` | uni-upper | `antenna-parameters`, `physics.em-theory.radiation-resistance` |
| Matching antennas to lines | `antenna-impedance-matching` | uni-upper | `dipole-antennas`, `stub-matching` |
| Analyzing uniform linear arrays | `antenna-arrays` | uni-upper | `dipole-antennas`, `physics.waves-thermo-optics.multi-slit-intensity` |
| Using effective aperture | `effective-aperture` | uni-upper | `antenna-parameters` |
| Finding received power with the Friis equation | `friis-link-budget` | uni-upper | `effective-aperture` |
| Describing aperture and reflector antennas | `aperture-antennas` | uni-upper | `effective-aperture` |

## engr.power: 43 topics

Follows `engr.em-fields`, `engr.electronics`, `math.numerical`.

### Power fundamentals

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding complex power in single-phase systems | `single-phase-power-review` | uni-upper | `circuits.complex-power` |
| Analyzing balanced three-phase systems by per-phase equivalents | `balanced-three-phase-analysis` | uni-upper | `circuits.three-phase-power` |
| Measuring three-phase power with wattmeters | `three-phase-power-measurement` | uni-upper | `balanced-three-phase-analysis` |
| Using the per-unit system | `per-unit-system` | uni-upper | `balanced-three-phase-analysis` |

### Transformers

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the practical transformer equivalent circuit | `practical-transformer-model` | uni-upper | `circuits.ideal-transformers`, `em-fields.magnetic-circuits-engineering` |
| Finding transformer parameters from open- and short-circuit tests | `transformer-tests` | uni-upper | `practical-transformer-model` |
| Finding transformer regulation and efficiency | `voltage-regulation-and-efficiency` | uni-upper | `transformer-tests` |
| Analyzing three-phase transformer connections | `three-phase-transformers` | uni-upper | `practical-transformer-model`, `per-unit-system` |
| Analyzing autotransformers and tap changers | `autotransformers-and-taps` | uni-upper | `three-phase-transformers` |

### Electromechanical energy conversion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding forces and torques from coenergy | `electromechanical-energy-conversion` | uni-upper | `em-fields.magnetic-circuits-engineering`, `controls.electromechanical-models` |
| Explaining rotating magnetic fields | `rotating-magnetic-fields` | uni-upper | `electromechanical-energy-conversion`, `balanced-three-phase-analysis` |

### Synchronous machines

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the synchronous generator equivalent circuit | `synchronous-generator-model` | uni-upper | `rotating-magnetic-fields` |
| Using the power-angle relation | `synchronous-power-angle` | uni-upper | `synchronous-generator-model` |
| Analyzing synchronous motors and power factor control | `synchronous-motors` | uni-upper | `synchronous-power-angle` |
| Operating generators in parallel | `parallel-generators` | uni-upper | `synchronous-power-angle` |

### Induction and DC machines

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the induction motor equivalent circuit | `induction-motor-model` | uni-upper | `rotating-magnetic-fields` |
| Finding induction motor torque-speed characteristics | `induction-torque-speed` | uni-upper | `induction-motor-model` |
| Finding induction motor parameters from tests | `induction-motor-tests` | uni-upper | `induction-motor-model` |
| Analyzing starting and speed control | `induction-starting-and-speed-control` | uni-upper | `induction-torque-speed` |
| Analyzing DC motors and generators | `dc-machines` | uni-upper | `electromechanical-energy-conversion` |
| Describing single-phase motors | `single-phase-motors` | uni-upper | `induction-motor-model` |
| Analyzing variable-frequency and DC drives | `motor-drives` | uni-upper | `induction-starting-and-speed-control`, `electronics.inverters-and-thyristors` |

### Transmission lines and networks

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding resistance, inductance and capacitance of overhead lines | `line-parameters-power` | uni-upper | `em-fields.inductance-calculations`, `per-unit-system` |
| Modelling short and medium lines | `short-and-medium-lines` | uni-upper | `line-parameters-power` |
| Modelling long lines | `long-line-model` | uni-upper | `short-and-medium-lines`, `em-fields.telegrapher-equations` |
| Finding power transfer limits of lines | `line-power-flow-limits` | uni-upper | `long-line-model`, `synchronous-power-angle` |
| Compensating lines with reactive power | `reactive-compensation` | uni-upper | `line-power-flow-limits` |
| Building the bus admittance matrix | `bus-admittance-matrix` | uni-upper | `short-and-medium-lines`, `math.linalg.matrix-times-vector` |

### Power flow

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing the power flow equations | `power-flow-equations` | uni-upper | `bus-admittance-matrix` |
| Solving power flow by Gauss-Seidel | `gauss-seidel-power-flow` | uni-upper | `power-flow-equations`, `math.numerical.gauss-seidel` |
| Solving power flow by Newton-Raphson | `newton-raphson-power-flow` | uni-upper | `power-flow-equations`, `math.numerical.systems-nonlinear-newton` |
| Controlling voltage with taps and reactive power | `voltage-control` | uni-upper | `newton-raphson-power-flow`, `autotransformers-and-taps` |
| Solving economic dispatch | `economic-dispatch` | uni-upper | `power-flow-equations`, `math.calc3.lagrange-one-constraint` |

### Faults and protection

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding symmetrical fault currents | `symmetrical-faults` | uni-upper | `bus-admittance-matrix`, `synchronous-generator-model` |
| Using symmetrical components | `symmetrical-components` | uni-upper | `balanced-three-phase-analysis`, `math.linalg.matrix-times-vector` |
| Building sequence networks | `sequence-networks` | uni-upper | `symmetrical-components`, `three-phase-transformers` |
| Finding unsymmetrical fault currents | `unsymmetrical-faults` | uni-upper | `sequence-networks`, `symmetrical-faults` |
| Describing relays, breakers and protection coordination | `protective-relays` | uni-upper | `unsymmetrical-faults` |

### Stability and modern grids

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the swing equation | `swing-equation` | uni-upper | `synchronous-power-angle`, `dynamics.fixed-axis-kinetics` |
| Applying the equal-area criterion | `equal-area-criterion` | uni-upper | `swing-equation` |
| Describing wind and solar integration | `renewable-integration` | uni-upper | `line-power-flow-limits`, `electronics.inverters-and-thyristors` |
| Analyzing harmonics and power quality | `power-quality-and-harmonics` | uni-upper | `signals.continuous-fourier-series`, `single-phase-power-review` |
| Describing grounding and electrical safety | `grounding-and-safety` | uni-upper | `protective-relays` |

## engr.communications: 40 topics

Follows `engr.em-fields`, `engr.signals`, `math.probstat`, `math.discrete`.

### Signals and noise

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Representing bandpass signals with complex envelopes | `bandpass-signals` | uni-upper | `signals.modulation-property`, `signals.parseval-and-bandwidth` |
| Describing random processes | `random-processes` | uni-upper | `math.probstat.joint-pdf`, `signals.ct-fourier-transform` |
| Finding power spectral density | `power-spectral-density` | uni-upper | `random-processes`, `signals.parseval-and-bandwidth` |
| Finding noise output of LTI systems | `noise-through-lti-systems` | uni-upper | `power-spectral-density` |
| Using thermal noise and noise figure | `thermal-noise-and-noise-figure` | uni-upper | `noise-through-lti-systems` |

### Amplitude modulation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing double-sideband suppressed-carrier modulation | `dsb-sc-modulation` | uni-upper | `bandpass-signals` |
| Analyzing conventional AM and envelope detection | `conventional-am` | uni-upper | `dsb-sc-modulation` |
| Analyzing single-sideband and vestigial-sideband modulation | `ssb-and-vsb` | uni-upper | `dsb-sc-modulation` |
| Analyzing superheterodyne receivers | `superheterodyne-receivers` | uni-upper | `conventional-am` |
| Using frequency-division multiplexing | `frequency-division-multiplexing` | uni-upper | `dsb-sc-modulation` |

### Angle modulation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing frequency and phase modulation | `fm-and-pm` | uni-upper | `bandpass-signals` |
| Finding FM bandwidth with Carson's rule | `fm-bandwidth` | uni-upper | `fm-and-pm` |
| Describing FM generation and detection | `fm-generation-and-detection` | uni-upper | `fm-bandwidth` |
| Analyzing phase-locked loops | `phase-locked-loops` | uni-upper | `fm-generation-and-detection`, `signals.system-functions-laplace` |

### Noise in analog systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding signal-to-noise ratio in AM systems | `snr-in-am` | uni-upper | `conventional-am`, `noise-through-lti-systems` |
| Finding signal-to-noise ratio in FM systems | `snr-in-fm` | uni-upper | `fm-bandwidth`, `noise-through-lti-systems` |

### Digitizing signals

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing pulse-code modulation | `pulse-code-modulation` | uni-upper | `signals.sampling-theorem`, `signals.quantization` |
| Using nonuniform quantization and companding | `companding` | uni-upper | `pulse-code-modulation` |
| Analyzing delta modulation | `delta-modulation` | uni-upper | `pulse-code-modulation` |
| Using time-division multiplexing | `time-division-multiplexing` | uni-upper | `pulse-code-modulation` |

### Baseband transmission

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing line codes and their spectra | `line-codes` | uni-upper | `pulse-code-modulation`, `power-spectral-density` |
| Explaining intersymbol interference and the Nyquist criterion | `intersymbol-interference` | uni-upper | `line-codes` |
| Designing raised-cosine pulse shaping | `pulse-shaping` | uni-upper | `intersymbol-interference` |
| Reading eye diagrams | `eye-diagrams` | uni-upper | `pulse-shaping` |
| Designing matched filters | `matched-filters` | uni-upper | `noise-through-lti-systems`, `line-codes` |
| Finding bit error probability for binary signalling | `binary-error-probability` | uni-upper | `matched-filters`, `math.probstat.normal-tables` |

### Digital modulation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Representing signals in signal space | `signal-space` | uni-upper | `matched-filters`, `math.linalg.gram-schmidt` |
| Analyzing ASK, FSK and PSK | `ask-fsk-psk` | uni-upper | `signal-space`, `binary-error-probability` |
| Analyzing M-ary PSK and QAM | `qam-and-mpsk` | uni-upper | `ask-fsk-psk` |
| Comparing power and bandwidth efficiency | `bandwidth-efficiency` | uni-upper | `qam-and-mpsk` |
| Analyzing noncoherent detection | `noncoherent-detection` | uni-upper | `ask-fsk-psk` |
| Explaining OFDM | `ofdm-basics` | uni-upper | `qam-and-mpsk`, `signals.dtft-properties` |

### Information and coding

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding entropy of information sources | `entropy-and-information` | uni-upper | `math.probstat.expectation-discrete` |
| Designing Huffman and other source codes | `source-coding` | uni-upper | `entropy-and-information`, `math.discrete.huffman-codes` |
| Using channel capacity and the Shannon limit | `channel-capacity` | uni-upper | `entropy-and-information`, `binary-error-probability` |
| Encoding and decoding linear block codes | `block-codes` | uni-upper | `channel-capacity`, `math.linalg.matrix-times-vector` |
| Using cyclic codes and CRC | `cyclic-codes-and-crc` | uni-upper | `block-codes` |
| Decoding convolutional codes with Viterbi | `convolutional-codes` | uni-upper | `block-codes` |
| Comparing FDMA, TDMA and CDMA | `multiple-access` | uni-upper | `time-division-multiplexing`, `frequency-division-multiplexing` |
| Computing communication link budgets | `link-budgets` | uni-upper | `thermal-noise-and-noise-figure`, `em-fields.friis-link-budget` |

## engr.dsp: 35 topics

Follows `engr.signals`, `engr.digital-logic`, `math.numerical`.

### Discrete Fourier transform

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Computing the discrete Fourier transform | `dft-definition` | uni-upper | `signals.dtft` |
| Using DFT properties | `dft-properties` | uni-upper | `dft-definition` |
| Computing circular convolution | `circular-convolution` | uni-upper | `dft-properties`, `signals.discrete-convolution` |
| Computing linear convolution with the DFT | `linear-convolution-with-dft` | uni-upper | `circular-convolution` |
| Filtering long signals by overlap-add and overlap-save | `overlap-add-save` | uni-upper | `linear-convolution-with-dft` |
| Computing the radix-2 FFT | `radix-2-fft` | uni-upper | `dft-properties`, `math.numerical.fft-intro` |
| Comparing FFT and direct DFT cost | `fft-complexity` | uni-upper | `radix-2-fft` |

### Spectral analysis

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining spectral leakage and windows | `windowing-and-leakage` | uni-upper | `dft-properties`, `signals.ct-fourier-properties` |
| Choosing record length for frequency resolution | `frequency-resolution` | uni-upper | `windowing-and-leakage` |
| Interpolating spectra with zero padding | `zero-padding` | uni-upper | `frequency-resolution` |
| Analyzing nonstationary signals with spectrograms | `spectrograms` | uni-upper | `frequency-resolution` |
| Estimating power spectra by periodogram averaging | `power-spectrum-estimation` | uni-upper | `windowing-and-leakage` |

### Filter structures

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing linear-phase FIR filters | `linear-phase-filters` | uni-upper | `signals.system-functions-z`, `signals.discrete-frequency-response` |
| Finding phase and group delay | `group-delay` | uni-upper | `linear-phase-filters` |
| Implementing direct-form filter structures | `direct-form-structures` | uni-upper | `signals.system-functions-z` |
| Implementing cascade and parallel structures | `cascade-parallel-structures` | uni-upper | `direct-form-structures` |
| Analyzing allpass and minimum-phase systems | `allpass-and-minimum-phase` | uni-upper | `group-delay`, `signals.pole-zero-frequency-response` |

### FIR filter design

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing digital filter specifications | `filter-specifications` | uni-upper | `linear-phase-filters` |
| Designing FIR filters by windowing | `window-method-fir` | uni-upper | `filter-specifications`, `windowing-and-leakage` |
| Designing FIR filters with Kaiser windows | `kaiser-window-design` | uni-upper | `window-method-fir` |
| Designing FIR filters by frequency sampling | `frequency-sampling-fir` | uni-upper | `window-method-fir`, `dft-definition` |
| Describing optimal equiripple FIR design | `optimal-equiripple-fir` | uni-upper | `window-method-fir` |

### IIR filter design

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing Butterworth and Chebyshev analog prototypes | `analog-prototypes` | uni-upper | `filter-specifications`, `circuits.passive-filters` |
| Designing IIR filters by impulse invariance | `impulse-invariance` | uni-upper | `analog-prototypes`, `signals.system-functions-laplace` |
| Designing IIR filters by the bilinear transform | `bilinear-transform` | uni-upper | `analog-prototypes` |
| Transforming lowpass designs to other bands | `frequency-transformations` | uni-upper | `bilinear-transform` |
| Choosing between FIR and IIR filters | `fir-vs-iir` | uni-upper | `bilinear-transform`, `kaiser-window-design` |

### Multirate processing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing downsampling in frequency | `downsampling` | uni-upper | `signals.aliasing`, `signals.dtft-properties` |
| Analyzing upsampling and interpolation | `upsampling` | uni-upper | `downsampling` |
| Converting sample rates by rational factors | `rational-rate-conversion` | uni-upper | `upsampling`, `window-method-fir` |
| Implementing polyphase filters | `polyphase-structures` | uni-upper | `rational-rate-conversion` |

### Implementation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing coefficient quantization and roundoff noise | `finite-word-length-effects` | uni-upper | `cascade-parallel-structures`, `signals.quantization` |
| Implementing filters in fixed point | `fixed-point-filters` | uni-upper | `finite-word-length-effects`, `digital-logic.fixed-point-numbers` |
| Explaining oversampling and noise shaping | `oversampling-converters` | uni-upper | `downsampling`, `finite-word-length-effects` |
| Designing LMS adaptive filters | `adaptive-filters` | uni-upper | `direct-form-structures`, `math.linalg.least-squares-normal` |

## engr.algorithms: 44 topics

Follows `engr.data-structures`, `math.discrete`, `math.probstat`, `math.linalg`.

### Analysis tools

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Proving algorithms correct with invariants and induction | `proving-algorithm-correctness` | uni-upper | `data-structures.asymptotic-analysis-of-code`, `math.discrete.loop-invariants` |
| Solving recurrences with recursion trees | `recursion-tree-method` | uni-upper | `data-structures.recurrence-runtime` |
| Proving recurrence bounds by substitution | `substitution-method` | uni-upper | `recursion-tree-method`, `math.discrete.induction-strong` |
| Analyzing expected running time | `probabilistic-analysis` | uni-upper | `data-structures.best-worst-average-case`, `math.probstat.expectation-discrete` |

### Divide and conquer

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing divide-and-conquer algorithms | `divide-and-conquer-design` | uni-upper | `recursion-tree-method` |
| Counting inversions by divide and conquer | `counting-inversions` | uni-upper | `divide-and-conquer-design` |
| Finding the closest pair of points | `closest-pair` | uni-upper | `divide-and-conquer-design` |
| Multiplying integers and matrices faster | `fast-multiplication` | uni-upper | `divide-and-conquer-design` |
| Selecting the k-th element in linear time | `selection-in-linear-time` | uni-upper | `divide-and-conquer-design`, `substitution-method` |
| Analyzing randomized quicksort | `randomized-quicksort-analysis` | uni-upper | `probabilistic-analysis`, `data-structures.quicksort` |

### Greedy algorithms

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Proving greedy algorithms with exchange arguments | `greedy-exchange-arguments` | uni-upper | `proving-algorithm-correctness`, `math.discrete.greedy-algorithms` |
| Solving interval scheduling and partitioning | `interval-scheduling` | uni-upper | `greedy-exchange-arguments` |
| Scheduling to minimize lateness | `scheduling-to-minimize-lateness` | uni-upper | `interval-scheduling` |
| Proving Huffman coding optimal | `huffman-optimality` | uni-upper | `greedy-exchange-arguments`, `math.discrete.huffman-codes` |
| Proving minimum spanning tree algorithms with the cut property | `mst-correctness` | uni-upper | `greedy-exchange-arguments`, `data-structures.mst-code` |

### Dynamic programming

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Identifying optimal substructure and overlapping subproblems | `dp-principles` | uni-upper | `proving-algorithm-correctness`, `programming.memoization` |
| Solving weighted interval scheduling | `weighted-interval-scheduling` | uni-upper | `dp-principles`, `interval-scheduling` |
| Solving the knapsack problem | `knapsack` | uni-upper | `dp-principles` |
| Solving edit distance and sequence alignment | `sequence-alignment` | uni-upper | `dp-principles` |
| Finding longest common subsequences | `longest-common-subsequence` | uni-upper | `dp-principles` |
| Solving interval dynamic programs | `matrix-chain-and-intervals` | uni-upper | `longest-common-subsequence` |
| Solving dynamic programs on trees | `dp-on-trees` | uni-upper | `dp-principles`, `data-structures.tree-traversal-code` |
| Reducing space in dynamic programs | `dp-space-reduction` | uni-upper | `sequence-alignment` |

### Graph algorithms

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying edges and finding articulation points | `dfs-applications` | uni-upper | `data-structures.dfs-code` |
| Finding strongly connected components | `strongly-connected-components` | uni-upper | `dfs-applications` |
| Finding shortest paths with Bellman-Ford | `shortest-paths-negative-edges` | uni-upper | `data-structures.dijkstra-code`, `dp-principles` |
| Finding all-pairs shortest paths with Floyd-Warshall | `all-pairs-shortest-paths` | uni-upper | `shortest-paths-negative-edges` |
| Proving Dijkstra's algorithm correct | `dijkstra-correctness` | uni-upper | `data-structures.dijkstra-code`, `greedy-exchange-arguments` |
| Finding shortest paths in DAGs | `dag-shortest-paths` | uni-upper | `data-structures.topological-sort-code`, `dp-principles` |

### Network flow

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding maximum flow with Ford-Fulkerson | `max-flow-ford-fulkerson` | uni-upper | `math.discrete.network-flow-intro`, `data-structures.bfs-code` |
| Using the max-flow min-cut theorem | `max-flow-min-cut` | uni-upper | `max-flow-ford-fulkerson` |
| Analyzing Edmonds-Karp | `edmonds-karp` | uni-upper | `max-flow-ford-fulkerson` |
| Solving bipartite matching with flow | `bipartite-matching-flow` | uni-upper | `max-flow-min-cut`, `math.discrete.matchings-hall` |
| Reducing problems to network flow | `flow-reductions` | uni-upper | `bipartite-matching-flow` |

### Strings and hashing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Matching strings with KMP and Rabin-Karp | `string-matching` | uni-upper | `data-structures.hash-functions`, `proving-algorithm-correctness` |
| Analyzing universal hashing | `universal-hashing` | uni-upper | `data-structures.hash-maps-and-sets`, `probabilistic-analysis` |

### Intractability

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reducing problems in polynomial time | `polynomial-reductions` | uni-upper | `flow-reductions` |
| Defining P and NP | `p-and-np` | uni-upper | `polynomial-reductions` |
| Proving NP-completeness | `np-completeness-proofs` | uni-upper | `p-and-np`, `math.discrete.satisfiability-intro` |
| Recognizing classic NP-complete problems | `classic-np-complete-problems` | uni-upper | `np-completeness-proofs` |
| Designing approximation algorithms | `approximation-algorithms` | uni-upper | `classic-np-complete-problems`, `greedy-exchange-arguments` |
| Solving hard problems by backtracking and branch-and-bound | `backtracking-and-branch-bound` | uni-upper | `classic-np-complete-problems` |
| Designing randomized algorithms | `randomized-algorithms` | uni-upper | `probabilistic-analysis` |
| Formulating problems as linear programs | `linear-programming-intro` | uni-upper | `flow-reductions`, `math.linalg.applications-of-systems` |

## engr.architecture: 39 topics

Follows `engr.digital-logic`, `engr.programming`.

### Performance and instruction sets

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing performance with CPI and execution time | `performance-metrics` | uni-upper | `programming.timing-programs`, `digital-logic.alu-design` |
| Using Amdahl's law | `amdahls-law` | uni-upper | `performance-metrics` |
| Describing instruction set architectures | `instruction-set-concepts` | uni-upper | `performance-metrics` |
| Writing arithmetic in assembly language | `assembly-arithmetic` | uni-upper | `instruction-set-concepts`, `digital-logic.twos-complement` |
| Loading and storing memory in assembly | `assembly-memory-access` | uni-upper | `assembly-arithmetic`, `programming.lists-basics` |
| Writing branches and loops in assembly | `assembly-control-flow` | uni-upper | `assembly-memory-access`, `programming.while-loops` |
| Writing procedure calls with the stack | `procedure-calls-and-stack` | uni-upper | `assembly-control-flow`, `programming.call-stack` |
| Encoding instructions in machine code | `instruction-encoding` | uni-upper | `assembly-arithmetic`, `digital-logic.binary-and-hex-codes` |
| Using addressing modes | `addressing-modes` | uni-upper | `assembly-memory-access` |
| Tracing compilation, assembly, linking and loading | `compilation-and-linking` | uni-upper | `procedure-calls-and-stack` |
| Representing IEEE floating-point numbers | `floating-point-hardware` | uni-upper | `digital-logic.fixed-point-numbers`, `assembly-arithmetic` |

### Single-cycle processor

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing datapath elements | `datapath-elements` | uni-upper | `digital-logic.datapath-and-controller`, `instruction-encoding` |
| Building a single-cycle datapath | `single-cycle-datapath` | uni-upper | `datapath-elements` |
| Designing the control unit | `control-unit-design` | uni-upper | `single-cycle-datapath` |
| Designing a multicycle processor | `multicycle-processor` | uni-upper | `control-unit-design`, `digital-logic.fsm-design` |

### Pipelining

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Building a pipelined datapath | `pipelined-datapath` | uni-upper | `single-cycle-datapath` |
| Resolving data hazards with forwarding | `data-hazards-and-forwarding` | uni-upper | `pipelined-datapath` |
| Inserting stalls for load-use hazards | `load-use-stalls` | uni-upper | `data-hazards-and-forwarding` |
| Handling control hazards | `control-hazards` | uni-upper | `pipelined-datapath` |
| Predicting branches | `branch-prediction` | uni-upper | `control-hazards` |
| Handling exceptions and interrupts in hardware | `exceptions-and-interrupts-hw` | uni-upper | `control-hazards` |
| Finding CPI of pipelined processors | `pipeline-performance` | uni-upper | `load-use-stalls`, `branch-prediction` |

### Memory hierarchy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing SRAM, DRAM and flash | `memory-technologies` | uni-upper | `digital-logic.memory-arrays` |
| Explaining temporal and spatial locality | `locality` | uni-upper | `memory-technologies` |
| Analyzing direct-mapped caches | `direct-mapped-caches` | uni-upper | `locality` |
| Analyzing set-associative caches | `set-associative-caches` | uni-upper | `direct-mapped-caches` |
| Comparing cache write policies | `cache-write-policies` | uni-upper | `direct-mapped-caches` |
| Finding average memory access time | `cache-performance` | uni-upper | `set-associative-caches`, `pipeline-performance` |
| Analyzing multilevel caches | `multilevel-caches` | uni-upper | `cache-performance` |
| Writing cache-friendly code | `cache-aware-programming` | uni-upper | `cache-performance`, `programming.nested-lists` |
| Translating addresses with page tables | `virtual-memory-hw` | uni-upper | `set-associative-caches` |
| Speeding translation with TLBs | `tlbs` | uni-upper | `virtual-memory-hw` |

### Input/output and parallelism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing buses and memory-mapped I/O | `io-and-buses` | uni-upper | `exceptions-and-interrupts-hw` |
| Using direct memory access | `dma` | uni-upper | `io-and-buses` |
| Comparing disks and solid-state storage | `storage-devices` | uni-upper | `memory-technologies` |
| Describing superscalar and out-of-order execution | `instruction-level-parallelism` | uni-upper | `pipeline-performance` |
| Describing SIMD and vector processing | `simd-and-vector` | uni-upper | `instruction-level-parallelism` |
| Explaining multicore cache coherence | `multicore-and-coherence` | uni-upper | `multilevel-caches` |
| Describing GPU architecture | `gpu-architecture` | uni-upper | `simd-and-vector` |

## engr.operating-systems: 42 topics

Follows `engr.architecture`, `engr.data-structures`.

### OS structure

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing operating system roles and the kernel | `os-roles-and-kernel` | uni-upper | `architecture.exceptions-and-interrupts-hw` |
| Using system calls | `system-calls` | uni-upper | `os-roles-and-kernel`, `architecture.procedure-calls-and-stack` |
| Explaining dual-mode operation and protection | `dual-mode-protection` | uni-upper | `os-roles-and-kernel` |

### Processes and threads

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing processes and their states | `processes` | uni-upper | `system-calls` |
| Creating processes with fork and exec | `process-creation` | uni-upper | `processes` |
| Explaining context switches | `context-switching` | uni-upper | `processes`, `dual-mode-protection` |
| Communicating between processes with pipes and shared memory | `interprocess-communication` | uni-upper | `process-creation` |
| Using threads | `threads` | uni-upper | `processes` |
| Comparing user and kernel threads | `thread-models` | uni-upper | `threads` |

### CPU scheduling

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing scheduling criteria | `scheduling-criteria` | uni-upper | `context-switching` |
| Scheduling with FCFS, SJF and SRTF | `fcfs-sjf-scheduling` | uni-upper | `scheduling-criteria` |
| Scheduling with round robin and priorities | `round-robin-and-priority` | uni-upper | `fcfs-sjf-scheduling` |
| Scheduling with multilevel feedback queues | `multilevel-feedback-queues` | uni-upper | `round-robin-and-priority` |
| Scheduling on multiprocessors | `multiprocessor-scheduling` | uni-upper | `multilevel-feedback-queues`, `thread-models` |
| Scheduling real-time tasks | `real-time-scheduling` | uni-upper | `round-robin-and-priority` |

### Synchronization

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Identifying race conditions and critical sections | `race-conditions` | uni-upper | `threads` |
| Implementing locks with atomic instructions | `locks` | uni-upper | `race-conditions`, `architecture.multicore-and-coherence` |
| Synchronizing with semaphores | `semaphores` | uni-upper | `locks` |
| Synchronizing with condition variables and monitors | `condition-variables-and-monitors` | uni-upper | `locks` |
| Solving producer-consumer and readers-writers problems | `classic-synchronization-problems` | uni-upper | `semaphores`, `condition-variables-and-monitors` |
| Explaining deadlock conditions | `deadlock-conditions` | uni-upper | `classic-synchronization-problems` |
| Preventing and avoiding deadlock with the banker's algorithm | `deadlock-prevention-avoidance` | uni-upper | `deadlock-conditions` |
| Detecting and recovering from deadlock | `deadlock-detection` | uni-upper | `deadlock-conditions`, `data-structures.cycle-detection` |

### Memory management

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing address spaces and binding | `address-spaces` | uni-upper | `processes`, `architecture.virtual-memory-hw` |
| Allocating memory contiguously | `contiguous-allocation` | uni-upper | `address-spaces` |
| Managing memory with paging | `paging` | uni-upper | `address-spaces` |
| Using multilevel page tables | `multilevel-page-tables` | uni-upper | `paging` |
| Implementing demand paging | `demand-paging` | uni-upper | `paging` |
| Comparing page replacement algorithms | `page-replacement` | uni-upper | `demand-paging` |
| Explaining thrashing and working sets | `thrashing-and-working-sets` | uni-upper | `page-replacement` |
| Implementing heap allocators | `memory-allocators` | uni-upper | `contiguous-allocation` |

### Storage and file systems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using files and directories | `file-system-interface` | uni-upper | `system-calls` |
| Scheduling disk requests | `disk-scheduling` | uni-upper | `architecture.storage-devices` |
| Comparing file allocation methods | `file-allocation-methods` | uni-upper | `file-system-interface` |
| Implementing directories and inodes | `directory-and-inode-structures` | uni-upper | `file-allocation-methods` |
| Managing free space | `free-space-management` | uni-upper | `file-allocation-methods` |
| Recovering file systems with journaling | `journaling-and-recovery` | uni-upper | `directory-and-inode-structures` |
| Using RAID | `raid` | uni-upper | `disk-scheduling` |

### Protection and virtualization

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Implementing access control | `access-control` | uni-upper | `dual-mode-protection`, `file-system-interface` |
| Describing operating system security threats | `security-threats-os` | uni-upper | `access-control` |
| Explaining virtual machines and hypervisors | `virtual-machines` | uni-upper | `dual-mode-protection`, `address-spaces` |
| Explaining containers | `containers` | uni-upper | `virtual-machines`, `process-creation` |

## engr.databases: 34 topics

Follows `engr.operating-systems`.

### Relational model and SQL

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing relations, keys and schemas | `relational-model` | uni-upper | `data-structures.abstract-data-types`, `math.discrete.relations-definition` |
| Writing relational algebra queries | `relational-algebra` | uni-upper | `relational-model` |
| Writing basic SQL queries | `sql-basic-queries` | uni-upper | `relational-algebra` |
| Writing SQL joins | `sql-joins` | uni-upper | `sql-basic-queries` |
| Writing SQL aggregation and grouping | `sql-aggregation` | uni-upper | `sql-basic-queries` |
| Writing nested SQL queries | `sql-subqueries` | uni-upper | `sql-joins`, `sql-aggregation` |
| Modifying data and declaring constraints in SQL | `sql-modification-and-constraints` | uni-upper | `sql-basic-queries` |
| Using views and access privileges | `views-and-access` | uni-upper | `sql-subqueries` |
| Connecting programs to databases | `database-applications` | uni-upper | `sql-modification-and-constraints`, `programming.modules-and-imports` |

### Database design

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Modelling data with entity-relationship diagrams | `er-modelling` | uni-upper | `relational-model` |
| Translating ER diagrams to relations | `er-to-relations` | uni-upper | `er-modelling` |
| Finding functional dependencies and closures | `functional-dependencies` | uni-upper | `relational-model` |
| Finding keys from functional dependencies | `keys-from-dependencies` | uni-upper | `functional-dependencies` |
| Testing for 3NF and BCNF | `normal-forms-db` | uni-upper | `keys-from-dependencies` |
| Decomposing relations losslessly | `decomposition` | uni-upper | `normal-forms-db` |

### Storage and indexing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Storing records in pages | `disk-pages-and-records` | uni-upper | `architecture.storage-devices` |
| Managing the buffer pool | `buffer-management` | uni-upper | `disk-pages-and-records` |
| Comparing heap and sorted files | `heap-and-sorted-files` | uni-upper | `disk-pages-and-records` |
| Using B+ tree indexes | `b-plus-tree-indexes` | uni-upper | `heap-and-sorted-files`, `data-structures.b-trees` |
| Using hash indexes | `hash-indexes` | uni-upper | `heap-and-sorted-files`, `data-structures.hash-maps-and-sets` |
| Comparing clustered and unclustered indexes | `clustered-indexes` | uni-upper | `b-plus-tree-indexes` |

### Query processing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Sorting data larger than memory | `external-sorting` | uni-upper | `buffer-management`, `data-structures.sort-comparisons` |
| Evaluating selections and projections | `selection-and-projection-algorithms` | uni-upper | `clustered-indexes`, `hash-indexes` |
| Comparing nested-loop, sort-merge and hash joins | `join-algorithms` | uni-upper | `external-sorting`, `hash-indexes` |
| Estimating query cost and selectivity | `query-cost-estimation` | uni-upper | `join-algorithms`, `selection-and-projection-algorithms` |
| Choosing query plans | `query-optimization` | uni-upper | `query-cost-estimation`, `relational-algebra` |

### Transactions

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing ACID properties | `acid-properties` | uni-upper | `sql-modification-and-constraints` |
| Testing conflict serializability | `serializability` | uni-upper | `acid-properties`, `data-structures.cycle-detection` |
| Using two-phase locking | `two-phase-locking` | uni-upper | `serializability` |
| Comparing isolation levels | `isolation-levels` | uni-upper | `two-phase-locking` |
| Explaining multiversion concurrency control | `multiversion-concurrency` | uni-upper | `isolation-levels` |
| Recovering with write-ahead logging | `logging-and-recovery` | uni-upper | `acid-properties`, `buffer-management` |

### Beyond single-node relational

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing partitioning and replication | `distributed-databases` | uni-upper | `logging-and-recovery` |
| Comparing document, key-value and graph databases | `nosql-models` | uni-upper | `relational-model` |

## engr.networks: 32 topics

Follows `engr.operating-systems`, `engr.algorithms`.

### Network fundamentals

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing protocol layers | `network-layers` | uni-upper | `operating-systems.interprocess-communication` |
| Finding delay and throughput | `delay-and-throughput` | uni-upper | `network-layers` |
| Comparing circuit and packet switching | `circuit-and-packet-switching` | uni-upper | `delay-and-throughput` |

### Application layer

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining HTTP and the web | `http-and-web` | uni-upper | `network-layers` |
| Explaining DNS resolution | `dns` | uni-upper | `http-and-web` |
| Writing socket programs | `socket-programming` | uni-upper | `network-layers`, `operating-systems.threads` |
| Explaining caching and content delivery | `content-delivery` | uni-upper | `http-and-web` |

### Transport layer

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using UDP | `udp` | uni-upper | `socket-programming` |
| Designing reliable data transfer protocols | `reliable-data-transfer` | uni-upper | `udp` |
| Analyzing go-back-N and selective repeat | `sliding-window-protocols` | uni-upper | `reliable-data-transfer`, `delay-and-throughput` |
| Explaining TCP connection setup and teardown | `tcp-connection-management` | uni-upper | `sliding-window-protocols` |
| Explaining TCP flow control | `tcp-flow-control` | uni-upper | `tcp-connection-management` |
| Estimating TCP retransmission timeouts | `tcp-timeout-estimation` | uni-upper | `tcp-connection-management` |
| Explaining congestion control principles | `congestion-control-principles` | uni-upper | `sliding-window-protocols` |
| Analyzing TCP congestion control | `tcp-congestion-control` | uni-upper | `congestion-control-principles`, `tcp-flow-control` |

### Network layer

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Assigning IP addresses and subnets | `ip-addressing-and-subnets` | uni-upper | `network-layers`, `digital-logic.binary-and-hex-codes` |
| Forwarding with longest prefix match | `forwarding-tables` | uni-upper | `ip-addressing-and-subnets` |
| Explaining NAT and DHCP | `nat-and-dhcp` | uni-upper | `ip-addressing-and-subnets` |
| Describing IPv6 | `ipv6` | uni-upper | `ip-addressing-and-subnets` |
| Computing routes with link-state routing | `link-state-routing` | uni-upper | `forwarding-tables`, `data-structures.dijkstra-code` |
| Computing routes with distance-vector routing | `distance-vector-routing` | uni-upper | `forwarding-tables`, `algorithms.shortest-paths-negative-edges` |
| Explaining BGP | `interdomain-routing` | uni-upper | `distance-vector-routing` |

### Link layer

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Detecting errors with checksums and CRC | `error-detection-link` | uni-upper | `digital-logic.error-detecting-codes` |
| Analyzing multiple access protocols | `multiple-access-protocols` | uni-upper | `delay-and-throughput`, `math.probstat.binomial-mean-variance` |
| Explaining Ethernet and learning switches | `ethernet-and-switches` | uni-upper | `multiple-access-protocols` |
| Explaining ARP | `arp` | uni-upper | `ethernet-and-switches`, `ip-addressing-and-subnets` |
| Describing wireless and mobile networks | `wireless-links` | uni-upper | `multiple-access-protocols` |

### Security and performance

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using symmetric and public-key cryptography | `cryptography-basics` | uni-upper | `math.discrete.rsa-cryptography` |
| Using message authentication and digital signatures | `authentication-and-integrity` | uni-upper | `cryptography-basics` |
| Explaining TLS | `secure-transport` | uni-upper | `authentication-and-integrity`, `tcp-connection-management` |
| Describing firewalls and intrusion detection | `firewalls-and-intrusion-detection` | uni-upper | `forwarding-tables`, `secure-transport` |
| Modelling router queues | `queueing-in-routers` | uni-upper | `delay-and-throughput`, `math.probstat.poisson-process-intro` |

## engr.software-engineering: 30 topics

Follows `engr.algorithms`.

### Process and requirements

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Comparing waterfall, iterative and agile processes | `software-processes` | uni-upper | `data-structures.choosing-data-structures` |
| Using agile practices such as sprints and stand-ups | `agile-practices` | uni-upper | `software-processes` |
| Eliciting and writing requirements | `requirements-elicitation` | uni-upper | `software-processes` |
| Writing user stories and acceptance criteria | `user-stories` | uni-upper | `requirements-elicitation`, `agile-practices` |
| Estimating and planning software work | `estimation-and-planning` | uni-upper | `user-stories` |

### Design and modelling

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Drawing UML class diagrams | `uml-class-diagrams` | uni-upper | `programming.inheritance`, `requirements-elicitation` |
| Drawing sequence and state diagrams | `uml-behaviour-diagrams` | uni-upper | `uml-class-diagrams` |
| Applying cohesion, coupling and SOLID principles | `design-principles` | uni-upper | `uml-class-diagrams`, `programming.abstract-interfaces` |
| Using creational design patterns | `creational-patterns` | uni-upper | `design-principles` |
| Using structural design patterns | `structural-patterns` | uni-upper | `design-principles` |
| Using behavioural design patterns | `behavioural-patterns` | uni-upper | `design-principles` |
| Comparing architectural styles | `software-architecture-styles` | uni-upper | `structural-patterns`, `behavioural-patterns` |
| Designing APIs | `api-design` | uni-upper | `design-principles` |

### Construction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Branching and merging with version control | `version-control-branching` | uni-upper | `programming.version-control-basics` |
| Reviewing code | `code-review` | uni-upper | `version-control-branching`, `programming.code-style` |
| Refactoring code safely | `refactoring` | uni-upper | `design-principles`, `programming.unit-test-suites` |
| Managing builds and dependencies | `build-and-dependency-management` | uni-upper | `version-control-branching` |
| Setting up continuous integration | `continuous-integration` | uni-upper | `build-and-dependency-management`, `programming.unit-test-suites` |

### Verification and validation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing unit tests with test doubles | `unit-testing-practice` | uni-upper | `programming.unit-test-suites`, `design-principles` |
| Developing test-first | `test-driven-development` | uni-upper | `unit-testing-practice` |
| Designing tests with coverage and partitioning | `coverage-and-test-design` | uni-upper | `unit-testing-practice` |
| Planning integration and system tests | `integration-and-system-testing` | uni-upper | `coverage-and-test-design` |
| Using static analysis and type checking | `static-analysis` | uni-upper | `code-review` |
| Writing preconditions, postconditions and invariants | `formal-specification` | uni-upper | `programming.docstrings-and-contracts`, `algorithms.proving-algorithm-correctness` |

### Quality and maintenance

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Debugging systematically | `debugging-techniques` | uni-upper | `integration-and-system-testing`, `programming.debugging-strategies` |
| Measuring software quality | `software-metrics` | uni-upper | `static-analysis` |
| Avoiding common security vulnerabilities | `secure-coding` | uni-upper | `code-review` |
| Profiling and optimizing performance | `performance-profiling` | uni-upper | `debugging-techniques`, `programming.timing-programs` |
| Maintaining and evolving software | `maintenance-and-evolution` | uni-upper | `refactoring`, `software-metrics` |
| Coordinating software teams | `team-collaboration` | uni-upper | `code-review`, `estimation-and-planning` |

## engr.embedded: 23 topics

Follows `engr.operating-systems`, `engr.electronics`.

### Microcontroller basics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing microcontroller architecture | `microcontroller-architecture` | uni-upper | `architecture.io-and-buses` |
| Configuring peripherals through memory-mapped registers | `memory-mapped-registers` | uni-upper | `microcontroller-architecture`, `programming.integer-division-and-remainder` |
| Setting and clearing bits with masks | `bit-manipulation` | uni-upper | `memory-mapped-registers`, `digital-logic.binary-and-hex-codes` |
| Using general-purpose input and output | `gpio` | uni-upper | `bit-manipulation`, `circuits.voltage-and-current-dividers` |
| Debouncing switches | `switch-debouncing` | uni-upper | `gpio` |

### Interrupts and timing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing interrupt service routines | `interrupt-service-routines` | uni-upper | `gpio`, `architecture.exceptions-and-interrupts-hw` |
| Managing interrupt priorities and latency | `interrupt-priorities-and-latency` | uni-upper | `interrupt-service-routines` |
| Protecting shared data in interrupts | `shared-data-and-volatile` | uni-upper | `interrupt-service-routines`, `operating-systems.race-conditions` |
| Using hardware timers | `hardware-timers` | uni-upper | `interrupt-service-routines` |
| Generating PWM signals | `pwm-output` | uni-upper | `hardware-timers` |
| Measuring signals with input capture | `input-capture` | uni-upper | `hardware-timers` |

### Analog interfacing

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading analog inputs with an ADC | `adc-interfacing` | uni-upper | `gpio`, `electronics.data-converters` |
| Producing analog output with DACs and PWM filtering | `dac-and-filtering` | uni-upper | `pwm-output`, `circuits.passive-filters` |
| Conditioning sensor signals for an ADC | `sensor-signal-conditioning` | uni-upper | `adc-interfacing`, `circuits.inverting-and-noninverting` |

### Communication interfaces

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Communicating over UART | `uart` | uni-upper | `interrupt-service-routines` |
| Communicating over SPI | `spi` | uni-upper | `uart` |
| Communicating over I2C | `i2c` | uni-upper | `uart` |
| Choosing a serial protocol | `communication-protocol-choice` | uni-upper | `spi`, `i2c` |

### Software structure

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Structuring firmware with loops and state machines | `superloop-and-state-machines` | uni-upper | `interrupt-service-routines`, `digital-logic.fsm-design` |
| Structuring firmware with RTOS tasks | `rtos-tasks` | uni-upper | `superloop-and-state-machines`, `operating-systems.real-time-scheduling` |
| Reducing power with sleep modes | `low-power-design` | uni-upper | `hardware-timers` |
| Controlling motors from a microcontroller | `motor-control-embedded` | uni-upper | `pwm-output`, `controls.digital-controller-implementation` |
| Debugging embedded systems | `embedded-debugging` | uni-upper | `uart` |

## engr.theory: 27 topics

Follows `engr.algorithms`.

### Regular languages

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining alphabets, strings and languages | `alphabets-strings-languages` | uni-upper | `math.discrete.set-operations`, `math.discrete.induction-structural` |
| Designing deterministic finite automata | `dfa` | uni-upper | `alphabets-strings-languages` |
| Designing nondeterministic finite automata | `nfa` | uni-upper | `dfa` |
| Converting NFAs to DFAs | `nfa-to-dfa` | uni-upper | `nfa` |
| Proving closure under regular operations | `regular-operations-closure` | uni-upper | `nfa-to-dfa` |
| Writing regular expressions | `regular-expressions` | uni-upper | `alphabets-strings-languages` |
| Converting between regular expressions and automata | `regex-nfa-equivalence` | uni-upper | `regular-expressions`, `nfa-to-dfa` |
| Minimizing DFAs | `dfa-minimization` | uni-upper | `nfa-to-dfa`, `math.discrete.equivalence-classes-discrete` |
| Proving languages nonregular with the pumping lemma | `pumping-lemma-regular` | uni-upper | `regular-operations-closure`, `math.discrete.pigeonhole` |

### Context-free languages

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing context-free grammars | `context-free-grammars` | uni-upper | `regular-expressions` |
| Drawing parse trees and finding ambiguity | `parse-trees-and-ambiguity` | uni-upper | `context-free-grammars` |
| Converting grammars to Chomsky normal form | `chomsky-normal-form` | uni-upper | `context-free-grammars` |
| Designing pushdown automata | `pushdown-automata` | uni-upper | `context-free-grammars`, `nfa` |
| Converting between grammars and pushdown automata | `cfg-pda-equivalence` | uni-upper | `pushdown-automata` |
| Proving languages not context-free | `pumping-lemma-context-free` | uni-upper | `cfg-pda-equivalence`, `pumping-lemma-regular` |
| Parsing with the CYK algorithm | `cyk-parsing` | uni-upper | `chomsky-normal-form`, `algorithms.dp-principles` |

### Computability

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Designing Turing machines | `turing-machines` | uni-upper | `pushdown-automata` |
| Showing equivalence of Turing machine variants | `tm-variants` | uni-upper | `turing-machines` |
| Explaining the Church-Turing thesis | `church-turing-thesis` | uni-upper | `tm-variants` |
| Proving languages decidable | `decidable-languages` | uni-upper | `church-turing-thesis` |
| Proving the halting problem undecidable | `diagonalization-and-halting` | uni-upper | `decidable-languages`, `math.discrete.countable-sets` |
| Proving undecidability by mapping reductions | `mapping-reductions` | uni-upper | `diagonalization-and-halting` |
| Using Rice's theorem | `rices-theorem` | uni-upper | `mapping-reductions` |
| Classifying recognizable and co-recognizable languages | `recognizable-languages` | uni-upper | `mapping-reductions` |

### Complexity

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining time complexity classes | `time-complexity-classes` | uni-upper | `turing-machines`, `algorithms.p-and-np` |
| Explaining the Cook-Levin theorem | `cook-levin` | uni-upper | `time-complexity-classes`, `algorithms.np-completeness-proofs` |
| Defining space complexity classes | `space-complexity-classes` | uni-upper | `time-complexity-classes` |
