from doQuery import doQuery
from flask import request

def get_all_movieactors():
    """
    SERVICE: returns all movie_actor data
    """
    sql = "SELECT * FROM movies.movie_actor"
    params = []
    result = doQuery(sql, params)
    return result

def get_id(id):
    """
    SERVICE: returns movie_actor by actor id
    """
    sql = "SELECT * FROM movies.movie_actor WHERE actor_id = %s"
    params = [id]
    result = doQuery(sql, params)
    return result