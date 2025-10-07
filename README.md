# task-api
Fines educativos

Objetivo
Construir una API RESTful en Python para gestionar tareas (to-do list), con operaciones CRUD (crear, leer, actualizar, eliminar), persistencia en archivo JSON y pruebas unitarias.

1. Endpoints requeridos
Implementa los siguientes endpoints usando FastAPI:

Método  	      Ruta	             Descripción
GET	            /tasks	           Listar todas las tareas
GET         	/tasks/{id}     	Obtener una tarea por ID
POST	         /tasks	           Crear una nueva tarea
PUT          	/tasks/{id}	       Actualizar una tarea existente
DELETE       	/tasks/{id}	       Eliminar una tarea por ID

2. Modelo de datos
cada tarea debe tener:

{
  "id": int,
  "title": str,
  "description": str,
  "completed": bool
}

3. Persistencia
Guarda las tareas en un archivo tasks.json.

Carga el archivo al iniciar la API.

Actualiza el archivo cada vez que se modifica una tarea.

4. Pruebas unitarias
Usa pytest para probar al menos:

Creación de tareas

Lectura de tareas

Actualización y eliminación

5. Documentación
Asegúrate de que la documentación automática de FastAPI esté disponible en /docs.