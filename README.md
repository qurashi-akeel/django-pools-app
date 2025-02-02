# Django Pools App

## Contents

1. [Docs Tutorials](#docs-tutorials)
2. [Install Deps](#install-deps)
3. [Initial Setup Instructions](#initial-setup-instructions)
4. [Models, Migrations and DB](#models-migrations-and-db)
5. [Interactive Shell](#interactive-shell)
6. [Change DB](#change-db)
7. [Docker Related](#docker-related)

## Docs tutorials

1. [Write Django App Part 1](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
1. [Write Django App Part 2](https://docs.djangoproject.com/en/5.1/intro/tutorial02/)
1. [Write Django App Part 3](https://docs.djangoproject.com/en/5.1/intro/tutorial03/)

## Install Deps:

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Initial Setup instructions

1. Create virtual env:

```bash
python3 -m venv venv
```

2. Activate virtual env: (using vscode bottom bar):

```bash
source venv/bin/activate
```

3. Install django:

```bash
pip install django
```

4. Create project:

```bash
django-admin startproject core .
```

5. Run server to make sure everything is ok:

```bash
python manage.py runserver
```

6. Migrate existing DB models:

```bash
python manage.py migrate
```

7. A project may contain multiple apps:

```bash
python manage.py startapp polls
```

8. Create the superuser to access admin dashboard:

```bash
python manage.py createsuperuser
```

## Models, Migrations and DB

1. Create models inside the app:

```bash
touch <app>/models.py
```

2. Generate the migrations file:

```bash
python manage.py makemigrations polls
```

3. See the SQL statements:

```bash
python manage.py sqlmigrate polls 0001
```

4. Check the migrations for any issues (before applying to DB):

```bash
python manage.py check;
```

5. Apply migrations

```bash
python manage.py migrate
```

## Interactive Shell:

```bash
python manage.py shell
```

Test Functionality:

```py
from polls.models import Choice, Question

# To get all objects in the Questions table
Question.objects.all()

from django.utils import timezone

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
```

## Change DB

1. Install psycopg2 (or psycopg2-binary) for Postgresql:

```bash
pip install psycopg2-binary
```

2. Start DB server and update the credentials in `settings.py` file:

```py
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pools_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. Apply migrations and Recreate superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run server and enjoy:

```bash
python manage.py runserver
```

## Docker related:

1. List existing volumes:

```bash
docker volume ls
```

2. Remove volume (if necessary):

```bash
docker volume rm <vol_name>
```

3. Stop and Remove any existing container (if necesssary):

```bash
docker stop <container_id>

docker rm -v <container_id>
```

4. Start the container:

```bash
docker compose up -d
```

5.
