import os


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    crabs = [int(n) for n in file.read().split(",")]
    min_pos, max_pos = min(crabs), max(crabs)


def get_min_fuel(mode):
    min_fuel, fuel = float("inf"), 0

    for pos in range(min_pos, max_pos + 1):
        for crab in crabs:
            distance = abs(crab - pos)
            fuel += distance if mode == "p1" else distance * (distance + 1) // 2
        if fuel < min_fuel:
            min_fuel = fuel
        fuel = 0
    return min_fuel


print(f"Part 1: {get_min_fuel('p1')}")  # 364898
print(f"Part 2: {get_min_fuel('p2')}")  # 104149091
