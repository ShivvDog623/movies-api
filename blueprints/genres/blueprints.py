"""
Genre Blueprint. Serves all genre table related endpoints
"""
from typing import Optional
from flask import Blueprint, request
from pydantic import BaseModel
from flask_pydantic import validate

from .service import(
    get_all, 
    get_id, 
    create_genre,
    update_by_id, 
    delete_by_id)

genre_blueprint = Blueprint('genre', __name__, url_prefix='/genre')

class GenreItem(BaseModel):
    """genre item data model"""
    genre: str

class GenreDataModel(BaseModel):
    """genre data model"""
    genre_id: int
    genre: str


class MessageModel(BaseModel):
    """generic message model"""
    message: str

class GenreResponseModel(BaseModel):
    """genre response data model"""
    status: int | str
    data: list[GenreDataModel | MessageModel]

class FieldValueModel(BaseModel):
    """genre field and value model"""
    field: str
    value: str | int | float | bool

class PatchModel(BaseModel):
    """genre search and patch model"""
    fields: list[FieldValueModel]

class ValueModel(BaseModel):
    """genre values model"""
    value: str | int | float | bool

class PostModel(BaseModel):
    """new genre model"""
    status: int | str



@genre_blueprint.route('/all', methods=['GET'])
@validate()
def get():
    """
    GET: returns all genres table data
    """
    result = get_all()
    return GenreResponseModel(status=result["status"], data=result["data"])

@genre_blueprint.route('/<int:id>', methods=['GET'])
@validate()
def get_by_id(id):
    """
    GET: returns genre by id
    """
    result = get_id(id)
    return GenreResponseModel(status=result["status"], data=result["data"])

@genre_blueprint.route('/create', methods= ['POST'])
@validate(body=GenreItem)
def create():
    """
    POST: creates genre in genre table
    """
    data = request.get_json()
    result = create_genre(data)
    if (result["status"] == 200):
        status = 201
    else:
        status = result["status"]
    return PostModel(status=status)

@genre_blueprint.route('/<int:id>', methods=['PUT'])
@validate(body=GenreItem)
def update(id):
    """
    PUT: updates genre by id
    """
    data = request.get_json()
    result = update_by_id(id, data)
    if (result["status"] == 204):
        return MessageModel(status=result["status"], message=result["message"])
    return GenreResponseModel(status=result["status"], data=result["data"])

@genre_blueprint.route('/<int:id>', methods= ['DELETE'])
@validate()
def delete(id):
    """
    DELETE: Deletes genre by id (be careful).
    """
    result = delete_by_id(id)
    return GenreResponseModel(status=result["status"], data=result["data"])
