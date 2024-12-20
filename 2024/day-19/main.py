from functools import cache


def part_one(patterns, displays):
    @cache
    def valid(display):
        if not display:
            return True

        for i in range(1, len(display) + 1):
            prefix = display[:i]
            suffix = display[i:]
            if prefix in patterns and valid(suffix):
                return True

        return False

    return sum(valid(d) for d in displays)


def part_two(patterns, displays):
    @cache
    def valid(display):
        if not display:
            return 1

        count = 0
        for i in range(1, len(display) + 1):
            prefix = display[:i]
            suffix = display[i:]
            if prefix in patterns:
                count += valid(suffix)
        return count

    return sum(valid(d) for d in displays)


def read_input(filename: str):
    with open(filename, "r") as f:
        patterns = set(f.readline().strip().split(", "))
        f.readline()
        displays = [line.strip() for line in f]
        return patterns, displays


input = read_input("input.txt")
print(f"Part 1: {part_one(*input)}")
print(f"Part 2: {part_two(*input)}")
