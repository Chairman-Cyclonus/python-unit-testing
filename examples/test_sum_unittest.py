import unittest


class TestBuiltInSum(unittest.TestCase):
    def test_list(self):
        self.assertEqual(sum([1, 2, 3]), 6)

    def test_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6)


if __name__ == "__main__":
    unittest.main()
