from collections import defaultdict
from copy import deepcopy

with open("2019/day-15/input.txt", "r") as file:
    numbers = list(map(int, file.read().split(",")))


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
            if len(out) == 1:
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
    dirs = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}

    memory = defaultdict(int, enumerate(numbers))
    pointer = 0
    relative_base = 0

    coords = defaultdict(lambda: "?")

    coords[(0, 0)] = [1, deepcopy(memory), pointer, relative_base]
    oxygen = False

    step = 0

    while not oxygen:
        # while not oxygen:
        step += 1
        new_cells = [coord for coord in coords if coords[coord][0] == step]
        # print(new_cells)

        for cell in new_cells:
            s, mem, poi, rb = coords[cell]
            # print(s)

            for dir in dirs:
                # print(dir, dirs[dir])
                me = deepcopy(mem)
                (result, memory, pointer, relative_base) = run_intcode_program(
                    me, poi, rb, dir
                )
                if result[0] == 0:
                    # wall
                    coords[(cell[0] + dirs[dir][0], cell[1] + dirs[dir][1])] = [
                        "#",
                        deepcopy(memory),
                        deepcopy(pointer),
                        deepcopy(relative_base),
                    ]
                if (
                    result[0] == 1
                    and (cell[0] + dirs[dir][0], cell[1] + dirs[dir][1]) not in coords
                ):
                    # all good
                    # print(step + 1)
                    coords[(cell[0] + dirs[dir][0], cell[1] + dirs[dir][1])] = [
                        step + 1,
                        deepcopy(memory),
                        deepcopy(pointer),
                        deepcopy(relative_base),
                    ]
                if result[0] == 2:
                    # finished
                    coords[(cell[0] + dirs[dir][0], cell[1] + dirs[dir][1])] = [
                        "*",
                        deepcopy(memory),
                        deepcopy(pointer),
                        deepcopy(relative_base),
                    ]
                    oxygen = True
                    print("oxygen", (cell[0] + dirs[dir][0], cell[1] + dirs[dir][1]))
    print(step)
    # (14, -12)

    st = 318
    while
    # break

    # hm = list(map(lambda coord: (coord, coords[coord][0]), coords))
    # min_x = min([item[0][0] for item in hm])
    # max_x = max([item[0][0] for item in hm])
    # min_y = min([item[0][1] for item in hm])
    # max_y = max([item[0][1] for item in hm])
    # range_x = abs(max_x - min_x)
    # range_y = abs(max_y - min_y)
    # gri = []
    # for y in range(min_y, max_y + 1):
    #     for x in range(min_x, max_x + 1):
    #         gri.append(coords[(x, y)][0])

    # for i in range(0, len(gri), range_x + 1):
    #     print(gri[i : i + range_x + 1])


def part2():

    return "part2"


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
