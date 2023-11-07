#!/usr/bin/env python3

import json

class FileStorage:
    def __init__(self):
        __file_path = "magic.json",
        __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj[id])
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as fp:
            json.dump(FileStorage.__objects, fp)
    
    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as fp:
                dict_obj = json.load(fp)
