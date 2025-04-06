#!/usr/bin/python3
import os
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def tearDown(self):
        """Remove created files after each test."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_create_square(self):
        """Test Square(1)"""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_create_square_with_x(self):
        """Test Square(1, 2)"""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_create_square_with_x_y(self):
        """Test Square(1, 2, 3)"""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_create_square_invalid_size_type(self):
        """Test Square("1") raises TypeError"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_create_square_invalid_x_type(self):
        """Test Square(1, "2") raises TypeError"""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_create_square_invalid_y_type(self):
        """Test Square(1, 2, "3") raises TypeError"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_create_square_with_extra_argument(self):
        """Test Square(1, 2, 3, 4)"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4)

    def test_create_square_negative_size(self):
        """Test Square(-1) raises ValueError"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_create_square_negative_x(self):
        """Test Square(1, -2) raises ValueError"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_create_square_negative_y(self):
        """Test Square(1, 2, -3) raises ValueError"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_create_square_zero_size(self):
        """Test Square(0) raises ValueError"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Test __str__ method"""
        s = Square(5, 1, 2, 99)
        output = str(s)
        self.assertIn("[Square]", output)
        self.assertIn("(99)", output)
        self.assertIn("5", output)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s_dict, expected)

    def test_update_args(self):
        """Test update with *args"""
        s = Square(5, 5, 5, 5)
        s.update(89)
        self.assertEqual(s.id, 89)

        s.update(89, 1)
        self.assertEqual(s.size, 1)

        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """Test update with **kwargs"""
        s = Square(5, 5, 5, 5)

        s.update(id=89)
        self.assertEqual(s.id, 89)

        s.update(id=89, size=1)
        self.assertEqual(s.size, 1)

        s.update(id=89, size=1, x=2)
        self.assertEqual(s.x, 2)

        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(s.y, 3)

    def test_create_with_id(self):
        """Test Square.create with id only"""
        s = Square.create(id=89)
        self.assertEqual(s.id, 89)

    def test_create_with_id_size(self):
        """Test Square.create with id and size"""
        s = Square.create(id=89, size=1)
        self.assertEqual(s.size, 1)

    def test_create_with_id_size_x(self):
        """Test Square.create with id, size, and x"""
        s = Square.create(id=89, size=1, x=2)
        self.assertEqual(s.x, 2)

    def test_create_with_id_size_x_y(self):
        """Test Square.create with id, size, x, and y"""
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test save_to_file with None"""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content.strip(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list"""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content.strip(), "[]")

    def test_save_to_file_square(self):
        """Test save_to_file with a list of one Square"""
        s = Square(1)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn("size", content)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file doesn't exist"""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_load_from_file_exists(self):
        """Test load_from_file when file exists"""
        s = Square(1)
        Square.save_to_file([s])
        squares = Square.load_from_file()
        self.assertIsInstance(squares, list)
        self.assertIsInstance(squares[0], Square)

if __name__ == "__main__":
    unittest.main()
