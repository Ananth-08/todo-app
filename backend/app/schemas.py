from pydantic import BaseModel, Field, ConfigDict


class TodoCreate(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=200
    )
    completed: bool = False


class TodoUpdate(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=200
    )
    completed: bool


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

    model_config = ConfigDict(
        from_attributes=True
    )