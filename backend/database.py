import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def initialize(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT NOT NULL    
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fitness_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            log_date TEXT NOT NULL,
            steps INTEGER,
            distance REAL,
            calories INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """)

        conn.commit()
        conn.close()