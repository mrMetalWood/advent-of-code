import bisect
with open("2020/day-05/input.txt", "r") as file:
    bin_map = {"F": "0", "B": "1", "L": "0", "R": "1"}
    ids = sorted([
        int("".join([bin_map[i] for i in p[:7]]), 2) * 8 + int("".join([bin_map[i] for i in p[-3:]]), 2)
        for p in [l.strip() for l in file.readlines()]
    ])
    print(f"Part 1: {ids[-1]}")  # 935
    print(f"Part 2: {[id for id in range(ids[0], ids[-1] + 1) if id not in ids][0]}")  # 743
