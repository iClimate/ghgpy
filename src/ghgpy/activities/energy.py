"""
GHG inventory for Energy sector
Base on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""


class s_combustion:
    """
    Stationary combustion
    
    Calculate GHG emissions from stationary fuel combustion.
    """
    def __init__(self, name='', fuels=None, activity='') -> None:
        self.name = name
        self.fuels = fuels if fuels is not None else []
        self.activity = activity
        self.efco2 = None
        self.efch4 = None
        self.efn2o = None
    
    def eval(self):
        """Evaluate emissions from fuel combustion."""
        # TODO: Implement emission calculations
        pass


class m_combustion:
    """
    Mobile combustion
    
    Calculate GHG emissions from mobile sources (vehicles).
    """
    def __init__(self, name='', vehicles=None) -> None:
        self.name = name
        self.vehicles = vehicles if vehicles is not None else []
