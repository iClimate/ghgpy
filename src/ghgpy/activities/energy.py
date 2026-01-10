"""
GHG inventory for Energy sector
Base on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""

class s_combustion:
    """
    Stationary combustion
    """
    def __init__(self, name='', fuels=None) -> None:
        self.name = name
        self.fuels = fuels if fuels is not None else []


class m_combustion:
    """
    Mobile combustion
    """
    def __init__(self, name='', vehicles=None) -> None:
        self.name = name
        self.vehicles = vehicles if vehicles is not None else []
