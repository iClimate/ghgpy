"""
Unit Converters for GHG inventory

(c) Bui Khac Tu (bkt92)
"""

class energy_units:
    """
    Convert between difference energy units
    """
    
    @staticmethod
    def convert(val: float, unit_in: str, unit_out: str) -> float:
        SI = {'J': 1.0, 'KJ': 1000.0, 'MJ': 1.0*10^6, 'TJ': 1.0*10^9}
        return val * SI[unit_in] / SI[unit_out]

class weigh_units:
    """
    Convert between difference weigh units
    """
    
    @staticmethod
    def convert(val: float, unit_in: str, unit_out: str) -> float:
        SI = {'J': 1.0, 'KJ': 1000.0, 'MJ': 1.0*10^6, 'TJ': 1.0*10^9}
        return val * SI[unit_in] / SI[unit_out]

class volume_units:
    """
    Convert between difference volume units
    """
    
    @staticmethod
    def convert(val: float, unit_in: str, unit_out: str) -> float:
        SI = {'J': 1.0, 'KJ': 1000.0, 'MJ': 1.0*10^6, 'TJ': 1.0*10^9}
        return val * SI[unit_in] / SI[unit_out]