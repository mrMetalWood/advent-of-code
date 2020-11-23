with open("2019/day-01/input.txt", "r") as file:
    masses = list(map(int, file.readlines()))


def get_fuel(mass):
    return mass // 3 - 2


def part1():
    return sum((map(get_fuel, masses)))


def part2():
    total_fuel = 0

    for mass in masses:
        fuel = mass

        while True:
            fuel = get_fuel(fuel)
            if fuel <= 0:
                break
            total_fuel += fuel

    return total_fuel


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
