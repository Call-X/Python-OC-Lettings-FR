FROM python:alpine3.16
# ARG SECRET_KEY
# ARG ALLOWED_HOSTS
# ARG DEBUG
# ENV SECRET_KEY=${SECRET_KEY}
# ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
# ENV DEBUG=${DEBUG}


# WORKDIR /app

# COPY requirements.txt requirements.txt
# COPY . .

# RUN pip install --upgrade setuptools
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN pip3 install -r requirements.txt

# EXPOSE 8000
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
ENV SECRET_KEY=${SECRET_KEY}
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
ENV DEBUG=${DEBUG}
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "oc_lettings_site.wsgi:application"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000

