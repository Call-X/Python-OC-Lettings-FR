FROM python:3.9.9-slim-buster
ARG secret_key
ENV SECRET_KEY=$secret_key


WORKDIR /app

COPY . .

COPY requirements.txt requirements.txt

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]