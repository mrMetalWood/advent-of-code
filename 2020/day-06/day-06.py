from collections import defaultdict
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    groups = [line.strip() for line in file.read().split("\n\n")]


def part1():
    return sum([len(set(group.replace("\n", ""))) for group in groups])


def part2():
    sum = 0
    for group in [group.split("\n") for group in groups]:
        yes_count = defaultdict(lambda: 0)
        for person in group:
            for answer in person:
                yes_count[answer] = yes_count[answer] + 1
        sum += len(list(filter(lambda v: v[1] == len(group), yes_count.items())))
    return sum


print(f"Part 1: {part1()}")  # 6310
print(f"Part 2: {part2()}")  # 3193
