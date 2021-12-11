def read_input() -> list[int]:
    with open('input.txt', 'r') as f:
        return list(map(int, f.readline().split(',')))


def solve(positions, get_fuel):
    avg_pos = sum(positions) // len(positions)
    min_fuel = get_fuel(positions, avg_pos)

    # go left
    pos = avg_pos - 1
    while True:
        new_fuel = get_fuel(positions, pos)
        if new_fuel > min_fuel:
            break
        min_fuel = new_fuel
        pos -= 1

    # go right
    pos = avg_pos + 1
    while True:
        new_fuel = get_fuel(positions, pos)
        if new_fuel > min_fuel:
            break
        min_fuel = new_fuel
        pos += 1

    return min_fuel


def get_fuel_part_one(positions, pos):
    return sum(abs(position - pos) for position in positions)


def get_fuel_part_two(positions, pos):
    return sum(abs(position - pos) * (abs(position - pos) + 1) // 2 for position in positions)


def part_one(positions):
    return solve(positions, get_fuel_part_one)


def part_two(positions):
    return solve(positions, get_fuel_part_two)


def main():
    positions = read_input()
    print('Part 1: ', part_one(positions))
    print('Part 2: ', part_two(positions))


if __name__ == '__main__':
    main()
