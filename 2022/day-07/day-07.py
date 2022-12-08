from collections import defaultdict
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]

    sizes = defaultdict(lambda: 0)
    current_dir_stack = []
    count = 1

    for line in lines:
        line_split = line.split(" ")

        if line == "$ cd ..":
            current_dir_stack.pop()
        elif line.startswith("$ cd"):
            current_dir_stack.append(line_split[-1] + str(count))
            count += 1

        if line_split[0].isnumeric():
            for item in current_dir_stack:
                sizes[item] += int(line_split[0])

    total = 70_000_000
    needed = 30_000_000
    need_to_free_at_least = needed - (total - max(list(sizes.values())))

print(f"Part 1: {sum(filter(lambda x: x <= 100000, list(sizes.values())))}")  # 1611443
print(
    f"Part 2: {min(filter(lambda x: x > need_to_free_at_least, list(sizes.values())))}"
)  # 2086088
