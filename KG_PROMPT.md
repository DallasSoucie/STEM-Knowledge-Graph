# Goal

I'm building a Math Academy-style adaptive learning app covering kindergarten through university-level math, physics, chemistry, biology, and engineering. Build the knowledge graph that will drive it: topics, the knowledge points (KPs) inside each topic, and the prerequisite and encompassing connections between topics, including connections across subjects. This task is graph only: no lessons and no problems.

`CLAUDE.md` is the source of truth for the graph model, data format, validation rules, and workflow. This prompt adds the mission: how big the graph is, how to author it well, and what order to build it in. Where the two disagree, follow `CLAUDE.md` and raise the disagreement with me.

**Done looks like:** every course in the catalog is built, `validate` is green, and a task-selection model could consume the graph without any further structural work.

# Size target

Math Academy runs about 2,500 topics on math alone. Matching that density across five subjects, and starting from kindergarten, gives a far larger graph:

| Scope | Courses | Topics (estimate) |
|---|---|---|
| Math | 27 | 4,370 |
| Physics | 12 | 1,335 |
| Chemistry | 12 | 790 |
| Biology | 15 | 755 |
| Engineering common core | 13 | 805 |
| **Core graph** | **79** | **~8.1k** |
| Engineering discipline courses | 31 | 1,295 |
| **Full graph** | **110** | **~9,350** |

At about 3.4 KPs and 5 weighted relationships per topic, the full graph holds roughly 32,000 KPs and 47,000 weights.

These are planning budgets, and they are my estimates rather than Math Academy's figures. Topic counts should come out of honest granularity:

- **Under budget:** check for overloaded topics and missing stepping stones. Add topics only where a real step is missing.
- **Over budget:** check for idiosyncratic or second-course material.
- **More than 20% off budget in either direction:** explain why when presenting the course.
- **Calibration check:** math from grade 4 through differential equations, proofs, discrete math, and probability budgets to about 3,300 topics. That is the span closest to Math Academy's 2,500, so land well below 2,500 there and the grain is probably too coarse.

# Course catalog (provisional)

The number after each course is its topic budget. Confirm or revise this list in the Phase 0 plan. A university course stays within the 200-topic cap.

**Math**
- Grades: k 60, g1 80, g2 100, g3 120, g4 150, g5 160, g6 170, g7 180, g8 200
- High school: alg1 240, geom 200, alg2 240, precalc 260, stats 120
- University: calc1 180, calc2 180, calc3 180, linalg 180, diffeq 190, discrete 170, probstat 190, proofs 110, analysis 160, abstract 160, numerical 130, pde 140, complex 120, number-theory 75, topology 80, geometry 65, optimization 55

**Physics**
- School: elem 40, ms 80, hs1 200, hs2 165
- University: mechanics 140, em 140, waves-thermo-optics 115, modern 100, classical 95, em-theory 100, quantum 95, stat-thermal 65, solid-state 65, nuclear-particle 55, optics 50

**Chemistry**
- School: elem 25, ms 55, hs1 125, hs2 90
- University: gen1 55, gen2 55, org1 100, org2 80, analytical 55, inorganic 50, pchem1 50, pchem2 50

**Biology**
- School: elem 30, ms 45, hs1 90, hs2 70
- University: intro1 35, intro2 55, cell-mol 55, genetics 45, biochem 55, ecology 35, evolution 35, micro 40, anat-phys1 60, anat-phys2 60, neuro 45, molecular-biology 50, immunology 45, developmental 40, plant 45

**Engineering common core**
- programming 100, data-structures 60, statics 65, dynamics 50, mech-materials 60, thermo 80, fluids 65, circuits 70, materials 65, digital-logic 50, signals 50, economics 40
- Shared upper course: controls 50 (mechanical, electrical and chemical)

