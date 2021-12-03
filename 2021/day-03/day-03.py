from collections import defaultdict
import os


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    report_lines = [l.strip() for l in file.readlines()]


def count_occurances(report_numbers):
    counts = defaultdict(lambda: {"0": 0, "1": 0})
    for line in report_numbers:
        for idx, value in enumerate(line):
            counts[idx][value] += 1
    return counts


def filter_list(l, idx, mode):
    counts = count_occurances(l)

    if counts[idx]["0"] > counts[idx]["1"]:
        l = list(filter(lambda b: b[idx] == ("0" if mode == "most" else "1"), l))
    if counts[idx]["0"] < counts[idx]["1"]:
        l = list(filter(lambda b: b[idx] == ("1" if mode == "most" else "0"), l))
    if counts[idx]["0"] == counts[idx]["1"]:
        l = list(filter(lambda b: b[idx] == ("1" if mode == "most" else "0"), l))

    return l


def part1():
    gamma_rate = epsilon_rate = ""
    counts = count_occurances(report_lines)

    for value in counts.values():
        if value["0"] > value["1"]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2():
    oxygen_list = co2_list = report_lines.copy()

    idx1 = 0
    while len(oxygen_list) > 1:
        oxygen_list = filter_list(oxygen_list, idx1, "most")
        idx1 += 1

    idx2 = 0
    while len(co2_list) > 1:
        co2_list = filter_list(co2_list, idx2, "least")
        idx2 += 1

    return int(oxygen_list[0], 2) * int(co2_list[0], 2)


print(f"Part 1: {part1()}")  # 1997414
print(f"Part 2: {part2()}")  # 1032597
