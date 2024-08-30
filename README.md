# Installing Django
pip install Django

# Creating new project
Django-admin startproject School

# Installing MySQL 
pip install django mysqlclient

# Creating Application
python manage.py startapp students
python manage.py startapp lecturers
python manage.py startapp courses
python manage.py startapp grades
python manage.py startapp attendance

# Making migrations
python manage.py makemigration

# Migrating
python manage.py migrate
