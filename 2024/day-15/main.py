def part_one(map, movements):
    start = (0, 0)
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == "@":
                start = (r, c)
                map[r][c] = "."
                break

    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }
    for movement in movements:
        dr, dc = directions[movement]
        nr, nc = start[0] + dr, start[1] + dc
        er, ec = nr, nc  # empty space
        while map[er][ec] == "O":  # skip over the boxes if any
            er, ec = er + dr, ec + dc
        if map[er][ec] == "#":  # no space to move
            continue
        if map[er][ec] == "." and (er != nr or ec != nc):  # push the boxes
            map[er][ec], map[nr][nc] = "O", "."
        start = (nr, nc)

    ans = 0
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == "O":
                ans += 100 * r + c
    return ans


def part_two(map, movements):
    new_map = []
    widen = {
        "#": "##",
        "O": "[]",
        ".": "..",
        "@": "@.",
    }
    for r in range(len(map)):
        new_map.append([])
        for c in range(len(map[r])):
            new_map[-1] += list(widen[map[r][c]])
    map = new_map

    start = (0, 0)
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == "@":
                start = (r, c)
                map[r][c] = "."
                break

    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }
    for movement in movements:
        dr, dc = directions[movement]
        nr, nc = start[0] + dr, start[1] + dc
        if movement in "<>":
            er, ec = nr, nc  # empty space
            while map[er][ec] in "[]":  # skip over the boxes if any
                er, ec = er + dr, ec + dc
            if map[er][ec] == "#":  # no space to move
                continue
            if map[er][ec] == "." and (er != nr or ec != nc):  # push the boxes
                for i in range(ec, nc, -dc):
                    map[er][i] = map[er][i - dc]
                map[nr][nc] = "."
            start = (nr, nc)
        else:

            def moveable(r, c, dr):
                if map[r][c] == ".":
                    return True
                if map[r][c] == "#":
                    return False
                if map[r][c] == "[":
                    return moveable(r + dr, c, dr) and moveable(r + dr, c + 1, dr)
                return moveable(r + dr, c, dr) and moveable(r + dr, c - 1, dr)

            def move(r, c, dr):
                if map[r][c] == ".":
                    return
                if map[r][c] == "[":
                    move(r + dr, c, dr)
                    move(r + dr, c + 1, dr)
                    map[r + dr][c] = "["
                    map[r + dr][c + 1] = "]"
                    map[r][c] = map[r][c + 1] = "."
                else:  # ]
                    move(r + dr, c, dr)
                    move(r + dr, c - 1, dr)
                    map[r + dr][c - 1] = "["
                    map[r + dr][c] = "]"
                    map[r][c] = map[r][c - 1] = "."

            if moveable(nr, nc, dr):
                move(nr, nc, dr)
                start = (nr, nc)

    ans = 0
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == "[":
                ans += 100 * r + c
    return ans


def read_input(filename: str):
    with open(filename, "r") as f:
        map = []
        while line := f.readline().strip():
            map.append(list(line))
        movements = "".join([line.strip() for line in f])
        return map, movements


map, movements = read_input("input.txt")
print(f"Part 1: {part_one(map, movements)}")
map, movements = read_input("input.txt")
print(f"Part 2: {part_two(map, movements)}")
