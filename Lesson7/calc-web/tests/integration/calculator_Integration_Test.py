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

    def test_calculator_addition(self):

        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        self.assertEqual('success', login_response_data['status'])
        self.assertIsNotNone(login_response_data['data']['token'])

        calculation_data = {
            'first_operand': 5,
            'operation': '+',
            'second_operand': 3
        }
        response = self.client.post('/calc', data=json.dumps(calculation_data), content_type='application/json')
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.get_data())
        self.assertEqual('success', response_data['status'])
        self.assertEqual(8, response_data['data']['result'])