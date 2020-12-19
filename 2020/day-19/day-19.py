import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]

    r, messages = lines[:135], lines[136:]
    rules = {n: c for n, c in [i.split(": ") for i in r]}


def solve(rules):
    reg = rules["0"]
    while re.search(r"\d", reg):
        next_number = re.findall(r"(?:^| )(\d+)(?:$| )", reg)[0].strip()
        reg = re.sub(
            rf"(?:^| )({next_number})(?:$| )", f" ( {rules[next_number]} ) ", reg
        )

    reg = "^" + reg.replace(" ", "").replace('"', "") + "$"

    return sum([1 for m in messages if re.match(reg, m)])


def part2(rules):
    update = {
        "8": "42 | 42 908",
        "908": "42 | 42 918",
        "918": "42 | 42 928",
        "928": "42 | 42 938",
        "938": "42 | 42 948",
        "948": "42 | 42 958",
        "958": "42 | 42 968",
        "968": "42 | 42 978",
        "978": "42",
        "11": "42 31 | 42 9011 31",
        "9011": "42 31 | 42 9111 31",
        "9111": "42 31 | 42 9211 31",
        "9211": "42 31 | 42 9311 31",
        "9311": "42 31 | 42 9411 31",
        "9411": "42 31 | 42 9511 31",
        "9511": "42 31 | 42 9611 31",
        "9611": "42 31 | 42 9711 31",
        "9711": "42 31 | 42 9811 31",
        "9811": "42 31",
        "0": "8 11",
    }
    rules = rules | update
    return solve(rules)


print(f"Part 1: {solve(rules)}")  # 216
# print(f"Part 2: {part2(rules)}")  # 400
