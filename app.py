#!/usr/bin/env python

from flask import Flask, jsonify
from flask.ext.restful import Api
# local imports
from resources import *

# configuration
# DEBUG = True
SECRET_KEY = '6C68D2BD65CE5D6740CE71F302ECE364148311B6'

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)


@app.errorhandler(404)
def page_not_found():
    return jsonify({"code": 404, "error": "Not found."}), 404


@app.errorhandler(401)
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    return jsonify({"code": 403, "error": "You are unauthorized to make this request."}), 403


@app.route('/')
def homepage():
    return 'Homepage'

api.add_resource(Lunches, '/lunches', endpoint='lunches')
api.add_resource(Lunch, '/lunches/<dt>', endpoint='lunch')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
