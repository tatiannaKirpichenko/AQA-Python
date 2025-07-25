import unittest

from Lesson2.tasks.src.sum_ex import sum_ex


class SumExTestCase(unittest.TestCase):

    def test_sumEx_sumThreePositiveNumbers_sumNumbersInSequence(self):
        sum_array_numbers = [1, 2, 3]

        sum_result = sum_ex(sum_array_numbers)

        self.assertEqual(6, sum_result)

    def test_sumEx_sumFourPositiveNumbers_sumNumbersInSequence(self):
        sum_array_numbers = [0, 2, 3, 4]

        sum_result = sum_ex(sum_array_numbers)

        self.assertEqual(9, sum_result)

    def test_sumEx_sumRoundPositiveNumbers_sumNumbersInSequence(self):
        sum_array_numbers = [10, 20, 30]

        sum_result = sum_ex(sum_array_numbers)

        self.assertEqual(60, sum_result)

    def test_sumEx_sumThreeNegativeNumbers_sumNumbersInSequence(self):
        sum_array_numbers = [-1, -2, -3]

        sum_result = sum_ex(sum_array_numbers)

        self.assertEqual(-6, sum_result)

    def test_sumEx_sumPositiveAndNegativeNumbers_sumNumbersInSequence(self):
        sum_array_numbers = [-1, 2, 3]

        sum_result = sum_ex(sum_array_numbers)

        self.assertEqual(4, sum_result)

    def test_sumEx_sumTwoOppositeNumbers_sumNumbersInSequence(self):
        sum_array_numbers = [-1, 1]

        sum_result = sum_ex(sum_array_numbers)

        self.assertEqual(0, sum_result)

    def test_sumEx_sumTwoOppositeNumbersAndZero_sumNumbersInSequence(self):
        sum_array_numbers = [-3, 0, 3]

        sum_result = sum_ex(sum_array_numbers)

        self.assertEqual(0, sum_result)
