#!/usr/bin/python3
"""file storage test_cases module"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os


class Testing_file_storage(unittest.TestCase):
    """file storage test_case"""

    file_storage_object = FileStorage()

    def test_case(self):
        count_of_objects_before_update = len(self.file_storage_object.all())
        old_dict = self.file_storage_object.all().copy()

        new_base_model_object = BaseModel()
        self.file_storage_object.new(new_base_model_object)

        self.file_storage_object.save()

        self.file_storage_object.reload()

        count_of_objects_after_update = len(self.file_storage_object.all())

        self.assertEqual(count_of_objects_before_update + 1,
                         count_of_objects_after_update)

        obj_key = f"BaseModel.{new_base_model_object.id}"
        self.assertIn(obj_key, self.file_storage_object.all())

        reloaded_obj = self.file_storage_object.all()[obj_key]
        self.assertEqual(reloaded_obj.updated_at,
                         new_base_model_object.updated_at)

        os.remove("file.json")
        new_base_model = BaseModel()
        new_base_model.save()
        self.assertTrue(os.path.exists("file.json"))
