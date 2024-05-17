# GHGPy (Green House Gas Python)

---
---
![Python](https://img.shields.io/pypi/bkt92/ghgpy)
![PyPI](https://img.shields.io/pypi/v/ghgpy)
![license](https://img.shields.io/github/license/bkt92/ghgpy)

<h1 align="center">
<img src="https://github.com/bkt92/ghgpy/blob/bf841540ea4500ab9306586aacb6e961367fb77c/branding/logo/ghgpylogofull.jpeg" width="700">
</h1><br>

GHGPy is a Python package for the GHG Inventory. 

- **Website:** https://iclimate.io.vn
- **Our services** https://decarbdirect.com/
- **Documentation:** https://ghgpy.iclimate.io.vn
- **Source code:** https://github.com/iClimate/ghgpy
- **Contributing:** https://ghgpy.iclimate.io.vn/devdocs/
- **Bug reports:** https://github.com/iClimate/ghgpy/issues

---

## Installation

Pip installable package:

`pip install ghgpy`

[pypi: ghgpy](https://pypi.org/project/ghgpy/)


---

## Requirements / Dependencies

Python 3.11 and up

---


Call for Contributions
----------------------

The GHGPy project welcomes your expertise and enthusiasm!

Examples
----------------------

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
