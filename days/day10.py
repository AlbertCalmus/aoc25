from collections import deque

import numpy as np
from scipy.optimize import LinearConstraint, milp


def state_after_button(state: str, button: tuple[int, ...]) -> str:
    """
    Takes a state and a button and returns the state after the button is pressed.
    If i is in button, the the i-th character of the state is toggled ('.' -> '#' or '#' -> '.').
    All other characters remain unchanged.
    """
    output = ""
    for i in range(len(state)):
        if i in button:
            output += "." if state[i] == "#" else "#"
        else:
            output += state[i]
    return output


def part1(data: str):
    machines = [
        (
            line.split(" ")[0].replace("[", "").replace("]", ""),
            [
                tuple(map(int, line.replace("(", "").replace(")", "").split(",")))
                for line in line.split(" ")[1:-1]
            ],
            tuple(
                map(
                    int,
                    line.split(" ")[-1].replace("{", "").replace("}", "").split(","),
                )
            ),
        )
        for line in data.splitlines()
    ]
    result = 0
    for goal, buttons, _ in machines:
        start = goal.replace("#", ".")
        visited, queue = set([start]), deque([(start, 0)])
        while queue:
            current, steps = queue.popleft()
            if current == goal:
                result += steps
                break
            for button in buttons:
                new_position = state_after_button(current, button)
                if new_position not in visited:
                    visited.add(new_position)
                    queue.append((new_position, steps + 1))

    return result


def part2(data: str):
    machines = [
        (
            line.split(" ")[0].replace("[", "").replace("]", ""),
            [
                tuple(map(int, line.replace("(", "").replace(")", "").split(",")))
                for line in line.split(" ")[1:-1]
            ],
            tuple(
                map(
                    int,
                    line.split(" ")[-1].replace("{", "").replace("}", "").split(","),
                )
            ),
        )
        for line in data.splitlines()
    ]

    result = 0

    for _, buttons, goal in machines:
        A = np.zeros((len(goal), len(buttons)))
        for i, button in enumerate(buttons):
            for j in button:
                A[j, i] = 1

        b = np.array(goal)

        constraints = LinearConstraint(A, b, b)
        integrality = np.ones(len(buttons))

        solution = milp(
            c=np.ones(len(buttons)), constraints=constraints, integrality=integrality
        )
        result += np.sum(np.round(solution.x).astype(int))

    return result
