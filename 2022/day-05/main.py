from collections import deque
import unittest


def part_one(filename):
    with open(filename, "r") as f:
        l = []
        i = 0
        s = ""
        while True:
            if s == "\n":
                i = 0

            if i == len(l):
                l.append(deque())

            s = f.read(1)
            if s == "[":
                l[i].appendleft(f.read(1))
                f.read(1)  # ']'
            else:  # ' '
                t = f.read(1)
                if t == "1":
                    break
                f.read(1)

            s = f.read(1)  # space or new line
            i += 1

        f.readline()
        f.readline()

        for line in f:
            words = line.split()
            n = int(words[1])
            src = int(words[3]) - 1
            dst = int(words[5]) - 1
            for _ in range(n):
                l[dst].append(l[src].pop())

        return "".join(s[-1] for s in l)


def part_two(filename):
    with open(filename, "r") as f:
        l = []
        i = 0
        s = ""
        while True:
            if s == "\n":
                i = 0

            if i == len(l):
                l.append(deque())

            s = f.read(1)
            if s == "[":
                l[i].appendleft(f.read(1))
                f.read(1)  # ']'
            else:  # ' '
                t = f.read(1)
                if t == "1":
                    break
                f.read(1)

            s = f.read(1)  # space or new line
            i += 1

        f.readline()
        f.readline()

        for line in f:
            words = line.split()
            n = int(words[1])
            src = int(words[3]) - 1
            dst = int(words[5]) - 1
            t = deque()
            for _ in range(n):
                t.appendleft(l[src].pop())
            l[dst].extend(t)

        return "".join(s[-1] for s in l)


def main():
    filename = "input.txt"
    print(f"Part 1: {part_one(filename)}")
    print(f"Part 2: {part_two(filename)}")


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("input_test.txt"), "CMZ")

    def test_part_two(self):
        self.assertEqual(part_two("input_test.txt"), "MCD")


if __name__ == "__main__":
    main()