**Engineering discipline courses** (built after the core graph)
- Civil: structural-analysis 55, soil-mechanics 60, hydraulics 45, steel-design 35, concrete-design 40, transportation 40, environmental 35, surveying 35, construction 35
- Chemical: mass-energy-balances 40, cheme-thermo 40, mass-transfer 30, separations 40, reactors 40, process-control 30, process-design-safety 35
- Mechanical: heat-transfer 65, machine-design 55, vibrations 35, manufacturing 35, measurements 25
- Electrical: electronics 65, em-fields 40, power 50, communications 45, dsp 40
- Computer/software: algorithms 50, architecture 45, operating-systems 50, databases 40, networks 35, software-engineering 35, embedded 25, theory 30, programming-languages 45

Each topic has exactly one home course, where it is first taught. Vectors live in math, and "resolving forces into components" lives in physics with a prerequisite on math vectors. Courses that repackage existing material (AP Calculus, for example) are views in the manifest that list existing topic IDs. They add no new topics.

# Authoring heuristics

These come from how Math Academy built its graph. Apply them to every topic.

**Judge each item individually.** Math Academy handcrafts its graph, and the value is in the expert judgement behind each entry. Reason about what a student actually does in that KP, then set its edges and weight. A course where the weights cluster on a few default values has been templated, so redo it.

**Size topics with the stepping-stone test.** Picture stones across a creek: every gap should be crossable by an ordinary student, not just a gifted one. Standard textbook sequences often contain big jumps, so look for the missing stone rather than inheriting the gap.
- **Split test:** could a student reasonably learn the second half after sleeping on the first? If so, it's two topics. Example: one iteration of Euler's method, then multiple iterations.
- **Concrete first:** a tangent-line approximation by hand comes before Euler's method, and exploring linearity comes before integrating factors.
- Splitting is the most common repair. Math Academy's author estimates using the split tool about 500 times, so expect to split often and make it cheap.

**Build each KP as a rung.** Three KPs is the ideal and four is common: the vanilla case, a twist, another twist, and sometimes the pieces combined. Students must pass each rung before climbing, so every `can_do` needs to be demonstrable on its own in a handful of problems.

**Treat each topic as an intersection.**
- Direct prerequisites: 1-2 is great, 3 is fine, and 4 means look for a stepping stone. 5 is a rare, justified exception.
- Key prerequisites are the real pressure point, because students meet them one KP at a time and working memory holds about four chunks. A single KP with 3-4 is acceptable. A topic where every KP has 3-4 is congested, so restructure it.
- The limit is a ceiling. Many KPs should need only one or two.

**Set encompassing weights by simulating a problem.** Ask what fraction of the prerequisite topic gets exercised, on average across this topic's problems.

| Weight | Meaning |
|---|---|
| 0 | Must come first, but isn't practiced here |
| 0.1-0.3 | A small part appears, or it appears in only some KPs |
| 0.4-0.6 | A substantial part is exercised in a typical problem |
| 0.7-1.0 | Nearly the whole prerequisite is a step in nearly every problem |

These weights are what make the task-selection model work: Math Academy reported that it began performing very well once they were in place. When unsure, lean low, because too much credit lets a skill go unreviewed and fade, while too little only adds some extra review. Use `confidence` to say how sure you are.

**Hidden context is a prerequisite.** Math Academy found a young student stuck on algebra mixture problems because they had never learned what a mixture is. When a KP's context assumes outside knowledge, especially in K-8, add the real prerequisite or a stepping stone. If neither fits, flag it for review.

**Scope university courses by survey.** For each course, compare about 8-10 strong universities' public syllabi and exams, plus well-regarded textbooks.
- Keep what nearly all of them cover, plus a handful of topics that some cover.
- Cut what only one professor would teach.
- Move second-course material to its own course.
- A learner comparing our course with a strong university's should find nothing important missing.

`refs/uni_course_descriptions` has only two universities, so it can't support this survey by itself. Use public syllabi as well. Survey for coverage only, and write topic names and order yourself, so that no single source shows through.

