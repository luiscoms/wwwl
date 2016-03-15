FROM python:alpine

MAINTAINER Luis Fernando Gomes <dev@luiscoms.com.br>

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
