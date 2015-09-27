#!/usr/bin/env bash


export APP_SETTINGS='project.config.DevelopmentConfig'
export PG_ENV='DubaiDevConfig'
log_file="project/logs/celery_"$(date +"%y_%m")".log"


celery -A project.worker.tasks worker --loglevel=INFO --purge

# celery -A project.worker.tasks worker --loglevel=INFO --logfile=$log_file --purge