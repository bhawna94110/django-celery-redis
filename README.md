Django E-commerce.
       

It is an E-commerce system built in Django. It contains all the essentials for adding products, delete and update in cart.
About this Project:
It is an E-commerce system built in Django. It contains all the essentials for adding products, delete and update in cart.

The repository is a start point for most of my professional projects; for this, I'm using as a part of my portfolio, feel free to use wherever you want. I'll be happy if you provide any feedback or code improvements or suggestions.

Connect with me at:

       

📫 How to reach me: bhawnarajput94110@gmail.com



Some technical information:
Django - 3.1.1
Django Allauth - 0.42.0
Django Crispy Forms - 1.9.2
Django Environ - 0.4.5
Stripe - 2.51.0
To Install:
Cloning the Repository:

$ git clone https://github.com/bhawna94110/django-celery-redis.git

$ cd storefront3

Installing the environment control:

$ pip install virtu]alenv

$ virtualenv env

Activating the environment:

on Windows:

env\Scripts\activate

on Mac OS / Linux:

$ source env/bin/activate

Installing dependencies:

$ pip install -r requirements.txt

Create a .env file on ecom folder (/ecom/.env) setting all requirements without using space after "=".

Copy and paste on our .env file:

DEBUG=
SECRET_KEY=
DEFAULT_FROM_EMAIL=
NOTIFY_EMAIL=
PAYPAL_SANDBOX_CLIENT_ID=
PAYPAL_SANDBOX_SECRET_KEY=
PAYPAL_LIVE_CLIENT_ID=
PAYPAL_LIVE_SECRET_KEY=
STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=

Last commands to start:

$ python manage.py makemigrations

$ python manage.py migrate

Create a super user:

$ python manage.py createsuperuser admin-name

Finishing running server:

$ python manage.py runserver
   
Thank you!
