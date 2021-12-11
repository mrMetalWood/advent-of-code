import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    items = [re.split(" \| | ", l.strip()) for l in file.readlines()]
    items = [["".join(sorted(j)) for j in i] for i in items]

    # Finding Numbers:
    # -> 1 (given)
    # -> 7 (given)
    # -> 4 (given)
    # -> 8 (given)
    # all of 7 and 5 chars -> 3
    # all of 3 and 6 chars -> 9
    # all of 1 and 6 chars -> 0
    # 6 chars -> 6
    # 5 now has all of 6 -> 5
    # -> 2


def sublist(lst1, lst2):
    return all([c in lst1 for c in lst2])


def solve(mode):
    count = 0
    for row in items:
        signals = row[:10]
        output = row[10:]
        mapping = {}

        for signal in signals:
            if len(signal) == 2:
                mapping[1] = signal
            if len(signal) == 3:
                mapping[7] = signal
            if len(signal) == 4:
                mapping[4] = signal
            if len(signal) == 7:
                mapping[8] = signal

        signals.remove(mapping[1])
        signals.remove(mapping[7])
        signals.remove(mapping[4])
        signals.remove(mapping[8])

        three_signal = [s for s in signals if sublist(s, mapping[7]) and len(s) == 5][0]
        mapping[3] = three_signal
        signals.remove(three_signal)

        nine_signal = [s for s in signals if sublist(s, mapping[3]) and len(s) == 6][0]
        mapping[9] = nine_signal
        signals.remove(nine_signal)

        zero_signal = [s for s in signals if sublist(s, mapping[1]) and len(s) == 6][0]
        mapping[0] = zero_signal
        signals.remove(zero_signal)

        six_signal = [s for s in signals if len(s) == 6][0]
        mapping[6] = six_signal
        signals.remove(six_signal)

        five_signal = [s for s in signals if sublist(mapping[6], s)][0]
        mapping[5] = five_signal
        signals.remove(five_signal)

        mapping[2] = signals[0]
        signals.remove(signals[0])

        number_string = ""
        for output_chars in output:
            for (signal, chars) in mapping.items():
                if output_chars == chars:
                    if mode == "p1":
                        if signal == 1 or signal == 4 or signal == 7 or signal == 8:
                            count += 1
                    number_string += str(signal)

        if mode == "p2":
            count += int(number_string)

    return count


print(f"Part 1: {solve('p1')}")  # 310
print(f"Part 2: {solve('p2')}")  # 915941
