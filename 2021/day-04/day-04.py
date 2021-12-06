from collections import deque
import os


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:

    data = deque([l.strip() for l in file.readlines()])
    draws = [int(n) for n in data.popleft().split(",")]
    data.popleft()

    boards = []
    board = []
    for row in data:
        if row == "":
            boards.append(board)
            board = []
        else:
            for n in list(filter(lambda x: x != "", row.split(" "))):
                board.append(int(n.strip()))
    boards.append(board)

    winners = [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [0, 5, 10, 15, 20],
        [1, 6, 11, 16, 21],
        [2, 7, 12, 17, 22],
        [3, 8, 13, 18, 23],
        [4, 9, 14, 19, 24],
    ]


def simulate(mode="first"):
    boar = boards.copy()
    solved = set()

    for draw in draws:
        new_boards = []
        for idx, bo in enumerate(boar):
            b = [(n if n != draw else "X") for n in bo]

            for [one, two, three, four, five] in winners:
                if (
                    b[one] == "X"
                    and b[two] == "X"
                    and b[three] == "X"
                    and b[four] == "X"
                    and b[five] == "X"
                ):
                    solved.add(idx)

                    if mode == "first":
                        return (b, draw)

                    if mode == "last" and len(solved) == len(boar):
                        return (b, draw)

            new_boards.append(b)
        boar = new_boards


def part1():
    result = simulate("first")
    s = sum(list(filter(lambda x: x != "X", result[0])))

    return s * result[1]


def part2():
    result = simulate("last")
    s = sum(list(filter(lambda x: x != "X", result[0])))

    return s * result[1]


print(f"Part 1: {part1()}")  # 45031
print(f"Part 2: {part2()}")  # 2568
