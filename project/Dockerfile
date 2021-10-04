# Pull official base image
FROM python:3.9.6-slim-buster

# set working directory
WORKDIR /usr/src/app

# set env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 11

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql\
    && apt-get clean

# install python deps
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]