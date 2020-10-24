FROM python:3.7

ENV HOME /opt/chat
RUN mkdir $HOME
WORKDIR $HOME

RUN python3 -m pip install --upgrade pip

COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .