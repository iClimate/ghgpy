"""
iClimate - ghgpy

Fuel objects
Represent a amount of a specific fuel
(C) Bui Khac Tu (bkt92)
(C) iClimate
"""

from .unit_converters import *
from .unumber import UNumber, ufnum
from typing import Optional
from pydantic import BaseModel
from src.ghgpy.datamodel.db import FuelDataHandle

# Data model for properties 
class FuelProperties(BaseModel):
    desc: Optional[str] = None # More information about fuel
    ncv: Optional[UNumber] = None # Net calorific value (Tj/Gg)
    ccf: Optional[UNumber] = None # Carbon content of fuel (tonne/TJ, kg/Gj)
    density: Optional[UNumber] = None # Density (kg/m3)

# Data model for Fuel data
class FuelData(BaseModel):
    name: str = None # Name/code of fuel
    amount: UNumber = None # amount of fuel
    unit: str = None # unit of fuel
    properties: Optional[FuelProperties] = None

class BaseFuel(FuelData):
    """
    Base Fuel Object (use for all kind of fuel) \n
    Representative by TJ \n
    Allow "+, -" operators with the same kind of fuel \n
    Allow convert to different property (Weight, Volume, Carbon Content)
    """
    # Init attributes of fuel
    #def __init__(self, **kwargs):
    #    super().__init__(**kwargs)

    # Validate unit
    def _is_valid_unit(self, unit):
        if not ((unit in weigh_units.units) or (unit in volume_units.units)):
            raise ValueError("Invalid Unit.")
        return unit

    # Convert to TJ
    def cal_energy(self, unit='tj'):
        '''
        Energy of Fuel in unit \n
        Default unit `Tj`
        '''
        if any(x == None for x in [self.amount, self.properties.ncv]):
            return None
        amount = self.amount.to_ufnum()
        ncv = self.properties.ncv.to_ufnum()
        if self.unit in weigh_units.units:
            energy = weigh_units.convert(amount, self.unit, 'Gg')*ncv
            return energy_units.convert(energy, 'tj', unit)
        if self.unit in volume_units.units:
            if self.properties.density == None:
                return None
            else:
                density = self.properties.density.to_ufnum()
                energy = weigh_units.convert(volume_units.convert(amount, self.unit, 'm3')\
                                           *density, 'kg', 'Gg')*ncv
                return energy_units.convert(energy, 'tj', unit)
        
    # Convert to kg
    def cal_weight(self, unit='kg'):
        '''
        Weight of Fuel in unit \n
        Unit default `kg`
        '''
        amount = self.amount.to_ufnum()
        if self.unit in weigh_units.units:
            return weigh_units.convert(amount, self.unit, unit)
        if self.unit in volume_units.units:
            if self.properties.density == None:
                return None
            else:
                density = self.properties.density.to_ufnum()
                weight = volume_units.convert(amount, self.unit, 'm3')*density
                return weigh_units.convert(weight, 'kg', unit)
        
    # Convert carbon content (kg)
    def calc_cc(self, unit='kg'):
        '''
        Carbon content of Fuel in unit \n
        Default unit `kg`
        '''
        if self.properties.ccf == None:
            return None
        else:
            ccf = self.properties.ccf.to_ufnum()
            return weigh_units.convert(1000*self.cal_energy()*ccf, 'kg', unit)

    # Convert to volume (litre)
    def cal_volume(self, unit='l'):
        '''
        Volume of Fuel in unit \n
        Default unit `litre`
        '''
        amount = self.amount.to_ufnum()
        if self.unit in weigh_units.units:
            if self.properties.density == None:
                return None
            else:
                density = self.properties.density.to_ufnum()
                volume = weigh_units.convert(amount, self.unit, 'kg')/density
                return volume_units.convert(volume, 'm3', unit)
        if self.unit in volume_units.units:
            return volume_units.convert(amount, self.unit, unit)
    
    # Check two object have enough fuel data
    def _check_fuel(self, other):
        if not isinstance(other, BaseFuel):
            return NotImplemented
        if (self.name, self.properties.desc, self.properties.ncv, self.properties.density) == \
            (other.name, other.properties.desc, other.properties.ncv, other.properties.density):
            return True
        else:
            return False
    
    # Convert data to dict
    def to_dict(self, properties = True):
        if properties:
            return self.dict()
        else:
            data = self.dict()
            data.pop("properties")
            return data
    
    # Return to tj (energy of fuel)
    def __repr__(self) -> str:
        return (
            'fuel('
            f'name={self.name!r}, amount={self.cal_energy()!r} Tj)'
        )

    def __hash__(self) -> int:
        return hash((self.name, self.properties.desc, self.cal_energy(), self.properties.ncv))

    def __eq__(self, other) -> bool:
        if not isinstance(other, BaseFuel):
            return NotImplemented
        return (
            (self.name, self.cal_energy(), self.properties.ncv) == 
            (other.name, other.cal_energy(), other.properties.ncv))
    
    def __add__(self, other) -> float:
        if not isinstance(other, BaseFuel):
            return NotImplemented
        if self._check_fuel(other):
            sum = self.cal_weight()+other.cal_weight()
            amount = ufnum(sum.value, sum.uncertainty)
            return BaseFuel(self.name, self.properties.desc, self.properties.ncv.to_ufnum(), \
                            self.properties.ccf.to_ufnum(), self.properties.density.to_ufnum(), amount, "kg")    
        else:
            return NotImplemented

    def __sub__(self, other) -> float:
        if not isinstance(other, BaseFuel):
            return NotImplemented
        if self._check_fuel(other):
            sub = self.cal_weight()-other.cal_weight()
            amount = ufnum(sub.value, sub.uncertainty)
            return BaseFuel(self.name, self.properties.desc, self.properties.ncv.to_ufnum(), \
                            self.properties.ccf.to_ufnum(), self.properties.density.to_ufnum(), amount, "kg")    
        else:
            return NotImplemented
    
    # Load fuel from json file
    @classmethod
    def from_dict(cls, data):
        '''
        Load json file to fuel class
        schema:
        { 
        name: Name/code of fuel,
        amount: Amount of fuel (unit),
        unit: Unit of amount fuel,
        properties:
            {
            desc: More information about fuel
            ncv: Net calorific value (Tj/Gg)
            ccf: Carbon content of fuel (kg/GJ)
            density: Density of fuel (kg/m3)
            }
        }
        '''
        return cls(**data)                

