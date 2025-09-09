# footballshop
indivudual assaigment 2


https://muhammad-rifqi46-footballshop.pbp.cs.ui.ac.id/


Create a new Django project by running the command  django-admin startproject football_shop . this will create the base project with settings.py, urls.py, wsgi.py, and more

Create an application named main by running the python manage.py startapp main , this will create a directory named main with models.py , views.py , urls.py 
Manually create a directory named template and put a main html file

Configure routing in the project to run the main application
1.By adding main in INSTALLED APP at football_shop/settings.py
2.Add a main app url in football_shop/urls.py
3.in the main, create a urls.py file and add urls pattern 

Create a model in the main application named Product with the following mandatory attributes.
1.Create a 'Product' model in main/models.py
2.migrate it

Create a function in views.py to be returned to an HTML template that displays the application name, your name, and your class.Create a function to display info in views.py
in main views.py
from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    context = {
        'app_name': 'Football Shop',
        'student_name': 'Muhammad Rifqi Al Ghani',
        'student_class': 'KKI',
        'products': products,
    }
    return render(request, 'main.html', context)

7.Create the HTML template by creating main.html and then add the codes

8.Deploy it to the pws,then create an admin account to manage adding the conents of the shoes by accesing the django admin

Views.py : a bridge that connects a user request and application response
it will process a HTTP request, sends data to a template and generate a response

Urls.py : routing systems in django, locates which url goes where
it behaves as a routing table that paths to view function in views.py

In football_shop urls.py will be a first entry point of every request to the django project, it will read the urls patterns 
and if reads only '/' it will route to the application part of urls.py

In main urls.py , it will mapped the path to the view in app that is within main views.py

diagram of the relation ship of 
urls.py, views.py, models.py, and the HTML file
![Diagram Alur Django](https://miro.medium.com/v2/resize:fit:720/format:webp/1*8GLGtS0YYD1c8-QQZIshqw.png)
From medium.com

The role of settings.py is the central configuration file for a django project
it defines apps that you use in the project
sets up database django will use isn "DATABASE" segment
Controls debugging and manage the domain the app can run on


Database migrasion
1.Add classes or modify inside models.py
2.Create migration by python manage.py makemigrations
3.Apply the migrations to database python manage.py migrate (Django applies the changes to your database)

Django frame works takes cares most of the hassle of web development by having a lot of built in features and can focues more making and developing the app 





