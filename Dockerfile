FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /ILead

COPY Pipfile Pipfile.lock /ILead/

RUN pip install pipenv && pipenv install --system

COPY . /ILead/
