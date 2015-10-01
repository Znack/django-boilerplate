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
from project.exceptions import ProjectBaseDirectoryVariableException
from django.utils.translation import ugettext_lazy as _

# base repo folder, here stored virtualenv files, manage.py etc
try:
    BASE_DIR = os.environ['PROJECT_PATH']
except KeyError as error:
    raise ProjectBaseDirectoryVariableException(
        "You have no set env variable PROJECT_PATH, it should store a reference to project directory. "
        "Maybe you haven't used the manage.py file for launch project? "
        "Or set PROJECT_PATH manually, it must contain absolute path to project main directory with manage.py file."
    )

# folder with collected static files, ready to download by client apps
PUBLIC_ROOT = os.path.join(BASE_DIR, "public")

# folder with main django project which contains settings, urls and applications package
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

sys.path.append(os.path.join(PROJECT_ROOT, 'applications'))


# SECURITY WARNING: keep the secret key used in production secret!


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
)


ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'





