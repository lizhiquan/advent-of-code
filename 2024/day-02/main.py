def is_safe(report):
    deltas = [b - a for a, b in zip(report, report[1:])]
    return all(1 <= d <= 3 for d in deltas) or all(-1 >= d >= -3 for d in deltas)


def part_one(reports):
    return sum(map(is_safe, reports))


def part_two(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1 :]):
                    count += 1
                    break
    return count


def read_input(filename: str):
    with open(filename, "r") as f:
        return list(map(lambda x: list(map(int, x.split())), f.readlines()))


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
