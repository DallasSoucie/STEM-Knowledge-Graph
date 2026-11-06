# Topic lists: physics.mechanics and physics.em

Draft for approval. In the Needs column, a plain name is in the same course, `mechanics.`, `hs1.` and `hs2.` name physics courses, and a prefix such as `g7.` names a math course.

## Proposed manifest changes

- `physics.mechanics` gains `physics.hs1` in `follows`, so university topics can build on high school mechanics without reteaching it.
- `physics.em` gains `physics.hs2` in `follows`, for the same reason.

## Survey

Sources are indexed in `refs/uni_syllabi/SOURCES.md` under `physics-mechanics` and `physics-em`. Several are short or policy-only documents, so coverage was judged from the fuller syllabi plus AP Physics C. Waves, fluids and thermal physics stay in `physics.waves-thermo-optics`; relativity stays in `physics.modern`.


## physics.mechanics: 133 topics, budget 190

### Motion with calculus

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding velocity as a derivative | `velocity-as-derivative` | uni-lower | `hs1.instantaneous-velocity`, `calc1.position-velocity-acceleration` |
| Finding acceleration as a second derivative | `acceleration-as-derivative` | uni-lower | `velocity-as-derivative` |
| Finding turning points with derivatives | `turning-points-of-motion` | uni-lower | `velocity-as-derivative`, `calc1.critical-numbers` |
| Integrating acceleration to find velocity | `velocity-from-acceleration-integral` | uni-lower | `acceleration-as-derivative`, `calc1.motion-from-acceleration` |
| Integrating velocity to find position | `position-from-velocity-integral` | uni-lower | `velocity-from-acceleration-integral`, `calc1.displacement-distance` |
| Deriving the constant-acceleration equations | `deriving-motion-equations` | uni-lower | `position-from-velocity-integral`, `hs1.choosing-a-motion-equation` |
| Solving motion with time-varying acceleration | `time-varying-acceleration` | uni-lower | `position-from-velocity-integral` |
| Solving motion with velocity-dependent acceleration | `velocity-dependent-acceleration` | uni-lower | `time-varying-acceleration`, `calc1.substitution-with-exp-log` |
| Solving motion with position-dependent acceleration | `position-dependent-acceleration` | uni-lower | `time-varying-acceleration`, `calc1.chain-rule-general` |
| Relating motion graphs with calculus | `motion-graphs-with-calculus` | uni-lower | `position-from-velocity-integral`, `hs1.translating-motion-graphs` |
| Solving related-rates motion problems | `related-rates-in-motion` | uni-lower | `velocity-as-derivative`, `calc1.related-rates-setup` |
| Predicting formulas with dimensional analysis | `dimensional-analysis` | uni-lower | `hs1.checking-with-units` |

### Vectors and motion in space

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using unit vector notation | `unit-vector-notation` | uni-lower | `hs1.adding-by-components`, `precalc.unit-vectors` |
| Writing position vectors in three dimensions | `position-vectors` | uni-lower | `unit-vector-notation`, `precalc.vectors-in-3d` |
| Using the dot product in physics | `dot-product-in-physics` | uni-lower | `unit-vector-notation`, `precalc.dot-product` |
| Using the cross product in physics | `cross-product-in-physics` | uni-lower | `unit-vector-notation`, `precalc.determinants-3x3` |
| Differentiating position vectors | `velocity-vector-derivative` | uni-lower | `position-vectors`, `velocity-as-derivative` |
| Finding acceleration vectors | `acceleration-vectors` | uni-lower | `velocity-vector-derivative`, `acceleration-as-derivative` |
| Eliminating time to find a path | `path-from-position` | uni-lower | `velocity-vector-derivative`, `precalc.parametric-eliminate` |
| Integrating acceleration vectors | `integrating-vector-motion` | uni-lower | `acceleration-vectors`, `position-from-velocity-integral` |
| Splitting acceleration along and across a path | `tangential-and-normal-parts` | uni-lower | `acceleration-vectors`, `dot-product-in-physics` |
| Deriving projectile motion with calculus | `projectiles-with-calculus` | uni-lower | `integrating-vector-motion`, `hs1.range-and-peak` |
| Optimizing a launch angle | `optimizing-a-launch` | uni-lower | `projectiles-with-calculus`, `calc1.optimization-setup` |
| Using relative position and velocity vectors | `relative-position-vectors` | uni-lower | `velocity-vector-derivative`, `hs1.relative-velocity-plane` |
| Using Galilean transformations | `galilean-transformations` | uni-lower | `relative-position-vectors` |
| Deriving centripetal acceleration with vectors | `circular-motion-derivation` | uni-lower | `velocity-vector-derivative`, `calc1.derivatives-of-sine-cosine`, `hs1.centripetal-acceleration` |
| Analyzing non-uniform circular motion | `nonuniform-circular-motion` | uni-lower | `circular-motion-derivation`, `tangential-and-normal-parts` |

