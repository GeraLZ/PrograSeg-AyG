#!/bin/bash

sleep 15

su -c 'python3 -u manage.py makemigrations' limitado
su -c 'python3 -u manage.py migrate' limitado

su -c 'gunicorn --bind :8000 monitor.wsgi:application --reload' limitado