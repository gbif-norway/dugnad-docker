FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev gettext build-essential
WORKDIR /srv/dugnad
ADD ./requirements.txt /srv/dugnad
RUN pip install -r requirements.txt
