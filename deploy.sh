#!/bin/sh

# Prefer python from virtualenv
PYTHON=`which python`
test -x ./.env/bin/python && PYTHON=./.env/bin/python
echo "Selected $PYTHON executable"

find ./project -name '*.pyc' -delete
echo "Removed all .pyc files"

$PYTHON manage.py collectstatic --noinput
$PYTHON manage.py migrate
$PYTHON manage.py compress

supervisorctl restart turkmen

