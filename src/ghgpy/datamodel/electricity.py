"""
Electricity Data Class
Base on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""
from pydantic import BaseModel
from typing import Optional
from src.ghgpy.datamodel.unumber import UNumber
from src.ghgpy.datamodel.unit_converters import weigh_units, energy_units

class Electricity(BaseModel):
    """
    Electricity use data class\n
    `amount`: power consumption in unit 
    `unit`: unit of power 
    `process`: [optional] proceess / section associated with electricity use
    `desc`: [optional] More description / notes
    `gef`: git emission factor tCO2e/MWh (in year)
    """
    name: Optional[str] = None
    amount: UNumber = None
    unit: str = None
    process: Optional[str] = None
    desc: Optional[str] = None
    gef: UNumber = None # tCO2e/MWh

    def emission(self, unit='tonne'):
        energy = energy_units.convert(self.amount.to_ufnum(), self.unit, 'MWh')
        return weigh_units.convert(energy*self.gef.to_ufnum(), 'tonne', unit)