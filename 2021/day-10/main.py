import collections
import enum
import functools


class ChunkState(enum.Enum):
    COMPLETE = 1
    INCOMPLETE = 2
    CORRUPTED = 3


class Line:
    def __init__(self, chunks):
        self.chunks = chunks
        self.state = None
        self.first_illegal_char = None
        self.missing_closing_chars = []
        self._parse_chunks()

    def _parse_chunks(self):
        stack = collections.deque()
        for token in self.chunks:
            if token in ['(', '[', '{', '<']:
                # opening token, push to the stack
                stack.append(token)
            else:
                # closing token, match with the top opening token in the stack
                if not stack:
                    self.state = ChunkState.CORRUPTED
                    self.first_illegal_char = token
                    return

                if get_closing_token(stack[-1]) == token:
                    stack.pop()
                else:
                    self.state = ChunkState.CORRUPTED
                    self.first_illegal_char = token
                    return

        self.state = ChunkState.INCOMPLETE if stack else ChunkState.COMPLETE
        while stack:
            self.missing_closing_chars.append(get_closing_token(stack.pop()))


def get_closing_token(opening_token):
    token_map = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    return token_map[opening_token]


def read_input(filename) -> list[Line]:
    with open(filename, 'r') as f:
        return [Line(line.rstrip()) for line in f]


def part_one(lines):
    point_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    syntax_error_score = sum(point_map[i.first_illegal_char] for i in lines if i.state == ChunkState.CORRUPTED)
    return syntax_error_score


def part_two(lines):
    def get_score(missing_closing_chars):
        point_map = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4,
        }
        score = functools.reduce(lambda acc, val: acc * 5 + point_map[val], missing_closing_chars, 0)
        return score

    scores = [get_score(i.missing_closing_chars) for i in lines if i.state == ChunkState.INCOMPLETE]
    scores.sort()
    middle_score = scores[len(scores) // 2]
    return middle_score


def main():
    lines = read_input('input.txt')
    print('Part 1: ', part_one(lines))
    print('Part 2: ', part_two(lines))


if __name__ == '__main__':
    main()
