# Django Rest Framework Project

This project contains microservices for working with users and tasks.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Suslicke/auth_microservice.git
```

2. Install dependencies in all service:

```bash
pip install -r requirements.txt
```

3. Create the database in all service:

```bash
python manage.py migrate
```

## Running

Start the server:

```bash
python backend/todo/manage.py runserver 8080
python backend/users/manage.py runserver 8000
```

## Authentication

Authentication is required to interact with the user and task microservices. To authenticate, you need to obtain a token.

### Obtaining a Token

To obtain a token, make a POST request to the URL `http://localhost:8000/api/token/`. Include the username (`username`) and password (`password`) in the request body.

In response to this request, you will receive a JSON object containing the access token (`access`) and the refresh token (`refresh`):

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIwOTM1NzA4LCJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSJ9.JhjKgB0SgcSbdCvM0i3qHY85a_K5j5O5yV7QGtW_fCk",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIzNDc2MzA4fQ.nWSYtpIwAQOJqW8EGb0-6I67Sy-npyZgB-YWJ9HsBOs"
}
```

### Using the Token

To use the token, include it in the `Authorization` header of all requests to the microservices.
