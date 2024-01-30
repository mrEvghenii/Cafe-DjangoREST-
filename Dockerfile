FROM python:3.10

RUN mkdir "/Cafe_app"

WORKDIR /Cafe_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

WORKDIR cafe_dr

