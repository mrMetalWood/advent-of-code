with open('2019/day-02/input.txt', 'r') as file:
    numbers = list(map(int, file.read().split(',')))


def run_intcode_program(noun, verb):
    memory = numbers.copy()
    pointer = 0

    memory[1] = noun
    memory[2] = verb

    while True:
        opcode, param1, param2, address = memory[pointer: pointer + 4]

        if opcode == 1:
            memory[address] = memory[param1] + memory[param2]
        elif opcode == 2:
            memory[address] = memory[param1] * memory[param2]
        elif opcode == 99:
            break

        pointer += 4

    return memory[0]


def part1():
    return run_intcode_program(12, 2)


def part2():
    for noun in range(0, 100):
        for verb in range(0, 100):
            if run_intcode_program(noun, verb) == 19690720:
                return 100 * noun + verb


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
