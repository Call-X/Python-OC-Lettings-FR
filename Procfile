web: /bin/sh -c gunicorn\ oc_lettings_site.wsgi:application\ --bind\ 0.0.0.0:\$PORT
heroku ps:scale web=1:eco -a oclettingswebapp
release: python manage.py migrate 