from collections import deque
import unittest


def solve(filename, length):
    with open(filename, "r") as f:
        buffer = f.readline()
        s = set()
        q = deque()
        for i, c in enumerate(buffer):
            q.append(c)

            if c not in s:
                s.add(c)
            else:
                while True:
                    p = q.popleft()
                    if p == c:
                        break
                    s.remove(p)

            if len(q) == length:
                return i + 1


def part_one(filename):
    return solve(filename, 4)


def part_two(filename):
    return solve(filename, 14)


def main():
    filename = "input.txt"
    print(f"Part 1: {part_one(filename)}")
    print(f"Part 2: {part_two(filename)}")


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("input_test.txt"), 7)

    def test_part_two(self):
        self.assertEqual(part_two("input_test.txt"), 19)


if __name__ == "__main__":
    main()
