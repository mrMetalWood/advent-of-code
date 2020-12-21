import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip().split(" (contains ") for l in file.readlines()]
    foods = []
    for line in lines:
        ingredients = line[0].split()
        allergens = [a[:-1] for a in line[1].split()]
        foods.append([ingredients, allergens])

    allergen_mapping = {}

    for idx, food in enumerate(foods):
        _, allergens = food
        for allergen in allergens:
            all_with_a = [set(food[0])]
            for idx2, f in enumerate(foods):
                if idx == idx2:
                    continue
                if allergen in f[1]:
                    all_with_a.append(set(f[0]))

            possible_with_a = set(all_with_a[0])
            for food_with_a in all_with_a[1:]:
                possible_with_a = possible_with_a.intersection(food_with_a)

            diff = list(possible_with_a.difference(set(allergen_mapping)))
            if len(diff) == 1:
                allergen_mapping[diff[0]] = allergen


def part1():
    ans = 0
    for food in foods:
        for ing in food[0]:
            if ing not in allergen_mapping:
                ans += 1

    return ans


def part2():
    return ",".join(
        [ing for ing, val in sorted(allergen_mapping.items(), key=lambda i: i[1])]
    )


print(f"Part 1: {part1()}")  # 2461
print(f"Part 2: {part2()}")  # ltbj,nrfmm,pvhcsn,jxbnb,chpdjkf,jtqt,zzkq,jqnhd
