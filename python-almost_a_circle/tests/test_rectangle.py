#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test the Rectangle class."""

    def test_initialization_valid(self):
        """Test the initialization of a Rectangle instance."""
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_initialization_with_custom_position(self):
        """Test initialization with custom x and y."""
        rectangle = Rectangle(5, 10, 2, 3)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_initialization_with_id(self):
        """Test initialization with a specific id."""
        rectangle = Rectangle(5, 10, 2, 3, 100)
        self.assertEqual(rectangle.id, 100)

    def test_width_setter(self):
        """Test setting the width via setter."""
        rectangle = Rectangle(5, 10)
        rectangle.width = 20
        self.assertEqual(rectangle.width, 20)

    def test_height_setter(self):
        """Test setting the height via setter."""
        rectangle = Rectangle(5, 10)
        rectangle.height = 15
        self.assertEqual(rectangle.height, 15)

    def test_x_setter(self):
        """Test setting the x coordinate via setter."""
        rectangle = Rectangle(5, 10)
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

    def test_y_setter(self):
        """Test setting the y coordinate via setter."""
        rectangle = Rectangle(5, 10)
        rectangle.y = 8
        self.assertEqual(rectangle.y, 8)

    def test_invalid_width_type(self):
        """Test invalid width (not an integer)."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle("width", 10)

    def test_invalid_height_type(self):
        """Test invalid height (not an integer)."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, "height")

    def test_invalid_x_negative(self):
        """Test invalid x coordinate (negative value)."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, -1)

    def test_invalid_y_negative(self):
        """Test invalid y coordinate (negative value)."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, 0, -1)

    def test_invalid_width_zero_or_negative(self):
        """Test invalid width (less than or equal to 0)."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 10)

    def test_invalid_height_zero_or_negative(self):
        """Test invalid height (less than or equal to 0)."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 0)

    def test_invalid_width_setter_type(self):
        """Test setting invalid width via setter (not an integer)."""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rectangle.width = "invalid"

    def test_invalid_height_setter_negative(self):
        """Test setting invalid height via setter (less than or equal to 0)."""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rectangle.height = -5

    def test_invalid_x_setter_negative(self):
        """Test setting invalid x via setter (negative value)."""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rectangle.x = -5

    def test_invalid_y_setter_negative(self):
        """Test setting invalid y via setter (negative value)."""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rectangle.y = -5

if __name__ == "__main__":
    unittest.main()
