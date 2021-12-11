from collections import defaultdict
from collections import deque
import os


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    rows = [l.strip() for l in file.readlines()]

    grid = defaultdict(lambda: 9)

    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            grid[(x, y)] = int(col)

    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # top/right/bottom/left
    low_points = {}


def part1():
    count = 0
    new_grid = grid.copy()
    for (coordinates, value) in new_grid.items():
        if all(
            [
                grid[(coordinates[0] + dx, coordinates[1] + dy)] > value
                for [dx, dy] in directions
            ]
        ):
            low_points[coordinates] = value
            count += value + 1
    return count


def part2():
    basins = []

    for ([x, y], _) in low_points.items():
        points_to_check = deque([(x, y)])
        checked = set()
        basin = set()

        while points_to_check:
            current = points_to_check.popleft()

            checked.add(current)
            basin.add(current)

            (current_x, current_y) = current
            for [dx, dy] in directions:
                new_coords = (current_x + dx, current_y + dy)
                field = grid[new_coords]

                if field != 9:
                    basin.add(new_coords)

                    if new_coords not in checked:
                        points_to_check.append((new_coords))
        basins.append(basin)

    largest_basins = sorted(list(basins), key=len, reverse=True)

    return len(largest_basins[0]) * len(largest_basins[1]) * len(largest_basins[2])


print(f"Part 1: {part1()}")  # 535
print(f"Part 2: {part2()}")  # 1122700
