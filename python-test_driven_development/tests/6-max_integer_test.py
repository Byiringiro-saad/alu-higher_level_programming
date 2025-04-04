#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestCase class for testing the max_integer function
    """

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        """Test with a list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1, -5]), -1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-10, 0, 10, 0]), 10)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 5, 5, 3]), 5)
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_single_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([0]), 0)

    def test_floats(self):
        """Test with a list of floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1.5, 3.5, 2.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

    def test_mixed_types(self):
        """Test with a list of mixed integer and float types"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([5, 4.5, 3, 2.5]), 5)

    def test_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")
        self.assertEqual(max_integer(["hello", "world"]), "world")

    def test_mixed_strings_and_numbers(self):
        """Test that function raises TypeError when mixing incomparable types"""
        with self.assertRaises(TypeError):
            max_integer([1, "string"])

    def test_none_argument(self):
        """Test with None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable(self):
        """Test with a non-iterable argument"""
        with self.assertRaises(TypeError):
            max_integer(123)

    def test_default_argument(self):
        """Test with default argument (empty list)"""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()