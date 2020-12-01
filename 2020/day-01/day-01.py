import os
import itertools

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    numbers = [int(l.strip()) for l in file.readlines()]

for i, j, k in itertools.combinations(numbers, 3):
    if i + j == 2020:
        part1 = i * j
    if i + j + k == 2020:
        part2 = i * j * k


print(f"Part 1: {part1}")  # 1010299
print(f"Part 2: {part2}")  # 42140160
