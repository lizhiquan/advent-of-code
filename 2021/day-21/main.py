import functools
import itertools


def part_one(p1_start, p2_start):
    die = itertools.cycle(range(1, 101)).__next__
    rolls_count = 0
    p1_pos, p2_pos = p1_start - 1, p2_start - 1
    p1_score = p2_score = 0
    win_score = 1000
    loser = None

    while True:
        roll_total = sum(die() for _ in range(3))
        rolls_count += 3
        p1_pos = (p1_pos + roll_total) % 10
        p1_score += p1_pos + 1
        if p1_score >= win_score:
            return p2_score * rolls_count

        roll_total = sum(die() for _ in range(3))
        rolls_count += 3
        p2_pos = (p2_pos + roll_total) % 10
        p2_score += p2_pos + 1
        if p2_score >= win_score:
            return p1_score * rolls_count


QUANTUM_ROLLS = list(map(sum, itertools.product(range(1, 4), range(1, 4), range(1, 4))))


def part_two(p1_start, p2_start):
    @functools.cache
    def solve(p1_pos, p1_score, p2_pos, p2_score):
        win_score = 21

        if p1_score >= win_score:
            return 1, 0

        if p2_score >= win_score:
            return 0, 1

        p1_wins = p2_wins = 0

        for roll_total in QUANTUM_ROLLS:
            new_pos = (p1_pos + roll_total) % 10
            new_score = p1_score + new_pos + 1
            p2w, p1w = solve(p2_pos, p2_score, new_pos, new_score)
            p1_wins += p1w
            p2_wins += p2w

        return p1_wins, p2_wins

    return max(solve(p1_start - 1, 0, p2_start - 1, 0))


def main():
    p1_start, p2_start = 9, 3
    print('Part 1: ', part_one(p1_start, p2_start))
    print('Part 2: ', part_two(p1_start, p2_start))


if __name__ == '__main__':
    main()
