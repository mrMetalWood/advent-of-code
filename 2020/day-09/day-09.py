import itertools
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    numbers = [int(l.strip()) for l in file.readlines()]


def part1():
    for i in range(25, len(numbers)):
        if not [
            n1 for (n1, n2) in itertools.combinations(numbers[i - 25 : i], 2) if n1 + n2 == numbers[i]
        ]:
            return numbers[i]


def part2():
    for range_size in range(2, len(numbers)):
        for i in range(0, len(numbers)):
            window = numbers[i : i + range_size]
            if sum(window) == 14360655:  # answer part one
                return min(window) + max(window)


print(f"Part 1: {part1()}")  # 14360655
print(f"Part 2: {part2()}")  # 1962331
