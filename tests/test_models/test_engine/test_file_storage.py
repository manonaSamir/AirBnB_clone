#!/usr/bin/python3

""" testing file storage"""

import unittest
from models.base_model import BaseModel
from models import storage

class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """
    def test_all_method(self):        
        obj = BaseModel()     
        result = storage.all()       
        self.assertIsInstance(result, dict)

    def test_empty_list(self):
            """ empty List """
            self.assertEqual(len(storage.all()), 0)
