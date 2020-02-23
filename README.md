#Dealership Portal Project


[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2.7-brightgreen.svg)](https://djangoproject.com)

Make sure you have installed python3.7 on your machine can be downloaded from:

https://www.python.org/downloads/release/python-370/

Set environment 

```bash
python3 -m venv venv
source venv/bin/activate
```

Clone the repository to your local machine:
```bash
git clone https://github.com/AshirogiMaxx/Dealership-Portal-Project.git
```

Access the project directory 

```bash
cd /Dealership-Portal-Project
```

Install the reqirements 
```bash
pip install Django==2.2.7
pip install djangorestframework
```

Create the database
```bash
python manage.py makemigrations
python manage.py migrate
```

Create admin user and input username, email and password
```bash
python manage.py createsuperuser
```

Start the Django server
```bash
python manage.py runserver
```

Access the project path at **http://127.0.0.1:8000/v1/**

Access the Django Administration page at: **http://127.0.0.1:8000/admin/** and type in the admin user and password

Access the Django Rest framework API endpoint **http://127.0.0.1:8000/v1/portal/vehicles**


