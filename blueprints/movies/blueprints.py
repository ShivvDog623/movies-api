"""
Movie Blueprint. Serves all movies table related endpoints. 
"""
from flask import Blueprint, request, jsonify
from pydantic import BaseModel
from flask_pydantic import validate

from .service import (
    get_all,
    get_id, 
    create_movie, 
    update_by_id, 
    delete_by_id, 
    exact_search, 
    like_search, 
    in_search, 
    movie_directors_by_id, 
    movie_actors_by_id
)

movie_blueprint = Blueprint('movie', __name__, url_prefix='/movies')

class MovieItem(BaseModel):
    """movie item data model"""
    title: str 
    year: int
    description: str
    time: int
    rating: float
    vote: int
    revenue: float
    metascore: int

class MovieDataModel(BaseModel):
    """movie data model"""
    movie_id: int
    title: str 
    year: int
    description: str
    time: int
    rating: float
    vote: int
    revenue: float
    metascore: int

class MessageModel(BaseModel):
    """generic message model"""
    message: str


class ResponseModel(BaseModel):
    """movie response data model"""
    status: int | str
    data: list[MovieDataModel | MessageModel]

class FieldValueModel(BaseModel):
    """movie field and value model"""
    field: str
    value: str | int | float | bool

class PatchModel(BaseModel):
    """movie search and patch model"""
    fields: list[FieldValueModel]

class ValueModel(BaseModel):
    """movie values model"""
    value: str | int | float | bool

class InModel(BaseModel):
    """movie search model"""
    field: str
    values: list[ValueModel]

class PostModel(BaseModel):
    """new movie model"""
    status: str | int


@movie_blueprint.route('/all', methods=['GET'])
@validate()
def get():
    """
    GET: returns movies table data
    """
    result = get_all()
    print(result)
    return ResponseModel(status=result["status"], data=result["data"])

@movie_blueprint.route('/<int:id>', methods=['GET'])
@validate()
def get_by_id(id):
    """
    GET: returns movie by id
    """
    result = get_id(id)
    # return result
    return ResponseModel(status=result["status"], data=result["data"])


@movie_blueprint.route('/directors/<int:id>', methods=['GET'])
def movie_directors(id):
    """
    GET: returns director and movie data by movie_id
    """
    result = movie_directors_by_id(id)
    return result

@movie_blueprint.route('/actors/<int:id>', methods=['GET'])
def movie_actors(id):
    """
    GET: returns actor and movie data by movie_id
    """
    result = movie_actors_by_id(id)
    return result

@movie_blueprint.route('/filter/exact', methods=['POST'])
def filter_exact():
    """
    POST: return movie data by exact title (lower or upper)
    """
    data = request.get_json()
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

