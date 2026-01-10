"""
GHGPy - GHG Inventory Python Package

A Python package for greenhouse gas (GHG) inventory calculations
based on IPCC 2006 Guidelines with 2019 Refinements.

Modules:
    - data: Database access and emission factors
    - activities: GHG calculation modules by IPCC sector

Example:
    >>> from ghgpy.data import fuels_database
    >>> db = fuels_database(db='xlsx')
    >>> print(db.data.head())
"""

__version__ = "0.1.0"
__author__ = "Bùi Khắc Tú"
__email__ = ""
__license__ = "MIT"

# Public API exports
from ghgpy.data import fuels_database, energy_units, weigh_units, volume_units
from ghgpy.activities import s_combustion, m_combustion

__all__ = [
    "__version__",
    "fuels_database",
    "energy_units",
    "weigh_units", 
    "volume_units",
    "s_combustion",
    "m_combustion",
]
