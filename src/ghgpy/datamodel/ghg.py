"""
iClimate - ghgpy

GHG Gas objects
Represent a amount of a specific ghg gas
(C) Bui Khac Tu (bkt92)
(C) iClimate
"""

from .unit_converters import *
from typing import Optional
from pydantic import BaseModel
from src.ghgpy.datamodel.db import GHGDataHandle
from .unumber import UNumber, ufnum

class GHGDATA(BaseModel):
    name: str = None # Name of green house gas
    amount: UNumber = None # Amount of GHG gas in tonne
    unit: str = None # unit of ghg gas
    desc: Optional[str] = None # Description of GHG Gas
    gwp: float = None # Green house gas potential (tCO2e)
    density: Optional[UNumber]  = None # Density of gas (Kg/m3)

class GHGGas(GHGDATA):
    """
    GHG Gas Object (use for all kind of GHG gas) \n
    Representative by tCO2e \n
    Allow "+, -" operators with the same kind of gas
    """
    # Convert to tonnes
    def cal_weight(self, unit='tonne'):
        '''
        Convert to metric unit /n
        Default unit metric tonnes
        '''
        amount = self.amount.to_ufnum()
        if self.unit in weigh_units.units:
            return weigh_units.convert(amount, self.unit, unit)
        if self.unit in volume_units.units:
            if self.density == None:
                return None
            else:
                weight = volume_units.convert(amount, self.unit, 'm3')*self.density
                return weigh_units.convert(weight, 'kg', unit)
    
    def emission(self):
        return self.cal_weight()*self.gwp

    def __repr__(self) -> str:
        return (f'name={self.name!r}, amount={self.emission()!r} tCO2e')

    def __hash__(self) -> int:
        return hash((self.amount, self.name, self.gwp))
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, GHGGas):
            return NotImplemented
        return (
            (self.amount, self.name, self.gwp) == 
            (other.amount, other.name, other.gwp))
    
    def __add__(self, other) -> float:
        if not isinstance(other, GHGGas):
            return NotImplemented
        if (self.name, self.gwp) == (other.name, other.gwp):
            amount  = ufnum(self.cal_weight() + other.cal_weight())
            return GHGGas(self.name, amount, "tonne", \
                          self.desc, self.gwp, self.density)
        else:
            return NotImplemented

    def __sub__(self, other) -> float:
        if not isinstance(other, GHGGas):
            return NotImplemented
        if (self.name, self.gwp) == (other.name, other.gwp):
            amount  = ufnum(self.cal_weight() - other.cal_weight())
            return GHGGas(self.name, amount, "tonne", \
                          self.desc, self.gwp, self.density)
        else:
            return NotImplemented
    
    @classmethod
    def from_dict(cls, data):
        '''
        {'name': {'title': 'Name', 'type': 'string'},
        'amount': {'title': 'Amount', 'type': 'number'},
        'unit': {'title': 'Unit', 'type': 'string'},
        'desc': {'title': 'Desc', 'type': 'string'},
        'gwp': {'title': 'Gwp', 'type': 'number'},
        'density': {'title': 'Density', 'type': 'number'}}
        '''
        return cls(**data)
    
class CO2(GHGGas):
    def __init__(self, amount, unit, database: GHGDataHandle):
        if not database.check_exist("CO2"):
            raise ValueError("CO2 data not not found in database.")
        else:
            super().__init__(name="CO2", amount=amount, unit=unit, desc=database.get("CO2")["desc"], \
                           gwp=database.get("CO2")["gwp"], density=database.get("CO2")["density"])

class CH4(GHGGas):
    def __init__(self, amount, unit, database: GHGDataHandle):
        if not database.check_exist("CH4"):
            raise ValueError("CH4 data not not found in database.")
        else:
            super().__init__(name="CH4", amount=amount, unit=unit, desc=database.get("CH4")["desc"], \
                           gwp=database.get("CH4")["gwp"], density=database.get("CH4")["density"])

class N2O(GHGGas):
    def __init__(self, amount, unit, database: GHGDataHandle):
        if not database.check_exist("N2O"):
            raise ValueError("N2O data not not found in database.")
        else:
            super().__init__(name="N2O", amount=amount, unit=unit, desc=database.get("N2O")["desc"], \
                           gwp=database.get("N2O")["gwp"], density=database.get("N2O")["density"])