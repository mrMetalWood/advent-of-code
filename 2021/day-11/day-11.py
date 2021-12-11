from collections import defaultdict
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:

    rows = [l.strip() for l in file.readlines()]
    octopuses = defaultdict(int)

    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            octopuses[(x, y)] = int(col)

    directions = [
        [0, -1],
        [1, -1],
        [1, 0],
        [1, 1],
        [0, 1],
        [-1, 1],
        [-1, 0],
        [-1, -1],
    ]

flash_count = step = 0

while True:
    has_flashed = set()

    step += 1

    for coord in octopuses:
        octopuses[coord] += 1

    while True:
        next_round = False
        for (coord, value) in octopuses.items():
            if value > 9 and coord not in has_flashed:
                has_flashed.add(coord)
                flash_count += 1
                for [dx, dy] in directions:
                    new_coord = (coord[0] + dx, coord[1] + dy)
                    if new_coord in octopuses:
                        octopuses[new_coord] += 1
                        if octopuses[new_coord] > 9 and new_coord not in has_flashed:
                            next_round = True

        if not next_round:
            break

    for (coord, value) in octopuses.items():
        if value > 9:
            octopuses[coord] = 0

    if step == 100:
        print(f"Part 1: {flash_count}")  # 1642

    if sum(octopuses.values()) == 0:
        print(f"Part 2: {step}")  # 320
        break
