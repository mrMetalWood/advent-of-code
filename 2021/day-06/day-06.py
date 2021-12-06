from collections import defaultdict
import os


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    numbers = [int(n) for n in file.read().split(",")]


def part1():
    fish = numbers.copy()

    for _ in range(80):
        new_fishies = []
        new_count = 0
        for f in fish:
            new_fish = f - 1
            if new_fish == -1:
                new_fish = 6
                new_count += 1

            new_fishies.append(new_fish)

        for _ in range(new_count):
            new_fishies.append(8)

        fish = new_fishies

    return len(fish)


def part2():
    initial_fish = numbers.copy()
    fishies = defaultdict(lambda: 0)

    for fish in initial_fish:
        fishies[fish] += 1

    for _ in range(256):
        new_fishies = defaultdict(lambda: 0)
        for fish_number, count in fishies.items():
            new_fish = fish_number - 1
            if new_fish == -1:
                new_fish = 6
                new_fishies[8] += count
            new_fishies[new_fish] += count
        fishies = new_fishies

    return sum([count for count in fishies.values()])


print(f"Part 1: {part1()}")  # 388739
print(f"Part 2: {part2()}")  # 1741362314973
