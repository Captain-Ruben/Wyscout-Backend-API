import os
import pandas as pd

from Models.Player import Player
from Models.Parameter import Parameter
from pymongo.collection import Collection
from Connection.config import parameters_collection, players_collection

def start_up():
    data = pd.read_excel(find_excel_file("input_wyscout.xlsx"))
    data.fillna(0)

    if is_not_seeded(parameters_collection):
        seed_parameter_database(data)
    
    if is_not_seeded(players_collection):
        seed_player_database(data)


def seed_parameter_database(data:pd.DataFrame):
    parameters = data.columns

    for parameter in parameters:
        if parameter != "Player":
            new_parameter = Parameter(parameter)
            new_parameter.save_to_database(parameters_collection)
    
    print("Parameter data succesfully seeded!")


def seed_player_database(data: pd.DataFrame):
    parameters = {param['name']: param['_id'] for param in parameters_collection.find()}

    for _, player in data.iterrows():
        new_player = Player(player["Player"])
        player_values = []

        for column, value in player.items():
            if column == "Player":
                continue

            if column in parameters:
                player_values.append({"parameter_id": parameters[column], "value": value})
            else:
                print(f"Column: {column} not found in parameters")

        new_player.set_parameter_values(player_values)
        new_player.save_to_database(players_collection)

    print("Player data succesfully seeded!")


#region Helpers
def find_excel_file(name:str):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    excel_file_name = name
    
    for root, dirs, files in os.walk(root_dir):
        if excel_file_name in files:
            return os.path.join(root, excel_file_name)

    print(f"Excel file '{excel_file_name}' not found.")
    return None


def is_not_seeded(collection:Collection):
    return collection.count_documents({}) <= 1
#endregion