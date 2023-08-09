#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""importing everything for `FileStorage` class"""


class FileStorage:
    """
    The `FileStorage` class provides methods for storing
    and retrieving objects in a JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        The method returns all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        The method "new" takes an object and adds it to a
        dictionary with a key that consists of the
        object's class name and id.
        """
        name = obj.__class__.__name__ + "." + obj.id
        self.__objects.update([(name, obj)])
        return self.__objects

    def save(self):
        """
        The above method saves the objects in a dictionary
        to a JSON file.
        """
        with open(self.__file_path, mode="w") as f:
            json.dump({key: value.to_dict() for key,
                       value in self.__objects.items()
                       }, f, indent=4)

    def reload(self):
        """
        The `reload` method reads data from a file,
        converts it into objects, and stores them in a
        dictionary.
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                if f.read() != "":
                    f.seek(0)
                    my_dict = json.load(f)
                    for value in my_dict.values():
                        if value["__class__"]:
                            my_class = value["__class__"]
                            self.new(eval(my_class)(**value))
        except FileNotFoundError:
            pass
        return self.__objects