import pytest
from backend.app import app
from backend.database import Database
import json

# Test for: missing fields, duplicate user and success case. 

@pytest.fixture
def client(tmp_path):
    # 1. Create a temporary DB path for this test
    test_db = tmp_path / "test.db"
    app.config["DATABASE_PATH"] = str(test_db)

    # 2. Reinitialize DB so it starts empty
    db = Database(str(test_db))
    db.initialize()

    # 3. Create test client
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# Missing fields
def test_missing_fields(client):
    # Send HTTP POST request to /register
    # Send empty JSON object to simulate missing fields
    response = client.post("/register", json = {})
    assert response.status_code == 400 # Endpoint returns 400 Bad Request
    assert "missing" in response.json["error"].lower()

# Duplicate users
def test_duplicate_user(client):
    # First registration
    client.post("/register", json = {
        "username": "alice",
        "password": "pass",
        "email": "alice@example.com"
    })

    # Second registration with same name
    response = client.post("/register", json = {
        "username": "alice",
        "password": "pass",
        "email": "alice2@example.com"
    })

    assert response.status_code == 409
    assert "already exists" in response.json["error"]

# Success case
def test_registration_success(client):
    response = client.post("/register", json = {
        "username": "james", 
        "password": "mypassword",
        "email": "james@example.com"
    })

    assert response.status_code == 201
    assert "user_id" in response.json