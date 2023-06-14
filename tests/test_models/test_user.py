#!/usr/bin/python3
"""Module to test the User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test case class for User instances"""

    def setUp(self):
        """Set up for the tests"""
        self.user = User()

    def tearDown(self):
        """Tear down for the tests"""
        del self.user

    def test_attributes(self):
        """Tests if the User attributes exist and are as expected"""

        # Test if attributes exist
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

        # Test if attributes are of the expected type and initial value
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "")

        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "")

        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "")

        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
