# Topic lists: physics.hs1 and physics.hs2

Draft for approval. In the Needs column, a plain name is in the same course, `ms.` and `hs1.` name physics courses, and a prefix such as `g7.` names a math course.

## Proposed manifest change

`physics.hs1` gains `math.geom` in `follows`, because vector components and rotation need right-triangle trig and radians.


## physics.hs1: 167 topics, budget 200

### Measurement and models

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using SI units and prefixes | `si-units-and-prefixes` | g9 | `g8.choose-scientific-units`, `ms.unit-conversions-speed` |
| Using significant figures | `significant-figures` | g9 | `alg1.appropriate-precision`, `si-units-and-prefixes` |
| Estimating measurement uncertainty | `measurement-uncertainty` | g9 | `significant-figures` |
| Making order-of-magnitude estimates | `order-of-magnitude` | g9 | `si-units-and-prefixes` |
| Checking equations with units | `checking-with-units` | g9 | `si-units-and-prefixes`, `alg1.units-in-formulas` |
| Rearranging physics formulas | `rearranging-physics-formulas` | g9 | `alg1.formula-rearrange-science`, `checking-with-units` |
| Graphing lab data with a best-fit line | `graphing-lab-data` | g9 | `measurement-uncertainty`, `alg1.fit-line-technology` |
| Finding physical meaning in slope and intercept | `slope-meaning-in-data` | g9 | `graphing-lab-data`, `alg1.linear-interpret-parameters` |
| Linearizing data from a square or inverse pattern | `linearizing-data` | g10 | `slope-meaning-in-data`, `g8.square-roots` |

### One-dimensional motion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Telling scalars from vectors | `scalars-and-vectors-1d` | g9 | `ms.velocity-with-direction` |
| Finding displacement with signs | `displacement-with-signs` | g9 | `scalars-and-vectors-1d` |
| Calculating average velocity | `average-velocity` | g9 | `displacement-with-signs`, `rearranging-physics-formulas` |
| Drawing motion diagrams | `motion-diagrams` | g9 | `displacement-with-signs` |
| Analyzing position-time graphs | `position-time-graphs` | g9 | `average-velocity`, `ms.slope-as-speed`, `motion-diagrams` |
| Using the constant velocity model | `constant-velocity-model` | g9 | `position-time-graphs`, `alg1.linear-model-from-context` |
| Finding instantaneous velocity from a curved graph | `instantaneous-velocity` | g9 | `position-time-graphs`, `alg1.rate-of-change-intervals` |
| Calculating acceleration with signs | `acceleration-with-signs` | g9 | `average-velocity`, `ms.acceleration-intro`, `motion-diagrams` |
| Analyzing velocity-time graphs | `velocity-time-graphs` | g9 | `acceleration-with-signs`, `ms.speed-time-graphs` |
| Finding displacement from a velocity graph's area | `displacement-from-area` | g9 | `velocity-time-graphs`, `g6.area-of-triangles` |
| Analyzing acceleration-time graphs | `acceleration-time-graphs` | g9 | `velocity-time-graphs` |
| Translating between motion graphs | `translating-motion-graphs` | g9 | `instantaneous-velocity`, `displacement-from-area`, `acceleration-time-graphs` |
| Using the velocity equation for constant acceleration | `velocity-equation` | g9 | `velocity-time-graphs` |
| Using the displacement equation for constant acceleration | `displacement-equation` | g9 | `velocity-equation`, `displacement-from-area` |
| Using the time-free motion equation | `velocity-squared-equation` | g9 | `displacement-equation`, `g8.square-roots` |
| Choosing a motion equation | `choosing-a-motion-equation` | g9 | `velocity-squared-equation` |
| Solving for time with the quadratic formula | `time-from-a-quadratic` | g9 | `choosing-a-motion-equation`, `alg1.quadratic-formula` |
| Solving when two moving objects meet | `two-object-meeting` | g9 | `choosing-a-motion-equation`, `alg1.systems-review-three-methods` |
| Finding stopping distance and reaction time | `stopping-distance` | g9 | `choosing-a-motion-equation` |
| Solving free fall problems | `free-fall-equations` | g9 | `choosing-a-motion-equation`, `ms.free-fall` |
| Solving upward-thrown motion | `thrown-upward` | g9 | `free-fall-equations`, `time-from-a-quadratic` |
| Reading free fall graphs | `free-fall-graphs` | g9 | `thrown-upward`, `translating-motion-graphs` |

