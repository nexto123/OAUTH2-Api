# OAuth2 App


[![Build Status](https://travis-ci.org/nexto123/OAUTH2-Api.svg?branch=master)](https://travis-ci.org/nexto123/OAUTH2-Api)


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

[live app here](https://oauth2-user.herokuapp.com/)

*To keep things simple we will assume that the first four parts have been 
implemented & we are starting with our oauth2 processes.*


## Used Extensions for the App Dependencies

 pip is a package-management system used to install and manage software packages written in Python.
 These dependencies are installed to assist some features that might not come with Django. In our app we will use this list:

* allauth - Third party adds-on to the regular Django authentication/user system and has view/forms etc for some administrative tasks.
* Django==2.2 - Python Framework
* Whitenoise - For web app's to serve its own static files
* django-crispy-forms==1.7.2 - Premade form template
* psycopg2==2.8.2 - sycopg2 is a DB API 2.0 compliant PostgreSQL driver
* dj-database-url==0.5.0 - DATABASE_URL environment variable
* gunicorn==19.9.0 - Web Server Gateway Interface 

### Django all-auth setup(oAuth API)

    As we are aiming to only demonstrate the use of a user authentication system 
    we will limit the components of our app to only the navbars and forms.

We will use these components from [all-auth](https://django-allauth.readthedocs.io/en/latest/configuration.html)

* ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS (=True)
* AUTHENTICATION_BACKENDS 
* ACCOUNT_AUTHENTICATION_METHOD = Specifies the login method to use.
* ACCOUNT_EMAIL_REQUIRED = True
* ACCOUNT_USERNAME_REQUIRED = True
* ACCOUNT_ADAPTER (=”allauth.account.adapter.DefaultAccountAdapter”)
* admin.site.login = login_required(admin.site.login)



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

6. Google credentials

    To allow users to log in with their Gmail credentials we need to register our new website with Google. Go to the 
    Google Developers Console and enter the name of your new project. We must grab the Client id & the Secerete Key and voila.
    
7. Update Templates
    
    The last step is to update our templates file. We need to load socialaccount which comes from Allauth. And our named URLs 
    are slightly different as well: we add an account_ in front of the existing logout, signup, 
    login links. Finally we add a provider link for Google.   
    
 ```
     #<!-- templates/home.html -->
    {% load socialaccount %}

```

8. Now try everything out. Go back to the homepage at http://127.0.0.1:8000/. 
You’re probably logged in so click on the “Log out” link.

9. Now navigate to the “Users” section of the admin at http://127.0.0.1:8000/admin and 
we can see both our new user and his/her email address. We can add additional fields to CustomUser;
we can add additional 3rd party logins; and we can override Allauth default templates.

One more thing that’s nice to do is require email confirmation for new accounts. 
Django does not have this capability but Allauth does.


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

 *Lets push the project to our GitHub repo*

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

* Finally let's collectstatic as we will host our static files on whitenoise [whitenoise](http://whitenoise.evans.io/en/stable/).

 To disable static ``heroku config:set DISABLE_COLLECTSTATIC=1``.

* Finally run the code ``git push heroku master``
   
## Versioning

 Git


## Author

Ernest Bruce Brown
   
   