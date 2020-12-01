from collections import defaultdict
from collections import deque
from collections import Counter
import itertools
import math
import os


input_file = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_file, "r") as file:
    # numbers on single line without separator
    # numbers = [int(n) for n in file.read()]

    # single line numbers, comma separated
    # numbers = [int(n) for n in file.read().split(",")]

    # numbers on multiple lines
    numbers = [int(l.strip()) for l in file.readlines()]

    # tuple split by "(" on multiple lines
    # items = [tuple(l.strip().split(")")) for l in file.readlines()]


def part1():
    return "part 1"


def part2():
    return "part 2"


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
