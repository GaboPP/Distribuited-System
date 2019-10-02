# FROM ubuntu:latest

# # Use an official Python runtime as a parent image
FROM python:3.7-slim

#mantenerdor Mantainer fue deprecado
LABEL Gabriel Astorga “gabriel.astorga@sansano.usm.cl”

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

EXPOSE 4001
EXPOSE 4002

# Define environment variable
ENV NAME datanode

ARG id_datanode
RUN echo $PWD
RUN echo "Oh dang look at that ${id_datanode}"
# Run datanode.py when the container launches
# CMD ["python3", "-u", "/app/datanode/datanode.py", "${id_datanode}"]