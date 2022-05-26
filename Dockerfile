FROM python:3.10.4-alpine
LABEL maintainer="GuestReady"

ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements
COPY ./app /app

WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements/dev.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 775 /vol

ENV PATH="/py/bin:$PATH"

USER app

CMD [ "entrypoint.sh" ]