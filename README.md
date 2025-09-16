# footballshop
indivudual assaigment 2


https://muhammad-rifqi46-footballshop.pbp.cs.ui.ac.id/
-I Created the django project by starting making local repository, preparing the dependencies and then the django project with
django-admin startproject 
-I Started making the main application with python manage.py startapp main 
Models.py : file that define the data structure of the application
it will be filled mostly with class and it will django will handle its query

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









Assaigment 3
1.Data delivery is essential, it allows information exchanged beetween the server and clients. Without it  it cannot share resources and
intergrate with other systems.

2.JSON,it feels more similar to phyton code and its indentation
Its compact and easier to write and read for human

3.is_valid() is to prevent invalid data from being saved ensuring consistency
if its method retuns True. Django will know that it is safe
else it will prevoide error to the user

4.csrf_token serves as a protection a protection to csrf attacks
where it will tricks the user to submitting dangerous request via a fake web
and with csrf_token, on each form submission will carries a hidden token that gives proof that the request came from your site



implemented the checklist above step-by-step
1.Created base.html inside the templates/ folder 
2.Added button inside main.html(Add detail, Add)
3.Created the supporting templates html(add_product , product_detail)
4.Hooking it up the XML/Json views and their urls


Postman XML
![XML All Products](screenshots/xml.png)

Postman JSON
![JSON All Products](screenshots/json.png)


Postman XML by ID
![XML All Products](screenshots/xml_by_id1.png)


Postman JSON by ID
![JSON  Product 1](screenshots/json_by_id1.png)

