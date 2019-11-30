FROM python:2.7

ARG nginx_pre
ARG db
ARG livecheck_interval
ENV NAMESERVER_DB_PATH=${db}
ENV NAMESERVER_NGINX_PRE=${nginx_pre}
ENV NAMESERVER_LIVECHECK_INTERVAL=${livecheck_interval}

RUN mkdir -p /usr/src/app
RUN mkdir -p /external
WORKDIR /usr/src/app

ADD NameServer ./

RUN pip install django djangorestframework markdown django-filter djangorestframework-xml requests

RUN apt-get update && apt-get install -y \
sqlite3 \
--no-install-recommends && rm -rf /var/lib/apt/lists/*

EXPOSE 8800

RUN python manage.py makemigrations

CMD  python manage.py migrate --database $NAMESERVER_DB_PATH && python manage.py runserver 0.0.0.0:8800
