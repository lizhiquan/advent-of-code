import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def test_part_one(self):
        self.assertEqual(main.part_one(self.input), 37)

    def test_part_two(self):
        self.assertEqual(main.part_two(self.input), 168)
