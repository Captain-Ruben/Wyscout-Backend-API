from bson import ObjectId
from Connection.config import parameters_collection

def find_all_parameters():
    parameters_cursor = parameters_collection.find()
    parameters_list = []

    for parameter in parameters_cursor:
        parameter['_id'] = str(parameter['_id'])
        parameters_list.append(parameter)

    return parameters_list


def find_parameter_by_id(param_id):
    parameter = parameters_collection.find_one({'_id': ObjectId(param_id)})

    if parameter:
        parameter['_id'] = str(parameter['_id'])
        return parameter
    else:
        return None