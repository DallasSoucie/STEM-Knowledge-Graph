# Topic lists: university math

Draft for approval. In the Needs column, a plain name is a topic in the same course, and a prefix such as `calc1.` names another course. Needs implied through another listed need are left out here and become `encompassed` entries when the course is written.

## Proposed manifest changes

| Course | `follows` now | `follows` proposed | Why |
|---|---|---|---|
| `math.diffeq` | calc2 | calc3, linalg | Systems use eigenvalues; exact equations and linearization use partial derivatives |
| `math.probstat` | calc2 | calc3, stats | Joint distributions use multiple integrals; inference builds on the statistics course |
| `math.numerical` | calc2, linalg | calc3, linalg | Newton's method for systems, multiple integrals and gradient descent use multivariable calculus |

## math.calc1: 150 topics, budget 180 (-17%)

### Limits

| Topic | Slug | Needs |
|---|---|---|
| Defining a limit informally | `limit-definition-informal` | `precalc.limit-intuition` |
| Reading limits from graphs | `limits-from-graphs` | `limit-definition-informal` |
| Estimating limits from tables | `limits-from-tables` | `limit-definition-informal` |
| Using one-sided limit notation | `one-sided-limit-notation` | `limits-from-graphs`, `precalc.one-sided-limits` |
| Using the limit laws | `limit-laws` | `limit-definition-informal` |
| Finding limits by direct substitution | `limits-by-substitution` | `limit-laws` |
| Finding limits by factoring | `limits-by-factoring` | `limits-by-substitution`, `precalc.limits-algebraic-simple` |
| Finding limits with conjugates | `limits-by-conjugates` | `limits-by-factoring`, `alg2.radical-conjugate` |
| Finding limits by combining fractions | `limits-of-complex-fractions` | `limits-by-factoring`, `alg2.complex-fractions` |
| Finding limits with absolute values | `limits-of-absolute-value` | `one-sided-limit-notation`, `alg2.absolute-value-as-piecewise` |
| Using the squeeze theorem | `squeeze-theorem` | `limits-by-substitution` |
| Finding the limit of sin x over x | `sinx-over-x` | `squeeze-theorem`, `precalc.unit-circle-fluency` |
| Finding trigonometric limits | `trig-limits` | `sinx-over-x` |
| Finding infinite limits and vertical asymptotes | `infinite-limits` | `one-sided-limit-notation` |
| Finding limits at infinity of rational functions | `limits-at-infinity-rational` | `limits-by-substitution`, `precalc.limits-at-infinity` |
| Finding limits at infinity with roots | `limits-at-infinity-roots` | `limits-at-infinity-rational` |
| Finding limits at infinity of exponentials and logs | `limits-at-infinity-exp-log` | `limits-at-infinity-rational`, `precalc.exponential-compare-growth-rates` |
| Finding horizontal asymptotes with limits | `horizontal-asymptotes-limits` | `limits-at-infinity-rational` |
| Understanding the epsilon-delta definition | `epsilon-delta-intro` | `limit-laws` |
| Proving a linear limit with epsilon and delta | `epsilon-delta-linear` | `epsilon-delta-intro` |
| Deciding if a limit exists from one-sided limits | `limit-existence-from-one-sided` | `one-sided-limit-notation` |
| Finding limits of piecewise functions | `limits-of-piecewise` | `limit-existence-from-one-sided` |
| Finding limits of composite functions | `limits-of-composite-functions` | `limits-by-substitution` |
| Choosing a constant so a limit exists | `limits-with-parameters` | `limits-by-factoring` |
| Proving a quadratic limit with epsilon and delta | `epsilon-delta-quadratic` | `epsilon-delta-linear` |

### Continuity

| Topic | Slug | Needs |
|---|---|---|
| Testing continuity at a point | `continuity-at-a-point` | `limits-of-piecewise`, `precalc.continuity-from-limits` |
| Classifying discontinuities | `types-of-discontinuity` | `continuity-at-a-point` |
| Finding intervals of continuity | `continuity-on-intervals` | `continuity-at-a-point` |
| Choosing a value to make a function continuous | `make-function-continuous` | `limits-with-parameters`, `types-of-discontinuity` |
| Using continuity of compositions | `continuity-of-compositions` | `continuity-on-intervals`, `limits-of-composite-functions` |
| Using the intermediate value theorem | `intermediate-value-applications` | `continuity-on-intervals`, `precalc.intermediate-value-theorem` |

### Defining the derivative

| Topic | Slug | Needs |
|---|---|---|
| Moving from average to instantaneous rate | `average-to-instantaneous` | `limit-definition-informal`, `precalc.rate-of-change-intuition` |
| Defining the tangent line as a limit | `tangent-as-limit` | `average-to-instantaneous`, `precalc.tangent-line-intuition` |
| Finding the derivative at a point from the definition | `derivative-at-a-point` | `tangent-as-limit` |
| Finding the derivative function from the definition | `derivative-as-function` | `derivative-at-a-point` |
| Using the definition for root and reciprocal functions | `derivative-of-root-and-reciprocal` | `derivative-as-function`, `limits-by-conjugates`, `limits-of-complex-fractions` |
| Using derivative notation | `derivative-notation` | `derivative-as-function` |
| Interpreting a derivative with units | `interpret-derivative-units` | `derivative-at-a-point` |
| Estimating a derivative from a table or graph | `estimate-derivative-table` | `derivative-at-a-point` |
| Sketching a derivative from a graph | `sketch-derivative-graph` | `derivative-as-function` |
| Writing the equation of a tangent line | `tangent-line-equation` | `derivative-at-a-point` |
| Writing the equation of a normal line | `normal-line` | `tangent-line-equation`, `alg1.perpendicular-lines` |
| Reading function behaviour from a derivative graph | `derivative-graph-features` | `sketch-derivative-graph` |
| Spotting corners, cusps and vertical tangents | `non-differentiable-points` | `sketch-derivative-graph`, `limits-of-absolute-value` |
| Testing differentiability | `differentiability` | `non-differentiable-points`, `make-function-continuous` |
| Showing differentiability implies continuity | `differentiability-implies-continuity` | `differentiability` |

### Differentiation rules

| Topic | Slug | Needs |
|---|---|---|
| Using the constant and power rules | `constant-and-power-rule` | `derivative-notation` |
| Using the power rule with negative and rational powers | `rule-with-negative-rational-powers` | `constant-and-power-rule`, `alg2.exponent-laws-rational` |
| Using sum, difference and constant multiple rules | `sum-difference-multiple-rules` | `constant-and-power-rule` |
| Rewriting before differentiating | `rewrite-before-differentiating` | `sum-difference-multiple-rules`, `rule-with-negative-rational-powers` |
| Using the product rule | `product-rule-derivative` | `sum-difference-multiple-rules` |
| Using the quotient rule | `quotient-rule-derivative` | `product-rule-derivative` |
| Choosing a rule to differentiate | `choose-a-rule` | `quotient-rule-derivative`, `rewrite-before-differentiating` |
| Finding higher derivatives | `higher-derivatives` | `sum-difference-multiple-rules` |
| Finding derivatives of sine and cosine | `derivatives-of-sine-cosine` | `trig-limits`, `sum-difference-multiple-rules` |
| Finding derivatives of other trig functions | `derivatives-of-other-trig` | `derivatives-of-sine-cosine`, `quotient-rule-derivative` |
| Using the chain rule on a power of a function | `chain-rule-power-of-function` | `sum-difference-multiple-rules`, `alg2.decompose-function` |
| Using the general chain rule | `chain-rule-general` | `chain-rule-power-of-function` |
| Applying the chain rule more than once | `chain-rule-repeated` | `chain-rule-general` |
| Using the chain rule with trig functions | `chain-rule-trig` | `derivatives-of-other-trig`, `chain-rule-repeated` |
| Finding derivatives of exponential functions | `derivative-of-exponential` | `chain-rule-general`, `precalc.exponential-function-analysis` |
| Using differentiation rules with table values | `rules-with-table-values` | `chain-rule-general` |
| Combining the chain rule with product and quotient rules | `chain-with-product-quotient` | `quotient-rule-derivative`, `rules-with-table-values` |
| Using implicit differentiation | `implicit-differentiation` | `chain-with-product-quotient` |
| Finding second derivatives implicitly | `implicit-second-derivative` | `implicit-differentiation`, `higher-derivatives` |
| Finding tangents to implicit curves | `tangent-to-implicit-curve` | `implicit-differentiation`, `tangent-line-equation` |
| Finding derivatives of logarithms | `derivative-of-log` | `derivative-of-exponential`, `implicit-differentiation` |
| Finding derivatives of inverse functions | `derivative-of-inverse-function` | `implicit-differentiation`, `precalc.inverse-with-restricted-domains` |
| Finding derivatives of inverse trig functions | `derivatives-of-inverse-trig` | `derivative-of-inverse-function`, `precalc.inverse-trig-functions` |
| Writing tangent lines using rules | `tangent-with-rules` | `tangent-line-equation`, `sum-difference-multiple-rules` |
| Finding horizontal tangents | `horizontal-tangents` | `tangent-with-rules` |
| Using the chain rule with exponentials | `chain-rule-exp` | `derivative-of-exponential` |
| Finding derivatives with any base | `derivative-of-general-exponential` | `chain-rule-exp` |
| Using the chain rule with logarithms | `chain-rule-log` | `derivative-of-log` |
| Using logarithmic differentiation | `logarithmic-differentiation` | `alg2.expand-condense-logs`, `chain-rule-log`, `derivative-of-general-exponential` |

### Applications of the derivative

| Topic | Slug | Needs |
|---|---|---|
| Using position, velocity and acceleration | `position-velocity-acceleration` | `higher-derivatives`, `interpret-derivative-units` |
| Finding speed and direction of motion | `speed-and-direction` | `position-velocity-acceleration` |
| Using derivatives in science and economics | `rates-in-science-economics` | `interpret-derivative-units`, `choose-a-rule` |
| Using marginal cost and revenue | `marginal-cost-revenue` | `rates-in-science-economics` |
| Setting up a related rates problem | `related-rates-setup` | `implicit-differentiation` |
| Solving related rates with geometry | `related-rates-geometry` | `related-rates-setup` |
| Solving related rates with the Pythagorean theorem | `related-rates-pythagorean` | `related-rates-geometry` |
| Using linear approximation | `linear-approximation` | `tangent-with-rules` |
| Using differentials to estimate error | `differentials` | `linear-approximation` |
| Using Newton's method | `newtons-method` | `tangent-with-rules` |
| Finding critical numbers | `critical-numbers` | `choose-a-rule`, `horizontal-tangents` |
| Using the extreme value theorem | `extreme-value-theorem` | `critical-numbers`, `continuity-on-intervals` |
| Finding absolute extrema on a closed interval | `closed-interval-method` | `extreme-value-theorem` |
| Using Rolle's theorem | `rolles-theorem` | `extreme-value-theorem`, `differentiability` |
| Using the mean value theorem | `mean-value-theorem` | `rolles-theorem` |
| Using consequences of the mean value theorem | `mvt-consequences` | `mean-value-theorem` |
| Using the first derivative test | `first-derivative-test` | `mvt-consequences` |
| Finding where a function increases or decreases | `increasing-decreasing-derivative` | `first-derivative-test` |
| Finding concavity with the second derivative | `concavity` | `increasing-decreasing-derivative`, `higher-derivatives` |
| Finding inflection points | `inflection-points` | `concavity` |
| Using the second derivative test | `second-derivative-test` | `concavity` |
| Sketching polynomials with calculus | `curve-sketching-polynomial` | `inflection-points`, `second-derivative-test` |
| Sketching rational functions with calculus | `curve-sketching-rational` | `curve-sketching-polynomial`, `horizontal-asymptotes-limits`, `infinite-limits`, `limits-at-infinity-roots` |
| Sketching exponential, log and trig functions | `curve-sketching-exp-log-trig` | `curve-sketching-polynomial`, `derivatives-of-inverse-trig`, `derivative-of-log` |
| Relating graphs of f, f prime and f double prime | `graphs-of-f-fprime-fdoubleprime` | `inflection-points`, `derivative-graph-features` |
| Recognizing indeterminate forms | `indeterminate-forms` | `limits-at-infinity-rational` |
| Using L'Hopital's rule | `lhopital-rule` | `indeterminate-forms`, `mean-value-theorem` |
| Using L'Hopital's rule with products and differences | `lhopital-products-differences` | `lhopital-rule` |
| Using L'Hopital's rule with indeterminate powers | `lhopital-powers` | `lhopital-products-differences`, `logarithmic-differentiation` |
| Comparing growth rates with limits | `growth-rate-comparison` | `lhopital-rule`, `limits-at-infinity-exp-log` |
| Setting up an optimization problem | `optimization-setup` | `closed-interval-method`, `precalc.function-from-description` |
| Solving geometric optimization problems | `optimization-geometry` | `optimization-setup` |
| Solving distance and time optimization problems | `optimization-distance-time` | `optimization-geometry` |
| Solving business optimization problems | `optimization-business` | `optimization-setup`, `marginal-cost-revenue` |
| Justifying extrema on open intervals | `optimization-open-intervals` | `optimization-geometry`, `first-derivative-test` |
| Solving related rates with similar triangles | `related-rates-similar-triangles` | `related-rates-geometry` |
| Solving related rates with trig | `related-rates-trig` | `chain-rule-trig`, `related-rates-similar-triangles` |

### Integration

| Topic | Slug | Needs |
|---|---|---|
| Finding antiderivatives | `antiderivatives` | `mvt-consequences` |
| Using indefinite integral notation | `indefinite-integral-notation` | `antiderivatives` |
| Using basic integration rules | `basic-integral-rules` | `indefinite-integral-notation`, `derivatives-of-other-trig` |
| Rewriting before integrating | `integrate-after-rewriting` | `basic-integral-rules` |
| Solving initial value problems by antidifferentiating | `initial-value-antiderivative` | `basic-integral-rules` |
| Finding motion from acceleration | `motion-from-acceleration` | `initial-value-antiderivative`, `position-velocity-acceleration` |
| Using sigma notation with area | `sigma-for-riemann` | `alg2.sigma-properties`, `precalc.sum-of-powers-formula` |
| Estimating area with rectangles | `area-by-rectangles` | `sigma-for-riemann`, `precalc.area-under-curve-intuition` |
| Using left, right and midpoint sums | `riemann-left-right-midpoint` | `area-by-rectangles` |
| Using Riemann sums from tables | `riemann-from-tables` | `riemann-left-right-midpoint` |
| Finding an area as a limit of a sum | `limit-of-riemann-sum` | `riemann-left-right-midpoint`, `limits-at-infinity-rational` |
| Defining the definite integral | `definite-integral-definition` | `limit-of-riemann-sum` |
| Evaluating integrals from geometry | `integral-as-signed-area` | `definite-integral-definition` |
| Using properties of definite integrals | `properties-of-definite-integrals` | `definite-integral-definition` |
| Bounding an integral | `integral-comparison-bounds` | `properties-of-definite-integrals` |
| Using substitution on indefinite integrals | `u-substitution-indefinite` | `chain-rule-general`, `integrate-after-rewriting` |
| Adjusting constants in a substitution | `substitution-adjusting-constants` | `u-substitution-indefinite` |
| Using substitution with exponentials and logs | `substitution-with-exp-log` | `derivative-of-log`, `substitution-adjusting-constants` |
| Using substitution with trig functions | `substitution-with-trig` | `substitution-adjusting-constants` |
| Integrating to inverse trig functions | `substitution-inverse-trig` | `substitution-with-trig`, `derivatives-of-inverse-trig` |
| Evaluating integrals from table and graph values | `integral-rules-with-tables` | `properties-of-definite-integrals` |
| Using the fundamental theorem to evaluate integrals | `ftc-part-2` | `basic-integral-rules`, `integral-rules-with-tables` |
| Differentiating an integral function | `ftc-part-1` | `ftc-part-2`, `chain-rule-general` |
| Finding the average value of a function | `average-value` | `ftc-part-2` |
| Using the mean value theorem for integrals | `mvt-for-integrals` | `average-value` |
| Using substitution on definite integrals | `u-substitution-definite` | `u-substitution-indefinite`, `ftc-part-2` |
| Using symmetry to integrate | `integrate-even-odd` | `u-substitution-definite` |
| Finding area between curves in x | `area-between-curves-x` | `ftc-part-2` |
| Finding area between curves in y | `area-between-curves-y` | `area-between-curves-x` |
| Finding area when curves cross | `area-with-intersections` | `area-between-curves-x` |
| Finding volume by disks | `volume-by-disks` | `area-between-curves-x` |
| Finding volume by washers | `volume-by-washers` | `volume-by-disks`, `area-between-curves-y`, `area-with-intersections` |
| Finding volume by known cross sections | `volume-known-cross-sections` | `volume-by-disks` |
| Evaluating integrals of piecewise and absolute value functions | `ftc-piecewise-absolute` | `ftc-part-2`, `integral-as-signed-area` |
| Using the net change theorem | `net-change-theorem` | `ftc-piecewise-absolute` |
| Finding displacement and total distance | `displacement-distance` | `net-change-theorem`, `motion-from-acceleration`, `speed-and-direction` |
| Reading graphs of accumulation functions | `accumulation-function-graphs` | `ftc-part-1` |
| Using the fundamental theorem with the chain rule | `ftc-with-chain-rule` | `accumulation-function-graphs` |

## math.calc2: 146 topics, budget 180 (-19%)

### Integration techniques

| Topic | Slug | Needs |
|---|---|---|
| Using integration by parts | `integration-by-parts` | `calc1.u-substitution-definite` |
| Using integration by parts on definite integrals | `parts-definite` | `integration-by-parts` |
| Evaluating improper integrals with infinite limits | `improper-infinite-limits` | `calc1.limits-at-infinity-exp-log`, `parts-definite` |
| Using the p-integral test | `p-integrals` | `improper-infinite-limits` |
| Choosing parts for integration by parts | `parts-choose-u` | `integration-by-parts` |
| Using parts with logs and inverse trig | `parts-with-log-inverse` | `integration-by-parts` |
| Using integration by parts repeatedly | `parts-repeated` | `parts-choose-u`, `parts-with-log-inverse` |
| Using cyclic integration by parts | `parts-cyclic` | `parts-repeated` |
| Deriving reduction formulas | `parts-reduction-formula` | `parts-repeated` |
| Integrating odd powers of sine or cosine | `odd-power-sine-cosine` | `calc1.substitution-with-trig` |
| Integrating even powers of sine and cosine | `even-power-sine-cosine` | `odd-power-sine-cosine`, `precalc.reduce-powers` |
| Integrating powers of sine and cosine | `powers-sine-cosine` | `even-power-sine-cosine` |
| Integrating products with different angles | `trig-products-different-angles` | `powers-sine-cosine`, `precalc.product-sum-identities` |
| Using trig substitution with sine | `trig-sub-sine` | `powers-sine-cosine`, `calc1.substitution-inverse-trig` |
| Integrating with even powers of secant | `tangent-secant-even` | `odd-power-sine-cosine` |
| Integrating with odd powers of tangent | `tangent-secant-odd` | `tangent-secant-even` |
| Integrating powers of tangent and secant | `powers-tangent-secant` | `powers-sine-cosine`, `tangent-secant-odd` |
| Using trig substitution with tangent | `trig-sub-tangent` | `trig-sub-sine`, `powers-tangent-secant` |
| Using trig substitution with secant | `trig-sub-secant` | `trig-sub-tangent` |
| Completing the square before trig substitution | `trig-sub-completing-square` | `trig-sub-secant` |
| Changing limits in a trig substitution | `trig-sub-definite` | `trig-sub-secant` |
| Choosing a partial fraction form | `partial-fractions-setup` | `calc1.substitution-with-exp-log`, `precalc.partial-fractions` |
| Integrating with distinct linear factors | `partial-fractions-linear` | `partial-fractions-setup` |
| Integrating with repeated linear factors | `partial-fractions-repeated-integral` | `partial-fractions-linear`, `precalc.partial-fractions-repeated` |
| Dividing before integrating a rational function | `long-division-first` | `partial-fractions-linear` |
| Using rationalizing substitutions | `rationalizing-substitutions` | `partial-fractions-linear` |
| Integrating simple rational functions | `log-and-arctan-integrals` | `calc1.substitution-with-exp-log`, `calc1.substitution-inverse-trig` |
| Integrating with quadratic factors | `partial-fractions-quadratic-integral` | `partial-fractions-linear`, `precalc.partial-fractions-quadratic`, `log-and-arctan-integrals` |
| Choosing a method of integration | `strategy-for-integration` | `partial-fractions-quadratic-integral`, `parts-reduction-formula`, `trig-sub-definite`, `partial-fractions-repeated-integral` |
| Splitting doubly infinite improper integrals | `improper-both-infinite` | `improper-infinite-limits` |
| Evaluating improper integrals with discontinuities | `improper-discontinuous` | `improper-both-infinite` |
| Handling a discontinuity inside the interval | `improper-interior-discontinuity` | `improper-discontinuous` |
| Comparing improper integrals | `comparison-improper` | `p-integrals`, `improper-interior-discontinuity`, `calc1.integral-comparison-bounds` |
| Using the trapezoid rule | `trapezoid-rule` | `calc1.riemann-left-right-midpoint` |
| Estimating with the trapezoid and Simpson's rules | `numerical-trapezoid-simpson` | `trapezoid-rule` |
| Bounding trapezoid and Simpson's errors | `numerical-error-bounds` | `numerical-trapezoid-simpson` |

### Applications of integration

| Topic | Slug | Needs |
|---|---|---|
| Finding center of mass of point masses | `moments-center-of-mass-discrete` | `calc1.ftc-part-2` |
| Finding the centroid of a region | `centroid-of-region` | `moments-center-of-mass-discrete`, `calc1.area-between-curves-x` |
| Using integrals for probability density | `probability-density-integral` | `improper-infinite-limits`, `calc1.average-value` |
| Using integrals in economics | `consumer-surplus-applications` | `calc1.area-between-curves-x` |
| Using shells around the y-axis | `shells-around-y-axis` | `calc1.volume-by-washers` |
| Finding volume by cylindrical shells | `volume-by-shells` | `shells-around-y-axis` |
| Choosing disks or shells | `choose-disk-or-shell` | `volume-by-shells` |
| Rotating about lines other than the axes | `rotation-about-other-lines` | `choose-disk-or-shell` |
| Finding simple arc lengths | `arc-length-simple` | `calc1.u-substitution-definite` |
| Finding arc length | `arc-length-integral` | `trig-sub-tangent`, `arc-length-simple` |
| Finding the area of a surface of revolution | `surface-of-revolution` | `arc-length-integral` |
| Writing the arc length function | `arc-length-function` | `arc-length-integral` |
| Finding work done by a variable force | `work-variable-force` | `calc1.ftc-part-2` |
| Finding work done by a spring | `work-springs` | `work-variable-force` |
| Finding work lifting a rope | `work-lifting-ropes` | `work-springs` |
| Finding work pumping from a cylindrical tank | `work-pumping-cylinder` | `work-lifting-ropes`, `calc1.volume-by-disks` |
| Finding work pumping a liquid | `work-pumping-liquid` | `calc1.volume-known-cross-sections`, `work-pumping-cylinder` |
| Finding hydrostatic force | `hydrostatic-force` | `work-pumping-liquid` |
| Finding the centroid between two curves | `centroid-between-curves` | `centroid-of-region` |
| Using Pappus' theorem | `pappus-theorem` | `volume-by-shells`, `centroid-between-curves` |
| Finding mean and median with integrals | `expected-value-integral` | `probability-density-integral` |

