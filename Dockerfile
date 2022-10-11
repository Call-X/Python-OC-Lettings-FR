FROM python:3

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade setuptools
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ARG SECRET_KEY
ARG ALLOWED_HOSTS=[]
ARG DEBUG
ARG PORT=8000

ENV SECRET_KEY=${SECRET_KEY}
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
ENV DEBUG=${DEBUG}

COPY . .

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

