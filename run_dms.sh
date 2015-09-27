#!/usr/bin/env bash

export APP_SETTINGS='project.config.ProductionConfig'
export PG_ENV='ProductionConfig'


python manage.py runserver --port 8000

