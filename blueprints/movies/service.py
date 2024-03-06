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



def update_by_id(id):
    """
    SERVICE: Update movie by id
    """
    sql = "UPDATE movies.movie SET title='MoneyBag' WHERE movie_id =%s RETURNING title"
    params = [id]
    result = doQuery(sql, params)
    return result


def delete_by_id(id):
    """
    SERVICE: Delete movie by id (Be careful)
    """
    sql = 'DELETE FROM movies.movie WHERE movie_id = %s RETURNING movie_id'
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
    title = data.get('title')
    sql = "SELECT * FROM movies.movie WHERE title ILIKE ANY(%s)"
    params = [title]
    result = doQuery(sql, params)
    return result