### Vectors and two-dimensional motion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Drawing vectors to scale | `drawing-vectors` | g10 | `scalars-and-vectors-1d`, `geom.angle-notation-measure` |
| Resolving a vector into components | `vector-components-physics` | g10 | `drawing-vectors`, `geom.trig-find-side` |
| Finding a vector from its components | `magnitude-direction-physics` | g10 | `vector-components-physics`, `geom.trig-find-angle`, `g8.pythagorean-irrational-answers` |
| Finding relative velocity along a line | `relative-velocity-line` | g10 | `displacement-with-signs`, `ms.relative-motion` |
| Separating horizontal and vertical motion | `independence-of-motion` | g10 | `vector-components-physics`, `free-fall-equations` |
| Solving horizontal projectile launches | `horizontal-launch` | g10 | `independence-of-motion` |
| Solving angled projectile launches | `angled-launch` | g10 | `horizontal-launch`, `thrown-upward` |
| Finding projectile range and peak height | `range-and-peak` | g10 | `angled-launch` |
| Scaling vectors | `scaling-vectors` | g10 | `drawing-vectors` |
| Adding vectors graphically | `adding-vectors-graphically` | g10 | `scaling-vectors` |
| Adding vectors by components | `adding-by-components` | g10 | `magnitude-direction-physics`, `adding-vectors-graphically` |
| Subtracting vectors | `subtracting-vectors` | g10 | `adding-by-components` |
| Finding two-dimensional displacement and velocity | `displacement-in-two-dimensions` | g10 | `adding-by-components`, `average-velocity` |
| Finding relative velocity in a plane | `relative-velocity-plane` | g10 | `relative-velocity-line`, `subtracting-vectors` |
| Choosing tilted axes for components | `tilted-axes` | g10 | `vector-components-physics` |
| Solving launches from a height | `launch-from-a-height` | g10 | `angled-launch` |
| Reading projectile motion graphs | `projectile-graphs` | g10 | `range-and-peak`, `free-fall-graphs`, `launch-from-a-height` |

### Forces

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Choosing a system | `choosing-a-system` | g10 | `ms.forces-as-interactions` |
| Drawing free-body diagrams | `free-body-diagrams` | g10 | `choosing-a-system`, `ms.force-diagrams`, `drawing-vectors` |
| Using weight and field strength | `weight-and-field-strength` | g10 | `ms.weight-calculation`, `rearranging-physics-formulas` |
| Finding normal force | `normal-force` | g10 | `free-body-diagrams`, `weight-and-field-strength` |
| Finding tension in a rope | `tension` | g10 | `free-body-diagrams`, `weight-and-field-strength` |
| Solving balanced force problems in one dimension | `first-law-in-one-dimension` | g10 | `normal-force`, `tension`, `ms.inertia` |
| Applying Newton's second law in one dimension | `second-law-in-one-dimension` | g10 | `first-law-in-one-dimension`, `ms.calculating-with-second-law` |
| Combining forces and motion equations | `second-law-with-motion` | g10 | `second-law-in-one-dimension`, `choosing-a-motion-equation` |
| Finding apparent weight in an elevator | `apparent-weight` | g10 | `second-law-in-one-dimension` |
| Applying Newton's third law to systems | `third-law-in-systems` | g10 | `second-law-in-one-dimension`, `ms.action-reaction` |
| Solving connected objects on a surface | `connected-objects` | g10 | `third-law-in-systems` |
| Solving hanging pulley systems | `pulley-systems` | g10 | `connected-objects` |
| Resolving forces at an angle | `forces-at-an-angle` | g10 | `second-law-in-one-dimension`, `vector-components-physics` |
| Solving inclined planes without friction | `inclines-without-friction` | g10 | `forces-at-an-angle`, `tilted-axes` |
| Using static friction | `static-friction` | g10 | `first-law-in-one-dimension`, `ms.friction-factors` |
| Using kinetic friction | `kinetic-friction` | g10 | `static-friction`, `second-law-in-one-dimension` |
| Finding a friction coefficient from data | `friction-coefficient-lab` | g10 | `kinetic-friction`, `slope-meaning-in-data` |
| Solving friction with an angled force | `friction-at-an-angle` | g10 | `kinetic-friction`, `forces-at-an-angle` |
| Solving inclined planes with friction | `inclines-with-friction` | g10 | `inclines-without-friction`, `kinetic-friction` |
| Modelling drag and terminal velocity | `drag-and-terminal-velocity` | g10 | `kinetic-friction`, `ms.air-and-water-resistance` |
| Using Hooke's law | `hookes-law` | g10 | `first-law-in-one-dimension`, `slope-meaning-in-data` |
| Comparing springs in series and parallel | `springs-in-combination` | g10 | `hookes-law` |
| Finding center of mass | `center-of-mass` | g10 | `choosing-a-system`, `alg1.equations-with-rational-coefficients` |
| Finding tension in angled ropes | `tension-at-angles` | g10 | `forces-at-an-angle` |
| Solving equilibrium in two dimensions | `equilibrium-in-two-dimensions` | g10 | `tension-at-angles` |

