import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_part_one(self):
        self.assertEqual(main.part_one(self.input), 7)

    def test_part_two(self):
        self.assertEqual(main.part_two(self.input), 5)
