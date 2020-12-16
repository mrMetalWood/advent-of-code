import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]
    rules = [re.split(r": |-| or |-", l) for l in lines[:20]]
    my_ticket = lines[22].split(",")
    nearby = lines[25:]


def matches_rule(ticket_field, rule):
    _, min1, max1, min2, max2 = rule
    return (int(min1) <= int(ticket_field) <= int(max1)) or (
        int(min2) <= int(ticket_field) <= int(max2)
    )


def is_valid_ticket_field(ticket_field):
    valid = False
    for rule in rules:
        if matches_rule(ticket_field, rule):
            valid = True
    return valid


def part1():
    not_matching_any = []
    for ticket_field in ",".join(nearby).split(","):
        if not is_valid_ticket_field(ticket_field):
            not_matching_any.append(int(ticket_field))

    return sum(not_matching_any)


def part2():
    def is_valid(ticket):
        for ticket_field in ticket.split(","):
            if not is_valid_ticket_field(ticket_field):
                return False
        return True

    valid_tickets = [ticket.split(",") for ticket in nearby if is_valid(ticket)]
    MAPPING = {}
    SOLVED_INDICES = []

    def find_next_field():
        for rule in rules:
            if rule[0] in MAPPING:
                continue

            possible_fields_count = 0
            idx = -1

            for ticket_fields in zip(*valid_tickets):
                idx += 1
                if idx in SOLVED_INDICES:
                    continue

                valid_field_count = 0
                for ticket_field in ticket_fields:
                    if matches_rule(ticket_field, rule):
                        valid_field_count += 1

                if valid_field_count == len(ticket_fields):
                    possible_fields_count += 1
                    position = idx

            if possible_fields_count == 1:
                SOLVED_INDICES.append(position)
                MAPPING[rule[0]] = position
                find_next_field()

    find_next_field()

    answer = 1
    for field, index in MAPPING.items():
        if field.startswith("departure"):
            answer *= int(my_ticket[index])
    return answer


print(f"Part 1: {part1()}")  # 23044
print(f"Part 2: {part2()}")  # 3765150732757