### Circular motion and gravitation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing uniform circular motion | `describing-circular-motion` | g10 | `vector-components-physics`, `geom.circle-terms` |
| Finding period and tangential speed | `period-and-tangential-speed` | g10 | `describing-circular-motion`, `geom.arc-length` |
| Calculating centripetal acceleration | `centripetal-acceleration` | g10 | `period-and-tangential-speed` |
| Identifying the centripetal force | `centripetal-force` | g10 | `centripetal-acceleration`, `second-law-in-one-dimension` |
| Solving a car on a flat curve | `flat-curves` | g10 | `centripetal-force`, `static-friction` |
| Solving banked curves | `banked-curves` | g10 | `flat-curves`, `inclines-without-friction` |
| Solving vertical circles | `vertical-circles` | g10 | `centripetal-force`, `apparent-weight` |
| Using Newton's law of gravitation | `universal-gravitation` | g10 | `ms.gravity-mass-distance`, `rearranging-physics-formulas` |
| Finding gravitational field strength | `field-strength-from-gravitation` | g10 | `universal-gravitation`, `weight-and-field-strength` |
| Analyzing circular orbits | `circular-orbits` | g10 | `universal-gravitation`, `centripetal-force` |
| Using Kepler's third law | `keplers-third-law` | g10 | `circular-orbits` |
| Explaining apparent weightlessness | `apparent-weightlessness` | g10 | `circular-orbits`, `apparent-weight` |

### Work and energy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating work with an angled force | `work-at-an-angle` | g10 | `ms.work`, `forces-at-an-angle` |
| Finding net work from several forces | `net-work` | g10 | `work-at-an-angle` |
| Finding work from a force-distance graph | `work-from-a-graph` | g10 | `net-work`, `displacement-from-area` |
| Using the work-energy theorem | `work-energy-theorem` | g10 | `net-work`, `ms.kinetic-energy-calculation` |
| Using gravitational potential energy in a system | `gravitational-energy-of-a-system` | g10 | `work-energy-theorem`, `ms.gravitational-potential` |
| Calculating elastic potential energy | `elastic-potential-energy` | g10 | `work-from-a-graph`, `hookes-law` |
| Using conservation of mechanical energy | `conserving-mechanical-energy` | g10 | `gravitational-energy-of-a-system`, `ms.energy-conservation` |
| Solving energy problems with springs | `energy-with-springs` | g10 | `conserving-mechanical-energy`, `elastic-potential-energy` |
| Combining energy and circular motion | `energy-in-circular-motion` | g10 | `conserving-mechanical-energy`, `vertical-circles` |
| Reading potential energy graphs | `potential-energy-graphs` | g10 | `energy-with-springs` |
| Calculating mechanical power | `power-from-work` | g10 | `work-energy-theorem`, `ms.power` |
| Finding power from force and velocity | `power-force-velocity` | g10 | `power-from-work` |
| Finding the efficiency of machines | `efficiency-of-machines` | g10 | `power-from-work`, `ms.efficiency` |
| Finding work by gravity and friction | `work-by-gravity-and-friction` | g10 | `net-work`, `kinetic-friction` |
| Solving energy problems with friction | `energy-with-friction` | g10 | `conserving-mechanical-energy`, `work-by-gravity-and-friction` |
| Using energy bar charts for systems | `system-bar-charts` | g10 | `energy-with-friction`, `ms.energy-bar-charts` |

### Momentum

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating momentum | `momentum` | g10 | `second-law-in-one-dimension`, `displacement-with-signs` |
| Using impulse and momentum change | `impulse` | g10 | `momentum` |
| Finding impulse from a force-time graph | `impulse-from-a-graph` | g10 | `impulse`, `displacement-from-area` |
| Designing to reduce impact force | `reducing-impact-force` | g10 | `impulse`, `ms.third-law-collisions` |
| Adding momenta in a system | `momentum-of-a-system` | g10 | `momentum` |
| Using conservation of momentum | `conserving-momentum` | g10 | `impulse`, `third-law-in-systems`, `momentum-of-a-system` |
| Solving recoil and explosions | `recoil-and-explosions` | g10 | `conserving-momentum` |
| Solving perfectly inelastic collisions | `inelastic-collisions` | g10 | `conserving-momentum` |
| Solving elastic collisions | `elastic-collisions` | g10 | `inelastic-collisions`, `work-energy-theorem`, `alg1.systems-review-three-methods` |
| Comparing energy before and after collisions | `energy-lost-in-collisions` | g10 | `inelastic-collisions`, `work-energy-theorem` |
| Solving collisions in two dimensions | `collisions-in-two-dimensions` | g10 | `conserving-momentum`, `adding-by-components` |
| Tracking the center of mass of a system | `motion-of-center-of-mass` | g10 | `conserving-momentum`, `center-of-mass` |
| Combining momentum and energy in one problem | `pendulum-collision` | g10 | `energy-lost-in-collisions`, `conserving-mechanical-energy` |

