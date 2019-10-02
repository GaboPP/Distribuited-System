# FROM ubuntu:latest

# # Use an official Python runtime as a parent image
FROM python:3.7-slim

#mantenerdor Mantainer fue deprecado
LABEL Gabriel Astorga “gabriel.astorga@sansano.usm.cl”

# descomentar para primer uso:
# RUN apt-get -y install python3
#     &&  apt-get update \
#     &&  apt-get -y install python3-pip \
#     &&  apt-get -y install vim
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port available to the world outside this container
EXPOSE 4000

# Define environment variable
ENV NAME client

# Run client.py when the container launches
# RUN python3 -u /app/client/client.py
# CMD ["python3", "-u", "/app/client/client.py"]