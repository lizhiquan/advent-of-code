def read_input() -> list[int]:
    with open('input.txt', 'r') as f:
        return list(map(int, f.readline().split(',')))


def solve(timers, days):
    freq = [0] * 9
    for timer in timers:
        freq[timer] += 1

    for _ in range(days):
        # rotate left by 1
        freq = freq[1:] + freq[:1]
        freq[6] += freq[8]

    return sum(freq)


def main():
    timers = read_input()
    print('Part 1: ', solve(timers, 80))
    print('Part 2: ', solve(timers, 256))


if __name__ == '__main__':
    main()
