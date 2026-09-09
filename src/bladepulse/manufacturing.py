from dataclasses import dataclass


@dataclass(frozen=True)
class ManufacturingScenario:
    """A synthetic manufacturing-cost scenario measured per kWh produced."""

    name: str
    capital_cost_usd: float
    annual_capacity_kwh: float
    energy_kwh_per_kwh: float
    electricity_cost_usd_per_kwh: float
    labor_hours_per_kwh: float
    hourly_labor_cost_usd: float
    scrap_rate: float

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must not be empty")

        if self.capital_cost_usd < 0:
            raise ValueError("capital_cost_usd must not be negative")

        if self.annual_capacity_kwh <= 0:
            raise ValueError("annual_capacity_kwh must be greater than zero")

        if self.energy_kwh_per_kwh < 0:
            raise ValueError("energy_kwh_per_kwh must not be negative")

        if self.electricity_cost_usd_per_kwh < 0:
            raise ValueError("electricity_cost_usd_per_kwh must not be negative")

        if self.labor_hours_per_kwh < 0:
            raise ValueError("labor_hours_per_kwh must not be negative")

        if self.hourly_labor_cost_usd < 0:
            raise ValueError("hourly_labor_cost_usd must not be negative")

        if not 0 <= self.scrap_rate < 1:
            raise ValueError("scrap_rate must be greater than or equal to zero and less than one")

    def capital_cost_per_kwh(self) -> float:
        """Return annualized capital cost allocated to one kWh."""
        return self.capital_cost_usd / self.annual_capacity_kwh

    def energy_cost_per_kwh(self) -> float:
        """Return electricity cost allocated to one kWh."""
        return self.energy_kwh_per_kwh * self.electricity_cost_usd_per_kwh

    def labor_cost_per_kwh(self) -> float:
        """Return labor cost allocated to one kWh."""
        return self.labor_hours_per_kwh * self.hourly_labor_cost_usd

    def cost_components_per_kwh(self) -> dict[str, float]:
        """Return transparent cost components including scrap adjustment."""
        capital_cost = self.capital_cost_per_kwh()
        energy_cost = self.energy_cost_per_kwh()
        labor_cost = self.labor_cost_per_kwh()
        pre_scrap_cost = capital_cost + energy_cost + labor_cost
        total_cost = pre_scrap_cost / (1 - self.scrap_rate)

        return {
            "capital": capital_cost,
            "energy": energy_cost,
            "labor": labor_cost,
            "scrap_adjustment": total_cost - pre_scrap_cost,
            "total": total_cost,
        }


def cost_delta_per_kwh(
    reference: ManufacturingScenario,
    challenger: ManufacturingScenario,
) -> float:
    """Return challenger cost minus reference cost per kWh."""
    reference_cost = reference.cost_components_per_kwh()["total"]
    challenger_cost = challenger.cost_components_per_kwh()["total"]

    return challenger_cost - reference_cost