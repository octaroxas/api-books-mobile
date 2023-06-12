FROM python:3.11.4

WORKDIR /code/
COPY . .

RUN apt-get update -y
RUN apt-get install g++ -y
RUN pip install -r requirements.txt
