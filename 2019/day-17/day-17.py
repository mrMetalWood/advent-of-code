from collections import defaultdict

with open('2019/day-17/input.txt', 'r') as file:
    numbers = list(map(int, file.read().split(',')))


def run_intcode_program(memory, pointer, relative_base, inp):
    out = []

    def get_value(memory_index, param_mode, read):
        value = memory[pointer + memory_index]
        base = relative_base if param_mode == '2' else 0

        if param_mode in ['0', '2']:
            return memory[value + base] if read else value + base
        if param_mode == '1':
            return value

    while int(str(memory[pointer])[-2:]) != 99:
        p3_mode, p2_mode, p1_mode, *op_split = str(memory[pointer]).zfill(5)
        opcode = int(''.join(op_split))

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
            memory[address] = inp.pop()
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

    print('Halting...')
    return (None, None, None, None)


def part1():
    coords = {}
    memory = defaultdict(int, enumerate(numbers))
    pointer = 0
    relative_base = 0
    row = 0
    col = 0

    def is_intersection(point):
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_x = max(coords, key=lambda point: point[0])
        max_y = max(coords, key=lambda point: point[1])

        return coords[point] == '#' and all(point[0] + d[0] >= 0 and point[0] + d[0] <= max_x[0] and point[1] + d[1] >= 0 and point[1] + d[1] <= max_y[1] and coords[(point[0] + d[0], point[1] + d[1])] == '#' for d in dirs)

    while True:
        (result, memory, pointer, relative_base) = run_intcode_program(
            memory, pointer, relative_base, 0)

        if result == None:
            break

        if result[0] == 10:
            col = 0
            row += 1
        else:
            coords[(col, row)] = chr(result[0])
            col += 1

    grid = list(map(lambda key: coords[key], coords))
    for i in range(0, len(grid) + 1, 49):
        part = grid[i: i+49]
        print(''.join(part))

    intersections = []
    for point in coords:
        if is_intersection(point):
            intersections.append(point)

    return sum(map(lambda p: p[0] * p[1], intersections))


def part2():
    coords = {}
    memory = defaultdict(int, enumerate(numbers))
    memory[0] = 2
    pointer = 0
    relative_base = 0

    # Got routines by looking at the grid
    main_routine = [ord(x) for x in 'A,A,B,C,B,C,B,C,C,A']
    main_routine.append(10)

    function_a = [ord(x) for x in 'L,10,R,8,R,8']
    function_a.append(10)

    function_b = [ord(x) for x in 'L,10,L,12,R,8,R,10']
    function_b.append(10)

    function_c = [ord(x) for x in 'R,10,L,12,R,10']
    function_c.append(10)

    inputs = main_routine + function_a + function_b + function_c

    # video feed: NO
    inputs.append(ord('n'))
    inputs.append(10)

    inputs.reverse()

    output = 0
    while True:
        (result, memory, pointer, relative_base) = run_intcode_program(
            memory, pointer, relative_base, inputs)

        if result == None:
            break

        output = result[0]

    return output


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')

# paths
# L,10,R,8,R,8 (A)
# L,10,R,8,R,8 (A)
# L,10,L,12,R,8,R,10 (B)
# R,10,L,12,R,10 (C)
# L,10,L,12,R,8,R,10 (B)
# R,10,L,12,R,10 (C)
# L,10,L,12,R,8,R,10 (B)
# R,10,L,12,R,10 (C)
# R,10,L,12,R,10 (C)
# L,10,R,8,R,8 (A)
