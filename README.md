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

    $ curl -v -u 'hungryemployee:iamhungry' http://localhost/token
    *   Trying 127.0.0.1...
    * Connected to localhost (127.0.0.1) port 80 (#0)
    * Server auth using Basic with user 'hungryemployee'
    > GET /token HTTP/1.1
    > Host: localhost
    > Authorization: Basic aHVuZ3J5ZW1wbG95ZWU6aWFtaHVuZ3J5
    > User-Agent: curl/7.43.0
    > Accept: */*
    > 
    * HTTP 1.0, assume close after body
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < Content-Length: 159
    < Server: Werkzeug/0.11.4 Python/3.5.1
    < Date: Thu, 17 Mar 2016 03:25:41 GMT
    < 
    {
      "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ1ODE4NTE0MSwiZXhwIjoxNDU4MTg1NzQxfQ.eyJpZCI6Imh1bmdyeWVtcGxveWVlIn0.X7Q-fC5jl4Q2F_mjWzwlgu7r84GWOr3uWcWtgZqqiP8"
    * Closing connection 0
    }

    $ curl -vu 'hungryemployeetwo:iamhungry' http://localhost/lunches
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
                "votes": [{
                    "username": "hungryemployeetwo",
                    "place": "Nice place"
                }]
            }
        ]
    }
    * Closing connection 0

### Tests

To run tests use the script

    docker/docker-run.sh

## API

**Lunches**
----

Retrieve a list of lunches

* **URL**

    /lunches

* **Method:**

    `GET`

*  **URL Params**

    **Required:**

    None

    **Optional:**

    None

* **Data Params**

    None

* **Success Response:**
    * **Code:** 200

          **Content:**
```json
{
    "lunches": [
        {
            "date": "2016-03-16 00:00:00",
            "votes": [{
                "username": "hungryemployeetwo",
                "place": "Nice place"
            }]
        }
    ]
}
```

* **Error Response:**
    * **Code:** 403 UNAUTHORIZED

          **Content:** `{ "code": 403, "error" : "You are unauthorized to make this request." }`

* **Sample Call:**

    `curl -u 'hungryemployeetwo:iamhungry' 'http://localhost/lunches'`

**Lunch**
----

Retrieve a lunch by date

* **URL**

    /lunches/<date>

* **Method:**

    `GET`

*  **URL Params**

    **Required:**

    None

    **Optional:**

    None

* **Data Params**

    None

* **Success Response:**
    * **Code:** 200

          **Content:**
```json
{
    "lunch": {
        "date": "2016-03-16 00:00:00",
        "votes": [{
            "username": "hungryemployeetwo",
            "place": "Nice place"
        }]
    }
}
```

* **Error Response:**
    * **Code:** 404 NOTFOUND

          **Content:** `{ "code": 404, "error" : "Not found." }`

    * **Code:** 403 UNAUTHORIZED

          **Content:** `{ "code": 403, "error" : "You are unauthorized to make this request." }`

* **Sample Call:**

    `curl -u 'hungryemployee:iamhungry' 'http://localhost/lunches/2016-03-16'`

**Votes**
----

Vote on a place to lunch

* **URL**

    /lunches/<date>/votes

* **Method:**

    `POST`

*  **URL Params**

    **Required:**

    None

    **Optional:**

    None

* **Data Params**

    `{ "username": "validusername", "place": "Some Place" }`

* **Success Response:**
    * **Code:** 201

          **Content:**
```json
{
    "lunch": {
        "date": "2016-03-16 00:00:00",
        "votes": [{
            "username": "hungryemployeetwo",
            "place": "Nice place"
        }]
    }
}
```

* **Error Response:**
    * **Code:** 400 Bad Request

          **Content:** `{ "code": 400, "error" : "Bad Request" }`

    * **Code:** 403 UNAUTHORIZED

          **Content:** `{ "code": 403, "error" : "You are unauthorized to make this request." }`

* **Sample Call:**

    `curl -X POST -u 'hungryemployee:iamhungry' -d '{ "username": "hungryemployee", "place": "Nice Place" }' 'http://localhost/lunches/2016-03-17/votes'`


**Token**
----

Retrieve an authentication token

* **URL**

    /token

* **Method:**

    `GET`

*  **URL Params**

    **Required:**

    None

    **Optional:**

    None

* **Data Params**

    None

* **Success Response:**
    * **Code:** 200

          **Content:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ1ODE4Njc2NywiZXhwIjoxNDU4MTg3MzY3fQ.eyJpZCI6Imh1bmdyeWVtcGxveWVlIn0.gefFc9LRhZiaKTX0CjTCVVBcz_6AVoItD8cPwjit-W4"
}
```

* **Error Response:**
    * **Code:** 400 Bad Request

          **Content:** `{ "code": 400, "error" : "Bad Request" }`

    * **Code:** 403 UNAUTHORIZED

          **Content:** `{ "code": 403, "error" : "You are unauthorized to make this request." }`

* **Sample Call:**

    `curl -u 'hungryemployee:iamhungry' 'http://localhost/token`

## Highlights

* Container isolation using Docker
* Better code formating using editorconfig

## Improvements

* Frontend site to be client for this API
* Log informations in file