### Forces and Newton's laws

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing force as a rate of change of momentum | `force-as-rate-of-momentum` | uni-lower | `velocity-as-derivative`, `hs1.momentum` |
| Writing Newton's second law in vector form | `newtons-laws-in-vector-form` | uni-lower | `force-as-rate-of-momentum`, `acceleration-vectors`, `hs1.second-law-with-motion` |
| Solving forces in three dimensions | `forces-in-three-dimensions` | uni-lower | `newtons-laws-in-vector-form` |
| Solving motion under a time-varying force | `time-varying-forces` | uni-lower | `newtons-laws-in-vector-form`, `time-varying-acceleration` |
| Solving motion under a position-dependent force | `position-dependent-forces` | uni-lower | `newtons-laws-in-vector-form`, `position-dependent-acceleration` |
| Solving motion with linear drag | `linear-drag` | uni-lower | `newtons-laws-in-vector-form`, `velocity-dependent-acceleration`, `hs1.drag-and-terminal-velocity` |
| Solving motion with quadratic drag | `quadratic-drag` | uni-lower | `linear-drag` |
| Finding the approach to terminal velocity | `terminal-velocity-approach` | uni-lower | `linear-drag`, `calc1.limits-at-infinity-exp-log` |
| Writing constraint equations for connected objects | `systems-with-constraints` | uni-lower | `newtons-laws-in-vector-form`, `hs1.pulley-systems` |
| Solving movable pulley systems | `movable-pulleys` | uni-lower | `systems-with-constraints` |
| Solving a block on a moving wedge | `moving-wedges` | uni-lower | `systems-with-constraints`, `hs1.inclines-with-friction` |
| Solving stacked blocks with friction | `stacked-blocks` | uni-lower | `systems-with-constraints`, `hs1.kinetic-friction` |
| Finding tension along a massive rope | `tension-in-a-massive-rope` | uni-lower | `newtons-laws-in-vector-form`, `calc1.definite-integral-definition` |
| Solving banked curves with friction | `curves-with-friction` | uni-lower | `nonuniform-circular-motion`, `hs1.banked-curves` |
| Solving a conical pendulum | `conical-pendulum` | uni-lower | `circular-motion-derivation`, `hs1.equilibrium-in-two-dimensions` |
| Using pseudo-forces in accelerating frames | `accelerating-frames` | uni-lower | `galilean-transformations`, `newtons-laws-in-vector-form` |
| Using centrifugal force in rotating frames | `rotating-frames` | uni-lower | `accelerating-frames`, `circular-motion-derivation` |
| Describing the Coriolis effect | `coriolis-effect` | uni-lower | `rotating-frames`, `cross-product-in-physics` |

### Work and energy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating work as an integral | `work-as-an-integral` | uni-lower | `hs1.work-from-a-graph`, `calc1.ftc-part-2` |
| Calculating work with vectors | `work-as-a-dot-product` | uni-lower | `work-as-an-integral`, `dot-product-in-physics` |
| Calculating work along a curved path | `work-along-a-path` | uni-lower | `work-as-a-dot-product`, `calc1.u-substitution-definite` |
| Deriving spring work by integration | `spring-work-by-integration` | uni-lower | `work-as-an-integral`, `hs1.elastic-potential-energy` |
| Deriving the work-energy theorem | `work-energy-derivation` | uni-lower | `work-as-an-integral`, `position-dependent-acceleration`, `hs1.work-energy-theorem` |
| Testing whether a force is conservative | `conservative-forces` | uni-lower | `work-along-a-path` |
| Finding potential energy from a force | `potential-from-force` | uni-lower | `conservative-forces`, `spring-work-by-integration` |
| Finding a force from potential energy | `force-from-potential` | uni-lower | `potential-from-force` |
| Finding equilibrium from a potential energy function | `equilibrium-from-potential` | uni-lower | `force-from-potential`, `calc1.second-derivative-test` |
| Analyzing motion from a potential energy function | `energy-diagrams-with-calculus` | uni-lower | `equilibrium-from-potential`, `hs1.potential-energy-graphs` |
| Solving energy problems with variable forces | `energy-with-variable-forces` | uni-lower | `work-energy-derivation`, `potential-from-force` |
| Using energy conservation with nonconservative work | `nonconservative-work-general` | uni-lower | `energy-with-variable-forces`, `hs1.energy-with-friction` |
| Finding power as a derivative | `power-as-a-derivative` | uni-lower | `work-as-a-dot-product`, `hs1.power-force-velocity` |
| Integrating power to find energy | `energy-from-power` | uni-lower | `power-as-a-derivative` |
| Finding maximum power | `optimizing-power` | uni-lower | `power-as-a-derivative`, `calc1.optimization-setup` |

