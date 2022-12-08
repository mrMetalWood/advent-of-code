from collections import defaultdict
from collections import deque
from functools import reduce
from copy import deepcopy
import itertools as it
import operator
import math
import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    # numbers on single line without separator
    numbers = [int(n) for n in file.read()]

    # single line numbers, comma separated
    numbers = [int(n) for n in file.read().split(",")]

    # numbers on multiple lines
    numbers = [int(l.strip()) for l in file.readlines()]

    # tuple split by "(" on multiple lines
    items = [tuple(l.strip().split(")")) for l in file.readlines()]

    # multiple separators
    items = [re.split("-| |: ", l.strip()) for l in file.readlines()]

    # 2d grid
    lines = [l.strip() for l in file.readlines()]
    grid = defaultdict(lambda: -1)

    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            grid[(x, y)] = int(cell)

    directions = [
        [0, -1],  # top
        [1, 0],  # right
        [0, 1],  # bottom
        [-1, 0],  # left
    ]


def part1():
    return "part 1"


def part2():
    return "part 2"


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
