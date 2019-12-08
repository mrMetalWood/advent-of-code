import textwrap

with open('2019/day-08/input.txt', 'r') as file:
    pixel = list(map(int, file.read()))
    step = 25 * 6
    layers = [pixel[i:i + step] for i in range(0, len(pixel), step)]


def part1():
    fewest_0 = sorted(layers, key=lambda layer: layer.count(0))[0]
    return fewest_0.count(1) * fewest_0.count(2)


def part2():
    final_image = []
    for pixels in zip(*layers):
        final_image.append(
            next("◼" if p == 1 else '_' for p in pixels if p == 0 or p == 1))
    return ''.join(final_image)


print(f"Part 1: {part1()}")
print("Part 2:")
for line in textwrap.TextWrapper(width=25).wrap(text=part2()):
    print(line)