### Systems and momentum

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating impulse as an integral | `impulse-as-an-integral` | uni-lower | `force-as-rate-of-momentum`, `hs1.impulse-from-a-graph`, `calc1.ftc-part-2` |
| Writing total momentum of a system | `momentum-of-particle-systems` | uni-lower | `force-as-rate-of-momentum`, `hs1.momentum-of-a-system` |
| Deriving momentum conservation from internal forces | `internal-and-external-forces` | uni-lower | `momentum-of-particle-systems`, `hs1.conserving-momentum` |
| Finding center of mass in three dimensions | `center-of-mass-in-space` | uni-lower | `position-vectors`, `hs1.center-of-mass` |
| Finding center of mass of a rod by integration | `center-of-mass-by-integration` | uni-lower | `center-of-mass-in-space`, `calc1.definite-integral-definition` |
| Finding center of mass of a plate by integration | `center-of-mass-of-a-shape` | uni-lower | `center-of-mass-by-integration`, `calc1.area-between-curves-x` |
| Deriving the motion of the center of mass | `center-of-mass-motion` | uni-lower | `center-of-mass-in-space`, `momentum-of-particle-systems`, `hs1.motion-of-center-of-mass` |
| Splitting kinetic energy of a system | `kinetic-energy-of-a-system` | uni-lower | `center-of-mass-motion`, `work-energy-derivation` |
| Deriving elastic collision formulas | `elastic-collision-formulas` | uni-lower | `internal-and-external-forces`, `hs1.elastic-collisions` |
| Solving collisions in the center-of-mass frame | `collisions-in-center-of-mass-frame` | uni-lower | `center-of-mass-motion`, `elastic-collision-formulas`, `galilean-transformations` |
| Solving elastic collisions in a plane | `elastic-collisions-in-a-plane` | uni-lower | `elastic-collision-formulas`, `hs1.collisions-in-two-dimensions` |
| Using the coefficient of restitution | `coefficient-of-restitution` | uni-lower | `elastic-collision-formulas` |
| Finding rocket thrust | `rocket-thrust` | uni-lower | `internal-and-external-forces` |
| Deriving the rocket equation | `rocket-equation` | uni-lower | `rocket-thrust`, `calc1.substitution-with-exp-log` |
| Solving variable-mass systems | `variable-mass-systems` | uni-lower | `rocket-thrust` |

### Rotation of rigid bodies

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using calculus for rotational kinematics | `angular-kinematics-with-calculus` | uni-lower | `hs1.rotational-motion-equations`, `time-varying-acceleration` |
| Using angular velocity as a vector | `angular-velocity-vectors` | uni-lower | `angular-kinematics-with-calculus`, `cross-product-in-physics` |
| Finding acceleration of a point on a rigid body | `acceleration-on-a-rigid-body` | uni-lower | `angular-velocity-vectors`, `nonuniform-circular-motion` |
| Calculating torque as a cross product | `torque-as-a-cross-product` | uni-lower | `cross-product-in-physics`, `hs1.torque-at-an-angle` |
| Calculating moment of inertia of point masses | `inertia-of-point-masses` | uni-lower | `hs1.rotational-inertia`, `angular-kinematics-with-calculus` |
| Calculating moment of inertia of a rod by integration | `inertia-of-a-rod` | uni-lower | `inertia-of-point-masses`, `center-of-mass-by-integration` |
| Calculating moment of inertia of disks and cylinders | `inertia-of-disks-and-cylinders` | uni-lower | `inertia-of-a-rod`, `calc1.u-substitution-definite` |
| Calculating moment of inertia of a sphere | `inertia-of-spheres` | uni-lower | `inertia-of-disks-and-cylinders`, `calc1.volume-by-disks` |
| Using the parallel-axis theorem | `parallel-axis-theorem` | uni-lower | `inertia-of-a-rod` |
| Using the perpendicular-axis theorem | `perpendicular-axis-theorem` | uni-lower | `inertia-of-disks-and-cylinders` |
| Finding moment of inertia of composite bodies | `inertia-of-composite-bodies` | uni-lower | `parallel-axis-theorem` |
| Deriving Newton's second law for fixed-axis rotation | `fixed-axis-dynamics` | uni-lower | `torque-as-a-cross-product`, `inertia-of-point-masses`, `hs1.second-law-for-rotation` |
| Solving pulleys with mass | `massive-pulleys` | uni-lower | `fixed-axis-dynamics`, `systems-with-constraints` |
| Solving a falling or pivoting rod | `pivoting-rods` | uni-lower | `fixed-axis-dynamics`, `parallel-axis-theorem` |
| Solving rotation with energy methods | `rotational-energy-general` | uni-lower | `fixed-axis-dynamics`, `energy-with-variable-forces`, `hs1.rotational-kinetic-energy` |
| Calculating rotational work and power with calculus | `rotational-work-as-integral` | uni-lower | `fixed-axis-dynamics`, `work-as-an-integral` |
| Analyzing rolling as translation plus rotation | `rolling-kinematics` | uni-lower | `acceleration-on-a-rigid-body`, `kinetic-energy-of-a-system`, `hs1.rolling` |
| Solving rolling with forces and torques | `rolling-dynamics` | uni-lower | `rolling-kinematics`, `fixed-axis-dynamics` |
| Solving the transition from sliding to rolling | `rolling-to-sliding` | uni-lower | `rolling-dynamics`, `hs1.kinetic-friction` |
| Calculating angular momentum of a particle | `angular-momentum-of-a-particle` | uni-lower | `cross-product-in-physics`, `hs1.angular-momentum` |
| Calculating angular momentum of a system | `angular-momentum-of-systems` | uni-lower | `angular-momentum-of-a-particle`, `center-of-mass-motion` |
| Relating torque to the rate of angular momentum | `torque-and-angular-momentum` | uni-lower | `angular-momentum-of-systems`, `torque-as-a-cross-product` |
| Solving collisions with a pivoted rod | `angular-collisions` | uni-lower | `torque-and-angular-momentum`, `parallel-axis-theorem`, `hs1.conserving-angular-momentum` |
| Explaining gyroscopic precession | `precession` | uni-lower | `torque-and-angular-momentum`, `angular-velocity-vectors` |
| Solving rigid body statics in three dimensions | `statics-of-rigid-bodies` | uni-lower | `torque-as-a-cross-product`, `hs1.beams-and-ladders` |
| Deciding whether an object tips or slides | `tipping-and-sliding` | uni-lower | `statics-of-rigid-bodies`, `hs1.static-friction` |
| Finding the center of gravity | `center-of-gravity` | uni-lower | `statics-of-rigid-bodies`, `center-of-mass-in-space` |
| Using stress, strain and Young's modulus | `stress-and-strain` | uni-lower | `statics-of-rigid-bodies`, `hs1.hookes-law` |
| Using shear and bulk moduli | `shear-and-bulk-moduli` | uni-lower | `stress-and-strain` |

