FROM python:3.12-slim AS builder

WORKDIR /app

COPY pyproject.toml poetry.lock LICENSE ./

RUN python3 -m pip install poetry && \
    poetry config virtualenvs.path ./.venv && \
    poetry install

FROM python:3.12-alpine

LABEL org.opencontainers.image.authors="rtav3d@gmail.com"

WORKDIR /app

COPY --from=builder /app/.venv .

COPY . .

ENV PYTHONPATH=/app/.venv

RUN addgroup -S docker && adduser docker -S docker -G docker && \
    chown -R docker:docker /app

USER docker

EXPOSE 8095

CMD ["gunicorn", "wsgi:app", "-c", "gunicorn_conf.py"]
