"""
GHGPy Activities Module

GHG inventory calculation modules for each IPCC sector:
- Energy (Category 1)
- IPPU - Industrial Processes and Product Use (Category 2)
- AFOLU - Agriculture, Forestry and Other Land Use (Category 3)
- Waste (Category 4)

Based on IPCC 2006 Guidelines with 2019 Refinements.
"""

from .energy import s_combustion, m_combustion
# from .ippu import *
# from .afolu import *
# from .waste import *

__all__ = [
    's_combustion',
    'm_combustion',
]
