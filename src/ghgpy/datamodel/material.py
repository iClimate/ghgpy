"""
iClimate - ghgpy

Material objects
Represent a amount of a specific material/product and it's property

(C) Bui Khac Tu (bkt92)
(C) iClimate
"""

from pydantic import BaseModel
from src.ghgpy.datamodel.unumber import UNumber
from typing import List, Dict, Optional

class Material(BaseModel):
    '''
    `name`: name of product/ material use
    `desc`: more description about the product
    `amount`: amount of product in unit
    `unit`: unit of product    
    '''
    name: str = None
    desc: str = None
    amount: UNumber = None
    unit: str = None
    properties: Optional[dict] = None