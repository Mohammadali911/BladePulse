import pytest

from bladepulse.bom import BomNode, cost_breakdown_usd


def build_synthetic_vehicle_bom() -> BomNode:
    battery_cells = BomNode(
        component_id="battery_cell",
        quantity_per_parent=4,
        direct_unit_cost_usd=10.0,
    )
    battery_pack = BomNode(
        component_id="battery_pack",
        quantity_per_parent=1,
        direct_unit_cost_usd=20.0,
        children=(battery_cells,),
    )

    return BomNode(
        component_id="vehicle",
        quantity_per_parent=1,
        direct_unit_cost_usd=100.0,
        children=(battery_pack,),
    )


def test_bom_rolls_cell_cost_up_to_vehicle_cost():
    vehicle = build_synthetic_vehicle_bom()

    assert vehicle.total_cost_usd() == 160.0


def test_bom_cost_breakdown_reconciles_to_total_cost():
    vehicle = build_synthetic_vehicle_bom()

    assert cost_breakdown_usd(vehicle) == {
        "battery_cell": 40.0,
        "battery_pack": 20.0,
        "vehicle": 100.0,
    }
    assert sum(cost_breakdown_usd(vehicle).values()) == vehicle.total_cost_usd()


@pytest.mark.parametrize(
    ("quantity_per_parent", "direct_unit_cost_usd"),
    [
        (0, 1.0),
        (-1, 1.0),
        (1, -1.0),
    ],
)
def test_bom_rejects_invalid_cost_inputs(
    quantity_per_parent: float,
    direct_unit_cost_usd: float,
):
    with pytest.raises(ValueError):
        BomNode(
            component_id="invalid_component",
            quantity_per_parent=quantity_per_parent,
            direct_unit_cost_usd=direct_unit_cost_usd,
        )