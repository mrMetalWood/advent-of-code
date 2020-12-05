import math
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    passes = [l.strip() for l in file.readlines()]
    bin_map = {"F": "0", "B": "1", "L": "0", "R": "1"}

ids = []
for p in passes:
    row = int("".join([bin_map[i] for i in p[:7]]), 2)
    col = int("".join([bin_map[i] for i in p[-3:]]), 2)
    ids.append(row * 8 + col)
ids = sorted(ids)

part1 = ids[-1]
part2 = [id for id in range(ids[0], ids[-1] + 1) if id not in ids][0]

print(f"Part 1: {part1}")  # 935
print(f"Part 2: {part2}")  # 743