### Rotation

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Measuring rotation in radians | `angles-in-radians-physics` | g11 | `geom.radians-intro`, `period-and-tangential-speed` |
| Calculating angular velocity | `angular-velocity` | g11 | `angles-in-radians-physics` |
| Calculating angular acceleration | `angular-acceleration` | g11 | `angular-velocity`, `acceleration-with-signs` |
| Using rotational motion equations | `rotational-motion-equations` | g11 | `angular-acceleration`, `choosing-a-motion-equation` |
| Linking linear and angular quantities | `linking-linear-and-angular` | g11 | `angular-velocity`, `geom.arc-length-radian-connection` |
| Calculating torque | `torque` | g11 | `vector-components-physics`, `ms.mechanical-advantage`, `first-law-in-one-dimension` |
| Calculating torque at an angle | `torque-at-an-angle` | g11 | `torque` |
| Comparing rotational inertia | `rotational-inertia` | g11 | `torque`, `center-of-mass` |
| Applying Newton's second law to rotation | `second-law-for-rotation` | g11 | `rotational-inertia`, `angular-acceleration` |
| Calculating rotational kinetic energy | `rotational-kinetic-energy` | g11 | `rotational-inertia`, `angular-velocity`, `work-energy-theorem` |
| Finding work done by a torque | `work-by-torque` | g11 | `rotational-kinetic-energy` |
| Solving rolling without slipping | `rolling` | g11 | `rotational-kinetic-energy`, `linking-linear-and-angular`, `conserving-mechanical-energy` |
| Calculating angular momentum | `angular-momentum` | g11 | `rotational-inertia`, `angular-velocity`, `momentum` |
| Using conservation of angular momentum | `conserving-angular-momentum` | g11 | `angular-momentum` |
| Analyzing satellites with energy and angular momentum | `satellite-energy-and-momentum` | g11 | `conserving-angular-momentum`, `keplers-third-law`, `gravitational-energy-of-a-system` |
| Finding net torque | `net-torque` | g11 | `torque` |
| Solving rotational equilibrium | `rotational-equilibrium` | g11 | `center-of-mass`, `net-torque` |
| Solving beams and ladders | `beams-and-ladders` | g11 | `rotational-equilibrium`, `torque-at-an-angle`, `equilibrium-in-two-dimensions` |
| Writing circular motion in angular form | `circular-motion-in-angular-form` | g11 | `linking-linear-and-angular`, `centripetal-acceleration` |

### Oscillations

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing periodic motion | `periodic-motion` | g10 | `ms.frequency-and-period`, `hookes-law` |
| Testing for simple harmonic motion | `simple-harmonic-conditions` | g10 | `periodic-motion` |
| Finding the period of a mass on a spring | `mass-on-a-spring` | g10 | `simple-harmonic-conditions`, `g8.square-roots` |
| Finding the period of a simple pendulum | `simple-pendulum` | g10 | `simple-harmonic-conditions`, `g8.square-roots` |
| Reading oscillation graphs | `oscillation-graphs` | g10 | `mass-on-a-spring`, `translating-motion-graphs` |
| Tracking energy in an oscillator | `oscillation-energy` | g10 | `mass-on-a-spring`, `energy-with-springs` |
| Describing damping and resonance | `damping-and-resonance` | g10 | `oscillation-energy` |
| Tracking energy in a pendulum | `pendulum-energy` | g10 | `simple-pendulum`, `conserving-mechanical-energy` |

### Mechanical waves

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Telling pulses from periodic waves | `pulses-and-periodic-waves` | g10 | `ms.transverse-and-longitudinal`, `periodic-motion` |
| Finding wave speed on a string | `wave-speed-on-a-string` | g10 | `pulses-and-periodic-waves`, `ms.wave-speed`, `g8.square-roots` |
| Solving wave equation problems | `wave-equation-problems` | g10 | `pulses-and-periodic-waves`, `ms.wave-speed` |
| Reading wave graphs of position and time | `position-and-time-wave-graphs` | g10 | `wave-equation-problems`, `oscillation-graphs` |
| Predicting wave reflection at a boundary | `boundary-behaviour` | g10 | `pulses-and-periodic-waves` |
| Using superposition | `superposition` | g10 | `boundary-behaviour` |
| Finding standing waves on strings | `standing-waves-on-strings` | g10 | `superposition`, `wave-speed-on-a-string` |
| Relating sound speed to the medium | `sound-speed-factors` | g10 | `wave-equation-problems`, `ms.sound-needs-a-medium` |
| Calculating sound intensity with distance | `sound-intensity` | g10 | `sound-speed-factors`, `power-from-work`, `ms.pitch-and-loudness` |
| Finding standing waves in pipes | `open-and-closed-pipes` | g10 | `standing-waves-on-strings`, `sound-speed-factors` |
| Calculating beat frequency | `beats-in-sound` | g10 | `superposition`, `sound-speed-factors` |
| Using the Doppler effect for sound | `doppler-sound` | g10 | `sound-speed-factors`, `relative-velocity-line` |
| Explaining resonance in instruments | `sound-resonance` | g10 | `open-and-closed-pipes`, `damping-and-resonance` |
| Comparing wave phase | `comparing-wave-phase` | g10 | `position-and-time-wave-graphs` |
| Predicting interference from two sources | `two-source-interference` | g10 | `superposition`, `comparing-wave-phase` |

