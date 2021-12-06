import unittest


class Board:
    def __init__(self, data):
        self.data = data
        self.marked = [[False] * 5 for _ in range(5)]
        self.is_win = False
        self.points = -1

    def reset(self):
        self.marked = [[False] * 5 for _ in range(5)]
        self.is_win = False
        self.points = -1

    def select(self, number):
        if self.is_win:
            return

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == number:
                    self.marked[i][j] = True
        self.is_win = any(all(i) for i in self.marked) or \
            any(all(i) for i in zip(*self.marked))
        if self.is_win:
            self.points = self.unselected_sum() * number

    def unselected_sum(self):
        ans = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if not self.marked[i][j]:
                    ans += self.data[i][j]
        return ans


def read_input():
    with open('input.txt', 'r') as f:
        draws = list(map(int, f.readline().split(',')))
        boards = []
        while f.readline():
            data = [list(map(int, f.readline().split())) for _ in range(5)]
            boards.append(Board(data))
    return draws, boards


def part_one(draws, boards):
    for draw in draws:
        for board in boards:
            board.select(draw)
            if board.is_win:
                return board.points


def part_two(draws, boards):
    win_count = 0
    for draw in draws:
        for board in boards:
            if board.is_win:
                continue
            board.select(draw)
            if board.is_win:
                win_count += 1
                if win_count == len(boards):
                    return board.points


def main():
    draws, boards = read_input()
    print("Part 1: ", part_one(draws, boards))
    for board in boards:
        board.reset()
    print("Part 2: ", part_two(draws, boards))


class TestCase(unittest.TestCase):
    def setUp(self):
        self.draws = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
                      16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

        self.boards = [
            Board([[22, 13, 17, 11, 0],
                   [8, 2, 23, 4, 24],
                   [21, 9, 14, 16, 7],
                   [6, 10, 3, 18, 5],
                   [1, 12, 20, 15, 19]]),

            Board([[3, 15, 0, 2, 22],
                   [9, 18, 13, 17, 5],
                   [19, 8, 7, 25, 23],
                   [20, 11, 10, 24, 4],
                   [14, 21, 16, 12, 6]]),

            Board([[14, 21, 17, 24, 4],
                   [10, 16, 15, 9, 19],
                   [18, 8, 23, 26, 20],
                   [22, 11, 13, 6, 5],
                   [2, 0, 12, 3, 7]])
        ]

    def test_part_one(self):
        self.assertEqual(part_one(self.draws, self.boards), 4512)

    def test_part_two(self):
        self.assertEqual(part_two(self.draws, self.boards), 1924)


if __name__ == '__main__':
    main()
