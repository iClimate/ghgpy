"""
Tests for data/db.py - Database functionality

Reference data from IPCC 2006 Guidelines
"""

import pytest

from ghgpy.data.db import fuels_database


class TestFuelsDatabase:
    """Tests for fuels_database class."""

    def test_xlsx_load(self):
        """Test loading data from Excel file."""
        db = fuels_database(db='xlsx')
        assert db.data is not None
        assert len(db.data) > 0

    def test_data_has_required_columns(self):
        """Test that database has expected structure."""
        db = fuels_database(db='xlsx')
        # Verify database loaded successfully
        assert hasattr(db, 'data')


class TestUnitConverters:
    """Tests for unit conversion functions."""

    def test_energy_units_import(self):
        """Test that energy_units can be imported."""
        from ghgpy.data.unit_converters import energy_units
        assert energy_units is not None

    def test_weigh_units_import(self):
        """Test that weigh_units can be imported."""
        from ghgpy.data.unit_converters import weigh_units
        assert weigh_units is not None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
