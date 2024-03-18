"""
Actors Blueprint. Serves actor table related endpoints.
"""
from typing import Optional
from pydantic import BaseModel
from flask import Blueprint, jsonify
from flask_pydantic import validate


from .service import (
    get_all_actors, 
    get_by_id, 
    create_new_actor, 
    update_by_id, 
    delete_by_id
)

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

class MessageModel(BaseModel):
    """generic message model"""
    message: str

class ActorResponseModel(BaseModel):
    """actor response data model"""
    status: int | str
    data: list[ActorDataModel | MessageModel]

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



@actor_blueprint.route('/create', methods= ['POST'])
def create():
    """
    POST: creates actor in actor table
    """
    result = create_new_actor()
    return jsonify(result)


@actor_blueprint.route('/<int:id>', methods=['GET'])
def get_id(id):
    result = get_by_id(id)
    return jsonify(result)

@actor_blueprint.route('/<int:id>', methods=['PUT'])
def update_id(id):
    """
    PUT: updates actor by id
    """
    result = update_by_id(id)
    return jsonify(result)

@actor_blueprint.route('/<int:id>', methods= ['DELETE'])
def delete_id(id):
    """
    DELETE: Deletes actor by id (be careful).
    """
    result = delete_by_id(id)
    return jsonify(result)
