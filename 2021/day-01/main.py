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


def read_input() -> list[int]:
    with open('input.txt', 'r') as f:
        return list(map(int, f.readlines()))


def main():
    nums = read_input()
    print(f'Part 1: {part_one(nums)}')
    print(f'Part 2: {part_two(nums)}')


if __name__ == '__main__':
    main()