### Fluids

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating density of composite objects | `internal-structure-and-density` | g10 | `ms.density`, `si-units-and-prefixes` |
| Calculating pressure at a depth | `pressure-in-fluids` | g10 | `internal-structure-and-density`, `ms.pressure`, `weight-and-field-strength` |
| Telling gauge from absolute pressure | `gauge-and-absolute-pressure` | g10 | `pressure-in-fluids` |
| Using Pascal's principle | `pascals-principle` | g10 | `pressure-in-fluids`, `ms.mechanical-advantage` |
| Calculating buoyant force | `buoyant-force` | g10 | `pressure-in-fluids`, `ms.floating-and-sinking` |
| Solving floating and submerged object problems | `floating-object-problems` | g10 | `buoyant-force`, `first-law-in-one-dimension` |
| Using barometers and manometers | `barometers-and-manometers` | g10 | `gauge-and-absolute-pressure` |
| Calculating flow rate | `flow-rate` | g10 | `internal-structure-and-density`, `average-velocity` |
| Using the continuity equation | `continuity-equation` | g10 | `flow-rate` |
| Using Bernoulli's equation | `bernoullis-equation` | g10 | `continuity-equation`, `conserving-mechanical-energy`, `pressure-in-fluids` |
| Explaining lift and flow applications | `lift-and-flow-applications` | g10 | `bernoullis-equation` |

## physics.hs2: 165 topics, budget 200

### Thermal physics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Relating temperature to particle energy | `temperature-and-particle-energy` | g11 | `ms.heat-vs-temperature`, `hs1.work-energy-theorem` |
| Using absolute temperature | `absolute-temperature` | g11 | `temperature-and-particle-energy` |
| Calculating thermal expansion | `thermal-expansion` | g11 | `absolute-temperature` |
| Calculating with specific heat | `specific-heat` | g11 | `ms.heat-capacity-factors`, `hs1.rearranging-physics-formulas` |
| Solving calorimetry problems | `calorimetry` | g11 | `specific-heat`, `ms.thermal-equilibrium` |
| Calculating with latent heat | `latent-heat` | g11 | `specific-heat` |
| Reading heating curves | `heating-curves` | g11 | `latent-heat`, `calorimetry` |
| Calculating the rate of thermal conduction | `conduction-rate` | g11 | `specific-heat`, `ms.thermal-insulation`, `hs1.power-from-work` |
| Comparing thermal radiation with temperature | `radiation-rate` | g11 | `conduction-rate`, `absolute-temperature` |
| Using the ideal gas law | `ideal-gas-law` | g11 | `absolute-temperature`, `hs1.pressure-in-fluids` |
| Solving gas problems with two states | `gas-law-relationships` | g11 | `ideal-gas-law`, `alg2.inverse-variation` |
| Explaining gas pressure with kinetic theory | `kinetic-theory-of-gases` | g11 | `ideal-gas-law`, `hs1.impulse` |
| Defining internal energy | `internal-energy` | g11 | `kinetic-theory-of-gases`, `hs1.system-bar-charts` |
| Using the first law of thermodynamics | `first-law-of-thermodynamics` | g11 | `internal-energy`, `calorimetry` |
| Using sign conventions in the first law | `first-law-signs` | g11 | `first-law-of-thermodynamics` |
| Reading pressure-volume diagrams | `pressure-volume-diagrams` | g11 | `gas-law-relationships` |
| Finding work on a gas from a pressure-volume graph | `work-on-a-gas` | g11 | `hs1.work-from-a-graph`, `first-law-signs`, `pressure-volume-diagrams` |
| Analyzing constant-pressure, volume and temperature processes | `thermal-processes` | g11 | `work-on-a-gas` |
| Analyzing a thermal cycle | `thermal-cycles` | g11 | `thermal-processes` |
| Analyzing heat engines | `heat-engines` | g11 | `hs1.efficiency-of-machines`, `thermal-cycles` |
| Finding the maximum engine efficiency | `carnot-limit` | g11 | `heat-engines` |
| Explaining entropy and the second law | `entropy-and-second-law` | g11 | `heat-engines` |
| Analyzing refrigerators and heat pumps | `refrigerators-and-heat-pumps` | g11 | `heat-engines` |
| Solving calorimetry with a phase change | `calorimetry-with-phase-change` | g11 | `calorimetry`, `latent-heat` |

