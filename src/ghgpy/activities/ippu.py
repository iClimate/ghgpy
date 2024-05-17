"""
GHG inventory for Industrial Processes and Product Use
Base on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""

from src.ghgpy.datamodel.unumber import UNumber
from src.ghgpy.datamodel.ghg import OtherGHG
from pydantic import BaseModel, Field
from src.ghgpy.datamodel.unit_converters import weigh_units
from typing import Optional, Dict
import logging


class RefrigerantUse(BaseModel):
    name: str = None
    desc: str = None
    refrigerant: Dict[str, OtherGHG] = {}
    result: Optional[UNumber] = None
    process: Optional[str] = None
    ghg_db: Optional[object] = Field(exclude=True)
    '''
    Calculate emission from: \n
    Refrigerant Use
    '''
    
    def add(self, name, amount, unit, ghg_db=None, force=False):
        """
        Add new refrigerant
        - Refrigerant
        - Required GHG database
        """
        if not force:
            if name in self.refrigerant.keys():
                return f'{name} exist in list, using `force = True` to overwrite!'
            
        if ghg_db == None:
            if self.ghg_db == None:
                logging.info("No db connection")
                return "No db connection"
            else:
                ghg_db = self.ghg_db
            
        self.refrigerant[name] = OtherGHG(name, amount, unit, ghg_db)
        return f'Added {name} to {self.name}'
    
    def remove(self, name):
        """
        Remove a refrigerant from the list
        """
        if name in self.refrigerant.keys():
            self.refrigerant.pop(name)
            self.refrigerant.pop(name)
            return f'Removed {name} from {self.name}'
        else:
            return f'{name} not in the list'
        
    def emission(self, unit='t'):
        """
        Evaluate the activity for ghg emission
        """
        if len(self.refrigerant) == 0:
            return "No refrigerant in the list, please add some"
        else:
            emission = 0
            for ref in self.refrigerant.values():
                emission += ref.emission()
        return weigh_units.convert(emission, 't', unit)