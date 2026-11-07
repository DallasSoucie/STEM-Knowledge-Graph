# Topic lists: remaining university physics

Draft for approval. Covers `physics.waves-thermo-optics`, `physics.modern`, `physics.classical`, `physics.em-theory`, `physics.quantum` and `physics.stat-thermal`. In the Needs column, a plain name is in the same course; `hs1.`, `hs2.`, `mechanics.`, `em.`, `waves-thermo-optics.` and `modern.` name physics courses; any other prefix (such as `calc3.`) names a math course.

## Proposed manifest changes

`follows` additions, so each course can reach the topics it builds on:

- `physics.waves-thermo-optics`: add `physics.hs2` (high school thermal physics and optics) and `math.calc3` (partial derivatives for the wave equation, Gaussian integrals for speed distributions).
- `physics.em-theory`: add `physics.modern` (relativity for relativistic electrodynamics) and `math.pde` (Laplace's equation, Legendre expansions, delta functions).
- `physics.quantum`: add `math.pde` (Fourier transforms, spherical Laplacian, Legendre functions).
- `physics.stat-thermal`: add `physics.modern` (quantized energy levels, spin, Fermi energy).

Budgets: every list came in well under its budget, so I propose lowering them to fit the content:

| Course | Topics | Budget now | Proposed |
|---|---|---|---|
| waves-thermo-optics | 112 | 170 | 115 |
| modern | 95 | 150 | 100 |
| classical | 90 | 160 | 95 |
| em-theory | 98 | 170 | 100 |
| quantum | 89 | 180 | 95 |
| stat-thermal | 61 | 150 | 65 |
| **Total** | **545** | **980** | **570** |

That would bring the physics total from 1,780 to 1,370 and the full graph from about 15,600 to about 15,170. The alternative is keeping the budgets and splitting topics more finely; these upper-level topics are already near lesson size, so splitting would mostly add padding.

## Survey

Sources are indexed in `refs/uni_syllabi/SOURCES.md` under `physics-waves-thermo-optics`, `physics-modern`, `physics-classical`, `physics-em-theory`, `physics-quantum` and `physics-stat-thermal` (24 of 32 downloads saved). The strongest anchors are MIT (8.04, 8.05, 8.09, 8.044), Washington, Chicago, Wellesley, NTU Singapore, NTNU, Edinburgh and Westlake. The common backbones match: relativity, early quanta, Schrodinger, atoms, nuclei for modern; variations, Lagrangian, central forces, rigid bodies, normal modes, Hamiltonian for classical; boundary-value problems, multipoles, matter, waves, radiation for E&M; formalism, angular momentum, spin, identical particles, perturbation theory for quantum; ensembles and quantum statistics for thermal.

## Scope decisions

- Oscillations stay in `physics.mechanics`; `waves-thermo-optics` starts at waves. Fluids there are a short calculus layer; most fluid mechanics belongs to `engr.fluids`.
- Chaos topics build on `math.diffeq` (nonlinear pendulum, bifurcations, limit cycles) instead of reteaching them.
- Calculus of variations, Hermite polynomials and Stirling's approximation are homed in physics because no math course has them.
- Chemistry interface, to recheck when chemistry is drafted: `enthalpy`, `multi-electron-atoms`, `ideal-mixtures`, `law-of-mass-action`, `semiconductor-carrier-statistics`.
- Left out as second-course or specialist material: general relativity, quantum field theory, plasma physics, continuum mechanics beyond a string, and solid state beyond bands.

## physics.waves-thermo-optics: 112 topics, budget 170 (proposed 115)

### Wave kinematics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing traveling wave functions | `wave-functions` | uni-lower | `hs1.position-and-time-wave-graphs`, `mechanics.sinusoidal-solutions` |
| Using wave number and angular frequency | `wave-number-and-angular-frequency` | uni-lower | `wave-functions` |
| Finding particle velocity in a wave with partial derivatives | `particle-velocity-in-a-wave` | uni-lower | `wave-number-and-angular-frequency`, `calc3.partial-derivatives-compute` |
| Checking solutions of the one-dimensional wave equation | `wave-equation-one-dimension` | uni-lower | `particle-velocity-in-a-wave`, `calc3.higher-partials` |
| Deriving the wave equation for a string | `string-wave-equation-derivation` | uni-lower | `wave-equation-one-dimension`, `mechanics.tension-in-a-massive-rope` |
| Recognizing any shape moving at constant speed as a wave | `general-traveling-solutions` | uni-lower | `wave-equation-one-dimension`, `calc3.chain-rule-multivariable` |
| Writing waves with complex exponentials | `complex-wave-notation` | uni-lower | `wave-functions`, `precalc.polar-form-complex`, `calc2.series-for-exp` |
| Finding energy carried by a string wave | `energy-on-a-string` | uni-lower | `string-wave-equation-derivation`, `mechanics.energy-of-shm-with-calculus` |
| Finding average power of a string wave | `power-of-a-string-wave` | uni-lower | `energy-on-a-string` |
| Writing plane and spherical waves | `waves-in-two-and-three-dimensions` | uni-lower | `wave-functions`, `mechanics.dot-product-in-physics` |
| Finding intensity of spherical waves | `spherical-wave-intensity` | uni-lower | `waves-in-two-and-three-dimensions`, `power-of-a-string-wave` |

### Superposition and boundaries

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding reflected and transmitted waves at a junction | `reflection-at-a-boundary` | uni-lower | `general-traveling-solutions`, `hs1.boundary-behaviour` |
| Using wave impedance at a string junction | `impedance-of-a-string` | uni-lower | `reflection-at-a-boundary` |
| Adding sinusoidal waves with trig identities | `superposing-sinusoidal-waves` | uni-lower | `wave-functions`, `hs1.superposition` |
| Building standing waves from opposite traveling waves | `standing-waves-from-superposition` | uni-lower | `superposing-sinusoidal-waves`, `hs1.standing-waves-on-strings` |
| Finding normal modes of a fixed string | `normal-modes-of-a-string` | uni-lower | `standing-waves-from-superposition`, `string-wave-equation-derivation` |
| Finding energy in standing waves | `energy-in-standing-waves` | uni-lower | `standing-waves-from-superposition`, `energy-on-a-string` |
| Building periodic waves from harmonics | `fourier-synthesis-of-waves` | uni-lower | `superposing-sinusoidal-waves`, `normal-modes-of-a-string` |
| Finding harmonic amplitudes with integrals | `harmonic-amplitudes-by-integration` | uni-lower | `fourier-synthesis-of-waves`, `calc2.trig-products-different-angles` |
| Describing modes of a rectangular membrane | `membrane-modes` | uni-lower | `normal-modes-of-a-string`, `waves-in-two-and-three-dimensions` |
| Deriving beats with sum-to-product identities | `beats-with-trig-identities` | uni-lower | `superposing-sinusoidal-waves`, `hs1.beats-in-sound` |
| Describing wave packets and their spread | `wave-packets` | uni-lower | `beats-with-trig-identities`, `fourier-synthesis-of-waves` |
| Finding group and phase velocity | `group-and-phase-velocity` | uni-lower | `wave-packets`, `wave-number-and-angular-frequency` |
| Using dispersion relations | `dispersion-relations` | uni-lower | `group-and-phase-velocity` |

### Sound

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing sound as pressure and displacement waves | `sound-as-pressure-wave` | uni-lower | `wave-functions`, `hs1.sound-speed-factors` |
| Deriving the speed of sound from bulk modulus | `speed-of-sound-derivation` | uni-lower | `sound-as-pressure-wave`, `mechanics.shear-and-bulk-moduli` |
| Relating sound intensity to pressure amplitude | `sound-intensity-and-pressure` | uni-lower | `sound-as-pressure-wave`, `spherical-wave-intensity` |
| Combining sound levels in decibels | `decibel-calculations` | uni-lower | `sound-intensity-and-pressure`, `hs1.sound-intensity` |
| Finding pipe modes from boundary conditions | `pipe-modes-from-boundary-conditions` | uni-lower | `normal-modes-of-a-string`, `sound-as-pressure-wave`, `hs1.open-and-closed-pipes` |
| Deriving the Doppler effect for moving source and observer | `doppler-general` | uni-lower | `sound-as-pressure-wave`, `hs1.doppler-sound` |
| Finding Mach cone angles | `shock-waves` | uni-lower | `doppler-general` |
| Finding reflection with acoustic impedance | `acoustic-impedance` | uni-lower | `impedance-of-a-string`, `sound-as-pressure-wave` |

### Fluids

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding pressure with depth by integration | `pressure-variation-by-integration` | uni-lower | `hs1.pressure-in-fluids`, `calc1.ftc-part-2` |
| Finding pressure in an isothermal atmosphere | `pressure-in-a-compressible-atmosphere` | uni-lower | `pressure-variation-by-integration`, `calc2.exponential-growth-de` |
| Finding forces on submerged surfaces | `forces-on-dams` | uni-lower | `pressure-variation-by-integration`, `calc2.hydrostatic-force` |
| Analyzing buoyancy and floating stability | `buoyancy-and-stability` | uni-lower | `forces-on-dams`, `hs1.buoyant-force` |
| Finding the surface of a rotating fluid | `rotating-fluids` | uni-lower | `pressure-variation-by-integration`, `mechanics.rotating-frames` |
| Deriving Bernoulli's equation from work and energy | `bernoulli-derivation` | uni-lower | `hs1.bernoullis-equation`, `mechanics.work-energy-derivation` |
| Finding the time to drain a tank | `draining-tanks` | uni-lower | `bernoulli-derivation`, `calc2.separable-equations` |
| Describing viscosity and laminar flow | `viscosity` | uni-lower | `bernoulli-derivation` |
| Finding viscous flow through a pipe | `poiseuille-flow` | uni-lower | `viscosity`, `calc1.ftc-part-2` |
| Using Stokes drag and Reynolds number | `stokes-drag-and-reynolds-number` | uni-lower | `viscosity`, `mechanics.linear-drag` |
| Finding forces from surface tension | `surface-tension` | uni-lower | `pressure-variation-by-integration` |
| Finding capillary rise | `capillary-rise` | uni-lower | `surface-tension` |

### Temperature and kinetic theory

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding thermal expansion with varying coefficients | `thermal-expansion-with-calculus` | uni-lower | `hs2.thermal-expansion`, `calc1.differentials` |
| Finding thermal stress in constrained rods | `thermal-stress` | uni-lower | `thermal-expansion-with-calculus`, `mechanics.stress-and-strain` |
| Integrating heat capacity that varies with temperature | `heat-capacity-with-calculus` | uni-lower | `hs2.specific-heat`, `calc1.ftc-part-2` |
| Finding conduction through layered walls | `conduction-through-layers` | uni-lower | `hs2.conduction-rate` |
| Finding conduction through pipes and shells | `radial-conduction` | uni-lower | `conduction-through-layers`, `calc2.separable-equations` |
| Modeling cooling with differential equations | `cooling-with-differential-equations` | uni-lower | `conduction-through-layers`, `calc2.newton-cooling-de` |
| Finding net radiation between surfaces | `radiation-exchange` | uni-lower | `hs2.radiation-rate` |
| Deriving pressure from molecular collisions | `ideal-gas-microscopic-model` | uni-lower | `hs2.kinetic-theory-of-gases`, `mechanics.impulse-as-an-integral` |
| Using equipartition of energy | `equipartition` | uni-lower | `ideal-gas-microscopic-model`, `hs2.temperature-and-particle-energy` |
| Finding molar heat capacities from degrees of freedom | `heat-capacities-of-gases` | uni-lower | `equipartition`, `heat-capacity-with-calculus` |
| Explaining heat capacity of solids classically | `heat-capacity-of-solids` | uni-lower | `equipartition` |
| Using the Maxwell speed distribution | `maxwell-speed-distribution` | uni-lower | `equipartition`, `calc2.probability-density-integral` |
| Finding mean, rms and most probable speeds | `average-and-rms-speeds` | uni-lower | `maxwell-speed-distribution`, `calc3.gaussian-integral` |
| Finding mean free path and collision rate | `mean-free-path` | uni-lower | `ideal-gas-microscopic-model` |
| Describing effusion and diffusion rates | `effusion-and-diffusion` | uni-lower | `mean-free-path`, `average-and-rms-speeds` |
| Using the van der Waals equation | `real-gases` | uni-lower | `ideal-gas-microscopic-model`, `hs2.ideal-gas-law` |
| Reading phase diagrams and critical points | `phase-diagrams` | uni-lower | `real-gases`, `hs2.latent-heat` |

### First law of thermodynamics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding work as an integral of pressure | `work-as-pressure-integral` | uni-lower | `hs2.work-on-a-gas`, `calc1.definite-integral-definition` |
| Telling state functions from path functions | `state-functions-and-path-dependence` | uni-lower | `work-as-pressure-integral`, `hs2.first-law-of-thermodynamics` |
| Finding internal energy of ideal gases | `internal-energy-of-ideal-gases` | uni-lower | `heat-capacities-of-gases`, `hs2.internal-energy` |
| Analyzing isothermal processes with integrals | `isothermal-processes` | uni-lower | `work-as-pressure-integral`, `internal-energy-of-ideal-gases`, `calc1.integrate-simple-division` |
| Analyzing constant pressure and constant volume processes | `isobaric-and-isochoric-processes` | uni-lower | `work-as-pressure-integral`, `internal-energy-of-ideal-gases` |
| Deriving the relation between heat capacities | `cp-cv-relation` | uni-lower | `isobaric-and-isochoric-processes` |
| Deriving the adiabatic relation | `adiabatic-processes` | uni-lower | `cp-cv-relation`, `calc2.separable-equations` |
| Finding work in adiabatic processes | `adiabatic-work` | uni-lower | `adiabatic-processes` |
| Finding net work and heat in a cycle | `cycle-analysis` | uni-lower | `isothermal-processes`, `adiabatic-processes`, `hs2.thermal-cycles` |
| Analyzing free expansion | `free-expansion` | uni-lower | `state-functions-and-path-dependence` |
| Using enthalpy for constant pressure processes | `enthalpy` | uni-lower | `isobaric-and-isochoric-processes` |

### Second law and entropy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding efficiency of heat engines | `heat-engine-efficiency` | uni-lower | `cycle-analysis`, `hs2.heat-engines` |
| Deriving Carnot efficiency from the cycle | `carnot-cycle-derivation` | uni-lower | `heat-engine-efficiency`, `isothermal-processes`, `adiabatic-processes` |
| Analyzing Otto and Diesel cycles | `otto-and-diesel-cycles` | uni-lower | `cycle-analysis`, `adiabatic-work` |
| Finding performance of refrigerators and heat pumps | `refrigerator-performance` | uni-lower | `carnot-cycle-derivation`, `hs2.refrigerators-and-heat-pumps` |
| Linking the Kelvin and Clausius statements | `second-law-statements` | uni-lower | `carnot-cycle-derivation` |
| Defining entropy from reversible heat | `entropy-definition` | uni-lower | `carnot-cycle-derivation`, `hs2.entropy-and-second-law` |
| Finding entropy change of an ideal gas | `entropy-change-of-ideal-gas` | uni-lower | `entropy-definition`, `isothermal-processes` |
| Finding entropy change in heating and phase change | `entropy-in-heating-and-melting` | uni-lower | `entropy-definition`, `heat-capacity-with-calculus` |
| Finding entropy change in irreversible processes | `entropy-of-irreversible-processes` | uni-lower | `entropy-change-of-ideal-gas`, `free-expansion` |
| Using total entropy to judge processes | `entropy-of-the-universe` | uni-lower | `entropy-of-irreversible-processes`, `entropy-in-heating-and-melting` |
| Reading temperature-entropy diagrams | `ts-diagrams` | uni-lower | `entropy-definition`, `cycle-analysis` |
| Linking entropy to counting microstates | `microstates-and-entropy` | uni-lower | `entropy-definition`, `alg2.combinations` |
| Finding lost work and available energy | `available-work` | uni-lower | `entropy-of-the-universe` |

### Geometric optics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving reflection and refraction from least time | `fermat-principle` | uni-lower | `hs2.snells-law`, `calc1.optimization-distance-time` |
| Deriving the mirror equation with small angles | `mirror-equation-derivation` | uni-lower | `hs2.mirror-equation`, `mechanics.small-angle-approximation` |
| Finding images from one refracting surface | `refraction-at-a-spherical-surface` | uni-lower | `hs2.snells-law`, `mechanics.small-angle-approximation` |
| Deriving the lensmaker's equation | `lensmaker-equation` | uni-lower | `refraction-at-a-spherical-surface`, `hs2.thin-lens-equation` |
| Tracing images through multi-lens systems | `multiple-lens-systems` | uni-lower | `lensmaker-equation`, `hs2.lens-combinations` |
| Using ray transfer matrices | `ray-transfer-matrices` | uni-lower | `multiple-lens-systems`, `precalc.matrix-transformations` |
| Describing spherical and chromatic aberration | `aberrations` | uni-lower | `lensmaker-equation`, `hs2.dispersion-and-prisms` |
| Finding magnification of magnifiers and microscopes | `magnifiers-and-microscopes` | uni-lower | `multiple-lens-systems`, `hs2.optical-instruments` |
| Finding angular magnification of telescopes | `telescopes` | uni-lower | `multiple-lens-systems` |
| Finding minimum deviation in a prism | `prism-minimum-deviation` | uni-lower | `hs2.dispersion-and-prisms`, `hs2.snells-law` |
| Finding acceptance angle and modal spread in fibers | `fiber-acceptance-angle` | uni-lower | `hs2.optical-fibres`, `hs2.total-internal-reflection` |

### Wave optics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using Huygens' principle | `huygens-principle` | uni-lower | `waves-in-two-and-three-dimensions`, `hs2.light-as-a-wave-evidence` |
| Deriving two-slit intensity | `two-slit-intensity` | uni-lower | `superposing-sinusoidal-waves`, `hs2.double-slit` |
| Adding light waves with phasors | `phasor-addition-of-light` | uni-lower | `two-slit-intensity`, `complex-wave-notation` |
| Finding intensity from many slits | `multi-slit-intensity` | uni-lower | `phasor-addition-of-light`, `hs2.diffraction-gratings` |
| Finding resolving power of gratings | `grating-resolving-power` | uni-lower | `multi-slit-intensity` |
| Deriving single-slit intensity by integration | `single-slit-intensity` | uni-lower | `phasor-addition-of-light`, `huygens-principle`, `hs2.single-slit` |
| Combining diffraction and interference patterns | `combined-slit-patterns` | uni-lower | `single-slit-intensity`, `two-slit-intensity` |
| Using the Rayleigh criterion | `circular-aperture-and-rayleigh` | uni-lower | `single-slit-intensity`, `hs2.resolution-limit` |
| Analyzing thin films with phase changes | `thin-films-with-phase-shifts` | uni-lower | `reflection-at-a-boundary`, `hs2.thin-film-interference` |
| Using the Michelson interferometer | `michelson-interferometer` | uni-lower | `superposing-sinusoidal-waves`, `thin-films-with-phase-shifts` |
| Describing coherence length and time | `coherence` | uni-lower | `wave-packets`, `michelson-interferometer` |
| Using Bragg's law for crystal diffraction | `x-ray-diffraction` | uni-lower | `multi-slit-intensity` |
| Describing linear, circular and elliptical polarization | `polarization-states` | uni-lower | `superposing-sinusoidal-waves`, `hs2.polarization` |
| Using Malus's law with several polarizers | `malus-law-and-polarizers` | uni-lower | `polarization-states` |
| Finding Brewster's angle | `brewster-angle` | uni-lower | `polarization-states`, `hs2.snells-law` |
| Using quarter-wave and half-wave plates | `wave-plates` | uni-lower | `polarization-states` |

## physics.modern: 95 topics, budget 150 (proposed 100)

### Special relativity

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining the Michelson-Morley null result | `michelson-morley` | uni-lower | `waves-thermo-optics.michelson-interferometer`, `hs2.relativity-postulates` |
| Deriving the Lorentz transformation | `lorentz-transformation` | uni-lower | `hs2.time-dilation`, `mechanics.galilean-transformations` |
| Applying Lorentz transformations to events | `lorentz-transformation-problems` | uni-lower | `lorentz-transformation` |
| Finding simultaneity shifts with Lorentz transformations | `simultaneity-with-lorentz` | uni-lower | `lorentz-transformation-problems`, `hs2.simultaneity` |
| Deriving relativistic velocity addition | `velocity-addition` | uni-lower | `lorentz-transformation` |
| Drawing spacetime diagrams | `spacetime-diagrams` | uni-lower | `lorentz-transformation-problems` |
| Using the invariant interval | `spacetime-interval` | uni-lower | `spacetime-diagrams` |
| Finding proper time along worldlines | `proper-time` | uni-lower | `spacetime-interval` |
| Resolving the twin paradox | `twin-paradox` | uni-lower | `proper-time` |
| Deriving the relativistic Doppler effect | `relativistic-doppler` | uni-lower | `lorentz-transformation`, `waves-thermo-optics.doppler-general`, `hs2.doppler-light` |
| Defining relativistic momentum | `relativistic-momentum` | uni-lower | `velocity-addition`, `mechanics.force-as-rate-of-momentum` |
| Deriving relativistic kinetic energy | `relativistic-energy-derivation` | uni-lower | `relativistic-momentum`, `mechanics.work-energy-derivation`, `hs2.relativistic-energy` |
| Using the energy-momentum relation | `energy-momentum-relation` | uni-lower | `relativistic-energy-derivation` |
| Using four-vectors | `four-vectors` | uni-lower | `energy-momentum-relation`, `spacetime-interval` |
| Solving relativistic collisions and decays | `relativistic-collisions` | uni-lower | `energy-momentum-relation`, `four-vectors` |
| Finding threshold energies of reactions | `threshold-energy` | uni-lower | `relativistic-collisions` |
| Finding motion under a constant force relativistically | `relativistic-force` | uni-lower | `relativistic-momentum` |
| Linking electric and magnetic fields between frames | `electromagnetism-and-relativity` | uni-lower | `lorentz-transformation`, `em.field-of-moving-charge` |

### Quanta of light

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using Planck's law | `blackbody-spectrum` | uni-lower | `hs2.blackbody-radiation`, `waves-thermo-optics.radiation-exchange` |
| Deriving Wien's and Stefan's laws from Planck's law | `wien-and-stefan-from-planck` | uni-lower | `blackbody-spectrum`, `calc2.improper-infinite-limits` |
| Analyzing photoelectric data | `photoelectric-analysis` | uni-lower | `hs2.photoelectric-effect`, `hs2.stopping-potential` |
| Deriving the Compton shift | `compton-derivation` | uni-lower | `relativistic-collisions`, `hs2.compton-scattering` |
| Describing x-ray spectra and cutoff | `x-ray-production` | uni-lower | `photoelectric-analysis`, `waves-thermo-optics.x-ray-diffraction` |
| Analyzing pair production and annihilation | `pair-production-and-annihilation` | uni-lower | `energy-momentum-relation` |

### Matter waves

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using de Broglie relations relativistically | `de-broglie-relations` | uni-lower | `hs2.de-broglie-wavelength`, `energy-momentum-relation` |
| Analyzing electron diffraction by crystals | `davisson-germer` | uni-lower | `de-broglie-relations`, `waves-thermo-optics.x-ray-diffraction` |
| Building particles as wave packets | `wave-packets-for-particles` | uni-lower | `de-broglie-relations`, `waves-thermo-optics.group-and-phase-velocity` |
| Using the position-momentum uncertainty relation | `uncertainty-principle-quantified` | uni-lower | `wave-packets-for-particles`, `hs2.uncertainty-idea` |
| Using energy-time uncertainty | `energy-time-uncertainty` | uni-lower | `uncertainty-principle-quantified` |
| Interpreting two-slit experiments with single particles | `two-slit-with-particles` | uni-lower | `de-broglie-relations`, `waves-thermo-optics.two-slit-intensity` |

### Atomic models

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Analyzing Rutherford scattering | `rutherford-scattering` | uni-lower | `em.potential-of-point-charges-derivation`, `mechanics.effective-potential-orbits` |
| Deriving Bohr energy levels | `bohr-model-derivation` | uni-lower | `hs2.bohr-model`, `mechanics.circular-motion-derivation` |
| Finding levels of hydrogen-like ions | `hydrogen-like-ions` | uni-lower | `bohr-model-derivation` |
| Correcting atomic levels for reduced mass | `reduced-mass-correction` | uni-lower | `bohr-model-derivation`, `mechanics.two-body-problem` |
| Finding spectral series wavelengths | `spectral-series` | uni-lower | `bohr-model-derivation`, `hs2.hydrogen-spectrum` |
| Interpreting the Franck-Hertz experiment | `franck-hertz` | uni-lower | `bohr-model-derivation`, `hs2.energy-level-diagrams` |
| Explaining limits of the Bohr model | `bohr-model-limits` | uni-lower | `bohr-model-derivation`, `uncertainty-principle-quantified` |

### Schrodinger equation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Interpreting wave functions as probability amplitudes | `wave-function-and-probability` | uni-lower | `de-broglie-relations`, `calc2.probability-density-integral` |
| Normalizing wave functions | `normalization` | uni-lower | `wave-function-and-probability`, `calc2.improper-infinite-limits` |
| Writing the time-dependent Schrodinger equation | `schrodinger-equation-time-dependent` | uni-lower | `wave-function-and-probability`, `waves-thermo-optics.complex-wave-notation`, `waves-thermo-optics.wave-equation-one-dimension` |
| Separating time to get stationary states | `separation-into-stationary-states` | uni-lower | `schrodinger-equation-time-dependent`, `calc2.separable-equations` |
| Solving the time-independent equation for free particles | `time-independent-equation` | uni-lower | `separation-into-stationary-states` |
| Finding expectation values of position | `expectation-values` | uni-lower | `normalization` |
| Finding momentum expectation with an operator | `momentum-operator` | uni-lower | `expectation-values`, `time-independent-equation` |
| Solving the infinite square well | `infinite-square-well` | uni-lower | `time-independent-equation`, `normalization`, `waves-thermo-optics.normal-modes-of-a-string` |
| Finding expectation values in a square well | `square-well-expectation-values` | uni-lower | `infinite-square-well`, `expectation-values`, `calc2.integration-by-parts` |
| Evolving superpositions of stationary states | `superposition-of-states` | uni-lower | `infinite-square-well`, `separation-into-stationary-states` |
| Finding bound states of a finite well graphically | `finite-square-well` | uni-lower | `infinite-square-well` |
| Finding reflection at a potential step | `step-potential` | uni-lower | `time-independent-equation`, `waves-thermo-optics.reflection-at-a-boundary` |
| Finding tunneling probability through a barrier | `barrier-tunneling` | uni-lower | `step-potential`, `calc2.hyperbolic-definitions` |
| Explaining alpha decay and tunneling microscopes | `tunneling-applications` | uni-lower | `barrier-tunneling`, `hs2.alpha-beta-gamma` |
| Checking the oscillator ground state | `harmonic-oscillator-ground-state` | uni-lower | `time-independent-equation`, `mechanics.shm-differential-equation`, `calc3.gaussian-integral` |
| Using oscillator energy levels | `oscillator-energy-levels` | uni-lower | `harmonic-oscillator-ground-state` |
| Solving the three-dimensional box and degeneracy | `three-dimensional-box` | uni-lower | `infinite-square-well`, `calc3.partial-derivatives-compute` |

### Hydrogen and atoms

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing hydrogen solutions and quantum numbers | `hydrogen-schrodinger-overview` | uni-lower | `three-dimensional-box`, `bohr-model-derivation`, `calc3.spherical-coordinates` |
| Checking the hydrogen ground state | `hydrogen-ground-state` | uni-lower | `hydrogen-schrodinger-overview`, `calc3.triple-spherical` |
| Finding radial probability distributions | `radial-probability` | uni-lower | `hydrogen-ground-state` |
| Using quantized orbital angular momentum | `orbital-angular-momentum-quantization` | uni-lower | `hydrogen-schrodinger-overview`, `mechanics.angular-momentum-of-a-particle` |
| Finding normal Zeeman splitting | `zeeman-effect-normal` | uni-lower | `orbital-angular-momentum-quantization`, `em.torque-and-energy-of-a-loop` |
| Interpreting Stern-Gerlach and electron spin | `stern-gerlach-and-spin` | uni-lower | `zeeman-effect-normal`, `em.magnetic-dipole-moment` |
| Describing fine structure from spin-orbit coupling | `spin-orbit-overview` | uni-lower | `stern-gerlach-and-spin` |
| Using the exclusion principle | `pauli-exclusion` | uni-lower | `stern-gerlach-and-spin` |
| Explaining shell structure of many-electron atoms | `multi-electron-atoms` | uni-lower | `pauli-exclusion`, `hydrogen-schrodinger-overview` |
| Using Moseley's law for x-ray lines | `x-ray-spectra-and-moseley` | uni-lower | `multi-electron-atoms`, `x-ray-production` |
| Using selection rules for transitions | `selection-rules-and-transitions` | uni-lower | `orbital-angular-momentum-quantization`, `spectral-series` |
| Explaining stimulated emission and population inversion | `laser-principles` | uni-lower | `selection-rules-and-transitions`, `hs2.lasers` |

### Molecules and solids

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding molecular rotational energy levels | `molecular-rotation-spectra` | uni-lower | `orbital-angular-momentum-quantization`, `mechanics.inertia-of-point-masses` |
| Finding molecular vibrational levels | `molecular-vibration-spectra` | uni-lower | `oscillator-energy-levels`, `mechanics.small-oscillations-about-equilibrium` |
| Using the free electron model of metals | `free-electron-model` | uni-lower | `three-dimensional-box`, `pauli-exclusion` |
| Finding the Fermi energy of metals | `fermi-energy` | uni-lower | `free-electron-model` |
| Explaining energy bands in solids | `band-theory` | uni-lower | `free-electron-model`, `finite-square-well` |
| Telling conductors, insulators and semiconductors by bands | `band-classification-of-solids` | uni-lower | `band-theory` |
| Describing n-type and p-type semiconductors | `doped-semiconductors` | uni-lower | `band-classification-of-solids` |
| Explaining diodes from p-n junctions | `pn-junctions` | uni-lower | `doped-semiconductors` |
| Describing superconductivity | `superconductivity-overview` | uni-lower | `band-classification-of-solids` |

### Nuclear physics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding nuclear radius and density | `nuclear-size-and-density` | uni-lower | `rutherford-scattering`, `hs2.nuclear-notation` |
| Finding binding energy from atomic masses | `binding-energy-from-masses` | uni-lower | `energy-momentum-relation`, `hs2.binding-energy` |
| Using the semi-empirical mass formula | `semi-empirical-mass-formula` | uni-lower | `binding-energy-from-masses`, `hs2.binding-energy-curve` |
| Deriving the radioactive decay law | `decay-law-derivation` | uni-lower | `hs2.half-life`, `calc2.exponential-growth-de` |
| Solving parent-daughter decay chains | `decay-chains-with-equations` | uni-lower | `decay-law-derivation`, `hs2.decay-chains` |
| Finding Q values of decays | `q-values-of-decays` | uni-lower | `binding-energy-from-masses`, `hs2.decay-equations` |
| Finding alpha particle energies from recoil | `alpha-decay-energetics` | uni-lower | `q-values-of-decays`, `mechanics.momentum-of-particle-systems` |
| Explaining beta spectra and neutrinos | `beta-decay-and-neutrinos` | uni-lower | `q-values-of-decays` |
| Describing gamma transitions and isomers | `gamma-decay` | uni-lower | `q-values-of-decays` |
| Using cross sections for nuclear reactions | `nuclear-reactions-and-cross-sections` | uni-lower | `q-values-of-decays`, `threshold-energy` |
| Finding energy released in fission | `fission-energetics` | uni-lower | `semi-empirical-mass-formula`, `hs2.fission` |
| Using the multiplication factor in chain reactions | `chain-reactions` | uni-lower | `fission-energetics`, `hs2.nuclear-reactors` |
| Finding fusion energy and the Coulomb barrier | `fusion-energetics` | uni-lower | `binding-energy-from-masses`, `em.potential-of-point-charges-derivation`, `hs2.fusion` |
| Finding attenuation of radiation in matter | `radiation-attenuation` | uni-lower | `decay-law-derivation`, `hs2.radiation-dose` |

### Particles

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Classifying leptons, hadrons and bosons | `particle-classification` | uni-lower | `hs2.particles-intro` |
| Using conservation laws in particle reactions | `conservation-laws-in-reactions` | uni-lower | `particle-classification` |
| Building hadrons from quarks | `quark-model` | uni-lower | `particle-classification` |
| Comparing the four interactions and their carriers | `fundamental-interactions` | uni-lower | `quark-model`, `energy-time-uncertainty` |
| Reading simple Feynman diagrams | `feynman-diagrams-intro` | uni-lower | `fundamental-interactions` |
| Finding energies in accelerators and detectors | `accelerators-and-detectors` | uni-lower | `threshold-energy`, `em.cyclotrons` |

## physics.classical: 90 topics, budget 160 (proposed 95)

### Newtonian tools

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing motion in polar coordinates | `motion-in-polar-coordinates` | uni-upper | `mechanics.velocity-vector-derivative`, `calc2.polar-derivatives` |
| Writing velocity in cylindrical and spherical coordinates | `motion-in-spherical-coordinates` | uni-upper | `motion-in-polar-coordinates`, `calc3.spherical-coordinates` |
| Solving two-dimensional projectiles with linear drag | `drag-with-differential-equations` | uni-upper | `mechanics.linear-drag`, `diffeq.linear-first-order` |
| Testing forces for potentials in three dimensions | `energy-in-three-dimensions` | uni-upper | `mechanics.conservative-forces`, `calc3.conservative-test` |
| Solving one-dimensional motion from energy by integration | `one-dimensional-motion-by-quadrature` | uni-upper | `mechanics.energy-diagrams-with-calculus`, `diffeq.separable-odes` |

### Oscillations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving oscillators with complex exponentials | `oscillators-with-complex-exponentials` | uni-upper | `mechanics.damped-oscillator-equation`, `diffeq.constant-coefficients-complex` |
| Finding steady state with complex amplitudes | `driven-damped-steady-state` | uni-upper | `oscillators-with-complex-exponentials`, `diffeq.steady-transient` |
| Driving oscillators with periodic forces by Fourier series | `fourier-series-driving` | uni-upper | `driven-damped-steady-state`, `diffeq.fourier-series-intro` |
| Finding oscillator response to impulses and arbitrary forces | `impulse-response` | uni-upper | `driven-damped-steady-state`, `diffeq.convolution` |
| Drawing phase-space trajectories | `phase-space-of-oscillators` | uni-upper | `oscillators-with-complex-exponentials`, `diffeq.phase-portraits-complex` |
| Finding frequency shifts of anharmonic oscillators | `anharmonic-oscillators` | uni-upper | `oscillators-with-complex-exponentials`, `calc2.taylor-series` |

### Calculus of variations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Setting up functionals for path problems | `functionals-and-variations` | uni-upper | `calc2.arc-length-integral`, `calc3.partial-derivatives-compute` |
| Deriving the Euler-Lagrange equation | `euler-lagrange-equation` | uni-upper | `functionals-and-variations`, `calc2.integration-by-parts` |
| Solving shortest path and geodesic problems | `shortest-path-problems` | uni-upper | `euler-lagrange-equation` |
| Solving the brachistochrone | `brachistochrone` | uni-upper | `euler-lagrange-equation`, `calc2.parametric-derivatives` |
| Using first integrals when the integrand lacks the variable | `first-integrals-beltrami` | uni-upper | `euler-lagrange-equation` |
| Finding the hanging chain and soap-film surface | `minimal-surfaces-and-catenary` | uni-upper | `first-integrals-beltrami`, `calc2.catenary` |
| Extending variations to several functions | `several-dependent-variables` | uni-upper | `euler-lagrange-equation` |
| Using multipliers in variational problems | `constrained-variations` | uni-upper | `several-dependent-variables`, `calc3.lagrange-three-variables` |

### Lagrangian mechanics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing generalized coordinates and constraints | `generalized-coordinates` | uni-upper | `mechanics.systems-with-constraints`, `several-dependent-variables` |
| Stating Hamilton's principle | `hamiltons-principle` | uni-upper | `euler-lagrange-equation`, `mechanics.potential-from-force` |
| Deriving equations of motion with Lagrange's equations | `lagranges-equations` | uni-upper | `hamiltons-principle`, `generalized-coordinates` |
| Writing Lagrangians for pendulum systems | `lagrangian-for-pendulums` | uni-upper | `lagranges-equations`, `mechanics.pendulum-derivation` |
| Deriving equations for a double pendulum | `double-pendulum` | uni-upper | `lagrangian-for-pendulums` |
| Writing Lagrangians for beads and rotating systems | `lagrangian-in-rotating-systems` | uni-upper | `lagranges-equations`, `mechanics.rotating-frames` |
| Handling moving supports and time-dependent constraints | `moving-supports` | uni-upper | `lagranges-equations` |
| Using cyclic coordinates and generalized momenta | `cyclic-coordinates` | uni-upper | `lagranges-equations` |
| Finding the energy function and when it is conserved | `energy-function` | uni-upper | `cyclic-coordinates` |
| Linking symmetries to conservation laws | `noether-theorem` | uni-upper | `cyclic-coordinates` |
| Finding constraint forces with multipliers | `constraint-forces-with-multipliers` | uni-upper | `lagranges-equations`, `constrained-variations` |
| Recognizing nonholonomic constraints | `nonholonomic-constraints` | uni-upper | `constraint-forces-with-multipliers` |
| Finding equilibria and stability from the Lagrangian | `equilibrium-and-stability-lagrangian` | uni-upper | `lagranges-equations`, `mechanics.equilibrium-from-potential` |
| Finding small oscillation frequencies from a Lagrangian | `small-oscillations-lagrangian` | uni-upper | `equilibrium-and-stability-lagrangian`, `calc2.taylor-series` |

### Central forces

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reducing the two-body problem with a Lagrangian | `reduced-two-body-lagrangian` | uni-upper | `lagranges-equations`, `mechanics.two-body-problem` |
| Deriving radial and angular equations | `central-force-equations` | uni-upper | `reduced-two-body-lagrangian`, `cyclic-coordinates` |
| Classifying orbits with the effective potential | `effective-potential-analysis` | uni-upper | `central-force-equations`, `mechanics.effective-potential-orbits` |
| Deriving the orbit equation in inverse radius | `orbit-equation` | uni-upper | `central-force-equations`, `diffeq.undetermined-coefficients-poly-exp` |
| Deriving conic orbits for inverse-square forces | `kepler-orbits-from-orbit-equation` | uni-upper | `orbit-equation`, `calc2.conics-with-calculus` |
| Deriving Kepler's third law for elliptical orbits | `kepler-third-law-derivation` | uni-upper | `kepler-orbits-from-orbit-equation` |
| Finding orbit changes from impulses | `orbital-maneuvers` | uni-upper | `kepler-orbits-from-orbit-equation`, `mechanics.transfer-orbits` |
| Testing stability of circular orbits | `stability-of-circular-orbits` | uni-upper | `effective-potential-analysis` |
| Finding precession for nearly inverse-square forces | `precession-of-orbits` | uni-upper | `stability-of-circular-orbits`, `orbit-equation` |
| Using the Laplace-Runge-Lenz vector | `laplace-runge-lenz` | uni-upper | `kepler-orbits-from-orbit-equation`, `mechanics.cross-product-in-physics` |
| Defining differential cross sections | `scattering-cross-sections` | uni-upper | `effective-potential-analysis` |
| Deriving the Rutherford cross section | `rutherford-cross-section` | uni-upper | `scattering-cross-sections`, `kepler-orbits-from-orbit-equation` |
| Finding hard-sphere cross sections | `hard-sphere-scattering` | uni-upper | `scattering-cross-sections` |

### Noninertial frames

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving velocity and acceleration in rotating frames | `rotating-frame-transformation` | uni-upper | `mechanics.rotating-frames`, `mechanics.angular-velocity-vectors` |
| Finding fictitious forces in rotating frames | `centrifugal-and-coriolis-forces` | uni-upper | `rotating-frame-transformation`, `mechanics.coriolis-effect` |
| Analyzing the Foucault pendulum | `foucault-pendulum` | uni-upper | `centrifugal-and-coriolis-forces`, `mechanics.pendulum-derivation` |
| Finding deflection in free fall on Earth | `free-fall-on-rotating-earth` | uni-upper | `centrifugal-and-coriolis-forces` |
| Explaining tidal forces | `tides` | uni-upper | `mechanics.gravitation-in-vector-form`, `calc2.binomial-series` |

### Rigid bodies

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using rotation matrices for rigid bodies | `rotation-matrices` | uni-upper | `linalg.geometric-transformations-matrices`, `mechanics.angular-velocity-vectors` |
| Computing the inertia tensor | `inertia-tensor` | uni-upper | `mechanics.inertia-of-composite-bodies`, `linalg.matrix-as-transformation`, `calc3.change-of-variables-triple` |
| Finding angular momentum from the inertia tensor | `angular-momentum-with-inertia-tensor` | uni-upper | `inertia-tensor`, `mechanics.angular-momentum-of-systems` |
| Finding principal axes as eigenvectors | `principal-axes` | uni-upper | `inertia-tensor`, `linalg.spectral-theorem` |
| Finding kinetic energy with the inertia tensor | `rotational-energy-with-tensor` | uni-upper | `angular-momentum-with-inertia-tensor` |
| Shifting the inertia tensor to a new origin | `inertia-tensor-shifts` | uni-upper | `inertia-tensor`, `mechanics.parallel-axis-theorem` |
| Deriving Euler's equations for rigid bodies | `euler-equations` | uni-upper | `angular-momentum-with-inertia-tensor`, `principal-axes`, `rotating-frame-transformation` |
| Solving torque-free motion of a symmetric body | `torque-free-symmetric-top` | uni-upper | `euler-equations` |
| Testing stability of rotation about principal axes | `stability-of-rotation-axes` | uni-upper | `euler-equations` |
| Describing orientation with Euler angles | `euler-angles` | uni-upper | `rotation-matrices` |
| Analyzing a heavy symmetric top with a Lagrangian | `heavy-symmetric-top` | uni-upper | `euler-angles`, `lagranges-equations`, `torque-free-symmetric-top` |
| Finding precession and nutation of a top | `nutation-and-precession` | uni-upper | `heavy-symmetric-top`, `mechanics.precession` |

### Coupled oscillations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing coupled oscillators in matrix form | `coupled-oscillator-matrices` | uni-upper | `mechanics.coupled-oscillators`, `small-oscillations-lagrangian`, `diffeq.matrix-form-systems` |
| Finding normal modes as an eigenvalue problem | `normal-modes-by-eigenvalues` | uni-upper | `coupled-oscillator-matrices`, `linalg.find-eigenvectors` |
| Changing to normal coordinates | `normal-coordinates` | uni-upper | `normal-modes-by-eigenvalues`, `linalg.diagonalization` |
| Analyzing weak coupling and energy exchange | `weak-coupling-and-energy-exchange` | uni-upper | `normal-modes-by-eigenvalues` |
| Finding the response of driven coupled systems | `driven-coupled-oscillators` | uni-upper | `normal-coordinates`, `driven-damped-steady-state` |
| Finding modes of three-mass chains and molecules | `three-mass-chains` | uni-upper | `normal-modes-by-eigenvalues` |
| Recognizing zero-frequency modes | `zero-frequency-modes` | uni-upper | `normal-modes-by-eigenvalues` |
| Taking a chain of masses to a continuous string | `loaded-string-continuum-limit` | uni-upper | `three-mass-chains`, `diffeq.boundary-value-eigenproblems` |
| Writing a Lagrangian density for a string | `lagrangian-density-string` | uni-upper | `loaded-string-continuum-limit`, `hamiltons-principle` |

### Hamiltonian mechanics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using the Legendre transformation | `legendre-transform` | uni-upper | `cyclic-coordinates`, `calc3.partial-derivatives-compute` |
| Building the Hamiltonian from the Lagrangian | `hamiltonian-function` | uni-upper | `legendre-transform`, `energy-function` |
| Solving problems with Hamilton's equations | `hamiltons-equations` | uni-upper | `hamiltonian-function` |
| Writing Hamiltonians for central forces | `hamiltonian-for-central-forces` | uni-upper | `hamiltons-equations`, `central-force-equations` |
| Using phase space and Liouville's theorem | `phase-space-and-liouville` | uni-upper | `hamiltons-equations`, `phase-space-of-oscillators`, `calc3.divergence` |
| Computing Poisson brackets | `poisson-brackets` | uni-upper | `hamiltons-equations` |
| Finding conserved quantities with Poisson brackets | `conserved-quantities-from-brackets` | uni-upper | `poisson-brackets`, `noether-theorem` |
| Testing canonical transformations | `canonical-transformations` | uni-upper | `poisson-brackets` |
| Using generating functions for canonical transformations | `canonical-generating-functions` | uni-upper | `canonical-transformations` |
| Solving problems with the Hamilton-Jacobi equation | `hamilton-jacobi-equation` | uni-upper | `canonical-generating-functions` |
| Using action-angle variables | `action-angle-variables` | uni-upper | `hamilton-jacobi-equation` |
| Using adiabatic invariants | `adiabatic-invariants` | uni-upper | `action-angle-variables` |

### Nonlinear dynamics and chaos

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing chaos in a driven damped pendulum | `driven-damped-pendulum-chaos` | uni-upper | `diffeq.nonlinear-pendulum`, `diffeq.bifurcations-intro`, `driven-damped-steady-state` |
| Recognizing period doubling routes to chaos | `period-doubling` | uni-upper | `driven-damped-pendulum-chaos` |
| Iterating the logistic map | `logistic-map` | uni-upper | `period-doubling`, `calc2.recursive-sequence-limits` |
| Estimating Lyapunov exponents | `lyapunov-exponents` | uni-upper | `driven-damped-pendulum-chaos`, `logistic-map` |
| Reading Poincare sections | `poincare-sections` | uni-upper | `driven-damped-pendulum-chaos`, `phase-space-of-oscillators` |
| Describing strange attractors and fractal dimension | `strange-attractors` | uni-upper | `poincare-sections` |

## physics.em-theory: 98 topics, budget 170 (proposed 100)

### Vector calculus for fields

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using gradient, divergence and curl in curvilinear coordinates | `curvilinear-vector-derivatives` | uni-upper | `calc3.curl`, `calc3.spherical-coordinates` |
| Using the three-dimensional delta function | `dirac-delta-in-three-dimensions` | uni-upper | `pde.delta-function-pde`, `calc3.divergence-theorem` |
| Finding the divergence of a point-charge field | `divergence-of-inverse-square-field` | uni-upper | `dirac-delta-in-three-dimensions`, `curvilinear-vector-derivatives` |
| Stating the Helmholtz theorem | `helmholtz-theorem` | uni-upper | `curvilinear-vector-derivatives`, `calc3.curl-divergence-identities` |
| Using product rules for vector derivatives | `vector-identities-for-fields` | uni-upper | `calc3.curl-divergence-identities` |

### Electrostatics formalism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving Gauss's law in differential form | `differential-gauss-law` | uni-upper | `em.gauss-law-statement`, `divergence-of-inverse-square-field` |
| Showing electrostatic fields are curl-free | `curl-of-electrostatic-field` | uni-upper | `em.potential-as-a-line-integral`, `calc3.stokes-theorem` |
| Deriving Poisson's and Laplace's equations | `poisson-and-laplace-equations` | uni-upper | `differential-gauss-law`, `curl-of-electrostatic-field`, `pde.poisson-equation` |
| Finding potentials of volume charge distributions | `potential-of-continuous-distributions` | uni-upper | `em.potential-of-a-ring-and-disk`, `calc3.triple-spherical` |
| Deriving boundary conditions at surface charges | `boundary-conditions-on-fields` | uni-upper | `differential-gauss-law`, `curl-of-electrostatic-field` |
| Finding electrostatic energy from fields | `electrostatic-energy-in-fields` | uni-upper | `em.energy-density-of-electric-field`, `poisson-and-laplace-equations` |
| Finding surface charge and pressure on conductors | `conductors-and-surface-pressure` | uni-upper | `boundary-conditions-on-fields`, `em.conductors-with-gauss` |
| Using uniqueness theorems | `uniqueness-theorems` | uni-upper | `poisson-and-laplace-equations`, `pde.uniqueness-laplace` |

### Boundary-value problems

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving a charge near a grounded plane by images | `method-of-images-plane` | uni-upper | `uniqueness-theorems` |
| Finding induced charge and force from images | `induced-charge-and-force-images` | uni-upper | `method-of-images-plane` |
| Solving a charge near a grounded sphere by images | `method-of-images-sphere` | uni-upper | `method-of-images-plane` |
| Solving Laplace's equation in Cartesian coordinates | `separation-cartesian` | uni-upper | `uniqueness-theorems`, `pde.laplace-rectangle` |
| Solving azimuthally symmetric problems with Legendre polynomials | `separation-spherical-legendre` | uni-upper | `uniqueness-theorems`, `pde.spherical-laplace`, `pde.legendre-expansions` |
| Finding fields of a conducting sphere in a uniform field | `sphere-in-uniform-field` | uni-upper | `separation-spherical-legendre` |
| Solving Laplace's equation in cylindrical coordinates | `separation-cylindrical` | uni-upper | `uniqueness-theorems`, `pde.cylindrical-laplace` |
| Solving Laplace's equation numerically by relaxation | `relaxation-method` | uni-upper | `separation-cartesian`, `pde.mean-value-maximum-laplace` |
| Using Green's functions for boundary problems | `greens-function-electrostatics` | uni-upper | `method-of-images-sphere`, `pde.greens-functions` |

### Multipoles

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Expanding potentials in multipoles | `multipole-expansion` | uni-upper | `separation-spherical-legendre`, `calc2.binomial-series` |
| Finding monopole and dipole terms | `monopole-and-dipole-terms` | uni-upper | `multipole-expansion` |
| Finding how the dipole moment depends on origin | `dipole-moment-origin-dependence` | uni-upper | `monopole-and-dipole-terms` |
| Writing the dipole field in coordinate-free form | `dipole-field-coordinate-free` | uni-upper | `monopole-and-dipole-terms`, `em.electric-dipole-field` |
| Finding quadrupole terms | `quadrupole-terms` | uni-upper | `multipole-expansion` |

### Electric fields in matter

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding bound charges from polarization | `polarization-and-bound-charge` | uni-upper | `em.polarization-microscopic`, `differential-gauss-law` |
| Using the displacement field | `displacement-field` | uni-upper | `polarization-and-bound-charge` |
| Solving linear dielectric problems | `linear-dielectrics` | uni-upper | `displacement-field`, `em.gauss-with-dielectrics` |
| Applying boundary conditions at dielectric interfaces | `dielectric-boundary-conditions` | uni-upper | `displacement-field`, `boundary-conditions-on-fields` |
| Finding fields of a dielectric sphere in a uniform field | `dielectric-sphere-in-field` | uni-upper | `dielectric-boundary-conditions`, `sphere-in-uniform-field` |
| Finding energy and forces in dielectric systems | `energy-and-forces-in-dielectrics` | uni-upper | `linear-dielectrics`, `em.force-on-capacitor-plates` |
| Linking molecular polarizability to susceptibility | `clausius-mossotti` | uni-upper | `linear-dielectrics` |

### Magnetostatics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using volume and surface current densities | `volume-and-surface-currents` | uni-upper | `em.current-density` |
| Deriving charge conservation in differential form | `continuity-equation-charge` | uni-upper | `volume-and-surface-currents`, `calc3.divergence-theorem` |
| Finding divergence and curl of magnetic fields | `divergence-and-curl-of-b` | uni-upper | `em.amperes-law-statement`, `em.biot-savart-law`, `calc3.stokes-theorem` |
| Using Ampere's law in differential form | `differential-ampere-law` | uni-upper | `divergence-and-curl-of-b` |
| Finding the magnetic vector potential | `vector-potential` | uni-upper | `differential-ampere-law`, `helmholtz-theorem` |
| Finding vector potentials of wires, solenoids and spheres | `vector-potential-examples` | uni-upper | `vector-potential` |
| Deriving magnetic boundary conditions | `magnetic-boundary-conditions` | uni-upper | `divergence-and-curl-of-b`, `boundary-conditions-on-fields` |
| Finding the magnetic dipole term of the vector potential | `magnetic-dipole-term` | uni-upper | `vector-potential`, `multipole-expansion` |
| Finding forces and torques on magnetic dipoles | `forces-and-torques-on-magnetic-dipoles` | uni-upper | `magnetic-dipole-term`, `em.torque-and-energy-of-a-loop` |
| Finding fields of a spinning charged sphere | `spinning-charged-sphere` | uni-upper | `vector-potential-examples`, `separation-spherical-legendre` |

### Magnetic fields in matter

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding bound currents from magnetization | `magnetization-and-bound-currents` | uni-upper | `magnetic-dipole-term`, `em.magnetic-materials` |
| Using the H field | `h-field` | uni-upper | `magnetization-and-bound-currents`, `differential-ampere-law` |
| Solving problems with linear magnetic media | `linear-magnetic-media` | uni-upper | `h-field` |
| Applying boundary conditions in magnetic media | `magnetic-media-boundary-conditions` | uni-upper | `h-field`, `magnetic-boundary-conditions` |
| Describing ferromagnetism and hysteresis quantitatively | `ferromagnetism-and-hysteresis` | uni-upper | `linear-magnetic-media` |
| Analyzing magnetic circuits with cores | `magnetic-circuits` | uni-upper | `linear-magnetic-media` |

### Electrodynamics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using Ohm's law in local form with emf | `local-ohms-law-and-emf` | uni-upper | `em.microscopic-ohms-law` |
| Deriving Faraday's law in differential form | `differential-faraday-law` | uni-upper | `em.faraday-with-derivatives`, `calc3.stokes-theorem` |
| Writing Maxwell's equations in differential form | `maxwell-equations-differential` | uni-upper | `differential-faraday-law`, `differential-ampere-law`, `continuity-equation-charge`, `em.displacement-current` |
| Writing Maxwell's equations in matter | `maxwell-equations-in-matter` | uni-upper | `maxwell-equations-differential`, `displacement-field`, `h-field` |
| Using general electrodynamic boundary conditions | `boundary-conditions-general` | uni-upper | `maxwell-equations-in-matter`, `dielectric-boundary-conditions`, `magnetic-media-boundary-conditions` |
| Solving quasistatic induction problems | `quasistatic-induction-problems` | uni-upper | `differential-faraday-law`, `vector-potential-examples` |

### Conservation laws

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving Poynting's theorem | `poynting-theorem` | uni-upper | `maxwell-equations-differential`, `em.poynting-vector`, `vector-identities-for-fields` |
| Finding forces with the Maxwell stress tensor | `maxwell-stress-tensor` | uni-upper | `poynting-theorem` |
| Finding momentum stored in fields | `field-momentum` | uni-upper | `maxwell-stress-tensor` |
| Finding angular momentum stored in fields | `field-angular-momentum` | uni-upper | `field-momentum` |

### Electromagnetic waves

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving wave equations from Maxwell's equations | `wave-equation-from-maxwell` | uni-upper | `maxwell-equations-differential`, `pde.deriving-wave-equation` |
| Writing monochromatic plane waves with complex notation | `complex-plane-waves` | uni-upper | `wave-equation-from-maxwell`, `waves-thermo-optics.complex-wave-notation` |
| Describing polarization of electromagnetic waves | `polarization-of-em-waves` | uni-upper | `complex-plane-waves`, `waves-thermo-optics.polarization-states` |
| Finding energy and momentum of plane waves | `energy-momentum-of-em-waves` | uni-upper | `complex-plane-waves`, `poynting-theorem` |
| Finding waves in linear media | `waves-in-linear-media` | uni-upper | `complex-plane-waves`, `maxwell-equations-in-matter` |
| Finding reflection and transmission at normal incidence | `normal-incidence-reflection` | uni-upper | `waves-in-linear-media`, `boundary-conditions-general` |
| Deriving Fresnel equations at oblique incidence | `fresnel-equations` | uni-upper | `normal-incidence-reflection` |
| Explaining Brewster's angle and evanescent waves from Fresnel equations | `brewster-and-evanescent-waves` | uni-upper | `fresnel-equations`, `waves-thermo-optics.brewster-angle` |
| Finding skin depth in conductors | `waves-in-conductors` | uni-upper | `waves-in-linear-media`, `local-ohms-law-and-emf` |
| Finding reflection from conducting surfaces | `reflection-from-conductors` | uni-upper | `waves-in-conductors`, `normal-incidence-reflection` |
| Modeling frequency-dependent permittivity | `dispersion-in-dielectrics` | uni-upper | `waves-in-linear-media`, `mechanics.driven-oscillator` |
| Finding the plasma frequency and cutoff | `plasma-frequency` | uni-upper | `dispersion-in-dielectrics` |
| Finding modes of rectangular waveguides | `rectangular-waveguides` | uni-upper | `waves-in-conductors`, `separation-cartesian` |
| Finding cutoff frequencies and group velocity in guides | `waveguide-cutoff-and-group-velocity` | uni-upper | `rectangular-waveguides`, `waves-thermo-optics.group-and-phase-velocity` |
| Finding TEM waves in coaxial lines | `coaxial-transmission-lines` | uni-upper | `rectangular-waveguides`, `em.inductance-of-coax-and-toroid` |
| Finding modes of resonant cavities | `resonant-cavities` | uni-upper | `rectangular-waveguides` |

### Potentials and fields

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing fields from dynamic potentials | `dynamic-potentials` | uni-upper | `maxwell-equations-differential`, `vector-potential` |
| Using Coulomb and Lorenz gauges | `gauge-transformations` | uni-upper | `dynamic-potentials` |
| Using retarded potentials | `retarded-potentials` | uni-upper | `gauge-transformations` |
| Stating Jefimenko's equations | `jefimenko-equations` | uni-upper | `retarded-potentials` |
| Deriving Lienard-Wiechert potentials | `lienard-wiechert-potentials` | uni-upper | `retarded-potentials` |
| Finding fields of an accelerating point charge | `fields-of-an-accelerating-charge` | uni-upper | `lienard-wiechert-potentials` |
| Finding the relativistic field of a charge at constant velocity | `uniformly-moving-charge-field` | uni-upper | `fields-of-an-accelerating-charge` |

### Radiation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding fields of electric dipole radiation | `electric-dipole-radiation` | uni-upper | `retarded-potentials`, `multipole-expansion` |
| Finding radiated power and angular pattern | `radiated-power-and-pattern` | uni-upper | `electric-dipole-radiation`, `poynting-theorem` |
| Finding magnetic dipole radiation | `magnetic-dipole-radiation` | uni-upper | `electric-dipole-radiation`, `magnetic-dipole-term` |
| Deriving the Larmor formula | `larmor-formula` | uni-upper | `fields-of-an-accelerating-charge`, `radiated-power-and-pattern` |
| Describing radiation reaction | `radiation-reaction` | uni-upper | `larmor-formula` |
| Finding radiation resistance of antennas | `radiation-resistance` | uni-upper | `radiated-power-and-pattern`, `em.antennas-intro` |
| Explaining Rayleigh scattering and the blue sky | `rayleigh-scattering` | uni-upper | `electric-dipole-radiation`, `dispersion-in-dielectrics` |
| Describing synchrotron and bremsstrahlung radiation | `synchrotron-and-bremsstrahlung` | uni-upper | `larmor-formula`, `modern.relativistic-momentum` |

### Relativistic electrodynamics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Transforming electric and magnetic fields between frames | `field-transformations` | uni-upper | `modern.lorentz-transformation`, `modern.electromagnetism-and-relativity`, `uniformly-moving-charge-field` |
| Deriving magnetic force from relativity | `magnetism-as-relativistic-effect` | uni-upper | `field-transformations` |
| Using the four-current and four-potential | `four-current-and-four-potential` | uni-upper | `modern.four-vectors`, `gauge-transformations`, `continuity-equation-charge` |
| Writing the electromagnetic field tensor | `field-tensor` | uni-upper | `four-current-and-four-potential`, `field-transformations` |
| Writing Maxwell's equations in tensor form | `covariant-maxwell-equations` | uni-upper | `field-tensor` |
| Solving relativistic motion of charges in fields | `relativistic-particle-in-fields` | uni-upper | `modern.relativistic-force`, `em.lorentz-force` |
| Using invariants of the electromagnetic field | `field-invariants` | uni-upper | `field-tensor` |

## physics.quantum: 89 topics, budget 180 (proposed 95)

### Wave mechanics foundations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing the Schrodinger equation with operators | `operators-in-wave-mechanics` | uni-upper | `modern.momentum-operator`, `modern.schrodinger-equation-time-dependent` |
| Finding probability current | `probability-current` | uni-upper | `operators-in-wave-mechanics` |
| Using Ehrenfest's theorem | `ehrenfest-theorem` | uni-upper | `operators-in-wave-mechanics`, `modern.expectation-values` |
| Expanding states in stationary states | `stationary-state-expansion` | uni-upper | `modern.superposition-of-states`, `pde.eigenfunction-expansions` |
| Finding momentum-space wave functions | `momentum-space-wave-functions` | uni-upper | `modern.wave-packets-for-particles`, `pde.fourier-transform-definition` |
| Finding the spread of a free Gaussian packet | `gaussian-packet-spreading` | uni-upper | `momentum-space-wave-functions`, `calc3.gaussian-integral` |
| Solving the delta function potential | `delta-function-potential` | uni-upper | `modern.finite-square-well`, `pde.delta-function-pde` |
| Finding transmission for wells and barriers | `scattering-states-and-transmission` | uni-upper | `modern.barrier-tunneling`, `probability-current` |
| Solving the finite well exactly | `finite-well-exact` | uni-upper | `modern.finite-square-well` |
| Using general properties of one-dimensional bound states | `bound-state-properties` | uni-upper | `finite-well-exact` |
| Finding bands with a periodic potential | `periodic-potentials-and-bloch` | uni-upper | `delta-function-potential`, `modern.band-theory` |

### Formalism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Representing states as vectors in Hilbert space | `hilbert-space-and-kets` | uni-upper | `linalg.inner-product-spaces`, `stationary-state-expansion` |
| Using Dirac bra-ket notation | `dirac-notation` | uni-upper | `hilbert-space-and-kets` |
| Linking observables to Hermitian operators | `hermitian-operators-observables` | uni-upper | `dirac-notation`, `linalg.hermitian-intro` |
| Finding eigenvalues and eigenvectors of observables | `eigenvalues-of-observables` | uni-upper | `hermitian-operators-observables`, `linalg.spectral-theorem` |
| Normalizing continuous eigenstates with delta functions | `continuous-spectra` | uni-upper | `eigenvalues-of-observables`, `pde.fourier-inversion` |
| Applying measurement and collapse postulates | `measurement-postulates` | uni-upper | `eigenvalues-of-observables` |
| Computing commutators of operators | `commutators` | uni-upper | `hermitian-operators-observables`, `linalg.product-noncommutative` |
| Deriving the generalized uncertainty principle | `generalized-uncertainty` | uni-upper | `commutators`, `measurement-postulates` |
| Finding simultaneous eigenstates of compatible observables | `compatible-observables` | uni-upper | `commutators`, `eigenvalues-of-observables` |
| Changing between position, momentum and energy bases | `change-of-representation` | uni-upper | `dirac-notation`, `linalg.change-of-basis`, `continuous-spectra` |
| Representing operators as matrices | `matrix-representations` | uni-upper | `dirac-notation`, `linalg.matrix-of-transformation` |
| Using the time evolution operator | `time-evolution-operator` | uni-upper | `hermitian-operators-observables`, `diffeq.matrix-exponential` |
| Using the Heisenberg picture | `heisenberg-picture` | uni-upper | `time-evolution-operator`, `commutators` |
| Solving two-level systems | `two-level-systems` | uni-upper | `matrix-representations`, `time-evolution-operator` |

### Harmonic oscillator

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving the oscillator by power series | `oscillator-series-solution` | uni-upper | `modern.oscillator-energy-levels`, `diffeq.series-solutions-ordinary` |
| Using Hermite polynomials | `hermite-polynomials` | uni-upper | `oscillator-series-solution` |
| Solving the oscillator with ladder operators | `ladder-operators-oscillator` | uni-upper | `oscillator-series-solution`, `commutators` |
| Finding oscillator matrix elements with ladder operators | `oscillator-matrix-elements` | uni-upper | `ladder-operators-oscillator` |
| Describing coherent states | `coherent-states` | uni-upper | `ladder-operators-oscillator` |

### Three dimensions and angular momentum

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Separating the Schrodinger equation in three dimensions | `schrodinger-in-three-dimensions` | uni-upper | `modern.three-dimensional-box`, `pde.spherical-laplace` |
| Solving the angular equation with spherical harmonics | `spherical-harmonics` | uni-upper | `schrodinger-in-three-dimensions`, `pde.legendre-eigenfunctions` |
| Reducing the radial equation with an effective potential | `radial-equation` | uni-upper | `schrodinger-in-three-dimensions` |
| Solving the infinite spherical well | `infinite-spherical-well` | uni-upper | `radial-equation`, `diffeq.bessel-intro` |
| Solving the hydrogen radial equation | `hydrogen-radial-solution` | uni-upper | `radial-equation`, `diffeq.series-solutions-ordinary`, `modern.hydrogen-schrodinger-overview` |
| Using hydrogen wave functions and degeneracy | `hydrogen-wave-functions` | uni-upper | `hydrogen-radial-solution`, `spherical-harmonics` |
| Deriving angular momentum commutation relations | `angular-momentum-commutation` | uni-upper | `commutators`, `modern.orbital-angular-momentum-quantization` |
| Finding angular momentum spectra with ladder operators | `angular-momentum-ladder-operators` | uni-upper | `angular-momentum-commutation` |
| Writing angular momentum operators in spherical coordinates | `angular-momentum-operators-spherical` | uni-upper | `angular-momentum-commutation`, `spherical-harmonics` |
| Finding rigid rotor energy levels | `rigid-rotor` | uni-upper | `angular-momentum-operators-spherical` |

### Spin

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Representing spin one-half states | `spin-one-half-states` | uni-upper | `angular-momentum-ladder-operators`, `modern.stern-gerlach-and-spin`, `two-level-systems` |
| Using Pauli matrices | `pauli-matrices` | uni-upper | `spin-one-half-states`, `matrix-representations` |
| Finding spin probabilities along any axis | `spin-along-any-axis` | uni-upper | `pauli-matrices`, `measurement-postulates` |
| Finding Larmor precession of spin in a magnetic field | `spin-precession` | uni-upper | `pauli-matrices`, `time-evolution-operator` |
| Explaining magnetic resonance | `magnetic-resonance` | uni-upper | `spin-precession` |
| Adding two angular momenta | `addition-of-angular-momentum` | uni-upper | `angular-momentum-ladder-operators`, `spin-one-half-states` |
| Using Clebsch-Gordan coefficients | `clebsch-gordan-coefficients` | uni-upper | `addition-of-angular-momentum` |
| Building singlet and triplet states | `singlet-and-triplet-states` | uni-upper | `addition-of-angular-momentum` |
| Representing spin-one systems | `spin-one` | uni-upper | `angular-momentum-ladder-operators`, `matrix-representations` |

### Identical particles

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing two-particle wave functions | `two-particle-wave-functions` | uni-upper | `hilbert-space-and-kets`, `modern.infinite-square-well` |
| Symmetrizing states for bosons and fermions | `symmetrization` | uni-upper | `two-particle-wave-functions`, `modern.pauli-exclusion` |
| Explaining the exchange force | `exchange-force` | uni-upper | `symmetrization` |
| Analyzing the helium atom | `helium-atom` | uni-upper | `symmetrization`, `singlet-and-triplet-states`, `hydrogen-wave-functions` |
| Explaining shell structure from quantum mechanics | `shell-structure-from-quantum` | uni-upper | `helium-atom`, `modern.multi-electron-atoms` |
| Finding the density of states of a free electron gas | `free-electron-gas-density-of-states` | uni-upper | `symmetrization`, `modern.fermi-energy` |
| Describing entangled states | `entanglement` | uni-upper | `singlet-and-triplet-states`, `two-particle-wave-functions` |
| Deriving a Bell inequality | `bell-inequality` | uni-upper | `entanglement`, `spin-along-any-axis` |

### Time-independent perturbation theory

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding first-order energy corrections | `first-order-energy-correction` | uni-upper | `eigenvalues-of-observables`, `stationary-state-expansion` |
| Finding first-order state corrections | `first-order-state-correction` | uni-upper | `first-order-energy-correction` |
| Finding second-order energy corrections | `second-order-energy` | uni-upper | `first-order-state-correction` |
| Solving degenerate perturbation problems | `degenerate-perturbation` | uni-upper | `first-order-energy-correction`, `linalg.find-eigenvalues` |
| Finding fine structure of hydrogen | `fine-structure-hydrogen` | uni-upper | `degenerate-perturbation`, `hydrogen-wave-functions`, `addition-of-angular-momentum` |
| Finding weak-field and strong-field Zeeman splitting | `zeeman-effect-perturbation` | uni-upper | `fine-structure-hydrogen`, `spin-precession` |
| Finding hyperfine splitting and the 21 cm line | `hyperfine-structure` | uni-upper | `fine-structure-hydrogen`, `singlet-and-triplet-states` |
| Finding the Stark effect | `stark-effect` | uni-upper | `degenerate-perturbation`, `hydrogen-wave-functions` |

### Variational and WKB methods

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Bounding ground state energies variationally | `variational-principle` | uni-upper | `eigenvalues-of-observables`, `modern.expectation-values` |
| Estimating the helium ground state variationally | `variational-helium` | uni-upper | `variational-principle`, `helium-atom` |
| Estimating bonding in the hydrogen molecule ion | `hydrogen-molecule-ion` | uni-upper | `variational-principle` |
| Using the WKB approximation | `wkb-approximation` | uni-upper | `scattering-states-and-transmission` |
| Finding bound state energies with WKB | `wkb-bound-states` | uni-upper | `wkb-approximation` |
| Finding tunneling rates with WKB | `wkb-tunneling` | uni-upper | `wkb-approximation`, `modern.tunneling-applications` |

### Time-dependent perturbation theory

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Solving driven two-level systems | `driven-two-level-systems` | uni-upper | `two-level-systems`, `stationary-state-expansion` |
| Finding Rabi oscillations | `rabi-oscillations` | uni-upper | `driven-two-level-systems` |
| Finding first-order transition amplitudes | `first-order-transition-amplitudes` | uni-upper | `driven-two-level-systems` |
| Analyzing sinusoidal perturbations and resonance | `sinusoidal-perturbations` | uni-upper | `first-order-transition-amplitudes` |
| Using Fermi's golden rule | `fermi-golden-rule` | uni-upper | `sinusoidal-perturbations` |
| Finding absorption and stimulated emission rates | `absorption-and-stimulated-emission` | uni-upper | `fermi-golden-rule`, `modern.laser-principles` |
| Finding spontaneous emission rates and lifetimes | `spontaneous-emission-and-lifetimes` | uni-upper | `absorption-and-stimulated-emission` |
| Deriving selection rules | `selection-rules-derived` | uni-upper | `absorption-and-stimulated-emission`, `angular-momentum-operators-spherical` |
| Using the adiabatic approximation | `adiabatic-approximation` | uni-upper | `time-evolution-operator` |

### Scattering

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Relating scattering amplitude to cross section | `scattering-amplitude` | uni-upper | `schrodinger-in-three-dimensions`, `probability-current` |
| Using partial wave analysis | `partial-wave-analysis` | uni-upper | `scattering-amplitude`, `spherical-harmonics` |
| Finding phase shifts | `phase-shifts` | uni-upper | `partial-wave-analysis` |
| Using the Born approximation | `born-approximation` | uni-upper | `scattering-amplitude`, `momentum-space-wave-functions` |
| Finding Yukawa and Coulomb scattering in the Born approximation | `yukawa-and-coulomb-scattering` | uni-upper | `born-approximation` |

### Mixed states and quantum information

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using density matrices for mixed states | `density-matrix` | uni-upper | `matrix-representations`, `measurement-postulates` |
| Describing measurement and decoherence | `decoherence` | uni-upper | `density-matrix`, `entanglement` |
| Describing qubits and quantum gates | `qubits-and-gates` | uni-upper | `two-level-systems`, `pauli-matrices` |
| Explaining no-cloning and teleportation | `no-cloning-and-teleportation` | uni-upper | `qubits-and-gates`, `entanglement` |

## physics.stat-thermal: 61 topics, budget 150 (proposed 65)

### Counting states

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Counting microstates of simple systems | `microstates-and-macrostates` | uni-upper | `waves-thermo-optics.microstates-and-entropy`, `probstat.counting-for-probability` |
| Counting states of a two-state paramagnet | `two-state-paramagnet-counting` | uni-upper | `microstates-and-macrostates`, `probstat.bernoulli-binomial` |
| Counting states of an Einstein solid | `einstein-solid-counting` | uni-upper | `microstates-and-macrostates` |
| Using Stirling's approximation | `stirling-approximation` | uni-upper | `microstates-and-macrostates`, `calc2.integral-test` |
| Showing multiplicity peaks sharply for large systems | `multiplicity-sharpness` | uni-upper | `stirling-approximation`, `einstein-solid-counting`, `probstat.normal-approx-binomial` |
| Analyzing random walks | `random-walks` | uni-upper | `two-state-paramagnet-counting`, `probstat.variance-of-sums` |
| Finding the most probable split of energy | `interacting-systems-and-equilibrium` | uni-upper | `multiplicity-sharpness` |

### Entropy and temperature

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining entropy as the log of multiplicity | `statistical-entropy` | uni-upper | `interacting-systems-and-equilibrium`, `waves-thermo-optics.entropy-definition` |
| Using the microcanonical ensemble | `microcanonical-ensemble` | uni-upper | `statistical-entropy` |
| Defining temperature from entropy | `temperature-from-entropy` | uni-upper | `statistical-entropy`, `calc3.partial-derivatives-compute` |
| Deriving the entropy of an ideal gas | `sackur-tetrode` | uni-upper | `statistical-entropy`, `stirling-approximation`, `modern.three-dimensional-box` |
| Resolving the Gibbs paradox with entropy of mixing | `gibbs-paradox` | uni-upper | `sackur-tetrode` |
| Finding heat capacity and magnetization of a paramagnet | `paramagnet-thermodynamics` | uni-upper | `temperature-from-entropy`, `two-state-paramagnet-counting` |
| Explaining negative temperature | `negative-temperature` | uni-upper | `paramagnet-thermodynamics` |
| Defining pressure and chemical potential from entropy | `pressure-and-chemical-potential` | uni-upper | `temperature-from-entropy` |
| Using the thermodynamic identity | `thermodynamic-identity` | uni-upper | `pressure-and-chemical-potential`, `waves-thermo-optics.entropy-change-of-ideal-gas` |
| Using the third law | `third-law` | uni-upper | `temperature-from-entropy`, `waves-thermo-optics.heat-capacity-with-calculus` |
| Linking information entropy to thermodynamic entropy | `information-entropy` | uni-upper | `statistical-entropy` |

### Thermodynamic potentials

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining Helmholtz and Gibbs free energies | `free-energies` | uni-upper | `thermodynamic-identity`, `waves-thermo-optics.enthalpy` |
| Using free energy to predict equilibrium | `free-energy-minimum-principles` | uni-upper | `free-energies`, `waves-thermo-optics.entropy-of-the-universe` |
| Deriving Maxwell relations | `maxwell-relations` | uni-upper | `free-energies`, `calc3.clairaut-mixed-partials` |
| Relating heat capacities and compressibilities | `heat-capacity-relations` | uni-upper | `maxwell-relations` |
| Analyzing the Joule-Thomson process | `joule-thomson` | uni-upper | `maxwell-relations`, `waves-thermo-optics.real-gases` |
| Using extensivity and the Gibbs-Duhem relation | `gibbs-duhem` | uni-upper | `free-energies` |
| Finding maximum work with free energy | `maximum-work-from-free-energy` | uni-upper | `free-energy-minimum-principles`, `waves-thermo-optics.available-work` |

### Phase transitions and mixtures

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using chemical potential for phase equilibrium | `phase-equilibrium` | uni-upper | `free-energy-minimum-principles`, `waves-thermo-optics.phase-diagrams` |
| Deriving the Clausius-Clapeyron relation | `clausius-clapeyron` | uni-upper | `phase-equilibrium` |
| Finding liquid-gas transitions in the van der Waals model | `van-der-waals-transition` | uni-upper | `clausius-clapeyron`, `waves-thermo-optics.real-gases` |
| Analyzing ideal mixtures and solutions | `ideal-mixtures` | uni-upper | `gibbs-paradox`, `free-energies` |
| Deriving the law of mass action | `law-of-mass-action` | uni-upper | `ideal-mixtures`, `phase-equilibrium` |
| Solving the Ising model in mean field | `ising-mean-field` | uni-upper | `paramagnet-thermodynamics`, `free-energy-minimum-principles` |
| Describing critical behaviour and exponents | `critical-exponents` | uni-upper | `ising-mean-field`, `van-der-waals-transition` |

### Boltzmann statistics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving the Boltzmann factor | `boltzmann-factor-derivation` | uni-upper | `temperature-from-entropy` |
| Computing partition functions | `partition-function` | uni-upper | `boltzmann-factor-derivation` |
| Finding average energy from the partition function | `averages-from-partition-function` | uni-upper | `partition-function` |
| Finding energy fluctuations and heat capacity | `energy-fluctuations` | uni-upper | `averages-from-partition-function`, `probstat.variance-discrete` |
| Finding free energy from the partition function | `free-energy-from-partition-function` | uni-upper | `averages-from-partition-function`, `free-energies` |
| Finding thermal properties of two-level systems | `two-level-thermal-properties` | uni-upper | `averages-from-partition-function`, `paramagnet-thermodynamics` |
| Deriving equipartition from Boltzmann statistics | `equipartition-derived` | uni-upper | `averages-from-partition-function`, `waves-thermo-optics.equipartition`, `calc3.gaussian-integral` |
| Deriving the Maxwell speed distribution | `maxwell-distribution-derived` | uni-upper | `boltzmann-factor-derivation`, `waves-thermo-optics.maxwell-speed-distribution` |
| Finding the partition function of an ideal gas | `ideal-gas-partition-function` | uni-upper | `partition-function`, `sackur-tetrode` |
| Finding rotational and vibrational heat capacities | `molecular-heat-capacities` | uni-upper | `ideal-gas-partition-function`, `modern.molecular-rotation-spectra`, `modern.molecular-vibration-spectra` |
| Finding thermal properties of a quantum oscillator | `quantum-oscillator-thermal` | uni-upper | `averages-from-partition-function`, `modern.oscillator-energy-levels` |
| Finding the heat capacity of an Einstein solid | `einstein-solid-heat-capacity` | uni-upper | `quantum-oscillator-thermal` |
| Explaining the exponential atmosphere with Boltzmann factors | `exponential-atmosphere` | uni-upper | `boltzmann-factor-derivation`, `waves-thermo-optics.pressure-in-a-compressible-atmosphere` |

### Quantum statistics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving the Gibbs factor and grand partition function | `grand-canonical-ensemble` | uni-upper | `boltzmann-factor-derivation`, `pressure-and-chemical-potential` |
| Deriving the Fermi-Dirac distribution | `fermi-dirac-distribution` | uni-upper | `grand-canonical-ensemble`, `modern.pauli-exclusion` |
| Deriving the Bose-Einstein distribution | `bose-einstein-distribution` | uni-upper | `grand-canonical-ensemble` |
| Finding when quantum statistics reduce to Boltzmann | `classical-limit-of-quantum-statistics` | uni-upper | `fermi-dirac-distribution`, `bose-einstein-distribution`, `ideal-gas-partition-function` |
| Finding densities of states | `density-of-states` | uni-upper | `modern.three-dimensional-box`, `calc3.triple-spherical` |
| Analyzing a degenerate electron gas | `degenerate-fermi-gas` | uni-upper | `fermi-dirac-distribution`, `density-of-states`, `modern.fermi-energy` |
| Finding the electron heat capacity of metals | `electron-heat-capacity` | uni-upper | `degenerate-fermi-gas` |
| Finding degeneracy pressure in white dwarfs | `degeneracy-pressure` | uni-upper | `degenerate-fermi-gas` |
| Finding carrier densities in semiconductors | `semiconductor-carrier-statistics` | uni-upper | `fermi-dirac-distribution`, `modern.doped-semiconductors` |
| Deriving the blackbody spectrum from photon statistics | `photon-gas` | uni-upper | `bose-einstein-distribution`, `density-of-states`, `modern.blackbody-spectrum` |
| Finding heat capacity of solids with the Debye model | `debye-model` | uni-upper | `photon-gas`, `einstein-solid-heat-capacity` |
| Analyzing Bose-Einstein condensation | `bose-einstein-condensation` | uni-upper | `bose-einstein-distribution`, `density-of-states` |

### Transport and fluctuations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Estimating viscosity and conductivity from kinetic theory | `transport-coefficients` | uni-upper | `waves-thermo-optics.mean-free-path`, `waves-thermo-optics.viscosity` |
| Deriving the diffusion equation from random walks | `diffusion-equation-from-random-walks` | uni-upper | `random-walks`, `calc3.partial-derivatives-compute` |
| Using the Einstein relation for Brownian motion | `brownian-motion` | uni-upper | `diffusion-equation-from-random-walks`, `boltzmann-factor-derivation` |
| Explaining throttling and low-temperature techniques | `throttling-and-low-temperatures` | uni-upper | `joule-thomson` |
