from collections import deque


def find_pos(map, char):
    for r, row in enumerate(map):
        for c, cell in enumerate(row):
            if cell == char:
                return (r, c)
    return None


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def find_path(map, start, end):
    """Find path using BFS.
    Returns the path as list of coordinates if found, None if no path exists."""
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if map[nr][nc] != "#" and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None


def part_one(map, least_time_saved=100):
    start = find_pos(map, "S")
    end = find_pos(map, "E")

    path = find_path(map, start, end)
    if not path:
        return 0

    count = 0
    for i in range(len(path) - least_time_saved):
        for j in range(i + least_time_saved, len(path)):
            if manhattan_distance(path[i], path[j]) == 2:
                if j - i - 2 >= least_time_saved:
                    count += 1
    return count


def part_two(map, least_time_saved=100):
    start = find_pos(map, "S")
    end = find_pos(map, "E")

    path = find_path(map, start, end)
    if not path:
        return 0

    count = 0
    for i in range(len(path) - least_time_saved):
        for j in range(i + least_time_saved, len(path)):
            distance = manhattan_distance(path[i], path[j])
            if distance <= 20:
                if j - i - distance >= least_time_saved:
                    count += 1
    return count


def read_input(filename: str):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f]


input = read_input("input.txt")
print(f"Part 1: {part_one(input)}")
print(f"Part 2: {part_two(input)}")
