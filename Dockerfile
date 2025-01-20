FROM alpine:3.16

LABEL stage="gobuilder" org.opencontainers.image.authors=rtav3d@gmail.com

COPY /flaskr /app

RUN apk add --update --no-cache python3 py3-pip \
    && ln -sf python3 /usr/bin/python \
    && pip install -r /app/requirements.txt \
    && addgroup -S docker && adduser docker -S docker -G docker \
    && chown -R docker:docker /app

USER docker

WORKDIR /app

EXPOSE 8095

CMD ["gunicorn", "wsgi:app", "-c", "gunicorn_conf.py"]
