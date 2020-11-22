FROM python:3.7-alpine
LABEL maintainer="gabrielcandrade01@gmail.com"

RUN mkdir /usr/src/app 
WORKDIR /usr/src/app

RUN apk add --no-cache nginx ca-certificates tzdata git openjdk8-jre \
	gcc linux-headers libffi-dev libpq postgresql-libs postgis jpeg-dev build-base flex bison wget \
    zlib-dev mariadb-connector-c-dev nodejs npm cmake python3-dev unzip postgresql-dev musl-dev\
    && mkdir /run/nginx

ENV LIBRARY_PATH=/lib:/usr/lib
ENV TZ=America/Sao_Paulo

COPY . /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod -R 777 ./

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait