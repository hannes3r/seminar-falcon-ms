. env/bin/activate
gunicorn --reload main:app
deactivate