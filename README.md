# LeGourmand

A recipe management web app built with Django.
Users can sign up, log in, create, view, edit, and delete recipes.

---

## Installation Instructions

### 1. Install Python3

Go to [python](https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe)
And follow the instalattion instructions

### 2. Install dependencies

Run the following command inside the folder

```bash
pip install -r requirements.txt
```

### 3. (Optional) Execute database migrations
If you don't want to use the provided detabase
```bash
python manage.py migrate
```

## Running the application

### 1. To run the web app use
```bash
python manage.py runserver
```
You can access the app locally at [localhost:8000](http://localhost:8000/)

There is a default user in the database
| User       | password |
|------------|----------|
| `chef` | `Test123` |

### 2. To run the unit tests
```bash
python manage.py test
```

## Available pages
| URL | Description |
| --- | ----------- |
| `/` | Home page - List all recipes |
| `/signup/` | Sign up page |
| `/login/` | Log in page |
| `/logout/` | Log out |
| `/recipe/add/` | Add a recipe (logged-in users) |
| `/recipe/<id>/` | View a recipe detail |
| `/recipe/<id>/edit/` | Edit a recipe (logged-in users) |
| `/recipe/<id>/delete/` | Delete a recipe (logged-in users) |
