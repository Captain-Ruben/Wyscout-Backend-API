import pymongo

from Models.Interface.Model import ModelInterface
from abc import ABC


class Player(ModelInterface, ABC):
    def __init__(self, name: str, _id=None):
        super().__init__(name, _id)
        self.parameter_values = []


    def set_parameter_values(self, player_values:list):
        self.parameter_values = player_values


    def save_to_database(self, players_collection):
        try:
            player_data = {
                "_id": self.get_id(),
                "Player": self.get_name()
            }

            for parameter in self.parameter_values:
                player_data[str(parameter["parameter_id"])] = parameter["value"]

            players_collection.insert_one(player_data)
        
        except Exception as e:
            raise ValueError(f"Error saving Parameter to database: {e}")