import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def run(name: str):
    path = ROOT / name
    print(f"Running {name}...")
    runpy.run_path(str(path), run_name="__main__")
    print()

if __name__ == "__main__":
    run("tests.py")
    run("tests_refactored.py")
