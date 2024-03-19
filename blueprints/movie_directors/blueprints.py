"""
Movie_Director Blueprint. Serves movie_actor table related endpoints.
"""
from typing import Optional
from flask import Blueprint, request, jsonify
from pydantic import BaseModel
from flask_pydantic import validate

from .service import(
    get_all_movie_directors, 
    get_id
)

movie_director_blueprint = Blueprint('movie_director', __name__, url_prefix='/movie_director')

class Movie_DirectorItem(BaseModel):
    """movie_director item data model"""
    director_id: int
    movie_id : int


class Movie_DirectorDataModel(BaseModel):
    """movie_director data model"""
    director_id : int
    movie_id : int

class Movie_Director_FullDataModel(BaseModel):
    """movie_director_full data model"""
    director_id : int
    movie_id : int
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
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

class Movie_DirectorResponseModel(BaseModel):
    """movie_director response data model"""
    status: int | str
    data: list[Movie_DirectorDataModel | MessageModel]

class Movie_Director_FullResponseModel(BaseModel):
    """movie_director_full response data model"""
    status: int | str
    data: list[Movie_Director_FullDataModel | MessageModel]

class FieldValueModel(BaseModel):
    """movie_director field and value model"""
    field: str
    value: str | int | float | bool

class PatchModel(BaseModel):
    """movie_director search and patch model"""
    fields: list[FieldValueModel]

class ValueModel(BaseModel):
    """movie_director values model"""
    value: str | int | float | bool

class InModel(BaseModel):
    """movie_director search model"""
    field: str
    values: list[ValueModel]

class PostModel(BaseModel):
    """new movie_director model"""
    status: int | str

@movie_director_blueprint.route('/all', methods=['GET'])
@validate()
def get_all():
    """
    GET: returns movie_director table data
    """
    result = get_all_movie_directors()
    return Movie_DirectorResponseModel(status=result["status"], data=result["data"])


@movie_director_blueprint.route('/<int:id>', methods=['GET'])
@validate()
def get_by_id(id):
    """
    GET: returns movie_director table data by director_id
    """
    result = get_id(id)
    return Movie_Director_FullResponseModel(status=result["status"], data=result["data"])
