#!/bin/sh

# Prefer python from virtualenv
PYTHON=`which python`
test -x ./.env/bin/python && PYTHON=./.env/bin/python
echo "Selected $PYTHON executable"

echo "Removing all .pyc files..."
find ./project -name '*.pyc' -delete

$PYTHON manage.py collectstatic --noinput
$PYTHON manage.py migrate
# $PYTHON manage.py compress

supervisorctl restart PROJECT_NAME

