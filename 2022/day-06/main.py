import unittest


def solve(filename, length):
    with open(filename, "r") as f:
        buffer = f.readline()
        hm = {}
        start = 0
        for i, c in enumerate(buffer):
            if c not in hm:
                hm[c] = True
            else:
                for j in range(start, i):
                    if buffer[j] != c:
                        del hm[buffer[j]]
                    else:
                        start = j + 1
                        break

            if i - start + 1 == length:
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
