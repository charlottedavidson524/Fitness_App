# Product Backlog

This document contains the initial product backlog. Items are written as user stories, each with acceptance criteria, priority, and estimated effort (story points).

## Legend

- Priority:

  - P1 = High (must-have)
  - P2 = Medium (should-have)
  - P3 = Low (nice-to-have)

- Story Points:
  - 1 = Very small
  - 2 = Small
  - 3 = Medium
  - 5 = Large
  - 8 = Very Large

# Product Backlog

## Story ID: US01 – User Registration

As a new user, I want to create an account so that I can log in and store my fitness data securely.

### Acceptance Criteria

- User can enter username, email, and password.
- Password must be stored securely.
- Duplicate usernames/emails are not allowed.
- Backend returns success or appropriate error messages.

**Priority:** P1  
**Story Points:** 3

## Story ID: US02 – User Login

As a user, I want to log into my account so that I can access my personal fitness logs.

### Acceptance Criteria

- User enters email/username + password.
- Backend validates credentials.
- Invalid login attempts return an error.
- Successful login returns a session token or similar mechanism.

**Priority:** P1  
**Story Points:** 3

## Story ID: US03 – Add Daily Fitness Log

As a user, I want to log daily fitness stats so that I can track my activity over time.

### Acceptance Criteria

- User can add steps, workout type, duration, calories, and notes.
- Date defaults to today but can be selected manually.
- Data is stored in SQLite via the API.
- Input validation is applied.

**Priority:** P1  
**Story Points:** 5

## Story ID: US04 – View Fitness Logs

As a user, I want to view all my logged fitness data so that I can monitor my progress.

### Acceptance Criteria

- Backend returns logs for the authenticated user.
- User can see entries in a list or table.
- Streamlit displays them clearly.

**Priority:** P1  
**Story Points:** 3

## Story ID: US05 – Update an Existing Log

As a user, I want to edit any fitness log I have created so that I can fix mistakes or update information.

### Acceptance Criteria

- User selects a log to edit.
- All fields can be updated.
- Database is updated accordingly.
- Validation is re-applied.

**Priority:** P2  
**Story Points:** 5

## Story ID: US06 – Delete a Fitness Log

As a user, I want to delete old or incorrect data so that my records remain accurate.

### Acceptance Criteria

- User can delete logs.
- System asks for confirmation.
- Log is removed from SQLite permanently.

**Priority:** P2  
**Story Points:** 2

## Story ID: US07 – Weekly Summary Analytics

As a user, I want to see my weekly activity summary so that I can evaluate my performance.

### Acceptance Criteria

- Backend calculates weekly totals and averages.
- Streamlit displays summary cards.
- Must include at least steps, duration and calories.

**Priority:** P2  
**Story Points:** 5

## **Story ID: US08 – Charts & Visualisations**

As a user, I want to see charts (e.g., steps over time) so that I can visually interpret my fitness progress.

### Acceptance Criteria

- Line chart for steps.
- Bar or line chart for duration.
- Uses matplotlib or Plotly.
- Data pulled via Flask API.

**Priority:** P2  
**Story Points:** 5

---

## Story ID: US09 – Profile Page

As a user, I want to view my profile details so that I have a personalised experience.

### Acceptance Criteria

- User can see username and email.
- Optionally edit email in the future.

**Priority:** P3  
**Story Points:** 2

## Story ID: US10 – Motivational Insights

As a user, I want to receive simple automated insights so that I stay motivated to maintain my fitness.

### Acceptance Criteria

- Example insights:
  - “Your step count increased by 12% this week.”
  - “You exercised 4 days this week — great job!”
- Backend generates insights based on simple analytics.

**Priority:** P3  
**Story Points:** 8

---

# Backlog Summary Table

| Story ID | Title                   | Priority | Story Points |
| -------- | ----------------------- | -------- | ------------ |
| US01     | User Registration       | P1       | 3            |
| US02     | User Login              | P1       | 3            |
| US03     | Add Daily Fitness Log   | P1       | 5            |
| US04     | View Fitness Logs       | P1       | 3            |
| US05     | Update Log              | P2       | 5            |
| US06     | Delete Log              | P2       | 2            |
| US07     | Weekly Summary          | P2       | 5            |
| US08     | Charts & Visualisations | P2       | 5            |
| US09     | Profile Page            | P3       | 2            |
| US10     | Motivational Insights   | P3       | 8            |

---

# Additional Notes

- This backlog is iterative and may evolve during development.
- Items will be refined during sprint planning.
- Priorities and story points may change as new information emerges.
