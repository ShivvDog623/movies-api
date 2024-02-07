from flask import Blueprint, jsonify
from app import db
from doQuery import doQuery

#get cursor and get connection
conn = db.getConnection()
cur = db.getCursor()





health_blueprint = Blueprint('health', __name__)

@health_blueprint.route('/health', methods=["GET"])
def get_health():
    
    message = "OK"
    return jsonify (message)



dbconn_blueprint = Blueprint('dbconn', __name__)

@dbconn_blueprint.route('/dbconn', methods=['GET'])
def get_dbconn():

    return "DB : OK"