### First differential equations

| Topic | Slug | Needs |
|---|---|---|
| Introducing differential equations | `intro-differential-equations` | `calc1.initial-value-antiderivative` |
| Checking a solution of a differential equation | `verify-de-solutions` | `intro-differential-equations` |
| Reading and sketching slope fields | `slope-fields` | `verify-de-solutions` |
| Using Euler's method | `eulers-method-intro` | `slope-fields`, `calc1.linear-approximation` |
| Solving separable equations | `separable-equations` | `partial-fractions-linear`, `verify-de-solutions` |
| Solving simple mixing problems | `mixing-problems-intro` | `separable-equations` |
| Solving separable initial value problems | `separable-initial-value` | `separable-equations` |
| Modelling exponential growth | `exponential-growth-de` | `separable-initial-value` |
| Modelling Newton's law of cooling | `newton-cooling-de` | `precalc.newton-cooling-models`, `separable-initial-value` |
| Using half-life and doubling time | `half-life-doubling-de` | `exponential-growth-de` |
| Reading logistic behaviour without solving | `logistic-behaviour` | `slope-fields`, `precalc.logistic-growth` |
| Solving the logistic equation | `logistic-de` | `separable-equations`, `logistic-behaviour` |

### Sequences

| Topic | Slug | Needs |
|---|---|---|
| Finding formulas for sequences | `sequence-terms-formula` | `precalc.sequence-limits` |
| Finding limits of sequences | `sequence-notation-limits` | `calc1.limits-at-infinity-exp-log`, `sequence-terms-formula` |
| Using limit laws on sequences | `sequence-limit-laws` | `sequence-notation-limits` |
| Using monotonic and bounded sequences | `monotonic-bounded-sequences` | `sequence-limit-laws` |
| Finding sequence limits with squeeze and L'Hopital | `sequence-squeeze-and-lhopital` | `calc1.squeeze-theorem`, `calc1.growth-rate-comparison`, `sequence-limit-laws` |
| Finding limits of recursive sequences | `recursive-sequence-limits` | `monotonic-bounded-sequences` |
| Comparing powers and factorials in sequences | `sequences-powers-factorials` | `sequence-squeeze-and-lhopital` |

### Series and convergence

| Topic | Slug | Needs |
|---|---|---|
| Defining a series with partial sums | `series-as-partial-sums` | `sequence-notation-limits`, `alg2.series-with-partial-sums` |
| Summing geometric series | `geometric-series-calc` | `series-as-partial-sums`, `precalc.series-review-convergence` |
| Using the divergence test | `divergence-test` | `series-as-partial-sums` |
| Using the integral test | `integral-test` | `divergence-test`, `p-integrals` |
| Using p-series | `p-series` | `integral-test` |
| Estimating a sum with the integral test | `integral-test-remainder` | `integral-test` |
| Using the alternating series test | `alternating-series-test` | `divergence-test` |
| Telling absolute from conditional convergence | `absolute-conditional` | `alternating-series-test`, `p-series` |
| Using the ratio test | `ratio-test` | `absolute-conditional`, `sequences-powers-factorials` |
| Using the root test | `root-test` | `ratio-test` |
| Finding a partial sum formula | `series-partial-sum-formula` | `series-as-partial-sums` |
| Summing telescoping series | `telescoping-series` | `precalc.telescoping-sums`, `series-partial-sum-formula` |
| Using sums and multiples of series | `series-algebra` | `series-as-partial-sums` |
| Rewriting a series as geometric | `geometric-series-rewriting` | `geometric-series-calc` |
| Using the direct comparison test | `direct-comparison` | `p-series`, `series-algebra`, `geometric-series-rewriting` |
| Writing repeating decimals with series | `repeating-decimals-series` | `geometric-series-calc` |
| Choosing a series to compare against | `comparison-choose-bound` | `direct-comparison` |
| Using the limit comparison test | `limit-comparison` | `comparison-choose-bound` |
| Using limit comparison with roots | `limit-comparison-roots` | `limit-comparison` |
| Choosing a test for convergence | `choose-a-series-test` | `root-test`, `limit-comparison-roots` |
| Checking decreasing terms for alternating series | `alternating-decreasing-check` | `alternating-series-test`, `calc1.increasing-decreasing-derivative` |
| Bounding the remainder of an alternating series | `alternating-remainder` | `alternating-decreasing-check` |
| Using the ratio test with factorials | `ratio-test-factorials` | `ratio-test` |

### Power and Taylor series

| Topic | Slug | Needs |
|---|---|---|
| Understanding power series | `power-series-intro` | `ratio-test-factorials` |
| Finding the radius of convergence | `radius-of-convergence` | `power-series-intro` |
| Representing functions with geometric series | `functions-as-power-series` | `power-series-intro`, `geometric-series-calc` |
| Building Taylor polynomials | `taylor-polynomials` | `calc1.linear-approximation`, `calc1.higher-derivatives` |
| Finding the radius with factorials | `radius-with-factorials` | `radius-of-convergence` |
| Working with power series at other centres | `center-shifted-power-series` | `radius-of-convergence` |
| Testing endpoints of a power series | `endpoints-of-interval` | `radius-of-convergence` |
| Finding the interval of convergence | `interval-of-convergence` | `radius-with-factorials`, `center-shifted-power-series`, `endpoints-of-interval` |
| Rewriting a rational function as a series | `rational-function-as-series` | `functions-as-power-series` |
| Differentiating and integrating power series | `differentiate-integrate-series` | `rational-function-as-series` |
| Finding series for arctan and log | `series-for-arctan-log` | `differentiate-integrate-series` |
| Finding Taylor polynomials at other centres | `taylor-at-other-centers` | `taylor-polynomials` |
| Finding Taylor series | `taylor-series` | `power-series-intro`, `taylor-at-other-centers` |
| Using Taylor's remainder | `taylor-remainder` | `taylor-series`, `alternating-remainder` |
| Finding the series for sine and cosine | `series-for-sine-cosine` | `taylor-series` |
| Finding the series for the exponential | `series-for-exp` | `taylor-series` |
| Using common Maclaurin series | `maclaurin-common` | `series-for-sine-cosine`, `series-for-exp` |
| Building series by substituting | `substitute-into-series` | `maclaurin-common` |
| Multiplying and dividing series | `multiply-divide-series` | `maclaurin-common` |
| Estimating integrals with series | `series-to-estimate-integrals` | `substitute-into-series`, `alternating-remainder` |
| Finding limits with series | `series-for-limits` | `substitute-into-series`, `multiply-divide-series` |
| Using the binomial series | `binomial-series` | `maclaurin-common`, `precalc.binomial-theorem-applications` |
| Finding the sum of a series from a known function | `sum-a-series-from-known` | `maclaurin-common`, `series-for-arctan-log` |
| Estimating the error of a Taylor polynomial | `taylor-error-estimate` | `taylor-remainder` |
| Applying Taylor series in physics | `applications-of-taylor-physics` | `taylor-error-estimate`, `binomial-series` |
| Showing a Taylor series equals its function | `series-equals-function` | `taylor-remainder` |

### Parametric and polar calculus

| Topic | Slug | Needs |
|---|---|---|
| Finding derivatives of parametric curves | `parametric-derivatives` | `calc1.chain-rule-general`, `precalc.parametric-eliminate` |
| Finding areas with parametric curves | `parametric-area` | `parametric-derivatives`, `calc1.u-substitution-definite` |
| Finding arc length of parametric curves | `parametric-arc-length` | `parametric-derivatives`, `arc-length-integral` |
| Finding surface areas of parametric curves | `parametric-surface-area` | `parametric-arc-length`, `surface-of-revolution` |
| Finding area in polar coordinates | `polar-area` | `calc1.u-substitution-definite`, `precalc.polar-curves`, `powers-sine-cosine` |
| Using calculus on conic sections | `conics-with-calculus` | `parametric-derivatives`, `precalc.conic-applications` |
| Finding tangents to parametric curves | `parametric-tangent-lines` | `parametric-derivatives` |
| Finding second derivatives of parametric curves | `parametric-second-derivative` | `calc1.higher-derivatives`, `parametric-tangent-lines` |
| Finding horizontal and vertical tangents of parametric curves | `parametric-horizontal-vertical` | `parametric-tangent-lines` |
| Finding slopes of polar curves | `polar-derivatives` | `precalc.polar-curves`, `parametric-horizontal-vertical` |
| Finding arc length of polar curves | `polar-arc-length` | `polar-derivatives`, `arc-length-integral` |
| Writing tangent lines to polar curves | `polar-tangent-lines` | `polar-derivatives` |
| Finding the area of one petal | `polar-area-petal` | `polar-area` |
| Finding area between polar curves | `polar-area-between-curves` | `polar-area-petal` |

### Hyperbolic functions

| Topic | Slug | Needs |
|---|---|---|
| Defining hyperbolic functions | `hyperbolic-definitions` | `calc1.derivative-of-exponential` |
| Graphing hyperbolic functions | `hyperbolic-graphs` | `hyperbolic-definitions` |
| Using hyperbolic identities | `hyperbolic-identities` | `hyperbolic-graphs` |
| Differentiating and integrating hyperbolic functions | `hyperbolic-derivatives-integrals` | `hyperbolic-identities`, `calc1.u-substitution-indefinite` |
| Using inverse hyperbolic functions | `inverse-hyperbolic` | `hyperbolic-derivatives-integrals`, `calc1.derivative-of-inverse-function` |
| Using hyperbolic substitutions | `hyperbolic-substitutions` | `inverse-hyperbolic`, `trig-sub-tangent` |
| Applying the catenary | `catenary` | `hyperbolic-derivatives-integrals`, `arc-length-integral` |

## math.calc3: 153 topics, budget 180 (-15%)

### Vectors and geometry of space

| Topic | Slug | Needs |
|---|---|---|
| Using three-dimensional coordinates | `three-d-coordinates` | `precalc.vectors-in-3d` |
| Working with vectors in space | `vectors-in-space` | `three-d-coordinates`, `precalc.vector-add-subtract` |
| Finding the cross product | `cross-product` | `vectors-in-space`, `precalc.determinants-3x3` |
| Applying the cross product | `torque-applications` | `cross-product` |
| Writing equations of lines in space | `lines-in-space` | `vectors-in-space`, `precalc.line-as-vector-equation` |
| Recognizing cylinders | `cylinders-as-surfaces` | `three-d-coordinates` |
| Using cylindrical coordinates | `cylindrical-coordinates` | `three-d-coordinates`, `precalc.polar-rectangular-conversion` |
| Using spherical coordinates | `spherical-coordinates` | `cylindrical-coordinates` |
| Finding distance and midpoint in space | `distance-midpoint-space` | `three-d-coordinates` |
| Writing equations of spheres | `spheres-and-planes-simple` | `geom.equation-of-circle`, `distance-midpoint-space` |
| Finding magnitude and unit vectors in space | `vector-magnitude-unit-space` | `vectors-in-space` |
| Using the dot product in space | `dot-product-space` | `precalc.dot-product`, `vector-magnitude-unit-space` |
| Writing equations of planes | `planes` | `cross-product`, `dot-product-space` |
| Finding angles between planes | `angle-between-planes` | `planes` |
| Finding angles with the dot product | `angle-between-vectors-space` | `dot-product-space` |
| Finding projections in space | `projections-space` | `precalc.projections`, `angle-between-vectors-space` |
| Finding direction angles | `direction-cosines` | `angle-between-vectors-space` |
| Using properties of the cross product | `cross-product-properties` | `cross-product` |
| Using the cross product for area and volume | `cross-product-geometry` | `cross-product-properties` |
| Using the scalar triple product | `triple-scalar-product` | `cross-product-geometry`, `dot-product-space` |
| Writing symmetric equations of lines | `symmetric-line-equations` | `lines-in-space` |
| Finding how two lines in space relate | `relationships-of-lines` | `symmetric-line-equations` |
| Writing a plane through three points | `plane-from-three-points` | `planes` |
| Finding distances to planes and lines | `distance-to-plane` | `projections-space`, `plane-from-three-points` |
| Finding where a line meets a plane | `line-plane-intersection` | `plane-from-three-points`, `relationships-of-lines` |
| Finding the line where two planes meet | `line-of-intersection-planes` | `planes`, `lines-in-space` |
| Sketching traces of surfaces | `traces-of-surfaces` | `three-d-coordinates`, `precalc.classify-general-conic` |
| Recognizing quadric surfaces | `quadric-surfaces` | `spheres-and-planes-simple`, `traces-of-surfaces`, `cylinders-as-surfaces` |
| Rewriting surfaces in other coordinates | `surfaces-in-other-coordinates` | `spherical-coordinates`, `quadric-surfaces` |

### Vector functions

| Topic | Slug | Needs |
|---|---|---|
| Describing space curves | `vector-functions-space-curves` | `lines-in-space`, `precalc.parametric-basics` |
| Finding domains of vector functions | `domain-of-vector-function` | `vector-functions-space-curves` |
| Finding limits of vector functions | `vector-function-limits` | `calc2.parametric-derivatives`, `domain-of-vector-function` |
| Differentiating vector functions | `vector-derivative` | `vector-function-limits` |
| Finding tangent lines to space curves | `tangent-vectors` | `vector-derivative` |
| Integrating vector functions | `vector-integrals` | `vector-derivative`, `calc1.ftc-part-2` |
| Finding arc length of space curves | `arc-length-space-curves` | `vector-derivative`, `calc2.parametric-arc-length` |
| Reparametrizing by arc length | `arc-length-parameter` | `arc-length-space-curves`, `calc2.arc-length-function` |
| Finding velocity and acceleration in space | `motion-in-space` | `vector-integrals` |
| Modelling projectile motion | `projectile-vector` | `motion-in-space`, `precalc.projectile-parametric` |
| Exploring Kepler's laws | `keplers-laws-intro` | `motion-in-space`, `cross-product` |
| Finding where curves and surfaces meet | `curve-surface-intersections` | `vector-functions-space-curves` |
| Using differentiation rules for vector functions | `vector-derivative-rules` | `vector-derivative`, `cross-product` |
| Finding unit tangent and normal vectors | `unit-tangent-normal` | `tangent-vectors`, `arc-length-space-curves`, `vector-derivative-rules` |
| Finding curvature | `curvature` | `unit-tangent-normal`, `arc-length-parameter` |
| Finding the binormal and Frenet frame | `binormal-frame` | `curvature` |
| Splitting acceleration into components | `tangential-normal-acceleration` | `motion-in-space`, `unit-tangent-normal` |
| Finding curvature of plane curves | `curvature-plane-curves` | `curvature` |
| Finding the osculating circle | `osculating-circle` | `curvature` |

### Partial derivatives

| Topic | Slug | Needs |
|---|---|---|
| Describing functions of several variables | `functions-of-two-variables` | `three-d-coordinates`, `alg1.domain-restrictions-basic` |
| Finding limits in several variables | `multivariable-limits` | `functions-of-two-variables`, `calc1.limits-by-factoring` |
| Showing a limit does not exist with paths | `limit-does-not-exist-paths` | `multivariable-limits` |
| Defining partial derivatives | `partial-derivatives-definition` | `functions-of-two-variables`, `calc1.choose-a-rule` |
| Calculating partial derivatives | `partial-derivatives-compute` | `partial-derivatives-definition` |
| Finding higher partial derivatives | `higher-partials` | `partial-derivatives-compute` |
| Using equal mixed partials | `clairaut-mixed-partials` | `higher-partials` |
| Checking solutions of partial differential equations | `partial-differential-equation-check` | `higher-partials` |
| Finding directional derivatives | `directional-derivative` | `partial-derivatives-compute`, `dot-product-space` |
| Finding critical points in two variables | `critical-points-two-variables` | `partial-derivatives-compute` |
| Finding domains of multivariable functions | `domain-range-multivariable` | `functions-of-two-variables` |
| Reading level curves | `level-curves` | `domain-range-multivariable` |
| Matching functions to their graphs | `match-functions-graphs` | `level-curves` |
| Reading level surfaces | `level-surfaces` | `match-functions-graphs` |
| Finding limits with polar coordinates | `multivariable-limit-polar` | `multivariable-limits`, `precalc.polar-rectangular-conversion` |
| Testing continuity in several variables | `multivariable-continuity` | `multivariable-limit-polar`, `limit-does-not-exist-paths` |
| Estimating partial derivatives from contours | `partials-from-contours` | `partial-derivatives-definition`, `level-curves` |
| Finding tangent planes | `tangent-planes` | `partial-derivatives-compute`, `planes`, `partials-from-contours` |
| Using multivariable linearization | `linearization-multivariable` | `tangent-planes`, `calc1.linear-approximation` |
| Using multivariable differentials | `multivariable-differentials` | `linearization-multivariable` |
| Testing differentiability in several variables | `differentiability-multivariable` | `linearization-multivariable`, `multivariable-continuity` |
| Using the multivariable chain rule | `chain-rule-multivariable` | `differentiability-multivariable` |
| Finding partial derivatives of three variables | `partials-three-variables` | `partial-derivatives-compute` |
| Finding implicit partial derivatives | `implicit-partial` | `calc1.implicit-differentiation`, `partials-three-variables` |
| Using the chain rule for implicit functions | `implicit-function-chain` | `chain-rule-multivariable`, `implicit-partial` |
| Drawing tree diagrams for the chain rule | `tree-diagram-chain-rule` | `chain-rule-multivariable` |
| Using the chain rule with several parameters | `chain-rule-two-parameters` | `tree-diagram-chain-rule` |
| Finding second derivatives with the chain rule | `second-order-chain-rule` | `chain-rule-two-parameters`, `higher-partials` |
| Estimating directional derivatives from contour maps | `directional-from-contours` | `directional-derivative`, `level-curves` |
| Finding the gradient | `gradient-vector` | `directional-from-contours` |
| Using the gradient for steepest ascent | `gradient-direction` | `gradient-vector` |
| Finding gradients in three variables | `gradient-three-variables` | `gradient-vector` |
| Using the gradient as a normal to level sets | `gradient-normal-level` | `tangent-planes`, `gradient-three-variables`, `level-surfaces` |
| Using Lagrange multipliers with one constraint | `lagrange-one-constraint` | `gradient-normal-level`, `critical-points-two-variables` |
| Classifying critical points from contour maps | `classify-from-contours` | `critical-points-two-variables`, `level-curves` |
| Using the second derivatives test | `second-derivatives-test-two` | `higher-partials`, `precalc.determinants-2x2`, `classify-from-contours` |
| Parametrizing a boundary for optimization | `parametrize-a-boundary` | `second-derivatives-test-two`, `vector-functions-space-curves` |
| Finding absolute extrema on closed regions | `absolute-extrema-regions` | `parametrize-a-boundary` |
| Solving multivariable optimization problems | `optimization-multivariable` | `absolute-extrema-regions` |
| Deriving least squares with calculus | `least-squares-from-calculus` | `optimization-multivariable` |
| Using Lagrange multipliers in three variables | `lagrange-three-variables` | `lagrange-one-constraint` |
| Using Lagrange multipliers with two constraints | `lagrange-two-constraints` | `lagrange-three-variables` |
| Using second-order Taylor approximations | `taylor-two-variables` | `linearization-multivariable`, `higher-partials` |

### Multiple integrals

| Topic | Slug | Needs |
|---|---|---|
| Defining double integrals | `double-integral-definition` | `calc1.definite-integral-definition`, `functions-of-two-variables` |
| Estimating double integrals with Riemann sums | `double-riemann-sum` | `double-integral-definition` |
| Evaluating iterated integrals over rectangles | `iterated-rectangles` | `double-riemann-sum` |
| Using Fubini's theorem | `fubini` | `iterated-rectangles` |
| Evaluating triple integrals over boxes | `triple-integrals-boxes` | `fubini` |
| Describing regions of integration | `region-types` | `double-integral-definition` |
| Evaluating double integrals over general regions | `double-general-regions` | `fubini`, `region-types` |
| Sketching regions of integration | `sketch-regions-of-integration` | `double-general-regions` |
| Reversing the order of integration | `reverse-order` | `sketch-regions-of-integration` |
| Finding area and volume with double integrals | `area-volume-double` | `double-general-regions` |
| Finding mass and center of mass | `mass-center-double` | `area-volume-double`, `calc2.centroid-of-region` |
| Finding moments of inertia | `moments-of-inertia` | `mass-center-double` |
| Using double integrals for probability | `probability-double` | `area-volume-double`, `calc2.probability-density-integral` |
| Describing regions in polar form | `polar-region-setup` | `fubini`, `calc2.polar-area` |
| Evaluating double integrals in polar coordinates | `double-polar` | `double-general-regions`, `polar-region-setup` |
| Finding the area of a surface | `surface-area-double` | `double-polar`, `tangent-planes` |
| Finding Jacobians | `jacobian` | `double-polar`, `precalc.determinants-2x2` |
| Evaluating the Gaussian integral | `gaussian-integral` | `double-polar` |
| Setting limits for triple integrals | `triple-region-setup` | `triple-integrals-boxes`, `double-general-regions` |
| Evaluating triple integrals over general regions | `triple-general` | `triple-region-setup` |
| Changing the order in triple integrals | `triple-order-change` | `triple-general`, `reverse-order` |
| Evaluating triple integrals in cylindrical coordinates | `triple-cylindrical` | `triple-general`, `cylindrical-coordinates` |
| Finding mass and center of mass in three dimensions | `triple-mass-center` | `triple-general`, `mass-center-double` |
| Describing regions in spherical coordinates | `spherical-region-setup` | `spherical-coordinates`, `triple-general` |
| Evaluating triple integrals in spherical coordinates | `triple-spherical` | `triple-cylindrical`, `spherical-region-setup` |
| Choosing a transformation for a region | `choose-a-transformation` | `jacobian` |
| Changing variables in double integrals | `change-of-variables-double` | `choose-a-transformation` |
| Changing variables in triple integrals | `change-of-variables-triple` | `change-of-variables-double`, `triple-spherical` |

### Vector calculus

