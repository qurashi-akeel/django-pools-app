## Docs tutorials

1. [Write Django App Part 1](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)


## Setup instructions

1. Create virtual env:

```bash
python -m venv venv
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
