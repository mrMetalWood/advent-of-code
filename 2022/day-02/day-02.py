import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    plays = [l.strip() for l in file.readlines()]

    points = {
        "A X": 4,  # rock rock
        "A Y": 8,  # rock paper
        "A Z": 3,  # rock scissors
        "B X": 1,  # paper rock
        "B Y": 5,  # paper paper
        "B Z": 9,  # paper scissors
        "C X": 7,  # scissors rock
        "C Y": 2,  # scissors paper
        "C Z": 6,  # scissors scissors
    }

    points2 = {
        "A X": 3,  # rock scissors
        "A Y": 4,  # rock rock
        "A Z": 8,  # rock paper
        "B X": 1,  # paper rock
        "B Y": 5,  # paper paper
        "B Z": 9,  # paper scissors
        "C X": 2,  # scissors paper
        "C Y": 6,  # scissors scissors
        "C Z": 7,  # scissors rock
    }

    score = score2 = 0
    for play in plays:
        score += points[play]
        score2 += points2[play]

    print(f"Part 1: {score}")  # 14163
    print(f"Part 2: {score2}")  # 12091
