# Topic lists: physics.elem and physics.ms

Draft for approval. In the Needs column, a plain name is in the same course, `elem.` names `physics.elem`, and a prefix such as `g7.` names a math course.
## Proposed manifest change

`physics.elem` gains `follows: math.g4`, so it can use grade-level measurement skills. It currently follows nothing, so it could not link to math at all.


## physics.elem: 42 topics, budget 40

### Pushes and motion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Telling pushes from pulls | `pushes-and-pulls` | gk |  |
| Comparing strong and gentle pushes | `strength-of-a-push` | gk | `pushes-and-pulls` |
| Changing direction with a push | `direction-of-a-push` | gk | `pushes-and-pulls` |
| Comparing fast and slow motion | `fast-and-slow` | gk | `pushes-and-pulls`, `k.compare-lengths` |
| Seeing what happens when objects bump | `bumping-objects` | g1 | `strength-of-a-push`, `direction-of-a-push` |

### Light and sound

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming sources of light and sound | `sources-of-light-and-sound` | gk |  |
| Seeing that sunlight warms things | `sunlight-warms` | gk | `sources-of-light-and-sound` |
| Linking sound to vibration | `sound-from-vibration` | g1 | `sources-of-light-and-sound` |
| Showing sound can make things vibrate | `sound-makes-vibration` | g1 | `sound-from-vibration` |
| Showing we need light to see | `seeing-needs-light` | g1 | `sources-of-light-and-sound` |
| Testing what light passes through | `materials-and-light` | g1 | `seeing-needs-light` |
| Making and changing shadows | `shadows` | g1 | `materials-and-light` |
| Redirecting light with a mirror | `mirrors-redirect-light` | g1 | `seeing-needs-light` |
| Sending signals with light and sound | `signals-with-light-sound` | g1 | `sound-from-vibration`, `seeing-needs-light` |

### Forces

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Starting and stopping motion with forces | `forces-start-and-stop` | g2 | `bumping-objects` |
| Telling contact from non-contact forces | `contact-and-noncontact` | g2 | `forces-start-and-stop` |
| Comparing friction on different surfaces | `friction-on-surfaces` | g2 | `forces-start-and-stop` |
| Measuring distance and time for motion | `measuring-motion` | g3 | `fast-and-slow`, `g2.measure-with-a-ruler`, `g3.measure-time-intervals` |
| Telling balanced from unbalanced forces | `balanced-and-unbalanced` | g3 | `forces-start-and-stop` |
| Predicting a repeating motion | `predicting-repeating-motion` | g3 | `measuring-motion` |
| Testing what magnets attract | `magnets-attract` | g3 | `contact-and-noncontact` |
| Testing magnet poles | `magnet-poles` | g3 | `magnets-attract` |
| Testing how distance changes a magnet's pull | `magnet-distance` | g3 | `magnets-attract`, `g2.measure-with-a-ruler` |
| Seeing static attraction and repulsion | `static-electricity` | g3 | `contact-and-noncontact` |

### Energy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming sources of heat | `sources-of-heat` | g2 | `sunlight-warms` |
| Showing heat moves from warm to cool | `heat-moves` | g2 | `sources-of-heat` |
| Relating energy to speed | `energy-and-speed` | g4 | `forces-start-and-stop`, `measuring-motion` |
| Predicting energy changes in collisions | `energy-in-collisions` | g4 | `energy-and-speed` |
| Tracing energy through sound, light, heat and current | `energy-moves-between-places` | g4 | `energy-and-speed`, `heat-moves`, `sound-from-vibration` |
| Building a simple circuit | `simple-circuits` | g4 | `energy-moves-between-places` |
| Testing electrical conductors and insulators | `conductors-and-insulators` | g4 | `simple-circuits` |
| Finding energy changes in devices | `devices-transform-energy` | g4 | `simple-circuits` |
| Comparing energy sources | `energy-sources-compared` | g4 | `devices-transform-energy` |

### Waves

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing waves by amplitude and wavelength | `wave-patterns` | g4 | `sound-makes-vibration`, `g2.measure-with-a-ruler` |
| Showing waves can move objects | `waves-move-objects` | g4 | `wave-patterns` |
| Explaining sight with reflected light | `reflected-light-and-eyes` | g4 | `mirrors-redirect-light`, `materials-and-light` |
| Sending information with coded patterns | `coded-signals` | g4 | `signals-with-light-sound`, `wave-patterns` |

