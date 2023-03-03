#### Stage 1: Build the react application
FROM python:3.11-alpine as build

WORKDIR /app

COPY . ./

RUN pip3 install -r requirements.txt && python3 manage.py migrate

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
