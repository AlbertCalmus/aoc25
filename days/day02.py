def generate_invalid_ids(max_half: int) -> list[int]:
    return [int(f"{str(i)}{str(i)}") for i in range(1, max_half + 1)]


def generate_more_invalid_ids(max_half: int, max_length: int) -> list[int]:
    result = []
    for i in range(1, max_half + 1):
        for k in range(2, max_length // len(str(i)) + 1):
            result.append(int(f"{str(i)}" * k))
    return list(set(result))


def part1(data: str) -> int:
    intervals = [tuple(map(int, interval.split("-"))) for interval in data.split(",")]
    result = 0
    invalid_ids = sorted(generate_invalid_ids(99999))
    for start, end in intervals:
        for invalid_id in invalid_ids:
            if invalid_id >= start and invalid_id <= end:
                result += invalid_id
            elif invalid_id > end:
                break
    return result


def part2(data: str) -> int:
    intervals = [tuple(map(int, interval.split("-"))) for interval in data.split(",")]
    result = 0
    invalid_ids = sorted(generate_more_invalid_ids(99999, 10))
    for start, end in intervals:
        for invalid_id in invalid_ids:
            if invalid_id >= start and invalid_id <= end:
                result += invalid_id
            elif invalid_id > end:
                break
    return result
