from collections import defaultdict
from functools import lru_cache

GRAPH = defaultdict(list)


@lru_cache()
def count_paths(start: str, end: str) -> int:
    if start == end:
        return 1
    count = 0
    for neighbor in GRAPH[start]:
        count += count_paths(neighbor, end)
    return count


def part1(data: str):
    for line in data.splitlines():
        key, value = line.split(": ")
        GRAPH[key].extend(value.split(" "))

    return count_paths("you", "out")


def part2(data: str):
    result = 0

    paths = [("svr", "dac", "fft", "out"), ("svr", "fft", "dac", "out")]

    for path in paths:
        count = 1
        for i in range(len(path) - 1):
            count *= count_paths(path[i], path[i + 1])
            if count == 0:
                break

        result += count

    return result