### Gravity and machines

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Showing gravity pulls objects down | `gravity-pulls-down` | g5 | `contact-and-noncontact` |
| Telling mass from weight | `mass-and-weight-intro` | g5 | `gravity-pulls-down`, `g3.estimate-mass-capacity` |
| Using levers to change a force | `levers` | g5 | `balanced-and-unbalanced`, `g2.measure-with-a-ruler` |
| Using ramps and pulleys to change a force | `ramps-and-pulleys` | g5 | `levers`, `friction-on-surfaces` |
| Comparing speeds from distance and time | `comparing-speeds` | g5 | `measuring-motion`, `g4.distance-time-stories` |

## physics.ms: 77 topics, budget 80

### Motion

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing position from a reference point | `position-and-reference` | g6 | `elem.measuring-motion`, `g5.coordinate-plane` |
| Telling distance from displacement | `distance-and-displacement` | g6 | `position-and-reference`, `g6.negative-numbers-in-context` |
| Calculating speed in metres per second | `speed-as-a-rate` | g6 | `elem.comparing-speeds`, `g6.constant-speed` |
| Finding average speed for a trip | `average-speed` | g6 | `speed-as-a-rate` |
| Converting between metres per second and kilometres per hour | `unit-conversions-speed` | g7 | `speed-as-a-rate`, `g7.convert-between-unit-rates` |
| Telling velocity from speed | `velocity-with-direction` | g6 | `speed-as-a-rate`, `distance-and-displacement` |
| Drawing distance-time graphs | `distance-time-graphs` | g7 | `average-speed`, `g6.line-graphs` |
| Reading speed from a distance-time graph | `slope-as-speed` | g7 | `distance-time-graphs`, `g7.identify-unit-rate-on-graph` |
| Calculating acceleration | `acceleration-intro` | g7 | `velocity-with-direction`, `g7.rates-with-fractions` |
| Reading speed-time graphs | `speed-time-graphs` | g7 | `acceleration-intro`, `slope-as-speed` |
| Describing motion from different viewpoints | `relative-motion` | g7 | `velocity-with-direction` |

### Forces

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Describing forces as interactions | `forces-as-interactions` | g6 | `elem.balanced-and-unbalanced` |
| Measuring force in newtons | `newtons-and-spring-scales` | g6 | `forces-as-interactions`, `g3.read-measuring-scales` |
| Drawing force diagrams | `force-diagrams` | g6 | `forces-as-interactions` |
| Finding net force along a line | `net-force` | g7 | `force-diagrams`, `newtons-and-spring-scales`, `g7.add-integers-different-sign` |
| Explaining inertia and Newton's first law | `inertia` | g7 | `net-force`, `velocity-with-direction` |
| Relating force, mass and acceleration | `force-mass-acceleration` | g7 | `net-force`, `acceleration-intro` |
| Calculating with Newton's second law | `calculating-with-second-law` | g7 | `force-mass-acceleration`, `g7.one-step-rational-equations` |
| Finding action-reaction pairs | `action-reaction` | g7 | `inertia` |
| Applying Newton's third law to collisions | `third-law-collisions` | g7 | `action-reaction`, `elem.energy-in-collisions` |
| Testing what affects friction | `friction-factors` | g7 | `net-force`, `elem.friction-on-surfaces` |
| Explaining air and water resistance | `air-and-water-resistance` | g7 | `friction-factors` |
| Relating gravity to mass and distance | `gravity-mass-distance` | g7 | `elem.gravity-pulls-down`, `forces-as-interactions` |
| Calculating weight from mass | `weight-calculation` | g7 | `gravity-mass-distance`, `elem.mass-and-weight-intro`, `g7.proportional-equations` |
| Describing free fall | `free-fall` | g7 | `weight-calculation`, `force-mass-acceleration`, `air-and-water-resistance` |
| Calculating pressure | `pressure` | g8 | `newtons-and-spring-scales`, `g7.rates-with-fractions` |
| Calculating density | `density` | g7 | `g5.volume-formulas`, `g6.unit-rates` |
| Predicting floating and sinking | `floating-and-sinking` | g8 | `density`, `net-force`, `pressure` |
| Showing fields act at a distance | `fields-at-a-distance` | g8 | `gravity-mass-distance`, `elem.magnet-distance` |

### Work, energy and machines

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Calculating work in joules | `work` | g7 | `calculating-with-second-law`, `g6.formulas` |
| Finding mechanical advantage | `mechanical-advantage` | g7 | `work`, `elem.ramps-and-pulleys` |
| Calculating power in watts | `power` | g7 | `work` |
| Relating kinetic energy to mass and speed | `kinetic-energy-patterns` | g8 | `elem.energy-and-speed`, `speed-as-a-rate`, `g6.evaluate-with-exponents` |
| Calculating kinetic energy | `kinetic-energy-calculation` | g8 | `kinetic-energy-patterns`, `g7.evaluate-rational-expressions` |
| Calculating gravitational potential energy | `gravitational-potential` | g8 | `work`, `weight-calculation` |
| Describing elastic and other stored energy | `elastic-and-stored-energy` | g8 | `gravitational-potential`, `fields-at-a-distance` |
| Tracing energy transformations | `energy-transformations` | g8 | `kinetic-energy-patterns`, `gravitational-potential`, `elem.devices-transform-energy` |
| Using conservation of energy | `energy-conservation` | g8 | `energy-transformations`, `kinetic-energy-calculation` |
| Drawing energy bar charts | `energy-bar-charts` | g8 | `energy-conservation` |
| Calculating efficiency | `efficiency` | g8 | `energy-conservation`, `g7.percent-equation` |
| Comparing energy resources | `energy-resources` | g8 | `efficiency`, `elem.energy-sources-compared` |

