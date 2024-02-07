import os
import psycopg2
from psycopg2 import DatabaseError
from dotenv import load_dotenv

class Connection:
    def __init__(self):
        self.conn = None
        self.cur = None
        print('New connection created...')
        self.setConnection()

    def setConnection(self):
        load_dotenv()
        self.conn = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            database = os.getenv("DATABASE"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            port = os.getenv("DB_PORT"))
        self.cur = self.conn.cursor()
        
        self.cur = self.conn.cursor()

    def getConnection(self):
        return self.conn
    
    def getCursor(self):
        return self.cur


