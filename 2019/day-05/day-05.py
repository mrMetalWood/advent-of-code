with open('2019/day-05/input.txt', 'r') as file:
    numbers = list(map(int, file.read().split(',')))


def get_value(pointer, memory, memory_index, param_mode):
    value = memory[pointer + memory_index]
    return memory[value] if param_mode == '0' else value


def run_intcode_program(user_input):
    memory, pointer = numbers.copy(), 0

    def is_safe(index): return (memory[pointer + index]) < len(memory)

    while int(str(memory[pointer])[-2:]) != 99:
        p2_mode, p1_mode, *opcode_split = str(memory[pointer]).zfill(5)[1:]
        opcode = int(''.join(opcode_split))

        p1 = get_value(pointer,  memory, 1, p1_mode) if is_safe(1) else None
        p2 = get_value(pointer, memory, 2, p2_mode) if is_safe(2) else None

        addr_params, addr_no_params = memory[pointer + 3], memory[pointer + 1]
        has_params = opcode not in [3, 4]
        address = addr_params if has_params else addr_no_params

        # input
        if opcode == 3:
            memory[address] = user_input
        # output
        elif opcode == 4:
            print(f'Output ({user_input}): ', p1)
        # add
        elif opcode == 1:
            memory[address] = p1 + p2
        # mul
        elif opcode == 2:
            memory[address] = p1 * p2
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

        pointer += 4 if opcode in [1, 2, 7, 8] else 0
        pointer += 2 if opcode in [3, 4] else 0


run_intcode_program(1)  # part 1
run_intcode_program(5)  # part 2
