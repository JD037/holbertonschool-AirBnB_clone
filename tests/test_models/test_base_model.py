#!/usr/bin/env python3
"""Test cases for the BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """ Class providing unit tests for the BaseModel class """
    
    def setUp(self):
        """ Set up test environment """
        self.bm = BaseModel()

    def tearDown(self):
        """ Tear down test environment """
        del self.bm

    def test_id_creation(self):
        """ Test that id is created properly """
        self.assertIsInstance(self.bm.id, str)

    def test_datetime_created(self):
        """ Test that created_at is a datetime object """
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_datetime_updated(self):
        """ Test that updated_at is a datetime object """
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str_representation(self):
        """ Test the informal string representation of an instance """
        string = "[{}] ({}) {}".format(self.bm.__class__.__name__, self.bm.id, self.bm.__dict__)
        self.assertEqual(str(self.bm), string)

    def test_save_method(self):
        """ Test save method """
        old_datetime = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(old_datetime, self.bm.updated_at)

    def test_to_dict_method(self):
        """ Test to_dict method """
        dict_rep = self.bm.to_dict()
        self.assertEqual(dict_rep["id"], self.bm.id)
        self.assertEqual(dict_rep["__class__"], self.bm.__class__.__name__)
        self.assertEqual(dict_rep["created_at"], self.bm.created_at.isoformat())
        self.assertEqual(dict_rep["updated_at"], self.bm.updated_at.isoformat())

    def test_created_at(self):
        """Test for created_at attribute."""
        self.assertTrue(hasattr(self.bm, "created_at"))
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_updated_at(self):
        """Test for updated_at attribute."""
        self.assertTrue(hasattr(self.bm, "updated_at"))
        self.assertIsInstance(self.bm.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
