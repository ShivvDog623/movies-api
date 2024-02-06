from flask import Flask, jsonify, request


def register_blueprint(app):
    
    """registers blueprints"""

    from blueprints.health.blueprints import health_blueprint

    #register blueprints
    app.register_blueprint(health_blueprint)

def create_app():
    app = Flask(__name__)

    register_blueprint(app)

    return app



