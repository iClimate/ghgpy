"""
iClimate - ghgpy

Factory objects
Represent a factory which doing ghg inventory

(C) Bui Khac Tu (bkt92)
(C) iClimate
"""

from src.ghgpy.activities.energy import Combustion
from src.ghgpy.scope2.electricity import ElecUse
from src.ghgpy.activities.ippu import RefrigerantUse
import logging
from pydantic import BaseModel, Extra, Field
from typing import Dict, Optional

# Factory data in one year
class FactoryGeneral(BaseModel, extra=Extra.allow):
    name: Optional[str] = None # name of factory
    desc: Optional[str] = None # factory description
    # Scope 1 emission
    combustion: Dict[str, Combustion] = {} # Stationary combustion
    refrigerantuse: Dict[str, RefrigerantUse] = {} # Product use emission
    # Scope 2 emission
    elecuse: Dict[str, ElecUse] = {} # Indirect emission by using electricity
    # Scope 3 emission not implement yet
    fuel_db: Optional[object] = Field(exclude=True)
    ghg_db: Optional[object] = Field(exclude=True)
    ef_db: Optional[object] = Field(exclude=True)

    def connection(self, fuel_db, ef_db, ghg_db):
        self.fuel_db = fuel_db
        self.ef_db = ef_db
        self.ghg_db = ghg_db

    def add_combustion(self, name, desc: str = None, force=False):
        """
        Add a combussion process
        - `force` = True: Overwrite existing fuel data
        """
        if not force:
            if name in self.combustion.keys():
                return "The process already exist in the list, using `force = True` to overwrite!" 
        self.combustion[name] = Combustion(name=name, desc=desc, fuel_db=self.fuel_db, \
                                           ef_db=self.ef_db, ghg_db=self.ghg_db)
        return f'Added {name} to {self.name}'
    
    def remove_combustion(self, name: str):
        """
        Remove a combussion process\n
        """
        if name in self.combustion.keys():
            self.combustion.pop(name)
            return f'Removed {name} from {self.name}'
        else:
            f'{name} not in the list'
        
    def add_refrigerantuse(self, name, desc=None, process=None, force=False):
        """
        Add a emission from refrigerant
        - `force` = True: Overwrite existing fuel data
        """
        if not force:
            if name in self.refrigerantuse.keys():
                return "Already exist in the list, using `force = True` to overwrite!" 
        self.refrigerantuse[name] = RefrigerantUse(name=name, desc=desc, process=process, ghg_db=self.ghg_db)
        return f'Added {name} to {self.name}'
    
    def remove_refrigerantuse(self, name: str):
        """
        Remove emission from refrigerant\n
        """
        if name in self.refrigerantuse.keys():
            self.refrigerantuse.pop(name)
            return f'Removed {name} from {self.name}'
        else:
            return f'{name} not in the list'

    def add_elecuse(self, name, desc: str = None, process=None, force=False):
        """
        Add a electriciy end-users
        - `force` = True: Overwrite existing fuel data
        """
        if not force:
            if name in self.elecuse.keys():
                return "The end-users already exist in the list, using `force = True` to overwrite!" 
        self.elecuse[name] = ElecUse(name=name, desc=desc, process=process)
        return f'Added {name} to {self.name}'
    
    def remove_elecuse(self, name: str):
        """
        Remove a electriciy end-users
        """
        if name in self.elecuse.keys():
            self.elecuse.pop(name)
            return f'Removed {name} from {self.name}'
        else:
            f'{name} not in the list'
        
    def emission(self, scope=1):
        if scope == 1:
            emission = 0
            for process in self.combustion.values():
                emission += process.emission()
            for ref in self.refrigerantuse.values():
                emission += ref.emission()
            return emission
        if scope == 2:
            emission = 0
            for e in self.elecuse.values():
                emission += e.emission()
            return emission
    
    @classmethod
    def load_data(cls, data):
        """
        Load data to the class
        """
        return cls(**data) 

# Store historial factory data
class FHistory(BaseModel):
    hist: Dict[int, FactoryGeneral] = None