| Topic | Slug | Needs |
|---|---|---|
| Describing vector fields | `vector-fields` | `gradient-vector` |
| Finding curl | `curl` | `vector-fields`, `cross-product` |
| Finding divergence | `divergence` | `vector-fields` |
| Using curl and divergence identities | `curl-divergence-identities` | `curl`, `divergence`, `clairaut-mixed-partials` |
| Describing parametric surfaces | `parametric-surfaces` | `tangent-planes`, `surfaces-in-other-coordinates` |
| Sketching vector fields | `vector-fields-sketch` | `vector-fields` |
| Recognizing gradient fields | `gradient-fields` | `vector-fields-sketch` |
| Testing whether a field is conservative | `conservative-test` | `gradient-fields`, `clairaut-mixed-partials` |
| Finding a potential function | `find-potential` | `conservative-test` |
| Parametrizing paths for line integrals | `line-integral-parametrize` | `vector-functions-space-curves`, `functions-of-two-variables` |
| Evaluating scalar line integrals | `line-integrals-scalar` | `arc-length-space-curves`, `line-integral-parametrize` |
| Evaluating line integrals of vector fields | `line-integrals-vector` | `line-integrals-scalar`, `vector-fields` |
| Using the fundamental theorem for line integrals | `fundamental-theorem-line` | `find-potential`, `line-integrals-vector` |
| Using path independence | `path-independence` | `fundamental-theorem-line` |
| Using Green's theorem for circulation | `greens-theorem-circulation` | `line-integrals-vector`, `double-general-regions` |
| Finding area with Green's theorem | `greens-area` | `greens-theorem-circulation`, `calc2.parametric-area` |
| Evaluating line integrals in differential form | `line-integral-differential-form` | `line-integrals-vector` |
| Finding work with a line integral | `work-as-line-integral` | `precalc.work-as-dot-product`, `line-integral-differential-form` |
| Finding flux across a plane curve | `flux-plane-curve` | `line-integrals-vector` |
| Using Green's theorem for flux | `greens-theorem-flux` | `greens-theorem-circulation`, `flux-plane-curve` |
| Finding a potential in three variables | `potential-three-variables` | `find-potential`, `curl` |
| Interpreting curl as rotation | `curl-as-rotation` | `curl` |
| Interpreting divergence as expansion | `divergence-as-expansion` | `divergence` |
| Parametrizing spheres and cylinders | `parametrize-spheres-cylinders` | `parametric-surfaces` |
| Finding tangent planes to parametric surfaces | `tangent-plane-parametric` | `parametrize-spheres-cylinders` |
| Evaluating surface integrals of scalar functions | `surface-integrals-scalar` | `tangent-plane-parametric`, `surface-area-double` |
| Evaluating surface integrals over graphs | `surface-integrals-over-graphs` | `surface-integrals-scalar` |
| Choosing a surface orientation | `surface-orientation` | `surface-integrals-over-graphs` |
| Evaluating flux integrals | `flux-integrals` | `surface-orientation` |
| Using Stokes' theorem | `stokes-theorem` | `flux-integrals`, `greens-theorem-circulation`, `curl-as-rotation` |
| Using the divergence theorem | `divergence-theorem` | `flux-integrals`, `triple-spherical`, `divergence-as-expansion`, `greens-theorem-flux` |
| Using Green's theorem on regions with holes | `greens-with-holes` | `greens-theorem-circulation` |
| Choosing an integral theorem | `choose-integral-theorem` | `stokes-theorem`, `divergence-theorem`, `path-independence`, `greens-with-holes` |
| Interpreting vector calculus in physics | `physical-meaning-vector-calculus` | `choose-integral-theorem` |

## math.linalg: 161 topics, budget 180 (-11%)

### Linear systems

| Topic | Slug | Needs |
|---|---|---|
| Recognizing linear equations in several variables | `linear-equations-review` | `alg2.systems-three-variables` |
| Checking solutions of a linear system | `solution-check-system` | `linear-equations-review` |
| Writing a system as an augmented matrix | `augmented-matrix` | `precalc.matrix-dimensions`, `solution-check-system` |
| Using elementary row operations | `elementary-row-operations` | `augmented-matrix` |
| Recognizing row-equivalent matrices | `row-equivalence` | `elementary-row-operations` |
| Recognizing echelon forms | `identify-echelon-forms` | `elementary-row-operations` |
| Reducing to row echelon form | `row-echelon-form` | `row-equivalence`, `identify-echelon-forms` |
| Reducing to reduced row echelon form | `reduced-row-echelon` | `row-echelon-form` |
| Solving with Gauss-Jordan elimination | `gauss-jordan` | `reduced-row-echelon` |
| Finding pivot and free variables | `pivot-and-free-variables` | `reduced-row-echelon` |
| Writing solutions in parametric form | `parametric-solutions` | `pivot-and-free-variables` |
| Solving homogeneous systems | `homogeneous-systems` | `parametric-solutions` |
| Solving by back substitution | `back-substitution` | `row-echelon-form` |
| Solving with Gaussian elimination | `gaussian-elimination` | `back-substitution` |
| Finding rank from pivots | `rank-from-pivots` | `pivot-and-free-variables` |
| Picturing solution sets in space | `geometry-of-systems` | `linear-equations-review`, `precalc.vectors-in-3d` |
| Deciding the number of solutions | `consistency-and-solutions` | `rank-from-pivots`, `geometry-of-systems` |
| Analyzing systems with a parameter | `systems-with-parameters` | `consistency-and-solutions` |
| Fitting a polynomial through points | `polynomial-through-points` | `gaussian-elimination` |
| Applying linear systems | `applications-of-systems` | `polynomial-through-points` |
| Using systems for networks and balancing | `network-balance-applications` | `gaussian-elimination` |

### Vectors in n-space

| Topic | Slug | Needs |
|---|---|---|
| Working with vectors in n-space | `vectors-in-rn` | `precalc.vector-add-subtract` |
| Using vector algebra rules in n-space | `vector-arithmetic-rn` | `vectors-in-rn` |
| Finding linear combinations | `linear-combinations` | `gaussian-elimination`, `vector-arithmetic-rn` |
| Finding the span of vectors | `span-of-vectors` | `linear-combinations` |
| Multiplying a matrix by a vector as a combination | `matrix-times-vector` | `linear-combinations`, `precalc.matrix-multiply` |
| Writing a system as a vector equation | `vector-equation-of-system` | `matrix-times-vector` |
| Describing solution sets of Ax = b | `solution-set-structure` | `vector-equation-of-system`, `homogeneous-systems` |
| Testing whether a vector is in a span | `membership-in-span` | `span-of-vectors` |
| Describing spans geometrically | `span-geometric` | `span-of-vectors` |
| Defining linear independence | `linear-independence-definition` | `homogeneous-systems`, `membership-in-span`, `span-geometric` |
| Testing whether vectors span n-space | `spanning-rn-test` | `membership-in-span` |
| Picturing linear independence | `independence-geometric` | `linear-independence-definition` |
| Testing for linear independence | `linear-independence-test` | `independence-geometric` |
| Spotting dependence by inspection | `independence-by-inspection` | `linear-independence-test` |
| Finding dependence relations | `dependence-relations` | `independence-by-inspection` |
| Writing a solution as particular plus homogeneous | `particular-plus-homogeneous` | `solution-set-structure` |

### Matrix algebra

| Topic | Slug | Needs |
|---|---|---|
| Viewing matrix products in several ways | `matrix-product-three-views` | `matrix-times-vector` |
| Finding transposes | `transpose` | `matrix-product-three-views` |
| Working with block matrices | `block-matrices` | `matrix-product-three-views` |
| Spotting failures of commutativity and cancellation | `product-noncommutative` | `matrix-product-three-views` |
| Using rules of matrix algebra | `matrix-algebra-rules` | `product-noncommutative` |
| Finding powers of matrices | `powers-of-matrices` | `matrix-algebra-rules` |
| Defining invertible matrices | `invertible-matrices` | `matrix-algebra-rules`, `precalc.inverse-matrix-2x2` |
| Finding an inverse by row reduction | `inverse-by-row-reduction` | `invertible-matrices`, `gauss-jordan` |
| Using elementary matrices | `elementary-matrices` | `inverse-by-row-reduction` |
| Finding an LU factorization | `lu-factorization` | `elementary-matrices` |
| Solving with an LU factorization | `solve-with-lu` | `lu-factorization` |
| Using rules for transposes | `transpose-rules` | `transpose`, `matrix-algebra-rules` |
| Using diagonal, triangular and symmetric matrices | `special-matrices` | `transpose-rules` |
| Using properties of inverses | `inverse-properties` | `invertible-matrices` |
| Using equivalent conditions for invertibility | `invertible-matrix-theorem-basic` | `inverse-by-row-reduction`, `linear-independence-test`, `spanning-rn-test`, `inverse-properties` |
| Solving systems with an inverse | `solve-with-inverse` | `invertible-matrices` |
| Solving matrix equations | `matrix-equations` | `inverse-properties`, `solve-with-inverse` |
| Using a permuted LU factorization | `permuted-lu` | `lu-factorization` |
| Finding the trace | `trace-of-matrix` | `matrix-algebra-rules` |

### Linear transformations

| Topic | Slug | Needs |
|---|---|---|
| Treating a matrix as a transformation | `matrix-as-transformation` | `matrix-times-vector` |
| Defining linear transformations | `linear-transformation-definition` | `matrix-as-transformation` |
| Testing whether a map is linear | `test-linear-or-not` | `linear-transformation-definition` |
| Finding the standard matrix | `standard-matrix` | `test-linear-or-not` |
| Testing one-to-one and onto | `one-to-one-and-onto` | `standard-matrix`, `pivot-and-free-variables` |
| Composing transformations with matrix products | `composition-matrix-product` | `standard-matrix`, `matrix-algebra-rules` |
| Finding inverse transformations | `invertible-transformations` | `composition-matrix-product`, `inverse-by-row-reduction`, `one-to-one-and-onto` |
| Using matrices for shears and projections | `shear-projection-matrices` | `standard-matrix` |
| Using matrices for rotations and reflections | `geometric-transformations-matrices` | `precalc.matrix-rotation`, `shear-projection-matrices` |
| Finding the image of a shape under a transformation | `image-of-a-shape` | `standard-matrix` |

### Determinants

| Topic | Slug | Needs |
|---|---|---|
| Finding determinants by cofactors | `determinant-cofactors` | `precalc.determinants-3x3`, `matrix-algebra-rules` |
| Choosing a row for expansion | `cofactor-expansion-choice` | `determinant-cofactors` |
| Finding determinants of triangular matrices | `det-of-triangular` | `determinant-cofactors` |
| Finding determinants by row reduction | `determinant-row-reduction` | `cofactor-expansion-choice`, `det-of-triangular` |
| Tracking row operations in a determinant | `det-row-op-effects` | `determinant-row-reduction` |
| Using properties of determinants | `determinant-properties` | `det-row-op-effects` |
| Using Cramer's rule and the adjugate | `cramers-rule-general` | `determinant-properties` |
| Seeing a determinant as a volume | `determinant-as-volume` | `determinant-properties`, `geometric-transformations-matrices`, `image-of-a-shape` |
| Testing invertibility with a determinant | `det-invertibility` | `determinant-properties`, `invertible-matrix-theorem-basic` |
| Using determinants of products | `determinant-of-products` | `det-invertibility` |
| Finding when a determinant vanishes | `det-with-parameter` | `det-invertibility`, `systems-with-parameters` |
| Finding an inverse with the adjugate | `adjugate-inverse` | `cramers-rule-general` |

### Vector spaces

| Topic | Slug | Needs |
|---|---|---|
| Understanding the vector space axioms | `vector-space-axioms` | `linear-combinations` |
| Working with polynomial and function spaces | `examples-of-vector-spaces` | `vector-space-axioms` |
| Working with abstract linear transformations | `general-linear-transformations` | `linear-transformation-definition`, `examples-of-vector-spaces` |
| Checking whether a set is a vector space | `test-vector-space` | `vector-space-axioms` |
| Testing subspaces | `subspaces` | `examples-of-vector-spaces`, `test-vector-space` |
| Showing a span is a subspace | `span-as-subspace` | `subspaces`, `span-of-vectors` |
| Finding the null space | `null-space` | `subspaces`, `particular-plus-homogeneous` |
| Finding the column space | `column-space` | `subspaces`, `pivot-and-free-variables` |
| Finding the row space | `row-space` | `column-space`, `transpose` |
| Testing independence of polynomials and functions | `independence-function-spaces` | `examples-of-vector-spaces`, `linear-independence-test` |
| Defining a basis | `basis-definition` | `span-as-subspace`, `independence-function-spaces` |
| Using standard bases of common spaces | `standard-bases` | `basis-definition` |
| Finding a basis | `finding-a-basis` | `standard-bases`, `dependence-relations` |
| Finding coordinates relative to a basis | `coordinates-relative-to-basis` | `finding-a-basis` |
| Changing basis | `change-of-basis` | `coordinates-relative-to-basis`, `inverse-by-row-reduction` |
| Finding the matrix of a transformation in a basis | `matrix-of-transformation` | `general-linear-transformations`, `coordinates-relative-to-basis` |
| Extending and reducing to a basis | `extend-reduce-to-basis` | `finding-a-basis` |
| Finding dimension | `dimension` | `extend-reduce-to-basis` |
| Finding dimensions of subspaces | `dimension-of-subspaces` | `dimension` |
| Finding a transition matrix | `transition-matrix` | `change-of-basis` |
| Finding a basis for a column space | `basis-of-column-space` | `column-space`, `finding-a-basis` |
| Using the rank-nullity theorem | `rank-nullity` | `null-space`, `dimension-of-subspaces`, `basis-of-column-space` |
| Finding kernel and range | `kernel-and-range` | `general-linear-transformations`, `rank-nullity` |
| Recognizing isomorphic spaces | `isomorphism-of-spaces` | `kernel-and-range`, `invertible-transformations` |
| Deciding solvability from rank | `solvability-from-rank` | `rank-nullity` |
| Relating the four fundamental subspaces | `four-fundamental-subspaces` | `row-space`, `solvability-from-rank` |
| Finding matrices of compositions | `matrix-of-composition` | `matrix-of-transformation`, `composition-matrix-product` |
| Using similar matrices | `similar-matrices` | `transition-matrix`, `matrix-of-composition`, `determinant-of-products` |

### Eigenvalues

| Topic | Slug | Needs |
|---|---|---|
| Defining eigenvalues and eigenvectors | `eigen-definition` | `null-space` |
| Checking an eigenvector | `eigen-check` | `eigen-definition` |
| Finding the characteristic polynomial | `characteristic-polynomial` | `det-with-parameter`, `eigen-check` |
| Finding eigenvalues | `find-eigenvalues` | `characteristic-polynomial`, `alg2.solve-polynomial-equations` |
| Finding eigenvectors | `find-eigenvectors` | `find-eigenvalues` |
| Comparing algebraic and geometric multiplicity | `eigenspaces-multiplicity` | `find-eigenvectors` |
| Using trace and triangular shortcuts | `eigen-triangular-tricks` | `find-eigenvalues`, `special-matrices`, `trace-of-matrix` |
| Working with complex eigenvalues | `complex-eigenvalues` | `find-eigenvalues`, `alg2.quadratics-complex-solutions` |
| Picturing eigenvectors geometrically | `eigen-geometric` | `eigen-definition`, `geometric-transformations-matrices` |
| Reading rotation and scaling from complex eigenvalues | `rotation-scaling-form` | `complex-eigenvalues`, `eigen-geometric` |
| Using the Cayley-Hamilton theorem | `cayley-hamilton` | `characteristic-polynomial`, `powers-of-matrices` |
| Testing whether a matrix is diagonalizable | `diagonalizable-test` | `eigenspaces-multiplicity` |
| Proving eigenvectors for distinct eigenvalues are independent | `eigenvector-independence` | `find-eigenvectors` |
| Diagonalizing a matrix | `diagonalization` | `similar-matrices`, `diagonalizable-test`, `eigenvector-independence` |
| Finding matrix powers by diagonalizing | `powers-by-diagonalization` | `diagonalization`, `powers-of-matrices` |
| Using Markov chains | `markov-chains` | `powers-by-diagonalization` |
| Modelling with discrete dynamical systems | `discrete-dynamical-systems` | `powers-by-diagonalization` |
| Using eigenvalues on systems of differential equations | `systems-of-odes-preview` | `diagonalization` |
| Finding eigenvalues of a linear transformation | `eigen-of-transformation` | `matrix-of-transformation`, `find-eigenvectors` |
| Exploring Jordan form | `jordan-form-intro` | `diagonalizable-test` |
| Finding a steady state | `stationary-distribution` | `markov-chains` |
| Applying eigenvectors to ranking | `pagerank-example` | `stationary-distribution` |

### Orthogonality

| Topic | Slug | Needs |
|---|---|---|
| Using the inner product in n-space | `inner-product-rn` | `vectors-in-rn` |
| Finding lengths, angles and orthogonality | `length-angle-orthogonal` | `inner-product-rn` |
| Finding orthogonal complements | `orthogonal-complements` | `length-angle-orthogonal`, `four-fundamental-subspaces` |
| Using orthogonal sets and bases | `orthogonal-sets` | `length-angle-orthogonal`, `finding-a-basis` |
| Using the Cauchy-Schwarz and triangle inequalities | `cauchy-schwarz-triangle` | `length-angle-orthogonal` |
| Working with general inner product spaces | `inner-product-spaces` | `examples-of-vector-spaces`, `cauchy-schwarz-triangle` |
| Finding coordinates in an orthogonal basis | `orthogonal-coordinates` | `orthogonal-sets` |
| Using orthogonal matrices | `orthonormal-matrices` | `transpose`, `orthogonal-coordinates` |
| Projecting onto a line | `project-onto-line` | `length-angle-orthogonal` |
| Finding orthogonal projections | `orthogonal-projection` | `orthogonal-coordinates`, `project-onto-line` |
| Finding projection matrices | `projection-matrix` | `orthogonal-projection`, `matrix-algebra-rules` |
| Finding the closest point in a subspace | `closest-point` | `orthogonal-projection` |
| Solving least squares with normal equations | `least-squares-normal` | `orthogonal-complements`, `closest-point` |
| Fitting lines and curves with least squares | `least-squares-line-fit` | `least-squares-normal` |
| Splitting a vector into orthogonal parts | `split-into-orthogonal-parts` | `orthogonal-projection` |
| Using the Gram-Schmidt process | `gram-schmidt` | `split-into-orthogonal-parts` |
| Finding a QR factorization | `qr-factorization` | `gram-schmidt` |
| Deciding uniqueness of least squares | `least-squares-uniqueness` | `least-squares-normal` |
| Solving least squares with QR | `least-squares-qr` | `qr-factorization`, `least-squares-uniqueness` |
| Finding projections in function spaces | `function-space-projection` | `inner-product-spaces`, `orthogonal-projection` |

### Symmetric matrices and SVD

| Topic | Slug | Needs |
|---|---|---|
| Diagonalizing symmetric matrices | `spectral-theorem` | `diagonalization`, `orthonormal-matrices` |
| Orthogonally diagonalizing a matrix | `orthogonal-diagonalization` | `spectral-theorem` |
| Working with quadratic forms | `quadratic-forms` | `orthogonal-diagonalization` |
| Testing positive definiteness | `positive-definite` | `quadratic-forms` |
| Using the principal axes theorem | `principal-axes` | `quadratic-forms`, `precalc.rotated-conic-intro` |
| Optimizing a quadratic form on the unit sphere | `constrained-quadratic` | `quadratic-forms` |
| Finding singular values | `singular-values` | `rank-nullity`, `constrained-quadratic` |
| Finding a singular value decomposition | `svd-compute` | `singular-values` |
| Using the pseudoinverse | `pseudoinverse` | `svd-compute`, `least-squares-normal` |
| Picturing the SVD geometrically | `svd-geometric` | `svd-compute` |
| Using low-rank approximation | `low-rank-approximation` | `svd-geometric` |
| Applying principal component analysis | `principal-component-analysis` | `low-rank-approximation` |
| Exploring Hermitian matrices | `hermitian-intro` | `spectral-theorem`, `complex-eigenvalues` |

## math.diffeq: 156 topics, budget 190 (-18%)

### First-order equations

| Topic | Slug | Needs |
|---|---|---|
| Classifying differential equations | `classify-odes` | `calc2.intro-differential-equations` |
| Analyzing direction fields | `direction-fields-analysis` | `calc2.slope-fields`, `classify-odes` |
| Moving from tangent lines to Euler's method | `tangent-line-to-euler` | `calc2.eulers-method-intro`, `direction-fields-analysis` |
| Identifying order and linearity | `order-linearity-identify` | `classify-odes` |
| Checking solutions of differential equations | `solution-checking` | `order-linearity-identify` |
| Telling general from particular solutions | `general-and-particular` | `solution-checking` |
| Solving separable equations with care | `separable-odes` | `calc2.separable-equations`, `general-and-particular` |
| Sketching with isoclines | `isoclines` | `direction-fields-analysis` |
| Analyzing autonomous equations | `autonomous-equations` | `isoclines` |
| Classifying equilibria by stability | `equilibrium-stability` | `autonomous-equations` |
| Drawing phase lines | `phase-lines` | `equilibrium-stability` |
| Modelling populations | `modelling-population` | `phase-lines`, `calc2.logistic-de` |
| Leaving separable solutions implicit | `separable-implicit` | `separable-odes` |
| Finding lost and singular solutions | `singular-solutions` | `separable-implicit` |
| Writing a linear equation in standard form | `linear-first-order-standard` | `classify-odes` |
| Exploring why integrating factors work | `integrating-factors-intro` | `linear-first-order-standard` |
| Solving linear first-order equations | `linear-first-order` | `integrating-factors-intro` |
| Solving Bernoulli equations | `bernoulli-equations` | `linear-first-order` |
| Exploring Riccati equations | `riccati-intro` | `bernoulli-equations` |
| Modelling falling objects with drag | `modelling-falling-objects` | `linear-first-order`, `separable-odes` |
| Modelling simple circuits | `modelling-circuits-first` | `linear-first-order` |
| Finding the interval of validity | `interval-of-validity` | `separable-odes`, `linear-first-order` |
| Using existence and uniqueness | `existence-uniqueness-first` | `interval-of-validity` |
| Solving linear equations with piecewise coefficients | `linear-with-piecewise` | `linear-first-order` |
| Testing whether an equation is exact | `exact-test` | `calc3.clairaut-mixed-partials` |
| Solving exact equations | `exact-equations` | `calc3.find-potential`, `exact-test` |
| Making equations exact | `exact-integrating-factors` | `exact-equations`, `linear-first-order` |
| Using a general linear substitution | `linear-substitution-general` | `separable-odes` |
| Using homogeneous substitution | `homogeneous-substitution` | `linear-substitution-general` |
| Reading long-term behaviour from a solution | `long-term-behaviour` | `linear-first-order` |
| Modelling tank mixing | `modelling-mixing` | `long-term-behaviour` |
| Choosing a first-order method | `choose-first-order-method` | `bernoulli-equations`, `homogeneous-substitution`, `exact-integrating-factors` |
| Modelling harvesting | `harvesting-model` | `modelling-population` |
| Exploring bifurcations | `bifurcations-intro` | `harvesting-model` |
| Finding orthogonal trajectories | `orthogonal-trajectories` | `separable-odes` |
| Modelling with variable gravity | `variable-gravity-model` | `modelling-falling-objects` |
| Modelling heating and cooling | `heating-cooling-model` | `linear-first-order` |
| Using Picard iteration | `picard-iteration` | `existence-uniqueness-first` |
| Building an Euler table | `euler-by-hand` | `tangent-line-to-euler` |
| Analyzing Euler's method error | `euler-error` | `calc2.taylor-remainder`, `euler-by-hand` |
| Using improved Euler and Runge-Kutta methods | `improved-euler-rk4` | `euler-error` |

### Second-order linear equations

