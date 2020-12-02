import os

input_file = os.path.join(os.path.dirname(__file__), "input.txt")


with open(input_file, "r") as file:

    def split_item(item):
        instruction, password = item.split(":")
        letter = instruction.strip()[-1]
        min, max = instruction.strip().split(" ")[0].split("-")

        return (int(min), int(max), letter, password.strip())

    items = [split_item(l) for l in file.readlines()]


def part1():
    def is_valid(min, max, letter, password):
        return min <= password.count(letter) <= max

    return len(list(filter(lambda item: is_valid(*item), items)))


def part2():
    def is_valid(index1, index2, letter, password):
        return (password[index1 - 1] == letter) != (password[index2 - 1] == letter)

    return len(list(filter(lambda item: is_valid(*item), items)))


print(f"Part 1: {part1()}")  # 483
print(f"Part 2: {part2()}")  # 482
