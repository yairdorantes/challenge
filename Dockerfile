# Dockerfile

FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /task_manager

COPY requirements.txt /task_manager/
RUN pip install -r requirements.txt

COPY . /task_manager/
