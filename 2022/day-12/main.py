import unittest
from collections import deque


def part_one(filename):
    data = [list(x) for x in open(filename).read().strip().splitlines()]
    for r, row in enumerate(data):
        for c, item in enumerate(row):
            if item == "S":
                sr = r
                sc = c
                data[r][c] = "a"
            if item == "E":
                er = r
                ec = c
                data[r][c] = "z"

    visited = {(sr, sc)}
    q = deque()
    q.append((0, sr, sc))

    while q:
        steps, r, c = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= len(data) or nc >= len(data[0]):
                continue
            if (nr, nc) in visited:
                continue
            if ord(data[nr][nc]) - ord(data[r][c]) > 1:
                continue
            if nr == er and nc == ec:
                return steps + 1
            visited.add((nr, nc))
            q.append((steps + 1, nr, nc))


def part_two(filename):
    data = [list(x) for x in open(filename).read().strip().splitlines()]
    for r, row in enumerate(data):
        for c, item in enumerate(row):
            if item == "S":
                sr = r
                sc = c
                data[r][c] = "a"
            if item == "E":
                er = r
                ec = c
                data[r][c] = "z"

    visited = {(er, ec)}
    q = deque()
    q.append((0, er, ec))

    while q:
        steps, r, c = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= len(data) or nc >= len(data[0]):
                continue
            if (nr, nc) in visited:
                continue
            if ord(data[r][c]) - ord(data[nr][nc]) > 1:
                continue
            if data[nr][nc] == "a":
                return steps + 1
            visited.add((nr, nc))
            q.append((steps + 1, nr, nc))


def main():
    filename = "input.txt"
    print(f"Part 1: {part_one(filename)}")
    print(f"Part 2: {part_two(filename)}")


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("input_test.txt"), 31)

    def test_part_two(self):
        self.assertEqual(part_two("input_test.txt"), 29)


if __name__ == "__main__":
    main()
