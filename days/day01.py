from dataclasses import dataclass
from typing import Literal


@dataclass
class Rotation:
    direction: Literal["L", "R"]
    distance: int

    def from_string(string: str) -> "Rotation":
        direction: Literal["L", "R"] = string[0]
        distance: int = int(string[1:])
        return Rotation(direction, distance)


def part1(data: str) -> int:
    position: int = 50
    rotations: list[Rotation] = [
        Rotation.from_string(line) for line in data.splitlines()
    ]
    result = 0
    for rotation in rotations:
        match rotation.direction:
            case "L":
                position = (position - rotation.distance) % 100
            case "R":
                position = (position + rotation.distance) % 100
        if position == 0:
            result += 1
    return result


def part2(data: str) -> int:
    position: int = 50
    rotations: list[Rotation] = [
        Rotation.from_string(line) for line in data.splitlines()
    ]
    result = 0
    for rotation in rotations:
        match rotation.direction:
            case "L":
                position = position - rotation.distance
            case "R":
                position = position + rotation.distance
        if position <= 0 or position >= 100:
            result += (
                rotation.direction == "L" and (position + rotation.distance) != 0
            ) + (abs(position) // 100)
        position %= 100
    return result
