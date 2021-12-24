from collections import defaultdict
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    [dots_raw, folds_raw] = file.read().split("\n\n")

    dots = defaultdict(lambda: " ")
    for dot in dots_raw.split("\n"):
        coords = dot.split(",")
        dots[(int(coords[0]), int(coords[1]))] = "#"

    folds = [f[11:].split("=") for f in folds_raw.strip().split("\n")]


fold_count = 0
for [axis, value] in folds:
    fold_count += 1
    value = int(value)
    new_dots = dots.copy()
    for (coords, v) in dots.items():
        if axis == "x":
            # if to the right of the fold
            if coords[0] > value and v == "#":
                distance_to_fold = coords[0] - value
                new_coords = (value - distance_to_fold, coords[1])
                new_dots[coords] = " "
                new_dots[new_coords] = "#"
        if axis == "y":
            # if below the fold
            if coords[1] > value and v == "#":
                distance_to_fold = coords[1] - value
                new_coords = (coords[0], value - distance_to_fold)
                new_dots[coords] = " "
                new_dots[new_coords] = "#"
    dots = new_dots

    if fold_count == 1:
        print(f"Part 1: {len([val for (_, val) in dots.items() if val == '#'])}")

min_x = min([coords[0] for (coords, val) in dots.items() if val == "#"])
max_x = max([coords[0] for (coords, val) in dots.items() if val == "#"])
min_y = min([coords[1] for (coords, val) in dots.items() if val == "#"])
max_y = max([coords[1] for (coords, val) in dots.items() if val == "#"])

print("Part 2:")
for y in range(min_y, max_y + 1):
    row = ""
    for x in range(min_x, max_x + 1):
        row += dots[(x, y)]
    print(row)
