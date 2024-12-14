import re
from collections import defaultdict
from functools import reduce


def part_one(robots, tiles_wide, tiles_tall):
    seconds = 100
    positions = defaultdict(int)
    for px, py, vx, vy in robots:
        x = (px + vx * seconds) % tiles_wide
        y = (py + vy * seconds) % tiles_tall
        positions[(x, y)] += 1

    count = [0] * 4
    mid_x = tiles_wide // 2 if tiles_wide & 1 else None
    mid_y = tiles_tall // 2 if tiles_tall & 1 else None
    for x in range(tiles_wide):
        if x == mid_x:
            continue
        for y in range(tiles_tall):
            if y == mid_y:
                continue
            if (x, y) in positions:
                index = (
                    0
                    if x < tiles_wide // 2 and y < tiles_tall // 2
                    else (
                        1
                        if x < tiles_wide // 2 and y > tiles_tall // 2
                        else 2 if x > tiles_wide // 2 and y < tiles_tall // 2 else 3
                    )
                )
                count[index] += positions[(x, y)]
    return reduce(lambda x, y: x * y, count)


def part_two(robots, tiles_wide, tiles_tall):
    for seconds in range(10000):
        positions = defaultdict(int)
        for px, py, vx, vy in robots:
            x = (px + vx * seconds) % tiles_wide
            y = (py + vy * seconds) % tiles_tall
            positions[(x, y)] += 1

        def print_positions(positions):
            for x in range(tiles_wide):
                for y in range(tiles_tall):
                    if (x, y) in positions:
                        print(positions[(x, y)], end="")
                    else:
                        print(".", end="")
                print()

        for x in range(tiles_wide - 3):
            for y in range(tiles_tall - 3):
                if all(
                    (x + dx, y + dy) in positions for dx in range(3) for dy in range(3)
                ):
                    print(f"Second {seconds}")
                    print_positions(positions)
                    return seconds


def read_input(filename: str):
    with open(filename, "r") as f:
        r = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
        return [tuple(map(int, tpl)) for tpl in r.findall(f.read())]


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp, 101, 103)}")
print(f"Part 2: {part_two(inp, 101, 103)}")
