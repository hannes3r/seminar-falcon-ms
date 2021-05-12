#!/bin/sh
. env/bin/activate
gunicorn --reload main:app --bind=0.0.0.0:7373
deactivate
