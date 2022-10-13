release: python manage.py migrate
web: python manage.py runserver 0.0.0.0:8000
web: gunicorn --bind :$PORT oc_lettings_site.wsgi