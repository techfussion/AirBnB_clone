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
        dict_rep = obj.to_dict()
        self.__objects[f"{dict_rep['__class__']}.{dict_rep['id']}"] = obj

    def save(self):
        """
            Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self._FileStorage__file_path, "w") as write_stream:
            json.dump(self._FileStorage__objects, write_stream)

    def reload(self):
        """
            Deserializes the JSON file to __objects
        """
        if (os.path.isfile(self._FileStorage__file_path)):
            with open(self._FileStorage__file_path, "r") as read_stream:
                self.__objects = json.load(read_stream)
