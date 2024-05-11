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

class GHGDATA(BaseModel):
    name: str = None # Name of green house gas
    amount: float = None # Amount of GHG gas in tonne
    unit: str = None # unit of ghg gas
    desc: Optional[str] = None # Description of GHG Gas
    gwp: float = None # Green house gas potential (tCO2e)
    density: Optional[float]  = None # Density of gas (Kg/m3)

class GHGGas:
    """
    GHG Gas Object (use for all kind of GHG gas) \n
    Representative by tCO2e \n
    Allow "+, -" operators with the same kind of fuel
    """
    # Init attributes of fuel
    def __init__(self, name: str, amount: float, unit: str, desc: str, gwp: float, density: float):
        self.data = GHGDATA(name=name, amount=amount, unit=unit, desc=desc, gwp=gwp, density=density)
        self.emission = self._to_tonnes()*self.data.gwp

    # Convert to tonnes
    def to_tonnes(self):
        '''
        Convert to metric tonnes
        '''
        if self.data.unit in weigh_units.units:
            return weigh_units.convert(self.data.amount, self.data.unit, 'tonne')
        if self.data.unit in volume_units.units:
            if self.data.density == None:
                return None
            else:
                return volume_units.convert(self.data.amount, self.data.unit, 'm3')*self.data.density/1000

    def __repr__(self) -> str:
        return (
            'fuel('
            f'name={self.data.name!r}, amount={self.emission!r} tCO2e)'
        )

    def __hash__(self) -> int:
        return hash((self.data.amount, self.data.name, self.data.gwp))
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, GHGGas):
            return NotImplemented
        return (
            (self.data.amount, self.data.name, self.data.gwp) == 
            (other.data.amount, other.data.name, other.data.gwp))
    
    def __add__(self, other) -> float:
        if not isinstance(other, GHGGas):
            return NotImplemented
        if (self.data.name, self.data.gwp) == (other.data.name, other.data.gwp):
            return GHGGas(self.data.name, self.to_tonnes() + other.to_tonnes(), "tonne", \
                          self.data.desc, self.data.gwp, self.data.density)
        else:
            return NotImplemented

    def __sub__(self, other) -> float:
        if not isinstance(other, GHGGas):
            return NotImplemented
        if (self.data.name, self.data.gwp) == (other.data.name, other.data.gwp):
            return GHGGas(self.data.name, self.to_tonnes() - other.to_tonnes(), "tonne", \
                          self.data.desc, self.data.gwp, self.data.density)
        else:
            return NotImplemented
        
    def to_dict(self):
        return self.data.dict()
    
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
        return cls(data["name"], data["amount"], data["unit"], data["desc"], data["gwp"], data["density"])