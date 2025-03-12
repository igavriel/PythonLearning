from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# To-Do Item Model
class TodoItem(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

# In-memory database
todo_list: List[TodoItem] = []

@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return todo_list

@app.post("/todos", response_model=TodoItem)
def create_todo(todo: TodoItem):
    for item in todo_list:
        if item.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    todo_list.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, updated_todo: TodoItem):
    for index, item in enumerate(todo_list):
        if item.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, item in enumerate(todo_list):
        if item.id == todo_id:
            del todo_list[index]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
