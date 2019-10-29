# -*- coding: utf-8 -*-

LOCAL_APPS = (
    'core',
)

THIRD_PARTY_APPS = (
    'corsheaders',

    'django_filters',

    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',

    'rest_framework',
    'rest_framework.authtoken',

    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

INSTALLED_APPS = THIRD_PARTY_APPS + LOCAL_APPS
