import os
from functools import reduce
import operator

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    grid = [l.strip() for l in file.readlines()]


def count_trees(right, down):
    col = trees = 0

    for row in range(0, len(grid), down):
        if grid[row][col] == "#":
            trees += 1
        col = (col + right) % len(grid[0])

    return trees


def part1():
    return count_trees(3, 1)


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(operator.mul, [count_trees(x, y) for x, y in slopes], 1)


print(f"Part 1: {part1()}")  # 250
print(f"Part 2: {part2()}")  # 1592662500
