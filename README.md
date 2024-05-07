# DJANGO REST FRAMEWORK API SETUP

This repository contains a Django project with a RESTful API using Django REST Framework.

## Prerequisites

- Python (version 3.x recommended)
- Django
- Django REST Framework

# Setup Instructions

## Create a Virtual Environment:
- pip install virtualenvwrapper-win
- mkvirualenv environmentname

## Install Dependencies:
- pip install django
- pip install djangorestframework

## Set up a new project with a single application
- django-admin startproject vendor                 
- cd vendor
- django-admin startapp vendor_app              

## Database migration                    
- python manage.py makemigrations      
- python manage.py migrate

## Superuser creation 
- python manage.py createsuperuser

## Running the server
- python manage.py runserver

## Access Django Admin:
Open the Django admin at http://127.0.0.1:8000/admin/ and log in using the superuser credentials. 

