#!/usr/bin/env bash

export PG_ENV='project.config.DubaiDevConfig'


python manage.py runserver

celery -A project.worker.tasks worker --loglevel=info --purge