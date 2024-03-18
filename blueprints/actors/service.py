
from doQuery import doQuery
from flask import request

def get_all_actors():
    """
    SERVICE: returns all actors
    """
    sql = "SELECT * FROM movies.actor"
    params = []
    result = doQuery(sql, params)

    return result

def get_by_id(id):
    """
    SERVICE: returns actor by id
    """
    sql = "SELECT * FROM movies.actor WHERE actor_id = %s"
    params = [id]
    result = doQuery(sql, params)
    return result

def create_new_actor(data):
    """
    SERVICE: creates new actor in database table
    """
    first_name = data.get('first_name')
    middle_name = data.get('middle_name')
    last_name = data.get('last_name')
    sql = 'INSERT INTO movies.actor (first_name, middle_name, last_name) VALUES (%s,%s,%s) RETURNING *'
    params = [first_name, middle_name, last_name]
    result = doQuery(sql, params)
    return result

def update_by_id(id):
    """
    SERVICE: Update actor by id
    """
    sql = "UPDATE movies.actor SET first_name='Satyam' WHERE actor_id = %s RETURNING first_name"
    params = [id]
    result = doQuery(sql, params)
    return result

def delete_by_id(id):
    """
    SERVICE: Delete actor by id (Be careful)
    """
    sql = 'DELETE FROM movies.actor WHERE actor_id = %s RETURNING actor_id'
    params = [id]
    result = doQuery(sql, params) 
    return result 


def get_actor_movies_id(id):
    """
    SERVICE: return movies that the actor was in by actor_id
    """
    sql =   """
            SELECT * FROM movies.movie_actor
            INNER JOIN movies.movie
            ON movies.movie_actor.movie_id = movies.movie.movie_id
            WHERE actor_id = %s 
            """
    params = [id]
    result = doQuery(sql, params)
    return result