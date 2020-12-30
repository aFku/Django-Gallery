# Django-Gallery

This is my first Django project. It is a universal gallery built as web application. 
There is only one user which is also administrator. The user is able to add new images to gallery, edit them, also create and edit new groups of images. 
Each of images has its own preview website where image could be also deleted. There is a menu website with links to almost all admin functions. 
It is available only after successful log in.

## Requirements

*I used this versions to create project*

Python: 3.9

Django: 3.1.4

## Running app

It is recommended to create python virtual environment for this project. It could be done by executing command:

`python -m venv <relative path to directory with new venv>`

File *requirements.txt* contain all necessary dependencies (including Django framework). To install them and update pip  execute command:

`pip install -r <relative path to requirements.txt>`

If you successful installed Django, you need to apply database schemas for models. 
Default database type for Django is sqlite3 which is used. It can be changed in *settings.py* file if you need.
To create schemas navigate to Gallery directory where *manage.py* is located. Then execute command:

`python manage.py makemigrations home_site`

*home_site* is name of Django app. After creating schemas you need to apply them. To do this you have to execute command:

`python manage.py migrate`

Now you can run server with command:

`python manage.py runserver 0.0.0.0:8080 --insecure`

*--insecure* flag is required for static files, unless you put application behind static file server like apache or nginx. 
You can also change DEBUG mode in *settings.py* to True for static files.

## Create administrator account

As I mentioned at beginning this app is designed to contain only one user in database.
You can go to the register page with adress */register*. Type there your credentials and click button "Create new user account".
If everything goes OK you should be redirected to the home page. 
If you check out *register_view* in *views.py* file you can see that this view will redirect to homne page you when database has more than 0 users. 
This is mechanism prevent from creating another new users and allow only one administrator exists.

![Register site screenshot] (https://raw.githubusercontent.com/aFku/Django-Gallery/master/images/register.PNG)
