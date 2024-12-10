def part_one(map):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i, j, visited):
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        if map[i][j] == 9:
            return 1

        score = 0
        for dr, dc in directions:
            nr, nc = i + dr, j + dc
            if nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[nr]):
                continue
            if map[nr][nc] == map[i][j] + 1:
                score += dfs(nr, nc, visited)
        return score

    score = 0
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == 0:
                visited = set()
                score += dfs(r, c, visited)
    return score


def part_two(map):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = {}

    def dfs(i, j):
        if (i, j) in visited:
            return visited[(i, j)]
        if map[i][j] == 9:
            visited[(i, j)] = 1
            return 1

        rating = 0
        for dr, dc in directions:
            nr, nc = i + dr, j + dc
            if nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[nr]):
                continue
            if map[nr][nc] == map[i][j] + 1:
                rating += dfs(nr, nc)
        visited[(i, j)] = rating
        return rating

    rating = 0
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == 0:
                rating += dfs(r, c)
    return rating


def read_input(filename: str):
    with open(filename, "r") as f:
        return [list(map(int, line.strip())) for line in f]


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
