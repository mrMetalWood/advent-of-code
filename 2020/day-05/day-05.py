import math
import os


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    boardingpasses = [l.strip() for l in file.readlines()]
    bin_map = {"F": "0", "B": "1", "L": "0", "R": "1"}


def get_pass_ids():
    ids = []
    for boardingpass in boardingpasses:
        row = int("".join([bin_map[i] for i in boardingpass[:7]]), 2)
        col = int("".join([bin_map[i] for i in boardingpass[-3:]]), 2)
        ids.append(row * 8 + col)
    return ids


def part1():
    return sorted(get_pass_ids())[-1]


def part2():
    ids = sorted(get_pass_ids())
    return [id for id in range(ids[0], ids[-1] + 1) if id not in ids][0]


print(f"Part 1: {part1()}")  # 935
print(f"Part 2: {part2()}")  # 743