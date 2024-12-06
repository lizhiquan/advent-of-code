from collections import defaultdict
from functools import cmp_to_key


def part_one(orderings, updates):
    d = defaultdict(set)
    for p1, p2 in orderings:
        d[p1].add(p2)

    mid_sum = 0
    for update in updates:
        for i in range(len(update) - 1):
            if update[i + 1] not in d[update[i]]:
                break
        else:
            mid_sum += update[len(update) // 2]
    return mid_sum


def part_two(orderings, updates):
    d = defaultdict(set)
    for p1, p2 in orderings:
        d[p1].add(p2)

    def compare(a, b):
        return 1 if a in d[b] else -1

    mid_sum = 0
    for update in updates:
        for i in range(len(update) - 1):
            if update[i + 1] not in d[update[i]]:
                break
        else:
            continue
        sorted_update = sorted(update, key=cmp_to_key(compare))
        mid_sum += sorted_update[len(sorted_update) // 2]
    return mid_sum


def read_input(filename: str):
    with open(filename, "r") as f:
        orderings = []
        while (line := f.readline().strip()) != "":
            orderings.append([int(page) for page in line.split("|")])
        updates = []
        for line in f:
            updates.append([int(page) for page in line.split(",")])
        return orderings, updates


orderings, updates = read_input("input.txt")
print(f"Part 1: {part_one(orderings, updates)}")
print(f"Part 2: {part_two(orderings, updates)}")
