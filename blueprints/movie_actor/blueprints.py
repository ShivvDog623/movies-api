"""
Movie_Actor Blueprint. Serves movie_actor table related endpoints.
"""
from typing import Optional
from flask import Blueprint, request
from pydantic import BaseModel
from flask_pydantic import validate

from .service import(
    get_all_movieactors, 
    get_id
)

movie_actor_blueprint = Blueprint('movie_actor', __name__, url_prefix='/movie_actor')

class Movie_ActorItem(BaseModel):
    """movie_actor item data model"""
    actor_id : int
    movie_id : int


class Movie_ActorDataModel(BaseModel):
    """movie_actor data model"""
    actor_id : int
    movie_id : int

class Movie_Actor_FullDataModel(BaseModel):
    actor_id : int
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


class Movie_ActorResponseModel(BaseModel):
    """movie_actor response data model"""
    status: int | str
    data: list[Movie_ActorDataModel | MessageModel]

class Movie_Actor_FullResponsemodel(BaseModel):
    status: int | str
    data: list[Movie_Actor_FullDataModel| MessageModel]

class FieldValueModel(BaseModel):
    """movie_actor field and value model"""
    field: str
    value: str | int | float | bool

class PatchModel(BaseModel):
    """movie_actor search and patch model"""
    fields: list[FieldValueModel]

class ValueModel(BaseModel):
    """movie_actor values model"""
    value: str | int | float | bool

class InModel(BaseModel):
    """movie_actor search model"""
    field: str
    values: list[ValueModel]

class PostModel(BaseModel):
    """new movie_actor model"""
    status: int | str


@movie_actor_blueprint.route('/all', methods=['GET'])
@validate()
def get_all():
    """
    GET: returns movie_actor table data
    """
    result = get_all_movieactors()
    return Movie_ActorResponseModel(status=result["status"], data=result["data"])



@movie_actor_blueprint.route('/<int:id>', methods=['GET'])
@validate()
def get_by_id(id):
    """
    GET: returns movie_actor table data by actor_id
    """
    result = get_id(id)
    return Movie_Actor_FullResponsemodel(status=result["status"], data=result["data"])
