from collections import defaultdict

with open("2019/day-11/input.txt", "r") as file:
    numbers = list(map(int, file.read().split(",")))

DIRS = {
    "^": {0: {"new": "<", "x": -1, "y": 0}, 1: {"new": ">", "x": 1, "y": 0}},
    ">": {0: {"new": "^", "x": 0, "y": 1}, 1: {"new": "v", "x": 0, "y": -1}},
    "v": {0: {"new": ">", "x": 1, "y": 0}, 1: {"new": "<", "x": -1, "y": 0}},
    "<": {0: {"new": "v", "x": 0, "y": -1}, 1: {"new": "^", "x": 0, "y": 1}},
}


def run_intcode_program(memory, pointer, relative_base, inp):
    out = []

    def get_value(memory_index, param_mode, read):
        value = memory[pointer + memory_index]
        base = relative_base if param_mode == "2" else 0

        if param_mode in ["0", "2"]:
            return memory[value + base] if read else value + base
        if param_mode == "1":
            return value

    while int(str(memory[pointer])[-2:]) != 99:
        p3_mode, p2_mode, p1_mode, *op_split = str(memory[pointer]).zfill(5)
        opcode = int("".join(op_split))

        address_with_params = get_value(3, p3_mode, read=False)
        address_no_params = get_value(1, p1_mode, read=False)
        has_params = opcode not in [3, 4]
        address = address_with_params if has_params else address_no_params

        p1 = get_value(1, p1_mode, read=True)
        p2 = get_value(2, p2_mode, read=True)

        # add
        if opcode == 1:
            memory[address] = p1 + p2
        # mul
        elif opcode == 2:
            memory[address] = p1 * p2
        # input
        elif opcode == 3:
            memory[address] = inp
        # output
        elif opcode == 4:
            out.append(p1)
            if len(out) == 2:
                return (out, memory, pointer + 2, relative_base)
        # jump if true
        elif opcode == 5:
            pointer = p2 if p1 != 0 else pointer + 3
        # jump if false
        elif opcode == 6:
            pointer = p2 if p1 == 0 else pointer + 3
        # less than
        elif opcode == 7:
            memory[address] = 1 if p1 < p2 else 0
        # equals
        elif opcode == 8:
            memory[address] = 1 if p1 == p2 else 0
        # adjust the relative base
        elif opcode == 9:
            relative_base += p1

        pointer += 4 if opcode in [1, 2, 7, 8] else 0
        pointer += 2 if opcode in [3, 4, 9] else 0

    print("Halting...")
    return (None, None, None, None)


def part1():
    # tiles = defaultdict(lambda: '.')
    tiles = {}
    direction = "^"
    position = (0, 0)
    inp = 1
    memory = defaultdict(int, enumerate(numbers))
    pointer = 0
    relative_base = 0
    count = 0
    while True:
        (result, memory, pointer, relative_base) = run_intcode_program(
            memory, pointer, relative_base, inp
        )

        if result == None:
            break

        tiles[position] = "#" if result[0] == 1 else "."

        new_x = position[0] + DIRS[direction][result[1]]["x"]
        new_y = position[1] + DIRS[direction][result[1]]["y"]

        direction = DIRS[direction][result[1]]["new"]
        position = (new_x, new_y)

        if position in tiles:
            inp = 1 if tiles[position] == "#" else 0
        else:
            inp = 0
        count += 1

    max_x = max(tiles, key=lambda f: f[0])[0]
    max_y = max(tiles, key=lambda f: f[1])[1]
    min_x = min(tiles, key=lambda f: f[0])[0]
    min_y = min(tiles, key=lambda f: f[1])[1]
    print(max_x, max_y, min_x, min_y)
    final = []
    for k in range(42 + 1):
        hu = []
        for j in range(5 + 1):
            if (k, j - 5) in tiles:
                hu.append(tiles[(k, j - 5)])
            else:
                hu.append(".")
        final.append(hu)

    for line in final:
        print("".join(line))

    return len(list(tiles))


print(f"Part 1: {part1()}")
# HKJBAHCR part 2
