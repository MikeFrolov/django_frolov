# syntax=docker/dockerfile:1
FROM python:3.9.7-slim-buster

ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY:-AI4HUDpFhmJQWMCYsV3JM5np3hVRCeQ3}

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN mkdir db
VOLUME db-vol
RUN python3 manage.py migrate

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["python3", "manage.py"]