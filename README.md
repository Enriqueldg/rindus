# User Administration

A small Django application to manage (CRUD) users and their bank account data (IBAN).


## Getting Started

* Use Python 3.x
* Use PostgreSQL as the database backend
* Administrators should be able to create, read, update and delete users
* Required fields are first name, last name and IBAN. Data should be validated.
* Administrators of the app should authenticate using a Google account
* Restrict manipulation operations on a user to the administrator who created them

### Prerequisites

psycopg

```
pip install psycopg2
```

Django

```
pip install Django
```

Python Social Auth - Django

```
pip install social-auth-app-django
```

### Installing

Preparing the database, creating all the tables accordingly to the application model.

```
python manage.py migrate

```

Running the server for the test.

```
python manage.py runserver
```

## Built With

* [psycopg](http://initd.org/psycopg/) - PostgreSQL adapter
* [Django](https://www.djangoproject.com/) - The web framework used
* [Python Social Auth - Django](https://github.com/python-social-auth/social-app-django) - Library used for auth

## Author

**Enrique Ladrón de Guevara Santaella**
