from doQuery import doQuery
from flask import request

def get_all_movie_genres():
    """
    SERVICE: returns all movie_genre data
    """
    sql = "SELECT * FROM movies.movie_genre"
    params = []
    result = doQuery(sql, params)
    return result

def get_id(id):
    """
    SERVICE: returns movie_genre by genre id
    """
    sql = "SELECT * FROM movies.movie_genre WHERE genre_id = %s"
    params = [id]
    result = doQuery(sql, params)
    return result