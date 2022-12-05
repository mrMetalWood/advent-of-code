import os
import re
import copy

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    s = [
        ["R", "G", "H", "Q", "S", "B", "T", "N"],
        ["H", "S", "F", "D", "P", "Z", "J"],
        ["Z", "H", "V"],
        ["M", "Z", "J", "F", "G", "H"],
        ["T", "Z", "C", "D", "L", "M", "S", "R"],
        ["M", "T", "W", "V", "H", "Z", "J"],
        ["T", "F", "P", "L", "Z"],
        ["Q", "V", "W", "S"],
        ["W", "H", "L", "M", "T", "D", "N", "C"],
    ]

    instructions = file.read().split("\n\n")[1]
    instructions = [
        re.split("move | from | to ", n.strip()) for n in instructions.split("\n") if n
    ]
    instructions = [[int(j) for j in i if j] for i in instructions]


def process(stacks, p2=False):
    for instruction in instructions:

        [amount, move_from, move_to] = instruction

        items_to_move = stacks[move_from - 1][-amount:]
        stacks[move_to - 1].extend(items_to_move if p2 else reversed(items_to_move))
        stacks[move_from - 1] = stacks[move_from - 1][:-amount]

    result = ""
    for stack in stacks:
        result += stack[-1]

    return result


print(f"Part 1: {process(copy.deepcopy(s))}")  # PTWLTDSJV
print(f"Part 2: {process(copy.deepcopy(s), True)}")  # WZMFVGGZP
