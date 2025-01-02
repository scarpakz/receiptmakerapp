# Basic PDF receipt generator
This project uses ```fpdf``` package for PDF creation/manipulation. I am using a package in Python called ```jazzmin``` for Django admin UI. See this link - ```https://django-jazzmin.readthedocs.io/``` for more information

## Setup

Install python version 3 in your machine and ```pipenv``` for Django environment. When done, run the command ```pipenv shell``` to activate environment and run ```pipenv install``` for the package dependencies. 

### Pipfile (For your reference)
```Pipfile
[packages]
django = "*"
fpdf = "*"
django-jazzmin = "*"
```

Run ```python manage.py migrate``` and ```python manage.py runserver```. You will see the following if it's working:
```commandline
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 02, 2025 - 17:49:12
Django version 5.1.4, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
To access the Django admin, you need to create a superuser. Run the command, ```python manage.py createsuperuser```. Enter the required information of your choice and access the admin in your browser - ```http://127.0.0.1:8000/admin```.


