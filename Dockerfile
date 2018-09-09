FROM python:3.7.0-alpine3.8
LABEL maintainer="rubens.luiz@gmail.com"

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

WORKDIR /app
ADD src/ .

CMD gunicorn --workers ${APP_WORKERS:-3} --bind 0.0.0.0:8000 wsgi
