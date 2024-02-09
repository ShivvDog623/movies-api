"""
Movie Blueprint. Serves all movies table related endpoints. 
"""
from flask import Blueprint, jsonify, request
from app import db
from doQuery import doQuery 

movie_blueprint = Blueprint('movie', __name__)

@movie_blueprint.route('/movies-data', methods=['GET'])
def get_movies():
    """
    GET: returns movies table data
    """
    sql = "SELECT * FROM movies.movie"
    params = []
    result = doQuery(sql, params)
    movie_list = []
    for record in result:
        movie_list.append(record)
    return jsonify (movie_list)


@movie_blueprint.route('/movies-create', methods= ['POST'])
def create_movie():
    """
    POST: creates movie in movie table
    """
    data = request.get_json()
    title = data.get('title')
    year = data.get('year')
    description = data.get('description')
    time = data.get('time')
    rating = data.get('rating')
    vote = data.get('vote')
    revenue = data.get('revenue')
    metascore = data.get('metascore')
    sql = 'INSERT INTO movies.movie (title, year, description, time, rating, vote, revenue, metascore) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *'
    params = [title, year, description, time, rating, vote, revenue, metascore]
    result = doQuery(sql, params)
    print('result', result)
    return jsonify(result)


@movie_blueprint.route('/movies-update/<int:id>', methods=['PUT'])
def update_movie(id):
    """
    PUT: updates movie title by id
    """
    sql = "UPDATE movies.movie SET title='MoneyBag' WHERE movie_id =%s RETURNING title"
    params = [id]
    result = doQuery(sql, params)
    return jsonify(result)

@movie_blueprint.route('/movies-remove/<int:id>', methods= ['DELETE'])
def delete_movie(id):
    """
    DELETE: Deletes data by id (be careful).
    """
    sql = 'DELETE FROM movies.movie WHERE movie_id = %s RETURNING movie_id'
    params = [id]
    result = doQuery(sql, params)
    print('result', result)
    return jsonify(result)

