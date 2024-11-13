# FASTAPI SIMPLE
API que contiene un CRUD de usuarios manteniendo la persistencia de los datos en PostgreSQL.

## Iniciar proyecto
1. Asegurate de crear el archivo ``.env`` copiando el ``.env.template``.

2. Luego ejecuta el PostgreSQL a traves de ``docker compose up -d`` (Asegurate de tener corriendo Docker)

3. Instala las dependencias del proyecto con ``pip install -r requirements.txt``

4. Ahora en la raiz del proyecto ejecuta ``python app.py`` para arrancar el servidor.

## cURLs del proyecto

### Obtener usuarios
```bash
curl --location 'localhost:8000/usuarios'
```

### Crear usuario
```bash
curl --location 'localhost:8000/usuarios' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nombre": "nombre_prueba",
    "email": "test@test.cl"
}'
```

### Obtener usuario por ID
```bash
curl --location 'localhost:8000/usuarios/1'
```

### Modificar usuario por ID
```bash
curl --location --request PUT 'localhost:8000/usuarios/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nombre": "nombre_prueba",
    "email": "test@test.cl"
}'
```

### Eliminar usuario por ID
```bash
curl --location --request DELETE 'localhost:8000/usuarios/1'
```