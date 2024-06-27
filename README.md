# Prueba Técnica

## Requisitos

- Tener Docker y Docker Compose instalados.
- Puertos 3306 y 8000 disponibles para ser utilizados por los contenedores.

## Configuración

1. Clonar el [repositorio](https://github.com/yairdorantes/challenge) del proyecto o descarga la carpeta proporcionada por correo. Luego, navega hasta la carpeta del proyecto.
2. Construir y levantar los servicios utilizando Docker Compose ejecutando el siguiente comando en la terminal, asegurándose de que la terminal esté apuntando a la ruta del proyecto:

_En **caso de ser necesario** agregar **sudo** al comando_

```bash
docker-compose up
```

Este comando creará las imágenes necesarias e iniciará la ejecución del proyecto.

## Acceso a la API

La API está disponible en alguna de las siguientes URLs:

- `http://0.0.0.0:8000` (Linux)
- `http://localhost:8000` (Windows)

Endpoints

- **POST** /api/users/ - Crear un usuario.
- **GET** /api/users/list/ - Obtener la lista de usuarios.
- **POST** /api/tasks/ - Crear una tarea asignada a un usuario.
- **GET** /api/users/<user_id>/tasks/ - Obtener la lista de tareas de un usuario específico.

Notas:

- Puedes utilizar Postman o un navegador web para hacer las solicitudes

- Por fines prácticos, se incluye el archivo .env con sus respectivas variables.
