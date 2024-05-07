from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool

tasks = []

@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
async def get_tasks_by_completion(completed: Optional[bool] = None):
    if completed is not None:
        return [task for task in tasks if task.completed == completed]
    return tasks

@app.delete("/tasks/")
async def delete_all_tasks():
    global tasks
    tasks = []
    return {"message": "All tasks deleted successfully"}

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/tasks/title/{title}", response_model=Task)
async def get_task_by_title(title: str):
    for task in tasks:
        if task.title == title:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task_by_id(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task_by_id(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/title/{title}")
async def delete_task_by_title(title: str):
    for i, task in enumerate(tasks):
        if task.title == title:
            del tasks[i]
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
