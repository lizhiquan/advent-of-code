import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.template, self.rules = main.read_input('input_test.txt')

    def test_part_one(self):
        self.assertEqual(main.solve(self.template, self.rules, 10), 1588)

    def test_part_two(self):
        self.assertEqual(main.solve(self.template, self.rules, 40), 2188189693529)