### Gravitation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing gravitation in vector form | `gravitation-in-vector-form` | uni-lower | `unit-vector-notation`, `hs1.universal-gravitation` |
| Finding gravity of extended bodies by integration | `gravitation-of-extended-bodies` | uni-lower | `gravitation-in-vector-form`, `calc1.definite-integral-definition` |
| Using the shell theorem | `shell-theorem` | uni-lower | `gravitation-of-extended-bodies` |
| Finding gravity inside a uniform planet | `gravity-inside-a-planet` | uni-lower | `shell-theorem` |
| Deriving gravitational potential energy by integration | `gravitational-potential-by-integration` | uni-lower | `potential-from-force`, `gravitation-in-vector-form`, `hs1.gravitational-energy-at-a-distance` |
| Finding total energy of an orbit | `energy-of-an-orbit` | uni-lower | `gravitational-potential-by-integration`, `hs1.circular-orbits` |
| Deriving Kepler's second law from angular momentum | `keplers-second-law-derivation` | uni-lower | `angular-momentum-of-a-particle`, `hs1.keplers-third-law` |
| Analyzing elliptical orbits | `elliptical-orbits` | uni-lower | `energy-of-an-orbit`, `keplers-second-law-derivation`, `precalc.conic-applications` |
| Calculating a transfer orbit | `transfer-orbits` | uni-lower | `elliptical-orbits` |
| Solving the two-body problem with reduced mass | `two-body-problem` | uni-lower | `elliptical-orbits`, `center-of-mass-motion` |
| Using effective potential for orbits | `effective-potential-orbits` | uni-lower | `energy-diagrams-with-calculus`, `keplers-second-law-derivation` |

