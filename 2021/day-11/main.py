def read_input(filename) -> list[list[int]]:
    with open(filename, 'r') as f:
        return [[int(j) for j in line.rstrip()] for line in f]


def spread_flashing(energy_levels, i, j, visited):
    if i < 0 or j < 0 or \
            i > len(energy_levels) - 1 or j > len(energy_levels[i]) - 1 or \
            visited[i][j]:
        return

    if energy_levels[i][j] != 0:
        energy_levels[i][j] = (energy_levels[i][j] + 1) % 10

    if energy_levels[i][j] == 0 and not visited[i][j]:
        visited[i][j] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for di, dj in directions:
            spread_flashing(energy_levels, i + di, j + dj, visited)


def part_one(energy_levels, steps):
    energy_levels = [row.copy() for row in energy_levels]
    total_flashes = 0

    for _ in range(steps):
        # increase the levels by 1
        for i in range(len(energy_levels)):
            for j in range(len(energy_levels[i])):
                energy_levels[i][j] = (energy_levels[i][j] + 1) % 10

        # spread flashing
        visited = [[False] * len(i) for i in energy_levels]
        for i in range(len(energy_levels)):
            for j in range(len(energy_levels[i])):
                if energy_levels[i][j] == 0 and not visited[i][j]:
                    spread_flashing(energy_levels, i, j, visited)

        # count number of flashes
        flashes_count = sum(sum(energy == 0 for energy in row) for row in energy_levels)

        total_flashes += flashes_count

    return total_flashes


def part_two(energy_levels):
    energy_levels = [row.copy() for row in energy_levels]
    octopuses_count = len(energy_levels) * len(energy_levels[0])
    steps = 0

    while True:
        # increase the levels by 1
        for i in range(len(energy_levels)):
            for j in range(len(energy_levels[i])):
                energy_levels[i][j] = (energy_levels[i][j] + 1) % 10

        # spread flashing
        visited = [[False] * len(i) for i in energy_levels]
        for i in range(len(energy_levels)):
            for j in range(len(energy_levels[i])):
                if energy_levels[i][j] == 0 and not visited[i][j]:
                    spread_flashing(energy_levels, i, j, visited)

        # count number of flashes
        flashes_count = sum(sum(energy == 0 for energy in row) for row in energy_levels)

        steps += 1
        if flashes_count == octopuses_count:
            return steps


def main():
    energy_levels = read_input('input.txt')
    print('Part 1: ', part_one(energy_levels, 100))
    print('Part 2: ', part_two(energy_levels))


if __name__ == '__main__':
    main()
