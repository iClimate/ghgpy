"""
GHG inventory for Energy sector
Base on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""
from data.fuel import fuel

class s_combustion:
    """
    Stationary combustion
    """
    def __init__(self, name='', fuel=fuel(), activity='') -> None:
        self.name = name
        self.fuels = fuel
        self.activity = activity
        self.efco2 = 
        self.efch4 = 
        self.efn2o = 
    
    def eval(self):
        self.energy = fuel.to_tj()
        self.co2e = fuel.
        self.ch4 = 
        self.n2o = 

class m_combustion:
    """
    Mobile combustion
    """

    