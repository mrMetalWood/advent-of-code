import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    items = [re.split("-| |: ", l.strip()) for l in file.readlines()]


def part1():
    return len(
        [pw for (min, max, c, pw) in items if int(min) <= pw.count(c) <= int(max)]
    )


def part2():
    return len(
        [
            pw
            for (i1, i2, c, pw) in items
            if (pw[int(i1) - 1] == c) ^ (pw[int(i2) - 1] == c)
        ]
    )


print(f"Part 1: {part1()}")  # 483
print(f"Part 2: {part2()}")  # 482
