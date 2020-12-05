import os
import bisect

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    passes = [l.strip() for l in file.readlines()]

ids, bin_map = [], {"F": "0", "B": "1", "L": "0", "R": "1"}
for p in passes:
    row = int("".join([bin_map[i] for i in p[:7]]), 2)
    col = int("".join([bin_map[i] for i in p[-3:]]), 2)
    bisect.insort(ids, row * 8 + col)

print(f"Part 1: {ids[-1]}")  # 935
print(f"Part 2: {[id for id in range(ids[0], ids[-1] + 1) if id not in ids][0]}")  # 743
