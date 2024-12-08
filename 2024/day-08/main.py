from collections import defaultdict


def part_one(map):
    locations = set()
    antennas = defaultdict(list)

    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == ".":
                continue

            for ar, ac in antennas[map[r][c]]:
                dr, dc = r - ar, c - ac
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(map) and 0 <= nc < len(map[nr]):
                    locations.add((nr, nc))
                nr, nc = ar - dr, ac - dc
                if 0 <= nr < len(map) and 0 <= nc < len(map[nr]):
                    locations.add((nr, nc))

            antennas[map[r][c]].append((r, c))

    return len(locations)


def part_two(map):
    locations = set()
    antennas = defaultdict(list)

    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == ".":
                continue

            for ar, ac in antennas[map[r][c]]:
                dr, dc = r - ar, c - ac

                tr, tc = r, c
                while True:
                    nr, nc = tr + dr, tc + dc
                    if nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[nr]):
                        break
                    locations.add((nr, nc))
                    tr, tc = nr, nc

                tr, tc = ar, ac
                while True:
                    nr, nc = tr - dr, tc - dc
                    if nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[nr]):
                        break
                    locations.add((nr, nc))
                    tr, tc = nr, nc

            antennas[map[r][c]].append((r, c))
            locations.add((r, c))

    return len(locations)


def read_input(filename: str):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
