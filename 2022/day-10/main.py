import unittest


def part_one(filename):
    with open(filename, "r") as f:
        signal = 0
        x = 1
        cycles = 1
        for line in f:
            line = line.rstrip()
            if line == "noop":
                cycles += 1
                if cycles in [20, 60, 100, 140, 180, 220]:
                    signal += cycles * x
            else:
                cycles += 1
                if cycles in [20, 60, 100, 140, 180, 220]:
                    signal += cycles * x

                cycles += 1
                [_, val] = line.split(" ")
                x += int(val)
                if cycles in [20, 60, 100, 140, 180, 220]:
                    signal += cycles * x

        return signal


def part_two(filename):
    with open(filename, "r") as f:
        x = 0
        cycles = 0
        res = ""
        for line in f:
            line = line.rstrip()
            if line == "noop":
                res += "#" if cycles in [x, (x + 1) % 40, (x + 2) % 40] else "."
                cycles = (cycles + 1) % 40
            else:
                res += "#" if cycles in [x, (x + 1) % 40, (x + 2) % 40] else "."
                cycles = (cycles + 1) % 40

                res += "#" if cycles in [x, (x + 1) % 40, (x + 2) % 40] else "."
                cycles = (cycles + 1) % 40
                [_, val] = line.split(" ")
                x = (x + int(val)) % 40

        print(res[:40])
        print(res[40:80])
        print(res[80:120])
        print(res[120:160])
        print(res[160:200])
        print(res[200:240])


def main():
    filename = "input.txt"
    print(f"Part 1: {part_one(filename)}")
    print(f"Part 2:")
    part_two(filename)


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("input_test.txt"), 13140)


if __name__ == "__main__":
    main()
