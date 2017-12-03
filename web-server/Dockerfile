FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential curl net-tools vim dnsutils
ADD main.py /main.py
ADD req.txt /req.txt
RUN pip install --upgrade pip
RUN pip install -r /req.txt
RUN pip install requests
