import networkx as nx


def euclidean_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


def all_pairs_with_distance(
    points: list[tuple[int, int, int]],
) -> list[tuple[tuple[int, int, int], tuple[int, int, int], int]]:
    return [
        (a, b, euclidean_distance(a, b))
        for i, a in enumerate(points)
        for b in points[i + 1 :]
    ]


def point_to_str(point: tuple[int, int, int]) -> str:
    return f"{point[0]},{point[1]},{point[2]}"


def part1(data: str):
    points = [tuple(map(int, line.split(","))) for line in data.splitlines()]
    pairs = sorted(all_pairs_with_distance(points), key=lambda x: x[2])

    G = nx.Graph()
    for point in points:
        G.add_node(point_to_str(point))
    for p1, p2, _ in pairs[:1000]:
        G.add_edge(point_to_str(p1), point_to_str(p2))

    result = 1
    for component in sorted(nx.connected_components(G), key=len, reverse=True)[:3]:
        result *= len(component)
    return result


def part2(data: str):
    points = [tuple(map(int, line.split(","))) for line in data.splitlines()]
    pairs = sorted(all_pairs_with_distance(points), key=lambda x: x[2])

    G = nx.Graph()
    for point in points:
        G.add_node(point_to_str(point))
    for p1, p2, _ in pairs:
        G.add_edge(point_to_str(p1), point_to_str(p2))
        if nx.is_connected(G):
            x1, _, _ = p1
            x2, _, _ = p2
            return x1 * x2
