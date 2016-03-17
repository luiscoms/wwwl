from datetime import date
from flask import request, g
from flask.ext.restful import fields, inputs, marshal, marshal_with, Resource

# local imports
from src import auth
from src.resources.users import USERS

__all__ = ['Lunch', 'Lunches', 'Votes']

resource_fields = {
    # 'date': fields.DateTime(dt_format='iso8601'),
    'date': fields.String,
    'votes': fields.List(fields.Raw)
    # , 'uri': fields.Url('lunch_ep')
}

votes_fields = {
   'username': fields.String,
   'place': fields.String
}

LUNCHES = [
    {
        'date': inputs.date('2016-03-16'),
        'votes': [{
            "username": "hungryemployeetwo",
            "place": "Nice place"
        }]
    }
]


class Lunch(Resource):
    decorators = [auth.login_required]

    @staticmethod
    def update(lunch):
        global LUNCHES

        lunches = list(filter(lambda l: l['date'] != lunch['date'], LUNCHES))
        lunches.append(lunch)
        LUNCHES = lunches

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

    @staticmethod
    def addLunch(lunch):
        lunches = [l for l in LUNCHES if l['date'] == lunch['date']]
        if lunches:
            raise Exception('Lunch already exists')

        LUNCHES.append(lunch)

    @marshal_with(resource_fields, 'lunches')
    def get(self):
        return LUNCHES


class Votes(Resource):
    decorators = [auth.login_required]

    def validate(self, data):
        data = marshal(data, votes_fields)
        if not data['username'] or not data['place']:
            raise Exception('Required parameter missing')

        if data['username'] not in map(lambda u: u['username'], USERS):
            raise Exception('Invalid username')

        return data

    def validateDuplicatedVote(self, vote, votes):
        assert len(list(filter(lambda v: vote['username'] == v['username'], votes))) == 0

    def post(self, dt):
        try:
            dt = inputs.date(dt)
            vote = self.validate(request.get_json(force=True))
        except ValueError as e:
            return None, 400

        ret = {
            'lunch': {
                'date': dt,
                'votes': []
            }
        }

        lunches = [lunch for lunch in LUNCHES if lunch['date'] == dt]
        if len(lunches):
            ret['lunch'] = lunches[0]

        try:
            self.validateDuplicatedVote(vote, ret['lunch']['votes'])
        except AssertionError as e:
            return None, 400

        ret['lunch']['votes'].append(vote)
        Lunch.update(ret['lunch'])
        ret['lunch'] = marshal(ret['lunch'], resource_fields)

        return ret, 201
