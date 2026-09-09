from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class BomNode:
    """A component in a hierarchical bill of materials."""

    component_id: str
    quantity_per_parent: float
    direct_unit_cost_usd: float
    children: tuple["BomNode", ...] = ()

    def __post_init__(self) -> None:
        if not self.component_id.strip():
            raise ValueError("component_id must not be empty")

        if self.quantity_per_parent <= 0:
            raise ValueError("quantity_per_parent must be greater than zero")

        if self.direct_unit_cost_usd < 0:
            raise ValueError("direct_unit_cost_usd must not be negative")

    def total_cost_usd(self) -> float:
        """Return this component's direct and descendant cost."""
        child_cost = sum(child.total_cost_usd() for child in self.children)
        unit_rollup_cost = self.direct_unit_cost_usd + child_cost

        return self.quantity_per_parent * unit_rollup_cost


def cost_breakdown_usd(root: BomNode) -> dict[str, float]:
    """Return direct costs by component for a complete BOM tree."""
    breakdown: defaultdict[str, float] = defaultdict(float)

    def visit(node: BomNode, parent_quantity: float) -> None:
        total_quantity = parent_quantity * node.quantity_per_parent

        breakdown[node.component_id] += total_quantity * node.direct_unit_cost_usd

        for child in node.children:
            visit(child, total_quantity)

    visit(root, parent_quantity=1)

    return dict(sorted(breakdown.items()))