import unittest

from Lesson2.tasks.src.sum_ex import sum_ex


class SumExTestCase(unittest.TestCase):

    def test_sumEx_sumThreePositiveNumbers_sumNumbersInSequence(self):
        sum = 6

        sum_result = sum_ex([1, 2, 3])

        self.assertEqual(sum, sum_result)

    def test_sumEx_sumFourPositiveNumbers_sumNumbersInSequence(self):
        sum = 9

        sum_result = sum_ex([0, 2, 3, 4])

        self.assertEqual(sum, sum_result)

    def test_sumEx_sumRoundPositiveNumbers_sumNumbersInSequence(self):
        sum = 60

        sum_result = sum_ex([10, 20, 30])

        self.assertEqual(sum, sum_result)

    def test_sumEx_sumThreeNegativeNumbers_sumNumbersInSequence(self):
        sum = -6

        sum_result = sum_ex([-1, -2, -3])

        self.assertEqual(sum, sum_result)

    def test_sumEx_sumPositiveAndNegativeNumbers_sumNumbersInSequence(self):
        sum = 4

        sum_result = sum_ex([-1, 2, 3])

        self.assertEqual(sum, sum_result)

    def test_sumEx_sumTwoOppositeNumbers_sumNumbersInSequence(self):
        sum = 0

        sum_result = sum_ex([-1, 1])

        self.assertEqual(sum, sum_result)

    def test_sumEx_sumTwoOppositeNumbersAndZero_sumNumbersInSequence(self):
        sum = 0

        sum_result = sum_ex([-3, 0, 3])

        self.assertEqual(sum, sum_result)
