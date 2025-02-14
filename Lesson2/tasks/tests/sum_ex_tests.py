import unittest

from src.sum_ex import sum_ex

class SumExTestCase(unittest.TestCase):

    def test_sumWith_PositiveNumbers_True(self):

        self.assertEqual(sum_ex([1, 2, 3]),6)
        self.assertEqual(sum_ex([0, 2, 3, 4]),9)
        self.assertEqual(sum_ex([10, 20, 30]), 60)

    def test_sumWith_negativeNumbers_True(self):

        self.assertEqual(sum_ex([-1, -2, -3]), -6)
        self.assertEqual(sum_ex([-1, 2, 3]), 4)

    def test_sumWith_mixedNumbers_True(self):

        self.assertEqual(sum_ex([-1, 1]),0)
        self.assertEqual(sum_ex([-1, 0 , 1]), 0)