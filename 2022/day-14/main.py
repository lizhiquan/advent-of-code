import unittest
from functools import cmp_to_key


def is_right_order(a, b):
    if type(a) is int and type(b) is int:
        if a < b:
            return True
        if a > b:
            return False
        return None

    if type(a) is int:
        return is_right_order([a], b)

    if type(b) is int:
        return is_right_order(a, [b])

    for i in range(max(len(a), len(b))):
        if i == len(a):
            return True
        if i == len(b):
            return False
        ret = is_right_order(a[i], b[i])
        if ret != None:
            return ret


def part_one(filename):
    group = open(filename).read().strip().split("\n\n")
    s = 0
    for i, lines in enumerate(group):
        a, b = lines.splitlines()
        a, b = eval(a), eval(b)
        if is_right_order(a, b):
            s += i + 1
    return s


def part_two(filename):
    group = open(filename).read().strip().split("\n\n")

    d1, d2 = [[2]], [[6]]
    packets = [d1, d2]
    for lines in group:
        a, b = lines.splitlines()
        a, b = eval(a), eval(b)
        packets += [a, b]

    packets = sorted(
        packets, key=cmp_to_key(lambda a, b: -1 if is_right_order(a, b) else 1)
    )

    for i, p in enumerate(packets):
        if p == d1:
            i1 = i + 1
        elif p == d2:
            i2 = i + 1
            break

    return i1 * i2


def main():
    filename = "input.txt"
    print(f"Part 1: {part_one(filename)}")
    print(f"Part 2: {part_two(filename)}")


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("input_test.txt"), 13)

    def test_part_two(self):
        self.assertEqual(part_two("input_test.txt"), 140)


if __name__ == "__main__":
    main()
