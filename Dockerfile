FROM python:3.12-slim AS builder

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry \
    poetry install

FROM python:3.12-slim

LABEL Maintainer="Timur Ramonov"

WORKDIR /app

COPY --from=builder /app/.venv .

COPY . .

RUN addgroup -S docker && adduser docker -S docker -G docker \
    && chown -R docker:docker /app

USER docker

EXPOSE 8095

CMD ["gunicorn", "wsgi:app", "-c", "gunicorn_conf.py"]
