class Entry:
    def __init__(self, signal_patterns: list[str], digits: list[str]):
        self.signal_patterns = signal_patterns
        self.digits = digits

    def decode_digits(self) -> int:
        one = next(i for i in self.signal_patterns if len(i) == 2)
        four = next(i for i in self.signal_patterns if len(i) == 4)
        seven = next(i for i in self.signal_patterns if len(i) == 3)
        six_segments_digits = [i for i in self.signal_patterns if len(i) == 6]
        six = next(i for i in six_segments_digits if len(set(seven) - set(i)) > 0)
        nine = next(i for i in six_segments_digits if len(set(four) - set(i)) == 0)
        zero = next(i for i in six_segments_digits if i != six and i != nine)
        five_segments_digits = [i for i in self.signal_patterns if len(i) == 5]
        three = next(i for i in five_segments_digits if len(set(one) - set(i)) == 0)

        top_segment = (set(seven) - set(one)).pop()
        right_upper_segment = (set(one) - set(six)).pop()
        right_lower_segment = next(i for i in one if i != right_upper_segment)
        middle_segment = (set(four) - set(zero)).pop()
        left_upper_segment = (set(nine) - set(three)).pop()
        left_lower_segment = (set(six) - set(nine)).pop()
        bottom_segment = (set(nine) - set(seven) - set(four)).pop()

        decoded_digits = 0
        for d in self.digits:
            decoded_digits *= 10
            if len(d) == 2:
                decoded_digits += 1
            elif len(d) == 4:
                decoded_digits += 4
            elif len(d) == 3:
                decoded_digits += 7
            elif len(d) == 7:
                decoded_digits += 8
            elif len(d) == 5:
                if left_upper_segment in d:
                    decoded_digits += 5
                elif left_lower_segment in d:
                    decoded_digits += 2
                else:
                    decoded_digits += 3
            else:
                if right_upper_segment not in d:
                    decoded_digits += 6
                elif left_lower_segment not in d:
                    decoded_digits += 9

        return decoded_digits


def read_input(filename) -> list[Entry]:
    with open(filename, 'r') as f:
        entries = []
        for line in f:
            [patterns, digits] = line.split(' | ')
            entry = Entry(patterns.split(), digits.split())
            entries.append(entry)
        return entries


def part_one(entries):
    return sum(map(lambda entry: sum(len(digit) in [2, 3, 4, 7] for digit in entry.digits), entries))


def part_two(entries):
    return sum(entry.decode_digits() for entry in entries)


def main():
    entries = read_input('input.txt')
    print('Part 1: ', part_one(entries))
    print('Part 2: ', part_two(entries))


if __name__ == '__main__':
    main()
