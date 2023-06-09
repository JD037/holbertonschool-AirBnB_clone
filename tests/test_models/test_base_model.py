#!/usr/bin/env python3
"""Test cases for the BaseModel"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def setUp(self):
        """Set up method for each test."""
        self.base = BaseModel()

    def test_id(self):
        """Test for id attribute."""
        self.assertTrue(hasattr(self.base, "id"))

    def test_created_at(self):
        """Test for created_at attribute."""
        self.assertTrue(hasattr(self.base, "created_at"))

    def test_updated_at(self):
        """Test for updated_at attribute."""
        self.assertTrue(hasattr(self.base, "updated_at"))

if __name__ == "__main__":
    unittest.main()
