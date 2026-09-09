import pytest

from bladepulse.manufacturing import ManufacturingScenario, cost_delta_per_kwh


def build_centralized_scenario() -> ManufacturingScenario:
    return ManufacturingScenario(
        name="centralized_synthetic",
        capital_cost_usd=1000.0,
        annual_capacity_kwh=100.0,
        energy_kwh_per_kwh=2.0,
        electricity_cost_usd_per_kwh=0.5,
        labor_hours_per_kwh=3.0,
        hourly_labor_cost_usd=4.0,
        scrap_rate=0.1,
    )


def build_modular_scenario() -> ManufacturingScenario:
    return ManufacturingScenario(
        name="modular_synthetic",
        capital_cost_usd=400.0,
        annual_capacity_kwh=100.0,
        energy_kwh_per_kwh=1.0,
        electricity_cost_usd_per_kwh=0.5,
        labor_hours_per_kwh=1.0,
        hourly_labor_cost_usd=4.0,
        scrap_rate=0.0,
    )


def test_cost_components_are_transparent_and_reconcile():
    scenario = build_centralized_scenario()

    assert scenario.cost_components_per_kwh() == pytest.approx(
        {
            "capital": 10.0,
            "energy": 1.0,
            "labor": 12.0,
            "scrap_adjustment": 23.0 / 0.9 - 23.0,
            "total": 23.0 / 0.9,
        }
    )


def test_cost_delta_compares_two_synthetic_scenarios():
    centralized = build_centralized_scenario()
    modular = build_modular_scenario()

    assert cost_delta_per_kwh(centralized, modular) == pytest.approx(
        8.5 - 23.0 / 0.9
    )


@pytest.mark.parametrize(
    ("annual_capacity_kwh", "scrap_rate"),
    [
        (0.0, 0.0),
        (100.0, -0.01),
        (100.0, 1.0),
    ],
)
def test_scenario_rejects_invalid_capacity_or_scrap_rate(
    annual_capacity_kwh: float,
    scrap_rate: float,
):
    with pytest.raises(ValueError):
        ManufacturingScenario(
            name="invalid_synthetic",
            capital_cost_usd=1.0,
            annual_capacity_kwh=annual_capacity_kwh,
            energy_kwh_per_kwh=1.0,
            electricity_cost_usd_per_kwh=1.0,
            labor_hours_per_kwh=1.0,
            hourly_labor_cost_usd=1.0,
            scrap_rate=scrap_rate,
        )