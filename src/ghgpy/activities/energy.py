"""
GHG inventory for Energy sector
Base on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""
from src.ghgpy.datamodel.fuel import BaseFuel
from src.ghgpy.datamodel.unumber import ufnum, UNumber
from src.ghgpy.datamodel.ghg import CO2, CH4, N2O, GHGGas
from src.ghgpy.datamodel.db import EFDataHandle, GHGDataHandle
from src.ghgpy.datamodel.unit_converters import weigh_units
import logging
from pydantic import BaseModel
from typing import List, Dict

# Activity data class
class ADCombussion(BaseModel):
    name: str = '' # Activity name
    desc: str = '' # More description
    fuels_list: Dict[str, BaseFuel] = {} # Fuel list in dict
    efs_list: Dict[str, Dict[str, UNumber]] = {} # Emission factors list in dict
    results: List[GHGGas] = [] # Emission of the 

class Combustion(ADCombussion):
    """
    Stationary combustion (SC)
    """
    #def __init__(self, **kwargs):
    #    super().__init__(**kwargs)

    def eval(self, database: GHGDataHandle):
        """
        Evaluate the activity for ghg emission
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
        Total emission in unit of CO2e
        """
        if self.results == None:
            logging.info("The emission data is not evaluated yet, eval now ...")
            return """The emission data is not evaluated yet! \n
                        Eval now with eval() function"""
        
        return weigh_units.convert(sum([x.emission() for x in self.results]), 't', unit)

    def add_fuel(self, fuel: BaseFuel, efdb: EFDataHandle, force=False):
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
        if name in self.fuels_list.keys():
            self.fuels_list.pop(name)
            self.efs_list.pop(name)
            return f'Removed {name}'
        else:
            return "Fuel not in the list"
        
    def list_fuels(self):
        return self.fuels_list.keys()
    
    @classmethod
    def load_data(cls, data):
        return cls(**data)


    