| Topic | Slug | Needs |
|---|---|---|
| Introducing second-order linear equations | `second-order-intro` | `linear-first-order` |
| Using linear operators and superposition | `linear-operator-superposition` | `second-order-intro` |
| Using Euler's formula | `euler-formula` | `calc2.maclaurin-common` |
| Writing the characteristic equation | `characteristic-equation` | `second-order-intro`, `alg1.choose-quadratic-method` |
| Solving with real distinct roots | `constant-coefficients-real` | `linear-operator-superposition`, `characteristic-equation` |
| Solving with complex roots | `constant-coefficients-complex` | `constant-coefficients-real`, `euler-formula` |
| Using undetermined coefficients with polynomials and exponentials | `undetermined-coefficients-poly-exp` | `constant-coefficients-real` |
| Using undetermined coefficients with trig forcing | `undetermined-coefficients-trig` | `undetermined-coefficients-poly-exp`, `constant-coefficients-complex` |
| Combining forcing terms | `superposition-forcing` | `undetermined-coefficients-trig` |
| Solving Cauchy-Euler equations | `cauchy-euler` | `constant-coefficients-complex` |
| Testing independence of functions | `linear-independence-functions` | `linear-operator-superposition` |
| Using the Wronskian | `wronskian` | `precalc.determinants-2x2`, `linear-independence-functions` |
| Finding fundamental solution sets | `fundamental-solution-sets` | `wronskian` |
| Using reduction of order | `reduction-of-order` | `fundamental-solution-sets` |
| Using variation of parameters | `variation-of-parameters` | `fundamental-solution-sets`, `undetermined-coefficients-poly-exp` |
| Using Abel's theorem | `abel-theorem` | `wronskian` |
| Solving initial value problems with real roots | `ivp-real-roots` | `constant-coefficients-real` |
| Solving with repeated roots | `constant-coefficients-repeated` | `reduction-of-order`, `ivp-real-roots` |
| Solving initial value problems with complex roots | `ivp-complex-roots` | `constant-coefficients-complex` |
| Solving initial and boundary value problems | `initial-boundary-values` | `ivp-complex-roots` |
| Reading long-term behaviour from roots | `behaviour-from-roots` | `constant-coefficients-complex` |
| Writing oscillations with amplitude and phase | `amplitude-phase-form` | `constant-coefficients-complex` |
| Finding roots for higher-order equations | `higher-order-roots` | `constant-coefficients-repeated` |
| Solving higher-order homogeneous equations | `higher-order-homogeneous` | `constant-coefficients-complex`, `higher-order-roots` |
| Guessing forms for products of forcing terms | `undetermined-product-forms` | `undetermined-coefficients-trig` |
| Adjusting guesses for repeated forms | `undetermined-coefficients-resonance` | `undetermined-product-forms` |
| Using undetermined coefficients at higher order | `undetermined-higher-order` | `undetermined-coefficients-resonance`, `higher-order-homogeneous` |
| Choosing a method for forced equations | `forced-method-choice` | `variation-of-parameters`, `undetermined-coefficients-resonance`, `superposition-forcing` |
| Using variation of parameters with initial conditions | `variation-with-ivp` | `variation-of-parameters` |
| Solving forced Cauchy-Euler equations | `cauchy-euler-forced` | `cauchy-euler`, `variation-of-parameters` |
| Setting up spring-mass equations | `spring-setup` | `second-order-intro` |
| Modelling free oscillations | `free-oscillation` | `amplitude-phase-form`, `spring-setup` |
| Modelling damped oscillations | `damped-oscillation` | `free-oscillation`, `behaviour-from-roots` |
| Modelling RLC circuits | `rlc-circuits` | `damped-oscillation`, `modelling-circuits-first` |
| Telling overdamped from critically damped | `overdamped-critical` | `damped-oscillation` |
| Modelling forced oscillations | `forced-oscillation` | `undetermined-coefficients-trig`, `overdamped-critical` |
| Understanding beats | `beats` | `forced-oscillation` |
| Separating steady and transient behaviour | `steady-transient` | `forced-oscillation` |
| Understanding resonance | `resonance` | `beats`, `steady-transient` |
| Modelling forced RLC circuits | `rlc-forced` | `rlc-circuits`, `resonance` |

### Laplace transforms

| Topic | Slug | Needs |
|---|---|---|
| Defining the Laplace transform | `laplace-definition` | `calc2.improper-infinite-limits` |
| Testing existence of a Laplace transform | `laplace-existence` | `laplace-definition` |
| Finding basic transforms | `laplace-basic-transforms` | `calc2.parts-cyclic`, `laplace-existence` |
| Using a table of transforms | `laplace-table` | `laplace-basic-transforms` |
| Using linearity and shifting | `laplace-properties` | `laplace-table` |
| Finding inverse transforms | `inverse-laplace` | `laplace-properties`, `calc2.partial-fractions-linear` |
| Transforming derivatives | `laplace-of-derivatives` | `laplace-properties` |
| Using step functions | `step-functions-laplace` | `laplace-properties` |
| Using the first shifting theorem | `laplace-first-shift` | `laplace-properties` |
| Inverting with completed squares | `inverse-laplace-completing-square` | `inverse-laplace`, `alg1.complete-the-square-expression`, `laplace-first-shift` |
| Transforming t times a function | `laplace-t-multiplication` | `laplace-properties` |
| Inverting with quadratic factors | `laplace-quadratic-factors` | `inverse-laplace`, `precalc.partial-fractions-quadratic` |
| Solving initial value problems with Laplace transforms | `solve-ivp-laplace` | `laplace-of-derivatives`, `inverse-laplace-completing-square`, `laplace-quadratic-factors` |
| Using convolution | `convolution` | `solve-ivp-laplace` |
| Using transfer functions | `transfer-functions` | `convolution` |
| Writing piecewise functions with step functions | `piecewise-as-step` | `step-functions-laplace` |
| Using the second shifting theorem | `second-shift` | `step-functions-laplace` |
| Solving with discontinuous forcing | `discontinuous-forcing` | `solve-ivp-laplace`, `piecewise-as-step`, `second-shift` |
| Using impulse functions | `impulse-delta` | `discontinuous-forcing` |
| Transforming periodic functions | `periodic-laplace` | `laplace-properties`, `calc2.geometric-series-calc` |
| Solving systems with Laplace transforms | `laplace-systems` | `solve-ivp-laplace`, `systems-first-order-intro` |

### Power series solutions

| Topic | Slug | Needs |
|---|---|---|
| Shifting the index of a series | `series-shift-index` | `calc2.differentiate-integrate-series` |
| Finding series solutions of first-order equations | `series-first-order` | `series-shift-index`, `classify-odes` |
| Finding series solutions near an ordinary point | `series-solutions-ordinary` | `second-order-intro`, `series-first-order` |
| Finding recurrence relations from series | `recurrence-from-series` | `series-solutions-ordinary` |
| Solving Airy and Legendre equations by series | `airy-legendre-examples` | `recurrence-from-series` |
| Classifying singular points | `singular-points` | `series-solutions-ordinary` |
| Finding a lower bound on the radius of a series solution | `series-solution-radius` | `series-solutions-ordinary` |
| Solving the indicial equation | `frobenius-indicial` | `singular-points` |
| Using the method of Frobenius | `frobenius` | `recurrence-from-series`, `frobenius-indicial` |
| Handling repeated indicial roots | `frobenius-repeated-roots` | `frobenius` |
| Introducing Bessel functions | `bessel-intro` | `frobenius-repeated-roots` |

### Systems of equations

| Topic | Slug | Needs |
|---|---|---|
| Introducing first-order systems | `systems-first-order-intro` | `second-order-intro` |
| Checking a solution of a system | `verify-system-solution` | `systems-first-order-intro` |
| Converting a higher-order equation to a system | `convert-to-system` | `verify-system-solution` |
| Writing a system in matrix form | `matrix-form-systems` | `convert-to-system`, `linalg.matrix-times-vector` |
| Writing systems from applications | `system-from-application` | `systems-first-order-intro` |
| Using superposition for systems | `superposition-systems` | `matrix-form-systems` |
| Solving with real eigenvalues | `eigen-solutions-real` | `linalg.find-eigenvectors`, `superposition-systems` |
| Solving with complex eigenvalues | `eigen-solutions-complex` | `eigen-solutions-real`, `linalg.complex-eigenvalues`, `euler-formula` |
| Solving with repeated eigenvalues | `eigen-solutions-repeated` | `eigen-solutions-real`, `linalg.eigenspaces-multiplicity` |
| Drawing phase portraits with real eigenvalues | `phase-portraits-real` | `eigen-solutions-real` |
| Drawing phase portraits with complex eigenvalues | `phase-portraits-complex` | `eigen-solutions-complex`, `phase-portraits-real` |
| Modelling coupled tanks and springs | `coupled-tanks-springs` | `eigen-solutions-complex`, `modelling-mixing`, `system-from-application` |
| Testing fundamental sets of systems | `fundamental-set-systems` | `superposition-systems` |
| Solving initial value problems for systems | `ivp-systems` | `eigen-solutions-real` |
| Using fundamental matrices | `fundamental-matrices` | `fundamental-set-systems`, `ivp-systems` |
| Using generalized eigenvectors | `generalized-eigenvectors` | `eigen-solutions-repeated`, `linalg.jordan-form-intro` |
| Using undetermined coefficients for systems | `undetermined-systems` | `eigen-solutions-real` |
| Solving nonhomogeneous systems | `nonhomogeneous-systems` | `fundamental-matrices`, `variation-of-parameters`, `undetermined-systems` |
| Decoupling a system by diagonalizing | `decouple-by-diagonalizing` | `eigen-solutions-real`, `linalg.diagonalization` |
| Using the matrix exponential | `matrix-exponential` | `decouple-by-diagonalizing` |
| Drawing phase portraits with repeated eigenvalues | `phase-portrait-repeated` | `phase-portraits-real`, `generalized-eigenvectors` |
| Classifying stability of linear systems | `stability-of-linear-systems` | `phase-portraits-complex`, `phase-portrait-repeated` |
| Classifying with trace and determinant | `trace-determinant-plane` | `stability-of-linear-systems` |

### Nonlinear systems

| Topic | Slug | Needs |
|---|---|---|
| Finding equilibria of nonlinear systems | `nonlinear-equilibria` | `stability-of-linear-systems`, `alg2.nonlinear-systems` |
| Solving systems numerically | `numerical-systems` | `improved-euler-rk4`, `convert-to-system` |
| Drawing nullclines | `nullclines` | `nonlinear-equilibria` |
| Linearizing at equilibria | `linearization-jacobian` | `calc3.linearization-multivariable`, `nullclines`, `trace-determinant-plane` |
| Modelling predator and prey | `predator-prey` | `linearization-jacobian` |
| Modelling competing species | `competing-species` | `linearization-jacobian` |
| Exploring limit cycles | `limit-cycles-intro` | `predator-prey` |
| Using conserved quantities | `conserved-quantities` | `nonlinear-equilibria` |
| Analyzing a nonlinear pendulum | `nonlinear-pendulum` | `linearization-jacobian`, `free-oscillation`, `conserved-quantities` |
| Exploring Lyapunov functions | `lyapunov-intro` | `linearization-jacobian` |

### Introductory boundary problems and Fourier

| Topic | Slug | Needs |
|---|---|---|
| Telling when boundary problems have solutions | `boundary-solvability` | `constant-coefficients-complex` |
| Solving two-point boundary eigenvalue problems | `boundary-value-eigenproblems` | `boundary-solvability` |
| Finding sine and cosine eigenfunctions | `sine-cosine-eigenfunctions` | `boundary-value-eigenproblems` |
| Seeing orthogonality of sines and cosines | `trig-orthogonality-intro` | `calc2.trig-products-different-angles` |
| Introducing Fourier series | `fourier-series-intro` | `calc2.parts-cyclic`, `sine-cosine-eigenfunctions`, `trig-orthogonality-intro` |
| Using even and odd Fourier series | `fourier-even-odd` | `fourier-series-intro`, `calc1.integrate-even-odd` |
| Finding Fourier series of piecewise functions | `fourier-piecewise-compute` | `fourier-series-intro` |
| Stating Fourier convergence | `fourier-convergence-statement` | `fourier-piecewise-compute` |
| Finding half-range expansions | `fourier-half-range` | `fourier-even-odd` |
| Previewing separation of variables | `separation-of-variables-preview` | `calc3.partial-differential-equation-check`, `fourier-half-range` |

## math.discrete: 153 topics, budget 170 (-10%)

### Logic

| Topic | Slug | Needs |
|---|---|---|
| Working with propositions | `propositions` | `geom.truth-values` |
| Building truth tables | `truth-tables` | `propositions` |
| Using logical connectives | `logical-connectives` | `truth-tables` |
| Using conditionals and biconditionals | `conditional-biconditional-logic` | `logical-connectives`, `geom.biconditionals` |
| Finding tautologies and contradictions | `tautologies-contradictions` | `truth-tables` |
| Using predicates | `predicates` | `propositions` |
| Using quantifiers | `quantifiers` | `predicates` |
| Using nested quantifiers | `nested-quantifiers` | `quantifiers` |
| Translating English into logic | `translating-english-logic` | `quantifiers`, `conditional-biconditional-logic` |
| Using exclusive or and other connectives | `exclusive-or-nand` | `logical-connectives` |
| Connecting logic to circuits | `digital-logic-gates` | `exclusive-or-nand` |
| Finding converse, inverse and contrapositive | `converse-contrapositive-logic` | `conditional-biconditional-logic` |
| Showing logical equivalence | `logical-equivalence` | `converse-contrapositive-logic`, `tautologies-contradictions` |
| Using De Morgan's laws | `de-morgan-logic` | `logical-equivalence` |
| Negating quantified statements | `negating-quantifiers` | `de-morgan-logic`, `nested-quantifiers` |
| Using rules of inference | `rules-of-inference` | `logical-equivalence`, `translating-english-logic` |
| Writing disjunctive and conjunctive normal forms | `normal-forms` | `logical-equivalence` |
| Using Boolean algebra | `boolean-algebra` | `de-morgan-logic`, `normal-forms`, `digital-logic-gates` |
| Testing satisfiability | `satisfiability-intro` | `truth-tables` |
| Using inference rules with quantifiers | `quantifier-inference` | `rules-of-inference` |
| Spotting logical fallacies | `fallacies` | `rules-of-inference` |
| Using Karnaugh maps | `karnaugh-maps` | `boolean-algebra` |
| Minimizing Boolean expressions | `boolean-minimization` | `karnaugh-maps` |

### Proof

| Topic | Slug | Needs |
|---|---|---|
| Writing direct proofs | `direct-proof-discrete` | `quantifier-inference` |
| Proving by contrapositive | `contrapositive-proof-discrete` | `direct-proof-discrete` |
| Proving by contradiction | `contradiction-proof-discrete` | `contrapositive-proof-discrete` |
| Proving by cases | `cases-proof-discrete` | `direct-proof-discrete` |
| Proving by induction | `induction-weak` | `direct-proof-discrete`, `precalc.induction-sums` |
| Proving divisibility by induction | `induction-divisibility` | `induction-weak` |
| Proving inequalities by induction | `induction-inequalities-discrete` | `induction-weak` |
| Proving by strong induction | `induction-strong` | `induction-divisibility`, `induction-inequalities-discrete` |
| Using structural induction | `induction-structural` | `induction-strong`, `recursive-definitions` |
| Using the well-ordering principle | `well-ordering` | `induction-strong` |
| Disproving with counterexamples | `counterexamples-discrete` | `negating-quantifiers` |

### Sets, functions and relations

| Topic | Slug | Needs |
|---|---|---|
| Using set notation | `sets-notation` | `alg2.sample-space-set-notation` |
| Translating between set descriptions | `set-description-translation` | `sets-notation` |
| Using set operations | `set-operations` | `set-description-translation` |
| Using power sets and Cartesian products | `power-sets-cartesian` | `set-operations` |
| Defining functions on sets | `functions-discrete` | `power-sets-cartesian` |
| Using floor and ceiling functions | `floor-ceiling-discrete` | `functions-discrete` |
| Defining relations | `relations-definition` | `power-sets-cartesian` |
| Testing properties of relations | `relation-properties` | `relations-definition` |
| Using equivalence relations | `equivalence-relations` | `relation-properties` |
| Using partial orders | `partial-orders` | `relation-properties` |
| Drawing Hasse diagrams | `hasse-diagrams` | `partial-orders` |
| Representing relations with matrices and digraphs | `matrix-digraph-relations` | `relations-definition`, `precalc.matrix-multiply` |
| Proving set identities by elements | `set-proofs-elementwise` | `set-operations`, `direct-proof-discrete` |
| Using set identities | `venn-and-identities` | `de-morgan-logic`, `set-proofs-elementwise` |
| Working with sum and product notation | `sums-products-notation` | `alg2.sigma-properties` |
| Finding images and preimages | `images-preimages-discrete` | `functions-discrete` |
| Testing injective and surjective functions | `injective-surjective` | `images-preimages-discrete` |
| Composing and inverting functions | `composition-inverses-discrete` | `injective-surjective`, `alg2.verify-inverses-composition` |
| Using cardinality of finite sets | `cardinality-finite` | `composition-inverses-discrete` |
| Telling countable from uncountable sets | `countable-sets` | `cardinality-finite` |
| Showing the rationals are countable | `rationals-countable-discrete` | `countable-sets` |
| Using total orders and lattices | `total-orders-lattices` | `hasse-diagrams` |
| Finding equivalence classes | `equivalence-classes-discrete` | `equivalence-relations` |
| Using partitions | `partitions` | `equivalence-classes-discrete` |
| Composing relations | `relation-composition` | `relation-properties` |
| Finding transitive closures | `transitive-closure` | `matrix-digraph-relations`, `relation-composition` |
| Using Warshall's algorithm | `warshall` | `transitive-closure` |

### Number theory

| Topic | Slug | Needs |
|---|---|---|
| Proving divisibility facts | `divisibility-discrete` | `direct-proof-discrete` |
| Using the division algorithm | `division-algorithm` | `divisibility-discrete`, `floor-ceiling-discrete` |
| Using the Euclidean algorithm | `euclidean-algorithm` | `division-algorithm` |
| Using Bezout's identity | `bezout` | `euclidean-algorithm` |
| Using modular arithmetic | `modular-arithmetic` | `division-algorithm`, `equivalence-relations` |
| Finding modular inverses | `modular-inverses` | `modular-arithmetic`, `bezout` |
| Solving linear congruences | `linear-congruences` | `modular-inverses` |
| Using the Chinese remainder theorem | `chinese-remainder` | `linear-congruences` |
| Converting number bases | `number-bases` | `division-algorithm` |
| Testing primes and using a sieve | `primes-and-sieve` | `divisibility-discrete` |
| Using the fundamental theorem of arithmetic | `primes-fundamental-theorem` | `well-ordering`, `primes-and-sieve` |
| Proving there are infinitely many primes | `infinitely-many-primes` | `primes-fundamental-theorem`, `contradiction-proof-discrete` |
| Finding gcd and lcm from prime factorizations | `gcd-lcm-factorization` | `primes-fundamental-theorem` |
| Using fast modular exponentiation | `modular-exponentiation` | `modular-arithmetic` |
| Using Fermat's little theorem | `fermat-little` | `primes-fundamental-theorem`, `modular-exponentiation` |
| Using Euler's totient theorem | `euler-totient` | `fermat-little` |
| Applying RSA cryptography | `rsa-cryptography` | `euler-totient`, `modular-inverses` |
| Applying modular arithmetic to check digits | `check-digits` | `modular-arithmetic` |
| Doing arithmetic in other bases | `base-arithmetic` | `number-bases` |

### Counting

| Topic | Slug | Needs |
|---|---|---|
| Using sum and product rules | `sum-product-rules` | `alg2.factorial-notation`, `set-operations` |
| Using inclusion-exclusion for two sets | `inclusion-exclusion-two` | `sum-product-rules`, `venn-and-identities` |
| Using general inclusion-exclusion | `inclusion-exclusion-general` | `inclusion-exclusion-two` |
| Using the pigeonhole principle | `pigeonhole` | `sum-product-rules` |
| Using the generalized pigeonhole principle | `generalized-pigeonhole` | `pigeonhole` |
| Counting derangements | `derangements` | `inclusion-exclusion-general` |
| Counting with tree diagrams | `tree-diagrams-count` | `sum-product-rules` |
| Counting permutations | `permutations-discrete` | `tree-diagrams-count` |
| Counting combinations | `combinations-discrete` | `permutations-discrete`, `alg2.combinations` |
| Using stars and bars | `stars-and-bars` | `combinations-discrete` |
| Finding discrete probabilities by counting | `discrete-probability-counting` | `combinations-discrete`, `alg2.counting-probability` |
| Using linearity of expectation | `expected-value-discrete` | `discrete-probability-counting` |
| Using Bayes' rule in discrete settings | `bayes-discrete` | `discrete-probability-counting` |
| Counting with restrictions | `counting-with-restrictions` | `combinations-discrete` |
| Counting functions and surjections | `counting-functions` | `inclusion-exclusion-general`, `injective-surjective`, `counting-with-restrictions` |
| Counting permutations with repeats | `permutations-with-repetition` | `permutations-discrete` |
| Using multinomial coefficients | `multinomial` | `combinations-discrete`, `permutations-with-repetition` |
| Using Pascal's identity | `pascal-identity` | `combinations-discrete` |
| Using binomial coefficient identities | `binomial-coefficients-identities` | `alg2.binomial-theorem`, `pascal-identity` |
| Writing combinatorial proofs | `combinatorial-proofs` | `binomial-coefficients-identities` |
| Exploring Catalan numbers | `catalan-numbers` | `binomial-coefficients-identities`, `solve-recurrences-iteration` |
| Counting set partitions | `set-partition-counting` | `counting-functions`, `recursive-definitions` |

### Recurrences and algorithms

| Topic | Slug | Needs |
|---|---|---|
| Writing recursive definitions | `recursive-definitions` | `alg2.recursive-sequences` |
| Reading algorithms in pseudocode | `algorithms-pseudocode` | `recursive-definitions` |
| Using big-O notation | `big-o` | `algorithms-pseudocode`, `precalc.exponential-compare-growth-rates` |
| Setting up a recurrence from a problem | `setup-recurrence` | `recursive-definitions` |
| Solving recurrences by iteration | `solve-recurrences-iteration` | `sums-products-notation`, `setup-recurrence` |
| Solving linear homogeneous recurrences | `linear-homogeneous-recurrences` | `solve-recurrences-iteration`, `alg1.choose-quadratic-method` |
| Finding the closed form of Fibonacci numbers | `fibonacci-closed-form` | `linear-homogeneous-recurrences` |
| Using generating functions | `generating-functions-intro` | `linear-homogeneous-recurrences`, `alg2.binomial-theorem` |
| Counting with generating functions | `generating-functions-counting` | `generating-functions-intro`, `stars-and-bars` |
| Solving divide-and-conquer recurrences | `divide-and-conquer-recurrences` | `solve-recurrences-iteration`, `alg2.log-power-rule` |
| Using the master theorem | `master-theorem-intro` | `divide-and-conquer-recurrences` |
| Solving recurrences with repeated roots | `recurrence-repeated-roots` | `linear-homogeneous-recurrences` |
| Solving nonhomogeneous recurrences | `nonhomogeneous-recurrences` | `recurrence-repeated-roots` |
| Ordering growth rates | `growth-rate-ordering` | `big-o` |
| Using big-theta and big-omega | `big-theta-omega` | `growth-rate-ordering` |
| Analyzing simple algorithm runtimes | `algorithm-runtime` | `big-theta-omega` |
| Analyzing searching and sorting | `searching-sorting-analysis` | `algorithm-runtime`, `master-theorem-intro`, `binary-search-trees` |
| Analyzing greedy algorithms | `greedy-algorithms` | `algorithm-runtime` |
| Proving algorithms with loop invariants | `loop-invariants` | `algorithms-pseudocode`, `induction-weak` |
| Analyzing recursive algorithms | `recursive-algorithms` | `algorithm-runtime`, `solve-recurrences-iteration` |

