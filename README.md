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

`python manage.py runserver 0.0.0.0:8080`

App is running in DEBUG mode True, because it is easier way to handle static and media file. This means that you don't need any static file server like apache or nginx to check this app out.

## Create administrator account

As I mentioned at beginning this app is designed to contain only one user in database.
You can go to the register page with adress */register*. Type there your credentials and click button "Create new user account".
If everything goes OK you should be redirected to the home page. 
If you check out *register_view* in *views.py* file you can see that this view will redirect to homne page you when database has more than 0 users. 
This is mechanism prevent from creating another new users and allow only one administrator exists.

<img src="https://raw.githubusercontent.com/aFku/Django-Gallery/master/images/register.PNG" width="240" height="130">

## Log in

To log in go to the login page **/login** and type your credentials. Log in website is unavailable until you create a administrator account. After successful log in web app should redirect you to the menu (**/menu**). From the menu you can logout or change your password, add image, add new group of images called "gallery" and edit this groups. If you are not logged in and you will try to access menu, web app will redirect you to the home page.

<img src="https://raw.githubusercontent.com/aFku/Django-Gallery/master/images/login.PNG" width="240" height="130"> <img src="https://raw.githubusercontent.com/aFku/Django-Gallery/master/images/menu.PNG" width="240" height="130">

## Add new gallery and image

Let's add new gallery for our images. To do this you can use menu or address */menu/addgallery/*. You have to type there name of the gallery and description which will be displayed on a website. After that add new image to our gallery. Image have title, description and belongs to one of the galleries. When image is processed, web app changes its name with *RenamePath* class and *uuid4()* function.

<img src="https://raw.githubusercontent.com/aFku/Django-Gallery/master/images/newgallery.PNG" width="240" height="130"> <img src="https://raw.githubusercontent.com/aFku/Django-Gallery/master/images/addimage.PNG" width="240" height="130">

## Preview

## Gallery site

## Home site



