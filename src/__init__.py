#!/usr/bin/env python

from flask import Flask, g, jsonify
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api

# configuration
# DEBUG = True
SECRET_KEY = '6C68D2BD65CE5D6740CE71F302ECE364148311B6'

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)
auth = HTTPBasicAuth()

# local imports
from src.resources import *


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.filter_by_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.filter_by_userpass(username_or_token, password)
        if not user:
            return False
    g.user = user[0]
    return True


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"code": 404, "error": "Not found."}), 404


@app.errorhandler(401)
def unauthorized(e):
    # return 403 instead of 401 to prevent browsers from displaying the default
    return jsonify({"code": 403, "error": "You are unauthorized to make this request."}), 403


@app.route('/')
def homepage():
    return 'Homepage'

api.add_resource(Lunches, '/lunches', endpoint='lunches')
api.add_resource(Lunch, '/lunches/<dt>', endpoint='lunch')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
