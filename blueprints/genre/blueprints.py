"""
Genre Blueprint. Serves all genre table related endpoints
"""
from flask import Blueprint, jsonify
from .service import get_all, get_by_id, create_genre, update_by_id, delete_by_id

genre_blueprint = Blueprint('genre', __name__, url_prefix='/genre')

@genre_blueprint.route('/all', methods=['GET'])
def get():
    """
    GET: returns all genres table data
    """
    result = get_all()
    return jsonify (result)

@genre_blueprint.route('/<int:id>', methods=['GET'])
def get_id(id):
    """
    GET: returns genre by id
    """
    result = get_by_id(id)
    return jsonify (result)

@genre_blueprint.route('/create', methods= ['POST'])
def create():
    """
    POST: creates genre in genre table
    """
    result = create_genre()
    return jsonify(result)


@genre_blueprint.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    PUT: updates genre by id
    """
    result = update_by_id(id)
    return jsonify(result)

@genre_blueprint.route('/<int:id>', methods= ['DELETE'])
def delete(id):
    """
    DELETE: Deletes genre by id (be careful).
    """
    result = delete_by_id(id)
    return jsonify(result)