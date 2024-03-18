"""
Actors Blueprint. Serves actor table related endpoints.
"""
from typing import Optional
from pydantic import BaseModel
from flask import Blueprint, jsonify, request
from flask_pydantic import validate


from .service import (
    get_all_actors, 
    get_id, 
    create_new_actor, 
    update_by_id, 
    delete_by_id,
    get_actor_movies_id
)

from flask import Blueprint, jsonify, request
from app import db
from doQuery import doQuery
from .service import get_all_actors, get_by_id, create_new_actor, update_by_id, delete_by_id, get_actor_movies_id 

actor_blueprint = Blueprint('actor', __name__, url_prefix='/actor')

class ActorItem(BaseModel):
    """actor item data model"""
    first_name: str
    middle_name: str
    last_name: str

class ActorDataModel(BaseModel):
    """actor data model"""
    actor_id: int
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None

class ActorMovieDataModel(BaseModel):
    actor_id: int
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
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

class ActorResponseModel(BaseModel):
    """actor response data model"""
    status: int | str
    data: list[ActorDataModel | MessageModel]

class ActorMovieResponseModel(BaseModel):
    """actor and movie response date model"""
    status: int | str
    data: list[ActorMovieDataModel | MessageModel]  

class FieldValueModel(BaseModel):
    """actor field and value model"""
    field: str
    value: str | int | float | bool

class PatchModel(BaseModel):
    """actor search and patch model"""
    fields: list[FieldValueModel]

class ValueModel(BaseModel):
    """actor values model"""
    value: str | int | float | bool

class PostModel(BaseModel):
    """new actor model"""
    status: int | str


@actor_blueprint.route('/all', methods=['GET'])
@validate()
def get_all():
    """
    GET: returns actors table data
    """
    result = get_all_actors()
    return ActorResponseModel(status=result["status"], data=result["data"])

@actor_blueprint.route('/<int:id>', methods=['GET'])
@validate()
def get_by_id(id):
    result = get_id(id)
    return ActorResponseModel(status=result["status"], data=result["data"])


@actor_blueprint.route('/create', methods= ['POST'])
@validate(body=ActorItem)
def create():
    """
    POST: creates actor in actor table
    """
    data = request.get_json()
    result = create_new_actor(data)
    if (result["status"] == 200):
        status = 201
    else:
        status = result["status"]
    return PostModel(status=status)

@actor_blueprint.route('/<int:id>', methods=['PUT'])
def update_id(id):
    """
    PUT: updates actor by id
    """
    result = update_by_id(id)
    return jsonify(result)

@actor_blueprint.route('/<int:id>', methods= ['DELETE'])
@validate()
def delete_id(id):
    """
    DELETE: Deletes actor by id (be careful).
    """
    result = delete_by_id(id)
    return ActorResponseModel(status=result["status"], data=result["data"])

@actor_blueprint.route('/movies/<int:id>', methods= ['GET'])
@validate()
def actor_movie(id):
    """
    GET: returns actor and movie data by actor_id
    """
    result = get_actor_movies_id(id)
    return ActorMovieResponseModel(status=result["status"], data=result["data"])
