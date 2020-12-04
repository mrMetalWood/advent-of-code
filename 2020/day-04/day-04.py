import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:

    lines = [l.strip() for l in file.readlines()]
    lines.append("")

    passports = []
    passport = {}

    for line in lines:
        if not line:
            passports.append(passport)
            passport = {}
        else:
            items = line.split(" ")
            for item in items:
                key, value = item.split(":")
                passport[key] = value


def has_all_fields(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all([field in passport for field in required_fields])


def part1():
    return len(list(filter(has_all_fields, passports)))


def part2():
    passports_with_required_fields = list(filter(has_all_fields, passports))
    count = 0

    for p in passports_with_required_fields:
        valid = True

        if not 1920 <= int(p["byr"]) <= 2002:
            valid = False
        if not 2010 <= int(p["iyr"]) <= 2020:
            valid = False
        if not 2020 <= int(p["eyr"]) <= 2030:
            valid = False

        hgt_unit = p["hgt"][-2:]
        hgt_value = p["hgt"][:-2]
        if hgt_unit not in ["cm", "in"]:
            valid = False
        if hgt_unit == "cm" and not 150 <= int(hgt_value) <= 193:
            valid = False
        if hgt_unit == "in" and not 59 <= int(hgt_value) <= 76:
            valid = False

        if not re.search(r"^#[0-9a-f]{6}$", p["hcl"]) or len(p["hcl"]) != 7:
            valid = False
        if p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            valid = False
        if not re.search(r"\d{9}$", p["pid"]) or len(p["pid"]) != 9:
            valid = False

        if valid:
            count += 1

    return count


print(f"Part 1: {part1()}")  # 216
print(f"Part 2: {part2()}")  # 150