### Oscillations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing the equation of simple harmonic motion | `shm-differential-equation` | uni-lower | `hs1.simple-harmonic-conditions`, `acceleration-as-derivative` |
| Checking sinusoidal solutions of the motion equation | `sinusoidal-solutions` | uni-lower | `shm-differential-equation`, `calc1.derivatives-of-sine-cosine` |
| Finding amplitude and phase from initial conditions | `initial-conditions-and-phase` | uni-lower | `sinusoidal-solutions`, `alg2.compare-sine-cosine-forms` |
| Finding velocity and acceleration in simple harmonic motion | `velocity-and-acceleration-of-shm` | uni-lower | `sinusoidal-solutions` |
| Showing energy is constant in simple harmonic motion | `energy-of-shm-with-calculus` | uni-lower | `velocity-and-acceleration-of-shm`, `force-from-potential` |
| Solving vertical springs and shifted equilibrium | `vertical-springs` | uni-lower | `initial-conditions-and-phase`, `hs1.mass-on-a-spring` |
| Using the small-angle approximation | `small-angle-approximation` | uni-lower | `sinusoidal-solutions`, `calc1.linear-approximation` |
| Deriving the period of a pendulum | `pendulum-derivation` | uni-lower | `small-angle-approximation`, `fixed-axis-dynamics`, `hs1.simple-pendulum` |
| Finding the period of a physical pendulum | `physical-pendulum` | uni-lower | `pendulum-derivation`, `parallel-axis-theorem` |
| Finding the period of a torsion pendulum | `torsion-pendulum` | uni-lower | `pendulum-derivation` |
| Finding small oscillations about a stable equilibrium | `small-oscillations-about-equilibrium` | uni-lower | `equilibrium-from-potential`, `sinusoidal-solutions` |
| Linking simple harmonic motion with circular motion | `circular-motion-link` | uni-lower | `sinusoidal-solutions`, `circular-motion-derivation` |
| Writing the damped oscillator equation | `damped-oscillator-equation` | uni-lower | `shm-differential-equation`, `linear-drag` |
| Comparing underdamped, overdamped and critically damped motion | `damping-regimes` | uni-lower | `damped-oscillator-equation` |
| Finding energy decay and quality factor | `energy-decay-and-quality` | uni-lower | `damping-regimes` |
| Finding the response of a driven oscillator | `driven-oscillator` | uni-lower | `damping-regimes`, `hs1.damping-and-resonance` |
| Reading resonance curves | `resonance-curves` | uni-lower | `driven-oscillator`, `energy-decay-and-quality` |
| Describing coupled oscillators and normal modes | `coupled-oscillators` | uni-lower | `sinusoidal-solutions`, `systems-with-constraints` |

## physics.em: 118 topics, budget 190

### Electric charge and fields

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing Coulomb's law in vector form | `coulombs-law-vector-form` | uni-lower | `mechanics.unit-vector-notation`, `hs2.coulomb-forces-in-a-plane` |
| Adding forces and fields with unit vectors | `superposition-of-charges` | uni-lower | `coulombs-law-vector-form`, `hs2.adding-electric-fields` |
| Using linear, surface and volume charge densities | `charge-densities` | uni-lower | `hs2.charge-conservation`, `calc1.definite-integral-definition` |
| Setting up a field integral for continuous charge | `setting-up-field-integrals` | uni-lower | `superposition-of-charges`, `charge-densities` |
| Finding the field of a finite line of charge | `field-of-a-finite-line` | uni-lower | `setting-up-field-integrals`, `calc2.trig-sub-tangent` |
| Finding the field of an infinite line of charge | `field-of-an-infinite-line` | uni-lower | `field-of-a-finite-line`, `calc2.improper-infinite-limits` |
| Finding the field of a charged arc | `field-of-a-charged-arc` | uni-lower | `setting-up-field-integrals` |
| Finding the field on the axis of a ring | `field-of-a-ring` | uni-lower | `setting-up-field-integrals`, `calc1.u-substitution-definite` |
| Finding the field on the axis of a disk | `field-of-a-disk` | uni-lower | `field-of-a-ring` |
| Finding the field of an infinite sheet | `field-of-an-infinite-sheet` | uni-lower | `field-of-a-disk` |
| Approximating fields at large distances | `far-field-approximations` | uni-lower | `field-of-a-ring`, `calc2.binomial-series` |
| Finding the field of a dipole | `electric-dipole-field` | uni-lower | `far-field-approximations`, `hs2.electric-dipoles` |
| Finding torque and energy of a dipole in a field | `dipole-in-a-field` | uni-lower | `electric-dipole-field`, `mechanics.torque-as-a-cross-product` |
| Solving motion in a nonuniform field | `motion-in-a-nonuniform-field` | uni-lower | `superposition-of-charges`, `mechanics.position-dependent-forces`, `hs2.charge-in-a-field` |
| Finding oscillation of a charge near a ring | `oscillating-charges-in-fields` | uni-lower | `field-of-a-ring`, `mechanics.small-oscillations-about-equilibrium` |

