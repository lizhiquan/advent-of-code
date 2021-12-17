import math
import operator


class Packet:
    def __init__(self, data):
        self.version = next_chunk_as_int(data, 3)
        self.type_id = next_chunk_as_int(data, 3)
        self.subpackets = []
        self.value = 0

        if self.type_id == 4:
            self.value = self._parse_literal(data)
        else:
            self.subpackets = self._parse_operator(data)
            ops = {
                0: sum,
                1: math.prod,
                2: min,
                3: max,
                5: operator.gt,
                6: operator.lt,
                7: operator.eq,
            }
            if 0 <= self.type_id <= 3:
                self.value = ops[self.type_id](p.value for p in self.subpackets)
            else:
                self.value = ops[self.type_id](*[p.value for p in self.subpackets])

    @property
    def sum_version(self):
        return self.version + sum(p.sum_version for p in self.subpackets)

    def _parse_literal(self, data):
        bin_value = ""
        group = next_chunk(data, 5)
        while group[0] != '0':
            bin_value += ''.join(group[1:])
            group = next_chunk(data, 5)
        bin_value += ''.join(group[1:])
        return int(bin_value, 2)

    def _parse_operator(self, data):
        length_type_id = next_chunk_as_int(data, 1)
        subpackets = []

        if length_type_id == 0:
            subpackets_length_in_bits = next_chunk_as_int(data, 15)
            begin_len = len(data)
            end_len = begin_len - subpackets_length_in_bits
            while len(data) > end_len:
                subpackets.append(Packet(data))

        elif length_type_id == 1:
            num_subpackets = next_chunk_as_int(data, 11)
            for _ in range(num_subpackets):
                subpackets.append(Packet(data))

        return subpackets

    @classmethod
    def from_hex(cls, data):
        bin_data = ''.join([get_bin_from_hex(char) for char in data])
        return Packet([char for char in bin_data])


def next_chunk(bin_data, chunk_size):
    chunk = bin_data[:chunk_size]
    del bin_data[:chunk_size]
    return chunk


def next_chunk_as_int(bin_data, chunk_size):
    chunk = next_chunk(bin_data, chunk_size)
    return int(''.join(chunk), 2)


def get_bin_from_hex(char):
    return bin(int(char, 16))[2:].zfill(4)


def read_input(filename):
    with open(filename, 'r') as file:
        data = file.readline().rstrip()
        return Packet.from_hex(data)


def part_one(packet):
    return packet.sum_version


def part_two(packet):
    return packet.value


def main():
    packet = read_input('input.txt')
    print('Part 1: ', part_one(packet))
    print('Part 2: ', part_two(packet))


if __name__ == '__main__':
    main()
