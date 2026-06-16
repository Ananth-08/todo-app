from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db, engine
from app.models import Base
from app.schemas import (
    TodoCreate,
    TodoUpdate,
    TodoResponse
)
from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Todo API Running Successfully"
    }


@app.get(
    "/todos",
    response_model=list[TodoResponse]
)
def get_todos(
    db: Session = Depends(get_db)
):
    return crud.get_all_todos(db)


@app.post(
    "/todos",
    response_model=TodoResponse
)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    return crud.create_todo(
        db,
        todo.title,
        todo.completed
    )


@app.get(
    "/todos/{todo_id}",
    response_model=TodoResponse
)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    todo = crud.get_todo_by_id(db, todo_id)

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo


@app.put(
    "/todos/{todo_id}",
    response_model=TodoResponse
)
def update_todo(
    todo_id: int,
    todo_data: TodoUpdate,
    db: Session = Depends(get_db)
):
    todo = crud.update_todo(
        db,
        todo_id,
        todo_data.title,
        todo_data.completed
    )

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo


@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    todo = crud.delete_todo(db, todo_id)

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {
        "message": f"Todo {todo_id} deleted successfully"
    }