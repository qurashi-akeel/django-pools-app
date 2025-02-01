## Docs tutorials

1. [Write Django App Part 1](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
1. [Write Django App Part 2](https://docs.djangoproject.com/en/5.1/intro/tutorial02/)

## Setup:

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

6. A project may contain multiple apps:

```bash
python manage.py startapp polls
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
