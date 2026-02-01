FROM python:3.12.12-slim-trixie AS python-base

ENV PYTHONBUFFERED=1 \
    PYTHONWRITEBYTECODE=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
    && apt-get install --no-install-recommends -y tini \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["tini", "--"]


FROM python-base AS builder-base

RUN apt-get update \
    && apt-get install --no-install-recommends -y curl \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=2.1.1
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python3 - && chmod a+x /opt/poetry/bin/poetry

WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --without dev


FROM python-base AS development

ENV FASTAPI_ENV=development

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

WORKDIR $PYSETUP_PATH

RUN poetry install --with=dev

RUN apt update \
    && apt install --no-install-recommends -y \
        git \
        vim \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN . /opt/pysetup/.venv/bin/activate

RUN git init && git add . && pre-commit install

RUN mkdir -p /app/tests-reports

EXPOSE 8000
