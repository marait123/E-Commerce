# Base Image
FROM python:3.7

# set default environment variables
ENV PYTHONUNBUFFERED 1

# create and set working directory
WORKDIR /app

# Add current directory code to working directory
ADD . /app

# required
COPY ./requirements.txt /app/requirements.txt

#install the requirements
RUN pip install -r requirements.txt

COPY . /app

RUN echo 'hi'