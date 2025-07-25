import uuid

from app.models.AuthResult import AuthResult
from app.models.User import User


class AuthService:
    tokens = {}

    users = [
        User('admin', '123'),
        User('john', 'qwerty')
    ]

    def __init__(self) -> None:
        super().__init__()


    def login(self, loginData):
        result = AuthResult()

        user_name = loginData['userName']

        users = list(filter(lambda u: u.userName == user_name, AuthService.users))

        if len(users) == 0:
            return result

        user = users[0]

        if user.password != loginData['password']:
            return result

        token = str(uuid.uuid4())

        AuthService.add_token(token, user_name)

        result.success = True
        result.token = token

        return result

    def verify_token(self, token):
        return AuthService.tokens.__contains__(token)

    @classmethod
    def get_user_name(cls, token):
        return AuthService.tokens[token]

    @classmethod
    def add_token(cls, token, user_name):
        AuthService.tokens[token] = user_name

    @classmethod
    def clear_tokens(cls):
        AuthService.tokens = {}

    @classmethod
    def clear_users(cls):
        AuthService.users = []

    @classmethod
    def add_user(cls, user_name, password):
        AuthService.users.append(User(user_name, password))
