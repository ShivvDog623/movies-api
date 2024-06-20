"""
Health Blueprint. Serves all health related endpoints.
"""
from flask import Blueprint, jsonify, current_app
from app import db
from doQuery import doQuery

health_blueprint = Blueprint('health', __name__)

@health_blueprint.route('/health', methods=["GET"])
def get_health():
    """
    GET: returns api health
    """
    message = "OK"
    return jsonify (message)

@health_blueprint.route('/db-health', methods=['GET'])
def get_dbconn():
    """
    GET: returns database health
    """
    try:
        sql = 'SELECT CURRENT_TIMESTAMP'
        doQuery(sql, [])
        return 'DB : DB OK'
    except:
        return 'DB : NOT OK'    


@health_blueprint.route('/')
def home():
    """Blueprint Will make static html file with flask"""
    return current_app.send_static_file('index.html')
