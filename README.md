# Prueba Técnica

## Descripción

Este proyecto es un microservicio para la gestión de usuarios y tareas, desarrollado utilizando Django, Python, y MySQL. El microservicio expone una API REST para crear y obtener usuarios y tareas.

## Requisitos

- Docker
- Docker Compose
- Puerto 3306 y 8000 disponibles o cambiarlos en docker-compose.yml

## Configuración

1. Construir y levantar los servicios utilizando Docker Compose:

```bash
docker-compose up --build

```

Endpoints de la API

- **POST** http://0.0.0.0:8000/api/users/ - Crear un usuario.
- **GET** http://0.0.0.0:8000/api/users/list/ - Obtener la lista de usuarios.
- **POST** http://0.0.0.0:8000/api/tasks/ - Crear una tarea asignada a un usuario.
- **GET** http://0.0.0.0:8000/api/users/<user_id>/tasks/ - Obtener la lista de tareas de un usuario específico.
