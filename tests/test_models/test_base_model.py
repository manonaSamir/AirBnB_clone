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

    def test_to_dict_type(self):
        obj = BaseModel()
        self.assertTrue(dict, type(obj.to_dict()))
        
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
        
    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)
if __name__ == "__main__":
    unittest.main()
