from collections import defaultdict
import os


def solve(spoken_number_count):
    ledger = defaultdict(lambda: [])
    for idx, n in enumerate([1, 17, 0, 10, 18, 11, 6]):
        ledger[int(n)].append(idx + 1)
    spoken_number = list(ledger.keys())[-1]

    for i in range(len(ledger) + 1, spoken_number_count + 1):
        if len(ledger[spoken_number]) >= 2:
            spoken_number = ledger[spoken_number][-1] - ledger[spoken_number][-2]
        else:
            spoken_number = 0
        ledger[spoken_number].append(i)
    return spoken_number


print(f"Part 1: {solve(2020)}")  # 595
print(f"Part 2: {solve(30000000)}")  # 1708310
