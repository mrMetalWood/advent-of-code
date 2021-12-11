import os
import statistics

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]

syntax_error_score, autocomplete_scores = 0, []
parenthesis = {"(": ")", "[": "]", "{": "}", "<": ">"}
syntax_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomplete_points = {")": 1, "]": 2, "}": 3, ">": 4}

for line in lines:
    stack, corrupt = [], False

    for paren in line:
        if paren in parenthesis:
            stack.append(paren)

        if paren not in parenthesis:
            top_of_stack = stack.pop()

            if parenthesis[top_of_stack] != paren:
                syntax_error_score += syntax_points[paren]
                corrupt = True
                break

    if not corrupt:
        count = 0
        while stack:
            paren_to_be_closed = stack.pop()
            count = count * 5 + autocomplete_points[parenthesis[paren_to_be_closed]]
        autocomplete_scores.append(count)

print(f"Part 1: {syntax_error_score}")  # 415953
print(f"Part 2: {statistics.median(autocomplete_scores)}")  # 2292863731
