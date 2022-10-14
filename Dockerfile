FROM python:alpine3.16
ARG SECRET_KEY
ARG ALLOWED_HOSTS
ARG DEBUG
ENV SECRET_KEY=${SECRET_KEY}
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
ENV DEBUG=${DEBUG}

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN pip install --upgrade setuptools
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ADD . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", ":8000"]
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3"]
