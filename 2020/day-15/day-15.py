ledger = {n: idx + 1 for idx, n in enumerate([1, 17, 0, 10, 18, 11, 6])}
spoken_number = list(ledger)[-1]

for turn in range(len(ledger), 30000000):
    ledger[spoken_number], spoken_number = turn, turn - ledger.get(spoken_number, turn)
    if turn == 2020 - 1:
        print(f"Part 1: {spoken_number}")  # 595
print(f"Part 2: {spoken_number}")  # 1708310
