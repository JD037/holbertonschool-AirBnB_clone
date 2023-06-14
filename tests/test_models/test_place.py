#!/usr/bin/python3
"""Module to test the Place class"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test case class for Place instances"""

    def setUp(self):
        """Set up for the tests"""
        self.place = Place()

    def tearDown(self):
        """Tear down for the tests"""
        del self.place

    def test_attributes(self):
        """Tests if the Place attributes exist and are as expected"""

        # Test if attributes exist
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

        # Test if attributes are of the expected type and initial value
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "")

        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, "")

        self.assertIsInstance(self.place.name, str)
        self.assertEqual(self.place.name, "")

        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description, "")

        self.assertIsInstance(self.place.number_rooms, int)
        self.assertEqual(self.place.number_rooms, 0)

        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)

        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 0)

        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 0)

        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 0.0)

        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 0.0)

        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
