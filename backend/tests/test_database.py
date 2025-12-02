import os
import sqlite3
from backend.database import Database

# Checks two core requirements of the database layer: the Database class should open a
# SQLite connection, and when initialise() is called, tables for users and fitness_logs
# must exist.

TEST_DB_PATH = 'test_database.db'

# Remove test database if it exists before each new test.
def teardown_function():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

# Ensure working database connection layer before building repositories.
def test_database_connection():
    db = Database(TEST_DB_PATH)
    conn = db.get_connection()
    assert isinstance(conn, sqlite3.Connection)
    # Check for: correctly stored path, valid sqlite3.Connection instance and no Exception.

# Test that initialisation creates tables.
def test_create_tables():
    db = Database(TEST_DB_PATH)
    # Create users and fitness_logs tables, commiting changes.
    db.initialize()

    # Open db file again.
    conn = db.get_connection()
    cursor = conn.cursor()

    # Query SQL internal metadata table, retrieving all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    # Flatten names into a pyhton list
    tables = [t[0] for t in cursor.fetchall()]

    assert "users" in tables
    assert "fitness_logs" in tables