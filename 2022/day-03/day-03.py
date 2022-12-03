import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    suitcases = [[char for char in l.strip()] for l in file.readlines()]


def increase_priority_sum(character):
    if character.isupper():
        return ord(character) - 38
    else:
        return ord(character) - 96


def part1():
    priority_sum = 0
    for suitcase in suitcases:
        middle_index = len(suitcase) // 2

        priority_sum += increase_priority_sum(
            list(
                set(suitcase[:middle_index]).intersection(set(suitcase[middle_index:]))
            )[0]
        )

    return priority_sum


def part2():
    priority_sum = 0

    for i in range(0, len(suitcases), 3):
        s_1 = suitcases[i]
        s_2 = suitcases[i + 1]
        s_3 = suitcases[i + 2]

        priority_sum += increase_priority_sum(
            list(set(s_1).intersection(set(s_2)).intersection(set(s_3)))[0]
        )

    return priority_sum


print(f"Part 1: {part1()}")  # 8139
print(f"Part 2: {part2()}")  # 2668
