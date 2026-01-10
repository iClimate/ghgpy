---
description: Guide for working with the GHGPy database system
---

# Database Guide

## Overview

GHGPy supports multiple database backends for storing and retrieving emission factors and fuel data.

**Location:** `data/`
**Main class:** `data/db.py` → `fuels_database`

## Supported Backends

| Backend | File | Status | Use Case |
|---------|------|--------|----------|
| Excel | `database.xlsx` | ✅ Active | Development, small-scale |
| SQLite | `database.db` | 🔧 Planned | Local applications |
| MySQL | Remote | 🔧 Planned | Enterprise, web apps |

## Using the Database

### Loading Data

```python
from data.db import fuels_database

# Default: Load from Excel
db = fuels_database(db='xlsx')

# Access data as pandas DataFrame
print(db.data.head())
print(db.data.columns)

# Filter data
diesel_data = db.data[db.data['fuel_type'] == 'diesel']
```

### Database Schema

The `database.xlsx` file should contain these columns:

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| fuel_id | str | Unique identifier | "diesel_01" |
| fuel_name | str | Display name | "Diesel Oil (Gas Oil)" |
| fuel_type | str | Category | "liquid" |
| ncv_default | float | Net Calorific Value (TJ/Gg) | 43.0 |
| density | float | Density (kg/L) | 0.84 |
| ef_co2 | float | CO2 EF (kg/TJ) | 74100 |
| ef_ch4 | float | CH4 EF (kg/TJ) | 3 |
| ef_n2o | float | N2O EF (kg/TJ) | 0.6 |
| source | str | IPCC reference | "Vol 2, Table 2.3" |

### Custom Data

To use custom (country-specific) emission factors:

```python
# Load database
db = fuels_database(db='xlsx')

# Update a specific value (planned feature)
db.update(fuel_id='diesel_01', ef_co2=75000)

# Reset to defaults
db.reset_to_default()
```

## Data Sources

### IPCC 2006 Guidelines

| Data Category | Volume | Chapter | Table |
|---------------|--------|---------|-------|
| Fuel NCVs | 2 | 1 | 1.2, 1.3 |
| Fuel Densities | 2 | 1 | 1.4 |
| Stationary EFs | 2 | 2 | 2.2-2.6 |
| Mobile EFs | 2 | 3 | 3.2.1-3.2.2 |
| Fugitive EFs | 2 | 4 | Various |

### GWP Values

Global Warming Potentials should use AR6 values:

| Gas | GWP (100-year) | Source |
|-----|----------------|--------|
| CO2 | 1 | IPCC AR6 |
| CH4 | 27.9 | IPCC AR6 |
| N2O | 273 | IPCC AR6 |

## Adding New Data

See `add-emission-factor.md` workflow for detailed steps.

### Quick Steps:

1. Open `data/database.xlsx` in Excel or pandas
2. Add new row(s) following the schema above
3. Document the source reference
4. Test data loading:

```python
from data.db import fuels_database
db = fuels_database()
print(db.data.tail())  # Verify new data
```

## Planned Features

- [ ] SQLite backend for offline applications
- [ ] MySQL/PostgreSQL for web deployments
- [ ] Data versioning and change tracking
- [ ] Import/export functionality
- [ ] Data validation on load