**Expect cross-subject edges and only keep the real ones.** Math is the spine. Prerequisites across all disciplines are the goal, so an early course in any subject may have first topics that depend on other subjects, including engineering's opening topics. When a course's topic list is approved, settle its `follows` links in `graph/courses.yaml` so real cross-discipline prerequisites can exist. The test for an edge is whether a student gets stuck without that prerequisite, and an uncertain link gets `confidence: low`.

# Tooling

`CLAUDE.md` lists the required commands and validation rules. Math Academy's first tools were validators, and they grew to about 100 checks after hand edits broke production with cycles and bad IDs. Treat these as requirements on top of that list:

- **Keep `validate` fast.** It should finish in under 10 seconds on a synthetic 20,000-topic graph, because it runs on every batch. Test this.
- **Gate every commit.** Add a pre-commit hook that runs `validate`. The hook is `.githooks/pre-commit`; enable it with `git config core.hooksPath .githooks`.
- **Test the consumer's path.** Math Academy runs the real model build against each change. Until we have a model, `validate` should simulate a learner: starting from nothing, walk each course sequence in order and confirm every topic becomes reachable.
- **Prefer CLI tools.** Each tool does one job, with useful options and readable output. Build a new tool whenever a repeated edit is error-prone.
- **Add `export-weights` and `import-weights`.** Round-trip all weights through CSV, so that recalibrating from student data is one bulk operation.
- **Add `find-duplicates`.** Across 100 courses, the same skill will get written twice under different IDs, and validation can't see that. Compare names and `can_do` text across courses.
- **Add `review-queue`.** Extend `review-report` with a queue ranked by risk: low confidence, then high descendant count, then cross-subject edges.
- **Plan for change after launch.** `split-topic` and `rename-id` should record old-to-new IDs in `graph/id-history.yaml`, so that student records can follow them later. A new KP takes the next unused ID, and list position sets the order, so per-KP data stays attached when a rung is inserted.

# Human review at this scale

Math Academy's author spent about a month, full time, on weights for 1,500 topics, at about 2 minutes per weight. The same pace would take me about 2,600 hours on the full graph, so I can't review everything. Only I set `status: reviewed`, so the graph must stay honest while most of it is `draft`:

- `review-queue` decides where my time goes. The highest-leverage edges come first.
- Weights are initial estimates until student data arrives. Math Academy investigates when pass rates fall from its roughly 94-95% benchmark toward 80%, and the usual repair is adding a KP or splitting the topic. The IDs and CSV round trip above keep that path open.
- Report each course's `confidence` mix, so that I can see where you were guessing.

# Process

Each phase ends at a stop. Wait for my approval before moving on.

**Phase 0: Plan. (Done.)** Write no content yet. Propose the repo layout, any schema details `CLAUDE.md` leaves open, catalog revisions, and build order. Done when I've approved it.

**Phase 1: Tooling. (Done.)** Build the schema, the CLI, the manifest, and a tiny sample graph. Done when `pytest` passes, the 20,000-topic speed test passes, and a test shows each validation rule failing on a deliberately broken graph.

**Phase 2: Courses.** Build math first, in spine order, then physics, chemistry, biology, and engineering. On starting any session, run `stats` and read the manifest to find where things stand. For each course:

1. **Plan the course.** Present its topic list with the count, level range, cross-course dependencies, and scope survey results. Stop for approval.
2. **Write it.** Add topics in course order, in batches of 20-40. Create stubs for prerequisites in unbuilt courses. Run `validate` after each batch and commit it.
3. **Self-review it.** Check every topic against the authoring heuristics. Hunt for overloaded topics, large jumps, duplicates, missing prerequisites, invented links, and clustered weights. Fix what you find.
4. **Present it.** Run `review-report`, `find-duplicates`, and `stats`, then regenerate the map with `export-map` and show me it along with the results, the budget variance, and your uncertainties. The course is done when `validate` is green and I've accepted it.

When a course fills in stubs that others point at, recheck those edges.

**Milestones to pause and reassess:** math complete, core graph complete, and full graph complete. At each one, report totals against the budget and the distributions of prerequisites, KPs, weights, and depth.
