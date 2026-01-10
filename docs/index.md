# GHGPy Documentation

Welcome to the GHGPy documentation - your comprehensive guide to greenhouse gas inventory calculations.

**Carbon inventory, make it easy!**

## What is GHGPy?

GHGPy is a Python package for GHG (Greenhouse Gas) Inventory calculations based on IPCC 2006 Guidelines with 2019 Refinements. It provides a complete framework for:

- **Factory-level emissions tracking** - Model your facility's emission sources
- **Fuel combustion calculations** - Stationary and mobile sources
- **Refrigerant tracking** - F-gas emissions monitoring
- **Electricity consumption** - Scope 2 emissions
- **Uncertainty handling** - Built-in uncertainty data types

## Quick Installation

```bash
pip install ghgpy
```

## Table Of Contents

| Section | Description |
|---------|-------------|
| [About](about.md) | Project background and team |
| [Getting Started](getting_started.md) | Installation and first steps |
| [Reference](reference.md) | API documentation |
| [Developer Guide](devdocs.md) | Contributing guidelines |
| [Patch History](patch_history.md) | Version changelog |
| [License](license.md) | MIT License details |

## Quick Example

```python
from ghgpy.factory import FactoryGeneral
from ghgpy.datamodel.fuel import UNumber
from ghgpy.datamodel.db import FuelDataHandle, GHGDataHandle, EFDataHandle

# Create a factory
factory = FactoryGeneral(name="My Factory", desc="Production facility")

# Add combustion process
factory.add_combustion(name="Boiler", desc="Main boiler")

# Add fuel consumption
factory.combustion["Boiler"].add('Diesel_Oil', UNumber(value=1000), 'l')

# Calculate emissions
emissions = factory.emission(scope=1)
print(f"Scope 1 emissions: {emissions} tCO2e")
```

## Links

- [Website](https://iclimate.io.vn)
- [GitHub Repository](https://github.com/iClimate/ghgpy)
- [PyPI Package](https://pypi.org/project/ghgpy/)
- [Bug Reports](https://github.com/iClimate/ghgpy/issues)

---

*Developed by [iClimate](https://iclimate.io.vn) | [DecarbDirect](https://decarbdirect.com)*