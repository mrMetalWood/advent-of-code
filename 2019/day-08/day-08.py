with open('2019/day-08/input.txt', 'r') as file:
    pixel = list(map(int, file.read()))
    width, size = 25, 25 * 6
    layers = [pixel[i:i + size] for i in range(0, len(pixel), size)]


def part1():
    fewest_0 = min(layers, key=lambda layer: layer.count(0))
    return fewest_0.count(1) * fewest_0.count(2)


def part2():
    image = []
    for pixels in zip(*layers):
        image.append(
            next("█" if p == 1 else ' ' for p in pixels if p == 0 or p == 1)
        )
    return [image[i:i + width] for i in range(0, len(image), width)]


print(f"Part 1: {part1()}")
print("Part 2:")
for line in part2():
    print(''.join(line))
