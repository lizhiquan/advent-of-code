def part_one(map):
    directions = {
        "v": (1, 0),
        "^": (-1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }
    next_direction = {
        "v": "<",
        "^": ">",
        ">": "v",
        "<": "^",
    }
    direction = None
    position = None
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] in directions:
                direction = map[row][col]
                position = (row, col)
                map[row][col] = "X"
                break

    count = 1
    while True:
        nr, nc = (
            position[0] + directions[direction][0],
            position[1] + directions[direction][1],
        )
        if nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[nr]):
            break
        if map[nr][nc] == "#":
            direction = next_direction[direction]
            continue
        if map[nr][nc] == ".":
            map[nr][nc] = "X"
            count += 1
        position = (nr, nc)
    return count


def part_two(map):
    directions = {
        "v": (1, 0),
        "^": (-1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }
    next_direction = {
        "v": "<",
        "^": ">",
        ">": "v",
        "<": "^",
    }
    start_direction = None
    start = None
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] in directions:
                start_direction = map[row][col]
                start = (row, col)
                break

    count = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == ".":
                map[row][col] = "#"
                visited = set()
                visited.add((start[0], start[1], start_direction))
                position = start
                direction = start_direction
                while True:
                    nr, nc = (
                        position[0] + directions[direction][0],
                        position[1] + directions[direction][1],
                    )
                    if nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[nr]):
                        break
                    if (nr, nc, direction) in visited:
                        count += 1
                        break
                    if map[nr][nc] == "#":
                        direction = next_direction[direction]
                        continue
                    position = (nr, nc)
                    visited.add((nr, nc, direction))
                map[row][col] = "."
    return count


def read_input(filename: str):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f]


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
inp = read_input("input.txt")
print(f"Part 2: {part_two(inp)}")
