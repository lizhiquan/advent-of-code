import unittest

import main


class TestCase(unittest.TestCase):
    def setUp(self):
        self.snailfishes = main.read_input('input_test.txt')

    def test_parse_snailfish(self):
        data_list = [
            '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
            '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
            '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
            '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
            '[7,[5,[[3,8],[1,4]]]]',
            '[[2,[2,2]],[8,[8,1]]]',
            '[2,9]',
            '[1,[[[9,3],9],[[9,0],[0,7]]]]',
            '[[[5,[7,4]],7],1]',
            '[[[[4,2],2],6],[8,7]]'
        ]
        for data in data_list:
            snailfish = main.Snailfish.parse(data)
            self.assertEqual(str(snailfish), data)

    def test_addition(self):
        a = main.Snailfish.parse('[[[[4,3],4],4],[7,[[8,4],9]]]')
        b = main.Snailfish.parse('[1,1]')
        c = a + b
        self.assertEqual(str(c), '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

        a = main.Snailfish.parse('[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]')
        b = main.Snailfish.parse('[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]')
        c = a + b
        self.assertEqual(str(c), '[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]')

    def test_part_one(self):
        self.assertEqual(main.part_one(self.snailfishes), 4140)

    def test_part_two(self):
        self.assertEqual(main.part_two(self.snailfishes), 3993)
