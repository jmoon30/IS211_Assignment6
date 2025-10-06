
# IS211_Assignment6 — Testing & Refactoring

This project implements unit tests and conversion functions for temperatures (°C/°F/K), then refactors to a single generic converter that also supports distances (meters/yards/miles). It follows the Week 6 instructions for creating tests first, implementing functions, and finally refactoring with error handling.

## Repository Contents
- **conversions.py** — Six temperature conversion functions:
  - `convertCelsiusToKelvin`, `convertCelsiusToFahrenheit`
  - `convertFahrenheitToCelsius`, `convertFahrenheitToKelvin`
  - `convertKelvinToCelsius`, `convertKelvinToFahrenheit`
- **tests.py** — Unit tests for the six functions (5 cases per function, verbose output).
- **conversions_refactored.py** — Single generic function:
  - `convert(fromUnit: str, toUnit: str, value: float) -> float`
  - Supports **temperature** (C/F/K) and **distance** (meters/yards/miles).
  - Case-insensitive unit names; identity conversions (same unit) return the input value.
  - Raises `ConversionNotPossible` for incompatible or unknown units.
- **tests_refactored.py** — Unit tests for the generic converter:
  - Temperature conversions, distance conversions, identity conversions, and exception cases.
- **run_tests.py** — Cross‑platform runner to execute both test suites (uses `pathlib` relative paths).

## How to Run Tests
Requirements: Python 3.8+ (no third‑party packages).

```bash
# Part I–III tests (six temperature functions)
python tests.py

# Part IV tests (generic converter + exceptions)
python tests_refactored.py

# Run both
python run_tests.py
```

Expected result for each suite:
```
----------------------------------------------------------------------
Ran N tests in 0.00s
OK
```

## Assignment Mapping (Checklist)
- **Part I (Create tests for Celsius conversions):** `tests.py` includes tests for Celsius→Kelvin and Celsius→Fahrenheit with **5 cases each** and prints output lines for each case.
- **Part II (Implement Celsius functions):** `conversions.py` implements both functions and they pass the tests.
- **Part III (Repeat for all six conversions):** All six temperature functions are implemented in `conversions.py` and each has **5 test cases** in `tests.py` (verbose).
- **Part IV (Refactor to generic converter):** `conversions_refactored.py` provides a single `convert()` that:
  - Handles **C/F/K** and **meters/yards/miles**.
  - Returns the same value for identical units (case‑insensitive).
  - Raises `ConversionNotPossible` for incompatible categories (e.g., Celsius→meters) or unknown units.
  - **Does not** rely on the separate six functions—formulas are implemented directly in the refactor.
  - `tests_refactored.py` verifies conversions, identity behavior, and exception paths.

## Supported Units (Refactored Converter)
- **Temperature:** `celsius`/`c`, `fahrenheit`/`f`, `kelvin`/`k`
- **Distance:** `meters`/`meter`/`m`, `yards`/`yard`/`yd`, `miles`/`mile`/`mi`

Units are matched case‑insensitively and normalized (e.g., `" C "` works).

## Design Notes
- **Temperature conversions** are implemented as affine transforms via Kelvin as the canonical reference.
- **Distance conversions** use meters as the canonical reference; factors:
  - 1 yard = 0.9144 meters
  - 1 mile = 1609.344 meters
- **Error handling:** `ConversionNotPossible` is raised for unknown units or category mismatches.
- **Identity conversions:** If `fromUnit == toUnit` after normalization, the function returns the input value.

## Developer Tips (Optional)
- To extend distance units, add to `_DISTANCE_TO_M` with a meters factor.
- To extend temperature aliases, add keys to `_TEMP_TO_K` / `_K_TO_TEMP`.

---

© 2025 — IS211 Assignment 6
