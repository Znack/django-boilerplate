# -*- coding: utf-8 -*-
import os
from logging import config
from .apps import LOCAL_APPS

try:
    from .local import BASE_DIR
except ImportError:
    from .base import BASE_DIR

INFO_LOG_FILE = os.path.join(BASE_DIR, "logs/info.log")
ERROR_LOG_FILE = os.path.join(BASE_DIR, "logs/error.log")
REQUEST_LOG_FILE = os.path.join(BASE_DIR, "logs/request.log")

loggers = {
    app: {
        'level': "INFO",
        'handlers': ['console', 'info.log', 'error.log'],
    } for app in LOCAL_APPS
}
loggers['django.request'] = {
    'level': "ERROR",
    'handlers': ["console", "mail_admins", "request.log"],
}
loggers['django.server'] = {
    'level': "INFO",
    'handlers': ['console'],
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s]%(levelname)-8s%(name)-30s'
                      '%(funcName)-20.20s:%(lineno)-4d | %(message)s',
            'dateformat': '%H:%M:%S',
        },
    },
    'handlers': {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'info.log': {
            'level': 'INFO',
            'formatter': 'verbose',
            'class': 'logging.FileHandler',
            'filename': INFO_LOG_FILE
        },
        'error.log': {
            'level': 'ERROR',
            'formatter': 'verbose',
            'class': 'logging.FileHandler',
            'filename': ERROR_LOG_FILE
        },
        'request.log': {
            'level': 'WARNING',
            'formatter': 'verbose',
            'class': 'logging.FileHandler',
            'filename': REQUEST_LOG_FILE
        }
    },
    'loggers': loggers
}

config.dictConfig(LOGGING)
