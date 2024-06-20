"""Database Connection file"""

import os
import psycopg2
from psycopg2 import DatabaseError
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

class Connection:
    def __init__(self):
        self.conn = None
        self.cur = None
        
        self.setConnection()

    def setConnection(self):
        load_dotenv()
        try:
            self.conn = psycopg2.connect(
                host = os.getenv("DB_HOST"),
                database = os.getenv("DATABASE"),
                user = os.getenv("DB_USER"),
                password = os.getenv("DB_PASSWORD"),
                port = os.getenv("DB_PORT"))
            
            print(os.getenv("DB_PASSWORD"))
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            print('New connection created...')
        except DatabaseError as e:
            print("Database connection failed", e) 


    def getConnection(self):
        return self.conn
    
    def getCursor(self):
        return self.cur