### Gauss's law

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating electric flux through a flat surface | `electric-flux` | uni-lower | `mechanics.dot-product-in-physics`, `hs2.uniform-electric-field` |
| Calculating flux through curved surfaces | `flux-through-curved-surfaces` | uni-lower | `electric-flux`, `charge-densities` |
| Stating Gauss's law | `gauss-law-statement` | uni-lower | `flux-through-curved-surfaces` |
| Choosing a Gaussian surface | `choosing-gaussian-surfaces` | uni-lower | `gauss-law-statement` |
| Using Gauss's law with spherical symmetry | `gauss-for-spheres` | uni-lower | `choosing-gaussian-surfaces` |
| Using Gauss's law with cylindrical symmetry | `gauss-for-cylinders` | uni-lower | `choosing-gaussian-surfaces` |
| Using Gauss's law with planar symmetry | `gauss-for-planes` | uni-lower | `choosing-gaussian-surfaces` |
| Using Gauss's law with nonuniform charge | `nonuniform-charge-distributions` | uni-lower | `gauss-for-spheres`, `gauss-for-cylinders`, `calc1.u-substitution-definite` |
| Finding the field inside charged objects | `inside-charged-objects` | uni-lower | `gauss-for-spheres` |
| Using Gauss's law for conductors | `conductors-with-gauss` | uni-lower | `gauss-for-spheres`, `gauss-for-planes`, `hs2.conductors-in-equilibrium` |
| Finding charge on cavities in conductors | `cavities-in-conductors` | uni-lower | `conductors-with-gauss` |
| Solving concentric shells and coaxial cylinders | `coaxial-and-concentric-shells` | uni-lower | `conductors-with-gauss`, `gauss-for-cylinders` |

### Electric potential

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding potential difference as an integral | `potential-as-a-line-integral` | uni-lower | `hs2.electric-potential`, `mechanics.work-as-a-dot-product` |
| Deriving the potential of a point charge | `potential-of-point-charges-derivation` | uni-lower | `potential-as-a-line-integral`, `mechanics.potential-from-force` |
| Finding potential from continuous charge on a line | `potential-of-a-charged-line` | uni-lower | `potential-of-point-charges-derivation`, `charge-densities`, `calc1.substitution-with-exp-log` |
| Finding potential of a ring and disk | `potential-of-a-ring-and-disk` | uni-lower | `potential-of-a-charged-line`, `field-of-a-ring` |
| Finding a field from potential by differentiating | `field-from-potential` | uni-lower | `potential-as-a-line-integral`, `mechanics.force-from-potential` |
| Finding potential inside and outside a sphere | `potential-of-spheres` | uni-lower | `potential-as-a-line-integral`, `gauss-for-spheres` |
| Finding potential near a charged cylinder | `potential-of-cylinders` | uni-lower | `potential-as-a-line-integral`, `gauss-for-cylinders` |
| Finding the energy of a system of charges | `energy-of-charge-systems` | uni-lower | `potential-of-point-charges-derivation`, `hs2.potential-energy-of-charges` |
| Finding the energy to assemble a charged sphere | `energy-to-assemble-a-sphere` | uni-lower | `energy-of-charge-systems`, `potential-of-spheres` |
| Connecting charged conductors by a wire | `isolated-conductors-at-potential` | uni-lower | `potential-of-spheres`, `hs2.sharing-charge` |

### Capacitance and dielectrics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Deriving parallel-plate capacitance with Gauss's law | `deriving-plate-capacitance` | uni-lower | `gauss-for-planes`, `hs2.parallel-plate-capacitors` |
| Deriving capacitance of cylindrical capacitors | `cylindrical-capacitors` | uni-lower | `potential-of-cylinders`, `coaxial-and-concentric-shells` |
| Deriving capacitance of spherical capacitors | `spherical-capacitors` | uni-lower | `potential-of-spheres`, `coaxial-and-concentric-shells` |
| Deriving capacitor energy by integration | `capacitor-energy-integral` | uni-lower | `deriving-plate-capacitance`, `hs2.capacitor-energy` |
| Using energy density of the electric field | `energy-density-of-electric-field` | uni-lower | `capacitor-energy-integral` |
| Finding force on capacitor plates | `force-on-capacitor-plates` | uni-lower | `capacitor-energy-integral`, `mechanics.force-from-potential` |
| Using Gauss's law with dielectrics | `gauss-with-dielectrics` | uni-lower | `deriving-plate-capacitance`, `hs2.dielectrics` |
| Solving partly filled capacitors | `partly-filled-capacitors` | uni-lower | `gauss-with-dielectrics`, `hs2.capacitors-in-circuits` |
| Explaining polarization of dielectrics | `polarization-microscopic` | uni-lower | `gauss-with-dielectrics`, `dipole-in-a-field` |

