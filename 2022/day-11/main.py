import unittest
from collections import deque


class Monkey:
    def __init__(self, items, operation, divisible_test, true_idx, false_idx) -> None:
        self.items = deque(items)
        self.operation = operation
        self.divisible_test = divisible_test
        self.true_idx = true_idx
        self.false_idx = false_idx
        self.inspection_count = 0


def part_one(filename):
    monkeys = []
    for group in open(filename).read().strip().split("\n\n"):
        lines = group.splitlines()
        items = list(map(int, lines[1].split(": ")[1].split(", ")))
        operation = eval("lambda old:" + lines[2].split("=")[1])
        divisible_test = int(lines[3].split(" ")[-1])
        true_idx = int(lines[4].split(" ")[-1])
        false_idx = int(lines[5].split(" ")[-1])
        monkey = Monkey(items, operation, divisible_test, true_idx, false_idx)
        monkeys.append(monkey)

    for _ in range(20):
        for monkey in monkeys:
            monkey.inspection_count += len(monkey.items)
            while monkey.items:
                worry_lvl = monkey.items.popleft()
                worry_lvl = monkey.operation(worry_lvl) // 3
                if worry_lvl % monkey.divisible_test == 0:
                    monkeys[monkey.true_idx].items.append(worry_lvl)
                else:
                    monkeys[monkey.false_idx].items.append(worry_lvl)

    inspection_counts = [monkey.inspection_count for monkey in monkeys]
    inspection_counts.sort()
    return inspection_counts[-1] * inspection_counts[-2]


def part_two(filename):
    monkeys = []
    for group in open(filename).read().strip().split("\n\n"):
        lines = group.splitlines()
        items = list(map(int, lines[1].split(": ")[1].split(", ")))
        operation = eval("lambda old:" + lines[2].split("=")[1])
        divisible_test = int(lines[3].split(" ")[-1])
        true_idx = int(lines[4].split(" ")[-1])
        false_idx = int(lines[5].split(" ")[-1])
        monkey = Monkey(items, operation, divisible_test, true_idx, false_idx)
        monkeys.append(monkey)

    common_mod = 1
    for monkey in monkeys:
        common_mod *= monkey.divisible_test

    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspection_count += len(monkey.items)
            while monkey.items:
                worry_lvl = monkey.items.popleft()
                worry_lvl = monkey.operation(worry_lvl) % common_mod
                if worry_lvl % monkey.divisible_test == 0:
                    monkeys[monkey.true_idx].items.append(worry_lvl)
                else:
                    monkeys[monkey.false_idx].items.append(worry_lvl)

    inspection_counts = [monkey.inspection_count for monkey in monkeys]
    inspection_counts.sort()
    return inspection_counts[-1] * inspection_counts[-2]


def main():
    filename = "input_test.txt"
    print(f"Part 1: {part_one(filename)}")
    print(f"Part 2: {part_two(filename)}")


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("input_test.txt"), 10605)

    def test_part_two(self):
        self.assertEqual(part_two("input_test.txt"), 2713310158)


if __name__ == "__main__":
    main()
