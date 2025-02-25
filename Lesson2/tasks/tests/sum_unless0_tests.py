import unittest

from Lesson2.tasks.src.sum_ex import sum_unless0


class TestSumUnless0(unittest.TestCase):

    def test_sumUnless0_sumThreeNumbersWithoutZero_sumNumbersInSequence(self):
        sum = 6

        sum_result = sum_unless0([1, 2, 3])

        self.assertEqual(sum, sum_result)

    def test_sumUnless0_countSumInSequenceOfNumbersUpToTheFirstZeroEncountered_sumNumbersInSequence(self):
        sum = 3

        sum_result = sum_unless0([1, 2, 0, 4])

        self.assertEqual(sum, sum_result)

    def test_sumUnless0_countSumInSequenceOfNumbersUpToTheFirstZeroEncounteredZeroTwo_sumNumbersInSequence(self):
        sum = 6

        sum_result = sum_unless0([1, 2, 3, 0, 0, 4])

        self.assertEqual(sum, sum_result)

    def test_sumUnless0_sumFourNumbersWithoutZero_sumNumbersInSequence(self):
        sum = 9

        sum_result = sum_unless0([2, 3, 4, 0])

        self.assertEqual(sum, sum_result)

    def test_sumUnless0_countsTheSumOfSequenceOfNumbersUpToTheFirstZeroFirstElementZero_sumNumbersInSequence(self):
        sum = 0

        sum_result = sum_unless0([0, 1, 2])

        self.assertEqual(sum, sum_result)

    def test_sumUnless0_countsTheSumOfSequenceOfNumbersUpToTheFirstZeroFirstElementTwoZero_sumNumbersInSequence(self):
        sum = 0

        sum_result = sum_unless0([0, 0, 1, 2])

        self.assertEqual(sum, sum_result)
