from flask.ext.restful import Resource
from passlib.apps import custom_app_context as pwd_context

# local imports
from src.authentication import Token

__all__ = ['User', 'Users']

USERS = [
    {
        'name': 'Hungry employee',
        'username': 'hungryemployee',
        'password_hash': pwd_context.encrypt('iamhungry')
    }
]


class Users(Resource):
    # decorators = [auth.login_required]

    # @marshal_with(resource_fields, 'lunches')
    def get(self):
        return USERS


class User(Resource):

    @staticmethod
    def filter_by_username(username):
        l = filter(
                lambda u: u['username'] == username,
                USERS
                )
        return list(l)

    @staticmethod
    def filter_by_userpass(username, password):
        l = User.filter_by_username(username)
        if not l:
            return l

        return list(filter(
                lambda u: pwd_context.verify(password, u['password_hash']),
                l
                ))


    @staticmethod
    def filter_by_token(token):
        username = Token().verify_auth_token(token)
        if not username:
            return False

        return User.filter_by_username(username)

        self.password_hash = pwd_context.encrypt(password)
