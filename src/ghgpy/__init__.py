"""
GHGPy - GHG Inventory Python Package

Do GHG Inventory and more.
Carbon inventory, make it easy!

A Python package for greenhouse gas (GHG) inventory calculations
based on IPCC 2006 Guidelines with 2019 Refinements.

Modules:
    - data: Database access and emission factors
    - activities: GHG calculation modules by IPCC sector
    - datamodel: Data models for fuel and emissions

Example:
    >>> from ghgpy.data import fuels_database
    >>> db = fuels_database(db='xlsx')
    >>> print(db.data.head())
"""

__version__ = "1.0.0"
__author__ = "Bui Khac Tu"
__email__ = "bkt992@gmail.com"
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