### Electric charge and fields

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using conservation of charge | `charge-conservation` | g11 | `ms.electric-charge` |
| Explaining charging by friction, contact and induction | `charging-processes` | g11 | `charge-conservation`, `ms.current-and-voltage` |
| Using Coulomb's law | `coulombs-law` | g11 | `charge-conservation`, `hs1.universal-gravitation` |
| Adding electric forces along a line | `coulomb-forces-on-a-line` | g11 | `coulombs-law`, `hs1.second-law-in-one-dimension` |
| Adding electric forces in a plane | `coulomb-forces-in-a-plane` | g11 | `coulomb-forces-on-a-line`, `hs1.adding-by-components` |
| Defining the electric field | `electric-field-concept` | g11 | `coulombs-law`, `ms.fields-at-a-distance` |
| Calculating the field of a point charge | `field-of-a-point-charge` | g11 | `electric-field-concept` |
| Adding electric fields | `adding-electric-fields` | g11 | `field-of-a-point-charge`, `hs1.adding-by-components` |
| Drawing electric field lines | `field-lines` | g11 | `field-of-a-point-charge` |
| Using uniform electric fields | `uniform-electric-field` | g11 | `field-lines`, `hs1.second-law-with-motion` |
| Solving charged particle motion in a uniform field | `charge-in-a-field` | g11 | `uniform-electric-field`, `hs1.horizontal-launch` |
| Calculating electric potential energy | `electric-potential-energy` | g11 | `uniform-electric-field`, `hs1.gravitational-energy-of-a-system` |
| Defining electric potential and potential difference | `electric-potential` | g11 | `electric-potential-energy`, `ms.current-and-voltage` |
| Calculating potential of point charges | `potential-of-point-charges` | g11 | `electric-potential` |
| Finding charge from a balanced oil drop | `millikan-idea` | g11 | `uniform-electric-field` |
| Comparing gravitational and electric forces | `gravity-electric-comparison` | g11 | `coulombs-law`, `hs1.field-strength-from-gravitation` |
| Describing electric dipoles | `electric-dipoles` | g11 | `adding-electric-fields` |
| Finding where an electric field is zero | `zero-field-points` | g11 | `adding-electric-fields` |
| Relating field to potential difference | `field-and-potential-difference` | g11 | `electric-potential` |
| Accelerating charges through a potential difference | `accelerating-charges` | g11 | `hs1.conserving-mechanical-energy`, `field-and-potential-difference` |
| Calculating potential energy of charge pairs | `potential-energy-of-charges` | g11 | `potential-of-point-charges` |
| Finding work done moving a charge | `work-moving-a-charge` | g11 | `electric-potential` |
| Drawing equipotential lines | `equipotential-lines` | g11 | `work-moving-a-charge` |
| Explaining charge on conductors | `conductors-in-equilibrium` | g11 | `equipotential-lines`, `charging-processes` |
| Finding charge shared between conductors | `sharing-charge` | g11 | `conductors-in-equilibrium` |

### Capacitors

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Defining capacitance | `capacitance` | g11 | `conductors-in-equilibrium`, `field-and-potential-difference` |
| Calculating parallel-plate capacitance | `parallel-plate-capacitors` | g11 | `capacitance` |
| Explaining dielectrics | `dielectrics` | g11 | `parallel-plate-capacitors` |
| Calculating capacitor energy | `capacitor-energy` | g11 | `capacitance`, `hs1.work-from-a-graph` |
| Combining capacitors | `capacitors-in-circuits` | g11 | `capacitance`, `alg2.add-subtract-rational` |

### Direct current circuits

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating current from charge flow | `current-as-charge-flow` | g11 | `ms.current-and-voltage`, `charge-conservation` |
| Calculating resistance from resistivity | `resistivity` | g11 | `current-as-charge-flow`, `ms.resistance` |
| Telling ohmic from non-ohmic devices | `ohmic-devices` | g11 | `resistivity`, `ms.ohms-law`, `hs1.slope-meaning-in-data` |
| Calculating power in circuit elements | `electric-power` | g11 | `ohmic-devices`, `ms.electric-power-and-cost` |
| Drawing and reading circuit diagrams | `circuit-diagrams` | g11 | `ms.measuring-circuits` |
| Solving series resistors | `series-resistors` | g11 | `ohmic-devices`, `ms.series-circuits`, `circuit-diagrams` |
| Solving parallel resistors | `parallel-resistors` | g11 | `series-resistors`, `ms.parallel-circuits`, `alg2.add-subtract-rational` |
| Explaining household circuits and safety | `household-circuits` | g11 | `electric-power`, `parallel-resistors` |
| Finding equivalent resistance by reduction | `equivalent-resistance` | g11 | `parallel-resistors` |
| Solving combination circuits | `combination-circuits` | g11 | `equivalent-resistance` |
| Comparing brightness and power in circuits | `power-in-combination-circuits` | g11 | `combination-circuits`, `electric-power` |
| Modelling meters in circuits | `using-meters-in-circuits` | g11 | `combination-circuits` |
| Using emf and internal resistance | `emf-and-internal-resistance` | g11 | `combination-circuits` |
| Using Kirchhoff's junction rule | `junction-rule` | g11 | `combination-circuits` |
| Using Kirchhoff's loop rule | `loop-rule` | g11 | `combination-circuits`, `electric-potential` |
| Solving multi-loop circuits | `multi-loop-circuits` | g11 | `junction-rule`, `loop-rule`, `alg2.systems-three-variables` |
| Describing a charging capacitor | `capacitor-charging` | g11 | `capacitors-in-circuits`, `combination-circuits` |
| Finding drift velocity | `drift-velocity` | g11 | `current-as-charge-flow` |
| Relating resistance to temperature | `temperature-and-resistance` | g11 | `resistivity` |
| Using voltage dividers | `voltage-dividers` | g11 | `series-resistors` |
| Describing a discharging capacitor | `capacitor-discharging` | g11 | `capacitor-charging` |
| Calculating an RC time constant | `rc-time-constant` | g11 | `alg2.graph-transformed-exponentials`, `capacitor-discharging` |

