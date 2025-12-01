# Requirements

## User Requirements:

- Register an account and login.
- Log daily fitness data.
  - Steps
  - Workout type
  - Duration
  - Calories burned
  - Optional notes
- View weekly or monthly summaries.
- View charts (e.g. steps over time).
- Update or delete previous logs.
- Securely store private data.

## System Requirements:

- Store user accounts amd authentication.
- Store daily fitness logs.
- Provide CRUD functionality for fitness data.
- Support API endpoints (Flask) for:
  - Get data
  - Post data
  - Update data
  - Delete data
- Database handling using SQLite.
- Frontend interface using Streamlit consuming Flask API.
- Generate charts using seaborn.
- Use MVC pattern inside Flask backend.

## Functional Requirements:

- Allow user registration and login.
- Allow authenticated users to:
  - Create fitness logs.
  - Read logs.
  - Update logs.
  - Delete logs.
- Compute summary analytics.
  - Weekly averages.
  - Total calories.
  - Best performance week.
- Provide visualisations:
  - Steps/time chart
  - Workout duration trends
- Return JSON responses via Flask routes.
- Streamlit must serve as UI (forms and dashboard).

## Non-Functional Requirements:

- Usability: Easy-to-navigate UI (Streamlit).
- Performance: API responses under a second.
- Security: Password hashing.
- Reliability: Local SQLite file; transactions ACID-compliant.
- Maintainability: Python OOP, MVC separation.
- Scalability: Could upgrade DB to PostgreSQL later id needed.
- Portability: Runs locally on Windows/Mac/Linux.
- Testability: Pytest TDD + clear test folder structure.
