import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.input_1 = main.read_input('input_test_1.txt')
        self.input_2 = main.read_input('input_test_2.txt')
        self.input_3 = main.read_input('input_test_3.txt')

    def test_part_one(self):
        self.assertEqual(main.part_one(self.input_1), 10)
        self.assertEqual(main.part_one(self.input_2), 19)
        self.assertEqual(main.part_one(self.input_3), 226)

    def test_part_two(self):
        self.assertEqual(main.part_two(self.input_1), 36)
        self.assertEqual(main.part_two(self.input_2), 103)
        self.assertEqual(main.part_two(self.input_3), 3509)
