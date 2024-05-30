# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10.12
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


RUN useradd -m -u 1000 user

USER user

ENV HOME=/home/user \
    PYTHONPATH=$HOME/app \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1\
    GRADIO_ALLOW_FLAGGING=never \
    GRADIO_NUM_PORTS=1 \
    GRADIO_SERVER_NAME=0.0.0.0 \
    OLLAMA_BASE_URL=http://ollama:11434\
    GRADIO_THEME=huggingface \
    SYSTEM=spaces

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

EXPOSE 7860

CMD python app.py