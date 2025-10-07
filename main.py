from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# 📦 Modelo de datos para una tarea
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

# 📂 Ruta del archivo JSON
DATA_FILE = "tasks.json"

# 📥 Cargar tareas desde el archivo
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# 📤 Guardar tareas en el archivo
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# 🔍 Obtener todas las tareas
@app.get("/tasks")
def get_tasks():
    return load_tasks()

# 🔍 Obtener una tarea por ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# ➕ Crear una nueva tarea
@app.post("/tasks")
def create_task(task: Task):
    tasks = load_tasks()
    if any(t["id"] == task.id for t in tasks):
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks.append(task.dict())
    save_tasks(tasks)
    return task

# ✏️ Actualizar una tarea existente
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[i] = updated_task.dict()
            save_tasks(tasks)
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# 🗑️ Eliminar una tarea
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(i)
            save_tasks(tasks)
            return deleted
    raise HTTPException(status_code=404, detail="Task not found")
