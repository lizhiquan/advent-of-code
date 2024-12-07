def part_one(equations):
    def test(result, nums, i, accu):
        if accu > result:
            return False
        if i == len(nums):
            return accu == result
        return test(result, nums, i + 1, accu + nums[i]) or test(
            result, nums, i + 1, accu * nums[i]
        )

    return sum(
        result for result, nums in equations if test(result, nums[1:], 0, nums[0])
    )


def part_two(equations):
    def test(result, nums, i, accu):
        if accu > result:
            return False
        if i == len(nums):
            return accu == result
        return (
            test(result, nums, i + 1, accu + nums[i])
            or test(result, nums, i + 1, accu * nums[i])
            or test(result, nums, i + 1, int(f"{accu}{nums[i]}"))
        )

    return sum(
        result for result, nums in equations if test(result, nums[1:], 0, nums[0])
    )


def read_input(filename: str):
    with open(filename, "r") as f:
        return [
            (int(result), list(map(int, nums.split())))
            for result, nums in (line.split(": ") for line in f)
        ]


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
