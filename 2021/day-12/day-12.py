from collections import defaultdict
import os


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    connections = defaultdict(list)

    for line in file.readlines():
        pair = line.strip().split("-")
        for p1, p2 in zip(pair, reversed(pair)):
            if p2 != "start":
                connections[p1].append(p2)
    del connections["end"]


def part1(data, path):
    final = 0
    for point in data[path[-1]]:
        if point.isupper() or not point in path:
            final += 1 if point == "end" else part1(data, path + [point])
    return final


def part2(data, path):
    final = 0
    for point in data[path[-1]]:
        final += (
            1
            if point == "end"
            else (part2, part1)[point.islower() and point in path](data, path + [point])
        )
    return final


print(f"Part 1: {part1(connections, ['start'])}")  # 3292
print(f"Part 2: {part2(connections, ['start'])}")  # 89592
