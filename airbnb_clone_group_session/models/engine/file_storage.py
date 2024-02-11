#!/usr/bin/python3

import json

from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    __our_classes = {
        "BaseModel": BaseModel,
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        instance_id = obj.id

        key = f"{class_name}.{instance_id}"

        self.__objects[key] = obj

    def save(self):
        temp_dict = {}

        for key, value in self.__objects.items():
            temp_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(temp_dict, file, indent=4)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                my_objects = json.load(file)

            for key, value in my_objects.items():
                class_name = value["__class__"]

                self.__objects[key] = self.__our_classes[class_name](**value)
        except FileNotFoundError:
            pass
