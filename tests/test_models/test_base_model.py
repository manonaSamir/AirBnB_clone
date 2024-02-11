#!/usr/bin/python3
""" base model testing """


import unittest
from models.base_model import BaseModel
import datetime
import uuid
import models

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""
    def test_init_method(self):
        """Test the __init__() method"""
        models = BaseModel()
        self.assertIsInstance(models.id, str)
        self.assertIsInstance(models.created_at, datetime.datetime)
        self.assertIsInstance(models.updated_at, datetime.datetime)      

    def test_init_with_data_method(self):
        id_val = str(uuid.uuid4())
        created_at_val = "2024-02-10T08:00:00"
        updated_at_val = "2024-02-10T09:00:00"
        kwargs = {
            "id": id_val,
            "created_at": created_at_val,
            "updated_at": updated_at_val,
            "other_attribute": "other_value"
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, id_val)
        self.assertEqual(obj.created_at,
                         datetime.datetime.fromisoformat(str(created_at_val)))
        self.assertEqual(obj.updated_at,
                         datetime.datetime.fromisoformat(str(updated_at_val)))
        self.assertEqual(obj.other_attribute, "other_value")

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_str_method(self):
        """test str method"""
        self.assertEqual(str, type(BaseModel().id))

    def test_save_method(self):
        """test save method"""
        obj = BaseModel()
        old_date = obj.updated_at
        obj.save()
        new_date = obj.updated_at
        self.assertNotEqual(old_date, new_date)

    def test_dict_method(self):
        """Test the dict method"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertTrue(isinstance(base_model_dict, dict))
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertTrue(isinstance(base_model_dict["created_at"], str))
        self.assertTrue(isinstance(base_model_dict["updated_at"], str))
        self.assertTrue(isinstance(base_model_dict["id"], str))


if __name__ == "__main__":
    unittest.main()
