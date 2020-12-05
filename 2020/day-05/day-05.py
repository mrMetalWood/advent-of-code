with open("2020/day-05/input.txt", "r") as file:
    ids = sorted([
        int("".join([str(int(i=="B")) for i in p[:7]]), 2) * 8 + int("".join([str(int(i=="R")) for i in p[-3:]]), 2)
        for p in [l.strip() for l in file.readlines()]
    ])
    print(f"Part 1: {ids[-1]}")  # 935
    print(f"Part 2: {[id for id in range(ids[0], ids[-1] + 1) if id not in ids][0]}")  # 743
