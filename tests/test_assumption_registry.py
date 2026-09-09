import csv
from pathlib import Path

REGISTRY_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "reference"
    / "assumption_registry.csv"
)

EXPECTED_COLUMNS = [
    "assumption_id",
    "category",
    "variable_name",
    "description",
    "unit",
    "baseline_value",
    "low_value",
    "high_value",
    "distribution",
    "evidence_class",
    "confidence_score",
    "source_url",
    "source_date",
    "scenario_scope",
    "research_status",
    "notes",
]


def load_registry():
    with REGISTRY_PATH.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return reader.fieldnames, list(reader)


def test_registry_has_expected_schema():
    columns, _ = load_registry()

    assert columns == EXPECTED_COLUMNS


def test_registry_contains_twenty_assumptions():
    _, rows = load_registry()

    assert len(rows) == 20


def test_assumption_ids_are_unique_and_rows_are_aligned():
    _, rows = load_registry()
    assumption_ids = [row["assumption_id"] for row in rows]

    assert len(assumption_ids) == len(set(assumption_ids))
    assert all(None not in row for row in rows)
