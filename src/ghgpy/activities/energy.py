"""
GHG inventory for Energy sector
Base on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""
from src.ghgpy.datamodel.fuel import BaseFuel, DefaultFuel
from src.ghgpy.datamodel.unumber import ufnum, UNumber
from src.ghgpy.datamodel.ghg import CO2, CH4, N2O, GHGGas
from src.ghgpy.datamodel.unit_converters import weigh_units
import logging
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

# Activity data class
class ADCombussion(BaseModel):
    name: str = '' # Activity name
    desc: str = '' # More description
    fuels_list: Dict[str, BaseFuel] = {} # Fuel list in dict
    efs_list: Dict[str, Dict[str, UNumber]] = {} # Emission factors list in dict
    results: List[GHGGas] = [] # Emission of the 
    fuel_db: Optional[object] = Field(exclude=True)
    ghg_db: Optional[object] = Field(exclude=True)
    ef_db: Optional[object] = Field(exclude=True)

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
    def connection(self, fuel_db, ef_db, ghg_db):
        self.fuel_db = fuel_db
        self.ef_db = ef_db
        self.ghg_db = ghg_db

    def eval(self):
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
            co2 = CO2(ufnum(co2v).to_unum(), 'kg', self.ghg_db)
            ch4 = CH4(ufnum(ch4v).to_unum(), 'kg', self.ghg_db)
            n2o = N2O(ufnum(n2ov).to_unum(), 'kg', self.ghg_db)
        self.results = [co2, ch4, n2o]
        return self.results
    
    def emission(self, unit='t'):
        """
        Total emission in unit of CO2e (`Default in metric tonnes`)
        """
        self.eval()
        return weigh_units.convert(sum([x.emission() for x in self.results]), 't', unit)

    def add(self, name, amount, unit, fuel_db=None, efdb=None, force=False):
        """
        Add a fuel to fuels list 
        - Required database for emission factors
        - Required fuel class (datamodel)
        - `force` = True: Overwrite existing fuel data

        """
        if efdb == None:
            if self.ef_db == None:
                logging.info("No db connection")
                return "No db connection"
            else:
                efdb = self.ef_db
        if fuel_db == None:
            if self.fuel_db == None:
                logging.info("No db connection")
            else:
                fuel_db = self.fuel_db

        if not force:
            if name in self.fuels_list.keys():
                return f'{name} exist in list, using `force = True` to overwrite!'
        if not efdb.check_exist(name):
            raise ValueError(f'{name} not found in database.')
        efco2 = UNumber(**efdb.get(name)["co2"])
        efch4 = UNumber(**efdb.get(name)["ch4"])
        efn2o = UNumber(**efdb.get(name)["n2o"])
        self.fuels_list[name] = DefaultFuel(name, amount, unit, fuel_db)
        self.efs_list[name] = {'co2': efco2, 'ch4': efch4, 'n2o': efn2o}
        return f'Added {name} to {self.name}'
    
    def add_custom(self, fuel_data, ef_data, force=False):
        """
        Add a custom fuel to fuels list with custom data
        fuel_data = {
            'name': 'Diesel_Oil',
            'amount': {'value': 1000.0, 'uncertainty': 0},
            'unit': 'l',
            'properties': {
                'desc': 'Gas/Diesel Oil',
                'ncv': {'value': 43.0, 'uncertainty': 0.0},
                'ccf': {'value': 20.2, 'uncertainty': 0.4},
                'density': {'value': 844.0, 'uncertainty': 0.0}}}

        ef_data = {
            "co2": {"value": 54600,
                    "uncertainty": 0
                    },
            "ch4": {"value": 1,
                    "uncertainty": 0
                    },
            "n2o": {"value": 0.1,
                    "uncertainty": 0}
        """
        if not force:
            if fuel_data["name"] in self.fuels_list.keys():
                return f'{fuel_data["name"]} exist in list, using `force = True` to overwrite!'
            
        efco2 = UNumber(**ef_data["co2"])
        efch4 = UNumber(**ef_data["ch4"])
        efn2o = UNumber(**ef_data["n2o"])
        self.fuels_list[fuel_data["name"]] = BaseFuel(**fuel_data)
        self.efs_list[fuel_data["name"]] = {'co2': efco2, 'ch4': efch4, 'n2o': efn2o}
        return f'Added {fuel_data["name"]} to {self.name}'
    
    def remove(self, name: str):
        """
        Remove a fuel from the list\n
        Use list_fuels() method to check the list
        """
        if name in self.fuels_list.keys():
            self.fuels_list.pop(name)
            self.efs_list.pop(name)
            return f'Removed {name} from {self.name}'
        else:
            return f'{name} not in the list'
        
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