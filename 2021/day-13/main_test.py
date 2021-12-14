import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.dots, self.folds = main.read_input('input_test.txt')

    def test_part_one(self):
        self.assertEqual(main.part_one(self.dots, self.folds), 17)
