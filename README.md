Open Technology Radio (OTR) is a community based project that aims to build community around open technologies and radio.

##INSTALLATION:
OTR is a Django application, and thus only works with Django projects. Starting your own OTR project requires python-2.7 or higher and Django-1.8 or higher. Once you have these dependencies met, open a terminal and enter:

###*cd projectparentdir && django-admin startproject otrproject*

These commands will create a new Django project called "otrproject" in the project's parent directory.
Once you've created the project, simply drag the original OTR folder into the "otrproject" folder. Then, open the settings.py file located in your project's "otrproject" folder. In the list called "INSTALLED_APPS", add the following line:

###*'otr',*

This will add the OTR app to your project. Now, all that's left to do is migrate the database. You can do this by running these commands inside the "otrproject" directory:

###*python manage.py makemigrations otr && python manage.py migrate*

Congratulations! You're ready to run OTR! You can now add shows and other media through the Django admin panel, which is accessible by starting a local server:

###*python manage.py runserver*

If you need assistance, check out the freenode IRC #otr or review Django's documentation.

##The authors of this software are:
Tristan Damron
(If you worked on the project's code, add your name here!)

