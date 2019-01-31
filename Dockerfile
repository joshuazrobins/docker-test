FROM python:3

WORKDIR /usr/src/app

COPY main.py requirements.txt ./
# COPY . .

RUN pip install -r requirements.txt
