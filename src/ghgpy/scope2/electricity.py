"""
GHG inventory - Scope2 - Electricity
Base on the IPCC 2006 w 2019 refinement
(c) Bui Khac Tu (bkt92)
"""

from pydantic import BaseModel
from typing import Optional, Dict
from src.ghgpy.datamodel.unumber import UNumber
from src.ghgpy.datamodel.unit_converters import weigh_units
from src.ghgpy.datamodel.electricity import Electricity
import logging

# Scope 2 electricity consumption
class ElecUse(BaseModel):
    """
    Electricity end-user
    """
    name: str = None
    desc: str = None
    elecuse: Dict[str, Electricity] = {}
    result: Optional[UNumber] = None
    process: Optional[str] = None

    def add(self, name, amount, unit, gef, desc= None, force=False):
        """
        Add new electricity use
        """
        if not force:
            if name in self.elecuse.keys():
                return f'{name} exist in list, using `force = True` to overwrite!'
            
        self.elecuse[name] = Electricity(name=name, amount=amount, unit=unit, gef=gef, desc=desc)
        return f'Added {name} to {self.name}'
    
    def remove(self, name):
        """
        Remove electricity use from the list
        """
        if name in self.elecuse.keys():
            self.elecuse.pop(name)
            self.elecuse.pop(name)
            return f'Removed {name} from {self.name}'
        else:
            return f'{name} not in the list'
        
    def emission(self, unit='t'):
        """
        Evaluate the activity for ghg emission
        """
        if len(self.elecuse) == 0:
            return "No electricity use in the list, please add some"
        else:
            emission = 0
            for ref in self.elecuse.values():
                emission += ref.emission()
        return weigh_units.convert(emission, 't', unit)