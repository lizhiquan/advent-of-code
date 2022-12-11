import unittest

directions = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}


def move_tail(head, tail):
    d = (head[0] - tail[0], head[1] - tail[1])
    if abs(d[0]) > 1 or abs(d[1]) > 1:
        tail = (tail[0] + max(min(d[0], 1), -1), tail[1] + max(min(d[1], 1), -1))
    return tail


def solve(filename, knot_count):
    knots = [(0, 0)] * knot_count
    visited = {}
    visited[knots[-1]] = True
    for line in open(filename):
        line = line.rstrip()
        [direction, steps] = line.split(" ")
        delta = directions[direction]
        for _ in range(int(steps)):
            knots[0] = (knots[0][0] + delta[0], knots[0][1] + delta[1])
            for i in range(1, knot_count):
                knots[i] = move_tail(knots[i - 1], knots[i])
            visited[knots[-1]] = True
    return len(visited)


def part_one(filename):
    return solve(filename, 2)


def part_two(filename):
    return solve(filename, 10)


def main():
    filename = "input.txt"
    print(f"Part 1: {part_one(filename)}")
    print(f"Part 2: {part_two(filename)}")


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("input_test.txt"), 13)

    def test_part_two(self):
        self.assertEqual(part_two("input_test.txt"), 36)


if __name__ == "__main__":
    main()
