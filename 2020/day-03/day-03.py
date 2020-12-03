import os
import math

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    grid = [l.strip() for l in file.readlines()]


def trees(right, down):
    col = count = 0

    for row in range(0, len(grid), down):
        if grid[row][col] == "#":
            count += 1
        col = (col + right) % len(grid[0])

    return count


part1 = trees(3, 1)
part2 = math.prod([trees(r, d) for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])

print(f"Part 1: {part1}")  # 250
print(f"Part 2: {part2}")  # 1592662500
