---
description: How to add or update emission factors in the GHGPy database
---

# Adding/Updating Emission Factors

## Overview
Emission factors are the core data for GHG calculations. They are stored in `data/database.xlsx` and accessed via the `fuels_database` class.

## Steps to Add New Emission Factor

### 1. Identify the Data Source
- Use IPCC 2006 Guidelines with 2019 Refinements as primary source
- Document the specific table/chapter reference
- Note any country-specific or technology-specific values

### 2. Update the Database
1. Open `data/database.xlsx`
2. Add new row(s) with the following columns:
   - Fuel type / Activity name
   - Net Calorific Value (NCV) in TJ/Gg
   - Density (kg/L or kg/m³ if applicable)
   - CO2 Emission Factor (kg CO2/TJ)
   - CH4 Emission Factor (kg CH4/TJ)
   - N2O Emission Factor (kg N2O/TJ)
   - Source reference (IPCC table number)
   - Uncertainty range if available

### 3. Verify Data Access
```python
from data.db import fuels_database

# Test data loading
db = fuels_database(db='xlsx')
print(db.data)  # Verify new data appears
```

### 4. Update Data Classes (if needed)
If adding a new fuel category, update `data/fuel.py`:

```python
class new_fuel_category:
    '''
    Fuel List: [list of fuels]
    Reference: IPCC 2006 Table X.X
    '''
    pass
```

## Standard Data Sources

| Data Type | Source | IPCC Reference |
|-----------|--------|----------------|
| Fuel NCVs | IPCC 2006 Vol 2 | Table 1.2 |
| Fuel Densities | IPCC 2006 Vol 2 | Table 1.3 |
| Stationary EFs | IPCC 2006 Vol 2 | Table 2.2-2.6 |
| Mobile EFs | IPCC 2006 Vol 2 | Table 3.2.1-3.2.2 |
| GWP Values | IPCC AR6 | Table 7.SM.7 |

## Quality Checks

- [ ] Values match source document exactly
- [ ] Units are consistent with existing data
- [ ] Uncertainties documented where available
- [ ] Test calculation produces expected results
