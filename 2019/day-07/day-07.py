import itertools

with open('2019/day-07/input.txt', 'r') as file:
    numbers = list(map(int, file.read().split(',')))


def get_value(pointer, memory, memory_index, param_mode):
    value = memory[pointer + memory_index]
    return memory[value] if param_mode == '0' else value


def run_intcode_program(memory, pointer, inputs):

    def is_safe(index, mode):
        immediate_safe = (pointer + index) < len(memory)
        if mode == '1':
            return immediate_safe

        return immediate_safe and memory[pointer + index] < len(memory)

    while int(str(memory[pointer])[-2:]) != 99:
        p2_mode, p1_mode, *opcode_split = str(memory[pointer]).zfill(5)[1:]
        opcode = int(''.join(opcode_split))

        addr_params = memory[pointer + 3] if is_safe(3, '0') else None
        addr_no_params = memory[pointer + 1] if is_safe(1, '0') else None
        has_params = opcode not in [3, 4]
        address = addr_params if has_params else addr_no_params

        p1 = get_value(pointer,  memory, 1, p1_mode) if is_safe(
            1, p1_mode) else None
        p2 = get_value(pointer, memory, 2, p2_mode) if is_safe(
            2, p2_mode) else None

        # add
        if opcode == 1:
            memory[address] = p1 + p2
        # mul
        elif opcode == 2:
            memory[address] = p1 * p2
        # input
        elif opcode == 3:
            memory[address] = inputs.pop()
        # output
        elif opcode == 4:
            return (p1, memory, pointer + 2)
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

    return (None, None, None)


def part1():
    phases_permutation = list(itertools.permutations([0, 1, 2, 3, 4]))
    signals, result = [], 0

    for perm in phases_permutation:
        memory = numbers.copy()
        for phase in perm:
            (result, memory, pointer) = run_intcode_program(
                memory, 0, [result, phase]
            )
            signals.append(result)
        result = 0
    return max(signals)


def part2():
    phases_permutaions = list(itertools.permutations([5, 6, 7, 8, 9]))
    signals = []

    for permutation in phases_permutaions:
        current_result = phase_result = 0

        amps = {
            'A': [numbers.copy(), 0, permutation[0]],
            'B': [numbers.copy(), 0, permutation[1]],
            'C': [numbers.copy(), 0, permutation[2]],
            'D': [numbers.copy(), 0, permutation[3]],
            'E': [numbers.copy(), 0, permutation[4]],
        }

        for key in itertools.cycle(amps):
            inputs = [current_result, amps[key][2]] if len(
                amps[key]) == 3 else [current_result]

            (current_result, memory, pointer) = run_intcode_program(
                amps[key][0], amps[key][1], inputs)

            if not current_result:
                signals.append(phase_result)
                break

            amps[key] = [memory, pointer]
            phase_result = current_result if key == 'E' else phase_result

    return max(signals)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
