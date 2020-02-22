Dealership Portal Project

create the project directory 

```bash
mkdir Dealership
cd Dealership
```

Set enviromental environment 

```bash
python3 -m venv venv
source venv/bin/activate
```

Clone the repository to your local machine:
```bash
git clone https://github.com/AshirogiMaxx/Dealership-Portal-Project.git
```

Install the reqirements 
```bash
pip install requests
pip install Django=2.2.7
pip install djangorestframework
```

Create the database
```bash
manage.py makemigrations series
manage.py migrate  
```

Create admin user and input username, email and password
```bash
python manage.py createsuperuser
```

Start the Django server
```bash
python manage.py runserver
```

Access the project path at **http://127.0.0.1::8000/v1/**

Access the Django Administration page at: **http://127.0.0.1:8000/admin/** and type in the admin user and password


