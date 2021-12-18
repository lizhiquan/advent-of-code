import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.x_range, self.y_range = (20, 30), (-10, -5)

    def test_part_one(self):
        self.assertEqual(main.part_one(self.x_range, self.y_range), 45)

    def test_part_two(self):
        self.assertEqual(main.part_two(self.x_range, self.y_range), 112)
