import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.algo, self.image = main.read_input('input_test.txt')

    def test_part_one(self):
        self.assertEqual(main.part_one(self.algo, self.image), 35)

    def test_part_two(self):
        self.assertEqual(main.part_two(self.algo, self.image), 3351)
