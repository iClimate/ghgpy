"""
GHGPy Data Module

Database access and utility modules:
- db: Database connections and emission factor storage
- fuel: Fuel type definitions
- unit_converters: Unit conversion utilities
- ghggas: GHG gas properties and GWP values
- refrigerant: Refrigerant data for F-gas calculations

Data sources: IPCC 2006 Guidelines with 2019 Refinements
"""

from .db import fuels_database
from .unit_converters import energy_units, weigh_units, volume_units

__all__ = [
    'fuels_database',
    'energy_units',
    'weigh_units',
    'volume_units',
]
