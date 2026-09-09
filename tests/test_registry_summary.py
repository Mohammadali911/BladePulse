from pathlib import Path

from bladepulse.registry_summary import summarize_registry

REGISTRY_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "reference"
    / "assumption_registry.csv"
)


def test_summary_reports_expected_registry_counts():
    summary = summarize_registry(REGISTRY_PATH)

    assert summary["total_assumptions"] == 20
    assert summary["by_scenario_scope"] == {
        "both": 16,
        "centralized": 1,
        "modular": 3,
    }
    assert summary["by_category"]["capital"] == 2
    assert summary["by_category"]["supply_chain"] == 2