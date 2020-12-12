import os
from collections import Counter
from copy import deepcopy

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [[m for m in l.strip()] for l in file.readlines()]
    DIRS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def simulation(threshold):
    state = deepcopy(lines)
    previous_states = set()

    while True:
        new_state = deepcopy(state)
        for y in range(len(state)):
            for x in range(len(state[0])):
                current_value = state[y][x]
                if current_value == ".":
                    continue

                adjacent = ""
                for (dx, dy) in DIRS:
                    n_x = x + dx
                    n_y = y + dy
                    if 0 <= n_x < len(state[0]) and 0 <= n_y < len(state):
                        value = state[n_y][n_x]

                        while value == "." and threshold == 5:  # part2
                            n_x = n_x + dx
                            n_y = n_y + dy
                            if 0 <= n_x < len(state[0]) and 0 <= n_y < len(state):
                                value = state[n_y][n_x]
                            else:
                                break

                        adjacent += value

                counts = Counter(adjacent)

                if current_value == "L" and "#" not in counts:
                    new_state[y][x] = "#"
                elif current_value == "#" and counts["#"] >= threshold:
                    new_state[y][x] = "L"

        string_state = "".join(["".join(line) for line in new_state])
        if string_state in previous_states:
            break

        previous_states.add(string_state)
        state = new_state

    return Counter("".join(["".join(line) for line in state]))["#"]


print(f"Part 1: {simulation(4)}")
print(f"Part 2: {simulation(5)}")
