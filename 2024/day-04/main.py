def part_one(board):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    word = "XMAS"
    count = 0
    m, n = len(board), len(board[0])
    for row in range(m):
        for col in range(n):
            if board[row][col] == word[0]:
                for dr, dc in directions:
                    for i in range(1, len(word)):
                        new_row, new_col = row + i * dr, col + i * dc
                        if (
                            new_row < 0
                            or new_row >= m
                            or new_col < 0
                            or new_col >= n
                            or board[new_row][new_col] != word[i]
                        ):
                            break
                    else:
                        count += 1
    return count


def part_two(board):
    count = 0
    m, n = len(board), len(board[0])
    for row in range(1, m - 1):
        for col in range(1, n - 1):
            if board[row][col] == "A":
                if (
                    board[row - 1][col - 1] == "M"
                    and board[row + 1][col + 1] == "S"
                    or board[row - 1][col - 1] == "S"
                    and board[row + 1][col + 1] == "M"
                ) and (
                    board[row - 1][col + 1] == "M"
                    and board[row + 1][col - 1] == "S"
                    or board[row - 1][col + 1] == "S"
                    and board[row + 1][col - 1] == "M"
                ):
                    count += 1
    return count


def read_input(filename: str):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
