import heapq
import math


def read_input(filename) -> list[list[int]]:
    with open(filename, 'r') as f:
        height_map = [[int(i) for i in line.rstrip()] for line in f]
        return height_map


def part_one(height_map):
    def get_height(i, j):
        if i < 0 or j < 0 or i > len(height_map) - 1 or j > len(height_map[i]) - 1:
            return float('inf')
        return height_map[i][j]

    low_points = []
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            if height_map[i][j] < get_height(i, j + 1) and \
                    height_map[i][j] < get_height(i, j - 1) and \
                    height_map[i][j] < get_height(i + 1, j) and \
                    height_map[i][j] < get_height(i - 1, j):
                low_points.append(height_map[i][j])

    sum_risk_levels = sum(i + 1 for i in low_points)
    return sum_risk_levels


def part_two(height_map):
    basin_sizes = [float('-inf')] * 3
    visited = [[False] * len(i) for i in height_map]
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            if not visited[i][j] and height_map[i][j] < 9:
                basin_size = visit(height_map, i, j, visited)
                heapq.heappushpop(basin_sizes, basin_size)
    return math.prod(basin_sizes)


def visit(height_map, i, j, visited):
    if i < 0 or j < 0 or \
            i > len(height_map) - 1 or j > len(height_map[i]) - 1 or \
            visited[i][j] or \
            height_map[i][j] == 9:
        return 0

    visited[i][j] = True
    count = 1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        count += visit(height_map, i + dx, j + dy, visited)
    return count


def main():
    height_map = read_input('input.txt')
    print('Part 1: ', part_one(height_map))
    print('Part 2: ', part_two(height_map))


if __name__ == '__main__':
    main()
