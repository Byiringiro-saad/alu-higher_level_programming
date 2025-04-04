#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Unit tests for the Base class"""

    def test_init_with_id(self):
        base = Base(42)
        self.assertEqual(base.id, 42)

    def test_init_without_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_to_json_string_none(self):
        """Test conversion of None to JSON string"""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
        self.assertIsInstance(json_str, str)

    def test_to_json_string_empty_list(self):
        """Test conversion of empty list to JSON string"""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")
        self.assertIsInstance(json_str, str)

    def test_to_json_string_with_data(self):
        """Test conversion of list of dicts to JSON string"""
        json_str = Base.to_json_string([{ 'id': 12 }])
        self.assertEqual(json_str, '[{"id": 12}]')
        self.assertIsInstance(json_str, str)

    def test_from_json_string_none(self):
        """Test conversion from None JSON string"""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])
        self.assertIsInstance(result, list)

    def test_from_json_string_empty_list(self):
        """Test conversion from empty list JSON string"""
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])
        self.assertIsInstance(result, list)

    def test_from_json_string_with_data(self):
        """Test conversion from JSON string to list"""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{"id": 89}])
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
