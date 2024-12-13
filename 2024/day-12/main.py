def part_one(plots):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()

    def visit(r, c):
        visited.add((r, c))
        area = 1
        perimeter = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                nr < 0
                or nr >= len(plots)
                or nc < 0
                or nc >= len(plots[nr])
                or plots[nr][nc] != plots[r][c]
            ):
                perimeter += 1
                continue
            if (nr, nc) not in visited:
                a, p = visit(nr, nc)
                area += a
                perimeter += p
        return area, perimeter

    price = 0
    for r in range(len(plots)):
        for c in range(len(plots[r])):
            if (r, c) not in visited:
                area, perimeter = visit(r, c)
                price += area * perimeter

    return price


def part_two(plots):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()

    def visit(r, c, visited_sides):
        visited.add((r, c))
        area = 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                nr < 0
                or nr >= len(plots)
                or nc < 0
                or nc >= len(plots[nr])
                or plots[nr][nc] != plots[r][c]
            ):
                visited_sides.add((r, c, dr, dc))
                continue
            if (nr, nc) not in visited:
                area += visit(nr, nc, visited_sides)
        return area

    def count_sides(visited_sides):
        sides = 0
        for r, c, dr, dc in visited_sides:
            if (
                (
                    # only add top side if there is no one next to it
                    dr == -1
                    and (r, c + 1, dr, dc) not in visited_sides
                )
                or (
                    # only add bottom side if there is no one next to it
                    dr == 1
                    and (r, c + 1, dr, dc) not in visited_sides
                )
                or (
                    # only add left side if there is no one below it
                    dc == -1
                    and (r + 1, c, dr, dc) not in visited_sides
                )
                or (
                    # only add right side if there is no one below it
                    dc == 1
                    and (r + 1, c, dr, dc) not in visited_sides
                )
            ):
                sides += 1
        return sides

    price = 0
    for r in range(len(plots)):
        for c in range(len(plots[r])):
            if (r, c) not in visited:
                visited_sides = set()
                area = visit(r, c, visited_sides)
                sides = count_sides(visited_sides)
                price += area * sides
    return price


def read_input(filename: str):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
