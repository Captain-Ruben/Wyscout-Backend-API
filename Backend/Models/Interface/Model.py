import pandas as pd

from bson import ObjectId
from abc import ABC


class ModelInterface(ABC):
    def __init__(self, name:str, _id=None,):
        try:
            if _id is None:
                self._id = ObjectId()
            else:
                self._id = _id
            self.name = name

        except Exception as e:
            raise ValueError(f"Error initializing Parameter: {e}")

    def get_id(self):
        return self._id

    def get_name(self):
        return self.name
    
