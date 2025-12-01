# ER Diagram and Database Schema

## Diagram

See `docs/diagrams/er_diagram.png`

## Database Overview

The database uses SQLite and has two main tables:

- Users
- FitnessLogs

The relationship is one-to-many (one user can have many fitness logs).

## SQLite Schema

```
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password_hash TEXT NOT NULL,
email TEXT
);


CREATE TABLE IF NOT EXISTS fitness_logs (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
log_date TEXT NOT NULL,
steps INTEGER,
distance REAL,
calories INTEGER,
FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## Field Descriptions

### Table: Users

id -> int -> Unique user identifier
username -> text ->Unique username
password_hash -> text -> Securely hashed password
email -> text -> Optional contact field

### Table: FitnessLogs

id -> int -> Unique log identifier
user_id -> int -> References user ID
log_date -> date -> Date of the fitness record
steps -> int -> Number of steps taken
distance -> real -> Distance covered (km)
calories -> int -> Calories burned
