FROM python:3.12.2-bullseye

RUN pip install --upgrade pip && \
    pip install ag2 beautifulsoup4