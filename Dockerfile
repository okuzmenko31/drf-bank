FROM python:3.11

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /drf-bank/app

COPY req.txt /drf-bank/app/req.txt
RUN pip install -r /drf-bank/app/req.txt
COPY . .