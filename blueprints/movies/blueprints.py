"""
Movie Blueprint. Serves all movies table related endpoints. 
"""
from typing import Optional
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
    movie_actors_by_id,
    movie_genres_by_id
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

class MovieActorDataModel(BaseModel):
    """movie and actor data model"""
    movie_id: int
    actor_id: Optional[int] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    title: str 
    year: int
    description: str
    time: int
    rating: float
    vote: int
    revenue: float
    metascore: int


class MovieDirectorDataModel(BaseModel):
    """movie and director data model"""
    movie_id: int
    director_id: Optional[int] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    title: str 
    year: int
    description: str
    time: int
    rating: float
    vote: int
    revenue: float
    metascore: int

class MovieGenreDataModel(BaseModel):
    """movie and genre data model"""
    movie_id: int
    genre_id: Optional[int] = None
    genre: Optional[str] = None
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


class MovieResponseModel(BaseModel):
    """movie response data model"""
    status: int | str
    data: list[MovieDataModel | MessageModel]

class MovieDirectorResponseModel(BaseModel):
    """movie and director response data model"""
    status: int | str
    data: list[MovieDirectorDataModel | MessageModel]

class MovieActorResponseModel(BaseModel):
    """movie and director response data model"""
    status: int | str
    data: list[MovieActorDataModel | MessageModel]

class MovieGenreResponseModel(BaseModel):
    """movie and genre response data model"""
    status: int | str
    data: list[MovieGenreDataModel| MessageModel]


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
    status: int | str


@movie_blueprint.route('/all', methods=['GET'])
@validate()
def get():
    """
    GET: returns movies table data
    """
    result = get_all()
    return MovieResponseModel(status=result["status"], data=result["data"])

@movie_blueprint.route('/<int:id>', methods=['GET'])
@validate()
def get_by_id(id):
    """
    GET: returns movie by id
    """
    result = get_id(id)
    return MovieResponseModel(status=result["status"], data=result["data"])


@movie_blueprint.route('/directors/<int:id>', methods=['GET'])
@validate()
def movie_directors(id):
    """
    GET: returns director and movie data by movie_id
    """
    result = movie_directors_by_id(id)
    return MovieDirectorResponseModel(status=result["status"], data=result["data"])

@movie_blueprint.route('/actors/<int:id>', methods=['GET'])
@validate()
def movie_actors(id):
    """
    GET: returns actor and movie data by movie_id
    """
    result = movie_actors_by_id(id)
    return MovieActorResponseModel(status=result["status"], data=result["data"])


@movie_blueprint.route('/genres/<int:id>', methods=['GET'])
@validate()
def movie_genres(id):
    """
    GET: returns genres and movie data by movie_id
    """
    result = movie_genres_by_id(id)
    return MovieGenreResponseModel(status=result["status"], data=result["data"])

@movie_blueprint.route('/filter/exact', methods=['POST'])
@validate(body=PatchModel)
def filter_exact():
    """
    POST: return movie data by exact title (lower or upper)
    """
    data = request.get_json()
    result = exact_search(data)
    return MovieResponseModel(status=result["status"], data=result["data"])


@movie_blueprint.route('/filter/like', methods=['POST'])
@validate(body=PatchModel)
def filter_like():
    """
    POST: returns all data that has similar characters in json
    """
    data = request.get_json()
    result = like_search(data)
    return MovieResponseModel(status=result["status"], data=result["data"])

@movie_blueprint.route('/filter/in', methods=['POST'])
@validate(body=InModel)
def filter_in():
    """
    POST: return all movies passed through json list
    """
    data = request.get_json()
    print("******** ", data)
    result = in_search(data)
    return MovieResponseModel(status=result["status"], data=result["data"])

@movie_blueprint.route('/create', methods= ['POST'])
@validate(body=MovieItem)
def create():
    """
    POST: creates movie in movie table
    """
    data = request.get_json()
    result = create_movie(data)
    if (result["status"] == 200):
        status = 201
    else:
        status = result["status"]

    return PostModel(status=status)



@movie_blueprint.route('/<int:id>', methods=['PUT'])
@validate(body=MovieItem)
def update(id):
    """
    PUT: updates movie title by id
    """
    data = request.get_json()
    result = update_by_id(id, data)
    
    if (result["status"] == 204):
        return MessageModel(status=result["status"], message=result["message"])
    print (result)
    return MovieResponseModel(status=result["status"], data=result["data"])




@movie_blueprint.route('/<int:id>', methods= ['DELETE'])
@validate()
def delete(id):
    """
    DELETE: Deletes movie by id (be careful).
    """
    result = delete_by_id(id)
    return MovieResponseModel(status=result["status"], data=result["data"])

