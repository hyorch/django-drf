# Django REST Framework

```bash
python -m venv .venv
pip install requirements.txt
```

Visual Code Studio Extensions   
- python
- Django (Baptiste)
- Django Template
- Django Snippets
- PostgreSQL


## django

1. Create a Project. Create an App
2. Create the model
3. Configure the Serializer
4. Create Function / Class Based view/endpoints
5. Configure URL
6. Run db migrations.


```bash
# Create Project
django-admin startproject firstProject
cd firstProject
python manage.py startapp firstApp
```

firstProject -> settings.py
```py
INSTALLED_APPS = [
    ...
    'rest_framework', # Django REST framework
    'firstApp',  # My first app
]
```

- firstApp -> views.py Create function based view

- firstProject -> urls.py Add URL

- firstApp -> models.py Add Model Class

- firstProject -> setting.py configure Database (Model)

```bash
python manage.py makemigrations
python manage.py migrate
```

Add users

```sql
insert into public."firstApp_employee" values (2,'Pepe',4000.000)
``` 


## PostgreSQL

```sql
CREATE USER username WITH PASSWORD 'password'; 
CREATE DATABASE dbname OWNER username;

dbrest=# create user flight_usr with password 'vuelavuelavuela';
CREATE ROLE
dbrest=# CREATE DATABASE flightdb OWNER flight_usr;
CREATE DATABASE
```