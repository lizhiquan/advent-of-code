import re


def part_one(configs):
    tokens = 0
    for ax, ay, bx, by, px, py in configs:
        # axi + bxj = px
        # ayi + byj = py
        D = ax * by - ay * bx
        if D == 0:
            continue
        i = (px * by - py * bx) / D
        j = (py * ax - px * ay) / D
        if i.is_integer() and j.is_integer():
            tokens += int(i * 3 + j)
    return tokens


def part_two(configs):
    tokens = 0
    for ax, ay, bx, by, px, py in configs:
        px += 10000000000000
        py += 10000000000000
        # axi + bxj = px
        # ayi + byj = py
        D = ax * by - ay * bx
        if D == 0:
            continue
        i = (px * by - py * bx) / D
        j = (py * ax - px * ay) / D
        if i.is_integer() and j.is_integer():
            tokens += int(i * 3 + j)
    return tokens


def read_input(filename: str):
    with open(filename, "r") as f:
        r = re.compile(
            r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
        )
        return [tuple(map(int, tpl)) for tpl in r.findall(f.read())]


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
