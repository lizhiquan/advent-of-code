import heapq


def read_input(filename):
    with open(filename, 'r') as file:
        return [[int(i) for i in line.rstrip()] for line in file]


def part_one(risk_level_map):
    d = {}
    pq = [(0, 0, 0)]  # (cost, i, j)

    while pq:
        cost, i, j = heapq.heappop(pq)

        if i == len(risk_level_map) - 1 and j == len(risk_level_map[0]) - 1:
            return cost

        d[(i, j)] = cost
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if new_i < 0 or new_j < 0 or new_i > len(risk_level_map) - 1 or new_j > len(risk_level_map[0]) - 1:
                continue
            if (new_i, new_j) in d:
                continue

            in_pq = False
            new_cost = cost + risk_level_map[new_i][new_j]
            for pq_i in range(len(pq)):
                c, ci, cj = pq[pq_i]
                if ci == new_i and cj == new_j:
                    in_pq = True
                    if new_cost < c:
                        pq[pq_i] = (new_cost, ci, cj)
                        heapq.heapify(pq)
            if not in_pq:
                heapq.heappush(pq, (new_cost, new_i, new_j))


def scale_map(risk_level_map, times):
    tile_height = len(risk_level_map)
    tile_width = len(risk_level_map[0])
    new_map = [[0] * len(risk_level_map[0]) * times for _ in range(len(risk_level_map) * times)]

    # copy the original map over
    for i in range(tile_height):
        for j in range(tile_width):
            new_map[i][j] = risk_level_map[i][j]

    # generate first col of tiles
    for i in range(tile_height):
        for j in range(tile_width):
            for k in range(1, times):
                new_level = new_map[i + tile_height * (k - 1)][j] + 1
                new_map[i + tile_height * k][j] = new_level if new_level <= 9 else 1

    # generate each row of tiles
    for row in range(times):
        for i in range(tile_height):
            for j in range(tile_width):
                for k in range(1, times):
                    new_level = new_map[i + tile_height * row][j + tile_width * (k - 1)] + 1
                    new_map[i + tile_height * row][j + tile_width * k] = new_level if new_level <= 9 else 1

    return new_map


def part_two(risk_level_map):
    scaled_map = scale_map(risk_level_map, 5)
    return part_one(scaled_map)


def main():
    risk_level_map = read_input('input.txt')
    print('Part 1: ', part_one(risk_level_map))
    print('Part 2: ', part_two(risk_level_map))


if __name__ == '__main__':
    main()
