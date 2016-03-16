from flask import g, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

from src import app, auth

__all__ = ['Token']


@app.route('/token')
@auth.login_required
def get_auth_token():
    token = Token().generate_auth_token(g.user['username'])
    return jsonify({'token': token.decode('ascii')})


class Token(object):

    def generate_auth_token(self, id, expiration=600):
        s = Serializer(g.get('SECRET_KEY', 'secret'), expires_in=expiration)
        return s.dumps({'id': id})

    def verify_auth_token(self, token):
        s = Serializer(g.get('SECRET_KEY', 'secret'))
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        return data['id']
