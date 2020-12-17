from collections import defaultdict
from copy import deepcopy
import os
import re

dx = [-1, 0, 1]
dy = [-1, 0, 1]
dz = [-1, 0, 1]
dw = [-1, 0, 1]


def process(x, y, z, w, system):
    current_value, neighbours = system[(x, y, z, w)], ""
    for x2 in dx:
        for y2 in dy:
            for z2 in dz:
                for w2 in dw:
                    if not (
                        x == x + x2 and y == y + y2 and z == z + z2 and w == w + w2
                    ):
                        neighbours += system[(x + x2, y + y2, z + z2, w + w2)]

    active = neighbours.count("#")
    if (current_value == "#" and active in [2, 3]) or (
        current_value == "." and active == 3
    ):
        return "#"

    return "."


def boot(system, is_part1):
    for cycle in range(6):
        expansion = cycle + 1
        next_system = deepcopy(system)
        w_range_start = 0 if is_part1 else -expansion
        w_range_stop = 1 if is_part1 else expansion + 1

        for w in range(w_range_start, w_range_stop):
            for z in range(-expansion, 1 + expansion):
                for y in range(-expansion, len(lines) + expansion):
                    for x in range(-expansion, len(lines[0]) + expansion):
                        next_system[(x, y, z, w)] = process(x, y, z, w, system)

        system = deepcopy(next_system)
    return sum([1 for cell in system.values() if cell == "#"])


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]
    system = defaultdict(lambda: ".")
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            system[(x, y, 0, 0)] = cell

    print(f"Part 1: {boot(system, True)}")  # 319
    print(f"Part 2: {boot(system, False)}")  # 2324
