#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

python manage.py check_db_connection
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :8000 --workers 4 --master --enable-threads --module app.wsgi

