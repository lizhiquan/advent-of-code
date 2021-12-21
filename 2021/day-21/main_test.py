import unittest

import main


class TestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(main.part_one(4, 8), 739785)

    def test_part_two(self):
        self.assertEqual(main.part_two(4, 8), 444356092776315)
