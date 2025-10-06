from typing import Callable, Dict

class ConversionNotPossible(Exception):
    pass


# Temperature helpers (affine transformations to/from Kelvin)
def _c_to_k(c: float) -> float: return float(c) + 273.15
def _f_to_k(f: float) -> float: return (float(f) - 32.0) * 5.0 / 9.0 + 273.15
def _k_to_c(k: float) -> float: return float(k) - 273.15
def _k_to_f(k: float) -> float: return (float(k) - 273.15) * 9.0 / 5.0 + 32.0

_TEMP_TO_K = {
    "celsius": _c_to_k,
    "c": _c_to_k,
    "fahrenheit": _f_to_k,
    "f": _f_to_k,
    "kelvin": float,
    "k": float,
}

_K_TO_TEMP = {
    "celsius": _k_to_c,
    "c": _k_to_c,
    "fahrenheit": _k_to_f,
    "f": _k_to_f,
    "kelvin": float,
    "k": float,
}

# Distance factors (to meters)
_DISTANCE_TO_M = {
    "meters": 1.0,
    "meter": 1.0,
    "m": 1.0,
    "yards": 0.9144,
    "yard": 0.9144,
    "yd": 0.9144,
    "miles": 1609.344,
    "mile": 1609.344,
    "mi": 1609.344,
}

def _normalize(unit: str) -> str:
    if not isinstance(unit, str):
        raise ConversionNotPossible("Unit names must be strings.")
    return unit.strip().lower()

def _category(unit: str) -> str:
    u = _normalize(unit)
    if u in _TEMP_TO_K:
        return "temperature"
    if u in _DISTANCE_TO_M:
        return "distance"
    raise ConversionNotPossible(f"Unknown unit: {unit}")

def convert(fromUnit: str, toUnit: str, value: float) -> float:
    """Generic converter for temperature (C/F/K) and distance (m/yd/mi).
    
    - Returns the same value when units are identical (case-insensitive).
    - Raises ConversionNotPossible for incompatible categories or unknown units.
    """
    f, t = _normalize(fromUnit), _normalize(toUnit)
    if f == t:
        return float(value)

    cat_from = _category(f)
    cat_to = _category(t)
    if cat_from != cat_to:
        raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}.")

    if cat_from == "temperature":
        # value -> Kelvin -> target
        k = _TEMP_TO_K[f](value)
        return _K_TO_TEMP[t](k)

    # distance: value -> meters -> target
    meters = float(value) * _DISTANCE_TO_M[f]
    # convert meters -> target
    return meters / _DISTANCE_TO_M[t]
