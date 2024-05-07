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

# API Endpoints

## Vendors

- **List/Create Vendors**
  - URL: `/vendors/`
  - Method: `GET` (List), `POST` (Create)
  - View: `VendorListCreateView`

- **Retrieve/Update/Delete Vendor**
  - URL: `/vendors/<int:pk>/`
  - Method: `GET` (Retrieve), `PUT/PATCH` (Update), `DELETE` (Delete)
  - View: `VendorRetrieveUpdateDeleteView`

- **View Vendor Performance Metrics**
  - URL: `/vendors/<int:pk>/performance/`
  - Method: `GET`
  - View: `VendorPerformanceView`

## Purchase Orders

- **List/Create Purchase Orders**
  - URL: `/purchase_orders/`
  - Method: `GET` (List), `POST` (Create)
  - View: `PurchaseOrderListCreateView`

- **Retrieve/Update/Delete Purchase Order**
  - URL: `/purchase_orders/<int:pk>/`
  - Method: `GET` (Retrieve), `PUT/PATCH` (Update), `DELETE` (Delete)
  - View: `PurchaseOrderRetrieveUpdateDeleteView`

- **Acknowledge and Update Purchase Order**
  - URL: `/purchase_orders/<int:pk>/acknowledge/`
  - Method: `PUT`
  - View: `AcknowledgeUpdateView`

---

## Access Django Admin:
Open the Django admin at http://127.0.0.1:8000/admin/ and log in using the superuser credentials. 

