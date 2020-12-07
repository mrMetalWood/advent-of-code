from collections import deque
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    colors = {}
    for rule in [l.strip() for l in file.readlines()]:
        color, contents = rule.split(" bags contain ")
        contents = [
            (" ".join(i.split()[1:3]), int(i.split()[0]))
            for i in contents.split(",")
            if i.split()[0].isnumeric()
        ]
        colors[color] = contents


def part1():
    color_queue, colors_with_shiny_gold = deque(["shiny gold"]), set()

    while color_queue:
        current_color = color_queue.popleft()
        for color in colors:
            for (color_name, _) in colors[color]:
                if color_name == current_color:
                    color_queue.append(color)
                    colors_with_shiny_gold.add(color)

    return len(colors_with_shiny_gold)


def part2():
    def count_bags(color):
        count = 1
        for (bag_color, amount) in colors[color]:
            count += count_bags(bag_color) * amount
        return count

    return count_bags("shiny gold") - 1


print(f"Part 1: {part1()}")  # 139
print(f"Part 2: {part2()}")  # 58175
