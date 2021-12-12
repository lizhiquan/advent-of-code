import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.input = main.read_input('input_test.txt')

    def test_part_one(self):
        self.assertEqual(main.part_one(self.input), 15)

    def test_part_two(self):
        self.assertEqual(main.part_two(self.input), 1134)
