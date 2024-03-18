"""
Director Blueprint. Serves all director table related endpoints
"""
from typing import Optional
from flask import Blueprint, request
from pydantic import BaseModel
from flask_pydantic import validate



from .service import (
    get_all, 
    get_id, 
    create_director,
    update_by_id,
    delete_by_id, 
    get_movie_directors_by_id
)

class DirectorItem(BaseModel):
    """director item data model"""
    first_name: str
    middle_name: Optional[str] = None
    last_name: str

class DirectorDataModel(BaseModel):
    """director data model"""
    director_id: int
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None

class DirectorMovieDataModel(BaseModel):
    """director and movie data model"""
    director_id: int
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

class DirectorResponseModel(BaseModel):
    """director response data model"""
    status: int | str
    data: list[DirectorDataModel | MessageModel]

class DirectorMovieResponseModel(BaseModel):
    """director and movie response date model"""
    status: int | str
    data: list[DirectorMovieDataModel | MessageModel]  

class FieldValueModel(BaseModel):
    """director field and value model"""
    field: str
    value: str | int | float | bool

class PatchModel(BaseModel):
    """director search and patch model"""
    fields: list[FieldValueModel]

class ValueModel(BaseModel):
    """director values model"""
    value: str | int | float | bool

class PostModel(BaseModel):
    """new director model"""
    status: int | str


directors_blueprint = Blueprint('director', __name__, url_prefix='/directors')

@directors_blueprint.route('/all', methods=['GET'])
@validate()
def get():
    """
    GET: returns directors table data
    """
    result = get_all()
    return DirectorResponseModel(status=result["status"], data=result["data"])

@directors_blueprint.route('/<int:id>', methods=['GET'])
@validate()
def get_by_id(id):
    """
    GET: returns director by id
    """
    result = get_id(id)
    return DirectorResponseModel(status=result["status"], data=result["data"])

@directors_blueprint.route('/create', methods= ['POST'])
@validate(body=DirectorItem)
def create():
    """
    POST: creates director in director table
    """
    data = request.get_json()
    result = create_director(data)
    if (result["status"] == 200):
        status = 201
    else:
        status = result["status"]
    return PostModel(status=status)


@directors_blueprint.route('/movies/<int:id>', methods=['GET'])
def movie_director(id):
    """
    GET: returns all movie data by director_id 
    """
    result = get_movie_directors_by_id(id)
    return result

@directors_blueprint.route('/<int:id>', methods=['PUT'])
@validate(body=DirectorItem)
def update(id):
    """
    PUT: updates director title by id
    """
    data = request.get_json()
    result = update_by_id(id, data)
    if (result["status"] == 204):
        return MessageModel(status=result["status"], message=result["message"])
    return DirectorResponseModel(status=result["status"], data=result["data"])


@directors_blueprint.route('/<int:id>', methods= ['DELETE'])
@validate()
def delete(id):
    """
    DELETE: Deletes director by id (be careful).
    """
    result = delete_by_id(id)
    return DirectorResponseModel(status=result["status"], data=result["data"])
