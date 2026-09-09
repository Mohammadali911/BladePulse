import csv
from collections import Counter
from pathlib import Path

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

REQUIRED_FIELDS = [
    "assumption_id",
    "category",
    "variable_name",
    "description",
    "unit",
    "scenario_scope",
    "research_status",
]


class AssumptionRegistryError(ValueError):
    """Raised when the assumption registry violates its data contract."""


def load_assumptions(path: str | Path) -> list[dict[str, str]]:
    """Load and validate assumptions from a CSV registry."""
    registry_path = Path(path)

    if not registry_path.is_file():
        raise AssumptionRegistryError(
            f"Assumption registry does not exist: {registry_path}"
        )

    with registry_path.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != EXPECTED_COLUMNS:
            raise AssumptionRegistryError(
                "Assumption registry columns do not match the expected schema"
            )

        rows = []

        for line_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise AssumptionRegistryError(
                    f"Malformed CSV data on line {line_number}"
                )

            cleaned_row = {
                key: value.strip()
                for key, value in row.items()
            }

            missing_fields = [
                field
                for field in REQUIRED_FIELDS
                if not cleaned_row[field]
            ]

            if missing_fields:
                fields = ", ".join(missing_fields)
                raise AssumptionRegistryError(
                    f"Missing required fields on line {line_number}: {fields}"
                )

            rows.append(cleaned_row)

    if not rows:
        raise AssumptionRegistryError("Assumption registry is empty")

    assumption_ids = [row["assumption_id"] for row in rows]
    duplicate_ids = [
        assumption_id
        for assumption_id, count in Counter(assumption_ids).items()
        if count > 1
    ]

    if duplicate_ids:
        duplicates = ", ".join(sorted(duplicate_ids))
        raise AssumptionRegistryError(
            f"Duplicate assumption IDs found: {duplicates}"
        )

    return rows
