class Graph:
    def __init__(self, paths):
        self.cave_map = {}
        for start, end in paths:
            if start not in self.cave_map:
                self.cave_map[start] = Cave(start)
            if end not in self.cave_map:
                self.cave_map[end] = Cave(end)
            self.cave_map[start].add_neighbour(self.cave_map[end])
            self.cave_map[end].add_neighbour(self.cave_map[start])

    def find_paths_part_one(self):
        def dfs(cave, paths, results):
            if cave.name == 'end':
                results.append(paths + [cave.name])
                return

            for neighbouring_cave in cave.neighbours:
                if neighbouring_cave.name == 'start':
                    continue
                if neighbouring_cave.name.islower() and neighbouring_cave.name in paths:
                    continue
                dfs(neighbouring_cave, paths + [cave.name], results)

        results = []
        start = self.cave_map['start']
        dfs(start, [], results)
        return results

    def find_paths_part_two(self):
        def dfs(cave, paths_info, results):
            paths, small_cave_visited_twice = paths_info

            if cave.name == 'end':
                results.append(paths + [cave.name])
                return

            for neighbouring_cave in cave.neighbours:
                if neighbouring_cave.name == 'start':
                    continue
                visited_twice = small_cave_visited_twice
                if neighbouring_cave.name.islower() and neighbouring_cave.name in paths:
                    if visited_twice:
                        continue
                    visited_twice = True
                dfs(neighbouring_cave, (paths + [cave.name], visited_twice), results)
                visited_twice = small_cave_visited_twice

        results = []
        start = self.cave_map['start']
        dfs(start, ([], False), results)
        return results


class Cave:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, cave):
        self.neighbours.append(cave)


def read_input(filename) -> Graph:
    with open(filename, 'r') as f:
        paths = [tuple(line.rstrip().split('-')) for line in f]
        return Graph(paths)


def part_one(graph):
    paths = graph.find_paths_part_one()
    return len(paths)


def part_two(graph):
    paths = graph.find_paths_part_two()
    return len(paths)


def main():
    graph = read_input('input.txt')
    print('Part 1: ', part_one(graph))
    print('Part 2: ', part_two(graph))


if __name__ == '__main__':
    main()