### Graphs and trees

| Topic | Slug | Needs |
|---|---|---|
| Using graph terminology | `graph-terminology` | `sets-notation` |
| Using the handshake lemma | `degree-handshake` | `graph-terminology` |
| Representing graphs with matrices | `graph-representations` | `graph-terminology`, `precalc.matrix-multiply` |
| Testing graph isomorphism | `isomorphism-graphs` | `graph-representations` |
| Finding paths and connectivity | `paths-connectivity` | `graph-terminology` |
| Counting walks with matrix powers | `counting-walks-matrix-powers` | `graph-representations`, `paths-connectivity` |
| Finding Euler paths and circuits | `euler-paths` | `paths-connectivity`, `degree-handshake` |
| Finding Hamilton paths and circuits | `hamilton-paths` | `paths-connectivity` |
| Testing planar graphs | `planar-graphs` | `paths-connectivity` |
| Using Euler's formula for planar graphs | `euler-formula-planar` | `planar-graphs` |
| Using directed graphs | `directed-graphs` | `graph-terminology` |
| Exploring network flow | `network-flow-intro` | `directed-graphs` |
| Finding subgraphs and complements | `subgraphs-complements` | `graph-terminology` |
| Recognizing special graphs | `special-graphs` | `subgraphs-complements` |
| Testing bipartite graphs | `bipartite-graphs` | `special-graphs` |
| Coloring graphs | `graph-coloring` | `planar-graphs`, `bipartite-graphs` |
| Using matchings and Hall's theorem | `matchings-hall` | `bipartite-graphs` |
| Finding connected components | `connected-components` | `paths-connectivity` |
| Defining trees | `trees-definition` | `induction-weak`, `connected-components` |
| Proving properties of trees | `tree-properties` | `trees-definition`, `induction-structural` |
| Using rooted and binary trees | `rooted-binary-trees` | `tree-properties` |
| Using tree traversals | `tree-traversals` | `rooted-binary-trees` |
| Searching with breadth and depth first | `breadth-depth-search` | `paths-connectivity`, `algorithms-pseudocode` |
| Finding shortest paths with Dijkstra's algorithm | `shortest-paths` | `breadth-depth-search` |
| Finding spanning trees | `spanning-trees` | `tree-properties`, `breadth-depth-search` |
| Finding minimum spanning trees | `minimum-spanning-trees` | `spanning-trees`, `greedy-algorithms` |
| Finding a topological order | `topological-sort` | `directed-graphs`, `partial-orders`, `breadth-depth-search` |
| Recognizing non-planar graphs | `non-planar-graphs` | `euler-formula-planar` |
| Finding chromatic numbers | `chromatic-number` | `graph-coloring` |
| Using binary search trees | `binary-search-trees` | `rooted-binary-trees` |
| Building Huffman codes | `huffman-codes` | `rooted-binary-trees`, `greedy-algorithms` |

## math.probstat: 162 topics, budget 190 (-15%)

### Probability foundations

| Topic | Slug | Needs |
|---|---|---|
| Describing sample spaces and events | `sample-spaces-events` | `alg2.sample-space-set-notation` |
| Using set operations on events | `set-operations-events` | `sample-spaces-events` |
| Using the axioms of probability | `axioms-of-probability` | `set-operations-events` |
| Proving consequences of the axioms | `consequences-of-axioms` | `axioms-of-probability` |
| Defining conditional probability | `conditional-probability-definition` | `axioms-of-probability`, `alg2.conditional-probability` |
| Testing independence of events | `independence-events` | `conditional-probability-definition` |
| Counting with permutations and combinations | `counting-for-probability` | `alg2.combinations` |
| Finding probabilities by counting | `equally-likely-counting` | `axioms-of-probability`, `alg2.counting-probability`, `counting-for-probability` |
| Using inclusion-exclusion for probability | `inclusion-exclusion-prob` | `consequences-of-axioms` |
| Finding conditional probabilities from tables | `conditional-from-tables` | `conditional-probability-definition` |
| Using the multiplication law | `multiplication-law` | `conditional-from-tables` |
| Using tree diagrams | `tree-diagrams-prob` | `multiplication-law` |
| Using the law of total probability | `total-probability` | `tree-diagrams-prob` |
| Using Bayes' theorem | `bayes-theorem` | `total-probability`, `stats.bayes-intro` |
| Applying Bayes' theorem to testing | `diagnostic-test-bayes` | `bayes-theorem` |
| Telling independent from disjoint events | `independent-vs-disjoint` | `independence-events` |
| Using mutual independence | `mutual-independence` | `independent-vs-disjoint` |
| Finding reliability of systems | `reliability-systems` | `mutual-independence` |
| Using conditional independence | `conditional-independence` | `mutual-independence` |

### Discrete random variables

| Topic | Slug | Needs |
|---|---|---|
| Defining random variables | `random-variable-definition` | `axioms-of-probability` |
| Building a distribution from an experiment | `distribution-from-experiment` | `random-variable-definition` |
| Using probability mass functions | `pmf` | `distribution-from-experiment` |
| Finding expected value | `expectation-discrete` | `pmf` |
| Finding expected values of functions | `expectation-of-functions` | `expectation-discrete` |
| Using the hypergeometric distribution | `hypergeometric` | `expectation-discrete`, `equally-likely-counting` |
| Using moment generating functions for discrete variables | `mgf-discrete` | `expectation-of-functions`, `calc2.maclaurin-common` |
| Finding a constant to make a valid distribution | `pmf-valid` | `pmf` |
| Using cumulative distribution functions for discrete variables | `cdf-discrete` | `pmf-valid` |
| Recovering a mass function from a CDF | `cdf-to-pmf` | `cdf-discrete` |
| Using properties of expectation | `expectation-properties` | `expectation-of-functions` |
| Finding variance | `variance-discrete` | `expectation-properties` |
| Using linear transformations of random variables | `linear-transformations-rv` | `variance-discrete` |
| Using Bernoulli and binomial distributions | `bernoulli-binomial` | `variance-discrete`, `stats.binomial-mean-sd` |
| Using the Poisson distribution | `poisson` | `bernoulli-binomial`, `calc2.maclaurin-common` |
| Finding the binomial mean and variance | `binomial-mean-variance` | `bernoulli-binomial` |
| Approximating a binomial with a Poisson distribution | `poisson-approx-binomial` | `poisson`, `binomial-mean-variance` |
| Using the geometric distribution | `geometric-distribution` | `variance-discrete`, `calc2.geometric-series-calc` |
| Using geometric and negative binomial distributions | `geometric-negative-binomial` | `bernoulli-binomial`, `geometric-distribution` |
| Exploring Poisson processes | `poisson-process-intro` | `poisson` |
| Finding moments from a generating function | `mgf-moments` | `mgf-discrete` |

### Continuous random variables

| Topic | Slug | Needs |
|---|---|---|
| Using probability density functions | `pdf` | `random-variable-definition`, `calc2.probability-density-integral` |
| Finding expected values of continuous variables | `expectation-continuous` | `pdf`, `calc2.expected-value-integral` |
| Finding variances of continuous variables | `variance-continuous` | `expectation-continuous` |
| Using the uniform distribution | `uniform-distribution` | `variance-continuous` |
| Using the exponential distribution | `exponential-distribution` | `variance-continuous`, `poisson-process-intro` |
| Using the memoryless property | `memoryless-property` | `exponential-distribution`, `conditional-probability-definition` |
| Using the gamma distribution | `gamma-distribution` | `exponential-distribution` |
| Using the gamma function | `gamma-function` | `gamma-distribution` |
| Using the normal density | `normal-distribution-pdf` | `variance-continuous`, `stats.normal-calculations`, `calc3.gaussian-integral` |
| Standardizing normal variables | `standardizing` | `normal-distribution-pdf`, `linear-transformations-rv` |
| Using the beta distribution | `beta-distribution` | `gamma-function` |
| Using moment generating functions for continuous variables | `mgf-continuous` | `expectation-continuous`, `mgf-moments` |
| Finding a constant to make a valid density | `density-constant` | `pdf` |
| Using cumulative distribution functions for continuous variables | `cdf-continuous` | `calc1.ftc-part-1`, `density-constant` |
| Finding distributions of functions by the CDF method | `functions-of-rv-cdf` | `cdf-continuous` |
| Finding distributions by the change of variables method | `functions-of-rv-transform` | `functions-of-rv-cdf` |
| Recovering a density from a CDF | `cdf-to-pdf` | `cdf-continuous` |
| Finding percentiles of continuous variables | `percentiles-continuous` | `cdf-to-pdf` |
| Working with mixed distributions | `mixed-distributions` | `cdf-continuous` |
| Using normal tables | `normal-tables` | `standardizing` |
| Finding distributions of normal sums | `normal-linear-combinations` | `mgf-for-sums`, `standardizing` |
| Using the lognormal distribution | `lognormal` | `functions-of-rv-transform`, `standardizing` |
| Using hazard rates | `hazard-rates` | `exponential-distribution` |
| Using the chi-square distribution | `chi-square-distribution` | `gamma-function`, `standardizing` |
| Introducing chi-square, t and F distributions | `chi-square-t-f-intro` | `chi-square-distribution`, `transformations-joint` |

### Joint distributions

| Topic | Slug | Needs |
|---|---|---|
| Using joint probability mass functions | `joint-pmf` | `pmf` |
| Using joint density functions | `joint-pdf` | `pdf`, `calc3.probability-double` |
| Using the multinomial distribution | `multinomial-distribution` | `joint-pmf`, `bernoulli-binomial` |
| Using joint transformations | `transformations-joint` | `joint-pdf`, `calc3.jacobian`, `functions-of-rv-transform` |
| Using joint cumulative distribution functions | `joint-cdf` | `joint-pdf` |
| Finding marginal distributions | `marginal-distributions` | `joint-pmf`, `joint-cdf` |
| Finding conditional distributions | `conditional-distributions` | `marginal-distributions`, `conditional-probability-definition` |
| Testing independence of random variables | `independence-rv` | `marginal-distributions` |
| Finding conditional expectation | `conditional-expectation` | `conditional-distributions` |
| Using the law of total expectation | `law-of-total-expectation` | `conditional-expectation` |
| Finding sums of variables by convolution | `sums-by-convolution` | `independence-rv` |
| Finding probabilities over regions | `joint-probability-regions` | `joint-pdf` |
| Finding expected values of joint functions | `expectation-joint` | `marginal-distributions`, `joint-probability-regions` |
| Finding covariance | `covariance` | `expectation-joint`, `variance-discrete` |
| Finding correlation | `correlation` | `covariance`, `stats.correlation-properties` |
| Testing independence by factoring | `independence-factorization` | `independence-rv` |
| Using moment generating functions for sums | `mgf-for-sums` | `mgf-continuous`, `independence-factorization` |
| Using properties of covariance | `covariance-properties` | `covariance` |
| Finding the variance of a sum | `variance-of-sums` | `covariance-properties` |
| Telling uncorrelated from independent | `uncorrelated-vs-independent` | `correlation`, `independence-rv` |
| Using the bivariate normal distribution | `bivariate-normal` | `standardizing`, `uncorrelated-vs-independent` |
| Finding the mean and variance of a sample mean | `sample-mean-moments` | `variance-of-sums` |
| Using the law of total variance | `total-variance` | `law-of-total-expectation` |
| Finding moments of random sums | `random-sums` | `law-of-total-expectation` |
| Exploring the multivariate normal | `multivariate-normal-intro` | `bivariate-normal` |

### Limit theorems

| Topic | Slug | Needs |
|---|---|---|
| Using Markov's and Chebyshev's inequalities | `markov-chebyshev` | `variance-continuous` |
| Simulating random variables | `simulation-random-variables` | `functions-of-rv-cdf`, `uniform-distribution` |
| Using convergence in probability | `convergence-in-probability` | `markov-chebyshev` |
| Using the law of large numbers | `law-of-large-numbers` | `sample-mean-moments`, `convergence-in-probability` |
| Using convergence in distribution | `convergence-in-distribution` | `mgf-continuous` |
| Using the central limit theorem | `central-limit-theorem-formal` | `mgf-for-sums`, `standardizing`, `convergence-in-distribution` |
| Approximating binomials with the normal distribution | `normal-approx-binomial` | `central-limit-theorem-formal`, `bernoulli-binomial`, `normal-tables` |
| Using the continuity correction | `continuity-correction` | `normal-approx-binomial` |
| Applying the central limit theorem to sums and means | `clt-sums-means` | `central-limit-theorem-formal` |
| Finding the sampling distribution of the mean | `sampling-distribution-of-mean` | `stats.sampling-mean`, `normal-linear-combinations`, `clt-sums-means` |
| Finding the sampling distribution of the variance | `sample-variance-distribution` | `chi-square-t-f-intro`, `sampling-distribution-of-mean` |
| Finding the distribution of a minimum or maximum | `min-max-distribution` | `functions-of-rv-cdf`, `independence-rv` |
| Using order statistics | `order-statistics` | `min-max-distribution` |

### Estimation

| Topic | Slug | Needs |
|---|---|---|
| Defining point estimators | `point-estimators` | `sampling-distribution-of-mean` |
| Using the method of moments | `method-of-moments` | `point-estimators` |
| Writing a likelihood function | `likelihood-function` | `point-estimators` |
| Using sufficient statistics | `sufficient-statistics` | `likelihood-function` |
| Using Bayesian estimation | `bayesian-estimation` | `likelihood-function`, `bayes-theorem`, `beta-distribution` |
| Finding large-sample intervals for a mean | `ci-large-sample-mean` | `sampling-distribution-of-mean`, `stats.ci-idea` |
| Finding intervals for proportions | `ci-proportion-calc` | `ci-large-sample-mean`, `normal-approx-binomial` |
| Finding intervals for a variance | `ci-variance` | `sample-variance-distribution` |
| Finding a sample size for a given precision | `sample-size-calc` | `ci-proportion-calc` |
| Testing unbiased estimators | `unbiased-estimators` | `point-estimators` |
| Using bias, variance and mean squared error | `bias-variance-mse` | `unbiased-estimators` |
| Testing consistency and efficiency | `consistency-efficiency` | `bias-variance-mse`, `law-of-large-numbers` |
| Finding maximum likelihood estimates for discrete models | `mle-discrete` | `likelihood-function` |
| Finding maximum likelihood estimates for continuous models | `mle-continuous` | `mle-discrete` |
| Finding maximum likelihood estimates | `maximum-likelihood` | `mle-continuous` |
| Using properties of maximum likelihood estimators | `mle-properties` | `maximum-likelihood`, `consistency-efficiency` |
| Using Fisher information and the Cramer-Rao bound | `fisher-information` | `mle-properties` |
| Using conjugate priors | `conjugate-priors` | `bayesian-estimation` |
| Interpreting confidence intervals | `ci-interpretation` | `ci-large-sample-mean` |
| Finding small-sample t intervals | `ci-small-sample-t` | `sample-variance-distribution`, `ci-interpretation` |
| Finding intervals for two samples | `ci-two-samples` | `ci-small-sample-t`, `ci-proportion-calc` |
| Building intervals with pivotal quantities | `pivotal-quantities` | `ci-small-sample-t` |

### Hypothesis testing

| Topic | Slug | Needs |
|---|---|---|
| Using the hypothesis testing framework | `hypothesis-framework` | `ci-large-sample-mean`, `stats.null-alternative` |
| Testing a mean | `test-for-mean` | `hypothesis-framework`, `ci-small-sample-t` |
| Testing a proportion | `test-for-proportion` | `hypothesis-framework`, `ci-proportion-calc` |
| Testing a variance | `test-for-variance` | `hypothesis-framework`, `ci-variance` |
| Using paired tests | `paired-tests` | `test-for-mean` |
| Interpreting p-values formally | `p-values-formal` | `hypothesis-framework` |
| Recognizing multiple testing | `multiple-testing-issue` | `p-values-formal` |
| Using chi-square goodness of fit | `goodness-of-fit` | `hypothesis-framework`, `chi-square-t-f-intro`, `multinomial-distribution` |
| Testing independence in contingency tables | `independence-contingency` | `goodness-of-fit` |
| Using F tests for two variances | `f-test-variances` | `test-for-variance` |
| Using the bootstrap | `bootstrap` | `simulation-random-variables`, `ci-large-sample-mean` |
| Using rejection regions | `rejection-regions` | `hypothesis-framework` |
| Finding error rates and power | `type-errors-power-calc` | `rejection-regions` |
| Using the Neyman-Pearson lemma | `neyman-pearson` | `type-errors-power-calc`, `likelihood-function` |
| Using likelihood ratio tests | `likelihood-ratio-tests` | `neyman-pearson`, `maximum-likelihood` |
| Drawing power curves | `power-curves` | `type-errors-power-calc` |
| Finding a sample size for power | `sample-size-for-power` | `type-errors-power-calc` |
| Connecting tests to confidence intervals | `test-ci-duality` | `test-for-mean` |
| Testing two proportions | `two-proportion-test` | `test-for-proportion` |
| Comparing two samples | `two-sample-tests` | `test-for-mean`, `ci-two-samples`, `two-proportion-test` |
| Using nonparametric tests | `nonparametric-tests` | `two-sample-tests` |
| Telling pooled from unpooled tests | `pooled-unpooled` | `two-sample-tests` |
| Using one-way analysis of variance | `anova-one-way` | `f-test-variances`, `pooled-unpooled` |
| Building an analysis of variance table | `anova-table-compute` | `anova-one-way` |
| Comparing groups after analysis of variance | `anova-post-hoc` | `multiple-testing-issue`, `anova-table-compute` |
| Exploring two-way analysis of variance | `anova-two-way-intro` | `anova-one-way` |

### Regression

| Topic | Slug | Needs |
|---|---|---|
| Writing the simple linear regression model | `simple-linear-model` | `stats.least-squares-regression`, `point-estimators` |
| Deriving least squares estimates | `least-squares-derivation` | `simple-linear-model`, `calc3.least-squares-from-calculus` |
| Finding the sampling distribution of the slope | `sampling-of-slope` | `least-squares-derivation`, `variance-of-sums` |
| Using inference for regression | `inference-for-regression` | `sampling-of-slope`, `test-for-mean` |
| Using prediction and confidence intervals | `prediction-confidence-bands` | `inference-for-regression` |
| Checking regression assumptions | `regression-diagnostics` | `inference-for-regression`, `stats.residual-analysis` |
| Connecting correlation and regression | `correlation-regression-link` | `least-squares-derivation`, `correlation` |
| Reading an analysis of variance table for regression | `r-squared-anova-table` | `inference-for-regression`, `anova-one-way`, `correlation-regression-link` |
| Transforming variables in regression | `transforming-for-regression` | `regression-diagnostics` |
| Using multiple regression | `multiple-regression-intro` | `transforming-for-regression` |
| Exploring logistic regression | `logistic-regression-intro` | `multiple-regression-intro`, `maximum-likelihood` |

## math.proofs: 91 topics, budget 110 (-17%)

### Logic for proof

| Topic | Slug | Needs |
|---|---|---|
| Reading mathematical statements | `statements-and-sets-of-truth` | `geom.conditional-statements` |
| Using mathematical writing conventions | `math-writing-conventions` | `statements-and-sets-of-truth` |
| Using definitions in proofs | `definitions-and-their-use` | `math-writing-conventions` |
| Reading and checking proofs | `reading-proofs` | `definitions-and-their-use` |
| Translating statements into symbols | `translating-statements` | `statements-and-sets-of-truth` |
| Reading conditional statements in proof | `conditional-forms-proof` | `statements-and-sets-of-truth` |
| Handling quantifiers in proofs | `quantifiers-in-proofs` | `definitions-and-their-use`, `conditional-forms-proof` |
| Negating statements in practice | `negation-in-practice` | `quantifiers-in-proofs`, `translating-statements` |
| Using a proof outline | `proof-outlines` | `definitions-and-their-use` |
| Proving nested quantifier statements | `nested-quantifier-proofs` | `quantifiers-in-proofs`, `direct-proofs` |

### Proof techniques

| Topic | Slug | Needs |
|---|---|---|
| Writing direct proofs | `direct-proofs` | `proof-outlines` |
| Proving parity facts | `proofs-about-parity` | `direct-proofs` |
| Proving divisibility facts | `proofs-about-divisibility` | `direct-proofs` |
| Proving by contrapositive | `contrapositive-proofs` | `direct-proofs` |
| Proving by cases | `cases-proofs` | `direct-proofs` |
| Proving if-and-only-if statements | `iff-proofs` | `contrapositive-proofs` |
| Proving existence | `existence-proofs` | `negation-in-practice` |
| Proving uniqueness | `uniqueness-proofs` | `existence-proofs` |
| Disproving by counterexample | `counterexample-writing` | `negation-in-practice` |
| Proving by induction | `induction-proofs` | `direct-proofs`, `precalc.induction-sums` |
| Proving inequalities by induction | `induction-inequalities` | `induction-proofs` |
| Proving recursive facts by induction | `induction-recursive` | `induction-proofs` |
| Proving simple inequalities | `proofs-with-inequalities` | `direct-proofs` |
| Proving facts about rational numbers | `proofs-about-rationals` | `direct-proofs` |
| Using without loss of generality | `wlog-cases` | `cases-proofs` |
| Proving absolute value facts | `absolute-value-proofs` | `proofs-with-inequalities`, `wlog-cases` |
| Choosing between direct and contrapositive proof | `direct-or-contrapositive` | `contrapositive-proofs` |
| Proving by contradiction | `contradiction-proofs` | `direct-or-contrapositive` |
| Proving irrationality | `irrationality-proofs` | `contradiction-proofs`, `proofs-about-rationals`, `proofs-about-parity` |
| Telling constructive from nonconstructive proofs | `constructive-nonconstructive` | `existence-proofs` |
| Proving divisibility by induction | `induction-divisibility-proofs` | `induction-proofs` |
| Proving by strong induction | `strong-induction-proofs` | `induction-divisibility-proofs` |
| Proving with well-ordering | `well-ordering-proofs` | `strong-induction-proofs` |
| Proving Fibonacci-style facts | `fibonacci-style-proofs` | `strong-induction-proofs`, `induction-recursive` |
| Choosing a proof method | `choosing-a-proof-method` | `contradiction-proofs`, `induction-proofs`, `cases-proofs` |
| Finding errors in proofs | `proof-writing-errors` | `reading-proofs`, `choosing-a-proof-method` |

