#!/usr/bin/python3
import os
import io
import sys
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
        with self.assertRaises(TypeError):
            rectangle = Rectangle("width", 10)

    def test_invalid_height_type(self):
        """Test invalid height (not an integer)."""
        with self.assertRaises(TypeError):
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
        with self.assertRaises(TypeError):
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
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_y_type_string(self):
        """Test passing a string as y should raise ValueError"""
        with self.assertRaises(TypeError):
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

    def test_area_exists(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str_exists(self):
        r = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), expected)

    def test_display_without_x_y(self):
        r = Rectangle(2, 3)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = "##\n##\n##\n"
        self.assertEqual(captured.getvalue(), expected)

    def test_display_without_y(self):
        r = Rectangle(2, 3, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = " ##\n ##\n ##\n"
        self.assertEqual(captured.getvalue(), expected)

    def test_display_exists(self):
        r = Rectangle(2, 3, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = "\n ##\n ##\n ##\n"
        self.assertEqual(captured.getvalue(), expected)

    def test_to_dictionary_exists(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_exists(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_update_id_width_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_update_id_width_height_x(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_id_width_height_x_y(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kwargs_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89)
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1)
        self.assertEqual(r.width, 1)

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2)
        self.assertEqual(r.height, 2)

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3)
        self.assertEqual(r.x, 3)

    def test_update_kwargs_id_width_height_x_y(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        r = Rectangle.create(id=89)
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(id=89, width=1)
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        r = Rectangle.create(id=89, width=1, height=2)
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        r = Rectangle.create(id=89, width=1, height=2, x=3)
        self.assertEqual(r.x, 3)

    def test_create_id_width_height_x_y(self):
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        """Test saving None to file."""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content.strip(), "[]")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangle(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertIn('"width": 1', f.read())

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file_exists(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertTrue(all(isinstance(r, Rectangle) for r in rectangles))

if __name__ == "__main__":
    unittest.main()
