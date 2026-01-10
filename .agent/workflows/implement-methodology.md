---
description: How to implement a new IPCC GHG calculation methodology
---

# Implementing New IPCC Methodology

## Overview
This workflow guides implementing new GHG emission calculation methodologies following IPCC 2006 guidelines.

## Before Starting

1. **Identify the IPCC chapter and methodology tier**
   - Tier 1: Basic method using default emission factors
   - Tier 2: Country-specific emission factors
   - Tier 3: Higher-order methods with modeling

2. **Review existing similar implementations**
   - Check `activities/energy.py` for combustion examples
   - Review the class structure patterns

## Implementation Steps

### 1. Define the Class Structure

```python
"""
[Sector] - [Subsector] GHG Emissions
IPCC 2006 Volume X, Chapter Y

(c) Bui Khac Tu (bkt92)
"""

from typing import List, Dict, Optional
from data.db import fuels_database
from data.unit_converters import energy_units, weigh_units

class MethodologyName:
    """
    [Brief description of the methodology]
    
    IPCC Reference: Volume X, Chapter Y, Section Z
    Applicable Tier(s): 1, 2, 3
    
    Attributes:
        name: Identifier for the emission source
        activity_data: Activity data (consumption, production, etc.)
        emission_factor: Emission factor(s) used
    """
    
    def __init__(
        self, 
        name: str = '',
        activity_data: Optional[Dict] = None,
        tier: int = 1
    ) -> None:
        self.name = name
        self.activity_data = activity_data or {}
        self.tier = tier
        self.db = fuels_database()
    
    def calculate_co2(self) -> float:
        """
        Calculate CO2 emissions.
        
        Formula: E_CO2 = AD × EF_CO2 × OF
        
        Returns:
            CO2 emissions in kg
        """
        pass
    
    def calculate_ch4(self) -> float:
        """
        Calculate CH4 emissions.
        
        Returns:
            CH4 emissions in kg
        """
        pass
    
    def calculate_n2o(self) -> float:
        """
        Calculate N2O emissions.
        
        Returns:
            N2O emissions in kg
        """
        pass
    
    def calculate_total_co2eq(self, gwp_ch4: float = 28, gwp_n2o: float = 265) -> float:
        """
        Calculate total emissions in CO2 equivalent.
        
        Args:
            gwp_ch4: Global Warming Potential for CH4 (default AR5)
            gwp_n2o: Global Warming Potential for N2O (default AR5)
        
        Returns:
            Total CO2-equivalent emissions in kg
        """
        return (
            self.calculate_co2() + 
            self.calculate_ch4() * gwp_ch4 + 
            self.calculate_n2o() * gwp_n2o
        )
```

### 2. Add Required Emission Factors
Follow the `add-emission-factor.md` workflow to add any new emission factors.

### 3. Implement Unit Conversions
If new unit conversions are needed, update `data/unit_converters.py`:

```python
class new_units:
    """
    Convert between [unit type] units
    """
    
    @staticmethod
    def convert(val: float, unit_in: str, unit_out: str) -> float:
        SI = {'base': 1.0, 'kilo': 1000.0}
        return val * SI[unit_in] / SI[unit_out]
```

### 4. Add Tests
Create test file in `tests/`:

```python
"""Tests for [methodology name]"""

import pytest
from activities.[module] import MethodologyName

def test_tier1_calculation():
    """Test Tier 1 calculation against IPCC example."""
    source = MethodologyName(
        name='test_source',
        activity_data={'fuel_consumption': 1000}  # Example data
    )
    
    result = source.calculate_co2()
    expected = 1000 * EF  # From IPCC example
    
    assert abs(result - expected) < 0.01

def test_unit_conversion():
    """Test that different input units give same result."""
    pass
```

### 5. Add Documentation
Add example usage in `examples/`:

```python
"""
Example: [Methodology Name] Calculation

This example demonstrates calculating emissions for [description].
"""

from activities.[module] import MethodologyName

# Example calculation
source = MethodologyName(
    name='Example Source',
    activity_data={
        'fuel_consumption': 1000,  # tonnes
        'fuel_type': 'diesel'
    }
)

print(f"CO2 emissions: {source.calculate_co2():,.2f} kg")
print(f"Total CO2-eq: {source.calculate_total_co2eq():,.2f} kg")
```

## Validation Checklist

- [ ] Class follows naming conventions
- [ ] All methods have type hints
- [ ] Docstrings include IPCC references
- [ ] Emission factors added to database
- [ ] Unit tests pass
- [ ] Example code runs correctly
- [ ] Calculations validated against IPCC examples
