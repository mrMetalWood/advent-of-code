import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    items = [re.split("-| |: ", l.strip()) for l in file.readlines()]


def part1():
    def is_valid(min, max, char, pw):
        return int(min) <= pw.count(char) <= int(max)

    return len(list(filter(lambda item: is_valid(*item), items)))


def part2():
    def is_valid(idx1, idx2, char, pw):
        return (pw[int(idx1) - 1] == char) != (pw[int(idx2) - 1] == char)

    return len(list(filter(lambda item: is_valid(*item), items)))


print(f"Part 1: {part1()}")  # 483
print(f"Part 2: {part2()}")  # 482
