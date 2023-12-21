from Models.Interface.Model import ModelInterface
from abc import ABC


class Parameter(ModelInterface, ABC):
    def __init__(self, name: str, _id=None):
        super().__init__(name, _id)

    def save_to_database(self, parameters_collection):
        try:
            parameter_data = {
                "_id": self.get_id(),
                "name": self.get_name()
            }

            parameters_collection.insert_one(parameter_data)

        except Exception as e:
            raise ValueError(f"Error saving Parameter to database: {e}")
