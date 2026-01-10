"""
GHGPy Data Model Module

Data model classes for GHG inventory calculations:
- db: Database connections and emission factor storage
- fuel: Fuel type definitions and conversions
- ghggas: GHG gas properties and GWP values
- unit_converters: Unit conversion utilities

Data sources: IPCC 2006 Guidelines with 2019 Refinements
"""

from .db import fuels_database
from .fuel import fuel
from .ghggas import ghg_gas
from .unit_converters import energy_units, weigh_units, volume_units

__all__ = [
    'fuels_database',
    'fuel',
    'ghg_gas',
    'energy_units',
    'weigh_units',
    'volume_units',
]
