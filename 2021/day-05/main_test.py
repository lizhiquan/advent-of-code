import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.input = main.read_input('input_test.txt')

    def test_part_one(self):
        actual = main.part_one(self.input)
        expected = 5
        self.assertEqual(actual, expected)

    def test_part_two(self):
        actual = main.part_two(self.input)
        expected = 12
        self.assertEqual(actual, expected)
