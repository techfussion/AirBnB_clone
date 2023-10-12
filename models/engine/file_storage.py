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
            Deserializes the JSON file to __objects
        """
        if (os.path.isfile(__file_path)):
            with open(__file_path, "r") as read_stream:
                __objects = json.load(read_stream)
