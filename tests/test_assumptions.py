from pathlib import Path

import pytest

from bladepulse.assumptions import (
    EXPECTED_COLUMNS,
    AssumptionRegistryError,
    load_assumptions,
)

REGISTRY_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "reference"
    / "assumption_registry.csv"
)


def make_row(assumption_id: str) -> dict[str, str]:
    row = {column: "" for column in EXPECTED_COLUMNS}
    row.update(
        {
            "assumption_id": assumption_id,
            "category": "test",
            "variable_name": "test_variable",
            "description": "Test assumption",
            "unit": "count",
            "scenario_scope": "both",
            "research_status": "unresearched",
        }
    )
    return row


def test_load_assumptions_returns_clean_registry():
    rows = load_assumptions(REGISTRY_PATH)

    assert len(rows) == 20
    assert rows[0]["assumption_id"] == "A001"


def test_load_assumptions_rejects_missing_file(tmp_path):
    missing_path = tmp_path / "missing.csv"

    with pytest.raises(AssumptionRegistryError, match="does not exist"):
        load_assumptions(missing_path)
