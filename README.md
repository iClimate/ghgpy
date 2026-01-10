# GHGPy (Green House Gas Python)

---
![Python](https://img.shields.io/pypi/pyversions/ghgpy)
![PyPI](https://img.shields.io/pypi/v/ghgpy)
![license](https://img.shields.io/github/license/iClimate/ghgpy)

<h1 align="center">
<img src="https://github.com/iClimate/ghgpy/blob/main/branding/logo/ghgpylogofull.jpeg" width="700">
</h1><br>

# GHGPy

A Python package for GHG (Greenhouse Gas) Inventory calculations based on IPCC 2006 Guidelines with 2019 Refinements.

**Carbon inventory, make it easy!**

[![PyPI version](https://badge.fury.io/py/ghgpy.svg)](https://badge.fury.io/py/ghgpy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## Installation

```bash
pip install ghgpy
```

For development:
```bash
pip install ghgpy[dev]
```

[pypi: ghgpy](https://pypi.org/project/ghgpy/)

## Requirements / Dependencies

Python 3.11 and up

## Quick Start

```python
from ghgpy import __version__
from ghgpy.data import fuels_database

# Load the emission factors database
db = fuels_database(db='xlsx')

# Display available data
print(f"GHGPy v{__version__}")
print(f"Number of emission factors: {len(db.data)}")
print(db.data.head())
```

## Features

- **IPCC 2006 Guidelines**: Emission factors from IPCC 2006 with 2019 Refinements
- **Multiple Sectors**: Support for Energy, IPPU, AFOLU, and Waste sectors
- **Flexible Database**: Excel-based database with SQLite/MySQL support
- **Unit Converters**: Built-in energy, weight, and volume conversions
- **Factory Pattern**: Easy-to-use factory classes for GHG calculations
- **Uncertainty Support**: Built-in uncertainty data types

## Links

- **Website:** https://iclimate.io.vn
- **Our services** https://decarbdirect.com/
- **Documentation:** https://ghgpy.iclimate.io.vn
- **Source code:** https://github.com/iClimate/ghgpy
- **Contributing:** https://ghgpy.iclimate.io.vn/devdocs/
- **Bug reports:** https://github.com/iClimate/ghgpy/issues

---

## Call for Contributions

The GHGPy project welcomes your expertise and enthusiasm! We're looking for contributors to help with:

- Adding emission factors for additional regions
- Implementing new calculation methodologies
- Improving documentation
- Writing tests

## Basic Usage

### Import library

```python
    # General factory 
    from src.ghgpy.factory import FactoryGeneral
    # Uncertainty data type
    from src.ghgpy.datamodel.fuel import UNumber

    # Database handles
    from src.ghgpy.datamodel.db import FuelDataHandle, GHGDataHandle, EFDataHandle
    # Default databases
    from src.ghgpy.data.fuels import default_fuel_database
    from src.ghgpy.data.ghg import ghg_gas_data
    from src.ghgpy.data.efs import s_combustion_energy
```

### Create a factory

```python
    # Init the factory class
    MyFactory = FactoryGeneral(name="Hong Ha Textile", desc = "Textile production for export!")
```

### Connect to the database

```python
    MyFactory.connection(FuelDataHandle(default_fuel_database),\
                EFDataHandle(s_combustion_energy),\
                    GHGDataHandle(ghg_gas_data, 'ar6'))
```

### Add a combussion process in factory

```python
    MyFactory.add_combustion(name = "Boiler", desc = "Đốt lò hơi")
```

### Add another combussion process in factory

```python
    MyFactory.add_combustion(name = "Boiler1", desc = "Đốt lò than bùn")
```

### Add fuels use in these combussion

```python
    MyFactory.combustion["Boiler"].add('Diesel_Oil', UNumber(value=1000), 'l')
    MyFactory.combustion["Boiler"].add('Anthracite', UNumber(value=1000), 'kg')
    MyFactory.combustion["Boiler1"].add('Lignite', UNumber(value=1000), 'kg')
```

### Add refrigerant use in factory

```python
    MyFactory.add_refrigerantuse(name='AC', desc='refrigerant use for AC')
```

### Add amount of specific type of refrigerant

```python
    MyFactory.refrigerantuse["AC"].add("R32", UNumber(value=10, uncertainty=0), 'kg')
```

### Electriciy use in factory

```python
    MyFactory.add_elecuse(name='Office')
```

### Electriciy consumption

```python
    MyFactory.elecuse['Office'].add(name='01', amount=UNumber(value=1), unit='MWh', gef=UNumber(value=0.987), force=True)
```

### Calculate emission

```python
    MyFactory.emission(scope=1)
```

## License

MIT License - see [LICENSE](LICENSE) for details.
