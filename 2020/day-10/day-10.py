import os
from collections import Counter

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    numbers = sorted([int(l.strip()) for l in file.readlines()])
    numbers = [0] + numbers + [numbers[-1] + 3]


def part1():
    diffs = Counter([high - low for low, high in zip(numbers, numbers[1:])])
    return diffs[1] * diffs[3]


def part2():
    counts = [0] * len(numbers)
    counts[0] = 1

    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] - numbers[j] <= 3:
                counts[i] += counts[j]

    return counts[-1]


print(f"Part 1: {part1()}")  # 2170
print(f"Part 2: {part2()}")  # 24803586664192
