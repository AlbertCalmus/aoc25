import re


def part1(data: str):
    lines = data.splitlines()
    numbers, operations = (
        [list(map(int, re.split(r"\s+", line.strip()))) for line in lines[:-1]],
        re.split(r"\s+", lines[-1].strip()),
    )

    result = 0
    for i in range(len(operations)):
        operation = operations[i]
        operation_result = 0 if operation == "+" else 1
        for j in range(len(numbers)):
            if operation == "+":
                operation_result += numbers[j][i]
            elif operation == "*":
                operation_result *= numbers[j][i]
        result += operation_result
    return result


def part2(data: str):
    lines = data.split("\n")
    numbers, operations = (lines[:-1], lines[-1])

    result = 0

    operation_result = 0
    current_operation = None
    max_length = max([len(number) for number in numbers])
    for i in range(max_length):
        aggregated_number = ""
        if operations[i] in ["+", "*"]:
            current_operation = operations[i]
            result += operation_result
            operation_result = 0 if current_operation == "+" else 1
        for j in range(len(numbers)):
            aggregated_number += numbers[j][i]
        if current_operation == "+":
            operation_result += (
                int(aggregated_number) if aggregated_number.strip() else 0
            )
        elif current_operation == "*":
            operation_result *= (
                int(aggregated_number) if aggregated_number.strip() else 1
            )
    result += operation_result

    return result
