import json
import unittest

from app import application
from app.services.AuthService import AuthService
from configuration import TestConfig


class LoginTests(unittest.TestCase):

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

