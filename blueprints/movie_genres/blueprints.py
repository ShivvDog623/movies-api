"""
Movie_Genre Blueprint. Serves movie_actor table related endpoints.
"""

from flask import Blueprint, jsonify, request
from app import db
from doQuery import doQuery
from .service import get_all_movie_genres, get_id

movie_genre_blueprint = Blueprint('movie_genre', __name__, url_prefix='/movie_genre')


@movie_genre_blueprint.route('/all', methods=['GET'])
def get_all():
    """
    GET: returns movie_genre table data
    """
    result = get_all_movie_genres()
    return result


@movie_genre_blueprint.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    GET: returns movie_genre table data by genre_id
    """
    result = get_id(id)
    return result