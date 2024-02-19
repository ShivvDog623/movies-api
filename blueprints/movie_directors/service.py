from doQuery import doQuery
from flask import request

def get_all_movie_directors():
    """
    SERVICE: returns all movie_director data
    """
    sql = "SELECT * FROM movies.movie_director"
    params = []
    result = doQuery(sql, params)
    return result

def get_by_id(id):
    """
    SERVICE: returns movie_director by director id
    """
    sql = "SELECT * FROM movies.movie_director WHERE director_id = %s"
    params = [id]
    result = doQuery(sql, params)
    return result