import unittest

from Lesson2.tasks.src.sum_ex import sum_ex


class SumExTestCase(unittest.TestCase):

    def test_sumEx_sumThreePositiveNumbers_sumNumbersInSequence(self):
        self.assertEqual(sum_ex([1, 2, 3]), 6)

    def test_sumEx_sumFourPositiveNumbers_sumNumbersInSequence(self):
        self.assertEqual(sum_ex([0, 2, 3, 4]), 9)

    def test_sumEx_sumRoundPositiveNumbers_sumNumbersInSequence(self):
        self.assertEqual(sum_ex([10, 20, 30]), 60)

    def test_sumEx_sumThreeNegativeNumbers_sumNumbersInSequence(self):
        self.assertEqual(sum_ex([-1, -2, -3]), -6)

    def test_sumEx_sumPositiveAndNegativeNumbers_sumNumbersInSequence(self):
        self.assertEqual(sum_ex([-1, 2, 3]), 4)

    def test_sumEx_sumTwoOppositeNumbers_sumNumbersInSequence(self):
        self.assertEqual(sum_ex([-1, 1]), 0)

    def test_sumEx_sumTwoOppositeNumbersAndZero_sumNumbersInSequence(self):
        self.assertEqual(sum_ex([-3, 0, 3]), 0)
