#!/usr/bin/python3
"""Module to test the Amenity class"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test case class for Amenity instances"""

    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down for the tests"""
        del self.amenity

    def test_attributes(self):
        """Tests if the Amenity attributes exist and are as expected"""

        # Test if attribute exists
        self.assertTrue(hasattr(self.amenity, "name"))

        # Test if attribute is of the expected type and initial value
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
