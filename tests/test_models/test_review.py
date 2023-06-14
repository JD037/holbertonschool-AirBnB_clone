#!/usr/bin/python3
"""Module to test the Review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case class for Review instances"""

    def setUp(self):
        """Set up for the tests"""
        self.review = Review()

    def tearDown(self):
        """Tear down for the tests"""
        del self.review

    def test_attributes(self):
        """Tests if the Review attributes exist and are as expected"""

        # Test if attributes exist
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

        # Test if attributes are of the expected type and initial value
        self.assertIsInstance(self.review.place_id, str)
        self.assertEqual(self.review.place_id, "")
        self.assertIsInstance(self.review.user_id, str)
        self.assertEqual(self.review.user_id, "")
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
