import unittest


def part_one(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1
    return count


def part_two(arr):
    count = 0
    prev_sum = sum(arr[0:3])
    for i in range(3, len(arr)):
        cur_sum = prev_sum - arr[i - 3] + arr[i]
        if cur_sum > prev_sum:
            count += 1
        prev_sum = cur_sum
    return count


def main():
    with open('input.txt', 'r') as f:
        input = list(map(int, f.readlines()))
        print(f'Part 1: {part_one(input)}')
        print(f'Part 2: {part_two(input)}')


class TestCase(unittest.TestCase):
    def test_part_one(self):
        input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(part_one(input), 7)

    def test_part_two(self):
        input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(part_two(input), 5)


if __name__ == '__main__':
    main()