### Sets

| Topic | Slug | Needs |
|---|---|---|
| Using set-builder notation | `set-builder-proofs` | `definitions-and-their-use`, `precalc.set-builder-notation` |
| Proving statements by chasing elements | `element-chasing` | `set-builder-proofs`, `direct-proofs` |
| Proving subset relations | `subset-proofs` | `element-chasing` |
| Proving set equality | `set-equality-proofs` | `subset-proofs`, `iff-proofs` |
| Proving facts about unions and intersections | `union-intersection-proofs` | `set-equality-proofs`, `cases-proofs` |
| Proving facts about power sets | `power-set-proofs` | `subset-proofs` |
| Proving facts about Cartesian products | `cartesian-products` | `subset-proofs` |
| Working with indexed families of sets | `indexed-families` | `union-intersection-proofs` |
| Proving facts about set differences | `set-difference-proofs` | `union-intersection-proofs` |
| Proving De Morgan's laws for sets | `complement-de-morgan-proofs` | `set-difference-proofs` |
| Disproving set statements | `disproving-set-claims` | `subset-proofs`, `counterexample-writing` |

### Relations

| Topic | Slug | Needs |
|---|---|---|
| Treating relations as sets | `relations-as-sets` | `cartesian-products` |
| Testing reflexive, symmetric and transitive properties | `testing-relation-properties` | `relations-as-sets` |
| Proving equivalence relations | `equivalence-relation-proofs` | `testing-relation-properties` |
| Working with equivalence classes | `equivalence-classes` | `equivalence-relation-proofs` |
| Proving partitions and equivalence relations correspond | `partition-theorem` | `equivalence-classes` |
| Proving facts about congruence mod n | `congruence-mod-n` | `equivalence-classes`, `proofs-about-divisibility` |
| Proving order relations | `order-relations` | `testing-relation-properties` |
| Working with bounds in ordered sets | `least-upper-bounds-intro` | `order-relations`, `quantifiers-in-proofs` |
| Proving arithmetic mod n is well defined | `mod-n-well-defined` | `congruence-mod-n` |

### Functions

| Topic | Slug | Needs |
|---|---|---|
| Treating functions as relations | `functions-as-relations` | `relations-as-sets` |
| Proving injectivity | `injective-proofs` | `functions-as-relations` |
| Proving surjectivity | `surjective-proofs` | `functions-as-relations` |
| Testing whether a function is well-defined | `well-defined-functions` | `functions-as-relations`, `mod-n-well-defined` |
| Deciding whether a relation is a function | `testing-functions` | `functions-as-relations` |
| Working with images and preimages | `image-preimage` | `set-equality-proofs`, `testing-functions` |
| Proving facts about images and unions | `image-preimage-proofs` | `image-preimage`, `indexed-families` |
| Disproving injectivity and surjectivity | `disproving-inj-surj` | `injective-proofs`, `surjective-proofs`, `counterexample-writing` |
| Proving bijections | `bijection-proofs` | `disproving-inj-surj` |
| Proving facts about compositions | `composition-proofs` | `bijection-proofs` |
| Proving facts about inverse functions | `inverse-function-proofs` | `composition-proofs` |
| Proving left and right inverses | `left-right-inverses` | `inverse-function-proofs` |

### Cardinality

| Topic | Slug | Needs |
|---|---|---|
| Proving sets have the same size | `equal-cardinality` | `bijection-proofs` |
| Proving facts about finite sets | `finite-sets-proofs` | `equal-cardinality`, `induction-proofs` |
| Proving with the pigeonhole principle | `pigeonhole-proofs` | `finite-sets-proofs` |
| Proving a set is countable | `countable-sets-proofs` | `equal-cardinality` |
| Using Cantor's diagonal argument | `uncountable-diagonal` | `countable-sets-proofs`, `contradiction-proofs` |
| Using Cantor's theorem for power sets | `cantor-power-set` | `uncountable-diagonal`, `power-set-proofs` |
| Proving the integers are countable | `integers-countable` | `countable-sets-proofs` |
| Proving unions of countable sets are countable | `countable-unions` | `countable-sets-proofs` |
| Proving the rationals are countable | `rationals-countable` | `integers-countable`, `countable-unions` |
| Proving intervals have the same size | `intervals-same-size` | `equal-cardinality` |
| Using the Cantor-Schroeder-Bernstein theorem | `schroeder-bernstein` | `intervals-same-size` |

### Number theory and introductory analysis proofs

| Topic | Slug | Needs |
|---|---|---|
| Proving with the division algorithm | `division-algorithm-proofs` | `proofs-about-divisibility`, `well-ordering-proofs` |
| Proving facts about greatest common divisors | `gcd-proofs` | `division-algorithm-proofs` |
| Proving simple facts from axioms | `group-axiom-proofs` | `uniqueness-proofs` |
| Proving binomial identities | `binomial-proofs` | `induction-proofs`, `alg2.binomial-theorem` |
| Proving Bezout's identity | `bezout-proofs` | `gcd-proofs` |
| Proving facts with congruences | `congruence-proofs` | `congruence-mod-n` |
| Proving facts about primes | `prime-proofs` | `bezout-proofs`, `congruence-proofs` |
| Proving the fundamental theorem of arithmetic | `fundamental-theorem-proof` | `prime-proofs` |
| Proving bounds on sets of reals | `real-bound-proofs` | `least-upper-bounds-intro` |
| Proving a sequence's limit | `sequences-limit-proofs` | `absolute-value-proofs`, `nested-quantifier-proofs`, `real-bound-proofs` |
| Proving a sum rule for limits | `limit-sum-rule-proof` | `sequences-limit-proofs` |
| Proving a function's limit | `function-limit-proofs` | `precalc.limit-intuition`, `limit-sum-rule-proof` |

## math.analysis: 146 topics, budget 160 (-9%)

### Real numbers

| Topic | Slug | Needs |
|---|---|---|
| Using the field and order axioms | `axioms-of-reals` | `proofs.group-axiom-proofs`, `proofs.order-relations` |
| Proving absolute value inequalities | `absolute-value-inequalities-analysis` | `axioms-of-reals`, `proofs.absolute-value-proofs` |
| Using the triangle inequality | `triangle-inequality` | `absolute-value-inequalities-analysis` |
| Proving Bernoulli's inequality | `bernoulli-inequality` | `proofs.induction-inequalities` |
| Finding upper and lower bounds | `bounds-of-sets` | `axioms-of-reals` |
| Finding suprema and infima | `supremum-infimum` | `proofs.least-upper-bounds-intro`, `bounds-of-sets` |
| Proving a number is a supremum | `sup-proofs` | `supremum-infimum` |
| Using the completeness axiom | `completeness-axiom` | `sup-proofs` |
| Using the Archimedean property | `archimedean-property` | `completeness-axiom` |
| Proving density of the rationals | `density-of-rationals` | `archimedean-property` |
| Proving square roots exist | `existence-of-roots` | `completeness-axiom` |
| Using nested intervals | `nested-intervals` | `completeness-axiom` |
| Proving suprema of sums and multiples | `sup-of-combinations` | `sup-proofs` |
| Working with decimal expansions | `decimal-expansions` | `archimedean-property` |
| Proving the reals are uncountable | `countability-reals` | `nested-intervals`, `proofs.uncountable-diagonal`, `decimal-expansions` |

### Sequences

| Topic | Slug | Needs |
|---|---|---|
| Using the epsilon definition of a sequence limit | `sequence-limit-definition` | `proofs.sequences-limit-proofs`, `triangle-inequality` |
| Proving limits of sequences | `sequence-limit-proofs` | `sequence-limit-definition` |
| Proving a sequence diverges | `sequence-divergence-proofs` | `sequence-limit-definition` |
| Using the monotone convergence theorem | `monotone-convergence` | `completeness-axiom`, `sequence-limit-proofs`, `bernoulli-inequality` |
| Working with subsequences | `subsequences` | `sequence-limit-proofs` |
| Using the Bolzano-Weierstrass theorem | `bolzano-weierstrass` | `nested-intervals`, `subsequences` |
| Using Cauchy sequences | `cauchy-sequences` | `bolzano-weierstrass` |
| Proving limits are unique | `uniqueness-of-limits` | `sequence-limit-definition` |
| Proving convergent sequences are bounded | `bounded-convergent` | `sequence-limit-proofs` |
| Proving limit laws for sequences | `limit-laws-proofs` | `uniqueness-of-limits`, `bounded-convergent` |
| Proving limits preserve order | `limits-and-order` | `limit-laws-proofs` |
| Proving the squeeze theorem | `squeeze-proofs` | `limits-and-order` |
| Proving recursive sequences converge | `recursive-sequence-proofs` | `monotone-convergence` |
| Proving standard limits | `standard-limit-proofs` | `limit-laws-proofs`, `bernoulli-inequality` |
| Proving divergence to infinity | `divergence-to-infinity` | `sequence-divergence-proofs` |
| Finding subsequential limits | `subsequential-limits` | `subsequences` |
| Using limit superior and inferior | `limsup-liminf` | `monotone-convergence`, `divergence-to-infinity`, `subsequential-limits` |
| Proving Cauchy sequences converge | `cauchy-convergent-proof` | `cauchy-sequences` |
| Using completeness through Cauchy sequences | `completeness-from-cauchy` | `cauchy-convergent-proof` |

### Series

| Topic | Slug | Needs |
|---|---|---|
| Defining convergence of series | `series-convergence-formal` | `limit-laws-proofs`, `calc2.series-as-partial-sums` |
| Using the Cauchy criterion for series | `cauchy-criterion-series` | `series-convergence-formal`, `cauchy-sequences` |
| Proving absolute convergence implies convergence | `absolute-convergence-proof` | `cauchy-criterion-series` |
| Proving the alternating series test | `alternating-proof` | `monotone-convergence`, `series-convergence-formal` |
| Exploring rearrangements of series | `rearrangements` | `absolute-convergence-proof` |
| Proving geometric series convergence | `geometric-proofs` | `series-convergence-formal` |
| Proving the divergence test | `term-test-proof` | `series-convergence-formal` |
| Proving comparison tests | `comparison-proofs` | `monotone-convergence`, `geometric-proofs`, `term-test-proof` |
| Proving ratio and root tests | `ratio-root-proofs` | `comparison-proofs`, `limsup-liminf`, `standard-limit-proofs` |
| Using Cauchy condensation | `condensation-test` | `comparison-proofs` |
| Using Dirichlet and Abel tests | `dirichlet-abel-tests` | `alternating-proof` |
| Using Cauchy products of series | `series-products` | `absolute-convergence-proof` |

### Topology of the reals

| Topic | Slug | Needs |
|---|---|---|
| Working with open and closed sets | `open-closed-sets` | `supremum-infimum` |
| Working with limit points | `limit-points` | `open-closed-sets`, `sequence-limit-proofs` |
| Working with connected sets | `connected-sets` | `open-closed-sets` |
| Proving unions and intersections of open sets | `open-sets-proofs` | `open-closed-sets` |
| Finding closure and interior | `closure-interior` | `limit-points`, `open-sets-proofs` |
| Exploring perfect sets and the Cantor set | `perfect-and-cantor` | `closure-interior`, `proofs.uncountable-diagonal` |
| Characterizing closed sets with sequences | `closed-via-sequences` | `limit-points` |
| Defining compactness with sequences | `compact-sets-sequences` | `bolzano-weierstrass`, `closed-via-sequences` |
| Defining compactness with open covers | `compact-sets-covers` | `compact-sets-sequences` |
| Showing sets are not compact | `compact-nonexamples` | `compact-sets-covers` |
| Using the Heine-Borel theorem | `heine-borel` | `compact-nonexamples` |
| Proving properties of compact sets | `compact-properties` | `heine-borel` |
| Working with dense sets | `dense-sets` | `closure-interior`, `density-of-rationals` |

### Continuity

| Topic | Slug | Needs |
|---|---|---|
| Using the epsilon-delta limit definition | `function-limit-epsilon-delta` | `sequence-limit-definition`, `calc1.epsilon-delta-quadratic` |
| Proving function limits | `function-limit-proofs-analysis` | `function-limit-epsilon-delta`, `proofs.function-limit-proofs` |
| Using the sequential criterion for limits | `sequential-criterion` | `function-limit-proofs-analysis` |
| Proving a limit does not exist | `limit-nonexistence-proofs` | `sequential-criterion` |
| Using the epsilon-delta definition of continuity | `continuity-definition-analysis` | `limit-nonexistence-proofs` |
| Using uniform continuity | `uniform-continuity` | `continuity-definition-analysis` |
| Proving continuity on compact sets is uniform | `heine-cantor` | `uniform-continuity`, `compact-sets-covers` |
| Using Lipschitz functions | `lipschitz-functions` | `uniform-continuity` |
| Proving one-sided limits | `one-sided-limits-analysis` | `function-limit-proofs-analysis` |
| Classifying discontinuities of monotone functions | `discontinuities-monotone` | `continuity-definition-analysis`, `monotone-convergence`, `one-sided-limits-analysis` |
| Proving limit laws for functions | `limit-laws-functions` | `sequential-criterion` |
| Proving combinations of continuous functions | `continuity-algebra-proofs` | `continuity-definition-analysis`, `limit-laws-proofs`, `limit-laws-functions` |
| Testing continuity of unusual functions | `unusual-function-continuity` | `continuity-definition-analysis`, `density-of-rationals` |
| Proving continuous images of compact sets are compact | `continuous-image-compact` | `continuity-definition-analysis`, `compact-sets-sequences` |
| Proving the extreme value theorem | `extreme-value-proof` | `continuous-image-compact` |
| Proving continuous images of connected sets are connected | `continuous-image-connected` | `continuity-definition-analysis`, `connected-sets` |
| Proving the intermediate value theorem | `intermediate-value-proof` | `continuous-image-connected` |
| Proving a function is not uniformly continuous | `uniform-nonexamples` | `uniform-continuity` |
| Proving inverse functions are continuous | `inverse-continuous` | `intermediate-value-proof` |
| Proving a fixed point from the intermediate value theorem | `fixed-point-from-ivt` | `intermediate-value-proof` |

### Differentiation

| Topic | Slug | Needs |
|---|---|---|
| Proving derivatives from the definition | `derivative-definition-analysis` | `function-limit-proofs-analysis`, `calc1.differentiability` |
| Proving differentiation rules | `differentiation-rule-proofs` | `derivative-definition-analysis`, `continuity-algebra-proofs` |
| Proving the chain rule | `chain-rule-proof` | `differentiation-rule-proofs` |
| Proving the interior extremum theorem | `interior-extremum` | `derivative-definition-analysis` |
| Proving Rolle's theorem | `rolle-proof` | `interior-extremum`, `extreme-value-proof` |
| Proving the mean value theorem | `mvt-proof` | `rolle-proof` |
| Using Darboux's theorem | `darboux-theorem` | `interior-extremum` |
| Proving the derivative of an inverse function | `inverse-function-derivative-proof` | `differentiation-rule-proofs`, `inverse-continuous` |
| Proving Taylor's theorem | `taylor-theorem-analysis` | `mvt-proof`, `calc2.taylor-remainder` |
| Proving monotonicity from the derivative | `monotone-from-derivative` | `mvt-proof` |
| Using the mean value theorem in proofs | `mvt-applications-analysis` | `monotone-from-derivative` |
| Proving inequalities with the mean value theorem | `inequalities-from-mvt` | `mvt-proof` |
| Proving the generalized mean value theorem | `cauchy-mvt` | `mvt-proof` |
| Proving L'Hopital's rule | `lhopital-proof` | `cauchy-mvt` |
| Proving the second derivative test | `second-derivative-test-proof` | `taylor-theorem-analysis` |

### Riemann integration

| Topic | Slug | Needs |
|---|---|---|
| Using partitions and Darboux sums | `partitions-upper-lower-sums` | `supremum-infimum`, `calc1.definite-integral-definition` |
| Finding Darboux sums | `computing-darboux-sums` | `partitions-upper-lower-sums` |
| Using refinements of partitions | `refinement-lemmas` | `computing-darboux-sums` |
| Defining Riemann integrability | `riemann-integrable-definition` | `refinement-lemmas` |
| Showing a function is not integrable | `non-integrable-examples` | `riemann-integrable-definition`, `density-of-rationals` |
| Relating Riemann and Darboux sums | `riemann-vs-darboux` | `riemann-integrable-definition` |
| Using the Riemann criterion | `integrability-criterion` | `riemann-vs-darboux` |
| Proving continuous functions are integrable | `continuous-implies-integrable` | `integrability-criterion`, `heine-cantor` |
| Proving monotone functions are integrable | `monotone-integrable` | `integrability-criterion` |
| Finding an integral from the definition | `integrate-from-definition` | `integrability-criterion` |
| Proving properties of the integral | `integral-properties-proofs` | `integrate-from-definition` |
| Proving functions with few discontinuities are integrable | `finite-discontinuities` | `continuous-implies-integrable` |
| Proving the mean value theorem for integrals | `mvt-integrals-proof` | `integral-properties-proofs`, `intermediate-value-proof` |
| Proving the fundamental theorem of calculus | `ftc-proofs` | `mvt-proof`, `mvt-integrals-proof` |
| Proving integration by parts | `integration-by-parts-proof` | `ftc-proofs`, `differentiation-rule-proofs` |
| Working with improper integrals rigorously | `improper-integrals-analysis` | `ftc-proofs`, `comparison-proofs` |
| Proving the substitution rule | `substitution-proof` | `ftc-proofs`, `chain-rule-proof` |
| Stating the Lebesgue criterion | `lebesgue-criterion-statement` | `continuous-implies-integrable` |

### Sequences and series of functions

| Topic | Slug | Needs |
|---|---|---|
| Using pointwise convergence | `pointwise-convergence` | `sequence-limit-proofs`, `continuity-definition-analysis` |
| Showing pointwise limits lose continuity | `pointwise-failures` | `pointwise-convergence` |
| Using uniform convergence | `uniform-convergence` | `pointwise-failures` |
| Proving uniform limits are continuous | `uniform-limit-continuous` | `uniform-convergence` |
| Exchanging limits and integrals | `uniform-limit-integral` | `uniform-limit-continuous`, `integral-properties-proofs` |
| Exchanging limits and derivatives | `uniform-limit-derivative` | `uniform-limit-integral`, `mvt-applications-analysis` |
| Using the Weierstrass approximation theorem | `weierstrass-approximation` | `uniform-convergence`, `heine-cantor` |
| Exploring convergence of Fourier series | `fourier-convergence-intro` | `uniform-convergence`, `integral-properties-proofs` |
| Testing uniform convergence with suprema | `uniform-convergence-suprema` | `uniform-convergence` |
| Working with series of functions | `series-of-functions` | `uniform-convergence`, `series-convergence-formal` |
| Using the Weierstrass M-test | `uniform-cauchy-mtest` | `comparison-proofs`, `uniform-convergence-suprema`, `series-of-functions` |
| Proving properties of power series | `power-series-analysis` | `uniform-cauchy-mtest`, `ratio-root-proofs` |
| Defining exponential and log functions rigorously | `exp-log-rigorous` | `power-series-analysis`, `ftc-proofs` |
| Exploring a nowhere differentiable function | `nowhere-differentiable-example` | `uniform-cauchy-mtest` |
| Proving power series can be differentiated | `power-series-differentiation` | `power-series-analysis`, `uniform-limit-derivative` |
| Proving Taylor series converge | `taylor-series-convergence` | `taylor-theorem-analysis`, `power-series-differentiation` |
| Using Abel's theorem | `abel-theorem-series` | `power-series-analysis` |
| Exploring a smooth non-analytic function | `smooth-non-analytic` | `taylor-series-convergence` |
| Defining sine and cosine with series | `trig-from-series` | `power-series-analysis` |

### Metric spaces

| Topic | Slug | Needs |
|---|---|---|
| Defining metric spaces | `metric-space-definition` | `triangle-inequality` |
| Using norms on real n-space | `norms-on-rn` | `metric-space-definition` |
| Working with examples of metrics | `examples-of-metrics` | `norms-on-rn` |
| Using open and closed sets in a metric space | `open-balls-metric` | `open-closed-sets`, `examples-of-metrics` |
| Finding closures in metric spaces | `closure-in-metric` | `open-balls-metric` |
| Using sequences in metric spaces | `sequences-in-metric` | `sequence-limit-definition`, `closure-in-metric` |
| Using complete metric spaces | `complete-metric-spaces` | `sequences-in-metric`, `completeness-from-cauchy` |
| Using compactness in metric spaces | `compactness-metric` | `sequences-in-metric`, `compact-sets-covers` |
| Using continuity between metric spaces | `continuity-metric` | `sequences-in-metric`, `continuity-definition-analysis` |
| Using the contraction mapping theorem | `contraction-mapping` | `complete-metric-spaces`, `lipschitz-functions` |
| Using the sup norm on function spaces | `function-spaces-sup-norm` | `complete-metric-spaces`, `uniform-convergence` |
| Proving real n-space is complete | `rn-complete` | `complete-metric-spaces` |
| Characterizing continuity with open sets | `continuity-open-sets` | `continuity-metric` |
| Proving extreme values on compact metric spaces | `extreme-values-metric` | `compactness-metric`, `continuity-metric` |
| Applying contraction to integral equations | `contraction-integral-equation` | `contraction-mapping`, `function-spaces-sup-norm` |

## math.abstract: 136 topics, budget 160 (-15%)

### Foundations

| Topic | Slug | Needs |
|---|---|---|
| Reviewing integer divisibility for algebra | `integers-review-gcd` | `proofs.gcd-proofs` |
| Using modular arithmetic for algebra | `modular-arithmetic-algebra` | `integers-review-gcd`, `proofs.congruence-mod-n` |
| Treating permutations as functions | `permutations-as-functions` | `proofs.bijection-proofs` |
| Finding symmetries of polygons | `symmetries-of-polygons` | `geom.symmetries-of-shapes`, `permutations-as-functions` |
| Working with binary operations | `binary-operations` | `proofs.functions-as-relations` |
| Testing associativity and identities | `binary-op-properties` | `binary-operations` |
| Reading operation tables | `operation-tables` | `binary-operations` |
| Composing permutations | `composing-permutations` | `permutations-as-functions` |
| Using cycle notation | `cycle-notation` | `composing-permutations` |
| Finding the order of a permutation from cycles | `permutation-order-cycles` | `cycle-notation`, `order-of-element` |
| Working with units mod n | `units-mod-n` | `modular-arithmetic-algebra`, `group-definition` |

### Groups

