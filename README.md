# Where we will lunch?

This is a basic `REST` service made in `flask` framework.

## Objective

This application will help your team to chose the place to lunch by voting every day.

## Usage

This application runs under docker container, first you need to build this running:

    docker/docker-build.sh

Next, start the application runing the container

    docker/docker-run.sh

Now you are able to call the service, ie. using `curl`.

    curl -v http://localhost/lunches
    *   Trying ::1...
    * connect to ::1 port 80 failed: Connection refused
    *   Trying 127.0.0.1...
    * Connected to localhost (127.0.0.1) port 80 (#0)
    > GET /lunches HTTP/1.1
    > Host: localhost
    > User-Agent: curl/7.47.0
    > Accept: */*
    >
    * HTTP 1.0, assume close after body
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < Content-Length: 114
    < Server: Werkzeug/0.11.4 Python/3.5.1
    < Date: Tue, 15 Mar 2016 01:43:00 GMT
    <
    {
        "lunches": [
            {
                "date": "2016-03-16 00:00:00",
                "place": "Nice restaurant"
            }
        ]
    }
    * Closing connection 0
