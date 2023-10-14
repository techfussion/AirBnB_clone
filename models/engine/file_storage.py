#!/usr/bin/python3
import json
import os.path
"""
    Class (FileStorage): Serializes instances to a JSON file /
    and deserializes JSON file to instances
"""


class FileStorage:
    """Representation/Blueprint of FileStorage"""

    __file_path = 'storage.json'
    __objects = dict()

    def all(self) -> dict:
        """
            Returns:
                __objects -> dictionary: private class attribute
        """
        return self.__objects

    def new(self, obj):
        """
            Sets in __objects the obj with key <obj class name>.id

            Args:
                obj: the object/instance to store
        """
        self.__objects[f"{obj["__class__"]}.{obj["id"]}"] = obj

    def save(self):
        """
            Serializes __objects to the JSON file (path: __file_path)
        """
        with open(__file_path, "w") as write_stream:
            json.dump(__objects, write_stream)

    def reload(self):
        """
            Reloads the stored objects from the JSON file
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) if "__class__" in v else v for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
    def attributes(self):
        """
        Returns the valid attributes and their types for each classname.

        This method provides information about the expected attributes and their data types
        for various classes used in the application.
        """
        attributes = {
            "BaseModel": {"id": str, "created_at": datetime.datetime, "updated_at": datetime.datetime},
            "User": {"email": str, "password": str, "first_name": str, "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {"city_id": str, "user_id": str, "name": str, "description": str,
                      "number_rooms": int, "number_bathrooms": int, "max_guest": int,
                      "price_by_night": int, "latitude": float, "longitude": float, "amenity_ids": list},
            "Review": {"place_id": str, "user_id": str, "text": str}
        }
        return attributes

