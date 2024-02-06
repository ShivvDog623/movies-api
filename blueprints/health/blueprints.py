from flask import Blueprint, jsonify

health_blueprint = Blueprint('health', __name__, url_prefix='/status')

@health_blueprint.route('/health', methods=["GET"])
def get():
    
    message = "OK?"
    return jsonify (message)