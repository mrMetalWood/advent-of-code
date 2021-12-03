import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    instructions = [l.strip().split(" ") for l in file.readlines()]
    instructions = [(i[0], int(i[1])) for i in instructions]


def part1():
    x = depth = 0

    for (direction, value) in instructions:
        if direction == "forward":
            x += value
        if direction == "up":
            depth -= value
        if direction == "down":
            depth += value

    return x * depth


def part2():
    x = depth = aim = 0

    for (direction, value) in instructions:
        if direction == "forward":
            x += value
            depth += aim * value
        if direction == "up":
            aim -= value
        if direction == "down":
            aim += value

    return x * depth


print(f"Part 1: {part1()}")  # 1882980
print(f"Part 2: {part2()}")  # 1971232560
