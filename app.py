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
    
    #register blueprints
    app.register_blueprint(health_blueprint)
    app.register_blueprint(movie_blueprint)
    app.register_blueprint(actor_blueprint)


def create_app():
    app = Flask(__name__)
    app.app_context().push()



    register_blueprint(app)
    
    return app



