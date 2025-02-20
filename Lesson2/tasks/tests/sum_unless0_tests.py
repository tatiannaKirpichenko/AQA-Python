import unittest

from Lesson2.tasks.src.sum_ex import sum_unless0


class TestSumUnless0(unittest.TestCase):

    def test_sumUnless0_sumThreeNumbersWithoutZero_sumNumbersInSequence(self):
        self.assertEqual(sum_unless0([1, 2, 3]), 6)

    def test_sumUnless0_countSumInSequenceOfNumbersUpToTheFirstZeroEncountered_sumNumbersInSequence(self):
        self.assertEqual(sum_unless0([1, 2, 0, 4]), 3)

    def test_sumUnless0_countSumInSequenceOfNumbersUpToTheFirstZeroEncounteredZeroTwo_sumNumbersInSequence(self):
        self.assertEqual(sum_unless0([1, 2, 3, 0, 0, 4]), 6)

    def test_sumUnless0_sumFourNumbersWithoutZero_sumNumbersInSequence(self):
        self.assertEqual(sum_unless0([2, 3, 4, 0]), 9)

    def test_sumUnless0_countsTheSumOfSequenceOfNumbersUpToTheFirstZeroFirstElementZero_sumNumbersInSequence(self):
        self.assertEqual(sum_unless0([0, 1, 2]), 0)

    def test_sumUnless0_countsTheSumOfSequenceOfNumbersUpToTheFirstZeroFirstElementTwoZero_sumNumbersInSequence(self):
        self.assertEqual(sum_unless0([0, 0, 1, 2]), 0)
