import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    ins = [l.strip() for l in file.readlines()]

card_count = 10007
stack = []

for j in range(card_count):
    stack.append(j)

initial_stack = stack.copy()
count = 0

for i in ins:
    if "stack" in i:
        stack.reverse()

    if "cut" in i:
        amount = int(i.split(" ").pop())

        if amount < 0:
            stack[0:0] = stack[amount:]
            del stack[amount:]
        if amount > 0:
            stack.extend(stack[:amount])
            del stack[:amount]

    if "increment" in i:
        amount = int(i.split(" ").pop())
        old_stack = stack.copy()
        pointer = 0

        for k in old_stack:
            stack[pointer] = k
            pointer = (pointer + amount) % len(stack)


print("Part 1: ", stack.index(2019))
