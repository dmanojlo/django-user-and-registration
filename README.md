# django-user-and-registration
Django user and registration practice. In order to work properly you have to set two groups(admin, customer) in django administration page when you create super user and add super user to admin group.

## Running the project locally

Clone the repository to your local machine:

```bash
git clone https://github.com/dmanojlo/django-user-and-registration.git
```

Create your own virtual environment
```bash
py -m venv project-name
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create new superuser
```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```



The project will be available at **127.0.0.1:8000**.

