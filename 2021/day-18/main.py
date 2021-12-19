import collections
import functools
import operator


class Snailfish:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    @classmethod
    def parse(cls, data):
        root = Snailfish()
        current_node = root
        stack = collections.deque()
        stack.append(current_node)

        for token in data:
            if token == '[':
                current_node.left = Snailfish()
                stack.append(current_node)
                current_node = current_node.left

            elif token.isdigit():
                current_node.value = int(token)
                current_node = stack.pop()

            elif token == ',':
                current_node.value = token
                current_node.right = Snailfish()
                stack.append(current_node)
                current_node = current_node.right

            elif token == ']':
                current_node = stack.pop()

        return root

    @property
    def is_number(self):
        return isinstance(self.value, int) and self.left is None and self.right is None

    @property
    def magnitude(self):
        if not self.left and not self.right:
            return self.value
        return self.left.magnitude * 3 + self.right.magnitude * 2

    def _reduce(self):
        if pair := self._find_nested_pair_to_explode():
            self._explode(pair)
            self._reduce()
        elif number := self._find_number_to_split():
            self._split(number)
            self._reduce()

    def _find_nested_pair_to_explode(self):
        def find(root, level):
            if not root:
                return None
            if level >= 4 and not root.is_number and \
                    root.left.is_number and root.right.is_number:
                return root
            if node := find(root.left, level + 1):
                return node
            if node := find(root.right, level + 1):
                return node

        return find(self, 0)

    def _explode(self, pair):
        def traverse(root, prev):
            if not root:
                return
            traverse(root.left, prev)
            if root == pair.left and prev[0]:
                prev[0].value += pair.left.value
            if prev[0] == pair.right and root.is_number:
                root.value += pair.right.value
            if root.is_number:
                prev[0] = root
            traverse(root.right, prev)

        traverse(self, [None])
        pair.value = 0
        pair.left = pair.right = None

    def _find_number_to_split(self):
        def traverse(root):
            if not root:
                return
            if node := traverse(root.left):
                return node
            if root.is_number and root.value >= 10:
                return root
            if node := traverse(root.right):
                return node

        return traverse(self)

    def _split(self, number):
        left_val = number.value // 2
        right_val = left_val if number.value % 2 == 0 else left_val + 1
        number.left = Snailfish(left_val)
        number.right = Snailfish(right_val)
        number.value = ','

    def __add__(self, other):
        res = Snailfish(',')
        res.left = Snailfish.parse(str(self))
        res.right = Snailfish.parse(str(other))
        res._reduce()
        return res

    def __str__(self):
        res = []

        def postorder(node):
            if node:
                if node.value == ',':
                    res.append('[')
                postorder(node.left)
                res.append(str(node.value))
                postorder(node.right)
                if node.value == ',':
                    res.append(']')

        postorder(self)
        return ''.join(res)


def read_input(filename):
    with open(filename, 'r') as file:
        return [Snailfish.parse(line.rstrip()) for line in file]


def part_one(snailfishes):
    reduced_snailfish = functools.reduce(operator.add, snailfishes)
    return reduced_snailfish.magnitude


def part_two(snailfishes):
    max_magnitude = float('-inf')
    for i in range(len(snailfishes) - 1):
        for j in range(i + 1, len(snailfishes)):
            magnitude = max(
                (snailfishes[i] + snailfishes[j]).magnitude,
                (snailfishes[j] + snailfishes[i]).magnitude,
            )
            max_magnitude = max(max_magnitude, magnitude)
    return max_magnitude


def main():
    snailfishes = read_input('input.txt')
    print('Part 1: ', part_one(snailfishes))
    print('Part 2: ', part_two(snailfishes))


if __name__ == '__main__':
    main()
