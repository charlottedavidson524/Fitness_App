import pytest
from backend.app import app

@pytest.fixture
def client(tmp_path):
    # Use a temporary test database
    test_db_path = tmp_path / "test.db"
    app.config["DATABASE_PATH"] = str(test_db_path)

    # Re-initialize a clean database for every test
    from backend.database import Database
    db = Database(str(test_db_path))
    db.initialize()

    with app.test_client() as client:
        yield client

def test_nonexistent_user(client):
    response = client.post("/login", json = {
        "username": "ghost",
        "password": "whatever"
    })
    assert response.status_code == 404
    assert "not found" in response.json["error"].lower()

def test_login_incorrect_password(client):
    # Create user
    client.post("/register", json = {
        "username": "john",
        "password": "password",
        "email": "john@example.com"
    })

    # Try logging in with wrong password
    response = client.post("/login", json = {
        "username": "john",
        "password": "wrongpassword"
    })

    assert response.status_code == 401
    assert "incorrect" in response.json["error"].lower()

def test_login_success(client):
    client.post("/register", json = {
        "username": "sam",
        "password": "password123",
        "email": "sam@email.com"
    })

    response = client.post("/login", json = {
        "username": "sam",
        "password": "password123"
    })

    assert response.status_code == 200
    assert "token" in response.json 