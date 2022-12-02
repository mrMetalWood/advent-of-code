import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    plays = [l.strip() for l in file.readlines()]

    points = {
        "A X": (4, 3),  # rock rock | rock scissors
        "A Y": (8, 4),  # rock paper | rock rock
        "A Z": (3, 8),  # rock scissors | rock paper
        "B X": (1, 1),  # paper rock | paper rock
        "B Y": (5, 5),  # paper paper | paper paper
        "B Z": (9, 9),  # paper scissors | paper scissors
        "C X": (7, 2),  # scissors rock | scissors paper
        "C Y": (2, 6),  # scissors paper | scissors scissors
        "C Z": (6, 7),  # scissors scissors | scissors rock
    }

    score = score2 = 0
    for play in plays:
        score += points[play][0]
        score2 += points[play][1]

    print(f"Part 1: {score}")  # 14163
    print(f"Part 2: {score2}")  # 12091