| Topic | Slug | Needs |
|---|---|---|
| Defining groups | `group-definition` | `proofs.group-axiom-proofs`, `binary-op-properties`, `operation-tables` |
| Working with examples of groups | `group-examples` | `symmetries-of-polygons`, `units-mod-n` |
| Working with symmetric groups | `permutation-groups` | `permutation-order-cycles` |
| Working with dihedral groups | `dihedral-groups` | `group-examples` |
| Working with matrix groups | `matrix-groups` | `group-examples`, `linalg.invertible-matrices` |
| Showing a set is not a group | `non-group-examples` | `group-definition` |
| Proving cancellation and inverse laws | `cancellation-inverses` | `group-definition` |
| Proving elementary group facts | `elementary-group-proofs` | `non-group-examples`, `cancellation-inverses` |
| Testing subgroups | `subgroups` | `elementary-group-proofs` |
| Using the one-step subgroup test | `subgroup-tests-one-step` | `subgroups` |
| Finding centers and centralizers | `center-centralizer` | `subgroups` |
| Finding cosets | `cosets` | `subgroups`, `proofs.equivalence-classes` |
| Working with homomorphisms | `homomorphisms` | `subgroups` |
| Working with group actions | `group-actions` | `permutation-groups`, `homomorphisms`, `dihedral-groups` |
| Using powers of elements | `powers-of-elements` | `elementary-group-proofs` |
| Finding the order of an element | `order-of-element` | `group-examples`, `powers-of-elements` |
| Using the finite subgroup test | `finite-subgroup-test` | `subgroup-tests-one-step` |
| Finding the subgroup generated by a set | `subgroup-generated` | `subgroups` |
| Working with cyclic groups | `cyclic-groups` | `order-of-element`, `subgroup-generated` |
| Finding orders of powers | `order-of-powers` | `cyclic-groups` |
| Finding generators | `generators` | `order-of-powers` |
| Finding subgroups of cyclic groups | `subgroups-of-cyclic` | `generators` |
| Proving a group is abelian | `abelian-proofs` | `center-centralizer` |
| Writing permutations as transpositions | `products-of-transpositions` | `permutation-groups` |
| Telling even from odd permutations | `even-odd-permutations` | `products-of-transpositions` |
| Working with alternating groups | `alternating-groups` | `even-odd-permutations`, `subgroups` |
| Drawing subgroup lattices | `subgroup-lattice` | `subgroups-of-cyclic` |
| Working with conjugation | `conjugation` | `subgroups` |
| Finding conjugacy classes | `conjugacy-classes` | `conjugation` |
| Comparing left and right cosets | `left-right-cosets` | `cosets` |
| Proving properties of cosets | `coset-properties` | `cosets` |
| Using Lagrange's theorem | `lagrange-theorem` | `proofs.partition-theorem`, `coset-properties` |
| Using consequences of Lagrange's theorem | `consequences-of-lagrange` | `lagrange-theorem`, `order-of-element` |
| Proving Fermat's and Euler's theorems with groups | `euler-fermat-group` | `consequences-of-lagrange` |
| Classifying groups of prime order | `prime-order-groups` | `consequences-of-lagrange`, `cyclic-groups` |
| Proving properties of homomorphisms | `homomorphism-properties` | `homomorphisms` |
| Finding kernels and images | `kernels-and-images` | `homomorphism-properties` |
| Proving groups isomorphic | `isomorphisms` | `kernels-and-images`, `proofs.bijection-proofs` |
| Working with automorphisms | `automorphisms` | `isomorphisms` |
| Using Cayley's theorem | `cayley-theorem` | `isomorphisms`, `permutation-groups` |
| Testing normal subgroups | `normal-subgroups` | `kernels-and-images`, `left-right-cosets` |
| Working with quotient groups | `quotient-groups` | `normal-subgroups`, `proofs.well-defined-functions` |
| Classifying cyclic groups | `cyclic-classification` | `isomorphisms`, `cyclic-groups` |
| Working with direct products | `direct-products` | `cyclic-classification` |
| Counting homomorphisms between cyclic groups | `counting-homomorphisms` | `kernels-and-images`, `cyclic-groups` |
| Using isomorphism invariants | `isomorphism-invariants` | `isomorphisms` |
| Proving groups are not isomorphic | `non-isomorphism-proofs` | `order-of-element`, `isomorphism-invariants` |
| Finding inner automorphisms | `inner-automorphisms` | `automorphisms`, `conjugation` |
| Finding the structure of quotient groups | `quotient-structure` | `quotient-groups` |
| Using the first isomorphism theorem | `first-isomorphism` | `isomorphisms`, `quotient-structure` |
| Using the second and third isomorphism theorems | `second-third-isomorphism` | `first-isomorphism` |
| Using the correspondence theorem | `correspondence-theorem` | `first-isomorphism` |
| Proving index-two subgroups are normal | `index-two-normal` | `normal-subgroups` |
| Using the commutator subgroup | `commutator-subgroup` | `quotient-groups` |
| Recognizing internal direct products | `internal-direct-products` | `direct-products`, `normal-subgroups` |
| Finding orders in direct products | `orders-in-direct-products` | `direct-products` |
| Testing when a product is cyclic | `product-cyclic-test` | `orders-in-direct-products` |
| Classifying finite abelian groups | `finite-abelian-groups` | `subgroups-of-cyclic`, `internal-direct-products`, `product-cyclic-test` |
| Finding orbits and stabilizers | `orbits-stabilizers-examples` | `group-actions` |
| Using the orbit-stabilizer theorem | `orbit-stabilizer` | `lagrange-theorem`, `orbits-stabilizers-examples` |
| Counting with Burnside's lemma | `burnside-counting` | `orbit-stabilizer` |
| Using the class equation | `class-equation` | `orbit-stabilizer`, `center-centralizer`, `conjugacy-classes` |
| Using Cauchy's theorem | `cauchy-theorem-groups` | `class-equation` |
| Using the Sylow theorems | `sylow-theorems` | `cauchy-theorem-groups`, `quotient-groups` |
| Counting Sylow subgroups | `counting-sylow-subgroups` | `sylow-theorems` |
| Classifying small groups with Sylow theorems | `sylow-applications` | `counting-sylow-subgroups`, `non-isomorphism-proofs` |
| Working with simple groups | `simple-groups` | `sylow-applications`, `alternating-groups` |
| Introducing solvable groups | `solvable-groups-intro` | `correspondence-theorem`, `simple-groups`, `commutator-subgroup` |
| Classifying groups of order pq | `groups-of-order-pq` | `sylow-applications` |
| Exploring semidirect products | `semidirect-intro` | `internal-direct-products`, `automorphisms` |

### Rings

| Topic | Slug | Needs |
|---|---|---|
| Defining rings | `ring-definition` | `group-definition` |
| Proving basic ring facts | `basic-ring-proofs` | `ring-definition` |
| Working with examples of rings | `ring-examples` | `modular-arithmetic-algebra`, `linalg.matrix-algebra-rules`, `basic-ring-proofs` |
| Testing subrings | `subrings` | `ring-examples` |
| Finding the characteristic of a ring | `characteristic-of-ring` | `ring-examples`, `order-of-element` |
| Testing ideals | `ideals` | `subrings` |
| Working with quotient rings | `quotient-rings` | `ideals`, `quotient-groups` |
| Working with ring homomorphisms | `ring-homomorphisms` | `ideals`, `homomorphisms` |
| Working with polynomial rings | `polynomial-rings` | `ring-examples`, `alg2.polynomial-long-division` |
| Working with rings of integers mod n | `integers-mod-n-rings` | `ring-examples` |
| Finding units and zero divisors | `units-zero-divisors` | `integers-mod-n-rings` |
| Working with integral domains | `integral-domains` | `units-zero-divisors` |
| Defining fields | `fields-definition` | `integral-domains` |
| Building a field of fractions | `field-of-fractions` | `integral-domains`, `proofs.well-defined-functions` |
| Finding idempotents and nilpotents | `idempotents-nilpotents` | `units-zero-divisors` |
| Proving finite integral domains are fields | `finite-domain-field` | `fields-definition` |
| Finding ideals generated by elements | `ideal-generated` | `ideals` |
| Using sums and products of ideals | `ideal-operations` | `ideals` |
| Finding the structure of quotient rings | `quotient-ring-structure` | `quotient-rings` |
| Using prime and maximal ideals | `prime-maximal-ideals` | `fields-definition`, `quotient-ring-structure` |
| Proving kernels are ideals | `kernels-are-ideals` | `ring-homomorphisms` |
| Using the first isomorphism theorem for rings | `first-isomorphism-rings` | `quotient-rings`, `kernels-are-ideals` |
| Using the Chinese remainder theorem for rings | `chinese-remainder-rings` | `first-isomorphism-rings`, `ideal-operations` |
| Using degree in polynomial rings | `polynomial-degree` | `polynomial-rings` |
| Using the division algorithm for polynomials | `division-algorithm-polynomials` | `fields-definition`, `polynomial-degree` |
| Finding greatest common divisors of polynomials | `gcd-polynomials` | `division-algorithm-polynomials` |
| Using roots and the factor theorem in rings | `roots-factor-theorem-rings` | `division-algorithm-polynomials` |
| Working with principal ideal domains | `principal-ideal-domains` | `prime-maximal-ideals`, `gcd-polynomials`, `ideal-generated` |
| Working with Euclidean domains | `euclidean-domains` | `principal-ideal-domains` |
| Working with Gaussian integers | `gaussian-integers` | `euclidean-domains` |
| Working with polynomials mod p | `polynomials-mod-p` | `polynomial-rings` |
| Testing irreducible polynomials | `irreducible-polynomials` | `roots-factor-theorem-rings`, `polynomials-mod-p` |
| Testing reducibility by reducing mod p | `reducibility-mod-p` | `polynomials-mod-p` |
| Using Eisenstein's criterion and Gauss's lemma | `eisenstein-gauss` | `irreducible-polynomials`, `reducibility-mod-p`, `field-of-fractions` |
| Finding associates | `associates-in-domains` | `integral-domains` |
| Telling irreducible from prime elements | `irreducibles-and-primes` | `proofs.prime-proofs`, `associates-in-domains` |
| Working with unique factorization domains | `unique-factorization-domains` | `principal-ideal-domains`, `irreducibles-and-primes` |
| Building fields with quotient polynomial rings | `fields-from-quotients` | `irreducible-polynomials`, `prime-maximal-ideals` |
| Exploring a domain without unique factorization | `non-ufd-example` | `unique-factorization-domains` |
| Finding sums of two squares | `sums-of-two-squares` | `gaussian-integers` |

### Fields

| Topic | Slug | Needs |
|---|---|---|
| Working with field extensions | `field-extensions` | `fields-from-quotients` |
| Finding the degree of an extension | `degree-of-extension` | `field-extensions`, `linalg.basis-definition` |
| Working with simple extensions | `simple-extensions` | `field-extensions` |
| Working with algebraic elements | `algebraic-elements` | `degree-of-extension`, `simple-extensions` |
| Finding minimal polynomials | `minimal-polynomials` | `algebraic-elements` |
| Finding splitting fields | `splitting-fields` | `minimal-polynomials` |
| Introducing Galois theory | `galois-intro` | `splitting-fields`, `solvable-groups-intro` |
| Using the tower law | `tower-law` | `degree-of-extension` |
| Proving impossibility of classic constructions | `constructibility` | `geom.construct-polygons-in-circle`, `tower-law` |
| Testing repeated roots with the derivative | `repeated-roots-derivative` | `polynomial-rings` |
| Working with finite fields | `finite-fields` | `splitting-fields`, `characteristic-of-ring`, `repeated-roots-derivative` |
| Applying fields to coding theory | `coding-theory-application` | `finite-fields` |
| Finding small Galois groups | `small-galois-groups` | `galois-intro` |
| Stating the fundamental theorem of Galois theory | `galois-correspondence-statement` | `small-galois-groups` |
| Stating why the quintic is unsolvable | `quintic-unsolvable` | `galois-correspondence-statement` |

## math.numerical: 116 topics, budget 130 (-11%)

### Foundations

| Topic | Slug | Needs |
|---|---|---|
| Writing numbers in binary | `binary-representation` | `alg2.exponent-laws-rational` |
| Understanding floating-point numbers | `floating-point` | `binary-representation` |
| Finding machine epsilon | `machine-epsilon` | `floating-point` |
| Finding absolute and relative error | `absolute-relative-error` | `machine-epsilon` |
| Avoiding rounding and cancellation | `rounding-and-cancellation` | `absolute-relative-error` |
| Using Taylor's theorem for error analysis | `taylor-for-error` | `absolute-relative-error`, `calc2.taylor-remainder` |
| Finding order of convergence | `order-of-convergence` | `taylor-for-error` |
| Using big-O in numerical analysis | `big-o-numerical` | `taylor-for-error` |
| Counting operations in an algorithm | `algorithm-cost` | `big-o-numerical` |
| Rewriting formulas to avoid cancellation | `rewrite-to-avoid-cancellation` | `rounding-and-cancellation` |
| Propagating errors through a calculation | `error-propagation` | `absolute-relative-error`, `calc1.differentials` |
| Telling conditioning from stability | `conditioning-stability` | `rewrite-to-avoid-cancellation`, `error-propagation` |
| Spotting unstable recursions | `unstable-recurrences` | `conditioning-stability` |
| Estimating a convergence rate from data | `rate-from-data` | `order-of-convergence` |

### Root finding

| Topic | Slug | Needs |
|---|---|---|
| Using the bisection method | `bisection` | `absolute-relative-error`, `calc1.intermediate-value-applications` |
| Using Newton's method | `newton-method-numerical` | `calc1.newtons-method`, `order-of-convergence` |
| Using the secant method | `secant-method` | `newton-method-numerical` |
| Using Horner's method | `polynomial-roots-horner` | `algorithm-cost` |
| Using Newton's method for nonlinear systems | `systems-nonlinear-newton` | `newton-method-numerical`, `calc3.linearization-multivariable`, `gaussian-elimination-numerical` |
| Bounding bisection error | `bisection-error-bound` | `bisection` |
| Choosing stopping criteria | `stopping-criteria` | `bisection` |
| Combining root-finding methods | `hybrid-methods` | `secant-method`, `bisection-error-bound`, `stopping-criteria` |
| Rewriting an equation as a fixed-point problem | `fixed-point-rewriting` | `absolute-relative-error` |
| Using fixed-point iteration | `fixed-point-iteration` | `taylor-for-error`, `fixed-point-rewriting` |
| Proving fixed-point convergence | `fixed-point-convergence` | `fixed-point-iteration` |
| Finding where Newton's method fails | `newton-failure-cases` | `newton-method-numerical` |
| Analyzing Newton's method convergence | `newton-convergence` | `newton-failure-cases` |
| Handling multiple roots | `multiple-roots` | `newton-convergence` |
| Using Aitken acceleration | `aitken-acceleration` | `fixed-point-convergence`, `order-of-convergence` |
| Deflating a polynomial | `polynomial-deflation` | `polynomial-roots-horner` |

### Linear systems

| Topic | Slug | Needs |
|---|---|---|
| Using vector and matrix norms | `vector-matrix-norms` | `linalg.length-angle-orthogonal` |
| Finding condition numbers | `condition-number` | `vector-matrix-norms`, `conditioning-stability` |
| Bounding errors with residuals | `residuals-error-bounds` | `condition-number` |
| Using Jacobi iteration | `jacobi-method` | `vector-matrix-norms` |
| Using Gauss-Seidel iteration | `gauss-seidel` | `jacobi-method` |
| Using successive over-relaxation | `sor` | `gauss-seidel` |
| Solving triangular systems | `triangular-solves` | `linalg.gaussian-elimination` |
| Using Gaussian elimination numerically | `gaussian-elimination-numerical` | `algorithm-cost`, `triangular-solves` |
| Counting the cost of elimination | `elimination-cost` | `gaussian-elimination-numerical` |
| Seeing failure without pivoting | `failure-without-pivoting` | `gaussian-elimination-numerical`, `rounding-and-cancellation` |
| Using partial pivoting | `pivoting` | `failure-without-pivoting` |
| Using scaled pivoting | `scaled-pivoting` | `pivoting` |
| Using LU factorization numerically | `lu-numerical` | `elimination-cost`, `scaled-pivoting`, `linalg.solve-with-lu` |
| Using Cholesky factorization | `cholesky` | `lu-numerical`, `linalg.positive-definite` |
| Solving tridiagonal systems | `tridiagonal-systems` | `lu-numerical` |
| Solving without forming an inverse | `avoid-forming-inverse` | `lu-numerical` |
| Testing diagonal dominance | `diagonal-dominance` | `vector-matrix-norms` |
| Using the spectral radius | `spectral-radius` | `vector-matrix-norms`, `linalg.find-eigenvalues` |
| Proving convergence of iterative methods | `iterative-convergence` | `gauss-seidel`, `diagonal-dominance`, `spectral-radius` |
| Exploiting sparse matrices | `sparse-matrices` | `tridiagonal-systems` |
| Using the conjugate gradient method | `conjugate-gradient` | `iterative-convergence`, `linalg.positive-definite`, `sparse-matrices` |
| Using iterative refinement | `iterative-refinement` | `lu-numerical`, `residuals-error-bounds` |
| Exploring preconditioning | `preconditioning-intro` | `conjugate-gradient` |

### Least squares and eigenvalues

| Topic | Slug | Needs |
|---|---|---|
| Solving least squares numerically | `least-squares-numerical` | `linalg.least-squares-qr`, `condition-number` |
| Seeing why normal equations lose accuracy | `normal-equation-accuracy` | `least-squares-numerical` |
| Using Householder QR | `qr-householder` | `normal-equation-accuracy` |
| Using Givens rotations | `givens-rotations` | `qr-householder` |
| Using Gershgorin's theorem | `gershgorin` | `linalg.find-eigenvalues` |
| Using the power method | `power-method` | `linalg.find-eigenvectors`, `order-of-convergence`, `gershgorin` |
| Using inverse power iteration | `inverse-power-method` | `power-method`, `lu-numerical` |
| Introducing the QR algorithm | `qr-algorithm-intro` | `qr-householder`, `power-method` |
| Using Rayleigh quotient iteration | `rayleigh-quotient-iteration` | `inverse-power-method` |
| Using shifts in the QR algorithm | `qr-with-shifts` | `qr-algorithm-intro` |
| Using the SVD numerically | `svd-numerical` | `linalg.svd-compute`, `qr-with-shifts` |
| Handling rank-deficient least squares | `rank-deficient-least-squares` | `svd-numerical` |

### Interpolation

| Topic | Slug | Needs |
|---|---|---|
| Using polynomial interpolation | `polynomial-interpolation` | `alg2.write-polynomial-from-zeros`, `big-o-numerical` |
| Using Newton's divided differences | `newton-divided-differences` | `polynomial-interpolation` |
| Using Hermite interpolation | `hermite-interpolation` | `newton-divided-differences` |
| Approximating functions by least squares | `approximation-least-squares-functions` | `least-squares-numerical`, `polynomial-interpolation` |
| Using the Vandermonde system | `vandermonde` | `polynomial-interpolation` |
| Proving uniqueness of the interpolating polynomial | `interpolant-uniqueness` | `polynomial-interpolation` |
| Using the Lagrange form | `lagrange-form` | `vandermonde`, `interpolant-uniqueness` |
| Bounding interpolation error | `interpolation-error` | `lagrange-form` |
| Using piecewise linear interpolation | `piecewise-linear-interp` | `interpolation-error` |
| Using cubic splines | `cubic-splines` | `piecewise-linear-interp`, `tridiagonal-systems`, `hermite-interpolation` |
| Using Chebyshev polynomials | `chebyshev-polynomials` | `interpolation-error` |
| Avoiding Runge's phenomenon with Chebyshev nodes | `runge-chebyshev` | `chebyshev-polynomials` |
| Comparing natural and clamped splines | `natural-clamped-splines` | `cubic-splines` |
| Using trigonometric interpolation | `trig-interpolation` | `polynomial-interpolation` |
| Introducing the fast Fourier transform | `fft-intro` | `algorithm-cost`, `trig-interpolation` |

### Differentiation and integration

| Topic | Slug | Needs |
|---|---|---|
| Using finite differences | `finite-differences` | `taylor-for-error` |
| Using Newton-Cotes rules | `newton-cotes` | `lagrange-form`, `calc2.numerical-trapezoid-simpson` |
| Using composite rules and their errors | `composite-rules-error` | `newton-cotes`, `interpolation-error`, `calc2.numerical-error-bounds` |
| Using adaptive quadrature | `adaptive-quadrature` | `composite-rules-error` |
| Handling singular integrals numerically | `improper-numerical` | `composite-rules-error` |
| Estimating multiple integrals | `multiple-integrals-numerical` | `composite-rules-error`, `calc3.iterated-rectangles` |
| Using Monte Carlo integration | `monte-carlo` | `composite-rules-error` |
| Analyzing central difference error | `central-difference-error` | `finite-differences` |
| Choosing a step size | `step-size-tradeoff` | `finite-differences`, `rounding-and-cancellation` |
| Using Richardson extrapolation | `richardson-extrapolation` | `central-difference-error`, `step-size-tradeoff` |
| Using Romberg integration | `romberg` | `composite-rules-error`, `richardson-extrapolation` |
| Using differences for second derivatives | `second-derivative-difference` | `finite-differences` |
| Finding degree of precision | `degree-of-precision` | `newton-cotes` |
| Using orthogonal polynomials | `orthogonal-polynomials` | `approximation-least-squares-functions` |
| Using Gaussian quadrature | `gaussian-quadrature` | `degree-of-precision`, `orthogonal-polynomials` |

### Differential equations

| Topic | Slug | Needs |
|---|---|---|
| Using Euler's method numerically | `euler-numerical` | `finite-differences`, `calc2.eulers-method-intro` |
| Telling local from global error | `local-global-error` | `euler-numerical`, `order-of-convergence` |
| Handling stability and stiffness | `stability-stiff` | `local-global-error`, `conditioning-stability` |
| Using finite differences for boundary problems | `boundary-finite-difference` | `tridiagonal-systems`, `second-derivative-difference` |
| Introducing finite differences for PDEs | `pde-finite-difference-intro` | `boundary-finite-difference`, `stability-stiff` |
| Using gradient descent | `optimization-gradient-descent` | `calc3.gradient-direction`, `order-of-convergence` |
| Using Taylor methods | `taylor-methods` | `euler-numerical` |
| Using midpoint and Heun's methods | `midpoint-heun` | `local-global-error` |
| Using Runge-Kutta methods | `runge-kutta` | `taylor-methods`, `midpoint-heun` |
| Solving systems and higher-order equations | `systems-higher-order-ode` | `runge-kutta` |
| Using the shooting method | `boundary-shooting` | `systems-higher-order-ode`, `secant-method` |
| Using consistency and convergence | `consistency-convergence-ode` | `local-global-error` |
| Using multistep methods | `multistep-methods` | `runge-kutta`, `lagrange-form`, `consistency-convergence-ode` |
| Using adaptive step sizes | `adaptive-step-size` | `runge-kutta` |
| Using predictor-corrector methods | `predictor-corrector` | `multistep-methods` |
| Finding regions of absolute stability | `absolute-stability-regions` | `stability-stiff` |
| Using implicit methods | `implicit-methods` | `newton-method-numerical`, `absolute-stability-regions` |
| Using Newton's method for optimization | `newton-for-optimization` | `optimization-gradient-descent`, `systems-nonlinear-newton` |
| Solving PDEs with explicit finite differences | `numerical-pde-explicit` | `pde-finite-difference-intro` |
| Using von Neumann stability | `numerical-stability-von-neumann` | `numerical-pde-explicit` |
| Using an implicit method for the heat equation | `crank-nicolson` | `numerical-pde-explicit`, `implicit-methods` |

