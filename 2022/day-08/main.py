import unittest


def part_one(filename):
    with open(filename, "r") as f:
        data = []
        for line in f:
            line = line.rstrip()
            data.append([int(c) for c in line])

        visible = [[0] * len(data[0]) for i in data]

        # left -> right
        for i in range(1, len(data) - 1):
            highest_so_far = data[i][0]
            for j in range(1, len(data[i]) - 1):
                if data[i][j] > highest_so_far:
                    highest_so_far = data[i][j]
                    visible[i][j] = 1
        # right -> left
        for i in range(1, len(data) - 1):
            highest_so_far = data[i][len(data[i]) - 1]
            for j in range(len(data[i]) - 2, 0, -1):
                if data[i][j] > highest_so_far:
                    highest_so_far = data[i][j]
                    visible[i][j] = 1
        # top -> bottom
        for i in range(1, len(data[0]) - 1):
            highest_so_far = data[0][i]
            for j in range(1, len(data) - 1):
                if data[j][i] > highest_so_far:
                    highest_so_far = data[j][i]
                    visible[j][i] = 1
        # bottom -> top
        for i in range(1, len(data[0]) - 1):
            highest_so_far = data[len(data) - 1][i]
            for j in range(len(data) - 2, 0, -1):
                if data[j][i] > highest_so_far:
                    highest_so_far = data[j][i]
                    visible[j][i] = 1

        edges = (len(data) + len(data[0])) * 2 - 4
        return sum(sum(i) for i in visible) + edges


def part_two(filename):
    with open(filename, "r") as f:
        data = []
        for line in f:
            line = line.rstrip()
            data.append([int(c) for c in line])

        up = [[0] * len(data[0]) for i in data]
        left = [[0] * len(data[0]) for i in data]
        right = [[0] * len(data[0]) for i in data]
        down = [[0] * len(data[0]) for i in data]

        # left -> right
        for i in range(1, len(data) - 1):
            for j in range(1, len(data[i]) - 1):
                count = 0
                for k in range(j - 1, -1, -1):
                    count += 1
                    if data[i][k] >= data[i][j]:
                        break
                left[i][j] = count

        # right -> left
        for i in range(1, len(data) - 1):
            for j in range(len(data[i]) - 2, 0, -1):
                count = 0
                for k in range(j + 1, len(data[i])):
                    count += 1
                    if data[i][k] >= data[i][j]:
                        break
                right[i][j] = count

        # top -> bottom
        for i in range(1, len(data[0]) - 1):
            for j in range(1, len(data) - 1):
                count = 0
                for k in range(j - 1, -1, -1):
                    count += 1
                    if data[k][i] >= data[j][i]:
                        break
                up[j][i] = count

        # bottom -> top
        for i in range(1, len(data[0]) - 1):
            for j in range(len(data) - 2, 0, -1):
                count = 0
                for k in range(j + 1, len(data)):
                    count += 1
                    if data[k][i] >= data[j][i]:
                        break
                down[j][i] = count

        highest_score = 0
        for i in range(1, len(data) - 1):
            for j in range(1, len(data[i]) - 1):
                highest_score = max(
                    up[i][j] * left[i][j] * down[i][j] * right[i][j], highest_score
                )
        return highest_score


def main():
    filename = "input.txt"
    print(f"Part 1: {part_one(filename)}")
    print(f"Part 2: {part_two(filename)}")


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("input_test.txt"), 21)

    def test_part_two(self):
        self.assertEqual(part_two("input_test.txt"), 8)


if __name__ == "__main__":
    main()
