import operator
import os

ops = {"+": operator.add, "*": operator.mul}
precedences = {"+": 2, "*": 1}


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip().replace(" ", "") for l in file.readlines()]


def calc(expression, is_part1):
    output = []
    op_stack = []

    for c in expression:
        if c.isnumeric():
            output.append(c)
        elif c in ["+", "*"]:
            while (
                op_stack
                and op_stack[-1] in ["+", "*"]
                and (is_part1 or precedences[op_stack[-1]] > precedences[c])
            ):
                output.append(op_stack.pop())
            op_stack.append(c)
        elif c == "(":
            op_stack.append(c)
        elif c == ")":
            while op_stack[-1] != "(":
                output.append(op_stack.pop())

            if op_stack[-1] == "(":
                op_stack.pop()

    while op_stack:
        output.append(op_stack.pop())

    stack = []
    for c in output:
        if c in ops:
            stack.append(ops[c](stack.pop(), stack.pop()))
        else:
            stack.append(int(c))
    return stack[0]


def part1():
    return sum([calc(line, True) for line in lines])


def part2():
    return sum([calc(line, False) for line in lines])


print(f"Part 1: {part1()}")  # 1890866893020
print(f"Part 2: {part2()}")  # 34646237037193