## math.pde: 115 topics, budget 140 (-18%)

### Foundations

| Topic | Slug | Needs |
|---|---|---|
| Classifying partial differential equations | `pde-classification` | `calc3.partial-differential-equation-check` |
| Finding order and linearity | `order-linearity-pde` | `pde-classification` |
| Deriving the wave equation | `deriving-wave-equation` | `pde-classification`, `diffeq.free-oscillation` |
| Solving the transport equation | `transport-equation` | `pde-classification`, `calc3.chain-rule-multivariable` |
| Using the method of characteristics | `characteristics-first-order` | `transport-equation` |
| Checking solutions of PDEs | `pde-check-solutions` | `calc3.partial-differential-equation-check` |
| Using superposition for PDEs | `linear-operators-superposition-pde` | `order-linearity-pde`, `diffeq.linear-operator-superposition`, `pde-check-solutions` |
| Telling Dirichlet, Neumann and Robin conditions apart | `boundary-types` | `pde-classification` |
| Using boundary and initial conditions | `boundary-initial-conditions` | `diffeq.initial-boundary-values`, `boundary-types` |
| Understanding well-posed problems | `well-posed-problems` | `boundary-initial-conditions` |
| Classifying second-order equations | `classify-second-order` | `pde-classification` |
| Reducing second-order equations to canonical form | `canonical-forms` | `characteristics-first-order`, `classify-second-order`, `calc3.second-order-chain-rule` |
| Deriving conservation laws | `conservation-laws` | `calc3.divergence-theorem`, `pde-classification` |
| Deriving the heat equation | `deriving-heat-equation` | `conservation-laws` |
| Deriving Laplace's equation | `deriving-laplace-equation` | `deriving-heat-equation` |
| Solving the eigenvalue problem on an interval | `ode-eigen-recap` | `diffeq.boundary-value-eigenproblems` |
| Separating variables in a PDE | `separation-idea` | `linear-operators-superposition-pde`, `diffeq.separation-of-variables-preview`, `ode-eigen-recap` |
| Solving forced first-order equations | `forced-first-order` | `characteristics-first-order` |
| Using characteristics with variable coefficients | `nonconstant-characteristics` | `forced-first-order` |
| Solving with data on a curve | `characteristics-initial-curve` | `nonconstant-characteristics` |
| Exploring Burgers' equation and shocks | `nonlinear-burgers-intro` | `characteristics-initial-curve` |
| Modelling traffic flow | `traffic-flow-model` | `nonlinear-burgers-intro` |
| Finding shock speeds | `shock-speed` | `nonlinear-burgers-intro` |

### Fourier series

| Topic | Slug | Needs |
|---|---|---|
| Using orthogonality of trig functions | `periodic-functions-orthogonality` | `diffeq.fourier-series-intro`, `linalg.function-space-projection` |
| Finding Fourier coefficients | `fourier-coefficients` | `periodic-functions-orthogonality` |
| Using Parseval's identity | `parseval` | `fourier-coefficients` |
| Using complex Fourier series | `complex-fourier` | `fourier-coefficients` |
| Finding Fourier series of piecewise functions | `fourier-piecewise` | `fourier-coefficients` |
| Using periodic extensions | `fourier-periodic-extensions` | `fourier-piecewise` |
| Using the Fourier convergence theorem | `convergence-of-fourier` | `fourier-periodic-extensions`, `diffeq.fourier-convergence-statement` |
| Recognizing the Gibbs phenomenon | `gibbs-phenomenon` | `convergence-of-fourier` |
| Differentiating Fourier series | `differentiating-fourier` | `convergence-of-fourier` |
| Finding series on a general interval | `general-period` | `fourier-coefficients` |
| Building even and odd extensions | `even-odd-extension` | `fourier-periodic-extensions` |
| Finding sine and cosine series | `sine-cosine-series` | `diffeq.fourier-even-odd`, `general-period`, `even-odd-extension` |
| Using mean-square convergence | `mean-square-convergence` | `convergence-of-fourier`, `parseval` |
| Integrating Fourier series | `integrating-fourier` | `convergence-of-fourier` |
| Evaluating number series with Fourier series | `number-series-from-fourier` | `parseval` |
| Testing uniform convergence of Fourier series | `uniform-fourier-convergence` | `convergence-of-fourier` |

### Sturm-Liouville

| Topic | Slug | Needs |
|---|---|---|
| Writing Sturm-Liouville problems | `sturm-liouville-form` | `diffeq.boundary-value-eigenproblems` |
| Finding Sturm-Liouville eigenvalues | `sl-eigenvalues` | `sturm-liouville-form` |
| Using Bessel eigenfunctions | `bessel-eigenfunctions` | `sl-eigenvalues`, `diffeq.bessel-intro` |
| Using Legendre eigenfunctions | `legendre-eigenfunctions` | `sl-eigenvalues`, `diffeq.airy-legendre-examples` |
| Using self-adjoint operators | `self-adjoint-operators` | `sturm-liouville-form`, `linalg.inner-product-spaces` |
| Proving orthogonality of eigenfunctions | `sl-orthogonality` | `sl-eigenvalues`, `periodic-functions-orthogonality`, `self-adjoint-operators` |
| Using the Rayleigh quotient | `rayleigh-quotient` | `sl-orthogonality` |
| Using weight functions | `weight-function-orthogonality` | `sl-orthogonality` |
| Using eigenfunction expansions | `eigenfunction-expansions` | `fourier-coefficients`, `weight-function-orthogonality` |
| Proving eigenvalues are real | `sl-real-eigenvalues` | `self-adjoint-operators` |
| Solving periodic eigenvalue problems | `periodic-sl` | `sl-eigenvalues` |
| Expanding with Bessel functions | `bessel-expansions` | `bessel-eigenfunctions`, `eigenfunction-expansions` |
| Expanding with Legendre polynomials | `legendre-expansions` | `legendre-eigenfunctions`, `eigenfunction-expansions` |

### Heat equation

| Topic | Slug | Needs |
|---|---|---|
| Solving the heat equation with Dirichlet conditions | `heat-separation-dirichlet` | `sine-cosine-series`, `boundary-initial-conditions`, `deriving-heat-equation`, `separation-idea` |
| Using the maximum principle for heat | `maximum-principle-heat` | `heat-separation-dirichlet`, `well-posed-problems` |
| Using energy methods for uniqueness | `energy-methods` | `well-posed-problems`, `calc3.divergence-theorem` |
| Solving heat in a rectangle | `heat-2d-rectangle` | `heat-separation-dirichlet` |
| Matching initial data with a sine series | `heat-initial-fit` | `heat-separation-dirichlet` |
| Solving the heat equation with Neumann conditions | `heat-neumann` | `heat-initial-fit` |
| Solving with mixed and Robin conditions | `heat-mixed-robin` | `heat-neumann`, `sl-eigenvalues` |
| Reading long-time behaviour of heat solutions | `heat-long-term` | `heat-separation-dirichlet` |
| Handling steady boundary conditions | `heat-nonhomogeneous-bc` | `heat-long-term` |
| Solving the heat equation with sources | `heat-source-terms` | `heat-nonhomogeneous-bc`, `eigenfunction-expansions` |
| Proving uniqueness for the heat equation | `heat-uniqueness` | `maximum-principle-heat`, `energy-methods` |
| Solving heat on a ring | `heat-on-a-ring` | `heat-separation-dirichlet`, `periodic-sl` |
| Handling time-dependent boundary conditions | `heat-time-dependent-bc` | `heat-source-terms` |
| Solving heat in a box | `heat-3d-box` | `heat-2d-rectangle` |
| Using Duhamel's principle | `duhamel` | `heat-source-terms` |

### Wave equation

| Topic | Slug | Needs |
|---|---|---|
| Solving the wave equation by separation | `wave-separation` | `sine-cosine-series`, `deriving-wave-equation`, `separation-idea` |
| Using d'Alembert's solution | `dalembert` | `canonical-forms`, `deriving-wave-equation` |
| Using the method of reflections | `reflection-method` | `dalembert` |
| Solving forced wave equations | `wave-nonhomogeneous` | `wave-separation`, `eigenfunction-expansions` |
| Using conservation of energy for waves | `wave-energy` | `wave-separation`, `energy-methods` |
| Solving a vibrating rectangular membrane | `membrane-vibration` | `wave-separation` |
| Solving a plucked string | `plucked-string` | `wave-separation` |
| Reading modes of a vibrating string | `modes-of-string` | `plucked-string` |
| Solving a damped wave equation | `damped-wave` | `wave-separation` |
| Using d'Alembert's formula with initial velocity | `dalembert-initial-velocity` | `dalembert` |
| Finding domains of dependence | `domain-of-dependence` | `dalembert-initial-velocity` |
| Using Duhamel's formula for waves | `wave-duhamel` | `dalembert`, `duhamel` |
| Solving a semi-infinite string | `semi-infinite-string` | `reflection-method` |
| Finding nodal lines of a membrane | `nodal-lines` | `membrane-vibration` |
| Solving a vibrating circular membrane | `circular-membrane` | `polar-separation`, `bessel-expansions`, `nodal-lines` |

### Laplace equation

| Topic | Slug | Needs |
|---|---|---|
| Solving Laplace's equation in a rectangle | `laplace-rectangle` | `sine-cosine-series`, `deriving-laplace-equation`, `separation-idea` |
| Using harmonic functions | `harmonic-functions` | `deriving-laplace-equation` |
| Using mean value and maximum principles | `mean-value-maximum-laplace` | `harmonic-functions` |
| Solving Laplace's equation in a disk | `polar-separation` | `laplace-rectangle` |
| Using the Poisson kernel | `poisson-kernel` | `polar-separation` |
| Solving Laplace's equation in a sphere | `spherical-laplace` | `polar-separation`, `legendre-expansions` |
| Solving Laplace's equation in a cylinder | `cylindrical-laplace` | `polar-separation`, `bessel-expansions` |
| Using Green's identities | `greens-identities` | `harmonic-functions` |
| Superposing solutions for nonzero sides | `laplace-nonzero-sides` | `laplace-rectangle` |
| Solving Poisson's equation | `poisson-equation` | `eigenfunction-expansions`, `laplace-nonzero-sides` |
| Checking compatibility for Neumann problems | `neumann-compatibility` | `laplace-rectangle` |
| Solving in an annulus or wedge | `laplace-annulus-wedge` | `polar-separation` |
| Solving outside a disk | `laplace-exterior` | `polar-separation` |
| Proving uniqueness for Laplace's equation | `uniqueness-laplace` | `mean-value-maximum-laplace` |
| Finding one-dimensional Green's functions | `greens-one-dimension` | `diffeq.impulse-delta`, `diffeq.initial-boundary-values` |
| Finding free-space Green's functions | `greens-free-space` | `greens-identities`, `diffeq.impulse-delta` |
| Using Green's functions | `greens-functions` | `greens-one-dimension`, `greens-free-space`, `poisson-equation` |
| Using the method of images | `method-of-images` | `greens-functions` |

### Transforms

| Topic | Slug | Needs |
|---|---|---|
| Defining the Fourier transform | `fourier-transform-definition` | `complex-fourier` |
| Using Laplace transforms on PDEs | `laplace-transform-pde` | `diffeq.solve-ivp-laplace`, `pde-classification` |
| Finding common transform pairs | `fourier-transform-pairs` | `fourier-transform-definition` |
| Using the inversion formula | `fourier-inversion` | `fourier-transform-definition` |
| Using Fourier transform properties | `fourier-transform-properties` | `fourier-transform-pairs`, `fourier-inversion` |
| Using the convolution theorem | `fourier-convolution` | `fourier-transform-properties`, `diffeq.convolution` |
| Solving the wave equation with transforms | `wave-with-fourier` | `fourier-transform-properties`, `dalembert` |
| Using sine and cosine transforms | `semi-infinite-sine-cosine` | `fourier-transform-properties` |
| Transforming derivatives | `transform-derivatives` | `fourier-transform-properties` |
| Solving heat on the whole line | `heat-on-the-line` | `fourier-convolution`, `transform-derivatives` |
| Using the delta function | `delta-function-pde` | `diffeq.impulse-delta`, `fourier-transform-definition` |
| Using the heat kernel | `heat-kernel` | `heat-on-the-line`, `delta-function-pde` |
| Solving Laplace's equation in a half plane | `laplace-half-plane` | `fourier-convolution` |
| Solving heat on a half line | `heat-half-line` | `semi-infinite-sine-cosine` |
| Solving heat on a half line with Laplace transforms | `heat-half-line-laplace` | `laplace-transform-pde`, `heat-on-the-line` |

## math.complex: 106 topics, budget 120 (-12%)

### Complex numbers

| Topic | Slug | Needs |
|---|---|---|
| Working with complex arithmetic | `complex-review` | `precalc.polar-form-complex` |
| Using conjugates and modulus | `conjugate-modulus` | `complex-review` |
| Using the geometry of complex numbers | `geometry-of-complex` | `conjugate-modulus` |
| Using the triangle inequality for complex numbers | `triangle-inequality-complex` | `conjugate-modulus` |
| Describing regions in the complex plane | `complex-plane-sets` | `geometry-of-complex`, `triangle-inequality-complex` |
| Using the Riemann sphere | `stereographic-sphere` | `complex-plane-sets` |
| Finding principal arguments | `principal-argument` | `complex-review` |
| Using polar and exponential form | `polar-exponential-form` | `precalc.de-moivre`, `principal-argument` |
| Finding roots of unity | `roots-of-unity` | `polar-exponential-form` |
| Deriving trig identities with de Moivre | `identities-from-de-moivre` | `polar-exponential-form` |
| Finding nth roots of a complex number | `nth-roots-complex` | `roots-of-unity` |
| Telling open sets, domains and regions | `domains-and-regions` | `complex-plane-sets` |

### Analytic functions

| Topic | Slug | Needs |
|---|---|---|
| Working with complex functions | `complex-functions` | `complex-plane-sets` |
| Finding complex limits and continuity | `complex-limits-continuity` | `complex-functions`, `calc3.multivariable-limits`, `domains-and-regions` |
| Splitting a function into real and imaginary parts | `real-imaginary-parts` | `complex-functions` |
| Picturing complex mappings | `complex-mappings` | `real-imaginary-parts` |
| Showing a complex limit does not exist | `complex-limit-nonexistence` | `complex-limits-continuity` |
| Defining the complex derivative | `complex-derivative` | `complex-limit-nonexistence` |
| Using the Cauchy-Riemann equations | `cauchy-riemann` | `complex-derivative`, `calc3.partial-derivatives-compute` |
| Using limits at the point at infinity | `limits-at-infinity-complex` | `complex-limits-continuity`, `stereographic-sphere` |
| Using complex differentiation rules | `complex-derivative-rules` | `complex-derivative` |
| Showing a function is nowhere differentiable | `nowhere-differentiable-complex` | `cauchy-riemann` |
| Working with analytic functions | `analytic-functions` | `complex-derivative-rules`, `nowhere-differentiable-complex` |
| Using the complex exponential | `complex-exponential` | `analytic-functions`, `polar-exponential-form` |
| Using complex trig and hyperbolic functions | `complex-trig-hyperbolic` | `complex-exponential`, `calc2.hyperbolic-definitions` |
| Using Cauchy-Riemann in polar form | `polar-cauchy-riemann` | `cauchy-riemann` |
| Recognizing entire functions | `entire-functions` | `analytic-functions` |
| Testing harmonic functions | `harmonic-test` | `analytic-functions`, `calc3.higher-partials` |
| Finding harmonic conjugates | `harmonic-conjugates` | `harmonic-test` |
| Proving conditions that force an analytic function to be constant | `constant-analytic` | `analytic-functions` |
| Using properties of the complex exponential | `complex-exp-properties` | `complex-exponential` |
| Using the complex logarithm | `complex-logarithm` | `polar-cauchy-riemann`, `complex-exp-properties` |
| Using branches and branch cuts | `branch-cuts` | `complex-logarithm` |
| Using complex powers | `complex-powers` | `complex-logarithm` |
| Solving equations with complex functions | `solve-complex-equations` | `complex-trig-hyperbolic`, `complex-logarithm` |
| Using complex inverse trig functions | `complex-inverse-trig` | `complex-logarithm`, `complex-trig-hyperbolic` |
| Finding images under the exponential | `images-under-exponential` | `complex-exponential`, `complex-mappings` |
| Finding images under powers | `images-under-powers` | `complex-mappings` |

### Integration

| Topic | Slug | Needs |
|---|---|---|
| Parametrizing contours | `contours` | `complex-functions`, `calc2.parametric-derivatives` |
| Integrating functions of a real variable | `integrate-real-variable` | `complex-functions`, `calc1.ftc-part-2` |
| Evaluating contour integrals | `contour-integrals` | `contours`, `calc3.line-integrals-vector`, `integrate-real-variable` |
| Using the ML inequality | `ml-inequality` | `contour-integrals` |
| Using complex antiderivatives | `antiderivatives-complex` | `contour-integrals`, `analytic-functions` |
| Integrating powers around a circle | `powers-around-a-circle` | `contour-integrals` |
| Seeing when an integral depends on the path | `path-dependence` | `antiderivatives-complex` |
| Using the Cauchy-Goursat theorem | `cauchy-goursat` | `calc3.greens-theorem-circulation`, `path-dependence` |
| Using Cauchy's theorem on multiply connected regions | `multiply-connected` | `cauchy-goursat` |
| Deforming contours | `deformation-of-contours` | `powers-around-a-circle`, `multiply-connected` |
| Using Cauchy's integral formula | `cauchy-integral-formula` | `deformation-of-contours` |
| Using Morera's theorem | `morera` | `cauchy-integral-formula` |
| Evaluating integrals with Cauchy's formula | `cauchy-formula-compute` | `cauchy-integral-formula` |
| Using the generalized Cauchy formula | `higher-derivative-formula` | `cauchy-formula-compute` |
| Using Cauchy's inequalities | `cauchy-inequalities` | `higher-derivative-formula`, `ml-inequality` |
| Using Liouville's theorem | `liouville` | `entire-functions`, `cauchy-inequalities` |
| Proving the fundamental theorem of algebra | `fundamental-theorem-algebra-proof` | `liouville` |
| Using the Gauss mean value theorem | `gauss-mean-value` | `cauchy-integral-formula` |
| Using the maximum modulus principle | `maximum-modulus` | `gauss-mean-value` |
| Using the maximum principle for harmonic functions | `harmonic-maximum-principle` | `maximum-modulus`, `harmonic-conjugates` |

### Series

| Topic | Slug | Needs |
|---|---|---|
| Using complex sequences and series | `complex-sequences-series` | `complex-limits-continuity`, `calc2.choose-a-series-test` |
| Testing convergence of complex series | `complex-series-tests` | `complex-sequences-series` |
| Using complex power series | `complex-power-series` | `calc2.interval-of-convergence`, `complex-series-tests` |
| Finding the radius of a complex power series | `complex-radius` | `complex-power-series` |
| Proving power series are analytic | `power-series-analytic` | `complex-power-series`, `analytic-functions` |
| Finding complex Taylor series | `taylor-series-complex` | `higher-derivative-formula`, `complex-radius`, `power-series-analytic` |
| Finding Laurent series | `laurent-series` | `taylor-series-complex` |
| Using the identity theorem | `identity-theorem` | `taylor-series-complex` |
| Finding Laurent series with partial fractions | `laurent-partial-fractions` | `laurent-series` |
| Classifying singularities | `singularities-classify` | `laurent-partial-fractions` |
| Finding Laurent series in different annuli | `laurent-annuli` | `laurent-series` |
| Using Riemann's removable singularity theorem | `removable-singularities` | `singularities-classify` |
| Using the Casorati-Weierstrass theorem | `casorati-weierstrass` | `singularities-classify` |
| Finding the order of a zero | `order-of-zero` | `taylor-series-complex` |
| Finding zeros and poles | `zeros-and-poles` | `removable-singularities`, `order-of-zero` |
| Exploring analytic continuation | `analytic-continuation` | `identity-theorem` |

### Residues

| Topic | Slug | Needs |
|---|---|---|
| Defining residues | `residues-definition` | `singularities-classify` |
| Finding residues from Laurent series | `residue-from-laurent` | `residues-definition` |
| Finding residues at simple poles | `residue-simple-pole` | `residues-definition` |
| Finding residues at poles | `computing-residues` | `residue-from-laurent`, `residue-simple-pole` |
| Using the residue theorem | `residue-theorem` | `computing-residues` |
| Summing series with residues | `summing-series-residues` | `residue-theorem` |
| Using the argument principle | `argument-principle` | `residue-theorem`, `zeros-and-poles` |
| Using Rouche's theorem | `rouche` | `argument-principle` |
| Inverting Laplace transforms with residues | `inverse-laplace-residues` | `residue-theorem` |
| Using the residue at infinity | `residue-at-infinity` | `residue-theorem` |
| Evaluating contour integrals with residues | `contour-integrals-by-residues` | `residue-theorem` |
| Evaluating trig integrals with residues | `real-integrals-trig` | `contour-integrals-by-residues` |
| Evaluating improper rational integrals | `real-integrals-rational` | `contour-integrals-by-residues` |
| Using Jordan's lemma for Fourier integrals | `jordan-lemma` | `real-integrals-rational` |
| Using Cauchy principal values | `principal-value` | `real-integrals-rational` |
| Using indented contours | `indented-contours` | `jordan-lemma`, `principal-value` |
| Evaluating integrals with branch cuts | `branch-integrals` | `indented-contours`, `branch-cuts`, `complex-powers` |
| Using rectangular and sector contours | `rectangle-sector-contours` | `real-integrals-rational` |
| Counting zeros in a region with Rouche's theorem | `counting-zeros-rouche` | `rouche` |

### Conformal mappings

| Topic | Slug | Needs |
|---|---|---|
| Defining conformal maps | `conformal-definition` | `analytic-functions`, `complex-mappings` |
| Using linear fractional transformations | `linear-fractional` | `conformal-definition`, `stereographic-sphere` |
| Using the Schwarz lemma | `schwarz-lemma` | `maximum-modulus` |
| Testing where a map is conformal | `where-conformal` | `conformal-definition` |
| Using elementary conformal maps | `elementary-maps` | `images-under-exponential`, `images-under-powers`, `where-conformal` |
| Exploring Schwarz-Christoffel maps | `schwarz-christoffel-intro` | `elementary-maps` |
| Mapping circles and lines with linear fractional maps | `circles-lines-lft` | `linear-fractional` |
| Using the cross ratio | `cross-ratio` | `circles-lines-lft` |
| Mapping a half plane to a disk | `half-plane-to-disk` | `cross-ratio` |
| Stating the Riemann mapping theorem | `riemann-mapping-statement` | `elementary-maps`, `schwarz-lemma`, `half-plane-to-disk` |
| Composing conformal maps | `composed-conformal-maps` | `elementary-maps`, `linear-fractional` |
| Solving Laplace's equation by conformal mapping | `applied-laplace-conformal` | `harmonic-maximum-principle`, `composed-conformal-maps` |
| Applying conformal maps to flows | `conformal-flows` | `applied-laplace-conformal` |
