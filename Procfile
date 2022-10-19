web: gunicorn oc_lettings_site.wsgi:application --log-file --log-level debug
heroku ps:scale web=1
release: python manage.py migrate 