### Magnetism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing magnetic field sources | `magnetic-field-sources` | g11 | `ms.magnetic-fields`, `electric-field-concept` |
| Calculating force on a moving charge | `force-on-a-moving-charge` | g11 | `magnetic-field-sources`, `hs1.vector-components-physics` |
| Using right-hand rules | `right-hand-rules` | g11 | `force-on-a-moving-charge` |
| Finding a charge's circular path in a field | `circular-path-in-a-field` | g11 | `right-hand-rules`, `hs1.centripetal-force` |
| Solving crossed electric and magnetic fields | `crossed-fields` | g11 | `right-hand-rules`, `uniform-electric-field` |
| Calculating force on a current-carrying wire | `force-on-a-wire` | g11 | `right-hand-rules`, `current-as-charge-flow` |
| Calculating the field of a long wire | `field-of-a-wire` | g11 | `magnetic-field-sources`, `current-as-charge-flow` |
| Finding the force between parallel wires | `force-between-wires` | g11 | `field-of-a-wire`, `force-on-a-wire` |
| Calculating the field of a solenoid | `field-of-a-solenoid` | g11 | `field-of-a-wire`, `ms.electromagnets` |
| Calculating torque on a current loop | `motor-torque` | g11 | `force-on-a-wire`, `hs1.torque`, `ms.motors` |
| Analyzing a mass spectrometer | `mass-spectrometer` | g11 | `circular-path-in-a-field`, `crossed-fields` |
| Adding fields of several wires | `adding-magnetic-fields` | g11 | `field-of-a-wire`, `hs1.adding-by-components` |

### Electromagnetic induction

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating magnetic flux | `magnetic-flux` | g11 | `magnetic-field-sources`, `hs1.vector-components-physics` |
| Using Faraday's law | `faradays-law` | g11 | `magnetic-flux`, `ms.generators` |
| Using Lenz's law | `lenzs-law` | g11 | `faradays-law`, `right-hand-rules` |
| Calculating motional emf | `motional-emf` | g11 | `faradays-law`, `force-on-a-wire` |
| Describing self-inductance | `self-inductance-intro` | g11 | `lenzs-law`, `capacitor-charging` |
| Graphing flux and induced emf | `flux-and-emf-graphs` | g11 | `faradays-law` |
| Graphing generator output | `generators-output` | g11 | `alg2.graph-sine-cosine`, `flux-and-emf-graphs` |
| Using peak and effective alternating current | `alternating-current` | g11 | `generators-output`, `electric-power` |
| Using transformers | `transformers` | g11 | `alternating-current` |
| Explaining power transmission | `power-transmission` | g11 | `transformers`, `household-circuits` |
| Explaining eddy currents | `eddy-currents` | g11 | `lenzs-law` |

### Electromagnetic waves and geometric optics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing electromagnetic waves | `electromagnetic-wave-nature` | g11 | `faradays-law`, `ms.electromagnetic-spectrum`, `hs1.wave-equation-problems` |
| Evaluating health effects of radiation | `radiation-and-health` | g11 | `electromagnetic-wave-nature` |
| Explaining polarization | `polarization` | g11 | `electromagnetic-wave-nature` |
| Evaluating digital transmission and storage | `digital-transmission` | g11 | `electromagnetic-wave-nature`, `ms.digital-signals` |
| Using the ray model of light | `ray-model` | g11 | `ms.reflection-of-light` |
| Finding images in plane mirrors | `plane-mirror-images` | g11 | `ray-model` |
| Drawing rays for curved mirrors | `curved-mirror-rays` | g11 | `plane-mirror-images`, `geom.circle-terms` |
| Using the mirror equation | `mirror-equation` | g11 | `curved-mirror-rays`, `alg2.solve-rational-equations` |
| Calculating magnification | `magnification` | g11 | `mirror-equation` |
| Using index of refraction | `index-of-refraction` | g12 | `ms.refraction`, `hs1.wave-equation-problems` |
| Using Snell's law | `snells-law` | g12 | `geom.trig-find-angle`, `index-of-refraction` |
| Finding total internal reflection | `total-internal-reflection` | g12 | `snells-law` |
| Explaining dispersion and prisms | `dispersion-and-prisms` | g12 | `snells-law`, `ms.color` |
| Drawing lens ray diagrams | `lens-ray-diagrams` | g12 | `snells-law`, `ms.lenses` |
| Using the thin lens equation | `thin-lens-equation` | g12 | `lens-ray-diagrams`, `mirror-equation` |
| Solving two-lens systems | `lens-combinations` | g12 | `thin-lens-equation`, `magnification` |
| Explaining the eye and corrective lenses | `eye-and-corrective-lenses` | g12 | `thin-lens-equation` |
| Finding wavelength in a medium | `wavelength-in-a-medium` | g12 | `index-of-refraction` |
| Explaining optical fibres | `optical-fibres` | g12 | `total-internal-reflection` |
| Analyzing microscopes and telescopes | `optical-instruments` | g12 | `lens-combinations` |

