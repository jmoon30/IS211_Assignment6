def convertCelsiusToKelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return float(celsius) + 273.15


def convertCelsiusToFahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return float(celsius) * 9.0 / 5.0 + 32.0


def convertFahrenheitToCelsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (float(fahrenheit) - 32.0) * 5.0 / 9.0


def convertFahrenheitToKelvin(fahrenheit: float) -> float:
    """Convert Fahrenheit to Kelvin."""
    return convertCelsiusToKelvin(convertFahrenheitToCelsius(fahrenheit))


def convertKelvinToCelsius(kelvin: float) -> float:
    """Convert Kelvin to Celsius."""
    return float(kelvin) - 273.15


def convertKelvinToFahrenheit(kelvin: float) -> float:
    """Convert Kelvin to Fahrenheit."""
    return convertCelsiusToFahrenheit(convertKelvinToCelsius(kelvin))
