---
description: Core development workflow for GHGPy - GHG Inventory Python package
---

# GHGPy Development Workflow

## Project Overview

GHGPy is a Python package for Greenhouse Gas (GHG) Inventory calculations based on IPCC 2006 guidelines with 2019 refinements.

**Key Directories:**
- `activities/` - GHG inventory modules for each sector (Energy, AFOLU, IPPU, Waste)
- `data/` - Database, fuel definitions, emission factors, and unit converters
- `docs/` - Documentation (to be developed)
- `examples/` - Usage examples (to be developed)
- `tests/` - Unit tests (to be developed)
- `inventory/` - Inventory templates and outputs
- `branding/` - Logo and branding assets

## Development Standards

### 1. Code Style
- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return values
- Include docstrings for all classes and public methods
- Follow IPCC 2006 naming conventions where applicable

### 2. Module Structure
Each activity module (energy.py, afolu.py, ippu.py, waste.py) should follow this pattern:

```python
"""
GHG inventory for [Sector Name]
Based on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""

from data.db import fuels_database
from data.unit_converters import energy_units

class MethodologyClass:
    """
    Description of the IPCC methodology being implemented.
    
    Reference: IPCC 2006 Volume X, Chapter Y
    """
    
    def __init__(self, **kwargs) -> None:
        pass
    
    def calculate_emissions(self) -> float:
        """Calculate GHG emissions using specified methodology."""
        pass
```

### 3. Data Management
- Default emission factors are stored in `data/database.xlsx`
- Use `fuels_database` class to access and update emission factors
- Support multiple database backends (xlsx, sqlite, mysql)

### 4. Unit Handling
- Always use SI units internally (J, kg, m³)
- Convert user inputs using `unit_converters.py` classes
- Document expected units in docstrings

## Adding New Features

1. **Before coding:**
   - Review IPCC 2006 guidelines for the relevant methodology
   - Check existing implementations for similar patterns
   - Plan the class structure and methods

2. **Implementation:**
   - Create/update module in `activities/`
   - Add necessary data to `data/database.xlsx`
   - Update data classes if needed

3. **Testing:**
   - Add unit tests in `tests/`
   - Validate calculations against IPCC examples

4. **Documentation:**
   - Update docstrings
   - Add usage examples to `examples/`
   - Update `docs/` if applicable

## GHG Inventory Sectors

### Energy (1)
- Stationary Combustion (1A1-1A4)
- Mobile Combustion (1A3)
- Fugitive Emissions (1B)

### AFOLU (3)
- Livestock (3A)
- Land Use (3B)
- Agriculture (3C)

### IPPU (2)
- Mineral Industry (2A)
- Chemical Industry (2B)
- Metal Industry (2C)
- Product Use (2D-2H)

### Waste (4)
- Solid Waste Disposal (4A)
- Biological Treatment (4B)
- Incineration (4C)
- Wastewater (4D)
