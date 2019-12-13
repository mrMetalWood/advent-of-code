from collections import defaultdict

with open('2019/day-13/input.txt', 'r') as file:
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
            memory[address] = inp
        # output
        elif opcode == 4:
            out.append(p1)
            if len(out) == 3:
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
    values = []
    memory = defaultdict(int, enumerate(numbers))
    pointer = 0
    relative_base = 0

    while True:
        (result, memory, pointer, relative_base) = run_intcode_program(
            memory, pointer, relative_base, 0)

        if result == None:
            break

        values.append(result[2])

    return values.count(2)


def part2():
    memory = defaultdict(int, enumerate(numbers))
    pointer = 0
    relative_base = 0

    ball_x = 0
    paddle_x = 0
    joystick = 0
    score = 0

    memory[0] = 2  # insert quarters

    while True:
        (result, memory, pointer, relative_base) = run_intcode_program(
            memory, pointer, relative_base, joystick)

        if result == None:
            break

        [x, y, value] = result

        if value == 4:
            ball_x = x
        if value == 3:
            paddle_x = x

        if x == -1 and y == 0:
            score = value

        if ball_x < paddle_x:
            joystick = -1
        if ball_x > paddle_x:
            joystick = 1
        if ball_x == paddle_x:
            joystick = 0

    return score


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
