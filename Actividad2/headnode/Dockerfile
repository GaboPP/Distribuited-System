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
# RUN mkdir /app

ADD . /app
WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY ./headnode headnode.py ./
# COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 4000
EXPOSE 4001
EXPOSE 4002


# Run headnoder.py when the container launches

# CMD ["python3", "-u", "/app/headnode/headnode.py"]
# RUN "python3 -u /app/headnode/headnode.py"