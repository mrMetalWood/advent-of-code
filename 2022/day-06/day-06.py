import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    letters = [n for n in file.read().strip()]


def count_until_unique(amount):
    for i in range(len(letters)):
        if len(set(letters[i : i + amount])) == amount:
            return i + amount


print(f"Part 1: {count_until_unique(4)}")  # 1876
print(f"Part 2: {count_until_unique(14)}")  # 2202
