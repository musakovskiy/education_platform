#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

superuser_password="3151"
python manage.py createsuperuser --username=sasha --email=sasha@gmail.com --noinput
