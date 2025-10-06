import unittest
from conversions_refactored import convert, ConversionNotPossible

class TestRefactoredConvert(unittest.TestCase):
    def assertAlmost(self, a, b, places=4):
        self.assertAlmostEqual(a, b, places=places)

    def test_temperature_conversions(self):
        # C <-> K <-> F
        self.assertAlmost(convert('Celsius', 'Kelvin', 0.0), 273.15)
        self.assertAlmost(convert('C', 'F', 300.0), 572.0)
        self.assertAlmost(convert('Kelvin', 'Celsius', 373.15), 100.0)
        self.assertAlmost(convert('Fahrenheit', 'Kelvin', -40.0), 233.15)
        self.assertAlmost(convert('K', 'F', 298.15), 77.0)

    def test_distance_conversions(self):
        # meters, yards, miles
        self.assertAlmost(convert('meters', 'yards', 1.0), 1.0936133, places=6)
        self.assertAlmost(convert('yards', 'meters', 10.0), 9.144, places=6)
        self.assertAlmost(convert('miles', 'meters', 1.0), 1609.344, places=3)
        self.assertAlmost(convert('meters', 'miles', 1609.344), 1.0, places=6)
        self.assertAlmost(convert('miles', 'yards', 1.0), 1760.0, places=6)

    def test_same_unit_returns_value(self):
        self.assertEqual(convert('C', 'c', 12.34), 12.34)
        self.assertEqual(convert('meters', 'Meters', 5), 5.0)

    def test_incompatible_units_raise(self):
        with self.assertRaises(ConversionNotPossible):
            convert('Celsius', 'meters', 1.0)
        with self.assertRaises(ConversionNotPossible):
            convert('miles', 'Kelvin', 3.0)

    def test_unknown_units_raise(self):
        for bad in ['lightyears', 'rpm', '', None]:
            with self.assertRaises(ConversionNotPossible):
                convert('meters', bad, 1.0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
