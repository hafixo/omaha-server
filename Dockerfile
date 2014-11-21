FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python-pip python-lxml python-psycopg2 uwsgi supervisor
RUN apt-get install -y uwsgi-plugin-python
RUN apt-get clean

ADD . /srv/omaha
COPY ./conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /srv/omaha

RUN pip install paver --use-mirrors
RUN pip install -r requirements.txt --use-mirrors

EXPOSE 9090
ENTRYPOINT ["paver", "docker_run"]