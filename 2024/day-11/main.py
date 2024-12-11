from collections import defaultdict


def part_one(stones):
    s = stones.copy()
    for _ in range(25):
        new_s = []
        for stone in s:
            if stone == 0:
                new_s.append(1)
            else:
                stone_str = str(stone)
                if len(stone_str) % 2 == 0:
                    new_s.append(int(stone_str[: len(stone_str) // 2]))
                    new_s.append(int(stone_str[len(stone_str) // 2 :]))
                else:
                    new_s.append(stone * 2024)
        s = new_s
    return len(s)


def part_two(stones):
    freq = defaultdict(int)
    for stone in stones:
        freq[stone] += 1

    for _ in range(75):
        new_freq = defaultdict(int)
        for stone, count in freq.items():
            if stone == 0:
                new_freq[1] += count
            else:
                stone_str = str(stone)
                if len(stone_str) % 2 == 0:
                    new_freq[int(stone_str[: len(stone_str) // 2])] += count
                    new_freq[int(stone_str[len(stone_str) // 2 :])] += count
                else:
                    new_freq[stone * 2024] += count
        freq = new_freq
    return sum(freq.values())


def read_input(filename: str):
    with open(filename, "r") as f:
        return list(map(int, f.readline().split()))


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
