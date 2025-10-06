import unittest
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit,
)

class TestTemperatureConversions(unittest.TestCase):
    def assertAlmostEqualPlaces(self, a, b, places=2):
        self.assertAlmostEqual(a, b, places=places)

    def test_convertCelsiusToKelvin(self):
        cases = [
            (0.0, 273.15),
            (25.0, 298.15),
            (100.0, 373.15),
            (-40.0, 233.15),
            (300.0, 573.15),
        ]
        for c, expected_k in cases:
            result = convertCelsiusToKelvin(c)
            print(f"C->K: {c} °C -> {result:.2f} K (expected {expected_k:.2f})")
            self.assertAlmostEqualPlaces(result, expected_k, 2)

    def test_convertCelsiusToFahrenheit(self):
        cases = [
            (0.0, 32.0),
            (25.0, 77.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (300.0, 572.0),
        ]
        for c, expected_f in cases:
            result = convertCelsiusToFahrenheit(c)
            print(f"C->F: {c} °C -> {result:.2f} °F (expected {expected_f:.2f})")
            self.assertAlmostEqualPlaces(result, expected_f, 2)

    def test_convertFahrenheitToCelsius(self):
        cases = [
            (32.0, 0.0),
            (77.0, 25.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (572.0, 300.0),
        ]
        for f, expected_c in cases:
            result = convertFahrenheitToCelsius(f)
            print(f"F->C: {f} °F -> {result:.2f} °C (expected {expected_c:.2f})")
            self.assertAlmostEqualPlaces(result, expected_c, 2)

    def test_convertFahrenheitToKelvin(self):
        cases = [
            (32.0, 273.15),
            (77.0, 298.15),
            (212.0, 373.15),
            (-40.0, 233.15),
            (572.0, 573.15),
        ]
        for f, expected_k in cases:
            result = convertFahrenheitToKelvin(f)
            print(f"F->K: {f} °F -> {result:.2f} K (expected {expected_k:.2f})")
            self.assertAlmostEqualPlaces(result, expected_k, 2)

    def test_convertKelvinToCelsius(self):
        cases = [
            (273.15, 0.0),
            (298.15, 25.0),
            (373.15, 100.0),
            (233.15, -40.0),
            (573.15, 300.0),
        ]
        for k, expected_c in cases:
            result = convertKelvinToCelsius(k)
            print(f"K->C: {k} K -> {result:.2f} °C (expected {expected_c:.2f})")
            self.assertAlmostEqualPlaces(result, expected_c, 2)

    def test_convertKelvinToFahrenheit(self):
        cases = [
            (273.15, 32.0),
            (298.15, 77.0),
            (373.15, 212.0),
            (233.15, -40.0),
            (573.15, 572.0),
        ]
        for k, expected_f in cases:
            result = convertKelvinToFahrenheit(k)
            print(f"K->F: {k} K -> {result:.2f} °F (expected {expected_f:.2f})")
            self.assertAlmostEqualPlaces(result, expected_f, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
