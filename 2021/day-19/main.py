import collections
import itertools


class Scanner:
    def __init__(self):
        self.beacons = set()
        self.scanners = set()

    def append_beacon(self, beacon):
        self.beacons.add(beacon)

    def merge_beacons(self, other_scanner):
        facing_directions = [
            (1, 1, 1),
            (1, 1, -1),
            (1, -1, 1),
            (1, -1, -1),
            (-1, 1, 1),
            (-1, 1, -1),
            (-1, -1, 1),
            (-1, -1, -1),
        ]
        rotations = list(itertools.permutations([0, 1, 2]))

        for dx, dy, dz in facing_directions:
            for px, py, pz in rotations:
                diff_freq = collections.Counter()
                for beacon_1 in self.beacons:
                    for beacon_2 in other_scanner.beacons:
                        diff = (
                            beacon_1[0] - dx * beacon_2[px],
                            beacon_1[1] - dy * beacon_2[py],
                            beacon_1[2] - dz * beacon_2[pz],
                        )
                        diff_freq[diff] += 1

                diff, matching_count = diff_freq.most_common(1)[0]
                if matching_count >= 12:
                    self._do_merge(other_scanner, diff, (dx, dy, dz), (px, py, pz))
                    return True

        return False

    def _do_merge(self, other_scanner, diff, facing, order):
        for beacon in other_scanner.beacons:
            mapped_beacon = (
                beacon[order[0]] * facing[0] + diff[0],
                beacon[order[1]] * facing[1] + diff[1],
                beacon[order[2]] * facing[2] + diff[2],
            )
            self.beacons.add(mapped_beacon)

        self.scanners.add(diff)
        for scanner in other_scanner.scanners:
            mapped_scanner = (
                scanner[order[0]] * facing[0] + diff[0],
                scanner[order[1]] * facing[1] + diff[1],
                scanner[order[2]] * facing[2] + diff[2],
            )
            self.scanners.add(mapped_scanner)


def read_input(filename):
    with open(filename, 'r') as file:
        scanners = []
        scanner = None
        for line in file:
            if line.startswith('---'):
                scanner = Scanner()
            elif line == '\n':
                scanners.append(scanner)
            else:
                beacon = tuple(map(int, line.rstrip().split(',')))
                scanner.append_beacon(beacon)
        scanners.append(scanner)
        return scanners


def part_one(scanners):
    merged = [False] * len(scanners)
    merge_count = len(scanners) - 1

    while merge_count:
        try_merge = False

        for i in range(len(scanners) - 1):
            for j in range(i + 1, len(scanners)):
                if not merged[j] and scanners[i].merge_beacons(scanners[j]):
                    merged[j] = True
                    try_merge = True
                    merge_count -= 1

        if not try_merge:
            print('failed to merge')
            return

    return len(scanners[0].beacons)


def part_two(scanners):
    scanners_positions = list(scanners[0].scanners)
    largest_distance = float('-inf')
    for i in range(len(scanners_positions) - 1):
        for j in range(i + 1, len(scanners_positions)):
            distance = abs(scanners_positions[i][0] - scanners_positions[j][0]) + \
                       abs(scanners_positions[i][1] - scanners_positions[j][1]) + \
                       abs(scanners_positions[i][2] - scanners_positions[j][2])
            largest_distance = max(largest_distance, distance)
    return largest_distance


def main():
    scanners = read_input('input.txt')
    print('Part 1: ', part_one(scanners))
    print('Part 2: ', part_two(scanners))


if __name__ == '__main__':
    main()
