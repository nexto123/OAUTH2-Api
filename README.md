# oAuth2 System


[![Build Status](https://travis-ci.org/nexto123/ouath2-api.svg?branch=master)](https://travis-ci.org/nexto123/ouath2-api)


## Introduction

This is a django app which illustrates the use of the oauth2 user authentication
system.


### Prerequisites

I will first define the scope of this project. What we are trying to do here is to build a user authentication system,
utilizing also the oAuth2 protocol as part of our system. Oauth2 is the preferred method of authenticating access to the API
easily and safely. 

Once an application is registered you can use the client ID, client secret and redirect URL in the authorization flow. 
I will highlight the processes we will undergo and offer a bit of insight into them.

#### Project Structure

* Start a basic Django project
* Add an app for the homepage
* Implement a custom user model
* Signup, login, logout
* install django-allauth
* get Google credentials(We will use )
* update templates

*To keep things simple we will assume that the first four parts have 
implemented & we are starting with our oauth2 processes.*


## Used Extensions for App Dependencies

 pip is a package-management system used to install and manage software packages written in Python.
 These dependencies are installed to assist some features that might not come with Django. In our app we will use this list:

* allauth - Third party adds-on to the regular Django authentication/user system and has view/forms etc for some administrative tasks.
* Django==2.2 - Python Framework
* Whitenoise - For web app's to serve its own static files
* django-crispy-forms==1.7.2 - Premade form template
* psycopg2==2.8.2 - sycopg2 is a DB API 2.0 compliant PostgreSQL driver
* dj-database-url==0.5.0 - DATABASE_URL environment variable
* gunicorn==19.9.0 - Web Server Gateway Interface 

### Django all-auth setup

As we are aiming to only demonstrate the use of a user authentication system 
we will extend a navbar from our base file only.

1. ``pip install django django-allauth``

2. 

```
    INSTALLED_APPS = [
    
    # it's very important not to forget adding this line
    'django.contrib.sites', # new
    
     # add these apps after installation
    'allauth',
    'allauth.account', # new
    'allauth.socialaccount', # new
    'allauth.socialaccount.providers.google', # new

    'users',  
]

```
3. in our project file we will add this.
```
    # our_project/settings.py
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )
    
    SITE_ID = 1
    
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False

```
4. In our project URL file we will add these
```
# our_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('app.urls')),
    # Django Admin
    path('admin/', admin.site.urls),
    # User management
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')), # new
]

```
5. ```(venv) $ python manage.py migrate```





## Database setup

Django comes with a lot of features right out of the box, and SQLite database is one of it. But for more sophisticated 
functionality and durability, it becomes necessary to migrate your database to a more grounded one like MySQL or PostgreSQL.
To use Heroku Postgres;

1. First, create an account on [Heroku](www.heroku.com)
2. Within the resources tab search add-ons for Heroku postgres
3. Select and validate and move on to the settings tab.
4. within settings reveal config and copy database URL.
5. Update Database Configuration in settings.py and add your Heroku database_url.
6. Finally, you will perform a migration.
    ``` python manage.py migrate ```
    
 ## Deployment

To deploy our app to a hosting platform like Heroku we'll have to meet these few requirements.

 _*Lets first push the project to our GitHub repo*_

* create a new repository;
* first assign a repository name on GitHub since that's what I'm using.
* write a short description of the site to be uploaded.
* You will either select to initialize your repository with a README.md file. (optional)
* create your repository.
* You will perform a git remote login
* And finally, git push -u origin master.


*lets now push the project to Heroku*

Heroku is a cloud platform that lets you build, deliver, monitor and scale apps.
To deploy to Heroku, there are two critical steps to perform even before your final commit message.
We have the Procfile, runtime.txt file and the requirement.txt files. 
These are critical necessities if you are deploying to Heroku.
To get requirement.txt file input this into your cli.
```
sudo pip3 freeze —local > requirements.txt
```
To get the Procfile file input this into your cli.
```
$ echo web: python app.py > Procfile
```
* Inside your bash enter ``heroku login`` and follow the prompts. Perform ``git add --all`` and `` git commit``.

* Finally let's collectstatic as we will host our static files on whitenoise.
 To disable static ``heroku config:set DISABLE_COLLECTSTATIC=1``.

* Finally run the code ``git push heroku master``
   
## Mail Service

Mailgun.

check out documentation using [mailgun](https://documentation.mailgun.com/en/latest/)


## Versioning

 Git


## Author

Ernest Bruce Brown
   
   