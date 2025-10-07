import os
import json
import pytest
from fastapi.testclient import TestClient
from main import app, DATA_FILE

client = TestClient(app)

# 🧼 Esta función se ejecuta antes de cada prueba
@pytest.fixture(autouse=True)
def limpiar_archivo_json():
    # Reinicia el archivo con una lista vacía
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# 🧪 Prueba: crear una tarea nueva
def test_create_task():
    response = client.post("/tasks", json={
        "id": 1,
        "title": "Aprender FastAPI",
        "description": "Estudiar documentación oficial",
        "completed": False
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Aprender FastAPI"

# 🧪 Prueba: obtener todas las tareas
def test_get_tasks():
    # Primero creamos una tarea
    client.post("/tasks", json={
        "id": 2,
        "title": "Leer libros",
        "description": "Python avanzado",
        "completed": False
    })
    # Luego la consultamos
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 1

# 🧪 Prueba: obtener una tarea por ID
def test_get_task_by_id():
    client.post("/tasks", json={
        "id": 3,
        "title": "Practicar pytest",
        "description": "Escribir pruebas unitarias",
        "completed": False
    })
    response = client.get("/tasks/3")
    assert response.status_code == 200
    assert response.json()["id"] == 3

# 🧪 Prueba: actualizar una tarea
def test_update_task():
    client.post("/tasks", json={
        "id": 4,
        "title": "Tarea original",
        "description": "Sin cambios",
        "completed": False
    })
    response = client.put("/tasks/4", json={
        "id": 4,
        "title": "Tarea actualizada",
        "description": "Con cambios",
        "completed": True
    })
    assert response.status_code == 200
    assert response.json()["completed"] is True

# 🧪 Prueba: eliminar una tarea
def test_delete_task():
    client.post("/tasks", json={
        "id": 5,
        "title": "Eliminar esto",
        "description": "Prueba de borrado",
        "completed": False
    })
    response = client.delete("/tasks/5")
    assert response.status_code == 200
    assert response.json()["id"] == 5
