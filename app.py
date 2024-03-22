from flask import Flask, jsonify, request
from db.Connection import Connection
from flask_swagger_ui import get_swaggerui_blueprint

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
    app.json.sort_keys = False

    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Test application"
        },
        # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )



    app.register_blueprint(swaggerui_blueprint)
    
    return app






