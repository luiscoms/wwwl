FROM python:alpine

MAINTAINER Luis Fernando Gomes <dev@luiscoms.com.br>

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8080

# ENTRYPOINT ["python"]
ENV PYTHONDONTWRITEBYTECODE 1

CMD ["./app.py"]
