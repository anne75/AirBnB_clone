#!/usr/bin/python3
import json
import datetime
# from models.base_model import BaseModel
"""
This is module file_storage.
It defines one class
"""


class FileStorage:
    """
    Serialize and deserialize objects in models to json
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key obj.id"""
        # self.__objects.update({str(obj.id): obj.to_json()})
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj
        # print(self.__objects)

    def save(self):
        """serializes __objects to file __file_path in json format"""
        printable = {}
        for k, v in self.__objects.items():
            printable[k] = v.to_json()
        with open(self.__file_path, mode='w', encoding='utf-8') as fhandle:
            json.dump(printable, fhandle)

    def reload(self):
        """deserializes the json file __file_path to __objects"""
        from models.base_model import BaseModel

        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as fhandle:
                printable = json.load(fhandle)
            for i, j in printable.items():
                self.__objects[i] = BaseModel(**j)
        except FileNotFoundError:
            pass

    def mySerialize(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
