FROM python:alpine3.16

ENV PORT=8000
ENV SECRET_KEY=.ENV
ENV ALLOWED_HOSTS=127.0.0.1
ENV DEBUG=False

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT