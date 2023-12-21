import math
from flask import Blueprint, jsonify, request
from Services.player import find_player_score, find_ranking_by_categories

players_blueprint = Blueprint('players', __name__)

@players_blueprint.route('/players/ranking', methods=['POST'])
def get_ranking():
    #region swagger
    """
    Get player rankings based on specified categories and slider values.

    This endpoint calculates and returns player rankings based on the provided input.

    ---
    parameters:
      - in: body
        name: request_data
        description: JSON object containing player ranking criteria.
        required: true
        schema:
          example:
            createdCategories:
              - categoryName: "category_1"
                sliderValues:
                  "parameter_id_1": 100
                  "parameter_id_2": 0
              - categoryName: "category_2"
                sliderValues:
                  "parameter_id_1": 100
              - categoryName: "category_3"
                sliderValues:
                  "parameter_id_1": 50
                  "parameter_id_2": 25
                  "parameter_id_3": 25
                  
    responses:
      200:
        description: Successful response with player rankings.
    """
    #endregion
    request_data = request.json
    
    result = find_ranking_by_categories(request_data)
    result = replace_nan_with_zero_and_sort(result)
    
    return jsonify(result)


@players_blueprint.route('/players/ranking/top-three', methods=['POST'])
def get_ranking_top_three():
    #region swagger
    """
    Get top three player ranking based on specified categories and slider values.

    This endpoint calculates and returns the top three player ranking based on the provided input.

    ---
    parameters:
      - in: body
        name: request_data
        description: JSON object containing player ranking criteria.
        required: true
        schema:
          example:
            createdCategories:
              - categoryName: "category_1"
                sliderValues:
                  "parameter_id_1": 100
                  "parameter_id_2": 0
              - categoryName: "category_2"
                sliderValues:
                  "parameter_id_1": 100
              - categoryName: "category_3"
                sliderValues:
                  "parameter_id_1": 50
                  "parameter_id_2": 25
                  "parameter_id_3": 25
                    
    responses:
      200:
        description: Successful response with top three player ranking.
    """
    #endregion
    
    request_data = request.json
    
    result = find_ranking_by_categories(request_data)
    result = replace_nan_with_zero_and_sort(result)[:3]  

    return jsonify(result)


@players_blueprint.route('/players/ranking/<string:player_id>', methods=['POST'])
def get_player_score(player_id):
    #region swagger
    """
    Get the score of a specific player based on the provided input.

    This endpoint calculates and returns the score of a specific player based on the provided input.

    ---
    parameters:
      - in: path
        name: player_id
        type: string
        required: true
        description: The ID of the player whose score is requested.

      - in: body
        name: request_data
        description: JSON object containing player ranking criteria.
        required: true
        schema:
          example:
            createdCategories:
              - categoryName: "category_1"
                sliderValues:
                  "parameter_id_1": 100
                  "parameter_id_2": 0
              - categoryName: "category_2"
                sliderValues:
                  "parameter_id_1": 100
              - categoryName: "category_3"
                sliderValues:
                  "parameter_id_1": 50
                  "parameter_id_2": 25
                  "parameter_id_3": 25

    responses:
      200:
        description: Successful response with the player's score.
    """
    #endregion
    
    request_data = request.json
     
    result = find_player_score(player_id, request_data)
    
    return jsonify(result)


#region helper
def replace_nan_with_zero_and_sort(data, sort_key='total_score', reverse=True):
    def replace_nan_with_zero(item):
        if isinstance(item, list):
            return [replace_nan_with_zero(sub_item) for sub_item in item]
        elif isinstance(item, dict):
            return {key: replace_nan_with_zero(value) for key, value in item.items()}
        elif isinstance(item, (float, int)) and math.isnan(item):
            return 0
        else:
            return item

    data_with_zero = replace_nan_with_zero(data)

    if isinstance(data_with_zero, list):
        data_with_zero.sort(key=lambda x: x.get(sort_key, 0), reverse=reverse)
    else:
        data_with_zero = [data_with_zero]

    return data_with_zero
#endregion