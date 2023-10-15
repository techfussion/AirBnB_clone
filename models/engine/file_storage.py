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
        """Reload stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict

    def attributes(self):
        """This returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
