from collections import defaultdict
import itertools as it
import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]


def part1():
    memory = defaultdict(lambda: ["0"] * 36)

    mask = None
    for line in lines:
        if line.startswith("mask"):
            mask = line.split()[-1]
        else:
            _, address, value = re.split(r"\[|\] = ", line)
            value = bin(int(value))[2:]
            idx = 35
            for v, m in it.zip_longest(value[::-1], mask[::-1], fillvalue="0"):
                if m == "0":
                    memory[address][idx] = "0"
                if m == "1":
                    memory[address][idx] = "1"
                if m == "X":
                    memory[address][idx] = v
                idx -= 1

    return sum(map(lambda i: int("".join(i), 2), memory.values()))


def part2():
    memory = {}

    mask = None
    for line in lines:
        if line.startswith("mask"):
            mask = line.split()[-1]

        else:
            _, address, value = re.split(r"\[|\] = ", line)
            address = bin(int(address))[2:]
            final_address = ["0"] * 36
            floating_indices = []
            idx = 35
            for a, m in it.zip_longest(address[::-1], mask[::-1], fillvalue="0"):
                if m == "0":
                    final_address[idx] = a
                if m == "1":
                    final_address[idx] = "1"
                if m == "X":
                    final_address[idx] = "X"
                    floating_indices.append(idx)
                idx -= 1

            for combination in it.product(["0", "1"], repeat=len(floating_indices)):
                for idx_id, floating_idx in enumerate(floating_indices):
                    final_address[floating_idx] = combination[idx_id]
                memory[int("".join(final_address), 2)] = int(value)

    return sum(memory.values())


print(f"Part 1: {part1()}")  # 8332632930672
print(f"Part 2: {part2()}")  # 4753238784664
