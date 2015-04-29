# -*- coding: utf-8 -*-

##################################################################
# TEMPLATE OF LOCAL SETTINGS FILE
# Real file with local settings should have a name:
# local.py
##################################################################

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'turkmen-network',                 # Or path to database file if using sqlite3.
        'USER': '',                        # Not used with sqlite3.
        'PASSWORD': '',                     # Not used with sqlite3.
        'HOST': '',                            # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',
    }
}
SECRET_KEY = 'CREATE UNIQUE AND VERY COMPLEX SECRET KEY'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'xxx@gmail.com'
EMAIL_HOST_PASSWORD = ''