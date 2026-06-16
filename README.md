# Todo Application Backend

## Project Overview

This project is a backend implementation of a Todo Application developed using FastAPI and SQLite. The application will provide CRUD operations and filtering functionality for managing todos.

### Planned Features

* Create Todo
* View Todos
* Update Todo
* Delete Todo
* Filter Todos by Status

---

# Progress Completed

## 1. Project Structure Setup

The initial backend project structure has been created.

```
todo-app/
│
├── backend/
│   ├── app/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   └── venv/
│
├── requirements.txt
├── DockerFile
├── .gitignore
└── todo.db
```

---

## 2. Database Configuration

SQLite has been selected as the database for the application.

### Purpose

The database layer is responsible for:

* Establishing a connection with SQLite.
* Managing database sessions.
* Providing a common base class for all database models.

### Database File

```
todo.db
```

### Database Components

* Database URL configuration
* SQLAlchemy Engine
* Session Factory
* Declarative Base

---

## 3. Todo Data Model Design

The Todo entity structure has been finalized.

### Todo Model Fields

| Field      | Type     | Description                         |
| ---------- | -------- | ----------------------------------- |
| id         | Integer  | Unique identifier for each todo     |
| title      | String   | Title of the todo task              |
| status     | String   | Current status of the todo          |
| created_at | DateTime | Timestamp when the todo was created |

### Supported Status Values

```
pending
completed
```

### Database Table

todos

The Todo model will be used to generate the database table structure automatically through SQLAlchemy.

4. Pydantic Schema Validation
Completed
Implemented request and response validation using Pydantic.

Schemas Created
TodoCreate
Used while creating a new todo.

{
  "title": "Learn Docker",
  "completed": false
}
TodoUpdate
Used while updating an existing todo.

TodoResponse
Used for API responses.

5. CRUD Operations
Completed
All CRUD functionalities have been implemented.

Create Todo
POST /todos
Creates a new todo item.

Get All Todos
GET /todos
Returns all todo items.

Get Todo By ID
GET /todos/{todo_id}
Returns a specific todo.

Update Todo
PUT /todos/{todo_id}
Updates an existing todo.

Delete Todo
DELETE /todos/{todo_id}
Deletes a todo item.

6. Error Handling
Completed
Implemented FastAPI HTTP exception handling.

Examples
raise HTTPException(
    status_code=404,
    detail="Todo not found"
)
Handled Scenarios
Todo not found

Invalid Todo ID

Validation errors

7. API Documentation
Completed
FastAPI Swagger UI is available.

Endpoints
http://localhost:8000/docs
Provides:

Interactive API testing

Request validation

Response documentation

8. Dockerization
Completed
The application has been containerized using Docker.

Files Added
Dockerfile
Responsible for:

Creating Docker image

Installing dependencies

Running FastAPI application

.dockerignore
Used to exclude:

venv
__pycache__
.git
todo.db
Docker Commands Used
Build Image
docker build -t todo-api .
Run Container
docker run -p 8000:8000 todo-api
Result
Application successfully runs inside a Docker container.

9. Git & GitHub Workflow
Completed
Connected local repository to remote GitHub repository

Fetched remote branches

Switched to Feature1 branch

Committed project changes

Prepared for Pull Request workflow

Branches
main
Feature1
Feature2
