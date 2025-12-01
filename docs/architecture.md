# System Architecture

This app is built using a modular, layered architecture designed for maintainability, testability and scalability. The backend uses Flask to provide RESTful API endpoints, a SQLite database for persistent storage, and Python classes to structure business logic. The frontend uses Streamlit, communicating with the backend using HTTP.

flowchart TD
UI["Streamlit Frontend (Forms + Charts)"] --> API["Flask Controllers (Routes)"]
API --> Services["Service Layer (Business Logic)"]
Services --> Repo["Repository Layer (DB Access)"]
Repo --> DB["SQLite Database"]
