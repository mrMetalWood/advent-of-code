
import itertools
with open('2019/day-08/input.txt', 'r') as file:
    numbers = list(map(int, file.read()))


def assemble_layers(width, height):
    layers = []
    layer = []

    for i, j in zip(range(0, len(numbers), width), range(width, len(numbers) + 1, width)):
        layer.append(numbers[i:j])
        if j % (width * height) == 0:
            layers.append(layer)
            layer = []

    return layers


def part1():
    layer_counts = []
    for layer in assemble_layers(25, 6):

        def count(number):
            def numbers_in_row(n): return n == number

            def count_in_row(row): return len(
                list(filter(numbers_in_row, row))
            )

            return sum(map(count_in_row, layer))

        layer_counts.append((count(0), count(1), count(2),))

    fewest_0 = sorted(layer_counts, key=lambda layer: layer[0])[0]
    return fewest_0[1] * fewest_0[2]


def part2():
    final_image = []
    for layer in zip(*assemble_layers(25, 6)):
        for cell in zip(*layer):
            final_image.append(next(c for c in cell if c == 0 or c == 1))

    return final_image


print(f"Part 1: {part1()}")

print("Part 2:")
print(part2())
