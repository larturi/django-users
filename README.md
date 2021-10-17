# Empleados App
Usuarios App Django

# Get Started:

Instalar dependencias:
```
pipenv install
```

Crear el .env
```
cp .env.dist .env

# Modificar los valores si es necesario
```

Levantar Postgres con Docker
```
docker-compose up
```

Crear migraciones:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Ejecutar servidor local
```
python manage.py runserver
```

##### Made with ❤️ by Leandro Arturi
