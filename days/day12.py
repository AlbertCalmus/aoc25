"""
Input looking like this:
0:
#..
##.
.##

1:
###
.##
##.

2:
###
###
#..

3:
..#
.##
###

4:
###
.#.
###

5:
###
..#
###

42x45: 51 48 40 49 56 48
40x47: 38 43 52 44 61 48
49x41: 48 45 53 62 51 51
...

We need to parse the 3x3 chunks and the list of arrangements (e.g. 42x45: 51 48 40 49 56 48)
and find the number of arrangements that are possible.
"""

import re

import numpy as np


def parse_input(data: str):
    chunks, arrangements = [], []
    lines = [line.replace(".", "0").replace("#", "1") for line in data.splitlines()]
    i = 0
    while i < len(lines):
        if re.match(r"\d+x\d+:", lines[i]):
            size, weights = lines[i].split(": ")
            x, y = map(int, size.split("x"))
            weights = [int(weight) for weight in weights.split(" ")]
            arrangements.append(((x, y), np.array(weights)))
            i += 1
        elif re.match(r"^\d:$", lines[i]):
            chunks.append(
                [
                    np.array(list(map(int, line)))
                    for line in [lines[i + 1], lines[i + 2], lines[i + 3]]
                ]
            )
            i += 4
        else:
            i += 1

    chunk_surfaces = [np.sum(chunk) for chunk in chunks]

    return chunks, chunk_surfaces, arrangements


def part1(data: str):
    _, chunk_surfaces, arrangements = parse_input(data)
    result = 0
    for arrangement in arrangements:
        (x, y), weights = arrangement
        total_surface = x * y
        required_surface = sum(
            chunk_surface * weight
            for (chunk_surface, weight) in zip(chunk_surfaces, weights)
        )
        if total_surface >= required_surface:
            result += 1
    return result


def part2(data: str):
    return 0
