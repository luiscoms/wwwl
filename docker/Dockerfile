FROM python:alpine

MAINTAINER Luis Fernando Gomes <dev@luiscoms.com.br>

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 80

# ENTRYPOINT ["python"]

CMD ["./start.py"]
