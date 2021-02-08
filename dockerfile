FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY setup.sh ./

RUN pip install -r requirements.txt

RUN sh ./setup.sh