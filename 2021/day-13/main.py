def read_input(filename):
    with open(filename, 'r') as file:
        dots = []
        folds = []
        while (line := file.readline()) != '\n':
            dots.append([int(i) for i in line.rstrip().split(',')])
        while line := file.readline():
            axis, line = line.rstrip().split()[-1].split('=')
            folds.append([axis, int(line)])
        return dots, folds


def make_paper(dots):
    max_x = max(dot[0] for dot in dots)
    max_y = max(dot[1] for dot in dots)
    paper = [[False] * (max_x + 1) for _ in range(max_y + 1)]
    for x, y in dots:
        paper[y][x] = True
    return paper


def fold(paper, instruction):
    axis, line = instruction
    fold_map = {
        'x': fold_vertically,
        'y': fold_horizontally,
    }
    fold_map[axis](paper, line)


def fold_vertically(paper, line):
    for row in range(len(paper)):
        for i in range(1, min(line, len(paper[row]) - line - 1) + 1):
            if paper[row][line + i]:
                paper[row][line - i] = True

    for i in range(len(paper)):
        paper[i] = paper[i][:line]


def fold_horizontally(paper, line):
    for i in range(1, min(line, len(paper) - line - 1) + 1):
        for col in range(len(paper[0])):
            if paper[line + i][col]:
                paper[line - i][col] = True

    del paper[line:]


def part_one(dots, folds):
    paper = make_paper(dots)
    fold(paper, folds[0])
    visible_dots_count = sum(sum(dot for dot in row) for row in paper)
    return visible_dots_count


def part_two(dots, folds):
    paper = make_paper(dots)
    for instruction in folds:
        fold(paper, instruction)

    for i in range(len(paper)):
        for j in range(len(paper[i])):
            paper[i][j] = '#' if paper[i][j] else ' '
        print(''.join(paper[i]))


def main():
    dots, folds = read_input('input.txt')
    print('Part 1: ', part_one(dots, folds))
    print('Part 2:')
    part_two(dots, folds)


if __name__ == '__main__':
    main()
