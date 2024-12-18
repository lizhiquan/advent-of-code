import heapq


def part_one(bytes, n=1024, rows=71, cols=71):
    corrupted = set(bytes[:n])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start, end = (0, 0), (rows - 1, cols - 1)
    pq = [(0, start[0], start[1])]  # (cost, r, c)
    distances = {start: 0}

    # for r in range(rows):
    #     for c in range(cols):
    #         print("#" if (r, c) in corrupted else ".", end="")
    #     print()

    while pq:
        cost, r, c = heapq.heappop(pq)
        if (r, c) == end:
            return cost

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                nr < 0
                or nr > rows - 1
                or nc < 0
                or nc > cols - 1
                or (nr, nc) in corrupted
            ):
                continue

            new_cost = cost + 1
            if (nr, nc) not in distances or distances[(nr, nc)] > new_cost:
                distances[(nr, nc)] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc))

    return -1


def part_one_a_star(bytes, n=1024, rows=71, cols=71):
    def manhattan_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    corrupted = set(bytes[:n])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start, end = (0, 0), (rows - 1, cols - 1)
    pq = [
        (manhattan_distance(start, end), 0, start[0], start[1])
    ]  # (score, cost, r, c)
    distances = {start: 0}

    while pq:
        _, cost, r, c = heapq.heappop(pq)
        if (r, c) == end:
            return cost

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if (
                nr < 0
                or nr > rows - 1
                or nc < 0
                or nc > cols - 1
                or neighbor in corrupted
            ):
                continue

            new_cost = cost + 1
            if neighbor not in distances or distances[neighbor] > new_cost:
                distances[neighbor] = new_cost
                heapq.heappush(
                    pq, (manhattan_distance(neighbor, end), new_cost, nr, nc)
                )

    return -1


def part_two(bytes):
    for i in range(1, len(bytes)):
        if part_one_a_star(bytes, n=i) == -1:
            return bytes[i - 1]


def read_input(filename: str):
    with open(filename, "r") as f:
        return [tuple(map(int, line.split(","))) for line in f]


input = read_input("input.txt")
print(f"Part 1: {part_one(input)}")
print(f"Part 2: {part_two(input)}")
