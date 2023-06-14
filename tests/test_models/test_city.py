#!/usr/bin/python3
"""Module to test the City class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test case class for City instances"""

    def setUp(self):
        """Set up for the tests"""
        self.city = City()

    def tearDown(self):
        """Tear down for the tests"""
        del self.city

    def test_attributes(self):
        """Tests if the City attributes exist and are as expected"""

        # Test if attributes exist
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

        # Test if attributes are of the expected type and initial value
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.name, "")
        self.assertIsInstance(self.city.state_id, str)
        self.assertEqual(self.city.state_id, "")


if __name__ == "__main__":
    unittest.main()
