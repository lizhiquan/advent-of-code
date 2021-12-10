import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.draws, self.boards = main.read_input('input_test.txt')

    def test_part_one(self):
        self.assertEqual(main.part_one(self.draws, self.boards), 4512)

    def test_part_two(self):
        self.assertEqual(main.part_two(self.draws, self.boards), 1924)