### Current and circuits

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding current as a rate of charge | `current-as-a-derivative` | uni-lower | `hs2.current-as-charge-flow`, `calc1.chain-rule-general` |
| Using current density | `current-density` | uni-lower | `current-as-a-derivative`, `hs2.drift-velocity` |
| Using the microscopic form of Ohm's law | `microscopic-ohms-law` | uni-lower | `current-density`, `hs2.resistivity` |
| Finding resistance of a nonuniform conductor | `resistance-by-integration` | uni-lower | `microscopic-ohms-law`, `calc1.substitution-with-exp-log` |
| Finding maximum power transfer | `power-in-a-resistor-maximum` | uni-lower | `hs2.emf-and-internal-resistance`, `calc1.optimization-setup` |
| Solving general circuits with Kirchhoff's rules | `kirchhoff-general` | uni-lower | `hs2.multi-loop-circuits` |
| Writing the charging equation of an RC circuit | `rc-charging-equation` | uni-lower | `hs2.capacitor-charging`, `kirchhoff-general`, `calc2.verify-de-solutions` |
| Solving RC charging by separating variables | `rc-solving-charging` | uni-lower | `rc-charging-equation`, `calc2.separable-equations` |
| Solving RC discharging by separating variables | `rc-solving-discharging` | uni-lower | `rc-solving-charging`, `hs2.rc-time-constant` |
| Tracking energy in an RC circuit | `rc-energy-accounting` | uni-lower | `rc-solving-charging`, `capacitor-energy-integral` |
| Solving RC transients in larger circuits | `rc-in-larger-circuits` | uni-lower | `rc-solving-discharging` |

### Magnetic forces

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Writing the Lorentz force as a cross product | `lorentz-force` | uni-lower | `mechanics.cross-product-in-physics`, `hs2.force-on-a-moving-charge` |
| Finding helical motion in a magnetic field | `helical-motion` | uni-lower | `lorentz-force`, `hs2.circular-path-in-a-field` |
| Using the Hall effect | `hall-effect` | uni-lower | `lorentz-force`, `current-density`, `hs2.crossed-fields` |
| Finding force on a curved wire | `force-on-curved-wires` | uni-lower | `lorentz-force`, `hs2.force-on-a-wire`, `calc1.definite-integral-definition` |
| Finding the magnetic moment of a loop | `magnetic-dipole-moment` | uni-lower | `force-on-curved-wires`, `hs2.motor-torque` |
| Finding torque and energy of a current loop | `torque-and-energy-of-a-loop` | uni-lower | `magnetic-dipole-moment`, `dipole-in-a-field` |
| Analyzing cyclotrons | `cyclotrons` | uni-lower | `helical-motion`, `hs2.accelerating-charges` |

### Sources of magnetic field

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Stating the Biot-Savart law | `biot-savart-law` | uni-lower | `lorentz-force`, `setting-up-field-integrals` |
| Finding the field of a finite straight wire | `biot-savart-straight-wire` | uni-lower | `biot-savart-law`, `field-of-a-finite-line` |
| Finding the field at the center of an arc | `biot-savart-arc` | uni-lower | `biot-savart-law` |
| Finding the field on the axis of a loop | `biot-savart-loop-axis` | uni-lower | `biot-savart-law`, `field-of-a-ring` |
| Finding the field of paired coils | `helmholtz-coils` | uni-lower | `biot-savart-loop-axis` |
| Finding the field of a moving charge | `field-of-moving-charge` | uni-lower | `biot-savart-law` |
| Deriving the force between parallel wires | `force-between-wires-derivation` | uni-lower | `biot-savart-straight-wire`, `force-on-curved-wires` |
| Stating Ampere's law | `amperes-law-statement` | uni-lower | `biot-savart-straight-wire`, `potential-as-a-line-integral` |
| Using Ampere's law inside and outside a wire | `amperes-law-long-wire` | uni-lower | `amperes-law-statement` |
| Using Ampere's law with nonuniform current | `amperes-law-nonuniform-current` | uni-lower | `amperes-law-long-wire`, `current-density` |
| Deriving a solenoid's field with Ampere's law | `amperes-law-solenoid` | uni-lower | `amperes-law-statement`, `hs2.field-of-a-solenoid` |
| Finding a toroid's field | `amperes-law-toroid` | uni-lower | `amperes-law-solenoid` |
| Finding the field of a current sheet | `amperes-law-sheet` | uni-lower | `amperes-law-statement` |
| Finding the field of a coaxial cable | `coaxial-cable-field` | uni-lower | `amperes-law-long-wire` |
| Stating Gauss's law for magnetism | `gauss-law-for-magnetism` | uni-lower | `gauss-law-statement`, `biot-savart-law` |
| Describing paramagnetic, diamagnetic and ferromagnetic materials | `magnetic-materials` | uni-lower | `magnetic-dipole-moment`, `amperes-law-solenoid` |

