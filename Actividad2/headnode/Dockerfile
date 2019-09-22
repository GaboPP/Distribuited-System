FROM ubuntu:latest

# # Use an official Python runtime as a parent image
# FROM python:3.7-slim

#mantenerdor Mantainer fue deprecado
LABEL Gabriel Astorga “gabriel.astorga@sansano.usm.cl”

# descomentar para primer uso:
RUN apt-get update \
    &&  apt-get -y install iputils-ping \
    &&  apt-get -y install iproute2 \
    &&  apt-get -y install dnsutils \
    &&  apt-get -y install python3 \
    &&  apt-get -y install python3-pip \
    &&  apt-get -y install vim \
    &&  apt-get -y install sqlite3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME headnode

# Run servidor.py when the container launches
CMD ["python3", "-u", "/app/headnode.py"]