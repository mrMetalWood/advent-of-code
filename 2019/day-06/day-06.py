with open("2019/day-06/input.txt", "r") as file:
    p = [tuple(planet.strip().split(")")) for planet in file.readlines()]


def part1():
    planets = p.copy()
    com = next(x for x in planets if x[0] == "COM")
    planets.remove(com)
    levels, level = [[com[1]]], 1

    while len(planets):
        level_planets = []
        for planet in levels[level - 1]:
            while True:
                try:
                    n = next(x for x in planets if x[0] == planet)
                    planets.remove(n)
                    level_planets.append(n[1])

                except StopIteration:
                    break

        levels.append(level_planets)
        level += 1

    count = 0
    for index, level in enumerate(levels):
        count += len(level) * (index + 1)

    return count


def get_path(start, planets):
    path = []
    current_position = start
    while True:
        try:
            n = next(x for x in planets if x[1] == current_position[0])
            path.append(n[1])
            current_position = n
        except StopIteration:
            break
    return path


def part2():
    planets = p.copy()

    path_santa = get_path(next(x for x in planets if x[1] == "SAN"), planets)
    path_you = get_path(next(x for x in planets if x[1] == "YOU"), planets)

    for index, planet in enumerate(path_you):
        if planet in path_santa:
            return index + path_santa.index(planet)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
