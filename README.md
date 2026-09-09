# BladePulse

**Causal Manufacturing Disruption Digital Twin**

BladePulse is a portfolio data-engineering and analytics project that models how different battery-manufacturing architectures can affect cost, quality, flexibility, and resilience.

It uses BYD as a public case study, while keeping verified facts, secondary evidence, hypotheses, estimates, and simulation assumptions separate.

## Business Question

How can a modular, vertically integrated manufacturing system compete with a capital-intensive, highly automated system—and under what conditions does its advantage disappear?

BladePulse will explore counterfactual scenarios such as:

- What happens when labor costs rise?
- How do tariffs, freight, energy, and material prices change total vehicle cost?
- When does automation outperform labor-intensive flexibility?
- How does a cell-level cost difference roll up into a vehicle-level price difference?

## Current Capabilities

- A 20-row Assumption Registry with documented variables
- Automated CSV schema, row-count, and uniqueness checks
- A reusable fail-fast assumption loader
- A command-line registry summary
- Six automated tests and Ruff code-quality checks
- Python project configuration with an isolated virtual environment

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"

python -m bladepulse.registry_summary
ruff check .
pytest -v
```

## Current Architecture

```text
Assumption Registry CSV
        |
        v
Validated Python Loader
        |
        v
Registry Summary Command
        |
        v
Future BOM Roll-up and Digital Twin Simulation
        |
        v
Future AWS Data Lake and Analytics Dashboard
```

## Repository Structure

```text
data/reference/                 Documented model inputs
docs/                           Problem statement and project documentation
src/bladepulse/                 Reusable application code
tests/                          Automated data and application tests
infrastructure/cloudformation/ Future AWS infrastructure as code
notebooks/                      Future exploratory analysis
dashboards/                     Future decision dashboard
```

## Evidence and Modeling Policy

BladePulse does not claim access to confidential BYD manufacturing data.

Every future model input will be classified as one of:

- Verified fact
- Strong secondary evidence
- Estimate
- Hypothesis
- Simulation assumption
- Model output

The reported clean-box and pharmaceutical cross-pollination narrative remains a hypothesis until supported by credible sources.

## Roadmap

1. Build the cell-to-pack-to-vehicle bill-of-materials roll-up
2. Add scenario parameters for labor, energy, quality, tariffs, freight, and materials
3. Build a Monte Carlo manufacturing digital twin
4. Add multi-objective cost, quality, and flexibility analysis
5. Deploy reproducible datasets and queries to AWS
6. Publish an interactive decision dashboard

## Quality Controls

```bash
ruff check .
pytest -v
```

The project currently contains six passing automated tests.

## Author

Ali Ahmadi