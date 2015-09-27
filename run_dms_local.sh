#!/usr/bin/env bash

export APP_SETTINGS='project.config.DevelopmentConfig'
export PG_ENV='DubaiDevConfig'


python manage.py runserver --port 8000
# celery -A project.worker.tasks worker --loglevel=info --purge

