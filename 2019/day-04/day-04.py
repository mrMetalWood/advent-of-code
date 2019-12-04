password_min = 168630
password_max = 718098


def parse_password_range():
    passwords = {}

    for possible_password in range(password_min, password_max + 1):
        decreased = double = standalone_double = False
        numbers = [int(n) for n in str(possible_password)]
        count = 1

        for index, current in enumerate(numbers):
            prev_item = numbers[index - 1] if index > 0 else -99
            next_item = numbers[index + 1] if index < len(numbers) - 1 else 99

            decreased = True if prev_item > current else decreased
            double = True if prev_item == current else double

            new_count = count + 1 if prev_item == current else 1

            is_ex_double = count == 2 and new_count == 1
            is_ex_double_at_end = index == len(numbers) - 1 and new_count == 2

            if is_ex_double or is_ex_double_at_end:
                standalone_double = True

            count = new_count

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
