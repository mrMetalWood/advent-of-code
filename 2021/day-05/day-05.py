from collections import defaultdict
import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    items = [
        [int(i) for i in re.split(",| -> |, ", l.strip())] for l in file.readlines()
    ]

    lines = []
    for x1, y1, x2, y2 in items:
        point1, point2 = (x1, y1), (x2, y2)
        m = b = None

        if x2 != x1:
            m = (y2 - y1) / (x2 - x1)
            b = y1 - (m * x1)

        line = {"point1": point1, "point2": point2, "m": m, "b": b}
        lines.append(line)


def count_overlap(l):
    grid = defaultdict(lambda: 0)

    for line in l:
        if line["m"] == None:
            s = list(sorted([line["point1"][1], line["point2"][1]]))
            for i in range(s[0], s[1] + 1):
                grid[(line["point1"][0], i)] += 1
        else:
            s = list(sorted([line["point1"][0], line["point2"][0]]))
            for i in range(s[0], s[1] + 1):
                # y = mx + b
                y = line["m"] * i + line["b"]

                if y.is_integer():
                    grid[(i, y)] += 1

    return len([v for v in grid.values() if v > 1])


def part1():
    return count_overlap(
        list(
            filter(
                lambda x: x["point1"][0] == x["point2"][0]
                or x["point1"][1] == x["point2"][1],
                lines,
            )
        )
    )


def part2():
    return count_overlap(lines)


print(f"Part 1: {part1()}")  # 6856
print(f"Part 2: {part2()}")  # 20666
