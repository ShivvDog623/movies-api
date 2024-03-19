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

def get_id(id):
    """
    SERVICE: returns movie_director by director id
    """
    sql = """
            SELECT * FROM movies.movie_director
            INNER JOIN movies.director
            ON movies.movie_director.director_id = movies.director.director_id
            INNER JOIN movies.movie
            ON movies.movie.movie_id = movies.movie_director.movie_id
            WHERE movies.director.director_id = %s
            """
    params = [id]
    result = doQuery(sql, params)
    return result