### Induction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Finding magnetic flux by integration | `flux-by-integration` | uni-lower | `hs2.magnetic-flux`, `amperes-law-long-wire` |
| Using Faraday's law with derivatives | `faraday-with-derivatives` | uni-lower | `flux-by-integration`, `hs2.faradays-law` |
| Finding emf in a loop near a long wire | `loop-near-a-wire` | uni-lower | `faraday-with-derivatives`, `calc1.derivative-of-log` |
| Deriving motional emf from the Lorentz force | `motional-emf-derivation` | uni-lower | `lorentz-force`, `hs2.motional-emf` |
| Solving a rod on rails with a magnetic force | `rod-on-rails-dynamics` | uni-lower | `motional-emf-derivation`, `calc2.separable-equations`, `mechanics.linear-drag` |
| Deriving the emf of a rotating coil | `rotating-coil-emf` | uni-lower | `faraday-with-derivatives`, `hs2.generators-output` |
| Finding induced electric fields | `induced-electric-fields` | uni-lower | `faraday-with-derivatives` |
| Telling conservative from induced fields | `conservative-vs-induced-fields` | uni-lower | `induced-electric-fields` |
| Calculating mutual inductance | `mutual-inductance` | uni-lower | `faraday-with-derivatives` |
| Calculating self-inductance | `self-inductance` | uni-lower | `mutual-inductance`, `amperes-law-solenoid`, `hs2.self-inductance-intro` |
| Finding inductance of a coaxial cable and toroid | `inductance-of-coax-and-toroid` | uni-lower | `self-inductance`, `coaxial-cable-field`, `amperes-law-toroid` |
| Calculating energy stored in an inductor | `magnetic-energy` | uni-lower | `self-inductance` |
| Using energy density of the magnetic field | `magnetic-energy-density` | uni-lower | `magnetic-energy`, `energy-density-of-electric-field` |
| Solving current rise in an LR circuit | `lr-rise` | uni-lower | `self-inductance`, `rc-solving-charging` |
| Solving current decay in an LR circuit | `lr-decay` | uni-lower | `lr-rise` |
| Solving oscillation in an LC circuit | `lc-oscillation` | uni-lower | `magnetic-energy`, `capacitor-energy-integral`, `mechanics.sinusoidal-solutions` |
| Comparing LC circuits with springs | `lc-energy-and-spring-analogy` | uni-lower | `lc-oscillation`, `mechanics.energy-of-shm-with-calculus` |
| Analyzing a damped RLC circuit | `rlc-damped` | uni-lower | `lc-oscillation`, `mechanics.damping-regimes`, `lr-rise` |

### Alternating current

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing alternating sources with phase | `ac-sources-and-phase` | uni-lower | `hs2.alternating-current`, `mechanics.initial-conditions-and-phase` |
| Finding capacitive reactance | `reactance-of-capacitors` | uni-lower | `ac-sources-and-phase`, `current-as-a-derivative` |
| Finding inductive reactance | `reactance-of-inductors` | uni-lower | `ac-sources-and-phase`, `self-inductance` |
| Using phasor diagrams | `phasor-diagrams` | uni-lower | `reactance-of-capacitors`, `reactance-of-inductors` |
| Finding impedance of a series RLC circuit | `series-rlc-impedance` | uni-lower | `phasor-diagrams` |
| Finding resonance in an RLC circuit | `ac-resonance` | uni-lower | `series-rlc-impedance`, `rlc-damped`, `mechanics.resonance-curves` |
| Using average power and power factor | `ac-power-factor` | uni-lower | `series-rlc-impedance`, `hs2.power-transmission` |
| Analyzing simple filters | `filters-intro` | uni-lower | `series-rlc-impedance` |
| Deriving the transformer equations | `transformers-derivation` | uni-lower | `mutual-inductance`, `hs2.transformers` |

### Maxwell's equations and waves

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using displacement current | `displacement-current` | uni-lower | `amperes-law-statement`, `deriving-plate-capacitance` |
| Stating Maxwell's equations in integral form | `maxwells-equations-integral` | uni-lower | `displacement-current`, `gauss-law-for-magnetism`, `induced-electric-fields` |
| Finding the magnetic field in a charging capacitor | `fields-in-a-charging-capacitor` | uni-lower | `displacement-current` |
| Showing Maxwell's equations predict waves | `wave-solutions-of-maxwell` | uni-lower | `maxwells-equations-integral`, `hs2.electromagnetic-wave-nature` |
| Finding the speed of light from electric and magnetic constants | `speed-of-light-from-constants` | uni-lower | `wave-solutions-of-maxwell` |
| Describing plane electromagnetic waves | `plane-waves` | uni-lower | `wave-solutions-of-maxwell` |
| Using energy in electromagnetic waves | `energy-in-electromagnetic-waves` | uni-lower | `plane-waves`, `magnetic-energy-density` |
| Using the Poynting vector | `poynting-vector` | uni-lower | `energy-in-electromagnetic-waves` |
| Finding intensity of electromagnetic waves | `wave-intensity` | uni-lower | `poynting-vector` |
| Calculating radiation pressure | `radiation-pressure` | uni-lower | `wave-intensity`, `hs2.photon-momentum` |
| Describing electromagnetic radiation from antennas | `antennas-intro` | uni-lower | `plane-waves` |
