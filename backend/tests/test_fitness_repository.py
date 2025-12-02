import pytest
from datetime import date
from backend.database import Database
from backend.repositories.fitness_repository import FitnessRepository
from backend.repositories.user_repository import UserRepository

# Check that we can create a fitness log, retrieve a log, and check for invalid ID.

@pytest.fixture
# Create a temporary database file, initialise database schema and return two repos
# (one for fetching users and one for fetching fitness logs)
def repos(tmp_path):
    db_path = tmp_path / "test.db"
    db = Database(str(db_path))
    db.initialize()
    return {
        "fitness": FitnessRepository(db),
        "users": UserRepository(db)
    }

# Create user and fitness log, checking that log was created successfully.
# Log should return a valid integer primary key.
def test_create_log(repos):
    user_id = repos["users"].create_user("a", "b", "c@example.com")
    log_id = repos["fitness"].create_log(user_id, date.today(), 5000, 3.2, 200)
    assert isinstance(log_id, int)

# Check that a log can be retrieved.
def test_get_logs(repos):
    # Create user
    user_id = repos["users"].create_user("a", "b", "c@example.com")
    # Add one log
    repos["fitness"].create_log(user_id, date.today(), 5000, 3.2, 200)

    # Fetch all logs belonging to user
    logs = repos["fitness"].get_logs_by_user(user_id)
    # Check that only one log is retrieved.
    assert len(logs) == 1

# Test for invalid user ID.
def test_invalid_log_user(repos):
    with pytest.raises(ValueError):
        # User 999 doesn't exist (hasn't been created) so flag error.
        repos["fitness"].create_log(999, date.today(), 1000, 5.4, 300)