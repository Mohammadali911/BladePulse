import argparse
from collections import Counter
from pathlib import Path

from bladepulse.assumptions import load_assumptions

DEFAULT_REGISTRY_PATH = Path("data/reference/assumption_registry.csv")


def summarize_registry(path: str | Path) -> dict[str, int | dict[str, int]]:
    """Return counts that describe the assumption registry."""
    rows = load_assumptions(path)

    category_counts = Counter(row["category"] for row in rows)
    scope_counts = Counter(row["scenario_scope"] for row in rows)

    return {
        "total_assumptions": len(rows),
        "by_category": dict(sorted(category_counts.items())),
        "by_scenario_scope": dict(sorted(scope_counts.items())),
    }


def format_registry_summary(summary: dict[str, int | dict[str, int]]) -> str:
    """Format a human-readable registry summary."""
    category_counts = summary["by_category"]
    scope_counts = summary["by_scenario_scope"]

    lines = [
        "BladePulse Assumption Registry Summary",
        f"Total assumptions: {summary['total_assumptions']}",
        "",
        "Assumptions by category:",
    ]

    lines.extend(
        f"- {category}: {count}"
        for category, count in category_counts.items()
    )

    lines.extend(["", "Assumptions by scenario scope:"])

    lines.extend(
        f"- {scope}: {count}"
        for scope, count in scope_counts.items()
    )

    return "\n".join(lines)


def main() -> None:
    """Run the registry summary from the command line."""
    parser = argparse.ArgumentParser(
        description="Summarize the BladePulse assumption registry."
    )
    parser.add_argument(
        "--registry",
        type=Path,
        default=DEFAULT_REGISTRY_PATH,
        help="Path to the assumption registry CSV file.",
    )
    arguments = parser.parse_args()

    summary = summarize_registry(arguments.registry)
    print(format_registry_summary(summary))


if __name__ == "__main__":
    main()
