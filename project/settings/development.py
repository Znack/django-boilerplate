# -*- coding: utf-8 -*-
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]  # must specify domain for production

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'turkmen-network',                 # Or path to database file if using sqlite3.
        'USER': '',                        # Not used with sqlite3.
        'PASSWORD': '',                     # Not used with sqlite3.
        'HOST': '',                            # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',

        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
        },
    }
}
API_KEY = 'huBlW0v-HHC1fpo931HBFhAsBQMGrNO9'

WEB_SOCKET_ADDRESS = 'http://127.0.0.1:8888/sockets'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