### Wave optics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Using evidence for light as a wave | `light-as-a-wave-evidence` | g12 | `hs1.two-source-interference`, `electromagnetic-wave-nature` |
| Using double-slit interference | `double-slit` | g12 | `light-as-a-wave-evidence`, `geom.trig-find-angle` |
| Using diffraction gratings | `diffraction-gratings` | g12 | `double-slit` |
| Using single-slit diffraction | `single-slit` | g12 | `double-slit` |
| Explaining the limit of resolution | `resolution-limit` | g12 | `single-slit` |
| Explaining thin-film interference | `thin-film-interference` | g12 | `light-as-a-wave-evidence`, `snells-law` |
| Explaining the Doppler effect for light | `doppler-light` | g12 | `hs1.doppler-sound`, `electromagnetic-wave-nature` |

### Quantum and atomic physics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining blackbody radiation | `blackbody-radiation` | g12 | `radiation-rate`, `electromagnetic-wave-nature` |
| Calculating photon energy | `photon-energy` | g12 | `electromagnetic-wave-nature`, `ms.light-wave-and-particle` |
| Using electron volts | `electron-volts` | g12 | `photon-energy`, `accelerating-charges` |
| Explaining the photoelectric effect | `photoelectric-effect` | g12 | `electron-volts` |
| Finding work function from stopping potential | `stopping-potential` | g12 | `photoelectric-effect` |
| Calculating de Broglie wavelength | `de-broglie-wavelength` | g12 | `photon-energy`, `hs1.momentum` |
| Using the Bohr model | `bohr-model` | g12 | `electron-volts`, `hs1.centripetal-force` |
| Reading energy level diagrams | `energy-level-diagrams` | g12 | `bohr-model` |
| Explaining emission and absorption spectra | `emission-and-absorption` | g12 | `energy-level-diagrams` |
| Explaining how lasers work | `lasers` | g12 | `emission-and-absorption` |
| Calculating photon momentum | `photon-momentum` | g12 | `photon-energy` |
| Explaining Compton scattering | `compton-scattering` | g12 | `hs1.collisions-in-two-dimensions`, `photon-momentum` |
| Finding photons per second from power | `photon-rate` | g12 | `photon-energy`, `hs1.power-from-work` |
| Using electron diffraction as evidence | `electron-diffraction` | g12 | `de-broglie-wavelength` |
| Explaining wave-particle duality | `wave-particle-duality` | g12 | `photoelectric-effect`, `double-slit`, `electron-diffraction` |
| Describing the uncertainty principle | `uncertainty-idea` | g12 | `wave-particle-duality` |
| Finding hydrogen spectral lines | `hydrogen-spectrum` | g12 | `emission-and-absorption` |

### Nuclear physics

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading nuclear notation | `nuclear-notation` | g12 | `bohr-model` |
| Explaining nuclear stability | `strong-force` | g12 | `nuclear-notation` |
| Using mass-energy equivalence | `mass-energy` | g12 | `nuclear-notation` |
| Calculating binding energy | `binding-energy` | g12 | `mass-energy`, `strong-force` |
| Comparing alpha, beta and gamma radiation | `alpha-beta-gamma` | g12 | `strong-force` |
| Balancing nuclear decay equations | `decay-equations` | g12 | `alpha-beta-gamma` |
| Calculating with half-life | `half-life` | g12 | `decay-equations`, `alg2.solve-exponential-with-logs` |
| Evaluating radiation dose and safety | `radiation-dose` | g12 | `alpha-beta-gamma`, `radiation-and-health` |
| Introducing fundamental particles | `particles-intro` | g12 | `strong-force` |
| Reading the binding energy curve | `binding-energy-curve` | g12 | `binding-energy` |
| Explaining and calculating fission | `fission` | g12 | `decay-equations`, `binding-energy-curve` |
| Explaining and calculating fusion | `fusion` | g12 | `binding-energy-curve` |
| Following decay chains | `decay-chains` | g12 | `decay-equations` |
| Graphing decay curves | `decay-curves` | g12 | `half-life`, `alg2.graph-transformed-exponentials` |
| Using decay activity and dating | `activity-and-dating` | g12 | `decay-curves` |
| Explaining nuclear reactors | `nuclear-reactors` | g12 | `fission` |

### Special relativity

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Stating the postulates of special relativity | `relativity-postulates` | g12 | `hs1.relative-velocity-line`, `electromagnetic-wave-nature` |
| Explaining relativity of simultaneity | `simultaneity` | g12 | `relativity-postulates` |
| Deriving time dilation with a light clock | `light-clock` | g12 | `relativity-postulates` |
| Calculating time dilation | `time-dilation` | g12 | `simultaneity`, `alg2.radical-word-problems`, `light-clock` |
| Calculating length contraction | `length-contraction` | g12 | `time-dilation` |
| Comparing relativistic momentum and energy | `relativistic-energy` | g12 | `length-contraction`, `mass-energy` |
