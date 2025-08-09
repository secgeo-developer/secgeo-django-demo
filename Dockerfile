FROM python:3.14-rc-slim

RUN apt-get update 

RUN apt-get install python3-dev build-essential -y

RUN pip install --upgrade pip
RUN pip install virtualenv && python3 -m virtualenv /opt/venv 

ENV PATH="/opt/venv/bin:$PATH"

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /srv/app
WORKDIR /srv/app

