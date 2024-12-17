import heapq
from collections import defaultdict


def part_one(map):
    start = (0, 0)
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == "S":
                start = (r, c)
                break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    east = (0, 1)
    pq = [(0, start[0], start[1], east[0], east[1])]  # (cost, r, c, prev_dr, prev_dc)
    distances = defaultdict(lambda: {d: float("inf") for d in directions})
    distances[start][east] = 0

    while pq:
        cost, r, c, prev_dr, prev_dc = heapq.heappop(pq)
        if map[r][c] == "E":
            return cost

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if map[nr][nc] == "#":
                continue

            new_cost = cost + 1
            if (dr, dc) != (prev_dr, prev_dc):
                new_cost += 1000

            if new_cost < distances[(nr, nc)][(dr, dc)]:
                distances[(nr, nc)][(dr, dc)] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc, dr, dc))

    return -1


def part_two(map):
    start = (0, 0)
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == "S":
                start = (r, c)
                break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    east = (0, 1)
    pq = [
        (0, start[0], start[1], east[0], east[1], {start})
    ]  # (cost, r, c, prev_dr, prev_dc, visited_tiles)
    distances = defaultdict(
        lambda: {d: {"cost": float("inf"), "tiles": set()} for d in directions}
    )
    distances[start][east] = {"cost": 0, "tiles": {start}}

    end_states = []
    while pq:
        cost, r, c, prev_dr, prev_dc, tiles = heapq.heappop(pq)

        if map[r][c] == "E":
            end_states.append((cost, tiles))
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if map[nr][nc] == "#":
                continue

            new_cost = cost + 1
            if (dr, dc) != (prev_dr, prev_dc):
                new_cost += 1000

            new_tiles = tiles | {(nr, nc)}
            state = distances[(nr, nc)][(dr, dc)]

            if new_cost > state["cost"]:
                continue

            if new_cost < state["cost"]:
                state["cost"] = new_cost
                state["tiles"] = new_tiles
            elif new_cost == state["cost"]:
                state["tiles"] |= new_tiles

            heapq.heappush(pq, (new_cost, nr, nc, dr, dc, state["tiles"]))

    min_cost = min(cost for cost, _ in end_states)
    all_tiles = set()
    for cost, tiles in end_states:
        if cost == min_cost:
            all_tiles |= tiles
    return len(all_tiles)


def read_input(filename: str):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


input = read_input("input.txt")
print(f"Part 1: {part_one(input)}")
print(f"Part 2: {part_two(input)}")
