"""
iClimate - ghgpy
Uncertainty represent, the module for uncertainty number type use in the ghgpy
(C) Bui Khac Tu (bkt92)
(C) iClimate
"""

from uncertainty.utypes import ufloat
from pydantic import BaseModel
from typing import Optional

# Data model for number with uncertainty 
class UNumber(BaseModel):
    value: float
    uncertainty: Optional[float] = 0
    def to_ufnum(self):
        return ufnum(self.value, self.uncertainty)

# Ufloat data type with to_dict and from_dict function
class ufnum(ufloat):
    def __init__(self, value, uncertainty=0):
        super().__init__(value, uncertainty)
    @classmethod
    def from_dict(cls, dict : dict):
        return cls(dict['value'], dict['uncertainty'])
    def to_unum(self):
        return UNumber(value=self.value, uncertainty=self.uncertainty)