### Thermal energy

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Reading temperature scales | `temperature-scales` | g7 | `elem.heat-moves`, `g7.integers-in-temperature-money` |
| Telling heat from temperature | `heat-vs-temperature` | g8 | `temperature-scales`, `kinetic-energy-patterns` |
| Explaining conduction | `conduction` | g7 | `temperature-scales` |
| Explaining convection | `convection` | g7 | `conduction`, `density` |
| Explaining thermal radiation | `thermal-radiation` | g7 | `conduction` |
| Designing to reduce heat flow | `thermal-insulation` | g8 | `convection`, `thermal-radiation` |
| Testing how mass and material affect heating | `heat-capacity-factors` | g8 | `heat-vs-temperature`, `g7.test-proportional-table` |
| Predicting a final temperature | `thermal-equilibrium` | g8 | `heat-capacity-factors` |

### Waves and light

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Naming parts of a wave | `wave-parts` | g6 | `elem.wave-patterns` |
| Telling transverse from longitudinal waves | `transverse-and-longitudinal` | g6 | `wave-parts` |
| Finding frequency and period | `frequency-and-period` | g7 | `wave-parts`, `g6.unit-rates` |
| Calculating wave speed | `wave-speed` | g7 | `frequency-and-period`, `speed-as-a-rate`, `g7.proportional-equations` |
| Relating amplitude to wave energy | `amplitude-and-energy` | g7 | `wave-parts`, `elem.waves-move-objects` |
| Explaining how sound travels | `sound-needs-a-medium` | g7 | `transverse-and-longitudinal` |
| Relating pitch and loudness to a wave | `pitch-and-loudness` | g7 | `sound-needs-a-medium`, `frequency-and-period`, `amplitude-and-energy` |
| Using echoes to find distance | `echoes` | g7 | `sound-needs-a-medium`, `wave-speed` |
| Using the law of reflection | `reflection-of-light` | g7 | `elem.reflected-light-and-eyes`, `g7.angle-pairs` |
| Explaining refraction | `refraction` | g8 | `reflection-of-light`, `wave-speed` |
| Forming images with lenses | `lenses` | g8 | `refraction` |
| Predicting absorption, reflection and transmission | `absorption-and-transmission` | g8 | `reflection-of-light` |
| Explaining colour | `color` | g8 | `absorption-and-transmission`, `frequency-and-period` |
| Ordering the electromagnetic spectrum | `electromagnetic-spectrum` | g8 | `color`, `wave-speed` |
| Describing light as wave and particle | `light-wave-and-particle` | g8 | `electromagnetic-spectrum` |
| Comparing digital and analog signals | `digital-signals` | g8 | `elem.coded-signals`, `wave-parts` |

### Electricity and magnetism

| Topic | Slug | Level | Needs |
|---|---|---|---|
| Explaining electric charge | `electric-charge` | g7 | `elem.static-electricity`, `forces-as-interactions` |
| Describing current and voltage | `current-and-voltage` | g7 | `electric-charge`, `elem.simple-circuits` |
| Measuring current and voltage | `measuring-circuits` | g7 | `current-and-voltage`, `g3.read-measuring-scales` |
| Building and analyzing series circuits | `series-circuits` | g8 | `measuring-circuits` |
| Building and analyzing parallel circuits | `parallel-circuits` | g8 | `series-circuits` |
| Explaining resistance | `resistance` | g8 | `measuring-circuits`, `elem.conductors-and-insulators` |
| Calculating with Ohm's law | `ohms-law` | g8 | `resistance`, `g7.one-step-rational-equations` |
| Calculating electric power and cost | `electric-power-and-cost` | g8 | `ohms-law`, `power` |
| Mapping magnetic fields | `magnetic-fields` | g8 | `elem.magnet-poles`, `fields-at-a-distance` |
| Building and testing an electromagnet | `electromagnets` | g8 | `magnetic-fields`, `current-and-voltage` |
| Explaining electric motors | `motors` | g8 | `electromagnets`, `energy-transformations` |
| Explaining electric generators | `generators` | g8 | `motors` |
