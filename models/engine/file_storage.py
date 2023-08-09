#!/usr/bin/python3
import json
from models.base_model import BaseModel
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        name = obj.__class__.__name__ + "." + obj.id
        self.__objects.update([(name, obj)])

    def save(self):
        with open(self.__file_path, mode="w") as f:
             json.dump({key: value.to_dict() for key, value in self.__objects.items()
                       }, f)

    def reload(self):
        self.__objects = {}
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
