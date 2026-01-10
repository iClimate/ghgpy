import sys  
sys.path.append("./")

import unittest
from src.converter import convertLength
from src.converter import convertWeight
from src.converter import convertData
from src.converter import convertVolume
from src.converter import convertEnergy
from src.converter import convertPressure
from src.converter import convertTemperature
from src.converter import convertSpeed
from src.converter import convertTime

class TestConverter(unittest.TestCase):
    def test_convert_Length(self):
        self.assertEqual(convertLength(12, 'm', 'A'), 1.2e+11)

    def test_convert_Weight(self):
        self.assertEqual(convertWeight(1000, "g", "kg"), 1.0)

    def test_convert_Data(self):
        self.assertEqual(convertData(1000, "g", "kg"), 1.0)
    
    def test_convert_Volume(self):
        self.assertEqual(convertVolume(1000, "g", "kg"), 1.0)

    def test_convert_Energy(self):
        self.assertEqual(convertEnergy(1000, "g", "kg"), 1.0)

    def test_convert_Pressure(self):
        self.assertEqual(convertPressure(1000, "g", "kg"), 1.0)

    def test_convert_Temperature(self):
        self.assertEqual(convertTemperature(1000, "g", "kg"), 1.0)

    def test_convert_Time(self):
        self.assertEqual(convertTime(1000, "g", "kg"), 1.0)

    def test_convert_Speed(self):
        self.assertEqual(convertSpeed(1000, "g", "kg"), 1.0)
    

unittest.main()