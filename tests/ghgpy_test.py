import sys  
sys.path.append("./")

import unittest
from src.ghgpy.datamodel.fuel import BaseFuel, ufnum
from uncertainty.utypes import ufloat

class TestConverter(unittest.TestCase):
    def test_convert_Length(self):
        fuel = BaseFuel("H2", "Hydrogen", ufnum(10), ufnum(10), ufnum(10), ufnum(20000, 2000), "kg")
        self.assertEqual(fuel.cal_energy().value, 0.036292, 0.000)
    
unittest.main()