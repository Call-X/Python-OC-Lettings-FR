FROM python:alpine3.16
# ARG SECRET_KEY
# ARG ALLOWED_HOSTS=[]
# ARG DEBUG=True


ENV PORT=8000
ENV SECRET_KEY=$SECRET_KEY
ENV ALLOWED_HOSTS=127.0.0.1
ENV DEBUG=False

# WORKDIR /src

# COPY requirements.txt requirements.txt
# COPY . /src/

# RUN pip install --upgrade setuptools
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN pip3 install -r requirements.txt
# RUN Docker compose up


# ADD . .


# CMD gunicorn oc_lettings_site.wsgi -b 0.0.0.0:$PORT
# CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT 
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "oc_lettings_site.wsgi:application" ]


COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]