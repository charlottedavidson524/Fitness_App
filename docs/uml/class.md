# Classes

Describes the structure of the backend Python application, including models, services and repositories.

## Diagram

See `docs/diagrams/class_uml.png`.

## Overview of System Components

### Model Classes

User: Represents an authenticated user.

FitnessLog: Represents a daily fitness record linked to a user.

### Repository Layer

Handles all direct interactions with the SQLite database.

- UserRepository: CRUD operations for users.
- FitnessRepository: CRUD operations for fitness logs.

### Service Layer

Encapsulates business logic and orchestrates repository operations.

- UserService: Registration and login
- FitnessService: Add, update and delete logs

### Utility Classes

AuthUtils: Password hashing and password verification
