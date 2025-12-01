import argparse
import importlib
import time
from pathlib import Path


def run_day(day: int):
    day_str = f"day{day:02d}"
    module_name = f"days.{day_str}"
    base_dir = Path(__file__).parent
    input_path = base_dir / "inputs" / f"{day_str}.txt"

    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(
            f"❌ Could not import {module_name}. Make sure 'days/{day_str}.py' exists."
        )
        return

    if not input_path.exists():
        print(f"⚠️ Input file {input_path} not found.")
        data = ""
    else:
        data = input_path.read_text().strip()

    for part in [1, 2]:
        func_name = f"part{part}"
        if hasattr(module, func_name):
            print(f"\n⭐ Part {part}:")
            start_time = time.perf_counter()
            result = getattr(module, func_name)(data)
            end_time = time.perf_counter()

            print(f"Result: {result}")
            print(f"Time:   {(end_time - start_time) * 1000:.4f} ms")
        else:
            print(f"\nPart {part} not implemented.")


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2025 Runner")
    parser.add_argument("day", type=int, help="Day number to run (e.g., 1)")
    args = parser.parse_args()

    run_day(args.day)


if __name__ == "__main__":
    main()
