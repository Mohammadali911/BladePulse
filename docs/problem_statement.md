# BladePulse: Causal Manufacturing Disruption Digital Twin

## Project Mission

BladePulse is an AWS-based causal analytics and digital-twin platform that investigates how a modular, vertically integrated manufacturing system can compete with a capital-intensive, highly automated manufacturing system.

The project uses BYD as a public case study, but it does not assume that every published story about BYD is true. Verified facts, estimates, hypotheses, and simulation results are stored separately.

## Core Business Problem

Traditional analysis often explains manufacturing competitiveness using isolated measures such as wages, battery prices, sales volume, or government policy. That approach fails to show how process design, labour, energy, product architecture, supply-chain control, and external shocks interact.

BladePulse will connect these factors from battery cell to finished vehicle and answer counterfactual questions that historical reports alone cannot answer.

## Virtual Factory Comparison

BladePulse will simulate two configurable factories:

1. Centralized Factory: capital-intensive automation, large controlled environments, high fixed cost, and lower dependence on labour.
2. Modular Factory: localized environmental control, flexible production cells, lower initial capital cost, and higher dependence on trained labour.

These factories are analytical scenarios. They are not claimed to be exact replicas of BYD or any competitor.

## Questions This Project Must Answer

### Q1. Capital-versus-labour tipping point

At what wage, training cost, employee turnover rate, and defect rate does the modular factory lose its cost advantage over centralized automation?

### Q2. Micro-to-macro cost inheritance

How do savings or losses at the battery-cell level propagate through the battery pack, vehicle platform, factory, and final vehicle price?

### Q3. Quality and human-dependency risk

How do fatigue, training time, employee turnover, contamination events, and process variability affect yield, scrap, throughput, and warranty exposure?

### Q4. Flexibility value

When demand or product design changes, how much money and production time can each factory save through faster reconfiguration?

### Q5. Contamination and recovery resilience

Does localized process isolation reduce the operational impact and recovery time of a contamination event compared with a centralized clean environment?

### Q6. Vertical-integration resilience

Under what combinations of supplier failure, semiconductor shortage, battery-material volatility, and logistics disruption does vertical integration create measurable value?

### Q7. Macroeconomic and regulatory shocks

How do tariffs, lithium prices, electricity prices, wages, exchange rates, and freight costs change the competitive frontier?

### Q8. Cost-quality-flexibility frontier

Which factory configuration produces the best achievable balance among unit cost, quality, production speed, resilience, and flexibility?

### Q9. Evidence confidence

How much does each conclusion change when low-confidence assumptions are removed or assigned lower causal weights?

## Primary Metrics

BladePulse will calculate:

* Capital cost
* Operating cost
* Cost per battery cell
* Cost per kilowatt-hour
* Cost per battery pack
* Estimated manufacturing cost per vehicle
* Energy consumed per unit
* Labour hours per kilowatt-hour
* First-pass yield
* Defect and scrap rates
* Throughput
* Reconfiguration downtime
* Contamination recovery time
* Supplier concentration risk
* Expected disruption loss
* Scenario confidence score

## Evidence Classification

Every important input and causal relationship must be labelled as one of the following:

* Verified fact: supported by a primary or authoritative source
* Strong secondary evidence: supported by credible independent reporting
* Estimate: calculated from documented public information
* Hypothesis: plausible but not sufficiently verified
* Simulation assumption: deliberately selected for scenario testing
* Model output: produced by BladePulse and not presented as an observed fact

The reported clean-box or pharmaceutical cross-pollination story will remain a hypothesis until reliable evidence is documented.

## Planned Analytical Outputs

BladePulse will produce:

1. A source and assumption registry
2. A cell-to-pack-to-vehicle bill-of-materials roll-up
3. A Monte Carlo manufacturing digital twin
4. A causal knowledge graph
5. Stress tests for labour, tariffs, materials, energy, freight, and supplier failures
6. A multi-objective Pareto frontier
7. Reproducible Athena queries
8. An interactive decision dashboard
9. Automated tests and data-quality checks
10. Architecture, cost, security, and model documentation for GitHub

## Success Criteria

The project succeeds when another analyst can:

* Reproduce every published result
* Trace each input to a source or assumption
* Change a scenario without changing application code
* Explain why a result changed
* Distinguish correlation from causal assumptions
* Deploy and remove the AWS environment using version-controlled infrastructure
* Verify that no persistent AWS resource remains after cleanup

## Responsible Claims

BladePulse does not claim access to confidential BYD manufacturing data. It does not claim to prove corporate intent or establish that one company caused another company’s financial decline.

Its contribution is a transparent and reproducible framework that integrates manufacturing economics, operational risk, supply-chain structure, macroeconomic shocks, and evidence confidence within one decision system.

