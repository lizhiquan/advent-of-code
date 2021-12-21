import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.scanners = main.read_input('input_test.txt')

    def test_part_one(self):
        self.assertEqual(main.part_one(self.scanners), 79)

    def test_part_two(self):
        main.part_one(self.scanners)
        self.assertEqual(main.part_two(self.scanners), 3621)
