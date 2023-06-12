#!/usr/bin/env python3
""" Unit tests for the FileStorage """

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """ Class providing unit tests for the FileStorage class """

    def setUp(self):
        """ Set up test environment """
        self.fs = FileStorage()

    def tearDown(self):
        """ Tear down test environment """
        del self.fs

    def test_file_path(self):
        """ Test __file_path """
        self.assertIsInstance(self.fs._FileStorage__file_path, str)

    def test_objects(self):
        """ Test __objects """
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

    def test_all(self):
        """ Test all() """
        all_objects = self.fs.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """ Test new() """
        bm = BaseModel()
        self.fs.new(bm)
        key = "{}.{}".format(type(bm).__name__, bm.id)
        self.assertIn(key, self.fs.all())

    def test_save(self):
        """ Test save() """
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        key = "{}.{}".format(type(bm).__name__, bm.id)
        with open(self.fs._FileStorage__file_path, "r") as file:
            self.assertIn(key, file.read())

    def test_reload(self):
        """ Test reload() """
        self.fs.reload()
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

if __name__ == "__main__":
    unittest.main()
