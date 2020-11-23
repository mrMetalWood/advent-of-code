import itertools

with open("2019/day-16/input.txt", "r") as file:
    numbers = [int(n) for n in file.read()]


base_pattern = [0, 1, 0, -1]

patterns = []
for i, _ in enumerate(numbers):
    repeated_list = list(
        itertools.chain.from_iterable(itertools.repeat(x, i + 1) for x in base_pattern)
    )
    repeated_list.append(repeated_list.pop(repeated_list.index(0)))
    patterns.append(repeated_list)


def part1():
    phases = [numbers]
    for i in range(100):
        phase = []
        for pattern in patterns:
            result = 0
            for n, p in zip(phases[-1], itertools.cycle(pattern)):
                result += n * p
            phase.append(int(str(result)[-1]))
        phases.append(phase)
    return "".join(str(n) for n in phases[-1][:8])


def part2():
    message_offset = int("".join(str(n) for n in numbers[:7]))
    numbers_large = numbers * 10000
    numbers_needed = numbers_large[message_offset:]

    for _ in range(100):
        for i in reversed(range(len(numbers_needed) - 1)):
            numbers_needed[i] = (numbers_needed[i] + numbers_needed[i + 1]) % 10

    return "".join(str(n) for n in numbers_needed[:8])


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
