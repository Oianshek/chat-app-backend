FROM python:3.9-slim-buster

RUN mkdir /chat_app

WORKDIR /chat_app

ADD . /chat_app/

RUN pip install -r requirements.txt