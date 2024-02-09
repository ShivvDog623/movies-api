"""
Actors Blueprint. Serves actor table related endpoints.
"""

from flask import Blueprint, jsonify, request
from app import db
from doQuery import doQuery


actor_blueprint = Blueprint('actor', __name__)

@actor_blueprint.route('/actor-data', methods=['GET'])
def get_movies():
    """
    GET: returns actors table data
    """
    sql = "SELECT * FROM movies.actor"
    params = []
    result = doQuery(sql, params)
    actor_list = []
    for record in result:
        actor_list.append(record)
    return jsonify (actor_list)


@actor_blueprint.route('/actor-create', methods= ['POST'])
def create_actor():
    """
    POST: creates actor in actor table
    """
    data = request.get_json()
    first_name = data.get('first_name')
    middle_name = data.get('middle_name')
    last_name = data.get('last_name')
    sql = 'INSERT INTO movies.actor (first_name, middle_name, last_name) VALUES (%s,%s,%s) RETURNING *'
    params = [first_name, middle_name, last_name]
    result = doQuery(sql, params)
    print('result', result)
    return jsonify(result)


@actor_blueprint.route('/actor-update/<int:id>', methods=['PUT'])
def update_actor(id):
    """
    PUT: updates actor by id
    """
    sql = "UPDATE movies.actor SET first_name='Satyam' WHERE actor_id = %s RETURNING first_name"
    params = [id]
    result = doQuery(sql, params)
    return jsonify(result)

@actor_blueprint.route('/actor-remove/<int:id>', methods= ['DELETE'])
def delete_actor(id):
    """
    DELETE: Deletes actor by id (be careful).
    """
    sql = 'DELETE FROM movies.actor WHERE actor_id = %s RETURNING actor_id'
    params = [id]
    result = doQuery(sql, params)
    print('result', result)
    return jsonify(result)
