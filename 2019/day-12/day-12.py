import itertools
import math

start_positions = [
    (12, 0, -15),
    (-8, -5, -10),
    (7, -17, 1),
    (2, -11, -6)
]


def lcm(x, y):
    return x * y // math.gcd(x, y)


class Moon:
    def __init__(self, position):
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.pos_z = position[2]
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def update_velocity(self, velocity):
        self.vel_x += velocity[0]
        self.vel_y += velocity[1]
        self.vel_z += velocity[2]

    def apply_velocity(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z

    def get_potential_energy(self):
        return abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)

    def get_kinetic_energy(self):
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)

    def get_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()


def iterate(moons):
    moon_combinations = itertools.combinations(moons, 2)
    for (first, second) in moon_combinations:
        new_vel_first = [0, 0, 0]

        if first.pos_x < second.pos_x:
            new_vel_first[0] = 1
        if first.pos_x > second.pos_x:
            new_vel_first[0] = -1
        if first.pos_y < second.pos_y:
            new_vel_first[1] = 1
        if first.pos_y > second.pos_y:
            new_vel_first[1] = -1
        if first.pos_z < second.pos_z:
            new_vel_first[2] = 1
        if first.pos_z > second.pos_z:
            new_vel_first[2] = -1

        new_vel_second = [j * -1 for j in new_vel_first]

        first.update_velocity(new_vel_first)
        second.update_velocity(new_vel_second)

    for moon in moons:
        moon.apply_velocity()

    return moons


def part1():
    moons = [Moon(position) for position in start_positions]
    for i in range(1000):
        moons = iterate(moons)

    return sum(map(lambda moon: moon.get_energy(), moons))


def part2():
    moons = [Moon(position) for position in start_positions]

    seen_x = seen_y = seen_z = set()
    found_x = found_y = found_z = None

    steps = 0
    while True:
        if found_x and found_y and found_z:
            break

        moons = iterate(moons)

        if not found_x:
            x = str([[m.pos_x, m.vel_x] for m in moons])
            if x in seen_x:
                found_x = steps
            seen_x.add(x)

        if not found_y:
            y = str([[m.pos_y, m.vel_y] for m in moons])
            if y in seen_y:
                found_y = steps
            seen_y.add(y)

        if not found_z:
            z = str([[m.pos_z, m.vel_z] for m in moons])
            if z in seen_z:
                found_z = steps
            seen_z.add(z)

        steps += 1

    return lcm(lcm(found_x, found_y), found_z)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
