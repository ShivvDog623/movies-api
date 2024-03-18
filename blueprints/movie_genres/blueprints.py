"""
Movie_Genre Blueprint. Serves movie_actor table related endpoints.
"""

from typing import Optional
from flask import Blueprint, request, jsonify
from pydantic import BaseModel
from flask_pydantic import validate

from .service import(
    get_all_movie_genres, 
    get_id
)

movie_genre_blueprint = Blueprint('movie_genre', __name__, url_prefix='/movie_genre')

class Movie_GenreItem(BaseModel):
    """movie_genre item data model"""
    genre_id: int
    movie_id : int

class Movie_GenreDataModel(BaseModel):
    """movie_genre data model"""
    genre_id : int
    movie_id : int

class MessageModel(BaseModel):
    """generic message model"""
    message: str


class Movie_GenreResponseModel(BaseModel):
    """movie_genre response data model"""
    status: int | str
    data: list[Movie_GenreDataModel | MessageModel]


class FieldValueModel(BaseModel):
    """movie_genre field and value model"""
    field: str
    value: str | int | float | bool

class PatchModel(BaseModel):
    """movie_genre search and patch model"""
    fields: list[FieldValueModel]

class ValueModel(BaseModel):
    """movie_genre values model"""
    value: str | int | float | bool

class PostModel(BaseModel):
    """new movie_genre model"""
    status: int | str

@movie_genre_blueprint.route('/all', methods=['GET'])
@validate()
def get_all():
    """
    GET: returns movie_genre table data
    """
    result = get_all_movie_genres()
    return Movie_GenreResponseModel(status=result["status"], data=result["data"])


@movie_genre_blueprint.route('/<int:id>', methods=['GET'])
@validate()
def get_by_id(id):
    """
    GET: returns movie_genre table data by genre_id
    """
    result = get_id(id)
    return Movie_GenreResponseModel(status=result["status"], data=result["data"])
