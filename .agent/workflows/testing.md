---
description: How to run and write tests for GHGPy
---

# Testing Workflow

## Running Tests

// turbo
1. Ensure pytest is installed:
```powershell
pip install pytest pytest-cov
```

// turbo
2. Run all tests:
```powershell
cd f:\ghgpy
pytest tests/ -v
```

// turbo
3. Run tests with coverage:
```powershell
pytest tests/ --cov=activities --cov=data --cov-report=html
```

// turbo
4. Run specific test file:
```powershell
pytest tests/test_energy.py -v
```

## Writing Tests

### Test File Structure
Place tests in `tests/` with naming convention `test_<module>.py`.

```python
"""
Tests for activities/energy.py

Test data sources:
- IPCC 2006 Vol 2, Chapter 2, Examples
"""

import pytest
from activities.energy import s_combustion, m_combustion
from data.db import fuels_database


class TestStationaryCombustion:
    """Tests for stationary combustion calculations."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.db = fuels_database(db='xlsx')
    
    def test_basic_calculation(self):
        """Test basic CO2 calculation."""
        source = s_combustion(name='test', fuels=['diesel'])
        result = source.calculate_co2()
        assert result > 0
    
    def test_ipcc_example(self):
        """
        Validate against IPCC worked example.
        
        Reference: IPCC 2006 Vol 2, Chapter 2, Box 2.1
        """
        # Input from IPCC example
        fuel_consumption = 1000  # TJ
        ef_co2 = 74100  # kg CO2/TJ for natural gas
        
        expected = fuel_consumption * ef_co2
        
        source = s_combustion(
            name='ipcc_example',
            fuels=[{'type': 'natural_gas', 'consumption': fuel_consumption}]
        )
        
        result = source.calculate_co2()
        assert abs(result - expected) < 100  # Allow small rounding difference
    
    def test_invalid_fuel_raises_error(self):
        """Test that invalid fuel type raises appropriate error."""
        with pytest.raises(ValueError, match="Unknown fuel type"):
            s_combustion(name='test', fuels=['invalid_fuel'])


class TestUnitConverters:
    """Tests for unit conversion functions."""
    
    def test_energy_tj_to_mj(self):
        """Test TJ to MJ conversion."""
        from data.unit_converters import energy_units
        
        result = energy_units.convert(1.0, 'TJ', 'MJ')
        assert result == 1_000_000
    
    def test_roundtrip_conversion(self):
        """Test that conversion and back gives original value."""
        from data.unit_converters import energy_units
        
        original = 42.5
        intermediate = energy_units.convert(original, 'TJ', 'J')
        result = energy_units.convert(intermediate, 'J', 'TJ')
        
        assert abs(result - original) < 0.001
```

### Test Categories

1. **Unit Tests** - Individual function/method tests
2. **Integration Tests** - Database + calculation tests
3. **Validation Tests** - Compare against IPCC examples
4. **Edge Case Tests** - Zero values, negative values, invalid inputs

### Validation Data Sources

| Test Type | Data Source |
|-----------|-------------|
| Energy combustion | IPCC 2006 Vol 2, Box 2.1 |
| Mobile combustion | IPCC 2006 Vol 2, Box 3.2.1 |
| Fugitive emissions | IPCC 2006 Vol 2, Box 4.1 |

## Continuous Integration

When CI/CD is set up, tests will run automatically on:
- Pull requests to main branch
- Push to develop branch
- Nightly scheduled runs

## Troubleshooting

### Common Issues

**Database not found:**
```python
# Ensure correct path in tests
import os
os.chdir('f:/ghgpy')
```

**Module import errors:**
```python
# Add project root to path
import sys
sys.path.insert(0, 'f:/ghgpy')
```
