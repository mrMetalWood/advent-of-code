from collections import defaultdict

with open("2019/day-09/input.txt", "r") as file:
    numbers = list(map(int, file.read().split(",")))


def run_intcode_program(memory, pointer, relative_base, inputs):
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
            memory[address] = inputs.pop()
        # output
        elif opcode == 4:
            print(f"Output: {p1}")
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


memory = defaultdict(int, enumerate(numbers))

run_intcode_program(memory.copy(), 0, 0, [1])  # part 1
run_intcode_program(memory.copy(), 0, 0, [2])  # part 2
