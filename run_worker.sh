#!/usr/bin/env bash


export APP_SETTINGS='project.config.ProductionConfig'
export PG_ENV='ProductionConfig'
log_file="project/logs/celery_"$(date +"%y_%m")".log"

celery -A project.worker.tasks worker --loglevel=INFO --logfile=$log_file --purge