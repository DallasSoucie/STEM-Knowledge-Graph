# Degree coverage review

Date: 2026-11-08. This review checks the graph's university courses against real degree requirements. It proposes additions only; the graph is unchanged.

## Method

1. **Degree requirement pages (17 downloaded).** The pages are saved under `refs/uni_syllabi/degree-*` and indexed in `SOURCES.md`.
   - Math BS: UNH, Case, TCU.
   - Physics BS: Penn State, Cal Poly, Fort Hays, UVU.
   - Biochemistry BS: Tufts, K-State, UW, Case, Lehigh.
   - Biology BS: ECU, UConn.
   - Chemistry BS (ACS-certified): UW, Iowa, Harvey Mudd.
   - Eight further pages failed to download (HTTP 202, 403 or 404).
2. **Accreditation and exam specifications already in refs.** These are the ACS guidelines, the ABET CAC criteria, and the FE specifications for Civil, Chemical, Mechanical, and Electrical and Computer.
3. **Course-level check.** Each degree's required and common elective courses were compared with the course catalog in `graph/courses.yaml`.
4. **Topic-level check.** For each of the 37 university math, physics, chemistry and biology courses, a list of 15-25 core concepts was matched against topic names and KP statements.
   - Each miss was then searched across the whole graph and checked by hand.
   - Most misses turned out to be wording differences, or content taught in an earlier course. Only the real gaps are listed below.

**Limits of the method.** Keyword matching is coarse. Engineering courses were checked against the FE specifications and ABET only, not topic by topic. No degree pages were downloaded for engineering programs.

## Summary

The core of every target degree is covered:

- **Math:** the calculus sequence, linear algebra, differential equations, proofs, analysis, abstract algebra, complex analysis, numerical analysis, PDEs and probability.
- **Physics:** classical mechanics, electromagnetism, quantum mechanics, statistical physics, modern physics, and waves and optics.
- **Chemistry:** all five ACS foundation areas.
- **Biology:** the five core areas.
- **Engineering:** most FE content areas.

The gaps are mostly courses that degrees commonly require or offer as standard upper-level electives, plus a few missing topics inside existing courses.

## Proposed new courses

Topic counts are rough estimates. Every new course would get its own topic-list plan for approval before anything is written.

### Tier 1: required by many degrees, or on the FE

| Course | Degree | Evidence | Est. topics |
|---|---|---|---|
| `physics.solid-state` | Physics | Required at Fort Hays and an option at PSU, UVU and Cal Poly. The graph has only about 10 scattered topics on lattices, bands and semiconductors. | 70 |
| `physics.nuclear-particle` | Physics | Subatomic or nuclear physics at PSU and UVU. Only about 8 topics now, all in `physics.modern`. | 60 |
| `math.number-theory` | Math | Listed by UNH and Case and offered at nearly every school. Congruences now appear only in `math.discrete` and `math.abstract`. | 80 |
| `math.topology` | Math | Required at UNH and common elsewhere. Missing entirely. | 90 |
| `bio.molecular-biology` | Biochemistry, Biology | Required at Case, Tufts and Lehigh. Covers nucleic acid mechanisms, recombinant DNA, sequencing and genome tools; this content is now thinly spread across genetics, cell-mol and biochem. | 50 |
| `bio.immunology` | Biology, pre-med | A standard biology course and MCAT content. Immunology now appears only within `bio.micro` and `bio.anat-phys2`. | 45 |
| `engr.surveying` | Civil | FE Civil section 9: angles and distances, areas, earthwork volumes, coordinate systems, leveling. Missing entirely. | 30 |
| `engr.construction` | Civil | FE Civil section 14: project delivery, scheduling (critical path), earned value, estimating, productivity. Missing entirely. | 30 |
| `engr.programming-languages` | Software, Computer | ABET CAC requires "concepts of programming languages" for computer science. Covers paradigms, scope, type systems, functional programming, parsing and interpreters. Missing. | 40 |

### Tier 2: common electives or concentrations

| Course | Degree | Evidence | Est. topics |
|---|---|---|---|
| `math.geometry` | Math, math education | College geometry (axioms, non-Euclidean geometry) at UNH. Missing entirely. | 70 |
| `physics.optics` | Physics | Intermediate optics is required at Fort Hays, Cal Poly and UVU. Intro optics exists, but coherence, Fourier optics, interferometers and lasers are thin. | 50 |
| `bio.developmental` | Biology | Offered by most programs. Only 5 topics now, all intro or high school level. | 35 |
| `bio.plant` | Biology | Botany or plant biology at UConn and ECU. Only 5 topics now, in `bio.intro2`. | 40 |
| `engr.process-design-safety` | Chemical | FE ChE section 16 (safety, health and environment), plus capstone process design. Only 1 safety topic now. | 30 |
| `math.optimization` | Math, Industrial, Chemical, CS | Linear programming, the simplex method, convexity and KKT conditions. Missing entirely; Case lists convexity and optimization. | 50 |

### Tier 3: optional, lower priority

- **`physics.computational`.** Required at PSU and Fort Hays. It mostly applies `math.numerical` plus programming.
- **`chem.instrumental`.** A separate in-depth course at many ACS schools. `chem.analytical` already covers the main instrument families.
- **`bio.biochem2`.** Our `bio.biochem` compresses two semesters into 55 topics; the alternative is enlarging it.
- **`bio.bioinformatics`.**
- **`engr.machine-learning`.**
- **`engr.fea`.** Finite element analysis is now 1 topic.
- **`math.graph-theory`.**
- **Differential geometry.**
- **General relativity.**

## Topic gaps inside existing courses

These are small additions that need no new course:

- **`math.numerical`:** numerical differentiation (finite-difference derivative formulas, error, Richardson extrapolation). No university-level topic covers it anywhere.
- **`bio.biochem`:** photosynthesis (light reactions, the Calvin cycle, photorespiration). It now appears only in high school courses.
- **`physics.stat-thermal`:** phase transitions (an Ising model or mean-field treatment). Only 2 loose matches; worth checking by hand.
- **Polymers and macromolecules (ACS).** The ACS guidelines require this coverage across the curriculum. There are about 16 scattered topics; consider a small polymer cluster in `chem.org2` or `engr.materials`.

## Decisions for you

1. **Which tiers to build.** Tier 1 adds roughly 495 topics and Tier 2 roughly 275.
2. **Ethics and professional practice.** This appears on every FE exam but is not quantitative STEM content. I recommend leaving it out of scope.
3. **Path to `chem.pchem2`.** `chem.pchem2` follows `physics.quantum`, so a chemistry or biochemistry learner must take a 95-topic physics quantum course first. Most chemistry degrees teach quantum chemistry on its own. Keep the current design, or give pchem2 its own short quantum lead-in?
