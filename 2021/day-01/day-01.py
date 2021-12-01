import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    numbers = [int(l.strip()) for l in file.readlines()]


def count_increases(depths):
    return len([n for idx, n in enumerate(depths[:-1]) if depths[idx + 1] > n])


def part1():
    return count_increases(numbers)


def part2():
    return count_increases(
        [
            (n + numbers[idx + 1] + numbers[idx + 2])
            for idx, n in enumerate(numbers[:-2])
        ]
    )


print(f"Part 1: {part1()}")  # 1121
print(f"Part 2: {part2()}")  # 1065
