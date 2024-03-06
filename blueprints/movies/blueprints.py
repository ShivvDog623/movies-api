"""
Movie Blueprint. Serves all movies table related endpoints. 
"""
from flask import Blueprint, request
from app import db
from doQuery import doQuery 
from .service import get_all, get_id, create_movie, update_by_id, delete_by_id, exact_search, like_search, in_search

movie_blueprint = Blueprint('movie', __name__, url_prefix='/movies')

@movie_blueprint.route('/all', methods=['GET'])
def get():
    """
    GET: returns movies table data
    """
    result = get_all()
    return result

@movie_blueprint.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    GET: returns movie by id
    """
    result = get_id(id)
    return result

@movie_blueprint.route('/filter/exact', methods=['POST'])
def filter_exact():
    """
    POST: return movie data by exact title (lower or upper)
    """
    data = request.get_json()
    print(data)
    result = exact_search(data)
    return result


@movie_blueprint.route('/filter/like', methods=['POST'])
def filterlike():
    """
    POST: returns all data that has similar characters in json
    """
    data = request.get_json()
    result = like_search(data)
    return result

@movie_blueprint.route('/filter/in', methods=['POST'])
def filter_in():
    """
    POST: return all movies passed through json list
    """
    data = request.get_json()
    result = in_search(data)
    return result

@movie_blueprint.route('/create', methods= ['POST'])
def create():
    """
    POST: creates movie in movie table
    """
    data = request.get_json()
    result = create_movie(data)
    return result


@movie_blueprint.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    PUT: updates movie title by id
    """
    result = update_by_id(id)
    return result

@movie_blueprint.route('/<int:id>', methods= ['DELETE'])
def delete(id):
    """
    DELETE: Deletes movie by id (be careful).
    """
    result = delete_by_id(id)
    return result

