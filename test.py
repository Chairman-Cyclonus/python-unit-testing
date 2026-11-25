import unittest
from fractions import Fraction

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        numbers = [1, 2, 3]
        self.assertEqual(sum(numbers), 6)

    def test_list_fraction(self):
        numbers = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        self.assertEqual(sum(numbers), 1)


if __name__ == "__main__":
    unittest.main()


# The runner showed F. and reported that it ran two tests with one failure.
# The dot means the integer test passed because 1 + 2 + 3 equals 6.
# The F marks the fraction test. Its traceback points to the assertion
# that expected 1, but the three fractions actually add up to 9/10.
# Changing the expected value to Fraction(9, 10) makes both tests pass.
