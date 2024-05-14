"""
GHG inventory for Energy sector
Base on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""
from src.ghgpy.datamodel.fuel import BaseFuel
from src.ghgpy.datamodel.unumber import ufnum, UNumber
from src.ghgpy.datamodel.ghg import CO2, CH4, N2O, GHGGas
from src.ghgpy.datamodel.db import EFDataHandle, GHGDataHandle
from src.ghgpy.datamodel.unit_converters import weigh_units, energy_units
import logging
from pydantic import BaseModel
from typing import List, Dict, Optional

# Activity data class
class ADCombussion(BaseModel):
    name: str = '' # Activity name
    desc: str = '' # More description
    fuels_list: Dict[str, BaseFuel] = {} # Fuel list in dict
    efs_list: Dict[str, Dict[str, UNumber]] = {} # Emission factors list in dict
    results: List[GHGGas] = [] # Emission of the 

# Scope 1 combussion
class Combustion(ADCombussion):
    """
    Stationary combustion (SC)
    `name`: Activity name
    `desc`: More description
    `fuels_list`: Fuel list
    `efs_list`: List of emission factor corresponding to fuels
    `results`: Emission evaluation result <not input>
    """
    #def __init__(self, **kwargs):
    #    super().__init__(**kwargs)

    def eval(self, database: GHGDataHandle):
        """
        Evaluate the activity for ghg emission
        - Current GHG: CO2, CH4 and N2O
        - Required GHG database
        - Return a list of GHG emission from this activity
        """
        if len(self.fuels_list) == 0:
            return "No fuel in this activity, please add some fuels"
        else:
            co2v, ch4v, n2ov = 0, 0, 0
            for key, fuel in self.fuels_list.items():
                energy = fuel.cal_energy()
                co2v += energy*self.efs_list[key]['co2'].to_ufnum()
                ch4v += energy*self.efs_list[key]['ch4'].to_ufnum()
                n2ov += energy*self.efs_list[key]['n2o'].to_ufnum()
            co2 = CO2(ufnum(co2v).to_unum(), 'kg', database)
            ch4 = CH4(ufnum(ch4v).to_unum(), 'kg', database)
            n2o = N2O(ufnum(n2ov).to_unum(), 'kg', database)
        self.results = [co2, ch4, n2o]
        return self.results
    
    def emission(self, unit='t'):
        """
        Total emission in unit of CO2e (`Default in metric tonnes`)
        """
        if self.results == None:
            logging.info("The emission data is not evaluated yet, eval now ...")
            return """The emission data is not evaluated yet! \n
                        Eval now with eval() function"""
        
        return weigh_units.convert(sum([x.emission() for x in self.results]), 't', unit)

    def add_fuel(self, fuel: BaseFuel, efdb: EFDataHandle, force=False):
        """
        Add a fuel to fuels list of combussion class 
        - Required database for emission factors
        - Required fuel class (datamodel)
        - `force` = True: Overwrite existing fuel data

        """
        if not force:
            if fuel.name in self.fuels_list.keys():
                return "Fuel exist in database, using `force = True` to overwrite!"
        if not efdb.check_exist(fuel.name):
            raise ValueError("Fuel not found in database.")
        efco2 = UNumber(**efdb.get(fuel.name)["co2"])
        efch4 = UNumber(**efdb.get(fuel.name)["ch4"])
        efn2o = UNumber(**efdb.get(fuel.name)["n2o"])
        self.fuels_list[fuel.name] = fuel
        self.efs_list[fuel.name] = {'co2': efco2, 'ch4': efch4, 'n2o': efn2o}
        return f'Added {fuel.name}'
    
    def remove_fuel(self, name: str):
        """
        Remote a fuel from the list\n
        Use list_fuels() method to check the list
        """
        if name in self.fuels_list.keys():
            self.fuels_list.pop(name)
            self.efs_list.pop(name)
            return f'Removed {name}'
        else:
            return "Fuel not in the list"
        
    def list_fuels(self):
        """
        List all fuels in the combustion class
        """
        return self.fuels_list.keys()
    
    @classmethod
    def load_data(cls, data):
        """
        Load data to the class
        """
        return cls(**data)

# Scope 2 electricity consumption
class ElecUse(BaseModel):
    """
    Electricity use data class\n
    `consumption`: power consumption in unit 
    `unit`: unit of power 
    `year`: [optional] year of power consumption 
    `location`: [optional] location of end-user 
    `gef`: git emission factor (in year)
    """
    consumption: UNumber = None
    unit: str = None
    year: Optional[int] = None
    location: Optional[str] = None
    gef: UNumber = None # tCO2e/MWh

    def emission(self, unit='tonne'):
        energy = energy_units.convert(self.consumption.to_ufnum(), self.unit, 'MWh')
        return weigh_units.convert(energy*self.gef.to_ufnum(), 'tonne', unit)


    