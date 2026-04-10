# Proyecto FastAPI

# Descripción

Proyecto de una API hecha con FastAPI.
Usando los métodos HTTP o path operations: GET, POST, PUT y DELETE.

# Instalación

1. Primero creamos las carpetas (o directorios) en el cual crearemos el entorno virtual e instalaremos los paquetes.

2. Crear un entorno virtual:
   python3 -m venv venv

3. Activar el entorno virtual:
  source venv/bin/activate

3. Luego instalamos la version standard de FastAPI en el entorno virtual:
    pip install fastapi[standard]

4. Instalar dependencias:
   pip install -r requirements.txt

# Ejecución

Para correr el servidor, en mi caso utilicé dos formas, una más simplificada y la otra más extensa pero podés abrir docs caso contrario con uvicorn:

* uvicorn main:app --reload
* fastapi dev

Luego abrir en el navegador:
http://127.0.0.1:8000/docs

# Endpoints

* GET `/`
  Devuelve un mensaje simple.

* POST `/post`
  Ejemplo de método POST.

* PUT `/put`
  Ejemplo de método PUT.

* DELETE `/delete`
  Ejemplo de método DELETE.

# Notas

Este proyecto es una práctica básica para entender cómo funcionan las APIs con FastAPI.
