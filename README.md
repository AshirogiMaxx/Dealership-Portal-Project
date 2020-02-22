Dealership Portal Project

create the project directory 

```bash
mkdir Dealership
cd Dealership
```

Clone the repository to your local machine:
```bash
git clone https://github.com/AshirogiMaxx/Dealership-Portal-Project.git
```

Set enviromental environment 

```bash
python3 -m venv venv
source venv/bin/activate
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

Start the Django server
```bash
python manage.py runserver
```

Access the project at 127.0.0.1::8000/v1/

