# Advent of Code 2025

Minimal setup for Advent of Code 2025.

## Structure
- `days/`: Contains solution files (`day01.py`, etc.)
- `inputs/`: Contains input files (`day01.txt`, etc.)
- `main.py`: CLI runner
- `Makefile`: Command shortcuts

## Usage

### Run a specific day
```bash
make run d=1
# or
uv run main.py 1
```

### Benchmark a day (requires [hyperfine](https://github.com/sharkdp/hyperfine))
```bash
make time d=1
```

### Create a new day
```bash
make new d=2
```
This will create `days/day02.py` from the template and an empty `inputs/day02.txt`.

