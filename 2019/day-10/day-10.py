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


def part1():
    count = defaultdict(int)
    for start in asteroids:
        asteroids_copy = asteroids.copy()
        asteroids_copy.remove(start)
        for end in asteroids_copy:

            # translate to origin
            new_end_x = end[0] - start[0]
            new_end_y = end[1] - start[1]

            gcd = math.gcd(new_end_x, new_end_y)

            visible = True
            for i in range(1, gcd):
                next_x_on_line = start[0] + new_end_x / gcd * i
                next_y_on_line = start[1] + new_end_y / gcd * i

                if (next_x_on_line, next_y_on_line) in asteroids:
                    visible = False

            if visible:
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


print(f"Part 1: {part1()[1]}")

# output from part1 ((22, 19), 282)
print(f"Part 2: {part2(part1()[0])}")
