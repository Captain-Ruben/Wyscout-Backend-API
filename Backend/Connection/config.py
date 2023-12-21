import pymongo

client = pymongo.MongoClient("database", 27017)

db_parameters = client.parameters_database
parameters_collection = db_parameters.parameters

db_players = client.players_database
players_collection = db_players.players

