# System Architecture

## Overview

This app is built using a modular, layered architecture designed for maintainability, testability and scalability. The backend uses Flask to provide RESTful API endpoints, a SQLite database for persistent storage, and Python classes to structure business logic. The frontend uses Streamlit, communicating with the backend using HTTP.

## Architecture Diagram

UI["Streamlit Frontend (Forms + Charts)"] --> API["Flask Controllers (Routes)"]
API --> Services["Service Layer (Business Logic)"]
Services --> Repo["Repository Layer (DB Access)"]
Repo --> DB["SQLite Database"]

## Architecture Layers

### Streamlit Frontend

- Handles all user interactions.
- Submits requests to Flask API.
- Displays charts, tables and forms.

### Flask Backend

- Defines REST API endpoints.
- Validates input.
- Calls service layer.
- Returns JSON responses.

### Service Layer (Business Logic)

- Implements all processing rules.
- Ensures correct behaviour of fitness log operations.
- Performs calculations like weekly summaries.

### Repository Layer

- Executes SQL queries.
- Manages CRUD operations.
- Maps database rows to Python objects.

### Database Layer (SQLite)

Tables:

- users.
- fitness_logs.

Enforces:

- Primary keys.
- Foreign key constraints.
- Data integrity.

## MVC Pattern

Model:

- Python classes (User, FitnessLog) and SQLite tables.

View:

- JSON returned to Streamlit frontend.

Controller:

- Flask routes handling requests.
