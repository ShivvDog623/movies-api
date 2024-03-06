from flask import Flask, jsonify, request
from db.Connection import Connection

conn = None
cur = None

db = Connection()
conn = db.getConnection()
cur = db.getCursor()



def register_blueprint(app):
    
    """registers blueprints"""

    from blueprints.health.blueprints import health_blueprint
    from blueprints.movies.blueprints import movie_blueprint
    from blueprints.actors.blueprints import actor_blueprint
    from blueprints.directors.blueprints import directors_blueprint
    from blueprints.genres.blueprints import genre_blueprint 
    from blueprints.movie_actor.blueprints import movie_actor_blueprint
    from blueprints.movie_directors.blueprints import movie_director_blueprint
    from blueprints.movie_genres.blueprints import movie_genre_blueprint

    #register blueprints
    app.register_blueprint(health_blueprint)
    app.register_blueprint(movie_blueprint)
    app.register_blueprint(actor_blueprint)
    app.register_blueprint(directors_blueprint)
    app.register_blueprint(genre_blueprint)
    app.register_blueprint(movie_actor_blueprint)
    app.register_blueprint(movie_director_blueprint)
    app.register_blueprint(movie_genre_blueprint)
    


def create_app():
    app = Flask(__name__)
    app.app_context().push()
    register_blueprint(app)
    
    return app



