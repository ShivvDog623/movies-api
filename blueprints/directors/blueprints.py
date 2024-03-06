"""
Director Blueprint. Serves all director table related endpoints
"""
from flask import Blueprint, request
from .service import get_all, get_id, create_director, update_by_id, delete_by_id

directors_blueprint = Blueprint('director', __name__, url_prefix='/directors')

@directors_blueprint.route('/all', methods=['GET'])
def get():
    """
    GET: returns directors table data
    """
    result = get_all()
    return result

@directors_blueprint.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    GET: returns director by id
    """
    result = get_id(id)
    return result

@directors_blueprint.route('/create', methods= ['POST'])
def create():
    """
    POST: creates director in director table
    """
    data = request.get_json()
    result = create_director(data)
    return result


@directors_blueprint.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    PUT: updates director title by id
    """
    result = update_by_id(id)
    return result

@directors_blueprint.route('/<int:id>', methods= ['DELETE'])
def delete(id):
    """
    DELETE: Deletes director by id (be careful).
    """
    result = delete_by_id(id)
    return result