import collections


def read_input(filename):
    with open(filename, 'r') as file:
        polymer_template = file.readline().rstrip()
        file.readline()
        rules = {}
        while line := file.readline():
            pattern, element = line.rstrip().split(' -> ')
            rules[pattern] = element
        return polymer_template, rules


def solve(polymer_template, rules, steps):
    pattern_counter = collections.Counter()
    char_counter = collections.Counter(polymer_template)
    for i in range(len(polymer_template) - 1):
        pattern = polymer_template[i:i + 2]
        pattern_counter[pattern] += 1

    for _ in range(steps):
        new_counter = collections.Counter()
        for pattern in pattern_counter.keys():
            if pattern in rules:
                element = rules[pattern]
                new_counter[pattern[0] + element] += pattern_counter[pattern]
                new_counter[element + pattern[1]] += pattern_counter[pattern]
                char_counter[element] += pattern_counter[pattern]
            else:
                new_counter[pattern] = pattern_counter[pattern]
        pattern_counter = new_counter

    most_common = char_counter.most_common()
    return most_common[0][1] - most_common[-1][1]


def main():
    polymer_template, rules = read_input('input.txt')
    print('Part 1: ', solve(polymer_template, rules, 10))
    print('Part 2: ', solve(polymer_template, rules, 40))


if __name__ == '__main__':
    main()
