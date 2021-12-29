# crudapp
Django application to perform CRUD operations

## Run It
* Clone the project:
```
$ git clone https://github.com/FahadulShadhin/crudapp.git
```

* Install required packages:
```
$ pip install -r requirements.txt
```

* Run server:
```
$ python manage.py runserver
```
<p>>> The application should be running at development server 127.0.0.1:8000</p>

* Make migrations to database:
```
$ python manage.py makemigrations
$ python manage.py migrate
```

* Get admin access:
```
$ python manage.py createsuperuser (enter username, email, password)
```
