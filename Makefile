.PHONY: run time new

# Default day to 1 if not specified
d ?= 1
DAY_PADDED := $(shell printf "%02d" $(d))

run:
	@uv run main.py $(d)

time:
	@hyperfine --warmup 3 'uv run main.py $(d)'

new:
	@if [ -f days/day$(DAY_PADDED).py ]; then \
		echo "Day $(d) already exists!"; \
	else \
		echo "Creating Day $(d)..."; \
		cp days/template.py days/day$(DAY_PADDED).py; \
		touch inputs/day$(DAY_PADDED).txt; \
		echo "Created days/day$(DAY_PADDED).py and inputs/day$(DAY_PADDED).txt"; \
	fi

