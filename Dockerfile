# the blue print of our software and docker image -> create the docker image of our software
# Python Alpine is a lightweighted version of Python
FROM python:3.8-alpine

# Installing dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install -r /requirements.txt

# Copying the source code to 
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Creating and logging a user
RUN adduser -D user
USER user

# Commands for Docker run
EXPOSE 8000
CMD ["python", "app.py"]