from sqlalchemy.orm import Session
from app.models import Todo


def get_todos(db: Session, completed: bool | None = None):
    query = db.query(Todo)

    if completed is not None:
        query = query.filter(Todo.completed == completed)

    return query.all()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def create_todo(db: Session, title: str, completed: bool):
    new_todo = Todo(
        title=title,
        completed=completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


def update_todo(
    db: Session,
    todo_id: int,
    title: str,
    completed: bool
):
    todo = get_todo_by_id(db, todo_id)

    if not todo:
        return None

    todo.title = title
    todo.completed = completed

    db.commit()
    db.refresh(todo)

    return todo


def delete_todo(db: Session, todo_id: int):
    todo = get_todo_by_id(db, todo_id)

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return todo