import os
import copy

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    ins = [[l.split()[0], int(l.split()[1])] for l in file.readlines()]


def run(instructions, acc, pointer):
    op, value = instructions[pointer]
    if op == "acc":
        acc += value
        pointer += 1
    if op == "jmp":
        pointer += value
    if op == "nop":
        pointer += 1
    return (acc, pointer)


def part1():
    acc, pointer, seen = 0, 0, []
    while pointer not in seen:
        seen.append(pointer)
        acc, pointer = run(ins, acc, pointer)
    return acc


def part2():
    global_acc = 0
    for i in range(len(ins)):
        ins_copy, acc, pointer, seen = copy.deepcopy(ins), 0, 0, []

        if ins_copy[i][0] == "jmp":
            ins_copy[i][0] = "nop"
        elif ins_copy[i][0] == "nop":
            ins_copy[i][0] = "jmp"

        while pointer not in seen:
            seen.append(pointer)
            if pointer == len(ins_copy):
                global_acc = acc
                break
            acc, pointer = run(ins_copy, acc, pointer)

    return global_acc


print(f"Part 1: {part1()}")  # 1941
print(f"Part 2: {part2()}")  # 2096
