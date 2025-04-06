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

    def test_invalid_x_type_string(self):
        """Test passing a string as x should raise ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, "3")

    def test_invalid_y_type_string(self):
        """Test passing a string as y should raise ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, "4")

    def test_width_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_height_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_x_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, "3")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 3, "4")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_width_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -3, 0)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 0, -4)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_display_no_offset(self):
        """Test display without x and y offsets."""
        r = Rectangle(2, 3)
        r.display()
        output = self.held_output.getvalue()
        expected = "##\n##\n##\n"
        self.assertEqual(output, expected)

    def test_display_with_x_offset(self):
        """Test display with x offset."""
        r = Rectangle(2, 3, 2)
        r.display()
        output = self.held_output.getvalue()
        expected = "  ##\n  ##\n  ##\n"
        self.assertEqual(output, expected)

    def test_display_with_y_offset(self):
        """Test display with y offset."""
        r = Rectangle(2, 3, 0, 2)
        r.display()
        output = self.held_output.getvalue()
        expected = "\n\n##\n##\n##\n"
        self.assertEqual(output, expected)

    def test_display_with_x_and_y_offset(self):
        """Test display with both x and y offsets."""
        r = Rectangle(2, 3, 2, 2)
        r.display()
        output = self.held_output.getvalue()
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
