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
    sql =   """
            SELECT * FROM movies.movie_genre 
            FULL JOIN movies.genre
            ON movies.movie_genre.genre_id = movies.genre.genre_id
            FULL JOIN movies.movie
            ON movies.movie.movie_id = movies.movie_genre.movie_id
            WHERE movies.genre.genre_id = %s
            """
    params = [id]
    result = doQuery(sql, params)
    return result