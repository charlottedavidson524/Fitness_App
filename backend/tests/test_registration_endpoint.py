import pytest
from backend.app import app
import json

# Test for: missing fields, duplicate user and success case. 

@pytest.fixture
def client():
    # Turn on Flask testing mode
    app.config["TESTING"] = True
    # Creates a Flask test client.
    # Simulates HTTP requests to Flask app in memory without running a server.
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
        "username": "bob", 
        "password": "mypassword",
        "email": "bob@example.com"
    })

    assert response.status_code == 201
    assert "user_id" in response.json