from dataclasses import dataclass


@dataclass
class Grid:
    grid: list[list[str]]
    num_rows: int
    num_cols: int

    def from_input(input: str) -> "Grid":
        return Grid(
            [list(line) for line in input.splitlines()],
            len(input.splitlines()),
            len(input.splitlines()[0]),
        )

    def display(self) -> str:
        return "\n".join("".join(row) for row in self.grid)

    def neighbours(self, x: int, y: int) -> list[tuple[int, int]]:
        """
        Returns the neighbours of the cell at (x, y) in the grid.
        """
        neighbours = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if 0 <= x + dx < len(self.grid) and 0 <= y + dy < len(self.grid[0]):
                    neighbours.append(self.grid[x + dx][y + dy])
        return neighbours


def part1(data: str) -> int:
    result = 0
    grid = Grid.from_input(data)
    for x in range(grid.num_rows):
        for y in range(grid.num_cols):
            if grid.grid[x][y] == "@" and grid.neighbours(x, y).count("@") < 4:
                result += 1
    return result


def part2(data: str) -> int:
    result = 0
    grid = Grid.from_input(data)
    while True:
        to_be_removed = []
        for x in range(grid.num_rows):
            for y in range(grid.num_cols):
                if grid.grid[x][y] == "@" and grid.neighbours(x, y).count("@") < 4:
                    to_be_removed.append((x, y))
        if len(to_be_removed) == 0:
            break
        for x, y in to_be_removed:
            grid.grid[x][y] = "."
        result += len(to_be_removed)
    return result
