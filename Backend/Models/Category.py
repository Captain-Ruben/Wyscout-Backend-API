from abc import ABC
from Log.Logger import Logger
from Models.Interface.Model import ModelInterface
from Connection.config import players_collection

logger = Logger()

class Category(ModelInterface, ABC):
    def __init__(self, name, values, _id=None):
        super().__init__(name, _id)
        self.values = values


    def player_ranking_for_category(self):
        players_score = []

        for player in players_collection.find():
            player_id = player["_id"]
            player_name = player["Player"]
            player_cat_score = []

            total_category_score = 0 

            for _id, value in self.values.items():
                param_id = _id
                param_value = value

                if str(param_id) in player:
                    param_score = player[str(param_id)] * param_value
                    param_result = {
                        "_id": param_id,
                        "param_score": param_score
                    }

                    player_cat_score.append(param_result)
                    total_category_score += param_score
                else:
                    logger.log(f"Parameter {param_id} not found for player {player_id}")

            player_result = {
                "_id": str(player_id),
                "name": player_name,
                "category_id": str(self._id),
                "category_name": self.name,
                "category_score": player_cat_score,
                "total_category_score": total_category_score,
            }
            players_score.append(player_result)

        return players_score

    @staticmethod
    def normalize(value, min_value, max_value):
        return (value - min_value) / (max_value - min_value)
    
    @staticmethod
    def normalize_list(values):
        if not values:
            return values

        min_value = min(values)
        max_value = max(values)

        if max_value - min_value == 0:
            normalized_values = [0.0] * len(values)
        else:
            normalized_values = [(v - min_value) / (max_value - min_value) for v in values]
            
        return normalized_values