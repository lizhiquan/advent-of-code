import unittest


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self._size = size

    def size(self):
        return self._size

    def is_dir(self):
        return False

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"- {self.name} (file, size={self._size})"


class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.items = []

    def add(self, item):
        self.items.append(item)

    def size(self):
        return sum(i.size() for i in self.items)

    def is_dir(self):
        return True

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"- {self.name} (dir)"


def build_dir(filename):
    with open(filename, "r") as f:
        f.readline()
        root = Dir("/", None)
        cur_dir = root
        for line in f:
            line = line.rstrip()
            if line.startswith("$"):
                components = line.split(" ")
                cmd = components[1]
                if cmd == "cd":
                    dir_name = components[2]
                    if dir_name == "..":
                        cur_dir = cur_dir.parent
                    else:
                        for i in cur_dir.items:
                            if i.is_dir() and i.name == dir_name:
                                cur_dir = i
                                break
            else:
                components = line.split(" ")
                if components[0] == "dir":
                    d = Dir(components[1], cur_dir)
                    cur_dir.add(d)
                else:
                    f = File(components[1], int(components[0]))
                    cur_dir.add(f)

        return root


def helper1(dir, max_size):
    total = 0
    for i in dir.items:
        if i.is_dir():
            size = i.size()
            if size <= max_size:
                total += size
            total += helper1(i, max_size)
    return total


def part_one(filename):
    root = build_dir(filename)
    return helper1(root, 100000)


def helper2(dir, needed_space):
    min_space_to_delete = dir.size()
    for i in dir.items:
        if i.is_dir():
            size = helper2(i, needed_space)
            if size >= needed_space and size < min_space_to_delete:
                min_space_to_delete = size
    return min_space_to_delete


def part_two(filename):
    disk_space = 70000000
    required_space = 30000000
    root = build_dir(filename)
    taken_space = root.size()
    free_space = disk_space - taken_space
    space_need_to_be_free = required_space - free_space
    return helper2(root, space_need_to_be_free)


def main():
    filename = "input.txt"
    print(f"Part 1: {part_one(filename)}")
    print(f"Part 2: {part_two(filename)}")


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("input_test.txt"), 95437)

    def test_part_two(self):
        self.assertEqual(part_two("input_test.txt"), 24933642)


if __name__ == "__main__":
    main()
