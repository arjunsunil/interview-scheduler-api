FROM python:3.7-alpine
LABEL maintainer="Arjun"

ENV PYTHONUNBUFFRED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/