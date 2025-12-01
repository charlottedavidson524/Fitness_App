# API Endpoints

Describes the RESTful API endpoints for the backend.

Base URL (for local development):

`http://localhost:5000`

## User Authetication

**POST /register**

Create a new user account

**Request Body (JSON)**

```
{
"username": "john",
"email": "john@example.com",
"password": "mypassword"
}
```

**Responses:**

- `201 Created`: Registration successful
- `400 Bad Request`: Missing fields or duplicate email/password.

**POST /login**

Authenticate a user

**Request Body (JSON)**

```
{
"username": "john",
"password": "mypassword"
}
```

**Response (JSON)**

```
{
"token": "abc123"
}
```

- `200 OK`: Login successful
- `401 Unauthorised`: Invalid credentials

## Fitness Logs

**POST /fitness/create**

Add a new fitness log entry

**Request Body (JSON)**

```
{
"token": "abc123",
"steps": 5000,
"duration": 30,
"workout_type": "Running",
"calories": 250,
"notes": "Morning run"
}
```

**Response:**

- `201 created`: Log created
- `400 bad request`: Missing/invalid fields

**GET /fitness/list?token=abc123**

Get all fitness logs for the authenticated user

**Response:**

```
[
{"id":1, "date":"2025-12-01", "steps":5000, ...},
{...}
]
```

**PUT /fitness/update/<log_id>**

Update an existing fitness log.

**Request Body (JSON)**

```
{
"token": "abc123",
"steps": 6000,
"duration": 35
}
```

**Response:**

- `200 ok`: Log updated
- `404 not found`: Log does not exist

**DELETE /fitness/delete/<log_id>**

Delete a fitness log.

**Request Parameters:**

- log_id: ID of the log to delete
- token: Authentication token

**Response:**

- `200 OK`: Log deleted
- `404 Not Found`: Log does not exist

## Analytics

**GET /analytics/weekly_summary?token=abc123**

Get weekly summary statistics (total steps, total calories, etc.).

**GET /analytics/charts?token=abc123**

Get data formatted for chart visualizations.

## Notes

- All endpoints require authentication except /register and /login.

- Responses are JSON-formatted for frontend consumption.
