from collections import defaultdict
from copy import deepcopy
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]
    grid = defaultdict(lambda: -1)

    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            grid[(x, y)] = int(cell)

    directions = [
        [0, -1],  # top
        [1, 0],  # right
        [0, 1],  # bottom
        [-1, 0],  # left
    ]

    visible_count = 0

    grid_copy = deepcopy(grid)
    scores = []
    for (x, y), height in grid_copy.items():
        visible = False
        score = 1
        for [deltaX, deltaY] in directions:
            count = 0
            next_item = grid[(x + deltaX, y + deltaY)]

            stop = False
            while next_item < height and not stop:

                count += 1
                next_item = grid[(x + (deltaX * count), y + (deltaY * count))]
                if next_item == -1:
                    count -= 1
                    visible = True
                    stop = True

            score *= count

        scores.append(score)

        if visible:
            visible_count += 1
    print(visible_count)  # 1560
    print(max(scores))  # 252000
