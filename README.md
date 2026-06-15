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

