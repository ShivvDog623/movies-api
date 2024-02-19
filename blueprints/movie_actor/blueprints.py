"""
Movie_Actor Blueprint. Serves movie_actor table related endpoints.
"""

from flask import Blueprint, jsonify, request
from app import db
from doQuery import doQuery
from .service import get_all_movieactors, get_by_id

movie_actor_blueprint = Blueprint('movie_actor', __name__, url_prefix='/movie_actor')


@movie_actor_blueprint.route('/all', methods=['GET'])
def get_all():
    """
    GET: returns movie_actor table data
    """
    result = get_all_movieactors()
    return jsonify(result)


@movie_actor_blueprint.route('/<int:id>', methods=['GET'])
def get_id(id):
    """
    GET: returns movie_actor table data by actor_id
    """
    result = get_by_id(id)
    return jsonify (result)
