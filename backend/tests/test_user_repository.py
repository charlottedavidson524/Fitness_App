import pytest
from backend.database import Database
from backend.repositories.user_repository import UserRepository

# Testing for three requirements in this file: a user can be created, a user can be fetched
# by username, and duplicate usernames aren't allowed.

@pytest.fixture
# Create a temporary directory with a fresh SQLite file.
def repo(tmp_path):
    db_path = tmp_path / "test.db"
    # Loads database class pointing to file.
    db = Database(str(db_path))
    # Creates users table and ensures schema exists before repository operations.
    db.initialize()
    # Repository receives a database instance.
    # Ensures repository uses correct, isolated test database.
    return UserRepository(db)

# Check create_user works().
def test_create_user(repo):
    user_id = repo.create_user("alice", "hash123", "alice@example.com")
    assert isinstance(user_id, int)

# Check user can be retrieved.
def test_get_user_by_username(repo):
    repo.create_user("bob", "hashxyz", "bob@example.com")
    user = repo.get_user_by_username("bob")
    assert user["username"] == "bob"

# Duplicate username prevention
def test_prevent_duplicate_user(repo):
    repo.create_user("steve", "pass1", "steve@example.com")
    with pytest.raises(ValueError):
        repo.create_user("steve", "pass2", "steve2@example.com")