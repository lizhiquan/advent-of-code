import re


def part_one(memory):
    r = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    return sum(map(lambda x: int(x[0]) * int(x[1]), r.findall(memory)))


def part_two(memory):
    r = re.compile(r"do\(\)|don't\(\)|mul\(([0-9]+),([0-9]+)\)")
    matches = r.finditer(memory)
    do = True
    result = 0
    for match in matches:
        if match.group(0) == "do()":
            do = True
        elif match.group(0) == "don't()":
            do = False
        elif do:
            result += int(match.group(1)) * int(match.group(2))
    return result


def read_input(filename: str):
    with open(filename, "r") as f:
        return f.read()


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
