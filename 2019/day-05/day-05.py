with open('2019/day-05/input.txt', 'r') as file:
    numbers = list(map(int, file.read().split(',')))


def get_value(pointer, instruction, memory, i_idx, m_idx):
    position_mode = instruction[i_idx] == '0'
    param_value = memory[pointer + m_idx]

    return memory[param_value] if position_mode else param_value


def run_intcode_program(input):
    memory = numbers.copy()
    pointer = 0

    while int(str(memory[pointer])[-2:]) != 99:
        instruction = str(memory[pointer]).zfill(5)
        opcode = int(instruction[-2:])

        try:
            has_params = opcode != 3 and opcode != 4
            address_params = memory[pointer + 3]
            address_no_params = memory[pointer + 1]
            address = address_params if has_params else address_no_params
        except IndexError:
            pass

        try:
            param1 = get_value(pointer, instruction, memory, -3, 1)
        except IndexError:
            pass

        try:
            param2 = get_value(pointer, instruction, memory, -4, 2)
        except IndexError:
            pass

        # input
        if opcode == 3:
            address = memory[pointer + 1]
            memory[address] = input
            pointer += 2
        # output
        elif opcode == 4:
            output = get_value(pointer, instruction, memory, -3, 1)
            pointer += 2
            print('OUTPUT: ', output)
        # add
        elif opcode == 1:
            memory[address] = param1 + param2
            pointer += 4
        # mul
        elif opcode == 2:
            memory[address] = param1 * param2
            pointer += 4
        # jump if true
        elif opcode == 5:
            pointer = param2 if param1 != 0 else pointer + 3
        # jump if false
        elif opcode == 6:
            pointer = param2 if param1 == 0 else pointer + 3
        # less than
        elif opcode == 7:
            memory[address] = 1 if param1 < param2 else 0
            pointer += 4
        # equals
        elif opcode == 8:
            memory[address] = 1 if param1 == param2 else 0
            pointer += 4

    print('Halting...')


run_intcode_program(1)  # part 1
run_intcode_program(5)  # part 2
