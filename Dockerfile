FROM python:3.12-alpine

LABEL org.opencontainers.image.authors="rtav3d@gmail.com"

WORKDIR /app

COPY . .

RUN python3 -m pip install . && \
    addgroup -S docker && adduser docker -S docker -G docker && \
    chown -R docker:docker /app

USER docker

EXPOSE 8095

CMD ["gunicorn", "wsgi:app", "-c", "gunicorn_conf.py"]
