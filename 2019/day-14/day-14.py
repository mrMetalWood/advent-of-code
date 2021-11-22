from collections import defaultdict

# from collections import deque
# from functools import reduce
# import itertools
# import operator
import math
import os

# import re

with open(os.path.join(os.path.dirname(__file__), "test2.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]
    lines = [l.split(" => ") for l in lines]
    recipes = []
    for line in lines:
        recipe = {}
        produced = line[1]
        needed = line[0].split(", ")
        needed = [(int(i.split()[0]), i.split()[1]) for i in needed]

        prod_value, prod_name = produced.split()
        recipe["produced"] = (int(prod_value), prod_name)
        recipe["needed"] = needed
        recipes.append(recipe)


def def_value():
    return 0


def part1():
    total = defaultdict(def_value)
    total_size = defaultdict(def_value)
    total_ore = defaultdict(def_value)

    def count_ore(amount, chemical):
        count = 0
        start = [recipe for recipe in recipes if recipe["produced"][1] == chemical][0]

        extra = math.ceil(amount / start["produced"][0]) % amount
        extra_name = start["produced"][1]
        extra_value = (extra * start["produced"][0]) % amount
        extra_size = start["produced"][0]
        extra_ore = start["needed"][0][0]
        total[extra_name] += extra_value
        total_size[extra_name] = extra_size
        total_size[extra_name] = extra_size
        total_ore[extra_name] = extra_ore

        if len(start["needed"]) == 1 and start["needed"][0][1] == "ORE":

            # print(amount, start["produced"][1], start["produced"][0])
            # print("need", extra * start["produced"][0])

            print(extra_value, extra_name, extra_size)

            count = start["needed"][0][0] * math.ceil(amount / start["produced"][0])
        else:
            for need in start["needed"]:
                count += count_ore(
                    need[0] * math.ceil(amount / start["produced"][0]), need[1]
                )
        return count

    total_count = count_ore(1, "FUEL")

    print(total.items(), total_size.items(), total_ore.items())

    # subtract = 0
    # for (a, b, c) in zip(total.items(), total_size.items(), total_ore.items()):
    #     subtract = (a[1] // b[1]) * c[1]

    # return total_count - subtract


def part2():
    return "part 2"


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
