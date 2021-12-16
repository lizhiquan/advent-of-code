import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.map = main.read_input('input_test.txt')

    def test_part_one(self):
        self.assertEqual(main.part_one(self.map), 40)

    def test_part_two(self):
        self.assertEqual(main.part_two(self.map), 315)
