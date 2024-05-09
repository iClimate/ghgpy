"""
Fuel objects
Represent a amount of a specific fuel
"""
from data.unit_converters import *

class base_fuel:
    """
    Base Fuel Object
    amount unit: kg, g, tonne, m3, litre
    """
    # Init attributes of fuel
    def __init__(self, name: str, desc: str, ncv: float, ccf: float, density: float, amount: float, unit: str):
        self.name = name # Name of fuel
        self.desc = desc # More information about fuel
        self.ncv = ncv # Tj/Gg
        self.ccf = ccf # Carbon content of fuel
        self.density = density # kg/m3
        self.amount = amount # amount of fuel
        self.unit = unit # unit of fuel

    # Validate unit
    def _unit_val(self, unit):
        if not ((unit in weigh_units.units) or (unit in volume_units.units)):
            raise ValueError("Invalid Unit.")

    # Convert to TJ
    def _to_tj(self):
        '''
        Energy of Fuel
        '''
        if self.unit in weigh_units.units:
            return weigh_units.convert(self.amount, self.unit, 'Gg')*self.ncv
        if self.unit in volume_units.units:
            return weigh_units.convert(volume_units.convert(self.amount, self.unit, 'm3')*self.density, 'kg', 'Gg')*self.ncv
        
    # Convert to kg
    def _to_kg(self):
        '''
        Energy of Fuel
        '''
        if self.unit in weigh_units.units:
            return weigh_units.convert(self.amount, self.unit, 'kg')
        if self.unit in volume_units.units:
            return volume_units.convert(self.amount, self.unit, 'm3')*self.density
        
    def _check_fuel(self, other):
        if not isinstance(other, base_fuel):
            return NotImplemented
        if (self.name, self.desc, self.ncv, self.density) == (other.name, other.desc, other.ncv, other.density):
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return (
            'fuel('
            f'name={self.name!r}, amount={self._to_tj()!r} Tj)'
        )

    def __hash__(self) -> int:
        return hash((self.name, self.desc, self._to_tj(), self.ncv))

    def __eq__(self, other) -> bool:
        if not isinstance(other, base_fuel):
            return NotImplemented
        return (
            (self.name, self._to_tj(), self.ncv) == 
            (other.name, other._to_tj(), other.ncv))
    
    def __add__(self, other) -> float:
        if not isinstance(other, base_fuel):
            return NotImplemented
        if self._check_fuel(other):
            return base_fuel(self.name, self.desc, self.ncv, self.ccf, self.density,\
                             self._to_kg()+other._to_kg(), "kg")
        else:
            return NotImplemented

    def __sub__(self, other) -> float:
        if not isinstance(other, base_fuel):
            return NotImplemented
        if self._check_fuel(other):
            return base_fuel(self.name, self.desc, self.ncv, self.ccf, self.density,\
                             self._to_kg()+other._to_kg(), "kg")
        else:
            return NotImplemented

        
class DO(base_fuel):
    '''
    `amount: amount of fuel`\n
    `unit: unit of fuel`

    -------------
    Data Sources: \n
    Calorific value: 2006 IPCC Guidelines for National Greenhouse Gas Inventories V2_Ch1 - TABLE 1.2:
    https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/2_Volume2/V2_1_Ch1_Introduction.pdf\n
    Density: IEA Database documentation:
    https://wds.iea.org/wds/pdf/oil_documentation.pdf\n

    '''
    def __init__(self, amount, unit):
        super().__init__('DO', 'Gas/Diesel Oil', 43.0, 20.2, 844, amount, unit)

class DO(base_fuel):
    '''
    `amount: amount of fuel`\n
    `unit: unit of fuel`

    -------------
    Data Sources: \n
    Calorific value and Carbon content (ccf): 2006 IPCC Guidelines for National Greenhouse Gas Inventories V2_Ch1 - TABLE 1.2:
    https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/2_Volume2/V2_1_Ch1_Introduction.pdf\n
    Density: IEA Database documentation:
    https://wds.iea.org/wds/pdf/oil_documentation.pdf\n

    '''
    def __init__(self, amount, unit):
        super().__init__('DO', 'Gas/Diesel Oil', 43.0, 20.2, 844, amount, unit)

