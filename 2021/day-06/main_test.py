import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.input = [3, 4, 3, 1, 2]

    def test_part_one(self):
        self.assertEqual(main.solve(self.input, 80), 5934)

    def test_part_two(self):
        self.assertEqual(main.solve(self.input, 256), 26984457539)
