from flask import Blueprint, jsonify, abort
from Services.parameter import find_all_parameters, find_parameter_by_id

parameter_blueprint = Blueprint('parameter', __name__)

@parameter_blueprint.route('/parameters', methods=['GET'])
def get_all_parameters():
    #region swagger
    """
    Get all parameters.

    This endpoint returns a list of all parameters.

    ---
    responses:
      200:
        description: A JSON array of parameters.
        schema:
          type: array
          items:
            type: object
            properties:
              _id:
                type: string
              name:
                type: string
    """
    #endregion
    
    result = find_all_parameters()
    return jsonify(result)


@parameter_blueprint.route('/parameters/<string:param_id>', methods=['GET'])
def get_parameter_by_id(param_id):
    #region swagger
    """
    Get a parameter by its ID.

    This endpoint returns a single parameter based on its ID.

    ---
    parameters:
      - name: param_id
        in: path
        type: string
        required: true
        description: The ID of the parameter to retrieve.
    responses:
      200:
        description: A JSON object representing the parameter.
        schema:
          type: object
          properties:
            _id:
              type: string
            name:
              type: string
      404:
        description: Parameter not found.
        schema:
          type: object
          properties:
            error:
              type: string
    """
    #endregion 
    
    parameter = find_parameter_by_id(param_id)

    if parameter:
        return jsonify(parameter)
    else:
        abort(404, description="Parameter not found.")
