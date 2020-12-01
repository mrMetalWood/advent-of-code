import os

input_file = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_file, "r") as file:
    numbers = [int(l.strip()) for l in file.readlines()]

for n in numbers:
    for m in numbers:
        if n + m == 2020:
            part1 = n * m
        for l in numbers:
            if n + m + l == 2020:
                part2 = n * m * l


print(f"Part 1: {part1}")  # 1010299
print(f"Part 2: {part2}")  # 42140160
