Below are the Python scripts for the requested items. The server is built using FastAPI, and the client interacts with it using the `requests` library. Additionally, unit tests are included with and without mocks.

---

## 1. FastAPI Server for To-Do List Management

```python
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
```

---

## 2. Client Script to Use the Server

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

def get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    return response.json()

def create_todo(todo):
    response = requests.post(f"{BASE_URL}/todos", json=todo)
    return response.json()

def update_todo(todo_id, updated_todo):
    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=updated_todo)
    return response.json()

def delete_todo(todo_id):
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    return response.json()

if __name__ == "__main__":
    # Example usage of the client
    new_todo = {"id": 1, "title": "Buy groceries", "description": "Milk, Eggs, Bread", "completed": False}
    print("Creating To-Do:", create_todo(new_todo))

    print("Getting To-Dos:", get_todos())

    updated_todo = {"id": 1, "title": "Buy groceries and fruits", "description": "Milk, Eggs, Bread, Apples", "completed": False}
    print("Updating To-Do:", update_todo(1, updated_todo))

    print("Getting To-Dos:", get_todos())

    print("Deleting To-Do:", delete_todo(1))

    print("Getting To-Dos:", get_todos())
```

---

## 3. Unit Test Script to Test API

```python
import unittest
from fastapi.testclient import TestClient
from server import app  # Import your FastAPI app

class TestTodoAPI(unittest.TestCase):
    
    def setUp(self):
        self.client = TestClient(app)
    
    def test_create_and_get_todos(self):
        # Create a new to-do item
        new_todo = {"id": 1, "title": "Test Task", "description": "Test Description", "completed": False}
        response = self.client.post("/todos", json=new_todo)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), new_todo)

        # Get all to-dos
        response = self.client.get("/todos")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_update_todo(self):
        # Create a new to-do item
        new_todo = {"id": 2, "title": "Another Task", "description": "Another Description", "completed": False}
        self.client.post("/todos", json=new_todo)

        # Update the to-do item
        updated_todo = {"id": 2, "title": "Updated Task", "description": "Updated Description", "completed": True}
        response = self.client.put("/todos/2", json=updated_todo)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), updated_todo)

    def test_delete_todo(self):
        # Create a new to-do item
        new_todo = {"id": 3, "title": "Task to Delete", "description": None, "completed": False}
        self.client.post("/todos", json=new_todo)

        # Delete the to-do item
        response = self.client.delete("/todos/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Todo deleted successfully"})

if __name__ == "__main__":
    unittest.main()
```

---

## 4. Unit Test with Mocking the API

```python
import unittest
from unittest.mock import patch
import requests

class TestTodoClientWithMock(unittest.TestCase):

    @patch("requests.get")
    def test_get_todos(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1, "title": "Mock Task", "description": None, "completed": False}]
        
        from client import get_todos
        todos = get_todos()
        
        mock_get.assert_called_once_with("http://127.0.0.1:8000/todos")
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]["title"], "Mock Task")

if __name__ == "__main__":
    unittest.main()
```

---

### How to Run These Scripts:
1. Save the server code as `server.py`, and run it using `uvicorn server:app --reload`.
2. Save the client code as `client.py`, and execute it to interact with the server.
3. Save the unit test scripts as `test_server.py` and `test_client_mock.py`, then run them using `python -m unittest`.
