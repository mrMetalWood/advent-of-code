import os
from copy import deepcopy

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]
    p1 = list(reversed([int(i) for i in lines[1:26]]))
    p2 = list(reversed([int(i) for i in lines[28:]]))


def part1(player1, player2):
    while player1 and player2:
        p1_card = player1.pop()
        p2_card = player2.pop()

        if p1_card > p2_card:
            player1.insert(0, p1_card)
            player1.insert(0, p2_card)
        else:
            player2.insert(0, p2_card)
            player2.insert(0, p1_card)

    winning_player = player1 or player2
    ans = 0
    for idx, card in enumerate(winning_player):
        ans += (idx + 1) * card
    return ans


def part2(player1, player2):
    def game(pl1, pl2):
        history = set()

        while pl1 and pl2:
            current = "".join([str(i) for i in pl1]) + "".join([str(i) for i in pl1])
            if current in history:
                return "p1"
            else:
                history.add(current)

            p1_card = pl1.pop()
            p2_card = pl2.pop()

            winner = ""
            if len(pl1) >= p1_card and len(pl2) >= p2_card:
                winner = game(deepcopy(pl1[-p1_card:]), deepcopy(pl2[-p2_card:]))
            else:
                if p1_card > p2_card:
                    winner = "p1"
                else:
                    winner = "p2"

            if winner == "p1":
                pl1.insert(0, p1_card)
                pl1.insert(0, p2_card)
            else:
                pl2.insert(0, p2_card)
                pl2.insert(0, p1_card)

        if pl1:
            return "p1"
        else:
            return "p2"

    winning_player = game(player1, player2)

    if winning_player == "p1":
        winning_player = player1
    else:
        winning_player = player2

    ans = 0
    for idx, card in enumerate(winning_player):
        ans += (idx + 1) * card
    return ans


print(f"Part 1: {part1(deepcopy(p1), deepcopy(p2))}")  # 35202
print(f"Part 2: {part2(deepcopy(p1), deepcopy(p2))}")  # 32317
