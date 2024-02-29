"""
Actors Blueprint. Serves actor table related endpoints.
"""

from flask import Blueprint, jsonify, request
from app import db
from doQuery import doQuery
from .service import get_all_actors, get_by_id, create_new_actor, update_by_id, delete_by_id

actor_blueprint = Blueprint('actor', __name__, url_prefix='/actor')

@actor_blueprint.route('/all', methods=['GET'])
def get_all():
    """
    GET: returns actors table data
    """
    result = get_all_actors()
    actor_list = []
    for record in result:
        actor_list.append(record)
    return jsonify (actor_list)


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
