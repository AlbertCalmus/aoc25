def get_disjoint_intervals_and_total_span(
    intervals: list[tuple[int, int]],
) -> (list[tuple[int, int]], int):
    sorted_intervals = sorted(intervals)
    disjoint_intervals = []
    result = 0
    for i, (start, end) in enumerate(sorted_intervals):
        if i + 1 < len(sorted_intervals) and sorted_intervals[i + 1][0] <= end:
            _, next_end = sorted_intervals[i + 1]
            sorted_intervals[i + 1] = (start, max(end, next_end))
        else:
            disjoint_intervals.append((start, end))
            result += end - start + 1
    return disjoint_intervals, result


def part1(data: str):
    intervals_data, ingredients_data = data.split("\n\n")
    intervals = [
        (int(x), int(y))
        for x, y in [interval.split("-") for interval in intervals_data.splitlines()]
    ]

    disjoint_intervals, _ = get_disjoint_intervals_and_total_span(intervals)
    ingredients = sorted(
        [int(ingredient) for ingredient in ingredients_data.splitlines()]
    )

    result = 0
    start_at = 0
    for ingredient in ingredients:
        for start, end in disjoint_intervals[start_at:]:
            if ingredient > end:
                start_at += 1
            elif ingredient < start:
                break
            else:
                result += 1
                break
    return result


def part2(data: str):
    intervals_data, _ = data.split("\n\n")
    intervals = [
        (int(x), int(y))
        for x, y in [interval.split("-") for interval in intervals_data.splitlines()]
    ]
    _, result = get_disjoint_intervals_and_total_span(intervals)
    return result
