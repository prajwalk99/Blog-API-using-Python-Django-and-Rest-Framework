# Blog API

## Description
A RESTful API for a blog application built with Django and Django REST Framework. This API allows users to perform CRUD operations on blog posts with user authentication and role-based access.

## Features
- User registration and login
- Token-based authentication
- CRUD operations for blog posts
- Role-based access control
- Pagination and filtering of posts

## Technologies Used
- Python 3.x
- Django
- Django REST Framework
- PostgreSQL

## Requirements
- Python 3.x
- PostgreSQL
- Virtual environment (optional but recommended)

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/blog-api.git
cd blog-api

### Step 2: Set Up a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

###Step 3: Install Dependencies
pip install -r requirements.txt


###Step 4: Configure PostgreSQL Database
Create a PostgreSQL database and user:

CREATE DATABASE myblog_db;
CREATE USER myblog_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE myblog_db TO myblog_user;
Update the DATABASES setting in myblog/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myblog_db',
        'USER': 'myblog_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


## Step 5: Run Migrations
py manage.py migrate


###Step 6: Run the Development Server
py manage.py runserver

API Endpoints
Authentication
POST /api/token/: Obtain a JWT token.
POST /api/token/refresh/: Refresh the JWT token.
Blog Posts
GET /api/posts/: List all posts (authenticated users only).
POST /api/posts/: Create a new post (authenticated users only).
GET /api/posts/<id>/: Retrieve a single post by its ID.
PUT /api/posts/<id>/: Update a post (only by the author).
DELETE /api/posts/<id>/: Delete a post (only by the author).

### Running Tests
py manage.py test

###API Documentation###
- SWAGGER (http://localhost:8000/swagger/)

### License
This project is licensed under MIT License

###Acknowledgement###
Django Documentation: http://docs.djangoproject.com/
Django REST Framework: http://www.django-rest-framework.org/