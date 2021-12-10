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


def read_input(filename) -> (list[int], list[Board]):
    with open(filename, 'r') as f:
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
    draws, boards = read_input('input.txt')
    print("Part 1: ", part_one(draws, boards))
    for board in boards:
        board.reset()
    print("Part 2: ", part_two(draws, boards))


if __name__ == '__main__':
    main()
