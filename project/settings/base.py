"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

# folder with main django project which contains settings, urls and applications package
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# base repo folder, here stored virtualenv files, manage.py etc
BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))

# folder with collected static files, ready to download by client apps
PUBLIC_ROOT = os.path.join(BASE_DIR, "public")

sys.path.append(os.path.join(PROJECT_ROOT, 'applications'))


ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

