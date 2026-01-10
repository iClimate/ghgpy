# Getting Started

This guide will help you get started with GHGPy for your GHG inventory calculations.

## Installation

### From PyPI (Recommended)

```bash
pip install ghgpy
```

### For Development

```bash
pip install ghgpy[dev]
```

### From Source

```bash
git clone https://github.com/iClimate/ghgpy.git
cd ghgpy
pip install -e ".[dev]"
```

## Requirements

- Python 3.11 or higher
- pandas, sqlalchemy, pydantic, openpyxl

## Basic Usage

### 1. Import the Package

```python
# Factory class for facility-level tracking
from ghgpy.factory import FactoryGeneral

# Uncertainty data type
from ghgpy.datamodel.fuel import UNumber

# Database handles
from ghgpy.datamodel.db import FuelDataHandle, GHGDataHandle, EFDataHandle

# Default databases
from ghgpy.data.fuels import default_fuel_database
from ghgpy.data.ghg import ghg_gas_data
from ghgpy.data.efs import s_combustion_energy
```

### 2. Create a Factory

```python
MyFactory = FactoryGeneral(
    name="Hong Ha Textile", 
    desc="Textile production for export!"
)
```

### 3. Connect to Databases

```python
MyFactory.connection(
    FuelDataHandle(default_fuel_database),
    EFDataHandle(s_combustion_energy),
    GHGDataHandle(ghg_gas_data, 'ar6')
)
```

### 4. Add Combustion Processes

```python
# Add boilers
MyFactory.add_combustion(name="Boiler", desc="Main steam boiler")
MyFactory.add_combustion(name="Boiler2", desc="Backup boiler")

# Add fuels to each boiler
MyFactory.combustion["Boiler"].add('Diesel_Oil', UNumber(value=1000), 'l')
MyFactory.combustion["Boiler"].add('Anthracite', UNumber(value=1000), 'kg')
MyFactory.combustion["Boiler2"].add('Lignite', UNumber(value=500), 'kg')
```

### 5. Add Refrigerant Use

```python
# Add refrigerant tracking
MyFactory.add_refrigerantuse(name='AC', desc='Office air conditioning')
MyFactory.refrigerantuse["AC"].add("R32", UNumber(value=10, uncertainty=0), 'kg')
```

### 6. Add Electricity Consumption

```python
# Add electricity use
MyFactory.add_elecuse(name='Office')
MyFactory.elecuse['Office'].add(
    name='01', 
    amount=UNumber(value=1), 
    unit='MWh', 
    gef=UNumber(value=0.987),  # Grid emission factor
    force=True
)
```

### 7. Calculate Emissions

```python
# Calculate Scope 1 emissions
scope1 = MyFactory.emission(scope=1)
print(f"Scope 1 emissions: {scope1} tCO2e")

# Calculate Scope 2 emissions
scope2 = MyFactory.emission(scope=2)
print(f"Scope 2 emissions: {scope2} tCO2e")
```

## Key Concepts

### UNumber (Uncertainty Number)

GHGPy uses `UNumber` for values with uncertainty:

```python
from ghgpy.datamodel.fuel import UNumber

# Value with uncertainty
fuel_amount = UNumber(value=1000, uncertainty=50)  # 1000 ± 50
```

### Emission Factors

Emission factors are based on IPCC 2006 Guidelines with 2019 Refinements:

- **CO2** - Carbon dioxide
- **CH4** - Methane  
- **N2O** - Nitrous oxide

### GWP Sources

Supported Global Warming Potential sources:

- `ar6` - IPCC AR6 (2021)
- `ar5` - IPCC AR5 (2014)
- `ar4` - IPCC AR4 (2007)

## Next Steps

- See the [Reference](reference.md) for detailed API documentation
- Read the [Developer Guide](devdocs.md) to contribute
- Check [Patch History](patch_history.md) for version updates