FROM python:3.9-alpine3.16

WORKDIR /app/

COPY ./main.py /app/
COPY ./dependencies.py /app/
COPY ./requirements.txt /app/
COPY ./exception/ /app/exception/
COPY ./service/ /app/service/
COPY ./routers /app/routers

RUN pip install -r requirements.txt

CMD uvicorn --host=0.0.0.0 --port 8000 main:app