import itertools

password_min = 168630
password_max = 718098


def parse_password_range():
    passwords = {}

    for possible_password in range(password_min, password_max + 1):
        decreased = double = standalone_double = False
        last_digit = 0

        for current, group in itertools.groupby(list(str(possible_password)), lambda x: x):
            number_count = len(list(group))

            double = True if number_count >= 2 else double
            standalone_double = True if number_count == 2 else standalone_double
            decreased = True if int(current) < last_digit else decreased

            last_digit = int(current)

        passwords.setdefault(
            possible_password, (decreased, double, standalone_double)
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
