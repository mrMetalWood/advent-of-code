import os
import re


input_file = os.path.join(os.path.dirname(__file__), "input.txt")


with open(input_file, "r") as file:
    items = [re.split("-| |: ", l.strip()) for l in file.readlines()]


def part1():
    def is_valid(min, max, char, password):
        return int(min) <= password.count(char) <= int(max)

    return len(list(filter(lambda item: is_valid(*item), items)))


def part2():
    def is_valid(idx1, idx2, char, password):
        return (password[int(idx1) - 1] == char) != (password[int(idx2) - 1] == char)

    return len(list(filter(lambda item: is_valid(*item), items)))


print(f"Part 1: {part1()}")  # 483
print(f"Part 2: {part2()}")  # 482
