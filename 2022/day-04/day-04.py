import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    items = [re.split("-|,|-", l.strip()) for l in file.readlines()]

    count_1 = count_2 = 0
    for section_boundaries in [[int(j) for j in i] for i in items]:
        sections_1 = set(range(section_boundaries[0], section_boundaries[1] + 1))
        sections_2 = set(range(section_boundaries[2], section_boundaries[3] + 1))

        # part 1
        if len(sections_1 | sections_2) == max(len(sections_1), len(sections_2)):
            count_1 += 1

        # part2
        if len(sections_1 & sections_2) > 0:
            count_2 += 1

print(f"Part 1: {count_1}")  # 582
print(f"Part 2: {count_2}")  # 893
