from collections import defaultdict
from collections import deque
from functools import reduce
import itertools as it
import operator
import math
import os
import re

input = "916438275"


def play(cups, rounds):
    llist = {}
    for a, b in it.zip_longest(cups, cups[1:], fillvalue=cups[0]):
        llist[a] = b

    current = cups[0]
    biggest_cup = max(cups)

    for _ in range(rounds):
        pickup = []
        pointer = current
        for _ in range(3):
            next_item = llist[pointer]
            pickup.append(next_item)
            pointer = next_item

        destination = current - 1 if current - 1 > 0 else biggest_cup
        while destination in pickup:
            destination -= 1
            if destination < 1:
                destination = biggest_cup

        llist[current] = llist[pickup[-1]]
        llist[pickup[-1]] = llist[destination]

        pic = destination
        for pi in pickup:
            llist[pic] = pi
            pic = pi
        current = llist[current]
    return llist


def part1():
    final_list = play([int(i) for i in input], 100)

    seen = []
    cups = []
    next_item = 1
    while True:
        seen.append(next_item)
        cups.append(next_item)
        next_item = final_list[next_item]

        if next_item in seen:
            break

    return "".join([str(i) for i in cups[1:]])


def part2():
    cups = [int(i) for i in input]
    for i in range(len(cups) + 1, 1000000 + 1):
        cups.append(i)

    final_list = play(cups, 10000000)

    item = 1
    ans = 1
    for _ in range(2):
        ans *= final_list[item]
        item = final_list[item]
    return ans


print(f"Part  1: {part1()}")  # 39564287
print(f"Part 2: {part2()}")  # 404431096944
