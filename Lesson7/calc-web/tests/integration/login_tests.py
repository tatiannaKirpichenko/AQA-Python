import json
import unittest


from app import application
from app.services.AuthService import AuthService
from configuration import TestConfig


class LoginTests(unittest.TestCase):


    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.calculator = None

    def setUp(self) -> None:
        super().setUp()
        application.config.from_object(TestConfig)
        self.client = application.test_client()

        AuthService.tokens = {}

    def test_Login_ValidUser_LoginSuccessAndTokenReturned(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('success', response_data['status'])
        self.assertIsNotNone(response_data['data']['token'])

    def test_Login_InvalidUser_ReturnsError(self):
        login_data = {
            'userName': 'fake-user',
            'password': 'fake-password'
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('fail', response_data['status'])
        self.assertIn('message', response_data)

    def test_Login_EmptyFields_ReturnsError(self):
        login_data = {
            'userName': '',
            'password': ''
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('fail', response_data['status'])
        self.assertIn('message', response_data)

    def test_Login_TokenFormat(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        response_data = json.loads(response.get_data())
        token = response_data['data']['token']

        self.assertTrue(isinstance(token, str))
        self.assertGreater(len(token), 0)


    def test_AccessProtectedResource_WithoutToken(self):
        response = self.client.get('/protected-resource')
        self.assertEqual(404, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('error', response_data['status'])
        self.assertIn('message', response_data)


    def test_Login_InvalidJSON_ReturnsError(self):
        response = self.client.post('/login', data='invalid_json', content_type='application/json')
        self.assertEqual(400, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('fail', response_data['status'])


    def test_Login_ValidUserNameAndEmptyPassword_ReturnsError(self):
        login_data = {
            'userName': 'admin',
            'password': ''
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('fail', response_data['status'])
        self.assertIn('message', response_data)

    def test_Login_emptyUserNameAndValidPassword_ReturnsError(self):
        login_data = {
            'userName': '',
            'password': '123'
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('fail', response_data['status'])
        self.assertIn('message', response_data)

    def test_Login_validUserNameAndInvalidPassword_ReturnsError(self):
        login_data = {
            'userName': 'admin',
            'password': '1234'
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('fail', response_data['status'])
        self.assertIn('message', response_data)

    def test_Login_InvalidUserNameAndValidPassword_ReturnsError(self):
        login_data = {
            'userName': 'Ivan',
            'password': '123'
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('fail', response_data['status'])
        self.assertIn('message', response_data)


