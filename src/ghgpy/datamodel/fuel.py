"""
iClimate - ghgpy

Fuel objects
Represent a amount of a specific fuel
(C) Bui Khac Tu (bkt92)
(C) iClimate
"""

from .unit_converters import *
from typing import Optional
from pydantic import BaseModel
from uncertainty.utypes import ufloat

# Data model, if include uncertainly in the data -> represent by tuple (value, uncertainty)
class FuelProperties(BaseModel):
    desc: Optional[str] = None # More information about fuel
    ncv: Optional[float | tuple[float, float]] = None # Net calorific value (Tj/Gg)
    ccf: Optional[float| tuple[float, float]] = None # Carbon content of fuel (tonne/TJ, kg/Gj)
    density: Optional[float | tuple[float, float]] = None # Density (kg/m3)

class FuelData(BaseModel):
    name: str = None # Name/code of fuel
    amount: float | tuple[float, float] = None # amount of fuel
    unit: str = None # unit of fuel
    properties: Optional[FuelProperties] = None

class BaseFuel:
    """
    Base Fuel Object (use for all kind of fuel) \n
    Representative by TJ \n
    Allow "+, -" operators with the same kind of fuel \n
    Allow convert to different property (Weight, Volume, Carbon Content)
    """
    # Init attributes of fuel
    def __init__(self, name: str, desc: str, ncv: float, ccf: float, \
                 density: float, amount: float, unit: str):
        
        properties = FuelProperties(desc=desc, ncv=ncv, ccf=ccf, density=density)
        self.data = FuelData(name=name, amount=amount, unit=self._is_valid_unit(unit), properties=properties)

    # Validate unit
    def _is_valid_unit(self, unit):
        if not ((unit in weigh_units.units) or (unit in volume_units.units)):
            raise ValueError("Invalid Unit.")
        return unit

    # Convert to TJ
    def to_tj(self):
        '''
        Energy of Fuel
        '''
        if any(x == None for x in [self.data.amount, self.data.properties.ncv]):
            return None
        if type(self.data.amount) == tuple:
            amount = ufloat(self.data.amount)
        else:
            amount = self.data.amount
        if type(self.data.properties.ncv) == tuple:
            ncv = ufloat(self.data.properties.ncv)
        else:
            ncv = self.data.properties.ncv
        if self.data.unit in weigh_units.units:
            return weigh_units.convert(amount, self.data.unit, 'Gg')*ncv
        if self.data.unit in volume_units.units:
            if self.data.properties.density == None:
                return None
            else:
                if type(self.data.properties.density) == tuple:
                    density = ufloat(self.data.properties.density)
                else:
                    density = self.data.properties.density
                return weigh_units.convert(volume_units.convert(amount, self.data.unit, 'm3')\
                                           *density, 'kg', 'Gg')*ncv
        
    # Convert to kg
    def to_kg(self):
        '''
        Weight of Fuel
        '''
        if type(self.data.amount) == tuple:
            amount = ufloat(self.data.amount)
        else:
            amount = self.data.amount       
        if self.data.unit in weigh_units.units:
            return weigh_units.convert(amount, self.data.unit, 'kg')
        if self.data.unit in volume_units.units:
            if self.data.properties.density == None:
                return None
            else:
                if type(self.data.properties.density) == tuple:
                    density = ufloat(self.data.properties.density)
                else:
                    density = self.data.properties.density
                return volume_units.convert(amount, self.data.unit, 'm3')*density
        
    # Convert carbon content (kg)
    def to_cc(self):
        '''
        Carbon content of Fuel
        '''
        if self.data.properties.ccf == None:
            return None
        else:
            if type(self.data.properties.ccf) == tuple:
                ccf = ufloat(self.data.properties.ccf)
            else:
                ccf = self.data.properties.ccf
            return 1000*self.to_tj()*ccf

    # Convert to volume (litre)
    def to_litre(self):
        '''
        Volume of Fuel
        '''
        if type(self.data.amount) == tuple:
            amount = ufloat(self.data.amount)
        else:
            amount = self.data.amount
        if self.data.unit in weigh_units.units:
            if self.data.properties.density == None:
                return None
            else:
                if type(self.data.properties.density) == tuple:
                    density = ufloat(self.data.properties.density)
                else:
                    density = self.data.properties.density
                return 1000*weigh_units.convert(amount, self.data.unit, 'kg')/density
        if self.data.unit in volume_units.units:
            return volume_units.convert(amount, self.data.unit, 'litre')
    
    # Check two object have enough fuel data
    def _check_fuel(self, other):
        if not isinstance(other, BaseFuel):
            return NotImplemented
        if (self.data.name, self.data.properties.desc, self.data.properties.ncv, self.data.properties.density) == \
            (other.data.name, other.data.properties.desc, other.data.properties.ncv, other.data.properties.density):
            return True
        else:
            return False
    
    # Convert data to dict
    def to_dict(self, properties = True):
        if properties:
            return self.data.dict()
        else:
            data = self.data.dict()
            data.pop("properties")
            return data
    
    # Return to tj (energy of fuel)
    def __repr__(self) -> str:
        return (
            'fuel('
            f'name={self.data.name!r}, amount={self.to_tj()!r} Tj)'
        )

    def __hash__(self) -> int:
        return hash((self.data.name, self.data.properties.desc, self.to_tj(), self.data.properties.ncv))

    def __eq__(self, other) -> bool:
        if not isinstance(other, BaseFuel):
            return NotImplemented
        return (
            (self.data.name, self.to_tj(), self.data.properties.ncv) == 
            (other.data.name, other.to_tj(), other.data.properties.ncv))
    
    def __add__(self, other) -> float:
        if not isinstance(other, BaseFuel):
            return NotImplemented
        if self._check_fuel(other):
            if type(self.to_kg()) == ufloat:
                amount = self.to_kg()+other.to_kg()
                return BaseFuel(self.data.name, self.data.properties.desc, self.data.properties.ncv, self.data.properties.ccf, \
                                self.data.properties.density, (amount.value, amount.uncertainty) , "kg")
            else:
                return BaseFuel(self.data.name, self.data.properties.desc, self.data.properties.ncv, self.data.properties.ccf, \
                                self.data.properties.density, self.to_kg()+other.to_kg(), "kg")
        else:
            return NotImplemented

    def __sub__(self, other) -> float:
        if not isinstance(other, BaseFuel):
            return NotImplemented
        if self._check_fuel(other):
            if type(self.to_kg()) == ufloat:
                amount = self.to_kg()-other.to_kg()
                return BaseFuel(self.data.name, self.data.properties.desc, self.data.properties.ncv, self.data.properties.ccf, \
                                self.data.properties.density, (amount.value, amount.uncertainty) , "kg")
            else:
                return BaseFuel(self.data.name, self.data.properties.desc, self.data.properties.ncv, self.data.properties.ccf, \
                                self.data.properties.density, self.to_kg()-other.to_kg(), "kg")
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
        return cls(data["name"], data["properties"]['desc'], data["properties"]['ncv'], \
                            data["properties"]['ccf'], data["properties"]['density'], data["amount"], data["unit"])                

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
    def __init__(self, database, fuel, amount, unit):
        if fuel not in database.keys():
            raise ValueError("Invalid Unit.")
        
        super().__init__(fuel, database[fuel]['desc'], database[fuel]['ncv'], \
                         database[fuel]['ccf'], database[fuel]['density'], amount, unit)
    
    # Load fuel from json file
    @classmethod
    def from_json(cls, data):
        '''
        Load json file to fuel class
        Schema:
        { 
        name: Name/code of fuel,
        amount: amount of fuel (unit),
        unit: unit of amount fuel
        }
        '''
        return cls(data["name"], data["amount"],  data["unit"])

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
        
        elif not "custom" in data.keys():
            if not data["name"] in database.keys():
                raise ValueError("Invalid data, fuel name not found in default fuel list!")
            else:
                fuel = data["name"]
                return DefaultFuel(data["name"], data["amount"],  data["unit"])
        else:
            if all(x in data["custom"].keys() for x in _attributes_list):
                return BaseFuel(data["name"], data["custom"]['desc'], data["custom"]['ncv'], \
                            data["custom"]['ccf'], data["custom"]['density'], data["amount"], data["unit"])                
            elif not data["name"] in database.keys():
                raise ValueError("Invalid data, missing atribute which can not get from default fuel list!")
            else:
                fuel = data["name"]
                input = {}
                for i in _attributes_list.difference(data["custom"].keys()):
                    input[i] = database[fuel][i]
                for i in data["custom"].keys():
                    input[i] = data["custom"][i]
                return BaseFuel(data["name"], input['desc'], input['ncv'], \
                            input['ccf'], input['density'], data["amount"],  data["unit"])