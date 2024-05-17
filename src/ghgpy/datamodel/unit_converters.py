"""
Unit Converters for GHG inventory
(c) Bui Khac Tu (bkt92)
"""

class energy_units:
    """
    Convert between difference energy units
    """
    units = ['j', 'kj', 'mj', 'tj', 'gj', 'Tj', 'kWh', 'Wh','MWh', 'GWh', 'TWh']
    @staticmethod
    def convert(val: float, unit_in: str, unit_out: str) -> float:
        SI = {'j': 1.0, 'kj': 1000.0, 'mj': 1.0*10**6, 'gj': 1.0*10**9, 'tj': 1.0*10**12, \
              'Wh': 3600 , 'kWh': 3600*10**3, 'MWh': 3600*10**6, 'GWh': 3600*10**9, 'TWh': 3600*10**12}
        return val * SI[unit_in] / SI[unit_out]

class weigh_units:
    """
    Convert between difference weigh units
    """
    units = ['g', 'kg', 'tonne', 'Gg']
    @staticmethod
    def convert(val: float, unit_in: str, unit_out: str) -> float:
        SI = {'g': 1.0, 'kg': 1000.0, 'tonne': 1.0*10**6, 't': 1.0*10**6,'tonnes': 1.0*10**6, 'Gg': 1.0*10**9}
        return val * SI[unit_in] / SI[unit_out]

class volume_units:
    """
    Convert between difference volume units
    """
    units = ['litre', 'l', 'm3']
    @staticmethod
    def convert(val: float, unit_in: str, unit_out: str) -> float:
        SI = {'litre': 1.0, 'l': 1.0, 'm3': 1000.0}
        return val * SI[unit_in] / SI[unit_out]