# Class with default fuel database        
class DefaultFuel(BaseFuel):
    '''
    `amount: amount of fuel`\n
    `unit: unit of fuel`

    -------------
    Data Sources: \n
    Calorific value: 2006 IPCC Guidelines for National Greenhouse Gas Inventories V2_Ch1 - TABLE 1.2:
    https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/2_Volume2/V2_1_Ch1_Introduction.pdf \n
    Density: IEA Database documentation:
    https://wds.iea.org/wds/pdf/oil_documentation.pdf \n

    '''
    def __init__(self, database :FuelDataHandle, fuel: str, amount: UNumber, unit: str):
        if not database.check_exist(fuel):
            raise ValueError("Fuel not found in database.")
        
        properties = FuelProperties(**database.get(fuel))
        super().__init__(**{"name": fuel, "amount": amount, "unit": unit, "properties": properties})
    
    # Load fuel from json file
    @classmethod
    def from_json(cls, database, data):
        '''
        Load json file to fuel class
        Schema:
        { 
        name: Name/code of fuel,
        amount: amount of fuel (unit),
        unit: unit of amount fuel
        }
        '''
        if not database.check_exist(data["name"]):
            raise ValueError("Fuel not found in database.")
        return cls(database, data["name"], data["amount"],  data["unit"])

def dict_to_fuel(data, database):
    '''
    Schema: Class FuelData

    Load json file to fuel class
    schema:
    { 
    name: Name/code of fuel,
    amount: Amount of fuel (unit),
    unit: Unit of amount fuel,
    properties:
        {
        desc: More information about fuel
        ncv: Net calorific value (Tj/Gg)
        ccf: Carbon content of fuel (kg/GJ)
        density: Density of fuel (kg/m3)
        }
    }
    '''
    _required_data = ['name', 'amount', 'unit']
    _attributes_list = set(['desc', 'ncv', 'ccf', 'density'])

    if not all(x in data.keys() for x in _required_data):
        raise ValueError("Invalid data, missing fields!")
    
    elif not "properties" in data.keys():
        if not data["name"] in database.keys():
            raise ValueError("Invalid data, fuel name not found in default fuel list!")
        else:
            fuel = data["name"]
            return DefaultFuel(database, data["name"], ufnum.from_dict(data["amount"]),  data["unit"])
    else:
        if all(x in data["properties"].keys() for x in _attributes_list):
            return BaseFuel(data["name"], data["properties"]['desc'], ufnum.from_dict(data["properties"]['ncv']), \
                        ufnum.from_dict(data["properties"]['ccf']), ufnum.from_dict(data["properties"]['density']), \
                            ufnum.from_dict(data["amount"]), data["unit"])                
        elif not data["name"] in database.keys():
            raise ValueError("Invalid data, missing atribute which can not get from default fuel list!")
        else:
            fuel = data["name"]
            input = {}
            for i in _attributes_list.difference(data["properties"].keys()):
                input[i] = database.get(fuel)[i]
            for i in data["properties"].keys():
                input[i] = data["properties"][i]
            return BaseFuel(data["name"], input['desc'], ufnum.from_dict(input['ncv']), \
                        ufnum.from_dict(input['ccf']), ufnum.from_dict(input['density']), \
                            ufnum.from_dict(data["amount"]),  data["unit"])