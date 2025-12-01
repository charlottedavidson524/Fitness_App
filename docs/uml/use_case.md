# Use Case

Identify the interactions between actors and the system.

## Actors

### User

This is the main actor who uses the fitness tracker to:

- Register an account.
- Log in.
- Enter daily fitness data.
- View progress and summaries.

### System (Backend Services)

This is an interbal actor responsible for:

- Storing and retrieving data.
- Running analytics.
- Authenticating users.

## Use Case Diagram

See `docs/diagrams/use_case_uml.png`

## Use Case Descriptions

### Register Account

Goal: Create a new user profile.

Trigger: User submits registration form.

Success: New account stored in database.

Failure: Username already exists/invalid.

### Log In

Goal: Authenticate the user.
Trigger: User submits login form.
Success: Session token or success response is returned
Failure: Incorrect credentials.

### Create Fitness Logs

Goal: Add new daily fitness record.
Trigger: User enters workout/health data.
Success: Data saved to SQLite.
Failure: Invalid data or missing fields.

### View Fitness Logs

Goal: Retrieve previous logs.
Trigger: User navigates to log history.
Success: Logs returned as JSON.
Failure: Database error.

### Update Fitness Logs

Goal: Modify an existing log.
Success: Update log saved.
Failure: Log not found.

### Delete Fitness Logs

Goal: Remove a log.
Success: Log deleted.
Failure: Invalid ID or permissions.

### View Analytics

Goal: Visualise progress over time.
Includes: Weekly/monthly summaries and chart generation.
