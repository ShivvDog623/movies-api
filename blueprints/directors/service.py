from doQuery import doQuery
from flask import request

def get_all():
    """
    SERVICE: returns all directors
    """
    sql = "SELECT * FROM movies.director"
    params = []
    result = doQuery(sql, params)
    return result

def get_id(id):
    """
    SERVICE: returns director by id
    """
    sql = "SELECT * FROM movies.director WHERE director_id = %s"
    params = [id]
    result = doQuery(sql, params)
    return result

def get_movie_directors_by_id(id):
    """
    SERVICE: returns movie data by director id
    """
    sql =   """
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


def create_director(data):
    """
    SERVICE: creates new director in database table
    """
    first_name = data.get('first_name')
    middle_name = data.get('middle_name')
    last_name = data.get('last_name')
    sql = 'INSERT INTO movies.director (first_name, middle_name, last_name) VALUES (%s,%s,%s) RETURNING *'
    params = [first_name, middle_name, last_name]
    result = doQuery(sql, params)
    return result



def update_by_id(id, data):
    """
    SERVICE: Update director by id
    """
    first_name = data.get('first_name')
    middle_name = data.get('middle_name')
    last_name = data.get('last_name')
    sql = """UPDATE movies.director 
            SET first_name= %s,
            middle_name = %s,
            last_name = %s 
            WHERE director_id = %s 
            RETURNING *"""
    params = [first_name, middle_name, last_name, id]
    result = doQuery(sql, params)
    return result


def delete_by_id(id):
    """
    SERVICE: Delete director by id (Be careful)
    """
    sql = 'DELETE FROM movies.director WHERE director_id = %s RETURNING *'
    params = [id]
    result = doQuery(sql, params)
    return result