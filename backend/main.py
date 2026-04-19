from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Data model
class Task(BaseModel):
    task: str

# In-memory storage
tasks = []
task_id = 1

@app.get("/")
def home():
    return {"message": "DevBoard API is running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: Task):
    global task_id

    new_task = {
        "id": task_id,
        "task": task.task
    }

    tasks.append(new_task)
    task_id += 1

    return new_task

@app.put("/tasks/{id}")
def update_task(id: int, updated_task: Task):
    for t in tasks:
        if t["id"] == id:
            t["task"] = updated_task.task
            return t

    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for t in tasks:
        if t["id"] == id:
            tasks.remove(t)
            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")