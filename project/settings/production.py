# -*- coding: utf-8 -*-
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["127.0.0.1:8000"]  # must specify domain for production

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

WEB_SOCKET_ADDRESS = 'http://127.0.0.1:8888/sockets'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

