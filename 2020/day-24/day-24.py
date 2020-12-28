from collections import defaultdict
from copy import deepcopy
import os

DIRS = {
    "nw": [0, 1, -1],
    "ne": [1, 0, -1],
    "e": [1, -1, 0],
    "se": [0, -1, 1],
    "sw": [-1, 0, 1],
    "w": [-1, 1, 0],
}

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]
    paths = []
    for line in lines:
        path = []
        pointer = 0
        while pointer < len(line):
            next_item = line[pointer : pointer + 2]
            if next_item in DIRS:
                path.append(next_item)
                pointer += 2
            else:
                path.append(next_item[0])
                pointer += 1
        paths.append(path)

    grid = defaultdict(lambda: False)
    for path in paths:
        tile = [0, 0, 0]
        for step in path:
            tile = [sum(x) for x in zip(tile, DIRS[step])]
        grid[tuple(tile)] = not grid[tuple(tile)]
    print("Part 1", len(list(filter(bool, grid.values()))))  # 465

    for _ in range(100):
        new_grid = deepcopy(grid)
        tiles_to_check = set()

        for x, y, z in list(grid):
            tiles_to_check.add((x, y, z))
            for d in DIRS.values():
                neighbour = [sum(x) for x in zip([x, y, z], d)]
                tiles_to_check.add(tuple(neighbour))

        for x, y, z in list(tiles_to_check):
            black_tiles = 0

            for d in DIRS.values():
                neighbour = [sum(x) for x in zip([x, y, z], d)]

                if grid[tuple(neighbour)]:
                    black_tiles += 1

            if grid[(x, y, z)] and (black_tiles == 0 or black_tiles > 2):
                new_grid[(x, y, z)] = False
            if not grid[(x, y, z)] and black_tiles == 2:
                new_grid[(x, y, z)] = True

        grid = deepcopy(new_grid)
    print("Part 2", len(list(filter(bool, grid.values()))))
