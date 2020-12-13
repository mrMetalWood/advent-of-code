import math
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]


def part1():
    time = int(lines[0])
    busses = [int(i) for i in lines[1].split(",") if i != "x"]
    id = 0
    min_time = max(busses) + 1
    for bus in busses:
        waiting_time = bus - (time % bus)
        if waiting_time < min_time:
            min_time = waiting_time
            id = bus
    return id * min_time


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def part2():
    busses = [(int(bus), i) for i, bus in enumerate(lines[1].split(",")) if bus != "x"]
    increment = busses[0][0]
    time = 0

    for bus, offset in busses[1:]:
        while (time + offset) % bus != 0:
            time += increment
        increment = lcm(increment, bus)  # works because all busses are primes

    return time


print(f"Part 1: {part1()}")  # 2545
print(f"Part 2: {part2()}")  # 266204454441577
