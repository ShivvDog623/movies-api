"""
Movie_Director Blueprint. Serves movie_actor table related endpoints.
"""

from flask import Blueprint, request
from app import db
from doQuery import doQuery
from .service import get_all_movie_directors, get_id

movie_director_blueprint = Blueprint('movie_director', __name__, url_prefix='/movie_director')


@movie_director_blueprint.route('/all', methods=['GET'])
def get_all():
    """
    GET: returns movie_director table data
    """
    result = get_all_movie_directors()
    return result


@movie_director_blueprint.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    GET: returns movie_director table data by director_id
    """
    result = get_id(id)
    return result