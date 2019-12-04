import itertools


def parse_password_range():
    passwords = {}

    for possible_password in range(168630, 718098 + 1):
        decreased = atleast_double = exact_double = False
        last_digit = 0

        for current, group in itertools.groupby(list(str(possible_password)), lambda x: x):
            count = len(list(group))

            atleast_double = True if count >= 2 else atleast_double
            exact_double = True if count == 2 else exact_double
            decreased = True if int(current) < last_digit else decreased

            last_digit = int(current)

        passwords[possible_password] = (
            decreased, atleast_double, exact_double
        )

    return passwords


def part1():
    pw = parse_password_range()
    return len(list(filter(lambda p: not pw[p][0] and pw[p][1], pw)))


def part2():
    pw = parse_password_range()
    return len(list(filter(lambda p: not pw[p][0] and pw[p][2], pw)))


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
