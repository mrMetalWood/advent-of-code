from collections import defaultdict

raw = """#..##
#.#..
#...#
##..#
#..##"""

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

state = defaultdict(lambda: ".")

for row, line in enumerate(raw.split("\n")):
    for col, cell in enumerate([x for x in line]):
        state[(col, row)] = cell

states = []

hm2 = ""
for i in range(5):
    for j in range(5):
        hm2 += state[(j, i)]
states.append(hm2)

while True:
    new_state = defaultdict(lambda: ".")
    for y in range(5):
        for x in range(5):
            count = 0
            for (dx, dy) in DIRS:
                if state[(x + dx, y + dy)] == "#":
                    count += 1
            if state[(x, y)] == "#" and count != 1:
                new_state[(x, y)] = "."
            elif state[(x, y)] == "." and count in [1, 2]:
                new_state[(x, y)] = "#"
            else:
                new_state[(x, y)] = state[(x, y)]

    hm = ""
    for i in range(5):
        for j in range(5):
            hm += new_state[(j, i)]

    if hm in states:
        final = 0
        for idx, k in enumerate(hm):
            if k == "#":
                final += pow(2, idx)
        print(final)
        break

    states.append(hm)
    state = new_state