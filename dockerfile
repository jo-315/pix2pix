FROM python:3

WORKDIR /usr/src/app

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
 libgl1-mesa-dev \

COPY requirements.txt ./
COPY setup.sh ./

RUN pip install -r requirements.txt

RUN sh ./setup.sh