from datetime import date
from flask import request, g
from flask.ext.restful import fields, inputs, marshal, marshal_with, Resource
from flask.ext.httpauth import HTTPBasicAuth

# local imports
from src import auth

__all__ = ['Lunch', 'Lunches']

# parser = reqparse.RequestParser()
# Look only in the POST body
# parser.add_argument('date', location='json')

resource_fields = {
    # 'date': fields.DateTime(dt_format='iso8601'),
    'date': fields.String,
    'place': fields.String
    # , 'uri': fields.Url('lunch_ep')
}

LUNCHES = [
    {
        'date': inputs.date('2016-03-16'),
        'place': 'Nice place'
    }
]


class Lunch(Resource):
    decorators = [auth.login_required]

    def get(self, dt):
        try:
            dt = inputs.date(dt)
        except ValueError as e:
            return None, 404

        lunches = [lunch for lunch in LUNCHES if lunch['date'] == dt]
        if len(lunches):
            return marshal(lunches[0], resource_fields, 'lunch')

        return None, 204


class Lunches(Resource):
    decorators = [auth.login_required]

    def validate(self, data):
        if 'date' in data:
            data['date'] = inputs.date(data['date'])

        return marshal(data, resource_fields)

    def addLunch(self, lunch):
        lunches = [l for l in LUNCHES if l['date'] == lunch['date']]
        if lunches:
            raise Exception('Lunch already exists')

        LUNCHES.append(lunch)

    @marshal_with(resource_fields, 'lunches')
    def get(self):
        return LUNCHES

    def post(self):
        ret = {'lunch': None}
        try:
            ret['lunch'] = self.validate(request.get_json(force=True))
            self.addLunch(ret['lunch'])
        except Exception as e:
            return None, 404

        return ret, 201
