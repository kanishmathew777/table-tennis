#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
sleep 5
DOCKERRUN=1 python manage.py makemigrations
DOCKERRUN=1 python manage.py migrate
exec gunicorn proj_settings.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile logfile