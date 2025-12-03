def first_max(bank: list[int], from_index: int, to_index: int) -> int:
    max_index, max_value = 0, -1
    for i in range(from_index, to_index):
        if bank[i] > max_value:
            max_value = bank[i]
            max_index = i
    return max_index, max_value


def part1(data: str):
    banks = [list(map(int, list(line))) for line in data.splitlines()]
    result = 0
    for bank in banks:
        max_index, max_value = first_max(bank, 0, len(bank) - 1)
        result += 10 * max_value + max(bank[max_index + 1 :])
    return result


def part2(data: str):
    banks = [list(map(int, list(line))) for line in data.splitlines()]
    result = 0
    for bank in banks:
        current_index = 0
        for shift in range(12):
            max_index, max_value = first_max(
                bank, current_index, len(bank) - 12 + shift + 1
            )
            result += 10 ** (12 - shift - 1) * max_value
            current_index = max_index + 1
    return result
