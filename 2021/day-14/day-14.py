from collections import defaultdict
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = file.readlines()
    polymer_template = lines[0].strip()
    rules = dict([l.strip().split(" -> ") for l in lines[2:]])


def solve(steps):
    pairs, counts = defaultdict(int), defaultdict(int)

    for p in polymer_template:
        counts[p] += 1

    for p1, p2 in zip(polymer_template, polymer_template[1:]):
        pairs[p1 + p2] += 1

    for _ in range(steps):
        new_pairs = pairs.copy()
        for (pair, pair_count) in pairs.items():
            if pair in rules:
                new_pairs[pair] -= pair_count
                if new_pairs[pair] == 0:
                    del new_pairs[pair]

                new_pairs[pair[0] + rules[pair]] += pair_count
                new_pairs[rules[pair] + pair[1]] += pair_count
                counts[rules[pair]] += pair_count

        pairs = new_pairs

    return max(counts.values()) - min(counts.values())


print(f"Part 1: {solve(10)}")  # 3411
print(f"Part 2: {solve(40)}")  # 7477815755570
