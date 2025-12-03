# Sprint One Plan

**Sprint Duration**: 1 evening (a highly accelerated project due to this being a test run for an assignment).
**Sprint Goal:** Establish the foundational system elements, primarily user authentication, database setup, and the first fully working CRUD capability (creating fitness logs). Focus is on building essential backend infrastructure and enabling the most fundamental user interactions.

# Sprint Goal

Deliver a minimal but functional core system that allows:

- User registration
- User login
- Creating a daily fitness log

Ensures a stable base for future sprints (analytics, charts, insights, etc.).

# Sprint Backlog Items (Selected From Product Backlog)

| Story ID | Title                            | Priority | Story Points | Status |
| -------- | -------------------------------- | -------- | ------------ | ------ |
| US01     | User Registration                | P1       | 3            | To Do  |
| US02     | User Login                       | P1       | 3            | To Do  |
| US03     | Add Daily Fitness Log            | P1       | 5            | To Do  |
| —        | Set up Flask backend structure   | —        | 3            | To Do  |
| —        | Set up SQLite database + schema  | —        | 2            | To Do  |
| —        | Set up TDD testing environment   | —        | 2            | To Do  |
| —        | Initial Streamlit UI placeholder | —        | 1            | To Do  |

Total Estimated Story Points: **19**

---

# Sprint Tasks (Breakdown)

Below are the actual development tasks required to complete the backlog items.

## **Task Group 1: Backend Setup (Flask + Project Structure)**

**Related Stories:** (Foundation work)

### Tasks

- Create Flask app folder structure
- Implement MVC-inspired layout
- Create `app.py` entrypoint
- Set up virtual environment & dependencies (`Flask`, `sqlite3`, `pytest`)
- Create a basic `/health` endpoint for testing

**DONE**

---

## **Task Group 2: Database Layer**

**Related Stories:** US01, US02, US03

### Tasks

- Design database schema (users + fitness_logs)
- Create SQLite DB initialization script
- Create repository classes:
  - `UserRepository`
  - `FitnessRepository`
- Implement database connection manager

**DONE**

---

## **Task Group 3: User Registration**

**Related Stories:** US01

### Tasks

- Write tests first (TDD) for registration:
  - test missing fields
  - test duplicate user
  - test success case
- Implement password hashing
- Create `/register` endpoint
- Validate JSON payload

**DONE**

---

## **Task Group 4: User Login**

**Related Stories:** US02

### Tasks

- Write tests:
  - incorrect password
  - non-existent user
  - successful login
- Implement login logic
- Create `/login` endpoint
- Add simple session token (JWT or dummy session ID)

---

## **Task Group 5: Add Fitness Log**

**Related Stories:** US03

### Tasks

- Write tests first:
  - valid log creation
  - invalid values
- Create FitnessLog model class
- Implement service + repository methods
- Create `/fitness/create` endpoint

---

## **Task Group 6: Streamlit Initial UI (Minimal)**

_(Just enough to test the API)_

### Tasks

- Set up `/frontend/main.py`
- Create:
  - Registration page
  - Login page
- Wire Streamlit forms to backend API endpoints

---

# Definition of Done (DoD)

Item is done when:

- All acceptance criteria are met
- All unit tests for that story pass
- No severe bugs remain
- Code is committed to GitHub with meaningful messages
- API endpoints tested using Postman or Streamlit
- Documentation updated (e.g., API endpoints file, ER diagram if changed)

---

# Testing Approach

- Use TDD: write tests before implementation.
- Use pytest.
- Tests stored in `backend/tests/`.
- Test categories for this sprint:
  - Repository tests
  - Service layer tests
  - Controller (route) tests

---

# Deliverables

By the end of Sprint 1, there should be:

### Fully working:

- Registration
- Login
- Create Fitness Log

### Working infrastructure:

- Flask backend
- SQLite database
- Basic Streamlit UI
- Testing environment (pytest)

### Documentation:

- Updated product backlog (if changes made)
- Sprint 1 review & retrospective (separate file)
