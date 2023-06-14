#!/usr/bin/python3
"""Module to test the State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test case class for State instances"""

    def setUp(self):
        """Set up for the tests"""
        self.state = State()

    def tearDown(self):
        """Tear down for the tests"""
        del self.state

    def test_attributes(self):
        """Tests if the State attribute exists and is as expected"""

        # Test if attribute exists
        self.assertTrue(hasattr(self.state, "name"))

        # Test if attribute is of the expected type and initial value
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()
