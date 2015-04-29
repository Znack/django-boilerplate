# -*- coding: utf-8 -*-
import os
from .base import BASE_DIR

LANGUAGE_CODE = 'en-us'

LOCALE_FOLDERS = [
    {"path":  BASE_DIR, "args": "--ignore=static --ignore=applications"},
    {"path":  os.path.join(BASE_DIR, "applications", "core")},
    {"path":  os.path.join(BASE_DIR, "applications", "friends")},
    {"path":  os.path.join(BASE_DIR, "applications", "profiles")},
    {"path":  os.path.join(BASE_DIR, "applications", "comments")},
    {"path":  os.path.join(BASE_DIR, "applications", "im")},
    {"path":  os.path.join(BASE_DIR, "applications", "notifications")},
    {"path":  os.path.join(BASE_DIR, "applications", "permissions")},
    {"path":  os.path.join(BASE_DIR, "applications", "photos")},
]
LOCALE_PATHS = [path['path'] for path in LOCALE_FOLDERS]