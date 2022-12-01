import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    calories = [l.strip() for l in file.readlines()]

    elves, elf = [], 0
    for cal in calories:
        if cal == "":
            elves.append(elf)
            elf = 0
        else:
            elf += int(cal)

    print(f"Part 1: {max(elves)}")  # 67633
    print(f"Part 2: {sum(sorted(elves)[-3:])}")  # 199628
