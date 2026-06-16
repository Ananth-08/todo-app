# Todo Application Backend

## Project Overview

This project is a backend implementation of a Todo Application developed using **FastAPI** and **SQLite**. The application provides RESTful APIs for managing todo items with complete CRUD functionality, status-based filtering, validation, error handling, and Docker support.

---

## Planned Features

* Create Todo
* View Todos
* Update Todo
* Delete Todo
* Filter Todos by Status

---

## Progress Completed

### 1. Project Structure Setup

The initial backend project structure has been successfully created.

#### Project Structure

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
├── Dockerfile
├── .gitignore
└── todo.db
```

---

### 2. Database Configuration

SQLite has been selected and configured as the database for the application.

#### Purpose

The database layer is responsible for:

* Establishing a connection with SQLite
* Managing database sessions
* Providing a common base class for database models
* Supporting automatic table creation through SQLAlchemy

#### Database File

```
todo.db
```

#### Database Components Implemented

* Database URL Configuration
* SQLAlchemy Engine
* Session Factory
* Declarative Base


---

### 3. Todo Data Model Design

The Todo entity structure has been finalized and implemented.

#### Database Table

```
todos
```

#### Todo Model Fields

| Field      | Type     | Description                         |
| ---------- | -------- | ----------------------------------- |
| id         | Integer  | Unique identifier for each todo     |
| title      | String   | Title of the todo task              |
| status     | String   | Current status of the todo          |
| created_at | DateTime | Timestamp when the todo was created |

#### Supported Status Values

* pending
* completed

The Todo model is configured using SQLAlchemy and automatically generates the corresponding database table structure.


---

### 4. Pydantic Schema Validation

Request and response validation has been implemented using Pydantic.

#### Schemas Created

##### TodoCreate

Used while creating a new todo.

```json
{
  "title": "Learn Docker",
  "completed": false
}
```

##### TodoUpdate

Used while updating an existing todo.

##### TodoResponse

Used for API responses.


---

### 5. CRUD Operations

All CRUD functionalities have been implemented successfully.

#### Create Todo

```http
POST /todos
```

Creates a new todo item.

#### Get All Todos

```http
GET /todos
```

Returns all todo items.

#### Get Todo By ID

```http
GET /todos/{todo_id}
```

Returns a specific todo item.

#### Update Todo

```http
PUT /todos/{todo_id}
```

Updates an existing todo item.

#### Delete Todo

```http
DELETE /todos/{todo_id}
```

Deletes a todo item.


---

### 6. Filter Todos by Status

Filtering functionality has been implemented to retrieve todos based on their current status.

#### Supported Filters

```http
GET /todos?status=pending
GET /todos?status=completed
```


---

### 7. Error Handling

FastAPI HTTP exception handling has been implemented.

#### Example

```python
raise HTTPException(
    status_code=404,
    detail="Todo not found"
)
```

#### Handled Scenarios

* Todo not found
* Invalid Todo ID
* Validation errors
* Bad request handling


---

### 8. API Documentation

FastAPI Swagger UI has been configured and is available for testing.

#### Endpoint

```text
http://localhost:8000/docs
```

#### Features

* Interactive API testing
* Request validation
* Response documentation
* Endpoint exploration


---

### 9. Dockerization

The application has been containerized using Docker.

#### Files Added

##### Dockerfile

Responsible for:

* Creating Docker images
* Installing dependencies
* Running the FastAPI application

##### .dockerignore

Used to exclude:

```text
venv/
__pycache__/
.git/
todo.db
```

#### Docker Commands

##### Build Image

```bash
docker build -t todo-api .
```

##### Run Container

```bash
docker run -p 8000:8000 todo-api
```

#### Result

The application successfully runs inside a Docker container.


---

### 10. Git & GitHub Workflow

Version control and collaboration workflow have been completed.

#### Activities Performed

* Connected local repository to remote GitHub repository
* Fetched remote branches
* Switched to Feature1 branch
* Committed project changes
* Prepared code for Pull Request workflow

#### Branches

* main
* Feature1
* Feature2


---
