import unittest

import main


class TestCase(unittest.TestCase):
    def test_part_one(self):
        packets = [
            main.Packet.from_hex('8A004A801A8002F478'),
            main.Packet.from_hex('620080001611562C8802118E34'),
            main.Packet.from_hex('C0015000016115A2E0802F182340'),
            main.Packet.from_hex('A0016C880162017C3686B18A3D4780'),
        ]

        packet = packets[0]
        self.assertEqual(packet.version, 4)
        self.assertEqual(len(packet.subpackets), 1)
        self.assertEqual(packet.subpackets[0].version, 1)
        self.assertEqual(len(packet.subpackets[0].subpackets), 1)
        self.assertEqual(packet.subpackets[0].subpackets[0].version, 5)
        self.assertEqual(len(packet.subpackets[0].subpackets[0].subpackets), 1)
        self.assertEqual(packet.subpackets[0].subpackets[0].subpackets[0].version, 6)

        self.assertEqual(main.part_one(packets[0]), 16)
        self.assertEqual(main.part_one(packets[1]), 12)
        self.assertEqual(main.part_one(packets[2]), 23)
        self.assertEqual(main.part_one(packets[3]), 31)

    def test_part_two(self):
        packets = [
            main.Packet.from_hex('C200B40A82'),
            main.Packet.from_hex('04005AC33890'),
            main.Packet.from_hex('880086C3E88112'),
            main.Packet.from_hex('CE00C43D881120'),
            main.Packet.from_hex('D8005AC2A8F0'),
            main.Packet.from_hex('F600BC2D8F'),
            main.Packet.from_hex('9C005AC2F8F0'),
            main.Packet.from_hex('9C0141080250320F1802104A08'),
        ]

        self.assertEqual(main.part_two(packets[0]), 3)
        self.assertEqual(main.part_two(packets[1]), 54)
        self.assertEqual(main.part_two(packets[2]), 7)
        self.assertEqual(main.part_two(packets[3]), 9)
        self.assertEqual(main.part_two(packets[4]), 1)
        self.assertEqual(main.part_two(packets[5]), 0)
        self.assertEqual(main.part_two(packets[6]), 0)
        self.assertEqual(main.part_two(packets[7]), 1)
