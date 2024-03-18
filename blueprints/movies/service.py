from doQuery import doQuery
from flask import request
import json


def get_all():
    """
    SERVICE: returns all movies
    """
    sql = "SELECT * FROM movies.movie"
    params = []
    result = doQuery(sql, params)
    return result


def get_id(id):
    """
    SERVICE: returns movie by id
    """
    sql = "SELECT * FROM movies.movie WHERE movie_id = %s"
    params = [id]
    result = doQuery(sql, params)
    print(result)
    return result


def create_movie(data):
    """
    SERVICE: creates new movie in database table
    """
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
    return result



def update_by_id(id, data):
    """
    SERVICE: Update movie by id
    """
    title = data.get('title')
    year = data.get('year')
    description = data.get('description')
    time = data.get('time')
    rating = data.get('rating')
    vote = data.get('vote')
    revenue = data.get('revenue')
    metascore = data.get('metascore')
    sql = """
    UPDATE movies.movie 
        SET title=%s, 
        year= %s, 
        description= %s, 
        time= %s, 
        rating= %s, 
        vote= %s, 
        revenue= %s, 
        metascore= %s 
    WHERE movie_id =%s RETURNING *
    """
    params = [title, year, description, time, rating, vote, revenue, metascore, id]
    result = doQuery(sql, params)
    return result


def delete_by_id(id):
    """
    SERVICE: Delete movie by id (Be careful)
    """
    sql = 'DELETE FROM movies.movie WHERE movie_id = %s RETURNING *'
    params = [id]
    result = doQuery(sql, params)
    return result

def exact_search(data):
    title = data.get('title')
    sql = 'SELECT * FROM movies.movie WHERE LOWER(title)=LOWER(%s)'
    params = [title]
    result = doQuery(sql, params)
    return result

def like_search(data):
    title = data.get('title')
    sql = "SELECT * FROM movies.movie WHERE title ILIKE %s"
    params = ['%' + title + '%']
    result = doQuery(sql, params)
    return result

def in_search(data):
    field = data.get('field')
    values = data.get('values')

    for idx, value in enumerate(values):
        val = value["value"]
        if idx == 0:
            in_clause = f"'{val}'"
        else:
            in_clause = f"{in_clause},'{val}'" 

    sql = f"SELECT * FROM movies.movie WHERE {field} IN ({in_clause})"
    result = doQuery(sql, [])
    return result


def movie_directors_by_id(id):
    """
    SERVICE: returns director and movie data by movie_id
    """
    sql =   """
            SELECT * FROM movies.movie_director
            INNER JOIN movies.director
            ON movies.movie_director.director_id = movies.director.director_id
            INNER JOIN movies.movie
            ON movies.movie.movie_id = movies.movie_director.movie_id
            WHERE movies.movie.movie_id = %s
            """
    params = [id]
    result = doQuery(sql, params)
    return result


def movie_actors_by_id(id):
    """
    SERVICE: returns actors and movie data by movie_id
    """
    sql =   """
            SELECT * FROM movies.movie_actor 
            FULL JOIN movies.actor
            ON movies.movie_actor.actor_id = movies.actor.actor_id
            FULL JOIN movies.movie
            ON movies.movie.movie_id = movies.movie_actor.movie_id
            WHERE movies.movie.movie_id = %s

            """
    params = [id]
    result = doQuery(sql, params)
    return result


def movie_genres_by_id(id):
    """
    SERVICE: returns genres and movie by movie_id
    """

    sql =   """
            SELECT * FROM movies.movie_genre 
            FULL JOIN movies.genre
            ON movies.movie_genre.genre_id = movies.genre.genre_id
            FULL JOIN movies.movie
            ON movies.movie.movie_id = movies.movie_genre.movie_id
            WHERE movies.movie.movie_id = %s
            """
    
    params = [id]
    result = doQuery(sql, params)
    return result



    