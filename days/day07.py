from dataclasses import dataclass, field


@dataclass
class Grid:
    grid: list[list[str]]
    num_rows: int
    num_cols: int
    start_position: tuple[int, int] | None = None
    beam_split_positions: list[tuple[int, int]] = field(default_factory=list)

    def from_input(input: str) -> "Grid":
        return Grid(
            [list(line) for line in input.splitlines()],
            len(input.splitlines()),
            len(input.splitlines()[0]),
        )

    def display(self) -> str:
        return "\n".join("".join(row) for row in self.grid)

    def locate_start_position(self) -> None:
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.grid[i][j] == "S":
                    self.start_position = (i, j)
                    return
        raise ValueError("Start position not found")

    def propagate_beam(
        self,
        from_position: tuple[int, int],
    ) -> None:
        x, y = from_position
        if x == self.num_rows:
            return
        elif self.grid[x][y] == "S":
            self.propagate_beam((x + 1, y))
        elif self.grid[x][y] == ".":
            self.grid[x][y] = "|"
            self.propagate_beam((x + 1, y))
        elif self.grid[x][y] == "^":
            self.beam_split_positions.append((x, y))
            self.propagate_beam((x, y - 1))  # down left
            self.propagate_beam((x, y + 1))  # down right

    def number_of_timelines(self, from_position: tuple[int, int]) -> int:
        x, y = from_position
        if x == self.num_rows:
            return 1
        if not isinstance(self.grid[x][y], int):
            if self.grid[x][y] in ["S", "."]:
                self.grid[x][y] = self.number_of_timelines((x + 1, y))
            else:
                self.grid[x][y] = self.number_of_timelines(
                    (x, y - 1)
                ) + self.number_of_timelines((x, y + 1))
        return self.grid[x][y]


def part1(data: str):
    grid = Grid.from_input(data)
    grid.locate_start_position()
    grid.propagate_beam(
        grid.start_position,
    )
    return len(set(grid.beam_split_positions))


def part2(data: str):
    grid = Grid.from_input(data)
    grid.locate_start_position()
    return grid.number_of_timelines(grid.start_position)
