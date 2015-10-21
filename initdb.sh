#!/bin/bash
#helper script for model changes and to load fixtures
#next time run migrations! 

rm /home/vagrant/django_cv/django_cv/db.sqlite3
rm -r /home/vagrant/django_cv/django_cv/cv/migrations
python manage.py makemigrations cv
python manage.py migrate
python manage.py loaddata cv/fixtures/initial_data.json
