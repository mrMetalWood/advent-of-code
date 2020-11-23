# Not happy with this one... kinda laborious

from shapely.geometry import LineString

with open("2019/day-03/input.txt", "r") as file:
    wires = [wire.strip().split(",") for wire in file.readlines()]


def get_wire_intersections(wires):
    lines = []

    for wire in wires:
        wire_coords = [(0, 0)]
        x = 0
        y = 0

        for instruction in wire:
            direction = instruction[0]
            value = int(instruction[1:])

            if direction == "U":
                wire_coords.append((x, y + value))
                y += value
            if direction == "R":
                wire_coords.append((x + value, y))
                x += value
            if direction == "D":
                wire_coords.append((x, y - value))
                y -= value
            if direction == "L":
                wire_coords.append((x - value, y))
                x -= value

        lines.append(wire_coords)

    wire1_line = LineString(lines[0])
    wire2_line = LineString(lines[1])

    return list(
        map(
            lambda point: (int(point.x), int(point.y)),
            wire1_line.intersection(wire2_line),
        )
    )


def get_steps(coords):
    total = []
    for wire in wires:
        x = 0
        y = 0
        step = 0
        for instruction in wire:
            direction = instruction[0]
            value = int(instruction[1:])

            if direction == "U":
                for i in range(1, value + 1):
                    step += 1
                    y += 1
                    if x == coords[0] and y == coords[1]:
                        total.append(step)
                        break
            if direction == "R":
                for i in range(1, value + 1):
                    step += 1
                    x += 1
                    if x == coords[0] and y == coords[1]:
                        total.append(step)
                        break
            if direction == "D":
                for i in range(1, value + 1):
                    step += 1
                    y -= 1
                    if x == coords[0] and y == coords[1]:
                        total.append(step)
                        break
            if direction == "L":
                for i in range(1, value + 1):
                    step += 1
                    x -= 1
                    if x == coords[0] and y == coords[1]:
                        total.append(step)
                        break

    return total


def part1():
    return sorted(
        list(
            map(
                lambda point: abs(point[0]) + abs(point[1]),
                get_wire_intersections(wires),
            )
        )
    )[1]


def part2():
    return sorted(
        list(map(lambda point: sum(get_steps(point)), get_wire_intersections(wires)))
    )[1]


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")


# Super smooth solution by fogleman <3  https://github.com/fogleman
# with open('2019/day-03/input.txt', 'r') as file:
#     wires = [wire.strip() for wire in file.readlines()]

# DIRS = {
#     'U': (0, -1), 'D': (0, 1),
#     'L': (-1, 0), 'R': (1, 0)
# }


# def parse(line):
#     result = {}
#     x = y = steps = 0
#     for token in line.split(','):
#         (dx, dy), n = DIRS[token[0]], int(token[1:])
#         for _ in range(n):
#             x, y, steps = x + dx, y + dy, steps + 1
#             result.setdefault((x, y), steps)
#     return result


# a = parse(wires[0])
# b = parse(wires[1])
# x = set(a) & set(b)


# print(min(sum(map(abs, p)) for p in x))
# print(min(a[k] + b[k] for k in x))
