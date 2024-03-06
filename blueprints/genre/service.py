from doQuery import doQuery
from flask import request

def get_all():
    """
    SERVICE: returns all genres
    """
    sql = "SELECT * FROM movies.genre"
    params = []
    result = doQuery(sql, params)
    return result

def get_id(id):
    """
    SERVICE: returns genre by id
    """
    sql = "SELECT * FROM movies.genre WHERE genre_id = %s"
    params = [id]
    result = doQuery(sql, params)
    return result

def create_genre():
    """
    SERVICE: creates new genre in database table
    """
    data = request.get_json()
    genre = data.get('genre')
    sql = 'INSERT INTO movies.genre (genre) VALUES (%s) RETURNING *'
    params = [genre]
    result = doQuery(sql, params)
    return result



def update_by_id(id):
    """
    SERVICE: Update genre by id
    """
    sql = "UPDATE movies.genre SET genre='CrazyKillerBee' WHERE genre_id =%s RETURNING genre"
    params = [id]
    result = doQuery(sql, params)
    return result


def delete_by_id(id):
    """
    SERVICE: Delete genre by id (Be careful)
    """
    sql = 'DELETE FROM movies.genre WHERE genre_id = %s RETURNING genre_id'
    params = [id]
    result = doQuery(sql, params)
    return result