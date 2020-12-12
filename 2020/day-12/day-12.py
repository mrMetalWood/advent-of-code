import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    instructions = [l.strip() for l in file.readlines()]
    instructions = [(i[:1], int(i[1:])) for i in instructions]

    DIRS = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    MAPPING = {"N": 0, "E": 1, "S": 2, "W": 3}


def part1():
    position, current_dir = [0, 0], 1

    for (op, val) in instructions:
        if op == "R":
            current_dir = (current_dir + val // 90) % len(DIRS)
        elif op == "L":
            current_dir = (current_dir - val // 90) % len(DIRS)
        elif op == "F":
            d = DIRS[current_dir]
            position = [position[0] + d[0] * val, position[1] + d[1] * val]
        else:
            d = DIRS[MAPPING[op]]
            position = [position[0] + d[0] * val, position[1] + d[1] * val]

    return abs(position[0]) + abs(position[1])


def part2():
    position, waypoint = [0, 0], [10, 1]

    for (op, val) in instructions:
        if op == "L":
            for _ in range(val // 90):
                waypoint = [waypoint[1] * -1, waypoint[0]]
        elif op == "R":
            for _ in range(val // 90):
                waypoint = [waypoint[1], waypoint[0] * -1]
        elif op == "F":
            position = [
                position[0] + waypoint[0] * val,
                position[1] + waypoint[1] * val,
            ]
        else:
            d = DIRS[MAPPING[op]]
            waypoint = [waypoint[0] + d[0] * val, waypoint[1] + d[1] * val]

    return abs(position[0]) + abs(position[1])


print(f"Part 1: {part1()}")  # 1186
print(f"Part 2: {part2()}")  # 47806
