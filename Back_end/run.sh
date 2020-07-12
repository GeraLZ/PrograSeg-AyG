#!/bin/bash
export DJANGO_SETTINGS_MODULE=webServices.settings
sleep 15

su -c 'python3 -u manage.py makemigrations' limitado
su -c 'python3 -u manage.py migrate' limitado
su -c 'python3 crear_usuario.py' limitado
su -c 'gunicorn --bind :8000 webServices.wsgi:application --reload' limitado