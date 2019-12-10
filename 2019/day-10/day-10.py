from collections import defaultdict
import math
import itertools

with open('2019/day-10/input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

asteroids = []
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell == '#':
            asteroids.append((x, y))


def view_is_blocked(start, middle, end):
    startX, startY = start
    middleX, middleY = middle
    endX, endY = end

    is_vertical = startX == middleX or startX == endX
    is_horizontal = startY == middleY or startY == endY

    in_vertical_range = startY < middleY < endY or startY > middleY > endY
    in_horizontal_range = startX < middleX < endX or startX > middleX > endX

    if is_vertical:
        return in_vertical_range and startX == middleX == endX
    if is_horizontal:
        return in_horizontal_range and startY == middleY == endY

    slope_to_end = (endY - startY) / (endX - startX)
    slope_to_middle = (middleY - startY) / (middleX - startX)

    if slope_to_end == slope_to_middle and in_vertical_range and in_horizontal_range:
        return True

    return False


def part1():
    count = defaultdict(int)
    for start in asteroids:
        asts2 = asteroids.copy()
        asts2.remove(start)
        for end in asts2:
            asts3 = asts2.copy()
            asts3.remove(end)
            if any([view_is_blocked(start, middle, end) for middle in asts3]):
                # something is blocking the view
                pass
            else:
                count[start] = count[start] + 1

    return max(list(count.items()), key=lambda i: i[1])


def part2(laser_base):
    asteroids_copy = asteroids.copy()
    asteroids_copy.remove(laser_base)
    degrees = defaultdict(list)

    for asteroid in asteroids_copy:
        rad = myradians = math.atan2(
            asteroid[1]-laser_base[1], asteroid[0]-laser_base[0]
        )
        degrees[math.degrees(rad)].append(asteroid)

    shifted_degrees = []
    for degree, asteroids_for_degree in degrees.items():
        asteroids_by_distance = sorted(
            asteroids_for_degree, key=lambda a: abs(
                a[0] - laser_base[1]) + abs(a[1] - laser_base[1])
        )
        asteroids_by_distance.reverse()
        shifted_degrees.append(
            ((degree + 360 + 90) % 360, asteroids_by_distance)
        )

    vaporized = []
    for degree in itertools.cycle(sorted(shifted_degrees, key=lambda i: i[0])):
        if len(degree[1]):
            vaporized.append(degree[1].pop())

        if len(vaporized) == 200:
            break

    return vaporized[-1][0] * 100 + vaporized[-1][1]


# print(f"Part 1: {part1()[1]}") # runs about 20 sec.

# output from part1 ((22, 19), 282)
print(f"Part 2: {part2((22, 19))}")
