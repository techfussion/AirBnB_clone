#!/usr/bin/python3
"""test cases for the base_module module"""


import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class Test_base_model(unittest.TestCase):
    """test class for base module"""

    obj = BaseModel()
    base = BaseModel()

    obj.name = "Model Name"
    obj.my_number = 2

    def test_consturctor_with_no_kwargs(self):
        """testing constructor without kwargs"""

        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertEqual(self.obj.name, "Model Name")
        self.assertEqual(self.obj.my_number, 2)

    def test_kwargs_constructor(self):
        """testing constructor with kwargs"""

        data = {
            'id': 'some_id',
            'created_at': '2023-08-13T12:34:56.789',
            'updated_at': '2023-08-13T12:34:56.789',
            'name': 'Test Model'
        }
        obj = BaseModel(**data)

        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

        self.assertEqual(obj.id, 'some_id')
        self.assertEqual(obj.name, 'Test Model')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(self.obj.name, "Model Name")
        self.assertEqual(self.obj.my_number, 2)

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        my_base_json = self.base.to_dict()
        new_base = BaseModel(**my_base_json)
        self.assertIsInstance(new_base, BaseModel)
        self.assertIsInstance(new_base.id, str)
        self.assertIsInstance(new_base.created_at, datetime)
        self.assertIsInstance(new_base.updated_at, datetime)
        self.assertEqual(new_base.name, "My First Model")
        self.assertEqual(new_base.my_number, 2)
        self.assertNotEqual(new_base, self.base)
        self.assertDictEqual(new_base.__dict__, self.base.__dict__)

    def test_save(self):
        """testing the save function"""

        before_the_update = self.obj.updated_at
        self.obj.save()
        After_the_update = self.obj.updated_at
        self.assertNotEqual(before_the_update, After_the_update)

    def printing_str_formats(self):
        """testing the str function"""

        expected_str = f"[{self.obj.__class__.__name__}]\
                       {self.obj.id}) <{self.base.__dict__}>"
        self.assertEqual(expected_str, self.obj.__str__())

    def to_dict(self):
        """testing to_dict function"""

        to_dict = self.obj.to_dict()
        expected_dict = self.obj.__dict__.copy()
        expected_dict["__class__"] = self.obj.__class__.__name__
        expected_dict["updated_at"] = self.obj.updated_at.isoformat()
        expected_dict["created_at"] = self.obj.created_at.isoformat()
        self.assertDictEqual(expected_dict, to_dict)
