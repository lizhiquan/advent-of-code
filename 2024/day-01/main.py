import collections


def part_one(nums):
    sorted_left = map(lambda x: x[0], sorted(nums, key=lambda x: x[0]))
    sorted_right = map(lambda x: x[1], sorted(nums, key=lambda x: x[1]))
    return sum(map(lambda a, b: abs(a - b), sorted_left, sorted_right))


def part_two(nums):
    right_counter = collections.Counter(map(lambda x: x[1], nums))
    return sum(map(lambda x: x[0] * right_counter[x[0]], nums))


def read_input(filename: str):
    with open(filename, "r") as f:
        return list(map(lambda x: tuple(map(int, x.split())), f.readlines()))


nums = read_input("input.txt")
print(f"Part 1: {part_one(nums)}")
print(f"Part 2: {part_two(nums)}")
