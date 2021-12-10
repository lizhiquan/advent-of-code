class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def is_horizontal(self):
        return self.y1 == self.y2

    @property
    def is_vertical(self):
        return self.x1 == self.x2

    def __repr__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"


def read_input(filename) -> list[Line]:
    with open(filename, 'r') as f:
        lines = []
        for line in f:
            points = line.split(' -> ')
            start = points[0].split(',')
            end = points[1].split(',')
            lines.append(Line(int(start[0]), int(start[1]), int(end[0]), int(end[1])))
        return lines


def part_one(lines: list[Line]):
    # only consider horizontal and vertical lines
    lines = list(filter(lambda x: x.is_horizontal or x.is_vertical, lines))

    max_x, max_y = 0, 0
    for line in lines:
        max_x = max(max_x, line.x1, line.x2)
        max_y = max(max_y, line.y1, line.y2)

    graph = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    for line in lines:
        if line.is_horizontal:
            for i in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
                graph[line.y1][i] += 1
        else:
            for i in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
                graph[i][line.x1] += 1

    overlaps = sum(map(lambda i: sum(j >= 2 for j in i), graph))
    return overlaps


def part_two(lines: list[Line]):
    max_x, max_y = 0, 0
    for line in lines:
        max_x = max(max_x, line.x1, line.x2)
        max_y = max(max_y, line.y1, line.y2)

    graph = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    for line in lines:
        if line.is_horizontal:
            for i in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
                graph[line.y1][i] += 1
        elif line.is_vertical:
            for i in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
                graph[i][line.x1] += 1
        else:
            x_delta = 1 if line.x1 < line.x2 else -1
            y_delta = 1 if line.y1 < line.y2 else -1
            x, y = line.x1, line.y1
            for _ in range(abs(line.x1 - line.x2) + 1):
                graph[y][x] += 1
                x += x_delta
                y += y_delta

    overlaps = sum(map(lambda i: sum(j >= 2 for j in i), graph))
    return overlaps


def main():
    lines = read_input('input.txt')
    print('Part 1: ', part_one(lines))
    print('Part 2: ', part_two(lines))


if __name__ == '__main__':
    main()
