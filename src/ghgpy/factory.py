"""
iClimate - ghgpy

Factory objects
Represent a factory which doing ghg inventory

(C) Bui Khac Tu (bkt92)
(C) iClimate
"""

from src.ghgpy.activities.energy import Combustion, ElecUse
from src.ghgpy.datamodel.fuel import BaseFuel
import logging
from pydantic import BaseModel
from typing import List, Dict, Optional

# Factory data in one year
class FactoryData(BaseModel):
    name: Optional[str] = None # name of factory
    desc: Optional[str] = None # factory description
    # Scope 1 emission
    scombustion: Dict[str, Combustion] = {} # Stationary combustion
    mcombustion: Dict[str, Combustion] = {} # Mobile combustion
    iprocess: dict = {} # Industrial process
    fugitive: dict = {} # Fugitive emission
    productuse: dict = {} # Product use emission
    # Scope 2 emission
    elecuse: ElecUse # Indirect emission by using electricity
    steamuse: None # Indirect emission by using stearm
    heatuse: None # Indirect emission by using heat/cooling
    # Scope 3 emission not implement yet

# Store historial factory data
class FHistory(BaseModel):
    hist: Dict[int, FactoryData] = {}



